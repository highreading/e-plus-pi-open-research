#!/usr/bin/env python3
"""Deterministic exact checker for Item 300.

The bounded rows replay universal strip, affine inclusion, transported-width,
denominator-grid, and opposite-phase identities. They do not scan the actual
orbit for a half-bound failure and are EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def beta_q(limit: int) -> list[int]:
    q = [1, 1]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
    return q


def nearest_fraction(value: Fraction) -> int:
    quotient, residue = divmod(value.numerator, value.denominator)
    if 2 * residue == value.denominator:
        return quotient
    return quotient + (2 * residue > value.denominator)


def strip(q: list[int], n: int) -> tuple[Fraction, Fraction]:
    coefficient = 4 * n - 2
    return (
        Fraction(4 * q[n - 2] - q[n - 3], coefficient),
        Fraction(5 * q[n - 2] - q[n - 3], coefficient + 1),
    )


def affine(q: list[int], n: int, value: Fraction) -> Fraction:
    return Fraction(q[n - 1], q[n]) * (4 * q[n - 2] - value)


def transported_strip(
    q: list[int],
    n: int,
    depth: int,
) -> tuple[Fraction, Fraction]:
    start = n - depth
    lower, upper = strip(q, start)
    for row in range(start + 1, n + 1):
        lower, upper = affine(q, row, upper), affine(q, row, lower)
    return lower, upper


def check_normalized_state(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(4, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        d_value = q[n - 3]
        assert b_value == coefficient * a_value + c_value
        assert a_value == (coefficient - 4) * c_value + d_value

        turan = b_value * c_value - a_value * a_value
        previous_turan = a_value * d_value - c_value * c_value
        x_value = Fraction(turan, b_value)
        previous_x = Fraction(previous_turan, a_value)
        assert x_value == affine(q, n, previous_x)

        theta = Fraction(c_value, a_value)
        previous_theta = Fraction(d_value, c_value)
        y_value = x_value / c_value
        previous_y = previous_x / d_value
        assert theta == 1 / (coefficient - 4 + previous_theta)
        assert y_value == (
            4 - previous_theta * previous_y
        ) / (coefficient + theta)

        lower, upper = strip(q, n)
        assert lower < x_value < upper
        normalized_lower = Fraction(4, 1) - previous_theta
        normalized_lower /= coefficient
        normalized_upper = Fraction(5, 1) - previous_theta
        normalized_upper /= coefficient + 1
        assert normalized_lower < y_value < normalized_upper

        t_value = nearest_fraction(x_value)
        r_value = b_value * t_value - turan
        s_value = Fraction(r_value, a_value)
        assert s_value == (coefficient + theta) * (t_value - x_value)

        previous_t = nearest_fraction(previous_x)
        previous_r = a_value * previous_t - previous_turan
        previous_s = Fraction(previous_r, c_value)
        phase = s_value - theta * t_value
        centered_phase = phase - nearest_fraction(phase)
        assert previous_s == -centered_phase / theta

        rows.append(
            {
                "n": n,
                "ratio_state": True,
                "normalized_strip": True,
                "centered_phase_update": True,
            }
        )
    return {
        "range": [4, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "half_bound_scan": False,
        "label": "EXACT FINITE ONLY",
    }


def check_strip_inclusion(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(4, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        d_value = q[n - 3]
        lower, upper = strip(q, n)
        previous_lower, previous_upper = strip(q, n - 1)
        image_lower = affine(q, n, previous_upper)
        image_upper = affine(q, n, previous_lower)
        assert lower < image_lower < image_upper < upper

        expected_width = Fraction(
            a_value,
            coefficient * (coefficient + 1),
        )
        expected_image_width = Fraction(
            a_value * c_value,
            b_value * (coefficient - 4) * (coefficient - 3),
        )
        assert upper - lower == expected_width
        assert image_upper - image_lower == expected_image_width

        turan = b_value * c_value - a_value * a_value
        x_value = Fraction(turan, b_value)
        assert x_value - lower == Fraction(
            a_value * c_value,
            coefficient * b_value,
        )
        assert upper - x_value == Fraction(
            a_value * (a_value - c_value),
            (coefficient + 1) * b_value,
        )

        left_cross_difference = (
            (coefficient - 3) * a_value
            - coefficient * (c_value - d_value)
        )
        assert left_cross_difference == (
            (coefficient - 2) * (coefficient - 6) * c_value
            + (2 * coefficient - 3) * d_value
        )
        assert left_cross_difference > 0
        assert (
            (coefficient - 4) * a_value * (a_value - c_value)
            > (coefficient + 1) * c_value * d_value
        )

        if n >= 5:
            assert expected_width > 2
        if n >= 8:
            assert expected_image_width > 2

        rows.append(
            {
                "n": n,
                "strict_image_inclusion": True,
                "strip_width_gt_2_from_n5": n < 5 or expected_width > 2,
                "one_step_width_gt_2_from_n8": (
                    n < 8 or expected_image_width > 2
                ),
            }
        )
    return {
        "range": [4, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "counterexample_search": False,
        "label": "EXACT FINITE ONLY",
    }


def check_depth_widths(limit: int, max_depth: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(8, limit + 1):
        for depth in range(1, min(max_depth, n - 3) + 1):
            start = n - depth
            lower, upper = transported_strip(q, n, depth)
            expected = Fraction(
                q[start] * q[start - 1],
                q[n] * (4 * start - 2) * (4 * start - 1),
            )
            assert upper - lower == expected
            current_lower, current_upper = strip(q, n)
            assert current_lower < lower < upper < current_upper
            rows.append(
                {
                    "n": n,
                    "depth": depth,
                    "width_formula": True,
                    "inside_current_strip": True,
                    "width_gt_2": expected > 2,
                }
            )
    return {
        "range": [8, limit],
        "max_depth": max_depth,
        "rows": len(rows),
        "digest": digest(rows),
        "asymptotic_extrapolation": False,
        "label": "EXACT FINITE ONLY",
    }


def check_opposite_phases(limit: int, max_depth: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(8, limit + 1):
        for depth in range(1, min(max_depth, n - 3) + 1):
            lower, upper = transported_strip(q, n, depth)
            if upper - lower <= 2:
                continue
            midpoint = (lower + upper) / 2
            k_value = nearest_fraction(midpoint)
            assert lower < k_value - Fraction(1, 2)
            assert k_value + Fraction(1, 2) < upper

            b_value = q[n]
            a_value = q[n - 1]
            close_state = Fraction(k_value * b_value + 1, b_value)
            far_state = Fraction(
                k_value * b_value + (b_value - 1) // 2,
                b_value,
            )
            assert lower < close_state < upper
            assert lower < far_state < upper
            assert math.gcd(close_state.numerator, close_state.denominator) == 1
            assert math.gcd(far_state.numerator, far_state.denominator) == 1
            assert close_state.denominator == b_value
            assert far_state.denominator == b_value

            close_r = b_value * k_value - (
                k_value * b_value + 1
            )
            far_r = b_value * k_value - (
                k_value * b_value + (b_value - 1) // 2
            )
            assert close_r == -1
            assert far_r == -(b_value - 1) // 2
            assert 2 * abs(close_r) < a_value
            assert 2 * abs(far_r) > a_value

            for label, current in (
                ("close", close_state),
                ("far", far_state),
            ):
                row = n
                while row > n - depth:
                    numerator_on_grid = current * q[row]
                    assert numerator_on_grid.denominator == 1
                    current = (
                        4 * q[row - 2]
                        - Fraction(q[row], q[row - 1]) * current
                    )
                    previous_lower, previous_upper = strip(q, row - 1)
                    assert previous_lower < current < previous_upper
                    previous_grid = current * q[row - 1]
                    assert previous_grid.denominator == 1
                    row -= 1
                assert row == n - depth
                rows.append(
                    {
                        "n": n,
                        "depth": depth,
                        "phase": label,
                        "all_strip_memberships": True,
                        "all_denominator_grids": True,
                        "primitive_all_levels_claim": False,
                        "actual_seed_orbit_claim": False,
                    }
                )
    return {
        "range": [8, limit],
        "max_depth": max_depth,
        "rows": len(rows),
        "digest": digest(rows),
        "actual_counterexample": False,
        "primitive_all_levels_claim": False,
        "label": "PROVED MODEL CONSTRUCTION; BOUNDED REPLAY EXACT FINITE ONLY",
    }


def symbolic_proof_data() -> dict[str, Any]:
    strip_base_margin = 1001 - 2 * 18 * 19
    one_step_base_margin = (
        398959 - 2 * 31 * 26 * 27
    )
    assert strip_base_margin > 0
    assert one_step_base_margin > 0
    assert 18**2 * 19 > 22 * 23
    assert (30 - 4) ** 2 * (30 - 3) > 30 * 35
    return {
        "strip_width": {
            "formula": "q_(n-1)/[(4n-2)(4n-1)]",
            "base_n": 5,
            "base_margin": strip_base_margin,
            "persistence": (
                "q_n>A*q_(n-1) and "
                "A^2*(A+1)>(A+4)*(A+5) for A>=18"
            ),
        },
        "one_step_width": {
            "formula": (
                "q_(n-1)q_(n-2)/"
                "[q_n(4n-6)(4n-5)]"
            ),
            "base_n": 8,
            "base_margin_for_c_bound": one_step_base_margin,
            "persistence": (
                "(A-4)^2*(A-3)>A*(A+5) for A>=30"
            ),
        },
        "sublinear_depth": {
            "exact_width": (
                "q_(n-L)q_(n-L-1)/"
                "[q_n(4(n-L)-2)(4(n-L)-1)]"
            ),
            "explicit_lower_bound": (
                "(2m-2)^floor(m/2)/(4n+1)^(L+2), m=n-L"
            ),
            "eventual_conditions": [
                "L<=n/4",
                "m>=3n/4",
                "floor(m/2)>=n/3",
                "L+2<=n/12",
                "log(2m-2)>=log(n)",
                "log(4n+1)<=2log(n)",
            ],
            "conclusion": (
                "log width>(n/6)log n and width tends to infinity "
                "for every L(n)=o(n)"
            ),
        },
        "label": "PROVED SYMBOLIC IN REPORT",
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item300-beta-short-branch-strip-certificate-v1",
        "description": (
            "Exact normalized beta state, seed strip, affine inclusion, "
            "sublinear-depth transported-width divergence, and opposite "
            "denominator-grid phase construction"
        ),
        "theorem": {
            "normalized_state": (
                "theta_n=1/(A-4+theta_(n-1)); "
                "y_n=(4-theta_(n-1)y_(n-1))/(A+theta_n)"
            ),
            "strip": (
                "I_n=((4c-d)/A,(5c-d)/(A+1)), "
                "length a/[A(A+1)]"
            ),
            "affine_inclusion": (
                "F_n(I_(n-1)) is a strict subset of I_n"
            ),
            "depth_width": (
                "|J_(n,L)|=q_(n-L)q_(n-L-1)/"
                "[q_n A_(n-L)(A_(n-L)+1)]"
            ),
            "sublinear_no_go": (
                "for L(n)=o(n), transported width tends to infinity; "
                "the declared model class contains close and far phases"
            ),
            "scope_limit": (
                "model witnesses preserve grids and strips but not the "
                "actual Turan seed numerator or primitivity at every level"
            ),
        },
        "symbolic_proof_data": symbolic_proof_data(),
        "bounded_exact_checks": {
            "normalized_state": check_normalized_state(72),
            "strip_inclusion": check_strip_inclusion(72),
            "depth_widths": check_depth_widths(40, 8),
            "opposite_phases": check_opposite_phases(40, 8),
            "actual_half_bound_scan": False,
            "counterexample_search": False,
            "exceptional_prime_search": False,
            "label": "EXACT FINITE ONLY",
        },
        "admission": {
            "actual_half_bound": "OPEN",
            "stronger_item295_inequality": "OPEN",
            "sublinear_depth_phase_blind_affine_strip": (
                "PROVED SCOPED NOT SUFFICIENT"
            ),
            "linear_depth_or_seed_phase_invariant": "OPEN",
            "actual_counterexample": "NONE PRODUCED",
            "proper_target_large_factor_bound": "OPEN",
            "item282_product_baseline": "OPEN AND SEPARATE",
            "new_route1_rate": 0,
            "new_beta_capacity_reduction": 0,
            "positive_linear_capacity_admission": "FAIL",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
