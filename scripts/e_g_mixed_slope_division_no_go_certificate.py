#!/usr/bin/env python3
"""Exact symbolic checks for e_g_mixed_slope_division_no_go.md."""

from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def q_coefficient(n: int, alpha: sp.Symbol) -> sp.Expr:
    exponential_partial = sum(Fraction(1, sp.factorial(k)) for k in range(n + 1))
    arctangent_partial = sum(
        Fraction(4 * ((-1) ** m), 2 * m + 1)
        for m in range((n - 1) // 2 + 1)
    )
    return sp.expand(-alpha + sp.Rational(exponential_partial.numerator,
                                          exponential_partial.denominator)
                     + sp.Rational(arctangent_partial.numerator,
                                   arctangent_partial.denominator))


def main() -> None:
    z, alpha = sp.symbols("z alpha")
    r = 1 / (1 + z**2)
    A = -((z - 1) * (z**2 - 3)) / ((z + 1) * (z**2 + 1))
    B = -(2 * (z**2 + 2 * z - 1)) / ((z + 1) * (z**2 + 1))

    exp_identity = sp.factor(1 + A + B)
    atan_identity = sp.factor(sp.diff(r, z, 2) + A * sp.diff(r, z) + B * r)

    cyclic_matrix = sp.Matrix([
        [alpha, -1, -4],
        [-4 * r, -1, 0],
        [-4 * sp.diff(r, z), -1, 0],
    ])
    cyclic_determinant = sp.factor(cyclic_matrix.det())
    expected_determinant = -16 * (z + 1) ** 2 / (z**2 + 1) ** 2

    # If L = D^3 + A D^2 + B D, then L((z-1)y) has these
    # coefficients on y''', y'', y', y, respectively.
    gauge_coefficients = [
        z - 1,
        sp.factor(3 + A * (z - 1)),
        sp.factor(2 * A + B * (z - 1)),
        sp.factor(B),
    ]

    # Verify H=(z-1)Q coefficientwise through a nontrivial exact prefix.
    prefix_length = 40
    q = [q_coefficient(n, alpha) for n in range(prefix_length + 1)]
    h_from_q = [-q[0]] + [sp.expand(q[n - 1] - q[n]) for n in range(1, prefix_length + 1)]
    h_expected = [alpha - 1]
    for n in range(1, prefix_length + 1):
        value = -sp.Rational(1, sp.factorial(n))
        if n % 2 == 1:
            m = (n - 1) // 2
            value -= sp.Rational(4 * ((-1) ** m), n)
        h_expected.append(sp.expand(value))

    assertions = {
        "exp_identity_zero": exp_identity == 0,
        "atan_identity_zero": atan_identity == 0,
        "cyclic_determinant_exact": sp.factor(cyclic_determinant - expected_determinant) == 0,
        "cyclic_determinant_nonzero": cyclic_determinant != 0,
        "coefficient_identity_prefix": h_from_q == h_expected,
        "gauge_leading_factor_is_z_minus_1": sp.expand(gauge_coefficients[0] - (z - 1)) == 0,
    }
    if not all(assertions.values()):
        raise AssertionError(assertions)

    result = {
        "artifact": "e_g_mixed_slope_division_no_go_certificate",
        "arithmetic": "exact symbolic/rational",
        "assertions": assertions,
        "A": sp.sstr(sp.factor(A)),
        "B": sp.sstr(sp.factor(B)),
        "cyclic_determinant": sp.sstr(cyclic_determinant),
        "gauge_coefficients_y3_y2_y1_y0": [sp.sstr(c) for c in gauge_coefficients],
        "q_prefix": [sp.sstr(value) for value in q[:8]],
        "verified_coefficient_prefix_length": prefix_length,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
