#!/usr/bin/env python3
"""Deterministic exact checker for Item 295.

The bounded rows check universal algebraic identities for the sharp nearest
window, its congruence-only relaxation, and the one-step beta/Turan descent.
They do not scan for a counterexample and are EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
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


def nearest_positive(numerator: int, denominator: int) -> int:
    assert numerator >= 0 and denominator > 0
    assert (2 * numerator) % denominator != 0 or (
        (2 * numerator) // denominator
    ) % 2 == 0
    return (2 * numerator + denominator) // (2 * denominator)


def centered(value: int, odd_modulus: int) -> int:
    assert odd_modulus > 0 and odd_modulus % 2 == 1
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def check_windows(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(2, limit + 1):
        a = q[n - 1]
        b = q[n]
        c = q[n - 2]
        coefficient = 4 * n - 2
        assert b == coefficient * a + c
        assert math.gcd(a, b) == 1
        assert b % 2 == 1

        # A half-integer tie ac/b=H+1/2 would force b|ac, hence b|c.
        assert (2 * a * c) % b != 0
        nearest_h = nearest_positive(a * c, b)

        kappa = nearest_positive(a * a, b)
        signed_r = a * a - kappa * b
        assert signed_r == centered(a * a, b)
        rho = abs(signed_r)
        h_value = a - coefficient * kappa
        assert coefficient * signed_r == b * h_value - a * c

        congruence = (nearest_h - a) % coefficient == 0
        sharp_window = (
            2 * abs(b * nearest_h - a * c) < coefficient * a
        )
        relaxed_window = 2 * abs(b * nearest_h - a * c) < b
        assert relaxed_window
        half_failure = 2 * rho < a
        relaxed_failure = 2 * coefficient * rho < b
        assert half_failure == (congruence and sharp_window)
        assert congruence == relaxed_failure
        if congruence:
            candidate_kappa = (a - nearest_h) // coefficient
            candidate_r = a * a - candidate_kappa * b
            assert candidate_r == signed_r
            assert nearest_h == h_value

        rows.append(
            {
                "n": n,
                "half_failure_iff_sharp_congruent": True,
                "bare_congruence_iff_relaxed_threshold": True,
                "tie_excluded": True,
                "signed_r_sign": (signed_r > 0) - (signed_r < 0),
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "counterexample_search": False,
        "label": "EXACT FINITE ONLY",
    }


def check_descent(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(3, limit + 1):
        coefficient = 4 * n - 2
        previous_coefficient = coefficient - 4
        a = q[n - 1]
        b = q[n]
        c = q[n - 2]
        d = q[n - 3]
        assert a == previous_coefficient * c + d
        assert b == coefficient * a + c

        kappa = nearest_positive(a * a, b)
        signed_r = a * a - kappa * b
        h_value = a - coefficient * kappa

        transformed_k = kappa - previous_coefficient * h_value
        assert signed_r == a * h_value - c * kappa
        assert signed_r == d * h_value - c * transformed_k

        defect = c - kappa
        assert transformed_k + previous_coefficient * h_value == kappa
        projected_k = transformed_k + defect
        assert projected_k + previous_coefficient * h_value == c

        projected_remainder = c * c - a * h_value
        assert projected_remainder == c * defect - signed_r
        previous_centered = centered(c * c, a)
        assert centered(projected_remainder, a) == previous_centered
        assert centered(c * defect - signed_r, a) == previous_centered

        turan = b * c - a * a
        previous_turan = a * d - c * c
        assert turan > 0
        assert previous_turan > 0
        assert turan + previous_turan == 4 * a * c
        assert defect == nearest_positive(turan, b)

        lower_numerator = 4 * c - d
        upper_numerator = 5 * c - d
        assert lower_numerator * b < coefficient * turan
        assert (coefficient + 1) * turan < upper_numerator * b
        if n >= 4:
            assert 1 <= defect < c

        rows.append(
            {
                "n": n,
                "defect_zero": defect == 0,
                "determinant_preserved": True,
                "previous_slice_hit": defect == 0,
                "projected_center_is_previous_residue": True,
                "turan_recurrence": True,
            }
        )
    return {
        "range": [3, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "counterexample_search": False,
        "label": "EXACT FINITE ONLY",
    }


def check_exact_bases() -> dict[str, Any]:
    q = beta_q(4)
    rows: list[dict[str, Any]] = []
    expected = {
        2: (0, 1),
        3: (1, -22),
        4: (5, 36),
    }
    for n, (expected_kappa, expected_r) in expected.items():
        a = q[n - 1]
        b = q[n]
        kappa = nearest_positive(a * a, b)
        signed_r = a * a - kappa * b
        assert (kappa, signed_r) == (expected_kappa, expected_r)
        assert 2 * abs(signed_r) >= a
        rows.append(
            {
                "n": n,
                "a": a,
                "b": b,
                "kappa": kappa,
                "signed_r": signed_r,
                "half_bound": True,
            }
        )
    return {
        "rows": rows,
        "label": "EXACT BASE CASES",
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item295-beta-nearest-window-descent-certificate-v1",
        "description": (
            "Exact sharp nearest-window iff, congruence-only relaxation, "
            "unimodular beta descent, Turan defect, and projected previous "
            "residue checker"
        ),
        "theorem": {
            "sharp_iff": (
                "rho_n<a/2 iff H=round(ac/b) satisfies H congruent a "
                "mod A and |H-ac/b|<Aa/(2b)=1/2-c/(2b)"
            ),
            "bare_relaxation": (
                "H=round(ac/b) congruent a mod A iff "
                "rho_n<b/(2A)=a/2+c/(2A)"
            ),
            "descent": (
                "for B=A-4,d=q_(n-3),K=kappa-BH, "
                "r=dH-cK and the defect (K+BH)-c equals -t; "
                "the defect is nonzero from n=4 onward"
            ),
            "defect": (
                "t=c-kappa=round((bc-a^2)/b), and projection to the "
                "previous square slice gives c^2-aH=ct-r"
            ),
            "turan": (
                "T_n=bc-a^2>0 and T_n+T_(n-1)=4ac"
            ),
            "scoped_obstruction": (
                "the determinant-preserving descent misses the previous "
                "affine square slice by t from n=4 onward; projection "
                "centers back to the already-known previous residue and "
                "introduces ct"
            ),
            "scope": (
                "no all-n half-bound, exact counterexample, or proper-target "
                "capacity theorem is proved"
            ),
        },
        "bounded_exact_checks": {
            "base_cases": check_exact_bases(),
            "window_identities": check_windows(96),
            "descent_identities": check_descent(96),
            "asymptotic_extrapolation": False,
            "counterexample_search": False,
            "exceptional_prime_search": False,
            "label": "EXACT FINITE ONLY",
        },
        "admission": {
            "all_n_half_bound": "OPEN",
            "counterexample": "NONE PRODUCED",
            "bare_congruence_exclusion": "OPEN",
            "sharp_window_exclusion": "OPEN",
            "natural_minimal_counterexample_descent": "PROVED NOT CLOSED",
            "proper_target_large_factor_bound": "OPEN",
            "item282_product_baseline": "OPEN AND SEPARATE",
            "new_route1_rate": 0,
            "new_beta_capacity_reduction": 0,
            "positive_linear_capacity_admission": "FAIL",
        },
        "open": [
            "exclude the sharp nearest-window congruence for every n",
            "prove the stronger bound A(2rho_n-a)>=2c without finite extrapolation",
            "control the coupled Turan defect t through descent",
            "construct an exact counterexample if the half-bound is false",
            "a large proper de-overlapped target residue theorem",
            "the Item282 common product baseline and weighted-return cover",
            "Route 1 and every conclusion about e+pi",
        ],
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
