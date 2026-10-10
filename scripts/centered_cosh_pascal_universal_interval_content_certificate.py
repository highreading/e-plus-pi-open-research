#!/usr/bin/env python3
"""Exact replay for the universal upper-prime interval in Pascal content.

The all-parameter proof is symbolic.  This certificate independently checks
its Euler congruences, reduced-border identity, Lucas edge cases, and endpoint
divisibility on finite declared grids.  No finite row is extrapolated.
"""

from __future__ import annotations

import hashlib
import json
import math
import resource
from pathlib import Path

from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/centered_cosh_pascal_universal_interval_content_certificate.json"
SCHEMA = "centered_cosh_pascal_universal_interval_content_certificate/v1"
Q_MAX = 40
PRIME_MAX = 61
CONGRUENCE_N_MAX = 80
RSS_GUARD_KIB = 2 * 1024 * 1024


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for value in range(2, math.isqrt(limit) + 1):
        if sieve[value]:
            sieve[value * value : limit + 1 : value] = b"\x00" * (
                (limit - value * value) // value + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def sha256_int(value: int) -> str:
    return hashlib.sha256(str(value).encode("ascii")).hexdigest()


def vector_content(values: list[int]) -> int:
    out = 0
    for value in values:
        out = math.gcd(out, abs(value))
    return out


def secant_numbers(limit: int) -> list[int]:
    """Return U_n=|E_{2n}| by exact factorial-basis inversion."""
    out = [1]
    for n in range(1, limit + 1):
        value = -sum(
            (-1) ** j * math.comb(2 * n, 2 * j) * out[n - j]
            for j in range(1, n + 1)
        )
        assert value > 0
        out.append(value)
    return out


def square_secant_numbers(values: list[int]) -> list[int]:
    return [
        sum(
            math.comb(2 * n, 2 * j) * values[j] * values[n - j]
            for j in range(n + 1)
        )
        for n in range(len(values))
    ]


def primitive_pascal_kernel(q: int) -> tuple[list[int], list[int]]:
    matrix = [
        [
            (-1 if i % 2 else 1) * math.comb(2 * (q + r), 2 * i)
            for i in range(q + 1)
        ]
        for r in range(1, q + 1)
    ]
    basis, nullity = fmpz_mat(matrix).nullspace()
    assert nullity == 1
    d = [int(basis[i, 0]) for i in range(q + 1)]
    content = vector_content(d)
    assert content
    d = [value // content for value in d]
    if d[0] < 0:
        d = [-value for value in d]
    assert vector_content(d) == 1
    assert all(value > 0 for value in d)
    assert all(sum(row[i] * d[i] for i in range(q + 1)) == 0 for row in matrix)
    e = [
        sum(
            (-1) ** (k - i) * math.comb(2 * k, 2 * i) * d[i]
            for i in range(k + 1)
        )
        for k in range(q + 1)
    ]
    assert e[0] == d[0]
    return d, e


def endpoint_w(
    q: int,
    m: int,
    d: list[int],
    e: list[int],
    u_values: list[int],
    t_values: list[int],
) -> int:
    return 2 * sum(
        math.comb(2 * m, 2 * i) * d[i] * u_values[m - i]
        for i in range(q + 1)
    ) - sum(
        math.comb(2 * m, 2 * k) * e[k] * t_values[m - k]
        for k in range(q + 1)
    )


def reduced_border(
    q: int,
    r: int,
    d: list[int],
    e: list[int],
    u_values: list[int],
    t_values: list[int],
) -> int:
    return 2 * sum(
        math.comb(2 * r - 1, 2 * i) * d[i] * u_values[r - i]
        for i in range(min(q, r - 1) + 1)
    ) - sum(
        math.comb(2 * r - 1, 2 * k) * e[k] * t_values[r - k]
        for k in range(min(q, r - 1) + 1)
    )


def valuations_at_primes(value: int, primes: list[int]) -> tuple[dict[str, int], int]:
    value = abs(value)
    result: dict[str, int] = {}
    for prime in primes:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        if exponent:
            result[str(prime)] = exponent
    return result, value


def main() -> None:
    top = max(CONGRUENCE_N_MAX + PRIME_MAX, 4 * Q_MAX + 1)
    u_values = secant_numbers(top)
    t_values = square_secant_numbers(u_values)

    congruence_primes = [prime for prime in primes_up_to(PRIME_MAX) if prime > 2]
    congruence_rows = []
    for prime in congruence_primes:
        h = (prime - 1) // 2
        chi = -1 if h % 2 else 1
        assert (u_values[h] - (chi - 1)) % prime == 0
        assert all(
            (u_values[n + h] - chi * u_values[n]) % prime == 0
            for n in range(1, CONGRUENCE_N_MAX + 1)
        )
        assert all(
            (t_values[n + h] - chi * t_values[n]) % prime == 0
            for n in range(CONGRUENCE_N_MAX + 1)
        )
        congruence_rows.append(
            {
                "prime": prime,
                "h": h,
                "chi": chi,
                "U_h_mod_prime": u_values[h] % prime,
            }
        )

    rows = []
    for q in range(1, Q_MAX + 1):
        d, e = primitive_pascal_kernel(q)
        assert all(
            reduced_border(q, r, d, e, u_values, t_values) == 0
            for r in range(1, 2 * q + 2)
        )

        w_even = endpoint_w(q, 4 * q, d, e, u_values, t_values)
        w_odd = endpoint_w(q, 4 * q + 1, d, e, u_values, t_values)
        endpoint_scale = (8 * q + 2) * (8 * q + 1)
        content = math.gcd(endpoint_scale * w_even, w_odd)
        interval_primes = [
            prime
            for prime in primes_up_to(8 * q + 2)
            if prime > 4 * q
        ]
        universal_product = math.prod(interval_primes)
        assert content % universal_product == 0
        assert all(w_odd % prime == 0 for prime in interval_primes)
        assert all(
            w_even % prime == 0
            for prime in interval_primes
            if prime <= 8 * q
        )
        assert all(
            endpoint_scale % prime == 0
            for prime in interval_primes
            if prime > 8 * q
        )

        small_primes = primes_up_to(8 * q + 2)
        factorization, residual = valuations_at_primes(content, small_primes)
        quotient = content // universal_product
        rows.append(
            {
                "q": q,
                "interval_primes": interval_primes,
                "universal_product": str(universal_product),
                "G_bits": content.bit_length(),
                "G_sha256": sha256_int(content),
                "exceptional_quotient_bits": quotient.bit_length(),
                "exceptional_quotient_sha256": sha256_int(quotient),
                "small_prime_valuations": factorization,
                "residual_after_primes_le_8q_plus_2": str(residual),
                "midpoint_prime_case": (4 * q + 1) in interval_primes,
                "prefactor_prime_case": (8 * q + 1) in interval_primes,
            }
        )

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB
    payload = {
        "schema": SCHEMA,
        "logical_scope": (
            "Finite exact replay for an all-parameter theorem.  The residual "
            "support and valuations are diagnostics only."
        ),
        "theorem": "product of primes 4q < p <= 8q+2 divides G_q^Pascal",
        "q_grid": [1, Q_MAX],
        "Euler_congruence_prime_grid": [3, PRIME_MAX],
        "Euler_congruence_n_grid": [0, CONGRUENCE_N_MAX],
        "congruence_rows": congruence_rows,
        "rows": rows,
        "rss_guard_kib": RSS_GUARD_KIB,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "q_rows": len(rows),
                "congruence_primes": len(congruence_rows),
                "peak_rss_kib": peak_rss_kib,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
