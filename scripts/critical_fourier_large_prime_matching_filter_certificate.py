"""Exact certificate for the large-prime critical-Fourier matching filter.

The all-parameter proof is in
sources/critical_fourier_large_prime_matching_filter.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


Gaussian = tuple[int, int]


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(scale: int, value: Gaussian) -> Gaussian:
    return scale * value[0], scale * value[1]


def gpow(base: Gaussian, exponent: int) -> Gaussian:
    value = (1, 0)
    while exponent:
        if exponent & 1:
            value = gmul(value, base)
        base = gmul(base, base)
        exponent //= 2
    return value


def polymul(left: list[Gaussian], right: list[Gaussian]) -> list[Gaussian]:
    value = [(0, 0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            index = left_index + right_index
            value[index] = gadd(
                value[index], gmul(left_value, right_value)
            )
    return value


def base_polynomial(n: int) -> list[Gaussian]:
    assert n > 0 and n % 2 == 0
    first = [
        (((-1) ** (n - index)) * math.comb(n, index), 0)
        for index in range(n + 1)
    ]
    second = [
        gscale(
            math.comb(n, index),
            gmul(
                gpow((1, 1), index),
                gpow((1, -1), n - index),
            ),
        )
        for index in range(n + 1)
    ]
    phase = gpow((0, -1), n)
    return [gmul(phase, value) for value in polymul(first, second)]


def fourier_polynomial(
    base: list[Gaussian], n: int, K: int
) -> list[Gaussian]:
    ell = K - n
    binomial = [
        (math.comb(2 * ell, index), 0)
        for index in range(2 * ell + 1)
    ]
    value = polymul(base, binomial)
    assert len(value) == 2 * K + 1
    return value


def r_polynomial_mod(
    base: list[Gaussian], s: int, prime: int
) -> list[Gaussian]:
    binomial = [
        (math.comb(s, index) % prime, 0)
        for index in range(s + 1)
    ]
    exact = polymul(
        [(real % prime, imaginary % prime) for real, imaginary in base],
        binomial,
    )
    return [
        (real % prime, imaginary % prime) for real, imaginary in exact
    ]


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def exponential_pair(n: int) -> tuple[int, int]:
    p_previous, p_current = 1, 3
    q_previous, q_current = 1, 1
    if n == 0:
        return p_previous, q_previous
    if n == 1:
        return p_current, q_current
    for index in range(2, n + 1):
        multiplier = 4 * index - 2
        p_previous, p_current = (
            p_current,
            multiplier * p_current + p_previous,
        )
        q_previous, q_current = (
            q_current,
            multiplier * q_current + q_previous,
        )
    return p_current, q_current


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is not used in this certificate")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def lcm_to(K: int) -> int:
    value = 1
    for index in range(1, K + 1):
        value = math.lcm(value, index)
    return value


def content_data(
    coefficients: list[Gaussian], K: int
) -> tuple[int, int, int, int]:
    c0_real, c0_imaginary = coefficients[K]
    assert c0_imaginary == 0 and c0_real > 0
    lcm_value = lcm_to(K)
    sine_values = (0, 1, 0, -1)
    cosine_values = (1, 0, -1, 0)
    t_value = 0
    for index in range(1, K + 1):
        real, imaginary = coefficients[K + index]
        n_value = (
            real * sine_values[index % 4]
            - imaginary * (1 - cosine_values[index % 4])
        )
        t_value += (lcm_value // index) * n_value
    h_value = math.gcd(4 * t_value, lcm_value * c0_real)
    return c0_real, t_value, lcm_value, h_value


def fourier_digits(
    base: list[Gaussian], n: int, K: int, prime: int
) -> tuple[int, int, int, int, int]:
    assert K < prime <= 2 * (K - n)
    s = 2 * (K - n) - prime
    u = prime - K
    d = 2 * K - prime
    residues = r_polynomial_mod(base, s, prime)
    assert len(residues) == d + 1
    sine_values = (0, 1, 0, -1)
    cosine_values = (1, 0, -1, 0)
    d_real = 0
    d_imaginary = 0
    u_value = 0
    for index, (real, imaginary) in enumerate(residues):
        denominator_d = K - index
        sign = 1 if (denominator_d - 1) % 2 == 0 else -1
        h_value = sign * pow(denominator_d, -1, prime)
        d_real = (d_real + real * h_value) % prime
        d_imaginary = (d_imaginary + imaginary * h_value) % prime

        m_value = u + index
        n_value = (
            real * sine_values[m_value % 4]
            - imaginary * (1 - cosine_values[m_value % 4])
        )
        u_value = (
            u_value + n_value * pow(m_value, -1, prime)
        ) % prime
    return d_real, d_imaginary, u_value, s, d


def exact_grid(max_n: int, max_K: int) -> dict[str, object]:
    primes = primes_up_to(2 * max_K)
    transcript: list[str] = []
    samples: list[dict[str, object]] = []
    categories: Counter[str] = Counter()
    parameter_pairs = 0
    prime_instances = 0

    for n in range(2, max_n + 1, 2):
        base = base_polynomial(n)
        p_value, q_value = exponential_pair(n)
        for K in range(n, max_K + 1):
            large_primes = [
                prime
                for prime in primes
                if K < prime <= 2 * (K - n)
            ]
            if not large_primes:
                continue
            parameter_pairs += 1
            coefficients = fourier_polynomial(base, n, K)
            c0, t_value, lcm_value, h_value = content_data(coefficients, K)
            A = 4 * t_value // h_value
            B = lcm_value * c0 // h_value
            assert math.gcd(abs(A), B) == 1
            common = math.gcd(q_value, B)
            q_zero = q_value // common
            b_zero = B // common
            M = q_zero * A - b_zero * p_value
            g_value = math.gcd(abs(M), common)

            for prime in large_primes:
                prime_instances += 1
                d_real, d_imaginary, u_value, s, degree = fourier_digits(
                    base, n, K, prime
                )
                assert c0 % prime == 0
                assert (c0 // prime) % prime == d_real
                assert d_imaginary == 0
                assert (
                    t_value * pow(lcm_value, -1, prime)
                ) % prime == u_value

                q_valuation = valuation(q_value, prime)
                actual_survival = g_value % prime == 0
                if d_real == 0:
                    category = "exceptional_D_zero"
                    assert c0 % (prime * prime) == 0
                else:
                    if q_valuation == 1 and u_value != 0:
                        q_quotient = (q_value // prime) % prime
                        congruence = (
                            4 * q_quotient * u_value
                            - p_value * d_real
                        ) % prime == 0
                    else:
                        q_quotient = None
                        congruence = False
                    predicted_survival = (
                        q_valuation == 1
                        and u_value != 0
                        and congruence
                    )
                    assert actual_survival == predicted_survival
                    if actual_survival:
                        category = "generic_survivor"
                    elif q_valuation != 1:
                        category = "excluded_q_valuation"
                    elif u_value == 0:
                        category = "excluded_U_zero"
                    else:
                        category = "excluded_final_congruence"
                categories[category] += 1
                transcript.append(
                    (
                        f"n={n};K={K};p={prime};s={s};d={degree};"
                        f"D={d_real};U={u_value};vq={q_valuation};"
                        f"survives={int(actual_survival)};category={category}"
                    )
                )
                if len(samples) < 30 and (
                    actual_survival
                    or d_real == 0
                    or category == "excluded_final_congruence"
                ):
                    samples.append(
                        {
                            "n": n,
                            "K": K,
                            "prime": prime,
                            "s": s,
                            "degree": degree,
                            "D": d_real,
                            "U": u_value,
                            "v_q": q_valuation,
                            "survives": actual_survival,
                            "category": category,
                        }
                    )

    return {
        "max_even_n": max_n,
        "max_K": max_K,
        "parameter_pairs_with_large_prime_band": parameter_pairs,
        "large_prime_instances": prime_instances,
        "category_counts": {
            category: categories[category] for category in sorted(categories)
        },
        "transcript_sha256": hashlib.sha256(
            "\n".join(transcript).encode("ascii")
        ).hexdigest(),
        "selected_samples": samples,
    }


def reflection_check(max_modulus: int) -> dict[str, int]:
    moduli = 0
    congruences = 0
    for modulus in range(3, max_modulus + 1, 2):
        p_values = [1, 3]
        q_values = [1, 1]
        for index in range(2, modulus):
            multiplier = 4 * index - 2
            p_values.append(
                (multiplier * p_values[-1] + p_values[-2]) % modulus
            )
            q_values.append(
                (multiplier * q_values[-1] + q_values[-2]) % modulus
            )
        for index in range(modulus):
            assert p_values[modulus - 1 - index] == p_values[index]
            assert q_values[modulus - 1 - index] == q_values[index]
            congruences += 2
        moduli += 1
    return {
        "largest_odd_modulus": max_modulus,
        "odd_moduli_checked": moduli,
        "reflection_congruences_checked": congruences,
    }


def known_survivors() -> list[dict[str, int]]:
    specifications = [
        (72, 189, 227, 163, 112, 88, 65, 153),
        (92, 442, 647, 261, 240, 324, 277, 480),
        (64, 797, 937, 257, 463, 601, 397, 833),
    ]
    records: list[dict[str, int]] = []
    for (
        n,
        K,
        prime,
        expected_D,
        expected_U,
        expected_q_quotient,
        expected_p,
        expected_common_residue,
    ) in specifications:
        base = base_polynomial(n)
        D, D_imaginary, U, s, degree = fourier_digits(
            base, n, K, prime
        )
        p_value, q_value = exponential_pair(n)
        assert D_imaginary == 0
        assert D == expected_D and U == expected_U
        assert valuation(q_value, prime) == 1
        q_quotient = (q_value // prime) % prime
        assert q_quotient == expected_q_quotient
        assert p_value % prime == expected_p
        left = 4 * q_quotient * U % prime
        right = p_value * D % prime
        assert left == right == expected_common_residue
        records.append(
            {
                "n": n,
                "K": K,
                "prime": prime,
                "s": s,
                "degree": degree,
                "D": D,
                "U": U,
                "v_q": 1,
                "q_over_p": q_quotient,
                "p_n": p_value % prime,
                "common_congruence_residue": left,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/critical_fourier_large_prime_matching_filter_certificate.json"
        ),
    )
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--max-K", type=int, default=160)
    arguments = parser.parse_args()
    assert arguments.max_n >= 2 and arguments.max_n % 2 == 0
    assert arguments.max_K >= arguments.max_n

    output = {
        "description": (
            "Exact finite-grid certificate for the large-prime "
            "critical-Fourier first-digit matching filter"
        ),
        "proof_status": (
            "The finite grid is diagnostic; the all-parameter proof is "
            "in the companion source note."
        ),
        "exact_grid": exact_grid(arguments.max_n, arguments.max_K),
        "bessel_reflection": reflection_check(321),
        "known_large_prime_survivors": known_survivors(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
