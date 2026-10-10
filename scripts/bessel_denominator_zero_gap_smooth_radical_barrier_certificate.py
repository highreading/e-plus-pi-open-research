"""Certificate for zero-gap sparsity and the smooth-radical valuation barrier.

The all-prime proof is in
sources/bessel_denominator_zero_gap_smooth_radical_barrier.md.  Finite checks
here include the exact first-lift law and are diagnostics/certificates, not
substitutes for that proof.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

from critical_fourier_three_adjacent_matching_product_certificate import (
    fourier_polynomial,
)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index in range(3, limit + 1, 2) if sieve[index]]


def pq_pair(n: int) -> tuple[int, int]:
    p_previous, p_value = 1, 3
    q_previous, q_value = 1, 1
    if n == 0:
        return 1, 1
    if n == 1:
        return 3, 1
    for index in range(2, n + 1):
        coefficient = 2 * (2 * index - 1)
        p_previous, p_value = p_value, coefficient * p_value + p_previous
        q_previous, q_value = q_value, coefficient * q_value + q_previous
    return p_value, q_value


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation(0) is not finite")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def residue_values(prime: int, length: int) -> list[int]:
    values = [1, 1]
    for index in range(2, length):
        values.append(
            (2 * (2 * index - 1) * values[-1] + values[-2]) % prime
        )
    return values[:length]


def zero_gap_record(prime: int) -> dict[str, object]:
    values = residue_values(prime, 2 * prime + 1)
    assert all(
        values[index + prime] == (-values[index]) % prime
        for index in range(prime + 1)
    )
    roots = [index for index in range(prime) if values[index] == 0]
    assert not any(
        values[index] == values[(index + 1) % prime] == 0
        for index in range(prime)
    )
    if roots:
        gaps = [
            (roots[(index + 1) % len(roots)] - roots[index]) % prime
            for index in range(len(roots))
        ]
        gaps = [prime if gap == 0 else gap for gap in gaps]
        assert sum(gaps) == prime
    else:
        gaps = []
    counts = Counter(gaps)
    assert all(length >= 2 for length in gaps)
    assert all(count <= length - 1 for length, count in counts.items())
    best_bound = min(
        D * (D - 1) / 2 + prime / (D + 1)
        for D in range(1, prime + 1)
    )
    assert len(roots) <= best_bound + 1e-12
    assert len(roots) <= 2 * prime ** (2 / 3) + 1e-12
    return {
        "p": prime,
        "root_count": len(roots),
        "roots": roots,
        "gap_counts": {str(key): counts[key] for key in sorted(counts)},
        "best_real_bound_over_integer_D": best_bound,
    }


def second_difference_record(prime: int) -> dict[str, object]:
    """Check Theorem 3 and its four explicit base residues."""
    modulus = prime * prime
    check_count = 2 * prime + 1
    values = residue_values(modulus, check_count + 2 * prime)
    assert all(
        (
            values[index + 2 * prime]
            + 2 * values[index + prime]
            + values[index]
            - 2 * prime * values[index]
        )
        % modulus
        == 0
        for index in range(check_count)
    )

    factorial = 1
    S = 1
    for index in range(1, prime - 1):
        factorial = factorial * index % prime
        S = (S + factorial) % prime
    factorial = 1
    T = 0
    for index in range(2, prime - 1):
        if index > 2:
            factorial = factorial * (index - 2) % prime
        T = (T + (index + 1) * factorial) % prime
    predicted = {
        "q_p": (-1 + prime * (S - 2)) % modulus,
        "q_2p": (1 + prime * (-2 * S + 6)) % modulus,
        "q_p_plus_1": (-1 + prime * (T - 5)) % modulus,
        "q_2p_plus_1": (1 + prime * (12 - 2 * T)) % modulus,
    }
    actual = {
        "q_p": values[prime],
        "q_2p": values[2 * prime],
        "q_p_plus_1": values[prime + 1],
        "q_2p_plus_1": values[2 * prime + 1],
    }
    assert actual == predicted
    return {
        "p": prime,
        "n_values_checked": check_count,
        "S_mod_p": S,
        "T_mod_p": T,
        "base_residues_mod_p_squared": actual,
    }


def anti_period_lift_records(prime: int) -> list[dict[str, object]]:
    """Check first-order anti-period lifting for every root modulo ``prime``."""
    modulus = prime * prime
    values = residue_values(prime=modulus, length=modulus)
    assert all(
        values[modulus - 1 - index] == values[index]
        for index in range(modulus)
    )
    records = []
    for root in range(prime):
        if values[root] % prime:
            continue
        base = values[root]
        delta = ((-values[root + prime] - base) // prime) % prime
        assert all(
            ((-1) ** lift * values[root + lift * prime]) % modulus
            == (base + lift * prime * delta) % modulus
            for lift in range(prime)
        )
        lifts = [
            lift
            for lift in range(prime)
            if values[root + lift * prime] == 0
        ]
        if delta:
            assert len(lifts) == 1
        elif base:
            assert lifts == []
        else:
            assert lifts == list(range(prime))
        if root == (prime - 1) // 2:
            assert delta == 0
        records.append(
            {
                "p": prime,
                "root_mod_p": root,
                "q_root_mod_p_squared": base,
                "anti_period_displacement_mod_p": delta,
                "lift_parameters_mod_p": lifts,
            }
        )
    return records


def matching_record(n: int, k: int, prime: int) -> dict[str, object]:
    K = k - 1
    coefficients = fourier_polynomial(n, k)
    assert len(coefficients) == 2 * K + 1
    center = K
    c0, c0_imaginary = coefficients[center]
    assert c0 > 0 and c0_imaginary == 0

    lcm_value = 1
    for index in range(1, K + 1):
        lcm_value = math.lcm(lcm_value, index)

    t_value = 0
    for index in range(1, K + 1):
        real, imaginary = coefficients[center + index]
        sine = (0, 1, 0, -1)[index % 4]
        cosine = (1, 0, -1, 0)[index % 4]
        numerator = real * sine - imaginary * (1 - cosine)
        t_value += (lcm_value // index) * numerator

    ratio = Fraction(4 * t_value, lcm_value * c0)
    A, B = ratio.numerator, ratio.denominator
    p_value, q_value = pq_pair(n)
    d = math.gcd(q_value, B)
    M = (q_value // d) * A - (B // d) * p_value
    g = math.gcd(abs(M), d)
    return {
        "n": n,
        "k": k,
        "K": K,
        "prime": prime,
        "v_prime_q_n": valuation(q_value, prime),
        "v_prime_B": valuation(B, prime),
        "v_prime_M": valuation(M, prime),
        "v_prime_d": valuation(d, prime),
        "v_prime_g": valuation(g, prime),
        "decimal_digits": {
            "A": len(str(abs(A))),
            "B": len(str(B)),
            "M": len(str(abs(M))),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=1000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_denominator_zero_gap_smooth_radical_barrier_certificate.json"
        ),
    )
    arguments = parser.parse_args()

    prime_records = [
        zero_gap_record(prime)
        for prime in primes_up_to(arguments.prime_limit)
    ]
    second_difference_records = [
        second_difference_record(prime)
        for prime in primes_up_to(arguments.prime_limit)
    ]
    lift_records_through_79 = [
        record
        for prime in primes_up_to(79)
        for record in anti_period_lift_records(prime)
    ]
    singular_lifts = [
        record
        for record in lift_records_through_79
        if record["anti_period_displacement_mod_p"] == 0
    ]
    assert singular_lifts == [
        {
            "p": 79,
            "root_mod_p": 39,
            "q_root_mod_p_squared": 948,
            "anti_period_displacement_mod_p": 0,
            "lift_parameters_mod_p": [],
        }
    ]
    p18, q18 = pq_pair(18)
    _, q361 = pq_pair(361)
    _, q1359 = pq_pair(1359)
    high_powers = {
        "v7_q18": valuation(q18, 7),
        "v7_q361": valuation(q361, 7),
        "v11_q1359": valuation(q1359, 11),
    }
    assert high_powers == {"v7_q18": 3, "v7_q361": 4, "v11_q1359": 5}
    assert math.gcd(p18, q18) == 1

    matching = [matching_record(18, k, 7) for k in (1004, 1005, 1006)]
    assert [record["v_prime_B"] for record in matching] == [3, 3, 3]
    assert [record["v_prime_M"] for record in matching] == [5, 2, 1]
    assert [record["v_prime_g"] for record in matching] == [3, 2, 1]

    output = {
        "description": (
            "Finite certificate for the all-prime zero-gap and first-lift "
            "theorems, plus exact diagnostics for the remaining prime-power "
            "valuation barrier"
        ),
        "prime_limit": arguments.prime_limit,
        "number_of_odd_primes_checked": len(prime_records),
        "maximum_root_count": max(
            (record["root_count"] for record in prime_records), default=0
        ),
        "prime_records": prime_records,
        "second_anti_period_difference_checks": second_difference_records,
        "anti_period_lift_scan_through_79": lift_records_through_79,
        "first_singular_anti_period_lift": singular_lifts[0],
        "high_power_examples": high_powers,
        "n18_three_adjacent_matching": matching,
        "v7_triple_gcd": min(record["v_prime_g"] for record in matching),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
