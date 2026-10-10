#!/usr/bin/env python3
"""Deterministic certificate for Item 285.

All checks use exact integer arithmetic.  The bounded rows replay algebraic
identities only; they are not a prime census or asymptotic experiment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def continuant(n: int, h: int) -> int:
    if h == 0:
        return 0
    previous, current = 0, 1
    for d in range(h - 1):
        previous, current = current, (4 * n + 4 * d + 6) * current + previous
    return current


def casoratian(q: list[int], n: int, h: int) -> int:
    return q[n] * q[n + h + 1] - q[n + 1] * q[n + h]


def product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def gcd_all(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return result


def symmetric_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def trim(coefficients: list[int]) -> list[int]:
    result = coefficients[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_eval(coefficients: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def bareiss_determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    denominator = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column] != 0),
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
                assert numerator % denominator == 0
                work[row][col] = numerator // denominator
            work[row][column] = 0
        denominator = pivot
    return sign * work[-1][-1]


def resultant(first: list[int], second: list[int]) -> int:
    """Sylvester determinant; coefficients are in increasing degree order."""
    first = trim(first)
    second = trim(second)
    degree_first = len(first) - 1
    degree_second = len(second) - 1
    assert degree_first >= 1 and degree_second >= 0
    if degree_second == 0:
        return second[0] ** degree_first
    first_descending = list(reversed(first))
    second_descending = list(reversed(second))
    size = degree_first + degree_second
    matrix: list[list[int]] = []
    for shift in range(degree_second):
        matrix.append(
            [0] * shift
            + first_descending
            + [0] * (size - shift - len(first_descending))
        )
    for shift in range(degree_first):
        matrix.append(
            [0] * shift
            + second_descending
            + [0] * (size - shift - len(second_descending))
        )
    return bareiss_determinant(matrix)


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def arbitrary_terms(n: int) -> list[int]:
    """A varying-size family; no fixed sparsity or degree is used by the lemma."""
    count = n + 3
    common = 2 * (n + 1)
    return [
        common * ((-1) ** index) * (index + 1) * (n + index + 2) ** (index % 5)
        for index in range(count)
    ]


def monomial_specs(n: int) -> tuple[tuple[int, ...], ...]:
    """Actual continuant/Casoratian monomials of unequal total degrees."""
    return (
        (2 + n % 2,),
        (2, 3 + n % 3),
        (2 + n % 3, 3, 4 + n % 2),
        (2, 3 + n % 2, 4, 5 + n % 3),
    )


def coefficient_sets(n: int) -> tuple[tuple[int, ...], ...]:
    return (
        (1, -1, 2, -3),
        (n + 1, -2, 1, 1),
        (2 * n + 3, n - 1, -3, 2),
        (n * n + 1, -(n + 2), 2, -1),
    )


def grouped_polynomial(terms: list[int], exponents: list[int]) -> list[int]:
    coefficients = [0] * (max(exponents) + 1)
    for term, exponent in zip(terms, exponents):
        coefficients[exponent] += term
    return trim(coefficients)


def build_result() -> dict[str, Any]:
    q = q_values(90)
    clearing_samples = (1, 3, 5, 7, 9, 11, 25, 49, 77, 121)

    arbitrary_rows: list[dict[str, Any]] = []
    for n in range(2, 31):
        terms = arbitrary_terms(n)
        residual = sum(terms)
        assert residual != 0
        baseline_integer = gcd_all(terms)
        assert baseline_integer > 0
        assert residual % baseline_integer == 0
        normalized_residual = residual // baseline_integer
        normalized_l1 = sum(abs(term) for term in terms) // baseline_integer
        assert abs(normalized_residual) <= normalized_l1
        for clearing in clearing_samples:
            target = q[n] // math.gcd(q[n], clearing)
            captured = math.gcd(target, abs(residual))
            baseline = math.gcd(target, baseline_integer)
            assert captured % baseline == 0
            quotient = captured // baseline
            assert normalized_residual % quotient == 0
            if residual % target == 0:
                assert normalized_residual % (target // baseline) == 0
            arbitrary_rows.append(
                {
                    "n": n,
                    "term_count": len(terms),
                    "D": clearing,
                    "target": target,
                    "baseline_integer": baseline_integer,
                    "captured": captured,
                    "cancellation_quotient": quotient,
                    "normalized_residual": normalized_residual,
                    "normalized_l1": normalized_l1,
                }
            )

    unit_rows: list[dict[str, Any]] = []
    homogenization_rows: list[dict[str, Any]] = []
    no_transfer_rows: list[dict[str, Any]] = []
    resultant_rows: list[dict[str, Any]] = []
    for n in range(2, 24):
        specs = monomial_specs(n)
        degrees = [len(gaps) for gaps in specs]
        minimum_degree = min(degrees)
        maximum_degree = max(degrees)
        exponents = [degree - minimum_degree for degree in degrees]
        residual_monomials = [
            product(continuant(n, gap) for gap in gaps) for gaps in specs
        ]
        scalar_monomials = [
            product(casoratian(q, n, gap) for gap in gaps) for gaps in specs
        ]
        boundary_integer = -(q[n + 1] ** 2)
        c_one = casoratian(q, n, 1)
        assert continuant(n, 1) == 1
        assert (c_one - boundary_integer) % q[n] == 0

        for coefficients in coefficient_sets(n):
            residual_terms = [
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, residual_monomials)
            ]
            scalar_terms = [
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, scalar_monomials)
            ]
            scalar_sum = sum(scalar_terms)
            baseline_integer = gcd_all(residual_terms)
            assert baseline_integer > 0
            polynomial = grouped_polynomial(residual_terms, exponents)
            assert all(coefficient % baseline_integer == 0 for coefficient in polynomial)
            normalized_polynomial = [
                coefficient // baseline_integer for coefficient in polynomial
            ]

            homogenized_scalar = sum(
                scalar_term * c_one ** (maximum_degree - degree)
                for scalar_term, degree in zip(scalar_terms, degrees)
            )
            homogenized_residual = sum(residual_terms)

            for clearing in clearing_samples:
                target = q[n] // math.gcd(q[n], clearing)
                if target <= 1:
                    continue
                unit = boundary_integer % target
                assert math.gcd(unit, target) == 1
                lift = symmetric_residue(boundary_integer, target)
                assert (lift - boundary_integer) % target == 0
                assert math.gcd(lift, target) == 1
                evaluated_residual = polynomial_eval(polynomial, lift)
                exact_boundary_residual = polynomial_eval(polynomial, boundary_integer)
                assert (
                    scalar_sum
                    - boundary_integer ** minimum_degree * exact_boundary_residual
                ) % target == 0
                scalar_capture = math.gcd(target, abs(scalar_sum))
                evaluated_capture = math.gcd(target, abs(evaluated_residual))
                assert scalar_capture == evaluated_capture
                baseline = math.gcd(target, baseline_integer)
                assert evaluated_capture % baseline == 0
                cancellation_quotient = evaluated_capture // baseline
                assert evaluated_residual % baseline_integer == 0
                normalized_evaluation = evaluated_residual // baseline_integer
                assert normalized_evaluation % cancellation_quotient == 0
                normalized_l1 = sum(
                    abs(term) * abs(lift) ** exponent
                    for term, exponent in zip(residual_terms, exponents)
                ) // baseline_integer
                assert abs(normalized_evaluation) <= normalized_l1

                assert (
                    homogenized_scalar
                    - boundary_integer ** maximum_degree * homogenized_residual
                ) % target == 0
                homogenized_capture = math.gcd(target, abs(homogenized_scalar))
                residual_capture = math.gcd(target, abs(homogenized_residual))
                assert homogenized_capture == residual_capture
                if homogenized_residual != 0:
                    homogenized_quotient = (
                        homogenized_capture // math.gcd(target, baseline_integer)
                    )
                    assert (
                        homogenized_residual // baseline_integer
                    ) % homogenized_quotient == 0
                if scalar_capture != homogenized_capture:
                    no_transfer_rows.append(
                        {
                            "n": n,
                            "D": clearing,
                            "target": target,
                            "coefficients": coefficients,
                            "gaps": specs,
                            "original_scalar": scalar_sum,
                            "homogenized_scalar": homogenized_scalar,
                            "scalar_capture": scalar_capture,
                            "homogenized_capture": homogenized_capture,
                            "degrees": degrees,
                        }
                    )

                multiplier = 2 + n % 3
                annihilator = [
                    -lift * multiplier,
                    multiplier - lift,
                    1,
                ]
                assert polynomial_eval(annihilator, boundary_integer) % target == 0
                result = resultant(annihilator, normalized_polynomial)
                if result != 0:
                    assert result % cancellation_quotient == 0
                    degree_m = len(trim(annihilator)) - 1
                    degree_f = len(trim(normalized_polynomial)) - 1
                    norm_m_squared = sum(value * value for value in annihilator)
                    norm_f_squared = sum(
                        value * value for value in normalized_polynomial
                    )
                    assert result * result <= (
                        norm_m_squared ** degree_f
                        * norm_f_squared ** degree_m
                    )
                    resultant_rows.append(
                        {
                            "n": n,
                            "D": clearing,
                            "target": target,
                            "degrees": [degree_m, degree_f],
                            "cancellation_quotient": cancellation_quotient,
                            "resultant": result,
                            "annihilator_l1": sum(abs(value) for value in annihilator),
                            "normalized_polynomial_l1": sum(
                                abs(value) for value in normalized_polynomial
                            ),
                        }
                    )

                unit_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "target": target,
                        "degrees": degrees,
                        "exponents": exponents,
                        "lift": lift,
                        "baseline_integer": baseline_integer,
                        "scalar_capture": scalar_capture,
                        "cancellation_quotient": cancellation_quotient,
                        "normalized_evaluation": normalized_evaluation,
                        "normalized_l1": normalized_l1,
                        "canonical_boundary_bits": abs(boundary_integer).bit_length(),
                    }
                )
                homogenization_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "target": target,
                        "original_capture": scalar_capture,
                        "homogenized_capture": homogenized_capture,
                        "homogenized_residual": homogenized_residual,
                    }
                )

    # Exact zero-resultant identity branch.  This is a formal algebraic witness,
    # not an actual-family construction.
    zero_resultant_rows: list[dict[str, Any]] = []
    for value in range(-7, 8):
        annihilator = [-value, 1]
        polynomial = [-3 * value, 3 - value, 1]  # (U-value)(U+3)
        result = resultant(annihilator, polynomial)
        assert result == 0
        zero_resultant_rows.append(
            {"root": value, "annihilator": annihilator, "polynomial": polynomial}
        )

    # Formal low-coefficient-height warning: Euler's theorem can encode an
    # arbitrary target in the exponent.  It is not admitted as an actual beta
    # construction and is recorded only to show why degree must enter height.
    formal_degree_rows: list[dict[str, Any]] = []
    for modulus in (5, 7, 9, 11, 13, 17, 25):
        for unit in range(1, modulus):
            if math.gcd(unit, modulus) != 1:
                continue
            exponent = math.prod(
                [
                    prime ** (power - 1) * (prime - 1)
                    for prime, power in factorization(modulus)
                ]
            )
            assert (pow(unit, exponent, modulus) - 1) % modulus == 0
            formal_degree_rows.append(
                {
                    "modulus": modulus,
                    "unit": unit,
                    "euler_degree": exponent,
                    "coefficient_l1": 2,
                }
            )

    assert no_transfer_rows
    assert resultant_rows

    return {
        "schema": "item285-beta-arbitrary-sum-unit-tracking-certificate-v1",
        "description": (
            "Exact arbitrary-sum cancellation quotient, nonhomogeneous boundary-unit "
            "tracking, designed homogenization, and annihilator-resultant criteria"
        ),
        "theorem": {
            "arbitrary_sum": (
                "for any finite nonzero integer sum R=sum T_j, B=gcd_j|T_j|, "
                "Q any target, and X=gcd(Q,R)/gcd(Q,B), one has X|R/B"
            ),
            "conditional_height": (
                "the explicit assumption log(sum|T_j|/B)=O(n) gives "
                "log X=O(n), with no sparsity or degree restriction"
            ),
            "nonhomogeneous_reduction": (
                "with u=-q_(n+1)^2, k0=min k_j, and "
                "F(U)=sum c_j A_j U^(k_j-k0), gcd(Q,S)=gcd(Q,F(u))"
            ),
            "unit_lift": (
                "if v is an integer unit lift of u mod Q and the normalized "
                "evaluated l1 height is O(n), then the sum-only quotient "
                "divides F(v)/B and has log height O(n)"
            ),
            "designed_homogenization": (
                "multiplication of each degree-k_j scalar term by C_1^(K-k_j) "
                "creates a different homogeneous sum with residual F(1); it does "
                "not transfer divisibility from the original F(u) sum"
            ),
            "resultant": (
                "if a monic integer M satisfies M(u)=0 mod Q, then the "
                "sum-only quotient divides Res(M,F/B); a nonzero O(n)-height "
                "resultant closes that quotient"
            ),
            "deoverlap": "every target may be chosen inside q_n/gcd(q_n,D_m)",
            "capacity": (
                "all closed sum-only branches have O(n)=o(n log n) height; "
                "the Item282 product baseline remains separate"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "arbitrary_rows": len(arbitrary_rows),
            "arbitrary_digest": digest(arbitrary_rows),
            "unit_rows": len(unit_rows),
            "unit_digest": digest(unit_rows),
            "homogenization_rows": len(homogenization_rows),
            "homogenization_digest": digest(homogenization_rows),
            "no_transfer_rows": len(no_transfer_rows),
            "no_transfer_digest": digest(no_transfer_rows),
            "first_no_transfer_row": no_transfer_rows[0],
            "resultant_rows": len(resultant_rows),
            "resultant_digest": digest(resultant_rows),
            "zero_resultant_rows": len(zero_resultant_rows),
            "zero_resultant_digest": digest(zero_resultant_rows),
            "formal_degree_rows": len(formal_degree_rows),
            "formal_degree_digest": digest(formal_degree_rows),
            "exceptional_singleton_search": False,
            "asymptotic_extrapolation": False,
        },
        "admission": {
            "arbitrary_complexity_conditional_sum_ceiling": "PROVED O(n)",
            "actual_low_height_nonhomogeneous_invariant": False,
            "product_baseline_closed": False,
            "actual_positive_linear_route1_mass": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "a prime-independent unit lift with normalized evaluated height O(n)",
            "or a low-height annihilator with nonzero O(n)-height resultant",
            "unrestricted nonhomogeneous sums without either certificate",
            "the Item282 product baseline and weighted-return cover",
            "the uniform beta prime-power-height or little-oh squarefull theorem",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def factorization(value: int) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= value:
        power = 0
        while value % divisor == 0:
            value //= divisor
            power += 1
        if power:
            result.append((divisor, power))
        divisor += 1
    if value > 1:
        result.append((value, 1))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
