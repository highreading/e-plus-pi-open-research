#!/usr/bin/env python3
"""Exact replay for the native CRT endpoint-layer sign obstruction."""

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


def integer_bytes(value: int) -> bytes:
    sign = b"-" if value < 0 else b"+"
    value = abs(value)
    length = max(1, (value.bit_length() + 7) // 8)
    return sign + length.to_bytes(8, "big") + value.to_bytes(length, "big")


def fraction_digest_update(digest: hashlib._Hash, value: Fraction) -> None:
    digest.update(integer_bytes(value.numerator))
    digest.update(integer_bytes(value.denominator))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "common_kernel_native_crt_endpoint_layer_sign_obstruction_"
            "certificate.json"
        ),
    )
    args = parser.parse_args()

    slope_checks = 0
    coefficient_budget_checks = 0
    derivative_bound_checks = 0
    base_sign_checks = 0
    perturbed_sign_checks = 0
    endpoint_checks = 0
    digest = hashlib.sha256()
    selected_rows: list[dict[str, object]] = []

    t_symbol, a_symbol, b_symbol = sp.symbols("t a b")
    h_symbol = sp.Function("H")(t_symbol)
    y_symbol = -h_symbol * (a_symbol + b_symbol * t_symbol)
    stein_in_t = sp.expand(
        -t_symbol * sp.diff(y_symbol, t_symbol)
        - (1 - t_symbol) * y_symbol
    )
    native_target = sp.expand(
        t_symbol * (a_symbol + b_symbol * t_symbol)
        * sp.diff(h_symbol, t_symbol)
        + (
            a_symbol * (1 - t_symbol)
            + b_symbol * t_symbol * (2 - t_symbol)
        )
        * h_symbol
    )
    assert sp.simplify(stein_in_t - native_target) == 0
    native_identity_checks = 1

    nonpositive_imaginary_indices: list[int] = []
    for n_value in range(2, 33):
        real, imag = gaussian_parts(n_value)
        m_native = math.factorial(n_value) - real
        assert m_native > 0 and m_native % 2 == 0
        if imag <= 0:
            nonpositive_imaginary_indices.append(n_value)
        else:
            # F(1)=-I_N<0 and F(0)=1.
            endpoint_checks += 1

    for q_value in range(2, 81):
        t = Fraction(1, 5 * q_value)
        x = 1 - t
        s = 1 - x**4
        a_poly = 4 - 6 * t + 4 * t**2 - t**3

        t_lambda = Fraction(
            4 * (1 + t) * a_poly,
            (1 - t) * (1 + a_poly),
        )
        assert 3 <= t_lambda <= 5
        slope_checks += 1

        h_base = x ** (20 * q_value) * (1 + 5 * q_value * s)
        lam = t_lambda / t
        assert h_base > 0

        primes = [
            int(prime)
            for prime in sp.primerange(3, 20 * q_value)
            if 3 * int(prime) > 48 * q_value + 14
        ]
        prime_product = math.prod(primes)
        coefficient_budget = (2 * len(primes) + 1) * prime_product

        # Saturate the permitted coefficient sum in the terminal channel.
        c_value = coefficient_budget * x**11
        u = 1 + x**2
        epsilon = (
            u**2
            * x ** (12 * q_value - 8)
            * s ** (4 * q_value)
            * (1 - x**2)
            * c_value
        )
        epsilon_bound = (
            4
            * coefficient_budget
            * Fraction(4, 5 * q_value) ** (4 * q_value)
        )
        assert 0 <= epsilon <= epsilon_bound
        coefficient_budget_checks += 1

        log_derivative_x = (
            4 * x / u
            + Fraction(12 * q_value - 8, 1) / x
            - 16 * q_value * x**3 / s
            - 2 * x / (1 - x**2)
            + Fraction(11, 1) / x
        )
        epsilon_x = epsilon * log_derivative_x
        assert abs(log_derivative_x) <= 120 * q_value**2
        assert t * abs(epsilon_x) <= 24 * q_value * epsilon
        derivative_bound_checks += 1

        j_value = 7 * epsilon + t * abs(epsilon_x)
        if q_value >= 2:
            assert j_value < Fraction(1, 4)

        for n_value in (2, 3, 4, 8, 9, 10, 11, 12, 16, 20, 24, 32):
            real, imag = gaussian_parts(n_value)
            if imag > 0:
                continue
            a_native = -imag
            b_native = Fraction(math.factorial(n_value) - real, 2)
            assert a_native >= 0 and b_native >= 1

            f_base = (
                t**n_value
                + a_native * h_base * (1 - t - t_lambda)
                + b_native * h_base * t * (2 - t - t_lambda)
            )
            assert f_base <= t**n_value - h_base * (
                2 * a_native + b_native * t
            )
            base_sign_checks += 1

            h_value = h_base * (1 - epsilon)
            # epsilon_t=-epsilon_x because x=1-t.
            h_prime_t = -lam * h_base * (1 - epsilon) + h_base * epsilon_x
            f_perturbed = (
                t**n_value
                + t * (a_native + b_native * t) * h_prime_t
                + (
                    a_native * (1 - t)
                    + b_native * t * (2 - t)
                )
                * h_value
            )

            perturbation = f_perturbed - f_base
            assert abs(perturbation) <= (
                h_base * j_value * (a_native + b_native * t)
            )

            if q_value >= 60:
                assert t**n_value <= b_native * t * h_base / 2
                assert f_perturbed < 0
                perturbed_sign_checks += 1

            digest.update(q_value.to_bytes(4, "big"))
            digest.update(n_value.to_bytes(4, "big"))
            fraction_digest_update(digest, t_lambda)
            fraction_digest_update(digest, epsilon)
            fraction_digest_update(digest, f_perturbed)

        if q_value in {2, 5, 10, 20, 40, 60, 80}:
            selected_rows.append(
                {
                    "q": q_value,
                    "window_prime_count": len(primes),
                    "window_product_bits": prime_product.bit_length(),
                    "coefficient_budget_bits": coefficient_budget.bit_length(),
                    "epsilon_numerator_bits": epsilon.numerator.bit_length(),
                    "epsilon_denominator_bits": epsilon.denominator.bit_length(),
                    "J_less_than_one_quarter": j_value < Fraction(1, 4),
                    "t_lambda": (
                        f"{t_lambda.numerator}/{t_lambda.denominator}"
                    ),
                }
            )

    result = {
        "schema": "common_kernel_native_crt_endpoint_layer_sign_obstruction_v1",
        "description": (
            "Exact rational replay for the endpoint-layer slope, CRT "
            "coefficient budget, perturbation bound, and uniform native "
            "sign obstruction."
        ),
        "slope_checks": slope_checks,
        "coefficient_budget_checks": coefficient_budget_checks,
        "derivative_bound_checks": derivative_bound_checks,
        "base_sign_checks": base_sign_checks,
        "perturbed_negative_checks_q_ge_60": perturbed_sign_checks,
        "positive_imaginary_endpoint_checks": endpoint_checks,
        "native_differential_identity_checks": native_identity_checks,
        "nonpositive_imaginary_indices_through_32": (
            nonpositive_imaginary_indices
        ),
        "selected_rows": selected_rows,
        "exact_digest_sha256": digest.hexdigest(),
        "scope": (
            "The theorem covers the existing beta-base/padded full-window "
            "CRT family with its uniform coefficient budget. It does not "
            "exclude every localizer with order/degree ratio between "
            "one third and one half."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
