#!/usr/bin/env python3
"""Exact replay for the third exterior sum of root-of-unity remainders.

The companion source proves the all-parameter endpoint-jet identity,
normalization, order, centered type, dimension criterion, and conditional
height ledger.  This script checks those identities on a small exact grid
containing both full and properly reduced endpoint spaces.  Finite rank
gaps are diagnostics only and are not extrapolated.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import resource
from pathlib import Path

import sympy as sp
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_third_exterior_sum_certificate.json"
X = sp.symbols("X")
RSS_LIMIT_KIB = 2 * 1024 * 1024

ExpPoly = dict[tuple[int, int], sp.Rational]


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def universal_Q(m: int, n: int) -> int:
    M = m * (n + 1)
    return (
        2**M
        * math.prod(math.factorial(a) for a in range(n + 1)) ** m
        * math.prod(
            h ** ((m - h) * (n + 1) ** 2)
            for h in range(1, m)
        )
    )


def interpolation_data(
    m: int, n: int, D: int, moments: list[sp.Rational]
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, list[tuple[int, int]]]:
    """Return C -> T_C, C -> beta_C, and C -> theta_C.

    Here beta_C=T_C(z,-1) and
    theta_C=(partial_z-partial_y)T_C(z,-1).
    """
    M = m * (n + 1)
    labels = [
        (frequency, degree)
        for frequency in range(m)
        for degree in range(n + 1)
    ]
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
                -sp.factorial(k) / sp.factorial(k - a)
                * moments[k - a]
                if a <= k
                else 0
                for a in range(D + 1)
            ]
            for k in range(M)
        ]
    )
    assert jet.det() != 0
    interpolation = jet.inv() * target
    beta = sp.zeros(n + 1, D + 1)
    theta = sp.zeros(n + 1, D + 1)
    for row, (frequency, degree) in enumerate(labels):
        sign = (-1) ** frequency
        beta[degree, :] += sign * interpolation[row, :]
        theta[degree, :] += frequency * sign * interpolation[row, :]
        if degree:
            theta[degree - 1, :] += degree * sign * interpolation[row, :]
    return interpolation, beta, theta, labels


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


def endpoint_constraint_matrix(
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
    rows: list[list[int]] = []
    for i in range(matrix.rows):
        values = [sp.Rational(value) for value in matrix.row(i)]
        denominator = math.lcm(*(int(sp.denom(value)) for value in values))
        row = [int(value * denominator) for value in values]
        content = math.gcd(*(abs(value) for value in row))
        assert content > 0
        row = [value // content for value in row]
        if next(value for value in row if value) < 0:
            row = [-value for value in row]
        rows.append(row)
    return sp.Matrix(rows) if rows else sp.zeros(0, matrix.cols)


def to_flint(matrix: sp.Matrix) -> fmpz_mat:
    return fmpz_mat(
        [
            [int(matrix[i, j]) for j in range(matrix.cols)]
            for i in range(matrix.rows)
        ]
    )


def from_flint(matrix: fmpz_mat) -> sp.Matrix:
    return sp.Matrix(
        [
            [int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())
        ]
    )


def exact_rank(matrix: sp.Matrix) -> int:
    return int(to_flint(matrix).rank())


def saturated_integer_kernel(matrix: sp.Matrix) -> sp.Matrix:
    """Return a saturated integral column basis for an integer kernel."""
    if matrix.rows == 0:
        return sp.eye(matrix.cols)
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
        [
            [transform[i, j] for j in range(transform.ncols())]
            for i in zero_rows
        ]
    )
    reduced, lll_transform = basis_rows.lll(transform=True)
    assert reduced == lll_transform * basis_rows
    assert abs(int(lll_transform.det())) == 1
    basis = from_flint(reduced).T
    assert matrix * basis == sp.zeros(matrix.rows, basis.cols)
    assert basis.cols == matrix.cols - exact_rank(matrix)
    return basis


def clean(poly: ExpPoly) -> ExpPoly:
    return {
        key: sp.cancel(value)
        for key, value in poly.items()
        if value
    }


def add(
    left: ExpPoly,
    right: ExpPoly,
    scale: sp.Rational = sp.Rational(1),
) -> ExpPoly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, sp.Rational(0)) + scale * value
    return clean(out)


def scalar(poly: ExpPoly, factor: sp.Rational) -> ExpPoly:
    return clean({key: factor * value for key, value in poly.items()})


def derivative(poly: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (frequency, degree), value in poly.items():
        if degree:
            key = (frequency, degree - 1)
            out[key] = out.get(key, sp.Rational(0)) + degree * value
        if frequency:
            key = (frequency, degree)
            out[key] = out.get(key, sp.Rational(0)) + frequency * value
    return clean(out)


def multiply(left: ExpPoly, right: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (q, k), a in left.items():
        for (r, ell), b in right.items():
            key = (q + r, k + ell)
            out[key] = out.get(key, sp.Rational(0)) + a * b
    return clean(out)


def multiply_three(a: ExpPoly, b: ExpPoly, c: ExpPoly) -> ExpPoly:
    return multiply(multiply(a, b), c)


def third_wronskian(a: ExpPoly, b: ExpPoly, c: ExpPoly) -> ExpPoly:
    forms = [a, b, c]
    first = [derivative(form) for form in forms]
    second = [derivative(form) for form in first]
    out: ExpPoly = {}
    signed_permutations = [
        ((0, 1, 2), 1),
        ((1, 2, 0), 1),
        ((2, 0, 1), 1),
        ((0, 2, 1), -1),
        ((2, 1, 0), -1),
        ((1, 0, 2), -1),
    ]
    for permutation, sign in signed_permutations:
        term = multiply_three(
            forms[permutation[0]],
            first[permutation[1]],
            second[permutation[2]],
        )
        out = add(out, term, sp.Rational(sign))
    return out


def monomial_remainders(
    m: int,
    n: int,
    D: int,
    interpolation: sp.Matrix,
    labels: list[tuple[int, int]],
) -> list[ExpPoly]:
    remainders: list[ExpPoly] = []
    for endpoint_degree in range(D + 1):
        remainder: ExpPoly = {(0, endpoint_degree): sp.Rational(1)}
        for row, (frequency, degree) in enumerate(labels):
            value = interpolation[row, endpoint_degree]
            if value:
                for q in (frequency, frequency + 1):
                    key = (q, degree)
                    remainder[key] = remainder.get(key, sp.Rational(0)) + value
        remainders.append(clean(remainder))
    return remainders


def linear_combination(forms: list[ExpPoly], coefficients: sp.Matrix) -> ExpPoly:
    out: ExpPoly = {}
    for coefficient, form in zip(coefficients, forms):
        if coefficient:
            out = add(out, form, sp.Rational(coefficient))
    return out


def endpoint_polynomial(poly: ExpPoly) -> list[sp.Rational]:
    out: dict[int, sp.Rational] = {}
    for (frequency, degree), value in poly.items():
        out[degree] = out.get(degree, sp.Rational(0)) + (-1) ** frequency * value
    if not out:
        return [sp.Rational(0)]
    result = [sp.cancel(out.get(k, sp.Rational(0))) for k in range(max(out) + 1)]
    return trim(result)


def trim(poly: list[sp.Rational]) -> list[sp.Rational]:
    out = [sp.cancel(value) for value in poly]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def poly_add(
    left: list[sp.Rational],
    right: list[sp.Rational],
    scale: sp.Rational = sp.Rational(1),
) -> list[sp.Rational]:
    size = max(len(left), len(right))
    out = [sp.Rational(0)] * size
    for i in range(size):
        out[i] = (
            (left[i] if i < len(left) else 0)
            + scale * (right[i] if i < len(right) else 0)
        )
    return trim(out)


def poly_scale(poly: list[sp.Rational], factor: sp.Rational) -> list[sp.Rational]:
    return trim([factor * value for value in poly])


def poly_derivative(poly: list[sp.Rational]) -> list[sp.Rational]:
    if len(poly) <= 1:
        return [sp.Rational(0)]
    return trim([k * poly[k] for k in range(1, len(poly))])


def poly_multiply(
    left: list[sp.Rational], right: list[sp.Rational]
) -> list[sp.Rational]:
    out = [sp.Rational(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_multiply_three(
    a: list[sp.Rational],
    b: list[sp.Rational],
    c: list[sp.Rational],
) -> list[sp.Rational]:
    return poly_multiply(poly_multiply(a, b), c)


def determinant_polynomial(
    first: list[list[sp.Rational]],
    second: list[list[sp.Rational]],
    third: list[list[sp.Rational]],
) -> list[sp.Rational]:
    out = [sp.Rational(0)]
    signed_permutations = [
        ((0, 1, 2), 1),
        ((1, 2, 0), 1),
        ((2, 0, 1), 1),
        ((0, 2, 1), -1),
        ((2, 1, 0), -1),
        ((1, 0, 2), -1),
    ]
    for permutation, sign in signed_permutations:
        term = poly_multiply_three(
            first[permutation[0]],
            second[permutation[1]],
            third[permutation[2]],
        )
        out = poly_add(out, term, sp.Rational(sign))
    return out


def matrix_image_polynomial(matrix: sp.Matrix, vector: sp.Matrix) -> list[sp.Rational]:
    image = matrix * vector
    return trim([sp.Rational(image[k]) for k in range(image.rows)])


def corrected_endpoint_polynomial(
    triple: tuple[int, int, int],
    endpoint_basis: sp.Matrix,
    beta: sp.Matrix,
    theta: sp.Matrix,
) -> list[sp.Rational]:
    zeroth: list[list[sp.Rational]] = []
    first: list[list[sp.Rational]] = []
    second: list[list[sp.Rational]] = []
    for index in triple:
        endpoint = trim(
            [sp.Rational(endpoint_basis[a, index]) for a in range(endpoint_basis.rows)]
        )
        beta_poly = matrix_image_polynomial(beta, endpoint_basis[:, index])
        theta_poly = matrix_image_polynomial(theta, endpoint_basis[:, index])
        first_jet = poly_add(poly_derivative(endpoint), beta_poly, -1)
        second_jet = poly_add(
            poly_add(poly_derivative(poly_derivative(endpoint)), beta_poly, -1),
            theta_poly,
            -2,
        )
        zeroth.append(endpoint)
        first.append(first_jet)
        second.append(second_jet)
    return determinant_polynomial(zeroth, first, second)


def taylor_coefficient(poly: ExpPoly, order: int) -> sp.Rational:
    value = sp.Rational(0)
    for (frequency, degree), coefficient in poly.items():
        if degree <= order:
            value += coefficient * sp.Rational(
                frequency ** (order - degree),
                math.factorial(order - degree),
            )
    return sp.cancel(value)


def vanishing_order(poly: ExpPoly, limit: int) -> int:
    for order in range(limit + 1):
        if taylor_coefficient(poly, order):
            return order
    raise AssertionError("vanishing order exceeds replay limit")


def primitive_integer_vector(vector: sp.Matrix) -> sp.Matrix:
    denominators = [int(sp.denom(value)) for value in vector]
    clearing = math.lcm(*denominators)
    values = [int(value * clearing) for value in vector]
    content = math.gcd(*(abs(value) for value in values))
    assert content > 0
    values = [value // content for value in values]
    if next(value for value in values if value) < 0:
        values = [-value for value in values]
    return sp.Matrix(values)


def contraction_rank(
    vector: sp.Matrix,
    triples: list[tuple[int, int, int]],
    dimension: int,
) -> int:
    pairs = list(itertools.combinations(range(dimension), 2))
    pair_index = {pair: i for i, pair in enumerate(pairs)}
    contraction = sp.zeros(len(pairs), dimension)
    for value, (i, j, k) in zip(vector, triples):
        contraction[pair_index[(j, k)], i] += value
        contraction[pair_index[(i, k)], j] -= value
        contraction[pair_index[(i, j)], k] += value
    return exact_rank(contraction)


def dictionary_digest(poly: ExpPoly) -> str:
    payload = [
        [frequency, degree, int(sp.numer(value)), int(sp.denom(value))]
        for (frequency, degree), value in sorted(poly.items())
    ]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()
    ).hexdigest()


def vector_digest(vector: sp.Matrix) -> str:
    payload = [int(value) for value in vector]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()
    ).hexdigest()


def center_phase(m: int) -> tuple[int, int]:
    """Return e^{-3 m i pi/2} as an exact Gaussian pair."""
    return ((1, 0), (0, -1), (-1, 0), (0, 1))[(3 * m) % 4]


def grid_row(m: int, n: int, D: int, nu: int, target_degree: int) -> dict:
    assert m >= 2 and n >= D >= 2 and 3 <= nu <= D + 1
    M = m * (n + 1)
    L = M + D + 1 - nu
    moments = logistic_moments(M + D + 5)
    Q = universal_Q(m, n)
    interpolation, beta, theta, labels = interpolation_data(m, n, D, moments)
    assert all(sp.denom(Q * value) == 1 for value in interpolation)
    assert all(sp.denom(Q * value) == 1 for value in beta)
    assert all(sp.denom(Q * value) == 1 for value in theta)

    constraints = endpoint_constraint_matrix(m, n, D, nu, moments)
    integer_constraints = primitive_integer_rows(constraints)
    endpoint_basis = saturated_integer_kernel(integer_constraints)
    assert endpoint_basis.shape == (D + 1, nu)
    assert constraints * endpoint_basis == sp.zeros(constraints.rows, nu)

    monomial_forms = monomial_remainders(m, n, D, interpolation, labels)
    forms = [
        linear_combination(monomial_forms, endpoint_basis[:, j])
        for j in range(nu)
    ]
    assert all(
        all(sp.denom(Q * value) == 1 for value in form.values())
        for form in forms
    )
    endpoint_orders = [vanishing_order(form, L + 2) for form in forms]
    assert min(endpoint_orders) >= L

    triples = list(itertools.combinations(range(nu), 3))
    analytic_triples: list[ExpPoly] = []
    corrected_triples: list[list[sp.Rational]] = []
    for triple in triples:
        analytic = third_wronskian(*(forms[i] for i in triple))
        corrected = corrected_endpoint_polynomial(
            triple, endpoint_basis, beta, theta
        )
        assert endpoint_polynomial(analytic) == corrected
        assert len(corrected) - 1 <= 2 * n + D
        assert all(sp.denom(Q**2 * value) == 1 for value in corrected)
        analytic_triples.append(analytic)
        corrected_triples.append(corrected)

    maximum_degree = 2 * n + D
    integer_map = sp.Matrix(
        [
            [
                int(Q**2 * (
                    corrected[ell] if ell < len(corrected) else 0
                ))
                for k, corrected in enumerate(corrected_triples)
            ]
            for ell in range(maximum_degree + 1)
        ]
    )
    tail = integer_map[target_degree + 1 :, :]
    full_rank = exact_rank(integer_map)
    tail_rank = exact_rank(tail)
    rank_gap = full_rank - tail_rank
    assert rank_gap > 0

    selected: sp.Matrix | None = None
    selected_contraction_rank = 0
    for candidate in tail.nullspace():
        if integer_map * candidate == sp.zeros(integer_map.rows, 1):
            continue
        primitive = primitive_integer_vector(candidate)
        rank = contraction_rank(primitive, triples, nu)
        output = integer_map * primitive
        output_degree = max(i for i, value in enumerate(output) if value)
        if rank > 3 and output_degree == target_degree:
            selected = primitive
            selected_contraction_rank = rank
            break
    assert selected is not None
    assert selected_contraction_rank > 3

    analytic_sum: ExpPoly = {}
    corrected_sum = [sp.Rational(0)]
    for coefficient, analytic, corrected in zip(
        selected, analytic_triples, corrected_triples
    ):
        if coefficient:
            analytic_sum = add(analytic_sum, analytic, coefficient)
            corrected_sum = poly_add(corrected_sum, corrected, coefficient)
    corrected_sum = trim(corrected_sum)
    assert endpoint_polynomial(analytic_sum) == corrected_sum
    assert len(corrected_sum) - 1 <= target_degree
    assert len(corrected_sum) - 1 == target_degree

    origin_order = vanishing_order(analytic_sum, 3 * L + 3)
    assert origin_order >= 3 * L
    frequencies = [frequency for frequency, _ in analytic_sum]
    polynomial_degrees = [degree for _, degree in analytic_sum]
    assert min(frequencies) == 0 and max(frequencies) == 3 * m
    assert max(polynomial_degrees) <= 3 * n

    cleared_analytic = scalar(analytic_sum, Q**3)
    assert all(sp.denom(value) == 1 for value in cleared_analytic.values())
    integer_endpoint = [int(Q**2 * value) for value in corrected_sum]
    content = math.gcd(*(abs(value) for value in integer_endpoint))
    assert content > 0
    primitive_endpoint = [value // content for value in integer_endpoint]
    assert math.gcd(*(abs(value) for value in primitive_endpoint)) == 1
    cleared_endpoint = endpoint_polynomial(cleared_analytic)
    assert cleared_endpoint == [sp.Integer(Q * value) for value in integer_endpoint]

    selected_height = max(abs(int(value)) for value in selected)
    cleared_height = max(abs(int(value)) for value in cleared_analytic.values())
    return {
        "parameters": {
            "m": m,
            "n": n,
            "D": D,
            "nu": nu,
            "target_degree": target_degree,
            "M": M,
            "L_nu": L,
        },
        "endpoint_constraint_count": constraints.rows,
        "endpoint_basis_saturated": True,
        "third_exterior_dimension": len(triples),
        "high_tail_row_count": maximum_degree - target_degree,
        "full_rank": full_rank,
        "tail_rank": tail_rank,
        "rank_gap": rank_gap,
        "selected_contraction_rank": selected_contraction_rank,
        "selected_is_genuinely_nondecomposable": True,
        "selected_coordinate_height_digits": len(str(selected_height)),
        "selected_coordinate_sha256": vector_digest(selected),
        "primitive_endpoint_coefficients_ascending": [
            str(value) for value in primitive_endpoint
        ],
        "primitive_endpoint_height_digits": len(
            str(max(abs(value) for value in primitive_endpoint))
        ),
        "corrected_content_digits": len(str(content)),
        "origin_order": origin_order,
        "origin_order_minus_3L": origin_order - 3 * L,
        "origin_order_at_least_3L": True,
        "raw_frequency_interval": [0, 3 * m],
        "centered_doubled_frequency_interval": [-3 * m, 3 * m],
        "centered_exponential_type": f"{3 * m}/2",
        "centering_endpoint_phase_real_imag": list(center_phase(m)),
        "analytic_polynomial_degree_bound": 3 * n,
        "actual_analytic_polynomial_degree": max(polynomial_degrees),
        "universal_Q_digits": len(str(Q)),
        "cleared_analytic_height_digits": len(str(cleared_height)),
        "analytic_sum_sha256": dictionary_digest(analytic_sum),
        "all_endpoint_jet_identities_exact": True,
        "Q_clears_each_auxiliary_map": True,
        "Q_squared_clears_corrected_endpoint": True,
        "Q_cubed_clears_analytic_sum": True,
        "cleared_endpoint_equals_Q_times_integer_endpoint": True,
    }


def dimension_diagnostics() -> list[dict]:
    rows = []
    for n in (10, 100, 1000, 10000):
        target_degree = 2
        # Minimal full endpoint dimension: D=nu-1, so solve the exact
        # implicit inequality binomial(nu,3)>2n+nu-1-d.
        nu = 3
        while math.comb(nu, 3) <= 2 * n + nu - 1 - target_degree:
            nu += 1
        rows.append(
            {
                "n": n,
                "minimal_full_endpoint_nu": nu,
                "third_exterior_dimension": math.comb(nu, 3),
                "tail_row_count": 2 * n + nu - 1 - target_degree,
                "nu_over_n_to_one_third": f"{nu / n ** (1 / 3):.12f}",
            }
        )
    return rows


def main() -> None:
    grid = [
        grid_row(2, 5, 5, 6, 2),
        grid_row(3, 5, 5, 6, 2),
        grid_row(2, 6, 6, 6, 2),
        grid_row(3, 6, 6, 6, 2),
    ]
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    payload = {
        "schema": "root-unity-third-exterior-sum-v1",
        "exact_grid": grid,
        "dimension_diagnostics": dimension_diagnostics(),
        "all_parameter_results_proved_in_source": {
            "endpoint_jets": [
                "R(i*pi)=C(i*pi)",
                "R'(i*pi)=(C'-beta)(i*pi)",
                "R''(i*pi)=(C''-beta-2*theta)(i*pi)",
            ],
            "theta_definition": "theta=(partial_z-partial_y)T(z,-1)",
            "common_origin_order": "at least 3*L_nu",
            "corrected_degree_bound": "at most 2*n+D",
            "analytic_degree_bound": "at most 3*n",
            "raw_frequency_support": "0,...,3*m",
            "centered_type": "3*m/2",
            "integer_endpoint_clearing": "Q^2",
            "integer_analytic_clearing": "Q^3",
            "primitive_endpoint_normalization_divisor": "Q*content(Q^2 Delta_3)",
            "tail_rank_gap_is_necessary_and_sufficient": True,
            "dimension_scale": "nu=Theta(n^(1/3))",
            "content_free_universal_ledger_is_strictly_negative": True,
            "matched_per_column_height_threshold_is_unchanged_from_k=2": True,
        },
        "limitations": {
            "finite_rank_gaps_are_not_extrapolated": True,
            "no_all_parameter_rank_gap_theorem": True,
            "no_intrinsic_height_or_content_theorem": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
        "peak_rss_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUT),
                "grid_rows": len(grid),
                "all_assertions_passed": True,
                "peak_rss_mib": round(peak_rss_kib / 1024, 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
