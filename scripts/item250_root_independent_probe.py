#!/usr/bin/env python3
"""Dependency-free audit of the corrected Item 250 affine phase formulas."""

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


def conv(a: list[int], b: list[int], modulus: int | None = None) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
            if modulus:
                out[i + j] %= modulus
    return out


def power(a: list[int], n: int, modulus: int | None = None) -> list[int]:
    out = [1]
    while n:
        if n & 1:
            out = conv(out, a, modulus)
        n //= 2
        if n:
            a = conv(a, a, modulus)
    return out


def rising(x: F, n: int) -> F:
    out = F(1)
    for j in range(n):
        out *= x + j
    return out


def fmod(x: F, p: int) -> int:
    assert x.denominator % p
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def bsum(kpoly: list[int], parity: int, n0: F, d0: F) -> F:
    out = F(0)
    for ell in range(parity, len(kpoly), 2):
        t = (ell - parity) // 2
        out += kpoly[ell] * ((-1) ** t) * rising(-n0, t) / rising(1 - d0, t)
    return out


def phase(r: int) -> dict[str, object]:
    assert r >= 1 and r % 2 and r % 3
    qbar = F(-(2 * r + 3), 3)
    k0 = conv(power([1, -1], r), [1, 1])
    k1 = conv(power([1, -1], r), power([1, 1], 4))

    # The degree-p term changes the terminal boundary from c to c-1.
    kstar = 2 * r + 3
    alpha = 1 / (qbar + kstar)
    beta = -alpha
    for k in range(kstar - 2, 0, -2):
        alpha, beta = (
            (1 - (3 * qbar + k) * alpha) / (qbar + k),
            -(3 * qbar + k) * beta / (qbar + k),
        )

    states: list[tuple[F, F, F] | None] = [None] * (r + 5)
    states[0] = (F(1), F(0), F(0))
    states[1] = (F(0), alpha, beta)
    for k in range(r + 3):
        u, v, w = states[k]  # type: ignore[misc]
        denominator = 3 * qbar + k
        states[k + 2] = (
            -(qbar + k) * u / denominator,
            (1 - (qbar + k) * v) / denominator,
            -(qbar + k) * w / denominator,
        )

    def lincomb(poly: list[int], offsets: tuple[int, ...]) -> tuple[F, F, F]:
        out = [F(0), F(0), F(0)]
        for ell, coefficient in enumerate(poly):
            for offset in offsets:
                current = states[ell + offset]
                for j in range(3):
                    out[j] += coefficient * current[j]  # type: ignore[index]
        return tuple(out)  # type: ignore[return-value]

    x0 = lincomb(k0, (1, 3))
    x1 = lincomb(k1, (0,))
    na = r + qbar + 1
    ba0 = F((-1) ** r * math.factorial(r)) * bsum(k0, 0, na, F(r + 1)) / rising(qbar + 1, r + 1)
    ba1 = F((-1) ** (r + 1) * math.factorial(r + 1)) * bsum(k1, 1, na, F(r + 2)) / rising(qbar, r + 2)
    dbar = F(r, 6)
    rbar = -F(r + 2, 2)
    st0 = bsum(k0, 1, rbar, dbar)
    st1 = (-dbar / qbar) * bsum(k1, 1, rbar, dbar + 1)

    # Independent aggregate rank-one check (the frozen proof is termwise).
    assert x0[0] * st1 == x1[0] * st0
    L = 9 * (st0 * x1[1] - st1 * x0[1])
    M = st0 * (9 * x1[2] - 10 * ba1) - st1 * (9 * x0[2] - 10 * ba0)
    R = L**3 + F(2 ** (2 * r + 2)) * M**3
    return {"terminal": (alpha, beta), "x": (x0, x1), "ba": (ba0, ba1), "st": (st0, st1), "L": L, "M": M, "R": R}


def direct_coordinates(p: int, s: int, r: int, nu: int) -> tuple[int, int, int]:
    q = 2 * s - nu
    pnu = power([1, p - 1], r, p)
    pnu = conv(pnu, power([1, 1], 1 + 3 * nu, p), p)
    pnu = conv(pnu, power([1, 0, 1], q, p), p)
    A = [0] * p
    B = [0] * (2 * p)
    for k in range(1, p):
        A[k] = -pow(k, -1, p) % p
        B[2 * k] = (1 if k & 1 else -1) * pow(k, -1, p) % p

    def coefficient(logpoly: list[int], target: int) -> int:
        return sum(logpoly[k] * pnu[target - k] for k in range(1, min(target, len(logpoly) - 1) + 1) if 0 <= target - k < len(pnu)) % p

    T = p - r - 1
    a = p - q - 1
    return coefficient(A, T), coefficient(B, a), coefficient(B, T)


def factorial_tail(p: int, r: int, q: int) -> int:
    d = (r + q + 1) // 2
    upper = q + d
    value = (-1) ** (d - 1) % p
    for k in range(1, q + 1):
        value = value * k % p
    for k in range(1, d):
        value = value * k % p
    for k in range(1, upper + 1):
        value = value * pow(k, -1, p) % p
    return value


def phase_coordinates(p: int, s: int, r: int, data: dict[str, object]) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int]]:
    q = 2 * s
    c = pow(2, q, p)
    e = sum(math.comb(q - 1, t) * pow(q + 2 * t, -1, p) for t in range(q)) % p
    f = factorial_tail(p, r, q)
    x_values = []
    for a, b, d in data["x"]:  # type: ignore[assignment]
        x_values.append((fmod(a, p) * e + fmod(b, p) * c + fmod(d, p)) % p)
    ba = tuple(fmod(x, p) for x in data["ba"])  # type: ignore[arg-type]
    bt = tuple(f * fmod(x, p) % p for x in data["st"])  # type: ignore[arg-type]
    gates = tuple((9 * x_values[nu] - 10 * ba[nu] - bt[nu]) % p for nu in (0, 1))
    linear = (fmod(data["st"][0], p) * gates[1] - fmod(data["st"][1], p) * gates[0]) % p  # type: ignore[index]
    assert linear == (fmod(data["L"], p) * c + fmod(data["M"], p)) % p  # type: ignore[arg-type]
    return (x_values[0], ba[0], bt[0]), (x_values[1], ba[1], bt[1]), gates


def actual_rows(bound: int):
    for p in range(11, bound + 1):
        if not is_prime(p):
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            yield p, s, (p - 6 * s - 3) // 2


def main() -> None:
    cache: dict[int, dict[str, object]] = {}
    rows: list[tuple[int, ...]] = []
    for p, s, r in actual_rows(101):
        data = cache.setdefault(r, phase(r))
        phased = phase_coordinates(p, s, r, data)
        direct = [direct_coordinates(p, s, r, nu) for nu in (0, 1)]
        for nu in (0, 1):
            x, ba, bt = phased[nu]
            assert direct[nu] == (x, ba, bt)
        gates = phased[2]
        rows.append((p, s, r, *direct[0], *direct[1], *gates))

    assert len(rows) == 85
    witness_rows = {}
    for p, s, r in ((23, 3, 1), (67, 7, 11), (367, 39, 65), (953, 158, 1)):
        data = cache.get(r) or phase(r)
        phased = phase_coordinates(p, s, r, data)
        c = pow(2, 2 * s, p)
        linear = (fmod(data["L"], p) * c + fmod(data["M"], p)) % p  # type: ignore[arg-type]
        resultant = fmod(data["R"], p)  # type: ignore[arg-type]
        if p == 23:
            assert phased[2] == (4, 13)
        elif p == 67:
            assert phased[2] == (53, 62) and linear != 0 and resultant == 0
        elif p == 367:
            assert phased[2] == (238, 354) and linear == resultant == 0
        else:
            assert phased[2] == (0, 374) and linear == resultant == 0
        witness_rows[str(p)] = {"row": [p, s, r], "gates": list(phased[2]), "linear": linear, "resultant": resultant}

    terminal = phase(1)["terminal"]
    assert terminal == (F(-87, 10), F(27, 10))
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    result = {
        "schema": "item250-root-independent-probe-v1",
        "imports_item_code": False,
        "prime_max_inclusive": 101,
        "actual_rows": len(rows),
        "coordinate_equalities": 6 * len(rows),
        "row_digest_sha256": hashlib.sha256(payload).hexdigest(),
        "r1_terminal": [[-87, 10], [27, 10]],
        "witnesses": witness_rows,
        "scope": "exact identities and bounded replays; no all-prime nonvanishing or rate",
    }
    (HERE / "item250_root_independent_probe.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
