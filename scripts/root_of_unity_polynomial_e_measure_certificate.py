#!/usr/bin/env python3
"""Exact checks for the low-degree endpoint polynomial measure note.

This certificate deliberately uses only Python's standard-library integer
and rational arithmetic.  The transcendence-measure theorem itself is a
cited all-parameter theorem; this script checks the finite optimizer table,
the exponent bookkeeping, and the tangent-number arithmetic used in the
archived comparison.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial, gcd, isqrt
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parents[1]
SOURCE = ARCHIVE / "sources" / "root_of_unity_low_degree_polynomial_e_measure.md"
DEFAULT_OUTPUT = (
    ARCHIVE / "results" / "root_of_unity_polynomial_e_measure_certificate.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def psi(field_degree: int, poly_degree: int, accessory: int) -> Fraction:
    """Fischler--Rivoal's exact exponent psi(d, delta, p)."""

    d = field_degree
    delta = poly_degree
    p = accessory
    assert p >= d * delta
    return (
        Fraction(delta * d * d * (p - delta + 1), p - delta * d + 1)
        + d * (p - delta + 1)
        - 1
    )


def optimizer_candidates(field_degree: int, poly_degree: int) -> tuple[int, int]:
    d = field_degree
    delta = poly_degree
    floor_term = isqrt(delta * delta * (d * d - d))
    p1 = delta * d - 1 + floor_term
    return p1, p1 + 1


def tangent_numbers(last_index: int) -> list[int]:
    """Return T_1,...,T_last_index for tan(x)."""

    assert last_index >= 1
    values = [0] * (last_index + 1)
    values[1] = 1
    # tan'(x)=1+tan(x)^2 gives this exact convolution.
    for n in range(1, last_index):
        values[n + 1] = sum(
            comb(2 * n, 2 * j - 1) * values[j] * values[n + 1 - j]
            for j in range(1, n + 1)
        )
    return values


def odd_part(value: int) -> int:
    value = abs(value)
    while value and value % 2 == 0:
        value //= 2
    return value


def build_certificate(max_r: int, max_degree: int, tangent_q_max: int) -> dict:
    optimizer_rows = []
    optimizer_checks = 0
    exponent_checks = 0

    for r in range(1, max_r + 1):
        direct_field_degree = 2 * r
        for degree in range(1, max_degree + 1):
            p1, p2 = optimizer_candidates(direct_field_degree, degree)
            candidate_values = {p1: psi(direct_field_degree, degree, p1),
                                p2: psi(direct_field_degree, degree, p2)}
            p_opt = min(candidate_values, key=lambda p: (candidate_values[p], p))
            mu = candidate_values[p_opt]

            # This is a finite replay, not the proof that p1 or p2 is the
            # global optimizer.  The latter is the cited primary theorem.
            brute_stop = p2 + 4 * direct_field_degree * degree + 20
            brute = min(
                range(direct_field_degree * degree, brute_stop + 1),
                key=lambda p: (psi(direct_field_degree, degree, p), p),
            )
            assert brute == p_opt
            optimizer_checks += 1

            gaussian_relative_norm_exponent = r * r * degree + r - 1
            rational_full_norm_exponent = (
                (2 * r) * (2 * r) * degree + 2 * r - 1
            )
            assert Fraction(gaussian_relative_norm_exponent, 1) < mu
            assert gaussian_relative_norm_exponent < rational_full_norm_exponent
            exponent_checks += 2

            optimizer_rows.append(
                {
                    "coefficient_real_degree_r": r,
                    "direct_field_degree_2r": direct_field_degree,
                    "polynomial_degree_D": degree,
                    "p1": p1,
                    "p2": p2,
                    "p_opt": p_opt,
                    "mu_numerator": mu.numerator,
                    "mu_denominator": mu.denominator,
                    "gaussian_relative_norm_height_exponent": (
                        gaussian_relative_norm_exponent
                    ),
                    "rational_full_norm_height_exponent": (
                        rational_full_norm_exponent
                    ),
                }
            )

    tangents = tangent_numbers(tangent_q_max + 1)
    expected_initial = [1, 2, 16, 272, 7936, 353792, 22368256, 1903757312]
    assert tangents[1 : 1 + len(expected_initial)] == expected_initial

    consecutive_odd_exceptions = []
    endpoint_gcd_odd_exceptions = []
    selected_q = {1, 2, 3, 10, 45, 100, 168, 200, tangent_q_max}
    selected_rows = []
    ratio_checks = 0
    primitive_checks = 0

    for q in range(1, tangent_q_max + 1):
        tq = tangents[q]
        tq1 = tangents[q + 1]

        u_q = Fraction(tq, (2 ** (2 * q)) * factorial(2 * q - 1))
        u_q1 = Fraction(
            tq1, (2 ** (2 * q + 2)) * factorial(2 * q + 1)
        )
        ratio_from_u = u_q / u_q1
        ratio_formula = Fraction(
            8 * q * (2 * q + 1) * tq,
            tq1,
        )
        assert u_q > 0
        assert ratio_from_u == ratio_formula
        ratio_checks += 1

        endpoint_gcd = gcd(tq1, 8 * q * (2 * q + 1) * tq)
        p_coeff = 8 * q * (2 * q + 1) * tq // endpoint_gcd
        q_coeff = tq1 // endpoint_gcd
        assert gcd(p_coeff, q_coeff) == 1
        assert Fraction(p_coeff, q_coeff) == ratio_formula
        primitive_checks += 2

        consecutive_gcd = gcd(tq, tq1)
        consecutive_odd = odd_part(consecutive_gcd)
        endpoint_odd = odd_part(endpoint_gcd)
        if consecutive_odd > 1:
            consecutive_odd_exceptions.append(
                {"q": q, "odd_part": str(consecutive_odd)}
            )
        if endpoint_odd > 1:
            endpoint_gcd_odd_exceptions.append(
                {"q": q, "odd_part": str(endpoint_odd)}
            )

        if q in selected_q:
            selected_rows.append(
                {
                    "q": q,
                    "T_q_decimal_digits": len(str(tq)),
                    "T_q_plus_1_decimal_digits": len(str(tq1)),
                    "endpoint_gcd_decimal_digits": len(str(endpoint_gcd)),
                    "Q_q_decimal_digits": len(str(q_coeff)),
                    "consecutive_gcd_odd_part": str(consecutive_odd),
                    "endpoint_gcd_odd_part": str(endpoint_odd),
                }
            )

    # The finite assertion reported in the source.
    assert consecutive_odd_exceptions == [
        {"q": 45, "odd_part": "587"},
        {"q": 168, "odd_part": "491"},
    ]

    source_text = SOURCE.read_text(encoding="utf-8")
    required_strings = [
        "r^2D+r-1",
        "T=(D+1)^{r-1}H^r",
        "Q_q=\\frac{T_{q+1}}",
        "2q\\log3",
        "Subexponential primitive endpoint",
    ]
    for marker in required_strings:
        assert marker in source_text

    return {
        "certificate": "root_of_unity_polynomial_e_measure",
        "checked_utc_date": "2026-08-27",
        "parameters": {
            "max_coefficient_real_degree_r": max_r,
            "max_polynomial_degree_D": max_degree,
            "tangent_q_max": tangent_q_max,
        },
        "checks": {
            "optimizer_finite_replays": optimizer_checks,
            "height_exponent_strict_comparisons": exponent_checks,
            "tangent_ratio_identities": ratio_checks,
            "tangent_primitive_pair_checks": primitive_checks,
            "source_marker_checks": len(required_strings),
        },
        "optimizer_rows": optimizer_rows,
        "tangent": {
            "initial_T_1_through_T_8": expected_initial,
            "consecutive_gcd_odd_exceptions": consecutive_odd_exceptions,
            "endpoint_gcd_odd_exceptions": endpoint_gcd_odd_exceptions,
            "selected_rows": selected_rows,
        },
        "sha256": {
            "source": sha256(SOURCE),
            "script": sha256(Path(__file__).resolve()),
        },
        "inspected_primary_source_sha256": {
            "ernvall_hytonen_matala_aho_seppala_arxiv_1704_01374v3_pdf": (
                "151e8e659be98c50bf931f1d9c35faa54c4a9a770e0d9ed66724593974d3c4dd"
            ),
            "fischler_rivoal_arxiv_2502_17992_author_pdf": (
                "0a1c89fb0856c29dca98720080968adec49a3f236ad06bbc501859b5860b1562"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=8)
    parser.add_argument("--max-degree", type=int, default=12)
    parser.add_argument("--tangent-q-max", type=int, default=300)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if args.max_r < 1 or args.max_degree < 1 or args.tangent_q_max < 8:
        raise SystemExit("all bounds must be positive, with tangent-q-max at least 8")

    result = build_certificate(args.max_r, args.max_degree, args.tangent_q_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        "ROOT_OF_UNITY_POLYNOMIAL_E_MEASURE_PASS",
        result["checks"],
    )


if __name__ == "__main__":
    main()
