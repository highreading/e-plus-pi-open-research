#!/usr/bin/env python3
"""Exact replay for the certified-coefficient corrected-content cap.

The companion source proves the all-parameter statements.  This finite
certificate works over QQ/ZZ and checks:

* saturated complementary-minor orientation;
* every augmented determinant identity B_(a,b);
* the pure-cardinal high-tail formula;
* the even-frequency certified constant coordinate;
* the certified gcd content cap and primitive-height lower bound; and
* invariance under the universal interpolation clearing.

No floating-point endpoint values are used.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import resource
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_certified_coefficient_content_cap_certificate.json"
BASE_PATH = ROOT / "scripts" / "root_unity_corrected_exterior_primitive_height_certificate.py"
SPEC = importlib.util.spec_from_file_location("primitive_height", BASE_PATH)
assert SPEC and SPEC.loader
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)
logistic = base.logistic


def gcd_values(values: list[int]) -> int:
    answer = 0
    for value in values:
        answer = math.gcd(answer, abs(int(value)))
    return answer


def endpoint_row(m: int, n: int, D: int) -> dict:
    M = m * (n + 1)
    moments = logistic.logistic_moments(M + D + 4)
    K = logistic.endpoint_matrix(m, n, D, moments, centered=False)
    assert K.rank() == D - 1

    basis = sp.Matrix.hstack(*K.nullspace())
    pairs, pluecker, _ = base.saturated_pluecker(basis)

    scale_K = 2 ** (M + D - 1)
    A_K = K * scale_K
    assert all(value.q == 1 for value in A_K)

    complementary = []
    for a, b in pairs:
        columns = [j for j in range(D + 1) if j not in (a, b)]
        complementary.append(abs(int(A_K[:, columns].det())))
    delta_K = gcd_values(complementary)
    assert delta_K > 0

    lambdas = logistic.hermite_cardinal_polynomials(m, n)
    E = logistic.beta_rows(lambdas, D, moments)
    q_E = math.lcm(*(int(sp.denom(value)) for value in E))
    E_star = E * q_E
    assert all(value.q == 1 for value in E_star)

    def make_lookup(vector: list[int]) -> dict[tuple[int, int], int]:
        return dict(zip(pairs, vector))

    def anti(lookup: dict[tuple[int, int], int], a: int, j: int) -> int:
        return base.antisymmetric_coordinate(lookup, a, j)

    def augmented(a: int, b: int) -> int:
        coordinate = sp.zeros(1, D + 1)
        coordinate[0, a] = 1
        return int(A_K.col_join(coordinate).col_join(E_star[b, :]).det())

    # Orient p so B_(a,b)=delta_K*sum_j E*_(b,j)p_(a,j).
    lookup = make_lookup(pluecker)
    orientation = None
    for a in range(D + 1):
        for b in range(n + 1):
            contraction = sum(
                int(E_star[b, j]) * anti(lookup, a, j)
                for j in range(D + 1)
            )
            determinant = augmented(a, b)
            if contraction:
                ratio = sp.Rational(determinant, delta_K * contraction)
                assert ratio in (-1, 1)
                orientation = int(ratio)
                break
            assert determinant == 0
        if orientation is not None:
            break
    assert orientation is not None
    if orientation == -1:
        pluecker = [-value for value in pluecker]
        lookup = make_lookup(pluecker)

    augmented_values: dict[tuple[int, int], int] = {}
    augmented_digest = hashlib.sha256()
    for a in range(D + 1):
        for b in range(n + 1):
            determinant = augmented(a, b)
            contraction = sum(
                int(E_star[b, j]) * anti(lookup, a, j)
                for j in range(D + 1)
            )
            assert determinant == delta_K * contraction
            augmented_values[a, b] = determinant
            augmented_digest.update(f"{a},{b},{determinant}\n".encode())

    w = base.wronskian_coefficients(pairs, pluecker, n, D)
    gamma = base.gamma_coefficients(pairs, pluecker, E, n, D)
    delta = [sp.Rational(wi) - gi for wi, gi in zip(w, gamma)]

    q_E_map, A_delta = base.corrected_integer_map(E, n, D)
    assert q_E_map == q_E
    N = A_delta * sp.Matrix(pluecker)
    assert all(N[ell] == q_E * delta[ell] for ell in range(n + D + 1))
    N_int = [int(value) for value in N]
    assert any(N_int)

    # Every coefficient strictly above the Wronskian range is a saturated
    # augmented-cardinal determinant quotient.
    high_start = 2 * D - 1
    high_formula = []
    for ell in range(high_start, n + D + 1):
        determinant_sum = sum(
            augmented_values[a, ell - a]
            for a in range(D + 1)
            if 0 <= ell - a <= n
        )
        assert determinant_sum % delta_K == 0
        predicted = -(determinant_sum // delta_K)
        assert N_int[ell] == predicted
        high_formula.append(predicted)

    constant_formula = (
        q_E * anti(lookup, 0, 1) - augmented_values[0, 0] // delta_K
    )
    assert N_int[0] == constant_formula

    forced_top = (
        (n % 2 == 0 and D % 2 == 1)
        or (m % 2 == 0 and n % 2 == 1 and D % 2 == 0)
    )
    actual_degree = max(index for index, value in enumerate(N_int) if value)
    degree_theorem_kind: str
    certified_nonzero_index: int
    if not forced_top:
        assert actual_degree == n + D
        assert N_int[n + D] != 0
        degree_theorem_kind = "parity-allowed top-cardinal"
        certified_nonzero_index = n + D
    elif m % 2 == 1:
        assert n % 2 == 0 and D % 2 == 1
        assert actual_degree == n + D - 1
        assert N_int[n + D - 1] != 0
        degree_theorem_kind = "forced odd-frequency next-cardinal"
        certified_nonzero_index = n + D - 1
    else:
        # No high-degree theorem is claimed here in an even-frequency forced
        # case.  The corrected constant-border theorem is the certificate.
        assert N_int[0] != 0
        degree_theorem_kind = "even-frequency corrected constant border"
        certified_nonzero_index = 0

    selected = high_formula.copy()
    if m % 2 == 0:
        selected.insert(0, N_int[0])
    G_cert = gcd_values(selected)
    assert G_cert > 0

    content_E = gcd_values(N_int)
    assert content_E > 0 and G_cert % content_E == 0
    height_N = max(abs(value) for value in N_int)
    primitive = [value // content_E for value in N_int]
    primitive_height = max(abs(value) for value in primitive)
    assert primitive_height * content_E == height_N
    lower_bound = sp.Rational(height_N, G_cert)
    assert sp.Rational(primitive_height) >= lower_bound

    high_gcd = gcd_values(high_formula)
    leading_abs = abs(N_int[actual_degree])

    V = base.interpolation_determinant(m, n)
    Q = (2**M) * V
    assert Q % q_E == 0
    clearing_scale = Q // q_E
    content_Q = clearing_scale * content_E
    G_Q = clearing_scale * G_cert
    height_N_Q = clearing_scale * height_N
    assert G_Q % content_Q == 0
    assert sp.Rational(height_N_Q, G_Q) == lower_bound

    record_digest = hashlib.sha256()
    for vector in (pluecker, N_int):
        record_digest.update(",".join(str(value) for value in vector).encode())
        record_digest.update(b"\n")
    record_digest.update(augmented_digest.hexdigest().encode())

    return {
        "m": m,
        "n": n,
        "D": D,
        "M": M,
        "endpoint_rank": int(K.rank()),
        "A_K_integer_scale": scale_K,
        "delta_K": delta_K,
        "primitive_pluecker_gcd": gcd_values(pluecker),
        "primitive_pluecker_height": max(abs(value) for value in pluecker),
        "q_E": q_E,
        "all_augmented_determinant_identities_exact": True,
        "augmented_determinant_digest_sha256": augmented_digest.hexdigest(),
        "pure_cardinal_high_start": high_start,
        "pure_cardinal_high_coefficients_ascending": high_formula,
        "all_high_determinant_quotient_formulas_exact": True,
        "constant_coordinate_formula_exact": True,
        "forced_top_parity": forced_top,
        "degree_theorem_kind": degree_theorem_kind,
        "certified_nonzero_index": certified_nonzero_index,
        "certified_nonzero_coordinate": N_int[certified_nonzero_index],
        "actual_degree_on_exact_row": actual_degree,
        "globally_cleared_content_c_E": content_E,
        "globally_cleared_height_H_N": height_N,
        "absolute_leading_coordinate": leading_abs,
        "high_tail_gcd": high_gcd,
        "certified_gcd_G_cert": G_cert,
        "content_divides_certified_gcd": True,
        "certified_gcd_over_true_content": G_cert // content_E,
        "single_leading_cap_over_true_content": leading_abs // content_E,
        "primitive_height": primitive_height,
        "primitive_height_lower_bound_H_N_over_G_cert": str(lower_bound),
        "primitive_height_lower_bound_verified": True,
        "universal_Q": Q,
        "Q_over_q_E": clearing_scale,
        "universal_clearing_content_c_Q": content_Q,
        "universal_clearing_certified_cap_G_Q": G_Q,
        "universal_clearing_height_H_N_Q": height_N_Q,
        "clearing_invariant_height_lower_bound": True,
        "record_sha256": record_digest.hexdigest(),
    }


def main() -> None:
    tuples = [
        (2, 3, 2),  # even-frequency forced top; constant certificate
        (2, 4, 3),  # even-frequency forced top; constant certificate
        (2, 4, 4),  # parity-allowed top
        (3, 3, 2),  # parity-allowed top
        (3, 4, 3),  # forced odd-frequency next coefficient
        (3, 5, 4),  # parity-allowed top
        (4, 5, 4),  # even-frequency forced top; constant certificate
        (4, 6, 4),  # parity-allowed top
        (5, 4, 3),  # forced odd-frequency next coefficient
    ]
    rows = [endpoint_row(*parameters) for parameters in tuples]

    digest = hashlib.sha256()
    for row in rows:
        digest.update((row["record_sha256"] + "\n").encode())

    strict_cap_rows = [
        row for row in rows
        if row["certified_gcd_over_true_content"] > 1
    ]
    leading_loose_rows = [
        row for row in rows
        if row["single_leading_cap_over_true_content"]
        > row["certified_gcd_over_true_content"]
    ]
    assert strict_cap_rows
    assert leading_loose_rows

    payload = {
        "schema": "root-unity-certified-coefficient-content-cap-v1",
        "theorem_scope": {
            "m": "m >= 2",
            "n_D": "n >= D >= 2",
            "all_parameter_claim": (
                "The source proves c_E divides G_cert and "
                "H(P_Delta) >= H(q_E Delta)/G_cert, with a certified "
                "nonzero coordinate in every tuple in scope."
            ),
            "rank_deficient_ambient_map_allowed": True,
            "no_transcendence_claim": True,
        },
        "exact_rows": rows,
        "row_count": len(rows),
        "exact_grid_digest_sha256": digest.hexdigest(),
        "summary": {
            "all_augmented_determinant_identities_exact": all(
                row["all_augmented_determinant_identities_exact"] for row in rows
            ),
            "all_content_caps_verified": all(
                row["content_divides_certified_gcd"] for row in rows
            ),
            "all_height_lower_bounds_verified": all(
                row["primitive_height_lower_bound_verified"] for row in rows
            ),
            "all_clearing_invariance_checks_verified": all(
                row["clearing_invariant_height_lower_bound"] for row in rows
            ),
            "rows_where_certified_cap_strictly_exceeds_true_content": len(
                strict_cap_rows
            ),
            "rows_where_multi_coordinate_cap_improves_leading_cap": len(
                leading_loose_rows
            ),
        },
        "logical_scope": {
            "finite_grid_is_replay_only": True,
            "certified_cap_is_not_exact_content_in_general": True,
            "threshold_test_is_necessary_not_sufficient": True,
            "no_unproved_even_frequency_next_coefficient_used": True,
        },
        "versions": {"sympy": sp.__version__},
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": payload["schema"],
        "row_count": payload["row_count"],
        "digest": payload["exact_grid_digest_sha256"],
        "summary": payload["summary"],
        "peak_rss_MiB": round(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 3
        ),
    }, indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
