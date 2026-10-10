#!/usr/bin/env python3
"""Exact finite certificate for the Cartier infinity-resonance barrier.

The companion note proves the global reduction and degree bound. This
standard-library replay verifies the monomial action of D, constructs
three genuine degree-(p+1) exact-combination witnesses, and independently
matches their coefficient ratios with the actual weighted-Cayley residues.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


Q = [1, 1, 1, 1]
U = [0, 1, -1]
Q_PRIME = [1, 2, 3]
U_PRIME = [1, -2]


def convolution(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            answer[i + j] += x_value * y_value
    return answer


Q_U = convolution(Q, U)
U_Q_PRIME = convolution(U, Q_PRIME)
Q_U_PRIME = convolution(Q, U_PRIME)


def direct_d_monomial(degree: int, q_value: int) -> list[Fraction]:
    """Coefficients of D(z^degree), computed from the defining operator."""
    rows = degree + 5
    answer = [Fraction(0) for _ in range(rows)]
    if degree:
        for shift, coefficient in enumerate(Q_U):
            answer[degree - 1 + shift] += degree * coefficient
    for shift, coefficient in enumerate(U_Q_PRIME):
        answer[degree + shift] += Fraction(2 * q_value - 3, 3) * coefficient
    for shift, coefficient in enumerate(Q_U_PRIME):
        answer[degree + shift] -= (q_value - 1) * coefficient
    return answer


def formula_d_monomial(degree: int, q_value: int) -> list[Fraction]:
    """The claimed five-diagonal monomial formula."""
    answer = [Fraction(0) for _ in range(degree + 5)]
    answer[degree] = degree - q_value + 1
    middle = Fraction(5 * q_value - 6, 3)
    for shift in (1, 2, 3):
        answer[degree + shift] = middle
    answer[degree + 4] = 1 - degree
    return answer


def d_column(degree: int, q_value: int, prime: int, rows: int) -> list[int]:
    return [
        int(value.numerator * pow(value.denominator, -1, prime) % prime)
        for value in direct_d_monomial(degree, q_value)
    ] + [0] * (rows - degree - 5)


def rref(
    matrix: list[list[int]], prime: int, variable_count: int
) -> tuple[list[list[int]], list[int]]:
    pivot_columns = []
    pivot_row = 0
    for column in range(variable_count):
        selected = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column] % prime
            ),
            None,
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column] % prime, -1, prime)
        matrix[pivot_row] = [(entry * inverse) % prime for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (entry - factor * pivot_entry) % prime
                    for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return matrix, pivot_columns


def exact_combination_kernel(
    prime: int, q_value: int, max_degree: int
) -> list[list[int]]:
    """Kernel of D(V)-c1*Q+c0 through the requested degree."""
    rows = max_degree + 5
    columns = [
        d_column(degree, q_value, prime, rows)
        for degree in range(max_degree + 1)
    ]
    c_zero = [0] * rows
    c_zero[0] = 1
    c_one = [0] * rows
    for degree, coefficient in enumerate(Q):
        c_one[degree] = -coefficient % prime
    columns.extend((c_zero, c_one))
    variable_count = len(columns)
    matrix = [
        [columns[column][row] for column in range(variable_count)]
        for row in range(rows)
    ]
    reduced, pivots = rref(matrix, prime, variable_count)
    free_columns = [
        column for column in range(variable_count) if column not in pivots
    ]
    basis = []
    for free_column in free_columns:
        vector = [0] * variable_count
        vector[free_column] = 1
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row][free_column] % prime
        basis.append(vector)
    return basis


def polynomial_product_mod(
    left: list[int], right: list[int], prime: int
) -> list[int]:
    return [value % prime for value in convolution(left, right)]


def polynomial_power_mod(base: list[int], exponent: int, prime: int) -> list[int]:
    answer = [1]
    while exponent:
        if exponent & 1:
            answer = polynomial_product_mod(answer, base, prime)
        base = polynomial_product_mod(base, base, prime)
        exponent //= 2
    return answer


def negative_binomial_series(q_value: int, degree: int, sign: int, prime: int) -> list[int]:
    coefficients = [1]
    for index in range(1, degree + 1):
        coefficients.append(
            coefficients[-1]
            * (q_value + index - 1)
            * pow(index, -1, prime)
            * sign
            % prime
        )
    return coefficients


def weighted_residues(prime: int, q_value: int, shift: int) -> tuple[int, int, int]:
    exponent = (prime + 2 * q_value - 3) // 3 - shift
    degree = q_value - 1
    at_zero = polynomial_product_mod(
        polynomial_power_mod([1, 1, 1, 1], exponent, prime),
        negative_binomial_series(q_value, degree, 1, prime),
        prime,
    )[degree]
    # Q(1+t)=4+6t+4t^2+t^3 and (1+t)^(-q).
    at_one = -polynomial_product_mod(
        polynomial_power_mod([4, 6, 4, 1], exponent, prime),
        negative_binomial_series(q_value, degree, -1, prime),
        prime,
    )[degree] % prime
    return at_zero, at_one, (2 * at_zero + at_one) % prime


def verify_witness(prime: int, q_value: int) -> dict[str, object]:
    m_value = (prime - q_value) // 6
    assert prime == 6 * m_value + q_value
    high_basis = exact_combination_kernel(prime, q_value, prime + 1)
    low_basis = exact_combination_kernel(prime, q_value, 1)
    assert not low_basis
    assert len(high_basis) == 1
    vector = high_basis[0]
    coefficients = vector[:-2]
    c_zero, c_one = vector[-2:]
    assert c_one
    inverse = pow(c_one, -1, prime)
    coefficients = [(value * inverse) % prime for value in coefficients]
    c_zero = c_zero * inverse % prime
    c_one = 1
    degree = max(index for index, value in enumerate(coefficients) if value)
    assert degree == prime + 1

    # Replay D(V)=c1*Q-c0 coefficient by coefficient.
    rows = prime + 6
    output = [0] * rows
    for monomial_degree, scalar in enumerate(coefficients):
        column = d_column(monomial_degree, q_value, prime, rows)
        for row, entry in enumerate(column):
            output[row] = (output[row] + scalar * entry) % prime
    expected = [0] * rows
    expected[0] = (c_one - c_zero) % prime
    for index in (1, 2, 3):
        expected[index] = c_one
    assert output == expected

    residue_zero = weighted_residues(prime, q_value, 0)
    residue_one = weighted_residues(prime, q_value, 1)
    actual_ratio = residue_zero[0] * pow(residue_one[0], -1, prime) % prime
    assert actual_ratio == c_zero
    assert residue_zero[2] or residue_one[2]

    coefficient_bytes = ",".join(map(str, coefficients)).encode("ascii")
    return {
        "p": prime,
        "m": m_value,
        "q": q_value,
        "normalized_c0_c1": [c_zero, c_one],
        "primitive_numerator_degree": degree,
        "primitive_leading_coefficient": coefficients[-1],
        "primitive_coefficients": coefficients,
        "primitive_coefficients_sha256": hashlib.sha256(coefficient_bytes).hexdigest(),
        "no_degree_at_most_one_solution": True,
        "actual_residues": {
            "c0_r0_B0": list(residue_zero),
            "c1_r1_B1": list(residue_one),
        },
        "actual_residue_ratio_matches": True,
        "actual_B0_B1_are_not_both_zero": True,
    }


def run() -> dict[str, object]:
    # An exact rational-arithmetic replay of the monomial identity over a
    # deliberately redundant grid.
    for q_value in range(-7, 26):
        for degree in range(0, 45):
            assert direct_d_monomial(degree, q_value) == formula_d_monomial(
                degree, q_value
            )

    witnesses = [
        verify_witness(11, 5),
        verify_witness(31, 13),
        verify_witness(97, 13),
    ]
    witness_stream = "\n".join(
        f"{row['p']}:{row['q']}:{row['normalized_c0_c1'][0]}:"
        f"{row['primitive_leading_coefficient']}:"
        f"{row['primitive_coefficients_sha256']}"
        for row in witnesses
    ).encode("ascii")
    return {
        "schema": "mixed-cubic-cartier-infinity-resonance-barrier-v1",
        "operator": (
            "D(V)=Q*u*V'+(A/3)*u*Q'*V-(q-1)*Q*u'*V, "
            "Q=1+z+z^2+z^3, u=z(1-z), A=2q-3"
        ),
        "monomial_formula": (
            "D(z^d)=(d-q+1)z^d+((5q-6)/3)"
            "(z^(d+1)+z^(d+2)+z^(d+3))+(1-d)z^(d+4)"
        ),
        "global_degree_statement": (
            "Hermite reduction gives deg(V)<=2p; low output then forces "
            "deg(V)<=1 or deg(V)=p+1, hence deg(V)<=p+1"
        ),
        "assertions": {
            "monomial_formula_exact_rational_replay": True,
            "three_degree_p_plus_one_witnesses": True,
            "all_witnesses_have_no_degree_at_most_one_solution": True,
            "all_actual_residue_ratios_match": True,
            "none_of_the_witnesses_has_B0_equals_B1_equals_zero": True,
        },
        "status": (
            "barrier/counterexample to the bounded-primitive step; "
            "not a counterexample to fresh-prime nonvanishing"
        ),
        "witness_stream_sha256": hashlib.sha256(witness_stream).hexdigest(),
        "witnesses": witnesses,
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    print(hashlib.sha256(rendered).hexdigest())
    if arguments.output:
        arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()
