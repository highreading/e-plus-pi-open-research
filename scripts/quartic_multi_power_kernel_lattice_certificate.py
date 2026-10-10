#!/usr/bin/env python3
"""Exact/finite certificate for adjacent quartic multi-power kernels."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

import sympy as sp


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    value = abs(value)
    return (value & -value).bit_length() - 1


def raw_coordinate_numerators(n: int, k: int) -> tuple[int, int, int, int]:
    out = [0, 0, 0, 0]
    products = [1] * (n + 1)
    for j in range(n + 1):
        m = n + j
        for s in range(1, k):
            products[j] *= 4 * s - m - 1
        residue = m % 4
        out[residue] += (
            (-1) ** (j + (m - residue) // 4) * comb(n, j) * products[j]
        )
    return tuple(out)


def coordinates(n: int, k: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    denominator = 4 ** (k - 1) * factorial(k - 1)
    return tuple(Fraction(value, denominator) for value in raw_coordinate_numerators(n, k))


def monomial_reduction(m: int, k: int) -> tuple[Fraction, Fraction]:
    scale = Fraction(1)
    endpoint = Fraction(0)
    for j in range(k, 1, -1):
        endpoint += scale * Fraction(1, 4 * (j - 1) * 2 ** (j - 1))
        scale *= Fraction(4 * j - m - 5, 4 * (j - 1))
    return scale, endpoint


def polynomial_integral(m: int) -> Fraction:
    q, residue = divmod(m, 4)
    return sum(
        (
            Fraction((-1) ** u, residue + 4 * (q - 1 - u) + 1)
            for u in range(q)
        ),
        Fraction(0),
    )


def rational_and_coordinates(
    n: int, k: int
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction, Fraction]]:
    rational = Fraction(0)
    out = [Fraction(0) for _ in range(4)]
    for j in range(n + 1):
        m = n + j
        coefficient = (-1) ** j * comb(n, j)
        scale, endpoint = monomial_reduction(m, k)
        q, residue = divmod(m, 4)
        out[residue] += coefficient * scale * (-1) ** q
        rational += coefficient * (endpoint + scale * polynomial_integral(m))
    return rational, tuple(out)


def triple_vector(
    logarithmic: list[Fraction], positive: list[Fraction]
) -> list[Fraction]:
    return [
        logarithmic[1] * positive[2] - logarithmic[2] * positive[1],
        logarithmic[2] * positive[0] - logarithmic[0] * positive[2],
        logarithmic[0] * positive[1] - logarithmic[1] * positive[0],
    ]


def four_vector(
    logarithmic: list[Fraction], positive: list[Fraction]
) -> tuple[list[Fraction], list[Fraction], Fraction, Fraction]:
    q = [
        logarithmic[1] * logarithmic[3] - logarithmic[2] ** 2,
        logarithmic[1] * logarithmic[2] - logarithmic[0] * logarithmic[3],
        logarithmic[0] * logarithmic[2] - logarithmic[1] ** 2,
    ]
    e0 = sum((q[j] * positive[j] for j in range(3)), Fraction())
    e1 = sum((q[j] * positive[j + 1] for j in range(3)), Fraction())
    c = [
        e1 * q[0],
        e1 * q[1] - e0 * q[0],
        e1 * q[2] - e0 * q[1],
        -e0 * q[2],
    ]
    return c, q, e0, e1


def primitive_integer_vector(values: list[Fraction]) -> list[int]:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [value.numerator * (denominator // value.denominator) for value in values]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    if content == 0:
        return integers
    return [value // content for value in integers]


def symbolic_geometric_checks() -> dict[str, bool]:
    u, v, x, y, p, m, t = sp.symbols("u v x y p m t", real=True)
    z = u + sp.I * v
    g = x + sp.I * y

    real_row = sp.Matrix([[sp.re(sp.expand(z * g**j)) for j in range(3)]])
    imag_row = sp.Matrix([[sp.im(sp.expand(z * g**j)) for j in range(3)]])
    p_row = sp.Matrix([[p**j for j in range(3)]])
    m_row = sp.Matrix([[m**j for j in range(3)]])

    delta = sp.expand(real_row[0, 1] ** 2 - real_row[0, 0] * real_row[0, 2])
    expected_delta = (u**2 + v**2) * y**2

    quadrature_det = sp.expand(sp.Matrix.vstack(real_row, p_row, imag_row).det())
    expected_quadrature = -y * (u**2 + v**2) * ((p - x) ** 2 + y**2)

    real_det = sp.expand(sp.Matrix.vstack(real_row, p_row, m_row).det())
    complex_vandermonde = z * (p - g) * (m - g) * (m - p)
    expected_real_det = sp.expand(sp.re(sp.expand(complex_vandermonde)))

    l0, l1, l2, l3 = [sp.re(sp.expand(z * g**j)) for j in range(4)]
    q0 = sp.expand(l1 * l3 - l2**2)
    q1 = sp.expand(l1 * l2 - l0 * l3)
    q2 = sp.expand(l0 * l2 - l1**2)
    q_polynomial = sp.expand(q0 + q1 * t + q2 * t**2)
    expected_q = sp.expand(q2 * ((t - x) ** 2 + y**2))

    r = sp.symbols("r", positive=True)
    gi = 1 - r**4 - sp.I * r**5 - sp.Rational(3, 4) * r**6 + sp.Rational(7, 32) * sp.I * r**7
    gp = 1 - r**4 - r**5 + sp.Rational(3, 4) * r**6 - sp.Rational(7, 32) * r**7
    gm = 1 - r**4 + r**5 + sp.Rational(3, 4) * r**6 + sp.Rational(7, 32) * r**7
    root_series = {
        "minus_imag_g_over_r5": sp.limit(-sp.im(gi) / r**5, r, 0) == 1,
        "abs_p_minus_g_squared_over_r10": sp.limit(sp.expand_complex((gp - gi) * (gp - sp.conjugate(gi))) / r**10, r, 0) == 2,
        "p_minus_m_over_r5": sp.limit((gp - gm) / r**5, r, 0) == -2,
        "abs_m_minus_g_squared_over_r10": sp.limit(sp.expand_complex((gm - gi) * (gm - sp.conjugate(gi))) / r**10, r, 0) == 2,
    }

    # Every real, positive-real, and complex saddle is obtained from the
    # same degree-five stationary equation.  Eliminating x in favor of
    # t=(1+x^4)^(-1) gives the polynomial recorded in the companion note.
    saddle_x, saddle_n, saddle_k = sp.symbols(
        "saddle_x saddle_n saddle_k", nonzero=True
    )
    saddle_a = (4 * saddle_k - saddle_n) * saddle_x**4 - saddle_n
    saddle_b = (4 * saddle_k - 2 * saddle_n) * saddle_x**4 - 2 * saddle_n
    saddle_equation = sp.expand(
        saddle_n * (1 - 2 * saddle_x) * (1 + saddle_x**4)
        - 4 * saddle_k * saddle_x**4 * (1 - saddle_x)
    )
    saddle_numerator = sp.expand(saddle_a**4 - saddle_x**4 * saddle_b**4)
    _, saddle_remainder = sp.div(saddle_numerator, saddle_equation, saddle_x)

    root_filter_ok = True
    for even_n in range(2, 42, 2):
        for exponent in range(even_n + 1):
            gaussian_projection = 2 * int(
                round((sp.I ** (even_n - 1 + exponent)).as_real_imag()[0])
            )
            selected = (
                1
                - (-1) ** exponent
                + gaussian_projection
            ) // 4
            root_filter_ok &= selected == int(
                (even_n + exponent) % 4 == 1
            )

    # The nonlinear four-power value used in the error argument is
    # multihomogeneous of degrees (4, 1, 1) in the L, E, and J rows.
    symbolic_l = sp.symbols("symbolic_l0:4")
    symbolic_e = sp.symbols("symbolic_e0:4")
    symbolic_j = sp.symbols("symbolic_j0:4")
    scale_l, scale_e, scale_j = sp.symbols("scale_l scale_e scale_j")
    symbolic_q = [
        symbolic_l[1] * symbolic_l[3] - symbolic_l[2] ** 2,
        symbolic_l[1] * symbolic_l[2] - symbolic_l[0] * symbolic_l[3],
        symbolic_l[0] * symbolic_l[2] - symbolic_l[1] ** 2,
    ]
    symbolic_e0 = sum(symbolic_q[j] * symbolic_e[j] for j in range(3))
    symbolic_e1 = sum(symbolic_q[j] * symbolic_e[j + 1] for j in range(3))
    symbolic_c = [
        symbolic_e1 * symbolic_q[0],
        symbolic_e1 * symbolic_q[1] - symbolic_e0 * symbolic_q[0],
        symbolic_e1 * symbolic_q[2] - symbolic_e0 * symbolic_q[1],
        -symbolic_e0 * symbolic_q[2],
    ]
    symbolic_value = sp.expand(
        sum(symbolic_c[j] * symbolic_j[j] for j in range(4))
    )
    scaled_value = sp.expand(
        symbolic_value.subs(
            {
                **{entry: scale_l * entry for entry in symbolic_l},
                **{entry: scale_e * entry for entry in symbolic_e},
                **{entry: scale_j * entry for entry in symbolic_j},
            },
            simultaneous=True,
        )
    )
    four_value_multihomogeneous = (
        sp.expand(
            scaled_value
            - scale_l**4 * scale_e * scale_j * symbolic_value
        )
        == 0
    )

    return {
        "delta_identity": sp.expand(delta - expected_delta) == 0,
        "quadrature_determinant_identity": sp.expand(quadrature_det - expected_quadrature) == 0,
        "real_vandermonde_identity": sp.expand(real_det - expected_real_det) == 0,
        "hankel_annihilator_identity": sp.expand(q_polynomial - expected_q) == 0,
        "odd_coordinate_root_filter": root_filter_ok,
        "saddle_multiplier_elimination": sp.expand(saddle_remainder) == 0,
        "four_value_multihomogeneous_degrees_4_1_1":
            four_value_multihomogeneous,
        **root_series,
    }


def exact_kernel_scan(n_max: int, k_max: int) -> dict[str, object]:
    triple_b_zeros: list[list[int]] = []
    four_vector_zeros: list[list[int]] = []
    four_b_zeros: list[list[int]] = []
    identity_failures: list[list[int | str]] = []
    count = 0
    for n in range(4, n_max + 1, 2):
        for k in range(n + 1, k_max + 1):
            rows = [coordinates(n, k + j) for j in range(4)]
            logarithmic = [row[0] - row[2] for row in rows]
            positive = [row[0] + row[2] for row in rows]
            odd = [row[1] for row in rows]

            triple = triple_vector(logarithmic[:3], positive[:3])
            if sum((triple[j] * logarithmic[j] for j in range(3)), Fraction()):
                identity_failures.append([n, k, "triple-L"])
            if sum((triple[j] * positive[j] for j in range(3)), Fraction()):
                identity_failures.append([n, k, "triple-E"])
            if sum((triple[j] * odd[j] for j in range(3)), Fraction()) == 0:
                triple_b_zeros.append([n, k])

            four, q, _, _ = four_vector(logarithmic, positive)
            if all(value == 0 for value in four):
                four_vector_zeros.append([n, k])
            if sum((q[j] * logarithmic[j] for j in range(3)), Fraction()):
                identity_failures.append([n, k, "Q-L0"])
            if sum((q[j] * logarithmic[j + 1] for j in range(3)), Fraction()):
                identity_failures.append([n, k, "Q-L1"])
            if sum((four[j] * logarithmic[j] for j in range(4)), Fraction()):
                identity_failures.append([n, k, "four-L"])
            if sum((four[j] * positive[j] for j in range(4)), Fraction()):
                identity_failures.append([n, k, "four-E"])
            if sum((four[j] * odd[j] for j in range(4)), Fraction()) == 0:
                four_b_zeros.append([n, k])
            count += 1
    return {
        "pairs_checked": count,
        "identity_failures": identity_failures,
        "triple_b_zeros": triple_b_zeros,
        "four_vector_zeros": four_vector_zeros,
        "four_b_zeros": four_b_zeros,
    }


def finite_difference_denominator_scan() -> dict[str, object]:
    failures: list[dict[str, int | str]] = []
    checks = 0
    records = []
    for n in range(4, 25, 4):
        for k in (n + 3, n + 7, n + 11, 2 * n + 5):
            values = [rational_and_coordinates(n, k + j) for j in range(13)]
            for s in range(13):
                rational = sum(
                    (
                        (-1) ** j * comb(s, j) * values[j][0]
                        for j in range(s + 1)
                    ),
                    Fraction(),
                )
                logarithmic = sum(
                    (
                        (-1) ** j
                        * comb(s, j)
                        * (values[j][1][0] - values[j][1][2])
                        for j in range(s + 1)
                    ),
                    Fraction(),
                )
                positive = sum(
                    (
                        (-1) ** j
                        * comb(s, j)
                        * (values[j][1][0] + values[j][1][2])
                        for j in range(s + 1)
                    ),
                    Fraction(),
                )
                power = k + s
                universal_exponent = 3 * (power - 1) - (power - 1).bit_count()
                expected_coordinate_exponent = universal_exponent - n // 4
                observed = {
                    "L": v2(logarithmic.denominator),
                    "E": v2(positive.denominator),
                    "R": v2(rational.denominator),
                }
                expected = {
                    "L": expected_coordinate_exponent,
                    "E": expected_coordinate_exponent,
                    "R": expected_coordinate_exponent + 1,
                }
                for name in expected:
                    if observed[name] != expected[name]:
                        failures.append(
                            {
                                "n": n,
                                "k": k,
                                "difference_order": s,
                                "coordinate": name,
                                "observed": observed[name],
                                "expected": expected[name],
                            }
                        )
                checks += 3
            records.append(
                {
                    "n": n,
                    "base_k": k,
                    "largest_difference_order": 12,
                }
            )
    return {"checks": checks, "failures": failures, "parameter_records": records}


def primitive_height_diagnostics() -> list[dict[str, int | float]]:
    records = []
    for n in range(8, 41, 4):
        k = round(n * math.log(n))
        data = [rational_and_coordinates(n, k + j) for j in range(3)]
        rational = [entry[0] for entry in data]
        rows = [entry[1] for entry in data]
        logarithmic = [row[0] - row[2] for row in rows]
        positive = [row[0] + row[2] for row in rows]
        odd = [row[1] for row in rows]
        triple = triple_vector(logarithmic, positive)
        primitive_triple = primitive_integer_vector(triple)
        a_coordinate = sum((triple[j] * rational[j] for j in range(3)), Fraction())
        b_coordinate = sum((triple[j] * odd[j] / 8 for j in range(3)), Fraction())
        primitive_period = primitive_integer_vector([a_coordinate, b_coordinate])
        records.append(
            {
                "n": n,
                "k": k,
                "primitive_kernel_max_bits": max(abs(value).bit_length() for value in primitive_triple),
                "primitive_rational_pi_max_bits": max(abs(value).bit_length() for value in primitive_period),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/quartic_multi_power_kernel_lattice_certificate.json"),
    )
    args = parser.parse_args()

    symbolic = symbolic_geometric_checks()
    exact_scan = exact_kernel_scan(30, 45)
    denominators = finite_difference_denominator_scan()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    if exact_scan["identity_failures"]:
        raise AssertionError(exact_scan)
    if denominators["failures"]:
        raise AssertionError(denominators)

    result = {
        "schema": "quartic-multi-power-kernel-lattice-certificate-v2",
        "symbolic_geometric_checks": symbolic,
        "exact_kernel_scan": exact_scan,
        "finite_difference_denominator_diagnostic": denominators,
        "primitive_height_diagnostics": primitive_height_diagnostics(),
        "warnings": [
            "Finite nonvanishing and denominator scans are diagnostics, not all-parameter proofs.",
            "The exact lattice and determinant identities are proved algebraically in the companion note.",
            "The growing-number-of-powers route is not closed by this certificate.",
            "The four-power sign uses the proved sufficient condition n*r^45 -> infinity.",
            "Nothing here classifies e+pi.",
        ],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
