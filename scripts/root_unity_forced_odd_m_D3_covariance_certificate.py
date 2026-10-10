#!/usr/bin/env python3
"""Exact replay for the hard odd-frequency D=3 covariance theorem.

The companion source proves the all-parameter result.  This checker verifies
the determinant algebra symbolically and reconstructs the rational functions,
Laurent coefficients, and Bernoulli-moment borders on a finite exact grid.
The grid is a replay, not the basis for the universal claim.
"""

from __future__ import annotations

import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_forced_odd_m_D3_covariance_certificate.json"
x, y, U, t = sp.symbols("x y U t")


def derivative_polynomial(order: int) -> sp.Poly:
    """H_order with D^order(csch u)=csch(u) H_order(coth u)."""
    value = sp.Integer(1)
    for _ in range(order):
        value = sp.expand((1 - y**2) * sp.diff(value, y) - y * value)
    return sp.Poly(value, y, domain=sp.QQ)


@lru_cache(None)
def base_moment(exponent: int, h: int) -> sp.Rational:
    """2 integral_0^infty t^(2*exponent+h)/sinh(pi*t) dt."""
    s = 2 * exponent + h + 1
    assert s >= 2 and s % 2 == 0
    return sp.factor(
        sp.Rational((-1) ** (s // 2 + 1) * (2 ** (s + 1) - 2), s)
        * sp.bernoulli(s)
    )


def coefficients(poly: sp.Poly, shift: int = 0, scale: sp.Rational = sp.Rational(1)) -> dict[int, sp.Rational]:
    """Ascending Laurent coefficient dictionary."""
    return {
        degree + shift: sp.Rational(scale) * poly.nth(degree)
        for degree in range(poly.degree() + 1)
        if poly.nth(degree)
    }


def add(*rows: dict[int, sp.Rational]) -> dict[int, sp.Rational]:
    answer: dict[int, sp.Rational] = {}
    for row in rows:
        for degree, value in row.items():
            answer[degree] = sp.cancel(answer.get(degree, 0) + value)
    return {degree: value for degree, value in answer.items() if value}


def euler(row: dict[int, sp.Rational], h: int) -> dict[int, sp.Rational]:
    return {
        degree: sp.Rational(2 * degree + h + 1) * value
        for degree, value in row.items()
    }


def paired_moment(row: dict[int, sp.Rational], h: int, column: int) -> sp.Rational:
    """Return <row,Q_0> or pi^2 <row,Q_1> exactly."""
    if column == 0:
        return sp.factor(
            sum(value * base_moment(degree, h) for degree, value in row.items())
        )
    assert column == 1
    return sp.factor(
        sum(
            value
            * (2 * degree + h)
            * (2 * degree + h - 1)
            * base_moment(degree - 1, h)
            for degree, value in row.items()
        )
    )


def normalized_border(
    ordinary: dict[int, sp.Rational],
    border: dict[int, sp.Rational],
    h: int,
) -> sp.Rational:
    """pi^2 times the d=1 normalized bordered determinant."""
    ordinary_zero = paired_moment(ordinary, h, 0)
    ordinary_one = paired_moment(ordinary, h, 1)
    border_zero = paired_moment(border, h, 0)
    border_one = paired_moment(border, h, 1)
    assert ordinary_zero > 0
    return sp.factor(
        border_one - ordinary_one * border_zero / ordinary_zero
    )


def rational_digest(values: list[sp.Rational]) -> str:
    encoded = ",".join(
        f"{sp.numer(value)}/{sp.denom(value)}" for value in values
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def exact_row(k: int, n: int) -> tuple[dict, list[sp.Rational]]:
    h = n + 1
    V = sp.Poly(
        sp.prod((x + r * r) ** h for r in range(1, k + 1)),
        x,
        domain=sp.QQ,
    )
    V_row = coefficients(V)
    G_row = euler(V_row, h)

    def weight(r: int) -> sp.Rational:
        return sp.Rational(
            1,
            math.factorial(n)
            * (math.factorial(k + r) * math.factorial(k - r)) ** h,
        )

    natural_rho = weight(0) / x + 2 * sum(
        weight(r) / (x + r * r) for r in range(1, k + 1)
    )
    centered_R = sum(weight(r) / (U - r) for r in range(-k, k + 1))
    assert sp.cancel(
        centered_R.subs(U, sp.I * t)
        + sp.I * t * natural_rho.subs(x, t**2)
    ) == 0

    rho_minus_terms = [coefficients(V, shift=-1, scale=-weight(0))]
    psi_terms: list[dict[int, sp.Rational]] = []
    residues: list[sp.Rational] = []
    regular_parts: list[sp.Rational] = []

    for r in range(1, k + 1):
        divisor = V.exquo(sp.Poly(x + r * r, x, domain=sp.QQ))
        rho_minus_terms.append(coefficients(divisor, scale=-2 * weight(r)))

        regular = sp.factor(
            sum(
                weight(s) / (r - s)
                for s in range(-k, k + 1)
                if s != r
            )
        )
        harmonic = sp.harmonic(k + r) - sp.harmonic(k - r)
        residue = sp.factor(2 * r * h * (h * harmonic * weight(r) + regular))
        assert regular > 0 and residue > 0
        regular_parts.append(regular)
        residues.append(residue)
        psi_terms.append(coefficients(divisor, scale=residue))

    V_rho_minus = add(*rho_minus_terms)
    V_psi = add(*psi_terms)
    f_minus = euler(V_rho_minus, h)

    assert min(V_rho_minus) == -1
    assert 2 * min(V_rho_minus) + h + 1 == n
    assert all(value < 0 for value in V_rho_minus.values())
    assert all(value < 0 for value in f_minus.values())
    assert all(value > 0 for value in V_psi.values())

    f_minus_zero = paired_moment(f_minus, h, 0)
    expectation_shift = sp.factor(
        paired_moment(G_row, h, 1) / paired_moment(G_row, h, 0)
        - paired_moment(V_row, h, 1) / paired_moment(V_row, h, 0)
    )
    assert f_minus_zero < 0
    assert expectation_shift < 0

    signed_euler_difference = sp.factor(
        normalized_border(V_row, f_minus, h)
        - normalized_border(G_row, f_minus, h)
    )
    covariance_factorization = sp.factor(f_minus_zero * expectation_shift)
    assert signed_euler_difference == covariance_factorization
    assert signed_euler_difference > 0

    natural_euler_difference = -signed_euler_difference
    assert natural_euler_difference < 0

    stieltjes_border = normalized_border(V_row, V_psi, h)
    equivalent_signed_total = sp.factor(
        signed_euler_difference + stieltjes_border
    )
    raw_total = sp.factor(stieltjes_border - natural_euler_difference)
    direct_signed_total = sp.factor(
        normalized_border(V_row, add(f_minus, V_psi), h)
        - normalized_border(G_row, f_minus, h)
    )
    assert stieltjes_border > 0
    assert raw_total == equivalent_signed_total == direct_signed_total
    assert raw_total > 0

    values = [
        *regular_parts,
        *residues,
        f_minus_zero,
        expectation_shift,
        signed_euler_difference,
        natural_euler_difference,
        stieltjes_border,
        raw_total,
    ]
    row = {
        "k": k,
        "m": 2 * k + 1,
        "n": n,
        "h": h,
        "minimum_laurent_exponent": min(V_rho_minus),
        "minimum_euler_multiplier": n,
        "natural_rho_sign": "positive",
        "signed_real_row_rho_sign": "negative",
        "centered_phase_R_it_equals_minus_it_rho_plus": True,
        "all_signed_rho_coefficients_negative": True,
        "all_signed_euler_border_coefficients_negative": True,
        "all_simple_pole_residues_positive": True,
        "all_Vpsi_coefficients_positive": True,
        "signed_f_zero_sign": -1,
        "tilted_q_expectation_shift_sign": -1,
        "signed_euler_difference_sign": 1,
        "natural_euler_difference_sign": -1,
        "stieltjes_border_sign": 1,
        "raw_target_sign": 1,
        "signed_euler_difference_pi2_scaled": str(signed_euler_difference),
        "natural_euler_difference_pi2_scaled": str(natural_euler_difference),
        "stieltjes_border_pi2_scaled": str(stieltjes_border),
        "raw_target_pi2_scaled": str(raw_total),
        "exact_data_sha256": rational_digest(values),
    }
    return row, values


def main() -> None:
    assert derivative_polynomial(0).as_expr() == 1
    assert derivative_polynomial(1).as_expr() == -y
    assert derivative_polynomial(2).as_expr() == 2 * y**2 - 1

    A0, A1, G0, G1, F0, F1 = sp.symbols(
        "A0 A1 G0 G1 F0 F1", nonzero=True
    )
    nb_a = F1 - A1 * F0 / A0
    nb_g = F1 - G1 * F0 / G0
    assert sp.factor(nb_a - nb_g - F0 * (G1 / G0 - A1 / A0)) == 0

    rows: list[dict] = []
    digest = hashlib.sha256()
    for k in range(1, 7):
        for n in range(4, 11, 2):
            row, values = exact_row(k, n)
            rows.append(row)
            digest.update(
                f"{k},{n},{rational_digest(values)}\n".encode()
            )

    selected = [
        row
        for row in rows
        if (row["k"], row["n"]) in {(1, 4), (2, 6), (4, 8), (6, 10)}
    ]
    anchor = next(row for row in rows if (row["k"], row["n"]) == (1, 4))
    assert anchor["stieltjes_border_pi2_scaled"] == "2025/9698"
    assert anchor["natural_euler_difference_pi2_scaled"] == "-2115/271544"
    assert anchor["raw_target_pi2_scaled"] == "58815/271544"
    payload = {
        "schema": "root-unity-forced-odd-m-D3-covariance-certificate-v1",
        "symbolic_identities": {
            "H0": "1",
            "H1": "-y",
            "H2": "2*y^2-1",
            "normalized_border_difference_factorization": True,
            "a_derivative_formula": "2*h*sum(r^2/(x+r^2)^2)",
            "natural_rho_global_sign": "positive",
            "signed_real_row_rho_global_sign": "negative",
            "centered_phase": "R(i*t)=-i*t*rho_plus(t^2)",
            "minimum_euler_multiplier": "h-1=n>0",
        },
        "phase_anchor_k1_n4": {
            "stieltjes_border_pi2_scaled": "2025/9698",
            "natural_euler_difference_pi2_scaled": (
                "16323/38792-3/7=-2115/271544"
            ),
            "raw_target_pi2_scaled": "58815/271544",
        },
        "exact_grid": {
            "k_rule": "1 <= k <= 6",
            "n_rule": "even 4 <= n <= 10",
            "D": 3,
            "row_count": len(rows),
            "all_regular_parts_positive": True,
            "all_simple_pole_residues_positive": True,
            "all_centered_phase_identities_exact": True,
            "all_signed_rho_and_euler_border_coefficients_negative": True,
            "all_tilted_q_expectation_shifts_negative": True,
            "all_signed_euler_differences_positive": True,
            "all_natural_euler_differences_negative": True,
            "all_stieltjes_borders_positive": True,
            "all_raw_targets_positive": True,
            "exact_grid_sha256": digest.hexdigest(),
        },
        "selected_rows": selected,
        "logical_scope": {
            "all_parameter_theorem": (
                "The source proves the corrected raw target sign for every "
                "k>=1 and every even n>=4 at D=3 by opposite-monotonicity "
                "and same-monotonicity covariance identities."
            ),
            "finite_replay_only": (
                "The exact grid checks formulas and sign normalization; it "
                "is not extrapolated to prove universality."
            ),
            "excluded": (
                "No claim is made for D>=5, primitive content, height, or "
                "the arithmetic nature of e+pi."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["exact_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
