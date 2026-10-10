"""Exact certificate for the scalar endpoint-period recurrence and Casoratian.

The all-parameter proofs are in
sources/critical_fourier_endpoint_period_scalar_recurrence.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy

from critical_fourier_large_prime_matching_filter_certificate import (
    base_polynomial,
    polymul,
)
from critical_fourier_normalized_three_dimensional_recurrence_certificate import (
    A_coefficient,
    coefficient_digit,
    endpoint_integral,
    exponential_pair,
    gadd,
    gmul,
    gpow,
    gscale,
    initial_r_polynomial,
    kappa_value,
    multiply_one_plus_z_squared,
    phi_mod,
    recurrence_coefficients,
    valuation,
)


Gaussian = tuple[int, int]


def matrix_multiply_gaussian(
    left: list[list[Gaussian]],
    right: list[list[Gaussian]],
    prime: int,
) -> list[list[Gaussian]]:
    value = [[(0, 0)] * len(right[0]) for _ in range(len(left))]
    for row in range(len(left)):
        for column in range(len(right[0])):
            entry = (0, 0)
            for index in range(len(right)):
                entry = gadd(
                    entry,
                    gmul(left[row][index], right[index][column], prime),
                    prime,
                )
            value[row][column] = entry
    return value


def simplified_transition(n: int, v: int, prime: int) -> list[list[Gaussian]]:
    T = (2 * n + 2 * v + 5) % prime
    inverse_T = pow(T, -1, prime)
    numerators = [
        [(0, 0), (T, 0), (0, 0)],
        [
            (-16 * (v + 1), -4 * n),
            (2 * (3 * n + 6 * v + 11), 2 * n),
            (0, -4 * n),
        ],
        [
            (2 * (n + 2), -2 * (n + 4 * v + 4)),
            (0, 2 * n + 2 * v + 3),
            (2 * (n + 4 * v + 6), -2 * n),
        ],
    ]
    return [
        [gscale(inverse_T, entry, prime) for entry in row]
        for row in numerators
    ]


def original_transition(
    n: int, c: int, v: int, prime: int
) -> list[list[Gaussian]]:
    coefficients = recurrence_coefficients(n, c, v, prime)
    inverse_b1 = pow(coefficients["b1"][0], -1, prime)
    inverse_g2 = (0, -pow(coefficients["g2"][1], -1, prime))
    row_three = [
        gscale(-inverse_b1, coefficients[name], prime)
        for name in ("a0", "a1", "b0")
    ]
    row_two = [
        gadd(
            row_three[index],
            gscale(
                -1,
                gmul(coefficients[name], inverse_g2, prime),
                prime,
            ),
            prime,
        )
        for index, name in enumerate(("g0", "g1", "d0"))
    ]
    return [[(0, 0), (1, 0), (0, 0)], row_two, row_three]


def scalar_coefficients(
    n: int, v: int, prime: int
) -> tuple[int, int, int]:
    E = (2 * n + 2 * v + 5) * (2 * n + 2 * v + 7) % prime
    Q = (
        n * n
        + 12 * n * v
        + 21 * n
        + 16 * v * v
        + 58 * v
        + 53
    ) % prime
    coefficient_zero = (
        64 * (v + 1) * (2 * v + 3) * pow(E, -1, prime)
    ) % prime
    coefficient_one = -8 * Q * pow(E, -1, prime) % prime
    coefficient_two = (
        2
        * (4 * n + 10 * v + 23)
        * pow(2 * n + 2 * v + 7, -1, prime)
    ) % prime
    return coefficient_zero, coefficient_one, coefficient_two


def determinant_three(matrix: list[list[int]], prime: int) -> int:
    return (
        matrix[0][0]
        * (
            matrix[1][1] * matrix[2][2]
            - matrix[1][2] * matrix[2][1]
        )
        - matrix[0][1]
        * (
            matrix[1][0] * matrix[2][2]
            - matrix[1][2] * matrix[2][0]
        )
        + matrix[0][2]
        * (
            matrix[1][0] * matrix[2][1]
            - matrix[1][1] * matrix[2][0]
        )
    ) % prime


def endpoint_integral_between(
    polynomial: list[Gaussian],
    u: int,
    extra_z: int,
    left: Gaussian,
    right: Gaussian,
    prime: int,
) -> Gaussian:
    value = (0, 0)
    for index, coefficient in enumerate(polynomial):
        denominator = u + index + extra_z
        assert 1 <= denominator < prime
        endpoint_difference = gadd(
            gpow(right, denominator, prime),
            gscale(-1, gpow(left, denominator, prime), prime),
            prime,
        )
        value = gadd(
            value,
            gscale(
                pow(denominator, -1, prime),
                gmul(coefficient, endpoint_difference, prime),
                prime,
            ),
            prime,
        )
    return value


def verify_modular_case(n: int, prime: int) -> dict[str, object]:
    c = (prime - 2 * n - 1) // 2
    assert c >= 3 and 2 * c + 2 * n + 1 == prime
    factorial = [1] * prime
    for index in range(1, prime):
        factorial[index] = factorial[index - 1] * index % prime
    p_value, q_value = exponential_pair(n)
    q_valuation = valuation(q_value, prime)
    q_quotient = (
        q_value // prime % prime if q_valuation >= 1 else None
    )

    R = initial_r_polynomial(n, prime)
    D_values: list[int] = []
    I_values: list[Gaussian] = []
    endpoint_transcript: list[str] = []
    direct_endpoint_checks = 3
    for v in range(direct_endpoint_checks):
        s = 2 * v + 1
        ell = (prime + s) // 2
        K = n + ell
        u = c - v
        D_pair = coefficient_digit(R, K, prime)
        assert D_pair[1] == 0
        D_value = D_pair[0]
        endpoint_D = endpoint_integral_between(
            R,
            u,
            0,
            (prime - 1, 0),
            (0, 0),
            prime,
        )
        assert endpoint_D == (D_value, 0)
        kappa = kappa_value(n, v, ell, K, factorial, prime)
        assert D_value == kappa * phi_mod(n, s, prime) % prime
        I_value = endpoint_integral(R, u, 0, prime)
        D_values.append(D_value)
        I_values.append(I_value)
        endpoint_transcript.append(
            (
                f"v={v};D={D_value};"
                f"I={I_value[0]},{I_value[1]}"
            )
        )
        if v + 1 < direct_endpoint_checks:
            R = multiply_one_plus_z_squared(R, prime)

    for v in range(c - 3):
        coefficients = scalar_coefficients(n, v, prime)
        next_I = (0, 0)
        next_D = 0
        for coefficient, offset in zip(coefficients, (0, 1, 2)):
            next_I = gadd(
                next_I,
                gscale(coefficient, I_values[v + offset], prime),
                prime,
            )
            next_D += coefficient * D_values[v + offset]
        I_values.append(next_I)
        D_values.append(next_D % prime)

    transition_identity_checks = 0
    scalar_recurrence_checks = 0
    forward_pivots: list[int] = []
    backward_pivots: list[int] = []
    for v in range(c - 3):
        matrix = simplified_transition(n, v, prime)
        assert matrix == original_transition(n, c, v, prime)
        next_matrix = simplified_transition(n, v + 1, prime)
        twice = matrix_multiply_gaussian(next_matrix, matrix, prime)
        coefficient_zero, coefficient_one, coefficient_two = (
            scalar_coefficients(n, v, prime)
        )
        predicted_row = []
        for column in range(3):
            entry = gadd(
                (coefficient_zero if column == 0 else 0, 0),
                (coefficient_one if column == 1 else 0, 0),
                prime,
            )
            entry = gadd(
                entry,
                gscale(coefficient_two, matrix[1][column], prime),
                prime,
            )
            predicted_row.append(entry)
        assert twice[1] == predicted_row
        transition_identity_checks += 1

        predicted_I = (0, 0)
        predicted_D = 0
        for coefficient, offset in zip(
            (coefficient_zero, coefficient_one, coefficient_two),
            (0, 1, 2),
        ):
            predicted_I = gadd(
                predicted_I,
                gscale(coefficient, I_values[v + offset], prime),
                prime,
            )
            predicted_D += coefficient * D_values[v + offset]
        assert predicted_I == I_values[v + 3]
        assert predicted_D % prime == D_values[v + 3]
        scalar_recurrence_checks += 2

        forward = (
            (2 * n + 2 * v + 5) * (2 * n + 2 * v + 7)
        )
        backward = 64 * (v + 1) * (2 * v + 3)
        assert 0 < 2 * n + 2 * v + 5 < prime
        assert 0 < 2 * n + 2 * v + 7 < prime
        assert 0 < v + 1 < prime
        assert 0 < 2 * v + 3 < prime
        assert forward % prime != 0 and backward % prime != 0
        forward_pivots.append(forward % prime)
        backward_pivots.append(backward % prime)

    W_values: list[int] = []
    for v in range(c - 2):
        matrix = [
            [
                D_values[v + offset],
                I_values[v + offset][0],
                I_values[v + offset][1],
            ]
            for offset in range(3)
        ]
        W_values.append(determinant_three(matrix, prime))
    for v in range(len(W_values) - 1):
        coefficient_zero = scalar_coefficients(n, v, prime)[0]
        assert W_values[v + 1] == coefficient_zero * W_values[v] % prime
    assert all(value != 0 for value in W_values)

    F_values: list[int] = []
    generic_zeros: list[int] = []
    if q_quotient is not None:
        for v, (D_value, I_value) in enumerate(
            zip(D_values, I_values)
        ):
            F_value = (
                4 * q_quotient * I_value[1] - p_value * D_value
            ) % prime
            F_values.append(F_value)
            if F_value == 0 and D_value != 0 and I_value[1] != 0:
                generic_zeros.append(v)
        assert any(F_values)
        assert not any(
            F_values[v] == F_values[v + 1] == F_values[v + 2] == 0
            for v in range(c - 2)
        )

    return {
        "n": n,
        "prime": prime,
        "c": c,
        "direct_endpoint_identity_checks": direct_endpoint_checks,
        "transition_row_identity_checks": transition_identity_checks,
        "scalar_recurrence_checks": scalar_recurrence_checks,
        "forward_pivots_all_units": all(forward_pivots),
        "backward_pivots_all_units": all(backward_pivots),
        "initial_contour_Casoratian": W_values[0],
        "all_contour_Casoratians_nonzero": all(W_values),
        "v_prime_q_n": q_valuation,
        "q_n_over_prime_mod_prime": q_quotient,
        "p_n_mod_prime": p_value % prime,
        "generic_target_zero_v": generic_zeros,
        "maximum_consecutive_target_zero_run": (
            max(
                (
                    len(run)
                    for run in "".join(
                        "1" if value == 0 else "0" for value in F_values
                    ).split("0")
                ),
                default=0,
            )
            if F_values
            else None
        ),
        "endpoint_transcript_sha256": hashlib.sha256(
            "\n".join(endpoint_transcript).encode("ascii")
        ).hexdigest(),
    }


def universal_base_Casoratian() -> dict[str, object]:
    n = 2
    rows_by_residue: list[list[list[Fraction]]] = []
    determinants: list[Fraction] = []
    base = base_polynomial(n)
    i_powers = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for c_residue in range(4):
        rows: list[list[Fraction]] = []
        for v in range(3):
            R = polymul(
                base,
                [
                    (math.comb(2 * v + 1, index), 0)
                    for index in range(2 * v + 2)
                ],
            )
            D_real = Fraction(0)
            D_imaginary = Fraction(0)
            I_real = Fraction(0)
            I_imaginary = Fraction(0)
            for index, (rho_real, rho_imaginary) in enumerate(R):
                denominator = Fraction(2 * (index - v - n) - 1, 2)
                endpoint = i_powers[(c_residue - v + index) % 4]
                product_real = (
                    rho_real * endpoint[0] - rho_imaginary * endpoint[1]
                )
                product_imaginary = (
                    rho_real * endpoint[1] + rho_imaginary * endpoint[0]
                )
                I_real += Fraction(product_real - rho_real) / denominator
                I_imaginary += (
                    Fraction(product_imaginary - rho_imaginary)
                    / denominator
                )
                sign = (
                    1
                    if (c_residue - v + index - 1) % 2 == 0
                    else -1
                )
                D_real += Fraction(sign * rho_real) / denominator
                D_imaginary += Fraction(sign * rho_imaginary) / denominator
            assert D_imaginary == 0
            rows.append([D_real, I_real, I_imaginary])
        rows_by_residue.append(rows)
        determinant = (
            rows[0][0]
            * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
            - rows[0][1]
            * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
            + rows[0][2]
            * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0])
        )
        determinants.append(determinant)
    magnitude = Fraction(2**24, 3**4 * 5**2 * 7**2)
    assert determinants == [magnitude, -magnitude, -magnitude, magnitude]
    return {
        "c_mod_4_determinants": [
            f"{value.numerator}/{value.denominator}"
            for value in determinants
        ],
        "magnitude": f"{magnitude.numerator}/{magnitude.denominator}",
    }


def symbolic_contiguity_certificate() -> dict[str, str]:
    z, n = sympy.symbols("z n")
    imaginary = sympy.I
    half = sympy.Rational(1, 2)
    c_residue = -n - half
    w = (1 + z) ** 2 / z
    logarithmic_derivative = (
        n / (z - 1)
        + n / (z - imaginary)
        + 1 / (z + 1)
        + (c_residue - 1) / z
    )
    H = -2 * imaginary * (z - 1) ** 2 * (z - imaginary) ** 2 / z**2
    common_factor = (z - 1) * (z + 1) * (z - imaginary)

    N0 = (
        n * z
        + n * (-sympy.Rational(3, 5) + sympy.Rational(4, 5) * imaginary)
        + z * (sympy.Rational(6, 5) + sympy.Rational(2, 5) * imaginary)
        - sympy.Rational(2, 5)
        + sympy.Rational(6, 5) * imaginary
    )
    N1 = (
        n**2 * z**3
        + n**2 * z**2 * (-1 + 2 * imaginary)
        + n**2 * z * (-2 + imaginary)
        - imaginary * n**2
        + sympy.Rational(5, 2) * n * z**3
        + n * z**2 * (1 + sympy.Rational(39, 2) * imaginary)
        + n * z * (-sympy.Rational(39, 2) - imaginary)
        - sympy.Rational(5, 2) * imaginary * n
        + 24 * imaginary * z**2
        - 24 * z
    )
    N2 = (
        n**3 * z**5
        + n**3 * z**4 * (1 - 2 * imaginary)
        + n**3 * z**3 * (-3 + imaginary)
        + n**3 * z**2 * (-1 + 3 * imaginary)
        + n**3 * z * (2 - imaginary)
        - imaginary * n**3
        + 6 * n**2 * z**5
        + n**2 * z**4 * (
            sympy.Rational(25, 2) - sympy.Rational(21, 2) * imaginary
        )
        + n**2 * z**3 * (
            -sympy.Rational(37, 2) + sympy.Rational(77, 2) * imaginary
        )
        + n**2 * z**2 * (
            -sympy.Rational(77, 2) + sympy.Rational(37, 2) * imaginary
        )
        + n**2 * z * (
            sympy.Rational(21, 2) - sympy.Rational(25, 2) * imaginary
        )
        - 6 * imaginary * n**2
        + sympy.Rational(35, 4) * n * z**5
        + n * z**4 * (25 - sympy.Rational(55, 4) * imaginary)
        + n * z**3 * (-sympy.Rational(5, 2) + 221 * imaginary)
        + n * z**2 * (-221 + sympy.Rational(5, 2) * imaginary)
        + n * z * (sympy.Rational(55, 4) - 25 * imaginary)
        - sympy.Rational(35, 4) * imaginary * n
        + 240 * imaginary * z**3
        - 240 * z**2
    )
    Q_functions = [
        (6 - 2 * imaginary)
        * common_factor
        * N0
        / (n * z * (n + sympy.Rational(5, 2))),
        -2
        * imaginary
        * common_factor
        * N1
        / (
            n
            * z**2
            * (n + sympy.Rational(5, 2))
            * (n + sympy.Rational(7, 2))
        ),
        -2
        * imaginary
        * common_factor
        * N2
        / (
            n
            * z**3
            * (n + sympy.Rational(5, 2))
            * (n + sympy.Rational(7, 2))
            * (n + sympy.Rational(9, 2))
        ),
    ]
    T = sympy.Matrix(
        [
            [
                16 * (2 * n**2 - 3 * n - 8) / (n * (2 * n + 5)),
                4 * (8 * n + 11) * (n + 4) / (n * (2 * n + 5)),
                -2 * (3 * n + 4) / n,
            ],
            [
                -384
                * (3 * n + 4)
                / (n * (2 * n + 5) * (2 * n + 7)),
                16
                * (7 * n**3 + 59 * n**2 + 166 * n + 132)
                / (n * (2 * n + 5) * (2 * n + 7)),
                -16 * (n**2 + 6 * n + 6) / (n * (2 * n + 7)),
            ],
            [
                -3072
                * (n**2 + 9 * n + 10)
                / (n * (2 * n + 5) * (2 * n + 7) * (2 * n + 9)),
                128
                * (n**4 + 30 * n**3 + 192 * n**2 + 457 * n + 330)
                / (n * (2 * n + 5) * (2 * n + 7) * (2 * n + 9)),
                -16
                * (n**3 + 31 * n**2 + 134 * n + 120)
                / (n * (2 * n + 7) * (2 * n + 9)),
            ],
        ]
    )
    for v in range(3):
        identity = sympy.together(
            H * w**v
            - sum(T[v, index] * w**index for index in range(3))
            - (
                sympy.diff(Q_functions[v], z)
                + Q_functions[v] * logarithmic_derivative
            )
        )
        assert sympy.expand(identity.as_numer_denom()[0]) == 0
    determinant = sympy.factor(T.det())
    expected = (
        4096
        * (n + 1) ** 2
        * (n + 2) ** 3
        / (n * (2 * n + 5) * (2 * n + 7) ** 2 * (2 * n + 9))
    )
    assert sympy.factor(determinant - expected) == 0
    return {
        "Hermite_reduction_identities": "verified_for_v_0_1_2",
        "T_determinant": str(determinant),
    }


def normalized_coefficients() -> dict[str, str]:
    n, v = sympy.symbols("n v")
    A = (
        (2 * v + 3)
        * (2 * n + 2 * v + 3)
        / (8 * (v + 2) * (v + 3))
    )
    B = -(
        n**2 + 12 * n * v + 21 * n + 16 * v**2 + 58 * v + 53
    ) / (8 * (v + 2) * (v + 3))
    C = (4 * n + 10 * v + 23) / (4 * (v + 3))
    return {
        "coefficient_X_v": str(sympy.factor(A)),
        "coefficient_X_v_plus_1": str(sympy.factor(B)),
        "coefficient_X_v_plus_2": str(sympy.factor(C)),
        "kappa_ratio": "8*(v + 1)/(2*n + 2*v + 3)",
        "p_independent": "true",
    }


def arbitrary_solution_counterexample() -> dict[str, object]:
    n = 2
    prime = 17
    c = 6
    values = [1, 9, 0]
    for v in range(c - 3):
        coefficients = scalar_coefficients(n, v, prime)
        values.append(
            sum(
                coefficients[index] * values[v + index]
                for index in range(3)
            )
            % prime
        )
    assert values == [1, 9, 0, 0, 2, 0]
    return {
        "n": n,
        "prime": prime,
        "initial_values": [1, 9, 0],
        "full_solution": values,
        "zero_v": [index for index, value in enumerate(values) if value == 0],
        "meaning": (
            "The scalar operator alone has a nonzero solution with three "
            "separated/partly consecutive zeros; target-specific period "
            "structure is essential."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_endpoint_period_scalar_recurrence_"
            "certificate.json"
        ),
    )
    arguments = parser.parse_args()
    cases = [
        verify_modular_case(4, 43),
        verify_modular_case(18, 3167),
        verify_modular_case(64, 937),
        verify_modular_case(82, 953),
    ]
    assert cases[1]["generic_target_zero_v"] == [713, 1306]
    assert cases[3]["generic_target_zero_v"] == [55, 281]
    output = {
        "description": (
            "Exact scalar recurrence, endpoint-period, Casoratian, "
            "contiguity, and zero-run certificate"
        ),
        "symbolic_contiguity": symbolic_contiguity_certificate(),
        "universal_n_2_Casoratian": universal_base_Casoratian(),
        "normalized_operator": normalized_coefficients(),
        "modular_cases": cases,
        "arbitrary_solution_three_zero_counterexample": (
            arbitrary_solution_counterexample()
        ),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
