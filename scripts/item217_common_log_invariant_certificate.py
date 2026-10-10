#!/usr/bin/env python3
"""Deterministic certificate for Item 217's common-log invariants.

The companion report proves the all-index statements.  This checker is
standalone and uses only exact integer arithmetic.  It verifies the constant-
term telescoper, the contiguous relation, its resultant degeneracy sets, the
two frozen-cell reductions, the scalar five-coordinate incidence, and a
bounded finite replay.  Output contains no host path, clock, or external
numeric-backend field.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item217_common_log_invariant_certificate.json"

DEPENDENCIES = {
    "sources/item197_common_log_locus_report.md":
        "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "scripts/item197_common_log_locus_certificate.py":
        "f85c36169c7eb0aee3fb73f8030d3ddb2296b00077370012be84479eea9aeeb9",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "scripts/item200_common_log_gcd_certificate.py":
        "26ef60a6f89d569d7f22fdd504dd76f5b3b6a2c11d9b99f2c56a0be645c1396b",
    "sources/item203_common_log_global_report.md":
        "dd48928d9e9535e1ffbbc960df4db9acbd161760a5aa06fca28e6f34f8993f67",
    "scripts/item203_common_log_global_certificate.py":
        "711a8fe500caf934cff62373f062f13abb9fa4c9f0306d0e795ac0a27b992df0",
}

A_POLY = [1, -3, 2]
D_POLY = [1, -2, 2]


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                out[i + j] += a * b
    return trim(out)


def power(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    base = poly[:]
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        exponent >>= 1
        if exponent:
            base = mul(base, base)
    return out


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def z_derivative(poly: list[int]) -> list[int]:
    """z*d/dz, preserving coefficient indices."""
    return [index * value for index, value in enumerate(poly)]


def recurrence_coefficients(m: int) -> tuple[int, int, int, int]:
    a = -6 * (3 * m + 1) * (6 * m + 1) * (6 * m + 5) * (
        1480100 * m**4
        + 3217800 * m**3
        + 2450801 * m**2
        + 775695 * m
        + 85874
    )
    b = -32 * (m + 1) * (2 * m + 1) * (4 * m + 1) * (4 * m + 3) * (
        8700 * m**3 + 22100 * m**2 + 16887 * m + 3782
    )
    d = 15 * (3 * m + 1) * (4 * m + 1) * (6 * m + 1) * (6 * m + 5) * (
        59204 * m**3 + 113256 * m**2 + 68461 * m + 13149
    )
    e = (
        80
        * (m + 1)
        * (2 * m + 1)
        * (4 * m + 1)
        * (4 * m + 3)
        * (4 * m + 5)
        * (6 * m + 5)
        * (58 * m + 23)
    )
    return a, b, d, e


def telescoper_n(m: int) -> list[int]:
    """Coefficients [z^i]N(z,m), 0<=i<=13, in the CT certificate."""
    return [
        -80 * (m + 1) * (2 * m + 1) * (4 * m + 1) * (4 * m + 3)
        * (6 * m + 5) * (58 * m + 23),
        8 * (2 * m + 1) * (4 * m + 1) * (4 * m + 3)
        * (17400 * m**3 + 38020 * m**2 + 26182 * m + 5507),
        -8 * (2 * m + 1) * (4 * m + 1)
        * (125280 * m**4 + 349200 * m**3 + 354924 * m**2 + 155348 * m + 24619),
        8 * (4 * m + 1)
        * (139200 * m**5 + 333080 * m**4 + 255036 * m**3
           + 46294 * m**2 - 20753 * m - 6496),
        -91456080 * m**6 - 288126560 * m**5 - 357261560 * m**4
        - 221319592 * m**3 - 71585857 * m**2 - 11314848 * m - 666303,
        -103928400 * m**6 - 373420080 * m**5 - 541356480 * m**4
        - 403794748 * m**3 - 162808543 * m**2 - 33515702 * m - 2740607,
        -2 * (189593760 * m**6 + 606314080 * m**5 + 766344616 * m**4
              + 486681116 * m**3 + 162661704 * m**2 + 26896059 * m + 1694525),
        -2 * (192266400 * m**6 + 663294400 * m**5 + 921293032 * m**4
              + 657913892 * m**3 + 254305288 * m**2 + 50366283 * m + 3986005),
        -2 * (6 * m + 1)
        * (47955240 * m**5 + 145978020 * m**4 + 171228626 * m**3
           + 96390583 * m**2 + 25989349 * m + 2684402),
        -2 * (287731440 * m**6 + 977692080 * m**5 + 1334965240 * m**4
              + 935714968 * m**3 + 354744203 * m**2 + 68942327 * m + 5364342),
        -2 * (6 * m + 1) * (6 * m + 5)
        * (5328360 * m**4 + 11801600 * m**3 + 9245444 * m**2
           + 3053065 * m + 360331),
        -2 * (6 * m + 5)
        * (31970160 * m**5 + 81033720 * m**4 + 77988992 * m**3
           + 35824706 * m**2 + 7888543 * m + 668239),
        -9 * (6 * m + 1) * (6 * m + 5)
        * (296020 * m**4 + 656660 * m**3 + 515301 * m**2
           + 170410 * m + 20129),
        -3 * (3 * m + 1) * (6 * m + 5)
        * (1776120 * m**4 + 3874460 * m**3 + 2966102 * m**2
           + 946105 * m + 106003),
    ]


def telescoper_identity_check() -> dict:
    """Verify the cleared bivariate CT identity by degree interpolation."""
    one_minus_z = [1, -1]
    one_plus_z = [1, 1]
    dpoly = [1, 0, 1]
    max_degree = 0
    digests: list[str] = []
    # Both sides have degree at most seven in m.  Eight exact specializations
    # therefore prove their equality in Z[m,z].
    for m in range(8):
        n_poly = telescoper_n(m)
        f_poly = mul(one_minus_z, n_poly)
        first = mul(dpoly, add(z_derivative(f_poly), scale(f_poly, -5)))
        first = add(first, scale(shift(f_poly, 2), -10))
        bracket = scale(mul(shift(n_poly, 1), dpoly), -6)
        bracket = add(bracket, scale(mul(dpoly, f_poly), -4))
        bracket = add(bracket, scale(shift(f_poly, 2), -8))
        lhs = add(first, scale(bracket, m))

        a, b, d, e = recurrence_coefficients(m)
        hnum = scale(mul(mul(shift([1], 5), one_plus_z), power(dpoly, 5)), a)
        hnum = add(
            hnum,
            scale(mul(mul(mul(shift([1], 1), power(one_minus_z, 6)),
                              one_plus_z), dpoly), b),
        )
        hnum = add(
            hnum,
            scale(mul(mul(shift([1], 4), power(one_plus_z, 4)),
                      power(dpoly, 4)), d),
        )
        hnum = add(hnum, scale(mul(power(one_minus_z, 6), power(one_plus_z, 4)), e))
        if lhs != hnum:
            raise AssertionError((m, lhs, hnum))
        max_degree = max(max_degree, len(lhs) - 1)
        digests.append(hashlib.sha256(",".join(map(str, lhs)).encode("ascii")).hexdigest())
    return {
        "identity": (
            "with F=(1-z)N and d=1+z^2: "
            "d(zF'-5F)-10z^2F+m(-6zdN-4dF-8z^2F)=Hnum"
        ),
        "rational_certificate": "S=(1-z)N/(z^5(1+z^2)^5)",
        "interpolation_m_values": list(range(8)),
        "degree_bound_in_m": 7,
        "maximum_z_degree": max_degree,
        "specialization_digest": hashlib.sha256("".join(digests).encode("ascii")).hexdigest(),
    }


def scalar_coefficients(m: int) -> list[int]:
    target = 4 * m + 1
    coefficient = [1]
    for degree in range(target):
        rhs = (20 * m - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += 2 * (10 * degree + 10 - 20 * m) * coefficient[degree - 1]
        if degree >= 2:
            rhs += 4 * (10 * m - 5 * degree - 6) * coefficient[degree - 2]
        if degree >= 3:
            rhs += 8 * (degree + 1 - 4 * m) * coefficient[degree - 3]
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise AssertionError((m, degree, remainder))
        coefficient.append(quotient)
    return coefficient


def scalar_pair(m: int) -> tuple[int, int]:
    g = scalar_coefficients(m)
    n = 4 * m
    return g[n] - 2 * g[n - 1] + 2 * g[n - 2], g[n + 1]


def contiguous_relation_check(max_m: int = 80) -> dict:
    pairs = {m: scalar_pair(m) for m in range(1, max_m + 2)}
    rows = []
    for m in range(1, max_m + 1):
        a, b, d, e = recurrence_coefficients(m)
        c0, c1 = pairs[m]
        n0, n1 = pairs[m + 1]
        residue = a * c0 + b * n0 + d * c1 + e * n1
        if residue:
            raise AssertionError((m, residue))
        rows.append((m, c0, c1, n0, n1))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "verified_m_max": max_m,
        "verified_rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def bounded_relation_rank_check() -> dict:
    """Prove uniqueness in the order-one, degree-at-most-seven ansatz."""
    modulus = 1_000_000_007
    pairs = {m: scalar_pair(m) for m in range(1, 42)}
    matrix = []
    for m in range(1, 41):
        row = []
        for component in (0, 1):
            for offset in (0, 1):
                value = pairs[m + offset][component] % modulus
                row.extend(value * pow(m, degree, modulus) % modulus for degree in range(8))
        matrix.append(row)
    rank = 0
    columns = 32
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], modulus - 2, modulus)
        matrix[rank] = [value * inverse % modulus for value in matrix[rank]]
        for index in range(rank + 1, len(matrix)):
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    (left - factor * right) % modulus
                    for left, right in zip(matrix[index], matrix[rank])
                ]
        rank += 1
    if rank != 31:
        raise AssertionError(rank)
    return {
        "ansatz": "sum over nu=0,1 and i=0,1 of P_(nu,i)(m) C_nu(m+i), deg P<=7",
        "modulus": modulus,
        "matrix_rows": 40,
        "matrix_columns": columns,
        "rank": rank,
        "nullity_over_Q": 1,
        "scope": "uniqueness only in this bounded order/degree ansatz",
    }


def bareiss_determinant(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise AssertionError("Bareiss nonexact division")
                a[i][j] = quotient
        previous = pivot_value
    return sign * a[-1][-1]


def resultant(left: list[int], right: list[int]) -> int:
    left = trim(left[:])
    right = trim(right[:])
    n, m = len(left) - 1, len(right) - 1
    lf = list(reversed(left))
    rg = list(reversed(right))
    size = n + m
    matrix = []
    for offset in range(m):
        matrix.append([0] * offset + lf + [0] * (size - offset - len(lf)))
    for offset in range(n):
        matrix.append([0] * offset + rg + [0] * (size - offset - len(rg)))
    return bareiss_determinant(matrix)


def resultant_check() -> dict:
    b3 = [3782, 16887, 22100, 8700]
    e3 = mul(mul([5, 4], [5, 6]), [23, 58])
    a4 = [85874, 775695, 2450801, 3217800, 1480100]
    d4 = mul([1, 4], [13149, 68461, 113256, 59204])
    next_resultant = resultant(b3, e3)
    current_resultant = resultant(a4, d4)
    next_factors = {2: 10, 3: 3, 5: 1, 11: 1, 29: 1, 43: 1, 79: 1, 1531: 1}
    current_factors = {2: 17, 3: 4, 5: 3, 7: 2, 19: 2, 41: 1, 71: 1, 1531: 1, 2683: 1}
    for value, factors in ((next_resultant, next_factors), (current_resultant, current_factors)):
        if abs(value) != math.prod(prime**exponent for prime, exponent in factors.items()):
            raise AssertionError((value, factors))
    return {
        "current_primitive_resultant": current_resultant,
        "current_primitive_resultant_factorization": current_factors,
        "next_primitive_resultant": next_resultant,
        "next_primitive_resultant_factorization": next_factors,
        "interpretation": (
            "outside the displayed finite prime support and the explicit common linear "
            "factors, each side of the one-row relation is a nonzero projective covector"
        ),
    }


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(flags) if flag]


def convolution_mod(left: list[int], right: list[int], p: int, limit: int | None = None) -> list[int]:
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit + 1)
    out = [0] * size
    for i, a in enumerate(left):
        if a:
            for j in range(min(len(right), size - i)):
                out[i + j] = (out[i + j] + a * right[j]) % p
    return out


def power_mod(poly: list[int], exponent: int, p: int, limit: int | None = None) -> list[int]:
    out = [1]
    base = [value % p for value in poly]
    while exponent:
        if exponent & 1:
            out = convolution_mod(out, base, p, limit)
        exponent >>= 1
        if exponent:
            base = convolution_mod(base, base, p, limit)
    return out


def inverse_series_mod(poly: list[int], limit: int, p: int) -> list[int]:
    out = [1]
    for degree in range(1, limit + 1):
        out.append(-sum(poly[k] * out[degree - k]
                        for k in range(1, min(degree, len(poly) - 1) + 1)) % p)
    return out


def ratio_series_mod(a_exp: int, d_exp: int, limit: int, p: int) -> list[int]:
    left = power_mod(A_POLY, a_exp, p, limit)
    right = power_mod(inverse_series_mod(D_POLY, limit, p), d_exp, p, limit)
    out = convolution_mod(left, right, p, limit)
    return out + [0] * (limit + 1 - len(out))


def coefficient_product(left: list[int], right: list[int], index: int, p: int) -> int:
    lower = max(0, index - len(right) + 1)
    upper = min(len(left) - 1, index)
    return sum(left[k] * right[index - k] for k in range(lower, upper + 1)) % p


def fixed_coefficient(j: int, kind: str) -> int:
    exponent_minus = 3 * j + (0 if kind == "u" else 1)
    exponent_plus = 2 * j + (1 if kind == "u" else 2)
    target = 2 * j if kind != "w" else 2 * j - 1
    answer = 0
    for b in range(target // 2 + 1):
        k = target - 2 * b
        answer += (
            (-1) ** k
            * math.comb(exponent_minus, k)
            * (-1) ** b
            * math.comb(exponent_plus + b - 1, b)
        )
    return answer


def moments(p: int, s: int, nu: int) -> tuple[int, int, int]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - nu
    pnu = convolution_mod(power_mod([1, -1], r, p), power_mod([1, 1], 1 + 3 * nu, p), p)
    pnu = convolution_mod(pnu, power_mod([1, 0, 1], q, p), p)
    a_log = [0] + [(-pow(k, -1, p)) % p for k in range(1, p)]
    b_log = [0] * (2 * p - 1)
    for k in range(1, p):
        b_log[2 * k] = ((-1) ** (k - 1) * pow(k, -1, p)) % p
    target = p - q - 1
    return (
        coefficient_product(a_log, pnu, target, p),
        coefficient_product(b_log, pnu, target, p),
        coefficient_product(b_log, pnu, target + p, p),
    )


def quotient_digits(p: int, j: int, s: int) -> tuple[int, int]:
    a, c = 3 * j + 1, 2 * j + 1
    u, v, w = (fixed_coefficient(j, kind) % p for kind in ("u", "v", "w"))
    out = []
    for nu in (0, 1):
        x, y, high = moments(p, s, nu)
        out.append((a * u * x - c * (v * y + w * high)) % p)
    return out[0], out[1]


def ratio_series_integer(a_exp: int, d_exp: int, limit: int) -> list[int]:
    inverse = [1]
    for degree in range(1, limit + 1):
        inverse.append(-sum(D_POLY[k] * inverse[degree - k]
                            for k in range(1, min(degree, 2) + 1)))
    left = power(A_POLY, a_exp)
    right = power(inverse, d_exp)
    return mul(left, right)[: limit + 1] + [0] * max(0, limit + 1 - len(mul(left, right)))


def j_vector(j: int) -> tuple[int, int, int, int]:
    a, c = 3 * j + 1, 2 * j + 1
    first = ratio_series_integer(a - 1, c, c - 1)
    second = ratio_series_integer(a, c + 1, c - 1)
    return a * first[c - 1], a * first[c - 2], -c * second[c - 1], -c * second[c - 2]


def frobenius_delta(poly: list[int], p: int) -> list[int]:
    modulus = p * p
    powered = power_mod(poly, p, modulus)
    evaluated = [0] * len(powered)
    for degree, value in enumerate(poly):
        evaluated[p * degree] = value % modulus
    out = []
    for left, right in zip(powered, evaluated):
        difference = (left - right) % modulus
        if difference % p:
            raise AssertionError((p, poly, difference))
        out.append((difference // p) % p)
    return out


def scalar_incidence(p: int, j: int, s: int) -> tuple[list[int], tuple[int, int]]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - 1
    moving = convolution_mod(power_mod(A_POLY, r, p), power_mod(D_POLY, q, p), p)
    da = convolution_mod(frobenius_delta(A_POLY, p), moving, p)
    dd = convolution_mod(frobenius_delta(D_POLY, p), moving, p)
    length = p - 2 * s - 5
    vector = j_vector(j)
    values = []
    for t in range(1, 6):
        row = (
            da[length + t] if length + t < len(da) else 0,
            da[p + length + t] if p + length + t < len(da) else 0,
            dd[length + t] if length + t < len(dd) else 0,
            dd[p + length + t] if p + length + t < len(dd) else 0,
        )
        values.append(sum(x * y for x, y in zip(row, vector)) % p)
    c0_digit = (values[3] - 2 * values[2] + 2 * values[1]) % p
    c1_digit = values[4]
    return values, (c0_digit, c1_digit)


def finite_cell_replay(prime_max: int, incidence_prime_max: int) -> dict:
    counts = {
        1: {"rows": 0, "q0_zero": 0, "q1_zero": 0, "common_zero": 0},
        2: {"rows": 0, "q0_zero": 0, "q1_zero": 0, "common_zero": 0},
    }
    rows = []
    incidence_rows = 0
    integer_bridge_rows = 0
    for p in primes_upto(prime_max):
        if p <= 7:
            continue
        for j in (1, 2):
            for s in range(1, (p - 3) // 6 + 1):
                numerator = (2 * j + 1) * p - 2 * s - 1
                if numerator % 4:
                    continue
                m = numerator // 4
                q0, q1 = quotient_digits(p, j, s)
                counts[j]["rows"] += 1
                counts[j]["q0_zero"] += q0 == 0
                counts[j]["q1_zero"] += q1 == 0
                counts[j]["common_zero"] += q0 == q1 == 0
                if j == 1:
                    y_conditions = []
                    for nu in (0, 1):
                        _, y, high = moments(p, s, nu)
                        y_conditions.append((2 * high - y) % p)
                    if (q0, q1) != tuple(6 * value % p for value in y_conditions):
                        raise AssertionError((p, j, s, q0, q1, y_conditions))
                else:
                    conditions = []
                    for nu in (0, 1):
                        x, y, high = moments(p, s, nu)
                        conditions.append((9 * x - 10 * y + high) % p)
                    if (q0, q1) != tuple(-35 * value % p for value in conditions):
                        raise AssertionError((p, j, s, q0, q1, conditions))
                if p <= incidence_prime_max:
                    values, scalar_pair_digits = scalar_incidence(p, j, s)
                    if scalar_pair_digits != (q0, q1):
                        raise AssertionError((p, j, s, values, scalar_pair_digits, q0, q1))
                    residuals = (
                        values[3],
                        (values[2] - 2 * values[0]) % p,
                        (values[1] - 2 * values[0]) % p,
                    )
                    if (q0 == q1 == 0) != all(value == 0 for value in residuals):
                        raise AssertionError((p, j, s, values, residuals))
                    incidence_rows += 1
                if p <= 31:
                    raw0, raw1 = scalar_pair(m)
                    if raw0 % p or raw1 % p:
                        raise AssertionError((p, j, s, m, "missing forced factor"))
                    if (raw0 // p % p, raw1 // p % p) != (q0, q1):
                        raise AssertionError((p, j, s, m, raw0, raw1, q0, q1))
                    integer_bridge_rows += 1
                rows.append((p, j, s, m, q0, q1))
    if any(counts[j]["common_zero"] for j in (1, 2)):
        raise AssertionError(counts)
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        "incidence_crosscheck_prime_max": incidence_prime_max,
        "incidence_crosscheck_rows": incidence_rows,
        "integer_bridge_prime_max": 31,
        "integer_bridge_rows": integer_bridge_rows,
        "j1": counts[1],
        "j2": counts[2],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": "zero observed collisions is not an all-prime theorem",
    }


def finite_log_functional_check(prime_max: int = 43) -> dict:
    checks = 0
    for p in primes_upto(prime_max):
        if p <= 3:
            continue
        a_log = [0] + [(-pow(k, -1, p)) % p for k in range(1, p)]
        # A_p(z)=A_p(1-z).
        transformed = [0]
        for k in range(1, p):
            term = power_mod([1, -1], k, p)
            term = [(a_log[k] * value) % p for value in term]
            if len(transformed) < len(term):
                transformed += [0] * (len(term) - len(transformed))
            for index, value in enumerate(term):
                transformed[index] = (transformed[index] + value) % p
        transformed += [0] * (len(a_log) - len(transformed))
        if transformed[:len(a_log)] != a_log:
            raise AssertionError((p, "one-minus"))
        # A_p(z)=-z^p A_p(1/z), coefficientwise.
        if any((a_log[k] + a_log[p - k]) % p for k in range(1, p)):
            raise AssertionError((p, "inversion"))
        # B_p(z)=A_p(-z^2)=A_p(1+z^2), using the first functional equation.
        b_direct = [0] * (2 * p - 1)
        for k in range(1, p):
            b_direct[2 * k] = ((-1) ** (k - 1) * pow(k, -1, p)) % p
        b_sub = [0]
        for k in range(1, p):
            term = power_mod([1, 0, 1], k, p)
            term = [(a_log[k] * value) % p for value in term]
            if len(b_sub) < len(term):
                b_sub += [0] * (len(term) - len(b_sub))
            for index, value in enumerate(term):
                b_sub[index] = (b_sub[index] + value) % p
        b_sub += [0] * (len(b_direct) - len(b_sub))
        if b_sub[:len(b_direct)] != b_direct:
            raise AssertionError((p, "quadratic substitution"))
        checks += 1
    return {
        "prime_max": prime_max,
        "prime_checks": checks,
        "identities": [
            "A_p(z)=A_p(1-z)",
            "A_p(z)=-z^p A_p(1/z)",
            "B_p(z)=A_p(-z^2)=A_p(1+z^2)",
        ],
        "outcome": (
            "the identities are exact, but after multiplication by P_nu and "
            "coefficient extraction they do not identify the two required moments"
        ),
    }


def cartier_degree(p: int, n: int, k: int) -> int:
    r, t = n % p, k % p
    return 2 * r if t == 0 else 2 * r + 3 * (p - t)


def forced_primes(m: int, primes: list[int]) -> list[int]:
    return [
        p for p in primes
        if p & 1
        and cartier_degree(p, 6 * m, 4 * m + 1) <= p - 2
        and cartier_degree(p, 6 * m, 4 * m + 2) <= p - 2
    ]


def normalization_counterexample() -> dict:
    primes = primes_upto(20)
    c_m = scalar_pair(1)
    c_next = scalar_pair(2)
    f_m = math.prod(forced_primes(1, primes))
    f_next = math.prod(forced_primes(2, primes))
    a, b, d, e = recurrence_coefficients(1)
    raw = a * c_m[0] + b * c_next[0] + d * c_m[1] + e * c_next[1]
    normalized = (
        a * (c_m[0] // f_m)
        + b * (c_next[0] // f_next)
        + d * (c_m[1] // f_m)
        + e * (c_next[1] // f_next)
    )
    if (f_m, f_next, raw, normalized) != (1, 11, 0, -73214064000):
        raise AssertionError((f_m, f_next, raw, normalized))
    return {
        "m": 1,
        "F_m": f_m,
        "F_m_plus_1": f_next,
        "raw_relation_residue": raw,
        "normalized_relation_residue": normalized,
        "conclusion": "the raw contiguous relation does not survive division by F_m",
    }


def rate_ledger() -> dict:
    getcontext().prec = 50
    raw = Decimal("0.0561745846664610")
    gap = Decimal("0.01963298366943179388")
    j1 = Decimal(1) / Decimal(36)
    j2 = Decimal(1) / Decimal(105)
    remaining = raw - j1 - j2
    return {
        "gap_per_6m": str(gap),
        "raw_j_ge_1_ceiling_per_6m": str(raw),
        "j1_cell_mass_per_6m": "1/36",
        "j2_cell_mass_per_6m": "1/105",
        "remaining_if_j1_j2_excluded_per_6m": str(remaining),
        "margin_below_gap_if_j1_j2_excluded": str(gap - remaining),
        "actual_j1_j2_all_prime_exclusion": "OPEN",
        "two_edge_thin_phase_bound": (
            "lower s<=S contributes <=S log(4m+1+2S); upper distance t<=T "
            "contributes <=2(T+1)log(6m); hence zero linear rate if S,T=o(m/log m)"
        ),
        "new_unconditional_linear_log_rate": 0,
        "new_divisibility_exponent": 0,
    }


def certificate(prime_max: int, incidence_prime_max: int) -> dict:
    j_vectors = {"j1": list(j_vector(1)), "j2": list(j_vector(2))}
    if j_vectors != {"j1": [-12, -12, 6, 12], "j2": [-245, 70, 315, -35]}:
        raise AssertionError(j_vectors)
    frozen = {
        "j1": [fixed_coefficient(1, kind) for kind in ("u", "v", "w")],
        "j2": [fixed_coefficient(2, kind) for kind in ("u", "v", "w")],
    }
    if frozen != {"j1": [0, 2, -4], "j2": [-45, -70, 7]}:
        raise AssertionError(frozen)
    return {
        "item": 217,
        "classification": {
            "PROVED": [
                "the exact all-m constant-term contiguous relation and rational telescoper",
                "factorization and finite resultant support of both primitive coefficient covectors",
                "the exact scalar five-coordinate incidence M_(p,s)J_j=0 retaining the initial state",
                "j=1 reduces to 2Y'_nu-Y_nu=0 for nu=0,1",
                "j=2 reduces to 9X_nu-10Y_nu+Y'_nu=0 for nu=0,1",
                "both lower and upper o(m/log m) phase edges have zero linear log rate",
            ],
            "OPEN": [
                "all-prime exclusion for the j=1 and j=2 frozen-cell congruences",
                "any positive linear-rate saving from the normalized common-log radical",
                "a subexponential bound for gcd(C_0/F_m,C_1/F_m)",
            ],
            "EXACT_FINITE_ONLY": [
                f"absence of j=1,j=2 collisions through p<={prime_max}",
            ],
        },
        "contiguous_relation": {
            "formula": "A_m C0(m)+B_m C0(m+1)+D_m C1(m)+E_m C1(m+1)=0",
            "constant_term_basis": {
                "R": "(1-z)^6/(z^4(1+z^2)^4)",
                "f0": "(1+z)/(1+z^2)",
                "f1": "(1+z)^4/(z(1+z^2)^2)",
                "Cnu": "CT R^m fnu",
            },
            "telescoper": telescoper_identity_check(),
            "finite_regression": contiguous_relation_check(),
            "bounded_ansatz_uniqueness": bounded_relation_rank_check(),
            "resultants": resultant_check(),
            "normalization_counterexample": normalization_counterexample(),
            "scoped_no_go": (
                "one primitive order-one scalar relation supplies only one projective "
                "condition on the neighboring divided pair; nonzero resultants do not "
                "turn that one covector into a zero-propagation theorem"
            ),
        },
        "five_coordinate_incidence": {
            "J_definition": (
                "(a[y^(c-1)]A^(a-1)/D^c, a[y^(c-2)]A^(a-1)/D^c, "
                "-c[y^(c-1)]A^a/D^(c+1), -c[y^(c-2)]A^a/D^(c+1))"
            ),
            "vectors": j_vectors,
            "row_definition": (
                "w_t=([v^(L+t)]DeltaA P,[v^(p+L+t)]DeltaA P," 
                "[v^(L+t)]DeltaD P,[v^(p+L+t)]DeltaD P), t=1..5"
            ),
            "common_log_matrix": "rows w4, w3-2w1, w2-2w1 annihilate J_j",
        },
        "frozen_item197_coordinates": {
            "UVW": frozen,
            "j1_primitive_conditions": "2Y'_0-Y_0=2Y'_1-Y_1=0 mod p",
            "j2_primitive_conditions": "9X_0-10Y_0+Y'_0=9X_1-10Y_1+Y'_1=0 mod p",
            "finite_log_functional_equations": finite_log_functional_check(),
            "admissibility_outcome": (
                "the primitive scalar factors are 6 and -35, so admissibility does "
                "not restrict p to finite support; moving truncated-log moments remain"
            ),
        },
        "finite_cell_replay": finite_cell_replay(prime_max, incidence_prime_max),
        "two_edge_phase_theorem": {
            "lower_identity": "4m+1+2s=(2j+1)p",
            "upper_p_1_mod_6_identity": "6m-2-3t=(3j+1)p",
            "upper_p_5_mod_6_identity": "6m-1-3t=(3j+1)p",
            "scope": "all candidate primes, hence also all common-log primes",
        },
        "rate_ledger": rate_ledger(),
        "dependency_sha256": DEPENDENCIES,
        "runtime": {"external_numeric_backend": None},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=199)
    parser.add_argument("--incidence-prime-max", type=int, default=61)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.incidence_prime_max > args.prime_max:
        raise SystemExit("incidence maximum must not exceed prime maximum")
    result = certificate(args.prime_max, args.incidence_prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "output": str(args.output),
        "j1_rows": result["finite_cell_replay"]["j1"]["rows"],
        "j2_rows": result["finite_cell_replay"]["j2"]["rows"],
        "common_zeros": (
            result["finite_cell_replay"]["j1"]["common_zero"]
            + result["finite_cell_replay"]["j2"]["common_zero"]
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
