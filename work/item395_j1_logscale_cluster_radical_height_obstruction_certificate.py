#!/usr/bin/env python3
"""Deterministic exact controls for Item 395.

The all-M logarithmic norm estimates and capacity theorem are in the report.
This standard-library checker pins Item 391 and independently verifies the
shifted-resultant factorization, both endpoint gcd radicals, the aggregate
cluster radical, the isolated-root packing decomposition, and exact rational
parameters in declared root-set controls.  The declared root sets are not
claimed to be actual collision sets; no gate scan is performed.
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
DEFAULT_OUTPUT = HERE / "item395_j1_logscale_cluster_radical_height_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item391_j1_logarithmic_spacing_resultant_criterion_report.md":
        "304713605fcf33675a882b4f333d60cc35fd36bc6b860353eff36472d4a27564",
    "scripts/item391_j1_logarithmic_spacing_resultant_criterion_certificate.py":
        "419c689a149be1056eca68410f5b8a756c9d3674a715df2602640cc3c1bf40ff",
    "results/item391_j1_logarithmic_spacing_resultant_criterion_certificate.json":
        "542676c4e2acf6718c63b362d6bbd7e3358cbcfb655033c6db1bc5e20ed7602f",
    "results/item391_j1_logarithmic_spacing_resultant_criterion_certificate_replay.json":
        "542676c4e2acf6718c63b362d6bbd7e3358cbcfb655033c6db1bc5e20ed7602f",
    "results/item391_j1_logarithmic_spacing_resultant_criterion_ledger_delta.json":
        "156ea31c7a4f47b6d9e9d0f7cc89a862d0837fdfa3fc45b52f631b40bc505d5c",
    "manifests/item391_j1_logarithmic_spacing_resultant_criterion_manifest.json":
        "07e4a438dbc32e52e67587d7a0fe4886d23e584fd7fae34aafe7f234c334e511",
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


def polynomial_from_roots(roots: list[int]) -> list[int]:
    coefficients = [1]
    for root in roots:
        output = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            output[index] -= root * coefficient
            output[index + 1] += coefficient
        coefficients = output
    return coefficients


def evaluate(coefficients: list[int], value: int) -> int:
    output = 0
    for coefficient in reversed(coefficients):
        output = output * value + coefficient
    return output


def resultant_direct(roots: list[int], d: int) -> int:
    output = 1
    for p in roots:
        for q in roots:
            output *= p + 2 * d - q
    return output


def resultant_paired(roots: list[int], d: int) -> int:
    output = (2 * d) ** len(roots)
    for left_index, left in enumerate(roots):
        for right in roots[left_index + 1:]:
            gap = right - left
            output *= (2 * d) ** 2 - gap ** 2
    return output


def radical(values: list[int]) -> int:
    output = 1
    for value in sorted(set(values)):
        output *= value
    return output


def control(M: int, roots: list[int], D: int) -> dict[str, Any]:
    candidate_primes = candidates(M)
    assert roots == sorted(set(roots))
    assert set(roots).issubset(candidate_primes)
    lower = Fraction(4 * M + 3, 3)
    upper = Fraction(3 * M - 1, 2)
    span = upper - lower
    assert span == Fraction(M - 9, 6)
    assert 2 * D < lower
    assert upper + 2 * D < 2 * lower

    root_set = set(roots)
    R = math.prod(roots)
    coefficients = polynomial_from_roots(roots)
    lower_endpoint_sets: list[list[int]] = []
    upper_endpoint_sets: list[list[int]] = []
    shift_controls = []
    for d in range(1, D + 1):
        direct = resultant_direct(roots, d)
        paired = resultant_paired(roots, d)
        assert direct == paired

        lower_endpoints = [p for p in roots if p + 2 * d in root_set]
        upper_endpoints = [p for p in roots if p - 2 * d in root_set]
        lower_endpoint_sets.append(lower_endpoints)
        upper_endpoint_sets.append(upper_endpoints)

        norm_minus = ((-1) ** len(roots)) * evaluate(coefficients, 2 * d)
        norm_plus = ((-1) ** len(roots)) * evaluate(coefficients, -2 * d)
        assert norm_minus == math.prod(p - 2 * d for p in roots)
        assert norm_plus == math.prod(p + 2 * d for p in roots)
        lower_radical = radical(lower_endpoints)
        upper_radical = radical(upper_endpoints)
        assert math.gcd(R, abs(norm_minus)) == lower_radical
        assert math.gcd(R, abs(norm_plus)) == upper_radical

        if direct:
            negative_factors = sum(
                1
                for left_index, left in enumerate(roots)
                for right in roots[left_index + 1:]
                if right - left > 2 * d
            )
            expected_sign = -1 if negative_factors % 2 else 1
            assert (1 if direct > 0 else -1) == expected_sign
        else:
            negative_factors = None
            expected_sign = 0

        # Exact rational parameters in the logarithmic inequalities of the report.
        minus_log_upper_parameter = Fraction(2 * d * len(roots), 1) / (lower - 2 * d)
        plus_log_upper_parameter = Fraction(2 * d * len(roots), 1) / lower
        assert 0 < norm_minus <= R <= norm_plus

        shift_controls.append({
            "d": d,
            "direct_resultant": str(direct),
            "paired_resultant": str(paired),
            "resultant_zero": direct == 0,
            "negative_gap_factors_if_nonzero": negative_factors,
            "resultant_sign_if_nonzero": expected_sign,
            "norm_minus": str(norm_minus),
            "norm_plus": str(norm_plus),
            "lower_endpoint_radical": str(lower_radical),
            "upper_endpoint_radical": str(upper_radical),
            "minus_log_upper_parameter": {
                "numerator": minus_log_upper_parameter.numerator,
                "denominator": minus_log_upper_parameter.denominator,
            },
            "plus_log_upper_parameter": {
                "numerator": plus_log_upper_parameter.numerator,
                "denominator": plus_log_upper_parameter.denominator,
            },
        })

    clustered = sorted(set().union(*map(set, lower_endpoint_sets + upper_endpoint_sets)))
    isolated = [p for p in roots if p not in set(clustered)]
    cluster_radical = radical(clustered)
    isolated_radical = radical(isolated)
    assert R == cluster_radical * isolated_radical
    assert all(
        right - left > 2 * D
        for left_index, left in enumerate(isolated)
        for right in isolated[left_index + 1:]
    )
    packing_bound = 1 + (M - 9) // (12 * D)
    assert len(isolated) <= packing_bound

    # Verify the aggregate endpoint union directly, without factoring a large
    # product or confusing a root-set product with an integer radical operation.
    endpoint_products = [
        int(entry["lower_endpoint_radical"]) * int(entry["upper_endpoint_radical"])
        for entry in shift_controls
    ]
    product_all = math.prod(endpoint_products)
    assert product_all % cluster_radical == 0
    assert all(product_all % p == 0 for p in clustered)
    assert all(product_all % p != 0 for p in isolated)

    return {
        "M": M,
        "D": D,
        "candidate_primes": candidate_primes,
        "declared_roots": roots,
        "collision_polynomial_coefficients_ascending": [str(value) for value in coefficients],
        "R": str(R),
        "clustered_roots": clustered,
        "isolated_roots": isolated,
        "cluster_radical": str(cluster_radical),
        "isolated_radical": str(isolated_radical),
        "R_equals_cluster_times_isolated": True,
        "isolated_packing_bound": packing_bound,
        "shift_controls": shift_controls,
    }


DECLARED_CONTROLS = [
    (180, [241, 251, 257, 263, 269], 3),
    (180, [241, 257, 269], 5),
    (300, [401, 409, 419, 421, 431, 433, 439, 443, 449], 2),
    (300, [401, 419, 431, 449], 5),
]


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    return {
        "schema": "item395-j1-logscale-cluster-radical-height-obstruction-certificate-v1",
        "item": 395,
        "checked_date_beijing": "2026-09-01",
        "classification": "EXACT_CLUSTER_RADICAL_CAPACITY_REDUCTION_AND_LOGSCALE_HEIGHT_NO_GO",
        "dependency_hashes": DEPENDENCIES,
        "controls": [control(M, roots, D) for M, roots, D in DECLARED_CONTROLS],
        "proved_by_report": [
            "exact discriminant-type paired factorization of each shifted resultant",
            "exact aggregate logarithmic-window cluster radical",
            "cluster-plus-isolated master capacity inequality",
            "sharp sufficient paired-mass threshold (2c-1)M/(12c) for strict saving",
            "logarithmic shifted norms differ from the collision radical by at most exp(c/4+o(1))",
            "ordinary norm height, resultant height, and resultant sign alone give no strict capacity reduction",
        ],
        "strict_scope": {
            "declared_roots_are_algebraic_controls_not_actual_collisions": True,
            "actual_gate_scan_performed": False,
            "finite_to_infinite_inference": False,
            "logarithmic_pair_freeness_proved": False,
            "strict_paired_mass_bound_proved": False,
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
