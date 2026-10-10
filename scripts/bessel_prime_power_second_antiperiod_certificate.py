#!/usr/bin/env python3
"""Exact diagnostics for the prime-power second anti-period theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation(0) is not used in this certificate")
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


def q_values(limit: int, modulus: int | None = None) -> list[int]:
    if limit < 1:
        return [1][: limit + 1]
    values = [1, 1]
    for n_value in range(2, limit + 1):
        value = (4 * n_value - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    if modulus is not None:
        values[0] %= modulus
        values[1] %= modulus
    return values


def primes_up_to(limit: int) -> list[int]:
    answer = []
    for candidate in range(2, limit + 1):
        if all(candidate % divisor for divisor in range(2, int(candidate**0.5) + 1)):
            answer.append(candidate)
    return answer


def theorem_checks() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for prime in [3, 5, 7, 11, 13, 17, 19, 23]:
        for exponent in [1, 2, 3]:
            modulus_root = prime**exponent
            modulus = modulus_root**2
            n_limit = min(3 * modulus_root, 1200)
            values = q_values(n_limit + 2 * modulus_root, modulus)
            target_scalar = 2 * prime ** (2 * exponent - 1)
            for n_value in range(n_limit + 1):
                left = (
                    values[n_value + 2 * modulus_root]
                    + 2 * values[n_value + modulus_root]
                    + values[n_value]
                ) % modulus
                right = target_scalar * values[n_value] % modulus
                assert left == right
            d_zero = (values[2 * modulus_root] + 2 * values[modulus_root] + 1) % modulus
            d_one = (
                values[2 * modulus_root + 1]
                + 2 * values[modulus_root + 1]
                + 1
            ) % modulus
            assert d_zero == target_scalar % modulus
            assert d_one == d_zero
            records.append(
                {
                    "prime": prime,
                    "exponent": exponent,
                    "M": modulus_root,
                    "checked_n_through": n_limit,
                    "D0_mod_M_squared": d_zero,
                    "D1_minus_D0_mod_M_squared": (d_one - d_zero) % modulus,
                }
            )
    return records


def valuation_lemma_checks() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for prime in [3, 5, 7, 11, 13, 17, 19]:
        for exponent in [2, 3, 4]:
            modulus_root = prime**exponent
            exceptional = []
            for index in range(1, modulus_root):
                difference = factorial_valuation(index - 1, prime) - valuation(index, prime)
                if difference < 0:
                    exceptional.append([index, difference])
            assert exceptional == [[prime, -1]]
            tail_bound = factorial_valuation(modulus_root, prime)
            assert tail_bound >= 2 * exponent
            records.append(
                {
                    "prime": prime,
                    "exponent": exponent,
                    "M": modulus_root,
                    "indices_with_v_factorial_below_v_index": exceptional,
                    "v_p_of_M_factorial": tail_bound,
                }
            )
    return records


def slope_compatibility_checks() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for prime in [3, 5, 7, 11, 13, 17, 19, 23, 41, 79]:
        for exponent in [2, 3, 4]:
            modulus_root = prime**exponent
            if modulus_root > 600_000:
                continue
            modulus = prime ** (exponent + 1)
            n_limit = min(4 * prime, 320)
            values = q_values(modulus_root + n_limit + prime, modulus)
            root_indices = []
            for n_value in range(n_limit + 1):
                large_slope = (
                    (-values[n_value + modulus_root] - values[n_value]) % modulus
                ) // modulus_root
                prime_slope = (
                    (-values[n_value + prime] - values[n_value]) % (prime * prime)
                ) // prime
                assert large_slope % prime == (
                    prime_slope - values[n_value]
                ) % prime
                if values[n_value] % prime == 0:
                    assert large_slope % prime == prime_slope % prime
                    root_indices.append(n_value)
            records.append(
                {
                    "prime": prime,
                    "exponent": exponent,
                    "M": modulus_root,
                    "checked_n_through": n_limit,
                    "root_indices_checked": root_indices,
                }
            )
    return records


def child_count_record(prime: int, exponent: int) -> dict[str, object]:
    modulus_root = prime**exponent
    modulus = modulus_root**2
    values = q_values(modulus, modulus)
    base_roots = [index for index in range(modulus_root) if values[index] % modulus_root == 0]
    large_roots = [index for index in range(modulus) if values[index] % modulus == 0]
    one_step_modulus = prime * modulus_root
    one_step_roots = [
        index for index in range(one_step_modulus)
        if values[index] % one_step_modulus == 0
    ]
    predicted: list[int] = []
    predicted_one_step: list[int] = []
    fibers = []
    for root in base_roots:
        numerator = (-values[root + modulus_root] - values[root]) % modulus
        assert numerator % modulus_root == 0
        slope = numerator // modulus_root
        quotient = values[root] // modulus_root
        # values[root] is a canonical residue modulo M^2.  Its quotient modulo
        # M is exactly the quotient occurring in the lift congruence.
        divisor = math.gcd(slope, modulus_root)
        children = []
        for digit in range(modulus_root):
            if (quotient + digit * slope) % modulus_root == 0:
                children.append(root + digit * modulus_root)
        expected_count = divisor if quotient % divisor == 0 else 0
        assert len(children) == expected_count
        predicted.extend(children)
        prime_slope = (
            (-values[root + prime] - values[root]) % (prime * prime)
        ) // prime
        assert slope % prime == prime_slope % prime
        one_step_children = [
            root + digit * modulus_root
            for digit in range(prime)
            if (quotient + digit * slope) % prime == 0
        ]
        expected_one_step_count = (
            1
            if slope % prime
            else (prime if quotient % prime == 0 else 0)
        )
        assert len(one_step_children) == expected_one_step_count
        predicted_one_step.extend(one_step_children)
        fibers.append(
            {
                "root": root,
                "slope_mod_M": slope,
                "slope_mod_p": slope % prime,
                "first_level_slope_at_same_index_mod_p": prime_slope,
                "gcd_slope_M": divisor,
                "child_count": len(children),
                "one_exponent_child_count": len(one_step_children),
            }
        )
    assert sorted(predicted) == large_roots
    assert sorted(predicted_one_step) == one_step_roots
    return {
        "prime": prime,
        "exponent": exponent,
        "M": modulus_root,
        "R_M": len(base_roots),
        "R_pM": len(one_step_roots),
        "R_M_squared": len(large_roots),
        "fibers": fibers,
    }


def ordinary_eleven_branch() -> dict[str, object]:
    prime = 11
    index = 1359
    exact_values = q_values(index)
    exact_value = exact_values[index]
    exact_valuation = valuation(exact_value, prime)
    assert exact_valuation == 5
    stages = []
    for exponent, root, child in [(1, 6, 28), (2, 28, 1359)]:
        modulus_root = prime**exponent
        modulus = modulus_root**2
        values = q_values(root + modulus_root, modulus)
        numerator = (-values[root + modulus_root] - values[root]) % modulus
        slope = numerator // modulus_root
        assert math.gcd(slope, modulus_root) == 1
        digit = (child - root) // modulus_root
        assert 0 <= digit < modulus_root
        assert (values[root] // modulus_root + digit * slope) % modulus_root == 0
        stages.append(
            {
                "from_modulus": modulus_root,
                "root": root,
                "unit_slope_mod_M": slope,
                "unique_digit": digit,
                "child_mod_M_squared": child,
            }
        )
    return {
        "index": index,
        "v_11_q_index": exact_valuation,
        "stages": stages,
    }


def build_payload() -> dict[str, object]:
    return {
        "claim": (
            "q[n+2*p^a]+2*q[n+p^a]+q[n] is congruent to "
            "2*p^(2a-1)*q[n] modulo p^(2a)"
        ),
        "slope_claim": (
            "delta_(p^a)(n) is congruent to delta_p(n)-q[n] modulo p "
            "for every a>=2"
        ),
        "theorem_checks": theorem_checks(),
        "valuation_lemma_checks": valuation_lemma_checks(),
        "slope_compatibility_checks": slope_compatibility_checks(),
        "child_count_checks": [
            child_count_record(prime, exponent)
            for prime, exponent in [(3, 1), (3, 2), (5, 1), (5, 2), (7, 1), (7, 2), (11, 1), (11, 2)]
        ],
        "ordinary_eleven_branch": ordinary_eleven_branch(),
        "status": (
            "finite exact diagnostic; the uniform proof is in the companion source note; "
            "no prime-power-height bound is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_prime_power_second_antiperiod_certificate.json"
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
