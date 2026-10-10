#!/usr/bin/env python3
"""Independent exact/modular probe of Item 251's surviving-period formula."""

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


def a_value(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def beta(s: int) -> F:
    return F(math.factorial(2 * s - 1) * math.factorial(s - 1), math.factorial(3 * s - 1))


def factorial_tail(s: int, h: int) -> F:
    return F(
        (-1) ** (s + h) * math.factorial(2 * s) * math.factorial(s + h),
        math.factorial(3 * s + h + 1),
    )


def tau(s: int, h: int) -> F:
    return F((-1) ** (s + h) * 2, 3) * rising(F(s), h + 1) / rising(F(3 * s + 1), h + 1)


def kappa(r: int) -> F:
    h = (r - 1) // 2
    return (
        F(2 * (4 * h + 5), 9 * (4 * h + 3))
        * (-1) ** h
        * rising(F(5 - 2 * h, 6), h)
        / rising(F(h, 1) + F(3, 2), h)
    )


def actual_rows(bound: int):
    for p in range(11, bound + 1):
        if not is_prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            yield p, s, (p - 6 * s - 3) // 2


def main() -> None:
    exact_tail_checks = 0
    for s in range(1, 21):
        for h in range(11):
            assert factorial_tail(s, h) == beta(s) * tau(s, h)
            exact_tail_checks += 1

    a_cache: dict[int, int] = {}
    rows = []
    for p, s, r in actual_rows(401):
        h = (r - 1) // 2
        a = a_cache.setdefault(s, a_value(s))
        bmod = fmod(beta(s), p)
        taumod = fmod(tau(s, h), p)
        f_direct = fmod(factorial_tail(s, h), p)
        assert f_direct == bmod * taumod % p

        q = 2 * s
        e_direct = sum(
            math.comb(q - 1, j) * pow(q + 2 * j, -1, p)
            for j in range(q)
        ) % p
        e_from_a = bmod * (a % p) * pow(2, -1, p) % p
        assert e_direct == e_from_a
        kap = fmod(kappa(r), p)
        z_direct = (9 * kap * e_direct - f_direct) % p
        z_normalized = bmod * ((9 * kap * (a % p) * pow(2, -1, p) - taumod) % p) % p
        assert z_direct == z_normalized
        rows.append((p, s, r, a % p, z_direct))

    assert len(rows) == 1153
    assert a_value(3) == 1023 == 33 * 31
    delta4 = a_value(4) + a_value(5)
    assert delta4 == 577280 == 14080 * 41
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    result = {
        "schema": "item251-root-period-probe-v1",
        "imports_item_code": False,
        "exact_tail_ratio_checks": exact_tail_checks,
        "prime_max_inclusive": 401,
        "actual_rows": len(rows),
        "beta_e_tail_Z_equalities_per_row": 3,
        "scalar_counterexamples": {"A_3": 1023, "Delta_4": 577280},
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "period normalization only; no gate nonvanishing, density, or rate",
    }
    (HERE / "item251_root_period_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
