"""Exact certificate for the exceptional large-prime digit polynomial.

The all-parameter proof is in
sources/critical_fourier_large_prime_exceptional_digit_polynomial.md.
This script uses the independent super-Catalan formula for C_0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path


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


def central_coefficient(n: int, K: int) -> int:
    """Compute C_0 from the exact super-Catalan sum."""
    assert n > 0 and n % 2 == 0 and K >= n
    r = n // 2
    value = 0
    for j in range(r + 1):
        numerator = (
            math.comb(n, 2 * j)
            * math.factorial(n + 2 * j)
            * math.factorial(2 * K - n - 2 * j)
        )
        denominator = (
            math.factorial(r + j)
            * math.factorial(K - r - j)
            * math.factorial(K)
        )
        assert numerator % denominator == 0
        value += numerator // denominator
    assert value > 0
    return value


def A_coefficient(n: int, h: int) -> int:
    numerator = (
        math.comb(n, 2 * h)
        * math.factorial(2 * n - 2 * h)
        * math.factorial(n)
    )
    denominator = math.factorial(n - h)
    assert numerator % denominator == 0
    return numerator // denominator


def phi_value(n: int, argument: int) -> int:
    value = 0
    product = 1
    for h in range(n // 2 + 1):
        if h:
            product *= argument + 2 * h - 1
        value += A_coefficient(n, h) * (2**h) * product
    return value


def predicted_digit(n: int, K: int, prime: int) -> int:
    ell = K - n
    s = 2 * ell - prime
    denominator = (
        math.factorial(n)
        * math.factorial(ell)
        * math.factorial(K)
    ) % prime
    return (
        -math.factorial(s)
        * phi_value(n, s)
        * pow(denominator, -1, prime)
    ) % prime


def exact_grid(max_n: int, max_K: int) -> dict[str, object]:
    primes = primes_up_to(2 * max_K)
    transcript: list[str] = []
    exception_roots: defaultdict[tuple[int, int], list[int]] = defaultdict(
        list
    )
    samples: list[dict[str, int]] = []
    parameter_pairs = 0
    prime_instances = 0
    exceptional_instances = 0

    for n in range(2, max_n + 1, 2):
        leading = (
            2 ** (n // 2)
            * math.factorial(n) ** 2
            // math.factorial(n // 2)
        )
        for K in range(n, max_K + 1):
            band = [
                prime
                for prime in primes
                if K < prime <= 2 * (K - n)
            ]
            if not band:
                continue
            parameter_pairs += 1
            c0 = central_coefficient(n, K)
            ell = K - n
            fixed_phi = phi_value(n, 2 * ell)
            for prime in band:
                prime_instances += 1
                assert prime > 2 * n
                assert c0 % prime == 0
                actual = (c0 // prime) % prime
                predicted = predicted_digit(n, K, prime)
                assert actual == predicted
                assert (actual == 0) == (fixed_phi % prime == 0)
                assert leading % prime != 0
                if actual == 0:
                    exceptional_instances += 1
                    exception_roots[(n, prime)].append(K)
                    if len(samples) < 30:
                        samples.append(
                            {
                                "n": n,
                                "K": K,
                                "prime": prime,
                                "s": 2 * ell - prime,
                                "D": actual,
                                "phi_mod_prime": fixed_phi % prime,
                            }
                        )
                transcript.append(
                    (
                        f"n={n};K={K};p={prime};s={2 * ell-prime};"
                        f"D={actual};PhiMod={fixed_phi % prime}"
                    )
                )

    maximum_roots = 0
    maximum_records: list[dict[str, object]] = []
    for (n, prime), K_values in sorted(exception_roots.items()):
        assert len(K_values) <= n // 2
        if len(K_values) > maximum_roots:
            maximum_roots = len(K_values)
            maximum_records = [
                {"n": n, "prime": prime, "K_values": K_values}
            ]
        elif len(K_values) == maximum_roots:
            maximum_records.append(
                {"n": n, "prime": prime, "K_values": K_values}
            )

    return {
        "max_even_n": max_n,
        "max_K": max_K,
        "parameter_pairs_with_large_prime_band": parameter_pairs,
        "large_prime_instances": prime_instances,
        "exceptional_D_zero_instances": exceptional_instances,
        "largest_observed_exception_count_for_fixed_n_p": maximum_roots,
        "fixed_n_p_records_at_observed_maximum": maximum_records[:20],
        "selected_exceptional_samples": samples,
        "transcript_sha256": hashlib.sha256(
            "\n".join(transcript).encode("ascii")
        ).hexdigest(),
    }


def known_normalizations() -> list[dict[str, int]]:
    specifications = [
        (72, 189, 227, 163),
        (92, 442, 647, 261),
        (64, 797, 937, 257),
        (4, 35, 43, 0),
    ]
    records: list[dict[str, int]] = []
    for n, K, prime, expected_D in specifications:
        c0 = central_coefficient(n, K)
        actual = (c0 // prime) % prime
        predicted = predicted_digit(n, K, prime)
        assert c0 % prime == 0
        assert actual == predicted == expected_D
        phi_mod = phi_value(n, 2 * (K - n)) % prime
        assert (actual == 0) == (phi_mod == 0)
        records.append(
            {
                "n": n,
                "K": K,
                "prime": prime,
                "D": actual,
                "phi_mod_prime": phi_mod,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_large_prime_exceptional_digit_polynomial_"
            "certificate.json"
        ),
    )
    parser.add_argument("--max-n", type=int, default=24)
    parser.add_argument("--max-K", type=int, default=300)
    arguments = parser.parse_args()
    assert arguments.max_n >= 2 and arguments.max_n % 2 == 0
    assert arguments.max_K >= arguments.max_n

    output = {
        "description": (
            "Exact super-Catalan certificate for the exceptional "
            "large-prime Fourier digit polynomial"
        ),
        "proof_status": (
            "The finite grid is diagnostic; the all-parameter proof is "
            "in the companion source note."
        ),
        "exact_grid": exact_grid(arguments.max_n, arguments.max_K),
        "known_normalizations": known_normalizations(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
