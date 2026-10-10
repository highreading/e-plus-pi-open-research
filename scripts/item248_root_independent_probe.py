#!/usr/bin/env python3
"""Dependency-free exact audit probes for Item 248."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
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


def conv(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_power(a: list[int], n: int, p: int) -> list[int]:
    out = [1]
    while n:
        if n & 1:
            out = conv(out, a, p)
        n //= 2
        if n:
            a = conv(a, a, p)
    return out


def add(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0] + b[0]) % p, (a[1] + b[1]) % p)


def sub(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0] - b[0]) % p, (a[1] - b[1]) % p)


def scale(c: int, a: tuple[int, int], p: int) -> tuple[int, int]:
    return (c * a[0] % p, c * a[1] % p)


def mul(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0] * b[0] - a[1] * b[1]) % p, (a[0] * b[1] + a[1] * b[0]) % p)


def power(a: tuple[int, int], n: int, p: int) -> tuple[int, int]:
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, a, p)
        n //= 2
        if n:
            a = mul(a, a, p)
    return out


def norm(a: tuple[int, int], p: int) -> int:
    return (a[0] * a[0] + a[1] * a[1]) % p


def pconv(a: list[tuple[int, int]], b: list[tuple[int, int]], p: int) -> list[tuple[int, int]]:
    out = [(0, 0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = add(out[i + j], mul(x, y, p), p)
    return out


def ppow(a: list[tuple[int, int]], n: int, p: int) -> list[tuple[int, int]]:
    out = [(1, 0)]
    while n:
        if n & 1:
            out = pconv(out, a, p)
        n //= 2
        if n:
            a = pconv(a, a, p)
    return out


def direct_factor(p: int, h: int, s: int, nu: int) -> list[tuple[int, int]]:
    r = 2 * h
    chi = 1 if p % 4 == 1 else -1
    x = (0, chi % p)
    linears = [
        [(1, 0), (p - 1, 0)],
        [(2, 0), (p - 1, 0)],
        [sub((1, 0), x, p), x],
        [add((1, 0), x, p), scale(-1, x, p)],
    ]
    exponents = (2 * s, 2 * s, r, 1) if nu == 0 else (2 * s - 1, 2 * s - 1, r, 4)
    out = [(1, 0)]
    for line, exponent in zip(linears, exponents):
        out = pconv(out, ppow(line, exponent, p), p)
    return out


def local_values(p: int, h: int, s: int, nu: int) -> dict[str, object]:
    factor = direct_factor(p, h, s, nu)
    n = p - 2 * s - 3 + nu
    harmonic = 0
    local_square = (0, 0)
    for k in range(n + 1):
        harmonic = (harmonic + pow(k + 1, -1, p)) % p
        a2 = 8 * harmonic * pow(k + 2, -1, p) % p
        coefficient = factor[n - k] if n - k < len(factor) else (0, 0)
        local_square = add(local_square, scale(a2, coefficient, p), p)
    target = n + 2
    first = (0, 0)
    for j in range(1, target + 1):
        source = target - j
        if source < len(factor):
            first = add(first, scale(-pow(j, -1, p), factor[source], p), p)
    second = scale(pow(4, -1, p), local_square, p)
    a_index = p - 2 * s - 1 + nu
    chi = 1 if p % 4 == 1 else -1
    x = (0, chi % p)
    leading = scale(-24, mul(power(x, (-a_index) % 4, p), local_square, p), p)
    return {"factor": factor, "first": first, "second": second, "leading": leading, "n": n}


def direct_section_leading(p: int, h: int, s: int, nu: int) -> tuple[int, int]:
    r = 2 * h
    b0 = [0] * (2 * p - 1)
    for k in range(1, p):
        b0[2 * k] = ((1 if k & 1 else -1) * pow(k, -1, p)) % p
    b02 = conv(b0, b0, p)
    pnu = poly_power([1, p - 1], r, p)
    pnu = conv(pnu, poly_power([1, 1], 1 + 3 * nu, p), p)
    pnu = conv(pnu, poly_power([1, 0, 1], 2 * s - nu, p), p)
    product = conv(b02, pnu, p)
    a_index = p - 2 * s - 1 + nu
    value = (0, 0)
    i_power = (1, 0)
    i_unit = (0, 1)
    j = 0
    while a_index + j * p < len(product):
        value = add(value, scale(product[a_index + j * p], i_power, p), p)
        i_power = mul(i_power, i_unit, p)
        j += 1
    return scale(-24, value, p)


def normalized_g_w(p: int, h: int, s: int) -> tuple[list[tuple[int, int]], tuple[int, int]]:
    data = [local_values(p, h, s, nu) for nu in (0, 1)]
    factorial = math.factorial(2 * h) % p
    g = [scale(pow(factorial, -1, p), entry["first"], p) for entry in data]
    raw = sub(mul(data[0]["first"], data[1]["second"], p), mul(data[1]["first"], data[0]["second"], p), p)
    w = scale(pow(2 * factorial * factorial % p, -1, p), raw, p)
    return g, w


def fconv(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def falling_poly(n: int) -> list[Fraction]:
    out = [Fraction(1)]
    for j in range(n):
        out = fconv(out, [Fraction(-j), Fraction(1)])
    return out


def divide_poly(numerator: list[Fraction], denominator: list[Fraction]) -> list[Fraction]:
    work = numerator + [Fraction(0)] * max(0, len(denominator) - len(numerator))
    quotient = [Fraction(0)] * (len(work) - len(denominator) + 1)
    for degree in range(len(work) - 1, len(denominator) - 2, -1):
        q = work[degree] / denominator[-1]
        index = degree - len(denominator) + 1
        quotient[index] = q
        for j, value in enumerate(denominator):
            work[index + j] -= q * value
    assert all(value == 0 for value in work[: len(denominator) - 1])
    return quotient


def tail_polynomials(h_values: list[int], R: int) -> tuple[list[Fraction], list[Fraction]]:
    d = len(h_values) - 1
    F = [Fraction(0)] * (d + R + 1)
    for k in range(d + 1):
        term = falling_poly(R + k)
        multiplier = Fraction(h_values[d - k] * ((-1) ** (R + k)), math.factorial(R + k))
        for j, value in enumerate(term):
            F[j] += multiplier * value
    G = divide_poly(F, falling_poly(R))
    return F, G


def main() -> None:
    direct_rows = 0
    direct_coordinates = 0
    digest_rows: list[tuple[int, ...]] = []
    for p in range(11, 62):
        if not is_prime(p):
            continue
        for h in range(1, p):
            remainder = p - 4 * h - 3
            if remainder < 6 or remainder % 6:
                continue
            s = remainder // 6
            direct_rows += 1
            for nu in (0, 1):
                local = local_values(p, h, s, nu)["leading"]
                direct = direct_section_leading(p, h, s, nu)
                assert local == direct
                digest_rows.append((p, h, s, nu, *local))
                direct_coordinates += 1

    # Exact individual-pair counterexample.
    pair_59 = local_values(59, 2, 8, 1)["leading"]
    assert pair_59 == (0, 0)
    assert direct_section_leading(59, 2, 8, 1) == (0, 0)

    g_41, _ = normalized_g_w(41, 2, 5)
    assert g_41[0] == (12, 15)
    assert (12 + 15 * 32) % 41 == 0 and 32 * 32 % 41 == 40

    wronskians: dict[str, object] = {}
    for p, h, s, expected, root in (
        (109, 4, 15, (88, 70), 33),
        (149, 26, 7, (42, 60), 44),
    ):
        _, w = normalized_g_w(p, h, s)
        assert w == expected and norm(w, p) == 0
        assert root * root % p == p - 1 and (w[0] + w[1] * root) % p == 0
        wronskians[str(p)] = {"row": [p, h, s], "pair": list(w), "root": root}

    # Generic exact tail-lemma and division-free determinant checks over Q.
    F0, G0 = tail_polynomials([3, -2, 5, 1], 4)
    F1, G1 = tail_polynomials([2, 7, -1], 4)
    A = falling_poly(4)
    assert F0 == fconv(A, G0) and F1 == fconv(A, G1)
    aprime = A[1]
    assert aprime == -6
    lhs = G1[1] * G0[0] - G1[0] * G0[1]
    rhs = (F0[1] * 2 * F1[2] - F1[1] * 2 * F0[2]) / (2 * aprime * aprime)
    assert lhs == rhs

    raw = "".join(",".join(map(str, row)) + "\n" for row in digest_rows).encode("ascii")
    result = {
        "schema": "item248-root-independent-probe-v1",
        "imports_item_code": False,
        "direct_prime_max_inclusive": 61,
        "direct_rows": direct_rows,
        "direct_coordinates": direct_coordinates,
        "direct_digest_sha256": hashlib.sha256(raw).hexdigest(),
        "individual_pair_zero": {"row_nu": [59, 2, 8, 1], "pair": list(pair_59)},
        "split_G_zero": {"row_nu": [41, 2, 5, 0], "pair": list(g_41[0]), "root": 32},
        "split_W_zeros": wronskians,
        "generic_tail_lemma": {"R": 4, "wronskian_identity": True},
    }
    (HERE / "item248_root_independent_probe.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
