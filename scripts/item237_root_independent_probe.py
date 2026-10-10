#!/usr/bin/env python3
"""Independent root checks for frozen Item 237.

This probe deliberately does not import the Item 237 checker.  It evaluates
the two coefficient formulas by separate formal-series constructions, checks
the published recurrence on a longer exact range, and evaluates the published
algebraic equation on independent points of the rational parametrization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def scale(a, s):
    return trim([s * x for x in a])


def mul(a, b, degree=None):
    size = len(a) + len(b) - 1
    if degree is not None:
        size = min(size, degree + 1)
    out = [F(0)] * size
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j >= size:
                break
            out[i + j] += x * y
    return trim(out)


def derivative(a):
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def power(a, n):
    out = [F(1)]
    base = list(a)
    while n:
        if n & 1:
            out = mul(out, base)
        n //= 2
        if n:
            base = mul(base, base)
    return out


def inverse_series(a, degree):
    if a[0] == 0:
        raise ZeroDivisionError
    out = [F(1, 1) / a[0]]
    for n in range(1, degree + 1):
        out.append(
            -sum(a[j] * out[n - j] for j in range(1, min(n, len(a) - 1) + 1))
            / a[0]
        )
    return out


def q_power(exponent, degree):
    """Series for (1+y+y^2/2)^exponent from Q F'=exponent Q' F."""
    out = [F(1)]
    for n in range(degree):
        previous = out[n]
        previous_two = out[n - 1] if n else F(0)
        out.append(
            ((exponent - n) * previous + (exponent - F(n - 1, 2)) * previous_two)
            / (n + 1)
        )
    return out


def negative_binomial(power_value, degree):
    """Series for (1+y)^(-power_value), power_value a positive integer."""
    return [
        F((-1) ** j * math.comb(power_value + j - 1, j))
        for j in range(degree + 1)
    ]


Q = [F(1), F(1), F(1, 2)]
A = [F(20, 3), F(14, 3), F(4, 3)]
B = [F(2), F(-5), F(-3)]
D = [F(6), F(14), F(7), F(2)]
N = [F(432), F(2064), F(4440), F(5376), F(4044), F(1860), F(486), F(48)]


def direct_c(h):
    degree = 2 * h
    kernel = mul(
        negative_binomial(2 * h + 1, degree),
        q_power(F(4 * h + 3, 3), degree),
        degree,
    )
    linear = add(scale(A, h), B)
    value = mul(kernel, linear, degree)
    return value[degree] if degree < len(value) else F(0)


def lagrange_c(h):
    n = 2 * h
    # C'(y)=(N'D-3ND')/D^4.
    numerator = add(mul(derivative(N), D), scale(mul(N, derivative(D)), -3))
    denominator = power(D, 4)
    cprime = mul(numerator, inverse_series(denominator, n - 1), n - 1)
    psi_n = mul(
        q_power(F(2 * n, 3), n - 1),
        negative_binomial(n, n - 1),
        n - 1,
    )
    product = mul(cprime, psi_n, n - 1)
    return product[n - 1] / n


def parse_fraction(text):
    return F(text)


def recurrence_coefficient(block, h):
    scalar = parse_fraction(block["scalar"])
    core = [F(x) for x in block["remaining_core_low_to_high"]]
    core_value = sum(value * h**i for i, value in enumerate(core))
    factors = F(1)
    for numerator, denominator in block["linear_factor_roots_numerator_denominator"]:
        # The frozen factorization records the root numerator/denominator but
        # uses the primitive integer factor denominator*h-numerator.
        factors *= denominator * h - numerator
    return scalar * factors * core_value


def evaluate_parametric_polynomial(terms, y):
    y = F(y)
    q2 = y * y + 2 * y + 2
    u = 4 * y**3 * (1 + y) ** 3 / q2**2
    d = sum(value * y**i for i, value in enumerate(D))
    n = sum(value * y**i for i, value in enumerate(N))
    v = n / d**3
    value = sum(F(coefficient) * u**i * v**j for i, j, coefficient in terms)
    return value


def digest_fractions(values):
    payload = "\n".join(f"{x.numerator}/{x.denominator}" for x in values).encode()
    return hashlib.sha256(payload).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--h-max", type=int, default=82)
    args = parser.parse_args()

    frozen = json.loads(args.certificate.read_text(encoding="utf-8"))
    blocks = frozen["all_h_recurrence"]["factored_coefficients"]
    terms = frozen["algebraic_resultant"]["primitive_coefficients_u_v_value"]

    c_values = {h: direct_c(h) for h in range(1, args.h_max + 1)}
    lagrange_failures = [
        h for h in range(1, min(50, args.h_max) + 1)
        if lagrange_c(h) != c_values[h]
    ]

    recurrence_failures = []
    for h in range(1, args.h_max - 8):
        residual = sum(
            recurrence_coefficient(blocks[k], F(h)) * c_values[h + 3 * k]
            for k in range(4)
        )
        if residual:
            recurrence_failures.append([h, str(residual)])

    points = [-5, -3, -2, -1, 0, 1, 2, 4, 7, 11]
    # y=-1 makes x=0 but is still a valid nonsingular evaluation; exclude only
    # roots of D, none of which occur in this integer list.
    resultant_failures = [
        [y, str(evaluate_parametric_polynomial(terms, y))]
        for y in points
        if evaluate_parametric_polynomial(terms, y)
    ]

    coefficient_gcd = 0
    for _, _, coefficient in terms:
        coefficient_gcd = math.gcd(coefficient_gcd, abs(int(coefficient)))

    p3_nonpositive = [
        h for h in range(1, args.h_max + 1)
        if recurrence_coefficient(blocks[3], F(h)) <= 0
    ]

    result = {
        "schema": "item237-root-independent-audit-v1",
        "classification": "EXACT_INDEPENDENT_AUDIT",
        "h_max": args.h_max,
        "direct_values": len(c_values),
        "direct_digest": digest_fractions([c_values[h] for h in sorted(c_values)]),
        "lagrange_checks": min(50, args.h_max),
        "lagrange_failures": lagrange_failures,
        "recurrence_checks": max(0, args.h_max - 9),
        "recurrence_failures": recurrence_failures,
        "resultant_points": points,
        "resultant_failures": resultant_failures,
        "resultant_term_count": len(terms),
        "resultant_coefficient_gcd": coefficient_gcd,
        "resultant_degrees": [
            max(i for i, _, _ in terms),
            max(j for _, j, _ in terms),
        ],
        "p3_positive_checks": args.h_max,
        "p3_nonpositive": p3_nonpositive,
        "all_pass": not (
            lagrange_failures
            or recurrence_failures
            or resultant_failures
            or p3_nonpositive
            or len(terms) != 38
            or coefficient_gcd != 1
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
