#!/usr/bin/env python3
"""Exact finite replay for the positive pole-truncation theorem.

The companion source proves an all-parameter theorem.  This script is only a
finite exact replay of its algebraic ingredients.  It uses QQ throughout and
checks, for all three cardinal families,

* the centered CRT factorization and its predicted global sign;
* the actual ordered confluent-Newton coefficients;
* finite canonical-product integral approximants, evaluated by exact beta
  moments;
* Hermite-remainder / polar-part reconstruction; and
* positivity of every ordered Newton coefficient of those finite remainders.

It also exhaustively checks the finite "completion" lemma on several repeated
rate lists.  No floating-point positivity test occurs here.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gamma_positive_pole_truncation_certificate.json"
X, U, x = sp.symbols("X U x")


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
    centered = sp.Poly(sp.expand(poly.as_expr().subs(X, center + U)), U)
    assert all(power[0] % 2 == 1 for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - 1) // 2)
            for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def even_flat_transform(
    poly: sp.Poly, center: sp.Rational, constant: sp.Rational, order: int
) -> sp.Poly:
    centered = sp.Poly(
        sp.expand(poly.as_expr().subs(X, center + U) - constant),
        U,
        domain=sp.QQ,
    )
    assert order % 2 == 0
    assert all(power[0] >= order for power, value in centered.terms() if value)
    assert all((power[0] - order) % 2 == 0
               for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - order) // 2)
            for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def odd_flat_transform(
    poly: sp.Poly, center: sp.Rational, linear: sp.Rational, order: int
) -> sp.Poly:
    centered = sp.Poly(
        sp.expand(poly.as_expr().subs(X, center + U) - linear * U),
        U,
        domain=sp.QQ,
    )
    assert order % 2 == 1
    assert all(power[0] >= order for power, value in centered.terms() if value)
    assert all((power[0] - order) % 2 == 0
               for power, value in centered.terms() if value)
    return sp.Poly(
        sum(value * (-x) ** ((power[0] - order) // 2)
            for power, value in centered.terms()),
        x,
        domain=sp.QQ,
    )


def normalize_sign(poly: sp.Poly) -> tuple[sp.Poly, int]:
    first = next(poly.nth(j) for j in range(poly.degree() + 1) if poly.nth(j))
    sign = int(sp.sign(first))
    return (poly if sign > 0 else -poly), sign


def base_rates(family: str, count: int) -> list[sp.Rational]:
    if family == "even-Lambda0":
        return [sp.Rational((2 * r - 1) ** 2, 4) for r in range(1, count + 1)]
    return [sp.Integer(r * r) for r in range(1, count + 1)]


def repeated_rates(rates: list[sp.Rational], h: int) -> list[sp.Rational]:
    return [rate for rate in rates for _ in range(h)]


def newton_coefficients(poly: sp.Poly, rates: list[sp.Rational]) -> list[sp.Rational]:
    """Coefficients in 1,(x+l_1),... for a polynomial of degree < len(rates)."""
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
    result = sp.Integer(0)
    for d, coefficient in enumerate(coefficients):
        result += coefficient * prefix
        if d < len(rates) - 1:
            prefix = sp.expand(prefix * (x + rates[d]))
    return sp.Poly(result, x, domain=sp.QQ)


def canonical_polynomial(rates: list[sp.Rational]) -> sp.Poly:
    return sp.Poly(sp.prod(1 + x / rate for rate in rates), x, domain=sp.QQ)


def beta_moment(power: int, beta_power: int) -> sp.Rational:
    """Integral_0^1 s^power (1-s)^beta_power ds, for integers."""
    return sp.Rational(
        math.factorial(power) * math.factorial(beta_power),
        math.factorial(power + beta_power + 1),
    )


def finite_product_integral(
    rates: list[sp.Rational], nu: int, alpha: int, beta_power: int
) -> sp.Poly:
    """Exact integral s^alpha(1-s)^beta P_L(s^2 x)^nu ds."""
    powered = canonical_polynomial(rates) ** nu
    return sp.Poly(
        sum(
            powered.nth(d) * beta_moment(2 * d + alpha, beta_power) * x**d
            for d in range(powered.degree() + 1)
        ),
        x,
        domain=sp.QQ,
    )


def digest_rationals(values: list[sp.Rational]) -> str:
    encoded = ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def actual_cardinal_numerator(
    family: str, k: int, n: int
) -> tuple[sp.Poly, int, int, int]:
    """Return normalized numerator, raw sign, m, and central order."""
    h = n + 1
    nu = 2 * (n // 2) + 1
    if family == "even-Lambda0":
        m = 2 * k
        cardinal = polynomial_crt_cardinal(m, n, 0)
        assert_cardinal(cardinal, m, n, 0)
        numerator = odd_center_transform(cardinal, sp.Rational(m - 1, 2))
        predicted_sign = (-1) ** k
        central_order = 1
    elif family == "odd-Lambda0":
        m = 2 * k + 1
        cardinal = polynomial_crt_cardinal(m, n, 0)
        assert_cardinal(cardinal, m, n, 0)
        sigma = (-1) ** k
        central_order = nu + 1
        assert central_order == h + (h % 2)
        numerator = even_flat_transform(
            cardinal, sp.Integer(k), sp.Integer(sigma), central_order
        )
        predicted_sign = -sigma
    elif family == "odd-Lambda1-defect":
        assert n % 2 == 1
        m = 2 * k + 1
        cardinal = polynomial_crt_cardinal(m, n, 1)
        assert_cardinal(cardinal, m, n, 1)
        sigma = (-1) ** k
        central_order = nu + 2
        assert central_order == h + 1
        numerator = odd_flat_transform(
            cardinal, sp.Integer(k), sp.Integer(sigma), central_order
        )
        predicted_sign = -sigma
    else:
        raise ValueError(family)
    normalized, raw_sign = normalize_sign(numerator)
    assert raw_sign == predicted_sign
    return normalized, raw_sign, m, central_order


def weight_parameters(family: str, nu: int) -> tuple[int, int]:
    if family == "even-Lambda0":
        return 0, 0
    if family == "odd-Lambda0":
        return nu, 0
    if family == "odd-Lambda1-defect":
        return nu, 1
    raise ValueError(family)


def check_family_row(family: str, k: int, n: int) -> dict:
    h = n + 1
    nu = 2 * (n // 2) + 1
    assert h in (nu, nu + 1)
    normalized, raw_sign, m, central_order = actual_cardinal_numerator(
        family, k, n
    )
    predicted_sign = (-1) ** k if family == "even-Lambda0" else -(-1) ** k
    assert raw_sign == predicted_sign
    finite_rates = base_rates(family, k)
    ordered_rates = repeated_rates(finite_rates, h)
    actual_coefficients = newton_coefficients(normalized, ordered_rates)
    assert normalized.degree() == k * h - 1
    assert all(value > 0 for value in actual_coefficients)
    assert reconstruct_newton(actual_coefficients, ordered_rates) == normalized

    # There are enough tail linear factors to realize every deletion path in
    # the h=nu+1 proof.  The h=nu case does not need this many, but using the
    # same deterministic cutoff makes the three replays uniform.
    product_cutoff = 2 * k + 1
    all_rates = base_rates(family, product_cutoff)
    alpha, beta_power = weight_parameters(family, nu)
    finite_integral = finite_product_integral(
        all_rates, nu, alpha, beta_power
    )
    modulus = canonical_polynomial(finite_rates) ** h
    quotient, remainder = sp.div(finite_integral, modulus)
    assert finite_integral == quotient * modulus + remainder
    assert remainder.degree() < k * h

    finite_coefficients = newton_coefficients(remainder, ordered_rates)
    assert all(value > 0 for value in finite_coefficients)
    assert reconstruct_newton(finite_coefficients, ordered_rates) == remainder

    return {
        "family": family,
        "m": m,
        "n": n,
        "h": h,
        "nu": nu,
        "central_order": central_order,
        "raw_cardinal_numerator_sign": raw_sign,
        "predicted_raw_sign": predicted_sign,
        "actual_degree": normalized.degree(),
        "actual_all_newton_coefficients_positive": True,
        "actual_first_newton_coefficient": str(actual_coefficients[0]),
        "actual_last_newton_coefficient": str(actual_coefficients[-1]),
        "actual_newton_sha256": digest_rationals(actual_coefficients),
        "finite_product_cutoff": product_cutoff,
        "finite_integral_weight": f"s^{alpha}(1-s)^{beta_power}",
        "finite_polar_reconstruction_exact": True,
        "finite_all_newton_coefficients_positive": True,
        "finite_first_newton_coefficient": str(finite_coefficients[0]),
        "finite_last_newton_coefficient": str(finite_coefficients[-1]),
        "finite_newton_sha256": digest_rationals(finite_coefficients),
    }


def check_completion_lemma(rates: tuple[int, ...]) -> int:
    """Exhaust every nonempty reciprocal subproduct for one ordered list."""
    count = 0
    for mask in range(1, 1 << len(rates)):
        complement = sp.Poly(
            sp.prod(x + rates[j] for j in range(len(rates)) if not (mask >> j) & 1),
            x,
            domain=sp.QQ,
        )
        coefficients = newton_coefficients(complement, list(map(sp.Integer, rates)))
        assert all(value >= 0 for value in coefficients)
        assert reconstruct_newton(coefficients, list(map(sp.Integer, rates))) == complement
        count += 1
    return count


def main() -> None:
    rows: list[dict] = []
    digest = hashlib.sha256()
    for family in ("even-Lambda0", "odd-Lambda0"):
        for k in range(1, 4):
            for n in range(2, 6):
                row = check_family_row(family, k, n)
                rows.append(row)
                digest.update(
                    (f"{family},{k},{n},{row['actual_newton_sha256']},"
                     f"{row['finite_newton_sha256']}\n").encode()
                )
    for k in range(1, 4):
        for n in (3, 5):
            row = check_family_row("odd-Lambda1-defect", k, n)
            rows.append(row)
            digest.update(
                (f"defect,{k},{n},{row['actual_newton_sha256']},"
                 f"{row['finite_newton_sha256']}\n").encode()
            )

    completion_lists = [
        (1, 2, 3, 4, 5, 6),
        (1, 1, 4, 4, 9, 9),
        (1, 1, 1, 4, 4, 9, 9),
    ]
    completion_rows = [
        {"rates": list(rates), "nonempty_subproducts_checked": check_completion_lemma(rates)}
        for rates in completion_lists
    ]

    selected = [
        row for row in rows
        if (row["family"], row["m"], row["n"])
        in {
            ("even-Lambda0", 6, 5),
            ("odd-Lambda0", 7, 4),
            ("odd-Lambda1-defect", 7, 5),
        }
    ]
    payload = {
        "schema": "root-unity-gamma-positive-pole-truncation-v1",
        "exact_arithmetic": "QQ only; no floating-point comparisons",
        "family_grid": {
            "generic_k_range": [1, 3],
            "generic_n_range": [2, 5],
            "defect_k_range": [1, 3],
            "defect_n_values": [3, 5],
            "row_count": len(rows),
            "all_cardinal_jets_exact": True,
            "all_predicted_global_signs_exact": True,
            "all_actual_newton_coefficients_positive": True,
            "all_finite_product_integrals_exact": True,
            "all_finite_polar_reconstructions_exact": True,
            "all_finite_newton_coefficients_positive": True,
            "row_digest_sha256": digest.hexdigest(),
        },
        "completion_lemma_grid": {
            "rows": completion_rows,
            "all_ordered_newton_coefficients_nonnegative": True,
        },
        "selected_rows": selected,
        "logical_scope": {
            "all_parameter_result": (
                "The companion source, not finite-grid extrapolation, proves the "
                "positive pole-truncation and strict Newton theorem for all parameters."
            ),
            "what_this_closes": (
                "Together with the frozen shifted-coordinate theorem, it proves the "
                "appropriate Gamma border nonzero for every m>=2 and n>=D>=2."
            ),
            "what_this_does_not_close": (
                "It does not prove corrected Delta nonzero and gives no primitive "
                "endpoint height/value estimate or transcendence conclusion."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["family_grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["completion_lemma_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
