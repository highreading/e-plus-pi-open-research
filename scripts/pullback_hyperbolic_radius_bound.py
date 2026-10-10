#!/usr/bin/env python3
"""Exact interval certificate for the universal analytic pullback radius.

The twice-punctured target C minus {1-i,1+i} is uniformized by the modular
lambda function.  This script evaluates the relevant inverse-lambda lift
using an exact rational truncation of

    H(z) = 2*K(z)/pi = sum binom(2n,n)^2 z^n / 16^n

at z=(1+i)/2.  A geometric tail majorant gives rigorous rational bounds for
the imaginary part y of tau=i*H(conj(z))/H(z), hence for

    R_* = sqrt((1+y)/(1-y)).

The hyperbolic argument establishing universality is in the companion note.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp


QComplex = tuple[Fraction, Fraction]


def cmul(left: QComplex, right: QComplex) -> QComplex:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cadd(left: QComplex, right: QComplex) -> QComplex:
    return left[0] + right[0], left[1] + right[1]


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def decimal_outward(value: Fraction, digits: int, upper: bool) -> str:
    scale = 10**digits
    numerator = value.numerator * scale
    if upper:
        integer = -((-numerator) // value.denominator)
    else:
        integer = numerator // value.denominator
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    whole, fractional = divmod(integer, scale)
    return f"{sign}{whole}.{fractional:0{digits}d}"


def elliptic_h_interval(last_index: int) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """Bounds for Re/Im H((1+i)/2), plus a common absolute tail bound."""
    z: QComplex = (Fraction(1, 2), Fraction(1, 2))
    power: QComplex = (Fraction(1), Fraction(0))
    coefficient = Fraction(1)
    partial: QComplex = (Fraction(0), Fraction(0))
    for n in range(last_index + 1):
        partial = cadd(partial, (coefficient * power[0], coefficient * power[1]))
        power = cmul(power, z)
        coefficient *= Fraction((2 * n + 1) ** 2, (2 * n + 2) ** 2)

    # |z|=1/sqrt(2)<71/100 and every hypergeometric coefficient is <=1.
    q = Fraction(71, 100)
    tail = q ** (last_index + 1) / (1 - q)
    a_lo, a_hi = partial[0] - tail, partial[0] + tail
    b_lo, b_hi = partial[1] - tail, partial[1] + tail
    assert a_lo > 0 and b_lo > 0 and a_lo > b_hi
    return a_lo, a_hi, b_lo, b_hi, tail


def y_interval(last_index: int) -> tuple[Fraction, Fraction, dict]:
    a_lo, a_hi, b_lo, b_hi, tail = elliptic_h_interval(last_index)
    numerator_lo = a_lo * a_lo - b_hi * b_hi
    numerator_hi = a_hi * a_hi - b_lo * b_lo
    denominator_lo = a_lo * a_lo + b_lo * b_lo
    denominator_hi = a_hi * a_hi + b_hi * b_hi
    y_lo = numerator_lo / denominator_hi
    y_hi = numerator_hi / denominator_lo
    assert 0 < y_lo < y_hi < 1
    details = {
        "H_real_lower": fraction_record(a_lo),
        "H_real_upper": fraction_record(a_hi),
        "H_imag_lower": fraction_record(b_lo),
        "H_imag_upper": fraction_record(b_hi),
        "common_component_tail_bound": fraction_record(tail),
    }
    return y_lo, y_hi, details


def strict_sqrt_upper(value: Fraction, digits: int) -> Fraction:
    """Return a positive decimal rational u with u^2>value."""
    scale = 10**digits
    quotient = value.numerator * scale * scale // value.denominator
    integer = math.isqrt(quotient) + 1
    upper = Fraction(integer, scale)
    assert upper * upper > value
    return upper


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--last-index", type=int, default=180)
    parser.add_argument("--decimal-digits", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    y_lo, y_hi, details = y_interval(args.last_index)
    radius_square_upper = (1 + y_hi) / (1 - y_hi)
    radius_upper = strict_sqrt_upper(radius_square_upper, args.decimal_digits)

    mp.mp.dps = max(70, args.decimal_digits + 30)
    z = (mp.mpf(1) + 1j) / 2
    tau = 1j * mp.ellipk(1 - z) / mp.ellipk(z)
    distance = mp.acosh(1 / tau.imag)
    radius = 1 / mp.tanh(distance / 2)

    result = {
        "series_last_index": args.last_index,
        "series_definition": "H(z)=sum_{n>=0} binom(2n,n)^2*z^n/16^n",
        "evaluation_point": "z=(1+i)/2",
        "exact_series_interval_details": details,
        "tau_imaginary_part_y_lower": fraction_record(y_lo),
        "tau_imaginary_part_y_upper": fraction_record(y_hi),
        "tau_imaginary_part_y_decimal_interval": [
            decimal_outward(y_lo, args.decimal_digits, False),
            decimal_outward(y_hi, args.decimal_digits, True),
        ],
        "radius_square_strict_upper": fraction_record(radius_square_upper),
        "universal_radius_strict_upper": fraction_record(radius_upper),
        "universal_radius_strict_upper_decimal": decimal_outward(
            radius_upper, args.decimal_digits, True
        ),
        "high_precision_diagnostic": {
            "tau_real": mp.nstr(tau.real, args.decimal_digits + 10),
            "tau_imag": mp.nstr(tau.imag, args.decimal_digits + 10),
            "tau_modulus": mp.nstr(abs(tau), args.decimal_digits + 10),
            "hyperbolic_distance": mp.nstr(distance, args.decimal_digits + 10),
            "sharp_analytic_radius": mp.nstr(radius, args.decimal_digits + 10),
        },
        "warning": (
            "Rational intervals and the stated decimal upper bound are exact. "
            "The longer mpmath values are diagnostics.  The companion proof "
            "supplies the modular-uniformization and Schwarz--Pick argument."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
