#!/usr/bin/env python3
"""Exact checks for the aggregate finite-shift/first-jet no-go theorem."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


def sequences(limit: int) -> tuple[list[int], list[int], list[int]]:
    q = [1, 1]
    p = [1, 3]
    b = [0, 4]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
        p.append((4 * n - 2) * p[-1] + p[-2])
        b.append((4 * n - 2) * b[-1] + b[-2] + 4 * q[n - 1])
    return q, p, b


def valuation_nonzero(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_aggregate_shift_jet_product_formula_no_go_certificate.json"
        ),
    )
    args = parser.parse_args()

    x, F, G, X, Y, K = sp.symbols("x F G X Y K")
    maximum_shift = 8
    U = [sp.Integer(1), sp.Integer(0)]
    V = [sp.Integer(0), sp.Integer(1)]
    for j in range(1, maximum_shift):
        coefficient = 4 * x + 4 * j + 2
        U.append(sp.expand(-coefficient * U[j] + U[j - 1]))
        V.append(sp.expand(-coefficient * V[j] + V[j - 1]))

    for j in range(maximum_shift):
        assert sp.expand(U[j] * V[j + 1] - U[j + 1] * V[j]) == (-1) ** j

    limit = 28
    q, p, b = sequences(limit + maximum_shift + 1)
    value_reduction_checks = 0
    jet_reduction_checks = 0
    for n in range(0, limit + 1):
        sign_n = -1 if n % 2 else 1
        f0 = sign_n * q[n]
        f1 = -sign_n * q[n + 1]
        d0 = (
            (-sign_n * p[n]),
            sign_n * b[n],
        )
        d1 = (
            sign_n * p[n + 1],
            -sign_n * b[n + 1],
        )
        for j in range(maximum_shift + 1):
            uj = int(U[j].subs(x, n))
            vj = int(V[j].subs(x, n))
            target_sign = -1 if (n + j) % 2 else 1
            assert uj * f0 + vj * f1 == target_sign * q[n + j]
            value_reduction_checks += 1

            up = int(sp.diff(U[j], x).subs(x, n))
            vp = int(sp.diff(V[j], x).subs(x, n))
            reduced_pair = (
                uj * d0[0] + vj * d1[0],
                up * f0 + vp * f1 + uj * d0[1] + vj * d1[1],
            )
            target_jet_sign = -1 if (n + j + 1) % 2 else 1
            target_pair = (
                target_jet_sign * p[n + j],
                -target_jet_sign * b[n + j],
            )
            assert reduced_pair == target_pair
            jet_reduction_checks += 1

    sample_cofactor = (
        (x + 2) * G
        + (F - 3 * G) * X
        + (2 * F + G) * Y
        + (X + 2 * Y) ** 2
    )
    coefficientwise_checks = 0
    coefficientwise_records = []
    for n in (0, 1, 2, 4, 7, 11):
        sign_n = -1 if n % 2 else 1
        substitution = {
            x: n,
            F: sign_n * q[n],
            G: -sign_n * q[n + 1],
            X: -sign_n * (p[n] * K - b[n]),
            Y: sign_n * (p[n + 1] * K - b[n + 1]),
        }
        for order in (1, 2, 3):
            psi = sp.Poly(
                sp.expand((F**order * sample_cofactor).subs(substitution)), K
            )
            divisor = q[n] ** order
            assert all(int(coefficient) % divisor == 0 for coefficient in psi.all_coeffs())
            coefficientwise_checks += len(psi.all_coeffs())
            coefficientwise_records.append(
                {
                    "n": n,
                    "formal_root_order": order,
                    "q_power_divisor": divisor,
                    "degree_in_K": psi.degree(),
                    "coefficient_count": len(psi.all_coeffs()),
                }
            )

    adjacent_records = []
    for n in range(0, 18):
        assert math.gcd(p[n], p[n + 1]) == 1
        sign_n = -1 if n % 2 else 1
        x_pair = (-sign_n * p[n], sign_n * b[n])
        y_pair = (sign_n * p[n + 1], -sign_n * b[n + 1])
        combined = (
            p[n + 1] * x_pair[0] + p[n] * y_pair[0],
            p[n + 1] * x_pair[1] + p[n] * y_pair[1],
        )
        expected_integer = sign_n * (
            p[n + 1] * b[n] - p[n] * b[n + 1]
        )
        assert combined == (0, expected_integer)
        adjacent_records.append(
            {
                "n": n,
                "primitive_coefficients": [p[n + 1], p[n]],
                "integer_after_K_cancellation": expected_integer,
            }
        )

    aggregate_records = []
    prime_sets = [(4, [7, 11, 13]), (8, [13]), (18, [7])]
    for n, primes in prime_sets:
        smooth_divisor = 1
        valuations = {}
        for prime in primes:
            exponent = valuation_nonzero(q[n], prime)
            valuations[str(prime)] = exponent
            smooth_divisor *= prime**exponent
        assert q[n] % smooth_divisor == 0
        for order in (1, 2, 3):
            integer_auxiliary = q[n] ** order * (2 * n + 1)
            assert integer_auxiliary % (smooth_divisor**order) == 0
        aggregate_records.append(
            {
                "n": n,
                "q_n": q[n],
                "prime_valuations": valuations,
                "aggregate_divisor": smooth_divisor,
            }
        )

    result = {
        "description": (
            "Exact regression checks for four-generator shift/first-jet "
            "reduction, formal F-adic root factors, coefficientwise q_n "
            "divisibility after Euler-constant elimination, and aggregate "
            "product-formula divisibility."
        ),
        "maximum_shift": maximum_shift,
        "integer_center_limit": limit,
        "value_reduction_checks": value_reduction_checks,
        "jet_reduction_checks": jet_reduction_checks,
        "coefficientwise_divisibility_checks": coefficientwise_checks,
        "coefficientwise_records": coefficientwise_records,
        "adjacent_jet_records": adjacent_records,
        "aggregate_records": aggregate_records,
        "scope_warning": (
            "Finite checks certify identities only. The theorem covers "
            "orders forced formally by the finite shift/first-jet algebra; "
            "it does not bound special residual values at actual roots or "
            "prove any estimate for v_p(q_n)."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
