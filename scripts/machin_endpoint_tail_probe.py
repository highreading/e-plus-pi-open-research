#!/usr/bin/env python3
"""Exact finite audit of the endpoint-normalized Machin tail bound.

The all-degree statements are proved in
``sources/machin_endpoint_asymptotics.md``.  This program only evaluates
the diagonal family in a finite degree range.  It reuses the exact solver
and rational enclosure for e+pi from ``mixed_hermite_pade_probe.py``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

from mixed_hermite_pade_probe import primitive_solution, s_interval

sys.set_int_max_str_digits(0)


def fraction_sha256(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def vector_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode()
    ).hexdigest()


def power_of_ten(k: int) -> Fraction:
    return Fraction(10**k) if k >= 0 else Fraction(1, 10 ** (-k))


def positive_scientific(value: Fraction, digits: int = 12) -> dict:
    if value <= 0:
        raise ValueError("scientific description requires a positive value")
    exponent = len(str(value.numerator)) - len(str(value.denominator))
    if value < power_of_ten(exponent):
        exponent -= 1
    scaled = value / power_of_ten(exponent)
    prefix_integer = (scaled.numerator * 10**digits) // scaled.denominator
    prefix = f"{prefix_integer // 10**digits}.{prefix_integer % 10**digits:0{digits}d}"
    return {
        "base10_exponent": exponent,
        "mantissa_lower_prefix": prefix,
        "fraction_sha256": fraction_sha256(value),
    }


def positive_interval_scientific(lo: Fraction, hi: Fraction) -> dict:
    if not 0 < lo <= hi:
        raise ValueError("expected a positive ordered interval")
    answer = positive_scientific(lo)
    answer["lower_fraction_sha256"] = answer.pop("fraction_sha256")
    answer["upper_fraction_sha256"] = fraction_sha256(hi)
    return answer


def record(n: int, s_lo: Fraction, s_hi: Fraction) -> dict:
    coefficients = primitive_solution(n, "machin")
    m = n + 1
    a_coefficients = coefficients[:m]
    b_coefficients = coefficients[m : 2 * m]
    c_coefficients = coefficients[2 * m :]
    raw_a = sum(a_coefficients)
    raw_b = sum(b_coefficients)
    raw_c = sum(c_coefficients)
    if raw_b == 0 or raw_c != raw_b:
        raise RuntimeError(f"n={n}: endpoint match/nonvanishing failed")

    endpoint_gcd = math.gcd(abs(raw_a), abs(raw_b))
    alpha = raw_a // endpoint_gcd
    beta = raw_b // endpoint_gcd
    effective_b_height = Fraction(max(map(abs, b_coefficients)), endpoint_gcd)
    effective_c_height = Fraction(max(map(abs, c_coefficients)), endpoint_gcd)

    K = 2 * n + 1
    exponential_bound = (
        effective_b_height
        * m
        * Fraction(K + 1, K * math.factorial(K))
    )
    # K is odd in the diagonal family.  The exact signed-tail integral gives
    # |U_K| <= 16/(K*5**K), improving the earlier coefficientwise constant 25.
    machin_bound = effective_c_height * m * Fraction(16, K * 5**K)
    total_bound = exponential_bound + machin_bound

    endpoints = sorted((Fraction(alpha) + beta * s_lo, Fraction(alpha) + beta * s_hi))
    lo, hi = endpoints
    if lo > 0:
        abs_lo, abs_hi = lo, hi
    elif hi < 0:
        abs_lo, abs_hi = -hi, -lo
    else:
        raise RuntimeError(f"n={n}: current rational enclosure does not certify nonzero")
    if abs_hi > total_bound:
        raise RuntimeError(f"n={n}: certified value exceeds proved tail bound")

    threshold_ratio = effective_c_height / 5 ** (2 * n)
    bound_to_value_ratio = total_bound / abs_lo
    return {
        "n": n,
        "vanishing_order": 3 * n + 1,
        "minimum_tail_index": K,
        "polynomial_vector_sha256": vector_sha256(coefficients),
        "primitive_polynomial_height_decimal_digits": len(
            str(max(map(abs, coefficients)))
        ),
        "raw_endpoint_gcd": endpoint_gcd,
        "primitive_endpoint_A_decimal_digits": len(str(abs(alpha))),
        "primitive_endpoint_B_decimal_digits": len(str(abs(beta))),
        "effective_B_coefficient_height": positive_scientific(effective_b_height),
        "effective_C_coefficient_height": positive_scientific(effective_c_height),
        "effective_C_height_over_5_to_2n": positive_scientific(threshold_ratio),
        "effective_C_height_exceeds_5_to_2n": threshold_ratio > 1,
        "exponential_tail_upper_bound": positive_scientific(exponential_bound),
        "machin_tail_upper_bound": positive_scientific(machin_bound),
        "total_tail_upper_bound": positive_scientific(total_bound),
        "total_tail_bound_below_one": total_bound < 1,
        "certified_endpoint_form_absolute_interval": positive_interval_scientific(
            abs_lo, abs_hi
        ),
        "certified_endpoint_form_nonzero": True,
        "tail_bound_verified_against_endpoint_interval": True,
        "tail_bound_to_certified_value_lower_ratio": positive_scientific(
            bound_to_value_ratio
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=18)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_n < 1:
        raise ValueError("max-n must be at least one")
    s_lo, s_hi = s_interval()
    result = {
        "construction": (
            "endpoint-matched diagonal type-I Hermite--Pade family for "
            "1, exp(z), and 16 atan(z/5)-4 atan(z/239)"
        ),
        "max_n": args.max_n,
        "tail_bound": (
            "after endpoint-gcd normalization: H_B*(n+1)*(K+1)/(K*K!) + "
            "H_C*(n+1)*16/(K*5^K), K=2n+1"
        ),
        "finite_scope_warning": (
            "Every degree record is exact, but trends through max_n are not "
            "extrapolated.  The all-degree tail identities and inequalities, "
            "not the observed height growth, are the proved statements."
        ),
        "records": [record(n, s_lo, s_hi) for n in range(1, args.max_n + 1)],
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
