#!/usr/bin/env python3
"""Exact checks for the Bessel large-prime unit-cancellation frontier."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


def q_sequence(limit: int) -> list[int]:
    q = [1, 1]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
    return q


def valuation_nonzero(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rising_half_square_over_factorial(index: int) -> Fraction:
    value = Fraction(1)
    for t in range(1, index + 1):
        value *= Fraction((2 * t - 1) ** 2, 4 * t)
    return value


def elementary(values: list[Fraction], degree: int) -> Fraction:
    coefficients = [Fraction(0)] * (degree + 1)
    coefficients[0] = Fraction(1)
    for value in values:
        for j in range(degree, 0, -1):
            coefficients[j] += value * coefficients[j - 1]
    return coefficients[degree]


def central_layers(prime: int) -> list[Fraction]:
    m = (prime - 1) // 2
    c = [rising_half_square_over_factorial(j) for j in range(m + 1)]
    layers = []
    for ell in range(m + 1):
        total = Fraction(0)
        for j in range(ell, m + 1):
            alphabet = [Fraction(1, (2 * t - 1) ** 2) for t in range(1, j + 1)]
            total += c[j] * elementary(alphabet, ell)
        layers.append(total)
    return layers


def fraction_mod(value: Fraction, modulus: int) -> int:
    assert math.gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def pade_polynomials(n: int, x: sp.Symbol) -> tuple[sp.Expr, sp.Expr]:
    q_poly = sp.Integer(0)
    for k in range(n + 1):
        coefficient = math.factorial(2 * n - k) // (
            math.factorial(k) * math.factorial(n - k)
        )
        q_poly += (-1) ** k * coefficient * x**k
    return sp.expand(q_poly.subs(x, -x)), sp.expand(q_poly)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_large_prime_unit_cancellation_frontier_certificate.json"
        ),
    )
    args = parser.parse_args()

    q = q_sequence(80)
    size_checks = 0
    for n in range(2, 81):
        crude = 4 ** (n - 1) * math.factorial(n)
        assert q[n] < crude
        assert math.factorial(n) <= n**n // (2 ** (n - 1))
        assert q[n] < (2 * n + 1) ** n
        size_checks += 1

    primes = list(sp.primerange(3, 250))
    term_unit_checks = 0
    coefficient_unit_checks = 0
    for n in range(1, 45):
        for prime in primes:
            if prime <= 2 * n:
                continue
            for k in range(n + 1):
                term = math.factorial(n + k) // (
                    math.factorial(k) * math.factorial(n - k)
                )
                assert term % prime
                term_unit_checks += 1
                coefficient = math.factorial(2 * n - k) // (
                    math.factorial(k) * math.factorial(n - k)
                )
                assert coefficient % prime
                coefficient_unit_checks += 1

    x = sp.symbols("x")
    wronskian_checks = 0
    for n in range(0, 11):
        p_poly, q_poly = pade_polynomials(n, x)
        wronskian = sp.expand(
            sp.diff(p_poly, x) * q_poly
            - p_poly * sp.diff(q_poly, x)
            - p_poly * q_poly
        )
        assert wronskian == (-1) ** (n + 1) * x ** (2 * n)
        wronskian_checks += 1

    central_records = []
    central_identity_checks = 0
    congruence_checks = 0
    for prime in list(sp.primerange(3, 44)):
        m = (prime - 1) // 2
        layers = central_layers(prime)
        assert all(layer > 0 for layer in layers)
        assert all(math.gcd(layer.denominator, prime) == 1 for layer in layers)
        expansion = sum(
            ((-prime * prime) ** ell) * layers[ell]
            for ell in range(m + 1)
        )
        assert expansion.denominator == 1
        assert int(expansion) == (-1) ** m * q[m]
        central_identity_checks += 1

        term_sum = Fraction(0)
        for j in range(m + 1):
            paired = Fraction(1, 4**j * math.factorial(j))
            for t in range(1, j + 1):
                paired *= prime * prime - (2 * t - 1) ** 2
            direct_term = Fraction(
                math.factorial(m + j),
                math.factorial(j) * math.factorial(m - j),
            )
            assert paired == direct_term
            term_sum += (-1) ** j * paired
        assert term_sum == (-1) ** m * q[m]
        central_identity_checks += m + 2

        for exponent in range(1, 9):
            modulus = prime**exponent
            cutoff = min(m, (exponent - 1) // 2)
            truncated = sum(
                ((-prime * prime) ** ell) * layers[ell]
                for ell in range(cutoff + 1)
            )
            assert fraction_mod(truncated, modulus) == ((-1) ** m * q[m]) % modulus
            assert (q[m] % modulus == 0) == (fraction_mod(truncated, modulus) == 0)
            congruence_checks += 1
        central_records.append(
            {
                "prime": prime,
                "m": m,
                "valuation_of_q_m": valuation_nonzero(q[m], prime)
                if q[m] % prime == 0
                else 0,
                "layer_count": len(layers),
            }
        )

    assert q[8] == 312129649
    assert q[8] == 13**2 * 1846921
    assert valuation_nonzero(q[8], 13) == 2

    comparison_checks = 0
    for prime in list(sp.primerange(3, 80)):
        m = (prime - 1) // 2
        for exponent in (1, 2, 5, 9):
            # Q_A(x)=x-1+p^A has unit derivative and exact root distance A.
            assert valuation_nonzero(prime**exponent, prime) == exponent
            # H_A(m)=(2m+1)^(2A)=p^(2A), with reflection symmetry.
            value = (2 * m + 1) ** (2 * exponent)
            assert valuation_nonzero(value, prime) == 2 * exponent
            test_x = 3 * prime + 2
            left = (2 * (-test_x - 1) + 1) ** (2 * exponent)
            right = (2 * test_x + 1) ** (2 * exponent)
            assert left == right
            modulus = prime**3
            shifted = (2 * (test_x + modulus) + 1) ** (2 * exponent)
            assert (shifted - right) % modulus == 0
            comparison_checks += 1

    result = {
        "description": (
            "Exact regression checks for the p>2n exponent bound, unit-term "
            "frontier, Pade Wronskian, all-power central cancellation tower, "
            "and sharply scoped comparison no-go families."
        ),
        "size_bound_checks": size_checks,
        "term_unit_checks": term_unit_checks,
        "coefficient_unit_checks": coefficient_unit_checks,
        "wronskian_checks": wronskian_checks,
        "central_identity_checks": central_identity_checks,
        "central_congruence_checks": congruence_checks,
        "central_records": central_records,
        "large_range_square_counterexample": {
            "n": 8,
            "prime": 13,
            "valuation": 2,
            "q_n": q[8],
            "cofactor": 1846921,
        },
        "comparison_family_checks": comparison_checks,
        "scope_warning": (
            "The theorem proves v_p(q_n)<=n-1 for p>2n and gives an exact "
            "central congruence tower. It does not prove the required "
            "little-oh bound or nonvanishing of any tower layer."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
