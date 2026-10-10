#!/usr/bin/env python3
"""Deterministic exact controls for Item 391.

The asymptotic Selberg-sieve argument is proved in the report.  This checker
pins the relevant fixed-j=1 sources and verifies the exact candidate-row,
collision-polynomial, shifted-resultant, shifted-norm/gcd, packing, and
finite Wallis-product identities used there.  The root sets below are
predeclared algebraic controls only; they are not claimed to be actual
collision sets and no collision search is performed.
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
DEFAULT_OUTPUT = HERE / "item391_j1_logarithmic_spacing_resultant_criterion_certificate.json"

DEPENDENCIES = {
    "sources/item216_gosper_phase_obstruction_report.md":
        "4465d67b3d6560dcb9033bea162eeadb76ddbc8a85c6a118c5eb0486a4704cb4",
    "sources/item217_common_log_invariant_report.md":
        "89e8f8f7f9fabdafa8d9330171eb388e854df835c10ee50be4f4f5b43e028466",
    "sources/item279_j1_bounded_cluster_report.md":
        "533383bdd073c2950ae5ff65e9c2888a80242c58317c6ca89306bd2d1864a28e",
    "sources/item363_j1_joint_gate_crt_elimination_no_go_report.md":
        "377ed30c0c6be630c124ccd3050d37176264c659d23a502453a9aaa34ff132ee",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_report.md":
        "9a7340ec9960ad6278e47c63de728048b52cfe59fc957ca93ea32558c6c39342",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_certificate.py":
        "c574d6f44e66380e53e0e4450190e349bf0d4875afbcc4c65045c354658ed231",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_certificate.json":
        "5fbdcbe3e7348f3776dab07c5dd6492278951929f3461f85fb78e5d11129e873",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_certificate_replay.json":
        "5fbdcbe3e7348f3776dab07c5dd6492278951929f3461f85fb78e5d11129e873",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_ledger_delta.json":
        "1327b3162009527b08e51a453f05fcb99c3cb2830ab65f3d0ad4e07cd06a1241",
    "work/item384_j1_universal_filtered_selector_capacity_no_go_manifest.json":
        "16cee992a61d220fb69a49e040e3c9299be087c0830cdfb1fe65f7a31168434b",
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
    upper = (3 * M - 1) // 2
    return [
        p for p in range(2, upper + 1)
        if is_prime(p) and 3 * p >= 4 * M + 3 and 2 * p <= 3 * M - 1
    ]


def row(M: int, p: int) -> tuple[int, int]:
    h = 3 * M - 2 * p
    numerator = 3 * p - 4 * M - 1
    assert numerator % 2 == 0
    s = numerator // 2
    assert h >= 1 and s >= 1
    assert p == 4 * h + 6 * s + 3
    assert M == 3 * h + 4 * s + 2
    return h, s


def polynomial_from_roots(roots: list[int]) -> list[int]:
    """Ascending coefficients of prod(X-root)."""
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


def shifted_resultant_product(roots: list[int], d: int) -> int:
    output = 1
    for p in roots:
        for q in roots:
            output *= p + 2 * d - q
    return output


def pair_lower_product(roots: list[int], d: int) -> int:
    root_set = set(roots)
    output = 1
    for p in roots:
        if p + 2 * d in root_set:
            output *= p
    return output


def pair_upper_product(roots: list[int], d: int) -> int:
    root_set = set(roots)
    output = 1
    for p in roots:
        if p - 2 * d in root_set:
            output *= p
    return output


def shifted_norm(roots: list[int], d: int) -> int:
    output = 1
    for q in roots:
        output *= q - 2 * d
    return output


def shifted_norm_plus(roots: list[int], d: int) -> int:
    output = 1
    for q in roots:
        output *= q + 2 * d
    return output


def factor_distinct(value: int) -> list[int]:
    output: list[int] = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            output.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        output.append(remaining)
    return output


def singular_factor(d: int) -> Fraction:
    output = Fraction(1)
    for prime in factor_distinct(d):
        if prime > 2:
            output *= Fraction(prime - 1, prime - 2)
    return output


def singular_factor_divisor_expansion(d: int) -> Fraction:
    odd_primes = [prime for prime in factor_distinct(d) if prime > 2]
    output = Fraction(0)
    for mask in range(1 << len(odd_primes)):
        term = Fraction(1)
        for index, prime in enumerate(odd_primes):
            if mask & (1 << index):
                term *= Fraction(1, prime - 2)
        output += term
    return output


def wallis_partial(number_of_terms: int) -> Fraction:
    output = Fraction(1)
    for k in range(1, number_of_terms + 1):
        output *= Fraction(4 * k * k, (2 * k - 1) * (2 * k + 1))
    return output


DECLARED_ROOT_SETS = {
    76: [
        [],
        [103],
        [103, 107],
        [103, 109, 113],
        [103, 107, 109, 113],
    ],
    180: [
        [241, 251, 263],
        [241, 257, 269],
        [251, 257, 263, 269],
        [241, 251, 257, 263, 269],
    ],
}


def root_set_control(M: int, roots: list[int]) -> dict[str, Any]:
    candidate_primes = candidates(M)
    assert roots == sorted(set(roots))
    assert set(roots).issubset(candidate_primes)
    for p in candidate_primes:
        row(M, p)

    coefficients = polynomial_from_roots(roots)
    radical = math.prod(roots)
    lower = Fraction(4 * M + 3, 3)
    upper = Fraction(3 * M - 1, 2)
    interval_length = upper - lower
    assert interval_length == Fraction(M - 9, 6)

    d_controls: list[dict[str, Any]] = []
    for d in range(1, 13):
        assert 2 * d < lower
        assert upper + 2 * d < 2 * lower
        resultant = shifted_resultant_product(roots, d)
        has_pair = any(p + 2 * d in set(roots) for p in roots)
        assert (resultant == 0) == has_pair

        norm = shifted_norm(roots, d)
        assert norm == ((-1) ** len(roots)) * evaluate(coefficients, 2 * d)
        pair_product = pair_lower_product(roots, d)
        assert math.gcd(radical, abs(norm)) == pair_product
        norm_plus = shifted_norm_plus(roots, d)
        assert norm_plus == ((-1) ** len(roots)) * evaluate(coefficients, -2 * d)
        upper_pair_product = pair_upper_product(roots, d)
        assert math.gcd(radical, abs(norm_plus)) == upper_pair_product
        d_controls.append({
            "d": d,
            "has_shifted_pair": has_pair,
            "resultant_product": str(resultant),
            "shifted_norm": str(norm),
            "pair_lower_radical": str(pair_product),
            "shifted_norm_plus": str(norm_plus),
            "pair_upper_radical": str(upper_pair_product),
        })

    if len(roots) <= 1:
        minimum_offset = None
        pair_free_D = 12
    else:
        minimum_offset = min((right - left) // 2 for left, right in zip(roots, roots[1:]))
        pair_free_D = min(12, minimum_offset - 1)
    if pair_free_D >= 1:
        packing_bound = 1 + (M - 9) // (12 * pair_free_D)
        assert len(roots) <= packing_bound
    else:
        packing_bound = None

    return {
        "M": M,
        "candidate_primes": candidate_primes,
        "candidate_rows": {
            str(p): {"h": row(M, p)[0], "s": row(M, p)[1]}
            for p in candidate_primes
        },
        "declared_roots": roots,
        "collision_polynomial_coefficients_ascending": [str(value) for value in coefficients],
        "radical": str(radical),
        "interval_length": {
            "numerator": interval_length.numerator,
            "denominator": interval_length.denominator,
        },
        "minimum_adjacent_offset": minimum_offset,
        "pair_free_D_control": pair_free_D,
        "packing_bound_at_pair_free_D": packing_bound,
        "shift_controls": d_controls,
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()

    root_controls = [
        root_set_control(M, roots)
        for M, root_sets in DECLARED_ROOT_SETS.items()
        for roots in root_sets
    ]

    wallis_controls = []
    previous = Fraction(1)
    for terms in [1, 2, 5, 10, 50, 100]:
        value = wallis_partial(terms)
        assert value > previous
        assert value < 2
        previous = value
        wallis_controls.append({
            "terms": terms,
            "numerator": str(value.numerator),
            "denominator": str(value.denominator),
            "decimal_18": f"{float(value):.18f}",
        })

    singular_controls = []
    for D in [1, 2, 5, 10, 50, 100, 250]:
        total = Fraction(0)
        for d in range(1, D + 1):
            product_form = singular_factor(d)
            expansion_form = singular_factor_divisor_expansion(d)
            assert product_form == expansion_form
            total += product_form
        # The report proves sum_{d<=D} S(d) <= D*pi/2 < 2D.
        assert total < 2 * D
        singular_controls.append({
            "D": D,
            "sum_numerator": str(total.numerator),
            "sum_denominator": str(total.denominator),
            "ratio_to_D_18": f"{float(total / D):.18f}",
            "strictly_below_2D": True,
        })

    return {
        "schema": "item391-j1-logarithmic-spacing-resultant-criterion-certificate-v1",
        "item": 391,
        "checked_date_beijing": "2026-09-01",
        "dependency_hashes": DEPENDENCIES,
        "classification": "EXACT_ACTUAL_FAMILY_REDUCTION_AND_UNCONDITIONAL_SUBLOG_CLUSTER_BOUND",
        "controls": {
            "root_sets": root_controls,
            "wallis_partial_products": wallis_controls,
            "singular_factor_averages": singular_controls,
        },
        "proved_by_report": [
            "exact actual-collision polynomial shifted-resultant zero criterion",
            "exact shifted norm/gcd identity for each tied offset",
            "uniform Selberg pair-sieve bound and o(M) endpoint mass for D=o(log M)",
            "pair-free and bounded-occupancy packing capacity criteria with exact constants",
            "positive normalized mass forces an actual collision pair at logarithmic offset",
        ],
        "strict_scope": {
            "root_sets_are_algebraic_controls_not_actual_collisions": True,
            "actual_collision_search_performed": False,
            "finite_to_infinite_inference": False,
            "nonvanishing_of_actual_shifted_resultants_proved": False,
            "actual_W_is_o_M_proved": False,
            "new_booked_mass": 0,
            "new_capacity_reduction": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
