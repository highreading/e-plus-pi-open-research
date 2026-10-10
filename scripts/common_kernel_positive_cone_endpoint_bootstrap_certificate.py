#!/usr/bin/env python3
"""Exact certificate for the positive common-kernel endpoint bootstrap note.

This verifier checks the finite assertions accompanying the analytic
all-degree theorem.  It uses only Python integer and rational arithmetic.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


def polynomial_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for j, value in enumerate(left):
        answer[j] += value
    for j, value in enumerate(right):
        answer[j] += value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_scale(polynomial: list[int], scale: int) -> list[int]:
    return [scale * value for value in polynomial]


def polynomial_eval_i(polynomial: list[int]) -> tuple[int, int]:
    real = 0
    imaginary = 0
    for j, value in enumerate(polynomial):
        residue = j % 4
        if residue == 0:
            real += value
        elif residue == 1:
            imaginary += value
        elif residue == 2:
            real -= value
        else:
            imaginary -= value
    return real, imaginary


def a_monomials(degree: int) -> list[int]:
    values = [1]
    for j in range(1, degree + 1):
        values.append(1 - j * values[-1])
    return values


def a_functional(polynomial: list[int]) -> int:
    values = a_monomials(len(polynomial) - 1)
    return sum(value * values[j] for j, value in enumerate(polynomial))


def b_functional(polynomial: list[int], h: list[int]) -> int:
    endpoint_b = sum(
        (-1) ** j * math.factorial(j) * value
        for j, value in enumerate(polynomial)
    )
    return -endpoint_b + 4 * sum(h)


def divide_by_x_squared_plus_one(
    polynomial: list[int], constant: int
) -> list[int]:
    remainder = polynomial[:]
    remainder[0] -= constant
    quotient = [0] * max(1, len(polynomial) - 2)
    for degree in range(len(remainder) - 1, 1, -1):
        quotient[degree - 2] = remainder[degree]
        remainder[degree - 2] -= remainder[degree]
        remainder[degree] = 0
    assert remainder[0] == 0 and remainder[1] == 0
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def derivative_clearing_multiplier(quotient: list[int]) -> int:
    multiplier = 1
    for degree, value in enumerate(quotient):
        denominator = (degree + 1) // math.gcd(abs(value), degree + 1)
        multiplier = math.lcm(multiplier, denominator)
    return multiplier


def integrate_derivative(quotient: list[int], multiplier: int) -> list[int]:
    h = [0] * (len(quotient) + 1)
    for degree, value in enumerate(quotient):
        numerator = multiplier * value
        assert numerator % (degree + 1) == 0
        h[degree + 1] = numerator // (degree + 1)
    return h


def reconstruct_f(a: int, h: list[int]) -> list[int]:
    f = [0] * (len(h) + 2)
    f[0] = a
    for degree in range(1, len(h)):
        derivative = degree * h[degree]
        f[degree - 1] += derivative
        f[degree + 1] += derivative
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def e_bracket(last_index: int = 30) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(j)) for j in range(last_index + 1)),
        Fraction(),
    )
    return partial, partial + Fraction(
        1, last_index * math.factorial(last_index)
    )


def atan_bracket(q: int, even_last_index: int) -> tuple[Fraction, Fraction]:
    assert even_last_index % 2 == 0
    upper = sum(
        (
            Fraction(
                (-1) ** j,
                (2 * j + 1) * q ** (2 * j + 1),
            )
            for j in range(even_last_index + 1)
        ),
        Fraction(),
    )
    next_term = Fraction(
        1,
        (2 * (even_last_index + 1) + 1)
        * q ** (2 * (even_last_index + 1) + 1),
    )
    return upper - next_term, upper


def alpha_bracket() -> tuple[Fraction, Fraction]:
    e_lower, e_upper = e_bracket()
    atan5_lower, atan5_upper = atan_bracket(5, 24)
    atan239_lower, atan239_upper = atan_bracket(239, 4)
    pi_lower = 16 * atan5_lower - 4 * atan239_upper
    pi_upper = 16 * atan5_upper - 4 * atan239_lower
    return e_lower + pi_lower, e_upper + pi_upper


def decimal_string(value: Fraction, digits: int = 40) -> str:
    with localcontext() as context:
        context.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def positive_witness() -> dict[str, object]:
    # f=-4*x*(x-1)^2*(3*x^2-31)
    f = [0, 124, -248, 112, 24, -12]
    h = [0, -272, 62, 8, -3]
    a = 272
    assert reconstruct_f(a, h) == f
    assert a_functional(f) == a
    assert polynomial_eval_i(f) == (a, 0)
    assert f[0] == 0 and sum(f) == 0
    b = b_functional(f, h)
    assert b == -1544

    alpha_lower, alpha_upper = alpha_bracket()
    form_lower = a * alpha_lower + b
    form_upper = a * alpha_upper + b
    assert 0 < form_lower < form_upper

    return {
        "f_coefficients_ascending": f,
        "h_coefficients_ascending": h,
        "a": a,
        "A_f": a_functional(f),
        "f_at_i": list(polynomial_eval_i(f)),
        "endpoints": [f[0], sum(f)],
        "b": b,
        "positive_factorization": "4*x*(1-x)^2*(31-3*x^2)",
        "form_interval_fraction": [str(form_lower), str(form_upper)],
        "form_interval_decimal": [
            decimal_string(form_lower),
            decimal_string(form_upper),
        ],
    }


def gaussian_multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_power(base: tuple[int, int], exponent: int) -> tuple[int, int]:
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = gaussian_multiply(answer, base)
        base = gaussian_multiply(base, base)
        exponent //= 2
    return answer


def gaussian_rotate_i(value: tuple[int, int], exponent: int) -> tuple[int, int]:
    real, imaginary = value
    rotations = [
        (real, imaginary),
        (-imaginary, real),
        (-real, -imaginary),
        (imaginary, -real),
    ]
    return rotations[exponent % 4]


def beta_a(n: int, k: int) -> int:
    return sum(
        (-1) ** j
        * math.comb(n + k, j)
        * math.factorial(n + j)
        for j in range(n + k + 1)
    )


def beta_at_i(n: int, k: int) -> tuple[int, int]:
    return gaussian_rotate_i(gaussian_power((1, 1), n), k)


def beta_discrepancy(n: int, k: int) -> tuple[int, int]:
    value_a = beta_a(n, k)
    real, imaginary = beta_at_i(n, k)
    return value_a - real, -imaginary


def determinant(left: tuple[int, int], right: tuple[int, int]) -> int:
    return left[0] * right[1] - left[1] * right[0]


def beta_polynomial(n: int, k: int) -> list[int]:
    # x^(n+k)*(1-x)^n
    polynomial = [0] * (2 * n + k + 1)
    for j in range(n + 1):
        polynomial[n + k + j] = (-1) ** j * math.comb(n, j)
    return polynomial


def beta_scan(maximum_n: int = 40) -> list[dict[str, object]]:
    records = []
    for n in range(1, maximum_n + 1):
        if n % 4 in (0, 1):
            indices = (1, 2, 3)
        else:
            indices = (0, 1, 2)
        columns = [beta_discrepancy(n, k) for k in indices]
        weights = [
            determinant(columns[1], columns[2]),
            determinant(columns[2], columns[0]),
            determinant(columns[0], columns[1]),
        ]
        if weights[0] < 0:
            weights = [-value for value in weights]
        common = math.gcd(*weights)
        weights = [value // common for value in weights]
        assert all(value > 0 for value in weights)
        assert math.gcd(*weights) == 1
        assert sum(
            weight * column[0]
            for weight, column in zip(weights, columns, strict=True)
        ) == 0
        assert sum(
            weight * column[1]
            for weight, column in zip(weights, columns, strict=True)
        ) == 0

        polynomial = [0]
        for weight, k in zip(weights, indices, strict=True):
            polynomial = polynomial_add(
                polynomial,
                polynomial_scale(beta_polynomial(n, k), weight),
            )
        target_a, target_imaginary = polynomial_eval_i(polynomial)
        assert target_imaginary == 0
        assert target_a == a_functional(polynomial)
        assert target_a != 0
        assert target_a % math.factorial(n) == 0
        assert all(value == 0 for value in polynomial[:n])

        quotient = divide_by_x_squared_plus_one(polynomial, target_a)
        multiplier = derivative_clearing_multiplier(quotient)
        h = integrate_derivative(quotient, multiplier)
        scaled_polynomial = polynomial_scale(polynomial, multiplier)
        scaled_a = multiplier * target_a
        assert reconstruct_f(scaled_a, h) == scaled_polynomial
        assert a_functional(scaled_polynomial) == scaled_a
        assert polynomial_eval_i(scaled_polynomial) == (scaled_a, 0)
        scaled_b = b_functional(scaled_polynomial, h)
        output_gcd = math.gcd(abs(scaled_a), abs(scaled_b))
        assert output_gcd > 0
        ordinary_integral = sum(
            (
                Fraction(value, degree + 1)
                for degree, value in enumerate(scaled_polynomial)
            ),
            Fraction(),
        )
        assert ordinary_integral > 0
        primitive_positive_lower_bound = (
            3 * ordinary_integral / output_gcd
        )
        assert primitive_positive_lower_bound > 5

        records.append(
            {
                "n": n,
                "indices": list(indices),
                "weights": weights,
                "discrepancy_columns": [list(column) for column in columns],
                "degree": len(polynomial) - 1,
                "target_a_before_derivative_clearing": target_a,
                "target_a_over_n_factorial": target_a // math.factorial(n),
                "derivative_clearing_multiplier": multiplier,
                "scaled_target_a": scaled_a,
                "scaled_target_b": scaled_b,
                "output_gcd": output_gcd,
                "primitive_pair": [
                    scaled_a // output_gcd,
                    scaled_b // output_gcd,
                ],
                "ordinary_integral": str(ordinary_integral),
                "primitive_positive_form_lower_bound": str(
                    primitive_positive_lower_bound
                ),
                "polynomial_coefficient_sha256": hashlib.sha256(
                    json.dumps(polynomial, separators=(",", ":")).encode("ascii")
                ).hexdigest(),
                "h_coefficient_sha256": hashlib.sha256(
                    json.dumps(h, separators=(",", ":")).encode("ascii")
                ).hexdigest(),
            }
        )
    return records


def r_polynomial(value: Fraction) -> Fraction:
    return (
        value**8
        - 20 * value**6
        - 26 * value**4
        - 20 * value**2
        + 1
    )


def r_enclosure() -> dict[str, object]:
    lower = Fraction(1152895447327, 250000000000)
    upper = Fraction(4611581789309, 1000000000000)
    lower_sign = r_polynomial(lower)
    upper_sign = r_polynomial(upper)
    assert lower > 4
    assert lower_sign < 0 < upper_sign
    # For y=r^2>=16, y^3-15y^2-13y-5 is positive and increasing;
    # hence the defining polynomial is strictly increasing throughout.
    y = lower * lower
    derivative_factor = y**3 - 15 * y**2 - 13 * y - 5
    assert derivative_factor > 0
    with localcontext() as context:
        context.prec = 40
        inverse_sqrt_lower = Decimal(upper.denominator).sqrt() / Decimal(
            upper.numerator
        ).sqrt()
        inverse_sqrt_upper = Decimal(lower.denominator).sqrt() / Decimal(
            lower.numerator
        ).sqrt()
    return {
        "minimal_polynomial": "r^8-20*r^6-26*r^4-20*r^2+1",
        "R_interval_fraction": [str(lower), str(upper)],
        "polynomial_signs_at_endpoints": [
            str(lower_sign),
            str(upper_sign),
        ],
        "R_inverse_square_root_interval_decimal": [
            str(inverse_sqrt_lower),
            str(inverse_sqrt_upper),
        ],
    }


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "common_kernel_positive_cone_endpoint_bootstrap_certificate.json"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "sources/common_kernel_positive_cone_endpoint_bootstrap_barrier.md"
        ),
    )
    arguments = parser.parse_args()

    result = {
        "status": "exact finite certificate; analytic all-degree theorem is in source",
        "source_sha256": file_sha256(arguments.source),
        "positive_endpoint_zero_witness": positive_witness(),
        "R_enclosure": r_enclosure(),
        "beta_scan": {
            "range": [1, 40],
            "relation_status": (
                "exact primitive positive adjacent three-column relation "
                "at every scanned n"
            ),
            "records": beta_scan(40),
        },
        "scope": (
            "The scan is finite. The endpoint-bootstrap lower bound is proved "
            "analytically in the source and is not inferred from this scan."
        ),
    }

    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
