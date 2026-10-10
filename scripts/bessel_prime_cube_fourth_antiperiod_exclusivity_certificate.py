#!/usr/bin/env python3
"""Exact replay for fourth anti-period and cube-threshold Bessel laws."""

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
    coefficients = [1, -2]
    previous = 0  # A_{-1}
    for j in range(0, limit - 1):
        current = coefficients[j]
        following = coefficients[j + 1]
        next_value = (
            -4 * (j + 2) * following
            - (8 * j + 6) * current
            - 4 * j * previous
        )
        coefficients.append(next_value)
        previous = current
    return coefficients[: limit + 1]


def check_mahler_initial_values(prime_bound: int) -> dict[str, int]:
    primes = [p for p in primes_below(prime_bound) if p >= 5]
    maximum = 4 * max(primes) + 1
    coefficients = mahler_coefficients(maximum)

    # Independent direct binomial-transform check at low degrees.
    exact_q = q_exact(16)
    direct_checks = 0
    for j in range(17):
        direct = sum(
            (-1) ** (j - k)
            * math.comb(j, k)
            * ((-1) ** k * exact_q[k])
            for k in range(j + 1)
        )
        assert direct == coefficients[j]
        direct_checks += 1

    special_checks = 0
    for prime in primes:
        even_index = 4 * prime
        odd_index = even_index + 1
        ratio_even = math.factorial(even_index) // math.factorial(2 * prime)
        ratio_odd = math.factorial(odd_index) // math.factorial(2 * prime)
        assert coefficients[even_index] % ratio_even == 0
        assert coefficients[odd_index] % ratio_odd == 0
        assert (coefficients[even_index] // ratio_even) % prime == 1
        assert (coefficients[odd_index] // ratio_odd) % prime == (-2) % prime
        modulus = prime**3
        assert coefficients[even_index] % modulus == 12 * prime * prime % modulus
        assert coefficients[odd_index] % modulus == -24 * prime * prime % modulus
        special_checks += 6

    return {
        "prime_bound_exclusive": prime_bound,
        "direct_binomial_transform_checks": direct_checks,
        "special_coefficient_checks": special_checks,
    }


def check_fourth_antiperiod(prime_bound: int, index_multiplier: int) -> dict:
    fourth_checks = 0
    second_checks = 0
    third_checks = 0
    initial_checks = 0
    primes_checked = 0
    for prime in primes_below(prime_bound):
        if prime == 2:
            continue
        primes_checked += 1
        modulus = prime**3
        max_n = index_multiplier * prime
        values = q_mod(max_n + 4 * prime, modulus)
        for n in range(max_n + 1):
            second = values[n + 2 * prime] + 2 * values[n + prime] + values[n]
            assert (second - 2 * prime * values[n]) % (prime * prime) == 0
            second_checks += 1

            third = (
                values[n + 3 * prime]
                + 3 * values[n + 2 * prime]
                + 3 * values[n + prime]
                + values[n]
            )
            assert third % (prime * prime) == 0
            third_checks += 1

            fourth = (
                values[n + 4 * prime]
                + 4 * values[n + 3 * prime]
                + 6 * values[n + 2 * prime]
                + 4 * values[n + prime]
                + values[n]
            )
            assert (fourth - 12 * prime * prime * values[n]) % modulus == 0
            fourth_checks += 1

        for n in (0, 1):
            fourth = sum(
                math.comb(4, j) * values[n + j * prime] for j in range(5)
            )
            assert (fourth - 12 * prime * prime * values[n]) % modulus == 0
            initial_checks += 1

    return {
        "prime_bound_exclusive": prime_bound,
        "index_multiplier": index_multiplier,
        "primes_checked": primes_checked,
        "second_antiperiod_checks": second_checks,
        "third_divisibility_checks": third_checks,
        "fourth_antiperiod_checks": fourth_checks,
        "initial_value_checks": initial_checks,
    }


def signed_q(residue: int, t: int, modulus: int) -> int:
    return residue if t % 2 == 0 else -residue


def check_cubic_root_fibres(prime_bound: int, translate_count: int) -> dict:
    root_fibres = 0
    cubic_law_checks = 0
    ordinary_fibres = 0
    singular_fibres = 0
    singular_all_square_fibres = 0
    qualifying_reflection_pair_count = 0
    reflection_polynomial_checks = 0

    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        modulus = prime**3
        values = q_mod((translate_count + 3) * prime, modulus)
        singular_polynomials: dict[int, tuple[int, int, int, int]] = {}
        for r in range(prime):
            if values[r] % prime:
                continue
            root_fibres += 1
            a = [
                signed_q(values[r + t * prime], t, modulus)
                for t in range(4)
            ]
            delta_1 = a[1] - a[0]
            delta_2 = a[2] - 2 * a[1] + a[0]
            delta_3 = a[3] - 3 * a[2] + 3 * a[1] - a[0]
            assert delta_1 % prime == 0
            assert delta_2 % (prime * prime) == 0
            assert delta_3 % (prime * prime) == 0
            d = (delta_1 // prime) % (prime * prime)
            e = (delta_2 // (prime * prime)) % prime
            h = (delta_3 // (prime * prime)) % prime

            for t in range(translate_count):
                expected = (
                    values[r]
                    + t * prime * d
                    + prime * prime * math.comb(t, 2) * e
                    + prime * prime * math.comb(t, 3) * h
                ) % modulus
                observed = signed_q(values[r + t * prime], t, modulus) % modulus
                assert observed == expected
                cubic_law_checks += 1

            c = (values[r] // prime) % prime
            slope = d % prime
            square_standard = [
                t
                for t in range(prime)
                if (
                    c
                    + t * slope
                )
                % prime
                == 0
            ]
            if slope:
                ordinary_fibres += 1
                assert len(square_standard) == 1
            else:
                singular_fibres += 1
                if c:
                    assert square_standard == []
                else:
                    singular_all_square_fibres += 1
                    assert len(square_standard) == prime
                    assert d % prime == 0
                    singular_polynomials[r] = (
                        (values[r] // (prime * prime)) % prime,
                        (d // prime) % prime,
                        e,
                        h,
                    )

        def polynomial(coefficients: tuple[int, int, int, int], t: int) -> int:
            c0, c1, c2, c3 = coefficients
            return (
                c0
                + c1 * t
                + c2 * math.comb(t, 2)
                + c3 * math.comb(t, 3)
            ) % prime

        for r, coefficients in singular_polynomials.items():
            s = prime - 1 - r
            if r < s and s in singular_polynomials:
                qualifying_reflection_pair_count += 1
                for t in range(prime):
                    assert polynomial(singular_polynomials[s], t) == polynomial(
                        coefficients, (-1 - t) % prime
                    )
                    reflection_polynomial_checks += 1
            elif r == s:
                qualifying_reflection_pair_count += 1
                for t in range(prime):
                    assert polynomial(coefficients, t) == polynomial(
                        coefficients, (-1 - t) % prime
                    )
                    reflection_polynomial_checks += 1

    return {
        "prime_bound_exclusive": prime_bound,
        "translate_count": translate_count,
        "root_fibres": root_fibres,
        "ordinary_fibres": ordinary_fibres,
        "singular_fibres": singular_fibres,
        "singular_all_square_fibres": singular_all_square_fibres,
        "qualifying_reflection_pair_count": qualifying_reflection_pair_count,
        "reflection_polynomial_checks": reflection_polynomial_checks,
        "cubic_law_checks": cubic_law_checks,
    }


def truncated_valuation(residue: int, prime: int, cap: int) -> int:
    if residue == 0:
        return cap
    exponent = 0
    while exponent < cap and residue % prime == 0:
        residue //= prime
        exponent += 1
    return exponent


def finite_large_prime_scan(prime_bound: int) -> dict:
    square_instances: list[dict[str, int]] = []
    cube_instances: list[dict[str, int]] = []
    root_count = 0
    value_count = 0
    prime_count = 0
    for prime in primes_below(prime_bound):
        prime_count += 1
        modulus = prime**3
        values = q_mod(2 * prime - 1, modulus)
        value_count += len(values)
        for n, value in enumerate(values):
            if value % prime:
                continue
            root_count += 1
            exponent = truncated_valuation(value, prime, 3)
            if exponent >= 2:
                square_instances.append(
                    {"prime": prime, "n": n, "valuation_at_least": exponent}
                )
            if exponent >= 3:
                cube_instances.append(
                    {"prime": prime, "n": n, "valuation_at_least": exponent}
                )

    assert square_instances == [
        {"prime": 13, "n": 8, "valuation_at_least": 2}
    ]
    assert cube_instances == []
    return {
        "prime_bound_exclusive": prime_bound,
        "prime_count": prime_count,
        "value_count": value_count,
        "root_count": root_count,
        "square_instances": square_instances,
        "cube_or_higher_instances": cube_instances,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mahler-prime-bound", type=int, default=50)
    parser.add_argument("--identity-prime-bound", type=int, default=500)
    parser.add_argument("--identity-index-multiplier", type=int, default=5)
    parser.add_argument("--fibre-prime-bound", type=int, default=2000)
    parser.add_argument("--translate-count", type=int, default=10)
    parser.add_argument("--window-prime-bound", type=int, default=10_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.json"
        ),
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    dependencies = check_dependencies(repo)
    mahler = check_mahler_initial_values(args.mahler_prime_bound)
    fourth = check_fourth_antiperiod(
        args.identity_prime_bound, args.identity_index_multiplier
    )
    fibres = check_cubic_root_fibres(
        args.fibre_prime_bound, args.translate_count
    )
    window = finite_large_prime_scan(args.window_prime_bound)

    exact = q_exact(8)
    assert exact[8] == 13**2 * 1846921
    assert all(
        1846921 % divisor
        for divisor in range(2, math.isqrt(1846921) + 1)
    )

    result = {
        "description": (
            "Deterministic exact replay for the fourth anti-period congruence, "
            "cubic Newton root-fibre law, and finite large-prime diagnostic."
        ),
        "frozen_dependencies": dependencies,
        "mahler_initial_value_checks": mahler,
        "fourth_antiperiod_grid": fourth,
        "cubic_root_fibre_grid": fibres,
        "finite_large_prime_window": window,
        "sharp_square_example": {
            "prime": 13,
            "n": 8,
            "q_n": exact[8],
            "factorization": {"13": 2, "1846921": 1},
        },
        "scope_warning": (
            "The fourth anti-period and cubic fibre laws are proved symbolically "
            "in the source. The p<10000 statement that q_8 is the sole square "
            "and that no cube occurs is finite evidence only. No uniform upper "
            "bound on the exceptional p-adic valuation is claimed. The replay "
            "records zero qualifying singular all-square reflection pairs, so "
            "the reflection/full-fibre theorem is symbolic rather than an "
            "extrapolation from tested examples."
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
