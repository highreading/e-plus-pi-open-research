#!/usr/bin/env python3
"""Replay the denominator-free Hardy endpoint quotient geometry.

The companion source proves that global-representative denominators are
irrelevant when the endpoint polynomial is already primitive integral, and
derives the exact two-dimensional evaluation coordinates.  This script:

* pins and imports the frozen Hardy-H2 and Gaussian-saturation constructors;
* checks the algebraic 2-by-2 normal-form identities symbolically;
* reconstructs the even saturated rows n=5,8,10 and the even reflection block
  at n=12;
* evaluates the quotient collapse parameters at the frozen diagnostic radii;
* checks the exact endpoint ranks and origin zeros in the dependencies; and
* repeats the Gram calculation at lower precision and shorter Taylor tail.

The decimal quotient matrices are stability diagnostics, not directed
interval enclosures.  The denominator theorem and normal-form identities are
proved in the companion source and do not depend on those decimals.
"""

from __future__ import annotations

import gc
import hashlib
import importlib.util
import itertools
import json
import math
import resource
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_hardy_endpoint_quotient_geometry_certificate.json"
)
HARDY_PATH = ROOT / "scripts" / "root_unity_hardy_h2_saturated_circle_certificate.py"
HARDY_SHA256 = "8cd98734331b75ea26990759c5d13a8d022065340feb1ef5cea4871452912b6b"
HARDY_SOURCE_PATH = ROOT / "sources" / "root_unity_hardy_h2_saturated_circle_audit.md"
HARDY_SOURCE_SHA256 = "24bc6c1e633118bec00659ed625d52266079555559c567e123d5d55943bc8a81"
GAUSSIAN_PATH = ROOT / "scripts" / "root_unity_gaussian_global_saturation_certificate.py"
GAUSSIAN_SHA256 = "89004cd7c35e890803f486f3a69036d21980497c718b75ad78be4441335e4f5a"
EMEASURE_SOURCE_PATH = ROOT / "sources" / "root_unity_gaussian_parity_mixing_barrier.md"
EMEASURE_SOURCE_SHA256 = "fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d"
QUOTIENT_LP_SOURCE_PATH = ROOT / "sources" / "root_unity_k2_exact_quotient_lp_audit.md"
QUOTIENT_LP_SOURCE_SHA256 = "070aa86143f9970c7925a07377fe1ff8f795992c8057e98505c6fc137f83f5e9"
WORK_DPS = 180
LOW_DPS = 120
FULL_TAIL = 240
SHORT_TAIL = 180
RSS_GUARD_KIB = 12 * 1024 * 1024

RADII = {
    5: "4.4248958951251394731309750864639720582140764725681",
    8: "4.9608883115562141734794136281519315667116159365528",
    10: "5.4329404060471230371159862935956298945155013192444",
    12: "5.0420477449039657",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_pinned(name: str, path: Path, digest: str):
    assert sha256_file(path) == digest
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


h2 = import_pinned("frozen_hardy_h2", HARDY_PATH, HARDY_SHA256)
gg = import_pinned("frozen_gaussian_saturation", GAUSSIAN_PATH, GAUSSIAN_SHA256)
assert sha256_file(HARDY_SOURCE_PATH) == HARDY_SOURCE_SHA256
assert sha256_file(EMEASURE_SOURCE_PATH) == EMEASURE_SOURCE_SHA256
assert sha256_file(QUOTIENT_LP_SOURCE_PATH) == QUOTIENT_LP_SOURCE_SHA256


def mp_string(value, digits: int = 60) -> str:
    return mp.nstr(value, digits)


def symbolic_normal_form_audit() -> dict:
    a, b, d, u, v = sp.symbols("a b d u v", nonzero=True)
    eta = b / a
    tau = (a * d - b**2) / a**2
    original = a * u**2 + 2 * b * u * v + d * v**2
    normal = a * ((u + eta * v) ** 2 + tau * v**2)
    assert sp.expand(original - normal) == 0
    assert sp.simplify(eta**2 + tau - d / a) == 0

    alpha = sp.symbols("alpha", real=True)
    c00, c02, c22 = sp.symbols("c00 c02 c22", real=True)
    C = sp.Matrix([[c00, c02], [c02, c22]])
    T = sp.Matrix([[1, alpha], [0, 1]])
    p = T * sp.Matrix([u, v])
    G = T.transpose() * C * T
    assert sp.expand((p.transpose() * C * p)[0] - (sp.Matrix([u, v]).transpose() * G * sp.Matrix([u, v]))[0]) == 0
    ell = sp.Matrix([1, -alpha])
    assert sp.expand((ell.transpose() * p)[0] - u) == 0

    # Completing in v gives the restricted-evaluation coefficient det(G)/G22.
    ga, gb, gd = sp.symbols("ga gb gd", nonzero=True)
    vv_star = -gb * u / gd
    completed_minimum = sp.expand(
        ga * u**2 + 2 * gb * u * vv_star + gd * vv_star**2
    )
    assert sp.simplify(completed_minimum - (ga * gd - gb**2) * u**2 / gd) == 0

    # One exact rational affine fiber illustrates that clearing changes the
    # endpoint scalar while the rational representative retains the endpoint.
    B = sp.Matrix([[1, 0], [0, 1], [1, 1]])
    endpoint = sp.Matrix([2, 3])
    rational_x = sp.Matrix([sp.Rational(3, 2), sp.Rational(5, 2), sp.Rational(1, 2)])
    assert B.transpose() * rational_x == endpoint
    clearing = sp.ilcm(*[term.q for term in rational_x])
    assert clearing == 2
    assert B.transpose() * (clearing * rational_x) == clearing * endpoint

    return {
        "coordinate_congruence_identity": True,
        "completed_square_identity": True,
        "epsilon_squared_equals_d_over_a": True,
        "restricted_evaluation_coefficient_is_determinant_over_G22": True,
        "rational_fiber_endpoint_is_exact": True,
        "integer_clearing_scales_endpoint_by_same_denominator": True,
    }


def n12_context(m: int, n: int, D: int) -> dict:
    M = m * (n + 1)
    moments = gg.nd.logistic_moments(M + n + 10)
    interpolation, beta, labels = gg.nd.interpolation_data(m, n, D, moments)
    common_denominator = gg.nd.universal_Q(m, n)
    corrected_map = gg.nd.corrected_Q_map(beta, common_denominator, n, D)
    pairs = list(itertools.combinations(range(D + 1), 2))
    remainders = gg.nd.cleared_remainders(
        m,
        n,
        D,
        common_denominator,
        interpolation,
        labels,
        sp.eye(D + 1),
    )
    global_rows = []
    for first, second in pairs:
        pair = gg.nd.exp_wronskian(remainders[first], remainders[second])
        global_rows.append([value for frequency in pair for value in frequency])
    return {
        "m": m,
        "n": n,
        "D": D,
        "nu": D + 1,
        "M": M,
        "Q": common_denominator,
        "corrected_map": corrected_map,
        "pairs": pairs,
        "global_map": sp.Matrix(global_rows),
    }


def hardy_object_from_even_basis(n: int, D: int, basis: sp.Matrix):
    """Build the numeric Hardy wrapper after an exact even-block saturation."""
    obj = h2.SaturatedHardyRow.__new__(h2.SaturatedHardyRow)
    obj.m = 2
    obj.n = n
    obj.target_degree = 2
    obj.D = D
    obj.nu = D + 1
    obj.M = 2 * (n + 1)
    obj.zero_order = 2 * obj.M
    obj.global_degree = 2 * n
    obj.basis = basis
    obj.rank = basis.nrows()
    obj.slot_count = basis.ncols()
    obj.endpoint_matrix = gg.k2.endpoint_rows(basis, obj.m, n)
    assert all(
        obj.endpoint_matrix[row, degree] == 0
        for row in range(obj.rank)
        for degree in range(1, obj.endpoint_matrix.cols, 2)
    )
    assert all(
        obj.endpoint_matrix[row, degree] == 0
        for row in range(obj.rank)
        for degree in range(3, obj.endpoint_matrix.cols)
    )
    assert int(obj.endpoint_matrix[:, [0, 2]].rank()) == 2

    obj.scales = [
        max(abs(int(basis[row, column])) for column in range(obj.slot_count))
        for row in range(obj.rank)
    ]
    obj.row_squared_norms = [
        sum(int(basis[row, column]) ** 2 for column in range(obj.slot_count))
        for row in range(obj.rank)
    ]

    maximum_order = obj.zero_order + FULL_TAIL
    factorials = [math.factorial(j) for j in range(maximum_order + 1)]
    obj.origin_derivatives = []
    cancellation_digits = 0
    for row in range(obj.rank):
        derivatives = []
        for order in range(maximum_order + 1):
            summands = []
            for frequency in range(2 * obj.m + 1):
                rate = frequency - obj.m
                offset = frequency * (obj.global_degree + 1)
                for degree in range(min(obj.global_degree, order) + 1):
                    coefficient = int(basis[row, offset + degree])
                    if coefficient:
                        summands.append(
                            coefficient
                            * factorials[order]
                            // factorials[order - degree]
                            * rate ** (order - degree)
                        )
            value = sum(summands)
            if order < obj.zero_order and summands:
                cancellation_digits = max(
                    cancellation_digits,
                    len(str(max(abs(term) for term in summands))),
                )
            derivatives.append(value)
        assert all(value == 0 for value in derivatives[: obj.zero_order])
        assert any(derivatives[obj.zero_order :])
        obj.origin_derivatives.append(derivatives)
    obj.exact_zero_cancellation_summand_decimal_digits = cancellation_digits

    obj.endpoint_basis = mp.matrix(obj.rank, 2)
    for row in range(obj.rank):
        obj.endpoint_basis[row, 0] = (
            mp.mpf(int(obj.endpoint_matrix[row, 0])) / obj.scales[row]
        )
        obj.endpoint_basis[row, 1] = (
            mp.mpf(int(obj.endpoint_matrix[row, 2])) / obj.scales[row]
        )
    return obj


def build_row(n: int):
    if n in (5, 8, 10):
        return h2.SaturatedHardyRow(n), "complete_minimal_endpoint_image"
    assert n == 12
    context = n12_context(2, 12, 6)
    even_block = gg.parity_block(context, 2, 0)
    return (
        hardy_object_from_even_basis(12, 6, even_block["saturated_lll"]),
        "separately_saturated_even_reflection_block",
    )


def quotient_matrix(row, radius: mp.mpf, tail: int) -> tuple[mp.matrix, mp.matrix]:
    gram = row.quotient_gram(radius, tail)
    inverse_times_endpoint = h2.solve_matrix(gram, row.endpoint_basis)
    dual = row.endpoint_basis.transpose() * inverse_times_endpoint
    quotient = dual ** -1
    return quotient, gram


def geometry_metrics(row, radius_text: str, tail: int) -> dict:
    radius = mp.mpf(radius_text)
    quotient, gram = quotient_matrix(row, radius, tail)
    alpha = mp.pi**2
    transform = mp.matrix([[1, alpha], [0, 1]])
    evaluation_coordinates = transform.transpose() * quotient * transform
    a = evaluation_coordinates[0, 0]
    b = evaluation_coordinates[0, 1]
    d = evaluation_coordinates[1, 1]
    determinant = mp.det(evaluation_coordinates)
    eta = b / a
    tau = determinant / a**2
    epsilon_squared = d / a
    epsilon = mp.sqrt(epsilon_squared)
    assert a > 0 and d > 0 and determinant > 0 and tau > 0
    assert abs(epsilon_squared - (eta**2 + tau)) < mp.mpf("1e-90")

    hardy_floor = (1 - (mp.pi / radius) ** 2) / mp.pi ** (2 * row.zero_order)
    restricted_floor = determinant / d
    floor_ratio = restricted_floor / hardy_floor
    assert floor_ratio > 1

    # Directly test the pointwise reverse-triangle inequality on exact integer
    # samples using the numerically formed positive quotient matrix.
    maximum_normalized_inequality_residual = mp.mpf(0)
    for p0, p2 in [(1, 1), (10, 1), (987, 100), (27262976, 2762317)]:
        endpoint = mp.matrix([p0, p2])
        q_squared = (endpoint.transpose() * quotient * endpoint)[0]
        u = mp.mpf(p0) - alpha * p2
        residual = abs(mp.sqrt(q_squared / a) - abs(u)) - epsilon * abs(p2)
        maximum_normalized_inequality_residual = max(
            maximum_normalized_inequality_residual, residual
        )
        assert residual < mp.mpf("1e-80")

    return {
        "radius": mp_string(radius, 60),
        "quotient_matrix_C": [
            [mp_string(quotient[row_index, column], 80) for column in range(2)]
            for row_index in range(2)
        ],
        "evaluation_coordinate_matrix_G_over_a": [
            [
                mp_string(evaluation_coordinates[row_index, column] / a, 80)
                for column in range(2)
            ]
            for row_index in range(2)
        ],
        "a": mp_string(a, 80),
        "eta": mp_string(eta, 80),
        "tau": mp_string(tau, 80),
        "epsilon_squared_equals_d_over_a": mp_string(epsilon_squared, 80),
        "epsilon": mp_string(epsilon, 80),
        "restricted_evaluation_floor_over_full_Hardy_floor": mp_string(
            floor_ratio, 80
        ),
        "maximum_reverse_triangle_residual": mp_string(
            maximum_normalized_inequality_residual, 20
        ),
        "gram_log10_condition_number": mp_string(
            mp.log10(mp.cond(gram)), 50
        ),
    }


def relative_decimal_difference(first: str, second: str) -> mp.mpf:
    x = mp.mpf(first)
    y = mp.mpf(second)
    return abs(x - y) / max(abs(x), abs(y), mp.mpf("1e-300"))


def finite_row(n: int) -> dict:
    row, construction = build_row(n)
    assert int(row.endpoint_matrix[:, [0, 2]].rank()) == 2
    assert all(
        row.endpoint_matrix[row_index, degree] == 0
        for row_index in range(row.rank)
        for degree in range(1, row.endpoint_matrix.cols)
        if degree != 2
    )
    with mp.workdps(WORK_DPS):
        high = geometry_metrics(row, RADII[n], FULL_TAIL)
    with mp.workdps(LOW_DPS):
        low = geometry_metrics(row, RADII[n], SHORT_TAIL)

    stable_keys = [
        "a",
        "eta",
        "tau",
        "epsilon_squared_equals_d_over_a",
        "restricted_evaluation_floor_over_full_Hardy_floor",
    ]
    differences = {
        key: mp_string(relative_decimal_difference(high[key], low[key]), 20)
        for key in stable_keys
    }
    maximum_difference = max(mp.mpf(value) for value in differences.values())
    assert maximum_difference < mp.mpf("1e-70")

    output = {
        "n": n,
        "D": row.D,
        "rank": row.rank,
        "zero_order_K": row.zero_order,
        "construction": construction,
        "endpoint_rank_is_two_exactly": True,
        "only_endpoint_degrees_zero_and_two_survive_exactly": True,
        "all_origin_derivatives_below_K_vanish_exactly": True,
        "largest_exact_cancelling_summand_decimal_digits": (
            row.exact_zero_cancellation_summand_decimal_digits
        ),
        "high_precision_full_tail": high,
        "short_tail_low_precision_relative_differences": differences,
        "maximum_stability_relative_difference": mp_string(maximum_difference, 20),
    }
    del row
    gc.collect()
    return output


def main() -> None:
    mp.mp.dps = WORK_DPS
    exact_audit = symbolic_normal_form_audit()
    rows = [finite_row(n) for n in (5, 8, 10, 12)]

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB
    output = {
        "title": "Denominator-free Hardy endpoint quotient geometry",
        "parameters": {
            "m": 2,
            "target_endpoint_degrees": [0, 2],
            "n_values": [5, 8, 10, 12],
            "working_decimal_digits": WORK_DPS,
            "low_precision_decimal_digits": LOW_DPS,
            "full_post_zero_Taylor_tail": FULL_TAIL,
            "short_post_zero_Taylor_tail": SHORT_TAIL,
            "memory_guard_MiB": RSS_GUARD_KIB // 1024,
        },
        "dependencies": {
            str(HARDY_PATH.relative_to(ROOT)): HARDY_SHA256,
            str(HARDY_SOURCE_PATH.relative_to(ROOT)): HARDY_SOURCE_SHA256,
            str(GAUSSIAN_PATH.relative_to(ROOT)): GAUSSIAN_SHA256,
            str(EMEASURE_SOURCE_PATH.relative_to(ROOT)): EMEASURE_SOURCE_SHA256,
            str(QUOTIENT_LP_SOURCE_PATH.relative_to(ROOT)): QUOTIENT_LP_SOURCE_SHA256,
        },
        "exact_symbolic_audit": exact_audit,
        "exact_theorem_scope": {
            "common_origin_zero_is_a_complex_linear_subspace": True,
            "endpoint_identity_extends_to_real_and_complex_coefficients": True,
            "full_rational_endpoint_rank_makes_every_rational_endpoint_attainable": True,
            "real_Hardy_minimizer_is_analytically_admissible": True,
            "rational_points_in_exact_fiber_have_same_infimum": True,
            "global_denominator_clearing_is_not_required_for_endpoint_e_measure": True,
            "two_by_two_evaluation_normal_form": True,
            "primitive_endpoint_approximation_equivalence": True,
            "generic_exponent_two_not_strictly_improved_by_geometry_alone": True,
        },
        "finite_rows": rows,
        "finite_decimal_scope": {
            "high_precision_values_are_not_directed_intervals": True,
            "finite_collapse_is_not_an_asymptotic_theorem": True,
            "no_claim_of_irrationality_or_transcendence": True,
        },
    }
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
