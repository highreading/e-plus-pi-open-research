#!/usr/bin/env python3
"""Finite exact diagnostic for the uniform 3-adic determinant theorem.

The proof is in mixed_cubic_connection_determinant_3adic_nonvanishing.md.
This script uses only the Python standard library.  Its finite run is an
audit of the exact coefficient formulas and valuation law, not the proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def v3_integer(value: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("v3(0)")
    answer = 0
    while value % 3 == 0:
        value //= 3
        answer += 1
    return answer


def v3(value: Fraction) -> int:
    if not value:
        raise ValueError("v3(0)")
    return v3_integer(value.numerator) - v3_integer(value.denominator)


def denominator_exponent(index: int) -> int:
    return index + v3_integer(math.factorial(index)) if index else 0


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
        answer /= index + 1
    return answer


def rational_mod(value: Fraction, modulus: int) -> int:
    assert math.gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def h_power_coefficients(parameter: int, degree: int) -> list[Fraction]:
    """Coefficients of ((1+z)(1+z+z^2/2))^(parameter/3)."""
    exponent = Fraction(parameter, 3)
    h = (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    coefficients = [Fraction(1)]
    # From H W' = exponent H' W.
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(3, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * h[index]
                * coefficients[target - index]
            )
        coefficients.append(total / target)
    return coefficients


def negative_power_with_polynomial(q_value: int, degree: int, shift: int) -> int:
    """[z^degree](1+z)^(1 or 4)*(1-z)^(-q), exactly."""
    polynomial_degree = 1 if shift == 0 else 4
    return sum(
        math.comb(polynomial_degree, index)
        * math.comb(q_value + degree - index - 1, degree - index)
        for index in range(min(polynomial_degree, degree) + 1)
    )


def full_and_tail(q_value: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    n_value = q_value - 1
    r_value = n_value // 2
    parameter = 2 * q_value - 3

    full_zero_series = h_power_coefficients(parameter, n_value)
    c_zero = 2 * full_zero_series[n_value]
    if n_value:
        c_zero += full_zero_series[n_value - 1]

    full_one_series = h_power_coefficients(parameter - 3, n_value)
    c_one = Fraction(0)
    for index in range(min(4, n_value) + 1):
        c_one += (
            Fraction(math.comb(4, index) * 2 ** (4 - index), 2)
            * full_one_series[n_value - index]
        )

    exponent_zero = Fraction(parameter, 3)
    exponent_one = exponent_zero - 1
    binomial_zero = Fraction(1)
    binomial_one = Fraction(1)
    t_zero = Fraction(0)
    t_one = Fraction(0)
    for index in range(r_value + 1):
        remaining = n_value - 2 * index
        t_zero += binomial_zero * negative_power_with_polynomial(
            q_value, remaining, 0
        )
        t_one += binomial_one * negative_power_with_polynomial(
            q_value, remaining, 1
        )
        binomial_zero *= (exponent_zero - index) / (index + 1)
        binomial_one *= (exponent_one - index) / (index + 1)
    return c_zero, t_zero, c_one, t_one


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def run(max_q: int) -> dict[str, object]:
    assert max_q >= 1
    checked = []
    witness_lines = []
    selected_q = {1, 5, 7, 11, 13, 47, 101, 199, 499, 997, max_q}
    selected_rows = []

    for q_value in range(1, max_q + 1, 2):
        if q_value % 3 == 0:
            continue
        n_value = q_value - 1
        r_value = n_value // 2
        parameter = 2 * q_value - 3
        d_n = denominator_exponent(n_value)
        d_r = denominator_exponent(r_value)
        c_zero, t_zero, c_one, t_one = full_and_tail(q_value)
        determinant = c_zero * t_one - c_one * t_zero

        assert v3(c_zero) == -d_n
        assert v3(c_one) == -d_n
        assert v3(t_zero) == -d_r
        assert v3(t_one) == -d_r
        assert determinant
        assert v3(determinant) == 1 - d_n - d_r

        c_zero_scaled = c_zero * 3**d_n
        c_one_scaled = c_one * 3**d_n
        t_zero_scaled = t_zero * 3**d_r
        t_one_scaled = t_one * 3**d_r
        determinant_scaled = determinant * 3 ** (d_n + d_r)
        b_n = 3**d_n * generalized_binomial(Fraction(parameter, 3), n_value)
        b_r = 3**d_r * generalized_binomial(Fraction(parameter, 3), r_value)
        assert v3(b_n) == 0 and v3(b_r) == 0

        if q_value % 6 == 1:
            predicted = (
                3
                * b_n
                * b_r
                * Fraction(2**n_value * (3 * q_value - 1), parameter)
            )
            assert rational_mod(determinant_scaled - predicted, 9) == 0
        else:
            assert q_value % 6 == 5
            normalized = (
                rational_mod(c_zero_scaled / b_n, 9),
                rational_mod(c_one_scaled / b_n, 9),
                rational_mod(t_zero_scaled / b_r, 9),
                rational_mod(t_one_scaled / b_r, 9),
            )
            assert normalized == (2, 2, 4, 7)
            assert rational_mod(determinant_scaled / (b_n * b_r), 9) == 6

        checked.append(q_value)
        witness_lines.append(
            f"{q_value}:{v3(c_zero)}:{v3(c_one)}:{v3(t_zero)}:"
            f"{v3(t_one)}:{v3(determinant)}:"
            f"{rational_mod(determinant_scaled, 9)}"
        )
        if q_value in selected_q:
            selected_rows.append(
                {
                    "q": q_value,
                    "D_n": d_n,
                    "D_r": d_r,
                    "component_v3": {
                        "C0": v3(c_zero),
                        "C1": v3(c_one),
                        "T0": v3(t_zero),
                        "T1": v3(t_one),
                    },
                    "determinant_v3": v3(determinant),
                    "predicted_determinant_v3": 1 - d_n - d_r,
                    "scaled_component_residues_mod_9": {
                        "C0": rational_mod(c_zero_scaled, 9),
                        "C1": rational_mod(c_one_scaled, 9),
                        "T0": rational_mod(t_zero_scaled, 9),
                        "T1": rational_mod(t_one_scaled, 9),
                    },
                    "scaled_determinant_residue_mod_9": rational_mod(
                        determinant_scaled, 9
                    ),
                    "determinant": fraction_record(determinant),
                }
            )

    stream = "\n".join(witness_lines).encode("ascii")
    return {
        "scope": {
            "q_conditions": "positive odd q with gcd(q,6)=1",
            "max_q": max_q,
            "count": len(checked),
            "first_q": checked[0],
            "last_q": checked[-1],
        },
        "theorem_checked": (
            "v3(C0*T1-C1*T0) = 1-D(q-1)-D((q-1)/2), "
            "where D(k)=k+v3(k!)"
        ),
        "status": {
            "all_exact_assertions_passed": True,
            "finite_diagnostic_not_used_as_proof": True,
        },
        "witness_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "selected_rows": selected_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=1001)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run(arguments.max_q)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
