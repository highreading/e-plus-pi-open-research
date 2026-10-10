#!/usr/bin/env python3
"""Exact deterministic replay for Item 335.

The global first-survivor and zero-rate theorems are proved symbolically in
the report.  Declared canonical rows below are regression controls only.
There is no target census, half-bound scan, or exceptional-prime scan.
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
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "sources/item323_beta_all_depth_dual_transducer_no_go_report.md": (
        "e0b5e7279079a17556a0b287ea18a40e461b6fdb8e45d8ef5a357434b8e6d9ef"
    ),
    "results/item323_beta_all_depth_dual_transducer_no_go_root_audit.json": (
        "2455ebbc739cc235bea44e0d220dae6d29be73eac5a9e8a846465366562ca6c2"
    ),
    "sources/item330_beta_divided_quotient_resonance_no_go_report.md": (
        "fc5d30d59e96a40fdf77a1b9557235e54dcf784d888ed81a517736496dbc4116"
    ),
    "sources/item333_beta_nonlinear_state_saturation_no_go_report.md": (
        "8f4bc0a6f93cbd4882392ade311d68e25be1ceb282db71cc5e1ef2f70aee75d6"
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


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 335 uses n>=5")
    m = n - 2
    word = [0, 7] + [4 * index + 2 for index in range(2, m + 1)]
    word.append(4 * n - 2)
    assert len(word) == m + 2

    q_prefix = [0] * (m + 2)
    q_before, q_previous = 0, 1
    q_prefix[0] = 1
    for index in range(1, m + 2):
        q_before, q_previous = (
            q_previous,
            word[index] * q_previous + q_before,
        )
        q_prefix[index] = q_previous

    q_values = beta_q(n)
    assert q_prefix == q_values[1 : n + 1]
    return {
        "n": n,
        "m": m,
        "word": word,
        "Q": q_prefix,
        "A": 4 * n - 2,
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
    }


def validate_digits(digits: list[int], data: dict[str, Any]) -> None:
    m = data["m"]
    assert len(digits) == m + 2
    assert digits[0] == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, m + 1):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0
    assert digits[m + 1] == 0


def ostrowski_digits(value: int, data: dict[str, Any]) -> list[int]:
    if not 0 <= value < data["a"]:
        raise ValueError("Ostrowski input must lie in [0,a)")
    digits = [0] * (data["m"] + 2)
    remainder = value
    for index in range(data["m"], 0, -1):
        digits[index], remainder = divmod(
            remainder, data["Q"][index - 1]
        )
    assert remainder == 0
    validate_digits(digits, data)
    assert value == sum(
        digits[index] * data["Q"][index - 1]
        for index in range(1, data["m"] + 1)
    )
    return digits


def prefix_errors(digits: list[int], data: dict[str, Any]) -> list[int]:
    validate_digits(digits, data)
    errors = [0] * (data["m"] + 2)
    errors[0] = 0
    errors[1] = digits[1]
    for index in range(1, data["m"] + 1):
        errors[index + 1] = (
            data["word"][index + 1] * errors[index]
            + errors[index - 1]
            + ((-1) ** index) * digits[index + 1]
        )
    return errors


def suffix_state(digits: list[int], data: dict[str, Any]) -> dict[str, Any]:
    validate_digits(digits, data)
    m = data["m"]
    h_values = [0] * (m + 2)
    n_values = [0] * (m + 2)
    h_values[m] = 1
    h_values[m + 1] = 0
    n_values[m] = 0
    n_values[m + 1] = 0
    for index in range(m, 0, -1):
        h_values[index - 1] = (
            data["word"][index + 1] * h_values[index]
            + h_values[index + 1]
        )
        n_values[index - 1] = (
            data["word"][index + 1] * n_values[index]
            + n_values[index + 1]
            + digits[index + 1]
        )
    return {"H": h_values, "N": n_values}


def prime_factorization(value: int) -> list[list[int]]:
    remaining = abs(value)
    if remaining == 0:
        raise ValueError("zero has no finite prime factorization")
    factors: list[list[int]] = []
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            exponent += 1
            remaining //= prime
        if exponent:
            factors.append([prime, exponent])
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append([remaining, 1])
    reconstructed = 1
    for factor, exponent in factors:
        reconstructed *= factor**exponent
    assert reconstructed == abs(value)
    return factors


def state_row(n: int, value: int, value_label: str) -> dict[str, Any]:
    data = coordinates(n)
    digits = ostrowski_digits(value, data)
    assert 2 * data["c"] * value >= data["a"]
    assert 2 * value < data["a"]
    assert digits[data["m"]] <= data["word"][data["m"]] // 2

    errors = prefix_errors(digits, data)
    assert errors[data["m"]] != 0
    sigma = 1 if errors[data["m"]] > 0 else -1
    epsilon = ((-1) ** n) * sigma
    kappa = abs(errors[data["m"]])
    suffix = suffix_state(digits, data)
    j_values = [
        kappa * suffix["H"][index] + epsilon * suffix["N"][index]
        for index in range(data["m"] + 2)
    ]

    z_values: dict[int, int] = {}
    for index in range(3, data["m"] + 1):
        from_loads = (
            (1 + data["word"][index] * data["word"][index - 1])
            * j_values[index - 2]
            - data["word"][index] * j_values[index - 3]
            - j_values[index]
        )
        from_digits = epsilon * (
            digits[index] - data["word"][index] * digits[index - 1]
        )
        assert from_loads == from_digits
        assert abs(from_loads) < data["A"] ** 2
        z_values[index] = from_loads

    leading_index = max(
        index for index in range(1, data["m"] + 1) if digits[index] > 0
    )
    assert leading_index >= 2
    survivor_index = (
        data["m"] if leading_index == data["m"] else leading_index + 1
    )
    assert 3 <= survivor_index <= data["m"]
    for index in range(data["m"], survivor_index, -1):
        assert z_values[index] == 0
    survivor = z_values[survivor_index]
    assert survivor != 0
    assert 1 <= abs(survivor) <= (
        data["word"][data["m"]] * data["word"][data["m"] - 1]
    )
    assert abs(survivor) < data["A"] ** 2

    top_digits_zero = (
        digits[data["m"]] == 0 and digits[data["m"] - 1] == 0
    )
    assert (z_values[data["m"]] == 0) == top_digits_zero

    lower_digits = digits.copy()
    lower_digits[data["m"] - 1] = 0
    lower_digits[data["m"]] = 0
    lower_errors = prefix_errors(lower_digits, data)
    lower_part = sigma * lower_errors[data["m"] + 1]
    delta = sigma * errors[data["m"] + 1] - data["a"]
    primitive_numerator = (
        lower_part - data["a"]
        + epsilon * digits[data["m"] - 1]
    )
    assert primitive_numerator == delta + data["A"] * z_values[data["m"]]

    survivor_factors = prime_factorization(survivor)
    target_gcd = math.gcd(data["b"], abs(survivor))
    assert target_gcd <= abs(survivor) < data["A"] ** 2

    selected_nonzero = [
        z_values[index]
        for index in range(data["m"], 2, -1)
        if z_values[index] != 0
    ][:3]
    assert selected_nonzero
    portfolio_value = 1
    for position, z_value in enumerate(selected_nonzero, start=1):
        portfolio_value += position * z_value * z_value
    if len(selected_nonzero) >= 2:
        portfolio_value += selected_nonzero[0] * selected_nonzero[1]
    assert portfolio_value > 0
    # This declared example has K<=3, D=2, C=1 and coefficients <=A.
    polynomial_bound = math.comb(2 + len(selected_nonzero), len(selected_nonzero)) * (
        data["A"] ** 5
    )
    assert portfolio_value <= polynomial_bound

    return {
        "n": n,
        "value_label": value_label,
        "R": value,
        "a": data["a"],
        "b": data["b"],
        "c": data["c"],
        "A": data["A"],
        "sigma": sigma,
        "epsilon": epsilon,
        "Delta": delta,
        "actual_target_claim": False,
        "digits": digits[1 : data["m"] + 1],
        "digits_digest": digest(digits),
        "E_digest": digest(errors),
        "N_digest": digest(suffix["N"]),
        "J_digest": digest(j_values),
        "z_rows": [[index, z_values[index]] for index in sorted(z_values)],
        "z_digest": digest(z_values),
        "top_z_zero": z_values[data["m"]] == 0,
        "top_two_digits_zero": top_digits_zero,
        "leading_index": leading_index,
        "survivor_index": survivor_index,
        "survivor": survivor,
        "survivor_factorization": survivor_factors,
        "gcd_with_b": target_gcd,
        "gcd_bounded_by_survivor": True,
        "lower_part": lower_part,
        "primitive_numerator": primitive_numerator,
        "top_quotient_residual_identity": True,
        "selected_nonzero_cofactors": selected_nonzero,
        "portfolio_value": portfolio_value,
        "portfolio_bound": polynomial_bound,
        "finite_only": True,
    }


def exact_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for n in (5, 6, 8, 11, 16, 24):
        data = coordinates(n)
        lower_window = (
            data["a"] + 2 * data["c"] - 1
        ) // (2 * data["c"])
        declared_values = (
            ("lower_window_ceiling", lower_window),
            ("quarter", data["a"] // 4),
            ("upper_half_integer", (data["a"] - 1) // 2),
        )
        assert len({value for _, value in declared_values}) == 3
        for value_label, value in declared_values:
            rows.append(state_row(n, value, value_label))
    return {
        "declared_n_values": [5, 6, 8, 11, 16, 24],
        "declared_value_labels": [
            "lower_window_ceiling",
            "quarter",
            "upper_half_integer",
        ],
        "row_count": len(rows),
        "rows_digest": digest(rows),
        "rows": rows,
        "target_census_performed": False,
        "finite_rows_promoted": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "candidate_selection": (
            "After Item 333 sets Delta=0, the first primitive canonical "
            "coordinate is z_m=epsilon(delta_m-w_m delta_(m-1)); it is "
            "also an exact three-depth cancellation of J."
        ),
        "load_formula": (
            "For 3<=j<=m, z_j=(1+w_j w_(j-1))J_(j-2)-"
            "w_j J_(j-3)-J_j=epsilon(delta_j-w_j delta_(j-1))."
        ),
        "target_quotient": (
            "Writing L for the lower-digit contribution to Delta gives "
            "L-a+epsilon delta_(m-1)=Delta+A z_m; on target its exact "
            "quotient by A is z_m."
        ),
        "first_survivor": (
            "If ell is the leading nonzero digit, the first nonzero z when "
            "descending from m occurs at m when ell=m and at ell+1 "
            "otherwise. The target lower window forces ell>=2."
        ),
        "nonzero_height": (
            "The half-language and canonical bounds give "
            "1<=|z_*|<=w_m w_(m-1)<A^2."
        ),
        "proper_target_mass": (
            "For every Q|b, the captured prime-power mass is "
            "log gcd(Q,|z_*|)<2 log A=o(log b)."
        ),
        "fixed_complexity": (
            "For fixed K,D,C, a degree-D polynomial of coefficient height "
            "A^C in K cofactor values has nonzero height at most "
            "binom(D+K,K) A^(C+2D), hence O(log n) prime-power mass."
        ),
        "scope": (
            "Growing depth/degree/height, exact zero-versus-nonzero "
            "contradictions, full-word cofactors, and complement "
            "redigitization remain open."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    controls = exact_controls()
    proof = proof_object()
    return {
        "schema": "item335-beta-first-canonical-cofactor-zero-rate-certificate-v1",
        "item": 335,
        "date": "2026-09-01",
        "status": "PROVED_GLOBAL_FIRST_CANONICAL_COFACTOR_ZERO_RATE_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "actual_target_implication": "PROVED",
            "adjacent_load_cofactor_formula": "PROVED",
            "top_defect_quotient": "PROVED",
            "canonical_first_survivor_nonzero": "PROVED",
            "first_survivor_height_below_A_squared": "PROVED",
            "proper_target_prime_power_mass_zero_rate": "PROVED",
            "fixed_complexity_cofactor_algebra_zero_rate": "PROVED SCOPED NO-GO",
            "growing_complexity_portfolio": "OPEN",
            "canonical_complement_redigitization": "OPEN",
            "centered_half_bound": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "exact_controls": controls,
        "strict_scope": {
            "actual_target_claim_from_finite_rows": False,
            "finite_rows_promoted": False,
            "closes": [
                "the primitive top quotient as a positive-mass reservoir",
                "zero-top stripping followed by the first nonzero adjacent cofactor",
                "fixed-cardinality bounded-degree polynomial-height boundary-cofactor portfolios",
                "proper-target valuation mass supported only on those nonzero values",
            ],
            "does_not_close": [
                "the original exact target or centered half-bound",
                "growing-depth, growing-degree, or growing-height portfolios",
                "exact target-specific sign or nonvanishing contradictions",
                "full-word lower-coordinate arithmetic or complement redigitization",
                "proper-target residue lower bounds, beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "first_survivor_bound": "1<=|z_*|<A^2",
            "proper_target_mass_bound": "log gcd(Q,|z_*|)<2 log A",
            "normalization": "log b=n log n+O(n)",
            "first_cofactor_rate": 0,
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
            "work/item335_beta_first_canonical_cofactor_zero_rate_"
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
                "capacity_reduction": "ZERO",
                "centered_half_bound": "OPEN",
                "first_canonical_cofactor": "PROVED_NONZERO_BELOW_A_SQUARED",
                "fixed_complexity_portfolio": "PROVED_ZERO_RATE",
                "item": 335,
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
