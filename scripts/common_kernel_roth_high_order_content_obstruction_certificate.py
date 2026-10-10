#!/usr/bin/env python3
"""Exact replay for the native Roth/high-order content obstruction."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


def gaussian_parts(power: int) -> tuple[int, int]:
    real, imag = 1, 0
    for _ in range(power):
        real, imag = real + imag, imag - real
    return real, imag


def stein(expr: sp.Expr, x: sp.Symbol) -> sp.Expr:
    return sp.expand((1 - x) * sp.diff(expr, x) - x * expr)


def exact_quotient(numerator: sp.Expr, denominator: sp.Expr, x: sp.Symbol) -> sp.Expr:
    quotient, remainder = sp.div(sp.Poly(numerator, x), sp.Poly(denominator, x))
    assert remainder.is_zero
    return sp.expand(quotient.as_expr())


def coefficient(expr: sp.Expr, degree: int, x: sp.Symbol) -> int:
    return int(sp.Poly(expr, x).nth(degree))


def integral_fraction(expr: sp.Expr, x: sp.Symbol) -> Fraction:
    poly = sp.Poly(expr, x)
    result = Fraction(0)
    for (degree,), value in poly.terms():
        result += Fraction(int(value), degree + 1)
    return result


def valuation(value: int, prime: int) -> int:
    assert value
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def fraction_valuation(value: Fraction, prime: int) -> int:
    assert value
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def order_at_zero(expr: sp.Expr, x: sp.Symbol) -> int:
    poly = sp.Poly(expr, x)
    return min(degree[0] for degree, value in poly.terms() if value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "common_kernel_roth_high_order_content_obstruction_certificate.json"
        ),
    )
    args = parser.parse_args()

    x = sp.symbols("x")
    u = 1 + x**2
    t = 1 - x

    gaussian_checks = 0
    quotient_checks = 0
    prefix_checks = 0
    prime_valuation_checks = 0
    full_output_checks = 0
    primitive_checks = 0
    rows: list[dict[str, int]] = []
    digest_rows: list[tuple[int, ...]] = []

    for n_value in range(2, 13):
        real, imag = gaussian_parts(n_value)
        assert complex(real, imag) == (1 - 1j) ** n_value
        m_value_native = math.factorial(n_value) - real
        assert m_value_native > 0
        assert m_value_native % 2 == 0
        gaussian_checks += 1

        k_native = sp.expand(
            imag - sp.Integer(m_value_native) * (1 - x) / 2
        )
        tk_native = stein(k_native, x)
        assert tk_native == sp.expand(
            -sp.Integer(m_value_native) * u / 2
            + m_value_native
            - imag * x
        )

        p_zero = sp.expand(
            math.factorial(n_value)
            * sum(t**j / math.factorial(j + 1) for j in range(n_value))
        )
        assert all(value.q == 1 for value in sp.Poly(p_zero, x).all_coeffs())
        assert sp.expand(
            math.factorial(n_value) + stein(p_zero, x) - t**n_value
        ) == 0

        q_star = exact_quotient(
            t**n_value + tk_native - math.factorial(n_value), u, x
        )
        assert sp.degree(q_star, x) <= n_value - 2

        for localizer_index in range(3, 25):
            h = sp.expand(
                x ** (4 * localizer_index)
                * (localizer_index + 1 - localizer_index * x**4)
            )
            degree_h = int(sp.degree(h, x))
            order_h = order_at_zero(h, x)
            assert degree_h == 4 * localizer_index + 4
            assert order_h == 4 * localizer_index
            assert h.subs(x, 0) == 0
            assert h.subs(x, 1) == 1
            assert sp.rem(sp.Poly(h - 1, x), sp.Poly(u**2, x)).is_zero

            v_poly = exact_quotient(h - 1, u, x)
            hp_over_u = exact_quotient(sp.diff(h, x), u, x)
            s_direct = exact_quotient(
                stein(sp.expand(h * k_native), x) - tk_native, u, x
            )
            s_formula = sp.expand(
                -sp.Integer(m_value_native) * (h - 1) / 2
                + v_poly * (m_value_native - imag * x)
                + (1 - x) * hp_over_u * k_native
            )
            assert s_direct == s_formula
            assert sp.degree(s_direct, x) == degree_h
            quotient_checks += 1

            for exponent in range(order_h):
                expected = (
                    (-1) ** (exponent // 2 + 1) if exponent % 2 == 0 else 0
                )
                assert coefficient(v_poly, exponent, x) == expected
                prefix_checks += 1

            s_integral = integral_fraction(s_direct, x)
            q_full = sp.expand(q_star + s_direct)
            rational_coordinate = (
                Fraction(-math.factorial(n_value), 1)
                - Fraction(int(sp.expand(p_zero + h * k_native).subs(x, 0)), 1)
                + 4 * integral_fraction(q_full, x)
            )
            c_value = rational_coordinate.numerator
            d_value = rational_coordinate.denominator
            assert math.gcd(c_value, d_value) == 1

            content = math.gcd(math.factorial(n_value), c_value)
            rational_denominator = math.factorial(n_value) * d_value // content
            rational_numerator = -c_value // content
            assert math.gcd(rational_numerator, rational_denominator) == 1
            primitive_checks += 1

            predicted_primes: list[int] = []
            lower = max(n_value, (degree_h + 1) / 2)
            for prime in list(sp.primerange(3, order_h)):
                if not (prime > lower):
                    continue
                if m_value_native % prime == 0:
                    continue
                predicted_primes.append(prime)
                expected_sign = (-1) ** ((prime - 1) // 2 + 1)
                assert coefficient(s_direct, prime - 1, x) == (
                    expected_sign * m_value_native
                )
                assert fraction_valuation(s_integral, prime) == -1
                assert valuation(d_value, prime) == 1
                prime_valuation_checks += 1
                full_output_checks += 1

            if n_value in {2, 4, 8, 12} and localizer_index in {6, 12, 24}:
                row = {
                    "N": n_value,
                    "m": localizer_index,
                    "degree_h": degree_h,
                    "order_h": order_h,
                    "M_N": m_value_native,
                    "predicted_prime_count": len(predicted_primes),
                    "D_digits": len(str(d_value)),
                    "g_digits": len(str(content)),
                    "Q_digits": len(str(rational_denominator)),
                }
                rows.append(row)
                digest_rows.append(
                    (
                        n_value,
                        localizer_index,
                        degree_h,
                        order_h,
                        m_value_native,
                        len(predicted_primes),
                        d_value,
                        content,
                        rational_denominator,
                    )
                )

    # Exact exponent arithmetic for the convenient Roth choice delta=1/10.
    delta = Fraction(1, 10)
    epsilon = 2 * delta
    beta = Fraction(1, 2) - delta
    roth_product = beta * (2 + epsilon)
    assert roth_product == Fraction(22, 25)
    assert roth_product < 1

    # The CRT family lies strictly below the local-order threshold.
    crt_ratio_checks = 0
    for q_value in range(1, 101):
        assert Fraction(20 * q_value, 48 * q_value + 13) < Fraction(1, 2)
        crt_ratio_checks += 1

    digest = hashlib.sha256(repr(digest_rows).encode("utf-8")).hexdigest()
    result = {
        "schema": "common_kernel_roth_high_order_content_obstruction_v1",
        "description": (
            "Exact regression replay for the primitive Roth normalization, "
            "native quotient coefficient, prime-denominator survival, and "
            "high-order sparse-localizer specialization."
        ),
        "gaussian_checks": gaussian_checks,
        "quotient_checks": quotient_checks,
        "forced_prefix_coefficient_checks": prefix_checks,
        "prime_valuation_checks": prime_valuation_checks,
        "full_output_survival_checks": full_output_checks,
        "primitive_normalization_checks": primitive_checks,
        "crt_ratio_checks": crt_ratio_checks,
        "roth_exponent_example": {
            "delta": "1/10",
            "epsilon": "1/5",
            "beta_times_2_plus_epsilon": "22/25",
        },
        "selected_rows": rows,
        "exact_row_digest_sha256": digest,
        "scope": (
            "Finite rows check identities only. The theorem obstructs "
            "sign-controlled localizers with ord_0(h) >= (1/2+eta)deg(h); "
            "it does not cover the 20q versus 48q+13 CRT family."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
