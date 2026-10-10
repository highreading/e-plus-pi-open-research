#!/usr/bin/env python3
"""Exact certificate for the failure of a uniform s=1 rational telescoper.

For J_s=P^(alpha-s)/(z^q(1-z)^q) dz, this constructs the complete
Hermite-reduction system for

    a0 J_1 + a1 J_2 + a2 J_3 = d(H J_1),
    H=z(1-z)U/P, deg(U)<=7,

factors its determinant, and audits the only valid rank drops.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def build_system() -> tuple[sp.Matrix, tuple[sp.Symbol, ...], sp.Expr]:
    z, q = sp.symbols("z q")
    p_base = 1 + z + z**2 + z**3
    alpha = (2 * q - 3) / 3
    u = sp.symbols("u0:8")
    a = sp.symbols("a0:3")
    unknowns = (*u, *a)
    numerator = sum(u[index] * z**index for index in range(8))
    certificate = z * (1 - z) * numerator / p_base
    log_derivative = (
        -q / z
        + q / (1 - z)
        + (alpha - 1) * sp.diff(p_base, z) / p_base
    )
    recurrence = sum(a[index] / p_base**index for index in range(3))
    residual_numerator = sp.Poly(
        sp.together(
            sp.diff(certificate, z)
            + certificate * log_derivative
            - recurrence
        ).as_numer_denom()[0],
        z,
    )
    matrix, right = sp.linear_eq_to_matrix(
        residual_numerator.all_coeffs(), unknowns
    )
    assert right == sp.zeros(matrix.rows, 1)
    return matrix, unknowns, residual_numerator.as_expr()


def normalized_nullspace(
    matrix: sp.Matrix, q: sp.Symbol, value: sp.Rational
) -> list[list[sp.Expr]]:
    return [
        [sp.factor(entry) for entry in vector]
        for vector in matrix.subs(q, value).nullspace()
    ]


def modular_nullspace(matrix: sp.Matrix, prime: int) -> tuple[int, list[list[int]]]:
    rows = matrix.rows
    columns = matrix.cols
    values = [
        [int(matrix[row, column]) % prime for column in range(columns)]
        for row in range(rows)
    ]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        chosen = next(
            (row for row in range(pivot_row, rows) if values[row][column]),
            None,
        )
        if chosen is None:
            continue
        values[pivot_row], values[chosen] = values[chosen], values[pivot_row]
        inverse = pow(values[pivot_row][column], -1, prime)
        values[pivot_row] = [
            entry * inverse % prime for entry in values[pivot_row]
        ]
        for row in range(rows):
            if row == pivot_row or not values[row][column]:
                continue
            multiplier = values[row][column]
            values[row] = [
                (values[row][index] - multiplier * values[pivot_row][index])
                % prime
                for index in range(columns)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break

    free_columns = [
        column for column in range(columns) if column not in pivot_columns
    ]
    basis: list[list[int]] = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in reversed(list(enumerate(pivot_columns))):
            vector[pivot] = -sum(
                values[row][column] * vector[column]
                for column in free_columns
            ) % prime
        basis.append(vector)
    return pivot_row, basis


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    z, q = sp.symbols("z q")
    matrix, unknowns, _ = build_system()
    assert matrix.shape == (11, 11)

    determinant = sp.factor(matrix.det())
    expected = sp.factor(
        7_838_208
        * (q - 3)
        * (2 * q - 9) ** 2
        * (5 * q - 9)
        * (5 * q - 6)
    )
    assert sp.expand(determinant - expected) == 0

    exceptional_basis = normalized_nullspace(matrix, q, sp.Rational(9, 5))
    assert len(exceptional_basis) == 1
    exceptional_vector = exceptional_basis[0]
    expected_exceptional = [
        sp.Rational(-5, 4),
        sp.Rational(-5, 4),
        sp.Rational(-5, 4),
        sp.Rational(-5, 4),
        sp.Rational(25, 16),
        sp.Rational(25, 16),
        sp.Rational(25, 16),
        sp.Rational(25, 16),
        0,
        1,
        0,
    ]
    assert exceptional_vector == expected_exceptional

    # Verify the compact exceptional certificate directly.
    p_base = 1 + z + z**2 + z**3
    exceptional_h = sp.Rational(5, 16) * z * (1 - z) * (5 * z**4 - 4)
    exceptional_q = sp.Rational(9, 5)
    exceptional_alpha = (2 * exceptional_q - 3) / 3
    exceptional_log_derivative = (
        -exceptional_q / z
        + exceptional_q / (1 - z)
        + (exceptional_alpha - 1) * sp.diff(p_base, z) / p_base
    )
    exceptional_identity = sp.factor(
        sp.together(
            sp.diff(exceptional_h, z)
            + exceptional_h * exceptional_log_derivative
            - 1 / p_base
        )
    )
    assert exceptional_identity == 0

    # The other formal determinant root 5q-6=0 has a relation, but the
    # elementary ray equations show that it cannot occur for a valid prime.
    six_fifths_basis = normalized_nullspace(matrix, q, sp.Rational(6, 5))
    assert len(six_fifths_basis) == 1
    assert six_fifths_basis[0][-3:] == [sp.Rational(-25, 24), 1, 0]

    # For p=7,m=1,q=1 the determinant constant and 2q-9 both vanish.
    # Work directly over F_7: the only nullvectors have zero recurrence
    # coordinates, so there is still no nontrivial three-term relation.
    matrix_q1 = matrix.subs(q, 1)
    rank_mod_7, basis_mod_7 = modular_nullspace(matrix_q1, 7)
    assert rank_mod_7 == 9
    assert len(basis_mod_7) == 2
    assert all(vector[-3:] == [0, 0, 0] for vector in basis_mod_7)

    result = {
        "schema": "weighted-cayley-s1-three-term-no-go-v1",
        "unknown_order": [str(symbol) for symbol in unknowns],
        "matrix_shape": list(matrix.shape),
        "determinant": str(determinant),
        "constant_factorization": "7838208 = 2^9 * 3^7 * 7",
        "valid_ray_factor_analysis": {
            "q_minus_3": "impossible because q is positive, q<p, and 3 does not divide q",
            "two_q_minus_9": "only p=7,m=1,q=1; direct F_7 rank audit has no recurrence vector",
            "five_q_minus_9": "only p=10m+3; rank drop gives B_2=0 and no B_3 term",
            "five_q_minus_6": "no valid prime ray",
        },
        "exceptional_q_mod_p": "9/5",
        "exceptional_nullvector": [str(value) for value in exceptional_vector],
        "exceptional_recurrence_coordinates": [
            str(value) for value in exceptional_vector[-3:]
        ],
        "exceptional_compact_H": "5*z*(1-z)*(5*z^4-4)/16",
        "exceptional_identity_zero": True,
        "p7_rank": rank_mod_7,
        "p7_nullity": len(basis_mod_7),
        "p7_all_recurrence_coordinates_zero": True,
        "conclusion": (
            "The s=0 short rational telescoper does not propagate in the "
            "formal nonresonant connection at s=1.  Its complete simple-pole "
            "Hermite matrix is invertible after reduction on every valid "
            "nonexceptional ray; on p=10m+3 its sole reduced relation is the "
            "already-known B_2=0 identity.  Prime-specific higher-pole "
            "resonant certificates are outside this matrix."
        ),
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    digest = hashlib.sha256(payload).hexdigest()
    print(
        f"shape={matrix.shape}; determinant={determinant}; "
        f"p7_rank={rank_mod_7}; sha256={digest}"
    )
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
