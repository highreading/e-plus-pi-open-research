#!/usr/bin/env python3
"""Deterministic exact controls for Item 398.

The all-M proofs are in the report.  This checker pins Item 395 and verifies
the aggregate endpoint resultant, collision-graph valuation identity, modular
degree bound, near-perfect-power difference valuations, and exact rational
near-power parameters on declared root sets.  Root sets are algebraic controls
inside actual candidate intervals, not claimed actual collision sets.  No gate
scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item395_j1_logscale_cluster_radical_height_obstruction_report.md":
        "af0d85607d665f5d6c12c2695a44a89d984abffb008bbd1318978471e79f4487",
    "scripts/item395_j1_logscale_cluster_radical_height_obstruction_certificate.py":
        "fd501bca8b933c4afd3b31ba0a57e9d0788b2d0ba0ae553a64608649c2e9159a",
    "results/item395_j1_logscale_cluster_radical_height_obstruction_certificate.json":
        "3daa118ffe731765b089a5ea42a035ff081e9999377d54196ae683d131b6f563",
    "results/item395_j1_logscale_cluster_radical_height_obstruction_certificate_replay.json":
        "3daa118ffe731765b089a5ea42a035ff081e9999377d54196ae683d131b6f563",
    "results/item395_j1_logscale_cluster_radical_height_obstruction_ledger_delta.json":
        "56e83867fd5bc1b98f2805205ee6782965a8e12c6c8db4c3f6e033f0e1f6c4b3",
    "manifests/item395_j1_logscale_cluster_radical_height_obstruction_manifest.json":
        "3ef54ba9d3caa5af1b76bde52822447e253256c4c0ebb30dd6bb8a6200502cbd",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing dependency", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(("dependency mismatch", relative, expected, actual))


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


def candidates(M: int) -> list[int]:
    return [
        p for p in range(2, (3 * M - 1) // 2 + 1)
        if is_prime(p) and 3 * p >= 4 * M + 3 and 2 * p <= 3 * M - 1
    ]


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise AssertionError("valuation of zero not used in controls")
    output = 0
    remaining = abs(value)
    while remaining % prime == 0:
        remaining //= prime
        output += 1
    return output


def graph_degrees(roots: list[int], D: int) -> dict[int, int]:
    root_set = set(roots)
    return {
        p: sum(
            1
            for d in range(1, D + 1)
            for q in (p - 2 * d, p + 2 * d)
            if q in root_set
        )
        for p in roots
    }


def local_endpoint_polynomial(value: int, D: int) -> int:
    return math.prod(value * value - 4 * d * d for d in range(1, D + 1))


def shifted_norm_product(roots: list[int], D: int) -> int:
    output = 1
    for d in range(1, D + 1):
        output *= math.prod(p - 2 * d for p in roots)
        output *= math.prod(p + 2 * d for p in roots)
    return output


def squarefree_support_product(values: list[int]) -> int:
    return math.prod(sorted(set(values)))


DECLARED_CONTROLS = [
    (180, [241, 251, 257, 263, 269], 3),
    (180, [241, 257, 269], 5),
    (300, [401, 409, 419, 421, 431, 433, 439, 443, 449], 2),
    (300, [401, 419, 431, 449], 5),
]


def control(M: int, roots: list[int], D: int) -> dict[str, Any]:
    assert roots == sorted(set(roots))
    assert set(roots).issubset(candidates(M))
    lower = Fraction(4 * M + 3, 3)
    upper = Fraction(3 * M - 1, 2)
    assert upper + 2 * D < 2 * lower
    assert 4 * D < lower

    R = math.prod(roots)
    degrees = graph_degrees(roots, D)
    aggregate = math.prod(local_endpoint_polynomial(q, D) for q in roots)
    shifted_product = shifted_norm_product(roots, D)
    assert aggregate == shifted_product
    R_power = R ** (2 * D)
    assert 0 < aggregate < R_power
    difference = R_power - aggregate

    candidate_part = math.prod(p ** degrees[p] for p in roots)
    assert math.gcd(aggregate, R_power) == candidate_part
    assert math.gcd(difference, R_power) == candidate_part

    for p in roots:
        degree = degrees[p]
        assert degree <= D + D // 3
        assert degree < 2 * D
        assert valuation(aggregate, p) == degree
        assert valuation(difference, p) == degree

    clustered = [p for p in roots if degrees[p] > 0]
    cluster_radical = squarefree_support_product(clustered)
    assert math.gcd(R, aggregate) == cluster_radical
    assert math.gcd(R, difference) == cluster_radical

    sum_squares = D * (D + 1) * (2 * D + 1) // 6
    epsilon_upper = (
        Fraction(4 * len(roots) * sum_squares, 1)
        / (lower * lower - 4 * D * D)
    )
    ratio = Fraction(aggregate, R_power)
    assert 0 < ratio < 1

    edge_count = sum(degrees.values()) // 2
    edge_product = 1
    for index, p in enumerate(roots):
        for q in roots[index + 1:]:
            if q - p <= 2 * D:
                edge_product *= p * q
    assert edge_product == candidate_part

    return {
        "M": M,
        "D": D,
        "candidate_primes": candidates(M),
        "declared_roots": roots,
        "R": str(R),
        "aggregate_resultant": str(aggregate),
        "R_power_2D": str(R_power),
        "near_power_difference": str(difference),
        "aggregate_equals_product_of_shifted_norms": True,
        "graph_degrees": {str(p): degrees[p] for p in roots},
        "edge_count": edge_count,
        "candidate_prime_part": str(candidate_part),
        "candidate_prime_part_equals_edge_product": True,
        "clustered_roots": clustered,
        "cluster_radical": str(cluster_radical),
        "gcd_R_aggregate": str(math.gcd(R, aggregate)),
        "gcd_R_difference": str(math.gcd(R, difference)),
        "aggregate_to_R_power_ratio": {
            "numerator": str(ratio.numerator),
            "denominator": str(ratio.denominator),
        },
        "negative_log_ratio_upper_parameter": {
            "numerator": str(epsilon_upper.numerator),
            "denominator": str(epsilon_upper.denominator),
        },
        "mod_3_degree_bound": D + D // 3,
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    return {
        "schema": "item398-j1-aggregate-endpoint-resultant-graph-valuation-no-go-certificate-v1",
        "item": 398,
        "checked_date_beijing": "2026-09-01",
        "classification": "EXACT_AGGREGATE_RESULTANT_GRAPH_VALUATION_AND_NEAR_POWER_CANCELLATION_NO_GO",
        "dependency_hashes": DEPENDENCIES,
        "controls": [control(M, roots, D) for M, roots, D in DECLARED_CONTROLS],
        "proved_by_report": [
            "the product over all plus and minus endpoint norms is Res(F_M,G_D)",
            "its candidate-prime valuation at p is exactly the logarithmic-window collision-graph degree of p",
            "the candidate-prime part is the product of p*q over all graph edges",
            "modulo 3 gives degree at most D+floor(D/3), strictly below 2D",
            "subtracting the nearby perfect power R_M^(2D) preserves every candidate-prime graph-degree valuation",
            "the aggregate resultant is within exp(-(c^3/8+o(1))log^2(M)/M) of R_M^(2D) for D~c log M",
            "near-power cancellation and prime allocation alone do not meet the Item395 cluster threshold",
        ],
        "strict_scope": {
            "declared_roots_are_algebraic_controls_not_actual_collisions": True,
            "actual_gate_scan_performed": False,
            "finite_to_infinite_inference": False,
            "actual_cluster_upper_bound_proved": False,
            "new_booked_mass": 0,
            "new_capacity_reduction": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
