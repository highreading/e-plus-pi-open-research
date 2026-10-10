#!/usr/bin/env python3
"""Exact certificate for the augmented root-of-unity Gamma minors.

This certificate is deliberately split from the frozen logistic-minor package.
It checks, over QQ and without floating point arithmetic,

* the shifted even-column minors used in the all-parameter coordinate-border
  proof;
* the centered Hermite-cardinal factorizations which produce the generic
  rational functions rho_0 and the parity-defect rational function rho_1;
* strict positivity of every coefficient in their ordered confluent Newton
  expansions on a finite grid;
* the resulting exact Coxian/product-resolvent decomposition; and
* the appropriate generic or defect bordered determinant directly on a
  smaller grid.

Finite Newton positivity is an exact theorem for the recorded tuples, not an
extrapolation to all m and n.  The companion source isolates the universal
Newton-positivity statement which remains to be proved.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gamma_augmented_newton_certificate.json"
X, U, x = sp.symbols("X U x")


def polynomial_crt_cardinal(m: int, n: int, b: int) -> sp.Poly:
    """Return Lambda_b with Lambda_b^(a)(j)=(-1)^j delta_(a,b)."""
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


def normalize_positive(poly: sp.Poly) -> tuple[sp.Poly, int]:
    """Normalize only by a global sign; retain all exact rational scales."""
    first = next(poly.nth(j) for j in range(poly.degree() + 1) if poly.nth(j))
    sign = int(sp.sign(first))
    return (poly if sign > 0 else -poly), sign


def odd_center_transform(poly: sp.Poly, center: sp.Rational) -> sp.Poly:
    """P(c+U)=U R(-U^2); return R(x)."""
    centered = sp.Poly(sp.expand(poly.as_expr().subs(X, center + U)), U)
    assert all(power[0] % 2 == 1 for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - 1) // 2) for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def even_flat_transform(
    poly: sp.Poly, center: sp.Rational, constant: sp.Rational, order: int
) -> sp.Poly:
    """P(c+U)-constant=U^order R(-U^2), for even order."""
    centered = sp.Poly(
        sp.expand(poly.as_expr().subs(X, center + U) - constant),
        U,
        domain=sp.QQ,
    )
    assert order % 2 == 0
    assert all(power[0] >= order for power, value in centered.terms() if value)
    assert all((power[0] - order) % 2 == 0 for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - order) // 2) for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def odd_flat_transform(
    poly: sp.Poly, center: sp.Rational, linear: sp.Rational, order: int
) -> sp.Poly:
    """P(c+U)-linear*U=U^order R(-U^2), for odd order."""
    centered = sp.Poly(
        sp.expand(poly.as_expr().subs(X, center + U) - linear * U),
        U,
        domain=sp.QQ,
    )
    assert order % 2 == 1
    assert all(power[0] >= order for power, value in centered.terms() if value)
    assert all((power[0] - order) % 2 == 0 for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - order) // 2) for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def repeated_rates(m: int, h: int) -> list[sp.Rational]:
    if m % 2 == 0:
        base = [sp.Rational((2 * r - 1) ** 2, 4) for r in range(1, m // 2 + 1)]
    else:
        base = [sp.Integer(r * r) for r in range(1, (m - 1) // 2 + 1)]
    return [rate for rate in base for _ in range(h)]


def newton_coefficients(poly: sp.Poly, rates: list[sp.Rational]) -> list[sp.Rational]:
    """Coefficients in prod_{j<d}(x+rates[j]), d=0,...,len(rates)-1."""
    assert poly.degree() == len(rates) - 1
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


def verify_coxian_identity(
    numerator: sp.Poly, rates: list[sp.Rational], coefficients: list[sp.Rational]
) -> None:
    # Cross-multiplying the displayed product-resolvent identity gives exactly
    # the Newton reconstruction below.  Checking it in polynomial form avoids
    # an exponentially expensive expansion of one large common denominator.
    prefix = sp.Integer(1)
    reconstructed = sp.Integer(0)
    for d, coefficient in enumerate(coefficients):
        reconstructed += coefficient * prefix
        if d < len(rates) - 1:
            prefix = sp.expand(prefix * (x + rates[d]))
    assert sp.Poly(reconstructed, x, domain=sp.QQ) == numerator


def rational_digest(values: list[sp.Rational]) -> str:
    encoded = ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def functional(poly: sp.Expr, moments: list[sp.Rational]) -> sp.Rational:
    expanded = sp.Poly(sp.expand(poly), X, domain=sp.QQ)
    return sum(expanded.nth(k) * moments[k] for k in range(expanded.degree() + 1))


def centered_endpoint_matrix(
    m: int, n: int, D: int, moments: list[sp.Rational]
) -> sp.Matrix:
    center = sp.Rational(m - 1, 2)
    phi = sp.prod((X - j) ** (n + 1) for j in range(m))
    return sp.Matrix(
        [
            [
                functional(sp.diff((X - center) ** q * phi, X, a), moments)
                for a in range(D + 1)
            ]
            for q in range(D - 1)
        ]
    )


def beta_row(
    cardinal: sp.Poly, D: int, moments: list[sp.Rational]
) -> sp.Matrix:
    return sp.Matrix(
        [[-functional(sp.diff(cardinal.as_expr(), X, a), moments) for a in range(D + 1)]]
    )


def check_shifted_coordinate_minor(
    matrix: sp.Matrix, m: int, n: int, D: int
) -> sp.Rational:
    rows = [q for q in range(D - 1) if q % 2 == (m * n) % 2]
    columns = [a for a in range(2, D + 1, 2)]
    size = min(len(rows), len(columns))
    assert size == len(rows)
    selected = matrix.extract(rows, columns[:size])
    determinant = sp.factor(selected.det())
    assert determinant != 0
    return determinant


def bordered_determinant(
    matrix: sp.Matrix, extra: sp.Matrix, D: int
) -> sp.Rational:
    coordinate = sp.zeros(1, D + 1)
    coordinate[0, 0] = 1
    return sp.factor(matrix.col_join(coordinate).col_join(extra).det())


def main() -> None:
    max_m, max_n = 10, 7
    rows: list[dict] = []
    digest = hashlib.sha256()
    lambda_cache: dict[tuple[int, int, int], sp.Poly] = {}

    for m in range(2, max_m + 1):
        for n in range(2, max_n + 1):
            h = n + 1
            center = sp.Rational(m - 1, 2)
            lam0 = polynomial_crt_cardinal(m, n, 0)
            lambda_cache[m, n, 0] = lam0
            assert_cardinal(lam0, m, n, 0)

            if m % 2 == 0:
                numerator = odd_center_transform(lam0, center)
                family = "generic-even-m-Lambda0"
                central_order = 1
            else:
                q0 = h % 2
                central_order = h + q0
                constant = sp.Integer((-1) ** ((m - 1) // 2))
                numerator = even_flat_transform(
                    lam0, center, constant, central_order
                )
                family = "generic-odd-m-Lambda0"

            numerator, discarded_sign = normalize_positive(numerator)
            rates = repeated_rates(m, h)
            assert numerator.degree() == len(rates) - 1
            coefficients = newton_coefficients(numerator, rates)
            assert all(coefficient > 0 for coefficient in coefficients)
            verify_coxian_identity(numerator, rates, coefficients)
            row = {
                "family": family,
                "m": m,
                "n": n,
                "h": h,
                "central_order": central_order,
                "numerator_degree": numerator.degree(),
                "rate_count": len(rates),
                "discarded_global_sign": discarded_sign,
                "all_newton_coefficients_strictly_positive": True,
                "first_newton_coefficient": str(coefficients[0]),
                "last_newton_coefficient": str(coefficients[-1]),
                "newton_sha256": rational_digest(coefficients),
            }
            rows.append(row)
            digest.update(
                (
                    f"{family},{m},{n},{numerator.degree()},"
                    f"{rational_digest(coefficients)}\n"
                ).encode()
            )

    defect_rows: list[dict] = []
    for m in range(3, max_m + 1, 2):
        for n in range(3, max_n + 1, 2):
            h = n + 1
            center = sp.Rational(m - 1, 2)
            lam1 = polynomial_crt_cardinal(m, n, 1)
            lambda_cache[m, n, 1] = lam1
            assert_cardinal(lam1, m, n, 1)
            linear = sp.Integer((-1) ** ((m - 1) // 2))
            numerator = odd_flat_transform(lam1, center, linear, h + 1)
            numerator, discarded_sign = normalize_positive(numerator)
            rates = repeated_rates(m, h)
            assert numerator.degree() == len(rates) - 1
            coefficients = newton_coefficients(numerator, rates)
            assert all(coefficient > 0 for coefficient in coefficients)
            verify_coxian_identity(numerator, rates, coefficients)
            row = {
                "family": "defect-odd-m-odd-n-Lambda1",
                "m": m,
                "n": n,
                "h": h,
                "central_order": h + 1,
                "numerator_degree": numerator.degree(),
                "rate_count": len(rates),
                "discarded_global_sign": discarded_sign,
                "all_newton_coefficients_strictly_positive": True,
                "first_newton_coefficient": str(coefficients[0]),
                "last_newton_coefficient": str(coefficients[-1]),
                "newton_sha256": rational_digest(coefficients),
            }
            defect_rows.append(row)
            digest.update(
                (
                    f"defect,{m},{n},{numerator.degree()},"
                    f"{rational_digest(coefficients)}\n"
                ).encode()
            )

    # Direct determinant replay on a deliberately smaller exact grid.
    determinant_rows = []
    moment_bound = 6 * (5 + 1) + 7
    moments = logistic_moments(moment_bound)
    for m in range(2, 7):
        for n in range(2, 6):
            lam0 = lambda_cache.get((m, n, 0)) or polynomial_crt_cardinal(m, n, 0)
            lam1 = None
            if m % 2 == 1 and n % 2 == 1:
                lam1 = lambda_cache.get((m, n, 1)) or polynomial_crt_cardinal(m, n, 1)
            for D in range(2, min(5, n) + 1):
                matrix = centered_endpoint_matrix(m, n, D, moments)
                shifted = check_shifted_coordinate_minor(matrix, m, n, D)
                defect = (m * n) % 2 == 1 and D % 2 == 0
                extra = beta_row(lam1 if defect else lam0, D, moments)
                bordered = bordered_determinant(matrix, extra, D)
                assert bordered != 0
                determinant_rows.append(
                    {
                        "m": m,
                        "n": n,
                        "D": D,
                        "defect": defect,
                        "shifted_coordinate_minor_nonzero": True,
                        "appropriate_bordered_minor_nonzero": True,
                        "shifted_minor_sign": int(sp.sign(shifted)),
                        "bordered_minor_sign": int(sp.sign(bordered)),
                    }
                )

    selected_tuples = {
        (2, 2),
        (4, 3),
        (8, 3),
        (9, 6),
        (10, 7),
    }
    selected = [row for row in rows if (row["m"], row["n"]) in selected_tuples]
    selected += [
        row
        for row in defect_rows
        if (row["m"], row["n"]) in {(3, 3), (7, 5), (9, 7)}
    ]

    payload = {
        "schema": "root-unity-gamma-augmented-newton-certificate-v1",
        "newton_grid": {
            "generic_m_range": [2, max_m],
            "generic_n_range": [2, max_n],
            "generic_row_count": len(rows),
            "defect_m_rule": f"odd 3 <= m <= {max_m}",
            "defect_n_rule": f"odd 3 <= n <= {max_n}",
            "defect_row_count": len(defect_rows),
            "all_cardinal_congruences": True,
            "all_centered_factorizations": True,
            "all_numerator_degrees_rate_count_minus_one": True,
            "all_newton_coefficients_strictly_positive": True,
            "all_coxian_identities_exact": True,
            "exact_row_digest_sha256": digest.hexdigest(),
        },
        "determinant_grid": {
            "m_range": [2, 6],
            "n_range": [2, 5],
            "D_rule": "2 <= D <= min(5,n)",
            "row_count": len(determinant_rows),
            "all_shifted_coordinate_minors_nonzero": True,
            "all_appropriate_bordered_minors_nonzero": True,
        },
        "selected_newton_rows": selected,
        "selected_determinant_rows": [
            row
            for row in determinant_rows
            if (row["m"], row["n"], row["D"])
            in {(2, 4, 4), (3, 3, 2), (3, 5, 4), (5, 5, 4), (6, 5, 5)}
        ],
        "logical_scope": {
            "exact_finite_theorem": (
                "Every positivity assertion is an exact rational comparison. "
                "The Coxian identities prove complete monotonicity for every "
                "recorded rational function, with no sampled-t positivity step."
            ),
            "all_parameter_part": (
                "The companion source proves the shifted coordinate-border "
                "minor for all m,n,D by a Toeplitz/Andreief argument."
            ),
            "open_part": (
                "The finite Newton grid is not an all-parameter proof of strict "
                "Newton positivity; that universal lemma remains isolated."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["newton_grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["determinant_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
