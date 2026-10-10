#!/usr/bin/env python3
"""Independent exact-arithmetic audit of the diagonal Machin determinant.

This implementation deliberately does not import SymPy or any code from
``machin_diagonal_free_coefficient.py``.  Rational matrices are represented
with ``fractions.Fraction``.  Each row is cleared independently and the
resulting integer determinant is evaluated by a locally implemented Bareiss
elimination.  For n = 1, 4, 5 the script also enumerates every Laplace term
of D_E and checks that the unique term of least 2-adic valuation is S_0.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import factorial, gcd
from pathlib import Path


ARCHIVE_N_VALUES = (1, 4, 5, 8, 9, 12, 13, 16)


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def v2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def v2(value: Fraction) -> int:
    return v2_integer(value.numerator) - v2_integer(value.denominator)


def phi(k: int) -> int:
    if k < 0:
        raise ValueError("factorial index must be nonnegative")
    answer = 0
    while k:
        k //= 2
        answer += k
    return answer


def asum(q: int) -> int:
    return sum(phi(j) for j in range(q))


def g2(q: int) -> int:
    return q * (q - 1) // 2 + asum(q)


def beta(q: int) -> int:
    z = q - 1
    if z < 0:
        raise ValueError("beta requires q >= 1")
    return z * (z - 1) // 2 + asum(z) + z + (z & 1)


def gamma(index: int) -> Fraction:
    if index <= 0 or index % 2 == 0:
        return Fraction(0)
    sign = -1 if ((index - 1) // 2) & 1 else 1
    return sign * Fraction(
        4 * 239**index - 5**index,
        index * 5**index * 239**index,
    )


def bareiss_integer_determinant(matrix: list[list[int]]) -> int:
    """Return det(matrix) by exact fraction-free elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    if size == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    previous_pivot = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        for row in range(column + 1, size):
            for col in range(column + 1, size):
                numerator = (
                    work[row][col] * pivot
                    - work[row][column] * work[column][col]
                )
                quotient, remainder = divmod(numerator, previous_pivot)
                if remainder:
                    raise ArithmeticError("Bareiss division was not exact")
                work[row][col] = quotient
            work[row][column] = 0
        previous_pivot = pivot
    return sign * work[-1][-1]


def rational_determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Clear each row separately, then call integer Bareiss elimination."""

    if not matrix:
        return Fraction(1)
    integer_matrix: list[list[int]] = []
    scale_product = 1
    for row in matrix:
        scale = 1
        for entry in row:
            scale = lcm(scale, entry.denominator)
        integer_matrix.append(
            [entry.numerator * (scale // entry.denominator) for entry in row]
        )
        scale_product *= scale
    return Fraction(bareiss_integer_determinant(integer_matrix), scale_product)


def submatrix(
    matrix: list[list[Fraction]], rows: tuple[int, ...]
) -> list[list[Fraction]]:
    return [matrix[row] for row in rows]


def join(*blocks: list[list[Fraction]]) -> list[list[Fraction]]:
    if not blocks:
        return []
    row_count = len(blocks[0])
    if any(len(block) != row_count for block in blocks):
        raise ValueError("joined blocks must have the same number of rows")
    return [
        [entry for block in blocks for entry in block[row]]
        for row in range(row_count)
    ]


def digest(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode("ascii")
    ).hexdigest()


def build_blocks(n: int) -> tuple[
    list[list[Fraction]],
    list[list[Fraction]],
    list[list[Fraction]],
    list[list[Fraction]],
]:
    rows = range(n + 1, 3 * n + 2)
    e_block = [
        [Fraction(1, factorial(k - j)) for j in range(n + 1)] for k in rows
    ]
    p_block = [
        [Fraction(k - a - 1, factorial(k - a)) for a in range(n)]
        for k in rows
    ]
    gamma_block = [[gamma(k - j) for j in range(n + 1)] for k in rows]
    q_block = [
        [gamma(k - a - 1) - gamma(k - a) for a in range(n)] for k in rows
    ]
    return e_block, p_block, gamma_block, q_block


def formula_data(n: int) -> tuple[int, int]:
    if n % 4 == 0:
        rhalf = n // 2
        least = (
            asum(n + 1)
            - sum(phi(k) for k in range(2 * n + 1, 3 * n + 2))
            + 3 * g2(rhalf)
            + beta(rhalf + 1)
        )
        eta = phi(2 * n + 1) - phi(n) + rhalf + 2 * phi(rhalf)
    elif n % 4 == 1:
        rhalf = (n + 1) // 2
        least = (
            asum(n + 1)
            - sum(phi(k) for k in range(2 * n + 1, 3 * n + 2))
            + 2 * g2(rhalf)
            + g2(rhalf - 1)
            + beta(rhalf)
        )
        eta = (
            phi(2 * n + 1)
            - phi(n)
            + rhalf
            - 1
            + 2 * phi(rhalf - 1)
        )
    else:
        raise ValueError("the audit covers n congruent to 0 or 1 modulo 4")
    return least, eta


def enumerate_d_e_terms(
    n: int,
    e_block: list[list[Fraction]],
    q_block: list[list[Fraction]],
) -> dict[str, object]:
    row_count = 2 * n + 1
    all_rows = tuple(range(row_count))
    valuations: list[tuple[int, tuple[int, ...]]] = []
    zero_terms = 0
    for selected in itertools.combinations(all_rows, n + 1):
        selected_set = set(selected)
        complement = tuple(row for row in all_rows if row not in selected_set)
        term = rational_determinant(submatrix(e_block, selected))
        term *= rational_determinant(submatrix(q_block, complement))
        if term:
            valuations.append((v2(term), selected))
        else:
            zero_terms += 1
    least = min(value for value, _ in valuations)
    minimizers = [rows for value, rows in valuations if value == least]
    actual_minimizers = [
        [n + 1 + row for row in selected] for selected in minimizers
    ]
    sorted_distinct = sorted({value for value, _ in valuations})
    return {
        "term_count": len(valuations) + zero_terms,
        "zero_term_count": zero_terms,
        "least_term_valuation": least,
        "next_distinct_term_valuation": (
            sorted_distinct[1] if len(sorted_distinct) > 1 else None
        ),
        "minimizers_in_actual_row_indices": actual_minimizers,
    }


def audit_record(n: int) -> dict[str, object]:
    e_block, p_block, gamma_block, q_block = build_blocks(n)
    d_e = rational_determinant(join(e_block, q_block))
    d_g = rational_determinant(join(p_block, gamma_block))
    first_column = [
        [e_block[row][0] + 4 * gamma_block[row][0]]
        for row in range(2 * n + 1)
    ]
    four_q = [[4 * entry for entry in row] for row in q_block]
    determinant_t = rational_determinant(join(first_column, p_block, four_q))
    decomposition = 4**n * (d_e + 4 * (-1) ** n * d_g)
    least, eta = formula_data(n)

    assert determinant_t == decomposition
    assert v2(d_e) == least
    assert v2(d_g) >= least + eta
    assert v2(determinant_t) == 2 * n + least

    record: dict[str, object] = {
        "n": n,
        "D_E_sha256": digest(d_e),
        "D_G_sha256": digest(d_g),
        "T_sha256": digest(determinant_t),
        "D_E_2_adic_valuation": v2(d_e),
        "D_G_2_adic_valuation": v2(d_g),
        "T_2_adic_valuation": v2(determinant_t),
        "formula_least_D_E_valuation": least,
        "formula_eta": eta,
        "determinant_decomposition_exact": True,
    }
    if n in (1, 4, 5):
        enumeration = enumerate_d_e_terms(n, e_block, q_block)
        assert enumeration["least_term_valuation"] == least
        assert enumeration["minimizers_in_actual_row_indices"] == [
            list(range(2 * n + 1, 3 * n + 2))
        ]
        record["D_E_Laplace_enumeration"] = enumeration
    return record


def main() -> None:
    records = [audit_record(n) for n in ARCHIVE_N_VALUES]
    output = {
        "description": (
            "Independent Fraction/Bareiss regeneration of the frozen diagonal "
            "Machin determinant checks; exhaustive D_E Laplace enumeration is "
            "included for n=1,4,5."
        ),
        "records": records,
    }
    output_path = Path(
        "/content/drive/MyDrive/e_pi_research_20260826/results/"
        "independent_diagonal_machin_audit.json"
    )
    output_path.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "all_checks_passed": True,
                "output": str(output_path),
                "output_sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
