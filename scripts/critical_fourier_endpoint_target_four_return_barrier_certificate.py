"""Exact certificate for endpoint-target four returns and recurrence barriers.

The all-parameter derivations are in
sources/critical_fourier_endpoint_target_four_return_barrier.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy

from critical_fourier_endpoint_period_scalar_recurrence_certificate import (
    scalar_coefficients,
)
from critical_fourier_normalized_three_dimensional_recurrence_certificate import (
    coefficient_digit,
    endpoint_integral,
    gadd,
    gdiv,
    gmul,
    gpow,
    gscale,
    initial_r_polynomial,
    multiply_one_plus_z_squared,
    polynomial_multiply,
)


def symbolic_integral_recurrence() -> dict[str, str]:
    x, n, k = sympy.symbols("x n k")
    denominator = 8 * (k + 1) * (k + 2)
    coefficients = (
        (n + 2) / denominator,
        (n + 1) / (4 * (k + 1) * (k + 2)),
        -(2 * k - n) / denominator,
        -(k - n) / (4 * (k + 1) * (k + 2)),
    )
    polynomial = sum(
        coefficients[index] * x**index for index in range(4)
    )
    certificate = x * (1 - x) * polynomial / (1 + x**2) ** 2
    logarithmic_derivative = (
        n / x - n / (1 - x) - 2 * k * x / (1 + x**2)
    )
    derivative_quotient = sympy.factor(
        sympy.diff(certificate, x)
        + certificate * logarithmic_derivative
    )
    recurrence_coefficients = (
        -2 * (k - n) * (2 * k - 2 * n - 1),
        16 * k**2
        - 20 * k * n
        + 10 * k
        + 5 * n**2
        - 7 * n
        + 2,
        -4 * (k + 1) * (5 * k - 3 * n + 4),
        8 * (k + 1) * (k + 2),
    )
    recurrence_integrand = sum(
        recurrence_coefficients[index] / (1 + x**2) ** index
        for index in range(4)
    ) / denominator
    assert sympy.factor(derivative_quotient - recurrence_integrand) == 0
    return {
        "derivative_identity": "verified_symbolically",
        "certificate_denominator": "8*(k + 1)*(k + 2)*(1 + x^2)^2",
        "endpoint_values": "zero_from_x*(1-x)",
    }


def symbolic_band_specialization() -> dict[str, str]:
    n, v, p = sympy.symbols("n v p")
    k = n + (p + 2 * v + 3) / 2
    global_coefficients = (
        -16 * (k - n) * (2 * k - 2 * n - 1),
        2
        * (
            16 * k**2
            - 20 * k * n
            + 10 * k
            + 5 * n**2
            - 7 * n
            + 2
        ),
        -2 * (k + 1) * (5 * k - 3 * n + 4),
        (k + 1) * (k + 2),
    )
    endpoint_coefficients = (
        -64 * (v + 1) * (2 * v + 3),
        8
        * (
            n**2
            + 12 * n * v
            + 21 * n
            + 16 * v**2
            + 58 * v
            + 53
        ),
        -2 * (2 * n + 2 * v + 5) * (4 * n + 10 * v + 23),
        (2 * n + 2 * v + 5) * (2 * n + 2 * v + 7),
    )
    for global_value, endpoint_value in zip(
        global_coefficients, endpoint_coefficients
    ):
        difference = sympy.expand(4 * global_value - endpoint_value)
        assert sympy.rem(
            sympy.Poly(difference, p), sympy.Poly(p, p)
        ).as_expr() == 0

    lower_index = n + (p + 1) / 2
    lower_pivot = sympy.factor(
        -16
        * (lower_index - n)
        * (2 * lower_index - 2 * n - 1)
    )
    upper_index = p - 2
    upper_pivot = sympy.factor((upper_index + 1) * (upper_index + 2))
    assert sympy.factor(lower_pivot + 8 * p * (p + 1)) == 0
    assert sympy.factor(upper_pivot - p * (p - 1)) == 0
    return {
        "four_times_global_operator_mod_p": "endpoint_operator",
        "lower_reset_pivot": str(lower_pivot),
        "upper_reset_pivot": str(upper_pivot),
    }


def symbolic_generating_equation() -> dict[str, object]:
    theta, t, n, v = sympy.symbols("theta t n v")
    x0, x1, x2 = sympy.symbols("x0 x1 x2")
    values = (x0, x1, x2)
    recurrence_polynomials = (
        -64 * (v + 1) * (2 * v + 3),
        8
        * (
            n**2
            + 12 * n * v
            + 21 * n
            + 16 * v**2
            + 58 * v
            + 53
        ),
        -2 * (2 * n + 2 * v + 5) * (4 * n + 10 * v + 23),
        (2 * n + 2 * v + 5) * (2 * n + 2 * v + 7),
    )
    operator = sympy.expand(
        sum(
            t ** (3 - shift)
            * recurrence_polynomials[shift].subs(v, theta - shift)
            for shift in range(4)
        )
    )
    theta_two = sympy.factor(operator.coeff(theta, 2))
    theta_one = sympy.factor(operator.coeff(theta, 1))
    theta_zero = sympy.factor(operator.coeff(theta, 0))
    assert sympy.factor(
        theta_two + 4 * (2 * t - 1) * (4 * t - 1) ** 2
    ) == 0
    assert sympy.factor(
        theta_one
        + 8
        * (4 * t - 1)
        * (-3 * n * t + n + 10 * t**2 - 4 * t)
    ) == 0

    boundary = sympy.expand(
        sum(
            t ** (3 - shift + index)
            * recurrence_polynomials[shift].subs(v, index - shift)
            * values[index]
            for shift in range(1, 4)
            for index in range(shift)
        )
    )
    boundary_coefficients = [
        sympy.factor(boundary.coeff(t, degree)) for degree in range(3)
    ]
    diagonal = [
        sympy.factor(
            sympy.expand(boundary_coefficients[index]).coeff(values[index])
        )
        for index in range(3)
    ]
    expected_diagonal = [
        4 * n**2 - 1,
        (2 * n + 1) * (2 * n + 3),
        (2 * n + 3) * (2 * n + 5),
    ]
    assert all(
        sympy.factor(actual - expected) == 0
        for actual, expected in zip(diagonal, expected_diagonal)
    )
    return {
        "theta_squared_coefficient": str(theta_two),
        "theta_coefficient": str(theta_one),
        "constant_coefficient": str(theta_zero),
        "inhomogeneous_boundary_coefficients": [
            str(value) for value in boundary_coefficients
        ],
        "initial_state_triangular_diagonal": [
            str(value) for value in diagonal
        ],
        "homogeneous_boundary_kernel_dimension": 0,
    }


def exponential_pair_modulo(n: int, modulus: int) -> tuple[int, int]:
    p_previous, p_current = 1, 3
    q_previous, q_current = 1, 1
    for index in range(2, n + 1):
        multiplier = 4 * index - 2
        p_previous, p_current = (
            p_current,
            (multiplier * p_current + p_previous) % modulus,
        )
        q_previous, q_current = (
            q_current,
            (multiplier * q_current + q_previous) % modulus,
        )
    return p_current, q_current


def transition_matrix(n: int, prime: int) -> list[list[int]]:
    inverse = lambda value: pow(value % prime, -1, prime)
    return [
        [
            16
            * (2 * n**2 - 3 * n - 8)
            * inverse(n * (2 * n + 5)),
            4
            * (8 * n + 11)
            * (n + 4)
            * inverse(n * (2 * n + 5)),
            -2 * (3 * n + 4) * inverse(n),
        ],
        [
            -384
            * (3 * n + 4)
            * inverse(n * (2 * n + 5) * (2 * n + 7)),
            16
            * (7 * n**3 + 59 * n**2 + 166 * n + 132)
            * inverse(n * (2 * n + 5) * (2 * n + 7)),
            -16
            * (n**2 + 6 * n + 6)
            * inverse(n * (2 * n + 7)),
        ],
        [
            -3072
            * (n**2 + 9 * n + 10)
            * inverse(
                n * (2 * n + 5) * (2 * n + 7) * (2 * n + 9)
            ),
            128
            * (n**4 + 30 * n**3 + 192 * n**2 + 457 * n + 330)
            * inverse(
                n * (2 * n + 5) * (2 * n + 7) * (2 * n + 9)
            ),
            -16
            * (n**3 + 31 * n**2 + 134 * n + 120)
            * inverse(n * (2 * n + 7) * (2 * n + 9)),
        ],
    ]


def matrix_vector(
    matrix: list[list[int]], vector: list[int], prime: int
) -> list[int]:
    return [
        sum(matrix[row][column] * vector[column] for column in range(3))
        % prime
        for row in range(3)
    ]


def base_initial_periods(prime: int) -> tuple[list[int], list[int]]:
    n = 2
    c = (prime - 5) // 2
    polynomial = initial_r_polynomial(n, prime)
    central: list[int] = []
    imaginary: list[int] = []
    for v in range(3):
        K = n + (prime + 2 * v + 1) // 2
        digit = coefficient_digit(polynomial, K, prime)
        period = endpoint_integral(polynomial, c - v, 0, prime)
        assert digit[1] == 0
        central.append(digit[0])
        imaginary.append(period[1])
        if v < 2:
            polynomial = multiply_one_plus_z_squared(polynomial, prime)
    return central, imaginary


def initial_periods_by_contiguity(
    n: int, prime: int
) -> tuple[list[int], list[int]]:
    central, imaginary = base_initial_periods(prime)
    for old_n in range(2, n, 2):
        assert 0 < old_n < prime
        assert 0 < 2 * old_n + 9 < prime
        transition = transition_matrix(old_n, prime)
        central = matrix_vector(transition, central, prime)
        imaginary = matrix_vector(transition, imaginary, prime)
    return central, imaginary


def direct_initial_polynomial(n: int, prime: int) -> list[tuple[int, int]]:
    """Return P_n(z)(1+z) from a linear coefficient recurrence.

    If H=(1+i)-2z+(1-i)z^2 and P_n=H^n, the identity
    H P_n'=n H' P_n gives a first-order recurrence in the coefficient
    index.  This is independent of the n-contiguity matrices.
    """
    a = (1, 1)
    b = (prime - 2, 0)
    c = (1, prime - 1)
    coefficients = [gpow(a, n, prime)]
    previous = (0, 0)
    for index in range(2 * n):
        current = coefficients[index]
        numerator = gadd(
            gscale(n - index, gmul(b, current, prime), prime),
            gscale(
                2 * n - index + 1,
                gmul(c, previous, prime),
                prime,
            ),
            prime,
        )
        denominator = gscale(index + 1, a, prime)
        next_coefficient = gdiv(numerator, denominator, prime)
        coefficients.append(next_coefficient)
        previous = current

    assert coefficients[-1] == gpow(c, n, prime)
    value_at_one = (0, 0)
    value_at_i = (0, 0)
    for index, coefficient in enumerate(coefficients):
        value_at_one = gadd(value_at_one, coefficient, prime)
        value_at_i = gadd(
            value_at_i,
            gmul(coefficient, gpow((0, 1), index, prime), prime),
            prime,
        )
    assert value_at_one == (0, 0)
    assert value_at_i == (0, 0)
    return polynomial_multiply(
        coefficients, [(1, 0), (1, 0)], prime
    )


def target_return_case(
    n: int, prime: int, expected_zeros: list[int]
) -> dict[str, object]:
    assert n % 2 == 0 and sympy.isprime(prime)
    c = (prime - 2 * n - 1) // 2
    assert c >= 3 and 2 * c + 2 * n + 1 == prime
    p_value, q_value = exponential_pair_modulo(n, prime**2)
    assert q_value % prime == 0 and q_value % prime**2 != 0
    q_quotient = q_value // prime % prime

    central, imaginary = initial_periods_by_contiguity(n, prime)
    direct_polynomial = direct_initial_polynomial(n, prime)
    direct_central: list[int] = []
    direct_imaginary: list[int] = []
    for v in range(3):
        K = n + (prime + 2 * v + 1) // 2
        direct_digit = coefficient_digit(direct_polynomial, K, prime)
        direct_period = endpoint_integral(
            direct_polynomial, c - v, 0, prime
        )
        assert direct_digit[1] == 0
        direct_central.append(direct_digit[0])
        direct_imaginary.append(direct_period[1])
        if v < 2:
            direct_polynomial = multiply_one_plus_z_squared(
                direct_polynomial, prime
            )
    assert central == direct_central
    assert imaginary == direct_imaginary
    target = [
        (4 * q_quotient * imaginary[index] - p_value * central[index])
        % prime
        for index in range(3)
    ]
    for v in range(c - 3):
        coefficients = scalar_coefficients(n, v, prime)
        for sequence in (central, imaginary, target):
            sequence.append(
                sum(
                    coefficients[index] * sequence[v + index]
                    for index in range(3)
                )
                % prime
            )
    independently_combined = [
        (4 * q_quotient * imaginary[index] - p_value * central[index])
        % prime
        for index in range(c)
    ]
    assert independently_combined == target
    zeros = [index for index, value in enumerate(target) if value == 0]
    assert zeros == expected_zeros
    assert all(central[index] and imaginary[index] for index in zeros)
    transcript = ",".join(str(value) for value in target)
    return {
        "n": n,
        "prime": prime,
        "c": c,
        "p_n_mod_p": p_value % prime,
        "q_n_mod_p_squared": q_value,
        "q_n_over_p_mod_p": q_quotient,
        "direct_initial_endpoint_check": True,
        "initial_D": direct_central,
        "initial_U": direct_imaginary,
        "zero_v": zeros,
        "zero_count": len(zeros),
        "zero_records": [
            {
                "v": index,
                "K": n + (prime + 2 * index + 1) // 2,
                "D": central[index],
                "U": imaginary[index],
                "previous_F": target[index - 1] if index else None,
                "next_F": target[index + 1] if index + 1 < c else None,
            }
            for index in zeros
        ],
        "all_zeros_isolated": all(
            (index == 0 or target[index - 1] != 0)
            and (index + 1 == c or target[index + 1] != 0)
            for index in zeros
        ),
        "target_transcript_sha256": hashlib.sha256(
            transcript.encode("ascii")
        ).hexdigest(),
    }


def adjacent_minor_counterexample() -> dict[str, object]:
    n = 2
    prime = 109
    c = (prime - 2 * n - 1) // 2
    central, imaginary = base_initial_periods(prime)
    for v in range(c - 3):
        coefficients = scalar_coefficients(n, v, prime)
        for sequence in (central, imaginary):
            sequence.append(
                sum(
                    coefficients[index] * sequence[v + index]
                    for index in range(3)
                )
                % prime
            )
    minors = [
        (
            central[v] * imaginary[v + 1]
            - central[v + 1] * imaginary[v]
        )
        % prime
        for v in range(c - 1)
    ]
    zeros = [index for index, value in enumerate(minors) if value == 0]
    assert zeros == [18, 22, 42]
    return {
        "n": n,
        "prime": prime,
        "c": c,
        "zero_adjacent_minor_v": zeros,
        "minor_transcript_sha256": hashlib.sha256(
            ",".join(str(value) for value in minors).encode("ascii")
        ).hexdigest(),
        "meaning": (
            "The target-independent right-factor minor is not always a "
            "unit, so the exact order-two reduction gives no first-order "
            "injectivity theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_endpoint_target_four_return_barrier_"
            "certificate.json"
        ),
    )
    arguments = parser.parse_args()
    cases = [
        target_return_case(
            3996,
            291869,
            [34071, 69843, 112900, 121346],
        ),
        target_return_case(756, 18313, [2136, 2883, 7328]),
        target_return_case(946, 14629, [1778, 2010, 3483]),
    ]
    output = {
        "description": (
            "Exact four-return target counterexample, global-to-endpoint "
            "operator specialization, reset pivots, and generating equation"
        ),
        "symbolic_integral_recurrence": symbolic_integral_recurrence(),
        "symbolic_band_specialization": symbolic_band_specialization(),
        "symbolic_generating_equation": symbolic_generating_equation(),
        "target_return_cases": cases,
        "adjacent_minor_counterexample": adjacent_minor_counterexample(),
        "at_most_two_target_returns": "false",
        "at_most_three_target_returns": "false",
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
