#!/usr/bin/env python3
"""Dependency-free exact root audit for the Item 251 A_s recurrence.

This is deliberately independent of the Item 251 implementation.  It checks
the proposed telescoping certificate in Q[u] at enough exact integer values of
s to certify the cleared coefficient polynomials (degree at most six), and it
separately checks the integral, binomial, diagonal, and recurrence formulas.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def add(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a: list[F], c: F) -> list[F]:
    return [c * value for value in a]


def mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def derivative(a: list[F]) -> list[F]:
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def b_value(s: int) -> F:
    return F(math.factorial(2 * s - 1) * math.factorial(s - 1), math.factorial(3 * s - 1))


def a_binomial(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def a_diagonal(s: int) -> int:
    # [x^(s-1)] ((2+x)^(3s-1)-1)/(1+x).
    main = sum(
        (-1) ** (s - 1 - j) * math.comb(3 * s - 1, j) * 2 ** (3 * s - 1 - j)
        for j in range(s)
    )
    return main - (-1) ** (s - 1)


def e_integral(s: int) -> F:
    return sum(F(math.comb(2 * s - 1, j), s + j) for j in range(2 * s))


def recurrence_residual(s: int) -> int:
    a0, a1, a2 = a_binomial(s), a_binomial(s + 1), a_binomial(s + 2)
    c0 = -6 * (3 * s + 1) * (3 * s + 2) * (28 * s + 39)
    c1 = -(1456 * s**3 + 3456 * s**2 + 2303 * s + 435)
    c2 = (s + 1) * (2 * s + 3) * (28 * s + 11)
    return c0 * a0 + c1 * a1 + c2 * a2


def certificate_residual(s: int) -> list[F]:
    c0 = -6 * (3 * s + 1) * (3 * s + 2) * (28 * s + 39)
    c1 = -(1456 * s**3 + 3456 * s**2 + 2303 * s + 435)
    c2 = (s + 1) * (2 * s + 3) * (28 * s + 11)
    b0 = b_value(s)
    d0 = F(c0)
    d1 = F(c1) * b0 / b_value(s + 1)
    d2 = F(c2) * b0 / b_value(s + 2)

    rpoly = [F(0), F(1), F(2), F(1)]  # u(1+u)^2
    lhs = add([d0], add(scale(rpoly, d1), scale(mul(rpoly, rpoly), d2)))

    # P is listed in increasing powers of u.
    ppoly = [
        F(448 * s**2 + 848 * s + 312),
        F(2016 * s**2 + 3648 * s + 1182),
        F(2380 * s**2 + 4211 * s + 1287),
        F(1176 * s**2 + 2058 * s + 627),
        F(252 * s**2 + 435 * s + 132),
    ]
    prefactor = F(3 * (3 * s + 1) * (3 * s + 2), 4 * s * (2 * s + 1))
    hpoly = scale(mul([F(0), F(-1), F(0), F(1)], ppoly), prefactor)
    # H/u and H/(1+u) are evaluated after their visible factors cancel.
    h_over_u = scale(mul([F(-1), F(0), F(1)], ppoly), prefactor)
    h_over_one_plus_u = scale(mul([F(0), F(-1), F(1)], ppoly), prefactor)
    rhs = add(
        derivative(hpoly),
        add(scale(h_over_u, F(s - 1)), scale(h_over_one_plus_u, F(2 * s - 1))),
    )
    return add(lhs, scale(rhs, F(-1)))


def main() -> None:
    # After multiplication by 4*s*(s+1)*(2*s+1), every coefficient
    # residual is a polynomial in s of degree <= 6.  Seven distinct exact
    # values therefore certify the rational-function identity; we use eight.
    interpolation_points = list(range(1, 9))
    certificate_checks = []
    for s in interpolation_points:
        residual = certificate_residual(s)
        assert residual == [F(0)], (s, residual)
        certificate_checks.append((s, len(residual)))

    rows = []
    for s in range(1, 51):
        a = a_binomial(s)
        assert a == a_diagonal(s)
        assert e_integral(s) == b_value(s) * a
        assert recurrence_residual(s) == 0
        rows.append((s, a, a_diagonal(s)))
    assert rows[0][1] == 3 and rows[1][1] == 49

    digest_payload = "".join(f"{s},{a},{d}\n" for s, a, d in rows).encode("ascii")
    result = {
        "schema": "item251-root-telescoping-audit-v1",
        "imports_item_code": False,
        "cleared_s_degree_bound": 6,
        "exact_interpolation_points": interpolation_points,
        "telescoping_certificate_zero": True,
        "endpoint_factors": ["u", "u-1"],
        "independent_rows": len(rows),
        "A_1": 3,
        "A_2": 49,
        "binomial_diagonal_integral_equalities": len(rows),
        "recurrence_equalities": len(rows),
        "row_digest_sha256": hashlib.sha256(digest_payload).hexdigest(),
        "scope": "exact recurrence and representations only; no modular nonvanishing or density conclusion",
    }
    output = HERE / "item251_root_telescoping_audit.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
