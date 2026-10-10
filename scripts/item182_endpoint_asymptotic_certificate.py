#!/usr/bin/env python3
"""Exact extended diagnostics for the Item179 endpoint-matched family."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import item179_independent_diagonal_exact as exact

RESULT_NAME = "item182_endpoint_asymptotic_certificate.json"


def default_output_path() -> Path:
    return (HERE.parent / "results" / RESULT_NAME) if HERE.name.lower() == "scripts" else (HERE / RESULT_NAME)


def e_interval(last_index: int = 1000) -> tuple[Fraction, Fraction]:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(last_index + 1)), Fraction())
    return partial, partial + Fraction(1, last_index * math.factorial(last_index))


def atan_interval(inv: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        ((-1 if k & 1 else 1) * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1)) for k in range(last_index + 1)),
        Fraction(),
    )
    omitted = Fraction(1, (2 * last_index + 3) * inv ** (2 * last_index + 3))
    return (partial, partial + omitted) if last_index & 1 else (partial - omitted, partial)


def e_plus_pi_interval() -> tuple[Fraction, Fraction]:
    elo, ehi = e_interval()
    alo, ahi = atan_interval(5, 1500)
    blo, bhi = atan_interval(239, 300)
    return elo + 16 * alo - 4 * bhi, ehi + 16 * ahi - 4 * blo


def power10(k: int) -> Fraction:
    return Fraction(10**k) if k >= 0 else Fraction(1, 10 ** (-k))


def floor_log10(x: Fraction) -> int:
    assert x > 0
    k = len(str(x.numerator)) - len(str(x.denominator))
    while x < power10(k):
        k -= 1
    while x >= power10(k + 1):
        k += 1
    return k


def digits(x: int) -> int:
    return 1 if x == 0 else len(str(abs(x)))


def digest_ints(values: list[int]) -> str:
    return hashlib.sha256(json.dumps(values, separators=(",", ":")).encode("ascii")).hexdigest()


def endpoint_metrics(a: int, b: int, slo: Fraction, shi: Fraction) -> dict:
    ends = sorted((Fraction(a) + b * slo, Fraction(a) + b * shi))
    lo, hi = ends
    if lo > 0:
        sign, abslo, abshi = 1, lo, hi
    elif hi < 0:
        sign, abslo, abshi = -1, -hi, -lo
    elif lo == hi == 0:
        return {"degenerate_zero_pair": True, "interval_contains_zero": True, "certified_sign": 0}
    else:
        return {"degenerate_zero_pair": False, "interval_contains_zero": True, "certified_sign": None}
    height = max(abs(a), abs(b))
    return {
        "degenerate_zero_pair": False,
        "interval_contains_zero": False,
        "certified_sign": sign,
        "abs_value_gt_one": abslo > 1,
        "abs_value_floor_log10_lower": floor_log10(abslo),
        "abs_value_floor_log10_upper": floor_log10(abshi),
        "relative_to_endpoint_height_floor_log10_lower": floor_log10(abslo / height),
        "relative_to_endpoint_height_floor_log10_upper": floor_log10(abshi / height),
        "signed_lower_sha256": hashlib.sha256(f"{lo.numerator}/{lo.denominator}".encode("ascii")).hexdigest(),
        "signed_upper_sha256": hashlib.sha256(f"{hi.numerator}/{hi.denominator}".encode("ascii")).hexdigest(),
    }


def analytic_tail_factor(n: int) -> Fraction:
    """Uniform Phi_n with |R(1)| <= H_BC Phi_n for order 3n+1."""
    q = 2 * n + 1
    e_tail = Fraction(q + 1, q * math.factorial(q))
    f_tail = Fraction(12, q * 2**n)
    return (n + 1) * (e_tail + f_tail)


def one(n: int, slo: Fraction, shi: Fraction) -> dict:
    source = exact.one(n, False)
    triple = source["triple"]
    acoef = triple[: n + 1]
    bcoef = triple[n + 1 : 2 * n + 2]
    ccoef = triple[2 * n + 2 :]
    content = reduce(math.gcd, (abs(x) for x in triple))
    assert content == 1
    xa, yb, yc = source["endpoint_A_B_C"]
    assert yb == yc
    d = math.gcd(abs(xa), abs(yb))
    primitive_pair = [xa // d, yb // d] if d else [0, 0]
    hpoly = max(abs(x) for x in triple)
    hbc = max(abs(x) for x in bcoef + ccoef)
    hend_raw = max(abs(xa), abs(yb))
    hend_primitive = max(abs(x) for x in primitive_pair)
    phi = analytic_tail_factor(n)
    if d:
        absolute_bound = phi * hbc / d
        relative_bound = phi * hbc / hend_raw
        metrics = endpoint_metrics(primitive_pair[0], primitive_pair[1], slo, shi)
        assert not metrics["interval_contains_zero"]
        # The exact interval is also an independent check of the proved tail bound.
        ends = sorted((Fraction(primitive_pair[0]) + primitive_pair[1] * slo,
                       Fraction(primitive_pair[0]) + primitive_pair[1] * shi))
        actual_abs_upper = max(abs(ends[0]), abs(ends[1]))
        assert actual_abs_upper <= absolute_bound
        bound_record = {
            "absolute_upper_bound_floor_log10": floor_log10(absolute_bound),
            "absolute_upper_bound_lt_one": absolute_bound < 1,
            "relative_upper_bound_floor_log10": floor_log10(relative_bound),
            "relative_upper_bound_lt_one": relative_bound < 1,
        }
    else:
        metrics = endpoint_metrics(0, 0, slo, shi)
        bound_record = None
    return {
        "n": n,
        "zero_order": 3 * n + 1,
        "matrix_rank": source["rank"],
        "first_free_derivative_nonzero": source["first_free_derivative"] != 0,
        "first_free_derivative_sha256": hashlib.sha256(str(source["first_free_derivative"]).encode("ascii")).hexdigest(),
        "normalization": source["exact_normalization"],
        "A_reconstruction_lcm_denominator": source["A_reconstruction_lcm_denominator"],
        "full_triple_gcd_removed": source["full_triple_gcd_before_final_reduction"],
        "full_polynomial_content_after_normalization": content,
        "endpoint_pair_gcd": d,
        "endpoint_pair_gcd_digits": digits(d),
        "raw_endpoint_pair": [xa, yb],
        "primitive_endpoint_pair": primitive_pair,
        "primitive_endpoint_denominator": 1,
        "full_triple_sha256": digest_ints(triple),
        "primitive_BC_sha256": digest_ints(source["primitive_BC_before_A_reconstruction"]),
        "full_polynomial_height_digits": digits(hpoly),
        "BC_height_digits": digits(hbc),
        "raw_endpoint_height_digits": digits(hend_raw),
        "primitive_endpoint_height_digits": digits(hend_primitive),
        "BC_to_raw_endpoint_amplification_floor_log10": floor_log10(Fraction(hbc, hend_raw)) if hend_raw else None,
        "analytic_tail_factor_floor_log10": floor_log10(phi),
        "analytic_bound_after_endpoint_gcd": bound_record,
        "actual_primitive_value": metrics,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=45)
    ap.add_argument("--output", type=Path, default=default_output_path())
    args = ap.parse_args()
    slo, shi = e_plus_pi_interval()
    records = [one(n, slo, shi) for n in range(1, args.nmax + 1)]
    nondegenerate = records[1:]
    obj = {
        "item": 182,
        "status": "PROVED all-degree tail identity/bound (report); exact finite diagnostics; no all-degree nondecay theorem",
        "range": [1, args.nmax],
        "family": "endpoint-matched diagonal family A+B exp(z)+C F(z), degree <=n, zero order 3n+1",
        "tail_bound": "|R(1)| <= H_BC*(n+1)*((2n+2)/((2n+1)(2n+1)!)+12/((2n+1)2^n))",
        "all_exact_matrices_full_row_rank": all(r["matrix_rank"] == 2 * r["n"] + 1 for r in records),
        "all_zero_orders_exact_3n_plus_1": all(r["first_free_derivative_nonzero"] for r in records),
        "all_full_contents_one": all(r["full_polynomial_content_after_normalization"] == 1 for r in records),
        "all_n_2_through_nmax_values_exclude_zero": all(not r["actual_primitive_value"]["interval_contains_zero"] for r in nondegenerate),
        "all_n_2_through_nmax_abs_values_gt_one": all(r["actual_primitive_value"]["abs_value_gt_one"] for r in nondegenerate),
        "all_tail_bounds_verified_against_value_intervals": True,
        "value_decades_n_2_through_nmax": [r["actual_primitive_value"]["abs_value_floor_log10_lower"] for r in nondegenerate],
        "height_digits_n_2_through_nmax": [r["primitive_endpoint_height_digits"] for r in nondegenerate],
        "records": records,
        "runtime": {"python": sys.version, "exact_backend": "fractions.Fraction plus integer Gaussian elimination in sibling Item179 helper"},
        "open": [
            "No all-degree recurrence or sign theorem for the normalized endpoint value is proved.",
            "The analytic tail bound is scale-homogeneous and cannot by itself control the endpoint gcd.",
            "No all-degree lower bound for the primitive value, and hence no all-large nondecay theorem, is proved.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
