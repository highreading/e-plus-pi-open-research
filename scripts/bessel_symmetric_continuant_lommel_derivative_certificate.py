#!/usr/bin/env python3
"""Deterministic exact replay for the symmetric-continuant derivative theorem."""

from __future__ import annotations

import hashlib
import json
import math
import resource
import time
from pathlib import Path


DEPENDENCIES = {
    "sources/bessel_ordinary_symmetric_transfer_base_carry_barrier.md": (
        "769c886c1c8e5a6e406bd2018c71846e2831170359c2e97b43939e200a108c6e"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_dependencies(repo: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(repo / relative)
        assert actual == expected, (relative, expected, actual)
        observed[relative] = actual
    return observed


def continuant(values: list[int]) -> int:
    previous_previous, previous = 0, 1
    for value in values:
        previous_previous, previous = previous, value * previous + previous_previous
    return previous


def polynomial_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def multiply_by_shift(polynomial: list[int], offset: int) -> list[int]:
    result = [0] * (len(polynomial) + 1)
    for degree, coefficient in enumerate(polynomial):
        result[degree] += offset * coefficient
        result[degree + 1] += coefficient
    return result


def symmetric_continuant_polynomial(h: int) -> list[int]:
    previous_previous = [0]
    previous = [1]
    for index in range(-h, h + 1):
        current = polynomial_add(
            multiply_by_shift(previous, 4 * index), previous_previous
        )
        previous_previous, previous = previous, current
    return previous


def tail_formula(h: int, j: int) -> int:
    n = h - j
    total = 0
    for ell in range(n // 2 + 1):
        numerator = (
            4 ** (n - 2 * ell)
            * math.factorial(n - ell)
            * math.factorial(h - ell)
        )
        denominator = (
            math.factorial(ell)
            * math.factorial(n - 2 * ell)
            * math.factorial(j + ell)
        )
        quotient, remainder = divmod(numerator, denominator)
        assert remainder == 0
        total += quotient
    return total


def tails(h: int) -> list[int]:
    result = [0] * (h + 2)
    result[h] = 1
    result[h + 1] = 0
    for j in range(h - 1, -1, -1):
        result[j] = 4 * (j + 1) * result[j + 1] + result[j + 2]
    return result


def derivative_by_dual_numbers(h: int) -> int:
    value_previous_previous, derivative_previous_previous = 0, 0
    value_previous, derivative_previous = 1, 0
    for index in range(-h, h + 1):
        offset = 4 * index
        value = offset * value_previous + value_previous_previous
        derivative = (
            value_previous
            + offset * derivative_previous
            + derivative_previous_previous
        )
        value_previous_previous, derivative_previous_previous = (
            value_previous,
            derivative_previous,
        )
        value_previous, derivative_previous = value, derivative
    return derivative_previous


def derivative_by_cofactors(h: int) -> int:
    offsets = [4 * index for index in range(-h, h + 1)]
    return sum(
        continuant(offsets[:position]) * continuant(offsets[position + 1 :])
        for position in range(len(offsets))
    )


def derivative_by_squares(h: int) -> int:
    values = tails(h)
    bracket = values[0] ** 2 + 2 * sum(
        (-1) ** j * values[j] ** 2 for j in range(1, h + 1)
    )
    return (-1) ** h * bracket


def derivative_by_single_sum(h: int) -> int:
    return sum(
        (-16) ** a
        * math.factorial(a) ** 2
        * math.comb(h + a + 1, 2 * a + 1)
        for a in range(h + 1)
    )


def matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    rows = len(left)
    middle = len(right)
    columns = len(right[0])
    assert len(left[0]) == middle
    return [
        [sum(left[i][k] * right[k][j] for k in range(middle)) for j in range(columns)]
        for i in range(rows)
    ]


def parity_blocks(h: int) -> tuple[list[list[int]], list[list[int]]]:
    # A maps the odd basis to the even basis; B maps even to odd.
    a = [[0] * h for _ in range(h + 1)]
    b = [[0] * (h + 1) for _ in range(h)]
    a[0][0] = 2
    for j in range(1, h + 1):
        a[j][j - 1] = 4 * j
        if j >= 2:
            a[j][j - 2] = -1
        if j < h:
            a[j][j] = 1
        b[j - 1][j - 1] = -1
        b[j - 1][j] = 4 * j
        if j < h:
            b[j - 1][j + 1] = 1
    return a, b


def pentadiagonal(h: int) -> list[list[int]]:
    if h == 1:
        return [[14]]
    matrix = [[0] * h for _ in range(h)]
    matrix[0][0] = 13
    for j in range(2, h):
        matrix[j - 1][j - 1] = 16 * j * j - 2
    matrix[h - 1][h - 1] = 16 * h * h - 1
    for j in range(1, h):
        matrix[j - 1][j] = 8 * j + 4
        matrix[j][j - 1] = -(8 * j + 4)
    for j in range(1, h - 1):
        matrix[j - 1][j + 1] = 1
        matrix[j + 1][j - 1] = 1
    return matrix


def determinant_bareiss(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    previous_pivot = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                row
                for row in range(pivot_index + 1, size)
                if work[row][pivot_index] != 0
            )
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                quotient, remainder = divmod(numerator, previous_pivot)
                assert remainder == 0
                work[row][column] = quotient
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
        previous_pivot = pivot
    return sign * work[-1][-1]


def q_mod(index: int, modulus: int) -> int:
    if index <= 1:
        return 1
    previous, current = 1, 1
    for n in range(2, index + 1):
        previous, current = current, ((4 * n - 2) * current + previous) % modulus
    return current


def exact_formula_checks(max_h: int) -> dict[str, object]:
    factorial_checks = 0
    recurrence_checks = 0
    derivative_checks = 0
    single_sum_checks = 0
    polynomial_checks = 0
    bound_checks = 0
    samples: list[dict[str, object]] = []
    for h in range(max_h + 1):
        values = tails(h)
        for j in range(h + 1):
            direct = continuant(list(range(4 * (j + 1), 4 * h + 1, 4)))
            assert values[j] == direct == tail_formula(h, j)
            factorial_checks += 1
            if j < h:
                assert values[j] == 4 * (j + 1) * values[j + 1] + values[j + 2]
                assert values[j] >= 4 * (j + 1) * values[j + 1]
                assert (values[j] == 4 * (j + 1) * values[j + 1]) == (j == h - 1)
                recurrence_checks += 1

        derivative = derivative_by_dual_numbers(h)
        assert derivative == derivative_by_cofactors(h) == derivative_by_squares(h)
        derivative_checks += 1
        assert derivative == derivative_by_single_sum(h)
        single_sum_checks += 1
        bracket = (-1) ** h * derivative
        assert 13 * values[0] ** 2 < 15 * bracket < 17 * values[0] ** 2
        bound_checks += 1

        polynomial = symmetric_continuant_polynomial(h)
        assert polynomial[0] == 0
        assert polynomial[1] == derivative
        assert all(coefficient == 0 for degree, coefficient in enumerate(polynomial) if degree % 2 == 0)
        assert polynomial[-1] == 1
        polynomial_checks += 1
        if h <= 6:
            samples.append(
                {
                    "h": h,
                    "tail_P_h0": values[0],
                    "K_derivative_at_zero": derivative,
                    "positive_bracket": bracket,
                    "polynomial_coefficients_low_to_high": polynomial,
                }
            )
    return {
        "max_h_inclusive": max_h,
        "factorial_tail_checks": factorial_checks,
        "tail_recurrence_checks": recurrence_checks,
        "dual_cofactor_square_derivative_checks": derivative_checks,
        "single_terminating_sum_checks": single_sum_checks,
        "odd_monic_polynomial_checks": polynomial_checks,
        "strict_13_15_17_15_bound_checks": bound_checks,
        "small_samples": samples,
    }


def determinant_checks(max_h: int) -> dict[str, int]:
    block_checks = 0
    determinant_checks_count = 0
    cauchy_binet_minor_checks = 0
    for h in range(1, max_h + 1):
        a, b = parity_blocks(h)
        product = matrix_multiply(b, a)
        expected = pentadiagonal(h)
        assert product == expected
        block_checks += 1
        determinant = determinant_bareiss(expected)
        assert determinant == (-1) ** h * derivative_by_dual_numbers(h)
        assert determinant == (-1) ** h * derivative_by_squares(h)
        determinant_checks_count += 1
        values = tails(h)
        for omitted in range(h + 1):
            retained = [index for index in range(h + 1) if index != omitted]
            b_minor = [[b[row][column] for column in retained] for row in range(h)]
            a_minor = [[a[row][column] for column in range(h)] for row in retained]
            term = determinant_bareiss(b_minor) * determinant_bareiss(a_minor)
            expected_term = (
                values[0] ** 2
                if omitted == 0
                else 2 * (-1) ** omitted * values[omitted] ** 2
            )
            assert term == expected_term
            cauchy_binet_minor_checks += 1
    return {
        "max_h_inclusive": max_h,
        "exact_BA_entry_checks": block_checks,
        "bareiss_determinant_checks": determinant_checks_count,
        "individual_cauchy_binet_minor_checks": cauchy_binet_minor_checks,
    }


def diagnostic_checks() -> dict[str, int]:
    derivative_h2 = derivative_by_dual_numbers(2)
    assert derivative_h2 == 963 == 9 * 107
    q50 = q_mod(50, 107)
    assert q50 == 26
    return {
        "h": 2,
        "K_derivative_at_zero": derivative_h2,
        "large_prime_divisor": 107,
        "tied_r": 50,
        "q_50_mod_107": q50,
    }


def main() -> None:
    started = time.perf_counter()
    repo = Path(__file__).resolve().parents[1]
    result = {
        "description": (
            "Deterministic exact replay of the all-h Lommel-square and "
            "pentadiagonal formulas for the symmetric Bessel continuant derivative."
        ),
        "frozen_dependencies": check_dependencies(repo),
        "formula_checks": exact_formula_checks(80),
        "pentadiagonal_checks": determinant_checks(32),
        "modular_scope_diagnostic": diagnostic_checks(),
        "scope_warning": (
            "All-h formulas and inequalities are symbolically proved in the source; "
            "finite cutoffs are regression checks only. Integer nonvanishing does not "
            "imply nonvanishing modulo p. This package does not prove the remaining "
            "Charlier congruence or Bessel base squarefreeness."
        ),
    }
    output = repo / "results/bessel_symmetric_continuant_lommel_derivative_certificate.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    elapsed = time.perf_counter() - started
    rss_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"live_metrics: elapsed_seconds={elapsed:.6f}, peak_rss_mib={rss_mib:.3f}")


if __name__ == "__main__":
    main()
