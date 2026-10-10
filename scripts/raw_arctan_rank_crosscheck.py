#!/usr/bin/env python3
"""Exact low-degree cross-check for the all-m raw-arctangent rank proof.

This script is not part of the all-degree proof.  It independently checks,
with Fraction arithmetic, the square determinant T_ell, its complete Laplace
expansion, and the predicted unique least-2-adic summand for small ell.  It
also checks the rank of the original bordered integer matrix D_m.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from math import factorial
from pathlib import Path


def valuation_two_integer(value: int) -> int:
    if value == 0:
        raise ValueError("the 2-adic valuation of zero is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def valuation_two(value: Fraction) -> int:
    if value == 0:
        return 10**18
    return valuation_two_integer(value.numerator) - valuation_two_integer(value.denominator)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    if size == 0:
        return Fraction(1)
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for j in range(column, size):
            work[column][j] /= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column]
            if multiplier:
                for j in range(column, size):
                    work[row][j] -= multiplier * work[column][j]
    return result


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    row_count = len(work)
    column_count = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next((r for r in range(pivot_row, row_count) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        for j in range(column, column_count):
            work[pivot_row][j] /= pivot_value
        for row in range(row_count):
            if row == pivot_row:
                continue
            multiplier = work[row][column]
            if multiplier:
                for j in range(column, column_count):
                    work[row][j] -= multiplier * work[pivot_row][j]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def arctan_coefficient(index: int) -> Fraction:
    if index % 2 == 0:
        return Fraction(0)
    return Fraction((-1) ** ((index - 1) // 2), index)


def tau(index: int) -> int:
    if index % 2 == 0:
        return 0
    return (-1) ** ((index - 1) // 2) * factorial(index - 1)


def falling(k: int, a: int) -> int:
    return factorial(k) // factorial(k - a)


def original_matrix(m: int) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for k in range(m, 3 * m - 2):
        left = [Fraction(falling(k, a)) for a in range(m)]
        right = [Fraction(falling(k, a) * tau(k - a)) for a in range(m)]
        rows.append(left + right)
    rows.append([Fraction(-4)] * m + [Fraction(1)] * m)
    return rows


def reduced_blocks(ell: int) -> tuple[list[int], list[list[Fraction]], list[list[Fraction]]]:
    row_labels = list(range(ell + 1, 3 * ell + 1))
    p_block = [
        [Fraction(k - a - 1, factorial(k - a)) for a in range(ell)]
        for k in row_labels
    ]
    q_block = [
        [arctan_coefficient(k - a - 1) - arctan_coefficient(k - a) for a in range(ell)]
        for k in row_labels
    ]
    return row_labels, p_block, q_block


def submatrix_rows(matrix: list[list[Fraction]], indices: tuple[int, ...]) -> list[list[Fraction]]:
    return [matrix[i][:] for i in indices]


def check_ell(ell: int) -> dict[str, object]:
    row_labels, p_block, q_block = reduced_blocks(ell)
    full_matrix = [p + q for p, q in zip(p_block, q_block)]
    full_determinant = determinant(full_matrix)

    terms: list[tuple[int, tuple[int, ...], Fraction]] = []
    laplace_sum = Fraction(0)
    all_indices = tuple(range(2 * ell))
    for selected in itertools.combinations(all_indices, ell):
        selected_set = set(selected)
        complement = tuple(i for i in all_indices if i not in selected_set)
        p_det = determinant(submatrix_rows(p_block, selected))
        q_det = determinant(submatrix_rows(q_block, complement))
        sign = (-1) ** (sum(selected) + ell * (ell - 1) // 2)
        term = sign * p_det * q_det
        laplace_sum += term
        if term:
            terms.append((valuation_two(term), selected, term))

    least_valuation = min(item[0] for item in terms)
    minimizing = [item for item in terms if item[0] == least_valuation]
    if ell % 2 == 0:
        predicted_labels = tuple(range(2 * ell + 1, 3 * ell + 1))
    else:
        predicted_labels = (2 * ell,) + tuple(range(2 * ell + 2, 3 * ell + 1))
    predicted_indices = tuple(row_labels.index(label) for label in predicted_labels)

    m = ell + 1
    d_matrix = original_matrix(m)
    d_rank = rank(d_matrix)
    assertions = {
        "reduced_determinant_nonzero": full_determinant != 0,
        "laplace_sum_equals_direct_determinant": laplace_sum == full_determinant,
        "unique_least_valuation_term": len(minimizing) == 1,
        "least_term_has_predicted_rows": minimizing[0][1] == predicted_indices,
        "original_D_m_full_row_rank": d_rank == 2 * m - 1,
    }
    if not all(assertions.values()):
        raise AssertionError({"ell": ell, "assertions": assertions})

    return {
        "ell": ell,
        "m": m,
        "reduced_matrix_shape": [2 * ell, 2 * ell],
        "reduced_determinant_numerator": str(full_determinant.numerator),
        "reduced_determinant_denominator": str(full_determinant.denominator),
        "reduced_determinant_2_adic_valuation": valuation_two(full_determinant),
        "nonzero_laplace_terms": len(terms),
        "least_laplace_term_2_adic_valuation": least_valuation,
        "predicted_minimizing_actual_row_labels": list(predicted_labels),
        "verified_minimizing_actual_row_labels": [row_labels[i] for i in minimizing[0][1]],
        "original_D_m_rank": d_rank,
        "original_D_m_rows": 2 * m - 1,
        "assertions": assertions,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-ell", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_ell < 1:
        raise ValueError("--max-ell must be positive")

    records = [check_ell(ell) for ell in range(1, args.max_ell + 1)]
    result = {
        "checked_ell_inclusive": [1, args.max_ell],
        "all_checks_passed": True,
        "warning": (
            "This is an exact low-degree cross-check.  The all-degree proof is the "
            "2-adic argument in sources/raw_arctan_bordered_rank_proof.md."
        ),
        "records": records,
    }
    payload = json.dumps(result, indent=2, sort_keys=True).encode()
    rendered = payload.decode() + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
