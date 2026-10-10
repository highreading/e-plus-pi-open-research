#!/usr/bin/env python3
"""Exact finite checks for fixed-prime Bessel/Fourier matching formulas."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def valuation_nonzero(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation_nonzero requires a nonzero integer")
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def outside_part(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("outside_part requires a nonzero integer")
    value = abs(value)
    while value % prime == 0:
        value //= prime
    return value


def matching_record(
    prime: int,
    q_value: int,
    r_value: int,
    a_value: int,
    b_value: int,
) -> dict[str, int | str]:
    """Construct and verify one primitive minimal match."""
    assert prime > 2
    assert q_value > 0 and b_value > 0
    assert math.gcd(q_value, r_value) == 1
    assert math.gcd(a_value, b_value) == 1

    d_value = math.gcd(q_value, b_value)
    q_zero = q_value // d_value
    b_zero = b_value // d_value
    m_value = q_zero * a_value - b_zero * r_value
    if m_value == 0:
        raise ValueError("the nontrivial certificate excludes M=0")
    c_value = q_value * b_value // d_value
    g_value = math.gcd(abs(m_value), c_value)
    assert g_value == math.gcd(abs(m_value), d_value)
    assert math.gcd(abs(m_value), q_zero * b_zero) == 1

    q_final = c_value // g_value
    p_final = -m_value // g_value
    assert math.gcd(abs(p_final), q_final) == 1

    exponent_q = valuation_nonzero(q_value, prime)
    exponent_b = valuation_nonzero(b_value, prime)
    exponent_d = valuation_nonzero(d_value, prime)
    exponent_m = valuation_nonzero(m_value, prime)
    exponent_g = valuation_nonzero(g_value, prime)
    assert exponent_d == min(exponent_q, exponent_b)
    assert exponent_g == min(exponent_m, exponent_d)
    assert valuation_nonzero(q_final, prime) == (
        max(exponent_q, exponent_b) - exponent_g
    )
    assert valuation_nonzero(p_final, prime) == exponent_m - exponent_g

    if exponent_q != exponent_b:
        assert exponent_m == 0
        assert exponent_g == 0
        branch = "nonresonant"
    elif exponent_m < exponent_q:
        assert valuation_nonzero(q_final, prime) == exponent_q - exponent_m
        assert valuation_nonzero(p_final, prime) == 0
        branch = "resonant_partial_content"
    else:
        assert valuation_nonzero(q_final, prime) == 0
        assert valuation_nonzero(p_final, prime) == exponent_m - exponent_q
        branch = "resonant_full_content"

    q_out = outside_part(q_value, prime)
    b_out = outside_part(b_value, prime)
    d_out = outside_part(d_value, prime)
    g_out = outside_part(g_value, prime)
    m_out = outside_part(m_value, prime)
    assert d_out == math.gcd(q_out, b_out)
    assert g_out == math.gcd(m_out, d_out)
    predicted_q_out = q_out * b_out // (d_out * g_out)
    predicted_p_out = m_out // g_out
    assert outside_part(q_final, prime) == predicted_q_out
    assert outside_part(p_final, prime) == predicted_p_out
    assert outside_part(p_final, prime) * outside_part(
        q_final, prime
    ) == (m_out * q_out * b_out) // (d_out * g_out * g_out)

    # For a primitive pair, one coefficient is a prime-adic unit.  Thus
    # the product of outside parts always contains at least the smaller
    # archimedean coefficient in full.
    assert outside_part(p_final, prime) * outside_part(
        q_final, prime
    ) >= min(abs(p_final), q_final)

    return {
        "branch": branch,
        "prime": prime,
        "v_q": exponent_q,
        "v_B": exponent_b,
        "v_M": exponent_m,
        "v_g": exponent_g,
        "v_final_P": valuation_nonzero(p_final, prime),
        "v_final_Q": valuation_nonzero(q_final, prime),
        "outside_P": outside_part(p_final, prime),
        "outside_Q": outside_part(q_final, prime),
    }


def exhaustive_checks() -> dict[str, object]:
    branch_counts = {
        "nonresonant": 0,
        "resonant_partial_content": 0,
        "resonant_full_content": 0,
    }
    checks = 0
    representative: dict[str, dict[str, int | str]] = {}
    for prime in [3, 5, 7, 11]:
        for exponent_q in range(1, 4):
            for q_unit in range(1, 8):
                if q_unit % prime == 0:
                    continue
                q_value = prime**exponent_q * q_unit
                r_values = [
                    candidate
                    for candidate in range(1, min(q_value, 18))
                    if math.gcd(candidate, q_value) == 1
                ][:4]
                for exponent_b in range(0, 4):
                    for b_unit in range(1, 8):
                        if b_unit % prime == 0:
                            continue
                        b_value = prime**exponent_b * b_unit
                        for a_value in range(-12, 13):
                            if math.gcd(a_value, b_value) != 1:
                                continue
                            for r_value in r_values:
                                d_value = math.gcd(q_value, b_value)
                                m_value = (
                                    q_value // d_value * a_value
                                    - b_value // d_value * r_value
                                )
                                if m_value == 0:
                                    continue
                                record = matching_record(
                                    prime,
                                    q_value,
                                    r_value,
                                    a_value,
                                    b_value,
                                )
                                branch = str(record["branch"])
                                branch_counts[branch] += 1
                                representative.setdefault(branch, record)
                                checks += 1
    assert all(count > 0 for count in branch_counts.values())
    return {
        "checks": checks,
        "branch_counts": branch_counts,
        "representative_records": representative,
    }


def archived_case_checks() -> list[dict[str, object]]:
    """Replay two compact exact cases from the accepted Fourier archive."""
    cases = [
        {
            "n": 2,
            "k": 10,
            "A": -149056,
            "B": 135135,
            "r": 19,
            "q": 7,
            "primes": [3, 5, 7, 11, 13],
        },
        {
            "n": 4,
            "k": 40,
            "A": -335800013668180479955437617152,
            "B": 206693502597288724237259764725,
            "r": 2721,
            "q": 1001,
            "primes": [7, 11, 13],
        },
    ]
    records = []
    for case in cases:
        local_records = []
        for prime in case["primes"]:
            local_records.append(
                matching_record(
                    int(prime),
                    int(case["q"]),
                    int(case["r"]),
                    int(case["A"]),
                    int(case["B"]),
                )
            )
        d_value = math.gcd(int(case["q"]), int(case["B"]))
        q_zero = int(case["q"]) // d_value
        b_zero = int(case["B"]) // d_value
        m_value = q_zero * int(case["A"]) - b_zero * int(case["r"])
        g_value = math.gcd(abs(m_value), d_value)
        records.append(
            {
                "n": case["n"],
                "k": case["k"],
                "d": d_value,
                "g": g_value,
                "M": m_value,
                "local_records": local_records,
            }
        )
    assert records[0]["d"] == 7 and records[0]["g"] == 7
    assert records[1]["d"] == 1001 and records[1]["g"] == 143
    return records


def digit_sum(value: int, prime: int) -> int:
    assert value >= 0 and prime >= 2
    answer = 0
    while value:
        answer += value % prime
        value //= prime
    return answer


def floor_log(value: int, prime: int) -> int:
    assert value >= 1 and prime >= 2
    answer = 0
    while value >= prime:
        value //= prime
        answer += 1
    return answer


def super_catalan(first: int, second: int) -> int:
    assert first >= 0 and second >= 0
    numerator = math.factorial(2 * first) * math.factorial(2 * second)
    denominator = (
        math.factorial(first)
        * math.factorial(second)
        * math.factorial(first + second)
    )
    assert numerator % denominator == 0
    return numerator // denominator


def central_coefficient(r_value: int, k_value: int) -> int:
    return sum(
        math.comb(2 * r_value, 2 * index)
        * super_catalan(
            r_value + index,
            k_value - r_value - index,
        )
        for index in range(r_value + 1)
    )


def factorization_polynomials(r_value: int, k_value: int) -> tuple[int, int]:
    denominator = math.prod(
        2 * k_value - (2 * r_value + 1 + 2 * offset)
        for offset in range(r_value)
    )
    numerator = 0
    for index in range(r_value + 1):
        rising_odd = math.prod(
            2 * r_value + 1 + 2 * offset for offset in range(index)
        )
        descending_odd = math.prod(
            2 * k_value - (2 * r_value + 1 + 2 * offset)
            for offset in range(index, r_value)
        )
        numerator += (
            math.comb(2 * r_value, 2 * index)
            * rising_odd
            * descending_odd
        )
    return numerator, denominator


def central_fixed_prime_checks() -> dict[str, object]:
    checks = 0
    prime_checks = 0
    maximum_r = 14
    maximum_k = 90
    primes = [3, 5, 7, 11, 13, 17, 19]
    representatives: list[dict[str, int]] = []
    for r_value in range(1, maximum_r + 1):
        for k_value in range(2 * r_value, maximum_k + 1):
            coefficient = central_coefficient(r_value, k_value)
            factor_numerator, factor_denominator = factorization_polynomials(
                r_value, k_value
            )
            base_term = super_catalan(r_value, k_value - r_value)
            assert coefficient * factor_denominator == (
                base_term * factor_numerator
            )
            assert factor_denominator > 0
            assert 0 < factor_numerator
            assert factor_numerator <= (
                2 ** (2 * r_value - 1) * (2 * k_value) ** r_value
            )
            assert factor_numerator < (8 * k_value) ** r_value
            checks += 1

            for prime in primes:
                logarithmic_length = floor_log(k_value, prime)
                digit_numerator = (
                    digit_sum(r_value, prime)
                    + digit_sum(k_value - r_value, prime)
                    + digit_sum(k_value, prime)
                    - digit_sum(2 * r_value, prime)
                    - digit_sum(2 * k_value - 2 * r_value, prime)
                )
                assert digit_numerator % (prime - 1) == 0
                predicted_base_valuation = digit_numerator // (prime - 1)
                assert predicted_base_valuation == valuation_nonzero(
                    base_term, prime
                )
                assert predicted_base_valuation <= 3 * (
                    1 + logarithmic_length
                )

                coefficient_valuation = valuation_nonzero(coefficient, prime)
                numerator_valuation = valuation_nonzero(
                    factor_numerator, prime
                )
                denominator_valuation = valuation_nonzero(
                    factor_denominator, prime
                )
                assert coefficient_valuation == (
                    predicted_base_valuation
                    + numerator_valuation
                    - denominator_valuation
                )
                assert coefficient_valuation <= (
                    predicted_base_valuation + numerator_valuation
                )

                # Exact integer versions of equations (47) and (49).
                assert prime**coefficient_valuation <= (
                    (8 * k_value) ** r_value
                    * prime ** (3 * (1 + logarithmic_length))
                )
                maximum_fourier_valuation = (
                    coefficient_valuation + logarithmic_length
                )
                assert prime**maximum_fourier_valuation <= (
                    (8 * k_value) ** r_value
                    * prime ** (4 * (1 + logarithmic_length))
                )
                prime_checks += 1

            if (r_value, k_value) in [(1, 2), (4, 17), (14, 90)]:
                representatives.append(
                    {
                        "r": r_value,
                        "K": k_value,
                        "C0": coefficient,
                        "F": factor_numerator,
                        "D": factor_denominator,
                    }
                )

    return {
        "factorization_checks": checks,
        "fixed_prime_checks": prime_checks,
        "r_range": [1, maximum_r],
        "K_range_for_each_r": ["2r", maximum_k],
        "primes": primes,
        "representative_records": representatives,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for the fixed-prime Bessel/Fourier "
            "matching valuation and outside-cofactor dichotomy"
        ),
        "exhaustive_box": exhaustive_checks(),
        "archived_critical_fourier_cases": archived_case_checks(),
        "central_fixed_prime_bound": central_fixed_prime_checks(),
        "leading_scale_comparison": {
            "hypothetical_Bessel_root": "1 * n log n",
            "fixed_prime_Fourier_upper_bound": "(1/2 + o(1)) * n log n",
            "consequence": "exponent resonance is eventually impossible",
        },
        "status": (
            "finite diagnostic; the all-degree fixed-prime estimate and "
            "conditional no-go theorem are proved symbolically in the "
            "companion source; existence of a main-scale Bessel root is "
            "not claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_fixed_root_fourier_single_prime_certificate.json"
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
