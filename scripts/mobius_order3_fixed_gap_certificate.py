#!/usr/bin/env python3
"""Exact finite audit of the Möbius/endpoint identities.

The proofs are in mobius_order3_fixed_gap_analysis.md.  This checker uses
only the Python standard library and exact integer/Fraction arithmetic.
Its q-range is an audit, not a substitute for the symbolic proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


Gaussian = tuple[Fraction, Fraction]
Polynomial = list[Gaussian]


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= (value - index) / (index + 1)
    return answer


def power_coefficients(
    base: tuple[Fraction, ...], exponent: Fraction, degree: int
) -> list[Fraction]:
    """Coefficients through degree of base(z)^exponent, base(0)=1."""
    assert base[0] == 1
    answer = [Fraction(1)]
    base_degree = len(base) - 1
    # From B W' = exponent B' W.
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(base_degree, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * base[index]
                * answer[target - index]
            )
        answer.append(total / target)
    return answer


def polynomial_power_two_plus(degree: int) -> list[Fraction]:
    return [
        Fraction(math.comb(degree, index) * 2 ** (degree - index))
        for index in range(degree + 1)
    ]


def polynomial_power_one_plus(degree: int) -> list[Fraction]:
    return [Fraction(math.comb(degree, index)) for index in range(degree + 1)]


def coefficient_product(
    first: list[Fraction],
    second: list[Fraction],
    third: list[Fraction],
    degree: int,
) -> Fraction:
    answer = Fraction(0)
    for i, first_value in enumerate(first):
        for j, second_value in enumerate(second):
            remaining = degree - i - j
            if 0 <= remaining < len(third):
                answer += first_value * second_value * third[remaining]
    return answer


def rows(q_value: int, shift: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return C_s, T_s, and -2^(-alpha) Res_1(omega_s)."""
    n_value = q_value - 1
    alpha = Fraction(2 * q_value - 3, 3)
    beta = alpha - shift
    distinguished_degree = 1 + 3 * shift

    h_power = power_coefficients(
        (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2)),
        beta,
        n_value,
    )
    c_value = (
        coefficient_product(
            polynomial_power_two_plus(distinguished_degree),
            h_power,
            [Fraction(1)],
            n_value,
        )
        / 2**shift
    )

    quadratic_power = power_coefficients(
        (Fraction(1), Fraction(0), Fraction(1)), beta, n_value
    )
    negative_minus = [
        Fraction(math.comb(q_value + index - 1, index))
        for index in range(n_value + 1)
    ]
    t_value = coefficient_product(
        polynomial_power_one_plus(distinguished_degree),
        quadratic_power,
        negative_minus,
        n_value,
    )

    translated_quadratic_power = power_coefficients(
        (Fraction(1), Fraction(1), Fraction(1, 2)), beta, n_value
    )
    negative_plus = [
        Fraction((-1) ** index * math.comb(q_value + index - 1, index))
        for index in range(n_value + 1)
    ]
    reflected_residue = (
        coefficient_product(
            polynomial_power_two_plus(distinguished_degree),
            translated_quadratic_power,
            negative_plus,
            n_value,
        )
        / 2**shift
    )
    return c_value, t_value, reflected_residue


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return (left[0] + right[0], left[1] + right[1])


def gneg(value: Gaussian) -> Gaussian:
    return (-value[0], -value[1])


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gdiv(left: Gaussian, right: Gaussian) -> Gaussian:
    norm = right[0] ** 2 + right[1] ** 2
    return (
        (left[0] * right[0] + left[1] * right[1]) / norm,
        (left[1] * right[0] - left[0] * right[1]) / norm,
    )


ZERO: Gaussian = (Fraction(0), Fraction(0))
ONE: Gaussian = (Fraction(1), Fraction(0))
I: Gaussian = (Fraction(0), Fraction(1))


def matrix_multiply(
    left: tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]],
    right: tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]],
) -> tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]:
    return (
        (
            gadd(gmul(left[0][0], right[0][0]), gmul(left[0][1], right[1][0])),
            gadd(gmul(left[0][0], right[0][1]), gmul(left[0][1], right[1][1])),
        ),
        (
            gadd(gmul(left[1][0], right[0][0]), gmul(left[1][1], right[1][0])),
            gadd(gmul(left[1][0], right[0][1]), gmul(left[1][1], right[1][1])),
        ),
    )


def sigma(value: Gaussian) -> Gaussian:
    numerator = gadd(gmul(I, value), (Fraction(3), Fraction(0)))
    denominator = gadd(value, I)
    return gdiv(numerator, denominator)


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    degree = max(len(left), len(right))
    answer = [ZERO] * degree
    for index in range(degree):
        answer[index] = gadd(
            left[index] if index < len(left) else ZERO,
            right[index] if index < len(right) else ZERO,
        )
    return answer


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer = [ZERO] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            answer[i + j] = gadd(answer[i + j], gmul(first, second))
    return answer


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def run(max_q: int) -> dict[str, object]:
    checked_q: list[int] = []
    witness_lines: list[str] = []
    selected_rows: list[dict[str, object]] = []
    selected = {1, 5, 7, 11, 13, 47, 101, max_q}

    for q_value in range(1, max_q + 1, 2):
        if q_value % 3 == 0:
            continue
        n_value = q_value - 1
        alpha = Fraction(2 * q_value - 3, 3)
        falling = math.prod(2 * q_value - 3 - 3 * j for j in range(n_value))
        falling_from_binomial = (
            3**n_value
            * math.factorial(n_value)
            * generalized_binomial(alpha, n_value)
        )
        assert falling_from_binomial.denominator == 1
        assert falling_from_binomial.numerator == falling

        row_values = []
        for shift in (0, 1):
            c_value, t_value, reflected_residue = rows(q_value, shift)
            assert reflected_residue == c_value
            beta = alpha - shift
            # Exponent checks in gamma_s=-2^-alpha iota^* phi^* omega_s.
            phi_two_exponent = Fraction(1 + 2 * shift) - Fraction(q_value, 3)
            iota_two_exponent = Fraction(1 - q_value) + 2 * beta
            assert phi_two_exponent + iota_two_exponent == 0
            distinguished_degree = 1 + 3 * shift
            assert (
                q_value - distinguished_degree - 3 * beta - 2 == -q_value
            )
            # S=2/(1+t): the remaining S-power is beta and the
            # power-of-two constant is the one in equation (3.7).
            assert (
                2 * q_value - distinguished_degree - 2 * beta - 2 == beta
            )
            assert (
                distinguished_degree + beta - q_value + 1
                == phi_two_exponent
            )
            row_values.extend((c_value, t_value))

        for prime in primes_upto(2 * q_value + 3):
            if prime in (2, 3) or falling % prime == 0:
                continue
            assert prime > n_value

        checked_q.append(q_value)
        witness_lines.append(
            ":".join(
                [str(q_value), *(fraction_text(value) for value in row_values)]
            )
        )
        if q_value in selected:
            selected_rows.append(
                {
                    "q": q_value,
                    "C0": fraction_text(row_values[0]),
                    "T0": fraction_text(row_values[1]),
                    "C1": fraction_text(row_values[2]),
                    "T1": fraction_text(row_values[3]),
                }
            )

    # Exact order-three matrix and endpoint-orbit checks.
    matrix = ((I, (Fraction(3), Fraction(0))), (ONE, I))
    matrix_cubed = matrix_multiply(matrix_multiply(matrix, matrix), matrix)
    eight_i = (Fraction(0), Fraction(8))
    assert matrix_cubed == ((eight_i, ZERO), (ZERO, eight_i))

    zero_orbit = [ZERO]
    one_orbit = [ONE]
    for orbit in (zero_orbit, one_orbit):
        orbit.append(sigma(orbit[-1]))
        orbit.append(sigma(orbit[-1]))
        assert sigma(orbit[-1]) == orbit[0]
    assert zero_orbit == [
        ZERO,
        (Fraction(0), Fraction(-3)),
        (Fraction(0), Fraction(3)),
    ]
    assert one_orbit == [
        ONE,
        (Fraction(2), Fraction(-1)),
        (Fraction(2), Fraction(1)),
    ]

    # Cross-multiplied identity
    # ((t+i)^2+(it+3)^2)(t+i)=8i(1+t^2).
    denominator: Polynomial = [I, ONE]
    numerator: Polynomial = [(Fraction(3), Fraction(0)), I]
    left = polynomial_multiply(
        polynomial_add(
            polynomial_multiply(denominator, denominator),
            polynomial_multiply(numerator, numerator),
        ),
        denominator,
    )
    right: Polynomial = [eight_i, ZERO, eight_i, ZERO]
    assert left == right

    witness = "\n".join(witness_lines).encode("ascii")
    return {
        "schema": "mobius-order3-fixed-gap-certificate-v1",
        "scope": {
            "q_conditions": "positive odd q with gcd(q,6)=1",
            "max_q": max_q,
            "count": len(checked_q),
        },
        "assertions": {
            "C_s_equals_normalized_endpoint_one_residue_for_s_0_1": True,
            "cayley_inversion_power_cancellation": True,
            "P_equals_3_power_n_factorial_times_binomial": True,
            "prime_away_from_6P_is_greater_than_n_in_test_range": True,
            "order_three_matrix_cube_is_8i_identity": True,
            "branch_mobius_identity": True,
            "endpoint_orbits_are_distinct": True,
            "inverse_cubic_coordinate_exponents": True,
        },
        "warning": "Finite coefficient audit; symbolic proofs are in the companion note.",
        "witness_stream_sha256": hashlib.sha256(witness).hexdigest(),
        "selected_rows": selected_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=301)
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
