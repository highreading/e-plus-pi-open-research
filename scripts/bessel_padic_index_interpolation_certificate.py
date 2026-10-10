#!/usr/bin/env python3
"""Exact diagnostics for the canonical p-adic Bessel-index interpolation."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def valuation_nonzero(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("this helper is only for nonzero integers")
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def factorial_valuation(index: int, prime: int) -> int:
    answer = 0
    while index:
        index //= prime
        answer += index
    return answer


def floor_log(index: int, prime: int) -> int:
    answer = 0
    while index >= prime:
        index //= prime
        answer += 1
    return answer


def q_values(limit: int, modulus: int | None = None) -> list[int]:
    if limit == 0:
        return [1]
    values = [1, 1]
    for index in range(2, limit + 1):
        value = (4 * index - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    if modulus is not None:
        values[0] %= modulus
        values[1] %= modulus
    return values


def q_at_indices(indices: list[int], modulus: int) -> dict[int, int]:
    wanted = set(indices)
    if not wanted:
        return {}
    answer: dict[int, int] = {}
    if 0 in wanted:
        answer[0] = 1 % modulus
    if 1 in wanted:
        answer[1] = 1 % modulus
    previous, current = 1 % modulus, 1 % modulus
    for index in range(2, max(wanted) + 1):
        previous, current = (
            current,
            ((4 * index - 2) * current + previous) % modulus,
        )
        if index in wanted:
            answer[index] = current
    assert set(answer) == wanted
    return answer


def mahler_coefficients(limit: int) -> list[int]:
    coefficients = [1, -2]
    for index in range(limit - 1):
        previous = coefficients[index - 1] if index else 0
        coefficients.append(
            -4 * (index + 2) * coefficients[index + 1]
            - (8 * index + 6) * coefficients[index]
            - 4 * index * previous
        )
    return coefficients[: limit + 1]


def closed_mahler(index: int, factorials: list[int]) -> int:
    total = 0
    for half_index in range(index // 2 + 1):
        total += (
            (-1) ** half_index
            * (factorials[index] // factorials[half_index])
            * math.comb(2 * index - 2 * half_index, index)
        )
    return (-1) ** index * total


def coefficient_checks(limit: int = 220) -> tuple[list[int], dict[str, object]]:
    factorials = [math.factorial(index) for index in range(limit + 1)]
    coefficients = mahler_coefficients(limit)
    q_exact = q_values(40)
    for index in range(41):
        direct = sum(
            (-1) ** (index - value_index)
            * math.comb(index, value_index)
            * ((-1) ** value_index)
            * q_exact[value_index]
            for value_index in range(index + 1)
        )
        assert direct == coefficients[index]
    for index, coefficient in enumerate(coefficients):
        assert coefficient == closed_mahler(index, factorials)
        divisor = factorials[index] // factorials[index // 2]
        assert coefficient % divisor == 0
        if index:
            assert (-1 if coefficient < 0 else 1) == (-1) ** index
    return coefficients, {
        "checked_through": limit,
        "first_coefficients": coefficients[:16],
        "finite_difference_checks_through": 40,
        "closed_formula_checks": limit + 1,
        "factorial_divisibility_checks": limit + 1,
    }


def lipschitz_checks() -> list[dict[str, int]]:
    records = []
    for prime in [2, 3, 5, 7, 11, 13]:
        for exponent in range(1, 5):
            modulus = prime**exponent
            n_limit = 180
            values = q_values(n_limit + modulus, modulus)
            for index in range(n_limit + 1):
                left = (-1) ** (index + modulus) * values[index + modulus]
                right = (-1) ** index * values[index]
                assert (left - right) % modulus == 0
            records.append(
                {
                    "prime": prime,
                    "exponent": exponent,
                    "modulus": modulus,
                    "checked_n_through": n_limit,
                }
            )
    return records


def analytic_checks(coefficients: list[int]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    limit = len(coefficients) - 1
    for prime in [2, 3, 5, 7, 11, 13, 17, 19]:
        analytic_order = 2 if prime == 2 else 1
        previous_order = analytic_order - 1
        gaps = []
        for index in range(1, limit + 1):
            value = valuation_nonzero(coefficients[index], prime)
            assert value >= floor_log(index, prime)
            divisor_value = (
                factorial_valuation(index, prime)
                - factorial_valuation(index // 2, prime)
            )
            assert value >= divisor_value
            gaps.append(
                value
                - factorial_valuation(index // prime**analytic_order, prime)
            )
        sharp_records = []
        power = 1
        while 2 * prime**power <= limit:
            half_index = prime**power
            index = 2 * half_index
            divisor = math.factorial(index) // math.factorial(half_index)
            normalized = coefficients[index] // divisor
            assert normalized % prime == (-1) ** half_index % prime
            previous_gap = valuation_nonzero(coefficients[index], prime) - (
                factorial_valuation(index // prime**previous_order, prime)
                if previous_order
                else factorial_valuation(index, prime)
            )
            sharp_records.append(
                {
                    "index": index,
                    "normalized_mod_p": normalized % prime,
                    "v_A_over_index": str(
                        Fraction(
                            valuation_nonzero(coefficients[index], prime),
                            index,
                        )
                    ),
                    "previous_order_gap": previous_gap,
                }
            )
            power += 1
        records.append(
            {
                "prime": prime,
                "minimal_analytic_order": analytic_order,
                "checked_coefficients_through": limit,
                "minimum_gap_last_40": min(gaps[-40:]),
                "sharp_subsequence": sharp_records,
                "theoretical_liminf": str(Fraction(1, 2 * (prime - 1))),
            }
        )
    return records


def lift_branch(prime: int, base_root: int, max_exponent: int) -> dict[str, object]:
    assert q_at_indices([base_root], prime)[base_root] % prime == 0
    representatives = [base_root]
    digits = []
    root = base_root
    for exponent in range(1, max_exponent):
        base_modulus = prime**exponent
        next_modulus = prime ** (exponent + 1)
        candidates = [root + digit * base_modulus for digit in range(prime)]
        values = q_at_indices(candidates, next_modulus)
        surviving = [
            digit
            for digit, candidate in enumerate(candidates)
            if values[candidate] % next_modulus == 0
        ]
        assert len(surviving) == 1
        digit = surviving[0]
        digits.append(digit)
        root += digit * base_modulus
        representatives.append(root)

    final_modulus = prime**max_exponent
    test_indices = [
        index
        for index in range(base_root, 5001, prime)
    ]
    values = q_at_indices(test_indices, final_modulus)
    distance_checks = 0
    for index in test_indices:
        distance = (index - root) % final_modulus
        distance_value = (
            max_exponent
            if distance == 0
            else valuation_nonzero(distance, prime)
        )
        q_residue = values[index]
        q_value = (
            max_exponent
            if q_residue == 0
            else valuation_nonzero(q_residue, prime)
        )
        assert distance_value == q_value
        distance_checks += 1

    derivative_residues = []
    for exponent in range(1, min(max_exponent, 5) + 1):
        shift = prime**exponent
        modulus = prime ** (exponent + 1)
        values = q_at_indices([base_root, base_root + shift], modulus)
        numerator = (-values[base_root + shift] - values[base_root]) % modulus
        assert numerator % shift == 0
        delta = numerator // shift
        derivative_residues.append(((-1) ** base_root * delta) % prime)
    assert len(set(derivative_residues)) == 1
    assert derivative_residues[0] != 0

    return {
        "prime": prime,
        "base_root": base_root,
        "max_exponent": max_exponent,
        "representatives": representatives,
        "new_digits": digits,
        "derivative_difference_quotients_mod_p": derivative_residues,
        "truncated_distance_identity_checks": distance_checks,
    }


def branch_checks() -> list[dict[str, object]]:
    return [
        lift_branch(7, 4, 7),
        lift_branch(11, 6, 6),
        lift_branch(13, 8, 5),
        lift_branch(41, 25, 4),
    ]


def build_payload() -> dict[str, object]:
    coefficients, coefficient_record = coefficient_checks()
    return {
        "description": (
            "Exact finite diagnostics for the canonical 1-Lipschitz "
            "p-adic interpolation of (-1)^n q_n"
        ),
        "coefficient_checks": coefficient_record,
        "lipschitz_checks": lipschitz_checks(),
        "analytic_checks": analytic_checks(coefficients),
        "ordinary_branch_checks": branch_checks(),
        "status": (
            "finite diagnostic; the all-index interpolation and analytic-order "
            "proofs are in the companion source; no digit-depth bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_padic_index_interpolation_certificate.json"
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
