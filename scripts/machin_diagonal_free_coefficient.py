#!/usr/bin/env python3
"""Exact checks for the first free diagonal Machin HP coefficient.

The proof is in
``sources/diagonal_machin_free_coefficient_and_measure.md``.  For each
requested positive integer congruent to zero or one modulo four this script
constructs, over QQ,

    D_E = det(E | Q),
    D_G = det(P | Gamma),
    T   = det(E_0 + 4 Gamma_0 | P | 4 Q),

and verifies the exact determinant decomposition and all displayed 2-adic
valuation claims.  The finite calculations validate the implementation;
they are not used as an all-degree proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import factorial
from pathlib import Path

import sympy as sp


def valuation_2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("the 2-adic valuation of zero is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def valuation_2(value: sp.Rational) -> int:
    numerator, denominator = value.as_numer_denom()
    return valuation_2_integer(int(numerator)) - valuation_2_integer(
        int(denominator)
    )


def factorial_valuation_2(n: int) -> int:
    if n < 0:
        raise ValueError("factorial index must be nonnegative")
    answer = 0
    while n:
        n //= 2
        answer += n
    return answer


def A(q: int) -> int:
    return sum(factorial_valuation_2(j) for j in range(q))


def g2(q: int) -> int:
    return q * (q - 1) // 2 + A(q)


def beta(q: int) -> int:
    if q < 1:
        raise ValueError("beta is defined only for positive arguments")
    z = q - 1
    parity_term = z if z % 2 == 0 else z + 1
    return z * (z - 1) // 2 + A(z) + parity_term


def gamma_coefficient(index: int) -> sp.Rational:
    """Coefficient of G(z)/4 = 4 atan(z/5) - atan(z/239)."""
    if index <= 0 or index % 2 == 0:
        return sp.Rational(0)
    sign = -1 if ((index - 1) // 2) % 2 else 1
    return sign * sp.Rational(
        4 * 239**index - 5**index,
        index * 5**index * 239**index,
    )


def rational_digest(value: sp.Rational) -> str:
    numerator, denominator = value.as_numer_denom()
    encoded = f"{int(numerator)}/{int(denominator)}".encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def rational_size(value: sp.Rational) -> dict[str, int]:
    numerator, denominator = value.as_numer_denom()
    return {
        "numerator_bit_length": abs(int(numerator)).bit_length(),
        "denominator_bit_length": int(denominator).bit_length(),
    }


def exact_record(n: int) -> dict:
    if n < 1 or n % 4 not in (0, 1):
        raise ValueError("every n must be positive and congruent to 0 or 1 mod 4")

    row_indices = range(n + 1, 3 * n + 2)
    E = sp.Matrix(
        [
            [sp.Rational(1, factorial(k - j)) for j in range(n + 1)]
            for k in row_indices
        ]
    )
    P = sp.Matrix(
        [
            [sp.Rational(k - a - 1, factorial(k - a)) for a in range(n)]
            for k in row_indices
        ]
    )
    Gamma = sp.Matrix(
        [
            [gamma_coefficient(k - j) for j in range(n + 1)]
            for k in row_indices
        ]
    )
    Q = sp.Matrix(
        [
            [
                gamma_coefficient(k - a - 1) - gamma_coefficient(k - a)
                for a in range(n)
            ]
            for k in row_indices
        ]
    )

    D_E = E.row_join(Q).det(method="domain-ge")
    D_G = P.row_join(Gamma).det(method="domain-ge")
    first_column = E[:, 0] + 4 * Gamma[:, 0]
    determinant_T = (
        first_column.row_join(P).row_join(4 * Q).det(method="domain-ge")
    )

    decomposition_right = 4**n * (D_E + 4 * (-1) ** n * D_G)
    assert determinant_T == decomposition_right
    assert D_E != 0
    assert determinant_T != 0

    if n % 4 == 0:
        residue_class = 0
        R = n // 2
        least_term_valuation = (
            A(n + 1)
            - sum(
                factorial_valuation_2(k)
                for k in range(2 * n + 1, 3 * n + 2)
            )
            + 3 * g2(R)
            + beta(R + 1)
        )
        eta = (
            factorial_valuation_2(2 * n + 1)
            - factorial_valuation_2(n)
            + R
            + 2 * factorial_valuation_2(R)
        )
        formula_name = "v0 and eta_n from equations (29) and (38)"
    else:
        residue_class = 1
        R = (n + 1) // 2
        least_term_valuation = (
            A(n + 1)
            - sum(
                factorial_valuation_2(k)
                for k in range(2 * n + 1, 3 * n + 2)
            )
            + 2 * g2(R)
            + g2(R - 1)
            + beta(R)
        )
        eta = (
            factorial_valuation_2(2 * n + 1)
            - factorial_valuation_2(n)
            + (R - 1)
            + 2 * factorial_valuation_2(R - 1)
        )
        formula_name = "v1 and eta_n^(1) from equations (40d) and (40h)"

    valuation_D_E = valuation_2(D_E)
    valuation_D_G = valuation_2(D_G)
    valuation_T = valuation_2(determinant_T)
    assert valuation_D_E == least_term_valuation
    assert valuation_D_G >= least_term_valuation + eta
    assert valuation_T == 2 * n + least_term_valuation

    return {
        "n": n,
        "residue_class_mod_4": residue_class,
        "matrix_size": 2 * n + 1,
        "R": R,
        "formula_name": formula_name,
        "formula_least_D_E_valuation": least_term_valuation,
        "formula_D_G_gap_eta": eta,
        "D_E_2_adic_valuation": valuation_D_E,
        "D_G_2_adic_valuation": valuation_D_G,
        "observed_D_G_minus_D_E_valuation": valuation_D_G - valuation_D_E,
        "T_2_adic_valuation": valuation_T,
        "predicted_T_2_adic_valuation": 2 * n + least_term_valuation,
        "determinant_decomposition_exact": True,
        "D_E_sha256": rational_digest(D_E),
        "D_G_sha256": rational_digest(D_G),
        "T_sha256": rational_digest(determinant_T),
        "D_E_size": rational_size(D_E),
        "D_G_size": rational_size(D_G),
        "T_size": rational_size(determinant_T),
    }


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n-values",
        default="1,4,5,8,9,12,13,16",
        help="comma-separated positive integers congruent to 0 or 1 mod 4",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/machin_diagonal_free_coefficient.json"),
    )
    args = parser.parse_args()

    try:
        n_values = [int(item) for item in args.n_values.split(",") if item]
    except ValueError as error:
        raise SystemExit("--n-values must be comma-separated integers") from error
    if not n_values:
        raise SystemExit("--n-values must not be empty")

    records = [exact_record(n) for n in n_values]
    report = {
        "description": (
            "Exact QQ validation of the determinant proof for the first "
            "free diagonal Machin Hermite-Pade coefficient. Finite records "
            "are validation only; the source note proves every positive "
            "n congruent to 0 or 1 mod 4."
        ),
        "normalization": "Gamma is the coefficient matrix of G(z)/4.",
        "identity": "det(T_n) = 4^n (D_E + 4 (-1)^n D_G)",
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "output_sha256": sha256_file(args.output),
                "n_values": n_values,
                "all_checks_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
