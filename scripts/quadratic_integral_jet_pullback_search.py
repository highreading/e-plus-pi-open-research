#!/usr/bin/env python3
"""Finite search for unusually large-radius integral-jet arctan pullbacks.

Search

    u(z) = z(A+Bz)/(C+Dz+Ez^2),   A+B=C+D+E,

with primitive integer parameters, C>0, and no denominator zero on [0,1].
For each candidate, expand F'(z)=4u'(z)/(1+u(z)^2) exactly and require
F^(k)(0) integral through a requested finite order.  The reported singular
radius is the minimum modulus of a solution of u(z)=+i or u(z)=-i.

This is a finite diagnostic only: passing finitely many jet tests is not an
all-order integrality theorem, and absence from the search box is not a
classification theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def polynomial_subtract(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        (left[k] if k < len(left) else 0)
        - (right[k] if k < len(right) else 0)
        for k in range(size)
    ]


def derivative_rational_polynomials(
    a: int, b: int, c: int, d: int, e: int
) -> tuple[list[int], list[int]]:
    numerator = [0, a, b]
    denominator = [c, d, e]
    numerator_prime = [a, 2 * b]
    denominator_prime = [d, 2 * e]
    top = [
        4 * x
        for x in polynomial_subtract(
            convolution(numerator_prime, denominator),
            convolution(numerator, denominator_prime),
        )
    ]
    bottom_left = convolution(denominator, denominator)
    bottom_right = convolution(numerator, numerator)
    size = max(len(bottom_left), len(bottom_right))
    bottom = [
        (bottom_left[k] if k < len(bottom_left) else 0)
        + (bottom_right[k] if k < len(bottom_right) else 0)
        for k in range(size)
    ]
    return top, bottom


def integral_jets(
    top: list[int], bottom: list[int], jet_order: int
) -> tuple[bool, list[int]]:
    """Test F^(1)(0),...,F^(jet_order)(0) and return those integer jets."""
    coefficients: list[Fraction] = []
    jets: list[int] = []
    factorial = 1
    for r in range(jet_order):
        if r:
            factorial *= r
        rhs = Fraction(top[r] if r < len(top) else 0)
        for j in range(1, min(r, len(bottom) - 1) + 1):
            rhs -= bottom[j] * coefficients[r - j]
        coefficient = rhs / bottom[0]
        coefficients.append(coefficient)
        jet = coefficient * factorial
        if jet.denominator != 1:
            return False, jets
        jets.append(jet.numerator)
    return True, jets


def denominator_nonzero_unit_interval(c: int, d: int, e: int) -> bool:
    values = [c, c + d + e]
    if e and 0 < -d / (2 * e) < 1:
        x = Fraction(-d, 2 * e)
        values.append(Fraction(c) + d * x + e * x * x)
    return min(values) > 0 or max(values) < 0


def singular_radius(a: int, b: int, c: int, d: int, e: int) -> float:
    radii: list[float] = []
    for sign in (1, -1):
        # A z+B z^2 = sign*i(C+D z+E z^2).
        coefficients = [
            complex(b, -sign * e),
            complex(a, -sign * d),
            complex(0, -sign * c),
        ]
        while coefficients and abs(coefficients[0]) == 0:
            coefficients.pop(0)
        for root in np.roots(coefficients):
            radii.append(float(abs(root)))
    return min(radii)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--range", dest="coefficient_range", type=int, default=16)
    parser.add_argument("--c", type=int, nargs="+", default=[1, 2, 4, 8, 16])
    parser.add_argument("--jet-order", type=int, default=25)
    parser.add_argument("--radius-threshold", type=float, default=math.sqrt(2))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    bound = args.coefficient_range
    tested = 0
    reducible_skipped = 0
    integral_count = 0
    hits: list[dict] = []
    for c in args.c:
        if c <= 0:
            raise ValueError("the normalized constant denominator C must be positive")
        for a in range(-bound, bound + 1):
            if not a:
                continue
            for d in range(-bound, bound + 1):
                for e in range(-bound, bound + 1):
                    b = c + d + e - a
                    if abs(b) > bound or a + b == 0:
                        continue
                    if math.gcd(math.gcd(math.gcd(math.gcd(abs(a), abs(b)), c), abs(d)), abs(e)) != 1:
                        continue
                    # Apart from the factor z, the numerator has root -A/B.
                    # Since C is nonzero, a common factor exists exactly when
                    # the denominator also vanishes there.
                    if b and c * b * b - d * a * b + e * a * a == 0:
                        reducible_skipped += 1
                        continue
                    if not denominator_nonzero_unit_interval(c, d, e):
                        continue
                    tested += 1
                    top, bottom = derivative_rational_polynomials(a, b, c, d, e)
                    integral, jets = integral_jets(top, bottom, args.jet_order)
                    if not integral:
                        continue
                    integral_count += 1
                    radius = singular_radius(a, b, c, d, e)
                    if radius > args.radius_threshold + 1e-12:
                        hits.append(
                            {
                                "radius": radius,
                                "parameters": {"A": a, "B": b, "C": c, "D": d, "E": e},
                                "jet_sha256": hashlib.sha256(
                                    json.dumps(jets, separators=(",", ":")).encode()
                                ).hexdigest(),
                            }
                        )
    hits.sort(key=lambda item: item["radius"], reverse=True)
    result = {
        "box": {
            "coefficient_range": bound,
            "C_values": args.c,
            "jet_order": args.jet_order,
            "radius_threshold": args.radius_threshold,
        },
        "primitive_candidates_with_safe_real_path_tested": tested,
        "reducible_parameterizations_skipped": reducible_skipped,
        "candidates_integral_through_tested_jet_order": integral_count,
        "hits": hits,
        "warning": (
            "Finite search only. Passing the jet test is not an all-order theorem; "
            "absence is only within the displayed parameter box."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
