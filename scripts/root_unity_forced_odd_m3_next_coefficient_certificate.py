#!/usr/bin/env python3
"""Exact replay for the all-D m=3 forced next-coefficient theorem.

The companion source contains the all-parameter proof.  This script checks,
over QQ and without floating point:

* the two endpoint block/selector factorizations of the special one-border
  coefficient matrix;
* the rationally scaled reverse-TP csch pairing kernel;
* total nonnegativity of finite composed augmented moment windows;
* the terminal-flag normalized-border inequality; and
* the corrected phases against the original rational Hermite-cardinal
  bordered determinants for every admissible tuple with n <= 10.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_forced_odd_m3_next_coefficient_certificate.json"
BASE_PATH = ROOT / "scripts" / "root_unity_gamma_top_cardinal_degree_certificate.py"
SPEC = importlib.util.spec_from_file_location("top_certificate", BASE_PATH)
assert SPEC and SPEC.loader
top = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(top)

X = top.X
x, U = sp.symbols("x U")


def endpoint_vector(matrix: sp.Matrix, D: int, parity: int) -> list[sp.Rational]:
    columns = [a for a in range(D + 1) if a % 2 == parity]
    submatrix = matrix.extract(range(matrix.rows), columns)
    vector = submatrix.nullspace()[0]
    vector = [sp.factor(value / vector[-1]) for value in vector]
    lifted = [sp.Rational(0)] * (D + 1)
    for column, value in zip(columns, vector):
        lifted[column] = value
    return lifted


def even_transform(poly: sp.Expr) -> sp.Expr:
    """Return q(x) for an even p(U) satisfying p(U)=q(-U^2)."""
    expanded = sp.Poly(sp.expand(poly), U, domain=sp.QQ)
    assert all(power[0] % 2 == 0 for power, value in expanded.terms() if value)
    return sp.expand(
        sum(value * (-x) ** (power[0] // 2) for power, value in expanded.terms())
    )


def scaled_kernel(j: int, v: int, h: int) -> sp.Rational:
    """Return pi^(2v)<x^j,Q_v>, a positive rational number."""
    p = (h + 1) // 2
    ell = p + j - v
    assert ell >= 1
    zeta_over_pi = (
        sp.Rational((-1) ** (ell + 1) * 2 ** (2 * ell - 1), sp.factorial(2 * ell))
        * sp.bernoulli(2 * ell)
    )
    value = (
        4
        * sp.factorial(2 * j + h)
        * (1 - sp.Rational(1, 2 ** (2 * ell)))
        * zeta_over_pi
    )
    value = sp.factor(value)
    assert value > 0
    return value


def laurent_coefficients(poly: sp.Expr) -> tuple[sp.Rational, sp.Poly]:
    """Split a Laurent polynomial with at most a simple pole at zero."""
    pole = sp.factor(sp.limit(x * poly, x, 0))
    regular = sp.cancel(poly - pole / x)
    assert sp.denom(regular) == 1
    return pole, sp.Poly(sp.expand(regular), x, domain=sp.QQ)


def pair_row(poly: sp.Expr, d: int, h: int) -> sp.Matrix:
    pole, regular = laurent_coefficients(poly)
    values = []
    for v in range(d + 1):
        value = pole * scaled_kernel(-1, v, h)
        if not regular.is_zero:
            value += sum(
                regular.nth(j) * scaled_kernel(j, v, h)
                for j in range(regular.degree() + 1)
            )
        values.append(sp.factor(value))
    return sp.Matrix([values])


def coefficient_matrix(rows: list[sp.Expr], low: int, high: int) -> sp.Matrix:
    out = []
    for row in rows:
        pole, regular = laurent_coefficients(row)
        out.append(
            [
                pole
                if j == -1
                else (regular.nth(j) if 0 <= j <= regular.degree() else 0)
                for j in range(low, high + 1)
            ]
        )
    return sp.Matrix(out)


def all_minor_signs(
    matrix: sp.Matrix, expected_sign_by_order: dict[int, int]
) -> dict[int, dict[str, int]]:
    counts: dict[int, dict[str, int]] = {}
    max_order = min(matrix.rows, matrix.cols)
    for order in range(1, max_order + 1):
        expected = expected_sign_by_order[order]
        zero = strict = 0
        for row_set in itertools.combinations(range(matrix.rows), order):
            for column_set in itertools.combinations(range(matrix.cols), order):
                determinant = sp.factor(matrix.extract(row_set, column_set).det())
                sign = int(sp.sign(determinant))
                assert sign in (0, expected), (
                    order,
                    row_set,
                    column_set,
                    determinant,
                )
                if sign:
                    strict += 1
                else:
                    zero += 1
        counts[order] = {"strict": strict, "zero": zero}
    return counts


def block_selector_check(h: int, block_count: int) -> dict:
    """Check both endpoint factorizations entry-by-entry."""
    alpha = lambda u: h + 1 + 2 * u
    beta = lambda u: 3 * h + 1 + 2 * u

    # c=0: first rectangular 1-by-2 block, then 2-by-2 blocks.
    row_count_minus = 1 + 2 * block_count
    local_count_minus = 2 + 2 * block_count
    Bminus = sp.zeros(row_count_minus, local_count_minus)
    Bminus[0, 0], Bminus[0, 1] = alpha(-1), beta(-1)
    row_cursor, column_cursor = 1, 2
    for u in range(block_count):
        Bminus[row_cursor, column_cursor] = 1
        Bminus[row_cursor, column_cursor + 1] = 1
        Bminus[row_cursor + 1, column_cursor] = alpha(u)
        Bminus[row_cursor + 1, column_cursor + 1] = beta(u)
        row_cursor += 2
        column_cursor += 2

    targets_minus = [-1, 0] + [target for u in range(block_count) for target in (u, u + 1)]
    global_minus = list(range(-1, block_count + 1))
    Sminus = sp.zeros(local_count_minus, len(global_minus))
    for local, target in enumerate(targets_minus):
        Sminus[local, global_minus.index(target)] = 1

    rows_minus = [x ** -1 * (alpha(-1) + beta(-1) * x)]
    for u in range(block_count):
        rows_minus.extend(
            [x**u * (1 + x), x**u * (alpha(u) + beta(u) * x)]
        )
    expected_minus = coefficient_matrix(rows_minus, -1, block_count)
    assert Bminus * Sminus == expected_minus

    # c=1/2 away from x^-1: leading scalar block, then 2-by-2 blocks.
    row_count_plus = 1 + 2 * block_count
    local_count_plus = 1 + 2 * block_count
    Bplus = sp.zeros(row_count_plus, local_count_plus)
    Bplus[0, 0] = 1
    row_cursor, column_cursor = 1, 1
    for u in range(block_count):
        Bplus[row_cursor, column_cursor] = 1
        Bplus[row_cursor, column_cursor + 1] = 1
        Bplus[row_cursor + 1, column_cursor] = alpha(u)
        Bplus[row_cursor + 1, column_cursor + 1] = beta(u)
        row_cursor += 2
        column_cursor += 2

    targets_plus = [0] + [target for u in range(block_count) for target in (u, u + 1)]
    global_plus = list(range(0, block_count + 1))
    Splus = sp.zeros(local_count_plus, len(global_plus))
    for local, target in enumerate(targets_plus):
        Splus[local, global_plus.index(target)] = 1

    rows_plus = [sp.Integer(1)]
    for u in range(block_count):
        rows_plus.extend(
            [x**u * (1 + x), x**u * (alpha(u) + beta(u) * x)]
        )
    expected_plus = coefficient_matrix(rows_plus, 0, block_count)
    assert Bplus * Splus == expected_plus

    # The finite factors themselves are TN.
    expected_tn_minus = {
        order: 1 for order in range(1, min(Bminus.rows, Bminus.cols) + 1)
    }
    expected_tn_plus = {
        order: 1 for order in range(1, min(Bplus.rows, Bplus.cols) + 1)
    }
    expected_selector_minus = {
        order: 1 for order in range(1, min(Sminus.rows, Sminus.cols) + 1)
    }
    expected_selector_plus = {
        order: 1 for order in range(1, min(Splus.rows, Splus.cols) + 1)
    }
    all_minor_signs(Bminus, expected_tn_minus)
    all_minor_signs(Bplus, expected_tn_plus)
    all_minor_signs(Sminus, expected_selector_minus)
    all_minor_signs(Splus, expected_selector_plus)

    return {
        "h": h,
        "block_count": block_count,
        "minus_shape": list(expected_minus.shape),
        "plus_shape": list(expected_plus.shape),
        "minus_factorization_exact": True,
        "plus_factorization_exact": True,
        "all_finite_factor_minors_nonnegative": True,
    }


def normalized_border(matrix: sp.Matrix, row: sp.Matrix, d: int) -> sp.Rational:
    numerator = matrix.col_join(row).det()
    denominator = matrix[:, :d].det()
    assert denominator != 0
    return sp.factor(numerator / denominator)


def moment_window(h: int, d: int) -> tuple[dict, dict[str, sp.Expr]]:
    n = h - 1
    V = sp.expand((1 + x) ** h)
    w0 = sp.Rational(1, sp.factorial(n))
    w1 = sp.Rational(1, sp.factorial(n) * 2**h)
    rho = w0 / x + 2 * w1 / (x + 1)
    euler = lambda poly: sp.cancel(2 * x * sp.diff(poly, x) + (h + 1) * poly)
    b = euler(sp.cancel(V * rho))
    gamma = sp.factor(2 * h * (w0 + sp.Rational(3 * h + 1, 2) * w1))
    psi = gamma / (x + 1)

    A_polys = [sp.expand(x**u * V) for u in range(d)]
    G_polys = [euler(poly) for poly in A_polys]
    A = sp.Matrix.vstack(*[pair_row(poly, d, h) for poly in A_polys])
    G = sp.Matrix.vstack(*[pair_row(poly, d, h) for poly in G_polys])
    b_row = pair_row(b, d, h)
    psi_row = pair_row(sp.cancel(V * psi), d, h)

    augmented_rows = [b]
    for A_poly, G_poly in zip(A_polys, G_polys):
        augmented_rows.extend([A_poly, G_poly])
    augmented = sp.Matrix.vstack(*[pair_row(poly, d, h) for poly in augmented_rows])
    reversed_augmented = augmented[:, list(range(d, -1, -1))]
    tn_counts = all_minor_signs(
        reversed_augmented,
        {order: 1 for order in range(1, d + 2)},
    )

    nb_A_b = normalized_border(A, b_row, d)
    nb_G_b = normalized_border(G, b_row, d)
    nb_A_psi = normalized_border(A, psi_row, d)
    bracket = sp.factor(nb_A_psi - nb_A_b + nb_G_b)
    assert nb_A_b <= nb_G_b
    assert nb_A_psi > 0 and bracket > 0

    # The coefficient-row convexity identity and endpoint reductions.
    c = sp.Rational(1, 2 ** (h - 1))
    S = (1 + x) ** (h - 2)
    rho_c = 1 / x + c / (x + 1)
    b_c = euler(sp.cancel(V * rho_c))
    b_zero = euler(V / x)
    b_half = euler(sp.cancel(V * (1 / x + sp.Rational(1, 2) / (x + 1))))
    assert sp.cancel(b_c - ((1 - 2 * c) * b_zero + 2 * c * b_half)) == 0
    assert sp.cancel(
        b_zero / S
        - (
            (h - 1) / x
            + (4 * h - 2)
            + (3 * h - 1) * x
        )
    ) == 0
    B_h = sp.Rational(9 * h - 3, 2)
    assert sp.cancel(b_half / S - ((h - 1) / x + B_h * (1 + x))) == 0

    record = {
        "h": h,
        "n": n,
        "d": d,
        "D": 2 * d + 1,
        "actual_c": str(c),
        "augmented_pairing_shape": list(augmented.shape),
        "reversed_augmented_all_minors_nonnegative": True,
        "reversed_augmented_minor_counts": tn_counts,
        "reported_border_normalization": (
            "Every reported border equals pi^(2d) times the NB in the source, "
            "because kernel column v was scaled by pi^(2v)."
        ),
        "pi_2d_times_NB_A_b": str(nb_A_b),
        "pi_2d_times_NB_G_b": str(nb_G_b),
        "NB_A_b_le_NB_G_b": True,
        "pi_2d_times_NB_A_Vpsi": str(nb_A_psi),
        "NB_A_Vpsi_strictly_positive": True,
        "pi_2d_times_corrected_bracket": str(bracket),
        "corrected_bracket_strictly_positive": True,
        "one_border_affine_identity_exact": True,
        "c_zero_reduction_exact": True,
        "c_half_reduction_exact": True,
    }
    objects = {
        "A": A,
        "G": G,
        "b_row": b_row,
        "psi_row": psi_row,
        "bracket": bracket,
        "psi": psi,
        "b": b,
    }
    return record, objects


def main() -> None:
    # Exact endpoint block/selector replays.
    factor_rows = [block_selector_check(h, 3) for h in (5, 7, 9, 11)]

    # Kernel signatures on rationally scaled finite windows.
    kernel_rows = []
    for h, d in ((5, 1), (7, 2), (9, 3), (11, 4)):
        max_j = h + d
        kernel = sp.Matrix(
            [
                [scaled_kernel(j, v, h) for v in range(d + 1)]
                for j in range(-1, max_j + 1)
            ]
        )
        signatures = {
            order: (-1) ** (order * (order - 1) // 2)
            for order in range(1, d + 2)
        }
        counts = all_minor_signs(kernel, signatures)
        kernel_rows.append(
            {
                "h": h,
                "d": d,
                "j_rule": f"-1 <= j <= {max_j}",
                "shape": list(kernel.shape),
                "all_minors_have_reverse_TP_signature": True,
                "minor_counts": counts,
            }
        )

    # Composed augmented moment windows and normalized flag ratios.
    moment_rows: list[dict] = []
    moment_objects: dict[tuple[int, int], dict[str, sp.Expr]] = {}
    for h in (5, 7, 9, 11):
        p = (h + 1) // 2
        for d in range(1, p - 1):
            record, objects = moment_window(h, d)
            moment_rows.append(record)
            moment_objects[(h, d)] = objects

    # Raw Hermite-cardinal phases and bordered determinants.
    raw_rows: list[dict] = []
    moments = top.logistic_moments(80)
    raw_digest = hashlib.sha256()
    for n in (4, 6, 8, 10):
        h = n + 1
        phi = sp.expand(sp.prod((X - j) ** h for j in range(3)))
        lambda_n = top.top_cardinal_polynomial(3, n, phi)
        lambda_previous = top.penultimate_cardinal_polynomial(3, n, phi)
        F = sp.expand(lambda_previous - sp.diff(lambda_n, X))
        centered_quotient = sp.cancel((F / phi).subs(X, 1 + U))
        numerator_u, denominator_u = sp.fraction(centered_quotient)
        psi_exact = sp.cancel(even_transform(numerator_u) / even_transform(denominator_u))

        for D in range(3, n, 2):
            d = (D - 1) // 2
            objects = moment_objects[(h, d)]
            assert sp.cancel(psi_exact - objects["psi"]) == 0

            matrix = top.centered_endpoint_matrix(3, n, D, phi, moments)
            even_endpoint = endpoint_vector(matrix, D, 0)
            odd_endpoint = endpoint_vector(matrix, D, 1)
            top_row = top.beta_row(lambda_n, D, moments)
            previous_row = top.beta_row(lambda_previous, D, moments)

            C_star = sp.Rational((-1) ** ((h + 1) // 2), 2)
            A = objects["A"]
            G = objects["G"]
            b_row = objects["b_row"]
            psi_row = objects["psi_row"]
            sigma_row = psi_row - b_row

            for u in range(d):
                for v in range(d + 1):
                    assert sp.factor(
                        matrix[2 * u, 2 * v]
                        - C_star * (-1) ** (u + v) * A[u, v]
                    ) == 0
                    assert sp.factor(
                        matrix[2 * u + 1, 2 * v + 1]
                        - C_star * (-1) ** (u + v) * G[u, v]
                    ) == 0

            for v in range(d + 1):
                # Corrected opposite signs of the two extra rows.
                assert sp.factor(
                    top_row[0, 2 * v + 1]
                    - C_star * (-1) ** v * b_row[0, v]
                ) == 0
                assert sp.factor(
                    previous_row[0, 2 * v]
                    + C_star * (-1) ** v * sigma_row[0, v]
                ) == 0

            raw_endpoint_value = sp.factor(
                sum(
                    odd_endpoint[a] * top_row[0, a]
                    - even_endpoint[a] * previous_row[0, a]
                    for a in range(D + 1)
                )
            )
            # objects["bracket"] is already pi^(2d) times the source bracket.
            predicted = sp.factor(C_star * (-1) ** d * objects["bracket"])
            assert raw_endpoint_value == predicted != 0

            first_border = top.bordered(matrix, D, previous_row, D)
            second_border = top.bordered(matrix, D - 1, top_row, D)
            bordered_sum = sp.factor(first_border + second_border)
            assert first_border * second_border < 0
            assert bordered_sum != 0
            pluecker_ratio = sp.factor(bordered_sum / raw_endpoint_value)
            assert pluecker_ratio != 0

            row = {
                "m": 3,
                "n": n,
                "D": D,
                "d": d,
                "corrected_even_odd_extra_row_signs_exact": True,
                "raw_endpoint_coefficient": str(raw_endpoint_value),
                "corrected_normalized_prediction": str(predicted),
                "raw_equals_corrected_prediction": True,
                "first_raw_bordered_minor": str(first_border),
                "second_raw_bordered_minor": str(second_border),
                "raw_bordered_minors_opposite_sign": True,
                "raw_bordered_sum": str(bordered_sum),
                "raw_bordered_sum_nonzero": True,
                "bordered_sum_to_normalized_endpoint_pluecker_ratio": str(pluecker_ratio),
            }
            raw_rows.append(row)
            raw_digest.update(
                (
                    f"3,{n},{D},{raw_endpoint_value},{first_border},"
                    f"{second_border},{bordered_sum},{pluecker_ratio}\n"
                ).encode()
            )

    payload = {
        "schema": "root-unity-forced-odd-m3-next-coefficient-certificate-v1",
        "theorem_scope": {
            "m": 3,
            "n": "even n >= 4",
            "D": "odd 3 <= D <= n",
            "all_parameter_claim": (
                "The source proves [z^(n+D-1)] Gamma != 0, and hence "
                "deg Delta=n+D-1, for every tuple in this scope."
            ),
            "no_claim_for_m_ge_5": True,
        },
        "block_selector_factorizations": {
            "all_entrywise_factorizations_exact": True,
            "all_finite_factor_minors_nonnegative": True,
            "rows": factor_rows,
        },
        "reverse_TP_kernel_windows": {
            "all_exact_over_QQ": True,
            "all_minors_have_signature_minus_one_choose_two": True,
            "rows": kernel_rows,
        },
        "augmented_moment_windows": {
            "all_exact_over_QQ": True,
            "all_reversed_augmented_matrices_TN": True,
            "all_terminal_flag_inequalities_hold": True,
            "all_corrected_brackets_strictly_positive": True,
            "rows": moment_rows,
        },
        "raw_cardinal_grid": {
            "m": 3,
            "n_rule": "even 4 <= n <= 10",
            "D_rule": "odd 3 <= D < n",
            "row_count": len(raw_rows),
            "all_corrected_phase_identities_exact": True,
            "all_raw_endpoint_values_match_normalized_prediction": True,
            "all_raw_bordered_sums_nonzero": True,
            "exact_row_digest_sha256": raw_digest.hexdigest(),
            "rows": raw_rows,
        },
        "logical_scope": {
            "proof_not_grid_extrapolation": True,
            "single_border_row_only": True,
            "full_triple_lace_not_claimed": True,
            "generic_positive_divisor_combination_not_claimed": True,
            "corrected_phase": (
                "For positive rho, R(it)=-it rho, V sigma=V psi-E(V rho), "
                "and the even/odd extra cardinal rows have opposite signs."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["theorem_scope"], indent=2, sort_keys=True))
    print(json.dumps(payload["raw_cardinal_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
