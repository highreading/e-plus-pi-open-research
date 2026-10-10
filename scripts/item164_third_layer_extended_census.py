#!/usr/bin/env python3
"""Exact finite e=1 third-content-layer census beyond item 163.

This script reuses the item-162 local Hasse recurrence and the item-163
two-minor normalization.  It first computes the lifted A digit on every
forced e=1 row.  Only rows with A_0=0 are recomputed one p-adic digit deeper;
this is sufficient for the exact p^3 gate

    A_0=A_1=B_0=0.

The output is an exact deterministic finite census.  It makes no asymptotic
claim about the density or mass of surviving rows.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
DEFAULT_ITEM163 = DEFAULT_ARCHIVE / "scripts" / "item163_deeper_digits_certificate.py"
DEFAULT_ITEM163_JSON = DEFAULT_ARCHIVE / "results" / "item163_deeper_digits_certificate.json"
DEFAULT_RANK_TWO = DEFAULT_ARCHIVE / "results" / "mixed_cubic_rank_two_cartier_probe_m500.json"
DEFAULT_OUTPUT = DEFAULT_ARCHIVE / "results" / "item164_third_layer_extended_census_m250.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def task_key(row: dict[str, Any]) -> tuple[int, int]:
    return int(row["m"]), int(row["p"])


def source_delta_key(row: dict[str, Any]) -> str:
    return f'{row["source"]}|delta={int(row["delta"])}'


def prime_sieve(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p, flag in enumerate(sieve) if flag]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--item163-script", type=Path, default=DEFAULT_ITEM163)
    parser.add_argument("--item163-json", type=Path, default=DEFAULT_ITEM163_JSON)
    parser.add_argument("--rank-two-probe", type=Path, default=DEFAULT_RANK_TWO)
    parser.add_argument("--max-m", type=int, default=250)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not (101 <= args.max_m <= 500):
        raise ValueError("max-m must lie in [101,500] for the pinned rank-two probe")

    archived_base = args.archive / "scripts" / "lifted_endpoint_hasse_certificate.py"
    archived_extended = (
        args.archive / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
    )
    for path in (
        archived_base,
        archived_extended,
        args.item163_script,
        args.item163_json,
        args.rank_two_probe,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)

    item163 = load_module("item164_item163_exact", args.item163_script)
    extended = item163.load_module("item164_item162_extended_exact", archived_extended)
    base = extended.base

    rank_two = json.loads(args.rank_two_probe.read_text(encoding="utf-8"))
    if int(rank_two["max_m"]) < args.max_m:
        raise ValueError("rank-two probe does not cover requested max-m")

    tasks: dict[tuple[int, int], dict[str, Any]] = {}
    for m in range(1, args.max_m + 1):
        for archived in base.rank_one_rows(m):
            if int(archived["e"]) != 1:
                continue
            p = int(archived["p"])
            tasks[(m, p)] = {
                "m": m,
                "p": p,
                "delta": int(archived["delta"]),
                "sources": {"rank_one"},
            }

    rank_two_zero_candidates = 0
    for archived in rank_two["zeros"]:
        m = int(archived["m"])
        if m > args.max_m:
            continue
        p = int(archived["p"])
        if p * p <= 4 * m + 1:
            raise AssertionError(("rank-two row is not e=1", m, p))
        if int(archived["delta"]) != 0:
            raise AssertionError(("rank-two row has unexpected delta", m, p))
        rank_two_zero_candidates += 1
        existing = tasks.get((m, p))
        if existing is None:
            tasks[(m, p)] = {
                "m": m,
                "p": p,
                "delta": 0,
                "sources": {"rank_two_zero"},
            }
        else:
            if int(existing["delta"]) != 0:
                raise AssertionError(("source delta disagreement", m, p, existing))
            existing["sources"].add("rank_two_zero")

    forced_rows: list[dict[str, Any]] = []
    second_layer_candidates: list[dict[str, Any]] = []
    third_layer_survivors: list[dict[str, Any]] = []
    forced_counts: collections.Counter[str] = collections.Counter()
    second_counts: collections.Counter[str] = collections.Counter()
    third_counts: collections.Counter[str] = collections.Counter()
    prime_counts: collections.Counter[int] = collections.Counter()
    residue_counts: collections.Counter[str] = collections.Counter()
    divisibility_failures: list[dict[str, Any]] = []
    precision_lift_failures: list[dict[str, Any]] = []

    for (m, p), task in sorted(tasks.items()):
        delta = int(task["delta"])
        source = "+".join(sorted(task["sources"]))
        forced_power = 1 + delta
        low_precision = forced_power + 1

        l0, x0, e0, low_bands0 = item163.coordinates_mod(
            extended, m, 4 * m + 1, p, low_precision
        )
        l1, x1, e1, low_bands1 = item163.coordinates_mod(
            extended, m, 4 * m + 2, p, low_precision
        )
        low_modulus = p**low_precision
        determinant_a = (l1 * x0 - l0 * x1) % low_modulus
        determinant_b = (l1 * e0 - l0 * e1) % low_modulus
        divisor = p**forced_power
        if determinant_a % divisor or determinant_b % divisor:
            divisibility_failures.append(
                {"m": m, "p": p, "source": source, "delta": delta}
            )
            continue
        a0 = determinant_a // divisor % p
        b0_low = determinant_b // divisor % p
        key = f"{source}|delta={delta}"
        forced_counts[key] += 1
        forced_row = {
            "m": m,
            "p": p,
            "source": source,
            "delta": delta,
            "A0": a0,
        }
        forced_rows.append(forced_row)
        if a0:
            continue

        # One more coordinate digit determines A_1.  B_0 is recomputed at
        # the lifted precision and must agree with the first pass.
        high_precision = forced_power + 2
        l0h, x0h, e0h, bands0 = item163.coordinates_mod(
            extended, m, 4 * m + 1, p, high_precision
        )
        l1h, x1h, e1h, bands1 = item163.coordinates_mod(
            extended, m, 4 * m + 2, p, high_precision
        )
        high_modulus = p**high_precision
        determinant_a_high = (l1h * x0h - l0h * x1h) % high_modulus
        determinant_b_high = (l1h * e0h - l0h * e1h) % high_modulus
        if determinant_a_high % divisor or determinant_b_high % divisor:
            divisibility_failures.append(
                {"m": m, "p": p, "source": source, "delta": delta, "pass": 2}
            )
            continue
        a_digits = item163.p_digits(determinant_a_high // divisor, p, 2)
        b0 = determinant_b_high // divisor % p
        if a_digits[0] != a0 or b0 != b0_low:
            precision_lift_failures.append(
                {
                    "m": m,
                    "p": p,
                    "A0_low": a0,
                    "A0_high": a_digits[0],
                    "B0_low": b0_low,
                    "B0_high": b0,
                }
            )
        survives = a_digits == [0, 0] and b0 == 0
        row = {
            "m": m,
            "p": p,
            "source": source,
            "delta": delta,
            "A_digits_after_forced_power": a_digits,
            "B0_after_forced_power": b0,
            "p3_gate": survives,
            "Hasse_band_indices": sorted(set(bands0) | set(bands1)),
        }
        second_layer_candidates.append(row)
        second_counts[key] += 1
        if survives:
            third_layer_survivors.append(row)
            third_counts[key] += 1
            prime_counts[p] += 1
            residue_counts[f"p={p}|m_mod_p={m % p}|delta={delta}|source={source}"] += 1

    if divisibility_failures or precision_lift_failures:
        raise AssertionError(
            {
                "divisibility": divisibility_failures[:3],
                "precision_lift": precision_lift_failures[:3],
            }
        )

    # Exact overlap replay against all item-163 e=1 rows through m=100.
    old = json.loads(args.item163_json.read_text(encoding="utf-8"))
    old_rows = {task_key(row): row for row in old["rows"]}
    new_forced = {task_key(row): row for row in forced_rows if int(row["m"]) <= 100}
    old_keys = set(old_rows)
    new_keys = set(new_forced)
    overlap_failures: list[dict[str, Any]] = []
    if old_keys != new_keys:
        overlap_failures.append(
            {
                "missing_from_new": sorted(old_keys - new_keys),
                "extra_in_new": sorted(new_keys - old_keys),
            }
        )
    new_second = {task_key(row): row for row in second_layer_candidates if int(row["m"]) <= 100}
    for key in sorted(old_keys & new_keys):
        archived = old_rows[key]
        current = new_forced[key]
        if int(current["A0"]) != int(archived["A_digits_after_forced_power"][0]):
            overlap_failures.append({"key": key, "field": "A0"})
        archived_source = str(archived["source"])
        if str(current["source"]) != archived_source or int(current["delta"]) != int(
            archived["delta"]
        ):
            overlap_failures.append({"key": key, "field": "classification"})
        if int(current["A0"]) == 0:
            lifted = new_second[key]
            if lifted["A_digits_after_forced_power"] != archived[
                "A_digits_after_forced_power"
            ][:2] or int(lifted["B0_after_forced_power"]) != int(
                archived["B_digits_after_forced_power"][0]
            ):
                overlap_failures.append({"key": key, "field": "third_layer_digits"})
    if overlap_failures:
        raise AssertionError({"item163_overlap_failures": overlap_failures[:3]})

    new_only_survivors = [row for row in third_layer_survivors if int(row["m"]) > 100]
    large_prime_cutoffs = [29, 37, 43, 59, 101, 251]
    finite_large_prime_summary = {
        f"p>={cutoff}": {
            "forced_rows": sum(int(row["p"]) >= cutoff for row in forced_rows),
            "p2_rows": sum(int(row["p"]) >= cutoff for row in second_layer_candidates),
            "p3_rows": sum(int(row["p"]) >= cutoff for row in third_layer_survivors),
        }
        for cutoff in large_prime_cutoffs
    }

    survivor_keys = {task_key(row) for row in third_layer_survivors}

    # Classify against the supplied slab-tail condition.  Its proof belongs
    # to the structural branch and is intentionally not re-audited here.
    # This census merely evaluates the displayed arithmetic predicate.
    tail_condition_rows: list[dict[str, Any]] = []
    for row in forced_rows:
        m, p = int(row["m"]), int(row["p"])
        if p % 20 != 19:
            continue
        k = (p - 19) // 20
        difference = m - (18 * k + 17)
        if difference < 0 or difference % p:
            continue
        ell = difference // p
        if 4 * m + 1 >= p * p or 6 * ell + 4 < p:
            continue
        tail_condition_rows.append(
            {
                "m": m,
                "p": p,
                "k": k,
                "ell": ell,
                "source": str(row["source"]),
                "delta": int(row["delta"]),
                "p3_gate": (m, p) in survivor_keys,
            }
        )
    tail_hits = [row for row in tail_condition_rows if bool(row["p3_gate"])]
    tail_misses = [row for row in tail_condition_rows if not bool(row["p3_gate"])]
    tail_keys = {(int(row["m"]), int(row["p"])) for row in tail_condition_rows}
    survivors_outside_tail = [
        row for row in third_layer_survivors if task_key(row) not in tail_keys
    ]

    def finite_patterns(selected: list[dict[str, Any]]) -> dict[str, Any]:
        """Repeated mod-p classes and consecutive blocks, with no ray claim."""
        affine_groups: dict[
            tuple[int, int, int, str], list[int]
        ] = collections.defaultdict(list)
        for row in selected:
            group_key = (
                int(row["p"]),
                int(row["m"]) % int(row["p"]),
                int(row["delta"]),
                str(row["source"]),
            )
            affine_groups[group_key].append(int(row["m"]))
        repeated_affine_groups = []
        for key, values in sorted(affine_groups.items()):
            if len(values) < 2:
                continue
            p, residue, delta, source = key
            same_class_forced = [
                int(row["m"])
                for row in forced_rows
                if int(row["p"]) == p
                and int(row["m"]) % p == residue
                and int(row["delta"]) == delta
                and str(row["source"]) == source
            ]
            repeated_affine_groups.append(
                {
                    "p": p,
                    "m_mod_p": residue,
                    "delta": delta,
                    "source": source,
                    "surviving_m_values": sorted(values),
                    "non_surviving_forced_m_values": sorted(
                        m for m in same_class_forced if (m, p) not in survivor_keys
                    ),
                    "survivor_count": len(values),
                    "forced_class_count": len(same_class_forced),
                }
            )

        consecutive_blocks: list[dict[str, Any]] = []
        survivors_by_prime: dict[int, list[int]] = collections.defaultdict(list)
        for row in selected:
            survivors_by_prime[int(row["p"])].append(int(row["m"]))
        for p, values in sorted(survivors_by_prime.items()):
            values = sorted(values)
            start = previous = values[0]
            for current in values[1:] + [10**18]:
                if current == previous + 1:
                    previous = current
                    continue
                if previous > start:
                    consecutive_blocks.append(
                        {
                            "p": p,
                            "m_start": start,
                            "m_end": previous,
                            "length": previous - start + 1,
                        }
                    )
                start = previous = current
        return {
            "repeated_affine_groups": repeated_affine_groups,
            "consecutive_survivor_blocks": consecutive_blocks,
        }

    all_survivor_patterns = finite_patterns(third_layer_survivors)
    outside_tail_patterns = finite_patterns(survivors_outside_tail)
    complete_e1_primes = [
        p
        for p in prime_sieve(2 * math.isqrt(args.max_m + 1) + 3)
        if p != 2 and (p * p - 5) // 4 <= args.max_m
    ]

    payload = {
        "schema": "mixed-cubic-e1-third-layer-extended-census-v1",
        "status": {
            "local_Hasse_recurrence": "PROVED_IN_ITEM162_AND_REUSED_EXACTLY",
            "third_content_layer_gate": "PROVED_IN_ITEM163_AND_REUSED_EXACTLY",
            "finite_census": "EXACT_FINITE_AUDIT_ONLY",
            "congruence_patterns": "EXPERIMENTAL_FINITE_ONLY",
            "supplied_slab_tail_condition": "CLASSIFIER_ONLY_PROOF_NOT_REAUDITED_HERE",
            "positive_mass_or_asymptotic_claim": "OPEN_NONE_INFERRED",
        },
        "scope": {
            "m_min": 1,
            "m_max": args.max_m,
            "e": 1,
            "forced_row_count": len(forced_rows),
            "p2_candidate_count": len(second_layer_candidates),
            "p3_survivor_count": len(third_layer_survivors),
            "maximum_p2_candidate_prime": max(
                (int(row["p"]) for row in second_layer_candidates), default=None
            ),
            "maximum_p3_survivor_prime": max(
                (int(row["p"]) for row in third_layer_survivors), default=None
            ),
            "complete_e1_prime_bands_through_p": max(complete_e1_primes),
            "new_range_m_min": 101,
            "new_range_p3_survivor_count": len(new_only_survivors),
            "rank_two_zero_candidate_count": rank_two_zero_candidates,
        },
        "inputs": {
            str(archived_base): sha256(archived_base),
            str(archived_extended): sha256(archived_extended),
            str(args.item163_script): sha256(args.item163_script),
            str(args.item163_json): sha256(args.item163_json),
            str(args.rank_two_probe): sha256(args.rank_two_probe),
        },
        "exact_replay": {
            "forced_divisibility_failures": 0,
            "precision_lift_failures": 0,
            "item163_overlap_row_count": len(old_rows),
            "item163_overlap_failures": 0,
        },
        "counts_by_source_delta": {
            "forced": dict(sorted(forced_counts.items())),
            "p2": dict(sorted(second_counts.items())),
            "p3": dict(sorted(third_counts.items())),
        },
        "p3_prime_multiplicities": {
            str(p): count for p, count in sorted(prime_counts.items())
        },
        "finite_large_prime_summary": finite_large_prime_summary,
        "finite_all_survivor_patterns": all_survivor_patterns,
        "supplied_slab_tail_classifier": {
            "condition": "p=20k+19 prime; m=18k+17+ell*p; 4m+1<p^2; 6ell+4>=p",
            "tail_condition_row_count": len(tail_condition_rows),
            "tail_hit_count": len(tail_hits),
            "tail_miss_count": len(tail_misses),
            "tail_hits": tail_hits,
            "tail_misses": tail_misses,
            "outside_tail_survivor_count": len(survivors_outside_tail),
            "outside_tail_survivors": survivors_outside_tail,
            "outside_tail_patterns": outside_tail_patterns,
        },
        "row_fingerprints": {
            "forced_rows_canonical_sha256": canonical_hash(forced_rows),
            "p2_candidates_canonical_sha256": canonical_hash(second_layer_candidates),
            "p3_survivors_canonical_sha256": canonical_hash(third_layer_survivors),
            "outside_tail_survivors_canonical_sha256": canonical_hash(
                survivors_outside_tail
            ),
        },
        "p3_survivors": third_layer_survivors,
        "p2_candidates": second_layer_candidates,
        "forced_rows": forced_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    summary = {
        "output": str(args.output),
        "forced_rows": len(forced_rows),
        "p2_candidates": len(second_layer_candidates),
        "p3_survivors": len(third_layer_survivors),
        "new_p3_survivors": len(new_only_survivors),
        "max_p3_prime": max((int(row["p"]) for row in third_layer_survivors), default=None),
        "output_sha256": sha256(args.output),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    main()
