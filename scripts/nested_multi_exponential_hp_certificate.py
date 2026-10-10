#!/usr/bin/env python3
"""Exact finite certificate for the nested multi-exponential HP audit.

The script uses rational arithmetic to construct the residue polynomials

    A_j(z) = [u^(r_j-1)] exp(u z) prod_{k != j}(j-k+u)^(-r_k)

for prescribed pole multiplicities ``r``.  It checks the saturated diagonal
type-I identities, a universal integer clearing, the adjacent-system
determinant formula, and the ranks of the small type-II constraint matrices.

The finite checks support (but do not replace) the all-parameter proofs in
``sources/nested_multi_exponential_hp_norm_barrier.md``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import reduce
from math import comb, factorial, gcd, lcm
from pathlib import Path

import sympy as sp


Z = sp.Symbol("z")


def convolve_truncated(a: list[Fraction], b: list[Fraction], top: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(top + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= top:
                out[i + j] += ai * bj
    return out


def residue_polynomials(multiplicities: tuple[int, ...]) -> list[list[Fraction]]:
    """Return A_j as coefficient lists in increasing powers of z."""
    ans: list[list[Fraction]] = []
    for j, pole_order in enumerate(multiplicities):
        top = pole_order - 1
        series = [Fraction(1)] + [Fraction(0) for _ in range(top)]
        for k, other_order in enumerate(multiplicities):
            if k == j:
                continue
            difference = j - k
            factor = [
                Fraction(
                    (-1) ** ell * comb(other_order + ell - 1, ell),
                    difference ** (other_order + ell),
                )
                for ell in range(top + 1)
            ]
            series = convolve_truncated(series, factor, top)
        ans.append(
            [series[top - power] / factorial(power) for power in range(pole_order)]
        )
    return ans


def sympy_expression(coefficients: list[Fraction]) -> sp.Expr:
    return sp.expand(
        sum(sp.Rational(value.numerator, value.denominator) * Z**power
            for power, value in enumerate(coefficients))
    )


def remainder_taylor_coefficient(
    polynomials: list[list[Fraction]], exponent: int
) -> Fraction:
    total = Fraction(0)
    for node, polynomial in enumerate(polynomials):
        for power, coefficient in enumerate(polynomial):
            if power <= exponent:
                total += coefficient * Fraction(
                    node ** (exponent - power), factorial(exponent - power)
                )
    return total


def rational_vector_primitive_scale(values: list[Fraction]) -> tuple[int, int]:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in values]
    content = reduce(gcd, (abs(value) for value in integers), 0)
    return denominator // content, content


def type_two_matrix(m: int, denominator_degree: int, first: int, last: int) -> sp.Matrix:
    # This is obtained from the Taylor constraint matrix
    # j^(ell-k)/(ell-k)! by multiplying row (j,ell) by the nonzero rational
    # ell! * j^(denominator_degree-ell).  The integer-equivalent matrix is
    # dramatically faster for exact rank computations.
    rows = []
    for node in range(1, m + 1):
        for ell in range(first, last + 1):
            rows.append(
                [
                    (factorial(ell) // factorial(ell - k))
                    * node ** (denominator_degree - k)
                    if k <= ell else 0
                    for k in range(denominator_degree + 1)
                ]
            )
    return sp.Matrix(rows)


def run_checks() -> dict:
    diagonal_records = []
    determinant_records = []
    type_two_records = []

    for m in range(1, 5):
        delta = lcm(*range(1, m + 1))
        for n in range(0, 5):
            multiplicities = tuple([n + 1] * (m + 1))
            polynomials = residue_polynomials(multiplicities)
            order = (m + 1) * (n + 1) - 1
            for ell in range(order):
                assert remainder_taylor_coefficient(polynomials, ell) == 0
            assert remainder_taylor_coefficient(polynomials, order) == Fraction(
                1, factorial(order)
            )

            clearing = factorial(n) * factorial(m) ** (n + 1) * delta**n
            flattened = [value for polynomial in polynomials for value in polynomial]
            assert all((clearing * value).denominator == 1 for value in flattened)
            primitive_scale, content = rational_vector_primitive_scale(flattened)
            primitive_integers = [int(primitive_scale * value) for value in flattened]

            diagonal_records.append(
                {
                    "m": m,
                    "n": n,
                    "order": order,
                    "universal_clearing": clearing,
                    "primitive_scale": primitive_scale,
                    "universal_integer_content": clearing // primitive_scale,
                    "primitive_height": max(abs(value) for value in primitive_integers),
                    "primitive_polynomials": [
                        str(sp.expand(primitive_scale * sympy_expression(poly)))
                        for poly in polynomials
                    ]
                    if (m, n) in {(1, 2), (2, 1), (2, 2), (3, 1)}
                    else None,
                }
            )

    # The adjacent determinant is the computationally heavier check.  The
    # ranges below include 20 nontrivial matrices up to size 4 by 4.
    for m in range(1, 4):
        delta = lcm(*range(1, m + 1))
        superfactorial = reduce(lambda a, b: a * b, (factorial(k) for k in range(m + 1)), 1)
        for n in range(0, 4):
            base = [n + 1] * (m + 1)
            rows = []
            for distinguished in range(m + 1):
                multiplicities = base.copy()
                multiplicities[distinguished] += 1
                rows.append(
                    [sympy_expression(poly) for poly in residue_polynomials(tuple(multiplicities))]
                )
            determinant = sp.factor(sp.det(sp.Matrix(rows)))
            exponent = (m + 1) * (n + 1)
            sign = (-1) ** ((n + 1) * m * (m + 1) // 2)
            denominator = factorial(n + 1) ** (m + 1) * superfactorial ** (2 * (n + 1))
            expected = sp.Rational(sign, denominator) * Z**exponent
            assert sp.expand(determinant - expected) == 0

            clearing = (
                factorial(n + 1)
                * factorial(m) ** (n + 2)
                * delta ** (n + 1)
            )
            for row in rows:
                for expression in row:
                    for coefficient in sp.Poly(clearing * expression, Z).all_coeffs():
                        assert coefficient.q == 1
            cleared_coefficient = sp.Rational(clearing ** (m + 1), denominator)
            assert cleared_coefficient.q == 1

            determinant_records.append(
                {
                    "m": m,
                    "n": n,
                    "exponent": exponent,
                    "determinant": str(determinant),
                    "universal_row_clearing": clearing,
                    "cleared_monomial_coefficient": int(cleared_coefficient),
                }
            )

    # Finite normality checks for the degree/order count in the type-II audit.
    for m in range(1, 5):
        for n in range(1, 7):
            standard_degree = m * n
            standard = type_two_matrix(
                m, standard_degree, standard_degree + 1, (m + 1) * n
            )
            standard_rank = standard.rank()
            assert standard_rank == m * n

            restricted = []
            max_extra = (n + m - 1) // m + 1
            for extra in range(1, max_extra + 1):
                matrix = type_two_matrix(m, n, n + 1, n + extra)
                expected_rank = min(m * extra, n + 1)
                rank = matrix.rank()
                assert rank == expected_rank
                restricted.append({"extra_orders": extra, "rank": rank})

            type_two_records.append(
                {
                    "m": m,
                    "n": n,
                    "standard_denominator_degree": standard_degree,
                    "standard_conditions": m * n,
                    "standard_rank": standard_rank,
                    "degree_n_restricted_ranks": restricted,
                }
            )

    variance_checks = []
    for m in range(1, 8):
        for n in range(0, 8):
            total_parameter = (m + 1) * (n + 1)
            mean = Fraction(m, 2)
            weighted_second = Fraction(sum(j * j for j in range(m + 1)), m + 1)
            variance = (weighted_second - mean * mean) / (total_parameter + 1)
            expected = Fraction(m * (m + 2), 12 * (total_parameter + 1))
            assert variance == expected
            variance_checks.append(
                {"m": m, "n": n, "variance": str(variance)}
            )

    return {
        "status": "accepted",
        "scope": {
            "diagonal_type_I": "1<=m<=4, 0<=n<=4",
            "adjacent_determinants": "1<=m<=3, 0<=n<=3",
            "type_II_ranks": "1<=m<=4, 1<=n<=6",
            "dirichlet_variance": "1<=m<=7, 0<=n<=7",
        },
        "diagonal_records": diagonal_records,
        "adjacent_determinant_records": determinant_records,
        "type_II_records": type_two_records,
        "dirichlet_variance_records": variance_checks,
        "disclaimer": (
            "These are exact finite checks of identities proved symbolically in the companion "
            "source note. They do not classify e+pi."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run_checks()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.write_bytes(encoded)
    print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
