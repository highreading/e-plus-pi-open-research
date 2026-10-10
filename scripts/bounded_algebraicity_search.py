#!/usr/bin/env python3
"""Reproducible bounded searches for algebraic relations of e + pi.

This script has two deliberately separate modes:

1. PSLQ is a discovery heuristic. Failure to find a relation is *not* a proof.
2. ``--certify`` exhaustively excludes integer polynomials in a user-specified
   finite degree/height box.  It uses exact rational enclosures for e + pi and
   fixed-point integer arithmetic, so the bounded exclusion is rigorous.

No finite degree/height exclusion proves transcendence.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp


def atan_interval(inv: int, terms: int) -> tuple[Fraction, Fraction]:
    """Alternating-series enclosure of atan(1/inv).

    ``terms`` is the number of retained terms (j = 0, ..., terms-1).  The
    first omitted term has the sign of the remainder and bounds its magnitude.
    """
    partial = Fraction(0)
    for j in range(terms):
        term = Fraction(1 if j % 2 == 0 else -1, (2 * j + 1) * inv ** (2 * j + 1))
        partial += term
    j = terms
    omitted = Fraction(1 if j % 2 == 0 else -1, (2 * j + 1) * inv ** (2 * j + 1))
    other = partial + omitted
    return min(partial, other), max(partial, other)


def e_interval(n: int) -> tuple[Fraction, Fraction]:
    """Exact enclosure using the first n+1 terms of exp(1)."""
    partial = sum((Fraction(1, math.factorial(k)) for k in range(n + 1)), Fraction(0))
    # For n >= 1, the positive tail is strictly below 1/(n*n!).
    return partial, partial + Fraction(1, n * math.factorial(n))


def e_plus_pi_interval(n_e: int = 80, n_atan: int = 80) -> tuple[Fraction, Fraction]:
    e_lo, e_hi = e_interval(n_e)
    a_lo, a_hi = atan_interval(5, n_atan)
    b_lo, b_hi = atan_interval(239, n_atan)
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    pi_lo = 16 * a_lo - 4 * b_hi
    pi_hi = 16 * a_hi - 4 * b_lo
    return e_lo + pi_lo, e_hi + pi_hi


def nearest_integer_ratio(x_num: int, scale: int) -> int:
    """Nearest integer to x_num/scale, ties away from zero (ties are harmless)."""
    if x_num >= 0:
        return (2 * x_num + scale) // (2 * scale)
    return -nearest_integer_ratio(-x_num, scale)


def rounded_fraction_scaled(x: Fraction, scale: int) -> int:
    q, r = divmod(x.numerator * scale, x.denominator)
    if 2 * r >= x.denominator:
        q += 1
    return q


def certify_box(max_degree: int, height: int, decimal_scale: int) -> dict:
    """Exclude all nonzero P in Z[x] with deg(P)<=d and H(P)<=height.

    For each possible nonconstant coefficient vector, only the nearest allowed
    constant coefficient can minimize |P(s)|.  Powers of s are replaced by
    exact fixed-point integers; an exact uniform error bound proves that the
    observed nonzero gap cannot be caused by interval or rounding error.
    """
    lo, hi = e_plus_pi_interval()
    center = (lo + hi) / 2
    radius = (hi - lo) / 2
    scale = 10**decimal_scale

    rounded_powers: list[int] = [scale]
    power_errors: list[Fraction] = [Fraction(0)]
    for k in range(1, max_degree + 1):
        c_power = center**k
        rounded_powers.append(rounded_fraction_scaled(c_power, scale))
        # |s^k-c^k| <= k*hi^(k-1)*|s-c| for positive s,c.
        power_errors.append(Fraction(1, 2 * scale) + k * hi ** (k - 1) * radius)

    records = []
    for degree in range(1, max_degree + 1):
        min_scaled_gap = None
        minimizer = None
        tested = 0
        coeff_range = range(-height, height + 1)
        for coeffs in itertools.product(coeff_range, repeat=degree):
            # coeffs stores a_1,...,a_degree; require exact degree.
            if coeffs[-1] == 0:
                continue
            tested += 1
            fixed_value = sum(coeffs[k - 1] * rounded_powers[k] for k in range(1, degree + 1))
            target = nearest_integer_ratio(fixed_value, scale)
            target = max(-height, min(height, target))
            scaled_gap = abs(fixed_value - target * scale)
            if min_scaled_gap is None or scaled_gap < min_scaled_gap:
                min_scaled_gap = scaled_gap
                # P(s)=a_0+sum a_k s^k, so a_0=-target.
                minimizer = [-target, *coeffs]

        uniform_error = height * sum(power_errors[1 : degree + 1], Fraction(0))
        assert min_scaled_gap is not None
        fixed_gap = Fraction(min_scaled_gap, scale)
        certified = fixed_gap > uniform_error
        records.append(
            {
                "degree": degree,
                "height": height,
                "vectors_tested": tested,
                "minimizing_coefficients_low_to_high": minimizer,
                "certified_no_relation": certified,
                "gap_decimal": mp.nstr(mp.mpf(fixed_gap.numerator) / fixed_gap.denominator, 20),
                "error_decimal": mp.nstr(mp.mpf(uniform_error.numerator) / uniform_error.denominator, 10),
                "exact_comparison": {
                    "gap_numerator": fixed_gap.numerator,
                    "gap_denominator": fixed_gap.denominator,
                    "error_fraction_sha256": hashlib.sha256(str(uniform_error).encode()).hexdigest(),
                },
            }
        )
        if not certified:
            break

    return {
        "claim_scope": {
            "max_degree": max_degree,
            "naive_height_bound": height,
            "polynomial_coefficients": "integers, absolute value <= height",
        },
        "interval_width_decimal": mp.nstr(mp.mpf((hi - lo).numerator) / (hi - lo).denominator, 10),
        "fixed_point_decimal_scale": decimal_scale,
        "records": records,
        "warning": "A finite degree/height exclusion is not a proof of transcendence.",
    }


def pslq_search(max_degree: int, max_coeff: int, digits: int) -> list[dict]:
    mp.mp.dps = digits
    s = mp.e + mp.pi
    rows = []
    for degree in range(1, max_degree + 1):
        powers = [s**k for k in range(degree + 1)]
        relation = mp.pslq(mp.matrix(powers), tol=mp.mpf(10) ** (-(digits - 30)),
                           maxcoeff=max_coeff, maxsteps=10000)
        rows.append({"degree": degree, "relation": relation})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=5)
    parser.add_argument("--height", type=int, default=10)
    parser.add_argument("--scale-digits", type=int, default=100)
    parser.add_argument("--pslq-max-coeff", type=int, default=10**30)
    parser.add_argument("--digits", type=int, default=500)
    parser.add_argument("--certify", action="store_true")
    parser.add_argument("--pslq", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    output: dict = {}
    if args.certify:
        output["bounded_certificate"] = certify_box(args.max_degree, args.height, args.scale_digits)
    if args.pslq:
        output["pslq_heuristic"] = {
            "digits": args.digits,
            "max_coefficient": args.pslq_max_coeff,
            "records": pslq_search(args.max_degree, args.pslq_max_coeff, args.digits),
            "warning": "PSLQ failure is not a proof of algebraic independence or transcendence.",
        }
    encoded = json.dumps(output, indent=2, sort_keys=True).encode()
    rendered = encoded.decode() + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
