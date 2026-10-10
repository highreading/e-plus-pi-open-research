#!/usr/bin/env python3
"""Exact finite audit of the conjectural uniform 2-adic deflation law.

This is evidence, not an infinite proof.  It constructs the exact rational
two-state determinant, changes from x=2m to z=(5x+b)/2, divides the known
universal half-integer-root product and 2^(b-3), and checks the resulting
polynomial modulo 2.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "_sympy"))

import sympy as sp

try:
    import mixed_cubic_moving_ray_y5_minus_y_certificate as base
except ImportError:  # Standalone work-directory replay before archiving.
    import moving_ray_y5_minus_y_certificate as base


X, Z = sp.symbols("x z")


def determinant_in_x(intercept: int, parity: int) -> sp.Poly:
    coefficients = base.determinant_polynomial(intercept, parity)
    expression = sum(
        sp.Rational(value.numerator, value.denominator) * (X / 2) ** degree
        for degree, value in enumerate(coefficients)
    )
    return sp.Poly(expression, X, domain=sp.QQ)


def universal_product(intercept: int) -> sp.Poly:
    expression = sp.Integer(1)
    for odd in range(1, intercept - 1, 2):
        expression *= X**2 - odd**2
    for odd in range(1, intercept - 3, 2):
        if 2 * odd > intercept:
            expression *= X + odd
    return sp.Poly(expression, X, domain=sp.QQ)


def expected_mod_two(intercept: int) -> sp.Poly:
    if intercept % 4 == 3:
        h = (intercept - 3) // 4
        expression = (1 + Z) ** h
    else:
        h = (intercept - 1) // 4
        expression = (1 + Z) ** h + Z**h
    return sp.Poly(expression, Z, modulus=2)


def check_row(intercept: int, parity: int) -> dict[str, object]:
    determinant = determinant_in_x(intercept, parity)
    universal = universal_product(intercept)
    quotient_x = determinant.exquo(universal)
    quotient_z = sp.Poly(
        sp.expand(quotient_x.as_expr().subs(X, (2 * Z - intercept) / 5)),
        Z,
        domain=sp.QQ,
    )
    normalized = sp.Poly(
        quotient_z.as_expr() / 2 ** (intercept - 3), Z, domain=sp.QQ
    )

    low_coefficients = list(reversed(normalized.all_coeffs()))
    assert all(int(value.q) % 2 == 1 for value in low_coefficients)
    observed_mod_two = sp.Poly(
        sum((int(value.p) & 1) * Z**index for index, value in enumerate(low_coefficients)),
        Z,
        modulus=2,
    )
    expected = expected_mod_two(intercept)
    assert observed_mod_two == expected
    assert int(low_coefficients[0].p) & 1 == 1

    bitmask = sum(
        (int(value.p) & 1) << index
        for index, value in enumerate(low_coefficients)
    )
    return {
        "intercept": intercept,
        "parity": "even" if parity == 0 else "odd",
        "determinant_degree": determinant.degree(),
        "universal_degree": universal.degree(),
        "deflated_degree": normalized.degree(),
        "mod_two_bitmask_low_to_high": hex(bitmask),
        "constant_term_is_2_adic_unit": True,
    }


def run(max_b: int) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    stream = hashlib.sha256()
    # b=3 is an elementary edge case whose determinant degrees are below
    # the stable universal-product range; it is proved separately.
    for intercept in range(7, max_b + 1, 2):
        if intercept % 5 == 0:
            continue
        for parity in (0, 1):
            row = check_row(intercept, parity)
            rows.append(row)
            stream.update(
                (
                    f"{intercept}:{parity}:"
                    f"{row['mod_two_bitmask_low_to_high']}\n"
                ).encode()
            )
    return {
        "status": "finite exact evidence; not a uniform theorem",
        "max_intercept": max_b,
        "parity_rows": len(rows),
        "claim_tested": (
            "After x=2m, z=(5x+b)/2, division by U_b(x) and 2^(b-3), "
            "both parity determinants are 2-integral and reduce to "
            "(1+z)^h for b=4h+3, or (1+z)^h+z^h for b=4h+1."
        ),
        "stream_sha256": stream.hexdigest(),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=101)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "moving_ray_uniform_2adic_conjecture_b101.json",
    )
    arguments = parser.parse_args()
    payload = run(arguments.max_b)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    arguments.output.write_bytes(serialized.encode("utf-8"))
    print(arguments.output)


if __name__ == "__main__":
    main()
