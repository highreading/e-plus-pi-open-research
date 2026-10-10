#!/usr/bin/env python3
"""Deterministic certificate for Item 257's ordinary-j=2 height ceiling.

The theorem is symbolic and proved in the companion report.  This checker
replays the exact row reindexing, the reduced half-binomial numerators, a
bounded H-zero census, and two independence witnesses against the Item-250
affine eliminant.  Every bounded census is EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def resolve(name: str) -> Path:
    for candidate in (
        HERE / name,
        HERE.parent / "scripts" / name,
        HERE.parent / "sources" / name,
        HERE.parent / "results" / name,
    ):
        if candidate.is_file():
            return candidate
    return HERE / name


ITEM250 = resolve("item250_j2_ordinary_phase_certificate.py")
ITEM219 = resolve("item219_common_log_j2_certificate.py")
ITEM251_REPORT = resolve("item251_j2_exceptional_period_report.md")
ITEM254_REPORT = resolve("item254_half_binomial_arithmetic_report.md")
ITEM256_REPORT = resolve("item256_beta_first_jet_report.md")
DEFAULT_OUTPUT = HERE / "item257_j2_weighted_numerator_certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray([1]) * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = bytes([0]) * (
                (limit - q * q) // q + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def digit_sum_2(n: int) -> int:
    return n.bit_count()


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    return (n & -n).bit_length() - 1


def prefix_integer(k: int) -> int:
    return sum(math.comb(2 * j, j) * 8 ** (k - j) for j in range(k + 1))


def reduced_prefix(k: int) -> tuple[int, int, int]:
    """Return U_k, reduced numerator N_k, and power-of-two denominator D_k."""
    u = prefix_integer(k)
    shift = digit_sum_2(k)
    assert v2(u) == shift
    n = u >> shift
    d = 1 << (3 * k - shift)
    assert n * (1 << shift) == u
    assert n >= d
    assert n * n < 2 * d * d
    assert n & 1
    return u, n, d


def phase_s_values(global_m: int) -> list[int]:
    """All integral ordinary-j=2 s candidates before primality."""
    if global_m < 1:
        return []
    bound = (2 * global_m - 7) // 14
    if bound < 1:
        return []
    residue = (3 * (global_m - 1)) % 5
    return [s for s in range(1, bound + 1) if s % 5 == residue]


def row_from_ms(global_m: int, s: int) -> tuple[int, int, int]:
    numerator = 4 * global_m + 2 * s + 1
    assert numerator % 5 == 0
    p = numerator // 5
    r_numerator = 2 * global_m - 14 * s - 7
    assert r_numerator % 5 == 0
    r = r_numerator // 5
    k = s - 1
    assert p == 2 * r + 6 * s + 3
    assert p == 6 * k + 2 * (r + 4) + 1
    assert r >= 1 and r % 2 == 1
    assert p % 4 == (2 * k + 3) % 4
    return p, r, k


def audit_global_reindex(global_max: int, prime_max: int) -> dict[str, int]:
    primes = set(primes_upto(prime_max))
    candidates = 0
    prime_rows = 0
    converse_rows = 0
    for global_m in range(1, global_max + 1):
        ss = phase_s_values(global_m)
        candidates += len(ss)
        forward_primes: set[int] = set()
        for s in ss:
            p, r, k = row_from_ms(global_m, s)
            assert 14 * s <= 2 * global_m - 7
            assert 5 * p == 4 * global_m + 2 * s + 1
            assert p >= (4 * global_m + 3) / 5
            assert 7 * p <= 6 * global_m
            if p in primes:
                assert p > 7
                assert r % 3 != 0
                assert (5 * p - 2 * s - 1) // 4 == global_m
                forward_primes.add(p)
                prime_rows += 1

        interval_primes = {
            p
            for p in primes
            if p > 7
            and 5 * p >= 4 * global_m + 3
            and 7 * p <= 6 * global_m
        }
        assert forward_primes == interval_primes
        converse_rows += len(interval_primes)
    assert prime_rows == converse_rows
    return {
        "global_m_max": global_max,
        "candidate_s_rows": candidates,
        "prime_rows": prime_rows,
    }


def prefix_audit(k_max: int) -> dict[str, Any]:
    digest_rows: list[str] = []
    samples: list[dict[str, Any]] = []
    for k in range(k_max + 1):
        u, n, d = reduced_prefix(k)
        digest_rows.append(f"{k},{u},{n},{d}")
        if k in {0, 1, 2, 4, 7, 16, 31, 64, 127, k_max}:
            samples.append(
                {
                    "k": k,
                    "v2_U": v2(u),
                    "s2_k": digit_sum_2(k),
                    "N_k": str(n),
                    "D_k": str(d),
                }
            )
    digest = hashlib.sha256(("\n".join(digest_rows) + "\n").encode()).hexdigest()
    return {"k_max": k_max, "row_digest_sha256": digest, "samples": samples}


def h_zero_scan(prime_max: int) -> dict[str, Any]:
    rows = 0
    zeros: list[tuple[int, int, int, int, int]] = []
    by_global: dict[int, list[int]] = {}
    for p in primes_upto(prime_max):
        if p < 11:
            continue
        h = 1
        total = 1
        k_max = (p - 11) // 6
        for k in range(k_max + 1):
            if k:
                h = h * (2 * k - 1) * pow(4 * k, -1, p) % p
                total = (total + h) % p
            s = k + 1
            if (5 * p - 2 * s - 1) % 4:
                continue
            r = (p - 6 * s - 3) // 2
            assert r >= 1 and r % 2 and r % 3
            global_m = (5 * p - 2 * s - 1) // 4
            p2, r2, k2 = row_from_ms(global_m, s)
            assert (p2, r2, k2) == (p, r, k)
            rows += 1
            if total == 0:
                zeros.append((p, s, r, k, global_m))
                by_global.setdefault(global_m, []).append(p)

    assert all(len(values) == 1 for values in by_global.values())
    digest = hashlib.sha256(
        ("\n".join(",".join(map(str, row)) for row in zeros) + "\n").encode()
    ).hexdigest()
    ratios = [
        (math.log(p) / global_m, p, global_m)
        for global_m, values in by_global.items()
        for p in values
    ]
    max_ratio, max_p, max_global = max(ratios)
    return {
        "prime_max": prime_max,
        "actual_rows": rows,
        "H_zero_count": len(zeros),
        "distinct_global_m": len(by_global),
        "at_most_one_zero_per_global_m_in_scan": True,
        "zero_digest_sha256": digest,
        "first_20_zero_rows_p_s_r_k_global_m": [list(row) for row in zeros[:20]],
        "max_observed_log_weight_per_global_m": {
            "p": max_p,
            "global_m": max_global,
            "decimal": format(max_ratio, ".15f"),
        },
        "strict_label": "EXACT FINITE ONLY; no density or asymptotic inference",
    }


def phase_independence_witnesses() -> list[dict[str, int]]:
    item250 = load_module("item250_for_item257", ITEM250)
    witnesses: list[dict[str, int]] = []
    for p, s, r in ((43, 3, 11), (47, 5, 7), (367, 39, 65)):
        phase = item250.evaluate_phase_row(p, s, item250.phase_data(r))
        k = s - 1
        h = 1
        total = 1
        for j in range(1, k + 1):
            h = h * (2 * j - 1) * pow(4 * j, -1, p) % p
            total = (total + h) % p
        witnesses.append(
            {
                "p": p,
                "s": s,
                "r": r,
                "k": k,
                "H_k": total,
                "G_0": phase["g0"],
                "G_1": phase["g1"],
                "linear_eliminant": phase["linear"],
                "cubic_resultant": phase["resultant"],
            }
        )
    assert witnesses[0]["H_k"] == 0 and witnesses[0]["linear_eliminant"] != 0
    assert witnesses[1]["H_k"] == 0 and witnesses[1]["linear_eliminant"] != 0
    assert witnesses[2]["H_k"] != 0
    assert witnesses[2]["linear_eliminant"] == witnesses[2]["cubic_resultant"] == 0
    assert (witnesses[2]["G_0"], witnesses[2]["G_1"]) != (0, 0)
    return witnesses


def selected_product_data(global_values: tuple[int, ...]) -> list[dict[str, Any]]:
    max_k = max((max(phase_s_values(n), default=1) - 1 for n in global_values), default=0)
    numerators = [reduced_prefix(k)[1] for k in range(max_k + 1)]
    out: list[dict[str, Any]] = []
    for global_m in global_values:
        ks = [s - 1 for s in phase_s_values(global_m)]
        product = math.prod(numerators[k] for k in ks)
        lcm = 1
        for k in ks:
            lcm = math.lcm(lcm, numerators[k])
        out.append(
            {
                "global_m": global_m,
                "candidate_count": len(ks),
                "min_k": min(ks) if ks else None,
                "max_k": max(ks) if ks else None,
                "product_bit_length": product.bit_length(),
                "lcm_bit_length": lcm.bit_length(),
                "largest_numerator_bit_length": max(
                    (numerators[k].bit_length() for k in ks), default=0
                ),
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prime-max", type=int, default=5000)
    parser.add_argument("--global-audit-max", type=int, default=1000)
    parser.add_argument("--prefix-max", type=int, default=257)
    args = parser.parse_args()

    for dependency in (ITEM250, ITEM219, ITEM251_REPORT, ITEM254_REPORT, ITEM256_REPORT):
        if not dependency.is_file():
            raise FileNotFoundError(dependency)

    raw = 2 / 35
    closing_margin_per_global = 6 * 0.0007599863045581
    cauchy_h = 6.327627545440858
    output = {
        "schema": "item257-j2-weighted-numerator-v1",
        "status": {
            "global_row_reindex": "PROVED_IN_REPORT",
            "numerator_product_container": "PROVED_IN_REPORT",
            "height_residue_ceiling": "PROVED_SHARPLY_SCOPED_NO_GO",
            "joint_affine_height_ceiling": "PROVED_SCOPED_NO_GO_FOR_AVAILABLE_HEIGHT_DATA",
            "weighted_zero_rate": "NOT_PROVED",
            "capacity_reduction": "0",
            "finite_scan": "EXACT_FINITE_ONLY",
        },
        "exact_maps": {
            "global_cell": "4M+1=5p-2s",
            "prefix_index": "k=s-1",
            "candidate_prime": "p=(4M+2s+1)/5=(4M+2k+3)/5",
            "phase_r": "r=(2M-14s-7)/5=6M-7p",
            "candidate_s": "1<=s<=(2M-7)/14 and s=3(M-1) mod 5",
            "raw_prime_interval": "(4M+3)/5 <= p <= 6M/7",
            "actual_mod4": "p=2k+3 mod 4 (automatic from the global cell)",
            "actual_phase": "p=6k+2d+1, d=r+4=3 or 5 mod 6",
        },
        "theorems": {
            "reduced_prefix": (
                "H_k=N_k/2^(3k-s_2(k)), with N_k odd and "
                "2^(3k-s_2(k))<=N_k<2^(3k-s_2(k)+1/2)"
            ),
            "global_container": (
                "R_M^H=product of actual H-zero row primes divides "
                "P_M=product_{s in S_M} N_(s-1)"
            ),
            "product_height": "log P_M=(3 log 2/490)M^2+O(M log M)",
            "lcm_ceiling": (
                "even the unfiltered lcm container has log at least "
                "(3 log 2/7)M+O(log M), larger than the raw 2M/35 cell mass"
            ),
            "small_edge": (
                "N_(s-1)<p excludes only s=O(log M), hence only o(M) raw log weight"
            ),
            "joint_gate": (
                "Item251 prescribes an affine value of H_k, not H_k=0; "
                "the original fixed-M gate only supplies the known p^2 coefficient container"
            ),
        },
        "rate_comparison": {
            "raw_j2_per_global_m": "2/35",
            "raw_j2_decimal": format(raw, ".15f"),
            "raw_j2_per_6m": "1/105",
            "largest_prefix_height_coefficient_3log2_over7": format(
                3 * math.log(2) / 7, ".15f"
            ),
            "product_quadratic_coefficient_3log2_over490": format(
                3 * math.log(2) / 490, ".15f"
            ),
            "item197_square_container_per_global_m_H_over2": format(
                cauchy_h / 2, ".15f"
            ),
            "item197_square_container_multiplicity": 2,
            "multiplicity_needed_to_beat_raw_with_same_height": format(
                cauchy_h / raw, ".12f"
            ),
            "closing_exception_allowance_per_global_m_if_j1_fully_removed": format(
                closing_margin_per_global, ".15f"
            ),
            "verdict": "all available deterministic height ceilings are weaker than raw support",
            "new_bookable_rate": "0",
        },
        "global_reindex_replay": audit_global_reindex(
            args.global_audit_max, args.prime_max
        ),
        "prefix_replay": prefix_audit(args.prefix_max),
        "selected_container_replay": selected_product_data((100, 250, 500, 1000)),
        "finite_H_zero_scan": h_zero_scan(args.prime_max),
        "affine_independence_witnesses": phase_independence_witnesses(),
        "dependencies": {
            path.name: sha256(path)
            for path in (ITEM250, ITEM219, ITEM251_REPORT, ITEM254_REPORT, ITEM256_REPORT)
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
