#!/usr/bin/env python3
"""Deterministic certificate for Item 407.

This checker freezes canonical Items 349, 397, 399, and 402 together
with the Item 404 work package.  It verifies the exact support-difference
carrier for degenerate target rejection and the sharp one-ray aggregate
threshold

    max(0, d-g, 1/35-g-n).

The inherited integer packets are algebra replays, not actual connection
values.  The sharpness packets are abstract weighted information models,
not actual prime rows.  No prime or collision census is performed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item407_j2_rejection_density_boundary_certificate.json"


DEPENDENCIES = {
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "scripts/item349_j2_degenerate_triple_minor_carrier_certificate.py":
        "b72b1ee335f243ae6a2761c417e27640f443183ec625027a14d5b7e06b91cf9b",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "manifests/item349_j2_degenerate_triple_minor_carrier_manifest.json":
        "1c1dec25ac00ea5adb2befe885c9c96ba805564651b6e90c73ef2506d30e7f4f",
    "results/item349_j2_degenerate_triple_minor_carrier_root_audit.json":
        "e717c01d7429f7821a7ee75e8d979bc1362107bd70466af6af54d9748299a894",
    "sources/item397_j2_matched_aggregate_factor_localization_report.md":
        "4f30aab79be7039866bbad7e71cc545bd0e553d51d1166b77cb3d5f5371476ee",
    "scripts/item397_j2_matched_aggregate_factor_localization_certificate.py":
        "f7fe2d81b31ce31fb41e77c551119ac66fa7b62fadda2691ae06036ef4426186",
    "results/item397_j2_matched_aggregate_factor_localization_certificate.json":
        "45df777a3a93c0c7e4b62dadd75da7d7231d4235b2e9efde1b5204fee43254d3",
    "manifests/item397_j2_matched_aggregate_factor_localization_manifest.json":
        "a6aa125bcc12f5b258ea02fb2e552b2a658c6b8ca9bd56386297530891ef5044",
    "results/item397_j2_matched_aggregate_factor_localization_root_audit.json":
        "9e0c3c905895a9911131cad97702b91b25ef8ce6dbb371c939ee21de3b40588a",
    "sources/item399_j2_raywise_chosen_prime_invariant_report.md":
        "6c7aec34049d0ed74676166d746eeb5b256f2ff45fb8409671688abd4b4fbf26",
    "scripts/item399_j2_raywise_chosen_prime_invariant_certificate.py":
        "ab58b05023329805e06e66a4c20430943fc17cda33133cace0b83d79f7e67d90",
    "results/item399_j2_raywise_chosen_prime_invariant_certificate.json":
        "967cb7effb6bf2f3f2d255c4eec6418b5ae65244888026f2e6cbc0c20ad94a35",
    "manifests/item399_j2_raywise_chosen_prime_invariant_manifest.json":
        "3f2ae65892fa23a2b5ca0c12be81eda5d924daf2c78f2442662e43293d3f326d",
    "results/item399_j2_raywise_chosen_prime_invariant_root_audit.json":
        "aa5565b73f0e3068408ffd70ce985f948605f1ab4516d6a1a2abc94deb98d80f",
    "sources/item402_j2_marked_frobenius_descent_no_go_report.md":
        "c6ba6147dfe835a2f01654e71131ee4e7df4c54aae91811ad7fbb3c30ba1f720",
    "scripts/item402_j2_marked_frobenius_descent_no_go_certificate.py":
        "9c4404518a85396c29578a04998f19577bafce4f4aecf167c0102f8d0aed6997",
    "results/item402_j2_marked_frobenius_descent_no_go_certificate.json":
        "1ca82cfc211a97961ad615d931f09d97df074596caff61741f434e64eb0fe3b7",
    "manifests/item402_j2_marked_frobenius_descent_no_go_manifest.json":
        "25d66b0e60b21b397e7dbfd9fb399551f1d9e406432b981f5a4b73847b27e08f",
    "results/item402_j2_marked_frobenius_descent_no_go_root_audit.json":
        "9049f003d6d0b17eb728707369d1181e31a9fa79fe0f4c1938db1e782b239ea8",
    "work/item404_j2_degenerate_target_rejection_capacity_report.md":
        "862c2eab67e060cd1a0a2afb72843003cda6a968c3e41f1ec7a52c8e9806fa7b",
    "work/item404_j2_degenerate_target_rejection_capacity_certificate.py":
        "78da3ad78e34d65ca69ce0fa5ca1c773c86f439d1731dedf59faacc036b1e368",
    "work/item404_j2_degenerate_target_rejection_capacity_certificate.json":
        "e40b09431077bb8a432dfe8acb2678cd563f323e0ceab06f3da611bdba6a6636",
    "work/item404_j2_degenerate_target_rejection_capacity_certificate_replay.json":
        "e40b09431077bb8a432dfe8acb2678cd563f323e0ceab06f3da611bdba6a6636",
    "work/item404_j2_degenerate_target_rejection_capacity_ledger_delta.json":
        "9a2c3e1397502bf6f03a74d6718dd68d3b2e2bd770aaed0c487d9b798d0ea24c",
    "work/item404_j2_degenerate_target_rejection_capacity_manifest.json":
        "d5dba8890ead4118fff5ffff8098641464d237c7af568a2b632dcfcae9606a26",
    "work/item404_j2_degenerate_target_rejection_capacity_hashes.sha256":
        "6c0be73ce318ff280197feb1e7cb75228e186cb303660b1c702c5650fad6f8d4",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> dict[str, str]:
    actuals: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
        actuals[relative] = actual
    return actuals


def frac(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def largest_divisor_coprime_to(value: int, support: int) -> int:
    answer = abs(value)
    shared = math.gcd(answer, abs(support))
    while shared > 1:
        while answer % shared == 0:
            answer //= shared
        shared = math.gcd(answer, abs(support))
    return answer


def rejection_carrier_replay() -> dict[str, Any]:
    source = json.loads(
        (ROOT / "work/item404_j2_degenerate_target_rejection_capacity_certificate.json")
        .read_text(encoding="utf-8")
    )
    inherited = source["carrier_replay"]
    rows: list[dict[str, Any]] = []
    for packet in inherited["rows"]:
        p = int(packet["p"])
        pi_sat = int(packet["Pi_sat"])
        gamma_sat = int(packet["Gamma_sat"])
        if pi_sat % gamma_sat != 0:
            raise AssertionError((packet["name"], "Gamma_sat does not divide Pi_sat"))
        rejection_carrier = largest_divisor_coprime_to(pi_sat, gamma_sat)
        support_difference = (pi_sat % p == 0 and gamma_sat % p != 0)
        if (rejection_carrier % p == 0) != support_difference:
            raise AssertionError((packet["name"], "support difference failed"))
        if support_difference == bool(packet["target_hit"]):
            raise AssertionError((packet["name"], "hit/rejection complement failed"))
        rows.append({
            "name": packet["name"],
            "p": p,
            "Pi_sat": pi_sat,
            "Gamma_sat": gamma_sat,
            "J": rejection_carrier,
            "p_divides_J": rejection_carrier % p == 0,
            "degenerate_target_hit": bool(packet["target_hit"]),
            "degenerate_target_rejection": support_difference,
        })
    return {
        "classification": (
            "EXACT INTEGER ALGEBRA REPLAY ONLY / INHERITED ITEM 404 PACKETS / "
            "NOT ACTUAL VALUES / NO CENSUS"
        ),
        "definition": "J=(Pi_sat)_(Gamma_sat)",
        "equivalence": "p|J iff p|Pi_sat and p does not divide Gamma_sat",
        "rows": rows,
        "all_rows_verified": True,
    }


RAY = F(1, 35)
NORMALIZATION = F(1, 6)


def clamp(value: F, low: F, high: F) -> F:
    return max(low, min(value, high))


def sharp_mass_model(d: F, g: F, n: F) -> dict[str, Any]:
    if not (F(0) <= d <= RAY and g >= 0 and n >= 0):
        raise AssertionError((d, g, n, "invalid parameters"))

    candidates = {
        d,
        RAY,
        clamp(g, d, RAY),
        clamp(RAY - n, d, RAY),
    }

    def collision_mass(D: F) -> F:
        return min(D, g) + min(RAY - D, n)

    D = max(sorted(candidates), key=lambda value: (collision_mass(value), -value))
    G = min(D, g)
    N = min(RAY - D, n)
    W = G + N
    excluded = RAY - W
    formula = max(F(0), d - g, RAY - g - n)
    maximum_collision_formula = min(RAY, g + n, RAY - d + g)
    if W != maximum_collision_formula or excluded != formula:
        raise AssertionError({
            "d": d,
            "g": g,
            "n": n,
            "D": D,
            "G": G,
            "N": N,
            "W": W,
            "maximum_collision_formula": maximum_collision_formula,
            "excluded": excluded,
            "formula": formula,
        })
    if not (G <= D and N <= RAY - D and D >= d and G <= g and N <= n):
        raise AssertionError((d, g, n, D, G, N, "constraint failure"))

    return {
        "classification": (
            "ABSTRACT WEIGHTED INFORMATION MODEL / NOT ACTUAL PRIME ROWS / "
            "NOT ACTUAL CONNECTION VALUES / NO CENSUS"
        ),
        "inputs": {
            "degenerate_gate_lower_d": frac(d),
            "degenerate_collision_upper_g": frac(g),
            "nondegenerate_collision_upper_n": frac(n),
        },
        "extremizer": {
            "ray_mass_R": frac(RAY),
            "degenerate_gate_mass_D": frac(D),
            "degenerate_collision_mass_G": frac(G),
            "nondegenerate_collision_mass_N": frac(N),
            "union_collision_mass_W": frac(W),
            "excluded_mass": frac(excluded),
        },
        "threshold": frac(formula),
        "normalized_saving": frac(formula * NORMALIZATION),
    }


SCENARIOS = [
    ("pinned_dependencies_no_positive_density", F(0), RAY, RAY),
    ("Gamma_moving_divisor_oM_only", F(0), F(0), RAY),
    ("positive_degenerate_target_rejection", F(1, 70), F(1, 140), RAY),
    ("combined_chart_upper_bounds", F(0), F(1, 140), F(1, 140)),
    ("joint_bounds_degenerate_margin_dominates", F(3, 140), F(1, 140), F(1, 70)),
    ("both_chart_collision_masses_oM", F(0), F(0), F(0)),
]


def capacity_replay() -> dict[str, Any]:
    if RAY * NORMALIZATION != F(1, 210):
        raise AssertionError("one-ray normalization")
    if 2 * RAY * NORMALIZATION != F(1, 105):
        raise AssertionError("ordinary-j2 normalization")

    grid_count = 0
    for d_num in range(5):
        for g_num in range(5):
            for n_num in range(5):
                sharp_mass_model(F(d_num, 140), F(g_num, 140), F(n_num, 140))
                grid_count += 1

    scenarios: list[dict[str, Any]] = []
    for name, d, g, n in SCENARIOS:
        model = sharp_mass_model(d, g, n)
        scenarios.append({"name": name, **model})

    gate_rarity = [
        {
            "name": "gate_rarity_only",
            "gate_upper_q": "0/1",
            "nondegenerate_upper_n": frac(RAY),
            "excluded_mass": "0/1",
            "normalized_saving": "0/1",
        },
        {
            "name": "gate_rarity_with_selected_prime_bound",
            "gate_upper_q": "1/140",
            "nondegenerate_upper_n": "1/140",
            "excluded_mass": "1/70",
            "normalized_saving": "1/420",
        },
    ]
    for packet in gate_rarity:
        q = F(packet["gate_upper_q"])
        n = F(packet["nondegenerate_upper_n"])
        excluded = max(F(0), RAY - q - n)
        if frac(excluded) != packet["excluded_mass"]:
            raise AssertionError(packet)
        if frac(excluded * NORMALIZATION) != packet["normalized_saving"]:
            raise AssertionError(packet)

    return {
        "one_ray_mass_per_M": "1/35",
        "one_ray_normalized_capacity": "1/210",
        "ordinary_j2_normalized_ceiling": "1/105",
        "union_identity": "W_e=G_e+N_e",
        "degenerate_rejection_identity": "F_deg=D_e-G_e",
        "maximum_union_collision_mass": "min(1/35,g+n,1/35-d+g)",
        "sharp_excluded_mass": "max(0,d-g,1/35-g-n)",
        "normalized_saving": "max(0,d-g,1/35-g-n)/6",
        "exact_rational_grid_cases": grid_count,
        "grid_classification": (
            "EXACT RATIONAL LINEAR-PROGRAM REPLAY / NOT PRIME DATA / NO CENSUS"
        ),
        "scenarios": scenarios,
        "gate_rarity_coupling": gate_rarity,
        "proved_eta_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 407,
        "title": "ordinary-j2 target-rejection density boundary on one full ray",
        "checked_date_beijing": "2026-09-01",
        "status": (
            "PROVED_EXACT_REJECTION_CARRIER_AND_SHARP_UNION_"
            "INFORMATION_BOUNDARY_ETA_ZERO"
        ),
        "dependency_hashes_verified": verify_dependencies(),
        "exact_rejection_carrier": {
            "definition": "J_(r,s)=(Pi_sat_(r,s))_(Gamma_sat_(r,s))",
            "equivalence": (
                "on an actual row, p divides J iff p divides Pi_sat and "
                "p does not divide Gamma_sat"
            ),
            "mass": "F_deg=sum_(actual tied rows p|J) log p=D_e-G_e",
            "height": "log^+(J)<=log^+(Pi)=O(r log r)",
        },
        "rejection_carrier_replay": rejection_carrier_replay(),
        "capacity_replay": capacity_replay(),
        "information_class": {
            "name": "I_407(d,g,n)",
            "contains": [
                "actual ray parametrization and ray mass 1/35",
                "exact rowwise degenerate and selected-prime carrier equivalences",
                "chart inclusions, disjointness, and aggregate bounds D>=d, G<=g, N<=n",
                "safe saturation and pointwise carrier height",
                "unmarked invariant information closed by Item 402",
            ],
            "excludes": [
                "formula-specific weighted distribution for actual Pi_sat, Gamma_sat, or (E,Xi)",
                "cross-row arithmetic forcing additional rejection",
            ],
            "sharp_no_go": (
                "no excluded mass larger than max(0,d-g,1/35-g-n) follows "
                "from this information alone"
            ),
        },
        "proved": [
            "exact support-difference carrier for degenerate target rejection",
            "exact full-ray union accounting with the Item 399 selected-prime chart",
            "sharp joint density threshold max(0,d-g,1/35-g-n)",
            "gate rarity books only when paired with complementary selected-prime control",
            "precise aggregate information-class boundary",
            "proved eta and capacity reduction are zero",
        ],
        "conditional": [
            "D>=dM+o(M), G<=gM+o(M), d>g imply normalized saving at least (d-g)/6",
            "G<=gM+o(M), N<=nM+o(M), g+n<1/35 imply normalized saving at least (1/35-g-n)/6",
            "both sets of bounds imply normalized saving at least max(0,d-g,1/35-g-n)/6",
            "G=o(M) and N=o(M) on one ray remove its full 1/210 capacity",
        ],
        "open": [
            "actual positive lower density for tied-prime divisors of J",
            "actual moving-divisor or average-gcd theorem for Gamma_sat",
            "actual selected-prime weighted theorem for (E,Xi)",
            "positive full-ray saving and positive eta",
            "Route 1 and every conclusion about e+pi",
        ],
        "evidence_policy": {
            "no_prime_or_collision_census": True,
            "no_finite_extrapolation": True,
            "integer_packets_are_not_actual_values": True,
            "mass_extremizers_are_not_actual_rows": True,
            "no_ambient_tuple_claimed_actual": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / RESULT_NAME)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()

    payload = json.loads(json.dumps(build_payload(), sort_keys=True))
    if args.replay is not None:
        frozen = json.loads(args.replay.read_text(encoding="utf-8"))
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "item": 407,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
