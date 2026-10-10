"""Exact certificate for the generalized odd-prime Fourier bands.

The all-parameter proof is in
sources/critical_fourier_generalized_odd_prime_bands.md.  The finite-grid
checks below use exact Gaussian-integer arithmetic.  Floating point occurs
only in the explicitly labelled asymptotic-mass diagnostic.
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
    """Return P_n(y) from the exact Fourier normalization."""
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


def fourier_polynomial(n: int, K: int) -> list[Gaussian]:
    """Return G_{n,k}(y), where K=k-1, in increasing coefficient order."""
    assert K >= n
    ell = K - n
    binomial = [
        (math.comb(2 * ell, index), 0)
        for index in range(2 * ell + 1)
    ]
    value = polymul(base_polynomial(n), binomial)
    assert len(value) == 2 * K + 1
    return value


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def forced_bands(n: int, K: int, primes: list[int]) -> list[tuple[int, int]]:
    """Return (p,a) satisfying the exact hypotheses, using integers only."""
    ell = K - n
    value: list[tuple[int, int]] = []
    for prime in primes:
        if prime == 2 or prime * prime <= K:
            continue
        a = (2 * ell) // prime
        if a < 3 or a % 2 == 0:
            continue
        if not (a * prime <= 2 * ell and (a + 1) * prime > 2 * K):
            continue
        value.append((prime, a))
    return value


def lcm_to(K: int) -> int:
    value = 1
    for index in range(1, K + 1):
        value = math.lcm(value, index)
    return value


def fourier_content(
    coefficients: list[Gaussian], K: int
) -> tuple[int, int, int]:
    """Return C_0,T,h from exact Gaussian coefficients."""
    c0_real, c0_imaginary = coefficients[K]
    assert c0_imaginary == 0 and c0_real > 0
    lcm_value = lcm_to(K)
    t_value = 0
    sine_values = (0, 1, 0, -1)
    cosine_values = (1, 0, -1, 0)
    for index in range(1, K + 1):
        real, imaginary = coefficients[K + index]
        sine = sine_values[index % 4]
        cosine = cosine_values[index % 4]
        n_value = real * sine - imaginary * (1 - cosine)
        t_value += (lcm_value // index) * n_value
    h_value = math.gcd(4 * t_value, lcm_value * c0_real)
    return c0_real, t_value, h_value


def exact_grid(max_n: int, max_K: int) -> dict[str, object]:
    primes = primes_up_to(max_K)
    transcript: list[str] = []
    sample_records: list[dict[str, int]] = []
    band_exponents: Counter[int] = Counter()
    parameter_pairs = 0
    forced_prime_instances = 0
    coefficient_checks = 0

    for n in range(2, max_n + 1, 2):
        for K in range(n, max_K + 1):
            bands = forced_bands(n, K, primes)
            if not bands:
                continue
            parameter_pairs += 1
            coefficients = fourier_polynomial(n, K)
            c0, t_value, h_value = fourier_content(coefficients, K)
            forced_product = 1

            for prime, a in bands:
                forced_prime_instances += 1
                band_exponents[a] += 1
                ell = K - n
                s = 2 * ell - a * prime
                r = (prime + s + 2 * n) // 2
                degree_bound = 2 * n + s
                assert 0 <= s < prime and s % 2 == 1
                assert degree_bound < r < prime
                assert (a + 1) * prime > 2 * K
                assert a * prime <= 2 * ell
                assert prime < K < prime * prime

                for multiple in range(-(K // prime), K // prime + 1):
                    real, imaginary = coefficients[K + multiple * prime]
                    assert real % prime == 0
                    assert imaginary % prime == 0
                    coefficient_checks += 1

                assert c0 % prime == 0
                assert t_value % prime == 0
                assert h_value % prime == 0
                forced_product *= prime
                line = (
                    f"n={n};K={K};p={prime};a={a};s={s};r={r};"
                    f"d={degree_bound};C0mod={c0 % prime};"
                    f"Tmod={t_value % prime};hmod={h_value % prime}"
                )
                transcript.append(line)
                if len(sample_records) < 24:
                    sample_records.append(
                        {
                            "n": n,
                            "K": K,
                            "p": prime,
                            "a": a,
                            "s": s,
                            "r": r,
                            "degree_bound": degree_bound,
                        }
                    )

            assert h_value % forced_product == 0

    digest = hashlib.sha256("\n".join(transcript).encode("ascii")).hexdigest()
    return {
        "max_even_n": max_n,
        "max_K": max_K,
        "parameter_pairs_with_nonempty_band": parameter_pairs,
        "forced_prime_instances": forced_prime_instances,
        "coefficient_congruences_checked": coefficient_checks,
        "band_exponent_counts": {
            str(exponent): band_exponents[exponent]
            for exponent in sorted(band_exponents)
        },
        "transcript_sha256": digest,
        "sample_records": sample_records,
    }


def mass_diagnostic(K_values: list[int]) -> list[dict[str, object]]:
    """Numerically compare log H/K with 2 log(2)-1; not part of the proof."""
    primes = primes_up_to(max(K_values))
    target = 2 * math.log(2) - 1
    records: list[dict[str, object]] = []
    for K in K_values:
        n = 2 * max(1, math.isqrt(K) // 2)
        bands = forced_bands(n, K, primes)
        mass = math.fsum(math.log(prime) for prime, _ in bands) / K
        records.append(
            {
                "K": K,
                "n": n,
                "forced_prime_count": len(bands),
                "log_H_over_K": format(mass, ".12f"),
                "target_2_log_2_minus_1": format(target, ".12f"),
                "difference": format(mass - target, ".12f"),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/critical_fourier_generalized_odd_prime_bands_certificate.json"
        ),
    )
    parser.add_argument("--max-n", type=int, default=16)
    parser.add_argument("--max-K", type=int, default=240)
    arguments = parser.parse_args()
    assert arguments.max_n >= 2 and arguments.max_n % 2 == 0
    assert arguments.max_K >= arguments.max_n

    output = {
        "description": (
            "Exact finite-grid certificate for generalized odd-prime "
            "critical-Fourier content bands"
        ),
        "proof_status": (
            "The finite grid is diagnostic; the all-parameter proof is "
            "in the companion source note."
        ),
        "exact_grid": exact_grid(arguments.max_n, arguments.max_K),
        "asymptotic_mass_diagnostic": mass_diagnostic(
            [10_000, 100_000, 1_000_000]
        ),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
