#!/usr/bin/env python3
"""Deterministic certificate for Item 404.

This checker freezes the canonical dependencies, verifies the exact gcd and
safe-saturation algebra for the target-retaining degenerate carrier, replays
rank-one target-hit/target-miss countermodels on both internal branches, and
checks the sharp ray-capacity arithmetic.  Countermodels are ambient algebraic
models, not asserted values of the actual connection sequences.  No prime or
collision census is performed.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item404_j2_degenerate_target_rejection_capacity_certificate.json"


DEPENDENCIES = {
    "sources/item334_j2_coupled_cartier_carrier_report.md":
        "a9a1b42652e5157b850014758c321ffd8a5734e4f9ea3586510ae0549822357c",
    "scripts/item334_j2_coupled_cartier_carrier_certificate.py":
        "b9cab6a6ddc4a0817bae5852e78473ab3144ed9a3b8985c7eacaf27629c90cce",
    "results/item334_j2_coupled_cartier_carrier_certificate.json":
        "238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2",
    "manifests/item334_j2_coupled_cartier_carrier_manifest.json":
        "518176b7e7cf5908e350bb857063bae47658050ca63c4a0e1976554efac87bc9",
    "results/item334_j2_coupled_cartier_carrier_root_audit.json":
        "311404ffc6b6f2c6d74cb058e42fd4c1487fcbe077fd4f0e24ad933ec5846546",
    "sources/item338_j2_secondary_cartier_saturation_report.md":
        "14aa87b718b4bb83dd3e5371412fd231829f809b853d1a52eabba6181650ac33",
    "scripts/item338_j2_secondary_cartier_saturation_certificate.py":
        "5209d57fee32a6bad74e8f5b933116aa4d62448b1f9ca44e539cadf7f95fe6bd",
    "results/item338_j2_secondary_cartier_saturation_certificate.json":
        "accf5bf87b148c73117f05b8d9f7eee92af1d59611871498593cc992c758450d",
    "manifests/item338_j2_secondary_cartier_saturation_manifest.json":
        "d3ecc6c74e3dbd3b921a3f5c3aa363eac10e68322536c88ced5e6972785a6573",
    "results/item338_j2_secondary_cartier_saturation_root_audit.json":
        "9220fbfdbe2b8846720ea8df5754924232494ab205f9c01fd47eeec8f4df7e47",
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


def gcd_many(values: Iterable[int]) -> int:
    answer = 0
    for value in values:
        answer = math.gcd(answer, abs(value))
    return answer


def largest_divisor_coprime_to(value: int, support: int) -> int:
    answer = abs(value)
    shared = math.gcd(answer, abs(support))
    while shared > 1:
        while answer % shared == 0:
            answer //= shared
        shared = math.gcd(answer, abs(support))
    return answer


DECLARED_CARRIER_PACKETS = [
    {
        "name": "target_hit_with_foreign_5_support",
        "p": 17,
        "Pi": 17 * 5 * 5,
        "T0_num": 17 * 7,
        "T1_num": 17 * 11,
        "S": 2 * 3 * 5,
        "target_hit": True,
    },
    {
        "name": "target_rejection_same_triple_carrier",
        "p": 17,
        "Pi": 17 * 5 * 5,
        "T0_num": 1,
        "T1_num": 17 * 11,
        "S": 2 * 3 * 5,
        "target_hit": False,
    },
    {
        "name": "target_hit_with_foreign_7_support",
        "p": 29,
        "Pi": 29 * 7,
        "T0_num": 29 * 7 * 3,
        "T1_num": 29 * 5,
        "S": 2 * 3 * 7,
        "target_hit": True,
    },
    {
        "name": "target_rejection_second_coordinate",
        "p": 29,
        "Pi": 29 * 7,
        "T0_num": 29 * 3,
        "T1_num": 2,
        "S": 2 * 3 * 7,
        "target_hit": False,
    },
    {
        "name": "target_hit_gamma_itself_requires_saturation",
        "p": 31,
        "Pi": 31 * 5 * 7,
        "T0_num": 31 * 5,
        "T1_num": 31 * 5 * 11,
        "S": 2 * 5 * 7,
        "target_hit": True,
    },
]


def carrier_replay() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for packet in DECLARED_CARRIER_PACKETS:
        p = packet["p"]
        pi = packet["Pi"]
        t0 = packet["T0_num"]
        t1 = packet["T1_num"]
        support = packet["S"]
        gamma = gcd_many((pi, t0, t1))
        pi_sat = largest_divisor_coprime_to(pi, support)
        gamma_sat = largest_divisor_coprime_to(gamma, support)
        if support % p == 0:
            raise AssertionError((packet["name"], "tied prime in support"))
        if pi % gamma != 0 or pi_sat % gamma_sat != 0:
            raise AssertionError((packet["name"], "carrier divisibility"))
        if (pi % p == 0) != (pi_sat % p == 0):
            raise AssertionError((packet["name"], "Pi saturation"))
        if (gamma % p == 0) != (gamma_sat % p == 0):
            raise AssertionError((packet["name"], "Gamma saturation"))
        target_hit = (pi % p == 0 and t0 % p == 0 and t1 % p == 0)
        if target_hit != packet["target_hit"]:
            raise AssertionError((packet["name"], target_hit))
        if target_hit != (gamma % p == 0):
            raise AssertionError((packet["name"], "gcd equivalence"))
        rows.append({
            **packet,
            "Gamma": gamma,
            "Pi_sat": pi_sat,
            "Gamma_sat": gamma_sat,
            "p_divides_Pi_sat": pi_sat % p == 0,
            "p_divides_Gamma_sat": gamma_sat % p == 0,
        })
    return {
        "classification": (
            "EXACT INTEGER ALGEBRA REPLAY ONLY / NOT ACTUAL VALUES / NO CENSUS"
        ),
        "formula": "Gamma=gcd(Pi,abs(num(T0)),abs(num(T1)))",
        "rows": rows,
        "all_rows_verified": True,
    }


def det(left: tuple[int, int], right: tuple[int, int], p: int) -> int:
    return (left[0] * right[1] - left[1] * right[0]) % p


def target(
    f: tuple[int, int],
    b: tuple[int, int],
    v: tuple[int, int],
    W: int,
    c: int,
    p: int,
) -> tuple[int, int]:
    return tuple(
        (f[index] * W + 9 * c * b[index] - 11 * v[index]) % p
        for index in range(2)
    )


def minors(
    f: tuple[int, int],
    b: tuple[int, int],
    v: tuple[int, int],
    p: int,
) -> tuple[int, int, int]:
    return det(f, b, p), det(f, v, p), det(b, v, p)


DECLARED_FIELDS = [(17, 3), (29, 7), (31, 16), (43, 5)]


def rank_one_countermodel_replay() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for p, c in DECLARED_FIELDS:
        if p <= 11 or c % p == 0:
            raise AssertionError((p, c, "field range"))

        # f != 0: identical connection vectors and minors, only W changes.
        f = (1, 0)
        b = (1, 0)
        v = (0, 0)
        W_hit = (-9 * c) % p
        W_miss = (W_hit + 1) % p
        minor_packet = minors(f, b, v, p)
        T_hit = target(f, b, v, W_hit, c, p)
        T_miss = target(f, b, v, W_miss, c, p)
        if minor_packet != (0, 0, 0) or T_hit != (0, 0):
            raise AssertionError((p, "f_nonzero hit"))
        if T_miss == (0, 0):
            raise AssertionError((p, "f_nonzero miss"))

        # f == 0: same branch and zero minors; proportionality changes.
        f0 = (0, 0)
        b0 = (1, 0)
        inv11 = pow(11, -1, p)
        v_hit = (9 * c * inv11 % p, 0)
        v_miss = (0, 0)
        minors_hit = minors(f0, b0, v_hit, p)
        minors_miss = minors(f0, b0, v_miss, p)
        T0_hit = target(f0, b0, v_hit, 0, c, p)
        T0_miss = target(f0, b0, v_miss, 0, c, p)
        if minors_hit != (0, 0, 0) or minors_miss != (0, 0, 0):
            raise AssertionError((p, "f_zero minors"))
        if T0_hit != (0, 0) or T0_miss == (0, 0):
            raise AssertionError((p, "f_zero target"))

        # The two leftover ell=0 obstruction types cannot collide.
        f_mu = (1, 0)
        b_mu = (1, 0)
        v_mu = (0, 1)
        ell_mu, mu_mu, _ = minors(f_mu, b_mu, v_mu, p)
        old_gate = (9 * c * ell_mu - 11 * mu_mu) % p
        if ell_mu != 0 or mu_mu == 0 or old_gate == 0:
            raise AssertionError((p, "ell_zero_mu_nonzero obstruction"))
        f_c = (0, 0)
        b_c = (1, 0)
        v_c = (0, 1)
        ell_c, mu_c, C_c = minors(f_c, b_c, v_c, p)
        T_c = target(f_c, b_c, v_c, 0, c, p)
        if (ell_c, mu_c) != (0, 0) or C_c == 0 or T_c == (0, 0):
            raise AssertionError((p, "C_nonzero obstruction"))

        rows.append({
            "p": p,
            "c": c,
            "f_nonzero": {
                "f": f,
                "b": b,
                "v": v,
                "minors_both_models": minor_packet,
                "W_hit": W_hit,
                "W_miss": W_miss,
                "T_hit": T_hit,
                "T_miss": T_miss,
            },
            "f_zero": {
                "f": f0,
                "b": b0,
                "v_hit": v_hit,
                "v_miss": v_miss,
                "minors_both_models": minors_hit,
                "T_hit": T0_hit,
                "T_miss": T0_miss,
            },
            "obstruction_charts": {
                "ell_zero_mu_nonzero_old_gate": old_gate,
                "ell_mu_zero_C_nonzero_target": T_c,
            },
        })
    return {
        "classification": (
            "EXACT AMBIENT LINEAR-ALGEBRA COUNTERMODELS / "
            "NOT ACTUAL CONNECTION VALUES / NO CENSUS"
        ),
        "scope": (
            "minor residues, branch label, unit denominators, saturation, "
            "and pointwise height only; formula-specific actual target "
            "relations remain outside the no-go"
        ),
        "rows": rows,
    }


def frac(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def capacity_certificate() -> dict[str, Any]:
    ray = F(1, 35)
    normalization = F(1, 6)
    full_ordinary = 2 * ray * normalization
    full_ray_reward = ray * normalization
    if full_ordinary != F(1, 105) or full_ray_reward != F(1, 210):
        raise AssertionError((full_ordinary, full_ray_reward))

    scenarios: list[dict[str, Any]] = []

    def add_gate_scenario(name: str, d: F, g: F) -> None:
        saving = max(F(0), d - g) * normalization
        scenarios.append({
            "name": name,
            "degenerate_gate_lower_per_M": frac(d),
            "degenerate_collision_upper_per_M": frac(g),
            "normalized_saving_from_deg_target_rejection": frac(saving),
        })

    add_gate_scenario("good_reduction_Pi_equals_one_only", F(0), F(0))
    add_gate_scenario("degenerate_collision_oM_without_gate_lower_bound", F(0), F(0))
    add_gate_scenario("half_ray_gate_and_oM_degenerate_collisions", F(1, 70), F(0))
    add_gate_scenario("whole_ray_target_rejection", F(1, 35), F(0))

    g = F(1, 140)
    n = F(1, 140)
    combined_saving = max(F(0), ray - g - n) * normalization
    if combined_saving != F(1, 420):
        raise AssertionError(combined_saving)
    scenarios.append({
        "name": "combined_chart_upper_bounds",
        "degenerate_collision_upper_per_M": frac(g),
        "nondegenerate_collision_upper_per_M": frac(n),
        "normalized_saving": frac(combined_saving),
    })

    return {
        "ordinary_j2_mass_per_M": "2/35",
        "one_ray_mass_per_M": "1/35",
        "one_ray_normalized_capacity": "1/210",
        "ordinary_j2_retained_ceiling": "1/105",
        "exact_rejection_identity": (
            "raw ray mass - collision mass = rejected degenerate mass + "
            "rejected nondegenerate mass + automatic obstruction-chart mass"
        ),
        "degenerate_admission_formula": "normalized saving >= max(0,d-g)/6",
        "combined_admission_formula": (
            "normalized saving >= max(0,1/35-g-n)/6"
        ),
        "scenarios": scenarios,
        "proved_eta_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 404,
        "title": "ordinary-j2 degenerate target rejection and sharp ray capacity",
        "checked_date_beijing": "2026-09-01",
        "status": (
            "PROVED_EXACT_DEGENERATE_TARGET_CARRIER_AND_SCOPED_NO_GO_ETA_ZERO"
        ),
        "dependency_hashes_verified": verify_dependencies(),
        "exact_carrier": {
            "definition": (
                "Gamma_(r,s)=gcd(Pi_r,abs(num(T_0)),abs(num(T_1)))"
            ),
            "saturation": "Gamma_sat=(Gamma_(r,s))_(S_(r,s))",
            "equivalence": (
                "on an actual row, p divides Gamma_sat iff the row is an "
                "original collision in the triple-minor chart"
            ),
            "divisibility": "Gamma_sat divides Pi_sat",
            "height": "log^+(Gamma)<=log^+(Pi)=O(r log r)",
        },
        "carrier_replay": carrier_replay(),
        "rank_one_countermodel_replay": rank_one_countermodel_replay(),
        "capacity": capacity_certificate(),
        "proved": [
            "exact target-retaining degenerate carrier and safe saturation",
            "single surviving target coordinate on the f!=0 rank-one branch",
            "two period-free proportionality coordinates on the f=0 branch",
            "exact raw-ray partition into degenerate, nondegenerate, and automatic obstruction charts",
            "exact rejected-mass identity and sharp capacity criteria",
            "minor-information and pointwise-height scoped no-go",
            "proved eta and capacity reduction are zero",
        ],
        "conditional": [
            "D_e>=dM+o(M) and G_e<=gM+o(M) with d>g imply saving at least (d-g)/6",
            "G_e<=gM+o(M) and W_nd<=nM+o(M) with g+n<1/35 imply saving at least (1/35-g-n)/6",
            "o(M) collision mass on both charts of one ray removes its full 1/210 capacity",
        ],
        "open": [
            "actual good reduction for Pi_sat or Gamma_sat",
            "actual moving-divisor or average-gcd theorem for Gamma_sat",
            "positive lower density for rejected degenerate rows",
            "positive full-ray saving and positive eta",
            "Route 1 and every conclusion about e+pi",
        ],
        "evidence_policy": {
            "no_prime_or_collision_census": True,
            "countermodels_are_not_actual_values": True,
            "finite_objects": (
                "EXACT ALGEBRAIC REPLAY ONLY / NOT ACTUAL VALUES / DIAGNOSTIC"
            ),
            "no_finite_extrapolation": True,
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
        "item": 404,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
