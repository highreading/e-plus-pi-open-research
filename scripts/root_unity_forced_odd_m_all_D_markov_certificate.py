#!/usr/bin/env python3
"""Exact replay for the all-D forced odd-frequency Markov theorem.

The universal proof is in the companion source.  This script uses exact
rational arithmetic to replay the two determinant lemmas, the interpolation
identity behind the external-node kernel, and a finite root-of-unity
normalization grid.  The finite grid is an audit, not the source of the
universal quantifiers.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_forced_odd_m_all_D_markov_certificate.json"
BASE_PATH = (
    ROOT / "scripts" / "root_unity_gamma_forced_odd_m_next_coefficient_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("forced_odd_audit", BASE_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)

x = audit.x


def qstr(value: sp.Expr) -> str:
    """Canonical exact string for a rational expression."""
    return str(sp.factor(value))


def digest_rationals(values: list[sp.Expr]) -> str:
    encoded = "\n".join(qstr(value) for value in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def vandermonde(values: list[sp.Rational]) -> sp.Rational:
    answer = sp.Rational(1)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            answer *= values[j] - values[i]
    return sp.factor(answer)


def mixed_moment_matrix(
    nodes: list[sp.Rational],
    z_nodes: list[sp.Rational],
    weights: list[sp.Rational],
    d: int,
) -> sp.Matrix:
    return sp.Matrix(
        [
            [
                sum(
                    weights[i] * nodes[i] ** u * z_nodes[i] ** v
                    for i in range(len(nodes))
                )
                for v in range(d)
            ]
            for u in range(d)
        ]
    )


def discrete_markov_replay() -> tuple[list[dict], list[sp.Expr]]:
    """Replay the J and external-node K determinant signs over QQ."""
    rows: list[dict] = []
    exact_values: list[sp.Expr] = []

    for d in range(1, 6):
        support = d + 3
        nodes = [sp.Rational(2 * i + 1, 3) for i in range(1, support + 1)]
        z_nodes = [sp.cancel(1 / (1 + node)) for node in nodes]
        mu0_weights = [sp.Rational((i + 1) ** 2, i + 2) for i in range(support)]
        g_nodes = [sp.Rational(i + 3, i + 1) for i in range(support)]
        mu_weights = [mu0_weights[i] * g_nodes[i] for i in range(support)]

        M0 = mixed_moment_matrix(nodes, z_nodes, mu0_weights, d)
        M = mixed_moment_matrix(nodes, z_nodes, mu_weights, d)
        epsilon = (-1) ** (d * (d - 1) // 2)
        assert sp.sign(M0.det()) == epsilon
        assert sp.sign(M.det()) == epsilon

        # Monic degree-d p(z), biorthogonal to 1,x,...,x^(d-1).
        top_extended = sp.Matrix(
            [
                [
                    sum(
                        mu0_weights[i] * nodes[i] ** u * z_nodes[i] ** v
                        for i in range(support)
                    )
                    for v in range(d + 1)
                ]
                for u in range(d)
            ]
        )
        lower = M0
        coefficients = -lower.inv() * top_extended[:, d]

        def p_at(z_value: sp.Rational) -> sp.Expr:
            return sp.factor(
                z_value**d + sum(coefficients[v] * z_value**v for v in range(d))
            )

        j_values: list[sp.Expr] = []
        for pole in (sp.Rational(1), sp.Rational(4), sp.Rational(9)):
            J = sp.factor(
                sum(
                    mu0_weights[i] * p_at(z_nodes[i]) / (nodes[i] + pole)
                    for i in range(support)
                )
            )
            bottom = sp.Matrix(
                [[
                    sum(
                        mu0_weights[i] * z_nodes[i] ** v / (nodes[i] + pole)
                        for i in range(support)
                    )
                    for v in range(d + 1)
                ]]
            )
            determinant_J = sp.factor(top_extended.col_join(bottom).det() / M0.det())
            assert determinant_J == J
            assert J > 0
            j_values.append(J)
            exact_values.append(J)

        k_values: list[sp.Expr] = []
        andreief_checks = 0
        for a, b in (
            (sp.Rational(0), sp.Rational(1)),
            (sp.Rational(1), sp.Rational(1)),
            (sp.Rational(4), sp.Rational(1)),
            (sp.Rational(1), sp.Rational(4)),
            (sp.Rational(9), sp.Rational(4)),
        ):
            v_xi = sp.Matrix([(-b) ** u for u in range(d)])
            ell = sp.Matrix(
                [[
                    sum(
                        mu_weights[i] * z_nodes[i] ** v / (nodes[i] + a)
                        for i in range(support)
                    )
                    for v in range(d)
                ]]
            )
            K = sp.factor((ell * M.inv() * v_xi)[0])
            block = M.row_join(v_xi).col_join(ell.row_join(sp.zeros(1, 1)))
            assert sp.factor(block.det() + M.det() * K) == 0
            assert K > 0

            # Generalized Andreief, summed over unordered support subsets.
            andreief_sum = sp.Rational(0)
            for subset in itertools.combinations(range(support), d):
                xs = [nodes[i] for i in subset]
                zs = [z_nodes[i] for i in subset]
                ws = [mu_weights[i] for i in subset]
                F_columns = [
                    [node**u for u in range(d)] + [sp.cancel(1 / (node + a))]
                    for node in xs
                ]
                G_column = [(-b) ** u for u in range(d)] + [sp.Rational(0)]
                first = sp.Matrix.hstack(
                    *(sp.Matrix(column) for column in F_columns), sp.Matrix(G_column)
                ).det()
                second = sp.Matrix(
                    [[zs[j] ** v for j in range(d)] for v in range(d)]
                ).det()

                interpolation = sp.interpolate(
                    [(xs[j], sp.cancel(1 / (xs[j] + a))) for j in range(d)], x
                )
                interpolation_value = sp.factor(interpolation.subs(x, -b))
                if a == b:
                    closed_value = sum(sp.cancel(1 / (a + node)) for node in xs)
                else:
                    closed_value = sp.factor(
                        (
                            1
                            - sp.prod(
                                (b + node) / (a + node) for node in xs
                            )
                        )
                        / (a - b)
                    )
                assert sp.factor(interpolation_value - closed_value) == 0
                assert interpolation_value > 0
                assert sp.factor(first + vandermonde(xs) * interpolation_value) == 0
                andreief_sum += first * second * sp.prod(ws)

            assert sp.factor(andreief_sum - block.det()) == 0
            andreief_checks += 1
            k_values.append(K)
            exact_values.append(K)

        rows.append(
            {
                "d": d,
                "support_size": support,
                "mixed_moment_sign": epsilon,
                "all_J_strictly_positive": True,
                "all_external_K_strictly_positive": True,
                "generalized_andreief_checks": andreief_checks,
                "J_digest_sha256": digest_rationals(j_values),
                "K_digest_sha256": digest_rationals(k_values),
            }
        )

    return rows, exact_values


def euler(poly: sp.Expr, h: int) -> sp.Expr:
    return sp.cancel(2 * x * sp.diff(poly, x) + (h + 1) * poly)


def root_unity_replay() -> tuple[list[dict], list[sp.Expr]]:
    """Exact Bernoulli-moment audit of every divisor on a finite grid."""
    rows: list[dict] = []
    values: list[sp.Expr] = []

    cases = [
        (3, 4, 3),
        (3, 6, 5),
        (3, 8, 7),
        (5, 4, 3),
        (5, 6, 5),
        (5, 8, 7),
        (7, 4, 3),
        (7, 6, 5),
    ]

    for m, n, D in cases:
        k = (m - 1) // 2
        h = n + 1
        d = (D - 1) // 2
        V = sp.expand(sp.prod((x + j * j) ** h for j in range(1, k + 1)))
        A_rows = [sp.expand(x**u * V) for u in range(d)]
        G_rows = [euler(row, h) for row in A_rows]

        pole_differences: list[sp.Expr] = []
        for a in [0] + [j * j for j in range(1, k + 1)]:
            W = sp.cancel(V / (x + a))
            border = euler(W, h)
            nb_A = audit.normalized_border(A_rows, border, d, h)
            nb_G = audit.normalized_border(G_rows, border, d, h)
            difference = sp.factor(nb_A - nb_G)
            assert difference < 0
            pole_differences.append(difference)
            values.append(difference)

        weights = {
            j: sp.Rational(
                1,
                sp.factorial(n)
                * (sp.factorial(k + j) * sp.factorial(k - j)) ** h,
            )
            for j in range(0, k + 1)
        }
        rho = weights[0] / x + sum(
            2 * weights[j] / (x + j * j) for j in range(1, k + 1)
        )
        aggregate_border = euler(sp.cancel(V * rho), h)
        aggregate_difference = sp.factor(
            audit.normalized_border(A_rows, aggregate_border, d, h)
            - audit.normalized_border(G_rows, aggregate_border, d, h)
        )
        reconstructed = sp.factor(
            weights[0] * pole_differences[0]
            + sum(2 * weights[j] * pole_differences[j] for j in range(1, k + 1))
        )
        assert aggregate_difference == reconstructed
        assert aggregate_difference < 0
        values.append(aggregate_difference)

        rows.append(
            {
                "m": m,
                "n": n,
                "D": D,
                "h": h,
                "pole_count_including_central": k + 1,
                "all_polewise_NB_A_minus_NB_G_strictly_negative": True,
                "aggregate_reconstruction_exact": True,
                "aggregate_NB_A_minus_NB_G": qstr(aggregate_difference),
                "pole_difference_digest_sha256": digest_rationals(pole_differences),
            }
        )

    return rows, values


def main() -> None:
    abstract_rows, abstract_values = discrete_markov_replay()
    root_rows, root_values = root_unity_replay()

    payload = {
        "schema": "root-unity-forced-odd-m-all-D-markov-certificate-v1",
        "abstract_external_node_replay": {
            "d_rule": "1 <= d <= 5",
            "row_count": len(abstract_rows),
            "all_mixed_moment_determinants_have_expected_sign": True,
            "all_divisor_Markov_transforms_J_strictly_positive": True,
            "all_external_node_Stieltjes_kernels_K_strictly_positive": True,
            "all_Schur_determinant_identities_exact": True,
            "all_generalized_Andreief_identities_exact": True,
            "all_interpolation_identities_exact": True,
            "exact_value_digest_sha256": digest_rationals(abstract_values),
        },
        "root_unity_normalization_replay": {
            "case_count": len(root_rows),
            "all_central_and_noncentral_pole_differences_strictly_negative": True,
            "all_positive_cardinal_aggregate_reconstructions_exact": True,
            "all_positive_cardinal_aggregate_differences_strictly_negative": True,
            "exact_value_digest_sha256": digest_rationals(root_values),
        },
        "abstract_rows": abstract_rows,
        "root_unity_rows": root_rows,
        "logical_scope": {
            "universal_source": (
                "The source proves the external-node Stieltjes-kernel lemma, "
                "the negative-node moment representation, and the polewise "
                "Euler-border inequality for all parameters in its scope."
            ),
            "finite_replay": (
                "The exact grids here audit determinant orientation, "
                "normalized-border normalization, pole signs, and rho "
                "linearity; they are not extrapolated."
            ),
            "arithmetic_limit": (
                "The theorem proves corrected endpoint nonvanishing and degree, "
                "not the primitive content or value/height inequality needed "
                "to decide the arithmetic nature of e+pi."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["abstract_external_node_replay"], indent=2, sort_keys=True))
    print(json.dumps(payload["root_unity_normalization_replay"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
