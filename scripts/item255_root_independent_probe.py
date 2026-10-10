#!/usr/bin/env python3
"""Independent standard-library audit of Item 255's beta orbit."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def prime(n: int) -> bool:
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


def moment(m: int, d: int, c: F, q: int = 0) -> F:
    return sum(
        (F(math.comb(m, k), 2 * m + d + q + k) * c**k for k in range(m + 1)),
        F(0),
    )


def diagonal(m: int, d: int) -> F:
    n = 3 * m + d
    return sum((F((-1) ** k * math.comb(n, k), 2**k) for k in range(m + 1)), F(0))


def modq(x: F, p: int) -> int:
    assert x.denominator % p
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def hprefix(m: int, p: int) -> int:
    h = total = 1
    for k in range(m):
        h = h * (2 * k + 1) * pow(4 * (k + 1), -1, p) % p
        total = (total + h) % p
    return total


def rows(bound: int):
    for p in range(11, bound + 1):
        if not prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            x = p - 6 * s - 3
            if x <= 0:
                break
            if x % 2:
                continue
            r = x // 2
            if r % 2 == 1 and r % 3:
                yield p, r, s, s - 1, r + 4


def main() -> None:
    beta_checks = recurrence_checks = 0
    for m in range(10):
        for d in range(3, 18, 2):
            n = 3 * m + d
            assert 2**m * diagonal(m, d) == (2 * m + d) * math.comb(n, m) * moment(m, d, F(-2))
            beta_checks += 1
            for c in (F(-2), F(-1, 2), F(3, 2)):
                for q in range(m + 1):
                    lhs = (2 * m + d + q) * moment(m, d, c, q)
                    lhs += c * (3 * m + d + q + 1) * moment(m, d, c, q + 1)
                    assert lhs == (1 + c) ** (m + 1)
                    recurrence_checks += 1

    records = []
    harmonic_zeros = prefix_zeros = 0
    for p, r, s, m, d in rows(401):
        L = m + 1
        n = 3 * m + d
        I = moment(m, d, F(-2))
        J = moment(m, d, F(-1, 2))
        assert modq(diagonal(m, d), p) == hprefix(m, p)
        assert (modq(I, p) == 0) == (hprefix(m, p) == 0)
        assert modq(moment(m, d, F(-2), L), p) == -pow(-2 % p, m, p) * modq(J, p) % p
        assert modq(moment(m, d, F(-1, 2), L), p) == -pow(pow(-2 % p, -1, p), m, p) * modq(I, p) % p

        num = math.prod(range(2 * m + d, 3 * m + d + 1))
        den = math.prod(range(3 * m + d + 1, 4 * m + d + 2))
        R = F(num, den)
        assert modq(R, p) == (-1) ** L % p
        det = R * R - 1
        harmonic = sum((F(1, 2 * m + d + t) for t in range(L)), F(0))
        assert modq(det / p, p) == 2 * modq(harmonic, p) % p
        hz = modq(harmonic, p) == 0
        pz = hprefix(m, p) == 0
        harmonic_zeros += hz
        prefix_zeros += pz
        records.append((p, r, s, m, d, hprefix(m, p), modq(I, p), modq(J, p), modq(harmonic, p)))

    w23 = next(x for x in records if x[:3] == (23, 1, 3))
    w43 = next(x for x in records if x[:3] == (43, 11, 3))
    assert w23[-1] == 0
    assert w43[5] == w43[6] == 0 and w43[7] != 0
    payload = "".join(",".join(map(str, x)) + "\n" for x in records).encode("ascii")
    result = {
        "schema": "item255-root-independent-probe-v1",
        "imports_item_code": False,
        "exact_beta_checks": beta_checks,
        "exact_endpoint_recurrence_checks": recurrence_checks,
        "actual_rows_through_p_401": len(records),
        "phase_reflection_and_Hasse_checks": len(records),
        "prefix_zero_count_EXACT_FINITE_ONLY": prefix_zeros,
        "harmonic_zero_count_EXACT_FINITE_ONLY": harmonic_zeros,
        "witnesses": {"first_Hasse_nonunit": [23, 1, 3], "prefix_zero_companion_nonzero": [43, 11, 3]},
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "independent exact implementation and bounded replay; no all-prime nonvanishing, density, or rate inference",
    }
    (HERE.parent / "results" / "item255_root_independent_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
