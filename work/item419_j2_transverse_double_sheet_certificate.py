#!/usr/bin/env python3
"""Deterministic certificate for Item 419.

The checker certifies the exact parity/double-Frobenius geometry of a
transverse q>p foreign prime and the algebraic-height refinement of the
foreign-tail screen.  Declared rows are geometry replays only: no foreign
prime is asserted to divide the actual carrier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item419_j2_transverse_double_sheet_certificate.json"

DEPENDENCIES = {
    "sources/item250_j2_ordinary_phase_report.md":
        "56339ec89876abd68627d03b2d3e4e4d1c0fdc8b8d20a59afb274cb7dafe98ce",
    "results/item250_j2_ordinary_phase_certificate.json":
        "6f8d0165448dd8949436649e2824a14578c1bce08e8875a6fd88f770c72cb5e3",
    "results/item250_root_audit.json":
        "30645b03da6b217ef27dc5fac07d2a0d15b7b3a7e06577e23a720f713f15899e",
    "sources/item314_j2_two_branch_gate_report.md":
        "266f70523770a2a4147ee75289885fcb8dc945a65b650f2c8411e005ba110faa",
    "results/item314_j2_two_branch_gate_certificate.json":
        "77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1",
    "results/item314_root_audit.json":
        "e537cdfa34ddd47bc902fd66b6a64679ca2bd60e12b31ddedfe4009cdcc6c2e6",
    "sources/item315_j2_resultant_arithmetic_report.md":
        "3ce61af707268ceed6db0355a31333492bd8b07ec34e455cbee874fc6a2291b8",
    "results/item315_j2_resultant_arithmetic_certificate.json":
        "09fdd67a6535a043bcbd1e2a46c4b14a633b9928a5f1c65618c34fab65cfabb6",
    "results/item315_root_audit.json":
        "b764ea214de0c99a6398c981a5d35ca5b911c4d08e7e128f55276a30b1ea66d6",
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "results/item349_j2_degenerate_triple_minor_carrier_root_audit.json":
        "e717c01d7429f7821a7ee75e8d979bc1362107bd70466af6af54d9748299a894",
    "sources/item409_j2_actual_rejection_carrier_report.md":
        "99caf10f9f1561dcb0e3a712f381db639b8260da6594dd305915ebb66f0d69ce",
    "results/item409_j2_actual_rejection_carrier_certificate.json":
        "b6a68f27d131b9a9e8d7e2512d78d54dbbd7bb70f502b2fbaf8277b6a277f940",
    "results/item409_j2_actual_rejection_carrier_root_audit.json":
        "8a7545bbde4b339598a2c92cafbf5902dd1060a4c0d64d46e4590b05accc9674",
    "sources/item413_j2_tied_projection_anti_gcd_boundary_report.md":
        "0ee4ea341cc9ca1701f6b4ea2731d78aa686656ffc086c5c89734fd33b119d00",
    "results/item413_j2_tied_projection_anti_gcd_boundary_certificate.json":
        "c2f43f92b151de1a6f349a86d66c1e58250b7e2440c442a24818d488d3ffc1b3",
    "results/item413_j2_tied_projection_anti_gcd_boundary_root_audit.json":
        "a326e2e42258a8d75d24e0ff580297ddd1289ab32380ab332386682fe3db8fcc",
    "sources/item416_j2_adaptive_foreign_tail_transport_report.md":
        "66cde3c776df067b600038ff16734e120036274b1e248b7c4644d0564fcc2e30",
    "results/item416_j2_adaptive_foreign_tail_transport_certificate.json":
        "3effb6a6162df9c5639ca155721adb165ed60ff0656d09aac5851c1ffd0bc64b",
    "results/item416_j2_adaptive_foreign_tail_transport_root_audit.json":
        "a98e3f6744ad3ed1e42c242bbf5c70fbf1b0bf36cd9f9f5b30a0786f06bfba7c",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> dict[str, str]:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
    return dict(DEPENDENCIES)


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


def geometry_row(p: int, r: int, s: int, foreign_q: int) -> dict[str, Any]:
    kstar = 2 * r + 3
    if not (is_prime(p) and p == kstar + 6 * s and s >= 1):
        raise AssertionError((p, r, s, "actual source row"))
    if r % 2 != 1 or r % 3 == 0:
        raise AssertionError((p, r, "ordinary j=2 r"))
    if not (is_prime(foreign_q) and foreign_q > p):
        raise AssertionError((foreign_q, p, "forward foreign prime"))
    if foreign_q % 6 == kstar % 6:
        raise AssertionError((foreign_q, r, "not transverse"))

    numerator = 2 * foreign_q - kstar
    if numerator % 3:
        raise AssertionError((foreign_q, r, "nonintegral double-sheet Q"))
    q_lift = numerator // 3
    if not (0 < q_lift < foreign_q and q_lift % 2 == 1):
        raise AssertionError((foreign_q, r, q_lift, "odd lift"))
    if 3 * q_lift + kstar != 2 * foreign_q:
        raise AssertionError((foreign_q, r, q_lift, "double resonance"))

    # The terminal J_(kstar+2) denominators.  They are all even.  Their
    # range ends at 2q, so the only q-multiple is the top denominator 2q.
    terminal_denominators = [
        q_lift + kstar + 2 + 2 * t for t in range(q_lift)
    ]
    q_multiples = [value for value in terminal_denominators if value % foreign_q == 0]
    if q_multiples != [2 * foreign_q]:
        raise AssertionError((foreign_q, r, q_lift, q_multiples))
    if terminal_denominators[-1] != 2 * foreign_q:
        raise AssertionError((foreign_q, terminal_denominators[-1]))
    if any(value % 2 for value in terminal_denominators):
        raise AssertionError((foreign_q, r, "terminal parity"))

    # The ordinary upper-B common-period integer D ceases to be integral.
    upper_d_numerator = r + q_lift + 1
    if upper_d_numerator % 2 != 1:
        raise AssertionError((foreign_q, r, q_lift, "B parity should flip"))

    M_source = (r + 7 * p) // 6
    if r + 7 * p != 6 * M_source:
        raise AssertionError((p, r, "fixed-M source"))

    return {
        "classification": "EXACT GEOMETRY REPLAY ONLY / q IS NOT ASSERTED TO DIVIDE J",
        "p": p,
        "r": r,
        "s": s,
        "M": M_source,
        "foreign_q": foreign_q,
        "source_phase_mod_6": kstar % 6,
        "foreign_phase_mod_6": foreign_q % 6,
        "Q_perp": q_lift,
        "Q_perp_parity": "odd",
        "resonance": f"3*{q_lift}+{kstar}=2*{foreign_q}",
        "terminal_q_multiples": q_multiples,
        "top_binomial_coefficient": 1,
        "normalized_terminal_residue": 1,
        "ordinary_upper_B_D": f"{upper_d_numerator}/2",
        "ordinary_upper_B_D_is_integral": False,
    }


def geometry_replay() -> dict[str, Any]:
    declared = [
        (23, 7, 1, 43),
        (61, 23, 2, 89),
        (71, 31, 1, 79),
        (131, 55, 3, 139),
        (823, 407, 1, 1019),
    ]
    rows = [geometry_row(*row) for row in declared]
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": (
            "DECLARED EXACT PARAMETER REPLAY ONLY / NO CARRIER DIVISIBILITY / "
            "NO PRIME CENSUS / NO DENSITY EXTRAPOLATION"
        ),
        "rows": rows,
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
    }


def capacity_screen() -> dict[str, Any]:
    return {
        "actual_divisibility_chain": (
            "F_perp_(r,s) divides rad(J_(r,s)), J_(r,s) divides Pi_r, "
            "and Pi_r divides abs(num(a_r))"
        ),
        "sequence_specific_input": (
            "Item 314 proves the algebraic branch coefficient a_r has "
            "logarithmic height O(r), hence log abs(num(a_r))=O(r)"
        ),
        "actual_fixed_M_row_count": "O(M/log M) on one ray",
        "actual_r_range": "0<r<=2M/5",
        "proved_weighted_bound_transverse": "B_perp_e(M)=O(M^2/log M)",
        "proved_weighted_bound_full_forward_tail": "B^[p]_e(M)=O(M^2/log M)",
        "proved_support_count": (
            "sum omega(F^[p]_(r,s))=O(M^2/(log M)^2), since every q>p>>M"
        ),
        "strict_improvement_over_item416": (
            "O(M^2/log M) replaces O(M^2) for weighted mass; "
            "O(M^2/(log M)^2) replaces O(M^2/log M) for support count"
        ),
        "capacity_warning": (
            "the upper bound divided by M is O(M/log M), not a finite linear "
            "coefficient and not o(M)"
        ),
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_ordinary_j2_ceiling": "1/105",
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 419,
        "schema": "item419-j2-transverse-double-sheet-v1",
        "title": "transverse double-Frobenius parity boundary and algebraic-height tail screen",
        "checked_date_beijing": "2026-09-01",
        "status": "PROVED_SHARPER_ACTUAL_BOUND_AND_SCOPED_TRANSPORT_NO_GO_ZERO_BOOKING",
        "dependency_hashes_verified": verify_dependencies(),
        "theorem": {
            "transverse_lift": (
                "for q>p with q mod 6 opposite to 2r+3 mod 6, "
                "Q_perp=(2q-2r-3)/3 is the unique integer lift in (0,q); "
                "it is odd and 3Q_perp+2r+3=2q"
            ),
            "A_terminal": (
                "the J_(2r+5) denominator string is even and ends at 2q, "
                "so its sole q-multiple is 2q with top binomial coefficient 1; "
                "the normalized affine terminal remains (c-1)/(Q+2r+3)"
            ),
            "B_parity_break": (
                "D=(r+Q_perp+1)/2 is a half-integer, so Item 250's ordinary "
                "upper-B common factorial period and f-vector do not transport"
            ),
            "scope": (
                "this proves a parity/double-Frobenius obstruction to same-r "
                "gate transport; it does not identify the source target/rejection "
                "with any odd-Q object"
            ),
        },
        "geometry_replay": geometry_replay(),
        "capacity": capacity_screen(),
        "scoped_no_go": {
            "closed": [
                "treating a transverse q as a future ordinary same-r row",
                "reusing the Item 250/409 f-vector or target residual at odd Q without rederivation",
                "claiming an o(M) tail from the newly sharpened height bound alone",
            ],
            "not_closed": [
                "a separately derived parity-flipped B-tail with a bridge to the source target",
                "a formula-specific average gcd or modular zero-density theorem",
                "B_perp_e(M)=o(M) or any positive tail-minus-foreign margin",
                "the ordinary-j2 cell, Route 1, or any conclusion about e+pi",
            ],
        },
        "smallest_missing_lemma": {
            "statement": (
                "prove sum log rad_(q>p, transverse) J_(r,s)=o(M) on an actual "
                "fixed-M ray, using a formula-specific zero-density theorem; "
                "double-sheet geometry and algebraic height alone are insufficient"
            ),
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "transverse odd lift and double resonance",
                "unique top 2q terminal pole and unchanged normalized A-terminal",
                "ordinary upper-B parity obstruction",
                "actual O(M^2/log M) weighted-tail and O(M^2/(log M)^2) support screens",
                "zero booking and zero capacity reduction",
            ],
            "EXACT_GEOMETRY_REPLAY_ONLY": [
                "the five declared source/foreign parameter quadruples; no q-divisibility is asserted"
            ],
            "OPEN": [
                "every o(M) weighted-tail theorem",
                "every target/rejection transport theorem",
                "every numerical Route-1 improvement",
            ],
        },
        "evidence_policy": {
            "no_prime_or_collision_census": True,
            "no_declared_foreign_factor_claimed_actual": True,
            "gate_distinguished_from_target_and_rejection": True,
            "no_finite_extrapolation": True,
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
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "item": 419,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
        "new_booking": payload["capacity"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
