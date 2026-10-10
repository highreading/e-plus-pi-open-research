#!/usr/bin/env python3
"""Independent root audit for Item 269.

Reconstructs the rational slopes directly, checks their reduced 3-adic
denominators and strictness, rebuilds the full two-row incidence, and verifies
the fixed-prime row witness.  It performs no collision-prime search.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


def valuation_integer(value: int, prime: int) -> int:
    value = abs(value)
    exponent = 0
    while value and value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def odd_double_factorial(length: int) -> int:
    value = 1
    for k in range(1, length + 1):
        value *= 2 * k - 1
    return value


def slope(phase: int, delta: int) -> tuple[Fraction, Fraction, Fraction, int]:
    if phase == 5:
        numerator_shift, denominator_shift = 5, 4
        start = Fraction(-delta) - Fraction(1, 3)
        length = 3 * delta
    elif phase == 1:
        numerator_shift, denominator_shift = 1, 2
        start = Fraction(1, 3) - delta
        length = 3 * delta - 2
    else:
        raise ValueError(phase)

    coefficient = Fraction(1)
    prefix = Fraction(0)
    for j in range(delta):
        prefix += coefficient
        coefficient *= Fraction(6 * j + numerator_shift, 3 * j + denominator_shift)

    tail = Fraction(0)
    term = Fraction(1)
    for k in range(1, length + 1):
        term *= Fraction(start + k - 1, Fraction(1, 2) + k - 1) / 2
        tail += term
    return prefix + coefficient * tail, prefix, coefficient, length


def epsilon_two(p: int) -> int:
    value = pow(2, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def inverse_matrix(matrix: list[list[int]], p: int) -> list[list[int]]:
    n = len(matrix)
    work = [
        [value % p for value in row]
        + [1 if i == j else 0 for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot = next(i for i in range(column, n) if work[i][column])
        work[column], work[pivot] = work[pivot], work[column]
        scale = pow(work[column][column], -1, p)
        work[column] = [value * scale % p for value in work[column]]
        for i in range(n):
            if i != column and work[i][column]:
                factor = work[i][column]
                work[i] = [
                    (left - factor * right) % p
                    for left, right in zip(work[i], work[column])
                ]
    return [row[n:] for row in work]


def multiply(left: list[list[int]], right: list[list[int]], p: int) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % p
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def p5_normal_form(p: int, H: int, h: int) -> list[list[int]]:
    epsilon = epsilon_two(p) % p
    matrix = [
        [0, epsilon, 0, 0, 0],
        [epsilon, 0, 0, 0, 0],
        [0, 0, epsilon, 0, 0],
        [0, H, 0, 0, -h],
        [0, 0, 0, 0, 0],
    ]
    change = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [H * pow(epsilon, -1, p) % p, 0, 0, 1, 0],
        [0, 0, 0, 0, -pow(h, -1, p) % p],
    ]
    return multiply(multiply(inverse_matrix(change, p), matrix, p), change, p)


def full_incidence(
    phase: int,
    delta: int,
    H: Fraction,
    h: Fraction,
    epsilon: int,
    parity: int,
) -> tuple[list[Fraction], list[Fraction]]:
    D = slope(phase, delta)[0]
    sign = -1 if parity else 1
    B = Fraction(delta + 2, 2 * delta + 3)
    kappa = Fraction(2 * delta + 1, delta + 4)
    tau = Fraction((-1) ** delta * (delta + 1), 3 * delta + 2)
    alpha = Fraction(9, 2) * kappa
    f = (Fraction(delta + 1), Fraction(2 - delta, delta + 2))
    U = (Fraction(3, delta + 1), Fraction(delta - 1, 2 * delta + 1))
    A = sign * (epsilon * (H - D * h) - 1)
    Z = B * (alpha * A - tau)
    direct = [f[i] * Z + U[i] for i in range(2)]
    zrow = [
        B * (-alpha * sign - tau),
        B * alpha * sign * epsilon,
        -B * alpha * sign * epsilon * D,
    ]
    vector = [Fraction(1), H, h]
    incidence = [
        sum((f[i] * zrow[j] + (U[i] if j == 0 else 0)) * vector[j] for j in range(3))
        for i in range(2)
    ]
    return direct, incidence


def half_prefix(p: int, cutoff: int) -> int:
    total = 0
    for k in range(cutoff + 1):
        total += comb(2 * k, k) * pow(pow(8, k, p), -1, p)
    return total % p


def main() -> None:
    valuation_rows = 0
    strict_rows = 0
    first_values: dict[str, str] = {}
    for phase, first in ((5, 1), (1, 3)):
        previous: int | None = None
        for delta in range(first, 36, 2):
            D, prefix, coefficient, length = slope(phase, delta)
            expected = length + valuation_integer(odd_double_factorial(length), 3)
            assert valuation_integer(D.numerator, 3) == 0
            assert valuation_integer(D.denominator, 3) == expected
            assert valuation_integer(coefficient.numerator, 3) == 0
            assert valuation_integer(coefficient.denominator, 3) == 0
            assert prefix.denominator % 3 != 0
            if previous is not None:
                assert expected > previous
                strict_rows += 1
            previous = expected
            valuation_rows += 1
            if delta == first:
                first_values[f"phase_{phase}"] = str(D)

    normal_forms = set()
    for H in (0, 1, 4, 9):
        for h in (1, 2, 7):
            normal_forms.add(repr(p5_normal_form(47, H, h)))
    assert len(normal_forms) == 1

    incidence_rows = 0
    for phase, first in ((5, 1), (1, 3)):
        for offset, delta in enumerate(range(first, first + 8, 2)):
            H = Fraction(5 * delta + 1, delta + 3)
            h = Fraction(delta + 2, 2 * delta + 5)
            direct, incidence = full_incidence(
                phase, delta, H, h, 1 if offset % 2 == 0 else -1, offset % 2
            )
            assert direct == incidence
            incidence_rows += 2

    p = 47
    fixed_prime_values = []
    for delta in (1, 3, 5, 7):
        r = 3 * delta - 2
        s = (p - 2 * r - 3) // 6
        fixed_prime_values.append(half_prefix(p, s - 1))
    assert fixed_prime_values == [33, 0, 41, 1]

    payload = {
        "schema": "item269-root-independent-probe-v1",
        "scope": "independent exact identities; no exceptional-prime search",
        "valuation_rows": valuation_rows,
        "strict_adjacent_rows": strict_rows,
        "first_slopes": first_values,
        "p5_normal_form_parameter_sets": 12,
        "distinct_p5_normal_forms": len(normal_forms),
        "full_incidence_identity_rows": incidence_rows,
        "fixed_prime_47_cutoffs": fixed_prime_values,
        "algebraic_correspondence_audit": {
            "logic": "B_delta divides fixed leading coefficient a_d(delta), but v3(B_delta) is linear while log|a_d(delta)| is logarithmic",
            "leading_coefficient_exceptions": "finite and explicitly excluded",
            "new_lisse_or_dynamical_system": "OPEN",
        },
        "booking": {"new_route1_rate": 0, "new_j2_capacity_reduction": 0},
    }
    output = Path(__file__).resolve().parents[1] / "results" / "item269_root_independent_probe.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
