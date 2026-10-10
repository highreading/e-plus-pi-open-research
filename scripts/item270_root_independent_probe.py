#!/usr/bin/env python3
"""Independent exact arithmetic replay for Item 270.

The script does not import the canonical Item-270 checker.  Its bounded
rows corroborate the symbolic CT/twisted-de-Rham proof and are labelled
EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


SYZYGIES = (
    (
        (840, 13280, 20360, 7920),
        (-9504, -34848, -38016, -12672),
        (149580, 295740, 190590, 40590),
        (-256860, -483396, -305520, -64944),
        (514920, 617055, 246105, 32670),
        (-831096, -993093, -394929, -52272),
    ),
    (
        (4752, 124320, 197168, 77600),
        (-93120, -341440, -372480, -124160),
        (1589880, 3178860, 2080686, 450450),
        (-2716200, -5209200, -3346680, -720720),
        (3794112, 4548240, 1814643, 240975),
        (-6123600, -7319790, -2911950, -385560),
    ),
)


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def truncated_q_power(power: int, degree: int, modulus: int | None = None) -> list[int]:
    coefficients = [1] + [0] * degree
    for _ in range(power):
        future = [0] * (degree + 1)
        for index, value in enumerate(coefficients):
            if not value:
                continue
            for shift in range(4):
                if index + shift <= degree:
                    future[index + shift] += value
        if modulus:
            future = [value % modulus for value in future]
        coefficients = future
    return coefficients


def coefficient_value(s: int, q_power: int, modulus: int | None = None) -> int:
    degree = 3 * s + 2
    polynomial = truncated_q_power(q_power, degree, modulus)
    pole_order = 3 * s + 3
    answer = 0
    for index, value in enumerate(polynomial):
        answer += value * math.comb(pole_order + degree - index - 1, degree - index)
    return answer % modulus if modulus else answer


def pair(s: int, modulus: int | None = None) -> tuple[int, int]:
    g1 = coefficient_value(s, 2 * s, modulus)
    g0 = coefficient_value(s, 2 * s + 1, modulus)
    return g0, g1


def adjacent_coefficients(s: int) -> tuple[int, int, int, int]:
    a = 16 * (s + 1) * (2 * s + 3) * (75 * s * s + 100 * s + 3)
    b = -320 * (s + 1) * (2 * s + 3) * (6 * s * s + 11 * s + 4)
    c = 3 * (3 * s + 4) * (3 * s + 5) * (575 * s * s + 1525 * s + 998)
    d = -60 * (3 * s + 4) * (3 * s + 5) * (46 * s * s + 123 * s + 81)
    return a, b, c, d


def transfer(s: int) -> list[list[Fraction]]:
    a, b, c, d = adjacent_coefficients(s)
    second = [Fraction(-a, d), Fraction(-b, d), Fraction(-c, d)]
    p = [
        [polynomial_value(SYZYGIES[row][column], s) for column in range(6)]
        for row in range(2)
    ]
    right = []
    for row in range(2):
        right.append(
            [
                -Fraction(p[row][column]) - Fraction(p[row][3]) * second[column]
                for column in range(3)
            ]
        )
    determinant = p[0][4] * p[1][5] - p[0][5] * p[1][4]
    assert determinant
    third = [
        (right[0][column] * p[1][5] - p[0][5] * right[1][column])
        / determinant
        for column in range(3)
    ]
    return [
        [Fraction(0), Fraction(0), Fraction(1)],
        second,
        third,
    ]


def determinant3(matrix: list[list[Fraction]]) -> Fraction:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def transfer_determinant_formula(s: int) -> Fraction:
    return Fraction(
        512
        * (s + 1) ** 2
        * (2 * s + 1)
        * (2 * s + 3)
        * (2 * s + 5)
        * (23 * s + 50),
        9
        * (s + 2)
        * (3 * s + 4)
        * (3 * s + 5)
        * (3 * s + 7)
        * (3 * s + 8)
        * (23 * s + 27),
    )


def symbolic_rows(limit: int) -> dict[str, object]:
    pairs = [pair(s) for s in range(limit + 3)]
    adjacent = 0
    syzygy = 0
    transfer_rows = 0
    determinant_rows = 0
    for s in range(limit + 1):
        observations = list(pairs[s]) + list(pairs[s + 1]) + list(pairs[s + 2])
        a, b, c, d = adjacent_coefficients(s)
        assert a * observations[0] + b * observations[1] + c * observations[2] + d * observations[3] == 0
        adjacent += 1
        for row in SYZYGIES:
            assert sum(
                polynomial_value(row[column], s) * observations[column]
                for column in range(6)
            ) == 0
            syzygy += 1
        matrix = transfer(s)
        state = [Fraction(pairs[s][0]), Fraction(pairs[s][1]), Fraction(pairs[s + 1][0])]
        future = [
            sum(matrix[row][column] * state[column] for column in range(3))
            for row in range(3)
        ]
        assert future == [
            pairs[s + 1][0],
            pairs[s + 1][1],
            pairs[s + 2][0],
        ]
        transfer_rows += 1
        assert determinant3(matrix) == transfer_determinant_formula(s)
        assert determinant3(matrix)
        determinant_rows += 1
    return {
        "s_range": [0, limit],
        "adjacent_rows": adjacent,
        "three_layer_syzygy_rows": syzygy,
        "transfer_rows": transfer_rows,
        "transfer_determinant_rows": determinant_rows,
        "label": "EXACT FINITE ONLY",
    }


def witness() -> dict[str, object]:
    prime = 2399
    current = pair(299, prime)
    adjacent = pair(300, prime)
    assert current == (0, 0)
    assert adjacent == (2105, 1694)
    assert adjacent[0] != 0
    return {
        "p": prime,
        "current_s": 299,
        "current_pair": list(current),
        "adjacent_s": 300,
        "adjacent_pair": list(adjacent),
        "surviving_u": adjacent[0],
        "label": "EXACT FINITE ONLY existence witness",
    }


def container_audit() -> dict[str, object]:
    factors = (
        (1, 1), (1, 2), (2, 1), (2, 3), (2, 5),
        (3, 4), (3, 5), (3, 7), (3, 8), (23, 27), (23, 50),
    )
    rows = 0
    for m in (100, 231, 997):
        for prime in (101, 2399, 5003):
            for j in range(4):
                s = (j + 1) * prime - (2 * m + 1)
                for h in range(-3, 4):
                    for a, b in factors:
                        left = a * (s + h) + b
                        container = a * (2 * m + 1) - a * h - b
                        assert left - a * (j + 1) * prime == -container
                        rows += 1
    far = (
        Fraction(1, 45) + Fraction(2, 35) + Fraction(1, 230)
        + Fraction(1, 44) + Fraction(1, 90) + Fraction(11, 2185)
        + Fraction(1, 460) + Fraction(1, 1485)
    )
    assert far == Fraction(1139587, 9085230)
    return {
        "container_identity_rows": rows,
        "moving_factor_count": len(factors),
        "far_coefficient": str(far),
        "general_implication": "p dividing a(s+h)+b implies p divides a(2M+1)-ah-b",
    }


def build(limit: int) -> dict[str, object]:
    return {
        "schema": "item270-root-independent-audit-v1",
        "independence": "does not import the canonical Item-270 checker",
        "sequence_and_transfer": symbolic_rows(limit),
        "actual_witness": witness(),
        "exception_container": container_audit(),
        "scope": {
            "rank_three_CT_module": "audited from the separate symbolic package",
            "bounded_window_collision_line": "PROVED by invertibility of the exact transfer",
            "unbounded_or_nonlinear_window": "OPEN",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
            "common_zero_scan": "NOT PERFORMED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=24)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(
        json.dumps(build(args.limit), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
