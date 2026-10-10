#!/usr/bin/env python3
"""Exact certificate for Item 184's endpoint-height refinement."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path
from typing import Any


sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
RESULT_NAME = "item184_endpoint_height_certificate.json"
DEFAULT_OUTPUT = (
    HERE / RESULT_NAME
    if HERE.name.lower() != "scripts"
    else HERE.parent / "results" / RESULT_NAME
)
ITEM179_JSON = (
    HERE / "item179_independent_diagonal_certificate.json"
    if HERE.name.lower() != "scripts"
    else HERE.parent / "results" / "item179_independent_diagonal_certificate.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def content(values: list[int]) -> int:
    return reduce(gcd, (abs(value) for value in values if value), 0)


def old_phi(n: int) -> Fraction:
    q = 2 * n + 1
    return (n + 1) * (
        Fraction(q + 1, q * math.factorial(q))
        + Fraction(12, q * 2**n)
    )


def new_psi_sharp(n: int) -> Fraction:
    """Rational majorant: 16+12*sqrt(2) is replaced by 33."""
    q = 2 * n + 1
    return (
        Fraction((q + 1) ** 2, q * q * math.factorial(q))
        + Fraction(33, q * 2**n)
    )


def floor_log10(value: Fraction) -> int:
    if value <= 0:
        raise ValueError(value)
    guess = len(str(value.numerator)) - len(str(value.denominator))
    while value < (Fraction(10**guess) if guess >= 0 else Fraction(1, 10 ** (-guess))):
        guess -= 1
    while value >= (Fraction(10 ** (guess + 1)) if guess + 1 >= 0 else Fraction(1, 10 ** (-(guess + 1)))):
        guess += 1
    return guess


def row_certificate(record: dict[str, Any]) -> dict[str, Any]:
    n = int(record["n"])
    triple = [int(value) for value in record["triple"]]
    if len(triple) != 3 * n + 3:
        raise AssertionError((n, len(triple)))
    a_coeff = triple[: n + 1]
    b_coeff = triple[n + 1 : 2 * n + 2]
    c_coeff = triple[2 * n + 2 :]
    x_value, y_value, z_value = map(int, record["endpoint_A_B_C"])
    if sum(a_coeff) != x_value or sum(b_coeff) != y_value or sum(c_coeff) != z_value:
        raise AssertionError((n, "endpoint reconstruction"))
    if y_value != z_value:
        raise AssertionError((n, "endpoint mismatch"))
    full_content = content(triple)
    if full_content != 1:
        raise AssertionError((n, full_content))

    h_bc = max(abs(value) for value in b_coeff + c_coeff)
    h_end = max(abs(x_value), abs(y_value))
    endpoint_gcd = gcd(abs(x_value), abs(y_value))
    if n >= 2 and (not h_end or not endpoint_gcd):
        raise AssertionError((n, h_end, endpoint_gcd))

    # A deterministic rescaling verifies the general content/gcd identities.
    scale = n + 7
    scaled_triple = [scale * value for value in triple]
    scaled_content = content(scaled_triple)
    scaled_endpoint_gcd = gcd(abs(scale * x_value), abs(scale * y_value))
    if scaled_content != scale or scaled_endpoint_gcd != scale * endpoint_gcd:
        raise AssertionError((n, scaled_content, scaled_endpoint_gcd))
    if endpoint_gcd:
        if Fraction(scale * h_bc, scaled_endpoint_gcd) != Fraction(h_bc, endpoint_gcd):
            raise AssertionError((n, "effective height invariance"))
    if h_end:
        if Fraction(scale * h_bc, scale * h_end) != Fraction(h_bc, h_end):
            raise AssertionError((n, "projective amplification invariance"))

    phi = old_phi(n)
    psi = new_psi_sharp(n)
    if n >= 2 and not psi < phi:
        raise AssertionError((n, psi, phi))
    amplification = Fraction(h_bc, h_end) if h_end else None
    barrier_4n = bool(n >= 7 and amplification >= 4**n)
    if 7 <= n <= 30 and not barrier_4n:
        raise AssertionError((n, amplification, 4**n))
    relative_bound = amplification * psi if amplification is not None else None
    if 7 <= n <= 30 and not relative_bound > 1:
        raise AssertionError((n, relative_bound))

    return {
        "n": n,
        "full_content": full_content,
        "endpoint_gcd": str(endpoint_gcd),
        "H_BC": str(h_bc),
        "H_endpoint": str(h_end),
        "effective_height_H_BC_over_d": f"{h_bc}/{endpoint_gcd}" if endpoint_gcd else None,
        "projective_amplification": f"{h_bc}/{h_end}" if h_end else None,
        "projective_amplification_floor_log10": floor_log10(amplification) if amplification else None,
        "deterministic_scale_test": scale,
        "scaled_content": scaled_content,
        "scaled_endpoint_gcd": str(scaled_endpoint_gcd),
        "normalization_invariants_verified": bool(endpoint_gcd and h_end),
        "old_Phi": f"{phi.numerator}/{phi.denominator}",
        "new_rational_Psi_sharp": f"{psi.numerator}/{psi.denominator}",
        "Psi_sharp_strictly_less_than_Phi": psi < phi,
        "amplification_at_least_4_to_n": barrier_4n,
        "new_relative_bound_floor_log10": floor_log10(relative_bound) if relative_bound else None,
        "new_relative_bound_gt_one": bool(relative_bound and relative_bound > 1),
    }


def certificate() -> dict[str, Any]:
    source = json.loads(ITEM179_JSON.read_text(encoding="utf-8"))
    records = source["exact_rational"]["endpoint_matched"]
    rows = [row_certificate(record) for record in records]
    nondegenerate = [row for row in rows if row["n"] >= 2]

    # Rigorous radical majorization: sqrt(2)<17/12 because 289>288.
    if not 17 * 17 > 2 * 12 * 12:
        raise AssertionError("radical bound")
    radical_constant_upper = 16 + 12 * Fraction(17, 12)
    if radical_constant_upper != 33:
        raise AssertionError(radical_constant_upper)

    stream = "".join(
        f"{row['n']},{row['H_BC']},{row['H_endpoint']},{row['endpoint_gcd']}\n"
        for row in rows
    ).encode("ascii")
    return {
        "item": 184,
        "source": {
            "archive_path": "results/item179_independent_diagonal_certificate.json",
            "sha256": sha256(ITEM179_JSON),
        },
        "proved_all_degree": {
            "reverse_polynomial_identity": "sum_j c_j*T_(m-j)(w)=w^(m-n)*integral_0^1 t^(m-n-1)*Cstar(wt)/(1-wt) dt",
            "new_bound": "|R_n(1)| <= H_BC*Psi_n, Psi_n=(q+1)^2/(q^2*q!)+(16+12sqrt(2))/(q*2^n), q=2n+1",
            "rational_majorant": "Psi_n < Psi_sharp_n=(q+1)^2/(q^2*q!)+33/(q*2^n)",
            "strict_improvement": "Psi_sharp_n<Phi_n for every n>=2",
            "normalization_theorem": "For any integral scaling, H_BC/d and H_BC/H_endpoint are unchanged after full-content and endpoint-gcd normalization.",
            "radical_check": "sqrt(2)<17/12, hence 16+12sqrt(2)<33",
        },
        "finite_exact_barrier": {
            "range": "7<=n<=30",
            "all_projective_amplifications_at_least_4_to_n": all(row["amplification_at_least_4_to_n"] for row in rows if 7 <= row["n"] <= 30),
            "all_new_coefficient_height_relative_bounds_gt_one": all(row["new_relative_bound_gt_one"] for row in rows if 7 <= row["n"] <= 30),
            "interpretation": "Even the improved coefficient-height triangle bound cannot certify relative shrinking in this exact range.",
        },
        "exact_range": "1<=n<=30 (n=1 is the degenerate zero endpoint pair)",
        "all_non_degenerate_Psi_sharp_improvements": all(row["Psi_sharp_strictly_less_than_Phi"] for row in nondegenerate),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "rows": rows,
        "classification": {
            "PROVED": [
                "reverse-polynomial tail identity and improved all-degree height bound",
                "normalization/content/gcd invariance theorem",
                "exact 4^n amplification barrier for 7<=n<=30",
            ],
            "EXPERIMENTAL": ["growth of projective amplification beyond n=30"],
            "OPEN": [
                "all-degree projective comparison between the singular-ray norm and endpoint height",
                "shrinking subsequence or all-large nondecay",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    result = certificate()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(arguments.output),
        "row_stream_sha256": result["row_stream_sha256"],
        "all_improvements": result["all_non_degenerate_Psi_sharp_improvements"],
        "finite_barrier": result["finite_exact_barrier"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
