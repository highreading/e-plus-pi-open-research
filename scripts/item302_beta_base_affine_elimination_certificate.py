#!/usr/bin/env python3
"""Deterministic exact checker for Item 302.

The bounded rows replay universal base-composition, Turan, continuant,
matrix, unit, and modular congruence identities. They do not scan for
half-bound failures and are EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def beta_q(limit: int) -> list[int]:
    q = [1, 1]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
    return q


def continuant(word: list[int]) -> int:
    older = 1
    previous = 1
    for index, value in enumerate(word):
        if index == 0:
            current = value
        else:
            current = value * previous + older
        older, previous = previous, current
    return 1 if not word else previous


def continued_fraction(word: list[int]) -> Fraction:
    assert word
    value = Fraction(word[-1], 1)
    for entry in reversed(word[:-1]):
        value = entry + Fraction(1, value)
    return value


def matrix_multiply(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def word_for_n(n: int) -> list[int]:
    assert n >= 2
    return [7] + [4 * row - 2 for row in range(3, n + 1)]


def check_base_composition(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    turan = [None, None]
    for n in range(2, limit + 1):
        turan.append(q[n] * q[n - 2] - q[n - 1] * q[n - 1])
    assert turan[2] == 6

    composed = Fraction(6, 7)
    for n in range(2, limit + 1):
        if n >= 3:
            composed = Fraction(q[n - 1], q[n]) * (
                4 * q[n - 2] - composed
            )
        assert composed == Fraction(turan[n], q[n])
        if n >= 3:
            assert (
                turan[n] + turan[n - 1]
                == 4 * q[n - 1] * q[n - 2]
            )

        unrolled = (-1) ** (n - 2) * 6
        unrolled += 4 * sum(
            (-1) ** (n - row) * q[row - 1] * q[row - 2]
            for row in range(3, n + 1)
        )
        assert unrolled == turan[n]

        rows.append(
            {
                "n": n,
                "base_composition": True,
                "alternating_turan_formula": True,
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "half_bound_scan": False,
        "label": "EXACT FINITE ONLY",
    }


def check_continuants(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(2, limit + 1):
        word = word_for_n(n)
        assert continuant(word) == q[n]
        reversed_word = list(reversed(word))
        assert continued_fraction(reversed_word) == Fraction(q[n], q[n - 1])

        product = ((1, 0), (0, 1))
        for entry in word:
            product = matrix_multiply(product, ((entry, 1), (1, 0)))
        determinant = (
            product[0][0] * product[1][1]
            - product[0][1] * product[1][0]
        )
        assert product[0] == (q[n], q[n - 1])
        assert determinant == (-1) ** (n - 1)

        if n >= 3:
            tail_word = word[1:]
            tail = continuant(tail_word)
            assert product[1][0] == tail
            assert (
                q[n - 1] * tail - (-1) ** n
            ) % q[n] == 0

        rows.append(
            {
                "n": n,
                "continuant": True,
                "continued_fraction": True,
                "matrix_determinant": True,
                "tail_inverse": n < 3 or True,
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "finite_fit": False,
        "label": "EXACT FINITE ONLY",
    }


def check_units_and_congruences(limit: int) -> dict[str, Any]:
    q = beta_q(limit)
    rows: list[dict[str, Any]] = []
    for n in range(2, limit + 1):
        a_value = q[n - 1]
        b_value = q[n]
        turan = b_value * q[n - 2] - a_value * a_value
        assert math.gcd(a_value, b_value) == 1
        assert math.gcd(turan, b_value) == 1

        t_value = (2 * turan + b_value) // (2 * b_value)
        r_value = b_value * t_value - turan
        assert (r_value - a_value * a_value) % b_value == 0
        assert math.gcd(r_value, b_value) == 1

        if n >= 3:
            tail = continuant(word_for_n(n)[1:])
            assert (r_value * tail * tail - 1) % b_value == 0

        rows.append(
            {
                "n": n,
                "turan_unit_mod_qn": True,
                "centered_square_unit_mod_qn": True,
                "tail_square_inverse": n < 3 or True,
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "proper_divisor_nonvanishing_follows_from_gcd": True,
        "exceptional_prime_search": False,
        "label": "EXACT FINITE ONLY",
    }


def elimination_proof_data() -> dict[str, Any]:
    return {
        "ring": "Z[X_2,...,X_n]",
        "base_generator": "E_2=7*X_2-6",
        "update_generators": (
            "R_j=q_j*X_j+q_(j-1)*X_(j-1)"
            "-4*q_(j-1)*q_(j-2)"
        ),
        "endpoint_polynomial": "E_j=q_j*X_j-T_j",
        "induction": "E_j=R_j-E_(j-1)",
        "rational_elimination": (
            "I_Q intersect Q[X_n]=<X_n-T_n/q_n>"
        ),
        "primitivity": "gcd(T_n,q_n)=gcd(q_(n-1)^2,q_n)=1",
        "gauss_lemma": (
            "I intersect Z[X_n]=<q_n*X_n-T_n>"
        ),
        "scope": (
            "base-reaching affine-elimination identities only; "
            "nearest digits, inequalities, and modular-square estimates open"
        ),
        "label": "PROVED SYMBOLIC IN REPORT",
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item302-beta-base-affine-elimination-certificate-v1",
        "description": (
            "Exact full beta affine composition, alternating Turan numerator, "
            "continuant and matrix coordinates, endpoint elimination ideal, "
            "and all-divisor unit congruence"
        ),
        "theorem": {
            "full_composition": (
                "T_n=(-1)^(n-2)*6+4*sum_(j=3)^n "
                "(-1)^(n-j)q_(j-1)q_(j-2)"
            ),
            "continuant": (
                "q_n=K(7,10,14,...,4n-2) and "
                "q_n/q_(n-1)=[4n-2;4n-6,...,10,7]"
            ),
            "endpoint_elimination": (
                "I_n intersect Z[X_n]=<q_n*X_n-T_n>"
            ),
            "unit_square": (
                "for every Q|q_n, centered r_(n,Q) is a nonzero "
                "square unit and |r_(n,Q)|>=1"
            ),
            "scoped_no_go": (
                "full base-reaching affine-elimination identities give "
                "no independent endpoint polynomial"
            ),
            "scope_limit": (
                "does not cover nonlinear nearest digits, inequalities, "
                "modular-square distribution, or all linear-depth methods"
            ),
        },
        "symbolic_proof_data": {
            "endpoint_elimination": elimination_proof_data(),
        },
        "bounded_exact_checks": {
            "base_composition": check_base_composition(72),
            "continuants": check_continuants(72),
            "units_and_congruences": check_units_and_congruences(72),
            "actual_half_bound_scan": False,
            "counterexample_search": False,
            "exceptional_prime_search": False,
            "finite_fit": False,
            "label": "EXACT FINITE ONLY",
        },
        "admission": {
            "actual_half_bound": "OPEN",
            "stronger_item295_inequality": "OPEN",
            "base_reaching_affine_elimination": (
                "PROVED SCOPED NO INDEPENDENT ENDPOINT IDENTITY"
            ),
            "seed_modular_square_or_ostrowski_invariant": "OPEN",
            "proper_target_nonvanishing": "PROVED, LOWER BOUND 1 ONLY",
            "proper_target_upper_construction": "OPEN",
            "item282_product_baseline": "OPEN AND SEPARATE",
            "new_route1_rate": 0,
            "new_beta_capacity_reduction": 0,
            "positive_linear_capacity_admission": "FAIL",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
