"""Exact certificate for top-prime-power critical-Fourier bands.

The all-parameter proof is in
sources/critical_fourier_top_prime_power_bands.md.  Gaussian polynomial
utilities are imported from the certificate for the prime-band special
case, so the two normalizations are literally identical.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

from critical_fourier_generalized_odd_prime_bands_certificate import (
    fourier_content,
    fourier_polynomial,
    primes_up_to,
)


def top_power(prime: int, K: int) -> tuple[int, int]:
    exponent = 0
    value = 1
    while value * prime <= K:
        value *= prime
        exponent += 1
    return exponent, value


def forced_top_bands(
    n: int, K: int, primes: list[int]
) -> list[tuple[int, int, int, int]]:
    ell = K - n
    value: list[tuple[int, int, int, int]] = []
    for prime in primes:
        if prime == 2 or prime > K:
            continue
        exponent, Q = top_power(prime, K)
        a = (2 * ell) // Q
        if a < 3 or a % 2 == 0:
            continue
        if not (a * Q <= 2 * ell and (a + 1) * Q > 2 * K):
            continue
        value.append((prime, exponent, Q, a))
    return value


def exact_grid(max_n: int, max_K: int) -> dict[str, object]:
    primes = primes_up_to(max_K)
    transcript: list[str] = []
    samples: list[dict[str, int | bool]] = []
    exponent_counts: Counter[int] = Counter()
    parameter_pairs = 0
    prime_instances = 0
    new_small_prime_instances = 0
    coefficient_checks = 0

    for n in range(2, max_n + 1, 2):
        for K in range(n, max_K + 1):
            bands = forced_top_bands(n, K, primes)
            if not bands:
                continue
            parameter_pairs += 1
            coefficients = fourier_polynomial(n, K)
            c0, t_value, h_value = fourier_content(coefficients, K)
            forced_product = 1

            for prime, exponent, Q, a in bands:
                prime_instances += 1
                exponent_counts[exponent] += 1
                is_new_small_prime = prime * prime <= K
                if is_new_small_prime:
                    new_small_prime_instances += 1
                s = 2 * (K - n) - a * Q
                r = (Q + s + 2 * n) // 2
                degree_bound = 2 * n + s
                assert exponent >= 1 and Q == prime**exponent
                assert Q <= K < prime * Q
                assert 0 <= s < Q and s % 2 == 1
                assert degree_bound < r < Q

                for multiple in range(-(K // Q), K // Q + 1):
                    real, imaginary = coefficients[K + multiple * Q]
                    assert real % prime == 0
                    assert imaginary % prime == 0
                    coefficient_checks += 1
                assert c0 % prime == 0
                assert t_value % prime == 0
                assert h_value % prime == 0
                forced_product *= prime
                transcript.append(
                    (
                        f"n={n};K={K};p={prime};lambda={exponent};"
                        f"Q={Q};a={a};s={s};r={r};d={degree_bound};"
                        f"C0mod={c0 % prime};Tmod={t_value % prime};"
                        f"hmod={h_value % prime}"
                    )
                )
                if len(samples) < 30 and (
                    is_new_small_prime or len(samples) < 5
                ):
                    samples.append(
                        {
                            "n": n,
                            "K": K,
                            "prime": prime,
                            "lambda": exponent,
                            "Q": Q,
                            "a": a,
                            "s": s,
                            "r": r,
                            "degree_bound": degree_bound,
                            "new_beyond_prime_band": is_new_small_prime,
                        }
                    )
            assert h_value % forced_product == 0

    return {
        "max_even_n": max_n,
        "max_K": max_K,
        "parameter_pairs_with_nonempty_band": parameter_pairs,
        "forced_prime_instances": prime_instances,
        "new_small_prime_instances": new_small_prime_instances,
        "coefficient_congruences_checked": coefficient_checks,
        "top_power_exponent_counts": {
            str(exponent): exponent_counts[exponent]
            for exponent in sorted(exponent_counts)
        },
        "transcript_sha256": hashlib.sha256(
            "\n".join(transcript).encode("ascii")
        ).hexdigest(),
        "selected_samples": samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/critical_fourier_top_prime_power_bands_certificate.json"
        ),
    )
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--max-K", type=int, default=180)
    arguments = parser.parse_args()
    assert arguments.max_n >= 2 and arguments.max_n % 2 == 0
    assert arguments.max_K >= arguments.max_n

    output = {
        "description": (
            "Exact finite-grid certificate for top-prime-power "
            "critical-Fourier content bands"
        ),
        "proof_status": (
            "The finite grid is diagnostic; the all-parameter proof is "
            "in the companion source note."
        ),
        "exact_grid": exact_grid(arguments.max_n, arguments.max_K),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
