#!/usr/bin/env python3
"""Exact certificate for the smallest genuine mixed extension.

The script checks the rank-three system, its normalized fundamental
matrix, the split limiting case, the endpoint gauge exposing
e + pi + K(1), and the monodromy commutator used in
sources/explicit_nonsplit_mixed_extension_audit.md.
"""

import json

import sympy as sp


def matrix_is_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_doit_simplify(matrix):
    return matrix.applyfunc(lambda entry: sp.simplify(entry.doit()))


z, t = sp.symbols("z t", real=True)
a, b, c, d = sp.symbols("a b c d")
B, kappa, delta_i, lambda_2 = sp.symbols(
    "B kappa delta_i lambda_2"
)

x = sp.exp(z)
y = -4 * sp.atan(z)
q = -4 / (1 + z**2)
r = 1 / (z - 2)

J = x * sp.Integral(sp.exp(-t) / (t - 2), (t, 0, z))
K = x * sp.Integral(
    sp.exp(-t) * (-4 * sp.atan(t)) / (t - 2), (t, 0, z)
)

# The genuinely cross-coupled extension.  Relative to the split system,
# the added term is r(z)*y in the last differential equation.
A_cross = sp.Matrix(
    [
        [0, 0, 0],
        [q, 0, 0],
        [-q, 1 + r, 1],
    ]
)
Phi_cross = sp.Matrix(
    [
        [1, 0, 0],
        [y, 1, 0],
        [-y + K, x - 1 + J, x],
    ]
)

# The r=0 case is rationally split by w -> w+y.
A_split = sp.Matrix(
    [
        [0, 0, 0],
        [q, 0, 0],
        [-q, 1, 1],
    ]
)
P_split = sp.eye(3)
P_split[2, 1] = 1
A_split_decoupled = sp.simplify(P_split * A_split * P_split.inv())
A_split_expected = sp.Matrix([[0, 0, 0], [q, 0, 0], [0, 0, 1]])

# An endpoint-regular gauge with P(1)=I and
# P(0)^(-1)=I+E_31 turns the algebraic matrix coefficient
# C_31+C_33 into a literal normalized connection entry.
E31 = sp.zeros(3)
E31[2, 0] = 1
P_endpoint = sp.eye(3) - (1 - z) * E31
A_endpoint = sp.simplify(
    P_endpoint.diff(z) * P_endpoint.inv()
    + P_endpoint * A_cross * P_endpoint.inv()
)
Phi_endpoint = sp.simplify(
    P_endpoint * Phi_cross * P_endpoint.subs(z, 0).inv()
)

J1_integral = sp.E * sp.Integral(
    sp.exp(-t) / (t - 2), (t, 0, 1)
)
J1_ei = sp.exp(-1) * (sp.Ei(1) - sp.Ei(2))
K1 = sp.E * sp.Integral(
    sp.exp(-t) * (-4 * sp.atan(t)) / (t - 2), (t, 0, 1)
)
J_explicit = sp.exp(z - 2) * (sp.Ei(2 - z) - sp.Ei(2))

C_cross = sp.Matrix(
    [
        [1, 0, 0],
        [-sp.pi, 1, 0],
        [sp.pi + K1, sp.E - 1 + J1_integral, sp.E],
    ]
)
C_endpoint = sp.simplify(
    P_endpoint.subs(z, 1)
    * C_cross
    * P_endpoint.subs(z, 0).inv()
)

# Generic differential automorphism and its matrix in the normalized
# fundamental basis:
# x -> a*x, y -> y+b, J -> J+c*x, K -> K+b*J+d*x.
x0, y0, j0, k0 = sp.symbols("x0 y0 j0 k0")
Phi_formal = sp.Matrix(
    [[1, 0, 0], [y0, 1, 0], [-y0 + k0, x0 - 1 + j0, x0]]
)
Phi_sigma = sp.Matrix(
    [
        [1, 0, 0],
        [y0 + b, 1, 0],
        [
            -(y0 + b) + (k0 + b * j0 + d * x0),
            a * x0 - 1 + (j0 + c * x0),
            a * x0,
        ],
    ]
)
g_abcd = sp.Matrix(
    [[1, 0, 0], [b, 1, 0], [-b + d, a + c - 1, a]]
)

# Around i, b=B=-4*pi and c=0.  Around 2, b=0 and
# c=kappa=2*pi*i*exp(-2).  The unspecified central translations cancel
# from the commutator.
monodromy_i = sp.Matrix(
    [[1, 0, 0], [B, 1, 0], [delta_i - B, 0, 1]]
)
monodromy_2 = sp.Matrix(
    [[1, 0, 0], [0, 1, 0], [lambda_2, kappa, 1]]
)
monodromy_commutator = sp.simplify(
    monodromy_i
    * monodromy_2
    * monodromy_i.inv()
    * monodromy_2.inv()
)
commutator_expected = sp.eye(3)
commutator_expected[2, 0] = -B * kappa

checks = {
    "J_differential_equation": sp.simplify(sp.diff(J, z) - J - r) == 0,
    "K_differential_equation": (
        sp.simplify(sp.diff(K, z) - K - r * y) == 0
    ),
    "cross_fundamental_system": matrix_is_zero(
        Phi_cross.diff(z) - A_cross * Phi_cross
    ),
    "cross_fundamental_at_zero": (
        matrix_doit_simplify(Phi_cross.subs(z, 0)) == sp.eye(3)
    ),
    "cross_connection_at_one": (
        matrix_is_zero(Phi_cross.subs(z, 1) - C_cross)
    ),
    "split_case_decouples": A_split_decoupled == A_split_expected,
    "endpoint_gauged_fundamental_system": matrix_is_zero(
        Phi_endpoint.diff(z) - A_endpoint * Phi_endpoint
    ),
    "endpoint_gauged_fundamental_at_zero": (
        matrix_doit_simplify(Phi_endpoint.subs(z, 0)) == sp.eye(3)
    ),
    "endpoint_gauge_regular_and_unimodular": (
        sp.simplify(P_endpoint.det()) == 1
    ),
    "endpoint_connection_target_entry": (
        sp.simplify(C_endpoint[2, 0] - (sp.E + sp.pi + K1)) == 0
    ),
    "J1_Ei_formula_derivative_normalization": (
        sp.simplify(
            sp.diff(J_explicit, z) - J_explicit - r
        )
        == 0
    ),
    "J_Ei_formula_at_zero": sp.simplify(J_explicit.subs(z, 0)) == 0,
    "generic_galois_action_matrix": matrix_is_zero(
        Phi_formal * g_abcd - Phi_sigma
    ),
    "monodromy_commutator": (
        monodromy_commutator == commutator_expected
    ),
}

assert all(checks.values())

result = {
    "certificate": "explicit_nonsplit_mixed_extension",
    "sympy_version": sp.__version__,
    "checks": checks,
    "exact_data": {
        "q": str(q),
        "r": str(r),
        "A_cross": str(A_cross),
        "Phi_cross": str(Phi_cross),
        "A_split_decoupled": str(A_split_decoupled),
        "endpoint_gauge": str(P_endpoint),
        "endpoint_gauged_connection": str(C_endpoint),
        "target_connection_entry": str(C_endpoint[2, 0]),
        "J1_integral": str(J1_integral),
        "J1_Ei": str(J1_ei),
        "K1": str(K1),
        "generic_galois_matrix": str(g_abcd),
        "monodromy_i_symbolic": str(monodromy_i),
        "monodromy_2_symbolic": str(monodromy_2),
        "monodromy_commutator": str(monodromy_commutator),
        "B_value": "-4*pi",
        "kappa_value": "2*pi*i*exp(-2)",
        "central_commutator_value": "8*pi**2*i*exp(-2)",
        "K1_sign": "positive: r(t)<0 and y(t)<0 for 0<t<1",
        "nonsplitting_obstruction": (
            "r1'-r1=1+r forces a rational solution of "
            "R'-R=1/(z-2), impossible by pole order at z=2"
        ),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
