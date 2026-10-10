#!/usr/bin/env python3
"""Exact checks for two-center Bessel evaluation lattices and determinants."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def evaluate(coefficients: tuple[int, ...] | list[int], integer: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * integer + coefficient
    return result


def height_one(coefficients: tuple[int, ...] | list[int]) -> int:
    return sum(abs(coefficient) for coefficient in coefficients)


def content(coefficients: tuple[int, ...] | list[int]) -> int:
    result = 0
    for coefficient in coefficients:
        result = math.gcd(result, abs(coefficient))
    return result


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation requires a nonzero integer")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def prime_factors(value: int) -> dict[int, int]:
    value = abs(value)
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def extended_gcd(first: int, second: int) -> tuple[int, int, int]:
    if second == 0:
        return first, 1, 0
    gcd_value, old_second, new_second = extended_gcd(
        second, first % second
    )
    return (
        gcd_value,
        new_second,
        old_second - (first // second) * new_second,
    )


def coefficient_lattice_basis(
    integer: int, gap: int, first_modulus: int, second_modulus: int
) -> tuple[list[list[int]], int]:
    delta = math.gcd(first_modulus, second_modulus, gap)
    first_reduced = first_modulus // delta
    gap_reduced = gap // delta
    second_reduced = second_modulus // delta
    common, bezout_first, bezout_gap = extended_gcd(
        first_reduced, gap_reduced
    )
    assert common == math.gcd(first_reduced, gap_reduced)
    assert math.gcd(common, second_reduced) == 1

    parameter_columns = [
        [gap_reduced // common, -first_reduced // common],
        [
            second_reduced * bezout_first,
            second_reduced * bezout_gap,
        ],
    ]
    coefficient_columns: list[list[int]] = []
    for k_value, slope in parameter_columns:
        coefficient_columns.append(
            [first_modulus * k_value - integer * slope, slope]
        )
    determinant = abs(
        coefficient_columns[0][0] * coefficient_columns[1][1]
        - coefficient_columns[0][1] * coefficient_columns[1][0]
    )
    expected = first_modulus * second_modulus // delta
    assert determinant == expected
    return coefficient_columns, expected


def evaluation_index_checks() -> dict[str, object]:
    exact_image_checks = 0
    basis_checks = 0
    determinant_checks = 0
    content_checks = 0
    representatives: list[dict[str, object]] = []
    cases = [
        (0, 1, 5, 7),
        (3, 2, 8, 12),
        (5, 6, 18, 24),
        (7, 4, 25, 14),
        (11, 9, 27, 45),
        (13, 10, 32, 75),
    ]
    for integer, gap, first_modulus, second_modulus in cases:
        other = integer + gap
        period = math.lcm(first_modulus, second_modulus)
        image = {
            (
                (constant + integer * slope) % first_modulus,
                (constant + other * slope) % second_modulus,
            )
            for constant in range(period)
            for slope in range(period)
        }
        delta = math.gcd(first_modulus, second_modulus, gap)
        expected_index = first_modulus * second_modulus // delta
        assert len(image) == expected_index
        exact_image_checks += 1

        columns, determinant = coefficient_lattice_basis(
            integer, gap, first_modulus, second_modulus
        )
        assert determinant == expected_index
        for column in columns:
            assert evaluate(column, integer) % first_modulus == 0
            assert evaluate(column, other) % second_modulus == 0
        basis_checks += 1

        for weights in [
            ((1, 0), (0, 1)),
            ((2, -1), (3, 1)),
            ((-3, 2), (1, 4)),
            ((5, 3), (-2, 1)),
        ]:
            polynomials = [
                [
                    columns[0][row] * pair[0]
                    + columns[1][row] * pair[1]
                    for row in range(2)
                ]
                for pair in weights
            ]
            coefficient_determinant = (
                polynomials[0][0] * polynomials[1][1]
                - polynomials[0][1] * polynomials[1][0]
            )
            weight_determinant = (
                weights[0][0] * weights[1][1]
                - weights[0][1] * weights[1][0]
            )
            assert coefficient_determinant == (
                determinant * weight_determinant
            )
            if coefficient_determinant:
                assert coefficient_determinant % determinant == 0
                assert abs(coefficient_determinant) <= (
                    height_one(polynomials[0])
                    * height_one(polynomials[1])
                )
                determinant_checks += 1

                first_content = content(polynomials[0])
                second_content = content(polynomials[1])
                primitive_first = [
                    value // first_content for value in polynomials[0]
                ]
                primitive_second = [
                    value // second_content for value in polynomials[1]
                ]
                primitive_determinant = (
                    primitive_first[0] * primitive_second[1]
                    - primitive_first[1] * primitive_second[0]
                )
                remaining = determinant // math.gcd(
                    determinant, first_content * second_content
                )
                assert primitive_determinant % remaining == 0
                content_checks += 1

        representatives.append(
            {
                "n": integer,
                "h": gap,
                "P": first_modulus,
                "R": second_modulus,
                "delta": delta,
                "index": expected_index,
                "basis_columns": columns,
            }
        )
    return {
        "exact_finite_image_checks": exact_image_checks,
        "explicit_basis_checks": basis_checks,
        "rank_two_determinant_checks": determinant_checks,
        "primitive_content_checks": content_checks,
        "representatives": representatives,
    }


def single_interpolation_checks() -> dict[str, object]:
    checks = 0
    representatives: list[dict[str, object]] = []
    coprime_pairs = [
        (5, 7),
        (8, 9),
        (11, 25),
        (32, 81),
        (125, 343),
        (1024, 2187),
    ]
    for integer in range(0, 31):
        for first_modulus, second_modulus in coprime_pairs:
            slope = second_modulus - first_modulus
            coefficients = (
                first_modulus - integer * slope,
                slope,
            )
            assert evaluate(coefficients, integer) == first_modulus
            assert evaluate(coefficients, integer + 1) == second_modulus
            assert content(coefficients) == 1
            product = first_modulus * second_modulus
            upper = (
                height_one(coefficients) * (integer + 2)
            ) ** 2
            assert product <= upper
            checks += 1
            if (integer, first_modulus, second_modulus) in [
                (3, 8, 9),
                (17, 125, 343),
                (30, 1024, 2187),
            ]:
                representatives.append(
                    {
                        "n": integer,
                        "P": first_modulus,
                        "R": second_modulus,
                        "coefficients": list(coefficients),
                        "H1": height_one(coefficients),
                    }
                )
    return {
        "primitive_adjacent_center_interpolation_checks": checks,
        "representatives": representatives,
    }


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


def transfer_coefficients(integer: int, maximum_gap: int) -> tuple[list[int], list[int]]:
    a_values = [1, 0]
    c_values = [0, 1]
    for gap_index in range(maximum_gap - 1):
        coefficient = 4 * integer + 4 * gap_index + 6
        a_values.append(
            coefficient * a_values[gap_index + 1] + a_values[gap_index]
        )
        c_values.append(
            coefficient * c_values[gap_index + 1] + c_values[gap_index]
        )
    return a_values, c_values


def recurrence_cross_determinant_checks() -> dict[str, object]:
    maximum_index = 90
    maximum_gap = 16
    p_values, q_values, s_values = bessel_solutions(maximum_index)
    transfer_checks = 0
    determinant_checks = 0
    gcd_checks = 0
    valuation_checks = 0
    height_checks = 0
    representatives: list[dict[str, object]] = []

    for integer in range(0, maximum_index - maximum_gap + 1):
        a_values, c_values = transfer_coefficients(
            integer, maximum_gap
        )
        for gap in range(1, maximum_gap + 1):
            other = integer + gap
            for values in [p_values, q_values, s_values]:
                assert values[other] == (
                    a_values[gap] * values[integer]
                    + c_values[gap] * values[integer + 1]
                )
                transfer_checks += 1

            primitive_determinant = (
                q_values[integer] * s_values[other]
                - s_values[integer] * q_values[other]
            )
            assert primitive_determinant == (
                (-1) ** integer * c_values[gap]
            )
            pade_determinant = (
                p_values[other] * q_values[integer]
                - p_values[integer] * q_values[other]
            )
            assert pade_determinant == 2 * primitive_determinant
            determinant_checks += 1

            denominator_gcd = math.gcd(
                q_values[integer], q_values[other]
            )
            assert denominator_gcd == math.gcd(
                q_values[integer], c_values[gap]
            )
            gcd_checks += 1

            assert 1 <= c_values[gap] <= (
                4 * (integer + gap)
            ) ** (gap - 1)
            height_checks += 1

            for prime in prime_factors(denominator_gcd):
                first_depth = valuation(q_values[integer], prime)
                second_depth = valuation(q_values[other], prime)
                determinant_depth = valuation(c_values[gap], prime)
                assert determinant_depth >= min(
                    first_depth, second_depth
                )
                if first_depth != second_depth:
                    assert determinant_depth == min(
                        first_depth, second_depth
                    )
                assert s_values[integer] % prime
                assert s_values[other] % prime
                valuation_checks += 1

            if (integer, gap) in [(0, 1), (3, 4), (12, 7), (40, 16)]:
                representatives.append(
                    {
                        "n": integer,
                        "h": gap,
                        "C_h_n": c_values[gap],
                        "q_n": q_values[integer],
                        "q_n_plus_h": q_values[other],
                        "gcd": denominator_gcd,
                        "primitive_cross_determinant": primitive_determinant,
                    }
                )

    return {
        "three_solution_transfer_checks": transfer_checks,
        "primitive_and_Pade_cross_determinant_checks": determinant_checks,
        "denominator_gcd_identity_checks": gcd_checks,
        "common_prime_valuation_checks": valuation_checks,
        "transfer_height_checks": height_checks,
        "representatives": representatives,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for two-center evaluation lattices "
            "and the primitive Bessel cross-determinant"
        ),
        "two_center_lattice": evaluation_index_checks(),
        "single_vector_interpolation": single_interpolation_checks(),
        "Bessel_cross_determinant": recurrence_cross_determinant_checks(),
        "status": (
            "finite diagnostic; the all-parameter two-center index, "
            "rank-two determinant divisibility, transfer determinant and "
            "gcd law are proved symbolically in the companion source; no "
            "individual digit-depth bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_two_center_evaluation_lattice_certificate.json"
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
