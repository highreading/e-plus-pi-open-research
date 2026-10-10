#!/usr/bin/env python3
"""Independent exact regression audit for the positive derivative kernel.

This deliberately uses SymPy expansion and Euclidean polynomial division,
rather than the coefficient-building and synthetic-division recurrences in
``positive_derivative_kernel_probe.py``.  It compares the resulting exact
coordinates with the frozen primary regression file.  Numerical evaluation
of e or pi is neither used nor needed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial, gcd, lcm
from pathlib import Path

from sympy import Poly, Rational, div, expand, symbols


A_BASE = 13**3 * 239**2
Y = symbols("y")


def derangement_by_series(j: int) -> int:
    value = factorial(j) * sum(
        Fraction((-1) ** r, factorial(r)) for r in range(j + 1)
    )
    assert value.denominator == 1
    return value.numerator


def exact_case(reference: dict[str, object]) -> dict[str, object]:
    n = int(reference["n"])
    assert n > 0 and n % 2 == 0
    m = n // 2
    a = A_BASE**m
    b = 25**m
    delta = gcd(a - b, 57_096)
    assert delta == (2_196 if m % 2 else 4_392)

    u = (a - b) // delta
    v = (57_121 * a - 25 * b) // delta
    assert gcd(u, v) == 1

    # Work in y=x^2.  SymPy, not a hand-coded convolution, expands F_n(y).
    polynomial = Poly(
        expand(Y**n * (1 - Y) ** n * (u * Y + v) ** 2),
        Y,
        domain="ZZ",
    )
    assert polynomial.content() == 1
    assert polynomial.degree() == 2 * n + 2

    endpoint = 650**n * (57_096 * a // delta) ** 2
    assert polynomial.eval(-25) == endpoint
    assert polynomial.eval(-57_121) == endpoint

    # Use SymPy's Euclidean division independently at the two poles.
    numerator = polynomial - Poly(endpoint, Y, domain="ZZ")
    quotient_5, remainder_5 = div(
        numerator, Poly(Y + 25, Y, domain="ZZ"), domain="ZZ"
    )
    quotient_239, remainder_239 = div(
        numerator, Poly(Y + 57_121, Y, domain="ZZ"), domain="ZZ"
    )
    assert remainder_5.is_zero and remainder_239.is_zero

    coefficients = {
        monomial[0]: int(coefficient)
        for monomial, coefficient in polynomial.terms()
    }
    p_raw = sum(
        coefficient * factorial(2 * k)
        for k, coefficient in coefficients.items()
    )
    q_raw = sum(
        coefficient * derangement_by_series(2 * k)
        for k, coefficient in coefficients.items()
    )
    assert p_raw > 0 and q_raw > 0

    rational_part = Rational(0)
    for (monomial,), coefficient in quotient_5.terms():
        rational_part += Rational(80 * int(coefficient), 2 * monomial + 1)
    for (monomial,), coefficient in quotient_239.terms():
        rational_part -= Rational(956 * int(coefficient), 2 * monomial + 1)

    odd_lcm = 1
    for j in range(2 * n + 2):
        odd_lcm = lcm(odd_lcm, 2 * j + 1)
    pi_a_pre = int(odd_lcm * rational_part)
    pi_b_pre = odd_lcm * endpoint
    pi_content = gcd(abs(pi_a_pre), pi_b_pre)
    pi_a = pi_a_pre // pi_content
    pi_b = pi_b_pre // pi_content
    assert gcd(abs(pi_a), pi_b) == 1

    e_content = gcd(p_raw, q_raw)
    p_primitive = p_raw // e_content
    q_primitive = q_raw // e_content
    assert gcd(p_primitive, q_primitive) == 1

    matching_gcd = gcd(q_primitive, pi_b)
    q_zero = q_primitive // matching_gcd
    b_zero = pi_b // matching_gcd
    matched_constant = -b_zero * p_primitive + q_zero * pi_a
    matched_coefficient = matching_gcd * q_zero * b_zero
    final_content = gcd(abs(matched_constant), matched_coefficient)

    # This tests the prime-power content assertion, including its exact
    # coprimality precursor, rather than merely checking a square-free bound.
    assert gcd(matched_constant, q_zero * b_zero) == 1
    assert matching_gcd % final_content == 0

    primary_e = reference["e_pair"]
    primary_pi = reference["pi_pair"]
    primary_match = reference["minimal_matching"]
    assert str(p_raw) == primary_e["p_raw"]
    assert str(q_raw) == primary_e["q_raw"]
    assert str(rational_part.p) == primary_pi["rational_part_numerator"]
    assert str(rational_part.q) == primary_pi["rational_part_denominator"]
    assert str(odd_lcm) == primary_pi["odd_lcm"]
    assert str(endpoint) == reference["interpolation"]["common_endpoint_value"]
    assert str(matching_gcd) == primary_match["coefficient_gcd"]
    assert str(final_content) == primary_match["final_content"]

    digest = hashlib.sha256(
        (
            f"{p_raw}|{q_raw}|{rational_part.p}|{rational_part.q}|"
            f"{endpoint}|{matched_constant // final_content}|"
            f"{matched_coefficient // final_content}"
        ).encode("ascii")
    ).hexdigest()
    assert digest == reference["coordinate_digest_sha256"]

    return {
        "n": n,
        "delta": delta,
        "polynomial_degree_in_y": polynomial.degree(),
        "primitive_q_decimal_digits": len(str(q_primitive)),
        "primitive_pi_b_decimal_digits": len(str(pi_b)),
        "matching_gcd": str(matching_gcd),
        "final_content": str(final_content),
        "coordinate_digest_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--primary",
        type=Path,
        default=Path("results/positive_derivative_kernel_probe.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/positive_derivative_kernel_divergence.md"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/independent_positive_derivative_kernel_audit.json"
        ),
    )
    args = parser.parse_args()

    primary = json.loads(args.primary.read_text(encoding="utf-8"))
    cases = [exact_case(case) for case in primary["cases"]]
    payload = {
        "schema": "independent-positive-derivative-kernel-audit-v1",
        "scope": (
            "Independent exact SymPy expansion/division regression; the "
            "all-n theorem is checked mathematically in the audit note."
        ),
        "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
        "primary_result_sha256": hashlib.sha256(
            args.primary.read_bytes()
        ).hexdigest(),
        "case_count": len(cases),
        "all_exact_coordinate_digests_match": True,
        "all_final_contents_one": all(
            case["final_content"] == "1" for case in cases
        ),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
