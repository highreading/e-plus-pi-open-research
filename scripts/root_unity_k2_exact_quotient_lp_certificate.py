#!/usr/bin/env python3
"""Exact rational quotient-L1 certificate in the saturated k=2 image.

The structural image and endpoint maps are rebuilt from frozen audited
dependencies.  No floating LP output is used.  A fixed rational parameter
vector supplies a primal feasible point for the weighted quotient LP at
(m,n,D,d,R)=(2,8,7,2,13).  Every endpoint, origin-jet, objective, clearing,
and descent assertion is checked over QQ or ZZ.

The recorded primal is deliberately not called optimal: an exact rational
descent direction proves that it is not.  Decimal logarithms are diagnostics
computed only after all exact claims have been established.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import resource
import time
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_k2_exact_quotient_lp_certificate.json"
ND_PATH = ROOT / "scripts" / "root_unity_nondecomposable_exterior_sum_certificate.py"
SAT_PATH = ROOT / "scripts" / "root_unity_k2_global_image_saturation_certificate.py"
ND_SHA256 = "3056828b21e08759fd7520c169db074aa9250c4e8bf4c8b6357c460881c3dd5f"
SAT_SHA256 = "588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470"
RSS_LIMIT_KIB = 2 * 1024 * 1024

M = 2
N = 8
D = 7
TARGET = 2
RADIUS = 13
ENDPOINT = [5441060864, 0, 551294727]

# This is a fixed exact primal parameter vector in the normalized
# endpoint-zero kernel basis reconstructed below.  It originated as the
# output of an exact-rational simplex probe, but replay correctness relies
# only on the independent exact feasibility checks below.
PRIMAL_PARAMETERS = [
    sp.Rational(0),
    sp.Rational(
        151798024238578057629735537,
        606009731260200151101440,
    ),
    sp.Rational(0),
    sp.Rational(
        4685630986875173551324361,
        891190781265000222208,
    ),
    sp.Rational(0),
    sp.Rational(0),
    sp.Rational(0),
    sp.Rational(
        20378849056113298751404833,
        1782381562530000444416,
    ),
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


assert sha256_file(ND_PATH) == ND_SHA256
assert sha256_file(SAT_PATH) == SAT_SHA256
nd = load_module("root_unity_quotient_nd_dependency", ND_PATH)
sat = load_module("root_unity_quotient_sat_dependency", SAT_PATH)


def rational_digest(values: list[sp.Rational]) -> str:
    text = ",".join(str(sp.cancel(value)) for value in values)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def integer_digest(values: list[int]) -> str:
    text = ",".join(str(value) for value in values)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def exact_space() -> dict:
    origin_order = M * (N + 1)
    moments = nd.logistic_moments(origin_order + N + 10)
    interpolation, beta, labels = nd.interpolation_data(
        M, N, D, moments
    )
    common_denominator = nd.universal_Q(M, N)
    corrected_map = nd.corrected_Q_map(
        beta, common_denominator, N, D
    )
    tail = nd.primitive_integer_rows(corrected_map[TARGET + 1 :, :])
    tail_kernel, tail_audit = nd.saturated_integer_kernel(tail)

    coordinate_pairs = list(itertools.combinations(range(D + 1), 2))
    remainders = nd.cleared_remainders(
        M,
        N,
        D,
        common_denominator,
        interpolation,
        labels,
        sp.eye(D + 1),
    )
    global_map = sp.Matrix(
        [
            [
                value
                for frequency in nd.exp_wronskian(
                    remainders[first], remainders[second]
                )
                for value in frequency
            ]
            for first, second in coordinate_pairs
        ]
    )
    lattice = sat.saturation_from_row_lattice(
        tail_kernel.transpose() * global_map
    )
    rows = lattice["saturated_lll"]
    assert rows.ncols() == (2 * M + 1) * (2 * N + 1)
    assert rows.nrows() == 11

    evaluation = sp.zeros(TARGET + 1, rows.ncols())
    for frequency in range(2 * M + 1):
        for degree in range(TARGET + 1):
            evaluation[
                degree,
                frequency * (2 * N + 1) + degree,
            ] = (-1) ** frequency
    row_matrix = sp.Matrix(
        [
            [int(rows[i, j]) for j in range(rows.ncols())]
            for i in range(rows.nrows())
        ]
    )
    endpoint_rows = row_matrix * evaluation.transpose()
    assert endpoint_rows.rank() == TARGET + 1

    full_endpoint = sat.endpoint_rows(rows, M, N)
    assert full_endpoint[:, : TARGET + 1] == endpoint_rows
    assert all(
        full_endpoint[i, degree] == 0
        for i in range(full_endpoint.rows)
        for degree in range(TARGET + 1, full_endpoint.cols)
    )

    pivots = endpoint_rows.transpose().rref()[1]
    assert pivots == (4, 7, 10)
    selected_endpoint = endpoint_rows[list(pivots), :]
    selected_global = row_matrix[list(pivots), :]
    right_inverse = selected_endpoint.inv() * selected_global
    assert right_inverse * evaluation.transpose() == sp.eye(TARGET + 1)

    coefficient_kernel, coefficient_kernel_audit = nd.saturated_integer_kernel(
        endpoint_rows.transpose()
    )
    assert coefficient_kernel.rows == rows.nrows()
    assert coefficient_kernel.cols == rows.nrows() - (TARGET + 1)
    raw_global_kernel = coefficient_kernel.transpose() * row_matrix
    kernel_lattice = sat.saturation_from_row_lattice(raw_global_kernel)
    global_kernel_flint = kernel_lattice["saturated_lll"]
    global_kernel = sp.Matrix(
        [
            [
                int(global_kernel_flint[i, j])
                for j in range(global_kernel_flint.ncols())
            ]
            for i in range(global_kernel_flint.nrows())
        ]
    )
    assert global_kernel.rows == 8
    assert global_kernel * evaluation.transpose() == sp.zeros(8, TARGET + 1)
    assert sp.Matrix.vstack(global_kernel, row_matrix).rank() == row_matrix.rank()

    kernel_heights = [
        max(abs(int(global_kernel[i, j])) for j in range(global_kernel.cols))
        for i in range(global_kernel.rows)
    ]
    normalized_kernel = sp.Matrix(
        [
            [
                sp.Rational(global_kernel[i, j], kernel_heights[i])
                for j in range(global_kernel.cols)
            ]
            for i in range(global_kernel.rows)
        ]
    )
    return {
        "rows": row_matrix,
        "evaluation": evaluation,
        "right_inverse": right_inverse,
        "normalized_kernel": normalized_kernel,
        "kernel_heights": kernel_heights,
        "tail_audit": tail_audit,
        "coefficient_kernel_audit": coefficient_kernel_audit,
        "global_lattice_rank": lattice["rank"],
        "kernel_lattice_rank": kernel_lattice["rank"],
    }


def exact_weights(slot_count: int) -> list[sp.Rational]:
    weights = []
    for slot in range(slot_count):
        frequency, degree = divmod(slot, 2 * N + 1)
        exponent = abs(frequency - M) * RADIUS
        weights.append(sp.Rational(11, 4) ** exponent * RADIUS**degree)
    return weights


def global_vector(
    base: list[sp.Rational],
    kernel: sp.Matrix,
    parameters: list[sp.Rational],
) -> list[sp.Rational]:
    return [
        sp.cancel(
            base[slot]
            + sum(
                parameters[row] * kernel[row, slot]
                for row in range(kernel.rows)
            )
        )
        for slot in range(kernel.cols)
    ]


def weighted_l1(
    values: list[sp.Rational], weights: list[sp.Rational]
) -> sp.Rational:
    return sp.cancel(
        sum(weight * abs(value) for weight, value in zip(weights, values))
    )


def verify_endpoint_and_origin(
    values: list[sp.Rational],
    evaluation: sp.Matrix,
    normalized_endpoint: list[sp.Rational],
) -> None:
    vector = sp.Matrix([values])
    assert vector * evaluation.transpose() == sp.Matrix([normalized_endpoint])

    # Verify the full endpoint tail directly, not merely through the
    # construction of the subspace.
    for degree in range(2 * N + 1):
        endpoint_coefficient = sum(
            (-1) ** frequency
            * values[frequency * (2 * N + 1) + degree]
            for frequency in range(2 * M + 1)
        )
        expected = (
            normalized_endpoint[degree]
            if degree <= TARGET
            else sp.S.Zero
        )
        assert endpoint_coefficient == expected

    zero_order = 2 * M * (N + 1)
    for order in range(zero_order):
        derivative = sp.S.Zero
        for frequency in range(2 * M + 1):
            centered_rate = frequency - M
            offset = frequency * (2 * N + 1)
            for degree in range(min(2 * N, order) + 1):
                derivative += (
                    values[offset + degree]
                    * (
                        math.factorial(order)
                        // math.factorial(order - degree)
                    )
                    * centered_rate ** (order - degree)
                )
        assert derivative == 0


def clearing_data(values: list[sp.Rational], endpoint_height: int) -> dict:
    denominator = sp.ilcm(*(sp.denom(value) for value in values))
    integral = [int(value * denominator) for value in values]
    content = math.gcd(*(abs(value) for value in integral))
    assert content > 0
    primitive = [value // content for value in integral]
    multiplier = sp.Rational(denominator, endpoint_height * content)
    assert multiplier.q == 1
    return {
        "common_denominator": int(denominator),
        "integral_content_before_primitive_division": content,
        "primitive_endpoint_multiplier": int(multiplier),
        "primitive_global_height": max(abs(value) for value in primitive),
        "primitive_global_sha256": integer_digest(primitive),
    }


def rational_record(value: sp.Rational) -> dict:
    value = sp.cancel(value)
    return {
        "numerator": str(value.p),
        "denominator": str(value.q),
        "numerator_decimal_digits": len(str(abs(value.p))),
        "denominator_decimal_digits": len(str(value.q)),
    }


def main() -> None:
    start = time.perf_counter()
    data = exact_space()
    endpoint_height = max(abs(value) for value in ENDPOINT)
    assert math.gcd(*(abs(value) for value in ENDPOINT)) == 1
    normalized_endpoint = [
        sp.Rational(value, endpoint_height) for value in ENDPOINT
    ]
    base = list(sp.Matrix([normalized_endpoint]) * data["right_inverse"])
    kernel = data["normalized_kernel"]
    assert kernel.rows == len(PRIMAL_PARAMETERS) == 8
    weights = exact_weights(len(base))

    primal = global_vector(base, kernel, PRIMAL_PARAMETERS)
    verify_endpoint_and_origin(
        primal, data["evaluation"], normalized_endpoint
    )
    primal_objective = weighted_l1(primal, weights)
    assert primal_objective == sp.Rational(
        102212534483868087453404545818076700280569125554185793217865588198917,
        4436907957595689369959657450411102340881842176000,
    )

    # The exact rational simplex probe which produced PRIMAL_PARAMETERS did
    # not emit a dual certificate.  In fact this point is strictly nonoptimal.
    # The one-sided directional derivative along -kernel row 6 is negative.
    descent_direction = [-kernel[6, slot] for slot in range(kernel.cols)]
    directional_derivative = sp.cancel(
        sum(
            weights[slot]
            * (
                sp.sign(primal[slot]) * descent_direction[slot]
                if primal[slot]
                else abs(descent_direction[slot])
            )
            for slot in range(len(primal))
        )
    )
    assert directional_derivative == sp.Rational(
        -39710900240730900314101,
        17036837675827200,
    )
    assert directional_derivative < 0
    first_break = min(
        abs(primal[slot] / descent_direction[slot])
        for slot in range(len(primal))
        if primal[slot] and descent_direction[slot]
    )
    epsilon = sp.cancel(first_break / 2)
    assert epsilon == sp.Rational(1655947907, 22954475520)
    descended = [
        sp.cancel(primal[slot] + epsilon * descent_direction[slot])
        for slot in range(len(primal))
    ]
    descended_parameters = list(PRIMAL_PARAMETERS)
    descended_parameters[6] -= epsilon
    assert descended == global_vector(base, kernel, descended_parameters)
    verify_endpoint_and_origin(
        descended, data["evaluation"], normalized_endpoint
    )
    descended_objective = weighted_l1(descended, weights)
    assert descended_objective == sp.Rational(
        91071368225125801171257449603880567839798794312328234796186781437463399,
        3953284990217759228634054788316292185725721378816000,
    )
    assert descended_objective < primal_objective
    assert (
        descended_objective - primal_objective
        == epsilon * directional_derivative
    )

    zero_order = 2 * M * (N + 1)
    schwarz_factor = sp.Rational(22, 7 * RADIUS) ** zero_order
    primal_normalized_bound = sp.cancel(primal_objective * schwarz_factor)
    primal_absolute_bound = sp.cancel(
        endpoint_height * primal_normalized_bound
    )
    descended_normalized_bound = sp.cancel(
        descended_objective * schwarz_factor
    )
    descended_absolute_bound = sp.cancel(
        endpoint_height * descended_normalized_bound
    )
    assert descended_absolute_bound < primal_absolute_bound
    assert descended_absolute_bound > 1
    assert descended_absolute_bound * endpoint_height**TARGET > 1

    primal_clearing = clearing_data(primal, endpoint_height)
    descended_clearing = clearing_data(descended, endpoint_height)
    assert primal_clearing["integral_content_before_primitive_division"] == 1
    assert descended_clearing["integral_content_before_primitive_division"] == 1
    assert primal_clearing["primitive_endpoint_multiplier"] == (
        6518378303365776642144000
    )
    assert descended_clearing["primitive_endpoint_multiplier"] == (
        645319452033211887572256000
    )

    mp.mp.dps = 100
    endpoint_value = abs(
        mp.fsum(
            mp.mpf(value) * (mp.j * mp.pi) ** degree
            for degree, value in enumerate(ENDPOINT)
        )
    )
    log_height = mp.log(endpoint_height)
    primal_log_bound = mp.log(primal_absolute_bound.p) - mp.log(
        primal_absolute_bound.q
    )
    descended_log_bound = mp.log(descended_absolute_bound.p) - mp.log(
        descended_absolute_bound.q
    )
    actual_theta = -mp.log(endpoint_value / endpoint_height) / log_height
    descended_theta = 1 - descended_log_bound / log_height
    measure_margin = -descended_log_bound - TARGET * log_height
    assert measure_margin < 0

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    payload = {
        "schema": "root-unity-k2-exact-rational-quotient-lp-v1",
        "dependencies": [
            {
                "path": str(ND_PATH.relative_to(ROOT)),
                "sha256": ND_SHA256,
                "verified_before_import": True,
            },
            {
                "path": str(SAT_PATH.relative_to(ROOT)),
                "sha256": SAT_SHA256,
                "verified_before_import": True,
            },
        ],
        "parameters": {
            "m": M,
            "n": N,
            "D": D,
            "target_degree": TARGET,
            "integer_radius": RADIUS,
            "common_origin_zero_order": zero_order,
        },
        "exact_affine_quotient": {
            "saturated_global_image_rank": data["global_lattice_rank"],
            "global_coefficient_slot_count": len(base),
            "endpoint_rank": TARGET + 1,
            "endpoint_zero_kernel_rank": data["kernel_lattice_rank"],
            "selected_right_inverse_row_indices": [4, 7, 10],
            "right_inverse_identity_verified_over_QQ": True,
            "endpoint_zero_kernel_verified_over_QQ": True,
            "endpoint_zero_kernel_spans_full_rational_kernel": True,
            "kernel_row_normalizing_heights": [
                str(value) for value in data["kernel_heights"]
            ],
            "tail_kernel_audit": data["tail_audit"],
            "coefficient_kernel_audit": data["coefficient_kernel_audit"],
        },
        "fixed_primitive_endpoint": {
            "coefficients": ENDPOINT,
            "height": str(endpoint_height),
            "content_one_verified": True,
            "absolute_value_decimal_diagnostic": mp.nstr(endpoint_value, 50),
            "actual_relative_exponent_decimal_diagnostic": mp.nstr(
                actual_theta, 40
            ),
        },
        "rational_circle_certificate": {
            "weight_formula": "(11/4)^(abs(frequency-m)*R)*R^degree",
            "uses_elementary_strict_bounds_e_lt_11_over_4_and_pi_lt_22_over_7": True,
            "all_weights_rational": True,
            "all_endpoint_and_origin_constraints_verified_exactly": True,
            "input_primal_is_a_rational_feasible_certificate": True,
            "input_primal_is_not_claimed_optimal": True,
            "input_primal_weighted_L1_objective": rational_record(
                primal_objective
            ),
            "input_primal_normalized_bound": rational_record(
                primal_normalized_bound
            ),
            "input_primal_absolute_bound": rational_record(
                primal_absolute_bound
            ),
            "input_primal_absolute_log_bound_decimal_diagnostic": mp.nstr(
                primal_log_bound, 50
            ),
            "input_primal_global_rational_sha256": rational_digest(primal),
            "input_primal_zero_coefficient_count": sum(
                value == 0 for value in primal
            ),
            "strict_descent_direction_kernel_row": 6,
            "strict_descent_directional_derivative": rational_record(
                directional_derivative
            ),
            "strict_descent_step": rational_record(epsilon),
            "strict_descent_objective_identity_verified": True,
            "descended_primal_is_strictly_better": True,
            "descended_primal_is_also_not_claimed_optimal": True,
            "descended_primal_weighted_L1_objective": rational_record(
                descended_objective
            ),
            "descended_primal_global_rational_sha256": rational_digest(
                descended
            ),
            "descended_normalized_bound": rational_record(
                descended_normalized_bound
            ),
            "descended_absolute_bound": rational_record(
                descended_absolute_bound
            ),
            "descended_absolute_log_bound_decimal_diagnostic": mp.nstr(
                descended_log_bound, 50
            ),
            "descended_bound_is_greater_than_one": True,
            "descended_certified_relative_exponent_decimal_diagnostic": mp.nstr(
                descended_theta, 40
            ),
            "strict_rank_one_degree_two_threshold": 3,
            "relative_threshold_not_met": True,
            "degree_two_measure_margin_decimal_diagnostic": mp.nstr(
                measure_margin, 50
            ),
            "degree_two_measure_margin_is_negative": True,
            "no_exact_dual_optimality_certificate": True,
        },
        "clearing_obstruction": {
            "input_primal": {
                **{
                    key: str(value)
                    for key, value in primal_clearing.items()
                    if key not in {
                        "primitive_global_sha256",
                    }
                },
                "primitive_global_sha256": primal_clearing[
                    "primitive_global_sha256"
                ],
            },
            "descended_primal": {
                **{
                    key: str(value)
                    for key, value in descended_clearing.items()
                    if key not in {
                        "primitive_global_sha256",
                    }
                },
                "primitive_global_sha256": descended_clearing[
                    "primitive_global_sha256"
                ],
            },
            "cheap_rational_normalization_acquires_huge_integer_endpoint_multiplier": True,
            "continuous_or_rational_quotient_cost_does_not_control_clearing_denominator": True,
        },
        "logical_scope": {
            "exact_primal_feasibility_is_not_exact_optimality": True,
            "floating_LP_results_are_not_used": True,
            "no_uniform_denominator_or_content_bound": True,
            "one_finite_row_is_not_an_asymptotic_theorem": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
        "peak_RSS_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUT),
                "elapsed_seconds": round(time.perf_counter() - start, 6),
                "peak_rss_mib": round(peak_rss_kib / 1024, 6),
                "all_assertions_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
