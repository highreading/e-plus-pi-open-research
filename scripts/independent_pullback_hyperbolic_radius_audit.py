#!/usr/bin/env python3
"""Independent exact audit of the universal pullback-radius certificate.

The program under audit advances the hypergeometric coefficients recursively
and stores complex rationals as pairs of Fraction objects.  This audit instead
uses SymPy's exact Gaussian-rational expressions and the closed binomial
coefficient formula term by term.  It compares every exact interval field to
the frozen JSON and independently performs the strict decimal comparisons.

The modular-uniformization and Schwarz--Pick proof is audited in the companion
Markdown note; finite-precision theta calculations here are diagnostics only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


sys.set_int_max_str_digits(0)


FROZEN_HASHES = {
    "sources/universal_pullback_radius_bound.md":
        "eb753d610e81ffd909c97ae1e4c128f7cbdaa7fd90607edf2d9817ab37faac17",
    "scripts/pullback_hyperbolic_radius_bound.py":
        "f83f5d27a302c8fa74b4b0def2ada68037c1f0e555f1031410f1fd9eb10d3846",
    "results/pullback_hyperbolic_radius_bound.json":
        "f981094e58a95ad0070939bda6f2db0b6ea0b2bdef9ad33ba6b379971bef9993",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction(value: sp.Rational | int) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def fraction_record(value: sp.Rational | int) -> dict[str, int]:
    value = sp.Rational(value)
    return {"numerator": int(value.p), "denominator": int(value.q)}


def from_record(record: dict[str, int]) -> sp.Rational:
    return sp.Rational(record["numerator"], record["denominator"])


def decimal_floor(value: sp.Rational, digits: int) -> str:
    scale = 10**digits
    integer = int(sp.floor(value * scale))
    whole, remainder = divmod(abs(integer), scale)
    sign = "-" if integer < 0 else ""
    return f"{sign}{whole}.{remainder:0{digits}d}"


def decimal_ceil(value: sp.Rational, digits: int) -> str:
    scale = 10**digits
    integer = int(sp.ceiling(value * scale))
    whole, remainder = divmod(abs(integer), scale)
    sign = "-" if integer < 0 else ""
    return f"{sign}{whole}.{remainder:0{digits}d}"


def symbolic_series_interval(last_index: int) -> dict:
    z = (1 + sp.I) / 2
    partial = sp.Add(*[
        sp.Rational(sp.binomial(2 * n, n) ** 2, 16**n) * z**n
        for n in range(last_index + 1)
    ])
    partial = sp.expand_complex(sp.expand(partial))
    partial_real = sp.Rational(sp.re(partial))
    partial_imag = sp.Rational(sp.im(partial))

    q = sp.Rational(71, 100)
    tail = q ** (last_index + 1) / (1 - q)
    a_lo, a_hi = partial_real - tail, partial_real + tail
    b_lo, b_hi = partial_imag - tail, partial_imag + tail
    assert 0 < b_lo < b_hi < a_lo < a_hi

    numerator_lo = a_lo**2 - b_hi**2
    numerator_hi = a_hi**2 - b_lo**2
    denominator_lo = a_lo**2 + b_lo**2
    denominator_hi = a_hi**2 + b_hi**2
    y_lo = sp.factor(numerator_lo / denominator_hi)
    y_hi = sp.factor(numerator_hi / denominator_lo)
    assert 0 < y_lo < y_hi < 1

    radius_square_upper = sp.factor((1 + y_hi) / (1 - y_hi))
    asserted_radius_upper = sp.Rational(5262410788162386, 10**15)
    asserted_y_decimal_lower = sp.Rational(930296508588526, 10**15)
    asserted_y_decimal_upper = sp.Rational(930296508588527, 10**15)
    assert y_lo > asserted_y_decimal_lower
    assert y_hi < asserted_y_decimal_upper
    assert asserted_radius_upper**2 > radius_square_upper

    return {
        "last_index": last_index,
        "partial_real": fraction_record(partial_real),
        "partial_imag": fraction_record(partial_imag),
        "H_real_lower": fraction_record(a_lo),
        "H_real_upper": fraction_record(a_hi),
        "H_imag_lower": fraction_record(b_lo),
        "H_imag_upper": fraction_record(b_hi),
        "common_component_tail_bound": fraction_record(tail),
        "y_lower": fraction_record(y_lo),
        "y_upper": fraction_record(y_hi),
        "outward_y_decimal_interval": [
            decimal_floor(y_lo, 15),
            decimal_ceil(y_hi, 15),
        ],
        "strict_y_decimal_comparisons": {
            "y_lower_gt_0.930296508588526": bool(
                y_lo > asserted_y_decimal_lower
            ),
            "y_upper_lt_0.930296508588527": bool(
                y_hi < asserted_y_decimal_upper
            ),
        },
        "radius_square_upper": fraction_record(radius_square_upper),
        "asserted_radius_upper": fraction_record(asserted_radius_upper),
        "asserted_radius_upper_decimal": "5.262410788162386",
        "strict_radius_square_comparison": bool(
            asserted_radius_upper**2 > radius_square_upper
        ),
        "positive_exact_square_margin": fraction_record(
            sp.factor(asserted_radius_upper**2 - radius_square_upper)
        ),
    }


def compare_archived(root: Path, exact: dict) -> dict:
    archived = json.loads(
        (root / "results/pullback_hyperbolic_radius_bound.json").read_text()
    )
    details = archived["exact_series_interval_details"]
    comparisons = {
        "series_last_index": exact["last_index"] == archived["series_last_index"],
        "H_real_lower": exact["H_real_lower"] == details["H_real_lower"],
        "H_real_upper": exact["H_real_upper"] == details["H_real_upper"],
        "H_imag_lower": exact["H_imag_lower"] == details["H_imag_lower"],
        "H_imag_upper": exact["H_imag_upper"] == details["H_imag_upper"],
        "common_component_tail_bound": (
            exact["common_component_tail_bound"]
            == details["common_component_tail_bound"]
        ),
        "y_lower": (
            exact["y_lower"] == archived["tau_imaginary_part_y_lower"]
        ),
        "y_upper": (
            exact["y_upper"] == archived["tau_imaginary_part_y_upper"]
        ),
        "outward_y_decimal_interval": (
            exact["outward_y_decimal_interval"]
            == archived["tau_imaginary_part_y_decimal_interval"]
        ),
        "radius_square_upper": (
            exact["radius_square_upper"]
            == archived["radius_square_strict_upper"]
        ),
        "asserted_radius_upper": (
            exact["asserted_radius_upper"]
            == archived["universal_radius_strict_upper"]
        ),
        "asserted_radius_upper_decimal": (
            exact["asserted_radius_upper_decimal"]
            == archived["universal_radius_strict_upper_decimal"]
        ),
    }
    return {"field_comparisons": comparisons, "all_exact_fields_agree": all(comparisons.values())}


def theta_inverse_diagnostic() -> dict[str, str | bool]:
    """Check the inverse-lambda convention numerically via theta constants."""
    mp.mp.dps = 80
    z = mp.mpc(mp.mpf("0.5"), mp.mpf("0.5"))
    tau = 1j * mp.ellipk(1 - z) / mp.ellipk(z)
    nome = mp.exp(mp.pi * 1j * tau)
    recovered = (mp.jtheta(2, 0, nome) / mp.jtheta(3, 0, nome)) ** 4
    residual = abs(recovered - z)
    return {
        "tau_real": mp.nstr(tau.real, 70),
        "tau_imag": mp.nstr(tau.imag, 70),
        "tau_modulus": mp.nstr(abs(tau), 70),
        "lambda_via_theta_real": mp.nstr(recovered.real, 70),
        "lambda_via_theta_imag": mp.nstr(recovered.imag, 70),
        "absolute_residual": mp.nstr(residual, 12),
        "residual_less_than_1e-70": bool(residual < mp.mpf("1e-70")),
    }


def finite_gamma2_diagnostic(entry_bound: int = 21) -> dict:
    """Finite diagnostic for the all-matrix parity proof in the note."""
    mp.mp.dps = 60
    z = mp.mpc(mp.mpf("0.5"), mp.mpf("0.5"))
    tau = 1j * mp.ellipk(1 - z) / mp.ellipk(z)
    y = tau.imag
    records = []
    for a in range(-entry_bound, entry_bound + 1):
        for b in range(-entry_bound, entry_bound + 1):
            for c in range(-entry_bound, entry_bound + 1):
                if a % 2 != 1 or b % 2 or c % 2:
                    continue
                # ad-bc=1 determines d if a divides 1+bc.
                numerator = 1 + b * c
                if numerator % a:
                    continue
                d = numerator // a
                if abs(d) > entry_bound or d % 2 != 1:
                    continue
                value = (
                    abs(a * tau + b) ** 2 + abs(c * tau + d) ** 2
                ) / (2 * y)
                records.append((value, a, b, c, d))
    records.sort(key=lambda item: item[0])
    identity_value = 1 / y
    minimum = records[0]
    return {
        "entry_bound": entry_bound,
        "matrices_checked": len(records),
        "minimum_cosh_distance": mp.nstr(minimum[0], 50),
        "one_minimizing_matrix": list(minimum[1:]),
        "identity_cosh_distance": mp.nstr(identity_value, 50),
        "minimum_matches_identity_to_50_digits": bool(
            abs(minimum[0] - identity_value) < mp.mpf("1e-50")
        ),
        "warning": "Finite diagnostic only; the parity proof covers all Gamma(2).",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    observed_start = {
        relative: sha256_file(root / relative) for relative in FROZEN_HASHES
    }
    assert observed_start == FROZEN_HASHES, (observed_start, FROZEN_HASHES)

    exact = symbolic_series_interval(180)
    archived_comparison = compare_archived(root, exact)
    assert archived_comparison["all_exact_fields_agree"]
    theta = theta_inverse_diagnostic()
    assert theta["residual_less_than_1e-70"]
    gamma2 = finite_gamma2_diagnostic()
    assert gamma2["minimum_matches_identity_to_50_digits"]

    observed_end = {
        relative: sha256_file(root / relative) for relative in FROZEN_HASHES
    }
    frozen_unchanged = observed_start == observed_end == FROZEN_HASHES
    assert frozen_unchanged

    result = {
        "verdict": "accept",
        "frozen_hashes": FROZEN_HASHES,
        "observed_hashes_at_start": observed_start,
        "observed_hashes_at_end": observed_end,
        "frozen_files_unchanged": frozen_unchanged,
        "independent_exact_series_certificate": exact,
        "comparison_with_archived": archived_comparison,
        "inverse_lambda_theta_diagnostic": theta,
        "finite_Gamma2_diagnostic": gamma2,
        "warning": (
            "The exact series, y interval, and decimal square comparison are "
            "rigorous. Theta and finite Gamma(2) calculations are diagnostics; "
            "the companion audit note gives the all-matrix geometric proof."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
