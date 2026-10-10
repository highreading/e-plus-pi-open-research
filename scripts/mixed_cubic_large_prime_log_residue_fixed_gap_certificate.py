#!/usr/bin/env python3
"""Exact fixed-gap certificate for the two mixed-cubic log residues.

This is a finite-width theorem, not an all-prime support proof.  It proves
that no prime p with 6m < p < 6m+49 divides both scaled logarithmic
residues.  All symbolic coefficients use fractions; the few resultant
exceptional primes are checked directly in the fixed-gap formulas.  For
manageable indices they are also replayed by an independent linear-time
coefficient recurrence modulo p.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ODD_GAPS = (1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47)
NUMERATOR_FACTORS = {
    1: (2, 3),
    5: (7, 11),
    7: (2, 2, 11, 653),
    11: (2, 7, 13, 13, 19, 659),
    13: (5, 7, 17, 17, 23, 31, 97, 491),
    17: (5, 5, 5, 7, 11, 13, 19, 19, 31, 859667),
    19: (5, 7, 13, 23, 23, 29, 29, 3673, 1669951),
    23: (5, 5, 5, 17, 19, 31, 31, 37, 37, 43, 997, 9086729),
    25: (7, 11, 11, 13, 19, 29, 29, 41, 41, 47, 647, 3817515241),
    29: (
        5, 5, 7, 7, 11, 13, 17, 23, 31, 31, 37, 37, 43, 43, 71,
        1109014802531,
    ),
    31: (5, 7, 11, 19, 19, 41, 41, 47, 47, 53, 53, 59, 1215685868497699),
    35: (
        7, 7, 11, 13, 23, 29, 31, 37, 37, 43, 43, 61, 61, 67,
        139705851698215541,
    ),
    37: (
        5, 13, 13, 17, 19, 31, 41, 41, 47, 47, 53, 53, 59, 59, 71, 101,
        211, 306055151354467,
    ),
    41: (
        7, 7, 7, 11, 19, 23, 29, 37, 43, 43, 43, 61, 61, 67, 67, 73,
        73, 79, 6819625707194544521,
    ),
    43: (
        5, 5, 11, 11, 13, 17, 17, 31, 37, 47, 47, 53, 53, 59, 59, 71,
        71, 83, 7756733, 2006447, 449595109,
    ),
    47: (
        7, 7, 7, 11, 13, 17, 17, 19, 29, 41, 43, 61, 61, 67, 67, 73,
        73, 79, 79, 1772711, 221691347, 5885768887,
    ),
}


def is_prime(integer: int) -> bool:
    """Deterministic Miller--Rabin for integers below 2^64."""
    if integer < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if integer % prime == 0:
            return integer == prime
    assert integer < 2**64
    odd_part = integer - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        power_of_two += 1
    for witness in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if witness % integer == 0:
            continue
        value = pow(witness, odd_part, integer)
        if value in (1, integer - 1):
            continue
        for _ in range(power_of_two - 1):
            value = value * value % integer
            if value == integer - 1:
                break
        else:
            return False
    return True


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def multiply_truncated(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    answer = [Fraction(0)] * (min(degree, len(left) + len(right) - 2) + 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            if first + second <= degree:
                answer[first + second] += left_value * right_value
    return answer


def generalized_power(
    base: list[Fraction], exponent: Fraction, degree: int
) -> list[Fraction]:
    """Truncated base(z)^exponent, assuming base(0)=1."""
    increment = base[:]
    increment[0] -= 1
    answer = [Fraction(0)] * (degree + 1)
    power = [Fraction(1)]
    for index in range(degree + 1):
        multiplier = generalized_binomial(exponent, index)
        for target, value in enumerate(power):
            answer[target] += multiplier * value
        power = multiply_truncated(power, increment, degree)
    return answer


def full_and_tail(q_value: int, shift: int) -> tuple[Fraction, Fraction]:
    """Return C_s(q),T_s(q) in lambda_s = C_s*2^A-T_s (mod p)."""
    degree = q_value - 1
    m_residue = Fraction(-q_value, 6)
    r_value = 4 * m_residue + shift
    if shift == 0:
        exponent = 2 * m_residue + q_value - 1
        translated = generalized_power(
            [Fraction(1), Fraction(1), Fraction(1, 2)], exponent, degree
        )
        translated = multiply_truncated(
            translated, [Fraction(2), Fraction(1)], degree
        )
        power_of_two_adjustment = Fraction(1)

        def low_coefficient(index: int) -> Fraction:
            answer = Fraction(0)
            if index % 2 == 0:
                answer += generalized_binomial(exponent, index // 2)
            if index >= 1 and (index - 1) % 2 == 0:
                answer += generalized_binomial(exponent, (index - 1) // 2)
            return answer

    elif shift == 1:
        exponent = 2 * m_residue + q_value - 2
        translated = generalized_power(
            [Fraction(1), Fraction(1), Fraction(1, 2)], exponent, degree
        )
        translated = multiply_truncated(
            translated,
            [Fraction(math.comb(4, index) * 2 ** (4 - index)) for index in range(5)],
            degree,
        )
        # The common unknown is X=2^(2m+q-1), one power of two above 2^exponent.
        power_of_two_adjustment = Fraction(1, 2)

        def low_coefficient(index: int) -> Fraction:
            return sum(
                Fraction(math.comb(4, first))
                * generalized_binomial(exponent, (index - first) // 2)
                for first in range(5)
                if index >= first and (index - first) % 2 == 0
            )

    else:
        raise ValueError(shift)

    negative_power = generalized_power(
        [Fraction(1), Fraction(1)], -r_value - 1, degree
    )
    full = (
        multiply_truncated(negative_power, translated, degree)[degree]
        * power_of_two_adjustment
    )
    tail = Fraction(0)
    for h_value in range(q_value):
        low_index = q_value - 1 - h_value
        tail += low_coefficient(low_index) * generalized_binomial(
            Fraction(-h_value - 1), degree
        )
    return full, tail


def modular_log_residue(m_value: int, prime: int, shift: int) -> int:
    """Return lambda_0 or lambda_1 modulo prime by an O(m) recurrence."""
    n_value = 6 * m_value
    k_value = 4 * m_value + 1 + shift
    target = 4 * m_value + shift
    # f=A^n/R^k, A=t^2-3t+2, R=t^2-2t+2.  It satisfies
    # (A R) f'=(n A'R-k A R')f.
    p_coefficients = (4, -10, 10, -5, 1)
    n_coefficients = (
        4 * k_value - 6 * n_value,
        10 * (n_value - k_value),
        8 * k_value - 7 * n_value,
        2 * (n_value - k_value),
    )
    factorial_scaled = [pow(2, n_value - k_value, prime)]
    inverse_four = pow(4, -1, prime)
    factorial = 1
    for index in range(target):
        value = n_coefficients[0] * factorial_scaled[index]
        falling = 1
        for lag in range(1, 5):
            falling = falling * (index - lag + 1) % prime
            if lag < 4 and index - lag >= 0:
                value += (
                    n_coefficients[lag]
                    * falling
                    * factorial_scaled[index - lag]
                )
            if index - lag + 1 >= 0:
                value -= (
                    p_coefficients[lag]
                    * falling
                    * factorial_scaled[index - lag + 1]
                )
        factorial_scaled.append(value * inverse_four % prime)
        factorial = factorial * (index + 1) % prime
    coefficient = factorial_scaled[target] * pow(factorial, -1, prime) % prime
    clearing_power = 2 * m_value + (1 if shift == 0 else 3)
    return coefficient * pow(2, clearing_power, prime) % prime


def fraction_record(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_suffix(".json"),
    )
    args = parser.parse_args()
    rows = []
    fixed_data: dict[int, tuple[Fraction, Fraction, Fraction, Fraction]] = {}
    for q_value in ODD_GAPS:
        c0, t0 = full_and_tail(q_value, 0)
        c1, t1 = full_and_tail(q_value, 1)
        fixed_data[q_value] = (c0, t0, c1, t1)
        resultant = c0 * t1 - c1 * t0
        factors = NUMERATOR_FACTORS[q_value]
        assert math.prod(factors) == abs(resultant.numerator)
        assert all(is_prime(prime) for prime in factors)
        candidates = sorted(
            {
                prime
                for prime in factors
                if prime > q_value and (prime - q_value) % 6 == 0
            }
        )
        exceptional_checks = []
        for prime in candidates:
            m_value = (prime - q_value) // 6
            exponent = 2 * m_value + q_value - 1
            common_power = pow(2, exponent, prime)
            lambda0 = (
                fraction_mod(c0, prime) * common_power - fraction_mod(t0, prime)
            ) % prime
            lambda1 = (
                fraction_mod(c1, prime) * common_power - fraction_mod(t1, prime)
            ) % prime
            assert lambda0 or lambda1
            recurrence_replay = None
            if m_value <= 300000:
                replay0 = modular_log_residue(m_value, prime, 0)
                replay1 = modular_log_residue(m_value, prime, 1)
                assert (replay0, replay1) == (lambda0, lambda1)
                recurrence_replay = True
            exceptional_checks.append(
                {
                    "p": prime,
                    "m": m_value,
                    "lambda0_mod_p": lambda0,
                    "lambda1_mod_p": lambda1,
                    "independent_linear_recurrence_replay": recurrence_replay,
                }
            )
        rows.append(
            {
                "q": q_value,
                "C0": fraction_record(c0),
                "T0": fraction_record(t0),
                "C1": fraction_record(c1),
                "T1": fraction_record(t1),
                "resultant": fraction_record(resultant),
                "absolute_numerator_prime_factors_with_multiplicity": list(factors),
                "candidate_primes_compatible_with_p=6m+q": candidates,
                "exceptional_checks": exceptional_checks,
            }
        )

    small_formula_replays = 0
    for m_value in range(1, 51):
        for q_value, (c0, t0, c1, t1) in fixed_data.items():
            prime = 6 * m_value + q_value
            if not is_prime(prime):
                continue
            common_power = pow(2, 2 * m_value + q_value - 1, prime)
            predicted = (
                (fraction_mod(c0, prime) * common_power - fraction_mod(t0, prime))
                % prime,
                (fraction_mod(c1, prime) * common_power - fraction_mod(t1, prime))
                % prime,
            )
            replayed = (
                modular_log_residue(m_value, prime, 0),
                modular_log_residue(m_value, prime, 1),
            )
            assert predicted == replayed
            small_formula_replays += 1

    payload = {
        "schema": "mixed-cubic-large-prime-log-residue-fixed-gap-v2",
        "generator": Path(__file__).name,
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "theorem": "For m>=1 and prime p with 6m<p<6m+49, p does not divide both lambda0 and lambda1.",
        "lambda0": "2^(2m)*L0",
        "lambda1": "2^(2m+2)*L1",
        "coefficient_formulas": {
            "lambda0": "[y^(4m)] (1-y)^(6m)(1+y)/(1+y^2)^(4m+1)",
            "lambda1": "[y^(4m+1)] (1-y)^(6m)(1+y)^4/(1+y^2)^(4m+2)",
        },
        "omitted_odd_gaps": "q divisible by 3 makes p=6m+q a composite multiple of 3",
        "rows": rows,
        "independent_small_formula_replays": {
            "m_range": "1..50",
            "number_of_prime_cases": small_formula_replays,
            "all_fixed_gap_formulas_equal_scalar_recurrence": True,
        },
        "primality_certificate": "Every listed resultant factor is below 2^64 and passes the deterministic seven-base Miller-Rabin theorem for that range.",
        "exact_primality_boundary": "All factor primality claims are deterministic because max(factor)<2^64; no claim is made that the witness set is deterministic beyond 2^64.",
        "exceptional_ray_reduction": {
            "ray": "p=10m+3",
            "identity": "For f=A^(6m)/R^(4m+2), f_j=(1/2)[t^j]A^(6m)R^(6m+1) mod p for j<p.",
            "degree_five_map": "t*A(t)*R(t)=(1-t)^5-(1-t)",
            "status": "unresolved; this reduction is not a nonvanishing proof",
        },
        "warning": "This proves only a fixed-width fresh-prime exclusion, not p>6m for all p.",
    }
    output_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output_bytes)
    print(hashlib.sha256(output_bytes).hexdigest())


if __name__ == "__main__":
    main()

