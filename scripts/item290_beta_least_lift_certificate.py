#!/usr/bin/env python3
"""Deterministic exact certificate for Item 290's least-lift reduction.

The bounded rows check identities only.  They are not an exceptional-prime
search and are not used to infer any asymptotic bound for the least lift.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def continuant(word: list[int]) -> int:
    if not word:
        return 1
    previous, current = 1, word[0]
    for entry in word[1:]:
        previous, current = current, entry * current + previous
    return current


def matrix_multiply(
    first: tuple[tuple[int, int], tuple[int, int]],
    second: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (
            first[0][0] * second[0][0] + first[0][1] * second[1][0],
            first[0][0] * second[0][1] + first[0][1] * second[1][1],
        ),
        (
            first[1][0] * second[0][0] + first[1][1] * second[1][0],
            first[1][0] * second[0][1] + first[1][1] * second[1][1],
        ),
    )


def continuant_matrix(word: list[int]) -> tuple[tuple[int, int], tuple[int, int]]:
    result = ((1, 0), (0, 1))
    for entry in word:
        result = matrix_multiply(result, ((entry, 1), (1, 0)))
    return result


def centered_remainder(value: int, modulus: int) -> int:
    """Centered residue; positive tie convention if the modulus is even."""
    assert modulus > 0
    residue = value % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def nearest_quotient(numerator: int, denominator: int) -> int:
    """Nearest integer for positive numerator and odd positive denominator."""
    assert numerator >= 0 and denominator > 0 and denominator % 2 == 1
    return (2 * numerator + denominator) // (2 * denominator)


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def beta_word(n: int) -> list[int]:
    assert n >= 2
    if n == 2:
        return [7]
    return list(range(4 * n - 2, 9, -4)) + [7]


def palindrome_word(length: int) -> list[int]:
    assert length >= 1
    half = [11 + 4 * index for index in range((length + 1) // 2)]
    if length % 2:
        return half + list(reversed(half[:-1]))
    return half + list(reversed(half))


def build_result() -> dict[str, Any]:
    q = q_values(190)

    beta_rows: list[dict[str, Any]] = []
    descent_rows: list[dict[str, Any]] = []
    for n in range(2, 161):
        word = beta_word(n)
        denominator = continuant(word)
        numerator = continuant(word[1:]) if len(word) > 1 else 1
        assert denominator == q[n]
        assert numerator == q[n - 1]
        assert math.gcd(numerator, denominator) == 1
        matrix = continuant_matrix(word)
        assert matrix[0][0] == denominator
        assert matrix[1][0] == numerator

        next_value = q[n + 1]
        assert (next_value - numerator) % denominator == 0
        quotient = nearest_quotient(numerator * numerator, denominator)
        signed_remainder = numerator * numerator - quotient * denominator
        assert signed_remainder == centered_remainder(
            numerator * numerator, denominator
        )
        rho = abs(signed_remainder)
        assert 1 <= rho <= denominator // 2
        assert math.gcd(rho, denominator) == 1
        assert centered_remainder(next_value * next_value, denominator) == signed_remainder

        beta_rows.append(
            {
                "n": n,
                "word_length": len(word),
                "word_first": word[0],
                "word_last": word[-1],
                "q_n": denominator,
                "q_previous": numerator,
                "centered_quotient": quotient,
                "signed_remainder": signed_remainder,
                "rho": rho,
            }
        )

        if n >= 3:
            previous_previous = q[n - 2]
            leading = 4 * n - 2
            assert denominator == leading * numerator + previous_previous
            h_value = numerator - leading * quotient
            determinant = numerator * h_value - previous_previous * quotient
            assert determinant == signed_remainder
            assert abs(determinant) == rho
            scaled_determinant = denominator * h_value - numerator * previous_previous
            assert scaled_determinant == leading * signed_remainder
            assert (h_value - numerator) % leading == 0
            assert (leading + 1) * numerator > denominator
            assert leading * numerator < denominator
            descent_rows.append(
                {
                    "n": n,
                    "A": leading,
                    "a": numerator,
                    "b": denominator,
                    "c": previous_previous,
                    "kappa": quotient,
                    "h": h_value,
                    "determinant": determinant,
                    "scaled_determinant": scaled_determinant,
                }
            )

    half_pattern_minimum = beta_rows[0]
    for row in beta_rows:
        assert 2 * row["rho"] >= row["q_previous"]
        if (
            row["rho"] * half_pattern_minimum["q_previous"]
            < half_pattern_minimum["rho"] * row["q_previous"]
        ):
            half_pattern_minimum = row

    proper_rows: list[dict[str, Any]] = []
    clearing_samples = (1, 3, 5, 7, 9, 11, 13, 25, 49, 77, 121, 143)
    for row in beta_rows:
        n = row["n"]
        full_target = row["q_n"]
        signed_full = row["signed_remainder"]
        for clearing in clearing_samples:
            target = full_target // math.gcd(full_target, clearing)
            if target <= 1:
                continue
            signed_target = centered_remainder(signed_full, target)
            direct_target = centered_remainder(q[n + 1] ** 2, target)
            assert signed_target == direct_target
            rho_target = abs(signed_target)
            assert 1 <= rho_target <= target // 2
            assert rho_target <= min(row["rho"], target // 2)
            assert math.gcd(rho_target, target) == 1
            # The least boundary-unit lift is minus the centered square residue;
            # U + signed_target is the corresponding monic linear annihilator.
            boundary_lift = -signed_target
            assert (boundary_lift + q[n + 1] ** 2) % target == 0
            assert (-q[n + 1] ** 2 + signed_target) % target == 0
            proper_rows.append(
                {
                    "n": n,
                    "D": clearing,
                    "full_target": full_target,
                    "target": target,
                    "signed_full": signed_full,
                    "signed_target": signed_target,
                    "rho_full": row["rho"],
                    "rho_target": rho_target,
                    "boundary_lift": boundary_lift,
                }
            )

    palindrome_rows: list[dict[str, Any]] = []
    for length in range(1, 25):
        word = palindrome_word(length)
        assert word == list(reversed(word))
        matrix = continuant_matrix(word)
        denominator = matrix[0][0]
        numerator = matrix[1][0]
        assert matrix[0][1] == numerator
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        assert determinant == (-1) ** length
        signed = centered_remainder(numerator * numerator, denominator)
        assert abs(signed) == 1
        assert signed == (-1) ** (length + 1)
        palindrome_rows.append(
            {
                "length": length,
                "word": word,
                "denominator": denominator,
                "numerator": numerator,
                "signed_square_remainder": signed,
            }
        )

    return {
        "schema": "item290-beta-least-lift-certificate-v1",
        "description": (
            "Exact beta continuant, centered square remainder, one-step "
            "Euclidean determinant, proper-target reduction, and palindromic barrier"
        ),
        "theorem": {
            "continuant": (
                "for n=2, q_2=K(7) and q_1/q_2=[0;7]; for n>=3, "
                "q_n=K(7,10,14,...,4n-2) and q_(n-1)/q_n="
                "[0;4n-2,4n-6,...,10,7]"
            ),
            "centered_lift": (
                "with a=q_(n-1), b=q_n and kappa=floor((2a^2+b)/(2b)), "
                "r=a^2-kappa*b is the unique centered residue of q_(n+1)^2 "
                "mod b and rho_n=|r|"
            ),
            "euclidean_descent": (
                "if b=(4n-2)a+c and h=a-(4n-2)kappa, then "
                "r=a*h-c*kappa and (4n-2)r=b*h-a*c"
            ),
            "degree_one": (
                "the minimum coefficient height of a monic linear annihilator "
                "of -q_(n+1)^2 mod q_n is exactly log rho_n"
            ),
            "proper_target": (
                "for Q|q_n, the signed least residue is centered(r mod Q), so "
                "rho_(n,Q)<=min(rho_n,Q/2); full upper bounds transfer and "
                "full lower bounds do not"
            ),
            "coarse_continuant_barrier": (
                "palindromic positive continued-fraction words of arbitrary "
                "length have numerator square congruent to plus or minus 1 "
                "modulo the denominator"
            ),
            "scope": (
                "no all-n O(n) upper bound or superlinear lower bound for the "
                "specific arithmetic-progression beta word is proved"
            ),
            "deoverlap": "proper Q may be any divisor of q_n/gcd(q_n,D_m)",
            "capacity": "the Item282 common product baseline remains separate",
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "beta_rows": len(beta_rows),
            "beta_digest": digest(beta_rows),
            "descent_rows": len(descent_rows),
            "descent_digest": digest(descent_rows),
            "proper_target_rows": len(proper_rows),
            "proper_target_digest": digest(proper_rows),
            "palindrome_rows": len(palindrome_rows),
            "palindrome_digest": digest(palindrome_rows),
            "observed_half_pattern": (
                "2*rho_n>=q_(n-1) on the checked rows only; unproved globally"
            ),
            "observed_half_pattern_rows": len(beta_rows),
            "observed_half_pattern_minimum_row": {
                "n": half_pattern_minimum["n"],
                "rho": half_pattern_minimum["rho"],
                "q_previous": half_pattern_minimum["q_previous"],
                "twice_rho_minus_q_previous": (
                    2 * half_pattern_minimum["rho"]
                    - half_pattern_minimum["q_previous"]
                ),
            },
            "asymptotic_extrapolation": False,
            "exceptional_prime_search": False,
        },
        "admission": {
            "full_degree_one_O_n_lift": "OPEN",
            "full_degree_one_O_n_exclusion": "OPEN",
            "proper_target_degree_one_bound": "OPEN EXCEPT WHEN log Q=O(n)",
            "actual_target_bound": False,
            "product_baseline_closed": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "an all-n bound log rho_n=O(n)",
            "or a lower bound log rho_n/n tending to infinity",
            "an exact estimate exploiting the arithmetic-progression word rather than coarse continuant size",
            "a proper de-overlapped target residue theorem at n log n target height",
            "the Item282 common product baseline and weighted-return cover",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
