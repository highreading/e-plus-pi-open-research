#!/usr/bin/env python3
"""Exact certificate for the logistic-minor reduction of Gamma.

The certificate checks, over Q and without floating point arithmetic,

* the centered checkerboard structure and the predicted parity nullities of
  the reduced endpoint matrix;
* the coefficient-by-coefficient bordered-minor formula for
  Gamma=C beta_D-D beta_C;
* the parity reversal of beta+(m/2)C;
* the closed formula for the top Hermite-cardinal polynomial Lambda_n; and
* an exact negative 2-by-2 minor showing that the naturally sign-normalized
  centered block is not totally positive.

The finite grid only certifies the algebraic identities as implemented.  The
all-parameter rank theorem in the companion source is proved analytically.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gamma_logistic_minor_certificate.json"
X, Z = sp.symbols("X z")


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


def derivative(p: list[sp.Rational], order: int) -> list[sp.Rational]:
    out = p[:]
    for _ in range(order):
        out = [(j + 1) * out[j + 1] for j in range(len(out) - 1)]
    return out


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    mu = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        mu.append(-sum(sp.binomial(k, j) * mu[j] for j in range(k)) / 2)
    return mu


def functional(p: list[sp.Rational], mu: list[sp.Rational]) -> sp.Rational:
    return sum(coefficient * mu[k] for k, coefficient in enumerate(p))


def polynomial_coefficients(expr: sp.Expr) -> list[sp.Rational]:
    poly = sp.Poly(sp.expand(expr), X, domain=sp.QQ)
    if poly.is_zero:
        return [sp.Rational(0)]
    return [poly.nth(k) for k in range(poly.degree() + 1)]


def endpoint_matrix(
    m: int, n: int, D: int, mu: list[sp.Rational], centered: bool
) -> sp.Matrix:
    phi = sum(c * X**k for k, c in enumerate(phi_coefficients(m, n)))
    center = sp.Rational(m - 1, 2) if centered else sp.Integer(0)
    return sp.Matrix(
        [
            [
                functional(
                    polynomial_coefficients(
                        sp.diff((X - center) ** q * phi, X, a)
                    ),
                    mu,
                )
                for a in range(D + 1)
            ]
            for q in range(D - 1)
        ]
    )


def hermite_cardinal_polynomials(m: int, n: int) -> list[sp.Expr]:
    """Lambda_b^(a)(j)=(-1)^j delta_(a,b), 0<=a,b<=n."""
    M = m * (n + 1)
    matrix = sp.zeros(M, M)
    target = sp.zeros(M, n + 1)
    row = 0
    for j in range(m):
        for a in range(n + 1):
            for k in range(a, M):
                matrix[row, k] = (
                    sp.factorial(k) / sp.factorial(k - a) * j ** (k - a)
                )
            target[row, a] = (-1) ** j
            row += 1
    coefficients = matrix.inv() * target
    return [
        sp.expand(sum(coefficients[k, b] * X**k for k in range(M)))
        for b in range(n + 1)
    ]


def beta_rows(
    lambdas: list[sp.Expr], D: int, mu: list[sp.Rational]
) -> sp.Matrix:
    return sp.Matrix(
        [
            [
                -functional(polynomial_coefficients(sp.diff(lam, X, a)), mu)
                for a in range(D + 1)
            ]
            for lam in lambdas
        ]
    )


def convolution_gamma(
    basis: sp.Matrix, beta: sp.Matrix, n: int, D: int
) -> list[sp.Rational]:
    c = basis[:, 0]
    d = basis[:, 1]
    beta_c = beta * c
    beta_d = beta * d
    out = [sp.Rational(0)] * (n + D + 1)
    for a in range(D + 1):
        for b in range(n + 1):
            out[a + b] += c[a] * beta_d[b] - d[a] * beta_c[b]
    return out


def bordered_sums(
    matrix: sp.Matrix, beta: sp.Matrix, n: int, D: int
) -> list[sp.Rational]:
    out = []
    for ell in range(n + D + 1):
        value = sp.Rational(0)
        for a in range(D + 1):
            b = ell - a
            if not 0 <= b <= n:
                continue
            coordinate = sp.zeros(1, D + 1)
            coordinate[0, a] = 1
            bordered = matrix.col_join(coordinate).col_join(beta[b, :])
            value += bordered.det()
        out.append(sp.factor(value))
    return out


def primitive_integer_vector(values: list[sp.Rational]) -> list[int]:
    if not any(values):
        return [0] * len(values)
    denominator = math.lcm(*(int(sp.denom(value)) for value in values))
    integers = [int(value * denominator) for value in values]
    content = math.gcd(*(abs(value) for value in integers))
    integers = [value // content for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return integers


def parity_kernel_dimensions(matrix: sp.Matrix, D: int) -> tuple[int, int]:
    even = [a for a in range(D + 1) if a % 2 == 0]
    odd = [a for a in range(D + 1) if a % 2 == 1]
    return (
        len(even) - matrix[:, even].rank(),
        len(odd) - matrix[:, odd].rank(),
    )


def parity_basis(matrix: sp.Matrix, D: int, parity: int) -> list[sp.Matrix]:
    columns = [a for a in range(D + 1) if a % 2 == parity]
    small = matrix[:, columns]
    out = []
    for vector in small.nullspace():
        lifted = sp.zeros(D + 1, 1)
        for index, column in enumerate(columns):
            lifted[column] = vector[index]
        out.append(lifted)
    return out


def check_top_cardinal_formula(
    m: int, n: int, lambda_n: sp.Expr
) -> tuple[sp.Expr, list[sp.Rational]]:
    base = sp.prod((X - j) ** n for j in range(m))
    values = []
    for j in range(m):
        denominator = (
            sp.factorial(n)
            * (sp.factorial(j) * sp.factorial(m - 1 - j)) ** n
        )
        sign = (-1) ** (j + n * (m - 1 - j))
        values.append(sp.Rational(sign, denominator))
    lagrange = sp.interpolate([(j, values[j]) for j in range(m)], X)
    reconstructed = sp.expand(base * lagrange)
    assert sp.expand(reconstructed - lambda_n) == 0

    simple_denominator = sp.prod(X - j for j in range(m))
    residues = []
    for j in range(m):
        residue = sp.cancel(
            lagrange.subs(X, j) / sp.diff(simple_denominator, X).subs(X, j)
        )
        expected = sp.Rational(
            (-1) ** (j + (n + 1) * (m - 1 - j)),
            sp.factorial(n)
            * (sp.factorial(j) * sp.factorial(m - 1 - j)) ** (n + 1),
        )
        assert residue == expected
        residues.append(residue)
    assert sp.cancel(
        lambda_n
        / sp.prod((X - j) ** (n + 1) for j in range(m))
        - sum(residues[j] / (X - j) for j in range(m))
    ) == 0
    return sp.expand(lagrange), residues


def total_positivity_counterexample(mu: list[sp.Rational]) -> dict:
    m, n, D = 2, 4, 5
    centered = endpoint_matrix(m, n, D, mu, centered=True)
    block = centered.extract([1, 3], [1, 3, 5])
    row_signs = [1, -1]
    column_signs = [1, -1, 1]
    normalized = sp.diag(*row_signs) * block * sp.diag(*column_signs)
    assert all(value > 0 for value in normalized)
    negative_minor = normalized[:, [0, 2]].det()
    assert negative_minor == -145_920
    return {
        "tuple": [m, n, D],
        "raw_odd_block": [[int(value) for value in row] for row in block.tolist()],
        "row_signs": row_signs,
        "column_signs": column_signs,
        "entrywise_positive_normalization": [
            [int(value) for value in row] for row in normalized.tolist()
        ],
        "negative_minor_columns": [0, 2],
        "negative_minor": int(negative_minor),
    }


def main() -> None:
    max_m, max_n, max_D = 4, 5, 5
    mu = logistic_moments(max_m * (max_n + 1) + max_D + 5)
    rows = []
    digest = hashlib.sha256()
    cardinal_cache: dict[tuple[int, int], list[sp.Expr]] = {}

    for m in range(1, max_m + 1):
        for n in range(2, max_n + 1):
            lambdas = hermite_cardinal_polynomials(m, n)
            cardinal_cache[m, n] = lambdas
            top_polynomial, residues = check_top_cardinal_formula(
                m, n, lambdas[n]
            )
            for D in range(2, min(max_D, n) + 1):
                matrix = endpoint_matrix(m, n, D, mu, centered=False)
                centered = endpoint_matrix(m, n, D, mu, centered=True)
                assert matrix.rank() == centered.rank() == D - 1
                basis = sp.Matrix.hstack(*matrix.nullspace())
                assert basis.shape == (D + 1, 2)
                beta = beta_rows(lambdas, D, mu)

                gamma = convolution_gamma(basis, beta, n, D)
                minors = bordered_sums(matrix, beta, n, D)
                nonzero = [k for k, value in enumerate(minors) if value]
                if nonzero:
                    ratio = sp.cancel(gamma[nonzero[0]] / minors[nonzero[0]])
                    assert ratio
                    assert all(
                        sp.cancel(gamma[k] - ratio * minors[k]) == 0
                        for k in range(len(gamma))
                    )
                else:
                    assert not any(gamma)

                even_nullity, odd_nullity = parity_kernel_dimensions(centered, D)
                defect = (m * n) % 2 == 1 and D % 2 == 0
                expected = (2, 0) if defect else (1, 1)
                assert (even_nullity, odd_nullity) == expected

                # The gauge beta_hat=beta+(m/2)C reverses endpoint parity.
                beta_hat = sp.zeros(n + 1, D + 1)
                for b in range(n + 1):
                    for a in range(D + 1):
                        beta_hat[b, a] = beta[b, a]
                        if a == b:
                            beta_hat[b, a] += sp.Rational(m, 2)
                for parity in (0, 1):
                    for vector in parity_basis(centered, D, parity):
                        image = beta_hat * vector
                        assert all(
                            image[b] == 0 for b in range(n + 1) if b % 2 == parity
                        )

                gamma_primitive = primitive_integer_vector(gamma)
                minor_primitive = primitive_integer_vector(minors)
                assert gamma_primitive == minor_primitive
                gamma_is_zero = not any(gamma)
                row = {
                    "m": m,
                    "n": n,
                    "D": D,
                    "rank": matrix.rank(),
                    "even_endpoint_nullity": even_nullity,
                    "odd_endpoint_nullity": odd_nullity,
                    "parity_defect": defect,
                    "gamma_is_zero": gamma_is_zero,
                    "gamma_degree": (
                        None
                        if gamma_is_zero
                        else max(k for k, value in enumerate(gamma) if value)
                    ),
                    "first_nonzero_gamma_index": (
                        None
                        if gamma_is_zero
                        else next(k for k, value in enumerate(gamma) if value)
                    ),
                    "gamma_equals_bordered_sums_up_to_scalar": True,
                    "primitive_gamma_sha256": hashlib.sha256(
                        json.dumps(gamma_primitive, separators=(",", ":")).encode()
                    ).hexdigest(),
                }
                rows.append(row)
                digest.update(
                    (
                        f"{m},{n},{D},{matrix.rank()},{even_nullity},"
                        f"{odd_nullity},{row['first_nonzero_gamma_index']},"
                        f"{row['gamma_degree']},{row['primitive_gamma_sha256']}\n"
                    ).encode()
                )

    counterexample = total_positivity_counterexample(mu)
    payload = {
        "schema": "root-unity-gamma-logistic-minor-certificate-v1",
        "exact_grid": {
            "m_range": [1, max_m],
            "n_range": [2, max_n],
            "D_rule": "2 <= D <= min(5,n)",
            "row_count": len(rows),
            "all_endpoint_ranks_D_minus_1": True,
            "all_predicted_parity_nullities": True,
            "all_beta_hat_maps_reverse_parity": True,
            "all_gamma_coefficients_equal_bordered_minor_sums_up_to_one_scalar": True,
            "all_top_cardinal_closed_forms_and_residues": True,
            "exact_row_digest_sha256": digest.hexdigest(),
        },
        "selected_rows": [
            row
            for row in rows
            if (row["m"], row["n"], row["D"])
            in {(1, 4, 4), (2, 4, 4), (3, 3, 2), (3, 5, 4), (4, 5, 5)}
        ],
        "strict_total_positivity_counterexample": counterexample,
        "logical_scope": {
            "exact": (
                "Every recorded rank, nullity, parity, Hermite-cardinal, residue, "
                "Gamma, determinant, and negative-minor assertion is exact over Q."
            ),
            "finite_grid": (
                "The grid replays the identities and examples.  It is not used "
                "as an all-parameter proof of Gamma nonvanishing."
            ),
            "analytic_companion": (
                "The companion source proves the all-parameter rank/parity theorem "
                "by the sech/csch bi-moment representation and Andreief identity."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["exact_grid"], indent=2, sort_keys=True))
    print(json.dumps(counterexample, indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
