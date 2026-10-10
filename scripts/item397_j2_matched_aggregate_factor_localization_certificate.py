#!/usr/bin/env python3
"""Deterministic certificate for Item 397.

The checker replays Item 394's actual matched factors, their sharp
pairwise localization, the exact envelope-constant decomposition, and
the two endpoint phase identities.  Finite rows are diagnostic only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item397_j2_matched_aggregate_factor_localization_certificate.json"

DEPENDENCIES = {
    "sources/item394_j2_matched_modulus_aggregate_collapse_report.md":
        "f0fd654dc80ad3c0eab26abfd8f8741e89ba572f825ef5afd214f2c149c01204",
    "scripts/item394_j2_matched_modulus_aggregate_collapse_certificate.py":
        "f75e9637cb6d120f748ffe82b746275c978a3301f623ac67218f0932e7916e08",
    "results/item394_j2_matched_modulus_aggregate_collapse_certificate.json":
        "7d3fb95d1fe09d9508aa7e12d4bb87ef6f33887645f6691b64cd71fa2a0a56e1",
    "results/item394_j2_matched_modulus_aggregate_collapse_ledger_delta.json":
        "dcde114b5ba5d0a793a7fa80b8b142505ac86835ae62640969ee0d08ac19cd53",
    "sources/item315_j2_resultant_arithmetic_report.md":
        "3ce61af707268ceed6db0355a31333492bd8b07ec34e455cbee874fc6a2291b8",
    "sources/item361_j2_matched_cartier_norm_collapse_report.md":
        "0ad329d64d00853fd1b8adca1c982790bd293f01bdc1ea356ad3858374683af8",
    "sources/item392_j2_growing_window_aggregate_no_go_report.md":
        "9fd149b27a8ca64c727c35fca4cd8a196da0d9172883b31bb3aa75c45873bb7a",
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


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lcm(left: int, right: int) -> int:
    return abs(left // math.gcd(left, right) * right)


def product(values) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def constant_decomposition() -> dict[str, Any]:
    C6 = F(
        6979177263689987598318,
        56080510212831201972875,
    )
    raw = F(2, 35)
    composite = C6 - raw
    expected = F(
        3774576680099633199868,
        56080510212831201972875,
    )
    if composite != expected:
        raise AssertionError((composite, expected))
    alpha = F(4, 5)
    beta = F(6, 7)
    if beta - alpha != raw:
        raise AssertionError((beta - alpha, raw))
    if not beta / 5 < alpha:
        raise AssertionError("u>=5 support is not below the row interval")
    return {
        "C6_fraction": f"{C6.numerator}/{C6.denominator}",
        "C6_decimal": float(C6),
        "raw_fraction": "2/35",
        "raw_decimal": float(raw),
        "composite_fraction": (
            f"{composite.numerator}/{composite.denominator}"
        ),
        "composite_decimal": float(composite),
        "normalized": {
            "C6_over_6": float(C6 / 6),
            "raw_over_6": float(raw / 6),
            "composite_over_6": float(composite / 6),
        },
        "fraction_of_envelope_removed": float(composite / C6),
        "fraction_of_envelope_retained": float(raw / C6),
        "support_separation": {
            "u=1": "(4/5,6/7]",
            "u>=5_upper_bound": "6/35",
            "6/35_less_than_4/5": True,
        },
    }


def sharp_slice_replay(i394_payload: dict[str, Any], i394: Any) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for slice_data in i394_payload["actual_formula_slice_replays"]:
        M = slice_data["M"]
        lower, upper = slice_data["interval"]
        if not upper < 2 * lower:
            raise AssertionError((M, lower, upper))
        low_support = i394.primorial(lower - 1)
        rows = slice_data["rows"]
        sharp_rows: list[tuple[int, int]] = []
        for row in rows:
            d_value = row["d_matched"]
            sharp = i394.largest_divisor_coprime_to(d_value, low_support)
            expected = (
                row["q"]
                if row["prime"] and row["actual_collision"]
                else 1
            )
            if sharp != expected:
                raise AssertionError((M, row["q"], sharp, expected))
            sharp_rows.append((row["q"], sharp))

        pair_checks = 0
        for index, (q_left, d_left) in enumerate(
            (row["q"], row["d_matched"]) for row in rows
        ):
            for q_right, d_right in (
                (row["q"], row["d_matched"]) for row in rows[index + 1:]
            ):
                common = math.gcd(d_left, d_right)
                if math.gcd(q_left, q_right) % common:
                    raise AssertionError((M, q_left, q_right, common))
                if common > abs(q_left - q_right):
                    raise AssertionError((M, q_left, q_right, common))
                if common >= lower:
                    raise AssertionError((M, q_left, q_right, common, lower))
                pair_checks += 1

        sharp_product = product(value for _, value in sharp_rows)
        sharp_lcm = 1
        for _, value in sharp_rows:
            sharp_lcm = lcm(sharp_lcm, value)
        if sharp_product != sharp_lcm:
            raise AssertionError((M, sharp_product, sharp_lcm))
        if sharp_lcm != slice_data["aggregate_sharp"]:
            raise AssertionError((
                M, sharp_lcm, slice_data["aggregate_sharp"]
            ))
        output.append({
            "M": M,
            "interval": [lower, upper],
            "rows": len(rows),
            "pair_checks": pair_checks,
            "sharp_nontrivial_rows": sum(value > 1 for _, value in sharp_rows),
            "sharp_product": sharp_product,
            "sharp_lcm": sharp_lcm,
            "sharp_row_digest_sha256": hashlib.sha256(
                ("\n".join(f"{q},{value}" for q, value in sharp_rows) + "\n")
                .encode("ascii")
            ).hexdigest(),
        })
    return output


def phase_row(prime: int, r: int, s: int) -> dict[str, Any]:
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s))
    residue = r % 6
    if residue == 1:
        k = (2 * r + 1) // 3
        if 3 * k != 2 * r + 1 or prime % 6 != 5:
            raise AssertionError((prime, r, s, k))
        phase = pow(2, k + 2 * s, prime)
        if 2 * pow(phase, 3, prime) % prime != 1:
            raise AssertionError((prime, r, s, phase, "cube root of half"))
        if math.gcd(3, prime - 1) != 1:
            raise AssertionError((prime, "cube map not bijective"))
        equation = "t^3=1/2; unique because gcd(3,p-1)=1"
    elif residue == 5:
        k = (2 * r + 2) // 3
        if 3 * k != 2 * r + 2 or prime % 6 != 1:
            raise AssertionError((prime, r, s, k))
        phase = pow(2, k + 2 * s, prime)
        if pow(phase, 3, prime) != 1:
            raise AssertionError((prime, r, s, phase, "cube root of one"))
        equation = "t^3=1; t lies in mu_3(F_p)"
    else:
        raise AssertionError((prime, r, residue))
    return {
        "p": prime,
        "r": r,
        "s": s,
        "ray": residue,
        "k": k,
        "phase": phase,
        "equation": equation,
    }


def phase_replay() -> dict[str, Any]:
    declared = [
        (17, 1, 2),
        (29, 1, 4),
        (83, 19, 7),
        (271, 113, 7),
        (383, 109, 27),
        (2281, 5, 378),
    ]
    rows = [phase_row(*row) for row in declared]
    rays = {1: 0, 5: 0}
    for row in rows:
        rays[row["ray"]] += 1
    if not all(rays.values()):
        raise AssertionError(rays)
    return {
        "classification": "EXACT FINITE ONLY / DIAGNOSTIC",
        "declared_rows": rows,
        "ray_counts": {str(key): value for key, value in rays.items()},
        "symbolic_all_row_statement": {
            "r_mod_6=1": "p mod 6=5 and t^3=1/2 has a unique solution",
            "r_mod_6=5": "p mod 6=1 and the selected t always satisfies t^3=1",
        },
    }


def build_payload() -> dict[str, Any]:
    dependency_actuals = verify_dependencies()
    i394 = load(
        "item397_i394",
        "scripts/item394_j2_matched_modulus_aggregate_collapse_certificate.py",
    )
    payload394 = i394.build_payload()
    frozen394 = json.loads(
        (ROOT / "results/item394_j2_matched_modulus_aggregate_collapse_certificate.json")
        .read_text(encoding="utf-8")
    )
    if payload394 != frozen394:
        raise AssertionError("Item394 deterministic reconstruction mismatch")

    return {
        "item": 397,
        "title": "ordinary-j2 matched-aggregate factor localization",
        "checked_date_beijing": "2026-09-01",
        "status": "proved_eta_zero_factor_localization_obstruction",
        "dependency_hashes_verified": dependency_actuals,
        "evidence_policy": {
            "finite_rows_and_phases": "EXACT FINITE ONLY / DIAGNOSTIC",
            "no_asymptotic_inference_from_enumeration": True,
        },
        "proved_theorems": {
            "envelope_decomposition": "C6=2/35+C_comp",
            "C_comp": (
                "3774576680099633199868/"
                "56080510212831201972875"
            ),
            "atomic_localization": (
                "d_(M,q)^sharp is q exactly for an actual prime collision, "
                "and is 1 otherwise"
            ),
            "pairwise_localization": (
                "for q!=q', gcd(d_(M,q),d_(M,q')) divides "
                "gcd(q,q') and |q-q'|<L_M"
            ),
            "sharp_pairwise_coprimality": (
                "gcd(d_(M,q)^sharp,d_(M,q')^sharp)=1"
            ),
            "reciprocity_no_ray_exclusion": (
                "the endpoint phase equation is soluble on both actual rays"
            ),
            "proved_eta": 0,
        },
        "constant_certificate": constant_decomposition(),
        "actual_formula_sharp_slice_replays": sharp_slice_replay(
            payload394, i394
        ),
        "phase_replay": phase_replay(),
        "ledger": {
            "eta_per_M": 0,
            "delta_r1": 0,
            "delta_booked_capacity": 0,
            "ordinary_j2_raw_normalized_ceiling": "1/105",
            "closed_mechanism": (
                "strict saving from shared factors among distinct matched "
                "rows, or from endpoint phase solvability alone"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / RESULT_NAME)
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
        "item": 397,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
