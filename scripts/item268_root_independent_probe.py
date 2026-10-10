#!/usr/bin/env python3
"""Independent root audit for Item 268.

Rebuilds the integer sequences by two unrelated formulas, verifies the
adjacent identity and scoped degree-four rank, recomputes the resultants and
mandatory witness, and audits actual phase relocation.  It performs no
common-zero census.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path


def g_binomial(s: int) -> tuple[int, int]:
    k = 3 * s + 2
    values: list[int] = []
    for extra in (1, 0):
        numerator_power = 2 * s + extra
        denominator_power = 5 * s + 3 + extra
        total = 0
        for i in range(min(numerator_power, k // 4) + 1):
            degree = k - 4 * i
            total += (
                (-1) ** i
                * comb(numerator_power, i)
                * comb(denominator_power + degree - 1, degree)
            )
        values.append(total)
    return values[0], values[1]


def g_recurrence(s: int) -> tuple[int, int]:
    k = 3 * s + 2
    sequence = [1]
    for n in range(k):
        def at(index: int) -> int:
            return sequence[index] if index >= 0 else 0

        numerator = (
            (5 * s + 3) * (at(n) + at(n - 1) + at(n - 2))
            + (n - 3 * s) * at(n - 3)
        )
        assert numerator % (n + 1) == 0
        sequence.append(numerator // (n + 1))
    return sum(sequence[max(0, k - 3) : k + 1]), sequence[k]


def coefficients(s: int) -> tuple[int, int, int, int]:
    return (
        75 * s * s + 100 * s + 3,
        6 * s * s + 11 * s + 4,
        575 * s * s + 1525 * s + 998,
        46 * s * s + 123 * s + 81,
    )


def adjacent_identity(s: int) -> int:
    g0, g1 = g_binomial(s)
    h0, h1 = g_binomial(s + 1)
    a, b0, c, d = coefficients(s)
    return (
        16 * (s + 1) * (2 * s + 3) * (a * g0 - 20 * b0 * g1)
        + 3 * (3 * s + 4) * (3 * s + 5) * (c * h0 - 20 * d * h1)
    )


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    rows = [row[:] for row in matrix]
    value = Fraction(1)
    for column in range(len(rows)):
        pivot = next(i for i in range(column, len(rows)) if rows[i][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        pivot_value = rows[column][column]
        value *= pivot_value
        for j in range(column, len(rows)):
            rows[column][j] /= pivot_value
        for i in range(column + 1, len(rows)):
            scale = rows[i][column]
            if scale:
                for j in range(column, len(rows)):
                    rows[i][j] -= scale * rows[column][j]
    return value


def quadratic_resultant(f: tuple[int, int, int], g: tuple[int, int, int]) -> int:
    f0, f1, f2 = f
    g0, g1, g2 = g
    matrix = [
        [Fraction(f2), Fraction(f1), Fraction(f0), Fraction(0)],
        [Fraction(0), Fraction(f2), Fraction(f1), Fraction(f0)],
        [Fraction(g2), Fraction(g1), Fraction(g0), Fraction(0)],
        [Fraction(0), Fraction(g2), Fraction(g1), Fraction(g0)],
    ]
    result = determinant(matrix)
    assert result.denominator == 1
    return result.numerator


def matrix_rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [
                    left - scale * right
                    for left, right in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def g_mod(s: int, p: int) -> tuple[int, int, tuple[int, int, int, int]]:
    k = 3 * s + 2
    sequence = [1]
    for n in range(k):
        def at(index: int) -> int:
            return sequence[index] if index >= 0 else 0

        numerator = (
            (5 * s + 3) * (at(n) + at(n - 1) + at(n - 2))
            + (n - 3 * s) * at(n - 3)
        ) % p
        assert (n + 1) % p
        sequence.append(numerator * pow(n + 1, -1, p) % p)
    terminal = tuple(sequence[k - 3 : k + 1])
    return sum(terminal) % p, sequence[k], terminal  # type: ignore[return-value]


def primes(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for d in range(2, isqrt(limit) + 1):
        if flags[d]:
            flags[d * d : limit + 1 : d] = b"\x00" * (((limit - d * d) // d) + 1)
    return [n for n, flag in enumerate(flags) if flag]


def phase_audit(max_m: int) -> tuple[int, int]:
    plist = primes(2 * max_m + 20)
    far = 0
    boundary = 0
    for M in range(25, max_m + 1):
        for j in range(1, 2 * M + 1):
            for p in plist:
                if (3 * j + 2) * p > 6 * M:
                    break
                s = (j + 1) * p - (2 * M + 1)
                if s < 0 or p <= 3 * s + 2:
                    continue
                q = 1 if p >= 5 * s + 4 else 2
                b = q * p - 5 * s - 4
                if b > 3 * s + 4 or 5 * b < M:
                    continue
                far += 1
                if p <= 3 * s + 5:
                    boundary += 1
                    c = p - 3 * s
                    assert c in (3, 4, 5)
                    assert (3 * j + 2) * p == 6 * M + 3 - c
                    continue
                sn = s + 1
                bn = b - 5
                qn = 1 if p >= 5 * sn + 4 else 2
                assert qn == q and bn == qn * p - 5 * sn - 4
                assert 0 <= bn <= 3 * sn + 4 and p > 3 * sn + 2
                Mn = M + (p - 1) // 2
                assert 2 * Mn + 1 == (j + 2) * p - sn
    return far, boundary


def main() -> None:
    pairs = []
    identity_rows = 0
    for s in range(82):
        left = g_binomial(s)
        right = g_recurrence(s)
        assert left == right
        pairs.append(left)
        if s < 81:
            assert adjacent_identity(s) == 0
            identity_rows += 1

    matrix = []
    for s in range(25):
        values = [pairs[s][0], pairs[s][1], pairs[s + 1][0], pairs[s + 1][1]]
        matrix.append([value * s**degree for value in values for degree in range(5)])
    rank = matrix_rank(matrix)
    assert rank == 19

    current_resultant = quadratic_resultant((3, 100, 75), (4, 11, 6))
    adjacent_resultant = quadratic_resultant((998, 1525, 575), (81, 123, 46))
    assert current_resultant == -3051
    assert adjacent_resultant == 1564

    p = 2399
    current = g_mod(299, p)
    adjacent = g_mod(300, p)
    assert current == (0, 0, (7, 2392, 0, 0))
    assert adjacent[:2] == (2105, 1694)
    c = (575 * 299 * 299 + 1525 * 299 + 998) % p
    minus_twenty_d = (-20 * (46 * 299 * 299 + 123 * 299 + 81)) % p
    assert (c, minus_twenty_d) == (966, 128)
    assert (c * adjacent[0] + minus_twenty_d * adjacent[1]) % p == 0

    far_rows, boundary_rows = phase_audit(360)
    payload = {
        "schema": "item268-root-independent-probe-v1",
        "scope": "independent identity and phase replay; no common-zero census",
        "integer_sequence_rows_two_methods": len(pairs),
        "adjacent_identity_rows": identity_rows,
        "degree_le_4_matrix": {"shape": [25, 20], "rank": rank, "nullity": 1},
        "resultants": {"current": current_resultant, "adjacent": adjacent_resultant},
        "mandatory_witness": {
            "current_g0_g1_terminal": [current[0], current[1], list(current[2])],
            "adjacent_g0_g1_terminal": [adjacent[0], adjacent[1], list(adjacent[2])],
            "line": [c, minus_twenty_d],
        },
        "phase_replay": {
            "M_range": [25, 360],
            "far_rows": far_rows,
            "boundary_rows": boundary_rows,
            "label": "EXACT FINITE ONLY",
        },
        "booking": {
            "new_route1_rate": 0,
            "far_raw_ceiling_changed": False,
            "item149_extra_copy": False,
        },
    }
    output = Path(__file__).resolve().parents[1] / "results" / "item268_root_independent_probe.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
