#!/usr/bin/env python3
"""Independent exact probe for Item 264; imports no Item-264 code."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


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


def rows_by_phase(M: int) -> list[tuple[int, int, int]]:
    rows = []
    for s in range(1, (M - 5) // 4 + 1):
        if (s - M - 1) % 3:
            continue
        p = (4 * M + 2 * s + 1) // 3
        h = (M - 4 * s - 2) // 3
        assert M == 3 * h + 4 * s + 2
        assert p == 4 * h + 6 * s + 3
        if is_prime(p):
            rows.append((p, h, s))
    return rows


def rows_by_interval(M: int) -> list[tuple[int, int, int]]:
    lower = (4 * M + 5) // 3
    upper = (3 * M - 1) // 2
    rows = []
    for p in range(lower, upper + 1):
        if not is_prime(p):
            continue
        s = (3 * p - 4 * M - 1) // 2
        h = 3 * M - 2 * p
        assert s >= 1 and h >= 1
        assert 4 * M + 1 == 3 * p - 2 * s
        assert M == 3 * h + 4 * s + 2
        rows.append((p, h, s))
    return rows


def factorial_data(p: int) -> tuple[list[int], list[int], list[int]]:
    fact = [1] * p
    for n in range(1, p):
        fact[n] = fact[n - 1] * n % p
    ifact = [1] * p
    ifact[p - 1] = pow(fact[p - 1], p - 2, p)
    for n in range(p - 1, 0, -1):
        ifact[n - 1] = ifact[n] * n % p
    inv = [0] * p
    for n in range(1, p):
        inv[n] = fact[n - 1] * ifact[n] % p
    return fact, ifact, inv


def kernel(h: int, extra: int, p: int, fact: list[int], ifact: list[int]) -> list[int]:
    out = []
    for degree in range(2 * h + extra + 1):
        total = 0
        for right in range(extra + 1):
            left = degree - right
            if 0 <= left <= 2 * h:
                choose = fact[2 * h] * ifact[left] * ifact[2 * h - left] % p
                total += math.comb(extra, right) * choose * (-1 if left % 2 else 1)
        out.append(total % p)
    return out


def tail_sum(poly: list[int], a: int, q: int, odd: bool, p: int, inv: list[int]) -> int:
    last = (len(poly) - 2) // 2 if odd else (len(poly) - 1) // 2
    ratio, total = 1, 0
    for t in range(last + 1):
        total = (total + ratio * poly[2 * t + (1 if odd else 0)]) % p
        if t == last:
            break
        numerator = a + t + (1 if odd else 0)
        denominator = q + a + t + (2 if odd else 1)
        assert 0 < denominator < p
        ratio = -ratio * numerator * inv[denominator] % p
    return total


def full_gate(p: int, h: int, s: int) -> tuple[int, int, int]:
    fact, ifact, inv = factorial_data(p)
    k0, k1 = kernel(h, 1, p, fact, ifact), kernel(h, 4, p, fact, ifact)
    x = tail_sum(k0, s, 2 * s, True, p, inv)
    y = tail_sum(k0, h, 2 * s, True, p, inv)
    u = tail_sum(k1, s, 2 * s - 1, False, p, inv)
    v = tail_sum(k1, h, 2 * s - 1, True, p, inv)
    sign_s, sign_h = (-1 if s % 2 else 1), (-1 if h % 2 else 1)
    A = sign_s * fact[2 * s] * fact[s] * ifact[3 * s + 1] % p
    B = sign_h * fact[2 * s] * fact[h] * ifact[2 * s + h + 1] % p
    C = -sign_s * fact[2 * s - 1] * fact[s - 1] * ifact[3 * s - 1] % p
    D = sign_h * fact[2 * s - 1] * fact[h] * ifact[2 * s + h] % p
    q0, q1 = (2 * A * x - B * y) % p, (2 * C * u - D * v) % p
    eliminant = ((2 * s + h + 1) * x * v + 3 * (3 * s + 1) * u * y) * inv[2 * s] % p
    if q0 == q1 == 0:
        assert eliminant == 0
    return q0, q1, eliminant


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--M-bound", type=int, default=600)
    args = parser.parse_args()

    all_rows = []
    for M in range(9, args.M_bound + 1):
        left, right = rows_by_phase(M), rows_by_interval(M)
        assert left == right
        all_rows.extend((M,) + row for row in left)
    for j in range(1000):
        assert 6 * (2 * j + 1) < 4 * (3 * j + 4)

    witnesses = {
        (59, 2, 8, 40): (39, 11, 36),
        (109, 4, 15, 74): (71, 106, 87),
        (149, 26, 7, 108): (42, 106, 3),
    }
    witness_rows = []
    for (p, h, s, M), expected in witnesses.items():
        assert M == 3 * h + 4 * s + 2 and p == 4 * h + 6 * s + 3
        got = full_gate(p, h, s)
        assert got == expected and got[:2] != (0, 0)
        witness_rows.append((p, h, s, M, *got))
    assert 33 * 33 % 109 == 108 and (88 + 70 * 33) % 109 == 0
    assert 44 * 44 % 149 == 148 and (42 + 60 * 44) % 149 == 0

    getcontext().prec = 60
    rho = (Decimal(33).sqrt() - Decimal(3)) / Decimal(6)
    assert abs(Decimal(3) * rho * rho + Decimal(3) * rho - Decimal(2)) < Decimal("1e-55")
    H = 2 * (1 + rho).ln() - 4 * (1 - rho).ln() - 4 * rho.ln()
    assert H / 2 > Decimal(1) / 6
    assert H / 12 > Decimal(1) / 36
    assert 37 < 6 * H < 38

    digest = hashlib.sha256(json.dumps(all_rows, separators=(",", ":")).encode()).hexdigest()
    payload = {
        "schema": "item264-root-independent-probe-v1",
        "M_range": [9, args.M_bound],
        "prime_rows": len(all_rows),
        "prime_rows_digest_sha256": digest,
        "adjacent_interval_checks": 1000,
        "witness_gate_rows": witness_rows,
        "rho": str(rho),
        "H": str(H),
        "inherited_square_height_per_M": str(H / 2),
        "inherited_square_height_per_6M": str(H / 12),
        "same_height_minimum_integer_multiplicity": 38,
        "proof_audit": [
            "PNT applied to the exact interval gives raw M/6+o(M), hence 1/36 per 6M.",
            "R_M^2 divisibility plus the inherited componentwise Cauchy estimate is weaker than raw support.",
            "The bounded-degree statement is only an inherited-estimate information barrier; separately proved exponential cancellation remains open.",
            "The seed and Wronskian witnesses are not full-gate collisions.",
        ],
        "collision_scan_performed": False,
        "label": "EXACT FINITE independent replay supporting separately proved reindex and height comparisons",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
