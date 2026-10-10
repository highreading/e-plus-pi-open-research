#!/usr/bin/env python3
"""Deterministic certificate for Item 392.

The checker verifies exact singular-factor identities and finite prime-window
partitions.  Every enumerated prime statistic is diagnostic only.  The
asymptotic theorem is proved in the accompanying report by the uniform
Selberg upper bound, divisor averaging, and the elementary packing argument.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item392_j2_growing_window_aggregate_no_go_certificate.json"

DEPENDENCIES = {
    "work/item385_j2_bounded_window_aggregate_no_go_report.md":
        "68081934a0c5f836f826e3583cef21879686a0c68db5140d4b66387f4bebbe12",
    "work/item385_j2_bounded_window_aggregate_no_go_certificate.py":
        "add1ad77013208df83cdc1f6db39efaaa8338b0de128e2f941496cf7630d81ef",
    "work/item385_j2_bounded_window_aggregate_no_go_certificate.json":
        "0ddf03b5e159c7616fde0dfa8759d6733353a90c65d559ae1926a3fbc8c7c8bf",
    "work/item322_j2_fixedM_period_transfer_report.md":
        "7941d4102861a96145cc38267463da1a78cf7c2d9dec384857ef5c16a3f0b875",
    "work/item326_j1_selected_factor_step12_no_go_report.md":
        "12f42dff3d52ab5d257eac675d9cff6888925568d29ea4894cad5e37c0c31b37",
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


def prime_factors(value: int) -> list[int]:
    value = abs(value)
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return factors


def singular_product(k: int) -> Fraction:
    result = Fraction(1, 1)
    for prime in prime_factors(k):
        if prime >= 5:
            result *= Fraction(prime - 1, prime - 2)
    return result


def singular_divisor_expansion(k: int) -> Fraction:
    terms = [Fraction(1, 1)]
    for prime in prime_factors(k):
        if prime >= 5:
            addon = Fraction(1, prime - 2)
            terms += [term * addon for term in terms]
    return sum(terms, Fraction(0, 1))


def sieve(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start:limit + 1:prime] = b"\x00" * (((limit - start) // prime) + 1)
    return flags


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def interval_bounds(M: int) -> tuple[int, int]:
    return ceil_div(4 * M + 3, 5), (6 * M - 1) // 7


def classify_window(M: int, K: int, flags: bytearray) -> dict[str, Any]:
    lower, upper = interval_bounds(M)
    primes = [value for value in range(lower, upper + 1) if flags[value]]
    prime_set = set(primes)
    paired: list[int] = []
    isolated: list[int] = []
    for prime in primes:
        has_neighbor = any(
            prime + 6 * offset in prime_set
            for offset in range(-K, K + 1)
            if offset
        )
        (paired if has_neighbor else isolated).append(prime)

    if set(paired) & set(isolated):
        raise AssertionError("partition overlap")
    if sorted(paired + isolated) != primes:
        raise AssertionError("partition failure")

    by_ray: dict[int, list[int]] = {
        residue: [prime for prime in isolated if prime % 6 == residue]
        for residue in (1, 5)
    }
    minimum_gaps: dict[str, int | None] = {}
    for residue, values in by_ray.items():
        gaps = [right - left for left, right in zip(values, values[1:])]
        if gaps and min(gaps) <= 6 * K:
            raise AssertionError((M, K, residue, min(gaps)))
        minimum_gaps[str(residue)] = min(gaps) if gaps else None

    interval_span = upper - lower
    exact_packing_bound = 2 * (1 + interval_span // (6 * (K + 1)))
    if len(isolated) > exact_packing_bound:
        raise AssertionError((M, K, len(isolated), exact_packing_bound))

    raw_weight = math.fsum(math.log(prime) for prime in primes)
    paired_weight = math.fsum(math.log(prime) for prime in paired)
    isolated_weight = math.fsum(math.log(prime) for prime in isolated)
    if not math.isclose(raw_weight, paired_weight + isolated_weight,
                        rel_tol=2e-15, abs_tol=2e-12):
        raise AssertionError("weighted partition failure")

    return {
        "M": M,
        "K": K,
        "interval": [lower, upper],
        "interval_span": interval_span,
        "prime_count": len(primes),
        "paired_count": len(paired),
        "isolated_count": len(isolated),
        "isolated_count_exact_packing_bound": exact_packing_bound,
        "isolated_minimum_gaps_by_mod6_ray": minimum_gaps,
        "raw_log_weight": raw_weight,
        "paired_log_weight": paired_weight,
        "isolated_log_weight": isolated_weight,
        "raw_weight_over_M": raw_weight / M,
        "paired_weight_over_M": paired_weight / M,
        "isolated_weight_over_M": isolated_weight / M,
    }


def singular_diagnostics() -> dict[str, Any]:
    maximum = 10_000
    values: list[Fraction] = []
    for k in range(1, maximum + 1):
        product = singular_product(k)
        expansion = singular_divisor_expansion(k)
        if product != expansion:
            raise AssertionError((k, product, expansion))
        values.append(product)

    checkpoints: list[dict[str, Any]] = []
    for K in (10, 100, 1_000, 10_000):
        total = sum(values[:K], Fraction(0, 1))
        checkpoints.append({
            "K": K,
            "mean_singular_factor": float(total / K),
            "maximum_singular_factor": float(max(values[:K])),
            "argmax_first": 1 + values[:K].index(max(values[:K])),
        })
    return {
        "identity_verified_for_all_k_through": maximum,
        "checkpoints": checkpoints,
        "proof_identity": (
            "prod_{q|k,q>=5}(1+1/(q-2))="
            "sum_{d|k,d_squarefree,(d,6)=1} prod_{q|d}1/(q-2)"
        ),
    }


def build_payload() -> dict[str, Any]:
    dependency_actuals = verify_dependencies()
    Ms = (1_000, 5_000, 20_000, 100_000)
    maximum_upper = max(interval_bounds(M)[1] for M in Ms)
    flags = sieve(maximum_upper)

    windows: list[dict[str, Any]] = []
    for M in Ms:
        logarithm = math.log(M)
        choices = {
            "sublog_sqrt_log": max(1, math.floor(math.sqrt(logarithm))),
            "critical_floor_log": max(1, math.floor(logarithm)),
            "superlog_log_squared": max(1, math.ceil(logarithm * logarithm)),
        }
        for regime, K in choices.items():
            row = classify_window(M, K, flags)
            row["regime_label"] = regime
            windows.append(row)

    return {
        "item": 392,
        "title": "ordinary-j2 growing-window aggregate propagation theorem",
        "checked_date_beijing": "2026-09-01",
        "status": "proved_no_booking",
        "evidence_policy": {
            "finite_prime_data": "EXACT FINITE ONLY / DIAGNOSTIC",
            "no_asymptotic_inference_from_enumeration": True,
        },
        "dependency_hashes_verified": dependency_actuals,
        "exact_alignment": {
            "return": ["r-42k", "s+15k", "p+6k"],
            "selected_prime_offset": "6k",
        },
        "proved_theorems": {
            "general_weighted_bound": (
                "W_pair(M;H_M) << M*Sigma(H_M)/log(M), "
                "Sigma=sum_{k in H_M} prod_{q|k,q>=5}(q-1)/(q-2)"
            ),
            "general_zero_rate_condition": "Sigma(H_M)=o(log M)",
            "complete_window_pair_bound": "W_pair(M;K) << M*K/log(M)",
            "complete_window_zero_rate": "K(M)=o(log M)",
            "sublog_isolated_mass": "W_iso(M;K)=(2/35)M+o(M)",
            "packing_bound": "W_iso(M;K) << M*log(M)/K+log(M)",
            "superlog_paired_mass": (
                "if K/log(M)->infinity then W_pair=(2/35)M+o(M)"
            ),
            "critical_barrier": "K asymptotic to log(M)",
        },
        "singular_factor_diagnostics": singular_diagnostics(),
        "finite_window_diagnostics": windows,
        "ledger": {
            "delta_r1": 0,
            "delta_booked_capacity": 0,
            "ordinary_j2_raw_normalized_ceiling": "1/105",
            "closed_mechanism": (
                "all second-actual-row propagation in complete sublogarithmic "
                "same-ray windows, and sparse H_M with Sigma=o(log M)"
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
        "item": 392,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
