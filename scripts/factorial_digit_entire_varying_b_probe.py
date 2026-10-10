#!/usr/bin/env python3
"""Exact finite diagnostics for varying-b canonical factorial-digit rays.

The companion theorem note proves the identities used here.  This program
certifies the factorial digits of pi through a requested total degree,
constructs every admissible pair a+b<=N, and checks the exact decompositions

    W=a!*D,  Z=D*C_a+K,
    H=g*J,   g=gcd(D,K),
    J=gcd(a!, (D/g)*C_a+K/g).

It also checks the modular identities for D and K, exact denominator bounds,
and two finite square-root threshold tests.  Floating logarithmic rankings
are explicitly diagnostic; directed rational intervals certify the sign and
size records that are archived.
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


sys.set_int_max_str_digits(0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer_sha256(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def fraction_sha256(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def vector_sha256(values: list[int]) -> str:
    rendered = json.dumps(values, separators=(",", ":"))
    return hashlib.sha256(rendered.encode()).hexdigest()


def atan_interval(inv: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2*k+1)*inv**(2*k+1))
            for k in range(last_index+1)
        ),
        Fraction(),
    )
    omitted = Fraction(1, (2*last_index+3)*inv**(2*last_index+3))
    if last_index & 1:
        return partial, partial+omitted
    return partial-omitted, partial


def pi_interval(last5: int, last239: int) -> tuple[Fraction, Fraction]:
    a_lo, a_hi = atan_interval(5, last5)
    b_lo, b_hi = atan_interval(239, last239)
    return 16*a_lo-4*b_hi, 16*a_hi-4*b_lo


def e_interval(last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(k)) for k in range(last_index+1)),
        Fraction(),
    )
    return partial, partial+Fraction(1, last_index*math.factorial(last_index))


def decimal_fraction(value: Fraction, digits: int = 35) -> str:
    return mp.nstr(mp.mpf(value.numerator)/value.denominator, digits)


def floor_from_box(multiplier: int, box: tuple[Fraction, Fraction]) -> int:
    left = multiplier*box[0]
    right = multiplier*box[1]
    lower = left.numerator//left.denominator
    upper = right.numerator//right.denominator
    if lower != upper:
        raise AssertionError("rational interval does not certify factorial floor")
    return lower


def build_canonical_data(
    maximum: int, pi_box: tuple[Fraction, Fraction]
) -> tuple[list[int], list[int], list[int], list[int]]:
    factorials = [math.factorial(n) for n in range(maximum+1)]
    pi_floors = [floor_from_box(factorials[n], pi_box) for n in range(maximum+1)]
    e_floors = [
        sum(factorials[n]//factorials[k] for k in range(n+1))
        for n in range(maximum+1)
    ]
    combined = [x+y for x, y in zip(e_floors, pi_floors)]
    digits = [0, 0]
    for n in range(2, maximum+1):
        digit = pi_floors[n]-n*pi_floors[n-1]
        if not 0 <= digit <= n-1:
            raise AssertionError("invalid canonical factorial digit")
        digits.append(digit)
        if combined[n] != n*combined[n-1]+digit+1:
            raise AssertionError("combined-digit recurrence failed")
    return factorials, digits, combined, pi_floors


def derangements(maximum: int) -> list[int]:
    values = [1]
    if maximum:
        values.append(0)
    for n in range(2, maximum+1):
        values.append((n-1)*(values[n-1]+values[n-2]))
    return values


def push_top(heap: list, key: float, limit: int, record: dict) -> None:
    item = (key, record["a"], record["b"], record)
    if len(heap) < limit:
        heapq.heappush(heap, item)
    elif item[:3] > heap[0][:3]:
        heapq.heapreplace(heap, item)


def exact_delta_interval(
    w: int, z: int, s_box: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return w*s_box[0]-z, w*s_box[1]-z


def exact_delta_sign(
    w: int, z: int, s_box: tuple[Fraction, Fraction]
) -> int:
    """Certify a sign without constructing/reducing two large Fractions."""
    lower_numerator = w*s_box[0].numerator-z*s_box[0].denominator
    upper_numerator = w*s_box[1].numerator-z*s_box[1].denominator
    if lower_numerator > 0:
        return 1
    if upper_numerator < 0:
        return -1
    raise AssertionError("directed endpoint interval contains zero")


def interval_summary(lo: Fraction, hi: Fraction) -> dict:
    if lo > 0:
        sign = 1
        abs_lo, abs_hi = lo, hi
    elif hi < 0:
        sign = -1
        abs_lo, abs_hi = -hi, -lo
    else:
        raise AssertionError("selected interval contains zero")
    return {
        "certified_sign": sign,
        "absolute_lower_decimal": decimal_fraction(abs_lo),
        "absolute_upper_decimal": decimal_fraction(abs_hi),
        "absolute_lower_sha256": fraction_sha256(abs_lo),
        "absolute_upper_sha256": fraction_sha256(abs_hi),
    }


def compact_integer(value: int) -> dict:
    return {
        "decimal_digits": len(str(abs(value))),
        "sha256": integer_sha256(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=530)
    parser.add_argument("--atan5-last-index", type=int, default=950)
    parser.add_argument("--atan239-last-index", type=int, default=300)
    parser.add_argument("--e-last-index", type=int, default=650)
    parser.add_argument("--working-dps", type=int, default=1500)
    parser.add_argument("--ranking-size", type=int, default=20)
    parser.add_argument(
        "--source", type=Path,
        default=Path("sources/factorial_digit_entire_varying_b_regimes.md"),
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path("results/factorial_digit_entire_varying_b_total530.json"),
    )
    args = parser.parse_args()
    if args.max_total < 8:
        raise ValueError("max-total must be at least eight")
    mp.mp.dps = args.working_dps

    pi_box = pi_interval(args.atan5_last_index, args.atan239_last_index)
    e_box = e_interval(args.e_last_index)
    s_box = pi_box[0]+e_box[0], pi_box[1]+e_box[1]
    factorials, digits, combined, pi_floors = build_canonical_data(
        args.max_total, pi_box
    )
    combined_digits = [4, 1]+[digits[n]+1 for n in range(2, args.max_total+1)]
    subfactorial = derangements(args.max_total)

    # High-precision x_n values are used only to rank diagnostics.  Every
    # archived selected value is recertified with the rational box above.
    s_mid = (
        mp.mpf(s_box[0].numerator)/s_box[0].denominator
        + mp.mpf(s_box[1].numerator)/s_box[1].denominator
    )/2
    x_row = [mp.mpf(factorials[n])*s_mid-combined[n] for n in range(args.max_total+1)]
    x_lower_row = [
        factorials[n]*s_box[0].numerator-combined[n]*s_box[0].denominator
        for n in range(args.max_total+1)
    ]
    x_upper_row = [
        factorials[n]*s_box[1].numerator-combined[n]*s_box[1].denominator
        for n in range(args.max_total+1)
    ]
    w_row = factorials[:]
    z_row = combined[:]

    top_theta: list = []
    top_mu: list = []
    top_local_theta: list = []
    top_primitive_small: list = []
    exact_ratio_winner: tuple[int, int, dict] | None = None
    exact_sharp_ratio_winner: tuple[int, int, dict] | None = None
    square_threshold_count = 0
    sharp_square_threshold_count = 0
    nonzero_count = 0
    positive_count = 0
    negative_count = 0
    record_count = 0
    record_hasher = hashlib.sha256()
    selected_by_pair: dict[tuple[int, int], dict] = {}
    family_pairs: dict[str, set[tuple[int, int]]] = {
        "diagonal_b_eq_a": set(),
        "superdiagonal_b_eq_a_plus_1": set(),
        "subdiagonal_b_eq_a_minus_1": set(),
        "subdiagonal_b_eq_a_minus_5": set(),
        "half_ray_b_floor_a_over_2": set(),
        "sqrt_ray_b_floor_sqrt_a": set(),
        "log_ray_b_floor_log2_a": set(),
    }
    family_stats = {
        name: {
            "count": 0,
            "maximum_log_H_over_log_W": (-1.0, None),
            "maximum_log_g_over_log_W": (-1.0, None),
            "last_record": None,
        }
        for name in family_pairs
    }

    # First enumerate the desired deterministic families.
    for a in range(1, args.max_total+1):
        possible = {
            "diagonal_b_eq_a": a,
            "superdiagonal_b_eq_a_plus_1": a+1,
            "subdiagonal_b_eq_a_minus_1": a-1,
            "subdiagonal_b_eq_a_minus_5": a-5,
            "half_ray_b_floor_a_over_2": a//2,
            "sqrt_ray_b_floor_sqrt_a": math.isqrt(a),
            "log_ray_b_floor_log2_a": int(math.log2(a)),
        }
        for name, b in possible.items():
            if b >= 0 and a+b <= args.max_total and a >= max(1, b-1):
                family_pairs[name].add((a, b))

    for b in range(args.max_total+1):
        if b:
            w_row = [w_row[j+1]-w_row[j] for j in range(len(w_row)-1)]
            z_row = [z_row[j+1]-z_row[j] for j in range(len(z_row)-1)]
            x_row = [x_row[j+1]-x_row[j] for j in range(len(x_row)-1)]
            x_lower_row = [
                x_lower_row[j+1]-x_lower_row[j]
                for j in range(len(x_lower_row)-1)
            ]
            x_upper_row = [
                x_upper_row[j+1]-x_upper_row[j]
                for j in range(len(x_upper_row)-1)
            ]
        first_a = max(1, b-1)
        last_a = args.max_total-b
        if first_a > last_a:
            continue
        for a in range(first_a, last_a+1):
            w = w_row[a]
            z = z_row[a]
            if w <= 0 or w % factorials[a]:
                raise AssertionError("W=a!*D failed")
            d_value = w//factorials[a]
            k_value = z-d_value*combined[a]
            g_value = math.gcd(d_value, k_value)
            d_primitive = d_value//g_value
            k_primitive = k_value//g_value
            j_value = math.gcd(
                factorials[a], d_primitive*combined[a]+k_primitive
            )
            h_value = math.gcd(w, z)
            if h_value != g_value*j_value:
                raise AssertionError("H=g*J decomposition failed")

            if d_value % a != subfactorial[b] % a:
                raise AssertionError("D modulo a identity failed")
            k_mod = 0
            for j in range(1, b+1):
                k_mod = (
                    k_mod
                    + (math.comb(b, j) % a)
                    * (subfactorial[b-j] % a)
                    * combined_digits[a+j]
                ) % a
            if k_value % a != k_mod:
                raise AssertionError("K modulo a identity failed")

            if b:
                total_factorial_ratio = factorials[a+b]//factorials[a]
                n = a+b
                if not a*total_factorial_ratio <= n*d_value:
                    raise AssertionError("lower alternating D bound failed")
                if not d_value < total_factorial_ratio:
                    raise AssertionError("upper alternating D bound failed")
                # Exact two-term alternating-remainder upper bound.
                left = 2*n*(n-1)*d_value
                right = (2*a*(n-1)+b*(b-1))*total_factorial_ratio
                if left > right:
                    raise AssertionError("second-order D bound failed")

            if x_lower_row[a] > 0:
                sign = 1
                positive_count += 1
            elif x_upper_row[a] < 0:
                sign = -1
                negative_count += 1
            else:
                raise AssertionError(f"unresolved endpoint at {(a,b)}")
            nonzero_count += 1

            abs_delta = abs(x_row[a])
            if abs_delta == 0:
                raise AssertionError("working-precision endpoint rounded to zero")
            log_w = math.log(w)
            log_h = math.log(h_value) if h_value > 1 else 0.0
            log_g = math.log(g_value) if g_value > 1 else 0.0
            delta_as_float = float(abs_delta)
            log_delta = (
                math.log(delta_as_float)
                if delta_as_float > 0
                else float(mp.log(abs_delta))
            )
            theta = log_h/log_w if log_w else 0.0
            local_theta = log_g/log_w if log_w else 0.0
            reduced_denominator = w//h_value
            log_q = math.log(reduced_denominator) if reduced_denominator > 1 else 0.0
            mu = (
                (log_w-log_delta)/log_q
                if log_q else None
            )
            log_primitive_abs = log_delta-log_h
            primitive_abs = (
                math.exp(log_primitive_abs)
                if -740 < log_primitive_abs < 710
                else (0.0 if log_primitive_abs <= -740 else math.inf)
            )

            base_record = {
                "a": a,
                "b": b,
                "H": h_value,
                "g_local": g_value,
                "J_residual_factorial": j_value,
                "log_H_over_log_W_diagnostic": theta,
                "log_g_over_log_W_diagnostic": local_theta,
                "approximation_exponent_mu_diagnostic": mu,
                "primitive_abs_diagnostic": float(primitive_abs),
                "certified_sign": sign,
            }
            push_top(top_theta, theta, args.ranking_size, base_record)
            push_top(top_local_theta, local_theta, args.ranking_size, base_record)
            if mu is not None:
                push_top(top_mu, mu, args.ranking_size, base_record)
            push_top(
                top_primitive_small, -log_primitive_abs,
                args.ranking_size, base_record
            )

            crude_numerator = h_value*h_value
            crude_denominator = (2**(b+1))*w
            if crude_numerator > crude_denominator:
                square_threshold_count += 1
            if (
                exact_ratio_winner is None
                or crude_numerator*exact_ratio_winner[1]
                > exact_ratio_winner[0]*crude_denominator
            ):
                exact_ratio_winner = (
                    crude_numerator, crude_denominator, base_record
                )
            if b:
                n = a+b
                sharp_numerator = h_value*h_value*a*(n+1)
                sharp_denominator = (
                    w*(2**(b-1))*(n*(a+1)+1)
                )
                if sharp_numerator > sharp_denominator:
                    sharp_square_threshold_count += 1
                if (
                    exact_sharp_ratio_winner is None
                    or sharp_numerator*exact_sharp_ratio_winner[1]
                    > exact_sharp_ratio_winner[0]*sharp_denominator
                ):
                    exact_sharp_ratio_winner = (
                        sharp_numerator, sharp_denominator, base_record
                    )

            record_hasher.update(
                f"{a},{b},{w},{z},{d_value},{k_value},{g_value},{j_value},{h_value};".encode()
            )
            record_count += 1

            for name, pairs in family_pairs.items():
                if (a, b) not in pairs:
                    continue
                stats = family_stats[name]
                stats["count"] += 1
                stats["last_record"] = base_record
                if theta > stats["maximum_log_H_over_log_W"][0]:
                    stats["maximum_log_H_over_log_W"] = (theta, base_record)
                if local_theta > stats["maximum_log_g_over_log_W"][0]:
                    stats["maximum_log_g_over_log_W"] = (local_theta, base_record)

            if (a, b) in {
                (5, 1), (8, 2), (346, 3),
                (100, 100), (200, 200), (264, 265), (265, 265),
            }:
                selected_by_pair[(a, b)] = dict(
                    base_record, W=w, Z=z, D=d_value, K=k_value
                )

    if exact_ratio_winner is None or exact_sharp_ratio_winner is None:
        raise AssertionError("empty scan")

    def ranked(heap: list, reverse_key: bool = True) -> list[dict]:
        return [item[3] for item in sorted(heap, reverse=reverse_key)]

    top_sets = {
        "largest_log_H_over_log_W": ranked(top_theta),
        "largest_log_g_over_log_W": ranked(top_local_theta),
        "largest_approximation_exponent_mu": ranked(top_mu),
        "smallest_primitive_value_by_negative_log": ranked(top_primitive_small),
    }
    pairs_to_certify = set(selected_by_pair)
    for records in top_sets.values():
        pairs_to_certify.update((record["a"], record["b"]) for record in records)
    pairs_to_certify.add(
        (exact_ratio_winner[2]["a"], exact_ratio_winner[2]["b"])
    )
    pairs_to_certify.add(
        (
            exact_sharp_ratio_winner[2]["a"],
            exact_sharp_ratio_winner[2]["b"],
        )
    )

    # Reconstruct selected W,Z from fresh differences for compact exact records.
    selected_exact = []
    by_b: dict[int, set[int]] = {}
    for a, b in pairs_to_certify:
        by_b.setdefault(b, set()).add(a)
    current_w = factorials[:]
    current_z = combined[:]
    for b in range(max(by_b)+1):
        if b:
            current_w = [current_w[j+1]-current_w[j] for j in range(len(current_w)-1)]
            current_z = [current_z[j+1]-current_z[j] for j in range(len(current_z)-1)]
        for a in sorted(by_b.get(b, ())):
            w = current_w[a]
            z = current_z[a]
            d_value = w//factorials[a]
            k_value = z-d_value*combined[a]
            g_value = math.gcd(d_value, k_value)
            h_value = math.gcd(w, z)
            j_value = h_value//g_value
            lo, hi = exact_delta_interval(w, z, s_box)
            selected_exact.append(
                {
                    "a": a,
                    "b": b,
                    "W": compact_integer(w),
                    "Z": compact_integer(z),
                    "D": compact_integer(d_value),
                    "K": compact_integer(k_value),
                    "H": str(h_value),
                    "g_local": str(g_value),
                    "J_residual_factorial": str(j_value),
                    "absolute_Delta_b_x_interval": interval_summary(lo, hi),
                }
            )

    def ratio_record(item: tuple[int, int, dict]) -> dict:
        numerator, denominator, record = item
        ratio = Fraction(numerator, denominator)
        return {
            "a": record["a"],
            "b": record["b"],
            "ratio_decimal": decimal_fraction(ratio),
            "ratio_fraction_sha256": fraction_sha256(ratio),
            "strictly_below_one": ratio < 1,
        }

    rendered_family_stats = {}
    for name, stats in family_stats.items():
        rendered_family_stats[name] = {
            "count": stats["count"],
            "maximum_log_H_over_log_W_diagnostic": stats[
                "maximum_log_H_over_log_W"
            ][1],
            "maximum_log_g_over_log_W_diagnostic": stats[
                "maximum_log_g_over_log_W"
            ][1],
            "last_record": stats["last_record"],
        }

    source_path = args.source.resolve()
    script_path = Path(__file__).resolve()
    result = {
        "description": (
            "Exact finite varying-b scan for canonical factorial digits of pi; "
            "logarithmic rankings are diagnostics, not asymptotic theorems."
        ),
        "source_path": str(source_path),
        "source_sha256": sha256(source_path),
        "script_sha256": sha256(script_path),
        "parameters": {
            "max_total_a_plus_b": args.max_total,
            "atan5_last_index": args.atan5_last_index,
            "atan239_last_index": args.atan239_last_index,
            "e_last_index": args.e_last_index,
            "working_decimal_digits": args.working_dps,
            "number_of_admissible_records": record_count,
        },
        "canonical_digit_certificate": {
            "certified_through_index": args.max_total,
            "digit_vector_sha256": vector_sha256(digits),
            "pi_floor_vector_sha256": vector_sha256(pi_floors),
            "combined_C_vector_sha256": vector_sha256(combined),
            "all_digit_and_combined_recurrences_checked": True,
        },
        "all_degree_identity_checks_on_finite_box": {
            "W_equals_a_factorial_times_D": True,
            "Z_equals_D_times_C_a_plus_K": True,
            "H_equals_g_times_J": True,
            "D_mod_a_equals_subfactorial_b_mod_a": True,
            "K_mod_a_digit_identity": True,
            "alternating_D_bounds": True,
            "record_stream_sha256": record_hasher.hexdigest(),
        },
        "directed_interval_check": {
            "all_endpoints_exclude_zero": nonzero_count == record_count,
            "positive_count": positive_count,
            "negative_count": negative_count,
            "s_interval_width_sha256": fraction_sha256(s_box[1]-s_box[0]),
        },
        "exact_square_root_thresholds": {
            "count_H_squared_gt_2_power_b_plus_1_times_W": square_threshold_count,
            "maximum_H_squared_over_2_power_b_plus_1_W": ratio_record(
                exact_ratio_winner
            ),
            "count_H_squared_gt_sharper_range_bound_times_W_for_b_positive": (
                sharp_square_threshold_count
            ),
            "maximum_H_squared_over_sharper_range_bound_W": ratio_record(
                exact_sharp_ratio_winner
            ),
        },
        "diagnostic_rankings": top_sets,
        "deterministic_family_summaries": rendered_family_stats,
        "selected_exact_records": sorted(
            selected_exact, key=lambda record: (record["b"], record["a"])
        ),
        "warning": (
            "Finite nonvanishing, rankings, residue patterns, and observed gcd "
            "sizes imply no tail theorem.  In particular, no digit normality or "
            "equidistribution assumption is made."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
