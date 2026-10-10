#!/usr/bin/env python3
"""Deterministic exact controls for Item 389.

The all-degree proofs are in the report.  This checker pins Item 387,
reconstructs declared integer-polynomial decompositions, verifies the
endpoint identities and coefficient budgets, and records exact rational
constant bounds.  It performs no search for small or nonzero linear forms.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item389_mixed_kernel_analytic_cost_continued_fraction_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item387_mixed_kernel_quotient_and_claim_audit_report.md":
        "061e29589d427ccb5c8549c8344781c0c8f0e674d2fa525da03325312ce40625",
    "work/item387_mixed_kernel_quotient_and_claim_audit_certificate.py":
        "28bf4e9cdfcd64cf7e48cebf3f0dadb18115d54ff3a5136937f0ce2a042ba83b",
    "work/item387_mixed_kernel_quotient_and_claim_audit_certificate.json":
        "4e0b426e93032f526f8097bec3ed6c0663842b0c60a818fb49142ade89aa3200",
    "work/item387_mixed_kernel_quotient_and_claim_audit_certificate_replay.json":
        "4e0b426e93032f526f8097bec3ed6c0663842b0c60a818fb49142ade89aa3200",
    "work/item387_mixed_kernel_quotient_and_claim_audit_ledger_delta.json":
        "7564d3303016ea2a7c02efddaff22dd3211bb83e96ea618d11a7b31591ed57ed",
    "work/item387_mixed_kernel_quotient_and_claim_audit_root_audit.json":
        "62bc0ce724c8e0c03b04928126eee9a05c10359a326eeec07162309adf46b421",
    "work/item387_mixed_kernel_quotient_and_claim_audit_manifest.json":
        "98b61d8b34c64b7e9ffd6767aafe47f225577913c900ecb0174540b76c2e9fd1",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing dependency", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(("dependency mismatch", relative, expected, actual))


def trim(polynomial: list[int]) -> list[int]:
    output = polynomial[:]
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output or [0]


def add(left: list[int], right: list[int]) -> list[int]:
    length = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(length)
    ])


def scale(polynomial: list[int], scalar: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in polynomial])


def derivative(polynomial: list[int]) -> list[int]:
    if len(polynomial) <= 1:
        return [0]
    return trim([index * polynomial[index] for index in range(1, len(polynomial))])


def multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return trim(output)


def evaluate(polynomial: list[int], value: int) -> int:
    output = 0
    for coefficient in reversed(polynomial):
        output = output * value + coefficient
    return output


def alternating_derivative_sum(polynomial: list[int]) -> list[int]:
    output = [0]
    current = polynomial[:]
    sign = 1
    while current != [0]:
        output = add(output, scale(current, sign))
        current = derivative(current)
        sign = -sign
    return trim(output)


def construct_polynomial(a_value: int, c_value: int, r_poly: list[int]) -> tuple[list[int], list[int]]:
    endpoint = [a_value, a_value - c_value]
    s_poly = multiply([0, -1, 1], r_poly)  # x(x-1)R
    kernel = add(s_poly, derivative(s_poly))
    return add(endpoint, kernel), kernel


def declared_polynomial_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 3, [5]),
        (2, -1, [10, -3, 4]),
        (3, 7, [0, 1]),
        (-2, 5, [-10, 0, 1, -1]),
        (0, 1, [0, 2, -1, 3, 0, 1]),
        (5, -4, [25, -7, 0, 2, -3, 1]),
    ]
    output: list[dict[str, Any]] = []
    for a_value, c_value, r_poly in declared:
        p_poly, kernel = construct_polynomial(a_value, c_value, r_poly)
        s_p = alternating_derivative_sum(p_poly)
        if (evaluate(s_p, 1), evaluate(s_p, 0)) != (a_value, c_value):
            raise AssertionError(("endpoint pair", a_value, c_value, p_poly, s_p))
        if alternating_derivative_sum(kernel) != multiply([0, -1, 1], r_poly):
            raise AssertionError(("kernel inverse", a_value, c_value, r_poly))

        r0 = r_poly[0]
        mixed_endpoint = p_poly[0] + 4 * a_value
        if p_poly[0] != a_value - r0:
            raise AssertionError(("P(0)", a_value, c_value, r_poly, p_poly))
        if mixed_endpoint != 5 * a_value - r0:
            raise AssertionError(("mixed endpoint", a_value, c_value, r_poly))

        b0 = sum(abs(value) for value in p_poly)
        b1 = sum(index * abs(value) for index, value in enumerate(p_poly))
        analytic_cost = 3 * (b0 + b1 + abs(a_value))
        exact_encoding = r0 == 5 * a_value
        if exact_encoding:
            if max(abs(value) for value in r_poly) < 5 * abs(a_value):
                raise AssertionError(("R coefficient cost", a_value, c_value, r_poly))
            if b0 < 4 * abs(a_value):
                raise AssertionError(("P coefficient cost", a_value, c_value, p_poly))

        output.append({
            "classification": "PREDECLARED EXACT POLYNOMIAL CONTROL; NOT A SMALL-FORM SEARCH",
            "A": a_value,
            "C": c_value,
            "R_coefficients_low_to_high": r_poly,
            "P_coefficients_low_to_high": p_poly,
            "kernel_coefficients_low_to_high": kernel,
            "S_P_coefficients_low_to_high": s_p,
            "endpoint_pair": [evaluate(s_p, 1), evaluate(s_p, 0)],
            "mixed_integrand_value_at_zero": mixed_endpoint,
            "five_A_minus_R0": 5 * a_value - r0,
            "R0_equals_5A": exact_encoding,
            "B0": b0,
            "B1": b1,
            "Lambda": analytic_cost,
            "if_endpoint_nonzero_L1_lower_bound": (
                {"numerator": 1, "denominator": 2 * analytic_cost}
                if mixed_endpoint != 0 else None
            ),
        })
    return output


def exact_constant_controls() -> dict[str, Any]:
    # Machin: pi=16 atan(1/5)-4 atan(1/239).  The alternating-series
    # bounds atan(1/5)>1/5-1/(3*5^3), atan(1/239)<1/239 give this lower bound.
    pi_lower = 16 * (Fraction(1, 5) - Fraction(1, 3 * 5**3)) - 4 * Fraction(1, 239)
    if not pi_lower > 3:
        raise AssertionError(("pi lower bound", pi_lower))

    # The square of the exact rational-part derivative maximum
    # 3*sqrt(3)/2 is 27/4, strictly below 9.
    derivative_maximum_square = Fraction(27, 4)
    if not derivative_maximum_square < 9:
        raise AssertionError("rational derivative bound")

    return {
        "classification": "EXACT ELEMENTARY CONSTANT CONTROLS; NOT NUMERICAL EVIDENCE",
        "e_upper_bound": "e<1+1+sum_(n>=2)2^(-(n-1))=3, strict because n!>2^(n-1) for n>=3",
        "pi_Machin_lower_bound": {
            "numerator": pi_lower.numerator,
            "denominator": pi_lower.denominator,
            "greater_than_3": True,
        },
        "pi_upper_bound": "pi=4*integral_0^1 dx/(1+x^2)<4",
        "e_plus_pi_upper_bound": "e+pi<7",
        "rational_term_derivative_exact_maximum": "3*sqrt(3)/2",
        "rational_term_derivative_maximum_square": {
            "numerator": derivative_maximum_square.numerator,
            "denominator": derivative_maximum_square.denominator,
        },
        "rational_term_derivative_less_than_3": True,
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    return {
        "schema": "item389-mixed-kernel-analytic-cost-continued-fraction-no-go-certificate-v1",
        "item": 389,
        "date": "2026-09-01",
        "dependency_hashes_verified": True,
        "all_degree_theorems": {
            "endpoint": "F(0)=5A-R(0) is an integer",
            "uniform": "norm_infinity(F)>=|5A-R(0)|; norm_infinity(F)<1 forces R(0)=5A and p0=-4A",
            "L1_dichotomy": "R(0)=5A or norm_1(F)>=1/[2 Lambda], Lambda=3(B0+B1+|A|)",
            "coefficient_cost": "B0>=(3|A|-norm_1(F))/2, with strictness away from the zero tuple",
            "continued_fraction": "if B0>0 and 0<|A(e+pi)-C|<=norm_1(F)<min(1,1/(2B0)), then A!=0, |A|<=B0, and |e+pi-C/A|<1/(2A^2)",
            "degree_one_replacement": "under the same hypotheses B0(P_(A,C))<9B0(P)+1 while the integer linear form is unchanged",
            "nonzero_sequence_constructed": False,
        },
        "polynomial_controls": declared_polynomial_controls(),
        "constant_controls": exact_constant_controls(),
        "scope": {
            "unstructured_search_performed": False,
            "optimization_performed": False,
            "small_nonzero_form_claimed": False,
            "irrationality_claimed": False,
            "structured_family_ruled_out_without_hypotheses": False,
        },
        "ledger": {
            "new_nonzero_linear_form_sequence": 0,
            "new_route1_booking": 0,
            "new_capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
