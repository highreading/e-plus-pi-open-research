#!/usr/bin/env python3
"""Exact replay for the Bessel large-prime four-point theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


DEPENDENCIES = {
    "sources/bessel_denominator_zero_gap_smooth_radical_barrier.md": (
        "dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc"
    ),
    "sources/bessel_denominator_all_lift_branching_wieferich_barrier.md": (
        "f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


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
    return [index for index, is_prime in enumerate(sieve) if is_prime]


def q_sequence_mod(limit: int, modulus: int) -> list[int]:
    if limit == 0:
        return [1 % modulus]
    values = [1 % modulus, 1 % modulus]
    for n in range(2, limit + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values


def q_sequence_exact(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def truncated_valuation(residue: int, prime: int, cap: int) -> int:
    """Return min(v_p(residue), cap), with residue known modulo p**cap."""
    if residue == 0:
        return cap
    exponent = 0
    while exponent < cap and residue % prime == 0:
        residue //= prime
        exponent += 1
    return exponent


def check_frozen_dependencies(repo: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(repo / relative)
        assert actual == expected, (relative, expected, actual)
        observed[relative] = actual
    return observed


def check_universal_congruences(identity_bound: int) -> dict[str, int]:
    anti_period_checks = 0
    second_difference_checks = 0
    reflection_checks = 0
    for prime in primes_below(identity_bound):
        if prime == 2:
            continue

        modulus = prime * prime
        short = q_sequence_mod(4 * prime, modulus)
        for n in range(0, 3 * prime + 1):
            assert (short[n + prime] + short[n]) % prime == 0
            anti_period_checks += 1
        for n in range(0, 2 * prime + 1):
            left = short[n + 2 * prime] + 2 * short[n + prime] + short[n]
            right = 2 * prime * short[n]
            assert (left - right) % modulus == 0
            second_difference_checks += 1

        reflected = q_sequence_mod(modulus - 1, modulus)
        for u in range(modulus):
            assert reflected[modulus - 1 - u] == reflected[u]
            reflection_checks += 1

    return {
        "anti_period_checks": anti_period_checks,
        "second_difference_checks": second_difference_checks,
        "reflection_checks": reflection_checks,
    }


def scan_large_prime_window(scan_bound: int, valuation_cap: int) -> dict:
    assert valuation_cap >= 3
    prime_count = 0
    window_value_count = 0
    divisible_value_count = 0
    orbit_count = 0
    ordinary_orbit_count = 0
    singular_orbit_count = 0
    central_orbit_count = 0
    quotient_table_checks = 0
    exclusivity_checks = 0
    square_instances: list[dict[str, int]] = []
    cube_or_higher_instances: list[dict[str, int]] = []
    max_truncated_valuation = 0
    singular_orbits: list[dict[str, int | str]] = []

    for prime in primes_below(scan_bound):
        prime_count += 1
        modulus = prime**valuation_cap
        values = q_sequence_mod(2 * prime - 1, modulus)
        window_value_count += len(values)

        divisible_indices = [
            n for n, value in enumerate(values) if value % prime == 0
        ]
        divisible_value_count += len(divisible_indices)

        if prime in (2, 3):
            assert not divisible_indices
            continue

        covered: set[int] = set()
        midpoint = (prime - 1) // 2
        for r in range(midpoint + 1):
            if values[r] % prime:
                continue
            s = prime - 1 - r
            indices = sorted({r, s, r + prime, s + prime})
            covered.update(indices)
            orbit_count += 1

            c = (values[r] // prime) % prime
            delta_numerator = -values[r + prime] - values[r]
            assert delta_numerator % prime == 0
            delta = (delta_numerator // prime) % prime

            delta_s_numerator = -values[s + prime] - values[s]
            assert delta_s_numerator % prime == 0
            delta_s = (delta_s_numerator // prime) % prime
            assert delta_s == (-delta) % prime
            assert (values[s] - values[r] + prime * delta) % (prime * prime) == 0

            observed = [
                (values[r] // prime) % prime,
                (values[s] // prime) % prime,
                (values[r + prime] // prime) % prime,
                (values[s + prime] // prime) % prime,
            ]
            expected = [
                c,
                (c - delta) % prime,
                (-c - delta) % prime,
                (-c + 2 * delta) % prime,
            ]
            assert observed == expected
            quotient_table_checks += 1

            zero_count = sum(entry == 0 for entry in observed)
            if r == s:
                central_orbit_count += 1
                singular_orbit_count += 1
                assert delta == 0
                assert observed[0] == c
                assert observed[2] == (-c) % prime
                # The four-entry table repeats each of the two actual values.
                assert zero_count in (0, 4)
                singular_orbits.append(
                    {
                        "prime": prime,
                        "r": r,
                        "s": s,
                        "kind": "central",
                        "c": c,
                        "delta": delta,
                        "square_threshold_crossed": int(c == 0),
                    }
                )
            elif delta:
                ordinary_orbit_count += 1
                assert zero_count <= 1
            else:
                singular_orbit_count += 1
                assert zero_count in (0, 4)
                singular_orbits.append(
                    {
                        "prime": prime,
                        "r": r,
                        "s": s,
                        "kind": "noncentral",
                        "c": c,
                        "delta": delta,
                        "square_threshold_crossed": int(c == 0),
                    }
                )
            exclusivity_checks += 1

        assert covered == set(divisible_indices)

        for n in divisible_indices:
            exponent = truncated_valuation(values[n], prime, valuation_cap)
            max_truncated_valuation = max(max_truncated_valuation, exponent)
            if exponent >= 2:
                square_instances.append(
                    {"prime": prime, "n": n, "valuation_at_least": exponent}
                )
            if exponent >= 3:
                cube_or_higher_instances.append(
                    {"prime": prime, "n": n, "valuation_at_least": exponent}
                )

    return {
        "scan_bound_exclusive": scan_bound,
        "valuation_cap": valuation_cap,
        "prime_count": prime_count,
        "window_value_count": window_value_count,
        "divisible_value_count": divisible_value_count,
        "orbit_count": orbit_count,
        "ordinary_orbit_count": ordinary_orbit_count,
        "singular_orbit_count": singular_orbit_count,
        "central_orbit_count": central_orbit_count,
        "quotient_table_checks": quotient_table_checks,
        "exclusivity_checks": exclusivity_checks,
        "max_truncated_valuation": max_truncated_valuation,
        "square_instances": square_instances,
        "cube_or_higher_instances": cube_or_higher_instances,
        "singular_orbits": singular_orbits,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-bound", type=int, default=10_000)
    parser.add_argument("--identity-bound", type=int, default=200)
    parser.add_argument("--valuation-cap", type=int, default=4)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/bessel_large_prime_four_point_exclusivity_certificate.json"
        ),
    )
    args = parser.parse_args()
    assert args.scan_bound >= 5
    assert args.identity_bound >= 5

    repo = Path(__file__).resolve().parents[1]
    dependencies = check_frozen_dependencies(repo)
    universal = check_universal_congruences(args.identity_bound)
    scan = scan_large_prime_window(args.scan_bound, args.valuation_cap)

    exact = q_sequence_exact(21)
    assert exact[4] == 1001
    assert exact[8] == 312129649 == 13**2 * 1846921
    example_delta = ((-exact[17] - exact[4]) // 13) % 13
    assert example_delta == 12
    assert (exact[4] // 13) % 13 == 12
    assert (exact[8] // 13) % 13 == 0

    assert scan["square_instances"] == [
        {"prime": 13, "n": 8, "valuation_at_least": 2}
    ]
    assert scan["cube_or_higher_instances"] == []

    result = {
        "description": (
            "Exact replay for the all-prime four-point quotient theorem in "
            "the full p>n/2 window, plus an explicitly finite diagnostic scan."
        ),
        "frozen_dependencies": dependencies,
        "universal_congruence_grid": {
            "prime_bound_exclusive": args.identity_bound,
            **universal,
        },
        "finite_window_scan": scan,
        "sharp_example": {
            "prime": 13,
            "r": 4,
            "s": 8,
            "c": 12,
            "delta": example_delta,
            "q_4": exact[4],
            "q_8": exact[8],
            "q_8_factorization": {"13": 2, "1846921": 1},
        },
        "scope_warning": (
            "The symbolic theorem proves at most one square-threshold crossing "
            "per ordinary four-point orbit and an all-or-none singular dichotomy. "
            "It gives no upper bound for the exceptional valuation. The claim "
            "that (13,8) is the sole square and that no cube occurs is finite "
            "evidence only for primes below the recorded scan bound."
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
