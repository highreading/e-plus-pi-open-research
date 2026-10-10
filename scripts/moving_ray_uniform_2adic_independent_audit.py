#!/usr/bin/env python3
"""Independent audit calculations for the moving-ray note (temporary)."""

from __future__ import annotations

from math import comb
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "_sympy"))
import sympy as sp


x, z = sp.symbols("x z")
W = 1 - z + z**2 - z**3


def independent_determinant(b: int, parity: int) -> sp.Poly:
    """Build the two-state determinant directly from the rho recurrence.

    Here x=2m.  Modulo p=5x+b, the exact-derivative recurrence is
      (k+5-3b) rho[k+4] + (2x+b-1-k) rho[k] = 0.
    """
    k0 = 3 * b - 5
    max_degree = 3 * b - 3
    low_zero = k0 % 4
    anchor = (b - 1) % 4
    high_zero = (-1 if parity == 0 else 1) % 4
    other = (high_zero + 2) % 4
    zero = (sp.Integer(0), sp.Integer(0))
    rho: dict[int, tuple[sp.Expr, sp.Expr]] = {
        low_zero: zero,
        anchor: (sp.Integer(1), sp.Integer(0)),
        high_zero: zero,
        other: (sp.Integer(0), sp.Integer(1)),
    }
    for k in range(max_degree - 3):
        if k not in rho:
            continue
        divisor = k - k0
        if divisor == 0:
            rho[k] = zero
            continue
        factor = -(2 * x + b - 1 - k) / sp.Integer(divisor)
        rho[k + 4] = tuple(sp.expand(factor * entry) for entry in rho[k])

    rows = []
    for exponent in (b - 1, b - 2):
        polynomial = sp.Poly(sp.expand(W**exponent), z)
        row = [sp.Integer(0), sp.Integer(0)]
        for (degree,), coefficient in polynomial.terms():
            row[0] += coefficient * rho[degree][0]
            row[1] += coefficient * rho[degree][1]
        rows.append(tuple(sp.expand(entry) for entry in row))
    determinant = sp.expand(rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0])
    return sp.Poly(determinant, x, domain=sp.QQ)


def universal_product(b: int) -> sp.Poly:
    result = sp.Integer(1)
    for j in range(1, b - 1, 2):
        result *= x**2 - j**2
    for j in range(1, b - 3, 2):
        if 2 * j > b:
            result *= x + j
    return sp.Poly(result, x, domain=sp.QQ)


def row_signature(b: int, parity: int) -> tuple[int, int, int, str]:
    determinant = independent_determinant(b, parity)
    universal = universal_product(b)
    quotient = determinant.exquo(universal)
    transformed = sp.Poly(
        sp.expand(quotient.as_expr().subs(x, (2 * z - b) / 5) / 2 ** (b - 3)),
        z,
        domain=sp.QQ,
    )
    low = list(reversed(transformed.all_coeffs()))
    assert all(int(coefficient.q) % 2 for coefficient in low)
    mask = sum((int(coefficient.p) & 1) << degree for degree, coefficient in enumerate(low))
    return determinant.degree(), universal.degree(), transformed.degree(), hex(mask)


def convolution(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def power(base: list[int], exponent: int, prime: int) -> list[int]:
    result = [1]
    while exponent:
        if exponent & 1:
            result = convolution(result, base, prime)
        base = convolution(base, base, prime)
        exponent >>= 1
    return result


def direct_j_values(m: int, b: int) -> list[int]:
    """Compute all cyclic J_k directly in the local coordinate at y=1."""
    p = 10 * m + b
    assert sp.isprime(p)
    n, q, N = 4 * m + b, b - 2, 6 * m
    h_power = power([4, 10, 10, 5, 1], N, p)
    inverse_four = pow(4, -1, p)
    rho = []
    for k in range(p):
        coefficient = sum(
            comb(k, d) * h_power[n - 1 - d]
            for d in range(min(k, n - 1) + 1)
            if n - 1 - d < len(h_power)
        )
        rho.append(coefficient * inverse_four % p)
    w_power = power([1, -1, 1, -1], q, p)
    return [
        sum(coefficient * rho[(k + degree) % p]
            for degree, coefficient in enumerate(w_power)) % p
        for k in range(p)
    ]


def check_direct(m: int, b: int) -> None:
    p, n, q, N = 10 * m + b, 4 * m + b, b - 2, 6 * m
    j_values = direct_j_values(m, b)
    for k in range(p):
        assert (
            (k + 3*q + 5 - 5*n) * j_values[(k+4) % p]
            + (n-1-k) * j_values[k]
            + q * (j_values[(k+1) % p] - j_values[(k+2) % p]
                   + j_values[(k+3) % p])
        ) % p == 0
    rhs_polynomial = power([1, -1, 1, -1], q, p)
    rhs_polynomial = convolution(rhs_polynomial, power([1, 0, 0, 0, -1], N, p), p)
    rhs = [0] * p
    sign = -1 if q % 2 else 1
    for degree, coefficient in enumerate(rhs_polynomial):
        rhs[(degree + 5) % p] = (rhs[(degree + 5) % p] + sign * coefficient) % p
    assert [4 * value % p for value in j_values] == rhs
    assert all(j_values[k] == -j_values[(n + 4 - k) % p] % p for k in range(p))
    q_plus_one = (j_values[0] - j_values[1] + j_values[2] - j_values[3]) % p
    formula = ((q+n-1)*j_values[0] - j_values[4]) * pow(q, -1, p) % p
    assert q_plus_one == formula
    print("direct", m, b, p, j_values[:8], "checks=ok")


def main() -> None:
    requested = [(7, 0), (7, 1), (9, 0), (9, 1), (13, 0), (13, 1),
                 (57, 0), (57, 1), (101, 0), (101, 1)]
    for b, parity in requested:
        print("row", b, parity, row_signature(b, parity))
    for m, b in ((1, 7), (1, 9), (2, 11), (4, 13)):
        check_direct(m, b)
    examples: dict[int, tuple[int, int, int] | None] = {0: None, 1: None, 4: None}
    for b in range(7, 60, 2):
        if b % 5 == 0:
            continue
        for m in range(1, 20):
            p = 10 * m + b
            if not sp.isprime(p):
                continue
            values = direct_j_values(m, b)
            for index in examples:
                if examples[index] is None and values[index] == 0:
                    examples[index] = (m, b, p)
            if all(value is not None for value in examples.values()):
                break
        if all(value is not None for value in examples.values()):
            break
    print("individual-zero examples", examples)


if __name__ == "__main__":
    main()
