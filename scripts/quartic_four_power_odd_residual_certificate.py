#!/usr/bin/env python3
"""Certificate for the first surviving four-power odd-coordinate term."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

import sympy as sp


def raw_coordinate_numerators(n: int, k: int) -> tuple[int, int, int, int]:
    out = [0, 0, 0, 0]
    products = [1] * (n + 1)
    for j in range(n + 1):
        monomial = n + j
        for s in range(1, k):
            products[j] *= 4 * s - monomial - 1
        residue = monomial % 4
        out[residue] += (
            (-1) ** (j + (monomial - residue) // 4)
            * comb(n, j)
            * products[j]
        )
    return tuple(out)


def coordinates(n: int, k: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    denominator = 4 ** (k - 1) * factorial(k - 1)
    return tuple(
        Fraction(value, denominator)
        for value in raw_coordinate_numerators(n, k)
    )


def monomial_reduction(monomial: int, k: int) -> tuple[Fraction, Fraction]:
    scale = Fraction(1)
    endpoint = Fraction(0)
    for j in range(k, 1, -1):
        endpoint += scale * Fraction(1, 4 * (j - 1) * 2 ** (j - 1))
        scale *= Fraction(4 * j - monomial - 5, 4 * (j - 1))
    return scale, endpoint


def polynomial_integral(monomial: int) -> Fraction:
    quotient, residue = divmod(monomial, 4)
    return sum(
        (
            Fraction((-1) ** u, residue + 4 * (quotient - 1 - u) + 1)
            for u in range(quotient)
        ),
        Fraction(),
    )


def rational_and_coordinates(
    n: int, k: int
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction, Fraction]]:
    rational = Fraction()
    out = [Fraction() for _ in range(4)]
    for j in range(n + 1):
        monomial = n + j
        coefficient = (-1) ** j * comb(n, j)
        scale, endpoint = monomial_reduction(monomial, k)
        quotient, residue = divmod(monomial, 4)
        out[residue] += coefficient * scale * (-1) ** quotient
        rational += coefficient * (
            endpoint + scale * polynomial_integral(monomial)
        )
    return rational, tuple(out)


def four_vector(
    logarithmic: list[Fraction], positive: list[Fraction]
) -> list[Fraction]:
    q = [
        logarithmic[1] * logarithmic[3] - logarithmic[2] ** 2,
        logarithmic[1] * logarithmic[2]
        - logarithmic[0] * logarithmic[3],
        logarithmic[0] * logarithmic[2] - logarithmic[1] ** 2,
    ]
    e0 = sum((q[j] * positive[j] for j in range(3)), Fraction())
    e1 = sum((q[j] * positive[j + 1] for j in range(3)), Fraction())
    return [
        e1 * q[0],
        e1 * q[1] - e0 * q[0],
        e1 * q[2] - e0 * q[1],
        -e0 * q[2],
    ]


def primitive_integer_vector(values: list[Fraction]) -> list[int]:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [
        value.numerator * (denominator // value.denominator)
        for value in values
    ]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    if content == 0:
        return integers
    return [value // content for value in integers]


def first_variation_identity() -> dict[str, bool]:
    u, v, x, y = sp.symbols("u v x y", real=True)
    ar, ai, br, bi = sp.symbols("ar ai br bi", real=True)
    p, d, f = sp.symbols("p d f", real=True)
    z = u + sp.I * v
    g = x + sp.I * y
    curvature = ar + sp.I * ai
    linear = br + sp.I * bi

    complex_base = [sp.expand(z * g**j) for j in range(4)]
    complex_first = [
        sp.expand(
            complex_base[j]
            * (curvature * j * (j - 1) + linear * j)
        )
        for j in range(4)
    ]
    real_base = [sp.re(value).expand() for value in complex_base]
    real_first = [sp.re(value).expand() for value in complex_first]
    imag_base = [sp.im(value).expand() for value in complex_base]
    imag_first = [sp.im(value).expand() for value in complex_first]
    positive_base = [p**j for j in range(4)]
    positive_first = [
        p**j * (d * j * (j - 1) + f * j)
        for j in range(4)
    ]

    def first_product(
        left0: sp.Expr,
        left1: sp.Expr,
        right0: sp.Expr,
        right1: sp.Expr,
    ) -> sp.Expr:
        return left1 * right0 + left0 * right1

    q0 = [
        real_base[1] * real_base[3] - real_base[2] ** 2,
        real_base[1] * real_base[2]
        - real_base[0] * real_base[3],
        real_base[0] * real_base[2] - real_base[1] ** 2,
    ]
    q1 = [
        first_product(
            real_base[1], real_first[1], real_base[3], real_first[3]
        )
        - 2 * real_base[2] * real_first[2],
        first_product(
            real_base[1], real_first[1], real_base[2], real_first[2]
        )
        - first_product(
            real_base[0], real_first[0], real_base[3], real_first[3]
        ),
        first_product(
            real_base[0], real_first[0], real_base[2], real_first[2]
        )
        - 2 * real_base[1] * real_first[1],
    ]

    e00 = sum(q0[j] * positive_base[j] for j in range(3))
    e01 = sum(
        q1[j] * positive_base[j] + q0[j] * positive_first[j]
        for j in range(3)
    )
    e10 = sum(q0[j] * positive_base[j + 1] for j in range(3))
    e11 = sum(
        q1[j] * positive_base[j + 1]
        + q0[j] * positive_first[j + 1]
        for j in range(3)
    )

    c0 = [
        e10 * q0[0],
        e10 * q0[1] - e00 * q0[0],
        e10 * q0[2] - e00 * q0[1],
        -e00 * q0[2],
    ]
    c1 = [
        e11 * q0[0] + e10 * q1[0],
        e11 * q0[1]
        + e10 * q1[1]
        - e01 * q0[0]
        - e00 * q1[0],
        e11 * q0[2]
        + e10 * q1[2]
        - e01 * q0[1]
        - e00 * q1[1],
        -e01 * q0[2] - e00 * q1[2],
    ]
    residual_first = sum(
        c1[j] * imag_base[j] + c0[j] * imag_first[j]
        for j in range(4)
    )
    expected = (
        4
        * y**4
        * (u**2 + v**2) ** 2
        * ((p - x) ** 2 + y**2)
        * sp.im(
            curvature
            * z
            * g**2
            * (sp.conjugate(g) - p)
        ).expand()
    )
    identity = sp.expand(residual_first - expected) == 0

    return {
        "first_variation_factorization": identity,
        "linear_complex_correction_cancels": identity
        and not ({br, bi} & expected.free_symbols),
        "all_positive_row_corrections_cancel": identity
        and not ({d, f} & expected.free_symbols),
    }


def saddle_correction_series() -> dict[str, bool]:
    r, variable = sp.symbols("r variable", positive=True, real=True)
    ui = (
        1
        + sp.I * r / 4
        + sp.Rational(9, 32) * r**2
        - sp.I * r**3 / 4
        + sp.Rational(247, 2048) * r**4
    )
    up = (
        1
        + r / 4
        - sp.Rational(9, 32) * r**2
        + r**3 / 4
        + sp.Rational(247, 2048) * r**4
    )
    psi = (
        sp.log(variable)
        + sp.log(1 + sp.I * r * variable)
        - sp.log(1 + r**4 * variable**4) / (4 * r**4)
    )
    saddle_error = sp.series(
        sp.diff(psi, variable).subs(variable, ui), r, 0, 5
    ).removeO()
    negative_hessian = sp.series(
        -sp.diff(psi, variable, 2).subs(variable, ui), r, 0, 3
    ).removeO()
    log_multiplier_prime = (
        -4 * r**4 * variable**3 / (1 + r**4 * variable**4)
    )
    curvature = sp.series(
        log_multiplier_prime.subs(variable, ui) ** 2
        / (2 * negative_hessian),
        r,
        0,
        10,
    ).removeO()
    gi = sp.series(1 / (1 + (r * ui) ** 4), r, 0, 7).removeO()
    gp = sp.series(1 / (1 + (r * up) ** 4), r, 0, 7).removeO()
    phase_factor = sp.series(
        curvature * gi**2 * (sp.conjugate(gi) - gp),
        r,
        0,
        15,
    ).removeO()
    outer_factor = sp.series(
        sp.im(gi) ** 4
        * (gp - gi)
        * (gp - sp.conjugate(gi)),
        r,
        0,
        31,
    ).removeO()

    expected_curvature = 2 * r**8 + sp.Rational(5, 2) * sp.I * r**9
    expected_phase_factor = (
        2 * (1 + sp.I) * r**13
        + (-sp.Rational(11, 2) + sp.Rational(5, 2) * sp.I) * r**14
    )
    expected_outer = 2 * r**30

    return {
        "complex_saddle_through_r4": sp.expand(saddle_error) == 0,
        "quadratic_shift_correction_through_r9": sp.expand(
            curvature - expected_curvature
        )
        == 0,
        "odd_residual_phase_factor_through_r14": sp.expand(
            phase_factor - expected_phase_factor
        )
        == 0,
        "phase_factor_relative_correction":
            sp.expand(
                expected_phase_factor
                - 2
                * (1 + sp.I)
                * r**13
                * (
                    1
                    + (-sp.Rational(3, 4) + 2 * sp.I) * r
                )
            )
            == 0,
        "positive_outer_factor_through_r30": sp.expand(
            outer_factor - expected_outer
        )
        == 0,
    }


def hermite_constant_checks() -> dict[str, bool]:
    pi = sp.pi
    alpha_magnitude = 2 * sp.sqrt(2) / pi
    beta = sp.sqrt(2) / pi
    invariant_complex = sp.simplify(
        -sp.Rational(2, 1)
        / pi
        * alpha_magnitude**4
        * beta
        * 4
    )
    expanded_complex = sp.simplify(
        invariant_complex
        * 2
        * 2
        * sp.sqrt(2)
    )
    real_saddle = sp.simplify(
        sp.Rational(2, 1)
        / pi
        * (-512 * sp.sqrt(2) / pi**5)
    )
    normalized_ratio = sp.simplify(
        8
        * (-512 * sp.sqrt(2) / pi**5)
        / (-4096 / pi**6)
    )
    return {
        "invariant_complex_hermite_constant": sp.simplify(
            invariant_complex + 512 * sp.sqrt(2) / pi**6
        )
        == 0,
        "expanded_phase_hermite_constant": sp.simplify(
            expanded_complex + 4096 / pi**6
        )
        == 0,
        "real_saddle_hermite_constant": sp.simplify(
            real_saddle + 1024 * sp.sqrt(2) / pi**6
        )
        == 0,
        "normalized_ratio_constant": sp.simplify(
            normalized_ratio - sp.sqrt(2) * pi
        )
        == 0,
    }


def exact_nonvanishing_and_sign_scan() -> dict[str, object]:
    zeros: list[list[int]] = []
    pairs = 0
    for n in range(4, 41, 2):
        for k in range(n + 1, min(100, 3 * n + 40) + 1):
            rows = [coordinates(n, k + j) for j in range(4)]
            logarithmic = [row[0] - row[2] for row in rows]
            positive = [row[0] + row[2] for row in rows]
            odd = [row[1] for row in rows]
            vector = four_vector(logarithmic, positive)
            residual = sum(
                (vector[j] * odd[j] for j in range(4)),
                Fraction(),
            )
            if residual == 0:
                zeros.append([n, k])
            pairs += 1

    sign_windows = []
    for n in (20, 40):
        lower = round(0.7 * n * math.log(n))
        upper = round(1.3 * n * math.log(n))
        previous = None
        changes = []
        signs = []
        for k in range(lower, upper + 1):
            rows = [coordinates(n, k + j) for j in range(4)]
            logarithmic = [row[0] - row[2] for row in rows]
            positive = [row[0] + row[2] for row in rows]
            odd = [row[1] for row in rows]
            vector = four_vector(logarithmic, positive)
            residual = sum(
                (vector[j] * odd[j] for j in range(4)),
                Fraction(),
            )
            sign = (residual > 0) - (residual < 0)
            if previous is not None and sign != previous:
                changes.append(k)
            previous = sign
            signs.append(sign)
        sign_windows.append(
            {
                "n": n,
                "k_lower": lower,
                "k_upper": upper,
                "sign_change_locations": changes,
                "zeros": signs.count(0),
            }
        )
    return {
        "pairs_checked": pairs,
        "zeros": zeros,
        "critical_sign_windows": sign_windows,
    }


def primitive_height_diagnostics() -> list[dict[str, int]]:
    records = []
    for n in range(8, 41, 4):
        k = round(n * math.log(n))
        data = [rational_and_coordinates(n, k + j) for j in range(4)]
        rows = [entry[1] for entry in data]
        logarithmic = [row[0] - row[2] for row in rows]
        positive = [row[0] + row[2] for row in rows]
        odd = [row[1] for row in rows]
        vector = four_vector(logarithmic, positive)
        primitive_vector = primitive_integer_vector(vector)
        rational_coordinate = sum(
            (vector[j] * data[j][0] for j in range(4)),
            Fraction(),
        )
        pi_coordinate = sum(
            (vector[j] * odd[j] / 8 for j in range(4)),
            Fraction(),
        )
        primitive_pair = primitive_integer_vector(
            [rational_coordinate, pi_coordinate]
        )
        records.append(
            {
                "n": n,
                "k": k,
                "primitive_coefficient_max_bits": max(
                    abs(value).bit_length()
                    for value in primitive_vector
                ),
                "primitive_endpoint_pair_max_bits": max(
                    abs(value).bit_length()
                    for value in primitive_pair
                ),
                "odd_coordinate_sign": (
                    (pi_coordinate > 0) - (pi_coordinate < 0)
                ),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/quartic_four_power_odd_residual_certificate.json"
        ),
    )
    args = parser.parse_args()

    variation = first_variation_identity()
    saddle = saddle_correction_series()
    constants = hermite_constant_checks()
    exact_scan = exact_nonvanishing_and_sign_scan()
    if not all(variation.values()):
        raise AssertionError(variation)
    if not all(saddle.values()):
        raise AssertionError(saddle)
    if not all(constants.values()):
        raise AssertionError(constants)
    if exact_scan["zeros"]:
        raise AssertionError(exact_scan)

    result = {
        "schema": "quartic-four-power-odd-residual-certificate-v1",
        "symbolic_first_variation": variation,
        "symbolic_saddle_correction": saddle,
        "hermite_constant_checks": constants,
        "exact_nonvanishing_and_sign_diagnostic": exact_scan,
        "primitive_height_diagnostic": primitive_height_diagnostics(),
        "warnings": [
            "The symbolic first-variation and saddle-series identities are exact.",
            "Finite nonvanishing and height scans are diagnostics, not all-parameter proofs.",
            "No all-integer-power phase-separation theorem is claimed.",
            "No primitive endpoint-content theorem is claimed.",
            "Nothing here classifies e+pi.",
        ],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
