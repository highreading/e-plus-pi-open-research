#!/usr/bin/env python3
"""Exact finite grid for nondecomposable root-of-unity exterior sums.

For a reduced endpoint lattice of rank nu this script constructs the exact
linear corrected map on its second exterior power, kills every coefficient
above a fixed target degree, saturates the integer kernel by a transformed
Hermite normal form, and selects a short nondecomposable vector from a
bounded search in an LLL-reduced kernel basis.

All ranks, kernels, coefficient vectors, contents, and origin orders are
exact.  Decimal endpoint values and logarithmic margins are diagnostics
only and are never used in an assertion.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import resource
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import __version__ as flint_version
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_nondecomposable_exterior_sum_certificate.json"
X = sp.symbols("X")
TARGET_DEGREE = 2
RSS_LIMIT_KIB = 2 * 1024 * 1024


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def polynomial_coefficients(expression: sp.Expr) -> list[sp.Rational]:
    polynomial = sp.Poly(sp.expand(expression), X, domain=sp.QQ)
    if polynomial.is_zero:
        return [sp.Rational(0)]
    return [polynomial.nth(k) for k in range(polynomial.degree() + 1)]


def functional(
    coefficients: list[sp.Rational], moments: list[sp.Rational]
) -> sp.Rational:
    return sum(
        coefficient * moments[k]
        for k, coefficient in enumerate(coefficients)
    )


def universal_Q(m: int, n: int) -> int:
    M = m * (n + 1)
    vandermonde = math.prod(math.factorial(a) for a in range(n + 1)) ** m
    vandermonde *= math.prod(
        h ** ((m - h) * (n + 1) ** 2) for h in range(1, m)
    )
    return 2**M * vandermonde


def interpolation_data(
    m: int,
    n: int,
    D_max: int,
    moments: list[sp.Rational],
) -> tuple[sp.Matrix, sp.Matrix, list[tuple[int, int]]]:
    """Return C -> T_C, C -> beta_C, and interpolation row labels."""
    M = m * (n + 1)
    labels = [(frequency, degree) for frequency in range(m) for degree in range(n + 1)]
    jet = sp.Matrix(
        [
            [
                sp.factorial(k) / sp.factorial(k - degree)
                * frequency ** (k - degree)
                if degree <= k
                else 0
                for frequency, degree in labels
            ]
            for k in range(M)
        ]
    )
    target = sp.Matrix(
        [
            [
                -sp.factorial(k) / sp.factorial(k - a) * moments[k - a]
                if a <= k
                else 0
                for a in range(D_max + 1)
            ]
            for k in range(M)
        ]
    )
    assert jet.det() != 0
    interpolation = jet.inv() * target
    beta = sp.zeros(n + 1, D_max + 1)
    for row, (frequency, degree) in enumerate(labels):
        beta[degree, :] += (-1) ** frequency * interpolation[row, :]
    return interpolation, beta, labels


def endpoint_matrix(
    m: int,
    n: int,
    D: int,
    nu: int,
    moments: list[sp.Rational],
) -> sp.Matrix:
    row_count = D + 1 - nu
    if row_count == 0:
        return sp.zeros(0, D + 1)
    phi = sp.prod((X - j) ** (n + 1) for j in range(m))
    return sp.Matrix(
        [
            [
                functional(
                    polynomial_coefficients(sp.diff(X**q * phi, X, a)),
                    moments,
                )
                for a in range(D + 1)
            ]
            for q in range(row_count)
        ]
    )


def primitive_integer_rows(matrix: sp.Matrix) -> sp.Matrix:
    """Clear and primitive-normalize each nonzero rational row."""
    rows: list[list[int]] = []
    for i in range(matrix.rows):
        values = [sp.Rational(value) for value in matrix.row(i)]
        denominator = math.lcm(*(int(sp.denom(value)) for value in values))
        row = [int(value * denominator) for value in values]
        content = math.gcd(*(abs(value) for value in row))
        assert content > 0
        row = [value // content for value in row]
        first = next(value for value in row if value)
        if first < 0:
            row = [-value for value in row]
        rows.append(row)
    return sp.Matrix(rows) if rows else sp.zeros(0, matrix.cols)


def to_flint(matrix: sp.Matrix) -> fmpz_mat:
    return fmpz_mat(
        [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]
    )


def from_flint(matrix: fmpz_mat) -> sp.Matrix:
    return sp.Matrix(
        [[int(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]
    )


def exact_rank(matrix: sp.Matrix) -> int:
    return int(to_flint(matrix).rank())


def saturated_integer_kernel(matrix: sp.Matrix) -> tuple[sp.Matrix, dict]:
    """Return an LLL-reduced column basis of ker(matrix) cap Z^columns.

    If H = U matrix^T is a row Hermite normal form with U unimodular,
    the rows of U corresponding to zero rows of H are a saturated kernel
    basis.  LLL applies a second unimodular row transformation.
    """
    if matrix.rows == 0:
        basis_rows = fmpz_mat(matrix.cols, matrix.cols, [int(i == j) for i in range(matrix.cols) for j in range(matrix.cols)])
        reduced = basis_rows
        zero_row_count = matrix.cols
        transform_verified = True
    else:
        integer_matrix = to_flint(matrix)
        hermite, transform = integer_matrix.transpose().hnf(transform=True)
        assert hermite == transform * integer_matrix.transpose()
        assert abs(int(transform.det())) == 1
        zero_rows = [
            i
            for i in range(hermite.nrows())
            if all(hermite[i, j] == 0 for j in range(hermite.ncols()))
        ]
        basis_rows = fmpz_mat(
            [[transform[i, j] for j in range(transform.ncols())] for i in zero_rows]
        )
        assert basis_rows * integer_matrix.transpose() == fmpz_mat(
            basis_rows.nrows(), integer_matrix.nrows()
        )
        reduced, lll_transform = basis_rows.lll(transform=True)
        assert reduced == lll_transform * basis_rows
        assert abs(int(lll_transform.det())) == 1
        assert reduced * integer_matrix.transpose() == fmpz_mat(
            reduced.nrows(), integer_matrix.nrows()
        )
        zero_row_count = len(zero_rows)
        transform_verified = True

    reduced_sympy_rows = from_flint(reduced)
    basis = reduced_sympy_rows.T
    assert matrix * basis == sp.zeros(matrix.rows, basis.cols)
    assert basis.cols == matrix.cols - exact_rank(matrix)
    height = max((abs(int(value)) for value in basis), default=1)
    return basis, {
        "kernel_dimension": basis.cols,
        "hnf_zero_row_count": zero_row_count,
        "hnf_and_lll_transformations_verified": transform_verified,
        "lll_basis_height": str(height),
        "lll_basis_height_decimal_digits": len(str(height)),
    }


def exterior_embedding(
    basis: sp.Matrix,
) -> tuple[sp.Matrix, list[tuple[int, int]], list[tuple[int, int]]]:
    ambient_pairs = list(itertools.combinations(range(basis.rows), 2))
    coordinate_pairs = list(itertools.combinations(range(basis.cols), 2))
    embedding = sp.zeros(len(ambient_pairs), len(coordinate_pairs))
    for column, (i, j) in enumerate(coordinate_pairs):
        for row, (a, b) in enumerate(ambient_pairs):
            embedding[row, column] = (
                basis[a, i] * basis[b, j] - basis[b, i] * basis[a, j]
            )
    return embedding, ambient_pairs, coordinate_pairs


def corrected_Q_map(beta: sp.Matrix, Q: int, n: int, D: int) -> sp.Matrix:
    E_Q = beta * Q
    assert all(sp.denom(value) == 1 for value in E_Q)
    pairs = list(itertools.combinations(range(D + 1), 2))
    matrix = sp.zeros(n + D + 1, len(pairs))
    for column, (u, v) in enumerate(pairs):
        matrix[u + v - 1, column] += Q * (v - u)
        for b in range(n + 1):
            matrix[u + b, column] -= E_Q[b, v]
            matrix[v + b, column] += E_Q[b, u]
    assert all(sp.denom(value) == 1 for value in matrix)
    return matrix


def primitive_column(vector: sp.Matrix) -> sp.Matrix:
    values = [int(value) for value in vector]
    content = math.gcd(*(abs(value) for value in values))
    assert content > 0
    values = [value // content for value in values]
    first = next(value for value in values if value)
    if first < 0:
        values = [-value for value in values]
    assert math.gcd(*(abs(value) for value in values)) == 1
    return sp.Matrix(values)


def skew_rank(vector: sp.Matrix, nu: int, pairs: list[tuple[int, int]]) -> int:
    skew = sp.zeros(nu, nu)
    for value, (i, j) in zip(vector, pairs):
        skew[i, j] = value
        skew[j, i] = -value
    return int(skew.rank())


def select_short_candidate(
    kernel_basis: sp.Matrix,
    corrected_map: sp.Matrix,
    nu: int,
    coordinate_pairs: list[tuple[int, int]],
) -> tuple[sp.Matrix, dict]:
    """Bounded {-1,0,1} search in an LLL-reduced saturated basis."""
    dimension = kernel_basis.cols
    assert 1 <= dimension <= 10
    seen: set[tuple[int, ...]] = set()
    candidates: list[tuple[bool, int, int, tuple[int, ...], sp.Matrix, int]] = []
    tested = 0
    for coefficients in itertools.product((-1, 0, 1), repeat=dimension):
        if not any(coefficients):
            continue
        first_coefficient = next(value for value in coefficients if value)
        if first_coefficient < 0:
            continue
        vector = kernel_basis * sp.Matrix(coefficients)
        vector = primitive_column(vector)
        key = tuple(int(value) for value in vector)
        if key in seen:
            continue
        seen.add(key)
        tested += 1
        image = corrected_map * vector
        if not any(image):
            continue
        rank = skew_rank(vector, nu, coordinate_pairs)
        norm_squared = sum(int(value) ** 2 for value in vector)
        height = max(abs(int(value)) for value in vector)
        candidates.append((rank >= 4, norm_squared, height, key, vector, rank))
    assert candidates
    nondecomposable = [candidate for candidate in candidates if candidate[0]]
    pool = nondecomposable if nondecomposable else candidates
    chosen = min(pool, key=lambda item: (item[1], item[2], item[3]))
    _, norm_squared, height, _, vector, rank = chosen
    return vector, {
        "bounded_search_coefficient_box": [-1, 0, 1],
        "bounded_search_unique_primitive_vectors_tested": tested,
        "bounded_search_nonzero_low_image_count": len(candidates),
        "bounded_search_nondecomposable_count": len(nondecomposable),
        "selected_nondecomposable_when_found": bool(nondecomposable),
        "selected_coordinate_skew_rank": rank,
        "selected_coordinate_height": str(height),
        "selected_coordinate_height_decimal_digits": len(str(height)),
        "selected_coordinate_squared_norm": str(norm_squared),
    }


def zero_array(frequencies: int, degree: int) -> list[list[int]]:
    return [[0] * (degree + 1) for _ in range(frequencies)]


def cleared_remainders(
    m: int,
    n: int,
    D: int,
    Q: int,
    interpolation: sp.Matrix,
    labels: list[tuple[int, int]],
    endpoint_basis: sp.Matrix,
) -> list[list[list[int]]]:
    auxiliary = interpolation[:, : D + 1] * endpoint_basis * Q
    assert all(sp.denom(value) == 1 for value in auxiliary)
    remainders: list[list[list[int]]] = []
    for column in range(endpoint_basis.cols):
        coefficients = zero_array(m + 1, n)
        for a in range(D + 1):
            coefficients[0][a] += Q * int(endpoint_basis[a, column])
        for row, (frequency, degree) in enumerate(labels):
            value = int(auxiliary[row, column])
            coefficients[frequency][degree] += value
            coefficients[frequency + 1][degree] += value
        remainders.append(coefficients)
    return remainders


def exp_derivative(form: list[list[int]]) -> list[list[int]]:
    frequencies = len(form)
    degree = len(form[0]) - 1
    derivative = zero_array(frequencies, degree)
    for frequency in range(frequencies):
        for a in range(degree + 1):
            derivative[frequency][a] += frequency * form[frequency][a]
            if a < degree:
                derivative[frequency][a] += (a + 1) * form[frequency][a + 1]
    return derivative


def exp_product(
    first: list[list[int]], second: list[list[int]]
) -> list[list[int]]:
    degree_first = len(first[0]) - 1
    degree_second = len(second[0]) - 1
    product = zero_array(len(first) + len(second) - 1, degree_first + degree_second)
    for f, polynomial_first in enumerate(first):
        for g, polynomial_second in enumerate(second):
            for a, value_first in enumerate(polynomial_first):
                if not value_first:
                    continue
                for b, value_second in enumerate(polynomial_second):
                    if value_second:
                        product[f + g][a + b] += value_first * value_second
    return product


def exp_wronskian(
    first: list[list[int]], second: list[list[int]]
) -> list[list[int]]:
    first_second = exp_product(first, exp_derivative(second))
    second_first = exp_product(second, exp_derivative(first))
    return [
        [a - b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(first_second, second_first)
    ]


def exterior_wronskian_sum(
    remainders: list[list[list[int]]],
    vector: sp.Matrix,
    pairs: list[tuple[int, int]],
) -> list[list[int]]:
    result = zero_array(2 * (len(remainders[0]) - 1) + 1, 2 * (len(remainders[0][0]) - 1))
    for coefficient, (i, j) in zip(vector, pairs):
        coefficient = int(coefficient)
        if not coefficient:
            continue
        pair_wronskian = exp_wronskian(remainders[i], remainders[j])
        for frequency in range(len(result)):
            for degree in range(len(result[0])):
                result[frequency][degree] += coefficient * pair_wronskian[frequency][degree]
    return result


def exp_jet(form: list[list[int]], order: int) -> int:
    value = 0
    for frequency, polynomial in enumerate(form):
        for degree in range(min(order, len(polynomial) - 1) + 1):
            coefficient = polynomial[degree]
            if coefficient:
                value += (
                    coefficient
                    * math.factorial(order)
                    // math.factorial(order - degree)
                    * frequency ** (order - degree)
                )
    return value


def exact_origin_order(form: list[list[int]], lower_bound: int) -> int:
    dimension_bound = len(form) * len(form[0])
    for order in range(dimension_bound):
        value = exp_jet(form, order)
        if value:
            assert order >= lower_bound
            return order
    raise AssertionError("nonzero exponential polynomial exceeded zero-estimate dimension")


def endpoint_polynomial(form: list[list[int]]) -> list[int]:
    return [
        sum((-1) ** frequency * form[frequency][degree] for frequency in range(len(form)))
        for degree in range(len(form[0]))
    ]


def matrix_digest(matrix: sp.Matrix) -> str:
    digest = hashlib.sha256()
    digest.update(f"{matrix.rows},{matrix.cols}\n".encode())
    for value in matrix:
        digest.update(f"{int(value)}\n".encode())
    return digest.hexdigest()


def vector_digest(values: list[int] | sp.Matrix) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(f"{int(value)}\n".encode())
    return digest.hexdigest()


def polynomial_diagnostic(coefficients: list[int]) -> dict:
    height = max(abs(value) for value in coefficients)
    mp.mp.dps = max(100, 4 * len(str(height)) + 60)
    point = mp.j * mp.pi
    value = mp.fsum(
        mp.mpf(coefficient) * point**degree
        for degree, coefficient in enumerate(coefficients)
    )
    absolute = abs(value)
    exponent = None
    if height > 1 and absolute:
        exponent = -mp.log(absolute / height) / mp.log(height)
    return {
        "absolute_value_at_i_pi": mp.nstr(absolute, 50),
        "absolute_value_below_one": bool(absolute < 1),
        "relative_value_over_height": mp.nstr(absolute / height, 50),
        "relative_small_value_exponent": None if exponent is None else mp.nstr(exponent, 40),
        "diagnostic_only": True,
    }


def minimal_nu(n: int, D: int, target_degree: int) -> int:
    tail_count = n + D - target_degree
    for nu in range(2, D + 2):
        if math.comb(nu, 2) > tail_count:
            return nu
    raise AssertionError("no exterior dimension beats the tail count")


def minimal_full_endpoint_D(n: int, target_degree: int) -> int:
    for D in range(1, n + 1):
        if math.comb(D + 1, 2) > n + D - target_degree:
            return D
    raise AssertionError("no full endpoint degree found")


def full_endpoint_parity_rank_row(
    m: int,
    n: int,
    D: int,
    beta_max: sp.Matrix,
    Q: int,
    require_parity_maximal: bool = True,
) -> dict:
    """Compute the parity-block ranks for E=Q[z]_{<=D}."""
    corrected = corrected_Q_map(beta_max[:, : D + 1], Q, n, D)
    pairs = list(itertools.combinations(range(D + 1), 2))
    output_top_degree = n + D
    off_parity_zero = all(
        corrected[row, column] == 0
        for column, (a, b) in enumerate(pairs)
        for row in range(output_top_degree + 1)
        if row % 2 != (a + b - 1) % 2
    )
    assert off_parity_zero

    even_endpoint_dimension = D // 2 + 1
    odd_endpoint_dimension = (D + 1) // 2
    even_output_domain = even_endpoint_dimension * odd_endpoint_dimension
    odd_output_domain = (
        math.comb(even_endpoint_dimension, 2)
        + math.comb(odd_endpoint_dimension, 2)
    )
    even_output_coordinates = output_top_degree // 2 + 1
    odd_output_coordinates = (output_top_degree + 1) // 2
    tail_even_coordinates = sum(
        degree % 2 == 0
        for degree in range(TARGET_DEGREE + 1, output_top_degree + 1)
    )
    tail_odd_coordinates = sum(
        degree % 2 == 1
        for degree in range(TARGET_DEGREE + 1, output_top_degree + 1)
    )
    predicted_full_rank = min(even_output_domain, even_output_coordinates) + min(
        odd_output_domain, odd_output_coordinates
    )
    predicted_tail_rank = min(even_output_domain, tail_even_coordinates) + min(
        odd_output_domain, tail_odd_coordinates
    )
    even_rows = [degree for degree in range(output_top_degree + 1) if degree % 2 == 0]
    odd_rows = [degree for degree in range(output_top_degree + 1) if degree % 2 == 1]
    tail_even_rows = [degree for degree in even_rows if degree > TARGET_DEGREE]
    tail_odd_rows = [degree for degree in odd_rows if degree > TARGET_DEGREE]
    even_columns = [
        column
        for column, (a, b) in enumerate(pairs)
        if (a + b - 1) % 2 == 0
    ]
    odd_columns = [
        column
        for column, (a, b) in enumerate(pairs)
        if (a + b - 1) % 2 == 1
    ]
    actual_full_even_block_rank = exact_rank(
        corrected.extract(even_rows, even_columns)
    )
    actual_full_odd_block_rank = exact_rank(
        corrected.extract(odd_rows, odd_columns)
    )
    actual_tail_even_block_rank = exact_rank(
        corrected.extract(tail_even_rows, even_columns)
    )
    actual_tail_odd_block_rank = exact_rank(
        corrected.extract(tail_odd_rows, odd_columns)
    )
    actual_full_rank = exact_rank(corrected)
    actual_tail_rank = exact_rank(corrected[TARGET_DEGREE + 1 :, :])
    assert actual_full_rank == actual_full_even_block_rank + actual_full_odd_block_rank
    assert actual_tail_rank == actual_tail_even_block_rank + actual_tail_odd_block_rank
    if require_parity_maximal:
        assert actual_full_rank == predicted_full_rank
        assert actual_tail_rank == predicted_tail_rank
    return {
        "m": m,
        "n": n,
        "D": D,
        "even_endpoint_dimension": even_endpoint_dimension,
        "odd_endpoint_dimension": odd_endpoint_dimension,
        "even_output_wedge_domain_dimension": even_output_domain,
        "odd_output_wedge_domain_dimension": odd_output_domain,
        "even_output_coordinate_count": even_output_coordinates,
        "odd_output_coordinate_count": odd_output_coordinates,
        "tail_even_coordinate_count": tail_even_coordinates,
        "tail_odd_coordinate_count": tail_odd_coordinates,
        "off_parity_blocks_are_exactly_zero": True,
        "actual_full_even_block_rank": actual_full_even_block_rank,
        "actual_full_odd_block_rank": actual_full_odd_block_rank,
        "actual_full_rank": actual_full_rank,
        "predicted_parity_maximal_full_rank": predicted_full_rank,
        "full_rank_is_parity_maximal": actual_full_rank == predicted_full_rank,
        "actual_tail_even_block_rank": actual_tail_even_block_rank,
        "actual_tail_odd_block_rank": actual_tail_odd_block_rank,
        "actual_tail_rank": actual_tail_rank,
        "predicted_parity_maximal_tail_rank": predicted_tail_rank,
        "tail_rank_is_parity_maximal": actual_tail_rank == predicted_tail_rank,
        "rank_gap": actual_full_rank - actual_tail_rank,
    }


def exact_row(
    m: int,
    n: int,
    D: int,
    nu: int,
    family: str,
    moments: list[sp.Rational],
    interpolation: sp.Matrix,
    beta_max: sp.Matrix,
    labels: list[tuple[int, int]],
) -> dict:
    target_degree = TARGET_DEGREE
    M = m * (n + 1)
    L_nu = M + D + 1 - nu
    tail_count = n + D - target_degree
    exterior_dimension = math.comb(nu, 2)
    assert exterior_dimension > tail_count

    rational_endpoint_matrix = endpoint_matrix(m, n, D, nu, moments)
    integer_endpoint_matrix = primitive_integer_rows(rational_endpoint_matrix)
    endpoint_rank = exact_rank(integer_endpoint_matrix)
    assert endpoint_rank == D + 1 - nu
    endpoint_basis, endpoint_kernel_audit = saturated_integer_kernel(integer_endpoint_matrix)
    assert endpoint_basis.shape == (D + 1, nu)

    exterior, ambient_pairs, coordinate_pairs = exterior_embedding(endpoint_basis)
    exterior_height = max(abs(int(value)) for value in exterior)
    assert exact_rank(exterior) == exterior_dimension

    Q = universal_Q(m, n)
    beta = beta_max[:, : D + 1]
    ambient_map = corrected_Q_map(beta, Q, n, D)
    restricted_map = ambient_map * exterior
    full_rank = exact_rank(restricted_map)
    tail_map = restricted_map[target_degree + 1 :, :]
    tail_rank = exact_rank(tail_map)
    rank_gap = full_rank - tail_rank
    primitive_tail_rows = primitive_integer_rows(tail_map)
    tail_kernel, tail_kernel_audit = saturated_integer_kernel(primitive_tail_rows)
    assert tail_kernel.shape == (exterior_dimension, exterior_dimension - tail_rank)

    endpoint_basis_digest = matrix_digest(endpoint_basis)
    if rank_gap == 0:
        # Since the full map contains the tail rows, equality of ranks means
        # equality of kernels.  Verify this directly on a saturated basis.
        assert restricted_map * tail_kernel == sp.zeros(
            restricted_map.rows, tail_kernel.cols
        )
        digest = hashlib.sha256(
            (
                f"{m},{n},{D},{nu},{family},rank-gap-zero\n"
                + endpoint_basis_digest
                + matrix_digest(tail_kernel)
            ).encode()
        ).hexdigest()
        return {
            "family": family,
            "m": m,
            "n": n,
            "D": D,
            "nu": nu,
            "M": M,
            "target_degree": target_degree,
            "L_nu": L_nu,
            "proved_origin_order_lower_bound_2L_nu": 2 * L_nu,
            "endpoint_constraint_count": D + 1 - nu,
            "endpoint_rank": endpoint_rank,
            "endpoint_rank_is_full": True,
            "endpoint_basis_is_saturated_hnf_kernel": True,
            "endpoint_basis_height": str(max(abs(int(value)) for value in endpoint_basis)),
            "endpoint_basis_height_decimal_digits": len(
                str(max(abs(int(value)) for value in endpoint_basis))
            ),
            "endpoint_basis_digest_sha256": endpoint_basis_digest,
            "endpoint_kernel_audit": endpoint_kernel_audit,
            "exterior_dimension_N": exterior_dimension,
            "high_coefficient_count_S": tail_count,
            "N_strictly_exceeds_S": True,
            "exterior_embedding_height": str(exterior_height),
            "exterior_embedding_height_decimal_digits": len(str(exterior_height)),
            "corrected_full_rank": full_rank,
            "corrected_tail_rank": tail_rank,
            "rank_gap_low_image_dimension": 0,
            "rank_gap_nonzero": False,
            "full_kernel_dimension": exterior_dimension - full_rank,
            "tail_kernel_dimension": exterior_dimension - tail_rank,
            "tail_kernel_equals_full_kernel_verified": True,
            "tail_kernel_is_saturated_hnf_kernel": True,
            "tail_kernel_audit": tail_kernel_audit,
            "usable_nonzero_low_degree_endpoint": False,
            "obstruction": (
                "Every exterior vector killing degrees above the target also "
                "kills the full corrected polynomial on this exact row."
            ),
            "finite_row_digest_sha256": digest,
        }

    assert rank_gap > 0
    coordinate_vector, search_audit = select_short_candidate(
        tail_kernel, restricted_map, nu, coordinate_pairs
    )
    assert primitive_tail_rows * coordinate_vector == sp.zeros(primitive_tail_rows.rows, 1)
    assert math.gcd(*(abs(int(value)) for value in coordinate_vector)) == 1

    ambient_exterior_vector = exterior * coordinate_vector
    assert math.gcd(*(abs(int(value)) for value in ambient_exterior_vector)) == 1
    N_Q_vector = restricted_map * coordinate_vector
    assert any(N_Q_vector)
    assert all(N_Q_vector[index] == 0 for index in range(target_degree + 1, N_Q_vector.rows))
    corrected_content = math.gcd(*(abs(int(value)) for value in N_Q_vector))
    primitive_delta = [int(value) // corrected_content for value in N_Q_vector]
    first = next(value for value in primitive_delta if value)
    if first < 0:
        coordinate_vector = -coordinate_vector
        ambient_exterior_vector = -ambient_exterior_vector
        N_Q_vector = -N_Q_vector
        primitive_delta = [-value for value in primitive_delta]
    actual_degree = max(index for index, value in enumerate(primitive_delta) if value)
    primitive_delta = primitive_delta[: actual_degree + 1]
    assert actual_degree <= target_degree
    primitive_height = max(abs(value) for value in primitive_delta)
    assert math.gcd(*(abs(value) for value in primitive_delta)) == 1

    remainders = cleared_remainders(
        m, n, D, Q, interpolation, labels, endpoint_basis
    )
    remainder_height = max(
        abs(value) for remainder in remainders for row in remainder for value in row
    )
    for remainder in remainders:
        assert all(exp_jet(remainder, order) == 0 for order in range(L_nu))

    wronskian_sum = exterior_wronskian_sum(
        remainders, coordinate_vector, coordinate_pairs
    )
    endpoint_from_wronskian = endpoint_polynomial(wronskian_sum)
    expected_endpoint = [Q * int(value) for value in N_Q_vector]
    expected_endpoint += [0] * (len(endpoint_from_wronskian) - len(expected_endpoint))
    assert endpoint_from_wronskian == expected_endpoint
    origin_order = exact_origin_order(wronskian_sum, 2 * L_nu)
    wronskian_height = max(
        abs(value) for row in wronskian_sum for value in row
    )
    normalized_analytic_height = sp.Rational(
        wronskian_height, Q * corrected_content
    )

    A_nu = max(abs(int(value)) for value in endpoint_basis)
    B0 = max(1, (M - 1) ** n * max(1, m - 1) ** (M - 1))
    C_B = 2 ** (M - 1) * (D + 1) * math.factorial(M) * math.factorial(M - 1) * B0 ** (M - 1)
    B_delta = A_nu**2 * (2 * D**2 * Q + 2 * m * (D + 1) * C_B)
    B_wronskian_pair = (
        2
        * (m + 1)
        * (n + 1)
        * (n + m)
        * A_nu**2
        * (Q + 2 * C_B) ** 2
    )
    selected_coordinate_height = int(search_audit["selected_coordinate_height"])
    assert max(abs(int(value)) for value in restricted_map) <= B_delta
    assert remainder_height <= A_nu * (Q + 2 * C_B)
    assert wronskian_height <= (
        exterior_dimension * selected_coordinate_height * B_wronskian_pair
    )
    siegel_log_bound = (
        sp.Rational(tail_count, exterior_dimension - tail_count)
        * mp.log(2 * exterior_dimension * B_delta + 1)
        + mp.log(2)
    )

    mp.mp.dps = 100
    # Multiplication by exp(-m z) centers the Wronskian frequencies
    # 0,...,2m at -m,...,m without changing its zero order, coefficient
    # height, or endpoint absolute value.  The circle factor is therefore
    # exp(m rho), and the optimized radius doubles.
    stationary_radius = sp.Rational(2 * (L_nu - n), m)
    stationary_admissible = mp.mpf(stationary_radius.p) / stationary_radius.q > mp.pi
    uncentered_gain = (
        mp.mpf(L_nu - n)
        * mp.log(mp.mpf(L_nu - n) / (mp.e * mp.pi * m))
        - n * mp.log(mp.pi)
    )
    centered_gain = uncentered_gain + (L_nu - n) * mp.log(2)
    log_normalized_analytic_height = mp.log(int(sp.numer(normalized_analytic_height))) - mp.log(int(sp.denom(normalized_analytic_height)))
    log_primitive_height = mp.log(primitive_height) if primitive_height else mp.ninf
    schwarz_minus_log_lower = (
        2 * centered_gain
        - mp.log((2 * m + 1) * (2 * n + 1))
        - log_normalized_analytic_height
    )
    r_one_measure_margin = schwarz_minus_log_lower - actual_degree * log_primitive_height

    coordinate_digest = vector_digest(coordinate_vector)
    ambient_exterior_digest = vector_digest(ambient_exterior_vector)
    primitive_delta_digest = vector_digest(primitive_delta)
    digest = hashlib.sha256(
        (
            f"{m},{n},{D},{nu},{family}\n"
            + endpoint_basis_digest
            + coordinate_digest
            + ambient_exterior_digest
            + primitive_delta_digest
        ).encode()
    ).hexdigest()

    row = {
        "family": family,
        "m": m,
        "n": n,
        "D": D,
        "nu": nu,
        "M": M,
        "target_degree": target_degree,
        "L_nu": L_nu,
        "proved_origin_order_lower_bound_2L_nu": 2 * L_nu,
        "selected_sum_exact_origin_order": origin_order,
        "endpoint_constraint_count": D + 1 - nu,
        "endpoint_rank": endpoint_rank,
        "endpoint_rank_is_full": True,
        "endpoint_basis_is_saturated_hnf_kernel": True,
        "endpoint_basis_height": str(A_nu),
        "endpoint_basis_height_decimal_digits": len(str(A_nu)),
        "endpoint_basis_digest_sha256": endpoint_basis_digest,
        "endpoint_kernel_audit": endpoint_kernel_audit,
        "exterior_dimension_N": exterior_dimension,
        "high_coefficient_count_S": tail_count,
        "N_strictly_exceeds_S": True,
        "exterior_embedding_height": str(exterior_height),
        "exterior_embedding_height_decimal_digits": len(str(exterior_height)),
        "corrected_full_rank": full_rank,
        "corrected_tail_rank": tail_rank,
        "rank_gap_low_image_dimension": rank_gap,
        "rank_gap_nonzero": True,
        "usable_nonzero_low_degree_endpoint": True,
        "full_kernel_dimension": exterior_dimension - full_rank,
        "tail_kernel_dimension": exterior_dimension - tail_rank,
        "tail_kernel_is_saturated_hnf_kernel": True,
        "tail_kernel_audit": tail_kernel_audit,
        "search_audit": search_audit,
        "selected_ambient_exterior_height": str(max(abs(int(value)) for value in ambient_exterior_vector)),
        "selected_ambient_exterior_height_decimal_digits": len(str(max(abs(int(value)) for value in ambient_exterior_vector))),
        "selected_ambient_exterior_gcd_one": True,
        "selected_coordinate_digest_sha256": coordinate_digest,
        "selected_ambient_exterior_digest_sha256": ambient_exterior_digest,
        "selected_is_genuinely_nondecomposable": search_audit["selected_coordinate_skew_rank"] >= 4,
        "Q_decimal_digits": len(str(Q)),
        "Q_delta_content": str(corrected_content),
        "Q_delta_content_decimal_digits": len(str(corrected_content)),
        "primitive_delta_actual_degree": actual_degree,
        "primitive_delta_coefficients_ascending": [str(value) for value in primitive_delta],
        "primitive_delta_height": str(primitive_height),
        "primitive_delta_height_decimal_digits": len(str(primitive_height)),
        "primitive_delta_digest_sha256": primitive_delta_digest,
        "cleared_remainder_basis_height": str(remainder_height),
        "cleared_remainder_basis_height_decimal_digits": len(str(remainder_height)),
        "cleared_exterior_wronskian_height": str(wronskian_height),
        "cleared_exterior_wronskian_height_decimal_digits": len(str(wronskian_height)),
        "normalized_analytic_height_numerator": str(sp.numer(normalized_analytic_height)),
        "normalized_analytic_height_denominator": str(sp.denom(normalized_analytic_height)),
        "normalized_analytic_height_log": mp.nstr(log_normalized_analytic_height, 40),
        "universal_B_delta_log": mp.nstr(mp.log(B_delta), 40),
        "universal_pair_wronskian_bound_log": mp.nstr(
            mp.log(B_wronskian_pair), 40
        ),
        "universal_selected_sum_wronskian_bound_log": mp.nstr(
            mp.log(
                exterior_dimension
                * selected_coordinate_height
                * B_wronskian_pair
            ),
            40,
        ),
        "all_universal_coefficient_bounds_verified": True,
        "elementary_siegel_coordinate_log_bound": mp.nstr(siegel_log_bound, 40),
        "actual_selected_coordinate_log_height": mp.nstr(mp.log(int(search_audit["selected_coordinate_height"])), 40),
        "frequency_centering_by_exp_minus_mz_used": True,
        "centered_stationary_radius_2A_over_m": str(stationary_radius),
        "centered_stationary_radius_admissible": bool(stationary_admissible),
        "uncentered_optimized_gain_G_nu": mp.nstr(uncentered_gain, 40),
        "centered_optimized_gain_G_nu": mp.nstr(centered_gain, 40),
        "one_gain_frequency_centering_improvement_A_log_2": mp.nstr(
            (L_nu - n) * mp.log(2), 40
        ),
        "schwarz_certified_minus_log_value_lower_bound": mp.nstr(schwarz_minus_log_lower, 40),
        "leading_r_equals_one_measure_margin": mp.nstr(r_one_measure_margin, 40),
        "finite_row_digest_sha256": digest,
    }
    row.update(polynomial_diagnostic(primitive_delta))
    return row


def main() -> None:
    diagonal_rows: list[dict] = []
    diagonal_rescue_rows: list[dict] = []
    full_endpoint_rows: list[dict] = []
    full_endpoint_parity_rank_rows: list[dict] = []
    grid_digest = hashlib.sha256()

    for m in (2, 3):
        for n in range(2, 13):
            moments = logistic_moments(m * (n + 1) + n + 8)
            interpolation, beta_max, labels = interpolation_data(m, n, n, moments)
            Q = universal_Q(m, n)
            for parity_D in range(1, n + 1):
                parity_row = full_endpoint_parity_rank_row(
                    m, n, parity_D, beta_max, Q
                )
                full_endpoint_parity_rank_rows.append(parity_row)
                grid_digest.update(
                    (
                        f"parity,{m},{n},{parity_D},"
                        f"{parity_row['actual_full_rank']},"
                        f"{parity_row['actual_tail_rank']}\n"
                    ).encode()
                )

            diagonal_D = n
            diagonal_nu = minimal_nu(n, diagonal_D, TARGET_DEGREE)
            diagonal = exact_row(
                m,
                n,
                diagonal_D,
                diagonal_nu,
                "diagonal_D_equals_n",
                moments,
                interpolation,
                beta_max,
                labels,
            )
            diagonal_rows.append(diagonal)
            grid_digest.update((diagonal["finite_row_digest_sha256"] + "\n").encode())
            if not diagonal["rank_gap_nonzero"]:
                rescue_nu = diagonal_nu + 1
                assert rescue_nu <= diagonal_D + 1
                rescue = exact_row(
                    m,
                    n,
                    diagonal_D,
                    rescue_nu,
                    "diagonal_first_rank_gap_rescue",
                    moments,
                    interpolation,
                    beta_max,
                    labels,
                )
                assert rescue["rank_gap_nonzero"]
                diagonal_rescue_rows.append(rescue)
                grid_digest.update((rescue["finite_row_digest_sha256"] + "\n").encode())

            full_D = minimal_full_endpoint_D(n, TARGET_DEGREE)
            full_nu = full_D + 1
            full_endpoint = exact_row(
                m,
                n,
                full_D,
                full_nu,
                "minimal_full_endpoint_space",
                moments,
                interpolation,
                beta_max,
                labels,
            )
            full_endpoint_rows.append(full_endpoint)
            grid_digest.update((full_endpoint["finite_row_digest_sha256"] + "\n").encode())

    # A strategically chosen exact tuple outside the small grid disproves
    # any unrestricted extrapolation of parity-maximality.  It does not
    # destroy the low-degree rank gap.
    counterexample_m, counterexample_n, counterexample_D = 2, 21, 7
    counterexample_moments = logistic_moments(
        counterexample_m * (counterexample_n + 1) + counterexample_n + 8
    )
    _, counterexample_beta, _ = interpolation_data(
        counterexample_m,
        counterexample_n,
        counterexample_D,
        counterexample_moments,
    )
    parity_maximality_counterexample = full_endpoint_parity_rank_row(
        counterexample_m,
        counterexample_n,
        counterexample_D,
        counterexample_beta,
        universal_Q(counterexample_m, counterexample_n),
        require_parity_maximal=False,
    )
    assert parity_maximality_counterexample["actual_full_rank"] == 26
    assert parity_maximality_counterexample["predicted_parity_maximal_full_rank"] == 27
    assert parity_maximality_counterexample["actual_tail_rank"] == 23
    assert parity_maximality_counterexample["predicted_parity_maximal_tail_rank"] == 25
    assert parity_maximality_counterexample["rank_gap"] == 3
    grid_digest.update(
        (
            "parity-counterexample,2,21,7,26,23\n"
        ).encode()
    )

    usable_diagonal_rows = [row for row in diagonal_rows if row["rank_gap_nonzero"]]
    all_usable_rows = usable_diagonal_rows + diagonal_rescue_rows + full_endpoint_rows
    all_rows = diagonal_rows + diagonal_rescue_rows + full_endpoint_rows
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    payload = {
        "schema": "root-unity-nondecomposable-exterior-sum-certificate-v1",
        "target_degree": TARGET_DEGREE,
        "diagonal_grid": {
            "m_values": [2, 3],
            "n_equals_D_values": list(range(2, 13)),
            "row_count": len(diagonal_rows),
            "all_endpoint_ranks_full": all(row["endpoint_rank_is_full"] for row in diagonal_rows),
            "rank_gap_zero_row_count": sum(not row["rank_gap_nonzero"] for row in diagonal_rows),
            "all_selected_degrees_at_most_target_on_usable_rows": all(row["primitive_delta_actual_degree"] <= TARGET_DEGREE for row in usable_diagonal_rows),
            "all_selected_sums_nondecomposable_from_n_at_least_3": all(
                row["selected_is_genuinely_nondecomposable"]
                for row in usable_diagonal_rows
                if row["n"] >= 3
            ),
            "rows": diagonal_rows,
            "first_rank_gap_rescue_rows": diagonal_rescue_rows,
        },
        "minimal_full_endpoint_grid": {
            "m_values": [2, 3],
            "n_values": list(range(2, 13)),
            "row_count": len(full_endpoint_rows),
            "all_endpoint_constraint_counts_zero": all(row["endpoint_constraint_count"] == 0 for row in full_endpoint_rows),
            "all_endpoint_basis_heights_one": all(row["endpoint_basis_height"] == "1" for row in full_endpoint_rows),
            "all_rank_gaps_nonzero": all(row["rank_gap_nonzero"] for row in full_endpoint_rows),
            "all_selected_degrees_at_most_target": all(row["primitive_delta_actual_degree"] <= TARGET_DEGREE for row in full_endpoint_rows),
            "rows": full_endpoint_rows,
        },
        "full_endpoint_parity_rank_grid": {
            "m_values": [2, 3],
            "n_values": list(range(2, 13)),
            "D_rule": "every integer 1 <= D <= n",
            "target_degree": TARGET_DEGREE,
            "row_count": len(full_endpoint_parity_rank_rows),
            "all_off_parity_blocks_exactly_zero": all(
                row["off_parity_blocks_are_exactly_zero"]
                for row in full_endpoint_parity_rank_rows
            ),
            "all_full_ranks_parity_maximal": all(
                row["actual_full_rank"]
                == row["predicted_parity_maximal_full_rank"]
                for row in full_endpoint_parity_rank_rows
            ),
            "all_tail_ranks_parity_maximal": all(
                row["actual_tail_rank"]
                == row["predicted_parity_maximal_tail_rank"]
                for row in full_endpoint_parity_rank_rows
            ),
            "no_extrapolation": True,
            "rows": full_endpoint_parity_rank_rows,
        },
        "full_endpoint_parity_maximality_counterexample": {
            "exact_counterexample_to_unrestricted_parity_maximality": True,
            "rank_gap_remains_nonzero": True,
            "row": parity_maximality_counterexample,
        },
        "combined_grid_digest_sha256": grid_digest.hexdigest(),
        "finite_grid_summary": {
            "row_count": len(all_rows),
            "rank_gap_values": sorted(set(row["rank_gap_low_image_dimension"] for row in all_rows)),
            "rank_gap_zero_rows": [
                [row["m"], row["n"], row["D"], row["nu"], row["target_degree"]]
                for row in all_rows
                if not row["rank_gap_nonzero"]
            ],
            "actual_degree_values_on_usable_rows": sorted(set(row["primitive_delta_actual_degree"] for row in all_usable_rows)),
            "selected_skew_rank_values_on_usable_rows": sorted(set(row["search_audit"]["selected_coordinate_skew_rank"] for row in all_usable_rows)),
            "rows_with_absolute_value_below_one": sum(row["absolute_value_below_one"] for row in all_usable_rows),
            "rows_with_positive_r_equals_one_measure_margin": sum(
                mp.mpf(row["leading_r_equals_one_measure_margin"]) > 0 for row in all_usable_rows
            ),
            "no_extrapolation": True,
        },
        "resource_audit": {
            "required_peak_rss_limit_kib": RSS_LIMIT_KIB,
            "observed_peak_rss_below_2_GiB": True,
            "note": "Variable observed RSS is printed but omitted from deterministic JSON.",
        },
        "logical_scope": {
            "exact_finite": (
                "Every recorded rational/integer rank, saturated HNF kernel, LLL-basis "
                "candidate, content, coefficient vector, endpoint identity, and origin "
                "order is exact on the displayed finite grids."
            ),
            "diagnostic_only": (
                "Decimal values, logarithmic bounds, and margins are diagnostics and "
                "prove no asymptotic inequality."
            ),
            "not_classification": (
                "The bounded {-1,0,1} search does not find globally shortest vectors; "
                "the rank-gap and nondecomposability patterns are not extrapolated."
            ),
        },
        "versions": {
            "python": sys.version,
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "python_flint": flint_version,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["finite_grid_summary"], indent=2, sort_keys=True))
    print(json.dumps(payload["resource_audit"], indent=2, sort_keys=True))
    print(f"observed_peak_rss_kib={peak_rss_kib}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
