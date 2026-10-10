#!/usr/bin/env python3
"""Independent root-side identity probe for Item 266.

The bounded row enumeration is not a common-zero scan and has no asymptotic
status.  The capacity comparisons use exact rational arithmetic.
"""

from __future__ import annotations

import argparse
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def primes_to(limit: int) -> list[int]:
    flags = [True] * (limit + 1)
    flags[0:2] = [False, False]
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            for multiple in range(p * p, limit + 1, p):
                flags[multiple] = False
    return [p for p, flag in enumerate(flags) if flag]


def original_rows(M: int, primes: list[int]) -> set[tuple[int, int, int, int, int]]:
    rows: set[tuple[int, int, int, int, int]] = set()
    for j in range(1, 2 * M + 1):
        for p in primes:
            s = (j + 1) * p - (2 * M + 1)
            if s < 0:
                continue
            if 3 * s + 2 >= p:
                break
            q = 1 if p >= 5 * s + 4 else 2
            b = q * p - 5 * s - 4
            if 0 <= b <= 3 * s + 4:
                rows.add((j, p, q, s, b))
    return rows


def interval_rows(M: int, primes: list[int]) -> set[tuple[int, int, int, int, int]]:
    rows: set[tuple[int, int, int, int, int]] = set()
    for j in range(1, 2 * M + 1):
        for p in primes:
            if p < 11:
                continue
            if (8 * j + 7) * p >= 16 * M and (5 * j + 4) * p <= 10 * M + 1:
                s = (j + 1) * p - (2 * M + 1)
                b = p - 5 * s - 4
                rows.add((j, p, 1, s, b))
            if (4 * j + 3) * p >= 8 * M and (3 * j + 2) * p <= 6 * M:
                s = (j + 1) * p - (2 * M + 1)
                b = 2 * p - 5 * s - 4
                rows.add((j, p, 2, s, b))
    return rows


def falling(x: Fraction, length: int) -> Fraction:
    value = Fraction(1)
    for offset in range(length):
        value *= x - offset
    return value


def rising(x: Fraction, length: int) -> Fraction:
    value = Fraction(1)
    for offset in range(length):
        value *= x + offset
    return value


def localized_numerator(b: int, residue: int, a: int) -> int:
    B = b + 1 - a
    if residue > B:
        return 0
    s = Fraction(-(b + 4), 5)
    E = 2 * s + a
    t = (3 * s + 2 - residue) / 4
    total = Fraction(0)
    for h in range((B - residue) // 4 + 1):
        total += (
            (-1) ** h
            * math.comb(B, residue + 4 * h)
            * falling(t, h)
            / rising(E - t + 1, h)
        )
    return total.numerator


def terminal_state(s: int, p: int) -> tuple[int, int, int, int]:
    degree = 3 * s + 2
    values = [0] * (degree + 1)
    values[0] = 1
    for n in range(degree):
        def at(index: int) -> int:
            return values[index] if index >= 0 else 0

        numerator = (
            (5 * s + 3) * (at(n) + at(n - 1) + at(n - 2))
            + (n - 3 * s) * at(n - 3)
        ) % p
        values[n + 1] = numerator * pow(n + 1, -1, p) % p
    return tuple(values[-4:])


def check_rows(max_M: int) -> dict[str, int]:
    primes = primes_to(2 * max_M + 20)
    total = 0
    for M in range(1, max_M + 1):
        actual = {row for row in original_rows(M, primes) if row[1] >= 11}
        intervals = interval_rows(M, primes)
        assert actual == intervals
        for j, p, q, s, b in actual:
            assert 10 * M + 1 - b == (5 * j + 5 - q) * p
            assert 0 <= b < p
            assert 7 * b <= 6 * M + 7
        total += len(actual)
    return {"M_max": max_M, "stable_rows": total}


def check_capacities() -> dict[str, str]:
    far_terms = [
        Fraction(1, 45),
        Fraction(2, 35),
        Fraction(1, 230),
        Fraction(1, 44),
        Fraction(1, 90),
        Fraction(11, 2185),
        Fraction(1, 460),
        Fraction(1, 1485),
    ]
    far = sum(far_terms, Fraction(0))
    assert far == Fraction(1139587, 9085230)
    getcontext().prec = 40
    far_decimal = Decimal(far.numerator) / Decimal(far.denominator)
    gap = Decimal("0.117797902016590763")
    assert far_decimal > gap

    partial = Fraction(0)
    cutoff = 10000
    for j in range(1, cutoff + 1):
        partial += Fraction(6, (5 * j + 4) * (8 * j + 7))
        partial += Fraction(2, (3 * j + 2) * (4 * j + 3))
    lower = Decimal(partial.numerator) / Decimal(partial.denominator)
    upper = lower + Decimal(19) / (Decimal(60) * Decimal(cutoff))
    target = Decimal("0.239111014698")
    assert lower < target < upper
    return {
        "far_exact": f"{far.numerator}/{far.denominator}",
        "far_decimal": str(far_decimal),
        "far_minus_gap": str(far_decimal - gap),
        "stable_partial_lower": str(lower),
        "stable_tail_upper": str(upper),
    }


def check_witness() -> dict[str, object]:
    left = localized_numerator(900, 3, 0)
    right = localized_numerator(900, 3, 1)
    common = math.gcd(abs(left), abs(right))
    odd_primes = [911, 971, 991, 1031, 1051, 1091, 1151, 1171, 1231, 1291, 2399]
    expected = 2**449 * math.prod(odd_primes)
    assert common == expected
    assert all(all(p % d for d in range(2, math.isqrt(p) + 1)) for p in odd_primes)
    state = terminal_state(299, 2399)
    assert state == (7, 2392, 0, 0)
    assert 10 * 2249 + 1 - 900 == (5 * 1 + 4) * 2399
    return {
        "row": [2249, 299, 2399, 1, 1, 900, 3],
        "terminal": list(state),
        "gcd_two_adic_exponent": 449,
        "gcd_odd_prime_factors": odd_primes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "schema": "item266-root-independent-probe-v1",
        "scope": "bounded identity replay and exact rational comparisons; no common-zero scan",
        "checks": {
            "globalization": check_rows(360),
            "capacities": check_capacities(),
            "mandatory_witness": check_witness(),
        },
        "strict_labels": {
            "bounded_row_replay": "EXACT FINITE ONLY",
            "raw_capacity": "CEILING, NOT COMMON-ZERO MASS",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
        },
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
