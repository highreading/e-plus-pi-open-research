#!/usr/bin/env python3
"""Exact certificate for the fixed-gap cubic Smith reduction.

The algebraic DVR lemma is proved in the accompanying note.  This
standard-library program independently checks the coefficient formulas,
all twenty maximal minors (grouped into twelve forms), the Smith chains,
and finite evidence for d3 | P_q.  The last assertion is deliberately
reported only as a finite computation, not as a uniform theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def h_power_coefficients(parameter: int, degree: int) -> list[Fraction]:
    """Coefficients of ((1+z)(1+z+z^2/2))^(parameter/3)."""
    exponent = Fraction(parameter, 3)
    polynomial = (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    coefficients = [Fraction(1)]
    # If W=H^exponent, then H W'=exponent H' W.
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(3, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * polynomial[index]
                * coefficients[target - index]
            )
        coefficients.append(total / target)
    return coefficients


def negative_power_with_polynomial(q_value: int, degree: int, shift: int) -> int:
    """Coefficient of (1+z)^(1+3*shift) (1-z)^(-q)."""
    polynomial_degree = 1 + 3 * shift
    return sum(
        math.comb(polynomial_degree, index)
        * math.comb(q_value + degree - index - 1, degree - index)
        for index in range(min(polynomial_degree, degree) + 1)
    )


def full_and_tail(q_value: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return C0,T0,C1,T1 from their exact coefficient definitions."""
    n_value = q_value - 1
    half_n = n_value // 2
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
    for index in range(half_n + 1):
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


def strip_two_three(value: int) -> int:
    value = abs(value)
    for prime in (2, 3):
        while value and value % prime == 0:
            value //= prime
    return value


def determinant_three(
    matrix: tuple[tuple[int, ...], ...], columns: tuple[int, int, int]
) -> int:
    first, second, third = columns
    return (
        matrix[0][first]
        * (
            matrix[1][second] * matrix[2][third]
            - matrix[1][third] * matrix[2][second]
        )
        - matrix[0][second]
        * (
            matrix[1][first] * matrix[2][third]
            - matrix[1][third] * matrix[2][first]
        )
        + matrix[0][third]
        * (
            matrix[1][first] * matrix[2][second]
            - matrix[1][second] * matrix[2][first]
        )
    )


def determinant_divisors(
    matrix: tuple[tuple[int, ...], ...]
) -> tuple[int, int, int, dict[tuple[int, int, int], int]]:
    delta_one = math.gcd(*(abs(value) for row in matrix for value in row))
    two_minors = []
    for first_row, second_row in combinations(range(3), 2):
        for first_column, second_column in combinations(range(6), 2):
            two_minors.append(
                matrix[first_row][first_column]
                * matrix[second_row][second_column]
                - matrix[first_row][second_column]
                * matrix[second_row][first_column]
            )
    delta_two = math.gcd(*(abs(value) for value in two_minors))
    three_minors = {
        columns: determinant_three(matrix, columns)
        for columns in combinations(range(6), 3)
    }
    delta_three = math.gcd(*(abs(value) for value in three_minors.values()))
    return delta_one, delta_two, delta_three, three_minors


def expected_maximal_minors(
    c_zero: int, t_zero: int, c_one: int, t_one: int, k_value: int
) -> dict[tuple[int, int, int], int]:
    """The twenty minors, represented by the twelve advertised forms."""
    resultant = c_zero * t_one - c_one * t_zero
    cube_zero = t_zero**3 - k_value * c_zero**3
    cube_one = t_one**3 - k_value * c_one**3
    mixed_zero_zero_one = t_zero**2 * t_one - k_value * c_zero**2 * c_one
    mixed_zero_one_one = t_zero * t_one**2 - k_value * c_zero * c_one**2
    return {
        (0, 1, 2): -cube_zero,
        (0, 1, 3): -c_zero * resultant,
        (0, 1, 4): -t_zero * resultant,
        (0, 1, 5): -mixed_zero_zero_one,
        (0, 2, 3): t_zero * resultant,
        (0, 2, 4): mixed_zero_zero_one,
        (0, 2, 5): k_value * c_zero * resultant,
        (0, 3, 4): c_one * resultant,
        (0, 3, 5): -t_one * resultant,
        (0, 4, 5): -mixed_zero_one_one,
        (1, 2, 3): -mixed_zero_zero_one,
        (1, 2, 4): -k_value * c_zero * resultant,
        (1, 2, 5): -k_value * t_zero * resultant,
        (1, 3, 4): t_one * resultant,
        (1, 3, 5): mixed_zero_one_one,
        (1, 4, 5): k_value * c_one * resultant,
        (2, 3, 4): -mixed_zero_one_one,
        (2, 3, 5): -k_value * c_one * resultant,
        (2, 4, 5): k_value * t_one * resultant,
        (3, 4, 5): -cube_one,
    }


MINOR_FORM_NAMES = [
    "U0 = T0^3-K*C0^3",
    "U1 = T1^3-K*C1^3",
    "M001 = T0^2*T1-K*C0^2*C1",
    "M011 = T0*T1^2-K*C0*C1^2",
    "C0*R",
    "T0*R",
    "K*C0*R",
    "K*T0*R",
    "C1*R",
    "T1*R",
    "K*C1*R",
    "K*T1*R",
]


def run(max_q: int) -> dict[str, object]:
    assert max_q >= 1
    witness_lines = []
    selected_q = {1, 5, 7, 11, 13, 25, 37, 101, 251, 499, 751, max_q}
    selected_rows = []
    checked = 0
    largest_invariant_bits = 0
    for q_value in range(1, max_q + 1, 2):
        if q_value % 3 == 0:
            continue
        c_zero_q, t_zero_q, c_one_q, t_one_q = full_and_tail(q_value)
        common_denominator = math.lcm(
            c_zero_q.denominator,
            t_zero_q.denominator,
            c_one_q.denominator,
            t_one_q.denominator,
        )
        assert strip_two_three(common_denominator) == 1
        c_zero, t_zero, c_one, t_one = [
            value.numerator * (common_denominator // value.denominator)
            for value in (c_zero_q, t_zero_q, c_one_q, t_one_q)
        ]
        k_value = 4 ** (q_value - 1)
        matrix = (
            (-t_zero, 0, k_value * c_zero, -t_one, 0, k_value * c_one),
            (c_zero, -t_zero, 0, c_one, -t_one, 0),
            (0, c_zero, -t_zero, 0, c_one, -t_one),
        )
        delta_one, delta_two, delta_three, three_minors = determinant_divisors(
            matrix
        )
        assert three_minors == expected_maximal_minors(
            c_zero, t_zero, c_one, t_one, k_value
        )
        assert delta_two % delta_one == 0
        assert delta_three % delta_two == 0
        invariants = (
            delta_one,
            delta_two // delta_one,
            delta_three // delta_two,
        )
        assert invariants[1] % invariants[0] == 0
        assert invariants[2] % invariants[1] == 0
        localized_invariants = tuple(strip_two_three(value) for value in invariants)

        falling_product = abs(
            math.prod(2 * q_value - 3 - 3 * index for index in range(q_value - 1))
        )
        # Finite evidence only.  The uniform version is the missing theorem.
        assert falling_product % localized_invariants[2] == 0

        resultant = c_zero * t_one - c_one * t_zero
        cube_zero = t_zero**3 - k_value * c_zero**3
        cube_one = t_one**3 - k_value * c_one**3
        cubic_gcd = math.gcd(abs(resultant), math.gcd(abs(cube_zero), abs(cube_one)))
        localized_cubic_gcd = strip_two_three(cubic_gcd)
        localized_delta_three = strip_two_three(delta_three)
        # This is the finite replay of the uniformly proved DVR lemma G | Delta_3.
        assert localized_delta_three % localized_cubic_gcd == 0
        assert falling_product**3 % localized_cubic_gcd == 0

        witness_lines.append(
            ":".join(
                str(value)
                for value in (
                    q_value,
                    *localized_invariants,
                    localized_cubic_gcd,
                    falling_product // localized_invariants[2],
                )
            )
        )
        largest_invariant_bits = max(
            largest_invariant_bits, localized_invariants[2].bit_length()
        )
        if q_value in selected_q:
            selected_rows.append(
                {
                    "q": q_value,
                    "localized_smith_invariants": [
                        str(value) for value in localized_invariants
                    ],
                    "localized_cubic_gcd": str(localized_cubic_gcd),
                    "P_over_largest_invariant": str(
                        falling_product // localized_invariants[2]
                    ),
                }
            )
        checked += 1

    witness = "\n".join(witness_lines).encode("ascii")
    return {
        "schema": "mixed-cubic-fixed-gap-cube-smith-certificate-v1",
        "scope": {
            "q_conditions": "positive odd q with gcd(q,6)=1",
            "max_q": max_q,
            "count": checked,
        },
        "matrix": (
            "[[-T0,0,K*C0,-T1,0,K*C1],"
            "[C0,-T0,0,C1,-T1,0],[0,C0,-T0,0,C1,-T1]], K=4^(q-1)"
        ),
        "normalization": (
            "C0,T0,C1,T1 are multiplied by their common denominator; "
            "the denominator has no prime factors other than 2 and 3, "
            "and all reported invariants then discard only factors 2 and 3"
        ),
        "twelve_maximal_minor_forms_up_to_sign": MINOR_FORM_NAMES,
        "uniform_results_proved_in_note": [
            "the twenty maximal minors have the twelve displayed forms",
            "away from 2 and 3, G=gcd(R,U0,U1) divides Delta3",
            "if d3 divides P_q, then G divides P_q^3",
        ],
        "assertions": {
            "common_denominators_supported_only_at_2_and_3": True,
            "all_twenty_maximal_minors_match_twelve_forms": True,
            "smith_divisibility_chain": True,
            "largest_localized_invariant_divides_P_finite_range_only": True,
            "localized_cubic_gcd_divides_third_determinant_divisor": True,
            "localized_cubic_gcd_divides_P_cubed_finite_range_only": True,
        },
        "missing_uniform_theorem": (
            "For every admissible q, the largest Smith invariant d3 over "
            "Z[1/6] divides P_q=product_{j=0}^{q-2}(2q-3-3j)."
        ),
        "status": "finite exact evidence for d3|P; not a uniform proof",
        "largest_localized_invariant_bit_length": largest_invariant_bits,
        "witness_stream_sha256": hashlib.sha256(witness).hexdigest(),
        "selected_rows": selected_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=1001)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run(arguments.max_q)
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    print(
        f"q_count={payload['scope']['count']}; max_q={arguments.max_q}; "
        f"sha256={hashlib.sha256(rendered).hexdigest()}"
    )
    if arguments.output:
        arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()
