#!/usr/bin/env python3
"""Exact finite probe for the positive derivative-kernel family.

All polynomial and coordinate calculations are exact Python-integer or
Fraction calculations.  Only ``matched_log10_abs`` is numerical; it is
computed twice at increasing mpmath precision and checked for stability.
The finite cases are evidence and regression tests, not the all-n proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

import mpmath as mp


A_BASE = 125_494_837


def content(values: list[int]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def evaluate(poly: list[int], x: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def divide_by_y_plus_s2(poly: list[int], s2: int, remainder: int) -> list[int]:
    """Return (poly(y)-remainder)/(y+s2), in ascending coefficients."""
    dividend = poly[:]
    dividend[0] -= remainder
    quotient = [0] * (len(dividend) - 1)
    quotient[-1] = dividend[-1]
    for j in range(len(dividend) - 2, 0, -1):
        quotient[j - 1] = dividend[j] - s2 * quotient[j]
    assert dividend[0] == s2 * quotient[0]
    return quotient


def derangements(maximum: int) -> list[int]:
    values = [1]
    if maximum:
        values.append(0)
    for j in range(2, maximum + 1):
        values.append((j - 1) * (values[-1] + values[-2]))
    return values


def stable_log10_abs(matched_constant: int, matched_coefficient: int) -> str:
    digits = max(len(str(abs(matched_constant))), len(str(matched_coefficient)))

    def compute(extra: int) -> str:
        mp.mp.dps = digits + extra
        value = mp.mpf(matched_constant) + mp.mpf(matched_coefficient) * (
            mp.e + mp.pi
        )
        assert value > 0
        return mp.nstr(mp.log10(value), 30)

    first = compute(80)
    second = compute(130)
    assert first == second
    return first


def exact_case(n: int) -> dict[str, object]:
    assert n > 0 and n % 2 == 0
    m = n // 2
    a = A_BASE**m
    b = 25**m
    delta = gcd(a - b, 57_096)
    expected_delta = 2_196 if m % 2 else 4_392
    assert delta == expected_delta

    u = (a - b) // delta
    v = (57_121 * a - 25 * b) // delta
    assert gcd(u, v) == 1

    # P_n(x)=sum_k coefficients[k] (x^2)^k.
    coefficients = [0] * (2 * n + 3)
    for j in range(n + 1):
        factor = (-1) ** j * comb(n, j)
        coefficients[n + j] += factor * v * v
        coefficients[n + j + 1] += factor * 2 * u * v
        coefficients[n + j + 2] += factor * u * u
    assert content(coefficients) == 1

    endpoint = 650**n * (57_096 * a // delta) ** 2
    assert evaluate(coefficients, -25) == endpoint
    assert evaluate(coefficients, -57_121) == endpoint

    subfactorials = derangements(4 * n + 4)
    q_raw = sum(
        coefficients[k] * subfactorials[2 * k]
        for k in range(len(coefficients))
    )
    p_raw = sum(
        coefficients[k] * factorial(2 * k)
        for k in range(len(coefficients))
    )
    assert p_raw > 0 and q_raw > 0
    e_content = gcd(p_raw, q_raw)
    p_primitive = p_raw // e_content
    q_primitive = q_raw // e_content
    assert gcd(p_primitive, q_primitive) == 1

    quotient_5 = divide_by_y_plus_s2(coefficients, 25, endpoint)
    quotient_239 = divide_by_y_plus_s2(coefficients, 57_121, endpoint)
    rational_part = sum(
        Fraction(80 * quotient_5[j] - 956 * quotient_239[j], 2 * j + 1)
        for j in range(len(quotient_5))
    )
    odd_lcm = 1
    for j in range(len(quotient_5)):
        odd_lcm = lcm(odd_lcm, 2 * j + 1)
    assert (odd_lcm * rational_part).denominator == 1
    pi_a_pre = int(odd_lcm * rational_part)
    pi_b_pre = odd_lcm * endpoint
    pi_content = gcd(abs(pi_a_pre), pi_b_pre)
    pi_a = pi_a_pre // pi_content
    pi_b = pi_b_pre // pi_content
    assert pi_b > 0 and gcd(abs(pi_a), pi_b) == 1

    match_gcd = gcd(q_primitive, pi_b)
    q0 = q_primitive // match_gcd
    b0 = pi_b // match_gcd
    matched_constant_pre = -b0 * p_primitive + q0 * pi_a
    matched_coefficient_pre = match_gcd * q0 * b0
    final_content = gcd(abs(matched_constant_pre), matched_coefficient_pre)
    assert final_content <= match_gcd and match_gcd % final_content == 0
    matched_constant = matched_constant_pre // final_content
    matched_coefficient = matched_coefficient_pre // final_content

    return {
        "n": n,
        "m": m,
        "interpolation": {
            "a": str(a),
            "b": str(b),
            "delta": delta,
            "u": str(u),
            "v": str(v),
            "primitive_polynomial_content": content(coefficients),
            "common_endpoint_value": str(endpoint),
        },
        "e_pair": {
            "p_raw": str(p_raw),
            "q_raw": str(q_raw),
            "content": str(e_content),
            "p_primitive": str(p_primitive),
            "q_primitive": str(q_primitive),
        },
        "pi_pair": {
            "rational_part_numerator": str(rational_part.numerator),
            "rational_part_denominator": str(rational_part.denominator),
            "odd_lcm": str(odd_lcm),
            "a_pre": str(pi_a_pre),
            "b_pre": str(pi_b_pre),
            "content": str(pi_content),
            "a_primitive": str(pi_a),
            "b_primitive": str(pi_b),
        },
        "minimal_matching": {
            "coefficient_gcd": str(match_gcd),
            "constant_pre": str(matched_constant_pre),
            "coefficient_pre": str(matched_coefficient_pre),
            "final_content": str(final_content),
            "constant_primitive": str(matched_constant),
            "coefficient_primitive": str(matched_coefficient),
            "matched_log10_abs": stable_log10_abs(
                matched_constant, matched_coefficient
            ),
        },
        "coordinate_digest_sha256": hashlib.sha256(
            (
                f"{p_raw}|{q_raw}|{rational_part.numerator}|"
                f"{rational_part.denominator}|{endpoint}|{matched_constant}|"
                f"{matched_coefficient}"
            ).encode("ascii")
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/positive_derivative_kernel_probe.json"),
    )
    parser.add_argument("--max-n", type=int, default=20)
    args = parser.parse_args()
    if args.max_n < 2 or args.max_n % 2:
        parser.error("--max-n must be a positive even integer at least 2")

    cases = [exact_case(n) for n in range(2, args.max_n + 1, 2)]
    payload = {
        "schema": "positive-derivative-kernel-probe-v1",
        "scope": (
            "Finite exact coordinate and normalization regression test only; "
            "the all-n divergence proof is in the companion source note."
        ),
        "exact_arithmetic": True,
        "numerical_fields": ["minimal_matching.matched_log10_abs"],
        "max_n": args.max_n,
        "case_count": len(cases),
        "all_final_contents_one": all(
            case["minimal_matching"]["final_content"] == "1" for case in cases
        ),
        "cases": cases,
    }
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
