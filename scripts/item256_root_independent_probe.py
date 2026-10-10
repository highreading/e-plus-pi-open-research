#!/usr/bin/env python3
"""Independent root audit of Item 256's first beta jet."""

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


def rows(bound: int):
    for p in range(11, bound + 1):
        if not prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            r = (p - 6 * s - 3) // 2
            if r >= 1 and r % 2 == 1 and r % 3:
                yield p, r, s, s - 1, r + 4


def moment(m: int, d: int, c: F, q: int = 0, jet: int = 0) -> F:
    return sum(
        (
            F(math.comb(m, k), (2 * m + d + q + k) ** (jet + 1)) * c**k
            for k in range(m + 1)
        ),
        F(0),
    )


def transfer(m: int, d: int, c: F) -> tuple[F, F, F, F]:
    L = m + 1
    endpoint = (1 + c) ** L
    A, B, E, G = F(1), F(0), F(0), F(0)
    for q in range(L):
        aq, bq = 2 * m + d + q, 3 * m + d + q + 1
        lam = -F(aq, c * bq)
        mu = F(endpoint, c * bq)
        eta = F(L, c * bq * bq)
        nu = F(endpoint, c * bq * bq)
        A0, B0, E0, G0 = A, B, E, G
        A = lam * A0
        B = lam * B0 + eta * A0
        E = lam * E0 + mu
        G = lam * G0 + eta * E0 + nu
    return A, B, E, G


def modq(x: F, modulus: int) -> int:
    assert math.gcd(x.denominator, modulus) == 1
    return x.numerator % modulus * pow(x.denominator, -1, modulus) % modulus


def rank(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    rr = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rr, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = pow(a[rr][col], -1, p)
        a[rr] = [x * inv % p for x in a[rr]]
        for i in range(len(a)):
            if i != rr and a[i][col]:
                f = a[i][col]
                a[i] = [(x - f * y) % p for x, y in zip(a[i], a[rr])]
        rr += 1
    return rr


def main() -> None:
    exact_checks = 0
    for m in range(9):
        for d in range(3, 16, 2):
            for c in (F(-2), F(-1, 2), F(3, 2)):
                A, B, E, G = transfer(m, d, c)
                M, N = moment(m, d, c), moment(m, d, c, jet=1)
                assert moment(m, d, c, m + 1) == A * M + E
                assert moment(m, d, c, m + 1, 1) == B * M + A * N + G
                for q in range(m + 1):
                    aq, bq = 2 * m + d + q, 3 * m + d + q + 1
                    assert aq * moment(m, d, c, q) + c * bq * moment(m, d, c, q + 1) == (1 + c) ** (m + 1)
                    assert aq * moment(m, d, c, q, 1) + c * bq * moment(m, d, c, q + 1, 1) == moment(m, d, c, q) + c * moment(m, d, c, q + 1)
                    exact_checks += 2

    records = []
    for p, r, s, m, d in rows(401):
        L, c, ci = m + 1, F(-2), F(-1, 2)
        X, Y = moment(m, d, c), moment(m, d, ci)
        U, V = moment(m, d, c, jet=1), moment(m, d, ci, jet=1)
        assert modq(moment(m, d, c, L) + c**m * (Y + p * V), p * p) == 0
        assert modq(moment(m, d, c, L, 1) - c**m * V, p) == 0
        A, B, E, G = transfer(m, d, c)
        Ai, Bi, Ei, Gi = transfer(m, d, ci)
        harmonic = sum((F(1, 2 * m + d + t) for t in range(L)), F(0))
        assert modq(A - c ** (-L) * (1 + p * harmonic), p * p) == 0
        assert modq(A * Ai - 1 - 2 * p * harmonic, p * p) == 0
        assert Bi == c ** (2 * L) * B
        cm = -2 % p
        mat = [
            [modq(A, p), pow(cm, m, p), 0, 0],
            [pow(pow(cm, -1, p), m, p), modq(Ai, p), 0, 0],
            [modq(B, p), 0, modq(A, p), -pow(cm, m, p)],
            [0, modq(Bi, p), -pow(pow(cm, -1, p), m, p), modq(Ai, p)],
        ]
        assert rank(mat, p) == 2
        assert modq(Ei - c * E, p) == 0
        assert modq(Gi - (-c * G + c * B / A * E), p) == 0
        records.append((p, r, s, m, d, modq(X, p), modq(U, p), modq(harmonic, p)))

    w = next(x for x in records if x[:3] == (23, 1, 3))
    assert w[-1] == 0
    A, _, _, _ = transfer(2, 5, F(-2))
    Ai, _, _, _ = transfer(2, 5, F(-1, 2))
    z = abs((A * Ai - 1).numerator)
    valuation = 0
    while z % 23 == 0:
        valuation += 1
        z //= 23
    assert valuation == 2
    payload = "".join(",".join(map(str, x)) + "\n" for x in records).encode("ascii")
    result = {
        "schema": "item256-root-independent-probe-v1",
        "imports_item_code": False,
        "exact_value_and_jet_recurrence_checks": exact_checks,
        "actual_rows_through_p_401": len(records),
        "mod_p2_reflection_and_rank_checks": len(records),
        "augmented_rank_on_every_row": 2,
        "p23_first_Hasse_nonunit_reproduced": True,
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "scope": "independent exact implementation and bounded replay; no higher-jet, density, or rate inference",
    }
    (HERE.parent / "results" / "item256_root_independent_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
