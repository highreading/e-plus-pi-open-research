#!/usr/bin/env python3
"""Exact replay for the corrected low border when m is even.

All calculations use SymPy QQ arithmetic.  The all-parameter input is the
positive pole-truncation theorem proved in the companion source; this script
replays its concrete cardinal/Newton consequences on a finite grid.  It also
checks the corrected bordered determinants directly and records the exact
two-even endpoint coefficient and the odd-m central-jet obstruction.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_corrected_low_border_even_m_certificate.json"
X, U, x = sp.symbols("X U x")


def convolve(a: list[sp.Rational], b: list[sp.Rational]) -> list[sp.Rational]:
    out = [sp.Rational(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def phi_coefficients(m: int, n: int) -> list[sp.Rational]:
    out = [sp.Rational(1)]
    for j in range(m):
        for _ in range(n + 1):
            out = convolve(out, [-sp.Integer(j), sp.Integer(1)])
    return out


def polynomial_crt_cardinal(m: int, n: int, b: int) -> sp.Poly:
    """Lambda_b^(a)(j)=(-1)^j delta_(a,b), over QQ."""
    h = n + 1
    moduli = [sp.Poly((X - j) ** h, X, domain=sp.QQ) for j in range(m)]
    total = sp.Poly(sp.prod(mod.as_expr() for mod in moduli), X, domain=sp.QQ)
    answer = sp.Poly(0, X, domain=sp.QQ)
    for j, modulus in enumerate(moduli):
        cofactor = sp.div(total, modulus)[0]
        inverse = sp.invert(cofactor, modulus)
        target = sp.Poly(
            sp.Rational((-1) ** j, math.factorial(b)) * (X - j) ** b,
            X,
            domain=sp.QQ,
        )
        answer += target * cofactor * inverse
    return answer.rem(total)


def assert_cardinal(poly: sp.Poly, m: int, n: int, b: int) -> None:
    for j in range(m):
        for a in range(n + 1):
            expected = sp.Integer((-1) ** j) if a == b else sp.Integer(0)
            assert sp.diff(poly.as_expr(), X, a).subs(X, j) == expected


def odd_center_transform(poly: sp.Poly, center: sp.Rational) -> sp.Poly:
    """For P(c+U)=U N(-U^2), return N(x)."""
    centered = sp.Poly(sp.expand(poly.as_expr().subs(X, center + U)), U)
    assert all(power[0] % 2 == 1 for power, value in centered.terms() if value)
    return sp.Poly(
        sum(
            value * (-x) ** ((power[0] - 1) // 2)
            for power, value in centered.terms()
        ),
        x,
        domain=sp.QQ,
    )


def repeated_half_square_rates(k: int, h: int) -> list[sp.Rational]:
    return [
        sp.Rational((2 * r - 1) ** 2, 4)
        for r in range(1, k + 1)
        for _ in range(h)
    ]


def newton_coefficients(poly: sp.Poly, rates: list[sp.Rational]) -> list[sp.Rational]:
    assert poly.degree() < len(rates)
    basis = [sp.Integer(1)]
    for rate in rates[:-1]:
        basis.append(sp.expand(basis[-1] * (x + rate)))
    remainder = poly.as_expr()
    coefficients = [sp.Rational(0)] * len(rates)
    for d in range(len(rates) - 1, -1, -1):
        coefficient = sp.Poly(remainder, x, domain=sp.QQ).nth(d)
        coefficients[d] = coefficient
        remainder = sp.expand(remainder - coefficient * basis[d])
    assert remainder == 0
    return coefficients


def reconstruct_newton(
    coefficients: list[sp.Rational], rates: list[sp.Rational]
) -> sp.Poly:
    prefix = sp.Integer(1)
    answer = sp.Integer(0)
    for d, coefficient in enumerate(coefficients):
        answer += coefficient * prefix
        if d < len(rates) - 1:
            prefix = sp.expand(prefix * (x + rates[d]))
    return sp.Poly(answer, x, domain=sp.QQ)


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def functional(poly: sp.Expr, moments: list[sp.Rational]) -> sp.Rational:
    expanded = sp.Poly(sp.expand(poly), X, domain=sp.QQ)
    if expanded.is_zero:
        return sp.Rational(0)
    return sum(expanded.nth(k) * moments[k] for k in range(expanded.degree() + 1))


def centered_endpoint_matrix(
    m: int, n: int, degree: int, moments: list[sp.Rational]
) -> sp.Matrix:
    center = sp.Rational(m - 1, 2)
    phi = sum(c * X**j for j, c in enumerate(phi_coefficients(m, n)))
    return sp.Matrix(
        [
            [
                functional(sp.diff((X - center) ** q * phi, X, a), moments)
                for a in range(degree + 1)
            ]
            for q in range(degree - 1)
        ]
    )


def beta_row(
    cardinal: sp.Poly, degree: int, moments: list[sp.Rational]
) -> sp.Matrix:
    return sp.Matrix(
        [[
            -functional(sp.diff(cardinal.as_expr(), X, a), moments)
            for a in range(degree + 1)
        ]]
    )


def bordered(matrix: sp.Matrix, second: sp.Matrix, degree: int) -> sp.Rational:
    e0 = sp.zeros(1, degree + 1)
    e0[0, 0] = 1
    return sp.factor(matrix.col_join(e0).col_join(second).det())


def rational_digest(values: list[sp.Rational]) -> str:
    encoded = ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def check_even_newton_grid() -> tuple[list[dict], str]:
    rows: list[dict] = []
    digest = hashlib.sha256()
    for m in range(2, 11, 2):
        k = m // 2
        sigma = (-1) ** k
        center = sp.Rational(m - 1, 2)
        for n in range(2, 8):
            h = n + 1
            cardinal = polynomial_crt_cardinal(m, n, 0)
            assert_cardinal(cardinal, m, n, 0)
            numerator = odd_center_transform(cardinal, center)
            rates = repeated_half_square_rates(k, h)
            coefficients = newton_coefficients(numerator, rates)
            assert coefficients[0] == 2 * sigma
            assert all(sigma * value > 0 for value in coefficients)

            modified = sp.Poly(numerator.as_expr() + 2, x, domain=sp.QQ)
            modified_coefficients = coefficients[:]
            modified_coefficients[0] += 2
            assert reconstruct_newton(modified_coefficients, rates) == modified
            assert sigma * modified_coefficients[0] == (4 if sigma == 1 else 0)
            assert all(sigma * value > 0 for value in modified_coefficients[1:])
            assert any(value != 0 for value in modified_coefficients)

            row = {
                "m": m,
                "n": n,
                "h": h,
                "sigma": sigma,
                "raw_gamma_0": str(coefficients[0]),
                "modified_gamma_0": str(modified_coefficients[0]),
                "all_raw_coefficients_have_sign_sigma": True,
                "all_modified_coefficients_after_d0_are_strict_with_sign_sigma": True,
                "modified_rational_function_is_nonzero_strictly_completely_monotone_after_sigma": True,
                "modified_newton_sha256": rational_digest(modified_coefficients),
            }
            rows.append(row)
            digest.update(
                f"{m},{n},{sigma},{rational_digest(modified_coefficients)}\n".encode()
            )
    return rows, digest.hexdigest()


def check_direct_borders(moments: list[sp.Rational]) -> list[dict]:
    rows: list[dict] = []
    # A deliberately modest exact grid: the proof is the Newton theorem, not
    # a determinant extrapolation.
    for m in (2, 4):
        for n in range(2, 6):
            cardinal = polynomial_crt_cardinal(m, n, 0)
            for degree in range(2, n + 1):
                matrix = centered_endpoint_matrix(m, n, degree, moments)
                E0 = beta_row(cardinal, degree, moments)
                e1 = sp.zeros(1, degree + 1)
                e1[0, 1] = 1
                corrected = bordered(matrix, e1 - E0, degree)
                assert corrected != 0
                rows.append(
                    {
                        "m": m,
                        "n": n,
                        "D": degree,
                        "corrected_constant_border": str(corrected),
                        "nonzero": True,
                    }
                )
    return rows


def check_dual_polynomials(moments: list[sp.Rational]) -> dict:
    linear = 2 * X + 1
    quadratic = 2 * X**2 + 2 * X + 1
    linear_values = [functional(sp.diff(linear, X, a), moments) for a in range(6)]
    quadratic_values = [
        functional(sp.diff(quadratic, X, a), moments) for a in range(6)
    ]
    assert linear_values == [0, 1, 0, 0, 0, 0]
    assert quadratic_values == [0, 0, 2, 0, 0, 0]
    return {
        "L_derivatives_of_2X_plus_1": [str(v) for v in linear_values],
        "L_derivatives_of_2X2_plus_2X_plus_1": [str(v) for v in quadratic_values],
        "generic_second_row": "e1-E0 = L((Lambda0+2X+1)^(a))",
        "defect_second_row": "2e2-E1 = L((Lambda1+2X^2+2X+1)^(a))",
    }


def check_defect_grid(moments: list[sp.Rational]) -> list[dict]:
    rows: list[dict] = []
    for m in (3, 5):
        for n in (3, 5):
            cardinal = polynomial_crt_cardinal(m, n, 1)
            assert_cardinal(cardinal, m, n, 1)
            for degree in range(2, n + 1, 2):
                matrix = centered_endpoint_matrix(m, n, degree, moments)
                E1 = beta_row(cardinal, degree, moments)
                two_e2 = sp.zeros(1, degree + 1)
                two_e2[0, 2] = 2
                value = bordered(matrix, two_e2 - E1, degree)
                assert value != 0
                rows.append(
                    {
                        "m": m,
                        "n": n,
                        "D": degree,
                        "coefficient_border_2e2_minus_E1": str(value),
                        "nonzero_on_this_finite_grid_only": True,
                    }
                )
    return rows


def odd_boundary_obstruction(moments: list[sp.Rational]) -> dict:
    # The smallest nontrivial member of the remaining family n even, D odd.
    m, n, degree = 3, 4, 3
    h = n + 1
    center = sp.Integer(1)
    sigma = -1
    cardinal = polynomial_crt_cardinal(m, n, 0)
    N = sp.Poly(
        sp.expand(
            (cardinal.as_expr().subs(X, center + U) - sigma) / U ** (h + 1)
        ).subs(U**2, -x),
        x,
        domain=sp.QQ,
    )
    # SymPy substitution above is only used after exact divisibility; replay
    # the identity directly, which is the important assertion.
    assert sp.expand(
        cardinal.as_expr().subs(X, center + U)
        - sigma
        - U ** (h + 1) * N.as_expr().subs(x, -U**2)
    ) == 0
    corrected_centered = sp.expand(
        cardinal.as_expr().subs(X, center + U) - sigma + 2 * U
    )
    assert sp.Poly(corrected_centered, U).nth(1) == 2
    assert sp.rem(
        sp.Poly(corrected_centered, U, domain=sp.QQ),
        sp.Poly(U ** (h + 1), U, domain=sp.QQ),
    ) != 0

    matrix = centered_endpoint_matrix(m, n, degree, moments)
    E0 = beta_row(cardinal, degree, moments)
    e1 = sp.zeros(1, degree + 1)
    e1[0, 1] = 1
    corrected_border = bordered(matrix, e1 - E0, degree)

    power_row = sp.Matrix(
        [[
            functional(sp.diff((X - center) ** (h + 1), X, a), moments)
            for a in range(degree + 1)
        ]]
    )
    coordinate_border = bordered(matrix, e1, degree)
    power_border = bordered(matrix, power_row, degree)
    ratio = sp.factor(coordinate_border / power_border)
    assert ratio == sp.Rational(-3482, 63297)
    assert corrected_border == -sp.Integer(15_976_059_494_400)
    return {
        "tuple": [m, n, degree],
        "centered_corrected_row_exact": "U^(h+1) N(-U^2) + 2U",
        "central_remainder_linear_coefficient": "2",
        "not_divisible_by_U_to_h_plus_1": True,
        "corrected_border": str(corrected_border),
        "coordinate_border_over_U_power_border": str(ratio),
        "logical_obstruction": (
            "The coordinate term is a central boundary jet, not an addition "
            "to the polynomial Newton numerator covered by the positive "
            "pole-truncation theorem."
        ),
    }


def main() -> None:
    moments = logistic_moments(100)
    assert moments[:3] == [sp.Rational(1, 2), sp.Rational(-1, 4), 0]
    newton_rows, digest = check_even_newton_grid()
    direct_rows = check_direct_borders(moments)
    defect_rows = check_defect_grid(moments)
    payload = {
        "schema": "root-unity-corrected-low-border-even-m-v1",
        "exact_arithmetic": "QQ only; no floating-point comparisons",
        "dependency_sha256": {
            "sources/root_unity_gamma_augmented_newton_audit.md": (
                "d22b2cb5a92d4a8c4bebdb1f61a095cbf15e342fb8a19d1a61dfc3a3d87edb47"
            ),
            "sources/root_unity_gamma_positive_pole_truncation_theorem.md": (
                "af3049a869327cc7d1138cea448878c64bebadcf0305a124c5d6f923e7937ba6"
            ),
            "sources/root_unity_gamma_top_cardinal_degree_theorem.md": (
                "63d1b3532150fc7f2e9e2f142e6cd1c797c9ed3c3739a4b3de2d30932c27061c"
            ),
        },
        "even_m_newton_grid": {
            "m_values": [2, 4, 6, 8, 10],
            "n_range": [2, 7],
            "row_count": len(newton_rows),
            "all_raw_gamma0_equal_2sigma": True,
            "all_modified_gamma0_equal_4_or_0": True,
            "all_modified_coefficients_after_d0_strict_with_sign_sigma": True,
            "all_modified_rational_functions_strictly_completely_monotone_after_sigma": True,
            "row_digest_sha256": digest,
            "selected_rows": [
                row for row in newton_rows if (row["m"], row["n"]) in {(2, 2), (4, 5), (10, 7)}
            ],
        },
        "direct_corrected_border_grid": {
            "m_values": [2, 4],
            "n_range": [2, 5],
            "D_rule": "2 <= D <= n",
            "row_count": len(direct_rows),
            "all_nonzero": True,
            "rows": direct_rows,
        },
        "dual_polynomial_identities": check_dual_polynomials(moments),
        "defect_coefficient_finite_replay": {
            "identity": "[z]Delta is the border e0 wedge (2e2-E1)",
            "scope": "The identity is algebraic for all parameters; nonvanishing below is finite replay only.",
            "rows": defect_rows,
        },
        "odd_m_central_boundary_obstruction": odd_boundary_obstruction(moments),
        "logical_scope": {
            "all_parameter_theorem": (
                "Using the independently proved positive pole-truncation theorem "
                "and shifted-coordinate theorem, the corrected constant border "
                "is nonzero for every even m>=2 and n>=D>=2; hence Delta is nonzero."
            ),
            "combination_with_top_degree_theorem": (
                "Together with the top-cardinal degree theorem, only m>=3 odd, "
                "n even, D odd remains outside the proved universal Delta-nonzero "
                "regimes for m>=2."
            ),
            "not_claimed": (
                "The finite defect replay is not an all-parameter defect-border "
                "proof, and the odd-m central-boundary family is not resolved here."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["even_m_newton_grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["direct_corrected_border_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
