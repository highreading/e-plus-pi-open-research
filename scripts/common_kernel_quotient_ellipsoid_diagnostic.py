#!/usr/bin/env python3
"""High-precision diagnostic for the common-kernel real quotient ellipsoid.

This script is deliberately separate from the exact certificate.  It replaces
the polynomial sup norm by the Euclidean norm of shifted-Chebyshev
coefficients, computes the induced two-dimensional real quotient metric, and
Gauss-reduces the exact image lattice 8 Z x 2 Z.  Its output is numerical
diagnostic evidence only; it proves no all-degree estimate.
"""

from __future__ import annotations

import json
import math

import mpmath as mp


PRECISION_DIGITS = 500
M_VALUES = (20, 40, 60, 80)


def monomial_chebyshev_vector(j: int, degree: int) -> list[mp.mpf]:
    """Shifted-Chebyshev coefficients of x^j, converted exactly to mp.mpf."""
    values = [mp.mpf(0)] * (degree + 1)
    if j == 0:
        values[0] = 1
        return values
    denominator = mp.mpf(2) ** (2 * j)
    values[0] = mp.mpf(math.comb(2 * j, j)) / denominator
    for k in range(1, j + 1):
        values[k] = mp.mpf(2 * math.comb(2 * j, j - k)) / denominator
    return values


def gauss_reduce(gram: mp.matrix) -> tuple[list[list[int]], mp.matrix]:
    """Lagrange-Gauss reduction, tracking an exact unimodular 2x2 matrix."""
    transform = [[1, 0], [0, 1]]

    def current_gram() -> mp.matrix:
        matrix = mp.matrix(transform)
        return matrix.T * gram * matrix

    for _ in range(10000):
        reduced_gram = current_gram()
        if reduced_gram[1, 1] < reduced_gram[0, 0]:
            transform[0][0], transform[0][1] = (
                transform[0][1],
                transform[0][0],
            )
            transform[1][0], transform[1][1] = (
                transform[1][1],
                transform[1][0],
            )
            continue
        nearest = int(mp.nint(reduced_gram[0, 1] / reduced_gram[0, 0]))
        if nearest == 0:
            return transform, reduced_gram
        transform[0][1] -= nearest * transform[0][0]
        transform[1][1] -= nearest * transform[1][0]
    raise RuntimeError("Gauss reduction did not terminate")


def quotient_metric(M: int) -> dict[str, object]:
    # Variables are h_2,...,h_M.  Formula (9) of the source note has degree M+1.
    degree = M + 1
    variable_count = M - 1
    monomials = [
        monomial_chebyshev_vector(j, degree) for j in range(degree + 1)
    ]
    polynomial_map = mp.matrix(degree + 1, variable_count)
    for column, m in enumerate(range(2, M + 1)):
        for k in range(degree + 1):
            polynomial_map[k, column] = m * (
                monomials[m - 1][k]
                + monomials[m + 1][k]
                - 2 * monomials[2][k]
            )
    gram_variables = polynomial_map.T * polynomial_map

    u = [1]
    for j in range(1, M + 2):
        u.append(1 - j * u[-1])
    common = [
        m * (u[m - 1] + u[m + 1] - 4) for m in range(2, M + 1)
    ]
    a_row = [2 * m for m in range(2, M + 1)]
    b_row = [
        (-1) ** m * (m * m + m + 1) * math.factorial(m) + 4 * (1 - m)
        for m in range(2, M + 1)
    ]

    scales = [max(map(abs, row)) for row in (common, a_row, b_row)]
    constraint_matrix = mp.matrix(
        [
            [mp.mpf(value) / scale for value in row]
            for row, scale in zip((common, a_row, b_row), scales)
        ]
    )
    moment_matrix = (
        constraint_matrix
        * (gram_variables ** -1)
        * constraint_matrix.T
    )

    # Schur complement imposing the common constraint equal to zero.
    schur = mp.matrix(
        [
            [
                moment_matrix[i, j]
                - moment_matrix[i, 0]
                * moment_matrix[0, j]
                / moment_matrix[0, 0]
                for j in (1, 2)
            ]
            for i in (1, 2)
        ]
    )
    scaled_quotient_metric = schur ** -1
    quotient = mp.matrix(
        [
            [
                scaled_quotient_metric[i, j]
                / (scales[i + 1] * scales[j + 1])
                for j in range(2)
            ]
            for i in range(2)
        ]
    )

    image_basis = mp.matrix([[8, 0], [0, 2]])
    image_gram = image_basis.T * quotient * image_basis
    transform, reduced_gram = gauss_reduce(image_gram)

    lambda_1 = mp.sqrt(reduced_gram[0, 0])
    lambda_2 = mp.sqrt(reduced_gram[1, 1])
    metric_covolume = mp.sqrt(mp.det(image_gram))

    trace = quotient[0, 0] + quotient[1, 1]
    discriminant = mp.sqrt(
        (quotient[0, 0] - quotient[1, 1]) ** 2
        + 4 * quotient[0, 1] ** 2
    )
    eigenvalue_min = (trace - discriminant) / 2
    eigenvalue_max = (trace + discriminant) / 2
    minor_semiaxis = mp.sqrt(eigenvalue_min)
    major_semiaxis = mp.sqrt(eigenvalue_max)

    # An eigenvector (1,slope) for the cheap direction.
    cheap_slope = -(
        quotient[0, 0] - eigenvalue_min
    ) / quotient[0, 1]

    exact_pairs = []
    for column in range(2):
        lattice_u = transform[0][column]
        lattice_v = transform[1][column]
        a = 8 * lattice_u
        b = 2 * lattice_v
        exact_pairs.append(
            {
                "a": a,
                "b": b,
                "form_value_decimal": mp.nstr(a * (mp.e + mp.pi) + b, 50),
            }
        )
    determinant = (
        exact_pairs[0]["a"] * exact_pairs[1]["b"]
        - exact_pairs[1]["a"] * exact_pairs[0]["b"]
    )

    return {
        "M": M,
        "log_lambda_1": mp.nstr(mp.log(lambda_1), 18),
        "log_lambda_2": mp.nstr(mp.log(lambda_2), 18),
        "log_metric_covolume": mp.nstr(mp.log(metric_covolume), 18),
        "log_minor_semiaxis": mp.nstr(mp.log(minor_semiaxis), 18),
        "major_semiaxis": mp.nstr(major_semiaxis, 18),
        "cheap_slope": mp.nstr(cheap_slope, 50),
        "cheap_slope_plus_e_plus_pi": mp.nstr(
            cheap_slope + mp.e + mp.pi, 18
        ),
        "gauss_transform_columns": transform,
        "exact_reduced_coefficient_pairs": exact_pairs,
        "coefficient_determinant": determinant,
    }


def main() -> None:
    mp.mp.dps = PRECISION_DIGITS
    records = [quotient_metric(M) for M in M_VALUES]
    output = {
        "schema": "common-kernel-quotient-ellipsoid-diagnostic-v1",
        "status": "numerical diagnostic only; no all-degree conclusion",
        "precision_decimal_digits": PRECISION_DIGITS,
        "polynomial_norm": "Euclidean norm of shifted-Chebyshev coefficients",
        "image_lattice": "8 Z x 2 Z",
        "records": records,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
