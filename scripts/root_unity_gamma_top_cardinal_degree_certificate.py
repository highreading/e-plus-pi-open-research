#!/usr/bin/env python3
"""Exact replay for the top-cardinal coefficient of corrected Gamma.

The companion source proves an all-parameter theorem.  This script does not
extrapolate from a grid.  It checks, over QQ and without floating point:

* the simple-pole formula for Lambda_n/Phi and its centered parity;
* the positive Stieltjes residues when n is even;
* the explicit positive Fourier sums and the ordered Newton/Coxian identity
  when n is odd;
* the exact parity criterion for the top bordered determinant; and
* direct top- and next-coefficient bordered determinants on a finite grid.

The next-coefficient data in the parity-forced top-zero cases are explicitly
diagnostic only; the source does not promote them to an all-parameter claim.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gamma_top_cardinal_degree_certificate.json"
X, U, x = sp.symbols("X U x")


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


def top_residues(m: int, n: int) -> list[sp.Rational]:
    """Residues in Lambda_n/Phi=sum_j w_j/(X-j)."""
    h = n + 1
    return [
        sp.Rational(
            (-1) ** (j + h * (m - 1 - j)),
            math.factorial(n)
            * (math.factorial(j) * math.factorial(m - 1 - j)) ** h,
        )
        for j in range(m)
    ]


def centered_rho(m: int, n: int) -> tuple[sp.Expr, sp.Poly, sp.Poly, list[sp.Rational]]:
    """Return rho with Lambda_n/Phi=U^epsilon rho(-U^2)."""
    center = sp.Rational(m - 1, 2)
    residues = top_residues(m, n)
    epsilon = ((m - 1) * n + 1) % 2
    rho = sp.Rational(0)

    if m % 2:
        rho -= residues[(m - 1) // 2] / x

    for j in range((m + 1) // 2, m):
        s = sp.Rational(j) - center
        if epsilon:
            rho -= 2 * residues[j] / (x + s**2)
        else:
            rho -= 2 * s * residues[j] / (x + s**2)

    rho = sp.cancel(rho)
    numerator_expr, denominator_expr = sp.fraction(rho)
    numerator = sp.Poly(numerator_expr, x, domain=sp.QQ)
    denominator = sp.Poly(denominator_expr, x, domain=sp.QQ)
    leading = denominator.LC()
    numerator = sp.Poly(numerator.as_expr() / leading, x, domain=sp.QQ)
    denominator = sp.Poly(denominator.as_expr() / leading, x, domain=sp.QQ)

    R = sum(
        residues[j] / (U - (sp.Rational(j) - center)) for j in range(m)
    )
    assert sp.cancel(R - U**epsilon * rho.subs(x, -U**2)) == 0

    rates = (
        [sp.Integer(0)]
        + [sp.Integer(r * r) for r in range(1, (m - 1) // 2 + 1)]
        if m % 2
        else [
            sp.Rational((2 * r - 1) ** 2, 4)
            for r in range(1, m // 2 + 1)
        ]
    )
    expected_denominator = sp.Poly(
        sp.prod(x + rate for rate in rates), x, domain=sp.QQ
    )
    assert denominator == expected_denominator
    assert numerator.degree() == len(rates) - 1
    return rho, numerator, denominator, rates


def newton_coefficients(
    numerator: sp.Poly, rates: list[sp.Rational]
) -> list[sp.Rational]:
    basis = [sp.Integer(1)]
    for rate in rates[:-1]:
        basis.append(sp.expand(basis[-1] * (x + rate)))
    remainder = numerator.as_expr()
    coefficients = [sp.Rational(0)] * len(rates)
    for d in range(len(rates) - 1, -1, -1):
        coefficient = sp.Poly(remainder, x, domain=sp.QQ).nth(d)
        coefficients[d] = coefficient
        remainder = sp.expand(remainder - coefficient * basis[d])
    assert remainder == 0
    return coefficients


def fourier_sums(m: int, n: int) -> list[sp.Rational]:
    """Positive Parseval sums occurring for odd n."""
    assert n % 2 == 1
    if m % 2:
        k = (m - 1) // 2
        out = []
        for d in range(k + 1):
            value = sum(
                (-1 if r % 2 else 1)
                * sp.binomial(2 * d, d + r)
                * sp.binomial(2 * k, k + r) ** n
                for r in range(-d, d + 1)
            )
            out.append(sp.cancel(value / sp.factorial(2 * d)))
        return out

    k = m // 2
    out = []
    for d in range(k):
        value = sp.Rational(0)
        for j in range(2 * d + 2):
            s = sp.Rational(2 * j - 2 * d - 1, 2)
            value += (
                (-1) ** (d + 1 + j)
                * s
                * sp.binomial(2 * d + 1, j)
                * sp.binomial(2 * k - 1, k - d - 1 + j) ** n
            )
        out.append(sp.cancel(value / sp.factorial(2 * d + 1)))
    return out


def rational_digest(values: list[sp.Rational]) -> str:
    encoded = ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def top_cardinal_polynomial(m: int, n: int, phi: sp.Expr) -> sp.Expr:
    quotient = sum(top_residues(m, n)[j] / (X - j) for j in range(m))
    polynomial = sp.cancel(phi * quotient)
    assert sp.denom(polynomial) == 1
    polynomial = sp.expand(polynomial)
    for j in range(m):
        for a in range(n + 1):
            expected = (-1) ** j if a == n else 0
            assert sp.diff(polynomial, X, a).subs(X, j) == expected
    return polynomial


def penultimate_cardinal_polynomial(m: int, n: int, phi: sp.Expr) -> sp.Expr:
    """Construct Lambda_(n-1)/Phi from its exact double-pole expansion."""
    residues = top_residues(m, n)
    quotient = sp.Rational(0)
    for j, residue in enumerate(residues):
        harmonic_difference = sp.harmonic(j) - sp.harmonic(m - 1 - j)
        double = n * residue
        simple = -n * (n + 1) * harmonic_difference * residue
        quotient += double / (X - j) ** 2 + simple / (X - j)
    polynomial = sp.cancel(phi * quotient)
    assert sp.denom(polynomial) == 1
    polynomial = sp.expand(polynomial)
    for j in range(m):
        for a in range(n + 1):
            expected = (-1) ** j if a == n - 1 else 0
            assert sp.diff(polynomial, X, a).subs(X, j) == expected
    return polynomial


def centered_endpoint_matrix(
    m: int, n: int, D: int, phi: sp.Expr, moments: list[sp.Rational]
) -> sp.Matrix:
    center = sp.Rational(m - 1, 2)
    return sp.Matrix(
        [
            [
                functional(sp.diff((X - center) ** q * phi, X, a), moments)
                for a in range(D + 1)
            ]
            for q in range(D - 1)
        ]
    )


def beta_row(cardinal: sp.Expr, D: int, moments: list[sp.Rational]) -> sp.Matrix:
    return sp.Matrix(
        [[-functional(sp.diff(cardinal, X, a), moments) for a in range(D + 1)]]
    )


def coordinate_row(D: int, a: int) -> sp.Matrix:
    row = sp.zeros(1, D + 1)
    row[0, a] = 1
    return row


def bordered(matrix: sp.Matrix, coordinate: int, extra: sp.Matrix, D: int) -> sp.Rational:
    return sp.factor(matrix.col_join(coordinate_row(D, coordinate)).col_join(extra).det())


def top_parity_allowed(m: int, n: int, D: int) -> bool:
    return not ((n % 2 == 0 and D % 2 == 1) or (m % 2 == 0 and n % 2 == 1 and D % 2 == 0))


def main() -> None:
    digest = hashlib.sha256()
    cm_rows: list[dict] = []

    for m in range(2, 13):
        for n in range(2, 10):
            rho, numerator, denominator, rates = centered_rho(m, n)
            if n % 2 == 0:
                residues = [
                    sp.cancel(sp.limit((x + rate) * rho, x, -rate))
                    for rate in rates
                ]
                signs = {int(sp.sign(value)) for value in residues}
                assert len(signs) == 1 and 0 not in signs
                discarded_sign = next(iter(signs))
                positive_data = [discarded_sign * value for value in residues]
                family = "even-n-positive-simple-residues"
                ratio = None
            else:
                coefficients = newton_coefficients(numerator, rates)
                signs = {int(sp.sign(value)) for value in coefficients}
                assert len(signs) == 1 and 0 not in signs
                discarded_sign = next(iter(signs))
                positive_data = [discarded_sign * value for value in coefficients]
                sums = fourier_sums(m, n)
                assert all(value > 0 for value in sums)
                ratios = [sp.cancel(positive_data[d] / sums[d]) for d in range(len(sums))]
                assert len(set(ratios)) == 1 and ratios[0] > 0
                ratio = ratios[0]
                family = "odd-n-positive-ordered-Newton"

            assert all(value > 0 for value in positive_data)
            row = {
                "family": family,
                "m": m,
                "n": n,
                "rho_parity_epsilon": ((m - 1) * n + 1) % 2,
                "rate_count": len(rates),
                "numerator_degree": numerator.degree(),
                "discarded_global_sign": discarded_sign,
                "first_positive_datum": str(positive_data[0]),
                "last_positive_datum": str(positive_data[-1]),
                "positive_data_sha256": rational_digest(positive_data),
                "newton_to_fourier_common_ratio": None if ratio is None else str(ratio),
            }
            cm_rows.append(row)
            digest.update(
                (
                    f"{family},{m},{n},{discarded_sign},"
                    f"{rational_digest(positive_data)}\n"
                ).encode()
            )

    # Direct exact bordered-minor replay on a smaller grid.
    determinant_rows: list[dict] = []
    max_m, max_n, max_D = 6, 7, 6
    moments = logistic_moments(max_m * (max_n + 1) + max_D + 4)
    for m in range(2, max_m + 1):
        for n in range(2, max_n + 1):
            phi = sp.expand(sp.prod((X - j) ** (n + 1) for j in range(m)))
            lambda_n = top_cardinal_polynomial(m, n, phi)
            lambda_previous = penultimate_cardinal_polynomial(m, n, phi)
            for D in range(2, min(max_D, n) + 1):
                matrix = centered_endpoint_matrix(m, n, D, phi, moments)
                assert matrix.rank() == D - 1
                top = bordered(matrix, D, beta_row(lambda_n, D, moments), D)
                allowed = top_parity_allowed(m, n, D)
                assert (top != 0) == allowed

                next_value = bordered(
                    matrix, D, beta_row(lambda_previous, D, moments), D
                ) + bordered(matrix, D - 1, beta_row(lambda_n, D, moments), D)
                if not allowed:
                    # This is an exact finite diagnostic, not a universal claim.
                    assert next_value != 0

                determinant_rows.append(
                    {
                        "m": m,
                        "n": n,
                        "D": D,
                        "top_parity_allowed": allowed,
                        "top_bordered_minor_nonzero": top != 0,
                        "top_bordered_minor_sign": int(sp.sign(top)),
                        "next_bordered_sum_nonzero": next_value != 0,
                        "next_bordered_sum_sign": int(sp.sign(next_value)),
                    }
                )

    selected_cm = [
        row
        for row in cm_rows
        if (row["m"], row["n"]) in {(2, 3), (3, 4), (5, 5), (8, 7), (12, 9)}
    ]
    selected_determinants = [
        row
        for row in determinant_rows
        if (row["m"], row["n"], row["D"])
        in {(2, 3, 2), (2, 4, 3), (3, 4, 3), (3, 5, 4), (6, 5, 4), (6, 6, 5)}
    ]

    payload = {
        "schema": "root-unity-gamma-top-cardinal-degree-certificate-v1",
        "complete_monotonicity_grid": {
            "m_range": [2, 12],
            "n_range": [2, 9],
            "row_count": len(cm_rows),
            "all_centered_rational_identities_exact": True,
            "all_even_n_simple_residues_one_strict_sign": True,
            "all_odd_n_newton_coefficients_one_strict_sign": True,
            "all_odd_n_fourier_sums_strictly_positive": True,
            "all_newton_to_fourier_ratios_constant_in_d": True,
            "exact_row_digest_sha256": digest.hexdigest(),
        },
        "determinant_grid": {
            "m_range": [2, max_m],
            "n_range": [2, max_n],
            "D_rule": f"2 <= D <= min({max_D},n)",
            "row_count": len(determinant_rows),
            "top_allowed_rule": (
                "not (n even and D odd), and not "
                "(m even and n odd and D even)"
            ),
            "top_nonzero_exactly_when_parity_allowed": True,
            "forced_top_zero_next_sum_nonzero_on_grid": True,
        },
        "selected_complete_monotonicity_rows": selected_cm,
        "selected_determinant_rows": selected_determinants,
        "logical_scope": {
            "all_parameter_part": (
                "The companion source proves centered binomial-power positivity, "
                "the explicit Fourier-sum formulas, strict complete monotonicity, "
                "and top-border nonvanishing whenever parity permits."
            ),
            "finite_replay_part": (
                "All recorded identities, signs, determinants, and Fourier sums "
                "are exact rational computations, with no sampled real-variable step."
            ),
            "open_part": (
                "In the two parity-forced top-zero families, nonvanishing of the "
                "coefficient at n+D-1 is observed exactly on the grid only; it is "
                "a sum of two bordered minors and is not asserted universally."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["complete_monotonicity_grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["determinant_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
