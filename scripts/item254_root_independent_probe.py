#!/usr/bin/env python3
"""Independent root probe of Item 254's arithmetic forms."""

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


def legendre(a: int, p: int) -> int:
    return pow(a % p, (p - 1) // 2, p)


def prefix_terms(m: int, p: int) -> tuple[list[int], list[int]]:
    terms = [1]
    sums = [1]
    h = total = 1
    for k in range(m):
        h = h * (2 * k + 1) * pow(4 * (k + 1), -1, p) % p
        total = (total + h) % p
        terms.append(h)
        sums.append(total)
    return terms, sums


def actual_rows(bound: int):
    for p in range(11, bound + 1):
        if not prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            r = (p - 6 * s - 3) // 2
            if r >= 1 and r % 2 == 1 and r % 3:
                yield p, r, s, s - 1, r + 4


def frac_mod(x: F, p: int) -> int:
    assert x.denominator % p
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def beta(m: int, d: int) -> F:
    return sum((F(math.comb(m, k) * (-2) ** k, 2 * m + d + k) for k in range(m + 1)), F(0))


def fixed_boundary(p: int, delta: int) -> int:
    product = 1
    total = 0
    for k in range(delta):
        total = (total + product) % p
        if k + 1 < delta:
            if p % 6 == 1:
                num, den = 6 * k + 1, 3 * k + 2
            else:
                num, den = 6 * k + 5, 3 * k + 4
            product = product * num * pow(den, -1, p) % p
    return total


def character_probe(p: int) -> int:
    n = (p - 1) // 2
    terms, sums = prefix_terms(n, p)
    eps = pow(2, n, p)
    assert sums[-1] == eps and sum(sums) % p == 0
    checked = 0
    for s in range(1, (p - 3) // 6 + 1):
        r = (p - 6 * s - 3) // 2
        if r < 1 or r % 2 == 0 or r % 3 == 0:
            continue
        m = s - 1
        mellin = 0
        for x in range(1, p):
            Cx = sum(sums[k] * pow(x, k, p) for k in range(n + 1)) % p
            if x == 1:
                assert Cx == 0
            else:
                explicit = (legendre(1 - x * pow(2, -1, p), p) - eps * x * legendre(x, p))
                explicit = explicit * pow(1 - x, -1, p) % p
                assert Cx == explicit
            mellin = (mellin + pow(x, -m, p) * Cx) % p
        assert -mellin % p == sums[m]

        a = n - m + 1
        jacobi = sum(pow(x, a, p) * pow(1 - x, -1, p) for x in range(1, p) if x != 1) % p
        assert jacobi == a % p and jacobi != 0
        assert math.gcd(m, p - 1) == math.gcd(m, 2 * r + 8)
        if p % 6 == 5:
            weighted = 0
            unweighted = sum(legendre(pow(x, 3, p) - pow(2, -1, p), p) for x in range(p)) % p
            assert unweighted == 0
            for x in range(1, p):
                if x == 1:
                    continue
                weighted += (
                    pow(x, r + 4, p)
                    * legendre(x * (1 - pow(x, 3, p) * pow(2, -1, p)), p)
                    * pow(1 - pow(x, 3, p), -1, p)
                )
            assert (eps * a - weighted) % p == sums[m]
        else:
            q = (p - 1) // 6
            delta = (r + 4) // 3
            assert m == q - delta
            for x in range(1, p):
                assert pow(x, -m, p) == pow(x, delta, p) * pow(pow(x, q, p), -1, p) % p
        checked += 1
    return checked


def main() -> None:
    records = []
    for p, r, s, m, d in actual_rows(401):
        terms, sums = prefix_terms(max(m, p // 6), p)
        H = sums[m]
        pref = pow(2, -m, p) * (2 * m + d) * (math.comb(3 * m + d, m) % p) % p
        assert H == pref * frac_mod(beta(m, d), p) % p
        q = p // 6
        delta = (r + 4) // 3 if p % 6 == 1 else (r + 2) // 3
        assert m == q - delta
        assert H == (sums[q] - terms[q] * fixed_boundary(p, delta)) % p
        records.append((p, r, s, m, H))

    char_rows = sum(character_probe(p) for p in range(11, 102) if prime(p))

    numerator_checks = 0
    for m in range(257):
        U = sum(math.comb(2 * j, j) * 8 ** (m - j) for j in range(m + 1))
        v2 = (U & -U).bit_length() - 1
        assert v2 == m.bit_count()
        N = U >> v2
        D = 1 << (3 * m - v2)
        assert N % 2 == 1 and N * N < 2 * D * D
        numerator_checks += 1
    assert next(x for x in records if x[:3] == (43, 11, 3))[4] == 0
    assert next(x for x in records if x[:3] == (47, 7, 5))[4] == 0
    payload = "".join(",".join(map(str, x)) + "\n" for x in records).encode("ascii")
    result = {
        "schema": "item254-root-independent-probe-v1",
        "imports_item_code": False,
        "actual_rows_through_p_401": len(records),
        "beta_and_fixed_cutoff_equalities": len(records),
        "character_rows_through_p_101": char_rows,
        "numerator_valuation_and_height_checks": numerator_checks,
        "exact_actual_prefix_zeros": [[43, 11, 3], [47, 7, 5]],
        "container_limit_per_6m": "log(2)/2; positive and not bookable as zero rate",
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "independent exact implementation and bounded replay; no density, capacity, or rate inference",
    }
    (HERE.parent / "results" / "item254_root_independent_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
