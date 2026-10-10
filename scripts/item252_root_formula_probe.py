#!/usr/bin/env python3
"""Dependency-free root probe of Item 252's half-binomial localization."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def rising(x: F, n: int) -> F:
    out = F(1)
    for j in range(n):
        out *= x + j
    return out


def fmod(x: F, p: int) -> int:
    assert x.denominator % p
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def a_direct(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def h_term(j: int) -> F:
    return rising(F(1, 2), j) / (math.factorial(j) * 2**j)


def contiguous_lhs(m: int, d: int) -> F:
    return sum(
        rising(F(d, 1) + F(1, 2), j) / (math.factorial(j) * 2**j)
        for j in range(m + 1)
    ) / 2**d


def contiguous_rhs(m: int, d: int) -> F:
    h_m = h_term(m)
    h_prefix = sum((h_term(j) for j in range(m + 1)), F(0))
    correction = sum(
        rising(F(m, 1) + F(1, 2), k) / (rising(F(1, 2), k) * 2**k)
        for k in range(1, d + 1)
    )
    return h_prefix - h_m * correction


def localized_a(p: int, s: int, r: int) -> int:
    m, d = s - 1, r + 2
    assert 2 * d - 1 == p - 6 * s < p
    assert 2 * m + 2 * d - 1 == 2 * s + 2 * r + 1 < p
    h_m = fmod(h_term(m), p)
    h_prefix = sum(fmod(h_term(j), p) for j in range(m + 1)) % p
    correction = sum(
        fmod(rising(F(m, 1) + F(1, 2), k) / rising(F(1, 2), k), p)
        * pow(pow(2, k, p), -1, p)
        for k in range(1, d + 1)
    ) % p
    eps = pow(2, (p - 1) // 2, p)
    assert eps in (1, p - 1)
    return ((-1) ** m * (eps * (h_prefix - h_m * correction) - 1)) % p


def actual_rows(bound: int):
    for p in range(11, bound + 1):
        if not is_prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            r = (p - 6 * s - 3) // 2
            yield p, s, r


def main() -> None:
    contiguous_checks = 0
    for m in range(21):
        for d in range(1, 18):
            assert contiguous_lhs(m, d) == contiguous_rhs(m, d)
            contiguous_checks += 1

    rows = []
    for p, s, r in actual_rows(401):
        direct = a_direct(s) % p
        localized = localized_a(p, s, r)
        assert direct == localized, (p, s, r, direct, localized)
        rows.append((p, s, r, direct))
    assert len(rows) == 1153
    assert next(row for row in rows if row[:3] == (31, 3, 5))[3] == 0

    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    result = {
        "schema": "item252-root-formula-probe-v1",
        "imports_item_code": False,
        "contiguous_exact_fraction_checks": contiguous_checks,
        "prime_max_inclusive": 401,
        "actual_rows": len(rows),
        "localized_A_equalities": len(rows),
        "first_scalar_zero": [31, 3, 5],
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "exact formula implementation and bounded replay; no all-prime nonvanishing or rate",
    }
    (HERE / "item252_root_formula_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
