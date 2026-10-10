#!/usr/bin/env python3
"""Independent exact checks for Item 246's bulk-residual structure."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


ACTUAL_ROWS = [
    (17, 2),
    (19, 2),
    (29, 4),
    (37, 4),
    (101, 2),
    (401, 2),
    (503, 2),
    (809, 2),
    (1009, 2),
]


def trim(values):
    values = list(values)
    while values and values[-1] == 0:
        values.pop()
    return values


def add(left, right, modulus=None):
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    if modulus is not None:
        out = [value % modulus for value in out]
    return trim(out)


def scale(values, scalar, modulus=None):
    out = [scalar * value for value in values]
    if modulus is not None:
        out = [value % modulus for value in out]
    return trim(out)


def convolution(left, right, modulus=None):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right):
            if y:
                out[i + j] += x * y
    if modulus is not None:
        out = [value % modulus for value in out]
    return trim(out)


def binomial_factor(exponent, sign, step=1, modulus=None):
    out = [0] * (step * exponent + 1)
    for k in range(exponent + 1):
        value = math.comb(exponent, k) * sign**k
        out[step * k] = value if modulus is None else value % modulus
    return out


def s_value(L, coefficients):
    return sum(F((-1) ** v * value, 2 * (L + v) + 1) for v, value in enumerate(coefficients))


def b_closed(L, coefficients):
    total = F(0)
    for v, value in enumerate(coefficients):
        nv = 2 * (L + v) + 1
        for k in range(v):
            nk = 2 * (L + k) + 1
            total += F(((-1) ** (v - k - 1)) * value, nk * nv)
    return total


def b_recursive(L, coefficients):
    degree = len(coefficients) - 1
    q = [F(0)] * (degree + 2)
    bulk = [F(0)] * (degree + 1)
    for k in range(degree, -1, -1):
        q[k] = F(coefficients[k], 2 * (L + k) + 1) - q[k + 1]
        if k < degree:
            bulk[k] = bulk[k + 1] + q[k + 1] / (2 * (L + k) + 1)
    return bulk[0] if bulk else F(0)


def b_hat(L, coefficients):
    total = F(0)
    for v in range(len(coefficients)):
        nv = 2 * (L + v) + 1
        for k in range(v):
            nk = 2 * (L + k) + 1
            total += F(((-1) ** (v - k - 1)) * coefficients[k], nk * nv)
    return total


def j_value(L, coefficients):
    return sum(F(value, (2 * (L + k) + 1) ** 2) for k, value in enumerate(coefficients))


def a_value(L, degree):
    return sum(F((-1) ** k, 2 * (L + k) + 1) for k in range(degree + 1))


def small_symbolic_checks():
    failures = []
    rows = 0
    for L in range(1, 9):
        for degree in range(1, 9):
            coefficients = [((v + 2) ** 3 - 5 * v + 7) * (-1 if v % 3 == 1 else 1) for v in range(degree + 1)]
            if b_closed(L, coefficients) != b_recursive(L, coefficients):
                failures.append(["closed_recursive", L, degree])
            for epsilon in (-1, 1):
                multiplied = add(coefficients, [0] + scale(coefficients, epsilon))
                s_expected = s_value(L, coefficients) - epsilon * s_value(L + 1, coefficients)
                b_expected = (
                    b_closed(L, coefficients)
                    + epsilon
                    * (b_closed(L + 1, coefficients) + s_value(L + 1, coefficients) / (2 * L + 1))
                )
                if s_value(L, multiplied) != s_expected:
                    failures.append(["s_factor", L, degree, epsilon])
                if b_closed(L, multiplied) != b_expected:
                    failures.append(["b_factor", L, degree, epsilon])
            reflected = list(reversed(coefficients))
            dual = -L - degree - 1
            if b_closed(L, reflected) != b_hat(dual, coefficients):
                failures.append(["reflection", L, degree])
            rhs = j_value(dual, coefficients) - s_value(dual, coefficients) * a_value(dual, degree) - b_closed(dual, coefficients)
            if b_closed(L, reflected) != rhs:
                failures.append(["reciprocity", L, degree])
            rows += 1
    # Independent parity-seed coefficient checks.
    even = [1]
    odd = []
    for R in range(0, 25):
        direct_even = [math.comb(R, 2 * j) for j in range(R // 2 + 1)]
        direct_odd = [math.comb(R, 2 * j + 1) for j in range((R - 1) // 2 + 1)] if R else []
        if trim(even) != trim(direct_even) or trim(odd) != trim(direct_odd):
            failures.append(["seed", R])
        even, odd = add(even, [0] + odd), add(even, odd)
    return failures, rows


def actual_polynomial(p, s, nu, modulus):
    r = (p - 6 * s - 3) // 2
    result = binomial_factor(r, -1, modulus=modulus)
    result = convolution(result, binomial_factor(1 + 3 * nu, 1, modulus=modulus), modulus)
    result = convolution(result, binomial_factor(2 * s - nu, 1, step=2, modulus=modulus), modulus)
    return r, result


def f_polynomial(p, s):
    r = (p - 6 * s - 3) // 2
    result = binomial_factor(r, -1, modulus=p)
    result = convolution(result, [1, 1], p)
    result = convolution(result, binomial_factor(2 * s - 1, 1, step=2, modulus=p), p)
    return r, result


def b_mod(p, L, coefficients):
    total = 0
    for v, value in enumerate(coefficients):
        nv = 2 * (L + v) + 1
        for k in range(v):
            nk = 2 * (L + k) + 1
            total += ((-1) ** (v - k - 1)) * value * pow(nk * nv, -1, p)
    return total % p


def actual_pair_check(p, s):
    failures = []
    r, f = f_polynomial(p, s)
    delta = r % 2
    even = trim(f[0::2])
    odd = trim(f[1::2])
    if delta == 0:
        a, c = even, odd
    else:
        a, c = odd, even
    if not c:
        failures.append("companion_zero")
    _, p0 = actual_polynomial(p, s, 0, p)
    _, p1 = actual_polynomial(p, s, 1, p)
    d0 = trim(p0[delta::2])
    d1 = trim(p1[delta::2])
    rhs0 = convolution([1, 1], a, p)
    rhs1 = add(
        convolution([1, 3], a, p),
        ([0] if delta == 0 else []) + convolution([3, 1], c, p),
        p,
    )
    if d0 != rhs0:
        failures.append("D0_pair")
    if d1 != rhs1:
        failures.append("D1_pair")
    lower = (r + 1) // 2
    pole_separated = []
    bulk = []
    for d_values in (d0, d1):
        degree = len(d_values) - 1
        bound = 2 * lower + degree + 1
        largest = 2 * (lower + degree) + 1
        if not (0 < bound < p and largest < p):
            failures.append("pole_range")
        pole_separated.append(bound % p != 0)
        bulk.append(b_mod(p, lower, d_values))
    if not all(pole_separated):
        failures.append("pole_collision")
    return {
        "p": p,
        "s": s,
        "r": r,
        "delta": delta,
        "bulk": bulk,
        "companion_degree": len(c) - 1,
        "failures": failures,
    }


def exact_witness_37():
    p, s, nu = 37, 4, 0
    r, polynomial = actual_polynomial(p, s, nu, None)
    delta = r % 2
    selected = trim(polynomial[delta::2])
    lower = (r + 1) // 2
    value = b_closed(lower, selected)
    numerator = value.numerator
    valuation = 0
    remaining = abs(numerator)
    while remaining and remaining % p == 0:
        valuation += 1
        remaining //= p
    return {
        "value": f"{value.numerator}/{value.denominator}",
        "numerator": value.numerator,
        "denominator": value.denominator,
        "p_adic_numerator_valuation": valuation,
        "mod_p": numerator * pow(value.denominator, -1, p) % p,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    failures, symbolic_rows = small_symbolic_checks()
    actual = [actual_pair_check(p, s) for p, s in ACTUAL_ROWS]
    failures.extend([["actual", row] for row in actual if row["failures"]])
    witness = exact_witness_37()
    expected_value = "-140105504768/121628516625"
    if (
        witness["value"] != expected_value
        or witness["p_adic_numerator_valuation"] != 1
        or witness["mod_p"] != 0
    ):
        failures.append(["witness_37", witness])

    digest_payload = "\n".join(
        f"{row['p']},{row['s']},{row['r']},{row['bulk'][0]},{row['bulk'][1]}"
        for row in actual
    )
    result = {
        "schema": "item246-root-independent-audit-v1",
        "classification": "EXACT_INDEPENDENT_AUDIT",
        "symbolic_fraction_rows": symbolic_rows,
        "actual_rows": actual,
        "maximum_prime": max(p for p, _ in ACTUAL_ROWS),
        "actual_bulk_digest": hashlib.sha256(digest_payload.encode("ascii")).hexdigest(),
        "witness_37": witness,
        "failures": failures,
        "all_pass": not failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
