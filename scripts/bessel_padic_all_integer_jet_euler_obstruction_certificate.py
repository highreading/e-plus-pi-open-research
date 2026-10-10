#!/usr/bin/env python3
"""Exact regression checks for the all-integer Euler-jet obstruction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def valuation_nonzero(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def sequences(limit: int) -> tuple[list[int], list[int], list[int]]:
    q = [1, 1]
    p = [1, 3]
    b = [0, 4]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
        p.append((4 * n - 2) * p[-1] + p[-2])
        # b_n=(4n-2)b_(n-1)+b_(n-2)+4q_(n-1).
        b.append((4 * n - 2) * b[-1] + b[-2] + 4 * q[n - 1])
    return q, p, b


def derivative_tail_direct(n: int, k: int) -> int:
    """Differentiate the product in (13) at x=n, k>=n+1."""
    assert k >= n + 1
    factors = list(range(n - k + 1, n + k + 1))
    assert factors.count(0) == 1
    product = 1
    for value in factors:
        if value:
            product *= value
    factorial = 1
    for value in range(2, k + 1):
        factorial *= value
    numerator = (-1 if k % 2 else 1) * product
    assert numerator % factorial == 0
    return numerator // factorial


def derivative_tail_formula(n: int, k: int) -> int:
    left = 1
    for value in range(2, k - n):
        left *= value
    right = 1
    for value in range(2, n + k + 1):
        right *= value
    denominator = 1
    for value in range(2, k + 1):
        denominator *= value
    assert left * right % denominator == 0
    sign = -1 if (n + 1) % 2 else 1
    return sign * (left * right // denominator)


def kappa_mod_prime(prime: int) -> int:
    total = 0
    factorial = 1
    for m in range(prime):
        if m:
            factorial = factorial * m % prime
        total = (total + factorial) % prime
    return total


def q_mod_at(index: int, modulus: int) -> int:
    if index <= 1:
        return 1 % modulus
    q0 = q1 = 1 % modulus
    for n in range(2, index + 1):
        q0, q1 = q1, ((4 * n - 2) * q1 + q0) % modulus
    return q1


def lift_record(
    n: int, prime: int, q: list[int], p: list[int], b: list[int]
) -> dict[str, int]:
    exponent = valuation_nonzero(q[n], prime)
    modulus = prime**exponent
    next_modulus = modulus * prime
    assert n < modulus
    kappa = kappa_mod_prime(prime)
    unit = (p[n] * kappa - b[n]) % prime
    assert unit
    quotient = (q[n] // modulus) % prime
    digit = quotient * pow(unit, -1, prime) % prime
    lifted_index = n + digit * modulus
    assert q_mod_at(lifted_index, next_modulus) == 0
    for other in range(prime):
        if other != digit:
            assert q_mod_at(n + other * modulus, next_modulus) != 0
    return {
        "n": n,
        "prime": prime,
        "valuation": exponent,
        "kappa_mod_p": kappa,
        "jet_unit_mod_p": unit,
        "q_quotient_mod_p": quotient,
        "predicted_unique_next_digit": digit,
        "lifted_index_mod_p_power": lifted_index,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_padic_all_integer_jet_euler_obstruction_certificate.json"
        ),
    )
    args = parser.parse_args()

    limit = 80
    q, p, b = sequences(limit)

    tail_checks = 0
    for n in range(0, 13):
        for k in range(n + 1, n + 13):
            assert derivative_tail_direct(n, k) == derivative_tail_formula(n, k)
            tail_checks += 1

    # A pair (coefficient of K_p, rational constant) represents a jet.
    derivative_pairs = [(-1, 0), (3, -4)]
    for n in range(0, limit - 1):
        c0, d0 = derivative_pairs[n]
        c1, d1 = derivative_pairs[n + 1]
        sign_f_next = -1 if (n + 1) % 2 else 1
        derivative_pairs.append(
            (
                c0 - (4 * n + 6) * c1,
                d0 - (4 * n + 6) * d1 - 4 * sign_f_next * q[n + 1],
            )
        )
    assert len(derivative_pairs) == limit + 1
    for n, pair in enumerate(derivative_pairs):
        sign = -1 if (n + 1) % 2 else 1
        assert pair == (sign * p[n], -sign * b[n])
        assert 0 <= b[n] <= 4 * (n + 1) * p[n]

    lift_cases = [(2, 7), (8, 13), (18, 7), (28, 11), (30, 7)]
    lift_records = [lift_record(n, prime, q, p, b) for n, prime in lift_cases]

    result = {
        "description": (
            "Exact finite regression checks for the identity "
            "f_p'(n)=(-1)^(n+1)(p_n*K_p-b_n) and its ordinary-root "
            "next-digit consequence."
        ),
        "sequence_limit": limit,
        "tail_derivative_checks": tail_checks,
        "initial_linear_forms": {
            "n=0": "-K_p",
            "n=1": "3*K_p-4",
        },
        "sample_sequences": {
            "q_0_to_10": q[:11],
            "p_0_to_10": p[:11],
            "b_0_to_10": b[:11],
        },
        "ordinary_lift_records": lift_records,
        "scope_warning": (
            "The certificate verifies exact identities and lift digits. "
            "It does not prove irrationality of K_p or an upper bound "
            "for v_p(q_n)."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
