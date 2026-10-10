#!/usr/bin/env python3
"""Exact deterministic replay for Item 333.

The all-degree and all-modulus saturation theorem is proved symbolically in
the report and encoded in the proof object below.  Declared rows are exact
regression controls only.  No half-bound or exceptional-prime scan occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item265_beta_squarefull_capacity_report.md": (
        "c41d8d2c813d4952ce5a038f291b932817c28ae5b0b1512df0a6bf0ba92a8daa"
    ),
    "results/item265_root_audit.json": (
        "72e5f43c554e326d101d1b2c55de76f277a5a817eaa6b0fc2837dd8f6bbee24a"
    ),
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "scripts/item316_beta_intermediate_ostrowski_no_go_certificate.py": (
        "b7e25ea7248dbc774da7f3bd98a8665058117de84a2342009f8669bf5438cf6f"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "sources/item323_beta_all_depth_dual_transducer_no_go_report.md": (
        "e0b5e7279079a17556a0b287ea18a40e461b6fdb8e45d8ef5a357434b8e6d9ef"
    ),
    "scripts/item323_beta_all_depth_dual_transducer_no_go_certificate.py": (
        "385d57dca299737c3a7feb0523192e81032de865a8862e126f5ec8a0723779cc"
    ),
    "results/item323_beta_all_depth_dual_transducer_no_go_certificate.json": (
        "680c7e2c3d5dfdeae2b61e37e38a81a363cf3aa25a5229062e3620c727c77bc6"
    ),
    "manifests/item323_beta_all_depth_dual_transducer_no_go_manifest.json": (
        "dcf9a3e8087bc849a7a9cfd3807635520d7e5af0b63ae3e88d4e2a33154d8200"
    ),
    "results/item323_beta_all_depth_dual_transducer_no_go_root_audit.json": (
        "2455ebbc739cc235bea44e0d220dae6d29be73eac5a9e8a846465366562ca6c2"
    ),
    "sources/item330_beta_divided_quotient_resonance_no_go_report.md": (
        "fc5d30d59e96a40fdf77a1b9557235e54dcf784d888ed81a517736496dbc4116"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    archive_root = Path(__file__).resolve().parent.parent
    rows: list[dict[str, Any]] = []
    for relative_path, expected_hash in DEPENDENCY_HASHES.items():
        path = archive_root / relative_path
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        assert actual_hash == expected_hash, (
            relative_path,
            actual_hash,
            expected_hash,
        )
        rows.append(
            {
                "path": relative_path,
                "bytes": len(payload),
                "sha256": actual_hash,
            }
        )
    return {"count": len(rows), "rows": rows, "digest": digest(rows)}


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def add_scaled(
    left: list[int], left_scale: int, right: list[int], right_scale: int
) -> list[int]:
    assert len(left) == len(right)
    return [
        left_scale * left[index] + right_scale * right[index]
        for index in range(len(left))
    ]


def dot(left: list[int], right: list[int]) -> int:
    assert len(left) == len(right)
    return sum(left[index] * right[index] for index in range(len(left)))


def coordinates(n: int, sigma: int) -> dict[str, Any]:
    if n < 5 or sigma not in (-1, 1):
        raise ValueError("Item 333 uses n>=5 and sigma in {-1,1}")
    m = n - 2
    word = [0, 7] + [4 * index + 2 for index in range(2, m + 1)]
    word.append(4 * n - 2)
    assert len(word) == m + 2

    q_values = beta_q(n)
    a = q_values[n - 1]
    b = q_values[n]
    A = 4 * n - 2

    e_coefficients = [[0] * m for _ in range(m + 2)]
    e_coefficients[1][0] = 1
    for index in range(1, m + 1):
        next_row = add_scaled(
            e_coefficients[index],
            word[index + 1],
            e_coefficients[index - 1],
            1,
        )
        if index + 1 <= m:
            next_row[index] += (-1) ** index
        e_coefficients[index + 1] = next_row

    delta_coefficients = [
        sigma * item for item in e_coefficients[m + 1]
    ]
    s_value = sigma * ((-1) ** m)
    w_top = word[m]
    u_value = s_value * (A * w_top + 1)
    v_value = -s_value * A
    alpha = s_value
    beta = s_value * w_top

    assert delta_coefficients[m - 2] == u_value
    assert delta_coefficients[m - 1] == v_value
    assert alpha * u_value + beta * v_value == 1
    assert u_value * alpha - v_value * (-beta) == 1

    h_values = [0] * (m + 2)
    n_coefficients = [[0] * m for _ in range(m + 2)]
    h_values[m] = 1
    h_values[m + 1] = 0
    for index in range(m, 0, -1):
        h_values[index - 1] = (
            word[index + 1] * h_values[index] + h_values[index + 1]
        )
        next_row = add_scaled(
            n_coefficients[index],
            word[index + 1],
            n_coefficients[index + 1],
            1,
        )
        if index + 1 <= m:
            next_row[index] += 1
        n_coefficients[index - 1] = next_row

    kappa_coefficients = [
        sigma * item for item in e_coefficients[m]
    ]
    epsilon = ((-1) ** n) * sigma
    j_coefficients = [
        [
            h_values[index] * kappa_coefficients[column]
            + epsilon * n_coefficients[index][column]
            for column in range(m)
        ]
        for index in range(m + 2)
    ]

    g_values = [0] * (m + 2)
    g_values[m] = 0
    g_values[m + 1] = 1
    for index in range(m, 0, -1):
        g_values[index - 1] = (
            word[index + 1] * g_values[index] + g_values[index + 1]
        )
    assert a == 7 * g_values[0] + g_values[1]
    assert 0 < g_values[1] < g_values[0]

    return {
        "n": n,
        "m": m,
        "sigma": sigma,
        "epsilon": epsilon,
        "word": word,
        "A": A,
        "a": a,
        "b": b,
        "E_coefficients": e_coefficients,
        "Delta_coefficients": delta_coefficients,
        "Delta_constant": -a,
        "s": s_value,
        "w_top": w_top,
        "u": u_value,
        "v": v_value,
        "alpha": alpha,
        "beta": beta,
        "H": h_values,
        "N_coefficients": n_coefficients,
        "J_coefficients": j_coefficients,
        "G": g_values,
    }


def forward_coordinate(digits: list[int], data: dict[str, Any]) -> tuple[int, int]:
    m = data["m"]
    assert len(digits) == m
    target_coordinate = (
        dot(data["Delta_coefficients"], digits) + data["Delta_constant"]
    )
    z_value = (
        -data["beta"] * digits[m - 2]
        + data["alpha"] * digits[m - 1]
    )
    return target_coordinate, z_value


def inverse_coordinate(
    lower_digits: list[int], target_coordinate: int, z_value: int,
    data: dict[str, Any]
) -> list[int]:
    m = data["m"]
    assert len(lower_digits) == m - 2
    lower_linear = dot(
        data["Delta_coefficients"][: m - 2], lower_digits
    )
    translated = target_coordinate - lower_linear + data["a"]
    top_before = data["alpha"] * translated - data["v"] * z_value
    top_last = data["beta"] * translated + data["u"] * z_value
    digits = lower_digits + [top_before, top_last]
    assert forward_coordinate(digits, data) == (target_coordinate, z_value)
    return digits


def evaluate_state(digits: list[int], data: dict[str, Any]) -> dict[str, Any]:
    e_values = [dot(row, digits) for row in data["E_coefficients"]]
    n_values = [dot(row, digits) for row in data["N_coefficients"]]
    j_values = [dot(row, digits) for row in data["J_coefficients"]]
    delta = data["sigma"] * e_values[data["m"] + 1] - data["a"]
    assert delta == forward_coordinate(digits, data)[0]
    return {
        "E": e_values,
        "N": n_values,
        "J": j_values,
        "Delta": delta,
    }


def declared_lower_digits(n: int, sigma: int, length: int, phase: int) -> list[int]:
    return [
        ((index + 2) * (n + phase) + 3 * sigma) % 11 - 5
        for index in range(length)
    ]


def coordinate_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    target_value_digests: list[str] = []
    for n in (5, 6, 8, 11, 16, 24):
        for sigma in (-1, 1):
            data = coordinates(n, sigma)
            formal_target_values: list[dict[str, Any]] = []
            for phase, z_value in enumerate((-3, 0, 4)):
                lower = declared_lower_digits(n, sigma, data["m"] - 2, phase)
                digits = inverse_coordinate(lower, 0, z_value, data)
                state = evaluate_state(digits, data)
                assert state["Delta"] == 0
                nonlinear_value = (
                    state["N"][0] ** 2
                    + state["J"][0] * state["J"][1]
                    + state["E"][2] ** 3
                    + 1
                )
                formal_target_values.append(
                    {
                        "phase": phase,
                        "z": z_value,
                        "digits_digest": digest(digits),
                        "state_digest": digest(state),
                        "nonlinear_value": nonlinear_value,
                        "canonical_claim": False,
                    }
                )
            assert len({row["nonlinear_value"] for row in formal_target_values}) > 1
            target_value_digests.append(digest(formal_target_values))

            height_value = data["a"] * data["G"][0]
            assert 8 * height_value > data["a"] ** 2
            assert 7 * height_value < data["a"] ** 2
            rows.append(
                {
                    "n": n,
                    "sigma": sigma,
                    "m": data["m"],
                    "A": data["A"],
                    "a": data["a"],
                    "b": data["b"],
                    "u": data["u"],
                    "v": data["v"],
                    "alpha": data["alpha"],
                    "beta": data["beta"],
                    "bezout": (
                        data["alpha"] * data["u"]
                        + data["beta"] * data["v"]
                    ),
                    "affine_determinant": (
                        data["u"] * data["alpha"]
                        - data["v"] * (-data["beta"])
                    ),
                    "Delta_coefficients_digest": digest(
                        data["Delta_coefficients"]
                    ),
                    "N_coefficients_digest": digest(data["N_coefficients"]),
                    "J_coefficients_digest": digest(data["J_coefficients"]),
                    "target_height": height_value,
                    "formal_target_rows_digest": digest(formal_target_values),
                    "formal_target_rows": formal_target_values,
                }
            )
    return {
        "declared_n_values": [5, 6, 8, 11, 16, 24],
        "sign_chambers": [-1, 1],
        "row_count": len(rows),
        "rows_digest": digest(rows),
        "formal_target_value_digest": digest(target_value_digests),
        "rows": rows,
        "finite_only": True,
        "formal_points_are_canonical": False,
    }


def modular_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for n in (5, 7, 10, 15):
        for sigma in (-1, 1):
            data = coordinates(n, sigma)
            moduli = (2, 4, 9, data["A"], data["b"])
            for modulus_index, modulus in enumerate(moduli):
                target_multiple = modulus * (modulus_index - 2)
                lower = declared_lower_digits(
                    n, sigma, data["m"] - 2, modulus_index + 5
                )
                z_value = 2 * modulus_index - 3
                digits = inverse_coordinate(
                    lower, target_multiple, z_value, data
                )
                state = evaluate_state(digits, data)
                assert state["Delta"] == target_multiple
                cofactor = (
                    state["N"][0] ** 2
                    + state["J"][0] * state["J"][1]
                    - state["E"][2]
                    + 3
                )
                auxiliary = (
                    state["N"][1] ** 3
                    - state["J"][2]
                    + state["E"][1] ** 2
                )
                forced_polynomial = state["Delta"] * cofactor + modulus * auxiliary
                assert forced_polynomial % modulus == 0
                rows.append(
                    {
                        "n": n,
                        "sigma": sigma,
                        "modulus_label": (
                            "b" if modulus_index == 4 else str(modulus)
                        ),
                        "modulus": modulus,
                        "Delta_over_modulus": state["Delta"] // modulus,
                        "digits_digest": digest(digits),
                        "state_digest": digest(state),
                        "cofactor_digest": digest(cofactor),
                        "auxiliary_digest": digest(auxiliary),
                        "forced_polynomial_digest": digest(forced_polynomial),
                        "forced_modulus_zero": True,
                        "canonical_claim": False,
                    }
                )
    return {
        "declared_n_values": [5, 7, 10, 15],
        "sign_chambers": [-1, 1],
        "modulus_families": ["2", "4", "9", "A", "b"],
        "row_count": len(rows),
        "rows_digest": digest(rows),
        "rows": rows,
        "finite_only": True,
    }


def proof_object() -> dict[str, Any]:
    return {
        "actual_target": (
            "In sign chamber sigma, Item 316 is exactly Delta_sigma="
            "sigma E_(m+1)-a=0 after retaining its canonical window and "
            "small-error hypotheses."
        ),
        "top_coefficients": (
            "With s=sigma(-1)^m, the d_(m-1),d_m coefficients of Delta "
            "are u=s(A w_m+1), v=-sA, and s u+s w_m v=1."
        ),
        "integral_coordinate": (
            "Set alpha=s, beta=s w_m, t=Delta and "
            "z=-beta d_(m-1)+alpha d_m. The two-by-two determinant is 1; "
            "the displayed inverse is integral, so t is an affine "
            "polynomial coordinate over Z."
        ),
        "integral_ideal": (
            "Z[d]/(Delta) is a polynomial ring over Z. Thus (Delta) is "
            "prime, radical, and saturated with respect to nonzero integer "
            "content."
        ),
        "all_modulus_kernel": (
            "For every M>=2, Z[d]/(M,Delta) is a polynomial ring over "
            "Z/MZ, so the formal target-specialization kernel is exactly "
            "(M,Delta), including composite M and every prime power."
        ),
        "state_pullback": (
            "Every N_j,J_j and all prefix/suffix states are polynomial "
            "pullbacks from the digit ring. A formally forced nonlinear "
            "congruence is therefore a universal syzygy or Delta*C+M*D."
        ),
        "valuation_scope": (
            "For a numerical off-target word, v_p(Delta*C)="
            "v_p(Delta)+v_p(C). The recurrence supplies no theorem about "
            "the cofactor valuation; canonical arithmetic of C remains open."
        ),
        "capacity": (
            "On target J_0=aG_0 and a/8<G_0<a/7, so the class passes raw "
            "height admission. Saturation gives zero incremental codimension "
            "and zero booking."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    coordinates_result = coordinate_controls()
    modular_result = modular_controls()
    proof = proof_object()
    return {
        "schema": "item333-beta-nonlinear-state-saturation-no-go-certificate-v1",
        "item": 333,
        "date": "2026-09-01",
        "status": "PROVED_SCOPED_ALL_MODULUS_NONLINEAR_STATE_SATURATION_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "actual_target_defect": "Delta_sigma=sigma E_(m+1)-a",
            "top_coefficient_bezout": "PROVED",
            "integral_affine_target_coordinate": "PROVED",
            "target_ideal_prime_radical_saturated": "PROVED",
            "all_composite_modulus_kernel": "PROVED",
            "all_depth_nonlinear_state_pullback": "PROVED",
            "formal_polynomial_congruence_class": "PROVED SCOPED NO-GO",
            "formal_prime_power_valuation_lifts": "PROVED SCOPED NO-GO",
            "canonical_cofactor_arithmetic": "OPEN",
            "canonical_complement_redigitization": "OPEN",
            "centered_half_bound": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "coordinate_controls": coordinates_result,
        "modular_controls": modular_result,
        "strict_scope": {
            "actual_target_implication_checked": True,
            "formal_points_promoted_to_actual": False,
            "finite_rows_promoted": False,
            "closes": [
                "recurrence-only polynomial nonlinear invariants of all-depth N and J",
                "formal congruence lifts modulo arbitrary composite moduli",
                "formal prime-power valuation lifts without new cofactor arithmetic",
            ],
            "does_not_close": [
                "the original exact all-digit exclusion or centered half-bound",
                "canonical sign, size, nonvanishing, gcd, or valuation theorems for cofactors",
                "floors, absolute values, minimum valuations, or redigitization",
                "proper-target residue lower bounds or weighted zero density",
                "any beta capacity reduction, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_height_admission": "PASSES",
            "raw_height_is_prime_mass": False,
            "incremental_formal_codimension": 0,
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "work/item333_beta_nonlinear_state_saturation_no_go_"
            "certificate.json"
        ),
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
                "all_modulus_kernel": "PROVED",
                "capacity_reduction": "ZERO",
                "centered_half_bound": "OPEN",
                "item": 333,
                "nonlinear_state_class": "PROVED_SCOPED_NO_GO",
                "status": result["status"],
                "target_ideal": "PRIME_RADICAL_SATURATED",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
