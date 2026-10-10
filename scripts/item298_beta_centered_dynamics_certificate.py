#!/usr/bin/env python3
"""Deterministic exact checker for Item 298.

The bounded rows replay universal rational identities, the centered pair
bijection, the actual carry formula, and explicit obstruction witnesses.
They do not scan the actual orbit for half-bound failures and are
EXACT FINITE ONLY.
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


def nearest(numerator: int, denominator: int) -> int:
    """Unique nearest integer when denominator is odd."""
    assert denominator > 0 and denominator % 2 == 1
    quotient, residue = divmod(numerator, denominator)
    assert 2 * residue != denominator
    return quotient + (2 * residue > denominator)


def centered(numerator: int, odd_modulus: int) -> int:
    return numerator - odd_modulus * nearest(numerator, odd_modulus)


def pair_backward(
    r_value: int,
    t_value: int,
    coefficient: int,
    a_value: int,
    b_value: int,
    c_value: int,
) -> tuple[int, int]:
    assert abs(2 * r_value) < b_value
    carry = nearest(r_value - c_value * t_value, a_value)
    return (
        c_value * t_value - r_value + a_value * carry,
        4 * c_value - coefficient * t_value + carry,
    )


def pair_forward(
    previous_r: int,
    previous_t: int,
    a_value: int,
    b_value: int,
    c_value: int,
) -> tuple[int, int]:
    assert abs(2 * previous_r) < a_value
    t_value = nearest(
        4 * a_value * c_value
        - a_value * previous_t
        + previous_r,
        b_value,
    )
    r_value = (
        b_value * t_value
        - 4 * a_value * c_value
        + a_value * previous_t
        - previous_r
    )
    assert abs(2 * r_value) < b_value
    return r_value, t_value


def check_actual_dynamics(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(3, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        d_value = q[n - 3]
        assert b_value == coefficient * a_value + c_value

        turan = b_value * c_value - a_value * a_value
        previous_turan = a_value * d_value - c_value * c_value
        assert turan + previous_turan == 4 * a_value * c_value
        t_value = nearest(turan, b_value)
        r_value = b_value * t_value - turan
        previous_t = nearest(previous_turan, a_value)
        previous_r = a_value * previous_t - previous_turan

        w_value = Fraction(turan, b_value)
        previous_w = Fraction(previous_turan, a_value)
        assert w_value == Fraction(t_value, 1) - Fraction(r_value, b_value)
        assert previous_w == 4 * c_value - Fraction(b_value, a_value) * w_value
        assert w_value == Fraction(a_value, b_value) * (
            4 * c_value - previous_w
        )

        backward = pair_backward(
            r_value,
            t_value,
            coefficient,
            a_value,
            b_value,
            c_value,
        )
        assert backward == (previous_r, previous_t)
        assert pair_forward(
            previous_r,
            previous_t,
            a_value,
            b_value,
            c_value,
        ) == (r_value, t_value)

        forward_carry = coefficient * t_value - 4 * c_value + previous_t
        assert turan == a_value * (4 * c_value - previous_t) + previous_r
        assert (
            r_value
            == a_value * forward_carry
            + c_value * t_value
            - previous_r
        )

        epsilon = Fraction(r_value, b_value)
        previous_epsilon = Fraction(previous_r, a_value)
        assert (
            forward_carry
            == -Fraction(c_value, a_value) * w_value
            + coefficient * epsilon
            + previous_epsilon
        )
        carry_upper = Fraction(coefficient + 1, 2) - Fraction(
            3 * c_value,
            coefficient * (coefficient - 3),
        )
        assert Fraction(forward_carry, 1) < carry_upper
        if n == 6:
            assert (t_value, previous_t, forward_carry) == (181, 16, -6)
        if n >= 6:
            assert forward_carry < 0

        rows.append(
            {
                "n": n,
                "rank_one_affine_state": True,
                "pair_backward_inverse": True,
                "forward_carry_identity": True,
                "carry_negative_from_n6": n < 6 or forward_carry < 0,
            }
        )
    return {
        "range": [3, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "half_bound_scan": False,
        "counterexample_search": False,
        "label": "EXACT FINITE ONLY",
    }


def check_pair_bijection(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    test_r_multipliers = (-2, -1, 0, 1, 2)
    test_t_values = (-5, -1, 0, 1, 2, 7)
    for n in range(4, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        for multiplier in test_r_multipliers:
            r_value = multiplier * a_value
            assert abs(2 * r_value) < b_value
            for t_value in test_t_values:
                previous = pair_backward(
                    r_value,
                    t_value,
                    coefficient,
                    a_value,
                    b_value,
                    c_value,
                )
                recovered = pair_forward(
                    previous[0],
                    previous[1],
                    a_value,
                    b_value,
                    c_value,
                )
                assert recovered == (r_value, t_value)

        sample_r = a_value
        sample_t = 3
        first = pair_backward(
            sample_r,
            sample_t,
            coefficient,
            a_value,
            b_value,
            c_value,
        )
        second = pair_backward(
            sample_r,
            sample_t + a_value,
            coefficient,
            a_value,
            b_value,
            c_value,
        )
        assert second == (first[0], first[1] - b_value)

        rows.append(
            {
                "n": n,
                "sampled_inverse_identities": (
                    len(test_r_multipliers) * len(test_t_values)
                ),
                "vertical_lattice_equivariance": True,
            }
        )
    return {
        "range": [4, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "identity_regression_only": True,
        "label": "EXACT FINITE ONLY",
    }


def check_primitive_collapse(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(4, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        assert math.gcd(a_value, c_value) == 1

        target = (a_value - 3) // 2
        k_value = (target * pow(c_value, -1, a_value)) % a_value
        assert (k_value * c_value + 1 - (a_value - 1) // 2) % a_value == 0

        x_numerator = (
            4 * a_value * c_value - k_value * b_value - 1
        )
        y_numerator = k_value * b_value + 1
        x_value = Fraction(x_numerator, a_value)
        y_value = Fraction(y_numerator, b_value)
        assert Fraction(a_value, b_value) * (4 * c_value - x_value) == y_value
        assert math.gcd(x_numerator, a_value) == 1
        assert math.gcd(y_numerator, b_value) == 1
        assert centered(x_numerator, a_value) == -(a_value - 1) // 2
        assert centered(y_numerator, b_value) == 1

        current_t = nearest(y_numerator, b_value)
        current_r = b_value * current_t - y_numerator
        previous_t = nearest(x_numerator, a_value)
        previous_r = a_value * previous_t - x_numerator
        assert current_t == k_value
        assert current_r == -1
        assert previous_r == (a_value - 1) // 2
        assert pair_backward(
            current_r,
            current_t,
            coefficient,
            a_value,
            b_value,
            c_value,
        ) == (previous_r, previous_t)
        assert 2 * abs(current_r) < a_value

        rows.append(
            {
                "n": n,
                "previous_centered_numerator": (a_value - 1) // 2,
                "current_centered_numerator": -1,
                "both_denominators_primitive": True,
                "actual_orbit_claim": False,
            }
        )
    return {
        "range": [4, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "constructed_ambient_family": True,
        "actual_counterexample": False,
        "label": "PROVED CONSTRUCTION; BOUNDED REPLAY EXACT FINITE ONLY",
    }


def check_fixed_norm_witness(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(4, limit + 1):
        coefficient = 4 * n - 2
        a_value = q[n - 1]
        b_value = q[n]
        c_value = q[n - 2]
        assert c_value >= 7 and a_value > 2 * c_value
        first = pair_backward(
            c_value,
            1,
            coefficient,
            a_value,
            b_value,
            c_value,
        )
        second = pair_backward(
            c_value,
            2,
            coefficient,
            a_value,
            b_value,
            c_value,
        )
        assert first == (0, 4 * c_value - coefficient)
        assert second == (
            c_value,
            4 * c_value - 2 * coefficient,
        )
        assert (
            second[0] - first[0],
            second[1] - first[1],
        ) == (c_value, -coefficient)
        rows.append(
            {
                "n": n,
                "input_difference": [0, 1],
                "output_difference": [str(c_value), -coefficient],
                "actual_orbit_claim": False,
            }
        )
    return {
        "range": [4, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "constructed_ambient_family": True,
        "label": "PROVED CONSTRUCTION; BOUNDED REPLAY EXACT FINITE ONLY",
    }


def symbolic_carry_proof_data() -> dict[str, Any]:
    coefficient = 26
    c_value = 18089
    base_margin = 6 * c_value - coefficient * (coefficient - 3) * (
        coefficient + 1
    )
    persistence_difference = (
        (coefficient - 4) * coefficient * (coefficient - 3)
        - (coefficient + 4) * (coefficient + 5)
    )
    polynomial_at_26 = (
        coefficient**3
        - 8 * coefficient**2
        + 3 * coefficient
        - 20
    )
    forward_difference_at_26 = (
        3 * coefficient**2 - 13 * coefficient - 4
    )
    assert base_margin > 0
    assert persistence_difference > 0
    assert persistence_difference == polynomial_at_26
    assert forward_difference_at_26 > 0
    return {
        "base_n": 7,
        "base_A": coefficient,
        "base_c": c_value,
        "base_margin_6c_minus_A_Aminus3_Aplus1": base_margin,
        "persistence_polynomial": "A^3-8*A^2+3*A-20",
        "polynomial_at_26": polynomial_at_26,
        "forward_difference": "3*A^2-13*A-4",
        "forward_difference_at_26": forward_difference_at_26,
        "growth_bound": "q_(n-2)>7*product_(j=3)^(n-2)(4j-2)",
        "conclusion": "u_n<0 for n>=6 and u_n tends to -infinity",
        "label": "PROVED SYMBOLIC IN REPORT",
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item298-beta-centered-dynamics-certificate-v1",
        "description": (
            "Exact rank-one Turan state, centered pair bijection, actual "
            "unbounded carry, primitive-denominator collapse family, and "
            "ambient fixed-norm expansion witnesses"
        ),
        "theorem": {
            "rank_one_state": (
                "w_n=T_n/b=t_n-r_n/b and "
                "w_(n-1)=4c-(b/a)w_n"
            ),
            "pair_map": (
                "m=nint((r-ct)/a), "
                "Phi_n(r,t)=(ct-r+am,4c-At+m), with explicit inverse"
            ),
            "actual_forward_carry": (
                "u_n=A*t_n-4c+t_(n-1), "
                "r_n=a*u_n+c*t_n-r_(n-1), "
                "u_n<0 for n>=6 and u_n tends to -infinity"
            ),
            "primitive_collapse": (
                "there are exact-denominator affine states with previous "
                "centered numerator (a-1)/2 and current numerator -1"
            ),
            "scoped_obstruction": (
                "affine contraction, recurrence, coprimality, or a fixed "
                "unscaled ambient norm does not prove the actual half-bound"
            ),
            "scope_limit": (
                "collapse and norm witnesses are not actual Turan-orbit "
                "counterexamples and need not satisfy the short digit interval"
            ),
        },
        "symbolic_proof_data": {
            "actual_carry": symbolic_carry_proof_data(),
        },
        "bounded_exact_checks": {
            "actual_dynamics": check_actual_dynamics(72),
            "pair_bijection": check_pair_bijection(36),
            "primitive_collapse": check_primitive_collapse(72),
            "fixed_norm_witness": check_fixed_norm_witness(72),
            "half_bound_scan": False,
            "counterexample_search": False,
            "exceptional_prime_search": False,
            "label": "EXACT FINITE ONLY",
        },
        "admission": {
            "all_n_half_bound": "OPEN",
            "actual_counterexample": "NONE PRODUCED",
            "actual_short_branch_invariant": "OPEN",
            "bounded_forward_carry": "PROVED FALSE FOR ACTUAL FAMILY",
            "row_dependent_rescaled_lyapunov": "OPEN",
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
