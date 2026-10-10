#!/usr/bin/env python3
"""Exact tensor, exterior-power, and gauge checks for the mixed pair.

This is a finite deterministic companion to
sources/explicit_mixed_pair_tensor_gauge_no_go.md.  The general field and
representation-theoretic assertions in that note are proved there; this
script certifies every displayed matrix identity used in the concrete
examples.
"""

import json

import sympy as sp


def matrix_is_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


def exterior_square(matrix):
    """Matrix of wedge^2(matrix) in the basis 01, 02, 12."""
    pairs = [(0, 1), (0, 2), (1, 2)]
    return sp.Matrix(
        [
            [
                sp.det(matrix.extract(row_pair, column_pair))
                for column_pair in pairs
            ]
            for row_pair in pairs
        ]
    )


z, x, y, a, b, sigma = sp.symbols("z x y a b sigma")

q = -4 / (1 + z**2)
h = -4 * sp.atan(z)
X = sp.exp(z)

# The faithful standard representation of G_m x G_a.
group_xy = sp.Matrix([[1, 0, 0], [0, x, 0], [y, 0, 1]])
group_ab = sp.Matrix([[1, 0, 0], [0, a, 0], [b, 0, 1]])
group_product_expected = sp.Matrix(
    [[1, 0, 0], [0, x * a, 0], [y + b, 0, 1]]
)

M = sp.Matrix([[0, 0, 0], [0, 1, 0], [q, 0, 0]])
Phi = sp.Matrix([[1, 0, 0], [0, X, 0], [h, 0, 1]])

# Exterior square of the standard representation.
wedge2_Phi = sp.simplify(exterior_square(Phi))
wedge2_expected = sp.Matrix(
    [[X, 0, 0], [0, 1, 0], [-X * h, 0, X]]
)
wedge2_connection_expected = sp.Matrix(
    [[sp.E, 0, 0], [0, 1, 0], [sp.E * sp.pi, 0, sp.E]]
)

# The smallest visibly coupled tensor representation: the exponential line
# tensored with the two-dimensional logarithmic representation.
tensor_fundamental = sp.Matrix([[X, 0], [X * h, X]])
tensor_matrix = sp.Matrix([[1, 0], [q, 1]])
tensor_connection_expected = sp.Matrix(
    [[sp.E, 0], [-sp.E * sp.pi, sp.E]]
)

# A rational gauge that visually mixes all three standard coordinates.
nilpotent = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
P = sp.eye(3) + z * nilpotent
P_inverse = sp.simplify(P.inv())
gauged_matrix = sp.simplify(P.diff(z) * P_inverse + P * M * P_inverse)
gauged_fundamental = sp.simplify(P * Phi)  # P(0)=I.
gauged_connection = sp.simplify(gauged_fundamental.subs(z, 1))
connection = sp.simplify(Phi.subs(z, 1))
recovered_connection = sp.simplify(P.subs(z, 1).inv() * gauged_connection)

# The target hyperplane is not stable under right translation.  On the
# hyperplane y=x-sigma, its right translate has residual x(a-1)-b.
target_polynomial = x - y - sigma
right_translated_target = x * a - (y + b) - sigma
translated_residual_on_target = sp.expand(
    right_translated_target.subs(y, x - sigma)
)

checks = {
    "standard_group_law": matrix_is_zero(
        group_xy * group_ab - group_product_expected
    ),
    "standard_fundamental_system": matrix_is_zero(Phi.diff(z) - M * Phi),
    "standard_fundamental_at_zero": Phi.subs(z, 0) == sp.eye(3),
    "wedge2_formula": matrix_is_zero(wedge2_Phi - wedge2_expected),
    "wedge2_connection_at_one": (
        sp.simplify(wedge2_Phi.subs(z, 1))
        == wedge2_connection_expected
    ),
    "wedge3_is_exp": sp.simplify(Phi.det() - X) == 0,
    "tensor_coupling_system": matrix_is_zero(
        tensor_fundamental.diff(z) - tensor_matrix * tensor_fundamental
    ),
    "tensor_coupling_at_zero": tensor_fundamental.subs(z, 0) == sp.eye(2),
    "tensor_coupling_connection_at_one": (
        sp.simplify(tensor_fundamental.subs(z, 1))
        == tensor_connection_expected
    ),
    "gauge_fundamental_system": matrix_is_zero(
        gauged_fundamental.diff(z) - gauged_matrix * gauged_fundamental
    ),
    "gauge_fundamental_at_zero": (
        gauged_fundamental.subs(z, 0) == sp.eye(3)
    ),
    "gauge_connection_formula": (
        gauged_connection == sp.simplify(P.subs(z, 1) * connection)
    ),
    "gauge_recovers_original_connection": (
        recovered_connection == connection
    ),
    "target_hyperplane_value_at_connection": (
        sp.simplify(target_polynomial.subs({x: sp.E, y: -sp.pi}))
        == sp.E + sp.pi - sigma
    ),
    "translated_target_residual": (
        sp.simplify(translated_residual_on_target - (x * (a - 1) - b))
        == 0
    ),
}

assert all(checks.values())

result = {
    "certificate": "explicit_mixed_pair_tensor_gauge_no_go",
    "sympy_version": sp.__version__,
    "checks": checks,
    "exact_data": {
        "standard_group_element": str(group_xy),
        "standard_group_law_product": str(group_product_expected),
        "standard_fundamental": str(Phi),
        "standard_connection_at_one": str(connection),
        "wedge2_fundamental": str(wedge2_Phi),
        "wedge2_connection_at_one": str(
            sp.simplify(wedge2_Phi.subs(z, 1))
        ),
        "wedge3_fundamental": str(sp.simplify(Phi.det())),
        "tensor_coupling_matrix": str(tensor_matrix),
        "tensor_coupling_fundamental": str(tensor_fundamental),
        "tensor_coupling_connection_at_one": str(
            sp.simplify(tensor_fundamental.subs(z, 1))
        ),
        "rational_gauge": str(P),
        "gauged_matrix": str(gauged_matrix),
        "gauged_connection_at_one": str(gauged_connection),
        "recovered_connection": str(recovered_connection),
        "target_polynomial": str(target_polynomial),
        "right_translated_target": str(right_translated_target),
        "right_translated_residual_on_target": str(
            translated_residual_on_target
        ),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
