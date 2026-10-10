#!/usr/bin/env python3
"""Independent standard-library probe for Item 263.

This does not import or call the Item-263 certificate.  It reconstructs the
Cartier-selected quotient coefficients, compact coefficients, endpoint
non-descent identities, cutoff identities, and named witnesses directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def primes_upto(bound: int) -> list[int]:
    sieve = [True] * (bound + 1)
    sieve[:2] = [False, False]
    for n in range(2, int(bound**0.5) + 1):
        if sieve[n]:
            sieve[n * n : bound + 1 : n] = [False] * (((bound - n * n) // n) + 1)
    return [n for n, ok in enumerate(sieve) if ok]


def inv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def eps2(p: int) -> int:
    return pow(2, (p - 1) // 2, p)


def half_binomial_table(p: int, end: int) -> tuple[list[int], list[int]]:
    h = [1]
    H = [1]
    for j in range(end):
        nxt = h[-1] * (2 * j + 1) * inv(4 * (j + 1), p) % p
        h.append(nxt)
        H.append((H[-1] + nxt) % p)
    return h, H


def quotient_coefficients(p: int) -> list[int]:
    """Q where (v-1/2)^n-(1/2)^n=(v-1)Q, ascending coefficients."""
    n = (p - 1) // 2
    half = inv(2, p)
    coeff = [math.comb(n, k) * pow(-half, n - k, p) % p for k in range(n + 1)]
    coeff[0] = (coeff[0] - pow(half, n, p)) % p
    qcoeff = [0] * n
    qcoeff[-1] = coeff[-1]
    for k in range(n - 1, 0, -1):
        qcoeff[k - 1] = (coeff[k] + qcoeff[k]) % p
    assert (-qcoeff[0]) % p == coeff[0]
    for k in range(1, n):
        assert (qcoeff[k - 1] - qcoeff[k]) % p == coeff[k]
    return qcoeff


def cutoff_coefficients(p: int, delta: int) -> list[int]:
    if p % 6 == 1:
        num_shift, den_shift = 1, 2
    else:
        num_shift, den_shift = 5, 4
    c = [1]
    for j in range(delta):
        c.append(c[-1] * (6 * j + num_shift) * inv(3 * j + den_shift, p) % p)
    return c


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--prime-bound", type=int, default=401)
    args = parser.parse_args()

    cartier_rows = []
    endpoint_rows = []
    cutoff_rows = []
    zero_rows = []

    for p in primes_upto(args.prime_bound):
        if p < 5:
            continue
        q = (p - 1) // 6 if p % 6 == 1 else (p - 5) // 6
        h, H = half_binomial_table(p, q + 2)
        eps = eps2(p)
        qcoeff = quotient_coefficients(p)

        if p % 6 == 1:
            selected = qcoeff[2 * q]
            expected = H[q - 1]
            compact_eta = math.comb(3 * q, 2 * q) * pow(-inv(2, p), q, p) % p
            assert selected == expected
            assert compact_eta == h[q]
            if q >= 2:
                d0 = (-3 * h[q + 1] * inv(-2, p) - eps * (-1) * inv(6, p)) % p
                d1 = (-3 * h[q] * inv(4, p) - eps * 2 * inv(6, p)) % p
                assert (30 * d0 + 12 * d1) % p == eps
                endpoint_rows.append((p, d0, d1))
            lam = (H[q] - h[q]) % p
            characteristic = [0, eps, eps, eps, h[q]]
        else:
            selected = qcoeff[2 * q + 1]
            expected = H[q]
            compact_xi = math.comb(3 * q + 2, 2 * q + 1) * pow(-inv(2, p), q + 1, p) % p
            assert selected == expected
            assert compact_xi == (-h[q]) % p
            assert (-eps) % p != 0
            endpoint_rows.append((p, (-eps) % p))
            lam = H[q]
            characteristic = [0, 0, eps, 1, -1]

        cartier_rows.append((p, p % 6, selected, expected, h[q], lam, characteristic))

        max_s = (p - 3) // 6
        for s in range(1, max_s + 1):
            r_num = p - 6 * s - 3
            if r_num <= 0 or r_num % 2:
                continue
            r = r_num // 2
            # The actual ordinary-j=2 phase has odd r (equivalently odd delta).
            if r % 2 == 0:
                continue
            m = s - 1
            delta = (r + 4) // 3 if p % 6 == 1 else (r + 2) // 3
            assert m == q - delta
            c = cutoff_coefficients(p, delta)
            K = sum(c[:delta]) % p
            assert h[m] == h[q] * c[delta] % p
            assert H[m] == (H[q] - K * h[q]) % p
            cutoff_rows.append((p, r, s, m, delta, H[m], K, c[delta]))
            if H[m] == 0:
                zero_rows.append((p, r, s, m, delta))

    assert next(row for row in cartier_rows if row[0] == 19)[4:6] == (18, 15)
    row83 = next(row for row in cartier_rows if row[0] == 83)
    assert row83[3] == 0 and row83[4] == 22
    assert (43, 11, 3, 2, 5) in zero_rows
    assert (47, 7, 5, 4, 3) in zero_rows

    digest_input = json.dumps(
        {"cartier": cartier_rows, "endpoint": endpoint_rows, "cutoff": cutoff_rows},
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    payload = {
        "schema": "item263-root-independent-probe-v1",
        "prime_bound": args.prime_bound,
        "cartier_prime_rows": len(cartier_rows),
        "endpoint_nondescend_rows": len(endpoint_rows),
        "actual_cutoff_rows": len(cutoff_rows),
        "actual_prefix_zero_rows": zero_rows,
        "digest_sha256": hashlib.sha256(digest_input).hexdigest(),
        "checks": [
            "independent quotient construction and Cartier coefficient selection",
            "compact eta/xi coefficients",
            "all-prime endpoint non-descent identities in the tested range",
            "actual cutoff and h_m/h_q identities",
            "p=19, p=83, p=43, and p=47 named witnesses",
        ],
        "label": "EXACT FINITE independent replay of formulas supporting the all-row symbolic proofs",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
