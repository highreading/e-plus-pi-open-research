#!/usr/bin/env python3
"""Exact deterministic replay for Item 340.

The global complement-loop and ideal theorems are proved symbolically in
the report.  Declared seed rows below are regression controls only.  There
is no half-bound census, actual-target search, or promotion of bounded data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item295_beta_nearest_window_descent_report.md": (
        "3ecda6865cc7f6faa9b466d4ce3628dfc0043ceb327f8f8e72e86009b87c53a7"
    ),
    "results/item295_root_audit.json": (
        "c868af5aec25f28cf1f1b72d885c48f1288208fadac6b05dd55c7482e675565b"
    ),
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "sources/item320_beta_complement_resonance_report.md": (
        "c8b2fa4194385177a2da1c26682bd155092b2848ecca9d524767eadbeb86b312"
    ),
    "results/item320_beta_complement_resonance_root_audit.json": (
        "89c84a1cd2eab682a0e98f68c3310852a3216fc0a208dc855e6098011a31bfb6"
    ),
    "sources/item337_beta_global_cofactor_lcm_capacity_report.md": (
        "c997cce3ca0808acaa9b4a63e1ea29c68933ec950a48dcf7a6a8d0280b90f6d9"
    ),
    "results/item337_beta_global_cofactor_lcm_capacity_root_audit.json": (
        "ed7457856b921248da95318f6f80acdc3dabbcb60d4c609a0a6f90952b79a2eb"
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


def lcm_nonzero(values: list[int]) -> int:
    result = 1
    for value in values:
        if value:
            result = math.lcm(result, abs(value))
    return result


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 340 uses n>=5")
    m = n - 2
    word = [0] + [7] + [4 * index + 2 for index in range(2, m + 1)]
    word.append(4 * n - 2)
    assert len(word) == m + 2

    q_continuants = [1]
    p_continuants = [0]
    q_before, q_previous = 0, 1
    p_before, p_previous = 1, 0
    for index in range(1, m + 2):
        q_current = word[index] * q_previous + q_before
        p_current = word[index] * p_previous + p_before
        q_continuants.append(q_current)
        p_continuants.append(p_current)
        q_before, q_previous = q_previous, q_current
        p_before, p_previous = p_previous, p_current

    q_values = beta_q(n)
    assert q_continuants == q_values[1 : n + 1]
    assert q_continuants[m + 1] == q_values[n]
    return {
        "n": n,
        "m": m,
        "word": word,
        "Q": q_continuants,
        "P": p_continuants,
        "A": 4 * n - 2,
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
        "d": q_values[n - 3],
        "S": p_continuants[m],
    }


def validate_digits(
    digits: list[int], maximum_index: int, data: dict[str, Any]
) -> None:
    assert len(digits) == maximum_index + 1
    assert digits[0] == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, maximum_index + 1):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0


def ostrowski_digits(
    value: int, maximum_index: int, data: dict[str, Any]
) -> list[int]:
    if not 0 <= value < data["Q"][maximum_index]:
        raise ValueError("value outside the declared Ostrowski range")
    digits = [0] * (maximum_index + 1)
    remainder = value
    for index in range(maximum_index, 0, -1):
        digits[index], remainder = divmod(
            remainder, data["Q"][index - 1]
        )
    assert remainder == 0
    validate_digits(digits, maximum_index, data)
    reconstructed = sum(
        digits[index] * data["Q"][index - 1]
        for index in range(1, maximum_index + 1)
    )
    assert reconstructed == value
    return digits


def dual_coordinates(
    digits: list[int], maximum_index: int, data: dict[str, Any]
) -> tuple[int, int, int]:
    validate_digits(digits, maximum_index, data)
    value = sum(
        digits[index] * data["Q"][index - 1]
        for index in range(1, maximum_index + 1)
    )
    p_value = sum(
        digits[index] * data["P"][index - 1]
        for index in range(1, maximum_index + 1)
    )
    error = value * data["P"][maximum_index] - (
        p_value * data["Q"][maximum_index]
    )
    return value, p_value, error


def target_row(target: int, data: dict[str, Any], tower_lcm: int, t: int) -> dict[str, Any]:
    b = data["b"]
    assert b % target == 0
    complement_gcd = math.gcd(target, t)
    tower_gcd = math.gcd(target, tower_lcm)
    covered = math.gcd(tower_gcd, t)
    excess = tower_gcd // covered
    assert tower_gcd == covered * excess

    quotient_bridge_rows: list[dict[str, Any]] = []
    seed = data["seed"]
    declared_ell_values = sorted({0, 1 % target, t % target})
    for ell in declared_ell_values:
        left = (t - ell) % target == 0
        right = (
            seed["T"] + seed["epsilon"] * seed["R"] - b * ell
        ) % (b * target) == 0
        assert left == right
        quotient_bridge_rows.append(
            {"ell": str(ell), "left": left, "right": right}
        )

    # Coefficients of F=b*t_theta-T-epsilon*R_delta and
    # G=a^2-epsilon*R_delta agree modulo every target divisor of b.
    f_constant = -seed["T"]
    g_constant = data["a"] ** 2
    assert (f_constant - g_constant) % target == 0
    for index in range(1, data["m"] + 1):
        f_delta = -seed["epsilon"] * data["Q"][index - 1]
        g_delta = f_delta
        assert (f_delta - g_delta) % target == 0
    for index in range(1, data["m"]):
        f_theta = b * data["Q"][index - 1]
        assert f_theta % target == 0

    return {
        "target": str(target),
        "target_bit_length": target.bit_length(),
        "complement_gcd": str(complement_gcd),
        "tower_gcd": str(tower_gcd),
        "complement_covered": str(covered),
        "valuation_excess": str(excess),
        "gamma_multiplicative_decomposition": True,
        "ideal_coefficient_collapse": True,
        "quotient_bridge_rows": quotient_bridge_rows,
    }


def finite_row(n: int) -> dict[str, Any]:
    data = coordinates(n)
    m = data["m"]
    A, a, b, c, d, S = (
        data["A"],
        data["a"],
        data["b"],
        data["c"],
        data["d"],
        data["S"],
    )
    assert c * S - data["P"][m - 1] * a == (-1) ** (m - 1)
    assert math.gcd(S, a) == 1

    numerator = a * a
    kappa = (2 * numerator + b) // (2 * b)
    assert (2 * numerator) % b != 0
    remainder = numerator - kappa * b
    assert remainder != 0
    epsilon = 1 if remainder > 0 else -1
    R = abs(remainder)
    sigma = ((-1) ** n) * epsilon
    t = c - kappa
    T = b * c - a * a
    assert 0 < kappa < c
    assert 0 < t < c
    assert b * t == T + epsilon * R

    theta = ostrowski_digits(t, m - 1, data)
    theta_value, _, _ = dual_coordinates(theta, m - 1, data)
    assert theta_value == t

    inverse_s = pow(S, -1, a)
    returned_R = (sigma * kappa * inverse_s) % a
    assert returned_R == R % a
    returned_digits = ostrowski_digits(returned_R, m, data)
    returned_value, returned_p, returned_E = dual_coordinates(
        returned_digits, m, data
    )
    assert returned_value == returned_R
    assert returned_E == sigma * kappa

    appended_error = (
        returned_R * data["P"][m + 1] - returned_p * b
    )
    returned_U = ((-1) ** n) * appended_error
    h = R // a
    assert R == h * a + returned_R
    assert returned_U == epsilon * a - h
    assert 0 <= h <= A // 2

    z_values = {
        index: epsilon
        * (
            returned_digits[index]
            - data["word"][index] * returned_digits[index - 1]
        )
        for index in range(3, m + 1)
    }
    tower_lcm = lcm_nonzero(list(z_values.values()))

    data["seed"] = {
        "kappa": kappa,
        "epsilon": epsilon,
        "sigma": sigma,
        "R": R,
        "t": t,
        "T": T,
        "h": h,
    }
    deoverlapped_target = b // math.gcd(b, A * a)
    target_values = sorted({b, deoverlapped_target})
    target_rows = [target_row(target, data, tower_lcm, t) for target in target_values]

    height_checks: dict[str, Any]
    if n >= 9:
        assert 3 * d < t < 4 * d
        assert 2 * A**3 * t > 3 * b
        assert A * (A - 4) * (A - 8) * t < 4 * b
        height_checks = {
            "three_d_below_t_below_four_d": True,
            "lower_beta_height_inequality": True,
            "upper_beta_height_inequality": True,
        }
    else:
        height_checks = {"asymptotic_height_row_not_invoked": True}

    return {
        "n": n,
        "m": m,
        "A": A,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "d": str(d),
        "kappa": str(kappa),
        "epsilon": epsilon,
        "sigma": sigma,
        "R": str(R),
        "t": str(t),
        "T": str(T),
        "theta_digits": theta[1:],
        "theta_digest": digest(theta),
        "returned_R": str(returned_R),
        "returned_digits": returned_digits[1:],
        "returned_digits_digest": digest(returned_digits),
        "returned_E": str(returned_E),
        "returned_U": str(returned_U),
        "h": h,
        "h_bounded_by_A_over_two": True,
        "returned_R_is_R_mod_a": True,
        "z_rows": [[index, z_values[index]] for index in sorted(z_values)],
        "z_digest": digest(z_values),
        "tower_lcm": str(tower_lcm),
        "height_checks": height_checks,
        "target_rows": target_rows,
        "actual_item316_target_claim": False,
        "finite_only": True,
    }


def exact_controls() -> dict[str, Any]:
    declared_n_values = [5, 6, 8, 9, 12, 20, 32, 48, 64]
    rows = [finite_row(n) for n in declared_n_values]
    return {
        "declared_n_values": declared_n_values,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "half_bound_census_performed": False,
        "target_search_performed": False,
        "bounded_rows_promoted": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "seed_identity": "b t=T+epsilon R, where t=c-kappa and T=bc-a^2.",
        "dual_inverse": (
            "Euler gives cS=(-1)^(n-3) mod a, hence "
            "R S=sigma kappa mod a and the complement-inverse loop "
            "returns Rbar=R mod a."
        ),
        "returned_dual_coordinates": (
            "The unique dual representative gives Ebar=sigma kappa; the "
            "master identity gives Ubar=epsilon a-floor(R/a)."
        ),
        "actual_target_resonance": (
            "An Item-316 failure has R<a/2, so floor(R/a)=0 and canonical "
            "uniqueness makes the returned word and its Lambda identical "
            "to the original target word and tower."
        ),
        "loop_defect_capacity": (
            "0<=floor(R/a)<=A/2, so every nonzero loop defect has only "
            "O(log n)=o(log b) prime-power mass."
        ),
        "complement_height": (
            "For n>=9, 3d<t<4d and b is within constant multiples of "
            "A^3 d; thus log t=log b-3 log A+O(1)."
        ),
        "mod_Q_ideal": (
            "For Q|b, after adjoining both the small-error and appended "
            "target defects, the ideal with b t_theta-T-epsilon R_delta "
            "equals the ideal with a^2-epsilon R_delta; all complement "
            "digits disappear from the undivided Q-level incidence."
        ),
        "quotient_bridge": (
            "t=ell mod Q iff T+epsilon R=b ell mod bQ, and "
            "v_p(T+epsilon R)=v_p(b)+v_p(t)."
        ),
        "missing_correlation": (
            "Gamma_Q splits exactly into complement-covered and excess "
            "valuation mass. Neither term is bounded; progress requires a "
            "joint theorem for target cofactors and canonical complement "
            "digits or the bQ quotient lift."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    controls = exact_controls()
    proof = proof_object()
    return {
        "schema": "item340-beta-full-complement-loop-correlation-certificate-v1",
        "item": 340,
        "date": "2026-09-01",
        "status": "PROVED_FULL_COMPLEMENT_LOOP_RESONANCE_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "seed_complement_identity": "PROVED",
            "full_complement_inverse_return": "PROVED",
            "returned_dual_coordinate_formula": "PROVED",
            "actual_target_tower_identity": "PROVED CONDITIONAL",
            "loop_defect_zero_rate": "PROVED",
            "complement_value_full_raw_height": "PROVED",
            "all_composite_modulus_incidence_collapse": "PROVED",
            "bQ_quotient_bridge": "PROVED",
            "actual_Gamma_Q_bound_or_lower_gain": "OPEN",
            "centered_half_bound": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "exact_controls": controls,
        "strict_scope": {
            "actual_target_claim_from_finite_rows": False,
            "finite_rows_promoted": False,
            "closes": [
                "the natural value-preserving full canonical complement-inverse loop as an independent tower",
                "the nonzero loop defect as a positive beta-rate reservoir",
                "undivided Q-level polynomial congruences from the complete complement incidence",
            ],
            "isolates": [
                "the bQ quotient lift as the first residue level that sees t modulo Q",
                "the joint canonical digit correlation between theta and the actual z tower",
                "the complement-covered and valuation-excess pieces of Gamma_Q",
            ],
            "does_not_close": [
                "the Item-316 target or centered half-bound",
                "non-value-preserving joint complement/target digit statistics",
                "the actual size of either Gamma_Q component",
                "beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "loop_defect_rate": 0,
            "complement_value_raw_rate": 1,
            "returned_tower_incremental_rate": 0,
            "actual_Gamma_Q": "OPEN",
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
            "work/item340_beta_full_complement_loop_correlation_"
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
                "actual_Gamma_Q": "OPEN",
                "booking": 0,
                "centered_half_bound": "OPEN",
                "complement_loop": "PROVED_RESONANT",
                "item": 340,
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
