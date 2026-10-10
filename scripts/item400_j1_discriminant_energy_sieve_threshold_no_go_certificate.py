#!/usr/bin/env python3
"""Deterministic exact controls for Item 400.

The all-M arguments are proved in the report.  This checker pins Items 384,
391, 395, and 398 and verifies discriminant/derivative coprimality,
short-gap and endpoint products, multiplicative energy, graph energy, and
packing on declared prime-root sets.  The sets are algebraic controls inside
the actual tied intervals; they are not claimed actual collision sets.  No
gate scan or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = (
    HERE
    / "item400_j1_discriminant_energy_sieve_threshold_no_go_certificate.json"
)

DEPENDENCIES = {
    "sources/item384_j1_universal_filtered_selector_capacity_no_go_report.md":
        "9a7340ec9960ad6278e47c63de728048b52cfe59fc957ca93ea32558c6c39342",
    "manifests/item384_j1_universal_filtered_selector_capacity_no_go_manifest.json":
        "f0894c311c76a44c7ffb87d6a885dd0b05e4bd5ba4d3727cd0e8dbe3ffd57f21",
    "sources/item391_j1_logarithmic_spacing_resultant_criterion_report.md":
        "304713605fcf33675a882b4f333d60cc35fd36bc6b860353eff36472d4a27564",
    "manifests/item391_j1_logarithmic_spacing_resultant_criterion_manifest.json":
        "07e4a438dbc32e52e67587d7a0fe4886d23e584fd7fae34aafe7f234c334e511",
    "sources/item395_j1_logscale_cluster_radical_height_obstruction_report.md":
        "af0d85607d665f5d6c12c2695a44a89d984abffb008bbd1318978471e79f4487",
    "manifests/item395_j1_logscale_cluster_radical_height_obstruction_manifest.json":
        "3ef54ba9d3caa5af1b76bde52822447e253256c4c0ebb30dd6bb8a6200502cbd",
    "sources/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_report.md":
        "3773d8209ea6e5b08f524cc44f582739baa6393a9cb362a8e5cc0f9f34f13da4",
    "manifests/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_manifest.json":
        "d62e46075fd88086ffdba4b05545cf57ac52ab9dc981941faf5352b71cf9a69f",
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
            raise AssertionError(
                ("dependency mismatch", relative, expected, actual)
            )


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
        p
        for p in range(2, (3 * M - 1) // 2 + 1)
        if is_prime(p)
        and 3 * p >= 4 * M + 3
        and 2 * p <= 3 * M - 1
    ]


def polynomial_from_roots(roots: list[int]) -> list[int]:
    """Return ascending coefficients of product (X-root)."""
    coefficients = [1]
    for root in roots:
        output = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            output[index] -= root * coefficient
            output[index + 1] += coefficient
        coefficients = output
    return coefficients


def derivative(coefficients: list[int]) -> list[int]:
    return [
        index * coefficient
        for index, coefficient in enumerate(coefficients)
        if index >= 1
    ]


def evaluate(coefficients: list[int], value: int) -> int:
    output = 0
    for coefficient in reversed(coefficients):
        output = output * value + coefficient
    return output


def radical_of_support(values: list[int]) -> int:
    return math.prod(sorted(set(values)))


def graph_data(roots: list[int], D: int) -> tuple[
    list[tuple[int, int]], dict[int, int]
]:
    edges = [
        (p, q)
        for index, p in enumerate(roots)
        for q in roots[index + 1:]
        if q - p <= 2 * D
    ]
    degrees = {p: 0 for p in roots}
    for p, q in edges:
        degrees[p] += 1
        degrees[q] += 1
    return edges, degrees


def multiplicative_energy(roots: list[int]) -> int:
    multiplicities = Counter(a * b for a in roots for b in roots)
    return sum(count * count for count in multiplicities.values())


DECLARED_CONTROLS = [
    (76, [103, 107, 109, 113], 2, "full_candidate_set"),
    (180, [241, 251, 257, 263, 269], 5, "full_candidate_set"),
    (
        300,
        [401, 409, 419, 421, 431, 433, 439, 443, 449],
        5,
        "full_candidate_set",
    ),
    (300, [401, 419, 431, 449], 5, "declared_sparse_subset"),
]


def rational_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def control(
    M: int, roots: list[int], D: int, label: str
) -> dict[str, Any]:
    assert roots == sorted(set(roots))
    assert set(roots).issubset(candidates(M))
    assert D >= 1

    lower = Fraction(4 * M + 3, 3)
    upper = Fraction(3 * M - 1, 2)
    width = upper - lower
    assert width < lower

    coefficients = polynomial_from_roots(roots)
    derivative_coefficients = derivative(coefficients)
    R = math.prod(roots)
    vandermonde = math.prod(
        q - p
        for index, p in enumerate(roots)
        for q in roots[index + 1:]
    )
    discriminant = vandermonde * vandermonde
    derivative_values = {
        p: evaluate(derivative_coefficients, p) for p in roots
    }
    derivative_product = math.prod(derivative_values.values())
    pair_count = len(roots) * (len(roots) - 1) // 2
    assert derivative_product == (-1) ** pair_count * discriminant

    derivative_at_zero = evaluate(derivative_coefficients, 0)
    assert math.gcd(R, vandermonde) == 1
    assert math.gcd(R, discriminant) == 1
    assert math.gcd(R, derivative_product) == 1
    assert math.gcd(R, derivative_at_zero) == 1
    for p in roots:
        assert derivative_at_zero % p == (
            (-1) ** (len(roots) - 1) * (R // p)
        ) % p

    energy = multiplicative_energy(roots)
    expected_energy = 2 * len(roots) * len(roots) - len(roots)
    assert energy == expected_energy

    edges, degrees = graph_data(roots, D)
    short_gap_product = math.prod(q - p for p, q in edges)
    endpoint_edge_product = math.prod(p * q for p, q in edges)
    clustered = [p for p in roots if degrees[p] > 0]
    cluster_radical = radical_of_support(clustered)
    isolated = [p for p in roots if degrees[p] == 0]
    degree_energy = sum(degree * degree for degree in degrees.values())

    assert math.gcd(R, short_gap_product) == 1
    assert math.gcd(R, endpoint_edge_product) == cluster_radical
    assert endpoint_edge_product == math.prod(
        p ** degrees[p] for p in roots
    )
    assert sum(degrees.values()) == 2 * len(edges)
    assert len(clustered) <= 2 * len(edges)
    assert 4 * len(edges) * len(edges) <= len(clustered) * degree_energy

    isolated_bound = 1 + (
        width.numerator // (width.denominator * 2 * D)
    )
    assert len(isolated) <= isolated_bound

    return {
        "M": M,
        "D": D,
        "label": label,
        "candidate_primes": candidates(M),
        "declared_roots": roots,
        "polynomial_coefficients_ascending": coefficients,
        "R": str(R),
        "vandermonde": str(vandermonde),
        "discriminant": str(discriminant),
        "derivative_values_at_roots": {
            str(p): str(derivative_values[p]) for p in roots
        },
        "product_of_root_derivatives": str(derivative_product),
        "derivative_at_zero": str(derivative_at_zero),
        "all_candidate_gcds_are_one": True,
        "ordered_multiplicative_energy": energy,
        "energy_formula": expected_energy,
        "edges": edges,
        "degrees": {str(p): degrees[p] for p in roots},
        "edge_count": len(edges),
        "degree_energy": degree_energy,
        "short_gap_product": str(short_gap_product),
        "endpoint_edge_product": str(endpoint_edge_product),
        "clustered_roots": clustered,
        "cluster_radical": str(cluster_radical),
        "isolated_roots": isolated,
        "isolated_packing_bound": isolated_bound,
        "interval_width": rational_json(width),
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    threshold_controls = {}
    for c in (Fraction(3, 4), Fraction(1, 1), Fraction(2, 1)):
        threshold_controls[str(c)] = rational_json(
            (2 * c - 1) / (12 * c)
        )
    assert threshold_controls["1"] == {"numerator": 1, "denominator": 12}

    return {
        "schema":
            "item400-j1-discriminant-energy-sieve-threshold-no-go-certificate-v1",
        "item": 400,
        "checked_date_beijing": "2026-09-01",
        "classification":
            "EXACT_DISCRIMINANT_ENERGY_AND_AMBIENT_SIEVE_THRESHOLD_NO_GO",
        "dependency_hashes": DEPENDENCIES,
        "threshold_coefficients_a_of_c": threshold_controls,
        "controls": [
            control(M, roots, D, label)
            for M, roots, D, label in DECLARED_CONTROLS
        ],
        "proved_by_report": [
            "the actual root radical is coprime to the Vandermonde, discriminant, product of root derivatives, and derivative at zero",
            "the short-gap Vandermonde has o(M) logarithmic height at D~log M by the Item391 Selberg theorem but is coprime to the endpoint radical",
            "the ordered multiplicative energy of n distinct primes is exactly 2n^2-n and is independent of clustering",
            "universal graph-energy identities need an external positive-degree vertex bound",
            "the full ambient prime set has logarithmic-window cluster mass at least ((2c-1)/(12c))M+o(M)",
            "the last coefficient exactly saturates the Item395 strict-saving threshold",
            "generic discriminant, energy, Vandermonde, and support-only sieve information cannot give a strict fixed-j1 saving",
        ],
        "strict_scope": {
            "declared_roots_are_algebraic_controls_not_actual_collisions":
                True,
            "actual_gate_scan_performed": False,
            "finite_to_infinite_inference": False,
            "actual_cluster_upper_bound_proved": False,
            "gate_specific_large_sieve_ruled_out": False,
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
