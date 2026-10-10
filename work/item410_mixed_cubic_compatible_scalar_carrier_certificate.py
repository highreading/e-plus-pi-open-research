#!/usr/bin/env python3
"""Deterministic exact certificate for Item 410.

Uniform statements in the report are proved there.  This checker verifies
their exact formulas on transparent normalization rows, pins the dependencies,
and performs the explicitly finite m<=128 census.  The finite census is never
reported as an all-m support theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MAX_M = 128
SELECTED_M = {1, 2, 3, 10, 33, 34, 59, 67, 109, 122, 128}
COMPATIBLE_ROWS = (
    (1, 11),
    (1, 13),
    (2, 17),
    (2, 19),
    (3, 23),
    (3, 29),
    (10, 67),
    (10, 73),
)

DEPENDENCIES = {
    "sources/item373_beta_symmetric_singleton_first_quotient_report.md":
        "daa16600359a52501fcbe303359e39696c1f0b0acfdb62b944b19be77784d6c5",
    "sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md":
        "245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_report.md":
        "d76955fb4c0d89b96d0d4385c1ba4412ed15f1c8ae9bb8c449e54fc444bc32c3",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_certificate.py":
        "69e482f34421ac983d19330a5ef325cff706587137cc667ea6212228b66f0a35",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_certificate.json":
        "d306c02dee8b004b118870cdf8fbf34aaf6226bc86c247941ae7bd68899245dc",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_ledger_delta.json":
        "d37341bad5ab1d427e6cc6a611cc8ca83389a50825747e76bad0f2dea1b0c89f",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_manifest.json":
        "c1a87502b5b0f5264ecdd65f8b6fb89fb33c3db52c9add1903fbefb2c3f905a4",
    "work/item406_mixed_cubic_actual_adjacent_recurrence_hashes.sha256":
        "254defdb3ff0402c91298fe252d6554b765d81ad7df28fe8075568edb7216fd4",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def descending_binomial_values(
    initial: Fraction, degree: int, length: int
) -> list[Fraction]:
    """binom(initial-h, degree), 0<=h<length, by an exact ratio."""
    value = generalized_binomial(initial, degree)
    answer = []
    for offset in range(length):
        answer.append(value)
        value *= Fraction(initial - offset - degree, initial - offset)
    return answer


def r_scalars(m_value: int) -> tuple[Fraction, Fraction]:
    degree = 4 * m_value
    even_bins = descending_binomial_values(
        Fraction(2 * m_value - 1, 2), degree, 3 * m_value + 1
    )
    even = sum(
        (-1) ** index
        * math.comb(6 * m_value, 2 * index)
        * even_bins[index]
        for index in range(3 * m_value + 1)
    )
    odd_bins = descending_binomial_values(
        Fraction(2 * m_value - 3, 2), degree, 3 * m_value
    )
    odd = sum(
        (-1) ** index
        * math.comb(6 * m_value, 2 * index + 1)
        * odd_bins[index]
        for index in range(3 * m_value)
    )
    return even, odd


def s_scalar_for_residue(
    m_value: int, residue: int, upper_offset: int
) -> Fraction:
    degree = 4 * m_value
    numerator_degree = 10 * m_value + 1
    indices = list(range(residue, numerator_degree + 1, 4))
    bins = descending_binomial_values(
        Fraction(10 * m_value - upper_offset - residue, 4),
        degree,
        len(indices),
    )
    return sum(
        (-1) ** index * math.comb(numerator_degree, index) * value
        for index, value in zip(indices, bins)
    )


def s_scalars(m_value: int, phase: int) -> tuple[Fraction, Fraction]:
    assert phase in (0, 2)
    top = s_scalar_for_residue(m_value, phase, 1)
    previous = s_scalar_for_residue(m_value, (phase - 1) % 4, 2)
    return top, previous


def fraction_mod(value: Fraction, prime: int) -> int:
    assert value.denominator % prime
    return value.numerator * pow(value.denominator, -1, prime) % prime


def coefficient_r_mod(degree: int, m_value: int, prime: int) -> int:
    k_value = 4 * m_value + 1
    total = 0
    for numerator_degree in range(min(6 * m_value, degree) + 1):
        remainder = degree - numerator_degree
        if remainder % 2:
            continue
        half = remainder // 2
        total += (
            (-1) ** (numerator_degree + half)
            * math.comb(6 * m_value, numerator_degree)
            * math.comb(k_value + half - 1, k_value - 1)
        )
    return total % prime


def coefficient_s_mod(degree: int, m_value: int, prime: int) -> int:
    k_value = 4 * m_value + 1
    numerator_max = 10 * m_value + 1
    total = 0
    for numerator_degree in range(min(numerator_max, degree) + 1):
        remainder = degree - numerator_degree
        if remainder % 4:
            continue
        quarter = remainder // 4
        total += (
            (-1) ** numerator_degree
            * math.comb(numerator_max, numerator_degree)
            * math.comb(k_value + quarter - 1, k_value - 1)
        )
    return total % prime


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def compatible_normalization_rows() -> list[dict[str, object]]:
    rows = []
    for m_value, prime in COMPATIBLE_ROWS:
        assert is_prime(prime)
        q_value = prime - 6 * m_value
        assert q_value >= 5 and q_value % 2 and q_value % 3
        n_value = q_value - 1
        phase = n_value % 4
        even, odd = r_scalars(m_value)
        top, previous = s_scalars(m_value, phase)
        r_previous = coefficient_r_mod(n_value - 1, m_value, prime)
        r_top = coefficient_r_mod(n_value, m_value, prime)
        s_previous = coefficient_s_mod(n_value - 1, m_value, prime)
        s_top = coefficient_s_mod(n_value, m_value, prime)
        sign = -1 if (n_value // 2) % 2 else 1
        assert r_top == sign * fraction_mod(even, prime) % prime
        assert r_previous == sign * fraction_mod(odd, prime) % prime
        assert s_top == fraction_mod(top, prime)
        assert s_previous == fraction_mod(previous, prime)

        # Check the exact S recurrence modulo p through the target boundary.
        coefficients = [
            coefficient_s_mod(degree, m_value, prime)
            for degree in range(n_value + 2)
        ]
        for degree in range(n_value + 1):
            def at(index: int) -> int:
                return coefficients[index] if index >= 0 else 0
            recurrence = (
                (degree + 1) * at(degree + 1)
                + (10 * m_value + 1)
                * (at(degree) + at(degree - 1) + at(degree - 2))
                - (degree + 6 * m_value) * at(degree - 3)
            ) % prime
            assert recurrence == 0
        rows.append(
            {
                "m": m_value,
                "p": prime,
                "q": q_value,
                "n": n_value,
                "phase": phase,
                "R_adjacent": [r_previous, r_top],
                "S_adjacent": [s_previous, s_top],
                "scalar_congruences_verified": True,
                "S_recurrence_verified_through_degree": n_value,
                "normalization_only_not_support_evidence": True,
            }
        )
    return rows


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(limit + 1) if sieve[value]]


def remove_small_prime_support(value: int, primes: list[int]) -> int:
    answer = abs(value)
    for prime in primes:
        while answer and answer % prime == 0:
            answer //= prime
    return answer


def finite_census() -> dict[str, object]:
    primes = primes_up_to(6 * MAX_M)
    witness_lines = []
    selected_rows = []
    r_binomial_failures = []
    phase_binomial_failures = []
    phase_inequality_failures = []
    identically_resonant = []
    phase_support_failures = []

    for m_value in range(1, MAX_M + 1):
        even, odd = r_scalars(m_value)
        top_zero, previous_zero = s_scalars(m_value, 0)
        top_two, previous_two = s_scalars(m_value, 2)
        all_values = (
            even,
            odd,
            top_zero,
            previous_zero,
            top_two,
            previous_two,
        )
        assert all(
            value.denominator > 0
            and value.denominator & (value.denominator - 1) == 0
            for value in all_values
        )
        if even == 0 and odd == 0:
            identically_resonant.append(m_value)
        w_value = math.gcd(abs(even.numerator), abs(odd.numerator))
        j_zero = math.gcd(
            w_value, abs(top_zero.numerator), abs(previous_zero.numerator)
        )
        j_two = math.gcd(
            w_value, abs(top_two.numerator), abs(previous_two.numerator)
        )
        if j_zero != j_two:
            phase_inequality_failures.append(m_value)

        small_primes = [prime for prime in primes if prime <= 6 * m_value]
        residual_zero = remove_small_prime_support(j_zero, small_primes)
        residual_two = remove_small_prime_support(j_two, small_primes)
        if residual_zero != 1 or residual_two != 1:
            phase_support_failures.append(
                [m_value, residual_zero, residual_two]
            )

        central_binomial = math.comb(6 * m_value, 2 * m_value)
        r_leftover = w_value // math.gcd(w_value, central_binomial)
        phase_leftover_zero = j_zero // math.gcd(j_zero, central_binomial)
        phase_leftover_two = j_two // math.gcd(j_two, central_binomial)
        if r_leftover != 1:
            r_binomial_failures.append([m_value, r_leftover])
        if phase_leftover_zero != 1 or phase_leftover_two != 1:
            phase_binomial_failures.append(
                [m_value, phase_leftover_zero, phase_leftover_two]
            )

        # Exact integer form of the report's height bound.
        height_rhs = (2 ** (14 * m_value)) * (6 * m_value) ** (4 * m_value)
        factorial = math.factorial(4 * m_value)
        assert abs(even.numerator) * factorial <= height_rhs
        assert abs(odd.numerator) * factorial <= height_rhs

        witness_lines.append(
            ":".join(
                str(value)
                for value in (
                    m_value,
                    w_value,
                    j_zero,
                    j_two,
                    residual_zero,
                    residual_two,
                    r_leftover,
                    phase_leftover_zero,
                    phase_leftover_two,
                )
            )
        )
        if m_value in SELECTED_M:
            selected_rows.append(
                {
                    "m": m_value,
                    "W_m": str(w_value),
                    "J_m_phase_0": str(j_zero),
                    "J_m_phase_2": str(j_two),
                    "R_carrier_over_gcd_with_binomial": str(r_leftover),
                    "phase_0_carrier_over_gcd_with_binomial": str(
                        phase_leftover_zero
                    ),
                    "phase_2_carrier_over_gcd_with_binomial": str(
                        phase_leftover_two
                    ),
                    "phase_carriers_have_no_prime_above_6m": (
                        residual_zero == residual_two == 1
                    ),
                    "finite_only": True,
                }
            )

    expected_r_failure_m = [
        33, 34, 59, 67, 78, 80, 81, 94, 95, 102, 107, 109, 122
    ]
    expected_phase_failure_m = [109, 122]
    assert [row[0] for row in r_binomial_failures] == expected_r_failure_m
    assert [row[0] for row in phase_binomial_failures] == expected_phase_failure_m
    assert not phase_inequality_failures
    assert not identically_resonant
    assert not phase_support_failures
    witness = "\n".join(witness_lines).encode("ascii")
    return {
        "range": f"1<=m<={MAX_M}",
        "count": MAX_M,
        "selected_rows": selected_rows,
        "identically_resonant_m": identically_resonant,
        "phase_carrier_inequality_failures": phase_inequality_failures,
        "phase_support_above_6m_failures": phase_support_failures,
        "R_carrier_divides_binomial_failures": r_binomial_failures,
        "phase_carrier_divides_binomial_failures": phase_binomial_failures,
        "labels": {
            "phase_radical_support_through_128": "EXACT_FINITE_ONLY",
            "phase_equality_through_128": "EXACT_FINITE_ONLY",
            "nonresonance_through_128": "EXACT_FINITE_ONLY",
            "multiplicity_counterexamples": "EXACT_FINITE_ONLY",
        },
        "witness_sha256": sha256_bytes(witness),
    }


def run() -> dict[str, object]:
    dependencies = verify_dependencies()
    compatible = compatible_normalization_rows()
    census = finite_census()
    witness = json.dumps(
        {
            "dependencies": dependencies,
            "compatible": compatible,
            "census_witness": census["witness_sha256"],
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "schema": "item410-mixed-compatible-scalar-carrier-v1",
        "item": 410,
        "status": "WORK_ONLY_UNAUDITED_NO_CENTRAL_EDIT_NO_BOOKING",
        "labels": {
            "PROVED": [
                "S=(1-z)^(10m+1)/(1-z^4)^(4m+1) and its exact four-term recurrence",
                "uniform compatible-prime collapse of the R pair to phase-independent E_m,O_m",
                "uniform compatible-prime collapse of the S pair to U_(m,delta),V_(m,delta)",
                "actual collision primes lie in the phase carrier J_(m,delta), hence in W_m",
                "explicit O(m) numerator-height bound outside the declared identically-resonant exceptional set",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "no E_m=O_m=0 for 1<=m<=128",
                "phase carriers agree and have no prime factor above 6m for 1<=m<=128",
                "R-only binomial divisibility counterexamples begin at m=33",
                "phase-carrier binomial divisibility counterexamples occur at m=109 and m=122",
            ],
            "OPEN": [
                "uniform exclusion of E_m=O_m=0",
                "log(rad(W_m))=o(m)",
                "rad(J_(m,delta)) divides (6m)! for every m and both phases",
                "the four-adjacent lemma and compatible H support",
                "primitive G support, Route 1, and irrationality of e+pi",
            ],
        },
        "capacity": {
            "booking_delta": 0,
            "proved_total_capacity_ceiling_delta": 0,
            "H_only_perfect_success_numeric_ceiling_reduction": 0,
            "combined_large_component_ceiling": "log(136)/6 = 0.8187758142893420014...",
            "carrier_height_normalized_upper_constant": "(14 log 2 + 4 log(3e/2))/6 = 2.55...",
            "reason_no_reduction": "primitive G can still occupy the full combined ceiling, and the new carrier bound is weaker than that ceiling",
        },
        "uniform_formulas": {
            "R_top": "[z^n]R=(-1)^(n/2) E_m mod p",
            "R_previous": "[z^(n-1)]R=(-1)^(n/2) O_m mod p",
            "S_top": "[z^n]S=U_(m,delta) mod p",
            "S_previous": "[z^(n-1)]S=V_(m,delta) mod p",
            "phase": "delta=n mod 4 in {0,2}",
            "carrier": "p|H_q implies p|J_(m,delta)|W_m",
            "S_recurrence": "(j+1)s_(j+1)+(10m+1)(s_j+s_(j-1)+s_(j-2))-(j+6m)s_(j-3)=0",
        },
        "compatible_normalization_rows": compatible,
        "finite_census": census,
        "dependency_sha256": dependencies,
        "assertions": {
            "all_finite_rows_labeled_finite_only": True,
            "no_finite_support_census_promoted": True,
            "multiplicity_counterexamples_recorded": True,
            "actual_family_distinguished_from_scalar_finite_evidence": True,
            "booking_delta_is_zero": True,
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    print(sha256_bytes(rendered))
    if arguments.output:
        arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()

