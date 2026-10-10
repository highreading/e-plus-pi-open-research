#!/usr/bin/env python3
"""General exact zero-free-disk certificate for the frozen entire pullback.

This driver exposes the radius, exponential truncation degree, and dyadic
reflection precision as command-line parameters.  It reuses only the exact
integer/rational primitives and the frozen candidate constants from
nonpolynomial_integral_hurwitz_pullback_certificate.py.  It deliberately
omits numerical root and winding diagnostics.

The default target is

    radius = 17679119/10000000, truncation = 24, dyadic bits = 256.

At those values the reversed degree-65 polynomial has 65 strictly positive
fraction-free Schur--Cohn gaps, and its exact recursive boundary lower bound
strictly exceeds the exact exponential-tail upper bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

import nonpolynomial_integral_hurwitz_pullback_certificate as base


sys.set_int_max_str_digits(0)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decimal_string(value: Fraction, digits: int = 30) -> str:
    mp.mp.dps = digits + 15
    return mp.nstr(
        mp.mpf(value.numerator) / mp.mpf(value.denominator), digits
    )


def build_certificate(
    radius: Fraction, truncation: int, dyadic_bits: int
) -> dict:
    assert 0 < radius < 2
    assert truncation >= 0
    assert dyadic_bits >= 8

    jets = base.integral_hurwitz_jets(120)
    real, imag = base.truncated_q_coefficients(truncation)
    initial, cleared_denominator = (
        base.initial_reversed_gaussian_integer_polynomial(
            real, imag, radius
        )
    )
    records, reflection_product, final_constant = (
        base.fraction_free_schur_certificate(initial, dyadic_bits)
    )
    degree = len(real) - 1
    assert len(records) == degree
    assert all(item["gap_positive"] for item in records)

    boundary_squared_lower = 2 * reflection_product**2
    tail_upper = base.exponential_tail_bound(radius, truncation)
    tail_squared_upper = tail_upper**2
    exact_comparison = boundary_squared_lower > tail_squared_upper
    assert exact_comparison
    squared_ratio = boundary_squared_lower / tail_squared_upper

    dependency = Path(base.__file__).resolve()
    return {
        "verdict": "exact zero-free closed disk certified",
        "candidate": {
            "base_terms_K_over_m_factorial_times_zm_1_minus_z": [
                {"m": m, "K": coefficient}
                for m, coefficient in base.BASE_TERMS
            ],
            "exponential_terms_k_over_m_factorial_times_zm_z_minus_1_exp_az": [
                {"m": m, "a": a, "k": k}
                for m, a, k in base.EXPONENTIAL_TERMS
            ],
            "phi_at_zero": "0",
            "phi_at_one": "1",
            "real_entire_coefficients": True,
        },
        "all_order_integral_hurwitz_jet_formula": (
            "For H=(k/m!)*z^m*(z-1)*exp(a*z): H^(m)(0)=-k; "
            "for n=m+r>=m+1, "
            "H^(n)(0)=k*binom(n,m)*(r*a^(r-1)-a^r)."
        ),
        "computed_integral_jet_order": 120,
        "computed_integral_jets_sha256": base.vector_sha256(jets),
        "certified_zero_free_closed_disk_radius": base.fraction_record(
            radius
        ),
        "strict_Taylor_radius_lower_bound": (
            f"{radius.numerator}/{radius.denominator}"
        ),
        "exponential_truncation_degree": truncation,
        "truncated_q_degree": degree,
        "truncated_q_real_coefficients_sha256": hashlib.sha256(
            json.dumps(
                [base.fraction_record(value) for value in real],
                separators=(",", ":"),
                sort_keys=True,
            ).encode()
        ).hexdigest(),
        "truncated_q_imaginary_coefficients_sha256": hashlib.sha256(
            json.dumps(
                [base.fraction_record(value) for value in imag],
                separators=(",", ":"),
                sort_keys=True,
            ).encode()
        ).hexdigest(),
        "initial_reversed_primitive_gaussian_state_sha256": (
            base.gaussian_state_sha256(initial)
        ),
        "initial_cleared_denominator": cleared_denominator,
        "dyadic_reflection_modulus_bits": dyadic_bits,
        "fraction_free_schur_records": records,
        "all_schur_gaps_strictly_positive": True,
        "schur_gap_count": len(records),
        "final_fraction_free_constant": list(final_constant),
        "reflection_factor_product_rational_lower": (
            base.fraction_record(reflection_product)
        ),
        "boundary_modulus_squared_rational_lower": (
            base.fraction_record(boundary_squared_lower)
        ),
        "exponential_tail_rational_upper": base.fraction_record(
            tail_upper
        ),
        "exponential_tail_squared_rational_upper": base.fraction_record(
            tail_squared_upper
        ),
        "exact_boundary_lower_exceeds_tail": exact_comparison,
        "exact_squared_boundary_to_tail_ratio": base.fraction_record(
            squared_ratio
        ),
        "squared_boundary_to_tail_ratio_decimal_diagnostic": (
            decimal_string(squared_ratio)
        ),
        "rouche_conclusion": (
            "q=phi-(1+i) has zero zeros in the certified closed disk; "
            "real coefficients give the same for phi-(1-i)."
        ),
        "dependency": {
            "path": str(dependency),
            "sha256": file_sha256(dependency),
        },
        "warning": (
            "All Schur, dyadic, tail, and Rouche decisions are exact. "
            "The ratio decimal is for readability only."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius-numerator", type=int, default=17679119)
    parser.add_argument("--radius-denominator", type=int, default=10000000)
    parser.add_argument("--truncation", type=int, default=24)
    parser.add_argument("--dyadic-bits", type=int, default=256)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    certificate = build_certificate(
        Fraction(args.radius_numerator, args.radius_denominator),
        args.truncation,
        args.dyadic_bits,
    )
    rendered = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
