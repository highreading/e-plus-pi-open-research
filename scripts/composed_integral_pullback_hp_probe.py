#!/usr/bin/env python3
"""Exact endpoint-matched HP probe for an improved integral-jet pullback.

Let

    phi(z) = z-z^3/6+5z^4/24-z^5/24

and

    G(z) = 4*atan(phi(z)/(2-phi(z))).

Then phi(0)=0, phi(1)=1, all derivatives of phi at zero are integers,
G(1)=pi, and all derivatives of G at zero are integers.  This script
constructs the diagonal endpoint-matched type-I Hermite--Pade systems for
1, exp(z), G(z) using exact integer/rational arithmetic.

The finite calculation is diagnostic; it proves no all-degree rank,
nonvanishing, or asymptotic theorem.
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


PHI = [
    Fraction(0),
    Fraction(1),
    Fraction(0),
    Fraction(-1, 6),
    Fraction(5, 24),
    Fraction(-1, 24),
]


def convolution(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def composed_jets(maximum: int) -> list[int]:
    """Return G^(k)(0), 0 <= k <= maximum, by exact rational division."""
    phi_prime = [k * PHI[k] for k in range(1, len(PHI))]
    numerator = [4 * value for value in phi_prime]
    square = convolution(PHI, PHI)
    denominator = square + [Fraction(0)] * max(0, len(PHI) - len(square))
    for k, value in enumerate(PHI):
        denominator[k] -= 2 * value
    denominator[0] += 2
    coefficients: list[Fraction] = []
    for r in range(maximum):
        rhs = numerator[r] if r < len(numerator) else Fraction(0)
        for j in range(1, min(r, len(denominator) - 1) + 1):
            rhs -= denominator[j] * coefficients[r - j]
        coefficients.append(rhs / denominator[0])
    jets = [0]
    for k in range(1, maximum + 1):
        value = coefficients[k - 1] * math.factorial(k - 1)
        assert value.denominator == 1
        jets.append(value.numerator)
    return jets


def falling(k: int, j: int) -> int:
    if j > k:
        return 0
    return math.factorial(k) // math.factorial(k - j)


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def high_matrix(n: int, jets: list[int]) -> sp.Matrix:
    rows: list[list[int]] = []
    for k in range(n + 1, 3 * n + 1):
        rows.append(
            [falling(k, j) for j in range(n + 1)]
            + [falling(k, j) * jets[k - j] for j in range(n + 1)]
        )
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return sp.Matrix(rows)


def reconstruct_triple(n: int, bc: list[int], jets: list[int]) -> list[int]:
    b = bc[: n + 1]
    c = bc[n + 1 :]
    a: list[sp.Rational] = []
    for k in range(n + 1):
        value = 0
        for j in range(k + 1):
            value += falling(k, j) * (b[j] + c[j] * jets[k - j])
        a.append(sp.Rational(-value, math.factorial(k)))
    return primitive_integer_vector(
        sp.Matrix(a + list(map(sp.Rational, b)) + list(map(sp.Rational, c)))
    )


def first_free(n: int, triple: list[int], jets: list[int]) -> sp.Rational:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    value = sp.Rational(0)
    for j in range(n + 1):
        value += sp.Rational(b[j] + c[j] * jets[k - j], math.factorial(k - j))
    return value


def cofactor_content(matrix: sp.Matrix, primitive_kernel: list[int]) -> int:
    for j, coordinate in enumerate(primitive_kernel):
        if coordinate:
            minor = matrix[:, :j].row_join(matrix[:, j + 1 :])
            determinant = int(DomainMatrix.from_Matrix(minor).det())
            signed = determinant if j % 2 == 0 else -determinant
            assert signed % coordinate == 0
            return abs(signed // coordinate)
    raise RuntimeError("zero kernel vector")


def record(
    n: int, jets: list[int], s_interval: tuple[Fraction, Fraction]
) -> dict:
    matrix = high_matrix(n, jets)
    domain = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain.rank()
    nullspace = domain.nullspace()
    nullity = nullspace.shape[0]
    result = {
        "n": n,
        "shape": list(matrix.shape),
        "rank": rank,
        "nullity": nullity,
    }
    if nullity != 1:
        return result
    bc = primitive_integer_vector(nullspace.to_Matrix().row(0).T)
    content = cofactor_content(matrix, bc)
    triple = reconstruct_triple(n, bc, jets)
    a = triple[: n + 1]
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    assert sum(b) == sum(c)
    endpoint_a = sum(a)
    endpoint_b = sum(b)
    endpoint_gcd = gcd(abs(endpoint_a), abs(endpoint_b))
    alpha = endpoint_a // endpoint_gcd if endpoint_gcd else 0
    beta = endpoint_b // endpoint_gcd if endpoint_gcd else 0
    free = first_free(n, triple, jets)
    result.update(
        {
            "primitive_high_kernel_sha256": hashlib.sha256(
                json.dumps(bc, separators=(",", ":")).encode()
            ).hexdigest(),
            "maximal_cofactor_common_content_digits": len(str(content)),
            "primitive_triple_height_digits": len(str(max(map(abs, triple)))),
            "primitive_triple_sha256": hashlib.sha256(
                json.dumps(triple, separators=(",", ":")).encode()
            ).hexdigest(),
            "raw_endpoint_pair": [endpoint_a, endpoint_b],
            "endpoint_gcd": endpoint_gcd,
            "reduced_endpoint_pair": [alpha, beta],
            "endpoint_interval_certificate": signed_interval_record(
                alpha, beta, *s_interval
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
    parser.add_argument("--max-n", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    jets = composed_jets(3 * args.max_n + 1)
    s_interval = e_plus_pi_interval()
    result = {
        "function": (
            "G(z)=4*atan(phi(z)/(2-phi(z))), "
            "phi=z-z^3/6+5z^4/24-z^5/24"
        ),
        "phi_derivative_jets": [1, 0, -1, 5, -5],
        "all_computed_G_jets_integral": True,
        "computed_G_jet_sha256": hashlib.sha256(
            json.dumps(jets, separators=(",", ":")).encode()
        ).hexdigest(),
        "records": [
            record(n, jets, s_interval) for n in range(1, args.max_n + 1)
        ],
        "warning": "Finite exact diagnostic only; no all-degree conclusion.",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
