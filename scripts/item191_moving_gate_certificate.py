#!/usr/bin/env python3
"""Exact finite certificate for gates on the moving rank-two locus.

Every coordinate is reconstructed from the local Hasse recurrence; no
Cartier scalar is inverted.  The all-degree theorem is proved in the report;
this script provides exact finite replay and concrete gate witnesses.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
import hashlib
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCHIVE = Path(__file__).resolve().parents[1]
RESULT_NAME = "item191_moving_gate_certificate.json"
sys.path.insert(0, str(HERE))
import item180_moving_residual_certificate as moving


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def default_output() -> Path:
    return HERE.parent / "results" / RESULT_NAME if HERE.name.lower() == "scripts" else HERE / RESULT_NAME


def dependency_dir() -> Path:
    names = (
        "item163_deeper_digits_certificate.py",
        "lifted_endpoint_hasse_extended_certificate.py",
        "lifted_endpoint_hasse_certificate.py",
    )
    if all((HERE / name).exists() for name in names):
        return HERE
    return ARCHIVE / "scripts"


def label(p: int, s: int) -> str:
    labs = moving.known_ray_labels(p, s)
    return "+".join(labs) if labs else "off-ray"


def allowed_js(p: int, s: int) -> list[int]:
    top = (p * p - 2 * s - 2) // (2 * p)
    parity = s & 1
    return [j for j in range(1, top + 1) if (j & 1) == parity]


def interpolate_degree(values: list[int], p: int) -> int:
    cur = [v % p for v in values]
    if not any(cur):
        return -1
    degree = 0
    while len(cur) > 1:
        if all(value == cur[0] for value in cur):
            return degree
        cur = [(cur[k + 1] - cur[k]) % p for k in range(len(cur) - 1)]
        degree += 1
    return degree


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=43)
    ap.add_argument("--precision", type=int, default=4)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if args.precision < 4:
        raise ValueError("precision 4 is needed for A0,A1,B0")

    deps = dependency_dir()
    item163_path = deps / "item163_deeper_digits_certificate.py"
    extended_path = deps / "lifted_endpoint_hasse_extended_certificate.py"
    base_path = deps / "lifted_endpoint_hasse_certificate.py"
    item180_path = HERE / "item180_moving_residual_certificate.py"
    if not item180_path.exists():
        item180_path = ARCHIVE / "scripts" / "item180_moving_residual_certificate.py"
    item163 = load("item191_item163", item163_path)
    extended = load("item191_extended", extended_path)

    rows = []
    groups = []
    for p in moving.primes_upto(args.prime_max):
        for s in range((p - 1) // 3 + 1):
            if moving.determinant_mod_p(p, s):
                continue
            group_rows = []
            for j in allowed_js(p, s):
                m = (j * p + s) // 2
                l0, x0, e0, bands0 = item163.coordinates_mod(
                    extended, m, 4 * m + 1, p, args.precision
                )
                l1, x1, e1, bands1 = item163.coordinates_mod(
                    extended, m, 4 * m + 2, p, args.precision
                )
                mod = p ** args.precision
                da = (l1 * x0 - l0 * x1) % mod
                db = (l1 * e0 - l0 * e1) % mod
                if da % p or db % p:
                    raise AssertionError((p, s, j, da, db))
                a0 = da // p % p
                a1 = da // (p * p) % p
                b0 = db // p % p
                row = {
                    "p": p,
                    "s": s,
                    "j": j,
                    "m": m,
                    "t": (j - (1 if s & 1 else 2)) // 2,
                    "label": label(p, s),
                    "A0": a0,
                    "A1": a1,
                    "B0": b0,
                    "passes_p2": a0 == 0,
                    "passes_p3": a0 == a1 == b0 == 0,
                    "band_indices": sorted(set(bands0) | set(bands1)),
                }
                rows.append(row)
                group_rows.append(row)
            for key in ("A0", "A1", "B0"):
                # Nodes t are consecutive, so ordinary differences apply.
                pass
            groups.append(
                {
                    "p": p,
                    "s": s,
                    "label": label(p, s),
                    "j_count": len(group_rows),
                    "A0_values": [r["A0"] for r in group_rows],
                    "A1_values": [r["A1"] for r in group_rows],
                    "B0_values": [r["B0"] for r in group_rows],
                    "A0_interpolation_degree": interpolate_degree([r["A0"] for r in group_rows], p),
                    "A1_interpolation_degree": interpolate_degree([r["A1"] for r in group_rows], p),
                    "B0_interpolation_degree": interpolate_degree([r["B0"] for r in group_rows], p),
                    "A0_zero_js": [r["j"] for r in group_rows if r["A0"] == 0],
                    "B0_zero_js": [r["j"] for r in group_rows if r["B0"] == 0],
                    "p3_js": [r["j"] for r in group_rows if r["passes_p3"]],
                }
            )

    by_label = Counter(r["label"] for r in rows)
    a0_by_label = Counter(r["label"] for r in rows if r["passes_p2"])
    p3_by_label = Counter(r["label"] for r in rows if r["passes_p3"])
    regular_tail = [
        r for r in rows if 3 * r["j"] - 1 >= r["p"] and 2 * r["j"] + 2 <= r["p"]
    ]
    regular_tail_failures = [r for r in regular_tail if r["A0"] or r["B0"]]
    cubic_witnesses = [r for r in rows if r["passes_p3"]]
    if regular_tail_failures:
        raise AssertionError(("regular tail", regular_tail_failures[:3]))
    for row in rows:
        if row["passes_p3"] and not row["passes_p2"]:
            raise AssertionError(("gate nesting", row))

    output = {
        "schema": "item191-moving-ranktwo-gates-v1",
        "status": {
            "actual_scalar_free_gate_formula": "PROVED_IN_REPORT",
            "regular_second_cartier_tail": "PROVED_IN_REPORT",
            "finite_replay": "EXACT_FINITE_ONLY",
            "positive_weighted_entry_support": "OPEN",
            "positive_weighted_lift_support": "OPEN",
        },
        "scope": {"prime_max": args.prime_max, "precision": args.precision},
        "definitions": {
            "entry": "Delta_(p,s)=0 on kappa=0 with 2m=jp+s",
            "A0": "digit 0 of (L1*(pR0)-L0*(pR1))/p",
            "A1": "digit 1 of (L1*(pR0)-L0*(pR1))/p, including determinant carry",
            "B0": "digit 0 of (L1*E0-L0*E1)/p",
            "regular_tail": "3j-1>=p and 2j+2<=p",
        },
        "dependencies": {
            "scripts/item163_deeper_digits_certificate.py": sha256(item163_path),
            "scripts/lifted_endpoint_hasse_extended_certificate.py": sha256(extended_path),
            "scripts/lifted_endpoint_hasse_certificate.py": sha256(base_path),
            "scripts/item180_moving_residual_certificate.py": sha256(item180_path),
        },
        "coordinate_source": "Item163 exact local Hasse recurrence modulo p^4",
        "group_count": len(groups),
        "row_count": len(rows),
        "A0_zero_count": sum(r["passes_p2"] for r in rows),
        "cubic_gate_count": sum(r["passes_p3"] for r in rows),
        "row_counts_by_label": dict(sorted(by_label.items())),
        "A0_zero_counts_by_label": dict(sorted(a0_by_label.items())),
        "cubic_counts_by_label": dict(sorted(p3_by_label.items())),
        "proved_theorem_replay": {
            "regular_tail_row_count": len(regular_tail),
            "regular_tail_A0_B0_failure_count": len(regular_tail_failures),
            "tail_capacity": "For every regular-tail row, 6m>=p(p+1); hence its fixed-depth weighted capacity is O(sqrt(m))=o(m).",
        },
        "finite_cubic_witnesses": cubic_witnesses,
        "groups": groups,
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: output[k] for k in (
        "group_count", "row_count", "A0_zero_count", "cubic_gate_count",
        "row_counts_by_label", "A0_zero_counts_by_label", "cubic_counts_by_label"
    )}, sort_keys=True))


if __name__ == "__main__":
    main()
