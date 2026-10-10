#!/usr/bin/env python3
"""Standalone root audit probe for Item 231 (imports no project module)."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction


def convolution(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def power(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = convolution(out, poly)
    return out


def primes_upto(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = [False] * (((limit - q * q) // q) + 1)
    return [q for q, flag in enumerate(sieve) if flag]


def d_coefficient(r: int, s: int, n: int) -> int:
    if n < 0:
        return 0
    return sum(
        (-1) ** j
        * math.comb(2 * s + j - 1, j)
        * math.comb(r + n - 2 * j, n - 2 * j)
        for j in range(n // 2 + 1)
    )


def g_coefficient(r: int, s: int, n: int) -> int:
    return (
        (2 * r + 4 * s - 1) * d_coefficient(r, s, n)
        + (r + 1) * d_coefficient(r, s, n - 1)
        - (r + 8 * s) * d_coefficient(r, s, n - 2)
    )


def pi_coefficient(p: int, r: int, s: int, n: int) -> int:
    if n < 0:
        return 0
    total = 0
    for j in range(p - 2 * s + 1):
        k = n - 2 * j
        if 0 <= k <= p - r - 1:
            total += math.comb(p - 2 * s, j) * (-1) ** k * math.comb(p - r - 1, k)
    return total


def reciprocal_tail(p: int, r: int, s: int) -> int:
    upper = (p + r - 1) // 2
    aa, bb, cc = 2 * r + 4 * s - 1, r + 1, -(r + 8 * s)

    def t(j: int) -> int:
        return (-1) ** j * math.comb(2 * s + j - 1, j)

    return (
        cc * sum(t(j) * math.comb(2 * j - r - 1, r) for j in range(r + 1, upper + 1))
        + bb * sum(t(j) * math.comb(2 * j - r, r) for j in range(r, upper + 1))
        + aa * sum(t(j) * math.comb(2 * j - r + 1, r) for j in range(r, upper))
    ) % p


def gaussian_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def i_power(exponent: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[exponent % 4]


def ell(exponent: int, epsilon: int) -> int:
    first = gaussian_multiply((2 * epsilon, -1), i_power(3 * (exponent + 1)))
    second = gaussian_multiply((2 * epsilon, 1), i_power(exponent + 1))
    assert first[1] + second[1] == 0
    return first[0] + second[0]


def regularized_rhs(p: int, r: int, t: int, epsilon: int, sigma_weight: list[int]) -> int:
    base = p + r + t + 1
    first = max(1, (base + p - 1) // p)
    last = (base + len(sigma_weight) - 1) // p
    total = 0
    for multiple in range(first, last + 1):
        local = multiple * p - base
        coefficient = sigma_weight[local] if 0 <= local < len(sigma_weight) else 0
        total -= coefficient * ell(multiple * p - 1, epsilon)
    return total % p


def recurrence_coefficients(p: int, r: int, s: int, t: int) -> tuple[int, int, int, int]:
    return (
        p + r + t + 1,
        -(p + 2 * r + t + 2),
        p + r + 4 * s + t + 1,
        -(p + 2 * r + 4 * s + t + 2),
    )


def second_terminal_vector(p: int, r: int, s: int) -> tuple[int, int, int, int, int]:
    epsilon = 1 if ((p - 1) // 2) % 2 == 0 else -1
    weight = convolution(power([1, -1], r), power([1, 0, 1], 2 * s - 1))
    sigma_weight = convolution([1, -1, 1, -1], weight)
    first_terminal = 2 * s + 1
    second_terminal = first_terminal + p
    values: dict[int, tuple[int, int, int]] = {0: (0, 1, 0), 1: (0, 1, 0), 2: (0, -1, 0)}

    def lower(t: int) -> tuple[int, int, int]:
        coeffs = recurrence_coefficients(p, r, s, t)
        return tuple(sum(coeffs[k] * values[t + k][i] for k in range(3)) % p for i in range(3))

    for t in range(first_terminal):
        assert regularized_rhs(p, r, t, epsilon, sigma_weight) == 0
        pivot = -recurrence_coefficients(p, r, s, t)[3] % p
        values[t + 3] = tuple(v * pow(pivot, -1, p) % p for v in lower(t))
    first_vector = lower(first_terminal)
    assert first_vector[0] == first_vector[2] == 0
    assert first_vector[1] == g_coefficient(r, s, 2 * s + 4) % p
    assert regularized_rhs(p, r, first_terminal, epsilon, sigma_weight) == -4 * epsilon % p

    values[first_terminal + 3] = (0, 0, 1)
    for t in range(first_terminal + 1, second_terminal):
        pivot = -recurrence_coefficients(p, r, s, t)[3] % p
        rhs = regularized_rhs(p, r, t, epsilon, sigma_weight)
        numerator = list(lower(t))
        numerator[0] = (numerator[0] - rhs) % p
        values[t + 3] = tuple(v * pow(pivot, -1, p) % p for v in numerator)
    rho0, rho1, rhofree = lower(second_terminal)
    assert regularized_rhs(p, r, second_terminal, epsilon, sigma_weight) == 2 * epsilon % p
    return epsilon, first_vector[1], rho0, rho1, rhofree


def ode_solution_check(r: int, s: int, degree_max: int = 16) -> None:
    n0 = 2 * r + 4 * s - 1
    weight = convolution(power([1, -1], r), power([1, 0, 1], 2 * s - 1))
    f: list[Fraction] = []
    for n in range(degree_max + 1):
        f.append(sum(Fraction(weight[k] * g_coefficient(r, s, n - k), n0 + n - k) for k in range(min(n, len(weight) - 1) + 1)))
    assert f[:3] == [Fraction(1), Fraction(1), Fraction(-1)]
    ppoly = {1: 1, 2: -1, 3: 1, 4: -1}
    qpoly = {0: n0, 1: -(r + 4 * s - 1), 2: 2 * r + 1, 3: -(r + 1)}
    rpoly = {0: n0, 1: r + 1, 2: -(r + 8 * s)}
    for n in range(degree_max + 1):
        lhs = sum(mult * (n - d + 1) * f[n - d + 1] for d, mult in ppoly.items() if 0 <= n - d + 1 < len(f))
        lhs += sum(mult * f[n - d] for d, mult in qpoly.items() if 0 <= n - d < len(f))
        assert lhs == rpoly.get(n, 0)


def main() -> None:
    rows: list[tuple[int, ...]] = []
    for p in primes_upto(199):
        for s in range(1, (p - 7) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator % 4:
                continue
            h = numerator // 4
            if h < 1:
                continue
            r = 2 * h
            a = 2 * s + 4
            ode_solution_check(r, s)
            lower = g_coefficient(r, s, a)
            upper = g_coefficient(r, s, a + p)
            aa, bb, cc = 2 * r + 4 * s - 1, r + 1, -(r + 8 * s)
            direct = aa * pi_coefficient(p, r, s, a + p) + bb * pi_coefficient(p, r, s, a + p - 1) + cc * pi_coefficient(p, r, s, a + p - 2)
            assert (upper - lower - direct) % p == 0
            assert (upper - lower - reciprocal_tail(p, r, s)) % p == 0
            epsilon, delta_plus, rho0, rho1, rhofree = second_terminal_vector(p, r, s)
            forcing = -4 * epsilon
            assert delta_plus == lower % p
            assert rhofree == 0
            assert (lower * rho0 + forcing * rho1 - forcing * upper) % p == 0
            upper_j = (p + r - 1) // 2
            t_low = (-1) ** (s + 1) * math.comb(3 * s, s + 1)
            t_high = (-1) ** upper_j * math.comb(2 * s + upper_j - 1, upper_j)
            ratio_num = (-1) ** (h + 1)
            ratio_den = 1
            for offset in range(h + 1):
                ratio_num *= 3 * s + 1 + offset
                ratio_den *= s + 2 + offset
            assert (t_high * ratio_den - t_low * ratio_num) % p == 0
            rows.append((p, h, s, lower % p, upper % p, rho0, rho1))
    payload = json.dumps(rows, separators=(",", ":")).encode("ascii")
    print(json.dumps({"prime_max": 199, "actual_rows": len(rows), "stream_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
