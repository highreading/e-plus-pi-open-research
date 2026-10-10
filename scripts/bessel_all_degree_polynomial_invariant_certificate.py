#!/usr/bin/env python3
"""Exact checks for the all-degree Bessel polynomial-invariant exclusion."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


Polynomial = tuple[int, ...]


def normalize(values: list[int] | tuple[int, ...]) -> Polynomial:
    result = list(values)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def poly_add(first: Polynomial, second: Polynomial) -> Polynomial:
    size = max(len(first), len(second))
    return normalize(
        [
            (first[index] if index < len(first) else 0)
            + (second[index] if index < len(second) else 0)
            for index in range(size)
        ]
    )


def poly_scale(scale: int, polynomial: Polynomial) -> Polynomial:
    return normalize([scale * coefficient for coefficient in polynomial])


def poly_mul(first: Polynomial, second: Polynomial) -> Polynomial:
    result = [0] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            result[first_index + second_index] += first_value * second_value
    return normalize(result)


def poly_power(polynomial: Polynomial, exponent: int) -> Polynomial:
    result: Polynomial = (1,)
    factor = polynomial
    while exponent:
        if exponent & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        exponent //= 2
    return result


def bessel_solutions(maximum_index: int) -> tuple[list[int], list[int], list[int]]:
    q_values = [1, 1]
    p_values = [1, 3]
    for index in range(2, maximum_index + 1):
        coefficient = 4 * index - 2
        q_values.append(coefficient * q_values[-1] + q_values[-2])
        p_values.append(coefficient * p_values[-1] + p_values[-2])
    s_values = [
        (p_value - q_value) // 2
        for p_value, q_value in zip(p_values, q_values)
    ]
    return p_values, q_values, s_values


def recurrence_and_transfer_checks() -> dict[str, object]:
    maximum_index = 120
    p_values, q_values, s_values = bessel_solutions(maximum_index)
    recurrence_checks = 0
    wronskian_checks = 0
    transfer_checks = 0
    growth_checks = 0
    representatives: list[dict[str, object]] = []

    assert s_values[0:2] == [0, 1]
    for index in range(maximum_index + 1):
        assert p_values[index] % 2 == 1
        assert q_values[index] % 2 == 1
        assert p_values[index] - q_values[index] == 2 * s_values[index]
        if index >= 2:
            coefficient = 4 * index - 2
            for values in [p_values, q_values, s_values]:
                assert values[index] == (
                    coefficient * values[index - 1] + values[index - 2]
                )
                recurrence_checks += 1

    for index in range(1, maximum_index + 1):
        wronskian = (
            q_values[index] * s_values[index - 1]
            - s_values[index] * q_values[index - 1]
        )
        assert wronskian == (-1) ** index
        wronskian_checks += 1

        sign = (-1) ** index
        f_matrix = (
            (sign * q_values[index], sign * s_values[index]),
            (
                -sign * q_values[index - 1],
                -sign * s_values[index - 1],
            ),
        )
        determinant = (
            f_matrix[0][0] * f_matrix[1][1]
            - f_matrix[0][1] * f_matrix[1][0]
        )
        assert determinant == (-1) ** (index + 1)
        # F_n^{-1} e_2.
        inverse_column = (
            -f_matrix[0][1] // determinant,
            f_matrix[0][0] // determinant,
        )
        f_one = ((-1, -1), (1, 0))
        transfer_inverse_column = (
            f_one[0][0] * inverse_column[0]
            + f_one[0][1] * inverse_column[1],
            f_one[1][0] * inverse_column[0]
            + f_one[1][1] * inverse_column[1],
        )
        assert transfer_inverse_column == (
            q_values[index] - s_values[index],
            s_values[index],
        )
        transfer_checks += 1

        if index >= 2 and index % 2 == 0:
            assert q_values[index] >= index**index
            growth_checks += 1

        if index in [1, 2, 5, 12, 40, 80, 120]:
            representatives.append(
                {
                    "n": index,
                    "p_n": p_values[index],
                    "q_n": q_values[index],
                    "s_n": s_values[index],
                    "Wronskian": wronskian,
                    "M_n_inverse_e2": list(transfer_inverse_column),
                }
            )

    return {
        "solution_recurrence_checks": recurrence_checks,
        "Wronskian_checks": wronskian_checks,
        "fundamental_transfer_inverse_checks": transfer_checks,
        "even_superpolynomial_growth_checks": growth_checks,
        "representatives": representatives,
    }


def homogeneous_restriction_checks() -> dict[str, object]:
    checks = 0
    representatives: list[dict[str, object]] = []
    one_minus_t: Polynomial = (1, -1)
    t_polynomial: Polynomial = (0, 1)
    for state_degree in range(1, 13):
        coefficient_samples = [
            tuple(1 if index == selected else 0 for index in range(state_degree + 1))
            for selected in range(state_degree + 1)
        ]
        coefficient_samples.extend(
            [
                tuple((3 * index + seed) % 7 - 3 for index in range(state_degree + 1))
                for seed in range(1, 5)
            ]
        )
        for coefficients in coefficient_samples:
            if not any(coefficients):
                continue
            restriction: Polynomial = (0,)
            for index, coefficient in enumerate(coefficients):
                term = poly_mul(
                    poly_power(one_minus_t, state_degree - index),
                    poly_power(t_polynomial, index),
                )
                restriction = poly_add(
                    restriction, poly_scale(coefficient, term)
                )
            assert restriction != (0,)
            checks += 1
            if (state_degree, coefficients) in [
                (3, (1, 0, 0, 0)),
                (5, (0, 0, 1, 0, 0, 0)),
            ]:
                representatives.append(
                    {
                        "state_degree": state_degree,
                        "homogeneous_coefficients": list(coefficients),
                        "R_t_coefficients": list(restriction),
                    }
                )
    return {
        "nonzero_affine_line_restriction_checks": checks,
        "representatives": representatives,
    }


def matrix_rank_mod(matrix: list[list[int]], modulus: int) -> int:
    work = [[entry % modulus for entry in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0]) if work else 0
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
        inverse = pow(work[pivot_row][column], -1, modulus)
        for index in range(column, column_count):
            work[pivot_row][index] = (
                work[pivot_row][index] * inverse
            ) % modulus
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            for index in range(column, column_count):
                work[row][index] = (
                    work[row][index]
                    - scale * work[pivot_row][index]
                ) % modulus
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def shifted_monomial(exponent: int) -> Polynomial:
    return tuple(math.comb(exponent, index) for index in range(exponent + 1))


def affine_power(exponent: int) -> Polynomial:
    """Return (4x+2)^exponent."""
    return tuple(
        math.comb(exponent, index)
        * 2 ** (exponent - index)
        * 4**index
        for index in range(exponent + 1)
    )


def invariant_matrix(
    state_degree: int, index_degree: int, multiplier: int
) -> list[list[int]]:
    """Linear system for one homogeneous state degree in equation (2)."""
    column_count = (state_degree + 1) * (index_degree + 1)
    maximum_index_degree = index_degree + state_degree
    row_count = (state_degree + 1) * (maximum_index_degree + 1)
    matrix = [[0] * column_count for _ in range(row_count)]
    affine_powers = [
        affine_power(exponent) for exponent in range(state_degree + 1)
    ]

    # Input state monomial i is y^(m-i) z^i.  After
    # (y,z) -> (-(4x+2)y+z,y), choose k powers of z.
    for state_index in range(state_degree + 1):
        first_power = state_degree - state_index
        for index_exponent in range(index_degree + 1):
            column = (
                state_index * (index_degree + 1) + index_exponent
            )
            shifted = shifted_monomial(index_exponent)
            for output_state_index in range(first_power + 1):
                scalar = (
                    math.comb(first_power, output_state_index)
                    * (-1) ** (first_power - output_state_index)
                )
                polynomial = poly_scale(
                    scalar,
                    poly_mul(
                        shifted,
                        affine_powers[
                            first_power - output_state_index
                        ],
                    ),
                )
                row_offset = (
                    output_state_index * (maximum_index_degree + 1)
                )
                for power, coefficient in enumerate(polynomial):
                    matrix[row_offset + power][column] += coefficient

            target_row = (
                state_index * (maximum_index_degree + 1)
                + index_exponent
            )
            matrix[target_row][column] -= multiplier
    return matrix


def finite_rank_checks() -> dict[str, object]:
    modulus = 1_000_003
    records: list[dict[str, int]] = []
    for multiplier in [1, -1, 2]:
        for state_degree in range(1, 8):
            for index_degree in range(0, 11):
                matrix = invariant_matrix(
                    state_degree, index_degree, multiplier
                )
                rank = matrix_rank_mod(matrix, modulus)
                unknowns = (state_degree + 1) * (index_degree + 1)
                assert rank == unknowns
                records.append(
                    {
                        "lambda": multiplier,
                        "state_degree": state_degree,
                        "index_degree_bound": index_degree,
                        "rank_mod_1000003": rank,
                        "unknowns": unknowns,
                    }
                )
    return {
        "rank_modulus": modulus,
        "full_rank_system_checks": len(records),
        "records": records,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for the all-degree polynomial "
            "constant-multiplier invariant exclusion"
        ),
        "fundamental_solutions": recurrence_and_transfer_checks(),
        "homogeneous_line_restriction": homogeneous_restriction_checks(),
        "finite_symmetric_power_systems": finite_rank_checks(),
        "status": (
            "finite diagnostic; the all-state-degree theorem follows from "
            "the symbolic transfer-matrix and transcendence argument in "
            "the companion source; rational invariants and nonconstant "
            "Darboux multipliers are not claimed to be excluded"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_all_degree_polynomial_invariant_certificate.json"
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
