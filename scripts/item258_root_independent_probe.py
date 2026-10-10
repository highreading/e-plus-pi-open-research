#!/usr/bin/env python3
"""Independent root probe for Item 258's second-jet identities.

No Item-258 code is imported.  Exact rational identities are checked directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (((bound - start) // q) + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def actual_rows(bound: int):
    for p in primes_up_to(bound):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r % 2 and r % 3:
                yield p, r, s, s - 1, r + 4


def mod_fraction(value: F, modulus: int) -> int:
    assert math.gcd(value.denominator, modulus) == 1
    return value.numerator % modulus * pow(value.denominator, -1, modulus) % modulus


def moment(m: int, d: int, c: F, q: int, order: int) -> F:
    a = 2 * m + d
    return sum(
        (
            F(math.comb(m, k), (a + q + k) ** (order + 1)) * c**k
            for k in range(m + 1)
        ),
        F(0),
    )


def transfer_coefficients(m: int, d: int, c: F) -> tuple[F, F, F, F, F, F]:
    length = m + 1
    a = 2 * m + d
    b = a + length
    endpoint = (1 + c) ** length
    A, B, C = F(1), F(0), F(0)
    E, G, K = F(0), F(0), F(0)
    for q in range(length):
        alpha = a + q
        beta = b + q
        lam = -F(alpha, 1) / (c * beta)
        eta = F(length, 1) / (c * beta**2)
        theta = F(length, 1) / (c * beta**3)
        mu = endpoint / (c * beta)
        nu = endpoint / (c * beta**2)
        xi = endpoint / (c * beta**3)
        K = lam * K + eta * G + theta * E + xi
        C = lam * C + eta * B + theta * A
        G = lam * G + eta * E + nu
        B = lam * B + eta * A
        E = lam * E + mu
        A = lam * A
    return A, B, C, E, G, K


def rank_mod(matrix: list[list[int]], p: int) -> int:
    work = [[entry % p for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, p)
        work[row] = [x * inverse % p for x in work[row]]
        for i in range(len(work)):
            if i != row and work[i][column]:
                factor = work[i][column]
                work[i] = [
                    (x - factor * y) % p for x, y in zip(work[i], work[row])
                ]
        row += 1
    return row


def valuation(value: int, p: int) -> int:
    value = abs(value)
    out = 0
    while value and value % p == 0:
        value //= p
        out += 1
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    checked = 0
    digest_rows: list[str] = []
    witness_89 = None
    witness_157 = None
    for p, r, s, m, d in actual_rows(args.bound):
        length = m + 1
        c = F(-2)
        ci = 1 / c
        X = [moment(m, d, c, 0, order) for order in range(3)]
        Y = [moment(m, d, ci, 0, order) for order in range(3)]
        XL = [moment(m, d, c, length, order) for order in range(3)]
        assert mod_fraction(XL[0] + c**m * (Y[0] + p * Y[1] + p * p * Y[2]), p**3) == 0
        assert mod_fraction(XL[1] - c**m * (Y[1] + 2 * p * Y[2]), p**2) == 0
        assert mod_fraction(XL[2] + c**m * Y[2], p) == 0

        A, B, C, E, G, K = transfer_coefficients(m, d, c)
        Ai, Bi, Ci, Ei, Gi, Ki = transfer_coefficients(m, d, ci)
        delta1 = sum(
            (F(1, (2 * m + d + q)) - F(1, (3 * m + d + 1 + q))
             for q in range(length)),
            F(0),
        )
        delta2 = sum(
            (F(1, (2 * m + d + q) ** 2) - F(1, (3 * m + d + 1 + q) ** 2)
             for q in range(length)),
            F(0),
        )
        assert B == -A * delta1
        assert C == A * (delta1 * delta1 - delta2) / 2
        assert B * B - 2 * A * C == A * A * delta2
        assert (Ai, Bi, Ci) == tuple(c ** (2 * length) * value for value in (A, B, C))

        h1 = sum((F(1, 2 * m + d + t) for t in range(length)), F(0))
        h2 = sum((F(1, (2 * m + d + t) ** 2) for t in range(length)), F(0))
        h3 = sum((F(1, (2 * m + d + t) ** 3) for t in range(length)), F(0))
        approx = c ** (-length) * (
            1 + p * h1 + F(p * p, 2) * (h2 + h1 * h1)
        )
        assert mod_fraction(A - approx, p**3) == 0
        assert mod_fraction(
            A * Ai - 1 - 2 * p * h1 - p * p * (h2 + 2 * h1 * h1),
            p**3,
        ) == 0
        assert mod_fraction(delta2 + 2 * p * h3, p**2) == 0

        am = mod_fraction(A, p)
        bm = mod_fraction(B, p)
        cm = mod_fraction(C, p)
        aim = mod_fraction(Ai, p)
        bim = mod_fraction(Bi, p)
        cim = mod_fraction(Ci, p)
        t = mod_fraction(c**m, p)
        ti = pow(t, -1, p)
        matrix = [
            [am, t, 0, 0, 0, 0],
            [ti, aim, 0, 0, 0, 0],
            [bm, 0, am, -t, 0, 0],
            [0, bim, -ti, aim, 0, 0],
            [cm, 0, bm, 0, am, t],
            [0, cim, 0, bim, ti, aim],
        ]
        assert rank_mod(matrix, p) == 3
        checked += 1
        digest_rows.append(
            f"{p},{r},{s},{mod_fraction(h1,p)},{mod_fraction(h2,p)},"
            f"{mod_fraction(h3,p)},{bm},{cm}\n"
        )

        if (p, r, s) == (89, 19, 8):
            witness_89 = (
                mod_fraction(h1, p),
                mod_fraction(h2, p),
                mod_fraction(h2 + 2 * h1 * h1, p),
            )
        if (p, r, s) == (157, 59, 6):
            curvature = B * B - 2 * A * C
            witness_157 = (
                mod_fraction(h3, p),
                valuation(curvature.numerator, p),
            )

    assert witness_89 == (44, 44, 0)
    assert witness_157 == (0, 2)
    result = {
        "schema": "item258-root-independent-probe-v1",
        "imports_item258_code": False,
        "prime_bound": args.bound,
        "actual_rows_rank_three": checked,
        "witness_89_H1_H2_J2": witness_89,
        "witness_157_H3_curvature_numerator_valuation": witness_157,
        "row_digest_sha256": hashlib.sha256(
            "".join(digest_rows).encode("ascii")
        ).hexdigest(),
        "verdict": "all exact second-jet identities, all-row rank collapse, and both unit counterexamples replay independently",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
