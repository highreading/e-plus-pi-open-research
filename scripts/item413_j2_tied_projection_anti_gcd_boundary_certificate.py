#!/usr/bin/env python3
"""Deterministic certificate for Item 413.

The checker isolates the tied-prime projection of the actual ordinary-j=2
rejection carrier.  It verifies the exact binary Smith quotient, removes all
prime factors at or below 2r+3 before doing any support accounting, separates
the remaining matched and foreign support, and checks the sharp capacity
arithmetic.  Declared integer packets are algebraic countermodels only; they
are not claimed to be values of the actual connection formulae.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item413_j2_tied_projection_anti_gcd_boundary_certificate.json"


DEPENDENCIES = {
    "sources/item404_j2_degenerate_target_rejection_capacity_report.md":
        "e691d2118611781aee2a3e851afa9b26495b75b142d9f40f6b75234334df4de2",
    "scripts/item404_j2_degenerate_target_rejection_capacity_certificate.py":
        "8d74c388dbfa9aee5762a99243000a791e0d93b8d9bacb7ef6b3485e230e9694",
    "results/item404_j2_degenerate_target_rejection_capacity_certificate.json":
        "e40b09431077bb8a432dfe8acb2678cd563f323e0ceab06f3da611bdba6a6636",
    "manifests/item404_j2_degenerate_target_rejection_capacity_manifest.json":
        "8e47fe49f8237662ec7e5c58029ef674a37fcc9a753e319097c31fbe83b13c36",
    "results/item404_j2_degenerate_target_rejection_capacity_root_audit.json":
        "b8bb1418354478cfab10e036f86fcf17f2f8a3f77d4e8847903c0a2230309302",
    "sources/item407_j2_rejection_density_boundary_report.md":
        "1894dd0b9951c54f23705380fdc5c88c3fd0b6847293f91be985914cceb42208",
    "scripts/item407_j2_rejection_density_boundary_certificate.py":
        "4e71d8fc83a1df3c438de804ac0c77ac1803d530a6c1e6a1de8a32eb665c1c10",
    "results/item407_j2_rejection_density_boundary_certificate.json":
        "9dbf1069aedbc245ff986410529d26f96de6b6259c1e196fd4b42dffac964580",
    "manifests/item407_j2_rejection_density_boundary_manifest.json":
        "fbd0a9fc2689ed523729f1ccd4e72cd00613beb632f86358025d01a160c58972",
    "results/item407_j2_rejection_density_boundary_root_audit.json":
        "ee155a6b2fa3efc1b751fb4586a4a07e559bc1b243514fc622461576076b8dd6",
    "sources/item409_j2_actual_rejection_carrier_report.md":
        "99caf10f9f1561dcb0e3a712f381db639b8260da6594dd305915ebb66f0d69ce",
    "scripts/item409_j2_actual_rejection_carrier_certificate.py":
        "32c99d596ddf933e00cab032a4af741e0781a361644ddc685d66a4e651a023f7",
    "results/item409_j2_actual_rejection_carrier_certificate.json":
        "b6a68f27d131b9a9e8d7e2512d78d54dbbd7bb70f502b2fbaf8277b6a277f940",
    "results/item409_j2_actual_rejection_carrier_ledger_delta.json":
        "0627653e9ac2f1e97ebac0b4bebc0065674045a050dcb85151bb24d93a88c7ea",
    "manifests/item409_j2_actual_rejection_carrier_manifest.json":
        "b7f052f66eb42215ce0e4778b7a0bb994b3a54e205dae81e8b75715e0220cd71",
    "results/item409_j2_actual_rejection_carrier_root_audit.json":
        "8a7545bbde4b339598a2c92cafbf5902dd1060a4c0d64d46e4590b05accc9674",
    "results/item409_j2_actual_rejection_carrier_hashes.sha256":
        "d5a469d4798992324eaf5f6b4253be86ebb64c24485673c45309a1b8b171a416",
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


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def prime_divisors(value: int) -> list[int]:
    remaining = abs(value)
    answer: list[int] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            answer.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        answer.append(remaining)
    return answer


def radical(value: int) -> int:
    answer = 1
    for prime in prime_divisors(value):
        answer *= prime
    return answer


def tail_radical(value: int, bound: int) -> int:
    answer = 1
    for prime in prime_divisors(value):
        if prime > bound:
            answer *= prime
    return answer


def largest_divisor_coprime_to(value: int, support: int) -> int:
    answer = abs(value)
    while True:
        common = math.gcd(answer, abs(support))
        if common == 1:
            return answer
        answer //= common


def tied_row(prime: int, r: int, s: int) -> None:
    if not is_prime(prime):
        raise AssertionError((prime, "prime"))
    if r < 1 or r % 2 != 1 or r % 3 == 0 or s < 1:
        raise AssertionError((prime, r, s, "ordinary-j2 range"))
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "tied phase"))
    if not prime > 2 * r + 3:
        raise AssertionError((prime, r, s, "strict threshold"))


def packet(
    *,
    name: str,
    prime: int,
    r: int,
    s: int,
    pi_value: int,
    gamma_value: int,
    support: int,
    classification: str,
) -> dict[str, Any]:
    tied_row(prime, r, s)
    if pi_value <= 0 or gamma_value <= 0 or pi_value % gamma_value != 0:
        raise AssertionError((name, pi_value, gamma_value, "Gamma divides Pi"))
    if support % prime == 0:
        raise AssertionError((name, prime, support, "safe support"))

    pi_sat = largest_divisor_coprime_to(pi_value, support)
    gamma_sat = largest_divisor_coprime_to(gamma_value, support)
    if pi_sat % gamma_sat != 0:
        raise AssertionError((name, pi_sat, gamma_sat, "saturated divisibility"))
    rejection = largest_divisor_coprime_to(pi_sat, gamma_sat)

    raw_gate = math.gcd(prime, pi_value)
    raw_hit = math.gcd(prime, gamma_value)
    sat_gate = math.gcd(prime, pi_sat)
    sat_hit = math.gcd(prime, gamma_sat)
    if raw_gate != sat_gate or raw_hit != sat_hit:
        raise AssertionError((name, "safe saturation changed tied support"))
    if raw_gate % raw_hit != 0:
        raise AssertionError((name, raw_gate, raw_hit, "binary quotient"))
    tied_quotient = raw_gate // raw_hit
    if tied_quotient not in (1, prime):
        raise AssertionError((name, tied_quotient, "binary"))
    if tied_quotient != math.gcd(prime, rejection):
        raise AssertionError((name, "projection equivalence"))

    threshold = 2 * r + 3
    tail = tail_radical(rejection, threshold)
    tied_from_tail = math.gcd(prime, tail)
    if tied_from_tail != tied_quotient:
        raise AssertionError((name, tail, tied_quotient, "tail projection"))
    foreign_tail = largest_divisor_coprime_to(tail, prime)
    if tail != tied_quotient * foreign_tail:
        raise AssertionError((name, tail, tied_quotient, foreign_tail, "tail split"))
    if math.gcd(tied_quotient, foreign_tail) != 1:
        raise AssertionError((name, "coprime tail split"))

    return {
        "name": name,
        "classification": classification,
        "p": prime,
        "r": r,
        "s": s,
        "threshold_2r_plus_3": threshold,
        "Pi": pi_value,
        "Gamma": gamma_value,
        "support": support,
        "Pi_sat": pi_sat,
        "Gamma_sat": gamma_sat,
        "J": rejection,
        "rad_J": radical(rejection),
        "tied_gate": raw_gate,
        "tied_collision": raw_hit,
        "tied_binary_quotient": tied_quotient,
        "tail_radical": tail,
        "foreign_tail": foreign_tail,
    }


def actual_item409_witness() -> dict[str, Any]:
    frozen = json.loads(
        (ROOT / "results/item409_j2_actual_rejection_carrier_certificate.json")
        .read_text(encoding="utf-8")
    )
    rows = frozen["actual_rows_replay"]["rows"]
    row = next(entry for entry in rows if entry["p"] == 709)
    expected = {
        "p": 709,
        "r": 347,
        "s": 2,
        "Pi": 79,
        "Pi_sat": 79,
        "Gamma": 1,
        "Gamma_sat": 1,
        "J": 79,
        "p_divides_J": False,
    }
    for key, value in expected.items():
        if row[key] != value:
            raise AssertionError(("Item409 witness", key, row[key], value))
    threshold = 2 * row["r"] + 3
    tail = tail_radical(row["J"], threshold)
    tied_projection = math.gcd(row["p"], row["J"])
    if threshold != 697 or tail != 1 or tied_projection != 1:
        raise AssertionError((threshold, tail, tied_projection, "foreign witness filter"))
    return {
        "classification": "EXACT PINNED ACTUAL-FORMULA WITNESS / NOT A CENSUS",
        "row": expected,
        "threshold_2r_plus_3": threshold,
        "tail_radical_of_J": tail,
        "tied_projection": tied_projection,
        "conclusion": (
            "the actual factor 79 is foreign and below the mandatory tied-prime "
            "threshold 697, so it contributes zero to the rejection mass"
        ),
    }


def declared_packets() -> dict[str, Any]:
    rows = [
        packet(
            name="tied_rejection_with_small_content",
            prime=19,
            r=5,
            s=1,
            pi_value=19 * 5 * 5,
            gamma_value=5,
            support=6,
            classification="EXACT ALGEBRAIC PACKET / NOT ACTUAL",
        ),
        packet(
            name="tied_collision_with_foreign_tail",
            prime=19,
            r=5,
            s=1,
            pi_value=19 * 23,
            gamma_value=19,
            support=6,
            classification="EXACT ALGEBRAIC PACKET / NOT ACTUAL",
        ),
        packet(
            name="no_gate_with_foreign_tail",
            prime=31,
            r=11,
            s=1,
            pi_value=37,
            gamma_value=1,
            support=6,
            classification="EXACT ALGEBRAIC PACKET / NOT ACTUAL",
        ),
        packet(
            name="safe_saturation_preserves_tied_quotient",
            prime=19,
            r=5,
            s=1,
            pi_value=19 * 5 * 5,
            gamma_value=5,
            support=5,
            classification="EXACT ALGEBRAIC PACKET / NOT ACTUAL",
        ),
    ]
    tied = next(row for row in rows if row["name"] == "tied_rejection_with_small_content")
    collision = next(row for row in rows if row["name"] == "tied_collision_with_foreign_tail")
    no_gate = next(row for row in rows if row["name"] == "no_gate_with_foreign_tail")
    if tied["tied_binary_quotient"] != 19 or tied["foreign_tail"] != 1:
        raise AssertionError(tied)
    if collision["tail_radical"] != 23 or collision["tied_binary_quotient"] != 1:
        raise AssertionError(collision)
    if no_gate["tail_radical"] != 37 or no_gate["tied_binary_quotient"] != 1:
        raise AssertionError(no_gate)
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": (
            "EXACT ALGEBRAIC COUNTERMODELS / NOT ACTUAL CONNECTION VALUES / "
            "NO PRIME CENSUS"
        ),
        "rows": rows,
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
        "sharpness": (
            "large foreign tail support can coexist with tied quotient 1; "
            "therefore tail-size lower bounds need a foreign-tail upper bound"
        ),
    }


def frac(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def capacity_replay() -> dict[str, Any]:
    ray = F(1, 35)
    scenarios = []
    declared = (
        ("no_margin", F(0), F(0), ray, F(0)),
        ("half_ray_tail_all_matched", F(1, 70), F(0), ray, F(0)),
        ("full_tail_half_foreign", ray, F(1, 70), ray, F(0)),
        ("chart_bound_only", F(0), F(0), F(1, 140), F(1, 140)),
        ("tail_all_foreign", ray, ray, ray, F(0)),
    )
    for name, tail_lower, foreign_upper, g_upper, n_upper in declared:
        matched_lower = max(F(0), tail_lower - foreign_upper)
        chart_lower = max(F(0), ray - g_upper - n_upper)
        excluded = max(matched_lower, chart_lower)
        scenarios.append({
            "name": name,
            "tail_lower_per_M": frac(tail_lower),
            "foreign_tail_upper_per_M": frac(foreign_upper),
            "G_upper_per_M": frac(g_upper),
            "N_upper_per_M": frac(n_upper),
            "matched_J_lower_per_M": frac(matched_lower),
            "excluded_lower_per_M": frac(excluded),
            "normalized_saving": frac(excluded / 6),
        })
    if scenarios[1]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[1])
    if scenarios[2]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[2])
    if scenarios[3]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[3])
    if scenarios[4]["normalized_saving"] != "0/1":
        raise AssertionError(scenarios[4])

    upper_bound_rows = []
    for tail_upper in (F(0), F(1, 210), F(1, 70), ray, F(1, 10)):
        direct = min(ray, tail_upper)
        upper_bound_rows.append({
            "tail_upper_per_M": frac(tail_upper),
            "maximum_direct_J_margin_per_M": frac(direct),
            "maximum_direct_normalized_reward": frac(direct / 6),
        })
    if upper_bound_rows[0]["maximum_direct_normalized_reward"] != "0/1":
        raise AssertionError(upper_bound_rows[0])
    if upper_bound_rows[-1]["maximum_direct_normalized_reward"] != "1/210":
        raise AssertionError(upper_bound_rows[-1])

    return {
        "classification": "EXACT RATIONAL CAPACITY ARITHMETIC",
        "one_ray_mass_per_M": "1/35",
        "conditional_lower_formula": (
            "tail>=aM, foreign<=bM, G<=gM, N<=nM imply normalized saving "
            ">=max(0,a-b,1/35-g-n)/6"
        ),
        "direct_upper_boundary": (
            "tail<=uM implies the direct matched-J reward is at most "
            "min(u,1/35)/6; this is not an upper bound on other chart exclusions"
        ),
        "scenarios": scenarios,
        "upper_bound_rows": upper_bound_rows,
        "proved_tail_lower_per_M": 0,
        "proved_foreign_upper_per_M": None,
        "proved_matched_J_lower_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_ordinary_j2_ceiling_per_6M": "1/105",
    }


def build_payload() -> dict[str, Any]:
    dependencies = verify_dependencies()
    return {
        "item": 413,
        "schema": "item413-j2-tied-projection-anti-gcd-boundary-v1",
        "title": "tied-prime projection and foreign-tail boundary for the j=2 rejection carrier",
        "checked_date_beijing": "2026-09-01",
        "status": "PROVED_EXACT_PROJECTION_AND_SHARP_INFORMATION_BOUNDARY_ETA_ZERO",
        "dependency_hashes_verified": dependencies,
        "exact_projection": {
            "actual_carriers": (
                "Pi_r=gcd(abs(num a_r),abs(num b_r),abs(num K_r)); "
                "Gamma_(r,s)=gcd(Pi_r,abs(num T_0),abs(num T_1)); "
                "J=(Pi_sat)_(Gamma_sat)"
            ),
            "binary_Smith_quotient": (
                "j_tie=gcd(p,Pi_r)/gcd(p,Gamma_(r,s)) "
                "=gcd(p,Pi_sat)/gcd(p,Gamma_sat)=gcd(p,J) in {1,p}"
            ),
            "threshold": "p=2r+6s+3>2r+3 for every actual s>=1",
            "tail": "L=rad_(q>2r+3)(J)",
            "foreign_tail": "F=L_(p)",
            "factorization": "L=j_tie*F with gcd(j_tie,F)=1",
            "mass_identity": (
                "sum log j_tie = sum log L - sum log F = D_e-G_e = J_e"
            ),
        },
        "actual_item409_witness": actual_item409_witness(),
        "declared_packets": declared_packets(),
        "capacity": capacity_replay(),
        "scoped_no_go": {
            "classification": "SHARP FOR THE STATED SUPPORT-STATISTIC INFORMATION CLASS",
            "statement": (
                "a lower bound for the full size, radical, or >2r+3 tail of J "
                "does not imply any positive tied rejection mass unless foreign "
                "tail is controlled or matching to p is proved"
            ),
            "actual_formula_anchor": (
                "Item409's exact row already shows that a nontrivial actual J "
                "factor can be wholly foreign; here 79 is removed by the exact "
                "threshold before capacity accounting"
            ),
            "countermodel_scope": (
                "the declared packets establish information-theoretic sharpness "
                "only and are not asserted to occur in the actual sequences"
            ),
        },
        "smallest_missing_lemma": {
            "direct": (
                "for one ray and delta>0, sum log(gcd(p,J_(r,s))) "
                ">=delta*M+o(M) on the selected fixed-M rows"
            ),
            "decomposed_equivalent": (
                "prove tail mass >=aM+o(M) and foreign-tail mass <=bM+o(M) "
                "with a-b=delta>0"
            ),
            "zero_rate_closer": (
                "an o(M) upper bound for the tail mass proves J_e=o(M), "
                "closing this Builder mechanism but booking no saving by itself"
            ),
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "the exact binary tied Smith quotient before or after safe saturation",
                "the mandatory 2r+3 prime threshold and matched/foreign tail factorization",
                "the aggregate mass identity and sharp conditional capacity formula",
                "the direct-channel upper boundary from a tail upper bound",
                "zero new booking and zero capacity reduction",
            ],
            "EXACT_PINNED_ACTUAL_WITNESS_NOT_A_CENSUS": [
                "the Item409 row (p,r,s)=(709,347,2) with J=79 and tied projection 1"
            ],
            "EXACT_ALGEBRAIC_COUNTERMODELS_NOT_ACTUAL": [
                "the declared integer packets showing foreign-tail sharpness"
            ],
            "CONDITIONAL": [
                "every positive saving whose tail, foreign-tail, G, or N antecedent is explicit"
            ],
            "OPEN": [
                "any positive actual matched-J lower bound",
                "any useful actual tail lower bound plus foreign-tail upper bound",
                "the tied-prime good-reduction alternative and all weighted density inputs",
                "Route 1 and every conclusion about e+pi",
            ],
        },
        "evidence_policy": {
            "no_prime_or_collision_census": True,
            "no_finite_extrapolation": True,
            "no_foreign_factor_booking": True,
            "no_countermodel_claimed_actual": True,
            "canonical_files_modified": True,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / RESULT_NAME)
    parser.add_argument("--replay", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(json.dumps(build_payload(), sort_keys=True))
    if args.replay is not None:
        frozen = json.loads(args.replay.read_text(encoding="utf-8"))
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "item": 413,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
        "new_booking": payload["capacity"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
