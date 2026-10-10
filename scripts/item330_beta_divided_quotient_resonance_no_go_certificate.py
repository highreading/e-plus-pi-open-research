#!/usr/bin/env python3
"""Exact deterministic replay for Item 330.

The all-index factorization is proved symbolically in the report and encoded
in the proof object.  Bounded arbitrary-word rows are regression controls
only.  No actual half-bound or counterexample scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
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
    "sources/item327_beta_transducer_congruence_no_go_report.md": (
        "5210f265f531198f0f1d955640eb3027debe046b01c2ec9ed58234421e0218ea"
    ),
    "scripts/item327_beta_transducer_congruence_no_go_certificate.py": (
        "b96944c91d8bb90dcb2aeb8465aa330ac70d9984722656fd36ee46af63b42427"
    ),
    "results/item327_beta_transducer_congruence_no_go_certificate.json": (
        "12fadf2ad2b9703cb369cc7e0859bfdf68425f5267581aa6c4d76d9a7b33012a"
    ),
    "manifests/item327_beta_transducer_congruence_no_go_manifest.json": (
        "9f4fcd85e9d30a224503b3724df04d013cd49df8dbf6329babbfd0ee0b82ad0d"
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
                "verified": True,
            }
        )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "dependency_count": len(rows),
        "all_dependency_hashes_verified": True,
    }


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 330 coordinates use n>=5")
    q_values = beta_q(n)
    m = n - 2
    word = [None, 7] + [4 * index + 2 for index in range(2, m + 1)]
    word.append(4 * n - 2)

    q_prefix = [0] * (m + 2)
    p_prefix = [0] * (m + 2)
    q_before, q_previous = 0, 1
    p_before, p_previous = 1, 0
    q_prefix[0] = 1
    p_prefix[0] = 0
    for index in range(1, m + 2):
        q_before, q_previous = q_previous, word[index] * q_previous + q_before
        p_before, p_previous = p_previous, word[index] * p_previous + p_before
        q_prefix[index] = q_previous
        p_prefix[index] = p_previous
    assert q_prefix == q_values[1 : n + 1]
    return {
        "n": n,
        "m": m,
        "A": 4 * n - 2,
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
        "word": word,
        "Q": q_prefix,
        "P": p_prefix,
    }


def validate_digits(digits: list[int], data: dict[str, Any]) -> None:
    m = data["m"]
    assert len(digits) == m + 2
    assert digits[0] == 0 and digits[m + 1] == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, m + 1):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0


def ostrowski_digits(value: int, data: dict[str, Any]) -> list[int]:
    assert 0 < value < data["a"]
    digits = [0] * (data["m"] + 2)
    remainder = value
    for index in range(data["m"], 0, -1):
        digits[index], remainder = divmod(remainder, data["Q"][index - 1])
    assert remainder == 0
    validate_digits(digits, data)
    return digits


def prefix_state(digits: list[int], data: dict[str, Any]) -> dict[str, list[int]]:
    validate_digits(digits, data)
    r_values: list[int] = []
    z_values: list[int] = []
    e_values: list[int] = []
    for length in range(data["m"] + 2):
        top = min(length, data["m"])
        r_value = sum(
            digits[index] * data["Q"][index - 1]
            for index in range(1, top + 1)
        )
        z_value = sum(
            digits[index] * data["P"][index - 1]
            for index in range(1, top + 1)
        )
        r_values.append(r_value)
        z_values.append(z_value)
        e_values.append(
            r_value * data["P"][length] - z_value * data["Q"][length]
        )
    assert e_values[0] == 0
    for index in range(1, data["m"] + 1):
        assert e_values[index + 1] == (
            data["word"][index + 1] * e_values[index]
            + e_values[index - 1]
            + (-1) ** index * digits[index + 1]
        )
    return {"R": r_values, "Z": z_values, "E": e_values}


def suffix_state(
    value: int, digits: list[int], data: dict[str, Any]
) -> dict[str, list[int]]:
    validate_digits(digits, data)
    m = data["m"]
    h_values = [0] * (m + 2)
    g_values = [0] * (m + 2)
    n_values = [0] * (m + 2)
    h_values[m] = 1
    h_values[m + 1] = 0
    g_values[m] = 0
    g_values[m + 1] = 1
    for index in range(m, 0, -1):
        coefficient = data["word"][index + 1]
        h_values[index - 1] = coefficient * h_values[index] + h_values[index + 1]
        g_values[index - 1] = coefficient * g_values[index] + g_values[index + 1]
        n_values[index - 1] = (
            coefficient * n_values[index]
            + n_values[index + 1]
            + digits[index + 1]
        )
    l_values = [
        value * h_values[index] - data["b"] * n_values[index]
        for index in range(m + 2)
    ]
    assert h_values[m] == 1 and g_values[m - 1] == 1
    assert all(g_values[index] > 0 for index in range(m))
    for index in range(m):
        assert math.gcd(g_values[index], g_values[index + 1]) == 1
    return {"H": h_values, "G": g_values, "N": n_values, "L": l_values}


def factorization_row(n: int, value: int) -> dict[str, Any]:
    data = coordinates(n)
    digits = ostrowski_digits(value, data)
    prefix = prefix_state(digits, data)
    suffix = suffix_state(value, digits, data)
    m = data["m"]
    assert prefix["R"][m] == value
    assert prefix["E"][m] != 0

    sigma = 1 if prefix["E"][m] > 0 else -1
    epsilon = ((-1) ** n) * sigma
    k_values = [sigma * item for item in prefix["E"]]
    kappa = k_values[m]
    assert kappa == abs(prefix["E"][m]) > 0
    target_defect = k_values[m + 1] - data["a"]
    u_value = ((-1) ** n) * prefix["E"][m + 1]

    assert u_value - epsilon * data["a"] == epsilon * target_defect
    assert (
        data["a"] ** 2 - data["b"] * kappa - epsilon * value
        == -data["a"] * target_defect
    )

    residuals: list[int] = []
    lift_residuals: list[int] = []
    j_values: list[int] = []
    for index in range(m + 2):
        j_value = kappa * suffix["H"][index] + epsilon * suffix["N"][index]
        bridge = (
            j_value
            - data["a"] * suffix["G"][index]
            - ((-1) ** (m + index)) * k_values[index]
        )
        lift = (
            epsilon * suffix["L"][index]
            - data["a"] ** 2 * suffix["H"][index]
            + data["b"] * j_value
        )
        assert bridge == target_defect * suffix["G"][index]
        assert lift == data["a"] * target_defect * suffix["H"][index]
        residuals.append(bridge)
        lift_residuals.append(lift)
        j_values.append(j_value)

    assert residuals[m - 1] == target_defect
    assert math.gcd(*(abs(item) for item in residuals[:m])) == abs(target_defect)
    adjacent_gcds = [
        math.gcd(abs(residuals[index]), abs(residuals[index + 1]))
        for index in range(m - 1)
    ]
    assert all(item == abs(target_defect) for item in adjacent_gcds)

    recovered = [0] * (m + 2)
    for index in range(1, m + 1):
        recovered[index + 1] = (
            suffix["N"][index - 1]
            - data["word"][index + 1] * suffix["N"][index]
            - suffix["N"][index + 1]
        )
        assert recovered[index + 1] == digits[index + 1]
    recovered[1] = value - sum(
        recovered[index] * data["Q"][index - 1]
        for index in range(2, m + 1)
    )
    assert recovered == digits

    proper_rows: list[dict[str, Any]] = []
    for probe in (3, 5, 7, 11, 13, 17, 19, 23, 35, 55, 77, 143):
        divisor = math.gcd(data["b"], probe)
        if divisor <= 1 or any(row["Q"] == divisor for row in proper_rows):
            continue
        simultaneous = all(item % divisor == 0 for item in residuals[:m])
        assert simultaneous == (target_defect % divisor == 0)
        proper_rows.append(
            {
                "Q": divisor,
                "portfolio_vanishes": simultaneous,
                "Delta_vanishes": target_defect % divisor == 0,
            }
        )

    return {
        "n": n,
        "R": value,
        "digits": digits[1:-1],
        "sigma": sigma,
        "epsilon": epsilon,
        "kappa": kappa,
        "U": u_value,
        "Delta": target_defect,
        "H_digest": digest(suffix["H"]),
        "G_digest": digest(suffix["G"]),
        "N_digest": digest(suffix["N"]),
        "L_digest": digest(suffix["L"]),
        "J_digest": digest(j_values),
        "bridge_residual_digest": digest(residuals),
        "lift_residual_digest": digest(lift_residuals),
        "adjacent_gcd_digest": digest(adjacent_gcds),
        "proper_target_rows": proper_rows,
        "proper_target_row_digest": digest(proper_rows),
        "global_factorization": True,
        "ideal_equals_Delta": True,
        "digit_recovery": True,
    }


def exact_controls() -> dict[str, Any]:
    declared = {
        5: [1, 2, 7, 71, 419, 500, 1000],
        6: [1, 2, 71, 1001, 8072, 9044, 18088],
        7: [1, 7, 1001, 18089, 122555, 199479, 398958],
        9: [1, 71, 18089, 10391023, 156064824, 312129648],
        13: [1, 1001, 18089, 123456789, 781379079653016],
        20: [1, 71, 18089, 123456789, 9876543210123456789],
        30: [1, 1001, 18089, 123456789012345678901234567890],
    }
    rows: list[dict[str, Any]] = []
    for n, values in declared.items():
        data = coordinates(n)
        for value in values:
            value %= data["a"]
            if value == 0:
                value = 1
            rows.append(factorization_row(n, value))

    exhaustive: list[dict[str, Any]] = []
    for n in (5, 6):
        data = coordinates(n)
        aggregate = hashlib.sha256()
        for value in range(1, data["a"]):
            row = factorization_row(n, value)
            aggregate.update(
                json.dumps(
                    {
                        "R": value,
                        "Delta": row["Delta"],
                        "bridge": row["bridge_residual_digest"],
                        "lift": row["lift_residual_digest"],
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            )
        exhaustive.append(
            {
                "n": n,
                "canonical_word_count": data["a"] - 1,
                "aggregate_digest": aggregate.hexdigest(),
                "label": "EXACT FINITE ONLY",
            }
        )

    return {
        "declared_rows": rows,
        "declared_row_digest": digest(rows),
        "exhaustive_small_controls": exhaustive,
        "label": "EXACT FINITE ONLY CONTROLS FOR SYMBOLIC FACTORIZATION",
        "finite_rows_prove_all_index_factorization": False,
        "actual_half_bound_scan": False,
        "actual_counterexample_search": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "single_defect": (
            "Delta=k_(m+1)-a; U-epsilon*a=epsilon*Delta and "
            "a^2-b*kappa-epsilon*R=-a*Delta."
        ),
        "companion_suffix": (
            "G_m=0,G_(m+1)=1 and G_(j-1)=w_(j+1)G_j+G_(j+1); "
            "G_(m-1)=1 and adjacent G values are coprime."
        ),
        "bridge_factorization": (
            "J_j=kappa H_j+epsilon N_j and "
            "T_j=aG_j+(-1)^(m+j)k_j obey the same affine recurrence; "
            "their top difference is (0,Delta), hence J_j-T_j=Delta G_j."
        ),
        "ideal": (
            "The bridge residual ideal is exactly (Delta); any adjacent "
            "pair has gcd |Delta|."
        ),
        "first_lift": (
            "epsilon L_j-a^2H_j+bJ_j=a Delta H_j; on target the equality "
            "terminates exactly after the first divided coefficient."
        ),
        "digit_equivalence": (
            "delta_(j+1)=N_(j-1)-w_(j+1)N_j-N_(j+1); together with R "
            "this recovers the complete original canonical word."
        ),
        "scope": (
            "closes accumulation of divided-quotient bridge depths and "
            "same-state higher lifts, not nonlinear arithmetic of the first load."
        ),
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item330-beta-divided-quotient-resonance-no-go-v1",
        "item": 330,
        "date_beijing": "2026-09-01",
        "status": "PROVED_SCOPED_ALL_DEPTH_DIVIDED_QUOTIENT_RESONANCE_NO_GO",
        "dependency_pins": dependency_audit(),
        "proof": proof_object(),
        "exact_replay_controls": exact_controls(),
        "admission": {
            "full_b_modulus_is_thin": False,
            "raw_log_b_scale": "n log n+O(n)",
            "actual_item316_state_forces_loads": True,
            "closure_reason": "exact principal ideal (Delta), not thin support",
        },
        "strict_labels": {
            "single_defect_and_square_bridge": "PROVED",
            "all_depth_factorization": "PROVED",
            "bridge_ideal_equals_Delta": "PROVED",
            "same_state_first_lift_termination": "PROVED",
            "digit_load_triangular_equivalence": "PROVED",
            "divided_quotient_bridge_portfolio": "PROVED SCOPED NO-GO",
            "same_state_higher_b_adic_lifts": "PROVED SCOPED NO-GO",
            "bounded_controls": "EXACT FINITE ONLY",
            "Delta_nonzero_on_every_candidate": "OPEN",
            "centered_half_bound": "OPEN",
            "nonlinear_first_load_arithmetic": "OPEN",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "actual_target_implication_checked": True,
            "arbitrary_word_promoted_to_actual": False,
            "nonlinear_load_invariant_closed": False,
            "proper_target_lower_bound": False,
            "item282_product_content_rebooked": False,
            "canonical_files_modified": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "item": 330,
                "status": certificate["status"],
                "all_depth_factorization": "PROVED",
                "bridge_ideal": "(Delta)",
                "same_state_higher_lifts": "PROVED_SCOPED_NO_GO",
                "centered_half_bound": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
