#!/usr/bin/env python3
"""Exact finite probe of two natural mixed Hermite--Pade constructions.

For a chosen n, find polynomials A,B,C of degree at most n such that

    A(z) + B(z) exp(z) + C(z) F(z) = O(z**(3*n+1))

and impose the endpoint condition which makes the value at z=1 an integer
linear form in e+pi.  Two choices are tested:

* F(z)=atan(z), with C(1)=4 B(1);
* F(z)=16 atan(z/5)-4 atan(z/239), with C(1)=B(1).

The linear systems and normalization are exact over Q.  Exact rational bounds
for e+pi then certify whether the primitive endpoint form is nonzero and
whether its absolute value is below 1.  These are finite diagnostics only;
failure of these ansatzes does not rule out another auxiliary construction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as sp

sys.set_int_max_str_digits(0)


def e_interval(n: int) -> tuple[F, F]:
    partial = sum((F(1, math.factorial(k)) for k in range(n + 1)), F())
    return partial, partial + F(1, n * math.factorial(n))


def atan_interval(inv: int, last_index: int) -> tuple[F, F]:
    partial = sum(
        ((-1 if k & 1 else 1) * F(1, (2 * k + 1) * inv ** (2 * k + 1))
         for k in range(last_index + 1)),
        F(),
    )
    omitted = F(1, (2 * last_index + 3) * inv ** (2 * last_index + 3))
    return (partial, partial + omitted) if last_index & 1 else (partial - omitted, partial)


def s_interval() -> tuple[F, F]:
    e_lo, e_hi = e_interval(1200)
    a_lo, a_hi = atan_interval(5, 1700)
    b_lo, b_hi = atan_interval(239, 400)
    return e_lo + 16 * a_lo - 4 * b_hi, e_hi + 16 * a_hi - 4 * b_lo


def f_coefficient(kind: str, k: int) -> sp.Rational:
    if k < 1 or not k & 1:
        return sp.Rational(0)
    sign = -1 if ((k - 1) // 2) & 1 else 1
    if kind == "direct":
        return sp.Rational(sign, k)
    if kind == "machin":
        return sp.Rational(sign, k) * (
            sp.Rational(16, 5**k) - sp.Rational(4, 239**k)
        )
    raise ValueError(kind)


def primitive_solution(n: int, kind: str) -> list[int]:
    variables = 3 * (n + 1)
    rows: list[list[sp.Rational]] = []
    for k in range(3 * n + 1):
        row = [sp.Rational(0) for _ in range(variables)]
        if k <= n:
            row[k] = 1
        for j in range(n + 1):
            if k >= j:
                row[n + 1 + j] = sp.Rational(1, sp.factorial(k - j))
                row[2 * (n + 1) + j] = f_coefficient(kind, k - j)
        rows.append(row)

    # At z=1: C(1)=4B(1) in the direct model and C(1)=B(1) in Machin's.
    endpoint_multiplier = 4 if kind == "direct" else 1
    row = [sp.Rational(0) for _ in range(variables)]
    for j in range(n + 1):
        row[n + 1 + j] = -endpoint_multiplier
        row[2 * (n + 1) + j] = 1
    rows.append(row)

    basis = sp.Matrix(rows).nullspace()
    if len(basis) != 1:
        raise RuntimeError(f"expected nullity 1, obtained {len(basis)}")
    vector = basis[0]
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    # Fix a deterministic sign.
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def scientific_bounds(lo: F, hi: F) -> dict[str, str | int]:
    """Compact exact description of a positive interval."""
    assert 0 < lo <= hi
    # A floor log10 is used only as a scale description; exact hashes remain.
    exponent = len(str(lo.numerator)) - len(str(lo.denominator))

    def power_of_ten(k: int) -> F:
        return F(10**k) if k >= 0 else F(1, 10 ** (-k))

    if lo < power_of_ten(exponent):
        exponent -= 1
    scale = power_of_ten(exponent)
    lower_mantissa = lo / scale
    upper_mantissa = hi / scale
    digits = 12

    def decimal_prefix(x: F) -> str:
        scaled = x * 10**digits
        return f"{scaled.numerator // scaled.denominator / 10**digits:.12f}"

    return {
        "base10_exponent": exponent,
        "lower_mantissa_prefix": decimal_prefix(lower_mantissa),
        "upper_mantissa_prefix": decimal_prefix(upper_mantissa),
        "lower_fraction_sha256": hashlib.sha256(f"{lo.numerator}/{lo.denominator}".encode()).hexdigest(),
        "upper_fraction_sha256": hashlib.sha256(f"{hi.numerator}/{hi.denominator}".encode()).hexdigest(),
    }


def p_adic_valuation(value: int, prime: int) -> int | None:
    if value == 0:
        return None
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def record(n: int, kind: str, s_lo: F, s_hi: F) -> dict:
    coeffs = primitive_solution(n, kind)
    raw_a = sum(coeffs[: n + 1])
    raw_b = sum(coeffs[n + 1 : 2 * (n + 1)])
    raw_c = sum(coeffs[2 * (n + 1) :])
    endpoint_multiplier = 4 if kind == "direct" else 1
    assert raw_c == endpoint_multiplier * raw_b
    # Irrationality needs only the two endpoint coefficients to be integral.
    # Their gcd may be removed even when it does not divide every polynomial
    # coefficient.  Omitting this second reduction would over-scale the form.
    endpoint_common_factor = gcd(abs(raw_a), abs(raw_b))
    if endpoint_common_factor == 0:
        raise RuntimeError("zero endpoint form")
    a = raw_a // endpoint_common_factor
    b = raw_b // endpoint_common_factor
    c = raw_c // endpoint_common_factor
    endpoints = sorted((F(a) + b * s_lo, F(a) + b * s_hi))
    lo, hi = endpoints
    nonzero = hi < 0 or lo > 0
    if not nonzero:
        absolute = None
    elif hi < 0:
        absolute = scientific_bounds(-hi, -lo)
    else:
        absolute = scientific_bounds(lo, hi)
    first_unconstrained_index = 3 * n + 1
    first_unconstrained_coefficient = sp.Rational(0)
    for j in range(n + 1):
        first_unconstrained_coefficient += (
            coeffs[n + 1 + j]
            * sp.Rational(1, sp.factorial(first_unconstrained_index - j))
            + coeffs[2 * (n + 1) + j]
            * f_coefficient(kind, first_unconstrained_index - j)
        )
    return {
        "n": n,
        "enforced_vanishing_order_at_least": 3 * n + 1,
        "first_unconstrained_taylor_coefficient": {
            "index": first_unconstrained_index,
            "numerator": int(first_unconstrained_coefficient.p),
            "denominator": int(first_unconstrained_coefficient.q),
        },
        "certified_exact_vanishing_order_at_zero": (
            first_unconstrained_index if first_unconstrained_coefficient else None
        ),
        "primitive_max_polynomial_coefficient_decimal_digits": len(str(max(map(abs, coeffs)))),
        "raw_endpoint_A_from_primitive_integer_polynomials": raw_a,
        "raw_endpoint_B_from_primitive_integer_polynomials": raw_b,
        "raw_endpoint_C_from_primitive_integer_polynomials": raw_c,
        "endpoint_common_factor_removed": endpoint_common_factor,
        "primitive_endpoint_A": a,
        "primitive_endpoint_B": b,
        "primitive_endpoint_C": c,
        "primitive_endpoint_A_239_adic_valuation": p_adic_valuation(a, 239),
        "primitive_endpoint_B_239_adic_valuation": p_adic_valuation(b, 239),
        "endpoint_form_after_endpoint_gcd_reduction": "A + B*(e+pi)",
        "certified_nonzero": nonzero,
        "certified_absolute_value_below_one": nonzero and -1 < lo and hi < 1,
        "absolute_value_interval": absolute,
        "primitive_vector_sha256": hashlib.sha256(
            json.dumps(coeffs, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    s_lo, s_hi = s_interval()
    result = {
        "construction": (
            "type-I Hermite--Pade for 1, exp(z), and an arctangent function, "
            "plus an endpoint coefficient-matching constraint"
        ),
        "models": {
            kind: [record(n, kind, s_lo, s_hi) for n in range(1, args.max_n + 1)]
            for kind in ("direct", "machin")
        },
        "warning": (
            "This exact finite audit tests only the stated ansatz. It proves neither "
            "irrationality nor an impossibility theorem for other constructions."
        ),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True).encode()
    rendered = encoded.decode() + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
