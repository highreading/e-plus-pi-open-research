#!/usr/bin/env python3
"""Exact checks for simultaneous CRT and recurrence-sublattice barriers."""

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


def poly_sub(first: Polynomial, second: Polynomial) -> Polynomial:
    return poly_add(first, poly_scale(-1, second))


def poly_mul(first: Polynomial, second: Polynomial) -> Polynomial:
    result = [0] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            result[first_index + second_index] += first_value * second_value
    return normalize(result)


def evaluate(polynomial: Polynomial | list[int], integer: int) -> int:
    result = 0
    for coefficient in reversed(polynomial):
        result = result * integer + coefficient
    return result


def height_one(polynomial: Polynomial | list[int]) -> int:
    return sum(abs(coefficient) for coefficient in polynomial)


def content(polynomial: Polynomial | list[int]) -> int:
    result = 0
    for coefficient in polynomial:
        result = math.gcd(result, abs(coefficient))
    return result


def weighted_height(polynomial: Polynomial | list[int], integer: int) -> int:
    return sum(
        abs(coefficient) * (integer + 1) ** index
        for index, coefficient in enumerate(polynomial)
    )


def prime_factors(value: int) -> dict[int, int]:
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


def simultaneous_crt_checks() -> dict[str, object]:
    prime_sets = [
        ((2, 3), (3, 2)),
        ((2, 5), (5, 3), (7, 2)),
        ((3, 4), (11, 2), (13, 1)),
        ((5, 6), (7, 4), (17, 2), (19, 1)),
    ]
    checks = 0
    dual_checks = 0
    representatives: list[dict[str, object]] = []
    for prime_data in prime_sets:
        modulus = math.prod(prime**exponent for prime, exponent in prime_data)
        assert prime_factors(modulus) == dict(prime_data)
        for integer in range(0, 21):
            for degree_bound in range(0, 8):
                columns: list[list[int]] = []
                first = [0] * (degree_bound + 1)
                first[0] = modulus
                columns.append(first)
                for index in range(1, degree_bound + 1):
                    column = [0] * (degree_bound + 1)
                    column[index - 1] = -integer
                    column[index] = 1
                    columns.append(column)
                determinant = math.prod(
                    columns[index][index]
                    for index in range(degree_bound + 1)
                )
                assert determinant == modulus
                for column_index, column in enumerate(columns):
                    value = evaluate(column, integer)
                    assert value == (modulus if column_index == 0 else 0)
                    for prime, exponent in prime_data:
                        assert value % (prime**exponent) == 0
                    assert value % modulus == 0
                    dual_checks += 1

                linear = (modulus - integer, 1)
                assert evaluate(linear, integer) == modulus
                assert content(linear) == 1
                assert weighted_height(linear, integer) >= modulus
                if modulus >= integer:
                    assert weighted_height(linear, integer) == modulus + 1
                checks += 1

                if (
                    prime_data,
                    integer,
                    degree_bound,
                ) in [
                    (prime_sets[0], 7, 3),
                    (prime_sets[2], 13, 5),
                    (prime_sets[3], 20, 7),
                ]:
                    representatives.append(
                        {
                            "prime_powers": [
                                {"p": prime, "a": exponent}
                                for prime, exponent in prime_data
                            ],
                            "Q": modulus,
                            "n": integer,
                            "d": degree_bound,
                            "determinant": determinant,
                            "linear_near_attainer": list(linear),
                            "weighted_height": weighted_height(
                                linear, integer
                            ),
                        }
                    )
    return {
        "simultaneous_lattice_and_near_attainer_checks": checks,
        "dual_pairing_checks": dual_checks,
        "representatives": representatives,
    }


def subgroup_accounting_checks() -> dict[str, object]:
    checks = 0
    residue_image_checks = 0
    representatives: list[dict[str, int]] = []
    for modulus in range(2, 121):
        for evaluation_gcd in range(1, 81):
            expected_index = modulus // math.gcd(modulus, evaluation_gcd)
            expected_value_step = math.lcm(modulus, evaluation_gcd)
            residues = {
                (multiplier * evaluation_gcd) % modulus
                for multiplier in range(modulus)
            }
            assert len(residues) == expected_index
            common_values = [
                multiple * evaluation_gcd
                for multiple in range(1, modulus + 1)
                if (multiple * evaluation_gcd) % modulus == 0
            ]
            assert min(common_values) == expected_value_step
            local_product = math.prod(
                prime ** max(0, exponent - prime_factors(evaluation_gcd).get(prime, 0))
                for prime, exponent in prime_factors(modulus).items()
            )
            assert local_product == expected_index
            assert (
                expected_index * evaluation_gcd
                >= modulus
            )
            checks += 1
            residue_image_checks += len(residues)
            if (modulus, evaluation_gcd) in [
                (72, 12),
                (100, 75),
                (120, 49),
            ]:
                representatives.append(
                    {
                        "Q": modulus,
                        "g": evaluation_gcd,
                        "index": expected_index,
                        "evaluation_step": expected_value_step,
                        "gcd": math.gcd(modulus, evaluation_gcd),
                    }
                )
    return {
        "subgroup_index_and_evaluation_ideal_checks": checks,
        "residue_image_elements_counted": residue_image_checks,
        "representatives": representatives,
    }


def shift_polynomials(maximum_shift: int) -> tuple[list[Polynomial], list[Polynomial]]:
    u_values: list[Polynomial] = [(1,), (0,)]
    v_values: list[Polynomial] = [(0,), (1,)]
    for shift in range(maximum_shift - 1):
        affine = (4 * shift + 6, 4)
        u_values.append(
            poly_sub(u_values[shift], poly_mul(affine, u_values[shift + 1]))
        )
        v_values.append(
            poly_sub(v_values[shift], poly_mul(affine, v_values[shift + 1]))
        )
    return u_values, v_values


def recurrence_shift_checks() -> dict[str, object]:
    maximum_shift = 45
    u_values, v_values = shift_polynomials(maximum_shift)
    bezout_checks = 0
    recurrence_value_checks = 0
    restricted_checks = 0
    representatives: list[dict[str, object]] = []

    for shift in range(maximum_shift):
        determinant = poly_sub(
            poly_mul(u_values[shift], v_values[shift + 1]),
            poly_mul(u_values[shift + 1], v_values[shift]),
        )
        assert determinant == (((-1) ** shift),)
        target = (3, -2, 5, 1)
        first_multiplier = poly_scale(
            (-1) ** (shift + 1),
            poly_mul(target, u_values[shift + 1]),
        )
        second_multiplier = poly_scale(
            (-1) ** shift,
            poly_mul(target, u_values[shift]),
        )
        recovered = poly_add(
            poly_mul(first_multiplier, v_values[shift]),
            poly_mul(second_multiplier, v_values[shift + 1]),
        )
        assert recovered == target
        bezout_checks += 1

        for integer in [0, 1, 3, 9, 27]:
            f_values = [1, -1]
            for index in range(maximum_shift - 1):
                f_values.append(
                    f_values[index]
                    - (4 * integer + 4 * index + 6) * f_values[index + 1]
                )
            assert f_values[shift] == (
                evaluate(u_values[shift], integer) * f_values[0]
                + evaluate(v_values[shift], integer) * f_values[1]
            )
            recurrence_value_checks += 1

            v_at_n = evaluate(v_values[shift], integer)
            if shift >= 1:
                assert ((-1) ** (shift - 1)) * v_at_n > 0
            if v_at_n:
                for multiplier_value in [-3, -1, 1, 4]:
                    residual_value = multiplier_value * v_at_n
                    assert abs(residual_value) >= abs(v_at_n)
                    restricted_checks += 1

        if shift in [1, 2, 5, 12, 30, 44]:
            representatives.append(
                {
                    "j": shift,
                    "U_j": list(u_values[shift]),
                    "V_j": list(v_values[shift]),
                    "bezout_determinant": (-1) ** shift,
                }
            )

    return {
        "adjacent_bezout_checks": bezout_checks,
        "recurrence_value_checks": recurrence_value_checks,
        "single_shift_evaluation_factor_checks": restricted_checks,
        "representatives": representatives,
    }


def composite_content_checks() -> dict[str, object]:
    checks = 0
    representatives: list[dict[str, object]] = []
    moduli = [
        2**5 * 3**3,
        3**4 * 5**2 * 7,
        2**7 * 11**3,
        5**3 * 7**2 * 13,
    ]
    for modulus in moduli:
        for integer in range(0, 22):
            for multiplier in range(1, 90):
                common = math.gcd(modulus, multiplier)
                remaining = modulus // common
                primitive = (remaining - integer, 1)
                original = poly_scale(multiplier, primitive)
                assert content(primitive) == 1
                assert evaluate(original, integer) % modulus == 0
                assert evaluate(primitive, integer) == remaining
                assert (
                    height_one(primitive) * (integer + 1)
                    >= remaining
                )
                assert (
                    height_one(original) * (integer + 1)
                    >= modulus
                )
                checks += 1
                if (modulus, integer, multiplier) in [
                    (moduli[0], 7, 12),
                    (moduli[1], 13, 35),
                    (moduli[3], 21, 70),
                ]:
                    representatives.append(
                        {
                            "Q": modulus,
                            "n": integer,
                            "content": multiplier,
                            "gcd_Q_content": common,
                            "remaining_modulus": remaining,
                            "primitive_coefficients": list(primitive),
                        }
                    )
    return {
        "composite_content_cancellation_checks": checks,
        "representatives": representatives,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for simultaneous ordinary-root CRT "
            "lattices and recurrence-special evaluation ideals"
        ),
        "simultaneous_CRT": simultaneous_crt_checks(),
        "general_sublattice": subgroup_accounting_checks(),
        "Bessel_shift_module": recurrence_shift_checks(),
        "primitive_composite_content": composite_content_checks(),
        "status": (
            "finite diagnostic; the all-parameter CRT collapse, subgroup "
            "index/evaluation-ideal theorem, adjacent-shift surjectivity, "
            "and primitive content accounting are proved symbolically in "
            "the companion source; no denominator-height bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_simultaneous_crt_recurrence_sublattice_certificate.json"
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
