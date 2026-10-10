#!/usr/bin/env python3
"""Independent exact probe for Item 262; imports no Item-262 code."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def valuation_int(n: int, prime: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("valuation of zero")
    value = 0
    while n % prime == 0:
        n //= prime
        value += 1
    return value


def valuation_fraction(x: Fraction, prime: int) -> int:
    return valuation_int(x.numerator, prime) - valuation_int(x.denominator, prime)


def prime_factors(n: int) -> set[int]:
    n = abs(n)
    factors: set[int] = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.add(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.add(n)
    return factors


def primes_upto(bound: int) -> list[int]:
    sieve = [True] * (bound + 1)
    sieve[:2] = [False, False]
    for n in range(2, int(bound**0.5) + 1):
        if sieve[n]:
            sieve[n * n : bound + 1 : n] = [False] * (((bound - n * n) // n) + 1)
    return [n for n, ok in enumerate(sieve) if ok]


def inv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def frac_mod(x: Fraction, p: int) -> int:
    assert x.denominator % p
    return x.numerator % p * inv(x.denominator, p) % p


def h_table(p: int, end: int) -> tuple[list[int], list[int]]:
    h, H = [1], [1]
    for j in range(end):
        h.append(h[-1] * (2 * j + 1) * inv(4 * (j + 1), p) % p)
        H.append((H[-1] + h[-1]) % p)
    return h, H


def shifted_sum(a: int, count: int, p: int) -> int:
    term = 1
    total = 0
    half = inv(2, p)
    for k in range(1, count + 1):
        term = term * half % p
        term = term * (a + k - 1) % p
        term = term * inv(half + k - 1, p) % p
        total = (total + term) % p
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--delta-bound", type=int, default=127)
    parser.add_argument("--prime-bound", type=int, default=401)
    args = parser.parse_args()

    c = [Fraction(1)]
    for j in range(args.delta_bound + 2):
        c.append(c[-1] * Fraction(6 * j + 5, 3 * j + 4))
    K = [Fraction(0)]
    for delta in range(1, args.delta_bound + 3):
        K.append(K[-1] + c[delta - 1])

    recurrence_checks = 0
    for delta in range(args.delta_bound):
        lhs = (3 * delta + 4) * K[delta + 2]
        lhs -= 9 * (delta + 1) * K[delta + 1]
        lhs += (6 * delta + 5) * K[delta]
        assert lhs == 0
        recurrence_checks += 1

    odd_recurrence_checks = 0
    for N in range(1, (args.delta_bound - 1) // 2):
        Lm, L0, Lp = K[2 * N - 1], K[2 * N + 1], K[2 * N + 3]
        astar = (12 * N - 1) * (12 * N + 5) * (N + 1)
        bstar = (6 * N + 4) * (6 * N + 7) * N
        assert bstar * Lp - (astar + bstar) * L0 + astar * Lm == 0
        odd_recurrence_checks += 1

    valuation_checks = 0
    denominator_support_checks = 0
    gcd_checks = 0
    R = [Fraction(1)]
    for j in range(2 * ((args.delta_bound - 1) // 2) + 1):
        R.append(1 + Fraction(3 * j + 4, 6 * j + 5) * R[-1])
        assert R[-1] == K[j + 2] / c[j + 1]

    for delta in range(1, args.delta_bound + 1):
        factors = prime_factors(K[delta].denominator)
        assert not factors or max(factors) <= max(1, 3 * delta - 2)
        denominator_support_checks += 1
        if delta % 2:
            assert frac_mod(K[delta], 3) == 1
            assert valuation_fraction(K[delta], 3) == 0
            N = (delta - 1) // 2
            A = N + sum(valuation_int(3 * u + 2, 2) for u in range(N))
            assert valuation_fraction(K[delta], 2) == -A + valuation_fraction(R[2 * N], 2)
            if N % 2 == 1:
                assert valuation_fraction(R[2 * N], 2) == 1
            elif N > 0 and N % 4 == 0:
                assert valuation_fraction(R[2 * N], 2) == 2
            elif N % 4 == 2:
                assert valuation_fraction(R[2 * N], 2) >= 3
            valuation_checks += 1
        elif delta >= 2:
            N = delta // 2
            A = N + sum(valuation_int(3 * u + 2, 2) for u in range(N))
            assert valuation_fraction(K[delta], 2) == -A
            valuation_checks += 1
        if delta + 2 <= args.delta_bound:
            common = math.gcd(abs(K[delta].numerator), abs(K[delta + 2].numerator))
            assert all(prime <= 6 * delta + 5 for prime in prime_factors(common))
            gcd_checks += 1

    actual_rows = []
    zero_rows = []
    localization_checks = 0
    for p in primes_upto(args.prime_bound):
        if p < 5 or p % 6 != 5:
            continue
        q = (p - 5) // 6
        h, H = h_table(p, q + 1)
        eps = pow(2, (p - 1) // 2, p)
        for s in range(1, q + 1):
            r = (p - 6 * s - 3) // 2
            if r <= 0 or r % 2 == 0:
                continue
            assert r % 3 == 1
            delta = (r + 2) // 3
            m = s - 1
            assert delta % 2 == 1 and m == q - delta
            kmod = frac_mod(K[delta], p)
            cmod = frac_mod(c[delta], p)
            assert H[m] == (H[q] - kmod * h[q]) % p
            assert h[m] == cmod * h[q] % p
            a_actual = (m + inv(2, p)) % p
            a_fixed = (-delta - inv(3, p)) % p
            P = shifted_sum(a_actual, 3 * delta, p)
            Pi = shifted_sum(a_fixed, 3 * delta, p)
            assert P == Pi
            D = (kmod + cmod * Pi) % p
            old_pair = (H[m] - h[m] * P) % p
            new_pair = (H[q] - D * h[q]) % p
            assert old_pair == new_pair
            A_old = (pow(-1, m, p) * (eps * old_pair - 1)) % p
            A_new = (pow(-1, m, p) * (eps * new_pair - 1)) % p
            assert A_old == A_new
            row = (p, r, s, m, delta, H[m], kmod, A_new)
            actual_rows.append(row)
            if H[m] == 0 or kmod == 0:
                zero_rows.append(row)
            localization_checks += 4

    row47 = next(row for row in actual_rows if row[:5] == (47, 7, 5, 4, 3))
    row59 = next(row for row in actual_rows if row[:5] == (59, 7, 7, 6, 3))
    assert row47[5:7] == (0, 21)
    assert row59[5:7] == (57, 0)
    assert K[3] == Fraction(59, 14)
    assert K[5] == Fraction(175, 13)
    assert K[7] == Fraction(4857283, 110656)
    assert 4857283 == 521 * 9323

    digest = hashlib.sha256(
        json.dumps(actual_rows, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    payload = {
        "schema": "item262-root-independent-probe-v1",
        "delta_bound": args.delta_bound,
        "prime_bound": args.prime_bound,
        "recurrence_checks": recurrence_checks,
        "odd_recurrence_checks": odd_recurrence_checks,
        "valuation_checks": valuation_checks,
        "denominator_support_checks": denominator_support_checks,
        "numerator_gcd_checks": gcd_checks,
        "actual_p5_rows": len(actual_rows),
        "localization_equalities": localization_checks,
        "zero_or_boundary_rows": zero_rows,
        "actual_rows_digest_sha256": digest,
        "proof_audit": [
            "The pole-orbit arguments exclude rational order-one antidifferences; finite checks are not used for minimality.",
            "The recurrence forces the all-delta numerator-gcd bound after a large-prime unit audit.",
            "The O(delta) height summed over moving delta is O(M^2), so it gives no linear-capacity reduction.",
        ],
        "label": "EXACT FINITE independent replay supporting separately proved symbolic and height theorems",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
