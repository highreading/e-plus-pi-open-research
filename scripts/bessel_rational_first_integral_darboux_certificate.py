#!/usr/bin/env python3
"""Exact diagnostics for rational Bessel first-integral exclusion."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        for index in range(column, column_count):
            work[pivot_row][index] = (
                work[pivot_row][index] * inverse
            ) % prime
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            scale = work[row][column]
            for index in range(column, column_count):
                work[row][index] = (
                    work[row][index]
                    - scale * work[pivot_row][index]
                ) % prime
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def bessel_transfer_checks() -> dict[str, object]:
    maximum_index = 100
    q_values = [1, 1]
    p_values = [1, 3]
    for index in range(2, maximum_index + 1):
        factor = 4 * index - 2
        q_values.append(factor * q_values[-1] + q_values[-2])
        p_values.append(factor * p_values[-1] + p_values[-2])
    s_values = [(p - q) // 2 for p, q in zip(p_values, q_values)]

    transfer_checks = 0
    growth_checks = 0
    representatives = []
    for index in range(1, maximum_index + 1):
        sign = (-1) ** index
        fundamental = sp.Matrix(
            [
                [sign * q_values[index], sign * s_values[index]],
                [
                    -sign * q_values[index - 1],
                    -sign * s_values[index - 1],
                ],
            ]
        )
        fundamental_one = sp.Matrix([[-1, -1], [1, 0]])
        transfer = fundamental * fundamental_one.inv()
        backward = transfer.inv() * sp.Matrix([0, 1])
        assert backward == sp.Matrix(
            [q_values[index] - s_values[index], s_values[index]]
        )
        transfer_checks += 1
        if index >= 2 and index % 2 == 0:
            assert q_values[index] >= index**index
            growth_checks += 1
        if index in [1, 2, 8, 20, 50, 100]:
            representatives.append(
                {
                    "n": index,
                    "q_n": q_values[index],
                    "s_n": s_values[index],
                    "backward_vector": [int(value) for value in backward],
                }
            )
    return {
        "transfer_inverse_checks": transfer_checks,
        "even_growth_checks": growth_checks,
        "representatives": representatives,
    }


def automorphism_checks() -> dict[str, object]:
    x, y, z = sp.symbols("x y z")

    def sigma(polynomial: sp.Expr) -> sp.Expr:
        return sp.expand(
            polynomial.subs(
                {x: x + 1, y: -(4 * x + 2) * y + z, z: y},
                simultaneous=True,
            )
        )

    def sigma_inverse(polynomial: sp.Expr) -> sp.Expr:
        return sp.expand(
            polynomial.subs(
                {x: x - 1, y: z, z: y + (4 * x - 2) * z},
                simultaneous=True,
            )
        )

    samples = [
        sp.Integer(1),
        x,
        y,
        z,
        x**3 * y**2 - 7 * x * y * z + 5 * z**3,
        (x**2 + 3 * x + 1) * (y**4 - 2 * y * z**3 + z**4),
    ]
    for sample in samples:
        assert sp.expand(sigma_inverse(sigma(sample)) - sample) == 0
        assert sp.expand(sigma(sigma_inverse(sample)) - sample) == 0
    return {
        "two_sided_inverse_sample_checks": len(samples),
        "sigma_generators": [str(sigma(item)) for item in [x, y, z]],
        "inverse_generators": [
            str(sigma_inverse(item)) for item in [x, y, z]
        ],
    }


def finite_darboux_checks() -> dict[str, object]:
    x, y, z = sp.symbols("x y z")
    multipliers = [
        sp.Integer(1),
        sp.Integer(-1),
        sp.Integer(2),
        x + 2,
        4 * x + 2,
        x**2 + 1,
    ]
    records = []
    for state_degree in range(1, 5):
        for index_degree in range(0, 6):
            monomials = [
                x**a * y ** (state_degree - b) * z**b
                for b in range(state_degree + 1)
                for a in range(index_degree + 1)
            ]
            for multiplier in multipliers:
                transformed = [
                    sp.expand(
                        monomial.subs(
                            {
                                x: x + 1,
                                y: -(4 * x + 2) * y + z,
                                z: y,
                            },
                            simultaneous=True,
                        )
                        - multiplier * monomial
                    )
                    for monomial in monomials
                ]
                coefficient_rows: dict[tuple[int, int, int], list[int]] = {}
                for column, polynomial in enumerate(transformed):
                    for powers, coefficient in sp.Poly(
                        polynomial, x, y, z
                    ).terms():
                        row = coefficient_rows.setdefault(
                            powers, [0] * len(monomials)
                        )
                        row[column] = int(coefficient)
                matrix = list(coefficient_rows.values())
                rank = rank_mod(matrix, 1_000_003)
                assert rank == len(monomials)
                records.append(
                    {
                        "state_degree": state_degree,
                        "index_degree": index_degree,
                        "multiplier": str(multiplier),
                        "rank": rank,
                        "unknowns": len(monomials),
                    }
                )
    return {
        "rank_modulus": 1_000_003,
        "full_rank_positive_state_degree_systems": len(records),
        "records": records,
    }


def multiplier_product_checks() -> dict[str, object]:
    multipliers = [
        ("1/3", lambda k: sp.Rational(1, 3)),
        ("2", lambda k: sp.Integer(2)),
        ("x+2", lambda k: sp.Integer(k + 2)),
        ("x^2+1", lambda k: sp.Integer(k * k + 1)),
    ]
    records = []
    for name, function in multipliers:
        product = sp.Integer(1)
        for n in range(2, 26):
            product *= function(n - 1)
            assert product != 0
            records.append(
                {
                    "multiplier": name,
                    "n": n,
                    "absolute_product_numerator": abs(int(sp.numer(product))),
                    "absolute_product_denominator": abs(int(sp.denom(product))),
                }
            )
    return {
        "nonzero_product_checks": len(records),
        "records": records,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for polynomial Darboux and rational "
            "first-integral exclusion for one Bessel state"
        ),
        "polynomial_automorphism": automorphism_checks(),
        "primitive_transfer": bessel_transfer_checks(),
        "finite_polynomial_multipliers": finite_darboux_checks(),
        "multiplier_products": multiplier_product_checks(),
        "status": (
            "finite diagnostic; the all-degree polynomial-Darboux theorem "
            "and UFD reduction of rational invariants are the symbolic "
            "proof in the companion source; multi-state and nonlocal "
            "constructions are not excluded"
        ),
        "versions": {"sympy": sp.__version__},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_rational_first_integral_darboux_certificate.json"
    )
    parser.add_argument("--output", type=Path, default=default_output)
    arguments = parser.parse_args()
    payload = build_payload()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_bytes(encoded)
    print(f"wrote {arguments.output}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
