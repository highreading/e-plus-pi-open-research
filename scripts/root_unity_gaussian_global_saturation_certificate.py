#!/usr/bin/env python3
"""Gaussian phase alignment inside saturated k=2 global-image lattices.

For full endpoint spaces with D=n, this replay:

* splits the exterior tail kernel into even- and odd-output blocks;
* saturates each complete global Wronskian image intrinsically;
* audits the 2-primary glue in the unphased sum;
* verifies that the real/imaginary phase-aligned embedding is already
  saturated, so none of that glue survives alignment;
* enumerates a bounded box in each saturated LLL basis; and
* optimizes the exact coefficientwise centered Schwarz majorant for the
  selected component and mixed candidates.

All lattice, rank, endpoint, content, reflection, and saturation assertions
are exact. Radius optimizations and logarithmic margins are high-precision
diagnostics and are never used to infer an asymptotic theorem.
"""

from __future__ import annotations

import gc
import hashlib
import importlib.util
import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import __version__ as flint_version
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
ND_PATH = ROOT / "scripts" / "root_unity_nondecomposable_exterior_sum_certificate.py"
K2_PATH = ROOT / "scripts" / "root_unity_k2_global_image_saturation_certificate.py"
ND_SHA256 = "3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f"
K2_SHA256 = "588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470"
OUT = ROOT / "results" / "root_unity_gaussian_global_saturation_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
SEARCH_BOX = (-1, 0, 1)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependency(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


assert sha256_file(ND_PATH) == ND_SHA256
assert sha256_file(K2_PATH) == K2_SHA256
nd = load_dependency("gaussian_global_nd_dependency", ND_PATH)
k2 = load_dependency("gaussian_global_k2_dependency", K2_PATH)


def matrix_digest(matrix: fmpz_mat | sp.Matrix) -> str:
    if isinstance(matrix, sp.MatrixBase):
        rows = matrix.rows
        columns = matrix.cols
        getter = lambda i, j: matrix[i, j]
    else:
        rows = matrix.nrows()
        columns = matrix.ncols()
        getter = lambda i, j: matrix[i, j]
    digest = hashlib.sha256()
    digest.update(f"{rows},{columns}\n".encode())
    for i in range(rows):
        for j in range(columns):
            digest.update(f"{int(getter(i, j))}\n".encode())
    return digest.hexdigest()


def vector_digest(vector: list[int]) -> str:
    digest = hashlib.sha256()
    for value in vector:
        digest.update(f"{value}\n".encode())
    return digest.hexdigest()


def nonzero_rows(matrix: sp.Matrix) -> sp.Matrix:
    rows = [
        i
        for i in range(matrix.rows)
        if any(matrix[i, j] != 0 for j in range(matrix.cols))
    ]
    if not rows:
        return sp.zeros(0, matrix.cols)
    return matrix.extract(rows, range(matrix.cols))


def exact_rank(matrix: sp.Matrix) -> int:
    if matrix.rows == 0 or matrix.cols == 0:
        return 0
    return nd.exact_rank(matrix)


def saturated_kernel_allow_zero(matrix: sp.Matrix) -> tuple[sp.Matrix, dict]:
    rank = exact_rank(matrix)
    if rank == matrix.cols:
        return sp.zeros(matrix.cols, 0), {
            "kernel_dimension": 0,
            "zero_kernel_verified_by_full_column_rank": True,
            "saturated": True,
        }
    basis, audit = nd.saturated_integer_kernel(matrix)
    assert matrix * basis == sp.zeros(matrix.rows, basis.cols)
    assert basis.cols == matrix.cols - rank
    audit["zero_kernel_verified_by_full_column_rank"] = False
    audit["saturated"] = True
    return basis, audit


def fmpz_to_rows(matrix: fmpz_mat) -> list[list[int]]:
    return [
        [int(matrix[i, j]) for j in range(matrix.ncols())]
        for i in range(matrix.nrows())
    ]


def stack_fmpz_rows(*matrices: fmpz_mat) -> sp.Matrix:
    rows: list[list[int]] = []
    for matrix in matrices:
        rows.extend(fmpz_to_rows(matrix))
    assert rows
    return sp.Matrix(rows)


def aligned_real_doubling(even_basis: fmpz_mat, odd_basis: fmpz_mat) -> sp.Matrix:
    ambient = even_basis.ncols()
    assert odd_basis.ncols() == ambient
    rows: list[list[int]] = []
    for row in fmpz_to_rows(even_basis):
        rows.append(row + [0] * ambient)
    for row in fmpz_to_rows(odd_basis):
        rows.append([0] * ambient + row)
    return sp.Matrix(rows)


def endpoint_vector(vector: list[int], m: int, n: int) -> list[int]:
    polynomial_slots = 2 * n + 1
    assert len(vector) == (2 * m + 1) * polynomial_slots
    return [
        sum(
            (-1) ** frequency
            * vector[frequency * polynomial_slots + degree]
            for frequency in range(2 * m + 1)
        )
        for degree in range(polynomial_slots)
    ]


def primitive_vector(vector: list[int]) -> tuple[list[int], int]:
    content = math.gcd(*(abs(value) for value in vector))
    assert content > 0
    primitive = [value // content for value in vector]
    first = next(value for value in primitive if value)
    if first < 0:
        primitive = [-value for value in primitive]
    assert math.gcd(*(abs(value) for value in primitive)) == 1
    return primitive, content


def integer_pi_coefficients(endpoint: list[int], content: int) -> list[int]:
    primitive = [value // content for value in endpoint]
    return [
        (-1) ** (degree // 2) * value
        for degree, value in enumerate(primitive)
    ]


def centered_reflection_verified(
    basis: fmpz_mat,
    m: int,
    n: int,
    epsilon: int,
) -> bool:
    polynomial_slots = 2 * n + 1
    assert epsilon in (-1, 1)
    for row in range(basis.nrows()):
        for degree in range(polynomial_slots):
            central = int(basis[row, m * polynomial_slots + degree])
            assert (1 - epsilon * (-1) ** degree) * central == 0
        for frequency in range(1, m + 1):
            for degree in range(polynomial_slots):
                negative = int(
                    basis[
                        row,
                        (m - frequency) * polynomial_slots + degree,
                    ]
                )
                positive = int(
                    basis[
                        row,
                        (m + frequency) * polynomial_slots + degree,
                    ]
                )
                assert negative == epsilon * (-1) ** degree * positive
    return True


# A term is (kind, polynomial_degree, positive_frequency, exact_weight).
# For mono/cosh/sinh/exp, exact_weight is the positive integer coefficient.
# For gmono/gexp, exact_weight is the squared Gaussian modulus.
Term = tuple[str, int, int, int]


def reflection_terms(
    vector: list[int],
    m: int,
    n: int,
    epsilon: int,
) -> list[Term]:
    polynomial_slots = 2 * n + 1
    terms: list[Term] = []
    for degree in range(polynomial_slots):
        value = abs(vector[m * polynomial_slots + degree])
        if value:
            assert epsilon * (-1) ** degree == 1
            terms.append(("mono", degree, 0, value))
    for frequency in range(1, m + 1):
        for degree in range(polynomial_slots):
            value = abs(
                vector[(m + frequency) * polynomial_slots + degree]
            )
            if not value:
                continue
            kind = (
                "cosh"
                if epsilon * (-1) ** degree == 1
                else "sinh"
            )
            terms.append((kind, degree, frequency, 2 * value))
    assert terms
    return terms


def gaussian_exponential_terms(
    even_vector: list[int],
    odd_vector: list[int],
    m: int,
    n: int,
) -> list[Term]:
    polynomial_slots = 2 * n + 1
    terms: list[Term] = []
    for degree in range(polynomial_slots):
        even_value = even_vector[m * polynomial_slots + degree]
        odd_value = odd_vector[m * polynomial_slots + degree]
        squared = even_value * even_value + odd_value * odd_value
        if squared:
            terms.append(("gmono", degree, 0, squared))
    for frequency in range(1, m + 1):
        for degree in range(polynomial_slots):
            index = (m + frequency) * polynomial_slots + degree
            squared = (
                even_vector[index] * even_vector[index]
                + odd_vector[index] * odd_vector[index]
            )
            if squared:
                terms.append(("gexp", degree, frequency, squared))
    assert terms
    return terms


def term_log_and_elasticity_float(term: Term, radius: float) -> tuple[float, float]:
    kind, degree, frequency, weight = term
    if kind == "gmono":
        log_coefficient = 0.5 * math.log(weight)
        return log_coefficient + degree * math.log(radius), float(degree)
    if kind == "gexp":
        log_coefficient = math.log(2.0) + 0.5 * math.log(weight)
        argument = frequency * radius
        return (
            log_coefficient + degree * math.log(radius) + argument,
            degree + argument,
        )
    log_coefficient = math.log(weight)
    base = log_coefficient + degree * math.log(radius)
    if kind == "mono":
        return base, float(degree)
    argument = frequency * radius
    if kind == "exp":
        return base + argument, degree + argument
    if kind == "cosh":
        log_hyperbolic = (
            argument
            + math.log1p(math.exp(-2 * argument))
            - math.log(2.0)
        )
        return (
            base + log_hyperbolic,
            degree + argument * math.tanh(argument),
        )
    assert kind == "sinh"
    log_hyperbolic = (
        argument
        + math.log1p(-math.exp(-2 * argument))
        - math.log(2.0)
    )
    return (
        base + log_hyperbolic,
        degree + argument / math.tanh(argument),
    )


def logsumexp_float(values: list[float]) -> float:
    maximum = max(values)
    return maximum + math.log(sum(math.exp(value - maximum) for value in values))


def log_bound_and_elasticity_float(
    terms: list[Term],
    radius: float,
) -> tuple[float, float]:
    evaluated = [
        term_log_and_elasticity_float(term, radius) for term in terms
    ]
    logs = [item[0] for item in evaluated]
    log_bound = logsumexp_float(logs)
    elasticity = sum(
        math.exp(log_value - log_bound) * term_elasticity
        for log_value, term_elasticity in evaluated
    )
    return log_bound, elasticity


def optimize_terms_float(terms: list[Term], origin_order: int) -> tuple[float, float]:
    """Minimize B(R)*(pi/R)^origin_order for R>=pi."""
    lower = math.pi
    lower_log, lower_elasticity = log_bound_and_elasticity_float(terms, lower)
    if lower_elasticity >= origin_order:
        return lower, lower_log
    upper = max(4.0, float(origin_order))
    while log_bound_and_elasticity_float(terms, upper)[1] < origin_order:
        upper *= 2
    for _ in range(90):
        middle = (lower + upper) / 2
        if log_bound_and_elasticity_float(terms, middle)[1] < origin_order:
            lower = middle
        else:
            upper = middle
    radius = (lower + upper) / 2
    log_bound, _ = log_bound_and_elasticity_float(terms, radius)
    log_schwarz = log_bound + origin_order * (
        math.log(math.pi) - math.log(radius)
    )
    return radius, log_schwarz


def term_log_and_elasticity_mp(term: Term, radius: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    kind, degree, frequency, weight = term
    if kind == "gmono":
        log_coefficient = mp.log(weight) / 2
        return log_coefficient + degree * mp.log(radius), mp.mpf(degree)
    if kind == "gexp":
        log_coefficient = mp.log(2) + mp.log(weight) / 2
        argument = frequency * radius
        return (
            log_coefficient + degree * mp.log(radius) + argument,
            degree + argument,
        )
    log_coefficient = mp.log(weight)
    base = log_coefficient + degree * mp.log(radius)
    if kind == "mono":
        return base, mp.mpf(degree)
    argument = frequency * radius
    if kind == "exp":
        return base + argument, degree + argument
    if kind == "cosh":
        return (
            base + mp.log(mp.cosh(argument)),
            degree + argument * mp.tanh(argument),
        )
    assert kind == "sinh"
    return (
        base + mp.log(mp.sinh(argument)),
        degree + argument / mp.tanh(argument),
    )


def log_bound_and_elasticity_mp(
    terms: list[Term],
    radius: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    evaluated = [term_log_and_elasticity_mp(term, radius) for term in terms]
    maximum = max(item[0] for item in evaluated)
    weights = [mp.exp(item[0] - maximum) for item in evaluated]
    total = mp.fsum(weights)
    log_bound = maximum + mp.log(total)
    elasticity = mp.fsum(
        weight * item[1] for weight, item in zip(weights, evaluated)
    ) / total
    return log_bound, elasticity


def optimize_terms_mp(terms: list[Term], origin_order: int) -> tuple[mp.mpf, mp.mpf]:
    lower = mp.pi
    lower_log, lower_elasticity = log_bound_and_elasticity_mp(terms, lower)
    if lower_elasticity >= origin_order:
        return lower, lower_log
    upper = mp.mpf(max(4, origin_order))
    while log_bound_and_elasticity_mp(terms, upper)[1] < origin_order:
        upper *= 2
    for _ in range(240):
        middle = (lower + upper) / 2
        if log_bound_and_elasticity_mp(terms, middle)[1] < origin_order:
            lower = middle
        else:
            upper = middle
    radius = (lower + upper) / 2
    log_bound, _ = log_bound_and_elasticity_mp(terms, radius)
    log_schwarz = log_bound + origin_order * (
        mp.log(mp.pi) - mp.log(radius)
    )
    return radius, log_schwarz


def term_digest(terms: list[Term]) -> str:
    digest = hashlib.sha256()
    for kind, degree, frequency, weight in terms:
        digest.update(f"{kind},{degree},{frequency},{weight}\n".encode())
    return digest.hexdigest()


def candidate_from_vector(
    vector: list[int],
    basis_coefficients: tuple[int, ...],
    m: int,
    n: int,
    target_degree: int,
    epsilon: int,
    origin_order: int,
) -> dict | None:
    primitive_global, global_content = primitive_vector(vector)
    endpoint = endpoint_vector(primitive_global, m, n)
    nonzero_degrees = [
        degree for degree, value in enumerate(endpoint) if value
    ]
    if not nonzero_degrees:
        return None
    assert max(nonzero_degrees) <= target_degree
    assert all(
        endpoint[degree] == 0
        for degree in range(len(endpoint))
        if (-1) ** degree != epsilon
    )
    endpoint_content = math.gcd(
        *(abs(endpoint[degree]) for degree in nonzero_degrees)
    )
    assert endpoint_content > 0
    A_coefficients = integer_pi_coefficients(endpoint, endpoint_content)
    actual_degree = max(nonzero_degrees)
    endpoint_height = max(abs(value) for value in A_coefficients)
    terms = reflection_terms(primitive_global, m, n, epsilon)
    radius_float, log_raw_schwarz_float = optimize_terms_float(
        terms, origin_order
    )
    log_primitive_schwarz_float = (
        log_raw_schwarz_float - math.log(endpoint_content)
    )
    leading_r_one_margin_float = (
        -log_primitive_schwarz_float
        - actual_degree * math.log(endpoint_height)
    )
    return {
        "vector": primitive_global,
        "basis_coefficients": basis_coefficients,
        "global_content_removed": global_content,
        "endpoint": endpoint,
        "endpoint_content": endpoint_content,
        "A_coefficients": A_coefficients,
        "actual_degree": actual_degree,
        "endpoint_height": endpoint_height,
        "terms": terms,
        "radius_float": radius_float,
        "log_primitive_schwarz_float": log_primitive_schwarz_float,
        "leading_r_one_margin_float": leading_r_one_margin_float,
    }


def select_component_candidate(
    saturated_lll: fmpz_mat,
    m: int,
    n: int,
    target_degree: int,
    epsilon: int,
    origin_order: int,
) -> tuple[dict, dict]:
    basis_rows = fmpz_to_rows(saturated_lll)
    seen: set[tuple[int, ...]] = set()
    candidates: list[dict] = []
    coefficient_vectors_tested = 0
    for coefficients in itertools.product(SEARCH_BOX, repeat=len(basis_rows)):
        if not any(coefficients):
            continue
        coefficient_vectors_tested += 1
        vector = [
            sum(
                coefficients[row] * basis_rows[row][column]
                for row in range(len(basis_rows))
            )
            for column in range(len(basis_rows[0]))
        ]
        primitive_global, _ = primitive_vector(vector)
        key = tuple(primitive_global)
        if key in seen:
            continue
        seen.add(key)
        candidate = candidate_from_vector(
            vector,
            coefficients,
            m,
            n,
            target_degree,
            epsilon,
            origin_order,
        )
        if candidate is not None:
            candidates.append(candidate)
    assert candidates
    selected = max(
        candidates,
        key=lambda candidate: (
            candidate["leading_r_one_margin_float"],
            -candidate["endpoint_height"],
            -max(abs(value) for value in candidate["vector"]),
            tuple(candidate["vector"]),
        ),
    )

    mp.mp.dps = 100
    radius, log_raw_schwarz = optimize_terms_mp(
        selected["terms"], origin_order
    )
    log_primitive_schwarz = log_raw_schwarz - mp.log(
        selected["endpoint_content"]
    )
    margin = (
        -log_primitive_schwarz
        - selected["actual_degree"] * mp.log(selected["endpoint_height"])
    )
    endpoint_value = mp.fsum(
        mp.mpf(value) * mp.pi**degree
        for degree, value in enumerate(selected["A_coefficients"])
    )
    selected["optimized_radius"] = radius
    selected["log_primitive_schwarz"] = log_primitive_schwarz
    selected["leading_r_one_margin"] = margin
    selected["absolute_endpoint_value"] = abs(endpoint_value)
    audit = {
        "search_box": list(SEARCH_BOX),
        "basis_rank": len(basis_rows),
        "coefficient_vectors_tested": coefficient_vectors_tested,
        "unique_primitive_global_vectors_tested": len(seen),
        "nonzero_endpoint_candidates_tested": len(candidates),
        "bounded_search_not_a_shortest_or_global_optimum_certificate": True,
    }
    return selected, audit


def public_component_candidate(candidate: dict, audit: dict) -> dict:
    vector = candidate["vector"]
    endpoint = candidate["endpoint"]
    return {
        "search_audit": audit,
        "selected_LLL_basis_coefficients": list(candidate["basis_coefficients"]),
        "global_content_removed_before_endpoint_normalization": str(
            candidate["global_content_removed"]
        ),
        "primitive_global_vector_height": str(max(abs(value) for value in vector)),
        "primitive_global_vector_height_decimal_digits": len(
            str(max(abs(value) for value in vector))
        ),
        "primitive_global_vector_nonzero_slot_count": sum(
            value != 0 for value in vector
        ),
        "primitive_global_vector_sha256": vector_digest(vector),
        "raw_endpoint_coefficients_ascending": [str(value) for value in endpoint],
        "endpoint_content": str(candidate["endpoint_content"]),
        "primitive_integer_pi_polynomial_coefficients_ascending": [
            str(value) for value in candidate["A_coefficients"]
        ],
        "actual_endpoint_degree": candidate["actual_degree"],
        "primitive_endpoint_height": str(candidate["endpoint_height"]),
        "coefficientwise_term_count": len(candidate["terms"]),
        "coefficientwise_terms_sha256": term_digest(candidate["terms"]),
        "optimized_centered_radius": mp.nstr(
            candidate["optimized_radius"], 50
        ),
        "optimized_log_Schwarz_upper_bound_for_primitive_value": mp.nstr(
            candidate["log_primitive_schwarz"], 50
        ),
        "leading_r_equals_one_measure_margin": mp.nstr(
            candidate["leading_r_one_margin"], 50
        ),
        "absolute_endpoint_value_at_pi_diagnostic": mp.nstr(
            candidate["absolute_endpoint_value"], 50
        ),
        "radius_and_value_fields_are_high_precision_diagnostics": True,
    }


def mixed_candidate(
    even: dict,
    odd: dict,
    m: int,
    n: int,
    origin_order: int,
) -> dict:
    even_vector = even["vector"]
    odd_vector = odd["vector"]
    endpoint = [
        even_value + odd_value
        for even_value, odd_value in zip(even["endpoint"], odd["endpoint"])
    ]
    nonzero_degrees = [
        degree for degree, value in enumerate(endpoint) if value
    ]
    assert nonzero_degrees
    endpoint_content = math.gcd(
        *(abs(endpoint[degree]) for degree in nonzero_degrees)
    )
    A_coefficients = integer_pi_coefficients(endpoint, endpoint_content)
    actual_degree = max(nonzero_degrees)
    endpoint_height = max(abs(value) for value in A_coefficients)

    separated_terms = even["terms"] + odd["terms"]
    gaussian_terms = gaussian_exponential_terms(
        even_vector, odd_vector, m, n
    )
    separated_radius, separated_raw_log = optimize_terms_mp(
        separated_terms, origin_order
    )
    gaussian_radius, gaussian_raw_log = optimize_terms_mp(
        gaussian_terms, origin_order
    )
    if separated_raw_log <= gaussian_raw_log:
        selected_bound = "separated_paired_hyperbolic"
        optimized_radius = separated_radius
        raw_log = separated_raw_log
    else:
        selected_bound = "direct_gaussian_exponential"
        optimized_radius = gaussian_radius
        raw_log = gaussian_raw_log
    primitive_log = raw_log - mp.log(endpoint_content)
    margin = -primitive_log - actual_degree * mp.log(endpoint_height)

    # Exact arithmetic parts of the all-parameter domination theorem.
    assert endpoint_content <= even["endpoint_content"]
    assert endpoint_content <= odd["endpoint_content"]
    assert endpoint_height >= even["endpoint_height"]
    assert endpoint_height >= odd["endpoint_height"]
    assert actual_degree >= even["actual_degree"]
    assert actual_degree >= odd["actual_degree"]
    polynomial_slots = 2 * n + 1
    gaussian_slot_domination = all(
        even_vector[index] ** 2 + odd_vector[index] ** 2
        >= even_vector[index] ** 2
        and even_vector[index] ** 2 + odd_vector[index] ** 2
        >= odd_vector[index] ** 2
        for index in range((2 * m + 1) * polynomial_slots)
    )
    assert gaussian_slot_domination

    # The source proves this comparison pointwise for every radius.  The
    # numerical optimized values have ample slack on the finite grid.
    assert margin <= even["leading_r_one_margin"] + mp.mpf("1e-40")
    assert margin <= odd["leading_r_one_margin"] + mp.mpf("1e-40")

    endpoint_value = mp.fsum(
        mp.mpf(value) * mp.pi**degree
        for degree, value in enumerate(A_coefficients)
    )
    return {
        "formed_from_selected_even_and_odd_component_candidates": True,
        "raw_endpoint_coefficients_ascending": [
            str(value) for value in endpoint
        ],
        "joint_endpoint_content_is_gcd_across_parities": str(endpoint_content),
        "primitive_integer_pi_polynomial_coefficients_ascending": [
            str(value) for value in A_coefficients
        ],
        "actual_endpoint_degree": actual_degree,
        "primitive_endpoint_height": str(endpoint_height),
        "separated_hyperbolic_term_count": len(separated_terms),
        "direct_gaussian_term_count": len(gaussian_terms),
        "separated_hyperbolic_terms_sha256": term_digest(separated_terms),
        "direct_gaussian_terms_sha256": term_digest(gaussian_terms),
        "selected_coefficientwise_bound": selected_bound,
        "optimized_centered_radius": mp.nstr(optimized_radius, 50),
        "optimized_log_Schwarz_upper_bound_for_primitive_value": mp.nstr(
            primitive_log, 50
        ),
        "leading_r_equals_one_measure_margin": mp.nstr(margin, 50),
        "margin_no_larger_than_each_component_verified": True,
        "Gaussian_slot_moduli_dominate_each_component_exactly": True,
        "joint_content_no_larger_than_each_component_exactly": True,
        "joint_height_and_degree_no_smaller_than_each_component_exactly": True,
        "absolute_endpoint_value_at_pi_diagnostic": mp.nstr(
            abs(endpoint_value), 50
        ),
        "radius_and_value_fields_are_high_precision_diagnostics": True,
    }


def build_global_context(m: int, n: int) -> dict:
    D = n
    nu = D + 1
    M = m * (n + 1)
    moments = nd.logistic_moments(M + n + 10)
    interpolation, beta, labels = nd.interpolation_data(
        m, n, D, moments
    )
    Q = nd.universal_Q(m, n)
    corrected_map = nd.corrected_Q_map(beta, Q, n, D)
    pairs = list(itertools.combinations(range(nu), 2))
    remainders = nd.cleared_remainders(
        m,
        n,
        D,
        Q,
        interpolation,
        labels,
        sp.eye(nu),
    )
    global_rows = []
    for first, second in pairs:
        pair = nd.exp_wronskian(remainders[first], remainders[second])
        global_rows.append(
            [value for frequency in pair for value in frequency]
        )
    global_map = sp.Matrix(global_rows)
    return {
        "m": m,
        "n": n,
        "D": D,
        "nu": nu,
        "M": M,
        "Q": Q,
        "corrected_map": corrected_map,
        "pairs": pairs,
        "global_map": global_map,
    }


def parity_block(context: dict, target_degree: int, output_parity: int) -> dict:
    m = context["m"]
    n = context["n"]
    corrected_map: sp.Matrix = context["corrected_map"]
    pairs: list[tuple[int, int]] = context["pairs"]
    global_map: sp.Matrix = context["global_map"]
    columns = [
        column
        for column, (first, second) in enumerate(pairs)
        if (first + second - 1) % 2 == output_parity
    ]
    block_map = corrected_map[:, columns]
    assert all(
        block_map[row, column] == 0
        for row in range(block_map.rows)
        if row % 2 != output_parity
        for column in range(block_map.cols)
    )
    tail = nonzero_rows(block_map[target_degree + 1 :, :])
    primitive_tail = nd.primitive_integer_rows(tail)
    tail_kernel, tail_audit = saturated_kernel_allow_zero(primitive_tail)
    assert tail_kernel.cols > 0
    global_block = global_map.extract(columns, range(global_map.cols))
    raw_global_image = tail_kernel.transpose() * global_block
    lattice = k2.saturation_from_row_lattice(raw_global_image)
    saturated_basis = lattice["saturated_basis"]
    saturated_lll = lattice["saturated_lll"]
    epsilon = 1 if output_parity == 0 else -1
    assert centered_reflection_verified(
        saturated_basis, m, n, epsilon
    )
    assert centered_reflection_verified(saturated_lll, m, n, epsilon)
    endpoints = k2.endpoint_rows(saturated_basis, m, n)
    assert all(
        endpoints[row, degree] == 0
        for row in range(endpoints.rows)
        for degree in range(target_degree + 1, endpoints.cols)
    )
    assert all(
        endpoints[row, degree] == 0
        for row in range(endpoints.rows)
        for degree in range(target_degree + 1)
        if degree % 2 != output_parity
    )
    low_rank = int(endpoints[:, : target_degree + 1].rank())
    candidate, search_audit = select_component_candidate(
        saturated_lll,
        m,
        n,
        target_degree,
        epsilon,
        2 * context["M"],
    )
    return {
        "output_parity": output_parity,
        "epsilon": epsilon,
        "columns": columns,
        "tail_kernel": tail_kernel,
        "tail_audit": tail_audit,
        "lattice": lattice,
        "saturated_basis": saturated_basis,
        "saturated_lll": saturated_lll,
        "low_rank": low_rank,
        "candidate": candidate,
        "search_audit": search_audit,
        "public": {
            "output_parity": "even" if output_parity == 0 else "odd",
            "centered_reflection_eigenvalue": epsilon,
            "ambient_exterior_column_count": len(columns),
            "tail_kernel_dimension": tail_kernel.cols,
            "raw_global_image_rank": lattice["rank"],
            "intrinsic_saturation_index": str(lattice["index"]),
            "intrinsic_saturation_index_decimal_digits": len(
                str(lattice["index"])
            ),
            "intrinsic_saturated_basis_rank": saturated_basis.nrows(),
            "low_endpoint_image_rank": low_rank,
            "centered_reflection_verified_on_saturated_basis_and_LLL": True,
            "endpoint_tail_and_wrong_parity_zero_exactly": True,
            "tail_kernel_audit": tail_audit,
            "saturated_basis_sha256": matrix_digest(saturated_basis),
            "saturated_LLL_basis_sha256": matrix_digest(saturated_lll),
            "selected_component_candidate": public_component_candidate(
                candidate, search_audit
            ),
        },
    }


def row_audit(context: dict, target_degree: int) -> dict:
    even = parity_block(context, target_degree, 0)
    odd = parity_block(context, target_degree, 1)
    even_basis = even["saturated_basis"]
    odd_basis = odd["saturated_basis"]
    assert even_basis.ncols() == odd_basis.ncols()
    direct_sum = stack_fmpz_rows(even_basis, odd_basis)
    unphased_total = k2.saturation_from_row_lattice(direct_sum)
    assert unphased_total["rank"] == even_basis.nrows() + odd_basis.nrows()
    assert all(
        invariant in (1, 2)
        for invariant in unphased_total["smith_invariants"]
    )
    assert unphased_total["index"] == 2 ** sum(
        invariant == 2
        for invariant in unphased_total["smith_invariants"]
    )

    aligned_doubled = aligned_real_doubling(even_basis, odd_basis)
    # Each factor was just certified to be V_epsilon cap Z^P.  Therefore
    # its block product is (V_+ x V_-) cap Z^(2P), so its saturation index
    # is exactly one without another large 2P-dimensional HNF.  Replay one
    # explicit anchor to audit this block-product implementation.
    explicit_aligned_hnf_anchor = (
        context["m"] == 2
        and context["n"] == 4
        and target_degree == 2
    )
    if explicit_aligned_hnf_anchor:
        aligned_saturation = k2.saturation_from_row_lattice(aligned_doubled)
        assert aligned_saturation["index"] == 1
        assert all(
            invariant == 1
            for invariant in aligned_saturation["smith_invariants"]
        )

    mixed = mixed_candidate(
        even["candidate"],
        odd["candidate"],
        context["m"],
        context["n"],
        2 * context["M"],
    )
    best_component_margin = max(
        even["candidate"]["leading_r_one_margin"],
        odd["candidate"]["leading_r_one_margin"],
    )
    assert mp.mpf(mixed["leading_r_equals_one_measure_margin"]) <= (
        best_component_margin + mp.mpf("1e-40")
    )
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    return {
        "parameters": {
            "m": context["m"],
            "n": context["n"],
            "D": context["D"],
            "nu": context["nu"],
            "target_degree": target_degree,
            "common_origin_order": 2 * context["M"],
        },
        "even_block": even["public"],
        "odd_block": odd["public"],
        "unphased_real_sum_saturation": {
            "direct_parity_sum_rank": direct_sum.rows,
            "full_unphased_saturated_rank": unphased_total["rank"],
            "glue_index": str(unphased_total["index"]),
            "glue_index_is_a_power_of_two": True,
            "quotient_invariant_factors": [
                str(value) for value in unphased_total["smith_invariants"]
            ],
            "quotient_is_killed_by_two_exactly": True,
            "full_unphased_saturated_basis_sha256": matrix_digest(
                unphased_total["saturated_basis"]
            ),
        },
        "phase_aligned_Gaussian_fixed_lattice": {
            "real_doubled_rank": aligned_doubled.rows,
            "ambient_real_doubled_dimension": aligned_doubled.cols,
            "intrinsic_saturation_index": "1",
            "all_Smith_invariants_one": True,
            "aligned_direct_sum_is_already_intrinsically_saturated": True,
            "index_one_follows_exactly_from_the_block_product_intersection_identity": True,
            "explicit_tall_HNF_anchor_replayed_on_this_row": explicit_aligned_hnf_anchor,
            "aligned_real_doubled_basis_sha256": matrix_digest(
                aligned_doubled
            ),
        },
        "representative_mixed_candidate": mixed,
        "best_bounded_search_component_margin": mp.nstr(
            best_component_margin, 50
        ),
        "mixed_candidate_margin_no_larger_than_best_component": True,
        "row_digest_sha256": hashlib.sha256(
            (
                f"{context['m']},{context['n']},{target_degree}\n"
                + matrix_digest(even_basis)
                + matrix_digest(odd_basis)
                + matrix_digest(aligned_doubled)
            ).encode()
        ).hexdigest(),
        "peak_RSS_checked_below_2GiB_after_row": True,
    }


def main() -> None:
    start = time.perf_counter()
    rows: list[dict] = []
    # Largest contexts first makes RSS monitoring conservative.
    for m, n in ((3, 6), (2, 6), (3, 5), (2, 5), (3, 4), (2, 4)):
        context = build_global_context(m, n)
        for target_degree in (2, 3):
            rows.append(row_audit(context, target_degree))
            gc.collect()
            assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < RSS_LIMIT_KIB
        del context
        gc.collect()
    rows.sort(
        key=lambda row: (
            row["parameters"]["target_degree"],
            row["parameters"]["m"],
            row["parameters"]["n"],
        )
    )
    assert all(
        mp.mpf(row["best_bounded_search_component_margin"]) < 0
        for row in rows
    )
    assert all(
        mp.mpf(
            row["representative_mixed_candidate"][
                "leading_r_equals_one_measure_margin"
            ]
        )
        < 0
        for row in rows
    )
    explicit_aligned_anchor_count = sum(
        row["phase_aligned_Gaussian_fixed_lattice"][
            "explicit_tall_HNF_anchor_replayed_on_this_row"
        ]
        for row in rows
    )
    assert explicit_aligned_anchor_count == 1
    payload = {
        "schema": "root-unity-gaussian-global-saturation-certificate-v1",
        "dependencies": [
            {
                "path": str(ND_PATH.relative_to(ROOT)),
                "sha256": ND_SHA256,
                "hash_verified_before_import": True,
            },
            {
                "path": str(K2_PATH.relative_to(ROOT)),
                "sha256": K2_SHA256,
                "hash_verified_before_import": True,
            },
        ],
        "grid": {
            "m_values": [2, 3],
            "n_values": [4, 5, 6],
            "D_rule": "D=n so both parity tail spaces are nonzero",
            "target_degrees": [2, 3],
            "row_count": len(rows),
            "rows": rows,
            "all_unphased_glue_indices_are_powers_of_two": True,
            "all_unphased_quotient_invariants_are_one_or_two": True,
            "all_phase_aligned_real_doubled_lattices_are_saturated": True,
            "explicit_aligned_tall_HNF_anchor_count": explicit_aligned_anchor_count,
            "all_selected_component_and_mixed_leading_r_one_margins_negative": True,
            "finite_patterns_not_extrapolated": True,
        },
        "all_parameter_theorems_proved_in_source": {
            "full_unphased_parity_glue_quotient_is_killed_by_two": True,
            "phase_aligned_fixed_lattice_equals_direct_sum_of_separate_intrinsic_saturations": True,
            "no_one_plus_i_cross_saturation_survives_phase_alignment": True,
            "joint_endpoint_content_is_the_gcd_not_product_of_component_contents": True,
            "audited_absolute_coefficient_centered_majorant_of_a_mix_dominates_each_component": True,
            "joint_primitive_height_and_degree_dominate_each_component": True,
            "optimized_joint_measure_margin_is_no_larger_than_each_nonzero_component_margin": True,
            "allowing_a_zero_block_the_audited_coefficientwise_optimum_is_the_maximum_of_the_two_component_optima": True,
        },
        "logical_scope": {
            "exact": (
                "All global maps, tail kernels, ranks, HNF/Smith saturations, "
                "2-primary glue factors, fixed-lattice saturation indices, "
                "reflection identities, endpoint tails, contents, heights, "
                "degrees, and selected coefficient vectors are exact."
            ),
            "diagnostic": (
                "The bounded LLL-basis searches, optimized radii, logarithmic "
                "Schwarz bounds, values at pi, and finite negative margins are "
                "high-precision diagnostics and are not extrapolated."
            ),
            "remaining_survivor": (
                "The theorem removes only a cross-parity Gaussian-saturation "
                "gain. It does not rule out an exceptional short vector inside "
                "one separately saturated parity component."
            ),
            "not_classification": (
                "No all-parameter successive-minimum or content formula and no "
                "irrationality or transcendence conclusion is claimed."
            ),
        },
        "versions": {
            "python": sys.version,
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "python_flint": flint_version,
        },
        "peak_RSS_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(
        json.dumps(
            {
                "output": str(OUT),
                "rows": len(rows),
                "all_assertions_passed": True,
                "elapsed_seconds": round(time.perf_counter() - start, 6),
                "peak_rss_mib": round(peak_rss_kib / 1024, 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
