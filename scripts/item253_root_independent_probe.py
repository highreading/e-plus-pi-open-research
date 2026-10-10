#!/usr/bin/env python3
"""Independent root audit for Item 253; standard library only."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def qpoly(delta: int, m: int) -> int:
    return 28 * m * m + (21 * delta + 25) * m + 4 * delta * delta + 9 * delta + 5


def b_integer(delta: int, m: int) -> int:
    n = 3 * m + delta
    return sum((-1) ** k * math.comb(n, k) * 2 ** (n - k) for k in range(m + 1)) - 1


def increment_closed(delta: int, m: int) -> int:
    numerator = (
        (-1) ** (m + 1)
        * 2 ** (2 * m + delta)
        * math.comb(3 * m + delta, m)
        * qpoly(delta, m)
    )
    denominator = (m + 1) * (2 * m + delta + 1)
    assert numerator % denominator == 0
    return numerator // denominator


def h_prefix(m: int, p: int) -> int:
    term = total = 1
    for k in range(m):
        term = term * (2 * k + 1) * pow(4 * (k + 1), -1, p) % p
        total = (total + term) % p
    return total


def k_phase(delta: int, m: int, p: int) -> int:
    n = 3 * m + delta
    minus_half = -pow(2, -1, p) % p
    return sum(math.comb(n, k) * pow(minus_half, k, p) for k in range(m + 1)) % p


def actual_rows(bound: int):
    for p in range(11, bound + 1):
        if not is_prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r % 2 == 1 and r % 3:
                yield p, r, s, s - 1, r + 4


def cartier_check(p: int) -> None:
    n = (p - 1) // 2
    epsilon = pow(2, n, p)
    term = total = 1
    hs = [1]
    for k in range(1, n + 1):
        term = term * (2 * k - 1) * pow(4 * k, -1, p) % p
        total = (total + term) % p
        hs.append(total)
    left = [0] * (n + 2)
    for k, value in enumerate(hs):
        left[k] = (left[k] + value) % p
        left[k + 1] = (left[k + 1] - value) % p
    right = [0] * (n + 2)
    minus_half = -pow(2, -1, p) % p
    for k in range(n + 1):
        right[k] = math.comb(n, k) * pow(minus_half, k, p) % p
    right[n + 1] = -epsilon % p
    assert left == right
    assert sum(hs) % p == 0


def main() -> None:
    exact_increment_checks = 0
    for delta in range(3, 32, 2):
        for m in range(13):
            assert b_integer(delta, m + 1) - b_integer(delta, m) == increment_closed(delta, m)
            exact_increment_checks += 1

    rows = []
    terminal_zeros = 0
    h_zeros = 0
    for p, r, s, m, delta in actual_rows(401):
        assert p == 6 * m + 2 * delta + 1
        h = h_prefix(m, p)
        k = k_phase(delta, m, p)
        assert h == k
        epsilon = pow(2, (p - 1) // 2, p)
        b = b_integer(delta, m) % p
        assert h == epsilon * (b + 1) % p
        q = qpoly(delta, m)
        assert 2 * q - (2 * m * m - m + 3) == p * (4 * delta + 9 * m + 7)
        assert 18 * q - (2 * delta * delta + 5 * delta + 29) == p * (35 * delta + 84 * m + 61)
        assert 2 * delta * delta + 5 * delta + 29 == 2 * r * r + 21 * r + 81
        dzero = increment_closed(delta, m) % p == 0
        assert dzero == (q % p == 0) == ((2 * r * r + 21 * r + 81) % p == 0)
        terminal_zeros += dzero
        h_zeros += h == 0
        rows.append((p, r, s, m, delta, h, b, q % p, int(dzero)))

    for p in range(5, 102):
        if is_prime(p):
            cartier_check(p)

    h43 = next(row for row in rows if row[:3] == (43, 11, 3))
    d127 = next(row for row in rows if row[:3] == (127, 17, 15))
    assert h43[5] == 0 and h43[8] == 0
    assert d127[5] == 109 and d127[8] == 1
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    result = {
        "schema": "item253-root-independent-probe-v1",
        "imports_item_code": False,
        "exact_increment_checks": exact_increment_checks,
        "actual_rows_through_p_401": len(rows),
        "phase_equalities": len(rows),
        "terminal_zero_count_EXACT_FINITE_ONLY": terminal_zeros,
        "H_zero_count_EXACT_FINITE_ONLY": h_zeros,
        "cartier_primes_through_101": sum(is_prime(p) for p in range(5, 102)),
        "separation_witnesses": {
            "H_zero_terminal_nonzero": [43, 11, 3],
            "terminal_zero_H_nonzero": [127, 17, 15],
        },
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "independent exact implementation and bounded replay; no density, capacity, or rate inference",
    }
    (HERE.parent / "results" / "item253_root_independent_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
