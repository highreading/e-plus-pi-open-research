#!/usr/bin/env python3
"""Deterministic replay for Item 393's small-prime stratum ledger.

The PNT and irrationality-measure inputs are frozen dependencies.  This
script verifies their exact rationalized capacity arithmetic, the strict
inequalities used in the report, and the primewise/layerwise factorization
on a transparent algebraic test vector.  The test vector is not actual-row
data and is not used as evidence about valuations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def rational_decimal(text: str) -> Fraction:
    if "." not in text:
        return Fraction(int(text), 1)
    whole, fractional = text.split(".")
    sign = -1 if whole.startswith("-") else 1
    unsigned = whole[1:] if whole.startswith("-") else whole
    numerator = int(unsigned + fractional)
    return Fraction(sign * numerator, 10 ** len(fractional))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def product_from_exponents(exponents: dict[int, int]) -> int:
    value = 1
    for prime, exponent in exponents.items():
        value *= prime**exponent
    return value


def layer_sets(exponents: dict[int, int]) -> list[list[int]]:
    depth = max(exponents.values(), default=0)
    return [
        sorted(prime for prime, exponent in exponents.items() if exponent >= layer)
        for layer in range(1, depth + 1)
    ]


def layer_product(layers: list[list[int]]) -> int:
    value = 1
    for layer in layers:
        for prime in layer:
            value *= prime
    return value


def build_payload() -> dict[str, object]:
    getcontext().prec = 70

    # Certified endpoint choices from the frozen analytic and pi-measure
    # packages.  The rational mu_bar is strictly above the published bound.
    h_upper = rational_decimal(
        "2.3246783391437311102576951141305620522234564135413822"
    )
    d_lower = rational_decimal(
        "2.3370623743589729958539297805468573066534630858270130"
    )
    mu_bar = rational_decimal("7.103205334138")
    full_content_safe = h_upper - d_lower / mu_bar
    declared_full_upper = rational_decimal("1.995663160161498")
    if not full_content_safe < declared_full_upper:
        raise AssertionError("rationalized full-content ceiling failed")

    booked_r1_lower = rational_decimal("0.1365141682948128")
    small_remainder_safe = declared_full_upper - booked_r1_lower
    declared_small_upper = rational_decimal("1.859148991866686")
    if not small_remainder_safe < declared_small_upper:
        raise AssertionError("small-prime residual ceiling failed")

    r1 = Decimal("0.1365141682948128184504238226")
    rank_two_radical_ceiling = Decimal("0.1483939616269088458700310053")
    forced_radical_ceiling = r1 + rank_two_radical_ceiling
    threshold = Decimal("1.1561471519642446123307302239")
    deficit_after_booking = threshold - r1
    postbook_deep_tail_needed = deficit_after_booking - Decimal(1)
    raw_multiplicity_tail_needed = threshold - Decimal(1)
    forced_fifth_tail_needed = threshold - Decimal(4) * forced_radical_ceiling

    if not postbook_deep_tail_needed > 0:
        raise AssertionError("one post-book universal layer unexpectedly suffices")
    if not raw_multiplicity_tail_needed > 0:
        raise AssertionError("one raw radical layer unexpectedly suffices")
    if not forced_fifth_tail_needed > 0:
        raise AssertionError("four forced layers unexpectedly suffice")
    if not Decimal(5) * forced_radical_ceiling > threshold:
        raise AssertionError("five forced layers should be the first capacity-admissible count")

    forced_postbook_rows = []
    for residual_depth in range(1, 5):
        ceiling = r1 + Decimal(residual_depth) * forced_radical_ceiling
        forced_postbook_rows.append(
            {
                "postbook_residual_depth": residual_depth,
                "ceiling": str(ceiling),
                "threshold_minus_ceiling": str(threshold - ceiling),
                "can_reach_threshold_by_capacity": ceiling >= threshold,
            }
        )

    # Algebraic primewise replay.  Baseline 2 and the booked H-primes are
    # removed exactly once; the cutoff separates the large component.
    cutoff = 13
    booked_h = {3, 7}
    valuations = {2: 3, 3: 4, 5: 1, 7: 2, 11: 0, 13: 2, 17: 3}
    baseline_exponents = {
        prime: (1 if prime == 2 else 0) + (1 if prime in booked_h else 0)
        for prime in valuations
        if prime <= cutoff
    }
    small_residual_exponents = {
        prime: valuations[prime] - baseline_exponents.get(prime, 0)
        for prime in valuations
        if prime <= cutoff and valuations[prime] - baseline_exponents.get(prime, 0) > 0
    }
    large_exponents = {
        prime: exponent for prime, exponent in valuations.items() if prime > cutoff and exponent > 0
    }
    baseline_value = product_from_exponents(
        {prime: exponent for prime, exponent in baseline_exponents.items() if exponent > 0}
    )
    small_residual_value = product_from_exponents(small_residual_exponents)
    large_value = product_from_exponents(large_exponents)
    original_value = product_from_exponents(
        {prime: exponent for prime, exponent in valuations.items() if exponent > 0}
    )
    if baseline_value * small_residual_value * large_value != original_value:
        raise AssertionError("primewise factorization failed")

    residual_layers = layer_sets(small_residual_exponents)
    raw_small_exponents = {
        prime: exponent for prime, exponent in valuations.items() if prime <= cutoff and exponent > 0
    }
    raw_layers = layer_sets(raw_small_exponents)
    if layer_product(residual_layers) != small_residual_value:
        raise AssertionError("post-book layer cake failed")
    if layer_product(raw_layers) != product_from_exponents(raw_small_exponents):
        raise AssertionError("raw layer cake failed")

    generator = Path(__file__)
    return {
        "schema": "item393-mixed-cubic-small-prime-strata-ceiling-v1",
        "generator": generator.name,
        "generator_sha256": hashlib.sha256(generator.read_bytes()).hexdigest(),
        "exact_decomposition": {
            "baseline": "2*product_{p in H_m} p",
            "small_remainder": "product_{p<=6m} p^(v_p(c_m)-1_{p=2}-1_{p in H_m})",
            "large_component": "product_{p>6m} p^v_p(c_m)",
            "identity": "c_m=baseline*small_remainder*large_component",
            "warning": "G_m was already divided out before c_m; no whole M or T factor is subtracted again.",
        },
        "rationalized_global_ceiling": {
            "h_upper": fraction_text(h_upper),
            "d_lower": fraction_text(d_lower),
            "mu_bar": fraction_text(mu_bar),
            "h_upper-d_lower/mu_bar": fraction_text(full_content_safe),
            "declared_full_upper": fraction_text(declared_full_upper),
            "booked_r1_lower": fraction_text(booked_r1_lower),
            "small_remainder_from_declared_bounds": fraction_text(small_remainder_safe),
            "declared_small_upper": fraction_text(declared_small_upper),
            "conclusion": "limsup log(c_{m,<=6m,rem})/(6m)<1.859148991866686",
        },
        "capacity": {
            "threshold": str(threshold),
            "booked_r1": str(r1),
            "deficit_after_booking": str(deficit_after_booking),
            "universal_layer_ceiling": "1",
            "postbook_layers_j_ge_2_needed": str(postbook_deep_tail_needed),
            "raw_layers_k_ge_2_needed": str(raw_multiplicity_tail_needed),
            "rank_two_radical_ceiling": str(rank_two_radical_ceiling),
            "forced_radical_ceiling": str(forced_radical_ceiling),
            "four_forced_layers": str(Decimal(4) * forced_radical_ceiling),
            "forced_raw_layers_k_ge_5_needed": str(forced_fifth_tail_needed),
            "five_forced_layers": str(Decimal(5) * forced_radical_ceiling),
            "forced_postbook_rows": forced_postbook_rows,
        },
        "algebraic_layer_replay": {
            "actual_row_data": False,
            "cutoff": cutoff,
            "booked_H": sorted(booked_h),
            "valuations": {str(key): value for key, value in valuations.items()},
            "baseline_exponents": {str(key): value for key, value in baseline_exponents.items()},
            "small_residual_exponents": {
                str(key): value for key, value in small_residual_exponents.items()
            },
            "large_exponents": {str(key): value for key, value in large_exponents.items()},
            "baseline_value": str(baseline_value),
            "small_residual_value": str(small_residual_value),
            "large_value": str(large_value),
            "original_value": str(original_value),
            "factorization_verified": True,
            "postbook_layers": residual_layers,
            "raw_small_layers": raw_layers,
            "both_layer_cakes_verified": True,
            "warning": "This vector certifies only the algebra of de-overlap and layer cake.",
        },
        "strategic_status": {
            "total_small_remainder_ceiling_improved": True,
            "ceiling_source": "global pi-measure bound minus the booked Cartier mass",
            "new_route1_booking": "0",
            "remaining_unbounded_information": [
                "actual aggregate post-book layers j>=2",
                "actual raw multiplicity layers k>=2",
                "actual forced fifth-and-deeper layer",
                "off-forced small-prime content",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    rendered = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
