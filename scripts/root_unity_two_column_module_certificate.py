#!/usr/bin/env python3
"""Exact certificate for two-column endpoint inheritance.

For the natural two-dimensional constrained endpoint space, this script
constructs the unique auxiliary exponential polynomial B for each endpoint
polynomial C, forms beta_C(z)=B_C(z)|_{exp(z)=-1}, and checks the exact
cross-polynomial Gamma=C_0 beta_1-C_1 beta_0.  Gamma(i*pi)=0 is equivalent
to Gamma=0 because i*pi is transcendental.  Zero cases are factored all the
way to a common form and verified to be polynomial-multiple degeneracies.

All matrix, polynomial, content, and factorization assertions are exact.
There are no floating-point assertions in this certificate.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_two_column_module_certificate.json"
Z, Y = sp.symbols("z y")


def convolve(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def derivative(p: list[int], order: int) -> list[int]:
    p = p[:]
    for _ in range(order):
        p = [(k + 1) * p[k + 1] for k in range(len(p) - 1)]
    return p


def phi_coefficients(m: int, n: int) -> list[int]:
    p = [1]
    for j in range(m):
        for _ in range(n + 1):
            p = convolve(p, [-j, 1])
    return p


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def functional(p: list[int], moments: list[sp.Rational]) -> sp.Rational:
    return sum(sp.Integer(a) * moments[k] for k, a in enumerate(p))


def endpoint_matrix_two(
    m: int, n: int, D: int, moments: list[sp.Rational]
) -> sp.Matrix:
    phi = phi_coefficients(m, n)
    return sp.Matrix(
        [
            [
                functional(derivative([0] * q + phi, a), moments)
                for a in range(D + 1)
            ]
            for q in range(D - 1)
        ]
    )


def jet_interpolation_map(
    m: int, n: int, D: int, moments: list[sp.Rational]
) -> tuple[sp.Matrix, list[tuple[int, int]]]:
    """Map coefficients of C to coefficients of the matching B."""
    M = m * (n + 1)
    columns = [(j, a) for j in range(m) for a in range(n + 1)]
    jet = sp.Matrix(
        [
            [
                sp.factorial(k) / sp.factorial(k - a) * j ** (k - a)
                if a <= k
                else 0
                for j, a in columns
            ]
            for k in range(M)
        ]
    )
    target = sp.Matrix(
        [
            [
                -sp.factorial(k) / sp.factorial(k - a) * moments[k - a]
                if a <= k
                else 0
                for a in range(D + 1)
            ]
            for k in range(M)
        ]
    )
    assert jet.det() != 0
    return jet.inv() * target, columns


def primitive_coefficients(expression: sp.Expr, variable: sp.Symbol) -> list[int]:
    polynomial = sp.Poly(sp.expand(expression), variable, domain=sp.QQ)
    if polynomial.is_zero:
        return []
    rationals = [polynomial.nth(k) for k in range(polynomial.degree() + 1)]
    denominator = math.lcm(*(int(sp.denom(c)) for c in rationals))
    integers = [int(c * denominator) for c in rationals]
    content = math.gcd(*(abs(c) for c in integers))
    integers = [c // content for c in integers]
    if integers[-1] < 0:
        integers = [-c for c in integers]
    assert math.gcd(*(abs(c) for c in integers)) == 1
    return integers


def exact_row(
    m: int,
    n: int,
    D: int,
    moments: list[sp.Rational],
    interpolation: sp.Matrix,
    columns: list[tuple[int, int]],
) -> dict:
    matrix = endpoint_matrix_two(m, n, D, moments)
    rank = matrix.rank()
    assert rank == D - 1
    basis = sp.Matrix.hstack(*matrix.nullspace())
    assert basis.shape == (D + 1, 2)

    auxiliary_map = interpolation[:, : D + 1]
    auxiliary_basis = auxiliary_map * basis
    endpoints = [
        sp.expand(sum(basis[a, j] * Z**a for a in range(D + 1)))
        for j in range(2)
    ]
    auxiliaries = [
        sp.expand(
            sum(
                auxiliary_basis[index, j] * Z**a * Y**frequency
                for index, (frequency, a) in enumerate(columns)
            )
        )
        for j in range(2)
    ]
    beta = [sp.expand(auxiliary.subs(Y, -1)) for auxiliary in auxiliaries]
    gamma = sp.expand(endpoints[0] * beta[1] - endpoints[1] * beta[0])
    gamma_coefficients = primitive_coefficients(gamma, Z)

    row = {
        "m": m,
        "n": n,
        "D": D,
        "endpoint_matrix_rank": rank,
        "expected_rank": D - 1,
        "vanishing_order_lower_bound": m * (n + 1) + D - 1,
        "zero_estimate_degeneracy_condition": n + (2 - m) * D >= 0,
        "gamma_is_zero": not gamma_coefficients,
        "gamma_degree": None if not gamma_coefficients else len(gamma_coefficients) - 1,
        "gamma_primitive_coefficients_ascending": gamma_coefficients,
    }

    if gamma_coefficients:
        return row

    # Exact classification of every zero case found in the grid.
    full_cross = sp.expand(
        endpoints[0] * auxiliaries[1] - endpoints[1] * auxiliaries[0]
    )
    assert full_cross == 0
    gcd_poly = sp.gcd(sp.Poly(endpoints[0], Z), sp.Poly(endpoints[1], Z)).monic()
    common_endpoint = gcd_poly.as_expr()
    a = sp.cancel(endpoints[0] / common_endpoint)
    b = sp.cancel(endpoints[1] / common_endpoint)
    assert sp.denom(a) == 1 and sp.denom(b) == 1
    common_auxiliary_0 = sp.cancel(auxiliaries[0] / a)
    common_auxiliary_1 = sp.cancel(auxiliaries[1] / b)
    assert sp.denom(common_auxiliary_0) == 1
    assert sp.denom(common_auxiliary_1) == 1
    assert sp.expand(common_auxiliary_0 - common_auxiliary_1) == 0
    common_auxiliary = sp.expand(common_auxiliary_0)
    common_form = sp.expand(common_endpoint + (1 + Y) * common_auxiliary)
    form_0 = sp.expand(endpoints[0] + (1 + Y) * auxiliaries[0])
    form_1 = sp.expand(endpoints[1] + (1 + Y) * auxiliaries[1])
    assert sp.expand(form_0 - a * common_form) == 0
    assert sp.expand(form_1 - b * common_form) == 0

    endpoint_wronskian = sp.expand(
        endpoints[0] * sp.diff(endpoints[1], Z)
        - endpoints[1] * sp.diff(endpoints[0], Z)
    )
    multiplier_wronskian = sp.expand(a * sp.diff(b, Z) - b * sp.diff(a, Z))
    assert sp.expand(
        endpoint_wronskian - common_endpoint**2 * multiplier_wronskian
    ) == 0
    assert multiplier_wronskian != 0

    assert m == 1 and n % 2 == 0 and D % 2 == 1
    assert max(sp.degree(a, Z), sp.degree(b, Z)) == 1
    row["degenerate_common_factor"] = {
        "multiplier_a_primitive_coefficients_ascending": primitive_coefficients(a, Z),
        "multiplier_b_primitive_coefficients_ascending": primitive_coefficients(b, Z),
        "common_endpoint_primitive_coefficients_ascending": primitive_coefficients(
            common_endpoint, Z
        ),
        "common_auxiliary_bivariate": str(common_auxiliary),
        "multiplier_wronskian": str(multiplier_wronskian),
        "base_n": n - 1,
        "base_D": D - 1,
        "base_has_m1_parity_bonus": (n - 1) % 2 == 1 and (D - 1) % 2 == 0,
    }
    return row


def digest_row(row: dict) -> dict:
    return {
        key: row[key]
        for key in (
            "m",
            "n",
            "D",
            "endpoint_matrix_rank",
            "gamma_is_zero",
            "gamma_degree",
            "gamma_primitive_coefficients_ascending",
        )
    }


def selected(row: dict) -> bool:
    key = (row["m"], row["n"], row["D"])
    return row["gamma_is_zero"] or key in {
        (1, 8, 6),
        (2, 8, 6),
        (3, 8, 6),
        (4, 8, 6),
        (5, 10, 8),
        (6, 10, 8),
    }


def main() -> None:
    max_m = 6
    max_n = 10
    max_D = 8
    moments = logistic_moments(max_m * (max_n + 1) + max_D)
    rows = []

    for m in range(1, max_m + 1):
        for n in range(2, max_n + 1):
            D_limit = min(max_D, n)
            interpolation, columns = jet_interpolation_map(
                m, n, D_limit, moments
            )
            for D in range(2, D_limit + 1):
                rows.append(
                    exact_row(
                        m,
                        n,
                        D,
                        moments,
                        interpolation,
                        columns,
                    )
                )

    assert len(rows) == 252
    assert all(r["endpoint_matrix_rank"] == r["expected_rank"] for r in rows)
    zero_rows = [r for r in rows if r["gamma_is_zero"]]
    expected_zero_tuples = [
        [1, n, D]
        for n in range(2, max_n + 1)
        if n % 2 == 0
        for D in range(3, min(max_D, n) + 1, 2)
    ]
    observed_zero_tuples = [[r["m"], r["n"], r["D"]] for r in zero_rows]
    assert observed_zero_tuples == expected_zero_tuples
    assert all("degenerate_common_factor" in r for r in zero_rows)

    exact_material = json.dumps(
        [digest_row(row) for row in rows],
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    payload = {
        "schema": "root-unity-two-column-module-certificate-v1",
        "exact_grid": {
            "m_range": [1, max_m],
            "n_range": [2, max_n],
            "D_rule": "2 <= D <= min(8,n)",
            "row_count": len(rows),
            "all_expected_ranks": all(
                r["endpoint_matrix_rank"] == r["expected_rank"] for r in rows
            ),
            "gamma_zero_count": len(zero_rows),
            "gamma_zero_tuples": observed_zero_tuples,
            "all_gamma_zeros_are_factored_polynomial_multiples": all(
                "degenerate_common_factor" in r for r in zero_rows
            ),
            "zero_estimate_condition_row_count": sum(
                r["zero_estimate_degeneracy_condition"] for r in rows
            ),
            "no_gamma_zero_with_m_at_least_2": not any(
                r["gamma_is_zero"] and r["m"] >= 2 for r in rows
            ),
            "exact_tuple_sha256": hashlib.sha256(exact_material).hexdigest(),
        },
        "zero_rows_exact_factorizations": zero_rows,
        "selected_nonzero_rows": [
            digest_row(row) for row in rows if selected(row) and not row["gamma_is_zero"]
        ],
        "logical_scope": {
            "exact": (
                "All ranks, Gamma polynomials, zero classifications, common-form "
                "factorizations, and Wronskian identities are exact over Q[z,y]."
            ),
            "finite_grid": (
                "The absence of a nondegenerate Gamma-zero tuple outside the proved "
                "m=1 classification is only a finite-grid result."
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
