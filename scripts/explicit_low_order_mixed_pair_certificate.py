#!/usr/bin/env python3
"""Exact symbolic checks for the low-order mixed E/G pair.

This script is deliberately finite and deterministic.  It certifies the
differential systems, connection matrix, scalar annihilator, inverse-Borel
identity, rational gauge equivalence, and Laplace values used in
sources/explicit_low_order_mixed_pair_monodromy_stokes_audit.md.
"""

import json

import sympy as sp


def matrix_is_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


z, t, sigma = sp.symbols("z t sigma")
i = sp.I

# The rank-three mixed system for (1, exp(z), sigma-4 atan(z)).
mixed_matrix = sp.Matrix(
    [
        [0, 0, 0],
        [0, 1, 0],
        [-4 / (1 + z**2), 0, 0],
    ]
)
mixed_fundamental = sp.Matrix(
    [
        [1, 0, 0],
        [0, sp.exp(z), 0],
        [-4 * sp.atan(z), 0, 1],
    ]
)
mixed_solution = sp.Matrix([1, sp.exp(z), sigma - 4 * sp.atan(z)])

# A scalar order-three operator annihilating 1, exp(z), and atan(z).
scalar_A = -((z - 1) * (z**2 - 3)) / ((z + 1) * (z**2 + 1))
scalar_B = -2 * (z**2 + 2 * z - 1) / ((z + 1) * (z**2 + 1))


def scalar_operator(f):
    return sp.simplify(
        sp.diff(f, z, 3)
        + scalar_A * sp.diff(f, z, 2)
        + scalar_B * sp.diff(f, z)
    )


# A regular-at-1 E-system containing exp(z) and the components of L_sigma.
e_matrix = sp.Matrix(
    [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 1 / z, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, -1, 0],
    ]
)
e_vector = sp.Matrix(
    [1, sp.exp(z), sp.exp(-z), sp.Si(z), sp.sin(z), sp.cos(z)]
)
L_sigma = sigma * (1 - sp.exp(-z)) - 2 * sp.Si(z)
L_from_vector = sigma * e_vector[0] - sigma * e_vector[2] - 2 * e_vector[3]

# Inverse-Borel transform and the original arctangent interpolant.
B_sigma = sigma * t / (1 + t) - 2 * sp.atan(t)
A_sigma = sigma - 4 * sp.atan(t)
rational_gauge = sigma * (t - 1) / (t + 1)

# Coefficient-by-coefficient inverse-Borel check.
coefficient_cutoff = 30
B_series = sp.series(B_sigma, t, 0, coefficient_cutoff + 1).removeO().expand()
borel_coefficients_match = True
for n in range(coefficient_cutoff + 1):
    expected = sp.Integer(0)
    if n >= 1:
        expected += sigma * (-1) ** (n + 1)
    if n % 2 == 1:
        k = (n - 1) // 2
        expected += -2 * (-1) ** k / sp.Integer(2 * k + 1)
    if sp.simplify(B_series.coeff(t, n) - expected) != 0:
        borel_coefficients_match = False
        break

# Exact Laplace values at parameter 1.
x = sp.symbols("x", positive=True)
laplace_one_minus_exp = sp.integrate(
    sp.exp(-x) * (1 - sp.exp(-x)), (x, 0, sp.oo)
)
laplace_si = sp.integrate(sp.exp(-x) * sp.Si(x), (x, 0, sp.oo))

# Wronskian of 1, exp(z), atan(z), useful for linear independence.
wronskian = sp.simplify(
    sp.det(
        sp.Matrix(
            [
                [1, sp.exp(z), sp.atan(z)],
                [0, sp.exp(z), 1 / (1 + z**2)],
                [
                    0,
                    sp.exp(z),
                    sp.diff(1 / (1 + z**2), z),
                ],
            ]
        )
    )
)

result = {
    "certificate": "explicit_low_order_mixed_pair",
    "sympy_version": sp.__version__,
    "checks": {
        "mixed_fundamental_system_residual_zero": matrix_is_zero(
            mixed_fundamental.diff(z) - mixed_matrix * mixed_fundamental
        ),
        "mixed_solution_system_residual_zero": matrix_is_zero(
            mixed_solution.diff(z) - mixed_matrix * mixed_solution
        ),
        "mixed_fundamental_at_zero_is_identity": (
            mixed_fundamental.subs(z, 0) == sp.eye(3)
        ),
        "scalar_operator_annihilates_one": scalar_operator(sp.Integer(1)) == 0,
        "scalar_operator_annihilates_exp": scalar_operator(sp.exp(z)) == 0,
        "scalar_operator_annihilates_atan": scalar_operator(sp.atan(z)) == 0,
        "closed_E_system_residual_zero": matrix_is_zero(
            e_vector.diff(z) - e_matrix * e_vector
        ),
        "L_sigma_is_claimed_linear_combination": (
            sp.simplify(L_sigma - L_from_vector) == 0
        ),
        "inverse_borel_coefficients_match": borel_coefficients_match,
        "inverse_borel_checked_through_degree": coefficient_cutoff,
        "twice_borel_minus_atan_interpolant_is_rational_gauge": (
            sp.simplify(2 * B_sigma - A_sigma - rational_gauge) == 0
        ),
        "rational_gauge_vanishes_at_one": (
            sp.simplify(rational_gauge.subs(t, 1)) == 0
        ),
        "B_sigma_at_one": str(sp.simplify(B_sigma.subs(t, 1))),
        "B_sigma_residue_at_minus_one": str(
            sp.simplify(sp.limit((t + 1) * B_sigma, t, -1))
        ),
        "laplace_one_minus_exp": str(laplace_one_minus_exp),
        "laplace_Si": str(laplace_si),
        "laplace_L_sigma": str(
            sp.simplify(
                sigma * laplace_one_minus_exp - 2 * laplace_si
            )
        ),
    },
    "exact_data": {
        "mixed_matrix": str(mixed_matrix),
        "mixed_fundamental": str(mixed_fundamental),
        "mixed_connection_at_one": str(
            sp.simplify(mixed_fundamental.subs(z, 1))
        ),
        "mixed_solution_at_one": str(
            sp.simplify(mixed_solution.subs(z, 1))
        ),
        "wronskian_1_exp_atan": str(wronskian),
        "scalar_A": str(sp.factor(scalar_A)),
        "scalar_B": str(sp.factor(scalar_B)),
        "closed_E_matrix": str(e_matrix),
        "inverse_borel": str(B_sigma),
        "twice_inverse_borel_minus_original": str(
            sp.simplify(2 * B_sigma - A_sigma)
        ),
        "atan_log_formula": "atan(z)=(log(1+i*z)-log(1-i*z))/(2*i)",
        "atan_ccw_jump_at_i": "pi",
        "atan_ccw_jump_at_minus_i": "-pi",
        "mixed_monodromy_ccw_at_i": "I_3-4*pi*E_31",
        "mixed_monodromy_ccw_at_minus_i": "I_3+4*pi*E_31",
        "B_sigma_ccw_jump_at_i": "-2*pi",
        "B_sigma_ccw_jump_at_minus_i": "2*pi",
    },
}

assert all(
    value is True or key in {
        "inverse_borel_checked_through_degree",
        "B_sigma_at_one",
        "B_sigma_residue_at_minus_one",
        "laplace_one_minus_exp",
        "laplace_Si",
        "laplace_L_sigma",
    }
    for key, value in result["checks"].items()
)

print(json.dumps(result, indent=2, sort_keys=True))
