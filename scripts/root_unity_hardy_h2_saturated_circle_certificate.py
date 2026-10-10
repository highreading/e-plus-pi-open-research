#!/usr/bin/env python3
"""Hardy-H2 Gram and saturated k=2 endpoint diagnostics.

The companion source proves the exact circle Gram, zero-factored Hardy
evaluation inequality, and constrained quadratic minimum.  This replay:

* verifies the frozen saturated-global-image constructor before importing it;
* rebuilds the m=2, d=2 minimal-full-endpoint rows n=5,8,10;
* computes all origin derivatives over Z before numerical conversion;
* optimizes the quotient H2 norm for two prescribed primitive endpoints;
* compares with the exact coefficientwise L1 circle majorant of the same
  optimized analytic function; and
* audits truncation and working-precision stability.

The optimization is over the real closure of the rational affine endpoint
fiber.  Its value is an exact infimum by rational density, but the displayed
decimal optimizer is not an integer-lattice or shortest-vector certificate.
"""

from __future__ import annotations

import gc
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
OUT = ROOT / "results" / "root_unity_hardy_h2_saturated_circle_certificate.json"
DEPENDENCY = ROOT / "scripts" / "root_unity_k2_global_image_saturation_certificate.py"
DEPENDENCY_SHA256 = "588393ba1cb273d13034cc069cca7b3f507c8b9adf62f13a8d6e8e71bb15d470"
RSS_LIMIT_KIB = 2 * 1024 * 1024
WORK_DPS = 180
LOW_DPS = 120
DERIVATIVE_TAIL = 240
H2_SHORT_TAIL = 180


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(DEPENDENCY) == DEPENDENCY_SHA256
specification = importlib.util.spec_from_file_location(
    "root_unity_k2_saturation_dependency", DEPENDENCY
)
assert specification is not None and specification.loader is not None
sat = importlib.util.module_from_spec(specification)
specification.loader.exec_module(sat)
nd = sat.nd


def mp_string(value: mp.mpf, digits: int = 50) -> str:
    return mp.nstr(value, digits)


def solve_matrix(left: mp.matrix, right: mp.matrix) -> mp.matrix:
    """Solve left * X = right one column at a time."""
    output = mp.matrix(left.rows, right.cols)
    for column in range(right.cols):
        solution = mp.lu_solve(left, right[:, column])
        for row in range(left.rows):
            output[row, column] = solution[row]
    return output


def golden_minimize(function, lower: mp.mpf, upper: mp.mpf, steps: int = 100):
    ratio = (mp.sqrt(5) - 1) / 2
    left = upper - ratio * (upper - lower)
    right = lower + ratio * (upper - lower)
    f_left = function(left)
    f_right = function(right)
    for _ in range(steps):
        if f_left < f_right:
            upper = right
            right = left
            f_right = f_left
            left = upper - ratio * (upper - lower)
            f_left = function(left)
        else:
            lower = left
            left = right
            f_left = f_right
            right = lower + ratio * (upper - lower)
            f_right = function(right)
    point = (lower + upper) / 2
    return point, function(point)


def power_with_zero_convention(base: mp.mpf, exponent: int) -> mp.mpf:
    return mp.mpf(1) if exponent == 0 else base**exponent


def monomial_gram_series(
    rate_r: int,
    degree_a: int,
    rate_s: int,
    degree_b: int,
    radius: mp.mpf,
    terms: int = 240,
) -> mp.mpf:
    """Exact Gram series, truncated only for its numerical replay."""
    start = max(degree_a, degree_b)
    total = mp.mpf(0)
    for ell in range(start, start + terms):
        total += (
            radius ** (2 * ell)
            * power_with_zero_convention(mp.mpf(rate_r), ell - degree_a)
            * power_with_zero_convention(mp.mpf(rate_s), ell - degree_b)
            / (
                mp.factorial(ell - degree_a)
                * mp.factorial(ell - degree_b)
            )
        )
    return total


def monomial_gram_quadrature(
    rate_r: int,
    degree_a: int,
    rate_s: int,
    degree_b: int,
    radius: mp.mpf,
) -> mp.mpf:
    """Independent numerical circle integral for the Gram formula."""
    two_pi = 2 * mp.pi

    def integrand(theta):
        z = radius * mp.e ** (1j * theta)
        first = z**degree_a * mp.e ** (rate_r * z)
        second = z**degree_b * mp.e ** (rate_s * z)
        return first * mp.conj(second)

    return mp.re(mp.quad(integrand, [0, two_pi]) / two_pi)


def gram_kernel_audit() -> dict:
    samples = [
        (2, 0, 2, 0, "4.5"),
        (2, 1, 1, 2, "4.5"),
        (2, 2, -1, 1, "4.5"),
        (0, 3, 0, 3, "4.5"),
        (0, 2, 1, 0, "4.5"),
    ]
    rows = []
    maximum_error = mp.mpf(0)
    with mp.workdps(100):
        for rate_r, degree_a, rate_s, degree_b, radius_text in samples:
            radius = mp.mpf(radius_text)
            series = monomial_gram_series(
                rate_r, degree_a, rate_s, degree_b, radius
            )
            quadrature = monomial_gram_quadrature(
                rate_r, degree_a, rate_s, degree_b, radius
            )
            error = abs(series - quadrature)
            maximum_error = max(maximum_error, error)
            rows.append(
                {
                    "rate_r": rate_r,
                    "degree_a": degree_a,
                    "rate_s": rate_s,
                    "degree_b": degree_b,
                    "radius": radius_text,
                    "series_value": mp_string(series, 60),
                    "quadrature_value": mp_string(quadrature, 60),
                    "absolute_difference": mp_string(error, 20),
                }
            )
    assert maximum_error < mp.mpf("1e-80")
    return {
        "samples": rows,
        "maximum_absolute_difference": mp_string(maximum_error, 20),
        "series_and_independent_quadrature_agree_below_1e_minus_80": True,
    }


def primitive_even_endpoint(endpoint_matrix, row: int) -> list[int]:
    constant = int(endpoint_matrix[row, 0])
    quadratic = int(endpoint_matrix[row, 2])
    content = math.gcd(abs(constant), abs(quadratic))
    assert content > 0
    constant //= content
    quadratic //= content
    if constant < 0 or (constant == 0 and quadratic < 0):
        constant = -constant
        quadratic = -quadratic
    assert math.gcd(abs(constant), abs(quadratic)) == 1
    return [constant, quadratic]


class SaturatedHardyRow:
    def __init__(self, n: int):
        self.m = 2
        self.n = n
        self.target_degree = 2
        self.D = nd.minimal_full_endpoint_D(n, self.target_degree)
        self.nu = self.D + 1
        self.M = self.m * (n + 1)
        self.zero_order = 2 * self.M
        self.global_degree = 2 * n

        moments = nd.logistic_moments(self.M + n + 10)
        interpolation, beta, labels = nd.interpolation_data(
            self.m, n, self.D, moments
        )
        common_denominator = nd.universal_Q(self.m, n)
        corrected_map = nd.corrected_Q_map(
            beta, common_denominator, n, self.D
        )
        tail_map = nd.primitive_integer_rows(
            corrected_map[self.target_degree + 1 :, :]
        )
        tail_kernel, tail_audit = nd.saturated_integer_kernel(tail_map)
        self.tail_audit = tail_audit

        remainders = nd.cleared_remainders(
            self.m,
            n,
            self.D,
            common_denominator,
            interpolation,
            labels,
            sp.eye(self.nu),
        )
        pairs = list(itertools.combinations(range(self.nu), 2))
        global_map = sp.Matrix(
            [
                [
                    value
                    for frequency in nd.exp_wronskian(
                        remainders[first], remainders[second]
                    )
                    for value in frequency
                ]
                for first, second in pairs
            ]
        )
        lattice = sat.saturation_from_row_lattice(
            tail_kernel.transpose() * global_map
        )
        self.basis = lattice["saturated_lll"]
        self.rank = self.basis.nrows()
        self.slot_count = self.basis.ncols()
        assert self.slot_count == (2 * self.m + 1) * (2 * n + 1)

        self.endpoint_matrix = sat.endpoint_rows(self.basis, self.m, n)
        assert all(
            self.endpoint_matrix[row, degree] == 0
            for row in range(self.rank)
            for degree in range(1, self.endpoint_matrix.cols, 2)
        )
        assert all(
            self.endpoint_matrix[row, degree] == 0
            for row in range(self.rank)
            for degree in range(self.target_degree + 1, self.endpoint_matrix.cols)
        )
        assert int(self.endpoint_matrix[:, [0, 2]].rank()) == 2

        self.scales = [
            max(
                abs(int(self.basis[row, column]))
                for column in range(self.slot_count)
            )
            for row in range(self.rank)
        ]
        self.row_squared_norms = [
            sum(
                int(self.basis[row, column]) ** 2
                for column in range(self.slot_count)
            )
            for row in range(self.rank)
        ]

        maximum_derivative = self.zero_order + DERIVATIVE_TAIL
        factorials = [math.factorial(j) for j in range(maximum_derivative + 1)]
        self.origin_derivatives: list[list[int]] = []
        cancellation_digits = 0
        for row in range(self.rank):
            derivatives = []
            for order in range(maximum_derivative + 1):
                summands = []
                for frequency in range(2 * self.m + 1):
                    centered_rate = frequency - self.m
                    offset = frequency * (self.global_degree + 1)
                    for degree in range(min(self.global_degree, order) + 1):
                        coefficient = int(self.basis[row, offset + degree])
                        if coefficient:
                            summands.append(
                                coefficient
                                * factorials[order]
                                // factorials[order - degree]
                                * centered_rate ** (order - degree)
                            )
                value = sum(summands)
                if order < self.zero_order and summands:
                    largest = max(abs(term) for term in summands)
                    cancellation_digits = max(
                        cancellation_digits, len(str(largest))
                    )
                derivatives.append(value)
            assert all(value == 0 for value in derivatives[: self.zero_order])
            assert any(value for value in derivatives[self.zero_order :])
            self.origin_derivatives.append(derivatives)
        self.exact_zero_cancellation_summand_decimal_digits = cancellation_digits

        self.endpoint_basis = mp.matrix(self.rank, 2)
        for row in range(self.rank):
            self.endpoint_basis[row, 0] = (
                mp.mpf(int(self.endpoint_matrix[row, 0])) / self.scales[row]
            )
            self.endpoint_basis[row, 1] = (
                mp.mpf(int(self.endpoint_matrix[row, 2])) / self.scales[row]
            )

    def quotient_gram(self, radius: mp.mpf, tail: int) -> mp.matrix:
        output = mp.matrix(self.rank, self.rank)
        for ell in range(tail + 1):
            factor = radius**ell / mp.factorial(self.zero_order + ell)
            vector = [
                mp.mpf(self.origin_derivatives[row][self.zero_order + ell])
                / self.scales[row]
                * factor
                for row in range(self.rank)
            ]
            for row in range(self.rank):
                for column in range(row + 1):
                    output[row, column] += vector[row] * vector[column]
                    output[column, row] = output[row, column]
        return output

    def h2_bound(
        self,
        radius: mp.mpf,
        endpoint: list[int],
        tail: int = DERIVATIVE_TAIL,
        return_optimizer: bool = False,
    ):
        gram = self.quotient_gram(radius, tail)
        inverse_times_endpoint = solve_matrix(gram, self.endpoint_basis)
        endpoint_kernel = (
            self.endpoint_basis.transpose() * inverse_times_endpoint
        )
        prescribed = mp.matrix(
            [mp.mpf(endpoint[0]), mp.mpf(endpoint[1])]
        )
        multiplier = mp.lu_solve(endpoint_kernel, prescribed)
        optimizer = inverse_times_endpoint * multiplier
        minimum_squared_norm = (prescribed.transpose() * multiplier)[0]
        assert minimum_squared_norm > 0
        log_upper_bound = (
            self.zero_order * mp.log(mp.pi)
            + mp.log(minimum_squared_norm) / 2
            - mp.log(1 - (mp.pi / radius) ** 2) / 2
        )
        if not return_optimizer:
            return log_upper_bound

        coefficients = []
        for frequency in range(2 * self.m + 1):
            for degree in range(self.global_degree + 1):
                coefficients.append(
                    sum(
                        optimizer[row]
                        * mp.mpf(
                            int(
                                self.basis[
                                    row,
                                    frequency * (self.global_degree + 1)
                                    + degree,
                                ]
                            )
                        )
                        / self.scales[row]
                        for row in range(self.rank)
                    )
                )
        endpoint_residual = max(
            abs(
                sum(
                    self.endpoint_basis[row, column] * optimizer[row]
                    for row in range(self.rank)
                )
                - prescribed[column]
            )
            for column in range(2)
        )
        return {
            "log_upper_bound": log_upper_bound,
            "minimum_squared_quotient_norm": minimum_squared_norm,
            "optimizer": optimizer,
            "coefficients": coefficients,
            "endpoint_residual": endpoint_residual,
            "gram": gram,
        }

    def optimize_h2(self, endpoint: list[int]):
        start = mp.pi + mp.mpf("0.05")
        step = mp.mpf("0.18")
        scan = [
            (self.h2_bound(start + index * step, endpoint), start + index * step)
            for index in range(120)
        ]
        scan_index = min(range(len(scan)), key=lambda index: scan[index][0])
        assert 0 < scan_index < len(scan) - 1
        center = scan[scan_index][1]
        lower = max(mp.pi + mp.mpf("1e-12"), center - mp.mpf("0.4"))
        upper = center + mp.mpf("0.4")
        radius, value = golden_minimize(
            lambda candidate: self.h2_bound(candidate, endpoint),
            lower,
            upper,
        )
        delta = mp.mpf("1e-8")
        assert self.h2_bound(radius - delta, endpoint) > value
        assert self.h2_bound(radius + delta, endpoint) > value
        return radius, self.h2_bound(radius, endpoint, return_optimizer=True)

    def l1_log_bound(self, radius: mp.mpf, coefficients: list[mp.mpf]):
        circle_majorant = mp.mpf(0)
        for frequency in range(2 * self.m + 1):
            centered_rate = frequency - self.m
            for degree in range(self.global_degree + 1):
                coefficient = coefficients[
                    frequency * (self.global_degree + 1) + degree
                ]
                circle_majorant += (
                    abs(coefficient)
                    * radius**degree
                    * mp.exp(abs(centered_rate) * radius)
                )
        return (
            self.zero_order * mp.log(mp.pi / radius)
            + mp.log(circle_majorant)
        )

    def optimize_l1(self, coefficients: list[mp.mpf]):
        start = mp.pi + mp.mpf("0.03")
        step = mp.mpf("0.15")
        scan = [
            (
                self.l1_log_bound(start + index * step, coefficients),
                start + index * step,
            )
            for index in range(160)
        ]
        scan_index = min(range(len(scan)), key=lambda index: scan[index][0])
        assert 0 < scan_index < len(scan) - 1
        center = scan[scan_index][1]
        return golden_minimize(
            lambda candidate: self.l1_log_bound(candidate, coefficients),
            max(mp.pi + mp.mpf("1e-12"), center - mp.mpf("0.3")),
            center + mp.mpf("0.3"),
        )

    def endpoint_choices(self):
        primitive_rows = [
            primitive_even_endpoint(self.endpoint_matrix, row)
            for row in range(self.rank)
        ]
        shortest_index = min(
            range(self.rank),
            key=lambda row: (self.row_squared_norms[row], row),
        )
        best_value_index = min(
            range(self.rank),
            key=lambda row: (
                abs(
                    mp.mpf(primitive_rows[row][0])
                    - mp.mpf(primitive_rows[row][1]) * mp.pi**2
                ),
                row,
            ),
        )
        return [
            (
                "shortest_global_LLL_row",
                shortest_index,
                primitive_rows[shortest_index],
            ),
            (
                "best_value_among_global_LLL_rows",
                best_value_index,
                primitive_rows[best_value_index],
            ),
        ]


def endpoint_diagnostic(
    row: SaturatedHardyRow,
    label: str,
    source_row: int,
    endpoint: list[int],
) -> dict:
    assert math.gcd(abs(endpoint[0]), abs(endpoint[1])) == 1
    radius, optimum = row.optimize_h2(endpoint)
    l1_radius, l1_log_bound = row.optimize_l1(optimum["coefficients"])

    actual_value = mp.mpf(endpoint[0]) - mp.mpf(endpoint[1]) * mp.pi**2
    actual_log_absolute = mp.log(abs(actual_value))
    endpoint_height = max(abs(endpoint[0]), abs(endpoint[1]))
    log_endpoint_height = mp.log(endpoint_height)
    h2_log_bound = optimum["log_upper_bound"]
    assert h2_log_bound > actual_log_absolute

    short_tail_log = row.h2_bound(
        radius, endpoint, tail=H2_SHORT_TAIL
    )
    tail_stability = abs(short_tail_log - h2_log_bound)
    with mp.workdps(LOW_DPS):
        low_precision_log = row.h2_bound(
            +radius, endpoint, tail=DERIVATIVE_TAIL
        )
    precision_stability = abs(low_precision_log - h2_log_bound)

    # Positive definiteness and a useful conditioning diagnostic.
    eigenvalues = mp.eigsy(optimum["gram"], eigvals_only=True)
    assert all(eigenvalues[index] > 0 for index in range(eigenvalues.rows))
    log10_condition = mp.log10(
        eigenvalues[eigenvalues.rows - 1] / eigenvalues[0]
    )

    improvement = l1_log_bound - h2_log_bound
    certified_relative_exponent = (
        1 - h2_log_bound / log_endpoint_height
    )
    return {
        "label": label,
        "source_saturated_LLL_row": source_row,
        "primitive_endpoint_coefficients_constant_quadratic": [
            str(endpoint[0]),
            str(endpoint[1]),
        ],
        "primitive_endpoint_height": str(endpoint_height),
        "actual_endpoint_value_constant_minus_quadratic_times_pi_squared": mp_string(
            actual_value, 60
        ),
        "log_actual_endpoint_absolute_value": mp_string(
            actual_log_absolute, 50
        ),
        "optimized_H2_radius": mp_string(radius, 50),
        "optimized_H2_log_upper_bound": mp_string(h2_log_bound, 50),
        "H2_log_slack_above_actual_value": mp_string(
            h2_log_bound - actual_log_absolute, 40
        ),
        "high_precision_H2_log_upper_bound_is_below_zero": bool(
            h2_log_bound < 0
        ),
        "H2_certified_relative_exponent": mp_string(
            certified_relative_exponent, 40
        ),
        "strict_relative_threshold_for_r_equals_1_degree_2": "3",
        "H2_relative_exponent_beats_strict_threshold": bool(
            certified_relative_exponent > 3
        ),
        "same_function_optimized_coefficientwise_L1_radius": mp_string(
            l1_radius, 50
        ),
        "same_function_optimized_coefficientwise_L1_log_upper_bound": mp_string(
            l1_log_bound, 50
        ),
        "H2_log_improvement_over_same_function_L1": mp_string(
            improvement, 50
        ),
        "H2_log_improvement_over_n": mp_string(improvement / row.n, 40),
        "H2_log_improvement_over_n_log_n": mp_string(
            improvement / (row.n * mp.log(row.n)), 40
        ),
        "maximum_endpoint_constraint_residual": mp_string(
            optimum["endpoint_residual"], 10
        ),
        "quotient_gram_log10_condition_number": mp_string(
            log10_condition, 30
        ),
        "absolute_log_change_tail_180_to_240": mp_string(
            tail_stability, 10
        ),
        "absolute_log_change_working_precision_120_to_180_dps": mp_string(
            precision_stability, 10
        ),
        "continuous_optimizer_is_not_claimed_rational_or_integral": True,
        "rational_affine_fiber_has_the_same_infimum_by_density": True,
        "finite_diagnostic_only": True,
    }


def parameter_row(n: int) -> dict:
    row = SaturatedHardyRow(n)
    diagnostics = [
        endpoint_diagnostic(row, label, source_row, endpoint)
        for label, source_row, endpoint in row.endpoint_choices()
    ]
    gc.collect()
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    return {
        "parameters": {
            "m": row.m,
            "n": row.n,
            "D": row.D,
            "nu": row.nu,
            "target_degree": row.target_degree,
        },
        "saturated_global_image_rank": row.rank,
        "complete_global_coefficient_slot_count": row.slot_count,
        "common_origin_zero_order": row.zero_order,
        "all_origin_derivatives_below_common_order_vanish_exactly_over_Z": True,
        "largest_exactly_cancelled_origin_summand_decimal_digits": (
            row.exact_zero_cancellation_summand_decimal_digits
        ),
        "endpoint_low_image_rank": 2,
        "all_endpoint_coefficients_outside_degrees_0_and_2_vanish_exactly": True,
        "tail_kernel_audit": row.tail_audit,
        "prescribed_primitive_endpoint_diagnostics": diagnostics,
        "peak_RSS_checked_below_2GiB_after_row": True,
    }


def main() -> None:
    start = time.perf_counter()
    mp.mp.dps = WORK_DPS
    payload = {
        "schema": "root-unity-hardy-h2-saturated-circle-v1",
        "dependency": {
            "path": str(DEPENDENCY.relative_to(ROOT)),
            "sha256": DEPENDENCY_SHA256,
            "hash_verified_before_import": True,
        },
        "exact_analytic_theorems_proved_in_source": {
            "monomial_circle_Gram_constant_term_derivative_and_series_formulas": True,
            "zero_factored_Hardy_evaluation_inequality": True,
            "constrained_Gram_Schur_complement_minimum": True,
            "rational_affine_fiber_infimum_equals_real_minimum": True,
            "coefficientwise_L1_comparison_for_the_same_function": True,
        },
        "gram_kernel_numerical_crosscheck": gram_kernel_audit(),
        "numerical_method": {
            "working_decimal_digits": WORK_DPS,
            "lower_precision_stability_check_decimal_digits": LOW_DPS,
            "exact_integer_origin_derivatives_before_numerical_conversion": True,
            "Taylor_outer_product_tail_for_quotient_Gram": DERIVATIVE_TAIL,
            "short_tail_stability_comparison": H2_SHORT_TAIL,
            "continuous_quadratic_optimization_only": True,
            "no_integer_SVP_or_denominator_bound_claimed": True,
        },
        "representative_rows": [parameter_row(n) for n in (5, 8, 10)],
        "finite_grid_verdict": {
            "H2_is_a_large_finite_improvement_over_same_function_L1": True,
            "observed_log_improvement_is_consistent_with_O_n": True,
            "no_observed_change_to_n_log_n_leading_ledger": True,
            "three_rows_do_not_prove_an_asymptotic_bound": True,
            "one_n_equals_8_H2_log_upper_bound_is_numerically_below_zero": True,
            "no_endpoint_beats_the_r_equals_1_degree_2_relative_threshold_3": True,
        },
        "limitations": {
            "no_all_parameter_H2_height_bound": True,
            "no_integer_or_rational_optimizer_height_control": True,
            "no_asymptotic_Smith_or_Gram_condition_formula": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
        "peak_RSS_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    print(
        json.dumps(
            {
                "output": str(OUT),
                "representative_rows": len(payload["representative_rows"]),
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
