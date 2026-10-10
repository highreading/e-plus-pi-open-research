#!/usr/bin/env python3
"""Exact checks for Mahler/Newton residual and invariant barriers."""

from __future__ import annotations

import argparse
import hashlib
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
    return normalize([scale * value for value in polynomial])


def poly_sub(first: Polynomial, second: Polynomial) -> Polynomial:
    return poly_add(first, poly_scale(-1, second))


def poly_mul(first: Polynomial, second: Polynomial) -> Polynomial:
    result = [0] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            result[first_index + second_index] += first_value * second_value
    return normalize(result)


def poly_shift_one(polynomial: Polynomial) -> Polynomial:
    """Return polynomial(x+1), with ascending coefficients."""
    result = [0] * len(polynomial)
    for old_degree, value in enumerate(polynomial):
        for new_degree in range(old_degree + 1):
            result[new_degree] += value * math.comb(old_degree, new_degree)
    return normalize(result)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation requires a nonzero integer")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def factorial_valuation(value: int, prime: int) -> int:
    result = 0
    power = prime
    while power <= value:
        result += value // power
        power *= prime
    return result


def floor_log(value: int, prime: int) -> int:
    result = 0
    while value >= prime:
        value //= prime
        result += 1
    return result


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def bessel_denominators(maximum_index: int) -> list[int]:
    values = [1, 1]
    for index in range(2, maximum_index + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def mahler_coefficients(
    denominators: list[int], maximum_index: int
) -> list[int]:
    return [
        (-1) ** index
        * sum(
            math.comb(index, inner) * denominators[inner]
            for inner in range(index + 1)
        )
        for index in range(maximum_index + 1)
    ]


def mahler_value(
    coefficients: list[int], integer: int, cutoff: int
) -> int:
    return sum(
        coefficients[index] * math.comb(integer, index)
        for index in range(min(integer, cutoff) + 1)
    )


def mahler_checks() -> dict[str, object]:
    maximum_index = 90
    denominators = bessel_denominators(maximum_index + 2)
    coefficients = mahler_coefficients(denominators, maximum_index + 1)

    coefficient_checks = 0
    for index, coefficient in enumerate(coefficients):
        closed = (-1) ** index * sum(
            math.comb(index, inner) * denominators[inner]
            for inner in range(index + 1)
        )
        assert coefficient == closed
        divisor = math.factorial(index) // math.factorial(index // 2)
        assert coefficient % divisor == 0
        assert abs(coefficient) >= denominators[index]
        coefficient_checks += 1

    partial_checks = 0
    freeze_checks = 0
    for integer in range(1, 61):
        for cutoff in range(integer):
            direct = mahler_value(coefficients, integer, cutoff)
            same_sign = (-1) ** cutoff * sum(
                math.comb(integer, inner)
                * math.comb(integer - inner - 1, cutoff - inner)
                * denominators[inner]
                for inner in range(cutoff + 1)
            )
            assert direct == same_sign
            lower = math.comb(integer, cutoff) * denominators[cutoff]
            upper = (
                2**cutoff
                * math.comb(integer, cutoff)
                * denominators[cutoff]
            )
            assert lower <= abs(direct) <= upper
            partial_checks += 1

        for cutoff in [integer, integer + 1, integer + 4]:
            direct = mahler_value(coefficients, integer, cutoff)
            assert direct == (-1) ** integer * denominators[integer]
            freeze_checks += 1

    return {
        "coefficient_and_divisibility_checks": coefficient_checks,
        "same_sign_partial_sum_checks": partial_checks,
        "post_degree_freeze_checks": freeze_checks,
        "representative_coefficients": {
            str(index): coefficients[index]
            for index in [0, 1, 2, 5, 12, 30, 60, 90]
        },
    }


def tail_and_half_depth_checks() -> dict[str, object]:
    primes = [value for value in range(2, 48) if is_prime(value)]
    exponent_checks = 0
    half_depth_checks = 0
    representatives: list[dict[str, int]] = []
    for prime in primes:
        previous_divisibility = 0
        for index in range(0, 181):
            divisibility = factorial_valuation(
                index, prime
            ) - factorial_valuation(index // 2, prime)
            assert divisibility >= previous_divisibility
            previous_divisibility = divisibility
            exponent_checks += 1

        for cutoff in range(0, 180):
            d_value = factorial_valuation(
                cutoff + 1, prime
            ) - factorial_valuation((cutoff + 1) // 2, prime)
            v_value = factorial_valuation(cutoff // 2, prime)
            gap = d_value - v_value
            if cutoff % 2 == 0:
                half = cutoff // 2
                central_value = (2 * half + 1) * math.comb(
                    2 * half, half
                )
            else:
                half = (cutoff - 1) // 2
                central_value = (half + 1) * math.comb(
                    2 * half + 2, half + 1
                )
            assert gap == valuation(central_value, prime)
            assert 0 <= gap <= 2 * (
                1 + floor_log(cutoff + 2, prime)
            )

            for root_depth in [
                0,
                v_value,
                d_value + v_value,
                3 * cutoff + 17,
            ]:
                certified = min(d_value, root_depth - v_value)
                assert certified <= (
                    root_depth / 2
                    + 1
                    + floor_log(cutoff + 2, prime)
                )
                half_depth_checks += 1
            exponent_checks += 1

            if (prime, cutoff) in [(2, 31), (3, 40), (7, 73), (47, 179)]:
                representatives.append(
                    {
                        "p": prime,
                        "K": cutoff,
                        "D_K": d_value,
                        "V_K": v_value,
                        "gap": gap,
                    }
                )

    return {
        "primes": primes,
        "divisibility_and_gap_checks": exponent_checks,
        "half_depth_checks": half_depth_checks,
        "representative_records": representatives,
    }


def local_newton_checks() -> dict[str, object]:
    primes = [3, 5, 7, 11]
    maximum_m = 13
    maximum_index = max(
        prime - 1 + prime * maximum_m for prime in primes
    )
    denominators = bessel_denominators(maximum_index + 2)
    coefficient_checks = 0
    partial_checks = 0
    freeze_checks = 0
    representatives: list[dict[str, int]] = []

    for prime in primes:
        for residue in range(prime):
            local_values = [
                (-1) ** (residue + prime * index)
                * denominators[residue + prime * index]
                for index in range(maximum_m + 1)
            ]
            local_coefficients = [
                sum(
                    (-1) ** (index - inner)
                    * math.comb(index, inner)
                    * local_values[inner]
                    for inner in range(index + 1)
                )
                for index in range(maximum_m + 1)
            ]
            for index, coefficient in enumerate(local_coefficients):
                same_sign = (-1) ** (index + residue) * sum(
                    math.comb(index, inner)
                    * denominators[residue + prime * inner]
                    for inner in range(index + 1)
                )
                assert coefficient == same_sign
                assert denominators[residue + prime * index] <= abs(
                    coefficient
                )
                assert abs(coefficient) <= (
                    2**index
                    * denominators[residue + prime * index]
                )
                coefficient_checks += 1

            for integer in range(1, maximum_m + 1):
                for cutoff in range(integer):
                    direct = sum(
                        local_coefficients[index]
                        * math.comb(integer, index)
                        for index in range(cutoff + 1)
                    )
                    same_sign = (-1) ** (cutoff + residue) * sum(
                        math.comb(integer, inner)
                        * math.comb(
                            integer - inner - 1, cutoff - inner
                        )
                        * denominators[residue + prime * inner]
                        for inner in range(cutoff + 1)
                    )
                    assert direct == same_sign
                    lower = (
                        math.comb(integer, cutoff)
                        * denominators[residue + prime * cutoff]
                    )
                    upper = (
                        2**cutoff
                        * math.comb(integer, cutoff)
                        * denominators[residue + prime * cutoff]
                    )
                    assert lower <= abs(direct) <= upper
                    partial_checks += 1

                frozen = sum(
                    local_coefficients[index]
                    * math.comb(integer, index)
                    for index in range(integer + 1)
                )
                assert frozen == local_values[integer]
                freeze_checks += 1

            if residue == 1:
                representatives.append(
                    {
                        "p": prime,
                        "r": residue,
                        "C_4": local_coefficients[4],
                        "lower_q_index": residue + 4 * prime,
                        "lower_q": denominators[residue + 4 * prime],
                    }
                )

    return {
        "coefficient_height_checks": coefficient_checks,
        "same_sign_partial_sum_checks": partial_checks,
        "freeze_checks": freeze_checks,
        "representative_records": representatives,
    }


def matrix_rank_mod(matrix: list[list[int]], modulus: int) -> int:
    if not matrix:
        return 0
    work = [
        [entry % modulus for entry in row]
        for row in matrix
    ]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] % modulus
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, modulus)
        work[pivot_row] = [
            entry * inverse % modulus for entry in work[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    (work[row][index] - scale * work[pivot_row][index])
                    % modulus
                    for index in range(column_count)
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def invariant_equations(
    degree: int, epsilon: int
) -> list[list[int]]:
    unknown_count = 3 * (degree + 1)
    maximum_output_degree = degree + 2
    row_count = 3 * (maximum_output_degree + 1)
    matrix = [[0] * unknown_count for _ in range(row_count)]
    affine = (2, 4)
    affine_squared = poly_mul(affine, affine)

    for column in range(unknown_count):
        block = column // (degree + 1)
        exponent = column % (degree + 1)
        monomial = tuple([0] * exponent + [1])
        u_value = monomial if block == 0 else (0,)
        v_value = monomial if block == 1 else (0,)
        w_value = monomial if block == 2 else (0,)
        u_next = poly_shift_one(u_value)
        v_next = poly_shift_one(v_value)
        w_next = poly_shift_one(w_value)
        e00 = poly_sub(
            poly_add(
                poly_mul(affine_squared, u_next),
                poly_add(
                    poly_scale(-2, poly_mul(affine, v_next)),
                    w_next,
                ),
            ),
            poly_scale(epsilon, u_value),
        )
        e01 = poly_sub(
            poly_add(
                poly_scale(-1, poly_mul(affine, u_next)),
                v_next,
            ),
            poly_scale(epsilon, v_value),
        )
        e11 = poly_sub(u_next, poly_scale(epsilon, w_value))
        for block_index, polynomial in enumerate([e00, e01, e11]):
            for output_degree, coefficient in enumerate(polynomial):
                row = (
                    block_index * (maximum_output_degree + 1)
                    + output_degree
                )
                matrix[row][column] = coefficient
    return matrix


def invariant_and_hankel_checks() -> dict[str, object]:
    modulus = 1_000_003
    rank_records: list[dict[str, int]] = []
    for epsilon in [1, -1]:
        for degree in range(0, 15):
            matrix = invariant_equations(degree, epsilon)
            rank = matrix_rank_mod(matrix, modulus)
            unknowns = 3 * (degree + 1)
            assert rank == unknowns
            rank_records.append(
                {
                    "epsilon": epsilon,
                    "degree_bound": degree,
                    "rank_mod_1000003": rank,
                    "unknowns": unknowns,
                }
            )

    denominators = bessel_denominators(180)
    coprimality_checks = 0
    for index in range(1, 179):
        hankel = (
            denominators[index - 1] * denominators[index + 1]
            - denominators[index] ** 2
        )
        assert hankel % denominators[index] == (
            denominators[index - 1] ** 2
        ) % denominators[index]
        assert math.gcd(hankel, denominators[index]) == 1
        coprimality_checks += 1

    return {
        "finite_degree_invariant_rank_checks": rank_records,
        "rank_modulus": modulus,
        "Hankel_coprimality_checks": coprimality_checks,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for global and local Newton "
            "residuals and polynomial quadratic invariant barriers"
        ),
        "global_Mahler": mahler_checks(),
        "tail_half_depth": tail_and_half_depth_checks(),
        "local_p_step_Newton": local_newton_checks(),
        "quadratic_invariant_and_Hankel": invariant_and_hankel_checks(),
        "status": (
            "finite diagnostic; all-index same-sign formulas, half-depth "
            "bound, visibility statements, and all-degree quadratic "
            "invariant exclusion are proved symbolically in the companion "
            "source; no root digit-depth bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_mahler_newton_residual_invariant_certificate.json"
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
