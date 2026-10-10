#!/usr/bin/env python3
"""Deterministic certificate for Item 402.

This checker verifies the frozen inputs, the exact ray-capacity fractions,
declared instances of the ordered-cutoff stabilizer theorem, and exact
split-cyclotomic countermodels for unmarked symmetric and slope data.
The declared instances are algebraic replays, not a prime or collision
census.  The all-parameter proofs are in the companion report.
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
RESULT_NAME = "item402_j2_marked_frobenius_descent_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "scripts/item349_j2_degenerate_triple_minor_carrier_certificate.py":
        "b72b1ee335f243ae6a2761c417e27640f443183ec625027a14d5b7e06b91cf9b",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "manifests/item349_j2_degenerate_triple_minor_carrier_manifest.json":
        "1c1dec25ac00ea5adb2befe885c9c96ba805564651b6e90c73ef2506d30e7f4f",
    "sources/item397_j2_matched_aggregate_factor_localization_report.md":
        "4f30aab79be7039866bbad7e71cc545bd0e553d51d1166b77cb3d5f5371476ee",
    "scripts/item397_j2_matched_aggregate_factor_localization_certificate.py":
        "f7fe2d81b31ce31fb41e77c551119ac66fa7b62fadda2691ae06036ef4426186",
    "results/item397_j2_matched_aggregate_factor_localization_certificate.json":
        "45df777a3a93c0c7e4b62dadd75da7d7231d4235b2e9efde1b5204fee43254d3",
    "manifests/item397_j2_matched_aggregate_factor_localization_manifest.json":
        "a6aa125bcc12f5b258ea02fb2e552b2a658c6b8ca9bd56386297530891ef5044",
    "sources/item399_j2_raywise_chosen_prime_invariant_report.md":
        "6c7aec34049d0ed74676166d746eeb5b256f2ff45fb8409671688abd4b4fbf26",
    "scripts/item399_j2_raywise_chosen_prime_invariant_certificate.py":
        "ab58b05023329805e06e66a4c20430943fc17cda33133cace0b83d79f7e67d90",
    "results/item399_j2_raywise_chosen_prime_invariant_certificate.json":
        "967cb7effb6bf2f3f2d255c4eec6418b5ae65244888026f2e6cbc0c20ad94a35",
    "manifests/item399_j2_raywise_chosen_prime_invariant_manifest.json":
        "3f2ae65892fa23a2b5ca0c12be81eda5d924daf2c78f2442662e43293d3f326d",
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


def units_mod(modulus: int) -> list[int]:
    return [a for a in range(1, modulus) if math.gcd(a, modulus) == 1]


def cutoff_set(multiplier: int, m: int, modulus: int) -> tuple[int, ...]:
    return tuple(sorted((multiplier * u) % modulus for u in range(m + 1)))


def cutoff_stabilizer(m: int, modulus: int) -> list[int]:
    base = tuple(range(m + 1))
    return [a for a in units_mod(modulus) if cutoff_set(a, m, modulus) == base]


def generated_subgroup(generator: int, modulus: int) -> list[int]:
    if math.gcd(generator, modulus) != 1:
        raise AssertionError((generator, modulus, "not a unit"))
    subgroup: list[int] = []
    value = 1
    while value not in subgroup:
        subgroup.append(value)
        value = value * generator % modulus
    if value != 1:
        raise AssertionError((generator, modulus, subgroup, value))
    return sorted(subgroup)


def elementary_symmetric(values: list[int], prime: int) -> list[int]:
    coefficients = [1]
    for value in values:
        next_coefficients = coefficients + [0]
        for degree in range(len(coefficients), 0, -1):
            next_coefficients[degree] = (
                next_coefficients[degree]
                + value * coefficients[degree - 1]
            ) % prime
        coefficients = next_coefficients
    return coefficients


def product_mod(values: list[int], prime: int) -> int:
    answer = 1
    for value in values:
        answer = answer * value % prime
    return answer


def orbit_digest(rows: list[tuple[int, ...]]) -> str:
    body = "\n".join(",".join(map(str, row)) for row in sorted(rows)) + "\n"
    return hashlib.sha256(body.encode("ascii")).hexdigest()


DECLARED_ROWS = [
    # (p,r,s): two rows on each actual mod-6 ray, used only to replay
    # the group-theoretic formula N=p-1=6m+2r+8.
    (17, 1, 2),
    (29, 1, 4),
    (31, 5, 3),
    (43, 5, 5),
]


def stabilizer_replay() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for prime, r, s in DECLARED_ROWS:
        if prime != 2 * r + 6 * s + 3:
            raise AssertionError((prime, r, s, "tied row"))
        m = s - 1
        modulus = prime - 1
        if modulus != 6 * m + 2 * r + 8:
            raise AssertionError((prime, r, s, m, modulus))
        if not (m >= 1 and modulus > 6 * (m + 1) and modulus > 2 * m):
            raise AssertionError((prime, r, s, "range"))
        units = units_mod(modulus)
        stabilizer = cutoff_stabilizer(m, modulus)
        if stabilizer != [1]:
            raise AssertionError((prime, r, s, stabilizer))
        orbit = sorted({cutoff_set(a, m, modulus) for a in units})
        if len(orbit) != len(units):
            raise AssertionError((prime, len(orbit), len(units)))
        rows.append({
            "p": prime,
            "r": r,
            "s": s,
            "m": m,
            "N": modulus,
            "ray_r_mod_6": r % 6,
            "p_mod_6": prime % 6,
            "phi_N": len(units),
            "stabilizer": stabilizer,
            "cutoff_orbit_size": len(orbit),
            "orbit_digest_sha256": orbit_digest(orbit),
        })
    return {
        "classification": "EXACT FINITE ALGEBRAIC REPLAY ONLY / NO CENSUS",
        "rows": rows,
        "theorem_replayed": (
            "for m>=1 and N>2m, Stab_((Z/NZ)^x)({0,...,m})={1}"
        ),
    }


def split_countermodel(prime: int, r: int, s: int) -> dict[str, Any]:
    modulus = prime - 1
    group = units_mod(modulus)
    generator = modulus - 1  # complex conjugation, order two
    subgroup = generated_subgroup(generator, modulus)
    if subgroup != [1, generator]:
        raise AssertionError((prime, subgroup))

    # Coordinates model O_K/p O_K = product_(a in G) F_p.
    alpha = {a: a % prime for a in group}
    alpha[1] = 0
    beta = {a: alpha[a * generator % modulus] for a in group}
    if alpha[1] != 0 or beta[1] == 0:
        raise AssertionError((prime, alpha[1], beta[1]))

    alpha_packet = [alpha[h] for h in subgroup]
    beta_packet = [beta[h] for h in subgroup]
    if sorted(alpha_packet) != sorted(beta_packet):
        raise AssertionError((prime, alpha_packet, beta_packet))
    if sum(alpha_packet) % prime != sum(beta_packet) % prime:
        raise AssertionError((prime, "trace"))
    if product_mod(alpha_packet, prime) != product_mod(beta_packet, prime):
        raise AssertionError((prime, "norm"))
    alpha_es = elementary_symmetric(alpha_packet, prime)
    beta_es = elementary_symmetric(beta_packet, prime)
    if alpha_es != beta_es:
        raise AssertionError((prime, "characteristic polynomial"))

    alpha_valuations = {a: int(a == 1) for a in group}
    beta_valuations = {
        a: alpha_valuations[a * generator % modulus] for a in group
    }
    alpha_slope_packet = [alpha_valuations[h] for h in subgroup]
    beta_slope_packet = [beta_valuations[h] for h in subgroup]
    if sorted(alpha_slope_packet) != sorted(beta_slope_packet):
        raise AssertionError((prime, "slope multiset"))
    if alpha_valuations[1] != 1 or beta_valuations[1] != 0:
        raise AssertionError((prime, "selected slope"))

    return {
        "p": prime,
        "r": r,
        "s": s,
        "N": modulus,
        "subgroup": subgroup,
        "selected_alpha_mod_p": alpha[1],
        "selected_beta_mod_p": beta[1],
        "same_H_orbit_multiset": sorted(alpha_packet),
        "relative_trace_mod_p": sum(alpha_packet) % prime,
        "relative_norm_mod_p": product_mod(alpha_packet, prime),
        "elementary_symmetric_mod_p": alpha_es,
        "same_newton_slope_multiset": sorted(alpha_slope_packet),
        "selected_alpha_valuation_indicator": alpha_valuations[1],
        "selected_beta_valuation_indicator": beta_valuations[1],
    }


def split_countermodel_replay() -> dict[str, Any]:
    rows = [split_countermodel(*row) for row in DECLARED_ROWS]
    return {
        "classification": "EXACT SPLIT-ALGEBRA COUNTERMODELS / NO CENSUS",
        "rows": rows,
        "general_mechanism": (
            "CRT in O_K/pO_K and conjugation inside nontrivial H give "
            "identical complete H-invariant data but different selected coordinate"
        ),
        "scope": (
            "information-class no-go only; actual Xi requires a separate "
            "formula-specific conjugate relation"
        ),
    }


def capacity_certificate() -> dict[str, Any]:
    full = F(2, 35)
    ray = F(1, 35)
    normalized_ray = ray / 6
    if full / 6 != F(1, 105) or normalized_ray != F(1, 210):
        raise AssertionError((full, ray, normalized_ray))
    return {
        "ordinary_j2_full_mass_per_M": "2/35",
        "one_ray_mass_per_M": "1/35",
        "one_ray_normalized_capacity": "1/210",
        "retained_ordinary_j2_ceiling": "1/105",
        "proved_eta_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "chart_warning": (
            "a theorem on one chart alone has zero full-ray booking while "
            "the complementary chart can fill the ray"
        ),
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 402,
        "title": "marked-Frobenius descent obstruction on ordinary-j2 rays",
        "checked_date_beijing": "2026-09-01",
        "status": "proved_information_class_no_go_eta_zero",
        "dependency_hashes_verified": verify_dependencies(),
        "capacity": capacity_certificate(),
        "proved_theorems": {
            "cutoff_stabilizer": (
                "for m>=1 and N>2m, the multiplicative stabilizer of "
                "{0,...,m} in (Z/NZ)^x is trivial"
            ),
            "proper_descent": (
                "an exact formal mode-labelled Kummer descent preserving "
                "the ordered-cutoff support has H={1}, hence formal field "
                "of definition Q(mu_(p-1)); accidental formula-specific "
                "equalities among evaluated conjugates are outside the claim"
            ),
            "complete_invariant_no_go": (
                "no H-invariant function on the split conjugate packet "
                "determines vanishing of its selected coordinate"
            ),
            "unit_root_dichotomy": (
                "unmarked Frobenius/slope packets lose the selector; a marked "
                "P_p-coordinate retains it but is not a descent"
            ),
            "proved_eta": 0,
        },
        "stabilizer_replay": stabilizer_replay(),
        "split_countermodel_replay": split_countermodel_replay(),
        "closed_information_class": [
            "rational and proper-subfield traces and norms",
            "all unmarked symmetric conjugacy invariants",
            "unmarked Frobenius characteristic polynomials",
            "unmarked Newton polygons and unit-root packets",
            "proper-field descent claimed to preserve the ordered cutoff",
        ],
        "open": [
            "marked chosen-prime nonconcentration for the actual (E,Xi) ideal",
            "an actual formula tying conjugate cutoffs to the selected cutoff",
            "weighted control of the Item349 degenerate target-retaining gate",
            "a positive-mass exclusion across both charts on one ray",
            "Route 1 and every conclusion about e+pi",
        ],
        "evidence_policy": {
            "declared_group_and_split_algebra_rows": (
                "EXACT FINITE ALGEBRAIC REPLAY ONLY / DIAGNOSTIC"
            ),
            "no_prime_or_collision_census": True,
            "general_claims_proved_symbolically_in_report": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=ROOT / "results" / RESULT_NAME
    )
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if args.replay is not None:
        frozen = json.loads(args.replay.read_text(encoding="utf-8"))
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "item": 402,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
