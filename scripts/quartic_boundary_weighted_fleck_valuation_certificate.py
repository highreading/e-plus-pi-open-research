#!/usr/bin/env python3
"""Exact certificate for the boundary quartic weighted-Fleck valuation.

The all-m argument is in the accompanying source note.  This script checks
the algebraic identities, the residue-transfer carries, and a configurable
finite range in exact arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

import sympy as sp


def v2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    value = abs(value)
    return (value & -value).bit_length() - 1


def v2_fraction(value: Fraction) -> int:
    return v2_integer(value.numerator) - v2_integer(value.denominator)


def odd_double_factorial(index: int) -> int:
    if index == -1:
        return 1
    half = (index + 1) // 2
    return factorial(index + 1) // (2**half * factorial(half))


def a_value(m: int) -> int:
    return sum(
        comb(4 * m, 4 * h + 1)
        * odd_double_factorial(2 * m - 2 * h - 1)
        * odd_double_factorial(2 * m + 2 * h - 1)
        for h in range(m)
    )


def weights(m: int) -> list[int]:
    return [
        odd_double_factorial(2 * m - 2 * h - 1)
        * odd_double_factorial(2 * m + 2 * h - 1)
        // (4 * h + 1)
        for h in range(m)
    ]


def c_value(m: int) -> int:
    return sum(comb(4 * m - 1, 4 * h) * weights(m)[h] for h in range(m))


def s_value_via_a(m: int) -> Fraction:
    return Fraction(2 ** (2 * m) * a_value(m), factorial(2 * m))


def s_value_direct(m: int) -> Fraction:
    return sum(
        (
            Fraction(
                comb(4 * m, 4 * h + 1)
                * factorial(2 * m - 2 * h)
                * factorial(2 * m + 2 * h),
                factorial(m - h) * factorial(m + h) * factorial(2 * m),
            )
            for h in range(m)
        ),
        Fraction(),
    )


def newton_coefficients(values: list[int]) -> list[int]:
    output = []
    row = values[:]
    while row:
        output.append(row[0])
        row = [row[index + 1] - row[index] for index in range(len(row) - 1)]
    return output


def t_values(m: int) -> list[int]:
    return [
        sum(
            comb(4 * m - 1, 4 * h) * comb(h, j)
            for h in range(j, m)
        )
        for j in range(m)
    ]


def residue_vector(m: int) -> list[list[int]]:
    """R_r^(m)(y), represented by ascending coefficient lists."""
    output: list[list[int]] = []
    exponent = 4 * m - 1
    for residue in range(4):
        output.append(
            [
                comb(exponent, 4 * h + residue)
                for h in range((exponent - residue) // 4 + 1)
            ]
        )
    return output


def polynomial_add(*terms: list[int]) -> list[int]:
    size = max((len(term) for term in terms), default=0)
    output = [0] * size
    for term in terms:
        for index, value in enumerate(term):
            output[index] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_scale(term: list[int], scalar: int, shift: int = 0) -> list[int]:
    return [0] * shift + [scalar * value for value in term]


def transfer_vector(vector: list[list[int]]) -> list[list[int]]:
    r0, r1, r2, r3 = vector
    return [
        polynomial_add(r0, polynomial_scale(r0, 1, 1), polynomial_scale(r1, 4, 1), polynomial_scale(r2, 6, 1), polynomial_scale(r3, 4, 1)),
        polynomial_add(polynomial_scale(r0, 4), r1, polynomial_scale(r1, 1, 1), polynomial_scale(r2, 4, 1), polynomial_scale(r3, 6, 1)),
        polynomial_add(polynomial_scale(r0, 6), polynomial_scale(r1, 4), r2, polynomial_scale(r2, 1, 1), polynomial_scale(r3, 4, 1)),
        polynomial_add(polynomial_scale(r0, 4), polynomial_scale(r1, 6), polynomial_scale(r2, 4), r3, polynomial_scale(r3, 1, 1)),
    ]


def symbolic_checks() -> dict[str, bool]:
    m, h, y = sp.symbols("m h y", integer=True)
    ratio = (
        (2 * m + 2 * h + 1)
        * (4 * h + 1)
        / ((2 * m - 2 * h - 1) * (4 * h + 5))
    )
    a = (8 * h**2 + 10 * h - 4 * m + 3) / (
        (2 * m - 2 * h - 1) * (4 * h + 5)
    )
    b = (
        4 * y**2 * m
        - 2 * y**2
        + 20 * y * m
        - 8 * y
        + 8 * m**2
        + 17 * m
        - 6
    ) / (
        (2 * y + 5)
        * (2 * y + 9)
        * (y - 2 * m + 1)
        * (y - 2 * m + 3)
    )
    return {
        "weight_ratio_is_one_plus_2a": sp.factor(ratio - (1 + 2 * a)) == 0,
        "a_first_difference_is_4B_of_2h": sp.factor(
            a.subs(h, h + 1) - a - 4 * b.subs(y, 2 * h)
        )
        == 0,
    }


def exact_scan(max_m: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    failures: list[dict[str, object]] = []
    selected: list[dict[str, object]] = []
    selected_indices = {1, 2, 3, 4, 8, 16, 32, 64, max_m}
    previous_residue = residue_vector(1)

    for m in range(1, max_m + 1):
        a = a_value(m)
        c = c_value(m)
        w = weights(m)
        d = newton_coefficients(w)
        t = t_values(m)
        s_via_a = s_value_via_a(m)

        observed = {
            "A_equals_4mC": a == 4 * m * c,
            "newton_v2": [v2_integer(value) for value in d],
            "T_v2": [v2_integer(value) for value in t],
            "C_v2": v2_integer(c),
            "A_v2": v2_integer(a),
            "S_v2": v2_fraction(s_via_a),
        }
        expected = {
            "newton_v2": list(range(m)),
            "T_lower_bounds": [m - j for j in range(m - 1)],
            "T_top_is_odd": t[-1] % 2 == 1,
            "C_v2": m - 1,
            "A_v2": m + v2_integer(m) + 1,
            "S_v2": m + m.bit_count() + v2_integer(m) + 1,
        }

        if m <= 24 and s_via_a != s_value_direct(m):
            failures.append({"m": m, "failure": "direct S identity"})
        if not observed["A_equals_4mC"]:
            failures.append({"m": m, "failure": "A=4mC"})
        if observed["newton_v2"] != expected["newton_v2"]:
            failures.append(
                {
                    "m": m,
                    "failure": "Newton valuations",
                    "observed": observed["newton_v2"],
                }
            )
        if any(observed["T_v2"][j] < expected["T_lower_bounds"][j] for j in range(m - 1)):
            failures.append(
                {
                    "m": m,
                    "failure": "T lower bound",
                    "observed": observed["T_v2"],
                }
            )
        if not expected["T_top_is_odd"]:
            failures.append({"m": m, "failure": "T top parity"})
        for key in ("C_v2", "A_v2", "S_v2"):
            if observed[key] != expected[key]:
                failures.append(
                    {
                        "m": m,
                        "failure": key,
                        "observed": observed[key],
                        "expected": expected[key],
                    }
                )

        current_residue = residue_vector(m)
        if m > 1 and transfer_vector(previous_residue) != current_residue:
            failures.append({"m": m, "failure": "four-state transfer"})
        previous_residue = current_residue

        # Coefficients of R_0^(m)(1+2x) are 2^j T_(m,j).
        transformed = [2**j * t[j] for j in range(m)]
        modulus = 2**m
        expected_mod = [0] * m
        expected_mod[m - 1] = 2 ** (m - 1)
        if [value % modulus for value in transformed] != expected_mod:
            failures.append({"m": m, "failure": "transfer congruence"})

        if m in selected_indices:
            selected.append(
                {
                    "m": m,
                    "newton_v2": observed["newton_v2"],
                    "T_v2": observed["T_v2"],
                    "C_v2": observed["C_v2"],
                    "A_v2": observed["A_v2"],
                    "S_v2": observed["S_v2"],
                    "S_normalized_odd_residue_mod_256": (
                        (
                            (s_via_a.numerator // (2 ** observed["S_v2"]))
                            * pow(s_via_a.denominator, -1, 256)
                        )
                        % 256
                        if s_via_a.denominator % 2 == 1
                        else None
                    ),
                }
            )

    return failures, selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=64)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "quartic_boundary_weighted_fleck_valuation_certificate.json",
    )
    args = parser.parse_args()

    symbolic = symbolic_checks()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    failures, selected = exact_scan(args.max_m)
    if failures:
        raise AssertionError(failures[:5])

    result = {
        "schema": "quartic-boundary-weighted-fleck-valuation-v1",
        "claim_scope": (
            "The source proves the valuation for every m. "
            "This exact finite scan checks identities, transfer carries, and valuations."
        ),
        "symbolic_checks": symbolic,
        "max_m": args.max_m,
        "failures": failures,
        "selected_records": selected,
        "proved_formula": "v2(S_m)=m+s2(m)+v2(m)+1 for every m>=1",
        "corollary": (
            "v2(denominator of b_(4m,2m+1))="
            "3m-s2(m)-v2(m)-1"
        ),
        "warning": (
            "This proves the isolated first odd-coordinate valuation only; "
            "it does not control the final primitive endpoint gcd or classify e+pi."
        ),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
