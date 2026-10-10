#!/usr/bin/env python3
"""Exact diagnostics for the sole forced odd-m next-coefficient case.

Rigorous all-parameter statements are proved in the companion source.  This
script replays over QQ:

* cancellation of the double and central poles in
  (Lambda_(n-1)-Lambda_n')/Phi;
* the exact positive simple-residue formula after x=-U^2;
* the endpoint decomposition of [z^(n+D-1)] Gamma; and
* the corrected positive-rho imaginary-axis phases and finite-grid signs for
  the still-open Euler-border inequality.

The last item is diagnostic only.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gamma_forced_odd_m_next_coefficient_certificate.json"
BASE_PATH = ROOT / "scripts" / "root_unity_gamma_top_cardinal_degree_certificate.py"
SPEC = importlib.util.spec_from_file_location("top_certificate", BASE_PATH)
assert SPEC and SPEC.loader
top = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(top)

X, U, x, z = top.X, top.U, top.x, sp.symbols("z")


def even_transform(poly: sp.Expr) -> sp.Expr:
    """For an even polynomial p(U), return q(x) with p(U)=q(-U^2)."""
    expanded = sp.Poly(sp.expand(poly), U, domain=sp.QQ)
    assert all(power[0] % 2 == 0 for power, value in expanded.terms() if value)
    return sp.expand(
        sum(value * (-x) ** (power[0] // 2) for power, value in expanded.terms())
    )


def apply_operator(coefficients: list[sp.Rational], poly: sp.Expr) -> sp.Expr:
    return sp.expand(
        sum(coefficients[a] * sp.diff(poly, X, a) for a in range(len(coefficients)))
    )


def parity_endpoint(
    matrix: sp.Matrix, D: int, parity: int
) -> list[sp.Rational]:
    columns = [a for a in range(D + 1) if a % 2 == parity]
    vector = matrix[:, columns].nullspace()[0]
    vector = [sp.cancel(value / vector[-1]) for value in vector]
    lifted = [sp.Rational(0)] * (D + 1)
    for index, column in enumerate(columns):
        lifted[column] = vector[index]
    return lifted


def rational_digest(values: list[sp.Rational]) -> str:
    encoded = ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in values).encode()
    return hashlib.sha256(encoded).hexdigest()


def odd_zeta_normalized(q: int) -> sp.Rational:
    """Return sum_{a>=1 odd} a^(-2q) / pi^(2q), exactly over QQ."""
    assert q >= 1
    zeta_normalized = (
        (-1) ** (q + 1)
        * sp.bernoulli(2 * q)
        * 2 ** (2 * q - 1)
        / sp.factorial(2 * q)
    )
    return sp.factor((1 - sp.Rational(1, 2) ** (2 * q)) * zeta_normalized)


def laurent_coefficients(poly: sp.Expr) -> dict[int, sp.Rational]:
    """Coefficient dictionary for the Laurent polynomials used below."""
    out: dict[int, sp.Rational] = {}
    for term in sp.expand(poly).as_ordered_terms():
        exponent = int(term.as_powers_dict().get(x, 0))
        coefficient = sp.cancel(term / x**exponent)
        out[exponent] = sp.cancel(out.get(exponent, 0) + coefficient)
    assert all(not value.has(x) for value in out.values())
    return out


def scaled_pair(poly: sp.Expr, v: int, h: int) -> sp.Rational:
    """Return pi^(2v)<poly,Q_v> by the exact odd-exponential expansion."""
    p = (h + 1) // 2
    answer = sp.Rational(0)
    for j, coefficient in laurent_coefficients(poly).items():
        q = p + j - v
        assert q >= 1
        kernel = 4 * sp.factorial(2 * j + h) * odd_zeta_normalized(q)
        answer += coefficient * kernel
    return sp.factor(answer)


def normalized_border(
    rows: list[sp.Expr], extra: sp.Expr, d: int, h: int
) -> sp.Rational:
    """The rationally scaled border pi^(2d) NB from the source note."""
    matrix = sp.Matrix(
        [[scaled_pair(row, v, h) for v in range(d + 1)] for row in rows]
    )
    extra_row = sp.Matrix([[scaled_pair(extra, v, h) for v in range(d + 1)]])
    coordinate = sp.zeros(1, d + 1)
    coordinate[0, d] = 1
    return sp.factor(
        matrix.col_join(extra_row).det() / matrix.col_join(coordinate).det()
    )


def main() -> None:
    residue_rows: list[dict] = []
    residue_digest = hashlib.sha256()

    for m in range(3, 12, 2):
        k = (m - 1) // 2
        for n in range(4, 11, 2):
            h = n + 1
            center = sp.Integer(k)
            P = sp.expand(sp.prod(X - j for j in range(m)))
            phi = sp.expand(P ** h)
            lambda_n = top.top_cardinal_polynomial(m, n, phi)
            lambda_previous = top.penultimate_cardinal_polynomial(m, n, phi)
            F = sp.expand(lambda_previous - sp.diff(lambda_n, X))
            quotient = sp.cancel(F / phi)

            # F is divisible by P^n, and the remaining quotient by P has no
            # central pole after centering.
            assert sp.rem(sp.Poly(F, X), sp.Poly(P**n, X)) == 0
            centered = sp.cancel(quotient.subs(X, center + U))
            numerator_u, denominator_u = sp.fraction(centered)
            psi = sp.cancel(even_transform(numerator_u) / even_transform(denominator_u))

            weights = [
                sp.Rational(
                    1,
                    sp.factorial(n)
                    * (sp.factorial(k + r) * sp.factorial(k - r)) ** h,
                )
                for r in range(-k, k + 1)
            ]
            coefficients = []
            for r in range(1, k + 1):
                wr = weights[r + k]
                harmonic = sp.harmonic(k + r) - sp.harmonic(k - r)
                regular = sum(
                    weights[s + k] / (r - s)
                    for s in range(-k, k + 1)
                    if s != r
                )
                paired = sum(
                    (weights[r - t + k] - weights[r + t + k]) / t
                    for t in range(1, k - r + 1)
                ) + sum(
                    weights[r - t + k] / t
                    for t in range(k - r + 1, k + r + 1)
                )
                assert sp.cancel(regular - paired) == 0
                assert regular > 0 and harmonic > 0
                coefficient = sp.factor(2 * r * h * (h * harmonic * wr + regular))
                assert coefficient > 0
                exact_residue = sp.factor(sp.limit((x + r * r) * psi, x, -r * r))
                assert exact_residue == coefficient
                coefficients.append(coefficient)

            reconstructed = sum(
                coefficients[r - 1] / (x + r * r) for r in range(1, k + 1)
            )
            assert sp.cancel(psi - reconstructed) == 0
            row = {
                "m": m,
                "n": n,
                "h": h,
                "rate_count": k,
                "all_regular_parts_strictly_positive": True,
                "all_stieltjes_residues_strictly_positive": True,
                "first_residue": str(coefficients[0]),
                "last_residue": str(coefficients[-1]),
                "residue_sha256": rational_digest(coefficients),
            }
            residue_rows.append(row)
            residue_digest.update(
                f"{m},{n},{rational_digest(coefficients)}\n".encode()
            )

    # Direct endpoint decomposition on the hard parity grid.
    determinant_rows: list[dict] = []
    max_m, max_n, max_D = 7, 8, 7
    moments = top.logistic_moments(max_m * (max_n + 1) + max_D + 5)
    for m in range(3, max_m + 1, 2):
        for n in range(4, max_n + 1, 2):
            P = sp.expand(sp.prod(X - j for j in range(m)))
            phi = sp.expand(P ** (n + 1))
            lambda_n = top.top_cardinal_polynomial(m, n, phi)
            lambda_previous = top.penultimate_cardinal_polynomial(m, n, phi)
            F = sp.expand(lambda_previous - sp.diff(lambda_n, X))
            for D in range(3, min(max_D, n - 1) + 1, 2):
                k = (m - 1) // 2
                h = n + 1
                d = (D - 1) // 2
                matrix = top.centered_endpoint_matrix(m, n, D, phi, moments)
                even = parity_endpoint(matrix, D, 0)
                odd = parity_endpoint(matrix, D, 1)
                assert even[D - 1] == odd[D] == 1
                remainder = [
                    odd[a] - (even[a - 1] if a >= 1 else 0)
                    for a in range(D + 1)
                ]

                beta_top_odd = -top.functional(
                    apply_operator(odd, lambda_n), moments
                )
                beta_previous_even = -top.functional(
                    apply_operator(even, lambda_previous), moments
                )
                next_coefficient = sp.factor(beta_top_odd - beta_previous_even)

                f_term = sp.factor(
                    top.functional(apply_operator(even, F), moments)
                )
                remainder_term = sp.factor(
                    top.functional(apply_operator(remainder, lambda_n), moments)
                )
                assert sp.factor(next_coefficient - (f_term - remainder_term)) == 0
                assert next_coefficient != 0
                assert f_term * remainder_term < 0
                assert sp.sign(next_coefficient) == sp.sign(f_term)

                # Independent common-column replay of the corrected phases.
                # The pairing is rationally scaled columnwise by pi^(2v).
                V = sp.expand(sp.prod((x + r * r) ** h for r in range(1, k + 1)))
                weights = {
                    r: sp.Rational(
                        1,
                        sp.factorial(n)
                        * (sp.factorial(k + r) * sp.factorial(k - r)) ** h,
                    )
                    for r in range(-k, k + 1)
                }
                rho = weights[0] / x + sum(
                    2 * weights[r] / (x + r * r) for r in range(1, k + 1)
                )
                psi_coefficients = []
                for r in range(1, k + 1):
                    harmonic = sp.harmonic(k + r) - sp.harmonic(k - r)
                    regular = sum(
                        weights[s] / (r - s)
                        for s in range(-k, k + 1)
                        if s != r
                    )
                    psi_coefficients.append(
                        sp.factor(
                            2
                            * r
                            * h
                            * (h * harmonic * weights[r] + regular)
                        )
                    )
                psi = sum(
                    psi_coefficients[r - 1] / (x + r * r)
                    for r in range(1, k + 1)
                )
                V_rho = sp.cancel(V * rho)
                V_psi = sp.cancel(V * psi)
                euler_rho = sp.cancel(
                    2 * x * sp.diff(V_rho, x) + (h + 1) * V_rho
                )
                V_sigma = sp.cancel(V_psi - euler_rho)

                # Verify the corrected imaginary-axis phase and the sigma
                # row directly against the cardinal polynomials.  These are
                # rational identities in U after x=-U^2, so no numerical
                # branch choice for sqrt(x) is involved.
                if D == 3:
                    centered_top = sp.cancel(
                        (lambda_n / phi).subs(X, k + U)
                    )
                    centered_top_derivative = sp.cancel(
                        (sp.diff(lambda_n, X) / phi).subs(X, k + U)
                    )
                    centered_previous = sp.cancel(
                        (lambda_previous / phi).subs(X, k + U)
                    )
                    assert sp.cancel(
                        centered_top + U * rho.subs(x, -U**2)
                    ) == 0
                    assert sp.cancel(
                        centered_top_derivative
                        + (euler_rho / V).subs(x, -U**2)
                    ) == 0
                    assert sp.cancel(
                        centered_previous - (V_sigma / V).subs(x, -U**2)
                    ) == 0

                A_rows = [sp.expand(x**u * V) for u in range(d)]
                G_rows = [
                    sp.expand(2 * x * sp.diff(row, x) + (h + 1) * row)
                    for row in A_rows
                ]
                nb_psi = normalized_border(A_rows, V_psi, d, h)
                nb_A_euler = normalized_border(A_rows, euler_rho, d, h)
                nb_G_euler = normalized_border(G_rows, euler_rho, d, h)
                nb_sigma = normalized_border(A_rows, V_sigma, d, h)
                assert sp.factor(nb_sigma - (nb_psi - nb_A_euler)) == 0
                assert nb_psi > 0
                assert nb_A_euler < nb_G_euler

                C_star = sp.Rational(1, 2) * (-1) ** (
                    k + k * h + (h + 1) // 2
                )
                alpha_scaled = (-1) ** d * C_star
                assert sp.factor(f_term - alpha_scaled * nb_psi) == 0
                assert sp.factor(
                    remainder_term
                    - alpha_scaled * (nb_A_euler - nb_G_euler)
                ) == 0

                even_rows = list(range(0, D - 1, 2))
                odd_rows = list(range(1, D - 1, 2))
                even_columns = list(range(0, D + 1, 2))
                odd_columns = list(range(1, D + 1, 2))
                parity_coordinate = sp.zeros(1, d + 1)
                parity_coordinate[0, d] = 1
                K_even = matrix.extract(even_rows, even_columns)
                K_odd = matrix.extract(odd_rows, odd_columns)
                E_previous = top.beta_row(lambda_previous, D, moments)
                E_top = top.beta_row(lambda_n, D, moments)
                even_ratio = sp.factor(
                    K_even.col_join(E_previous[:, even_columns]).det()
                    / K_even.col_join(parity_coordinate).det()
                )
                odd_ratio = sp.factor(
                    K_odd.col_join(E_top[:, odd_columns]).det()
                    / K_odd.col_join(parity_coordinate).det()
                )
                assert sp.factor(
                    even_ratio - (-1) ** (d + 1) * C_star * nb_sigma
                ) == 0
                assert sp.factor(
                    odd_ratio - (-1) ** d * C_star * nb_G_euler
                ) == 0

                nonzero_remainder = [value for value in remainder if value]
                assert nonzero_remainder and all(value < 0 for value in nonzero_remainder)

                first_border = top.bordered(
                    matrix, D, top.beta_row(lambda_previous, D, moments), D
                )
                second_border = top.bordered(
                    matrix, D - 1, top.beta_row(lambda_n, D, moments), D
                )
                assert first_border * second_border < 0
                ratio = sp.factor(abs(first_border / second_border))
                assert 0 < ratio < 1

                determinant_rows.append(
                    {
                        "m": m,
                        "n": n,
                        "D": D,
                        "opposite_border_signs": True,
                        "absolute_first_to_second_ratio": str(ratio),
                        "ratio_strictly_between_zero_and_one": True,
                        "endpoint_remainder_coefficients_all_negative": True,
                        "F_and_remainder_terms_opposite_sign": True,
                        "target_has_F_term_sign": True,
                        "next_coefficient_nonzero": True,
                        "corrected_positive_rho_phase_verified": True,
                        "corrected_sigma_identity_verified": True,
                        "even_odd_border_prefactors_opposite": True,
                        "NB_A_psi_positive": True,
                        "NB_A_euler_strictly_below_NB_G_euler": True,
                    }
                )

    payload = {
        "schema": "root-unity-gamma-forced-odd-m-next-coefficient-certificate-v1",
        "stieltjes_grid": {
            "m_rule": "odd 3 <= m <= 11",
            "n_rule": "even 4 <= n <= 10",
            "row_count": len(residue_rows),
            "all_double_and_central_poles_cancel": True,
            "all_regular_parts_strictly_positive": True,
            "all_simple_residues_strictly_positive": True,
            "all_partial_fraction_reconstructions_exact": True,
            "exact_row_digest_sha256": residue_digest.hexdigest(),
        },
        "hard_parity_determinant_grid": {
            "m_rule": f"odd 3 <= m <= {max_m}",
            "n_rule": f"even 4 <= n <= {max_n}",
            "D_rule": f"odd 3 <= D <= min({max_D},n-1)",
            "row_count": len(determinant_rows),
            "all_endpoint_decompositions_exact": True,
            "all_border_summands_opposite_sign": True,
            "all_absolute_ratios_strictly_below_one": True,
            "all_endpoint_remainder_coefficients_negative": True,
            "all_F_and_remainder_terms_opposite_sign": True,
            "all_targets_have_F_term_sign": True,
            "all_corrected_positive_rho_phases_verified": True,
            "all_corrected_sigma_identities_verified": True,
            "all_even_odd_border_prefactors_opposite": True,
            "all_NB_A_psi_positive": True,
            "all_NB_A_euler_strictly_below_NB_G_euler": True,
        },
        "selected_stieltjes_rows": [
            row
            for row in residue_rows
            if (row["m"], row["n"]) in {(3, 4), (5, 6), (7, 8), (11, 10)}
        ],
        "selected_determinant_rows": [
            row
            for row in determinant_rows
            if (row["m"], row["n"], row["D"])
            in {(3, 4, 3), (3, 8, 7), (5, 6, 5), (7, 8, 7)}
        ],
        "logical_scope": {
            "all_parameter_theorem": (
                "The source proves the positive simple-pole/Stieltjes formula "
                "for (Lambda_(n-1)-Lambda_n')/Phi for every odd m and even n."
            ),
            "exact_identities": (
                "The endpoint and Euler-operator decompositions are algebraic "
                "identities for every m odd, n even, D odd in range n>=D."
            ),
            "open_part": (
                "The strict inequality NB_A(E(V*rho)) < NB_G(E(V*rho)), the "
                "raw bordered-sign comparison, and the observed sign of the "
                "coefficients of D_odd-z*C_even are verified only on the "
                "recorded grid.  The weak normalized-border inequality, which "
                "is sufficient for the theorem, remains unproved in general."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["stieltjes_grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["hard_parity_determinant_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
