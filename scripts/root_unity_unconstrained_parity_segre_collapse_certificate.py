#!/usr/bin/env python3
"""Exact finite replay for unconstrained parity-Segre collapse.

The companion source proves the reflection and Segre statements for all
parameters.  This script performs exact rational computations for m=2 and
n=4,6,8, and it checks the two explicit degree-four components used in the
finite structural audit.  Floating-point evaluations at i*pi are clearly
labelled diagnostics and are not used in any algebraic assertion.
"""

from __future__ import annotations

import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_unconstrained_parity_segre_collapse_certificate.json"
)
X, Z = sp.symbols("X z")
x = sp.symbols("x")


def convolve(
    left: list[sp.Rational], right: list[sp.Rational]
) -> list[sp.Rational]:
    out = [sp.Rational(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    """Taylor moments of 1/(1+exp(z))."""
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def functional(
    coefficients: list[sp.Rational], moments: list[sp.Rational]
) -> sp.Rational:
    return sum(a * moments[k] for k, a in enumerate(coefficients))


def polynomial_coefficients(expr: sp.Expr) -> list[sp.Rational]:
    poly = sp.Poly(sp.expand(expr), X, domain=sp.QQ)
    if poly.is_zero:
        return [sp.Rational(0)]
    return [poly.nth(k) for k in range(poly.degree() + 1)]


def hermite_cardinal_polynomials(m: int, n: int) -> tuple[sp.Expr, ...]:
    """Return Lambda_b with Lambda_b^(a)(j)=(-1)^j delta_(a,b)."""
    M = m * (n + 1)
    interpolation = sp.zeros(M, M)
    targets = sp.zeros(M, n + 1)
    row = 0
    for j in range(m):
        for a in range(n + 1):
            for k in range(a, M):
                interpolation[row, k] = (
                    sp.factorial(k) / sp.factorial(k - a) * j ** (k - a)
                )
            targets[row, a] = (-1) ** j
            row += 1
    coefficients = interpolation.inv() * targets
    return tuple(
        sp.expand(sum(coefficients[k, b] * X**k for k in range(M)))
        for b in range(n + 1)
    )


def beta_matrix(m: int, n: int) -> sp.Matrix:
    moments = logistic_moments(m * (n + 1) + n + 5)
    lambdas = hermite_cardinal_polynomials(m, n)
    return sp.Matrix(
        [
            [
                -functional(
                    polynomial_coefficients(sp.diff(lam, X, a)), moments
                )
                for a in range(n + 1)
            ]
            for lam in lambdas
        ]
    )


@lru_cache(maxsize=None)
def operator_data(m: int, n: int) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return E, A=d/dz-E-m/2, and its two parity blocks P,Q."""
    E = beta_matrix(m, n)
    derivative = sp.zeros(n + 1)
    for a in range(1, n + 1):
        derivative[a - 1, a] = a
    A = derivative - E - sp.Rational(m, 2) * sp.eye(n + 1)
    even = list(range(0, n + 1, 2))
    odd = list(range(1, n + 1, 2))
    P = A.extract(even, odd)
    Q = A.extract(odd, even)
    return E, A, P, Q


def apply_matrix_to_x_polynomial(matrix: sp.Matrix, poly: sp.Expr) -> sp.Expr:
    source = sp.Poly(poly, x, domain=sp.EX)
    return sp.expand(
        sum(
            matrix[i, j] * source.nth(j) * x**i
            for i in range(matrix.rows)
            for j in range(matrix.cols)
        )
    )


def corrected_x_polynomial(
    P: sp.Matrix, Q: sp.Matrix, U: sp.Expr, V: sp.Expr
) -> sp.Poly:
    """Delta(z), written in x=z^2, for C=zU(x), D=V(x)."""
    PU = apply_matrix_to_x_polynomial(P, U)
    QV = apply_matrix_to_x_polynomial(Q, V)
    return sp.Poly(sp.expand(x * U * QV - V * PU), x, domain=sp.EX)


def primitive_integer_vector(values: list[sp.Rational]) -> list[int]:
    values = [sp.Rational(value) for value in values]
    assert any(values)
    denominator = math.lcm(*(int(sp.denom(value)) for value in values))
    integers = [int(value * denominator) for value in values]
    content = math.gcd(*(abs(value) for value in integers))
    integers = [value // content for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return integers


def primitive_poly(poly: sp.Poly) -> sp.Poly:
    rational = sp.Poly(poly.as_expr(), *poly.gens, domain=sp.QQ)
    _, integer = rational.clear_denoms(convert=True)
    _, primitive = integer.primitive()
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


def term_digest(poly: sp.Poly) -> str:
    """Hash the canonical ordered list (monomial, integer coefficient)."""
    primitive = primitive_poly(poly)
    data = [([*monomial], int(coefficient)) for monomial, coefficient in primitive.terms()]
    encoded = json.dumps(data, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def is_unit_basis(basis: sp.GroebnerBasis) -> bool:
    return len(basis.polys) == 1 and basis.polys[0].as_expr() == 1


def triangular_field_eliminant(
    basis: sp.GroebnerBasis, variables: tuple[sp.Symbol, ...]
) -> sp.Poly:
    """Verify Q[variables]/I = Q[t]/(p(t)) from the lex basis."""
    assert len(basis.polys) == len(variables)
    last = variables[-1]
    univariate = [
        poly
        for poly in basis.polys
        if poly.as_expr().free_symbols <= {last}
    ]
    assert len(univariate) == 1
    eliminant = primitive_poly(
        sp.Poly(univariate[0].as_expr(), last, domain=sp.QQ)
    )
    for variable in variables[:-1]:
        candidates = [
            poly.as_expr()
            for poly in basis.polys
            if variable in poly.as_expr().free_symbols
            and poly.as_expr().free_symbols <= {variable, last}
            and sp.degree(poly.as_expr(), variable) == 1
        ]
        assert len(candidates) == 1
        coefficient = sp.Poly(candidates[0], variable).coeff_monomial(variable)
        assert coefficient in (sp.Integer(1), sp.Integer(-1))
        assert not coefficient.has(last)
    return eliminant


EXPECTED_CHARTS = {
    4: {(1, 1): (2, 17, [6, 5, 10]), (1, 2): (1, 3, [1, 2])},
    6: {
        (2, 2): (6, 13, [3, 9, 5, 3, 10, 10, 8]),
        (2, 3): (4, 13, [9, 2, 9, 2, 10]),
    },
    8: {
        (
            3,
            3,
        ): (
            20,
            67,
            [33, 36, 54, 43, 63, 45, 45, 27, 53, 46, 66, 13, 30, 28, 36, 9, 22, 50, 45, 25, 3],
        ),
        (
            3,
            4,
        ): (15, 17, [4, 8, 6, 4, 7, 4, 15, 8, 10, 10, 15, 10, 11, 0, 7, 5]),
    },
}

EXPECTED_N8_DIGESTS = {
    (3, 3): "189c82406a54b253dc23453b0ff0d0f00234247931c89bf3f49d72ad3bedbbb5",
    (3, 4): "d2a08748916f53a0f15cc766b17d44f281e400746c4343334453cc728c47bc37",
}


def maximal_degree_two_chart_audit(n: int) -> dict:
    _, _, P, Q = operator_data(2, n)
    d = n // 2
    nonempty: dict[tuple[int, int], dict] = {}
    empty: list[list[int]] = []
    for degree_U in range(d):
        for degree_V in range(d + 1):
            uvars = sp.symbols(f"u0:{degree_U}")
            vvars = sp.symbols(f"v0:{degree_V}")
            variables = tuple(uvars) + tuple(vvars)
            U = sum(uvars[j] * x**j for j in range(degree_U)) + x**degree_U
            V = sum(vvars[j] * x**j for j in range(degree_V)) + x**degree_V
            delta = corrected_x_polynomial(P, Q, U, V)
            equations = [delta.nth(k) for k in range(2, 2 * d + 1)]
            if not variables:
                assert any(equations)
                empty.append([degree_U, degree_V])
                continue
            grevlex = sp.groebner(
                equations, *variables, order="grevlex", domain=sp.QQ
            )
            if is_unit_basis(grevlex):
                empty.append([degree_U, degree_V])
                continue
            assert grevlex.is_zero_dimensional
            lex = grevlex.fglm(order="lex")
            eliminant = triangular_field_eliminant(lex, variables)
            expected_degree, prime, expected_mod_coefficients = EXPECTED_CHARTS[n][
                (degree_U, degree_V)
            ]
            assert eliminant.degree() == expected_degree
            assert int(eliminant.LC()) % prime != 0
            reduction = sp.Poly(eliminant.as_expr(), variables[-1], modulus=prime)
            assert reduction.degree() == eliminant.degree()
            assert reduction.is_irreducible
            coefficients_mod_prime = [
                int(eliminant.nth(k)) % prime
                for k in range(eliminant.degree(), -1, -1)
            ]
            assert coefficients_mod_prime == expected_mod_coefficients
            if n == 8:
                assert term_digest(eliminant) == EXPECTED_N8_DIGESTS[
                    (degree_U, degree_V)
                ]
            record = {
                "chart_highest_degrees_U_V": [degree_U, degree_V],
                "triangular_lex_quotient": True,
                "closed_point_degree": eliminant.degree(),
                "eliminant_sha256": term_digest(eliminant),
                "irreducible_reduction_prime": prime,
                "irreducible_reduction_coefficients_descending": coefficients_mod_prime,
                "rational_point": eliminant.degree() == 1,
            }
            if n <= 6:
                record["primitive_eliminant_coefficients_descending"] = [
                    int(eliminant.nth(k))
                    for k in range(eliminant.degree(), -1, -1)
                ]
            nonempty[degree_U, degree_V] = record

    assert set(nonempty) == set(EXPECTED_CHARTS[n])
    degrees = sorted(record["closed_point_degree"] for record in nonempty.values())
    segre_degree = math.comb(n - 1, n // 2 - 1)
    assert sum(degrees) == segre_degree
    assert len(empty) + len(nonempty) == d * (d + 1)
    return {
        "n": n,
        "m": 2,
        "chart_count": d * (d + 1),
        "empty_chart_count": len(empty),
        "nonempty_chart_count": len(nonempty),
        "nonempty_charts": [nonempty[key] for key in sorted(nonempty)],
        "closed_point_degrees": degrees,
        "proper_reduced_section": True,
        "scheme_degree": sum(degrees),
        "segre_degree": segre_degree,
        "has_rational_pair": any(
            record["rational_point"] for record in nonempty.values()
        ),
    }


def tail_matrix(P: sp.Matrix, Q: sp.Matrix, U: sp.Expr, start: int) -> sp.Matrix:
    d = P.rows - 1
    return sp.Matrix(
        2 * d - start + 1,
        d + 1,
        lambda row, column: corrected_x_polynomial(
            P, Q, U, x**column
        ).nth(start + row),
    )


def cofactor_kernel(matrix: sp.Matrix) -> sp.Matrix:
    assert matrix.rows + 1 == matrix.cols
    return sp.Matrix(
        [
            (-1) ** j
            * matrix[:, [k for k in range(matrix.cols) if k != j]].det()
            for j in range(matrix.cols)
        ]
    )


def primitive_output(
    P: sp.Matrix, Q: sp.Matrix, U_coefficients: list[int], V_coefficients: list[int]
) -> tuple[list[int], sp.Rational]:
    U = sum(value * x**j for j, value in enumerate(U_coefficients))
    V = sum(value * x**j for j, value in enumerate(V_coefficients))
    delta = corrected_x_polynomial(P, Q, U, V)
    values = [sp.Rational(delta.nth(j)) for j in range(2 * (P.rows - 1) + 1)]
    primitive = primitive_integer_vector(values)
    first = next(j for j, value in enumerate(primitive) if value)
    scale = sp.cancel(values[first] / primitive[first])
    assert all(value == scale * target for value, target in zip(values, primitive))
    return primitive, scale


def projective_cone_tail_jacobian_rank(
    P: sp.Matrix,
    Q: sp.Matrix,
    U_coefficients: list[int],
    V_coefficients: list[int],
    start: int,
) -> int:
    """Rank before quotienting the two independent projective scalings."""
    uvars = sp.symbols(f"jac_u0:{len(U_coefficients)}")
    vvars = sp.symbols(f"jac_v0:{len(V_coefficients)}")
    U = sum(uvars[j] * x**j for j in range(len(U_coefficients)))
    V = sum(vvars[j] * x**j for j in range(len(V_coefficients)))
    delta = corrected_x_polynomial(P, Q, U, V)
    equations = [delta.nth(k) for k in range(start, 2 * (P.rows - 1) + 1)]
    jacobian = sp.Matrix(
        [
            [sp.diff(equation, variable) for variable in (*uvars, *vvars)]
            for equation in equations
        ]
    )
    substitution = dict(
        zip((*uvars, *vvars), U_coefficients + V_coefficients)
    )
    return jacobian.subs(substitution).rank()


def value_diagnostic(even_coefficients: list[int]) -> dict:
    mp.mp.dps = 120
    value = abs(
        mp.fsum(
            mp.mpf(coefficient) * (-mp.pi**2) ** j
            for j, coefficient in enumerate(even_coefficients)
        )
    )
    height = max(abs(coefficient) for coefficient in even_coefficients)
    relative = value / height
    theta = -mp.log(relative) / mp.log(height)
    return {
        "height": height,
        "absolute_value_at_i_pi": mp.nstr(value, 55),
        "relative_value_over_height": mp.nstr(relative, 45),
        "relative_small_value_exponent_theta": mp.nstr(theta, 40),
        "absolute_value_exceeds_one": bool(value > 1),
        "diagnostic_only": True,
    }


def degree_four_n6_audit() -> dict:
    _, _, P, Q = operator_data(2, 6)
    c0, c1, c2 = sp.symbols("c0 c1 c2")
    U = c0 + c1 * x + c2 * x**2
    H = tail_matrix(P, Q, U, 3)
    determinant = sp.factor(H.det())
    linear = 590 * c0 - 5823 * c1 + 57465 * c2
    cubic = (
        7205321900 * c0**3
        - 3108229108110 * c0**2 * c1
        + 2198940343306875 * c0**2 * c2
        + 59247653649156 * c0 * c1**2
        - 43968648471037830 * c0 * c1 * c2
        + 428131795997165400 * c0 * c2**2
        - 288908249720832 * c1**3
        + 219756314527540290 * c1**2 * c2
        - 4252894345690332750 * c1 * c2**2
        + 20845875463468743825 * c2**3
    )
    assert sp.cancel(determinant - linear * cubic / 65610000) == 0
    assert term_digest(sp.Poly(cubic, c0, c1, c2)) == (
        "5490996be5c6c76040041bc4f64ff8e2cf9289ed1e70fe90c73f8b9de9ed1812"
    )

    s, t = sp.symbols("s t")
    substitution = {
        c0: 5823 * t - 57465 * s,
        c1: 590 * t,
        c2: 590 * s,
    }
    H_line = sp.simplify(H.subs(substitution))
    assert H_line[-1, :] == sp.zeros(1, 4)
    V_line = cofactor_kernel(H_line[:3, :])
    assert any(entry != 0 for entry in V_line)
    assert all(sp.cancel(entry) == 0 for entry in H_line * V_line)
    regular_U = primitive_integer_vector([-57465, 0, 590])
    regular_V = primitive_integer_vector(
        [entry.subs({s: 1, t: 0}) for entry in V_line]
    )
    regular_jacobian_rank = projective_cone_tail_jacobian_rank(
        P, Q, regular_U, regular_V, 3
    )
    assert regular_jacobian_rank == 4

    U_point = [5823, 590, 0]
    V_point = [38680872000, 14869741311, 1109528630, 0]
    assert math.gcd(*(abs(value) for value in U_point)) == 1
    assert math.gcd(*(abs(value) for value in V_point)) == 1
    primitive_delta, scale = primitive_output(P, Q, U_point, V_point)
    expected_delta = [683258923008000, 138458274343783, 7014432262780]
    assert primitive_delta[:3] == expected_delta
    assert not any(primitive_delta[3:])
    assert scale == -9

    # Bounded arithmetic diagnostic on the affine line c0=1,
    # c1=(590+57465*b)/5823, c2=b.
    b = sp.symbols("b")
    U_affine = (
        1 + (590 + 57465 * b) / sp.Integer(5823) * x + b * x**2
    )
    H_affine = tail_matrix(P, Q, U_affine, 3)
    V_affine = cofactor_kernel(H_affine[:3, :])
    delta_affine = corrected_x_polynomial(
        P,
        Q,
        U_affine,
        sum(V_affine[j] * x**j for j in range(4)),
    )
    low_affine = [sp.cancel(delta_affine.nth(j)) for j in range(3)]
    assert all(sp.degree(value, b) <= 4 for value in low_affine)
    best_absolute = None
    best_theta = None
    scan_count = 0
    for denominator in range(1, 31):
        for numerator in range(-30, 31):
            if math.gcd(abs(numerator), denominator) != 1:
                continue
            scan_count += 1
            rational_values = [
                sp.cancel(value.subs(b, sp.Rational(numerator, denominator)))
                for value in low_affine
            ]
            coefficients = primitive_integer_vector(rational_values)
            diagnostic = value_diagnostic(coefficients)
            absolute = mp.mpf(diagnostic["absolute_value_at_i_pi"])
            theta = mp.mpf(diagnostic["relative_small_value_exponent_theta"])
            row = {
                "parameter_numerator": numerator,
                "parameter_denominator": denominator,
                "primitive_delta_even_coefficients": coefficients,
                **diagnostic,
            }
            if best_absolute is None or absolute < best_absolute[0]:
                best_absolute = (absolute, row)
            if best_theta is None or theta > best_theta[0]:
                best_theta = (theta, row)
    assert scan_count == 1111
    assert best_absolute is not None and best_theta is not None
    assert best_absolute[1]["parameter_numerator"] == 0
    assert best_absolute[1]["parameter_denominator"] == 1
    assert best_theta[1]["parameter_numerator"] == 0
    assert best_theta[1]["parameter_denominator"] == 1

    return {
        "m": 2,
        "n": 6,
        "target_degree": 4,
        "tail_matrix_shape": list(H.shape),
        "determinant_factorization_denominator": 65610000,
        "linear_factor_coefficients_c0_c1_c2": [590, -5823, 57465],
        "cubic_factor_sha256": term_digest(sp.Poly(cubic, c0, c1, c2)),
        "rational_line_parameterization_c0_c1_c2": [
            "5823*t-57465*s",
            "590*t",
            "590*s",
        ],
        "cofactor_kernel_identity": True,
        "regular_line_point_tail_jacobian_rank": regular_jacobian_rank,
        "displayed_point": {
            "C_odd_coefficients_z_z3_z5": U_point,
            "D_even_coefficients_1_z2_z4_z6": V_point,
            "corrected_output_scale_times_primitive": str(scale),
            "primitive_delta_even_coefficients_1_z2_z4": expected_delta,
            "diagnostic": value_diagnostic(expected_delta),
        },
        "bounded_affine_parameter_scan": {
            "range": "gcd(|p|,q)=1, |p|<=30, 1<=q<=30",
            "sample_count": scan_count,
            "best_absolute_value": best_absolute[1],
            "best_theta": best_theta[1],
            "finite_diagnostic_only": True,
        },
    }


EXPECTED_QUINTIC_MOD_11 = [
    ([5, 0, 0], 1),
    ([4, 1, 0], 1),
    ([4, 0, 1], 7),
    ([3, 2, 0], 9),
    ([3, 0, 2], 8),
    ([2, 3, 0], 6),
    ([2, 2, 1], 3),
    ([2, 1, 2], 8),
    ([2, 0, 3], 2),
    ([1, 4, 0], 3),
    ([1, 3, 1], 4),
    ([1, 2, 2], 1),
    ([1, 1, 3], 5),
    ([1, 0, 4], 6),
    ([0, 5, 0], 4),
    ([0, 4, 1], 9),
    ([0, 2, 3], 9),
    ([0, 1, 4], 2),
    ([0, 0, 5], 10),
]


def degree_four_n8_audit() -> dict:
    _, _, P, Q = operator_data(2, 8)
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3")
    U = c0 + c1 * x + c2 * x**2 + c3 * x**3
    H = tail_matrix(P, Q, U, 3)
    linear = (
        42271 * c0 - 417198 * c1 + 4117575 * c2 - 40638465 * c3
    ) / 315
    assert H[-1, :] == sp.Matrix([[0, 0, 0, 0, -linear]])
    c0_solution = sp.solve(linear, c0)[0]
    assert c0_solution == (
        417198 * c1 - 4117575 * c2 + 40638465 * c3
    ) / 42271
    H5 = sp.simplify(H[:5, :].subs(c0, c0_solution))
    quintic = primitive_poly(sp.Poly(H5.det(), c1, c2, c3, domain=sp.QQ))
    assert quintic.total_degree() == 5
    assert len(quintic.terms()) == 21
    assert term_digest(quintic) == (
        "c4ec249109d6978875808dcdfc162aa1252dc15921fa44157cc8bab6a6f51f9c"
    )

    mod_terms = [
        ([*monomial], int(coefficient) % 11)
        for monomial, coefficient in quintic.terms()
        if int(coefficient) % 11
    ]
    assert mod_terms == EXPECTED_QUINTIC_MOD_11

    f = quintic.as_expr()
    gradient = [sp.diff(f, variable) for variable in (c1, c2, c3)]
    patch_c3 = sp.groebner(
        [value.subs(c3, 1) for value in gradient], c1, c2, modulus=11
    )
    patch_c3_zero_c2 = sp.groebner(
        [value.subs({c3: 0, c2: 1}) for value in gradient],
        c1,
        modulus=11,
    )
    remaining_gradient = [
        int(value.subs({c1: 1, c2: 0, c3: 0})) % 11
        for value in gradient
    ]
    assert is_unit_basis(patch_c3)
    assert is_unit_basis(patch_c3_zero_c2)
    assert remaining_gradient == [5, 1, 7]

    point = {c1: 1450665, c2: 14881, c3: 0}
    point_c0 = sp.cancel(c0_solution.subs(point))
    assert point_c0 == 12867945
    assert quintic.as_expr().subs(point) == 0
    H_point = H.subs({c0: point_c0, **point})
    assert H_point.rank() == 4
    kernel = H_point.nullspace()
    assert len(kernel) == 1
    V_point = primitive_integer_vector(list(kernel[0]))
    expected_V = [
        504574901556626789015258880,
        598191925197439504473212224125,
        68370439687845675316908865023,
        797647048410487887961952688,
        1091837679098938109485676,
    ]
    assert V_point == expected_V
    U_point = [12867945, 1450665, 14881, 0]
    primitive_delta, scale = primitive_output(P, Q, U_point, V_point)
    expected_delta = [
        380509576250859788241707901911040,
        77106572277272551446181984162605,
        3906224612207931823717824632944,
    ]
    assert primitive_delta[:3] == expected_delta
    assert not any(primitive_delta[3:])
    assert scale == -135
    tail_jacobian_rank = projective_cone_tail_jacobian_rank(
        P, Q, U_point, V_point, 3
    )
    assert tail_jacobian_rank == 6

    return {
        "m": 2,
        "n": 8,
        "target_degree": 4,
        "tail_matrix_shape": list(H.shape),
        "last_row_linear_factor_numerator_coefficients_c0_c1_c2_c3": [
            42271,
            -417198,
            4117575,
            -40638465,
        ],
        "last_row_linear_factor_denominator": 315,
        "plane_quintic": {
            "primitive_term_count": len(quintic.terms()),
            "sha256": term_digest(quintic),
            "modulus": 11,
            "nonzero_terms_mod_11": mod_terms,
            "gradient_patch_c3_equals_1_unit_ideal": True,
            "gradient_patch_c3_0_c2_1_unit_ideal": True,
            "gradient_at_1_0_0_mod_11": remaining_gradient,
            "smooth_mod_11": True,
            "geometrically_irreducible_over_Q": True,
            "geometric_genus": 6,
            "not_rationally_parametrizable": True,
        },
        "rational_point": {
            "quintic_projective_coordinates_c1_c2_c3": [1450665, 14881, 0],
            "recovered_c0": int(point_c0),
            "tail_matrix_rank": H_point.rank(),
            "projective_cone_tail_jacobian_rank": tail_jacobian_rank,
            "C_odd_coefficients_z_z3_z5_z7": U_point,
            "D_even_coefficients_1_z2_z4_z6_z8": V_point,
            "corrected_output_scale_times_primitive": str(scale),
            "primitive_delta_even_coefficients_1_z2_z4": expected_delta,
            "diagnostic": value_diagnostic(expected_delta),
        },
    }


def displayed_n4_audit() -> dict:
    _, _, P, Q = operator_data(2, 4)
    U = [69, 7]
    V = [3024, -73219, -7504]
    primitive_delta, scale = primitive_output(P, Q, U, V)
    expected = [387072, 39205]
    assert primitive_delta[:2] == expected
    assert not any(primitive_delta[2:])
    assert scale == -3
    return {
        "C_odd_coefficients_z_z3": U,
        "D_even_coefficients_1_z2_z4": V,
        "corrected_output_scale_times_primitive": str(scale),
        "primitive_delta_even_coefficients_1_z2": expected,
        "diagnostic": value_diagnostic(expected),
    }


def reflection_grid() -> dict:
    checked = []
    for m in range(1, 4):
        for n in range(1, 7):
            E, A, _, _ = operator_data(m, n)
            J = sp.diag(*[(-1) ** a for a in range(n + 1)])
            assert J * E * J == -E - m * sp.eye(n + 1)
            assert J * A * J == -A
            checked.append([m, n])
    return {
        "tuples": checked,
        "tuple_count": len(checked),
        "beta_matrix_identity": "J*E*J=-E-m*I",
        "gauged_operator_identity": "J*A*J=-A",
        "finite_check_only_the_source_contains_the_all_parameter_proof": True,
    }


def main() -> None:
    degree_two = [maximal_degree_two_chart_audit(n) for n in (4, 6, 8)]
    assert [row["closed_point_degrees"] for row in degree_two] == [
        [1, 2],
        [4, 6],
        [15, 20],
    ]
    assert [row["has_rational_pair"] for row in degree_two] == [True, False, False]

    segre_rows = []
    for n in (4, 6, 8):
        d = n // 2
        dimension = n - 1
        degree = math.comb(n - 1, d - 1)
        killed_for_degree_two = n - 1
        killed_for_degree_four = n - 2
        assert killed_for_degree_two == dimension
        segre_rows.append(
            {
                "n": n,
                "Segre_factors": [f"P^{d - 1}", f"P^{d}"],
                "dimension": dimension,
                "degree": degree,
                "degree_two_tail_hyperplanes": killed_for_degree_two,
                "degree_four_tail_hyperplanes": killed_for_degree_four,
                "degree_four_dimension_lower_bound": 1,
            }
        )

    payload = {
        "schema": "root-unity-unconstrained-parity-segre-collapse-v1",
        "scope": {
            "all_parameter_theorems_in_source": [
                "reflection identity and parity reversal",
                "bilinear parity formula for corrected Delta",
                "Segre dimension, degree, and projective dimension lower bound",
            ],
            "exact_finite_algebra": "m=2, n=4,6,8",
            "no_transcendence_or_irrationality_conclusion": True,
        },
        "reflection_exact_grid": reflection_grid(),
        "segre_geometry": segre_rows,
        "maximal_degree_two_sections": degree_two,
        "displayed_n4_rational_pair": displayed_n4_audit(),
        "degree_four_components": {
            "n6_rational_line": degree_four_n6_audit(),
            "n8_smooth_genus_six_component": degree_four_n8_audit(),
        },
        "limitations": {
            "no_all_even_n_rational_pair_theorem": True,
            "no_asymptotic_rational_curve_or_descent_theorem": True,
            "no_primitive_content_or_height_gain_theorem": True,
            "continuous_or_bounded_optimization_is_not_arithmetic_evidence": True,
            "nonzero_corrected_polynomial_does_not_imply_small_value": True,
        },
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUT),
                "degree_two_closed_point_degrees": [
                    row["closed_point_degrees"] for row in degree_two
                ],
                "degree_two_rational_pair_flags": [
                    row["has_rational_pair"] for row in degree_two
                ],
                "n8_quintic_genus": payload["degree_four_components"][
                    "n8_smooth_genus_six_component"
                ]["plane_quintic"]["geometric_genus"],
                "all_assertions_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
