#!/usr/bin/env python3
"""Exact finite probe for quadratic rational pullbacks of 4*atan.

For an integer p >= 2, set

    u_p(z) = (p-1)z/(p-z^2),   F_p(z) = 4*atan(u_p(z)).

Then F_p(0)=0 and F_p(1)=pi.  This script constructs the diagonal
endpoint-matched type-I Hermite--Pade system

    A + B exp(z) + C F_p(z) = O(z^(3n+1)),  C(1)=B(1),

using exact rational arithmetic.  The calculation is diagnostic only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from mobius_arctan_hp_probe import e_plus_pi_interval, signed_interval_record

sys.set_int_max_str_digits(0)


def falling(k: int, j: int) -> int:
    if j > k:
        return 0
    return math.factorial(k) // math.factorial(k - j)


def derivative_jets(p: int, maximum: int) -> list[Fraction]:
    """Return F_p^(k)(0), 0 <= k <= maximum, from its rational derivative."""
    # F_p'(z) = 4(p-1)(p+z^2) /
    #           (z^4+(p^2-4p+1)z^2+p^2).
    coefficient = [Fraction(0) for _ in range(maximum)]
    a = p * p - 4 * p + 1
    for m in range((maximum - 1) // 2 + 1):
        rhs = Fraction(4 * p * (p - 1) if m == 0 else 4 * (p - 1) if m == 1 else 0)
        if m >= 1:
            rhs -= a * coefficient[2 * (m - 1)]
        if m >= 2:
            rhs -= coefficient[2 * (m - 2)]
        coefficient[2 * m] = rhs / (p * p)
    jets = [Fraction(0) for _ in range(maximum + 1)]
    for k in range(1, maximum + 1):
        jets[k] = coefficient[k - 1] * math.factorial(k - 1)
    return jets


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def rational_high_matrix(n: int, jets: list[Fraction]) -> sp.Matrix:
    rows: list[list[sp.Rational]] = []
    for k in range(n + 1, 3 * n + 1):
        rows.append(
            [sp.Rational(falling(k, j)) for j in range(n + 1)]
            + [
                sp.Rational(
                    falling(k, j) * jets[k - j].numerator,
                    jets[k - j].denominator,
                )
                for j in range(n + 1)
            ]
        )
    rows.append([sp.Rational(-1)] * (n + 1) + [sp.Rational(1)] * (n + 1))
    return sp.Matrix(rows)


def reconstruct_primitive_triple(
    n: int, bc: list[int], jets: list[Fraction]
) -> list[int]:
    b = bc[: n + 1]
    c = bc[n + 1 :]
    a: list[sp.Rational] = []
    for k in range(n + 1):
        jet = sp.Rational(0)
        for j in range(k + 1):
            jet += falling(k, j) * b[j]
            value = jets[k - j]
            jet += sp.Rational(
                falling(k, j) * c[j] * value.numerator, value.denominator
            )
        a.append(-jet / math.factorial(k))
    vector = sp.Matrix(a + list(map(sp.Rational, b)) + list(map(sp.Rational, c)))
    return primitive_integer_vector(vector)


def first_free_coefficient(
    n: int, triple: list[int], jets: list[Fraction]
) -> sp.Rational:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    value = sp.Rational(0)
    for j in range(n + 1):
        value += sp.Rational(b[j], math.factorial(k - j))
        tau = jets[k - j]
        value += sp.Rational(c[j] * tau.numerator, tau.denominator * math.factorial(k - j))
    return value


def record(
    p: int, n: int, s_interval: tuple[Fraction, Fraction]
) -> dict:
    jets = derivative_jets(p, 3 * n + 1)
    matrix = rational_high_matrix(n, jets)
    domain_matrix = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain_matrix.rank()
    nullspace = domain_matrix.nullspace()
    nullity = nullspace.shape[0]
    result = {
        "p": p,
        "n": n,
        "rank": rank,
        "nullity": nullity,
        "shape": list(matrix.shape),
    }
    if nullity != 1:
        return result
    bc = primitive_integer_vector(nullspace.to_Matrix().row(0).T)
    triple = reconstruct_primitive_triple(n, bc, jets)
    a = triple[: n + 1]
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    assert sum(b) == sum(c)
    endpoint_a = sum(a)
    endpoint_b = sum(b)
    endpoint_gcd = gcd(abs(endpoint_a), abs(endpoint_b))
    reduced_a = endpoint_a // endpoint_gcd if endpoint_gcd else 0
    reduced_b = endpoint_b // endpoint_gcd if endpoint_gcd else 0
    free = first_free_coefficient(n, triple, jets)
    result.update(
        {
            "primitive_triple_height_digits": len(str(max(map(abs, triple)))),
            "primitive_triple_sha256": hashlib.sha256(
                json.dumps(triple, separators=(",", ":")).encode()
            ).hexdigest(),
            "endpoint_pair": [endpoint_a, endpoint_b],
            "endpoint_gcd": endpoint_gcd,
            "reduced_endpoint_pair": [reduced_a, reduced_b],
            "endpoint_interval_certificate": signed_interval_record(
                reduced_a, reduced_b, *s_interval
            ),
            "reduced_endpoint_height_digits": len(
                str(max(abs(reduced_a), abs(reduced_b)))
            ),
            "first_free": {
                "index": 3 * n + 1,
                "numerator": int(free.p),
                "denominator": int(free.q),
                "nonzero": bool(free),
            },
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--max-n", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if any(p < 2 for p in args.p):
        raise ValueError("all p must be at least 2")
    s_interval = e_plus_pi_interval()
    result = {
        "family": "F_p(z)=4*atan((p-1)z/(p-z^2)), F_p(1)=pi",
        "records": [
            record(p, n, s_interval)
            for p in args.p
            for n in range(1, args.max_n + 1)
        ],
        "warning": "Finite exact diagnostic only; no asymptotic claim is made.",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
