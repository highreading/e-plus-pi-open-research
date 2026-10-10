#!/usr/bin/env python3
"""Exact finite cross-check for the all-degree Machin rank proof.

This is not the proof: the proof is in
``sources/machin_bordered_rank_proof.md``.  For each requested n this
script constructs the reduced 2n-by-2n matrix after B=(z-1)B~ and
C=(z-1)C~, once with atan(z) and once with G(z)/4.  It computes both
determinants over Fraction and checks that they are nonzero and have the
same 2-adic valuation, as predicted by the proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial


def valuation_2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("the 2-adic valuation of zero is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def valuation_2(value: Fraction) -> int:
    return valuation_2_integer(value.numerator) - valuation_2_integer(
        value.denominator
    )


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    work = [row[:] for row in matrix]
    answer = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            answer = -answer
        pivot_value = work[column][column]
        answer *= pivot_value
        for j in range(column, size):
            work[column][j] /= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column]
            if multiplier:
                for j in range(column, size):
                    work[row][j] -= multiplier * work[column][j]
    return answer


def raw_coefficient(index: int) -> Fraction:
    if index <= 0 or index % 2 == 0:
        return Fraction(0)
    return (-1) ** ((index - 1) // 2) * Fraction(1, index)


def machin_normalized_coefficient(index: int) -> Fraction:
    """Coefficient of G(z)/4 = 4 atan(z/5) - atan(z/239)."""
    if index <= 0 or index % 2 == 0:
        return Fraction(0)
    sign = (-1) ** ((index - 1) // 2)
    return sign * Fraction(
        4 * 239**index - 5**index,
        index * 5**index * 239**index,
    )


def reduced_determinant(n: int, kind: str) -> Fraction:
    coefficient = (
        raw_coefficient if kind == "raw" else machin_normalized_coefficient
    )
    rows: list[list[Fraction]] = []
    for k in range(n + 1, 3 * n + 1):
        exponential = [
            Fraction(k - a - 1, factorial(k - a)) for a in range(n)
        ]
        arctangent = [
            coefficient(k - a - 1) - coefficient(k - a)
            for a in range(n)
        ]
        rows.append(exponential + arctangent)
    return determinant(rows)


def fraction_digest(value: Fraction) -> str:
    encoded = f"{value.numerator}/{value.denominator}".encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=8)
    args = parser.parse_args()
    if args.max_n < 1:
        raise SystemExit("--max-n must be positive")

    records = []
    for n in range(1, args.max_n + 1):
        raw = reduced_determinant(n, "raw")
        machin = reduced_determinant(n, "machin")
        assert raw
        assert machin
        raw_valuation = valuation_2(raw)
        machin_valuation = valuation_2(machin)
        assert raw_valuation == machin_valuation
        records.append(
            {
                "n": n,
                "matrix_size": 2 * n,
                "raw_determinant_2_adic_valuation": raw_valuation,
                "machin_normalized_determinant_2_adic_valuation": (
                    machin_valuation
                ),
                "raw_determinant_sha256": fraction_digest(raw),
                "machin_normalized_determinant_sha256": fraction_digest(
                    machin
                ),
            }
        )

    report = {
        "description": (
            "Exact Fraction cross-check of the reduced raw and Machin "
            "determinants. Equality of displayed valuations is a finite "
            "check only; the all-degree proof is in "
            "sources/machin_bordered_rank_proof.md."
        ),
        "normalization": "Machin arctangent block uses G(z)/4",
        "records": records,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
