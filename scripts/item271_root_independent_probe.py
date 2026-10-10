#!/usr/bin/env python3
"""Independent exact arithmetic audit for Item 271.

This script does not import the canonical Item-271 checker.  Its bounded
sequence rows are finite corroboration only; the universal recurrence is
certified by the separate degree-bounded WZ package.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def qpoly(phase: int, x: int) -> int:
    if phase == 5:
        return 78624 * x**3 + 245808 * x**2 + 232866 * x + 61727
    return 78624 * x**3 + 88560 * x**2 + 9954 * x - 7565


def recurrence(phase: int, x: int) -> tuple[int, int, int]:
    if phase == 5:
        p0 = (
            4 * (3 * x + 1) * (3 * x + 4)
            * (6 * x + 5) * (6 * x + 11) * qpoly(phase, x + 2)
        )
        p2 = (
            6561 * (2 * x + 5) * (2 * x + 7)
            * (6 * x + 13) * (6 * x + 19) * qpoly(phase, x)
        )
    else:
        p0 = (
            4 * (3 * x - 1) * (3 * x + 2)
            * (6 * x + 1) * (6 * x + 7) * qpoly(phase, x + 2)
        )
        p2 = (
            6561 * (2 * x + 3) * (2 * x + 5)
            * (6 * x + 11) * (6 * x + 17) * qpoly(phase, x)
        )
    return p0, -p0 - p2, p2


def slope(phase: int, delta: int) -> Fraction:
    if phase == 5:
        numerator_shift, denominator_shift = 5, 4
        mu, length = -1, 3 * delta
    else:
        numerator_shift, denominator_shift = 1, 2
        mu, length = 1, 3 * delta - 2
    coefficient = Fraction(1)
    prefix = Fraction(0)
    for j in range(delta):
        prefix += coefficient
        coefficient *= Fraction(
            6 * j + numerator_shift,
            3 * j + denominator_shift,
        )
    numerator = 1
    denominator = 1
    tail = Fraction(0)
    for k in range(length):
        numerator *= 3 * k - 3 * delta + mu
        denominator *= 3 * (2 * k + 1)
        tail += Fraction(numerator, denominator)
    return prefix + coefficient * tail


def mod_fraction(value: Fraction, prime: int) -> int:
    assert value.denominator % prime
    return value.numerator * pow(value.denominator, prime - 2, prime) % prime


def sequence_audit(limit: int) -> dict[str, object]:
    rows = 0
    orbit_rows = 0
    initials = {}
    for phase, start in ((5, 1), (1, 3)):
        values = {delta: slope(phase, delta) for delta in range(start, limit + 5, 2)}
        initials[str(phase)] = {
            "delta": start,
            "D": str(values[start]),
            "Delta": str(values[start + 2] - values[start]),
        }
        delta = start
        state = values[start]
        difference = values[start + 2] - values[start]
        while delta + 4 <= limit:
            p0, p1, p2 = recurrence(phase, delta)
            assert p0 + p1 + p2 == 0
            assert (
                p0 * values[delta]
                + p1 * values[delta + 2]
                + p2 * values[delta + 4]
                == 0
            )
            rows += 1
            assert p2
            next_difference = Fraction(p0, p2) * difference
            state += difference
            delta += 2
            assert state == values[delta]
            assert next_difference == values[delta + 2] - values[delta]
            difference = next_difference
            orbit_rows += 1
    return {
        "delta_limit": limit,
        "recurrence_rows": rows,
        "orbit_rows": orbit_rows,
        "initial_states": initials,
        "label": "EXACT FINITE ONLY",
    }


def singular_audit() -> dict[str, object]:
    rows = []
    for prime, phase, delta in ((167, 5, 7), (241, 1, 11)):
        p0, _, p2 = recurrence(phase, delta)
        current = slope(phase, delta)
        future = slope(phase, delta + 2)
        difference = future - current
        assert p2 % prime == 0
        assert p0 % prime != 0
        assert current.denominator % prime
        assert future.denominator % prime
        assert mod_fraction(difference, prime) == 0
        rows.append(
            {
                "p": prime,
                "phase": phase,
                "delta": delta,
                "P0_mod_p": p0 % prime,
                "P2_mod_p": p2 % prime,
                "Delta_mod_p": mod_fraction(difference, prime),
            }
        )
    return {
        "rows": rows,
        "label": "EXACT FINITE ONLY existence witnesses",
    }


def complexity_audit() -> dict[str, object]:
    modulus = 31
    root_checks = 0
    for phase in (5, 1):
        for value in range(modulus):
            assert qpoly(phase, value) % modulus
            root_checks += 1
    numerator_roots = {
        5: (Fraction(-1, 3), Fraction(-4, 3), Fraction(-5, 6), Fraction(-11, 6)),
        1: (Fraction(1, 3), Fraction(-2, 3), Fraction(-1, 6), Fraction(-7, 6)),
    }
    denominator_roots = {
        5: (Fraction(-5, 2), Fraction(-7, 2), Fraction(-13, 6), Fraction(-19, 6)),
        1: (Fraction(-3, 2), Fraction(-5, 2), Fraction(-11, 6), Fraction(-17, 6)),
    }
    disjoint = 0
    for phase in (5, 1):
        for left in numerator_roots[phase]:
            for right in denominator_roots[phase]:
                assert (left - right) / 2 not in (0, 1, 2, 3, 4, 5, 6)
                assert not ((left - right) / 2).denominator == 1
                disjoint += 1
    return {
        "Q_mod_31_no_root_checks": root_checks,
        "linear_translation_class_checks": disjoint,
        "iterate_degree": "4n+3 after the cubic endpoint cancellation",
    }


def build(limit: int) -> dict[str, object]:
    return {
        "schema": "item271-root-independent-audit-v1",
        "independence": "does not import the canonical Item-271 checker",
        "sequence": sequence_audit(limit),
        "singular_rows": singular_audit(),
        "complexity": complexity_audit(),
        "scope": {
            "universal_WZ_identity": "audited separately from the canonical degree grid",
            "lisse_or_crystalline_realization": "OPEN",
            "full_two_row_matrix_update": "OPEN",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
            "exceptional_collision_search": "NOT PERFORMED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=51)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(
        json.dumps(build(args.limit), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
