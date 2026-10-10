#!/usr/bin/env python3
"""Independent exact-integer/Fraction audit of Item 247."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def power(a, n):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def derivative(a):
    return trim([i * a[i] for i in range(1, len(a))])


def pad_equal(a, b):
    return trim(a) == trim(b)


def functional(lower, d):
    total = Fraction(0)
    for v in range(len(d)):
        nv = 2 * (lower + v) + 1
        for k in range(v):
            nk = 2 * (lower + k) + 1
            total += Fraction(((-1) ** (v - k - 1)) * d[v], nk * nv)
    return total


def mod_fraction(x, p):
    return x.numerator % p * pow(x.denominator % p, -1, p) % p


def prime_list(n):
    return [p for p in range(2, n + 1)
            if all(p % q for q in range(2, math.isqrt(p) + 1))]


def actual_rows(n):
    for p in prime_list(n):
        if p < 17:
            continue
        for s in range(2, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4 == 0:
                yield p, s


def direct_D(p, s, nu):
    r = (p - 6 * s - 3) // 2
    full = mul(mul(power([1, -1], r), power([1, 1], 1 + 3 * nu)),
               power([1, 0, 1], 2 * s - nu))
    return trim(full[r % 2::2])


def verify_row(p, s):
    r = (p - 6 * s - 3) // 2
    assert r >= 1 and r % 2 == 1
    assert r != 3
    lower = (r + 1) // 2
    R = r - 1
    base = power([1, -1], R)
    E = trim(base[0::2])
    O = scale(trim(base[1::2]), -1)
    G = mul([1, -1], power([1, 1], 2 * s - 1))
    A = scale(mul(G, O), -1)
    C = mul(G, E)
    D0, D1 = direct_D(p, s, 0), direct_D(p, s, 1)
    assert pad_equal(D0, mul([1, 1], A))
    assert pad_equal(D1, add(mul([1, 3], A), mul([3, 1], C)))

    b0, b1 = functional(lower, D0), functional(lower, D1)
    x, y, z = functional(lower, A), functional(lower, mul([0, 1], A)), functional(lower, mul([3, 1], C))
    assert b0 == x + y and b1 == x + 3 * y + z
    eliminated = b1 - 3 * b0
    assert eliminated == functional(lower, add(mul([3, 1], C), scale(A, -2)))

    if R:
        lhs_E = scale(E, R)
        rhs_E = add(mul([1, R - 1], O), scale(mul([0, 1, -1], derivative(O)), 2))
        assert pad_equal(lhs_E, rhs_E)
        d1_seed = add(mul([3 - R, -2, R - 1], O),
                      scale(mul([0, 3, -2, -1], derivative(O)), 2))
        assert pad_equal(scale(D1, R), mul(G, d1_seed))
        j_seed = add(mul([2 * R + 3, 3 * R - 2, R - 1], O),
                     scale(mul([0, 3, -2, -1], derivative(O)), 2))
        assert R * eliminated == functional(lower, mul(G, j_seed))
        assert 0 < 2 * R < 2 * p and (2 * R) % p != 0
    else:
        assert not D0
        assert pad_equal(D1, mul(G, [3, 1]))
        assert p == 6 * s + 5

    degree = max(len(D0), len(D1)) - 1
    assert degree == lower + 2 * s
    denominators = [2 * (lower + k) + 1 for k in range(degree + 1)]
    assert max(denominators) < p
    Q = math.prod(denominators)
    I0, I1 = b0 * Q * Q, b1 * Q * Q
    assert I0.denominator == I1.denominator == 1
    content = math.gcd(abs(I0.numerator), abs(I1.numerator))
    m0, m1 = mod_fraction(b0, p), mod_fraction(b1, p)
    assert (content % p == 0) == (m0 == 0 and m1 == 0)
    return {
        "p": p, "s": s, "r": r, "L": lower,
        "B0": m0, "B1": m1, "E": (m1 - 3 * m0) % p,
        "nonempty0": bool(D0), "nonempty1": bool(D1),
        "content_mod_p": content % p,
    }


def main():
    records = [verify_row(p, s) for p, s in actual_rows(151)]
    joint = [row for row in records if row["B0"] == row["B1"] == 0]
    assert not joint
    witness = next(row for row in records if (row["p"], row["s"]) == (127, 11))
    assert (witness["B0"], witness["B1"], witness["E"]) == (97, 37, 0)

    singular_records = []
    for p in prime_list(1000):
        if p >= 17 and (p - 5) % 6 == 0:
            s = (p - 5) // 6
            if s >= 2:
                row = verify_row(p, s)
                assert row["r"] == 1
                singular_records.append(row)
    assert all(row["B1"] != 0 for row in singular_records)

    output = {
        "item": 247,
        "audit": "independent exact-integer construction; imports neither Item246 nor Item247",
        "rows_through_151": len(records),
        "separate_nonempty_coordinate_zeros": sum(row["nonempty0"] and row["B0"] == 0 for row in records) + sum(row["nonempty1"] and row["B1"] == 0 for row in records),
        "eliminated_zeros": sum(row["E"] == 0 for row in records),
        "simultaneous_zeros": len(joint),
        "witness_127_11": witness,
        "singular_prime_bound": 1000,
        "singular_rows": len(singular_records),
        "singular_zeros": 0,
        "proved_checks": [
            "actual parity pair and determinant-two functional system",
            "parity differential identity and one-seed eliminant over Z",
            "exact r=1 singular specialization and admissibility",
            "common-denominator integrality and moving-prime gcd criterion",
        ],
    }
    path = Path(__file__).with_suffix(".json")
    payload = json.dumps(output, indent=2, sort_keys=True) + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    print(json.dumps({"output": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "rows": len(records), "singular_rows": len(singular_records)}, sort_keys=True))


if __name__ == "__main__":
    main()
