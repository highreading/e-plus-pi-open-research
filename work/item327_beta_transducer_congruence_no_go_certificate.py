#!/usr/bin/env python3
"""Exact deterministic replay for Item 327.

All-index statements are proved symbolically in the report and recorded in
the proof object.  Bounded rows below are exact regression controls only.
No actual half-bound or counterexample scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable


DEPENDENCY_HASHES = {
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
        raise ValueError("Item 327 coordinates use n>=5")
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
        "B": 4 * n - 6,
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
        "d": q_values[n - 3],
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
    assert 0 <= value < data["a"]
    digits = [0] * (data["m"] + 2)
    remainder = value
    for index in range(data["m"], 0, -1):
        digits[index], remainder = divmod(remainder, data["Q"][index - 1])
    assert remainder == 0
    validate_digits(digits, data)
    return digits


def prefix_state(digits: list[int], data: dict[str, Any]) -> dict[str, Any]:
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
    n_values = [0] * (m + 2)
    h_values[m] = 1
    h_values[m + 1] = 0
    for index in range(m, 0, -1):
        h_values[index - 1] = (
            data["word"][index + 1] * h_values[index] + h_values[index + 1]
        )
        n_values[index - 1] = (
            data["word"][index + 1] * n_values[index]
            + n_values[index + 1]
            + digits[index + 1]
        )
    l_values = [
        value * h_values[index] - data["b"] * n_values[index]
        for index in range(m + 2)
    ]
    assert h_values[m] == 1 and n_values[m] == 0 and l_values[m] == value
    assert all(-data["b"] < item < data["b"] for item in l_values[:-1])
    return {"H": h_values, "N": n_values, "L": l_values}


def moving_witness(n: int, s: int) -> dict[str, Any]:
    data = coordinates(n)
    assert n >= 6 and s >= 1 and 2**s <= 2 * n - 3
    modulus_half = 2 ** (s - 1)
    if modulus_half == 1:
        residue = 0
    else:
        residue = (
            ((data["a"] - 1) // 2)
            * pow(data["A"] // 2, -1, modulus_half)
        ) % modulus_half
    candidates = [
        kappa
        for kappa in range(data["B"] // 2 + 1, data["B"] + 1)
        if (kappa - residue) % modulus_half == 0
    ]
    assert len(candidates) >= 2
    candidates = [
        kappa for kappa in candidates if data["A"] * kappa + 1 != data["a"]
    ]
    assert candidates
    kappa = candidates[0]
    g_value = data["B"] - kappa

    digits = [0] * (data["m"] + 2)
    digits[data["m"] - 1] = 1
    digits[data["m"]] = g_value
    validate_digits(digits, data)
    prefix = prefix_state(digits, data)
    value = prefix["R"][data["m"]]
    e_value = prefix["E"][data["m"]]
    u_value = ((-1) ** n) * prefix["E"][data["m"] + 1]
    suffix = suffix_state(value, digits, data)

    assert value == g_value * data["c"] + data["d"]
    assert e_value == ((-1) ** n) * kappa
    assert u_value == data["A"] * kappa + 1
    assert 2 * data["c"] * value > data["a"]
    assert 2 * value < data["a"]
    assert 0 < abs(e_value) < data["c"]
    assert ((-1) ** n) * (1 if e_value > 0 else -1) == 1
    assert (u_value - data["a"]) % (2**s) == 0
    assert u_value != data["a"]

    return {
        "n": n,
        "s": s,
        "modulus": 2**s,
        "candidate_count_before_exact_exclusion": len(candidates)
        + int((data["a"] - 1) % data["A"] == 0
              and (data["a"] - 1) // data["A"]
              in range(data["B"] // 2 + 1, data["B"] + 1)),
        "kappa": kappa,
        "g": g_value,
        "R": value,
        "E": e_value,
        "U": u_value,
        "U_minus_a_over_modulus": (u_value - data["a"]) // (2**s),
        "suffix_H_digest": digest(suffix["H"]),
        "suffix_N_digest": digest(suffix["N"]),
        "suffix_L_digest": digest(suffix["L"]),
        "all_depth_unit_strip": True,
        "exact_target_equality": False,
    }


def moving_witness_controls() -> dict[str, Any]:
    all_rows: list[dict[str, Any]] = []
    selected_rows: list[dict[str, Any]] = []
    selected = {(6, 1), (6, 3), (10, 4), (18, 5), (34, 6), (66, 7), (120, 7)}
    for n in range(6, 121):
        for s in range(1, (2 * n - 3).bit_length() + 1):
            if 2**s > 2 * n - 3:
                continue
            row = moving_witness(n, s)
            all_rows.append(row)
            if (n, s) in selected:
                selected_rows.append(row)
    assert all_rows
    return {
        "checked_pair_count": len(all_rows),
        "aggregate_digest": digest(all_rows),
        "selected_rows": selected_rows,
        "selected_row_digest": digest(selected_rows),
        "label": "EXACT FINITE ONLY CONTROLS FOR A UNIFORM SYMBOLIC CONSTRUCTION",
        "moving_precision_promoted_from_rows": False,
        "actual_half_bound_scan": False,
    }


def homogeneous_f2(values: list[int], m: int) -> int:
    return values[0] ** 2 + 3 * values[1] * values[m] - 2 * values[2] ** 2


def homogeneous_f3(values: list[int], m: int) -> int:
    return values[0] * values[1] * values[m] + 5 * values[m] ** 3 - values[2] ** 3


def inhomogeneous_parts(values: list[int], m: int) -> tuple[int, int, int]:
    return (
        7,
        2 * values[0] - 3 * values[m],
        homogeneous_f2(values, m),
    )


def projective_row(n: int, value: int) -> dict[str, Any]:
    data = coordinates(n)
    assert 0 < value < data["a"] and math.gcd(value, data["b"]) == 1
    digits = ostrowski_digits(value, data)
    suffix = suffix_state(value, digits, data)
    h_values = suffix["H"][:-1]
    n_values = suffix["N"][:-1]
    l_values = suffix["L"][:-1]
    m = data["m"]

    assert l_values[m] == value and h_values[m] == 1
    for index in range(m + 1):
        assert l_values[index] - h_values[index] * l_values[m] == (
            -data["b"] * n_values[index]
        )
    minor_quotients: list[int] = []
    for i in range(m + 1):
        for j in range(m + 1):
            minor = h_values[i] * l_values[j] - h_values[j] * l_values[i]
            expected = -data["b"] * (
                h_values[i] * n_values[j] - h_values[j] * n_values[i]
            )
            assert minor == expected and minor % data["b"] == 0
            minor_quotients.append(minor // data["b"])

    divisors = [data["b"]]
    for probe in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 35, 77, 143):
        divisor = math.gcd(data["b"], probe)
        if divisor > 1 and divisor not in divisors:
            divisors.append(divisor)

    polynomial_rows: list[dict[str, Any]] = []
    for divisor in divisors:
        assert data["b"] % divisor == 0 and math.gcd(value, divisor) == 1
        assert all(
            (l_values[index] - value * h_values[index]) % divisor == 0
            for index in range(m + 1)
        )
        f2_l = homogeneous_f2(l_values, m)
        f2_h = homogeneous_f2(h_values, m)
        f3_l = homogeneous_f3(l_values, m)
        f3_h = homogeneous_f3(h_values, m)
        assert (f2_l - value**2 * f2_h) % divisor == 0
        assert (f3_l - value**3 * f3_h) % divisor == 0
        assert (f2_l % divisor == 0) == (f2_h % divisor == 0)
        assert (f3_l % divisor == 0) == (f3_h % divisor == 0)

        parts_l = inhomogeneous_parts(l_values, m)
        parts_h = inhomogeneous_parts(h_values, m)
        inhom_l = sum(parts_l)
        reduced = parts_h[0] + value * parts_h[1] + value**2 * parts_h[2]
        assert (inhom_l - reduced) % divisor == 0
        polynomial_rows.append(
            {
                "D": divisor,
                "F2_mod_D": f2_l % divisor,
                "F3_mod_D": f3_l % divisor,
                "inhomogeneous_mod_D": inhom_l % divisor,
                "homogeneous_piece_reduction_mod_D": reduced % divisor,
            }
        )

    if value == 1:
        assert all(item == 0 for item in n_values)
        assert l_values == h_values
        assert 2 * data["c"] < data["a"]

    return {
        "n": n,
        "R": value,
        "gcd_R_b": math.gcd(value, data["b"]),
        "digits": digits[1:-1],
        "H_digest": digest(h_values),
        "N_digest": digest(n_values),
        "L_digest": digest(l_values),
        "minor_quotient_digest": digest(minor_quotients),
        "polynomial_rows": polynomial_rows,
        "polynomial_row_digest": digest(polynomial_rows),
        "projective_rank_one_mod_every_checked_divisor": True,
        "R1_non_target_comparator": value == 1,
    }


def projective_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    declarations = {
        5: [1, 2, 7, 71, 500],
        6: [1, 2, 7, 71, 1001, 9044],
        8: [1, 2, 71, 1001, 18089, 100000],
        11: [1, 2, 7, 71, 18089, 1234567],
        15: [1, 2, 71, 1001, 18089, 123456789],
    }
    for n, candidates in declarations.items():
        data = coordinates(n)
        for value in candidates:
            value %= data["a"]
            if value == 0 or math.gcd(value, data["b"]) != 1:
                continue
            rows.append(projective_row(n, value))
    assert any(row["R1_non_target_comparator"] for row in rows)
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY CONTROLS FOR SYMBOLIC ALL-DEGREE COLLAPSE",
        "finite_rows_prove_arbitrary_degree": False,
        "actual_target_promoted_from_arbitrary_words": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "moving_dyadic": (
            "For M=2^(s-1), 2^s<=2n-3 gives at least two solutions "
            "kappa in (B/2,B] to (A/2)kappa=(a-1)/2 mod M; exclude "
            "the at-most-one exact equality and set g=B-kappa."
        ),
        "moving_witness_coordinates": (
            "delta_(m-1)=1, delta_m=g gives R=gc+d, "
            "E=(-1)^n(B-g), U=A(B-g)+1; exact inequalities put it in "
            "the intermediate positive-sign window."
        ),
        "moving_scope": (
            "closes only dyadic precision 2^s<=2n-3 without new odd "
            "coprimality data; its raw log mass is O(log n)=o(n)."
        ),
        "projective_normalization": (
            "L_j=RH_j-bN_j and H_m=1,N_m=0,L_m=R imply "
            "L_j-H_jL_m=-bN_j."
        ),
        "all_degree_collapse": (
            "For D|b and homogeneous F of degree e, F(L)=R^eF(H) mod D; "
            "if gcd(R,D)=1, vanishing is equivalent."
        ),
        "general_polynomial": (
            "Homogeneous decomposition gives F(L)=sum_e R^eF_e(H) mod D; "
            "an actual target further has R=epsilon*a^2 mod D."
        ),
        "non_target_comparator": (
            "R=1, delta_1=1 has every N_j=0 and L_j=H_j, while "
            "1<a/(2c), so projective tests cannot see the target window."
        ),
        "open_escape": (
            "division by b exposes suffix-load minors; mod b^2, integer "
            "size, redigitization, and super-logarithmic dyadic precision remain open."
        ),
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item327-beta-transducer-congruence-no-go-v1",
        "item": 327,
        "date_beijing": "2026-09-01",
        "status": "PROVED_SCOPED_MOVING_DYADIC_AND_PROJECTIVE_NONLINEAR_NO_GO",
        "dependency_pins": dependency_audit(),
        "proof": proof_object(),
        "exact_replay_controls": {
            "moving_dyadic_witnesses": moving_witness_controls(),
            "projective_polynomial_collapse": projective_controls(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "actual_half_bound_scan": False,
            "actual_counterexample_search": False,
        },
        "admission": {
            "moving_dyadic_log_mass": "at most log(2n-3)=o(n)",
            "moving_dyadic_positive_linear_capacity": False,
            "odd_projective_modulus_can_equal_full_b": True,
            "odd_projective_failure_reason": "exact rank-one residue collapse",
        },
        "strict_labels": {
            "uniform_2power_at_most_2n_minus_3_witness": "PROVED",
            "all_degree_projective_residue_collapse": "PROVED",
            "moving_dyadic_information_class": "PROVED SCOPED NO-GO",
            "projective_nonlinear_residue_class": "PROVED SCOPED NO-GO",
            "bounded_controls": "EXACT FINITE ONLY",
            "original_all_digit_exclusion": "OPEN",
            "centered_half_bound": "OPEN",
            "super_logarithmic_or_full_dyadic_precision": "OPEN",
            "divided_quotient_or_mod_b_squared": "OPEN",
            "redigitized_complement": "OPEN",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "actual_target_implication_checked": True,
            "moving_witness_is_actual_centered_square": False,
            "moving_witness_retains_independent_odd_coprimality": False,
            "projective_target_unit_from_gcd_R_b": True,
            "proper_target_bound": False,
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
                "item": 327,
                "status": certificate["status"],
                "moving_dyadic": "PROVED_SCOPED_NO_GO",
                "projective_nonlinear": "PROVED_SCOPED_NO_GO",
                "original_all_digit_exclusion": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
