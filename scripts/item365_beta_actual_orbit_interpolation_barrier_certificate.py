#!/usr/bin/env python3
"""Exact deterministic replay for Item 365.

Checks the endpoint load-coordinate unit, canonical-box interpolation bounds,
half-window rank, and fixed-n orbit collapse.  Declared controls are not
actual Item-316 targets and no prime or target census is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "sources/item333_beta_nonlinear_state_saturation_no_go_report.md": (
        "8f4bc0a6f93cbd4882392ade311d68e25be1ceb282db71cc5e1ef2f70aee75d6"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_certificate.json": (
        "933120c05e0f67663608e9e53354407f4593718c149941942d070f4af3c0a76a"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_root_audit.json": (
        "6ddd4949f5d7f91fdc160634da06079661ebf373ac0f061495a7b41135924ecc"
    ),
    "manifests/item333_beta_nonlinear_state_saturation_no_go_manifest.json": (
        "a1f55058846bdee5f33848f45af06fed8659f8c3402e4af6896540bf468aae77"
    ),
    "sources/item346_beta_t_avoiding_radical_localization_report.md": (
        "2ad742c14d0adbc74da6c46394ed89f68cec8888a3c9d22ee4f230a4e16548a5"
    ),
    "scripts/item346_beta_t_avoiding_radical_localization_certificate.py": (
        "76c020b07d199a7283d7373a3ef677643d3be01adfe7480628f92ccdad7498c0"
    ),
    "results/item346_beta_t_avoiding_radical_localization_certificate.json": (
        "29a20d6ede62db23658d66db8e57af4a2982c9b66fd12d104f0070b3280aefab"
    ),
    "results/item346_beta_t_avoiding_radical_localization_root_audit.json": (
        "c9273d7e187ee2c9b4b91bffc65769f1a29f937613c36960e4ed5871c5782089"
    ),
    "manifests/item346_beta_t_avoiding_radical_localization_manifest.json": (
        "5029cf3483fdf6cce4bbc0d454bca362bb2796104ca36b353d0161e374915530"
    ),
    "sources/item350_beta_mesoscopic_first_hit_crt_no_go_report.md": (
        "a028d87765b16bf921a219e43314c8020b635e052cf3a653a9213389d81ce532"
    ),
    "scripts/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.py": (
        "ae4be8e7e4675a30efe01cc1e7e40d57e63bd49590c34aaf9f8c97996038073f"
    ),
    "results/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.json": (
        "9c30d1c23b741e0e5b7e38ab39b16658f225f9846894b8a2b657bfa4eb145950"
    ),
    "results/item350_beta_mesoscopic_first_hit_crt_no_go_root_audit.json": (
        "e965a5131ebc4ff9a54b7ae8369b2855e562ebfa9190517817b7d2fd2af7e162"
    ),
    "manifests/item350_beta_mesoscopic_first_hit_crt_no_go_manifest.json": (
        "19e6e4ab0dfe99b7e6587e66006caa99bd39c368c574fec69762d1aee5cc3b21"
    ),
    "sources/item358_beta_actual_low_incidence_saturation_barrier_report.md": (
        "681c9f9cbe926978c78f632084c8be83439c2ac3f5e50f2c2697a49f2f0da68d"
    ),
    "scripts/item358_beta_actual_low_incidence_saturation_barrier_certificate.py": (
        "c997c7f3739fe5dc98ee2e48c3ebfd1a67e74289e175d52bc8d5adfb1f9565bf"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_certificate.json": (
        "4da88e55dec36f3c130def549007c8ae1509ff0a029dfed9ff25f67a78c2ffa3"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_root_audit.json": (
        "a1a48f7d7080834ebf3be56b47d8056733e88e1913e8f6ea784f97a5eb2d9172"
    ),
    "manifests/item358_beta_actual_low_incidence_saturation_barrier_manifest.json": (
        "4ba799fe2fc8cb6063034d844f91bcaec6c3fc84d043b1f46c675fce400acfb1"
    ),
    "sources/item362_beta_finite_field_singleton_indicator_barrier_report.md": (
        "cf3727b7349d4ae0355aba4f83fe19f7bd56374897224e686352d8d78e9e001b"
    ),
    "scripts/item362_beta_finite_field_singleton_indicator_barrier_certificate.py": (
        "8d1d09cad7224db2c6ec275e67532f156eb7b77ef7c57a0596cc39762473c61f"
    ),
    "results/item362_beta_finite_field_singleton_indicator_barrier_certificate.json": (
        "6489c8b8c00fad33247455f5aa82a41bb4cebaf4c8f26b7439c858d8d7de877e"
    ),
    "results/item362_beta_finite_field_singleton_indicator_barrier_root_audit.json": (
        "2f36a061d77a8804d34e1425bc18b00bab3778fc17615af605a6ecaffe765f7a"
    ),
    "manifests/item362_beta_finite_field_singleton_indicator_barrier_manifest.json": (
        "d88fc5cf94217a4c453b69f802d92bda6d03e83c1ec7ad046762addb007788f8"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    root = Path(__file__).resolve().parent.parent
    rows = []
    for relative_path, expected in DEPENDENCY_HASHES.items():
        payload = (root / relative_path).read_bytes()
        actual = hashlib.sha256(payload).hexdigest()
        assert actual == expected, (relative_path, actual, expected)
        rows.append(
            {"path": relative_path, "bytes": len(payload), "sha256": actual}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def q_sequence(n: int) -> list[int]:
    assert n >= 2
    values = [1, 1]
    for index in range(2, n + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def continuant(entries: list[int]) -> int:
    previous_previous = 1
    previous = 1
    for index, entry in enumerate(entries):
        if index == 0:
            current = entry
        else:
            current = entry * previous + previous_previous
        previous_previous, previous = previous, current
    return 1 if not entries else previous


def word_data(n: int) -> dict[str, Any]:
    assert n >= 5
    m = n - 2
    A = 4 * n - 2
    weights = [None] + [7] + [4 * index + 2 for index in range(2, m + 1)]
    q_values = q_sequence(n)
    a = q_values[n - 1]
    b = q_values[n]
    c = q_values[n - 2]

    Q_previous_previous = 0
    Q_previous = 1
    P_previous_previous = 1
    P_previous = 0
    Q_values = [1]
    for index in range(1, m + 1):
        Q_current = weights[index] * Q_previous + Q_previous_previous
        P_current = weights[index] * P_previous + P_previous_previous
        Q_previous_previous, Q_previous = Q_previous, Q_current
        P_previous_previous, P_previous = P_previous, P_current
        Q_values.append(Q_current)
    assert Q_previous == a
    S = P_previous
    hat_delta_0 = continuant(weights[2:] + [A])
    assert a * hat_delta_0 == b * S + (-1) ** n
    assert math.gcd(hat_delta_0, b) == 1
    assert b == A * a + c

    box_degree = 6 + sum(weights[2:])
    assert box_degree == 2 * m * m + 4 * m
    box_rank = 7 * math.prod(weight + 1 for weight in weights[2:])
    lower = (a + 2 * c - 1) // (2 * c)
    upper = (a - 1) // 2
    window_rank = upper - lower + 1
    assert window_rank == (a + 1) // 2 - lower
    assert 0 < window_rank < a

    return {
        "n": n,
        "m": m,
        "capital_A": A,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "S": str(S),
        "hat_delta_0": str(hat_delta_0),
        "bridge_residual": a * hat_delta_0 - b * S,
        "gcd_hat_delta_0_b": math.gcd(hat_delta_0, b),
        "box_degree": box_degree,
        "box_rank": str(box_rank),
        "window_lower_R": lower,
        "window_upper_R": str(upper),
        "window_rank": str(window_rank),
        "log_window_over_log_b": math.log(window_rank) / math.log(b),
        "actual_orbit_rank_upper": 1,
    }


def evaluate_endpoint(
    n: int, modulus: int, d1: int, d2: int, loads: list[int]
) -> int:
    m = n - 2
    A = 4 * n - 2
    weights = [None] + [7] + [4 * index + 2 for index in range(2, m + 1)]
    assert len(loads) == m - 2
    digits = [0, d1 % modulus, d2 % modulus]
    for index, load in enumerate(loads, start=3):
        digits.append((weights[index] * digits[index - 1] - load) % modulus)
    digits.append(0)
    E_previous_previous = 0
    E_previous = digits[1]
    for index in range(1, m + 1):
        next_weight = A if index + 1 == m + 1 else weights[index + 1]
        E_current = (
            next_weight * E_previous
            + E_previous_previous
            + (-1) ** index * digits[index + 1]
        ) % modulus
        E_previous_previous, E_previous = E_previous, E_current
    return E_previous


def endpoint_coordinate_controls() -> dict[str, Any]:
    rows = []
    for n in [5, 6, 7, 8]:
        data = word_data(n)
        b = int(data["b"])
        a = int(data["a"])
        hat = int(data["hat_delta_0"])
        m = n - 2
        modulus = b * b
        d2 = 3 * n + 1
        loads = [((index + 2) * (n + 3) + 1) % modulus for index in range(m - 2)]
        endpoint_at_zero = evaluate_endpoint(n, modulus, 0, d2, loads)
        d1 = ((a - endpoint_at_zero) * pow(hat, -1, modulus)) % modulus
        endpoint = evaluate_endpoint(n, modulus, d1, d2, loads)
        assert endpoint == a % modulus
        rows.append(
            {
                "n": n,
                "modulus": str(modulus),
                "d1_solution": str(d1),
                "d2": d2,
                "loads": loads,
                "endpoint": endpoint,
                "target_residual_mod_modulus": (endpoint - a) % modulus,
                "all_loads_free_before_solving_d1": True,
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "all_moduli_use_b_squared_without_factoring": True,
        "prime_or_target_census_performed": False,
    }


def greedy_digits(n: int, value: int) -> list[int]:
    m = n - 2
    weights = [0, 7] + [4 * index + 2 for index in range(2, m + 1)]
    Q = [1]
    q_previous_previous = 0
    q_previous = 1
    for index in range(1, m + 1):
        current = weights[index] * q_previous + q_previous_previous
        Q.append(current)
        q_previous_previous, q_previous = q_previous, current
    assert 0 <= value < Q[m]
    remaining = value
    digits = [0] * (m + 1)
    for index in range(m, 0, -1):
        digits[index] = remaining // Q[index - 1]
        remaining %= Q[index - 1]
    assert remaining == 0
    assert digits[1] <= 6
    for index in range(2, m + 1):
        assert digits[index] <= weights[index]
        if digits[index] == weights[index]:
            assert digits[index - 1] == 0
    reconstructed = sum(digits[index] * Q[index - 1] for index in range(1, m + 1))
    assert reconstructed == value
    return digits[1:]


def canonical_language_control() -> dict[str, Any]:
    n = 5
    data = word_data(n)
    a = int(data["a"])
    c = int(data["c"])
    all_words = [greedy_digits(n, value) for value in range(a)]
    assert len({tuple(word) for word in all_words}) == a
    lower = (a + 2 * c - 1) // (2 * c)
    upper = (a - 1) // 2
    window_words = all_words[lower : upper + 1]
    assert len(window_words) == int(data["window_rank"])
    return {
        "n": n,
        "canonical_words_checked": len(all_words),
        "distinct_words": len({tuple(word) for word in all_words}),
        "window_lower": lower,
        "window_upper": upper,
        "window_words": len(window_words),
        "actual_R_has_at_most_one_word": True,
        "words_digest": digest(all_words),
        "finite_control_only": True,
    }


def polynomial_multiply_mod(left: list[int], right: list[int], p: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_value * right_value
            ) % p
    return result


def lagrange_basis(nodes: list[int], selected: int, p: int) -> list[int]:
    polynomial = [1]
    denominator = 1
    chosen = nodes[selected]
    for index, node in enumerate(nodes):
        if index == selected:
            continue
        polynomial = polynomial_multiply_mod(polynomial, [(-node) % p, 1], p)
        denominator = denominator * (chosen - node) % p
    inverse = pow(denominator, -1, p)
    return [coefficient * inverse % p for coefficient in polynomial]


def evaluate_polynomial(coefficients: list[int], value: int, p: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % p
    return result


def interpolation_control() -> dict[str, Any]:
    p = 11
    grids = [[0, 1, 2], [0, 1, 2, 3, 4]]
    rows = []
    for nodes in grids:
        bases = [lagrange_basis(nodes, selected, p) for selected in range(len(nodes))]
        matrix = [
            [evaluate_polynomial(basis, node, p) for node in nodes]
            for basis in bases
        ]
        expected = [
            [int(row == column) for column in range(len(nodes))]
            for row in range(len(nodes))
        ]
        assert matrix == expected
        rows.append(
            {
                "nodes": nodes,
                "basis_degrees": [len(basis) - 1 for basis in bases],
                "evaluation_matrix": matrix,
            }
        )
    tensor_rank = math.prod(len(nodes) for nodes in grids)
    return {
        "p": p,
        "coordinate_rows": rows,
        "coordinate_rows_digest": digest(rows),
        "tensor_rank": tensor_rank,
        "tensor_total_degree_bound": sum(len(nodes) - 1 for nodes in grids),
        "evaluation_is_bijective": True,
        "finite_control_only": True,
    }


def degree_formulas() -> dict[str, Any]:
    rows = []
    for p, nonzero_rows in [(11, 5), (13, 13), (17, 9)]:
        degree = (
            nonzero_rows * (p - 1)
            if nonzero_rows % p
            else (nonzero_rows - 1) * (p - 1)
        )
        rows.append(
            {
                "p": p,
                "N": nonzero_rows,
                "endpoint_stratum_row_only_degree": degree,
                "unconditional_lower": (nonzero_rows - 1) * (p - 1),
                "actual_tied_range_case": nonzero_rows < p,
            }
        )
    return {
        "N_zero_scope": "singleton carrier equals 1; branch trivial",
        "actual_scope": "1<=N<=m-2=n-4<p, hence exact degree N(p-1)",
        "ambient_p_divides_N_row_is_completeness_control_only": True,
        "rows": rows,
        "rows_digest": digest(rows),
    }


def proof_object() -> dict[str, Any]:
    return {
        "endpoint_unit": (
            "In load coordinates [d1]Delta_sigma=sigma*hatDelta_0 and "
            "a*hatDelta_0=b*S+(-1)^n. Thus hatDelta_0 is a unit modulo "
            "every prime power over p|b, so Delta=0 solves d1 and leaves "
            "all row loads free."
        ),
        "endpoint_degree": (
            "After fixing any exact-zero stratum, the endpoint quotient is a "
            "polynomial-function algebra in the retained loads; the row-only "
            "singleton degree from Item362 is unchanged. If N=0 the carrier "
            "is 1. On the actual word 1<=N<=m-2=n-4<p, so the exact degree "
            "is N(p-1); the p|N branch is ambient completeness only."
        ),
        "box_interpolation": (
            "Since p>A>w_i, tensor Lagrange interpolation on the canonical "
            "digit box gives a p-dependent representative with degree at most "
            "6 in d1 and w_i in d_i, total 2m^2+4m."
        ),
        "rank": (
            "The intermediate half-window contains (a+1)/2-ceil(a/(2c)) "
            "canonical words, whose logarithm is asymptotic to log a and log b."
        ),
        "actual_orbit": (
            "At fixed n the actual centered remainder R_act is unique and has "
            "one canonical word, so the actual target orbit is empty or one "
            "point. Restriction there makes Phi the zero constant at a hit and "
            "Phi/p a candidate-dependent scalar."
        ),
        "admission": (
            "A useful cancellation must instead yield a candidate-independent "
            "nonzero integer H_n divisible by every singleton prime with a new "
            "sub-beta-scale height bound. Pointwise interpolation supplies no "
            "such H_n."
        ),
        "scope": (
            "Endpoint-only cancellation is closed. Box interpolation and the "
            "one-point orbit explain why degree can collapse, but no uniform "
            "cross-n height theorem or arbitrary Cartier closure is proved."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    word_rows = [word_data(n) for n in [5, 6, 7, 8, 9, 10]]
    endpoint = endpoint_coordinate_controls()
    language = canonical_language_control()
    interpolation = interpolation_control()
    degrees = degree_formulas()
    proof = proof_object()
    return {
        "schema": "item365-beta-actual-orbit-interpolation-barrier-certificate-v1",
        "item": 365,
        "date": "2026-09-01",
        "status": "PROVED_ENDPOINT_FREENESS_AND_ACTUAL_ORBIT_INTERPOLATION_BARRIER",
        "dependencies": dependencies,
        "theorem": {
            "endpoint_load_coordinate_unit": "PROVED",
            "endpoint_exact_zero_stratum_freeness": "PROVED",
            "endpoint_only_external_t_row_singleton_degree_preservation": "PROVED",
            "canonical_box_tensor_interpolation": "PROVED",
            "canonical_window_beta_scale_rank": "PROVED",
            "fixed_n_actual_orbit_rank_at_most_one": "PROVED",
            "pointwise_degree_zero_cancellation": "EXACT_BUT_INADMISSIBLE",
            "candidate_independent_sublinear_height_representative": "OPEN",
            "uniform_cross_n_orbit_density": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            "word_rows": word_rows,
            "word_rows_digest": digest(word_rows),
            "endpoint": endpoint,
            "canonical_language": language,
            "interpolation": interpolation,
            "degree_formulas": degrees,
            "controls_digest": digest(
                {
                    "word_rows": word_rows,
                    "endpoint": endpoint,
                    "language": language,
                    "interpolation": interpolation,
                    "degrees": degrees,
                }
            ),
            "finite_rows_promoted": False,
            "prime_or_target_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "closes": [
                "endpoint equality alone as a source of reduced degree for the externally t-saturated row-only singleton function",
                "formal exact-zero stratification plus endpoint as a source of load relations",
                "fixed-n actual-orbit degree as evidence for a low-height common carrier",
            ],
            "does_not_close": [
                "a uniform candidate-independent interpolation across n and p",
                "a cancellation essentially mixing internal t with the endpoint and box",
                "a sublinear-height nonzero integer carrier",
                "canonical inequality or small-quotient distribution",
                "an arbitrary F-crystal or Cartier-state theorem",
                "the actual singleton mass, Xi_Q, beta capacity, or Route 1",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_singleton_maximum": "log Q<=log b",
            "formal_endpoint_gain": 0,
            "box_interpolation_total_degree": "2m^2+4m",
            "box_interpolation_rank_log": "(1+o(1))*log b",
            "actual_orbit_rank": "at most 1",
            "pointwise_zero_representative_booking": 0,
            "candidate_independent_height_rate": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item365_beta_actual_orbit_interpolation_barrier_certificate.json",
    )
    args = parser.parse_args()
    result = build_certificate()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path(__file__).resolve().parent.parent / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "booking": 0,
                "candidate_independent_height": "OPEN",
                "item": 365,
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
