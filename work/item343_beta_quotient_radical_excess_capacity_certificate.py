#!/usr/bin/env python3
"""Exact deterministic replay for Item 343.

The radical/excess theorem is proved primewise in the report.  This replay
checks declared algebraic valuation tuples and unconditional seed quotient
identities.  It performs no prime, half-bound, or actual-target census.
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
    "sources/item337_beta_global_cofactor_lcm_capacity_report.md": (
        "c997cce3ca0808acaa9b4a63e1ea29c68933ec950a48dcf7a6a8d0280b90f6d9"
    ),
    "results/item337_beta_global_cofactor_lcm_capacity_root_audit.json": (
        "ed7457856b921248da95318f6f80acdc3dabbcb60d4c609a0a6f90952b79a2eb"
    ),
    "sources/item340_beta_full_complement_loop_correlation_report.md": (
        "4f3ddc5e09544e7c4d8077413b968f5b8a61694b8872dfdccf89d18dc03018b6"
    ),
    "results/item340_beta_full_complement_loop_correlation_certificate.json": (
        "4be0540e6835c3621482ab42bf5218420d76d7091a827386b1f6978146f6bfd0"
    ),
    "results/item340_beta_full_complement_loop_correlation_root_audit.json": (
        "1b0a53ab7a2c99a5be681a233c1a4c55ff8e6addb702ff287996cab3eb3e1900"
    ),
    "manifests/item340_beta_full_complement_loop_correlation_manifest.json": (
        "3197f620428af855b016842f156f69894f704de2d71846a675860d1a6b679366"
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


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization input must be positive")
    remaining = value
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors[remaining] = 1
    reconstructed = math.prod(
        prime**exponent for prime, exponent in factors.items()
    )
    assert reconstructed == value
    return factors


def radical(value: int) -> int:
    return math.prod(factorization(value))


def excess(value: int) -> int:
    return value // radical(value)


def squarefull(value: int) -> int:
    return math.prod(
        prime**exponent
        for prime, exponent in factorization(value).items()
        if exponent >= 2
    )


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def decomposition_row(label: str, target: int, tower: int, quotient: int) -> dict[str, Any]:
    if target <= 0 or tower <= 0 or quotient <= 0:
        raise ValueError("declared algebraic controls must be positive")
    captured = math.gcd(target, tower)
    covered = math.gcd(captured, quotient)
    k_value = captured // covered

    if target == 1:
        saturation_exponent = 0
        saturated = 1
        perpendicular = 1
    else:
        saturation_exponent = (target - 1).bit_length()
        assert 2 ** (saturation_exponent - 1) < target <= 2**saturation_exponent
        quotient_power_mod_captured = pow(
            quotient, saturation_exponent, captured
        )
        saturated = math.gcd(captured, quotient_power_mod_captured)
        perpendicular = captured // saturated

    perpendicular_radical = radical(perpendicular)
    assert k_value % perpendicular_radical == 0
    j_value = k_value // perpendicular_radical
    target_excess = excess(target)
    target_squarefull = squarefull(target)
    assert target_excess % j_value == 0
    assert target_squarefull % target_excess == 0

    target_factors = factorization(target)
    tower_factors = factorization(tower)
    quotient_factors = factorization(quotient)
    all_primes = sorted(
        set(target_factors) | set(tower_factors) | set(quotient_factors)
    )
    prime_rows: list[dict[str, Any]] = []
    predicted_perpendicular_radical = 1
    for prime in all_primes:
        q_exp = target_factors.get(prime, 0)
        lambda_exp = tower_factors.get(prime, 0)
        g_exp = min(q_exp, lambda_exp)
        t_exp = quotient_factors.get(prime, 0)
        h_exp = min(g_exp, t_exp)
        k_exp = g_exp - h_exp
        assert valuation(captured, prime) == g_exp
        assert valuation(covered, prime) == h_exp
        assert valuation(k_value, prime) == k_exp
        if g_exp and not t_exp:
            predicted_perpendicular_radical *= prime
        j_exp = k_exp - (1 if g_exp and not t_exp else 0)
        assert j_exp >= 0
        assert j_exp <= max(0, q_exp - 1)
        prime_rows.append(
            {
                "p": prime,
                "q": q_exp,
                "lambda": lambda_exp,
                "g": g_exp,
                "tau": t_exp,
                "h": h_exp,
                "k": k_exp,
                "j": j_exp,
            }
        )
    assert predicted_perpendicular_radical == perpendicular_radical
    assert captured == covered * perpendicular_radical * j_value

    return {
        "label": label,
        "Q": target,
        "Lambda": tower,
        "t": quotient,
        "G": captured,
        "H": covered,
        "K": k_value,
        "M_Q": saturation_exponent,
        "G_supported_on_t": saturated,
        "G_perpendicular": perpendicular,
        "R_perpendicular": perpendicular_radical,
        "J": j_value,
        "E_Q": target_excess,
        "sqfull_Q": target_squarefull,
        "K_equals_R_perpendicular_times_J": True,
        "J_divides_E_Q": True,
        "E_Q_divides_sqfull_Q": True,
        "prime_rows": prime_rows,
        "prime_rows_digest": digest(prime_rows),
        "finite_only": True,
    }


def algebraic_controls() -> dict[str, Any]:
    declared = [
        ("trivial_target", 1, 1, 1),
        ("squarefree_mixed_support", 2 * 3 * 5 * 7, 2 * 3 * 5, 2 * 3),
        (
            "repeated_mixed_support",
            2**5 * 3**4 * 5**2 * 7,
            2**4 * 3**3 * 5**2 * 7,
            2 * 3**2 * 11,
        ),
        (
            "complete_quotient_support",
            2**4 * 3**3 * 5**2,
            2**3 * 3**2 * 5,
            2**2 * 3 * 5**3,
        ),
        (
            "high_quotient_valuation",
            2**6 * 3**2 * 11**3,
            2**5 * 3**2 * 11**2,
            2**8 * 3**4,
        ),
    ]
    rows = [decomposition_row(*row) for row in declared]
    return {
        "declared_tuple_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "actual_family_claim": False,
        "finite_rows_promoted": False,
    }


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def seed_quotient_row(n: int) -> dict[str, Any]:
    values = beta_q(n)
    a, b, c = values[n - 1], values[n], values[n - 2]
    kappa = (2 * a * a + b) // (2 * b)
    signed_remainder = a * a - kappa * b
    assert signed_remainder
    epsilon = 1 if signed_remainder > 0 else -1
    R = abs(signed_remainder)
    T = b * c - a * a
    t = c - kappa
    assert T + epsilon * R == b * t

    lift_rows: list[dict[str, Any]] = []
    for precision in (1, 2, 3):
        target_power = b**precision
        true_ell = t % target_power
        false_ell = (true_ell + 1) % target_power
        for label, ell in (("true_residue", true_ell), ("adjacent_residue", false_ell)):
            left = (t - ell) % target_power == 0
            right = (
                T + epsilon * R - b * ell
            ) % (b * target_power) == 0
            assert left == right
            if label == "true_residue":
                assert left
            else:
                assert not left
            lift_rows.append(
                {
                    "precision_s": precision,
                    "label": label,
                    "ell": str(ell),
                    "left": left,
                    "right": right,
                }
            )

    return {
        "n": n,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "kappa": str(kappa),
        "epsilon": epsilon,
        "R": str(R),
        "T": str(T),
        "t": str(t),
        "seed_identity": True,
        "lift_rows": lift_rows,
        "lift_rows_digest": digest(lift_rows),
        "actual_item316_target_claim": False,
        "finite_only": True,
    }


def seed_controls() -> dict[str, Any]:
    declared_n_values = [5, 9, 16, 32, 64]
    rows = [seed_quotient_row(n) for n in declared_n_values]
    return {
        "declared_n_values": declared_n_values,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "prime_census_performed": False,
        "half_bound_census_performed": False,
        "target_search_performed": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "primewise_K": (
            "For q=v_p(Q), g=min(q,v_p(Lambda)), tau=v_p(t), one has "
            "v_p(H)=min(g,tau) and v_p(K)=max(0,g-tau)."
        ),
        "support_saturation": (
            "M=ceil(log_2 Q) is at least every v_p(Q); gcd(G,t^M) "
            "therefore contains exactly the full G-primary components "
            "whose primes divide t."
        ),
        "radical_excess": (
            "After extracting one radical copy for every G-prime avoiding "
            "t, all remaining K exponents are at most v_p(Q)-1. Hence "
            "K=R_perp J with J|E(Q)=Q/rad(Q)."
        ),
        "capacity": (
            "log K<=Xi+log E(Q)<=Xi+log sqfull(Q); the repeated part is "
            "the existing Item-265 squarefull barrier and Xi is the sole "
            "new squarefree support question."
        ),
        "all_precision_lift": (
            "For every s>=1, t=ell mod Q^s iff "
            "T+epsilon R=b ell mod bQ^s. The complete lift tower is one "
            "Q-adic scalar t."
        ),
        "ledger": (
            "Gamma_Q=log H_Q+Xi_Q+log J_Q with J_Q|E(Q). Raw gcd(Q,t) "
            "cannot be added independently because only H_Q overlaps G_Q."
        ),
        "scope": (
            "No bound for H_Q, Xi_Q, the Item-265 squarefull branch, or "
            "Gamma_Q is proved; booking remains zero."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    algebra = algebraic_controls()
    seeds = seed_controls()
    proof = proof_object()
    return {
        "schema": "item343-beta-quotient-radical-excess-capacity-certificate-v1",
        "item": 343,
        "date": "2026-09-01",
        "status": "PROVED_QUOTIENT_RADICAL_EXCESS_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "primewise_H_K_formula": "PROVED",
            "quotient_support_saturation": "PROVED",
            "K_radical_excess_factorization": "PROVED",
            "J_divides_target_excess": "PROVED",
            "global_K_capacity_bound": "PROVED",
            "all_precision_quotient_lift_saturation": "PROVED",
            "weighted_t_avoiding_radical_zero_density": "OPEN",
            "squarefull_zero_rate": "OPEN ITEM265",
            "actual_Gamma_Q": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "algebraic_controls": algebra,
        "seed_controls": seeds,
        "strict_scope": {
            "actual_target_claim_from_finite_rows": False,
            "finite_rows_promoted": False,
            "closes": [
                "same-quotient lifts as independent conditions at growing Q-adic precision",
                "quotient-supported K valuation excess as a branch separate from Item 265 squarefull excess",
                "raw gcd(Q,t) as an additive copy beyond Gamma_Q",
            ],
            "isolates": [
                "Xi_Q, the t-avoiding radical cofactor-hit mass",
                "Item 265 squarefull excess as the only remaining repeated-valuation branch",
            ],
            "does_not_close": [
                "H_Q, Xi_Q, J_Q, K_Q, or Gamma_Q on the actual target",
                "the centered half-bound",
                "beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "K_bound": "log K_Q<=Xi_Q+log E(Q)",
            "J_support": "J_Q divides E(Q) divides sqfull(Q)",
            "new_squarefree_branch": "Xi_Q",
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
            "work/item343_beta_quotient_radical_excess_capacity_"
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
                "item": 343,
                "new_squarefree_branch": "XI_Q",
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
