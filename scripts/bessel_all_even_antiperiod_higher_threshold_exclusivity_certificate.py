#!/usr/bin/env python3
"""Exact replay for all even Bessel anti-period congruences."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


DEPENDENCIES = {
    "sources/bessel_denominator_zero_gap_smooth_radical_barrier.md": (
        "dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc"
    ),
    "sources/bessel_large_prime_four_point_exclusivity.md": (
        "1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41"
    ),
    "sources/bessel_padic_index_interpolation_analytic_height_barrier.md": (
        "a50f45248133e437ee318b8cc28e6bbcc51de3568f3e621043221c90ddb4f348"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_dependencies(repo: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(repo / relative)
        assert actual == expected, (relative, expected, actual)
        observed[relative] = actual
    return observed


def primes_below(limit: int) -> list[int]:
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            count = (limit - 1 - start) // candidate + 1
            sieve[start:limit:candidate] = b"\x00" * count
    return [index for index, flag in enumerate(sieve) if flag]


def q_mod(limit: int, modulus: int) -> list[int]:
    if limit == 0:
        return [1 % modulus]
    values = [1 % modulus, 1 % modulus]
    for n in range(2, limit + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values


def q_exact(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def mahler_coefficients(limit: int) -> list[int]:
    values = [1, -2]
    previous = 0
    for j in range(0, limit - 1):
        current = values[j]
        following = values[j + 1]
        values.append(
            -4 * (j + 2) * following
            - (8 * j + 6) * current
            - 4 * j * previous
        )
        previous = current
    return values[: limit + 1]


def valuation(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def endpoint_and_valuation_checks(k_max: int, prime_bound: int) -> dict:
    primes = primes_below(prime_bound)
    maximum = max(
        2 * k * prime + 1
        for k in range(1, k_max + 1)
        for prime in primes
        if prime > 2 * k
    )
    mahler = mahler_coefficients(maximum)

    exact_q = q_exact(14)
    direct_checks = 0
    for j in range(15):
        direct = sum(
            (-1) ** (j - index)
            * math.comb(j, index)
            * ((-1) ** index * exact_q[index])
            for index in range(j + 1)
        )
        assert direct == mahler[j]
        direct_checks += 1

    pair_count = 0
    endpoint_checks = 0
    degree_valuation_checks = 0
    for k in range(1, k_max + 1):
        constant = math.factorial(2 * k) // math.factorial(k)
        for prime in primes:
            if prime <= 2 * k:
                continue
            pair_count += 1
            assert 2 * k * prime + 1 < prime * prime
            even_index = 2 * k * prime
            odd_index = even_index + 1
            half_index = k * prime
            ratio_even = math.factorial(even_index) // math.factorial(half_index)
            ratio_odd = ratio_even * odd_index
            assert mahler[even_index] % ratio_even == 0
            assert mahler[odd_index] % ratio_odd == 0
            assert (mahler[even_index] // ratio_even) % prime == (-1) ** k % prime
            assert (mahler[odd_index] // ratio_odd) % prime == (
                2 * (-1) ** (k + 1)
            ) % prime
            assert valuation(ratio_even, prime) == k
            normalized_ratio = (ratio_even // prime**k) % prime
            assert normalized_ratio == (
                (-1) ** k * constant
            ) % prime
            modulus = prime ** (k + 1)
            assert mahler[even_index] % modulus == constant * prime**k % modulus
            assert mahler[odd_index] % modulus == -2 * constant * prime**k % modulus
            endpoint_checks += 8

            for ell in range(1, k + 1):
                required = k + 1 - ell
                for d in range(ell, ell * (prime - 1) + 1):
                    j = (2 * k - ell) * prime + d
                    assert valuation(mahler[j], prime) >= required
                    assert valuation(mahler[j + 1], prime) >= required
                    degree_valuation_checks += 2

    return {
        "k_max": k_max,
        "prime_bound_exclusive": prime_bound,
        "admissible_k_prime_pairs": pair_count,
        "direct_mahler_checks": direct_checks,
        "endpoint_checks": endpoint_checks,
        "nonendpoint_degree_valuation_checks": degree_valuation_checks,
    }


def all_even_congruence_checks(
    k_max: int, prime_bound: int, index_multiplier: int
) -> dict:
    pair_count = 0
    even_checks = 0
    odd_checks = 0
    by_k: dict[str, dict[str, int]] = {}
    primes = primes_below(prime_bound)
    for k in range(1, k_max + 1):
        constant = math.factorial(2 * k) // math.factorial(k)
        k_pairs = 0
        k_even = 0
        for prime in primes:
            if prime <= 2 * k:
                continue
            pair_count += 1
            k_pairs += 1
            modulus = prime ** (k + 1)
            max_n = index_multiplier * prime
            values = q_mod(max_n + 2 * k * prime, modulus)
            for n in range(max_n + 1):
                even_sum = sum(
                    math.comb(2 * k, j) * values[n + j * prime]
                    for j in range(2 * k + 1)
                )
                assert (
                    even_sum - constant * prime**k * values[n]
                ) % modulus == 0
                even_checks += 1
                k_even += 1

                odd_sum = sum(
                    math.comb(2 * k - 1, j) * values[n + j * prime]
                    for j in range(2 * k)
                )
                assert odd_sum % (prime**k) == 0
                odd_checks += 1
        by_k[str(k)] = {
            "admissible_prime_count": k_pairs,
            "even_congruence_checks": k_even,
        }
    return {
        "k_max": k_max,
        "prime_bound_exclusive": prime_bound,
        "index_multiplier": index_multiplier,
        "admissible_k_prime_pairs": pair_count,
        "even_congruence_checks": even_checks,
        "odd_divisibility_checks": odd_checks,
        "by_k": by_k,
    }


def signed_value(value: int, t: int) -> int:
    return value if t % 2 == 0 else -value


def finite_difference_at_zero(values: list[int], order: int) -> int:
    return sum(
        (-1) ** (order - index) * math.comb(order, index) * values[index]
        for index in range(order + 1)
    )


def evaluate_binomial_polynomial(coefficients: list[int], t: int, prime: int) -> int:
    return sum(
        coefficient * math.comb(t, index)
        for index, coefficient in enumerate(coefficients)
    ) % prime


def root_fibre_checks(k_max: int, prime_bound: int) -> dict:
    primes = primes_below(prime_bound)
    root_fibre_count = 0
    newton_checks = 0
    divided_difference_checks = 0
    by_k: dict[str, dict[str, int]] = {}

    for k in range(1, k_max + 1):
        qualifying_full_fibres = 0
        zero_threshold_polynomials = 0
        qualifying_reflection_pairs = 0
        reflection_polynomial_checks = 0
        k_root_fibres = 0
        k_newton_checks = 0
        for prime in primes:
            if prime <= 2 * k:
                continue
            modulus = prime ** (k + 1)
            values = q_mod(prime * prime - 1, modulus)
            full_polynomials: dict[int, list[int]] = {}

            for r in range(prime):
                if values[r] % prime:
                    continue
                root_fibre_count += 1
                k_root_fibres += 1
                translated = [
                    signed_value(values[r + t * prime], t)
                    for t in range(prime)
                ]
                differences = [
                    finite_difference_at_zero(translated, order)
                    for order in range(2 * k)
                ]

                for h in range(k):
                    assert differences[2 * h] % (prime ** (h + 1)) == 0
                    assert differences[2 * h + 1] % (prime ** (h + 1)) == 0
                    divided_difference_checks += 2

                for t in range(prime):
                    expected = sum(
                        math.comb(t, order) * differences[order]
                        for order in range(2 * k)
                    ) % modulus
                    assert translated[t] % modulus == expected
                    newton_checks += 1
                    k_newton_checks += 1

                if not all(value % (prime**k) == 0 for value in translated):
                    continue
                qualifying_full_fibres += 1
                assert all(
                    difference % (prime**k) == 0 for difference in differences
                )
                coefficients = [
                    (difference // (prime**k)) % prime
                    for difference in differences
                ]
                full_polynomials[r] = coefficients
                roots = []
                for t in range(prime):
                    polynomial_value = evaluate_binomial_polynomial(
                        coefficients, t, prime
                    )
                    observed = (translated[t] // (prime**k)) % prime
                    assert polynomial_value == observed
                    if polynomial_value == 0:
                        roots.append(t)
                if any(coefficients):
                    assert len(roots) <= 2 * k - 1
                else:
                    zero_threshold_polynomials += 1
                    assert len(roots) == prime

            for r, coefficients in full_polynomials.items():
                s = prime - 1 - r
                if r < s and s in full_polynomials:
                    qualifying_reflection_pairs += 1
                    for t in range(prime):
                        assert evaluate_binomial_polynomial(
                            full_polynomials[s], t, prime
                        ) == evaluate_binomial_polynomial(
                            coefficients, (-1 - t) % prime, prime
                        )
                        reflection_polynomial_checks += 1
                elif r == s:
                    qualifying_reflection_pairs += 1
                    for t in range(prime):
                        assert evaluate_binomial_polynomial(
                            coefficients, t, prime
                        ) == evaluate_binomial_polynomial(
                            coefficients, (-1 - t) % prime, prime
                        )
                        reflection_polynomial_checks += 1

        by_k[str(k)] = {
            "root_fibres": k_root_fibres,
            "newton_checks": k_newton_checks,
            "qualifying_full_fibres": qualifying_full_fibres,
            "zero_threshold_polynomials": zero_threshold_polynomials,
            "qualifying_reflection_pairs": qualifying_reflection_pairs,
            "reflection_polynomial_checks": reflection_polynomial_checks,
        }

    return {
        "k_max": k_max,
        "prime_bound_exclusive": prime_bound,
        "root_fibre_count_with_k_multiplicity": root_fibre_count,
        "newton_checks": newton_checks,
        "divided_difference_checks": divided_difference_checks,
        "by_k": by_k,
        "scope_note": (
            "Qualifying full fibres are counted separately by k. Zero counts "
            "for k>=2 mean the symbolic higher-threshold/reflection theorem "
            "was not inferred from an actual full-survival example."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint-k-max", type=int, default=5)
    parser.add_argument("--endpoint-prime-bound", type=int, default=50)
    parser.add_argument("--congruence-k-max", type=int, default=5)
    parser.add_argument("--congruence-prime-bound", type=int, default=300)
    parser.add_argument("--index-multiplier", type=int, default=3)
    parser.add_argument("--fibre-k-max", type=int, default=4)
    parser.add_argument("--fibre-prime-bound", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.json"
        ),
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    dependencies = check_dependencies(repo)
    endpoints = endpoint_and_valuation_checks(
        args.endpoint_k_max, args.endpoint_prime_bound
    )
    congruences = all_even_congruence_checks(
        args.congruence_k_max,
        args.congruence_prime_bound,
        args.index_multiplier,
    )
    fibres = root_fibre_checks(args.fibre_k_max, args.fibre_prime_bound)

    result = {
        "description": (
            "Deterministic exact replay for all even Bessel anti-period "
            "congruences and higher-threshold Newton polynomial laws."
        ),
        "frozen_dependencies": dependencies,
        "endpoint_and_valuation_grid": endpoints,
        "all_even_congruence_grid": congruences,
        "root_fibre_grid": fibres,
        "scope_warning": (
            "The theorem requires p>2k. It bounds next-level survivors only "
            "after a fibre has survived completely through p^k. It gives no "
            "uniform bound on the valuation along an ordinary unique lift. "
            "The default replay has zero qualifying full fibres for every "
            "k>=2, so the higher-threshold conclusions are symbolic theorems, "
            "not finite extrapolations."
        ),
    }

    output = args.output
    if not output.is_absolute():
        output = repo / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
