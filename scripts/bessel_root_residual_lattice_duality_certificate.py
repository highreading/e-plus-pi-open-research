#!/usr/bin/env python3
"""Exact checks for the Bessel residual lattice and duality barrier."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def evaluate(coefficients: list[int], integer: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * integer + coefficient
    return result


def content(coefficients: list[int]) -> int:
    result = 0
    for coefficient in coefficients:
        result = math.gcd(result, abs(coefficient))
    return result


def height_one(coefficients: list[int]) -> int:
    return sum(abs(coefficient) for coefficient in coefficients)


def degree(coefficients: list[int]) -> int:
    result = len(coefficients) - 1
    while result > 0 and coefficients[result] == 0:
        result -= 1
    return result


def weighted_height(coefficients: list[int], integer: int) -> int:
    return sum(
        abs(coefficient) * (integer + 1) ** index
        for index, coefficient in enumerate(coefficients)
    )


def lattice_basis(integer: int, modulus: int, degree_bound: int) -> list[list[int]]:
    """Return columns P and (x-n)x^(j-1), represented as vectors."""
    columns: list[list[int]] = []
    constant = [0] * (degree_bound + 1)
    constant[0] = modulus
    columns.append(constant)
    for index in range(1, degree_bound + 1):
        column = [0] * (degree_bound + 1)
        column[index - 1] = -integer
        column[index] = 1
        columns.append(column)
    return columns


def linear_combination(columns: list[list[int]], weights: list[int]) -> list[int]:
    return [
        sum(weights[column] * columns[column][row] for column in range(len(columns)))
        for row in range(len(columns))
    ]


def reconstruct_in_basis(
    coefficients: list[int], integer: int, modulus: int
) -> list[int]:
    """Reconstruct a congruence-lattice point in the displayed basis."""
    work = coefficients[:]
    weights = [0] * len(coefficients)
    for index in range(len(coefficients) - 1, 0, -1):
        weight = work[index]
        weights[index] = weight
        work[index] -= weight
        work[index - 1] += integer * weight
    assert work[0] == evaluate(coefficients, integer)
    if work[0] % modulus:
        raise ValueError("coefficient vector is not in the congruence lattice")
    weights[0] = work[0] // modulus
    return weights


def primitive_base_construction(
    integer: int, modulus: int, degree_bound: int
) -> list[int]:
    """The base-n construction, made primitive by adding x-n if needed."""
    if integer < 2 or degree_bound < 1:
        raise ValueError("construction requires n >= 2 and d >= 1")
    quotient = modulus
    coefficients: list[int] = []
    for _ in range(degree_bound):
        quotient, remainder = divmod(quotient, integer)
        coefficients.append(remainder)
    coefficients.append(quotient)
    assert evaluate(coefficients, integer) == modulus
    if content(coefficients) != 1:
        coefficients[0] -= integer
        coefficients[1] += 1
    assert evaluate(coefficients, integer) == modulus
    assert content(coefficients) == 1
    return coefficients


def basis_and_dual_checks() -> dict[str, object]:
    checks = 0
    reconstruction_checks = 0
    dual_checks = 0
    representatives: list[dict[str, object]] = []
    for integer in range(0, 18):
        for prime in [2, 3, 5, 7, 11]:
            for exponent in range(1, 6):
                modulus = prime**exponent
                for degree_bound in range(0, 8):
                    columns = lattice_basis(integer, modulus, degree_bound)
                    # The column matrix is upper bidiagonal with diagonal
                    # (P,1,...,1), hence determinant P.
                    diagonal_product = math.prod(
                        columns[index][index]
                        for index in range(degree_bound + 1)
                    )
                    assert diagonal_product == modulus
                    for index, column in enumerate(columns):
                        value = evaluate(column, integer)
                        assert value == (modulus if index == 0 else 0)
                        # Pairing with (1,n,...,n^d)/P.
                        assert value % modulus == 0
                        dual_checks += 1

                    for seed in range(-2, 3):
                        weights = [
                            (seed + 2 * index) % 7 - 3
                            for index in range(degree_bound + 1)
                        ]
                        coefficients = linear_combination(columns, weights)
                        assert evaluate(coefficients, integer) % modulus == 0
                        recovered = reconstruct_in_basis(
                            coefficients, integer, modulus
                        )
                        assert recovered == weights
                        reconstruction_checks += 1
                    checks += 1

                    if (
                        integer,
                        prime,
                        exponent,
                        degree_bound,
                    ) in [(3, 2, 4, 3), (7, 5, 3, 5), (17, 11, 5, 7)]:
                        representatives.append(
                            {
                                "n": integer,
                                "P": modulus,
                                "d": degree_bound,
                                "basis_columns": columns,
                                "determinant": diagonal_product,
                            }
                        )
    return {
        "basis_determinant_checks": checks,
        "basis_reconstruction_checks": reconstruction_checks,
        "dual_pairing_checks": dual_checks,
        "representatives": representatives,
    }


def primitive_height_checks() -> dict[str, object]:
    construction_checks = 0
    linear_checks = 0
    content_repair_checks = 0
    representatives: list[dict[str, object]] = []
    primes = [value for value in range(2, 30) if is_prime(value)]
    for integer in range(2, 31):
        for prime in primes:
            for exponent in range(1, 9):
                modulus = prime**exponent
                for degree_bound in range(1, 9):
                    coefficients = primitive_base_construction(
                        integer, modulus, degree_bound
                    )
                    assert evaluate(coefficients, integer) == modulus
                    assert content(coefficients) == 1
                    lower = max(1, modulus / integer**degree_bound)
                    assert height_one(coefficients) >= lower
                    upper = (
                        modulus // integer**degree_bound
                        + degree_bound * (integer - 1)
                        + integer
                        + 1
                    )
                    assert height_one(coefficients) <= upper
                    assert (
                        height_one(coefficients)
                        * (integer + 1) ** degree(coefficients)
                        >= modulus
                    )
                    construction_checks += 1

                    # Count cases in which the raw base-n digits had
                    # nontrivial content and x-n was genuinely needed.
                    quotient = modulus
                    raw: list[int] = []
                    for _ in range(degree_bound):
                        quotient, remainder = divmod(quotient, integer)
                        raw.append(remainder)
                    raw.append(quotient)
                    if content(raw) != 1:
                        assert coefficients[0] == raw[0] - integer
                        assert coefficients[1] == raw[1] + 1
                        content_repair_checks += 1

                linear = [modulus - integer, 1]
                assert evaluate(linear, integer) == modulus
                assert content(linear) == 1
                assert (
                    height_one(linear) * (integer + 1) >= modulus
                )
                if modulus >= integer:
                    assert weighted_height(linear, integer) == modulus + 1
                linear_checks += 1

                if (integer, prime, exponent) in [
                    (3, 2, 8),
                    (11, 5, 6),
                    (29, 29, 7),
                ]:
                    example = primitive_base_construction(
                        integer, modulus, 4
                    )
                    representatives.append(
                        {
                            "n": integer,
                            "P": modulus,
                            "d": 4,
                            "coefficients": example,
                            "H1": height_one(example),
                            "weighted_height": weighted_height(
                                example, integer
                            ),
                            "value": evaluate(example, integer),
                        }
                    )
    return {
        "primitive_base_construction_checks": construction_checks,
        "content_repair_cases": content_repair_checks,
        "primitive_linear_near_attainer_checks": linear_checks,
        "representatives": representatives,
    }


def exhaustive_weighted_checks() -> dict[str, object]:
    checks = 0
    feasible_nonzero = 0
    primitive_nonzero = 0
    for integer in range(1, 6):
        for modulus in range(2, 14):
            for degree_bound in range(1, 4):
                for coefficients_tuple in itertools.product(
                    range(-4, 5), repeat=degree_bound + 1
                ):
                    if not any(coefficients_tuple):
                        continue
                    coefficients = list(coefficients_tuple)
                    value = evaluate(coefficients, integer)
                    if value % modulus:
                        continue
                    checks += 1
                    if value:
                        feasible_nonzero += 1
                        assert abs(value) >= modulus
                        assert weighted_height(
                            coefficients, integer
                        ) >= modulus
                        assert (
                            height_one(coefficients)
                            * (integer + 1) ** degree(coefficients)
                            >= modulus
                        )
                        if content(coefficients) == 1:
                            primitive_nonzero += 1
    return {
        "congruence_lattice_points_checked": checks,
        "nonzero_evaluation_points": feasible_nonzero,
        "primitive_nonzero_evaluation_points": primitive_nonzero,
    }


def content_checks() -> dict[str, object]:
    checks = 0
    representatives: list[dict[str, object]] = []
    for prime in [2, 3, 5, 7, 11, 13]:
        for depth in range(1, 10):
            modulus = prime**depth
            for content_depth in range(0, depth + 3):
                residual_depth = max(0, depth - content_depth)
                primitive_value = prime**residual_depth
                # x + (primitive_value-n) is primitive and has that value.
                integer = depth + prime + 2
                primitive = [primitive_value - integer, 1]
                multiplier = prime**content_depth
                original = [multiplier * value for value in primitive]
                assert content(primitive) == 1
                assert evaluate(
                    original, integer
                ) % modulus == 0
                assert evaluate(primitive, integer) == primitive_value
                assert (
                    residual_depth * math.log(prime)
                    <= math.log(height_one(primitive))
                    + degree(primitive) * math.log(integer + 1)
                    + 1e-12
                )
                checks += 1
                if (prime, depth, content_depth) in [
                    (2, 8, 3),
                    (5, 7, 7),
                    (13, 9, 11),
                ]:
                    representatives.append(
                        {
                            "p": prime,
                            "a": depth,
                            "v_p_content": content_depth,
                            "primitive_residual_depth": residual_depth,
                            "primitive_coefficients": primitive,
                        }
                    )
    return {
        "content_normalization_checks": checks,
        "representatives": representatives,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for the residual congruence lattice, "
            "its dual, primitive l1 height, and content normalization"
        ),
        "lattice_and_dual": basis_and_dual_checks(),
        "primitive_height": primitive_height_checks(),
        "exhaustive_small_box": exhaustive_weighted_checks(),
        "content_normalization": content_checks(),
        "status": (
            "finite diagnostic; the all-parameter lattice basis, dual, "
            "primitive height inequalities, and capacity threshold are "
            "proved symbolically in the companion source; no Bessel "
            "digit-depth bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_root_residual_lattice_duality_certificate.json"
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
