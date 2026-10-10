#!/usr/bin/env python3
"""Deterministic certificate for Item 416.

The checker sharpens Item 413's foreign-tail accounting by allowing a
selected-prime-safe adaptive cutoff.  Every prime at most Y except the tied
prime p is removed.  It verifies that raising the cutoff removes exactly the
same (purely foreign) radical mass from the tail and the foreign tail, so the
matched Smith quotient is invariant.  It also verifies the exact forward
transport geometry for residue-aligned foreign primes.  Declared integer
packets are algebraic support packets only and are never claimed actual.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item416_j2_adaptive_foreign_tail_transport_certificate.json"


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
    "sources/item409_j2_actual_rejection_carrier_report.md":
        "99caf10f9f1561dcb0e3a712f381db639b8260da6594dd305915ebb66f0d69ce",
    "scripts/item409_j2_actual_rejection_carrier_certificate.py":
        "32c99d596ddf933e00cab032a4af741e0781a361644ddc685d66a4e651a023f7",
    "results/item409_j2_actual_rejection_carrier_certificate.json":
        "b6a68f27d131b9a9e8d7e2512d78d54dbbd7bb70f502b2fbaf8277b6a277f940",
    "manifests/item409_j2_actual_rejection_carrier_manifest.json":
        "b7f052f66eb42215ce0e4778b7a0bb994b3a54e205dae81e8b75715e0220cd71",
    "results/item409_j2_actual_rejection_carrier_root_audit.json":
        "8a7545bbde4b339598a2c92cafbf5902dd1060a4c0d64d46e4590b05accc9674",
    "sources/item413_j2_tied_projection_anti_gcd_boundary_report.md":
        "0ee4ea341cc9ca1701f6b4ea2731d78aa686656ffc086c5c89734fd33b119d00",
    "scripts/item413_j2_tied_projection_anti_gcd_boundary_certificate.py":
        "00420076f3879eb233022227f230fffdab6c8884c050b5ee0876e107fe5830f0",
    "results/item413_j2_tied_projection_anti_gcd_boundary_certificate.json":
        "c2f43f92b151de1a6f349a86d66c1e58250b7e2440c442a24818d488d3ffc1b3",
    "results/item413_j2_tied_projection_anti_gcd_boundary_certificate_replay.json":
        "c2f43f92b151de1a6f349a86d66c1e58250b7e2440c442a24818d488d3ffc1b3",
    "results/item413_j2_tied_projection_anti_gcd_boundary_ledger_delta.json":
        "8a53a9211d43f1d52c5970aaea9f2c3a6dc439c16061114e7981f823c5d48cb0",
    "manifests/item413_j2_tied_projection_anti_gcd_boundary_manifest.json":
        "980997e0476ea3bd3a684cd6cf7af2ec2a3807934e16288ca6ace8c20a589b49",
    "results/item413_j2_tied_projection_anti_gcd_boundary_root_audit.json":
        "a326e2e42258a8d75d24e0ff580297ddd1289ab32380ab332386682fe3db8fcc",
    "results/item413_j2_tied_projection_anti_gcd_boundary_hashes.sha256":
        "cef20125e4b3a6653658685a70ece1020a6f7fee9dee57ac03e982d935d8a54b",
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


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def tied_row(prime: int, r: int, s: int) -> None:
    if not is_prime(prime):
        raise AssertionError((prime, "prime"))
    if r < 1 or r % 2 != 1 or r % 3 == 0 or s < 1:
        raise AssertionError((prime, r, s, "ordinary-j2 range"))
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "tied phase"))


def cutoff_packet(
    *, name: str, prime: int, r: int, s: int, rejection: int, cutoff: int,
    classification: str,
) -> dict[str, Any]:
    tied_row(prime, r, s)
    if rejection <= 0 or cutoff < prime:
        raise AssertionError((name, rejection, cutoff))
    threshold = 2 * r + 3
    support = prime_divisors(rejection)
    base_primes = [q for q in support if q > threshold]
    retained_primes = [q for q in base_primes if q == prime or q > cutoff]
    removed_primes = [q for q in base_primes if q != prime and q <= cutoff]
    tied = prime if prime in support else 1
    base_tail = product(base_primes)
    base_foreign = product([q for q in base_primes if q != prime])
    retained_tail = product(retained_primes)
    retained_foreign = product([q for q in retained_primes if q != prime])
    removed = product(removed_primes)

    if base_tail != tied * base_foreign:
        raise AssertionError((name, "base factorization"))
    if retained_tail != tied * retained_foreign:
        raise AssertionError((name, "retained factorization"))
    if base_tail != removed * retained_tail:
        raise AssertionError((name, "tail cutoff"))
    if base_foreign != removed * retained_foreign:
        raise AssertionError((name, "foreign cutoff"))
    if any(q == prime for q in removed_primes):
        raise AssertionError((name, "removed tied prime"))
    if any(q <= cutoff and q != prime for q in retained_primes):
        raise AssertionError((name, "bad retained support"))
    if retained_foreign > 1:
        omega = len(prime_divisors(retained_foreign))
        if retained_foreign <= prime ** omega:
            raise AssertionError((name, "q>p support count inequality"))
    else:
        omega = 0

    return {
        "name": name,
        "classification": classification,
        "p": prime,
        "r": r,
        "s": s,
        "J": rejection,
        "threshold_2r_plus_3": threshold,
        "cutoff_Y": cutoff,
        "radical_support": support,
        "base_tail": base_tail,
        "base_foreign": base_foreign,
        "removed_pure_foreign": removed,
        "adaptive_tail": retained_tail,
        "adaptive_foreign": retained_foreign,
        "tied_projection": tied,
        "adaptive_foreign_omega": omega,
        "identities": {
            "base": "L_0=j_tie*F_0",
            "adaptive": "L_Y=j_tie*F_Y",
            "cutoff": "L_0=C_Y*L_Y and F_0=C_Y*F_Y",
            "margin": "log(L_0)-log(F_0)=log(L_Y)-log(F_Y)=log(j_tie)",
        },
    }


def actual_item409_witness() -> dict[str, Any]:
    frozen = json.loads(
        (ROOT / "results/item409_j2_actual_rejection_carrier_certificate.json")
        .read_text(encoding="utf-8")
    )
    row = next(
        entry for entry in frozen["actual_rows_replay"]["rows"]
        if entry["p"] == 709
    )
    packet = cutoff_packet(
        name="item409_actual_witness",
        prime=709,
        r=347,
        s=2,
        rejection=row["J"],
        cutoff=709,
        classification="EXACT PINNED ACTUAL-FORMULA WITNESS / NOT A CENSUS",
    )
    if row["J"] != 79 or packet["tied_projection"] != 1:
        raise AssertionError((row, packet))
    return packet


def declared_packets() -> dict[str, Any]:
    classification = "EXACT ALGEBRAIC SUPPORT PACKET / NOT ACTUAL"
    rows = [
        cutoff_packet(
            name="middle_foreign_removed_at_p",
            prime=19, r=5, s=1, rejection=17, cutoff=19,
            classification=classification,
        ),
        cutoff_packet(
            name="tied_middle_and_high_foreign",
            prime=19, r=5, s=1,
            rejection=17 * 19 * 31 * 37, cutoff=31,
            classification=classification,
        ),
        cutoff_packet(
            name="all_tail_foreign",
            prime=19, r=5, s=1, rejection=23 * 31, cutoff=19,
            classification=classification,
        ),
        cutoff_packet(
            name="tied_only_after_cutoff",
            prime=31, r=11, s=1, rejection=29 * 31, cutoff=31,
            classification=classification,
        ),
    ]
    if rows[0]["removed_pure_foreign"] != 17 or rows[0]["adaptive_tail"] != 1:
        raise AssertionError(rows[0])
    if rows[1]["adaptive_tail"] != 19 * 37:
        raise AssertionError(rows[1])
    if rows[3]["adaptive_tail"] != 31:
        raise AssertionError(rows[3])
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": (
            "EXACT ALGEBRAIC SUPPORT PACKETS / NOT ACTUAL CONNECTION VALUES / "
            "NO PRIME CENSUS"
        ),
        "rows": rows,
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
    }


def transport(prime: int, r: int, s: int, foreign: int) -> dict[str, Any]:
    tied_row(prime, r, s)
    if not is_prime(foreign) or foreign <= prime:
        raise AssertionError((prime, foreign, "forward foreign prime"))
    threshold = 2 * r + 3
    difference = foreign - threshold
    aligned = difference % 6 == 0
    source_M = (r + 7 * prime) // 6
    if 6 * source_M != r + 7 * prime:
        raise AssertionError((prime, r, source_M, "source M"))
    result: dict[str, Any] = {
        "p": prime,
        "r": r,
        "s": s,
        "q_foreign": foreign,
        "source_M": source_M,
        "residue_aligned": aligned,
    }
    if aligned:
        future_s = difference // 6
        future_M = (r + 7 * foreign) // 6
        if future_s < 1 or 6 * future_M != r + 7 * foreign:
            raise AssertionError((result, "future row integrality"))
        if foreign != 2 * r + 6 * future_s + 3:
            raise AssertionError((result, "future tied phase"))
        if future_M - source_M != 7 * (foreign - prime) // 6:
            raise AssertionError((result, "forward displacement"))
        if future_M <= source_M:
            raise AssertionError((result, "not forward"))
        result.update({
            "future_s": future_s,
            "future_M": future_M,
            "future_displacement": future_M - source_M,
            "transport_conclusion": (
                "if q divides the actual r-only Pi_r, q is the tied prime of "
                "this future degenerate-gate row; no target status is transferred"
            ),
        })
    else:
        result["transport_conclusion"] = (
            "q has no same-r ordinary-j2 tied row; it is transverse residue pollution"
        )
    return result


def transport_replay() -> dict[str, Any]:
    rows = [
        transport(19, 5, 1, 31),
        transport(19, 5, 1, 37),
        transport(19, 5, 1, 23),
        transport(17, 1, 2, 23),
        transport(17, 1, 2, 19),
    ]
    aligned = [row for row in rows if row["residue_aligned"]]
    transverse = [row for row in rows if not row["residue_aligned"]]
    if len(aligned) != 3 or len(transverse) != 2:
        raise AssertionError(rows)
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": "EXACT GEOMETRY REPLAY / SUPPORT EXAMPLES NOT ACTUAL",
        "rows": rows,
        "aligned_rows": len(aligned),
        "transverse_rows": len(transverse),
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
        "theorem": (
            "for actual q>p dividing the aligned foreign support, q|Pi_r and "
            "q=2r+6t+3 give a unique future actual degenerate-gate row at "
            "M_q=(r+7q)/6>M"
        ),
        "target_warning": (
            "q not dividing the source Gamma_(r,s) does not determine "
            "Gamma_(r,t); the Item409 period replacement is tied-p-specific"
        ),
    }


def frac(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def capacity_replay() -> dict[str, Any]:
    ray = F(1, 35)
    scenarios = []
    for name, tail, foreign, g, n in (
        ("no_linear_input", F(0), F(0), ray, F(0)),
        ("adaptive_half_ray_matched", F(1, 70), F(0), ray, F(0)),
        ("adaptive_tail_cancelled", F(1, 35), F(1, 35), ray, F(0)),
        ("chart_only", F(0), F(0), F(1, 140), F(1, 140)),
    ):
        direct = max(F(0), tail - foreign)
        chart = max(F(0), ray - g - n)
        saving = max(direct, chart) / 6
        scenarios.append({
            "name": name,
            "adaptive_tail_lower_per_M": frac(tail),
            "adaptive_foreign_upper_per_M": frac(foreign),
            "direct_margin_per_M": frac(direct),
            "chart_margin_per_M": frac(chart),
            "normalized_saving": frac(saving),
        })
    if scenarios[1]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[1])
    if scenarios[2]["normalized_saving"] != "0/1":
        raise AssertionError(scenarios[2])
    if scenarios[3]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[3])
    return {
        "classification": "EXACT RATIONAL CAPACITY ARITHMETIC",
        "one_ray_mass_per_M": "1/35",
        "formula": (
            "A_Y>=aM, B_Y<=bM, G<=gM, N<=nM imply normalized saving "
            ">=max(0,a-b,1/35-g-n)/6"
        ),
        "cutoff_invariance": (
            "raising Y removes the same foreign mass from A_Y and B_Y and "
            "therefore cannot by itself change A_Y-B_Y=J_e"
        ),
        "scenarios": scenarios,
        "proved_adaptive_tail_lower_per_M": 0,
        "proved_adaptive_foreign_linear_upper_per_M": None,
        "proved_matched_J_lower_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_ordinary_j2_ceiling_per_6M": "1/105",
    }


def build_payload() -> dict[str, Any]:
    dependencies = verify_dependencies()
    return {
        "item": 416,
        "schema": "item416-j2-adaptive-foreign-tail-transport-v1",
        "title": "adaptive selected-prime saturation and forward foreign-tail transport",
        "checked_date_beijing": "2026-09-01",
        "status": "PROVED_ADAPTIVE_CUTOFF_AND_FORWARD_GATE_TRANSPORT_ETA_ZERO",
        "dependency_hashes_verified": dependencies,
        "adaptive_cutoff_theorem": {
            "definition": (
                "for Y_(r,s)>=p, remove from J every prime <=Y except p; "
                "L_Y is the radical of the remainder and F_Y=(L_Y)_(p)"
            ),
            "support": "supp(L_Y) is contained in {p} union {q:q>Y}",
            "rowwise_factorization": "L_Y=j_tie*F_Y with gcd(j_tie,F_Y)=1",
            "aggregate_identity": "A_Y(M)-B_Y(M)=J_e(M)=D_e(M)-G_e(M)",
            "monotonicity": (
                "if Y_2>=Y_1>=p, A_(Y1)-A_(Y2)=B_(Y1)-B_(Y2)>=0"
            ),
            "selected_prime_cutoff": (
                "Y=p discards every Item413 foreign factor in "
                "2r+3<q<p without changing tied support"
            ),
        },
        "actual_item409_witness": actual_item409_witness(),
        "declared_cutoff_packets": declared_packets(),
        "forward_transport": transport_replay(),
        "unconditional_size_screen": {
            "input": (
                "Item349 gives log J<=log Pi_r=O(r log r); on a fixed ray "
                "1<=r<=2M/5+O(1), and the prime-row count is O(M/log M)"
            ),
            "radical_weight_bound": "B_(Y=p)(M)=O(M^2)",
            "foreign_factor_incidence_bound": "sum omega(F_p)=O(M^2/log M)",
            "incidence_inequality": (
                "because every q in F_p satisfies q>p, F_p>p^omega(F_p) "
                "when F_p>1"
            ),
            "valuation_warning": (
                "B counts radical support once; valuation depth in J is neither "
                "credited nor needed for the displayed bounds"
            ),
            "capacity_screen": (
                "O(M^2) is superlinear and gives neither B_p=o(M) nor a finite "
                "linear coefficient; it is noncompetitive for the ledger"
            ),
        },
        "capacity": capacity_replay(),
        "scoped_obstruction": {
            "classification": "SCOPED TO CUTOFF, HEIGHT, AND SAME-r FORWARD TRANSPORT",
            "statements": [
                "raising the cutoff cannot create a matched margin because the removed mass is identically foreign",
                "aligned q>p transport proves only a future degenerate gate, not a future collision or rejection",
                "transverse q>p has no same-r ordinary-j2 row",
                "the inherited pointwise height gives only O(M^2) foreign radical weight",
            ],
            "not_excluded": [
                "a formula-specific large-prime theorem for Pi_r",
                "an unmatched cross-r resultant controlling transverse support",
                "a reciprocity law transporting the actual target residual",
                "an average weighted theorem for aligned or transverse foreign factors",
            ],
        },
        "smallest_missing_lemmas": {
            "foreign_closer": (
                "B_p(M)=sum log rad_{q>p} J_(r,s)=o(M), or separate o(M) "
                "bounds for its aligned and transverse pieces"
            ),
            "builder_pair": (
                "A_p(M)>=aM+o(M) together with B_p(M)<=bM+o(M), a>b"
            ),
            "direct_channel_closer": "A_p(M)=o(M), which would force J_e(M)=o(M)",
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "adaptive selected-prime-safe saturation and exact cutoff invariance",
                "removal of all 2r+3<q<p foreign contamination without changing tied support",
                "aligned q>p forward transport to a unique future actual degenerate-gate row",
                "the O(M^2) radical-weight and O(M^2/log M) incidence screens",
                "zero new booking and zero capacity reduction",
            ],
            "EXACT_PINNED_ACTUAL_WITNESS_NOT_A_CENSUS": [
                "the Item409 row (709,347,2) with J=79"
            ],
            "EXACT_ALGEBRAIC_SUPPORT_PACKETS_NOT_ACTUAL": [
                "the declared cutoff and transport examples"
            ],
            "CONDITIONAL": [
                "every positive saving whose adaptive tail, foreign, G, or N antecedent is explicit"
            ],
            "OPEN": [
                "B_p=o(M) and its aligned/transverse components",
                "any positive adaptive-tail minus foreign-tail margin",
                "any target-status transport for aligned foreign primes",
                "Route 1 and every conclusion about e+pi",
            ],
        },
        "evidence_policy": {
            "canonical_files_modified": True,
            "no_prime_or_collision_census": True,
            "no_finite_extrapolation": True,
            "no_foreign_factor_booking": True,
            "no_transport_of_target_status": True,
            "no_countermodel_claimed_actual": True,
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
        "item": 416,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
        "new_booking": payload["capacity"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
