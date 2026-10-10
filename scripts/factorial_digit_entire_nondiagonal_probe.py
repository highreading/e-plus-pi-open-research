#!/usr/bin/env python3
"""Exact finite diagnostics for the factorial-digit entire pi pullback.

For the canonical factorial digits

    d_n = floor(n!*pi) - n*floor((n-1)!*pi),

put G(z)=3+sum_{n>=2} d_n*z^n/n!.  The companion theorem note proves
G(1)=pi without needing irrationality of pi in the digit definition, and
derives the fully reduced endpoint on every (a,b,0) ray:

    W = Delta^b(a!),  Z = Delta^b C_a,
    H = gcd(W,Z),      L = (W*(e+pi)-Z)/H,

where C_n=floor(n!*e)+floor(n!*pi).

This program certifies the required factorial floors using a rational
Machin interval, scans a finite (a,b) box, and uses directed rational
intervals for every endpoint.  The finite minima are diagnostics; the
formula above is proved separately for all admissible a,b.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from math import comb, gcd
from pathlib import Path

import mpmath as mp


sys.set_int_max_str_digits(0)


def fraction_sha256(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def integer_sha256(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode()
    ).hexdigest()


def atan_interval(inv: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1))
            for k in range(last_index + 1)
        ),
        Fraction(),
    )
    omitted = Fraction(
        1, (2 * last_index + 3) * inv ** (2 * last_index + 3)
    )
    if last_index & 1:
        return partial, partial + omitted
    return partial - omitted, partial


def pi_interval(
    atan5_last_index: int, atan239_last_index: int
) -> tuple[Fraction, Fraction]:
    a_lo, a_hi = atan_interval(5, atan5_last_index)
    b_lo, b_hi = atan_interval(239, atan239_last_index)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def e_interval(last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(k)) for k in range(last_index + 1)),
        Fraction(),
    )
    return partial, partial + Fraction(
        1, last_index * math.factorial(last_index)
    )


def pow10(exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(10**exponent)
    return Fraction(1, 10 ** (-exponent))


def floor_log10_positive(value: Fraction) -> int:
    assert value > 0
    exponent = len(str(value.numerator)) - len(str(value.denominator))
    while value < pow10(exponent):
        exponent -= 1
    while value >= pow10(exponent + 1):
        exponent += 1
    return exponent


def decimal_fraction(value: Fraction, digits: int = 45) -> str:
    mp.mp.dps = digits + 20
    return mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)


def signed_interval_summary(lo: Fraction, hi: Fraction) -> dict:
    assert lo <= hi
    if lo > 0:
        sign = 1
        abs_lo, abs_hi = lo, hi
    elif hi < 0:
        sign = -1
        abs_lo, abs_hi = -hi, -lo
    else:
        return {
            "certified_sign": 0 if lo == hi == 0 else None,
            "interval_contains_zero": True,
            "lower_fraction_sha256": fraction_sha256(lo),
            "upper_fraction_sha256": fraction_sha256(hi),
        }
    lower_decade = floor_log10_positive(abs_lo)
    upper_decade = floor_log10_positive(abs_hi)
    midpoint = (lo + hi) / 2
    return {
        "certified_sign": sign,
        "interval_contains_zero": False,
        "floor_log10_abs_lower": lower_decade,
        "floor_log10_abs_upper": upper_decade,
        "single_certified_base10_decade": (
            lower_decade if lower_decade == upper_decade else None
        ),
        "absolute_lower_fraction_sha256": fraction_sha256(abs_lo),
        "absolute_upper_fraction_sha256": fraction_sha256(abs_hi),
        "absolute_lower_decimal_diagnostic": decimal_fraction(abs_lo),
        "absolute_upper_decimal_diagnostic": decimal_fraction(abs_hi),
        "signed_midpoint_decimal_diagnostic": decimal_fraction(midpoint),
    }


def factorial_floors(
    maximum_index: int, pi_box: tuple[Fraction, Fraction]
) -> tuple[list[int], list[int], list[int], list[int]]:
    factorials = [math.factorial(n) for n in range(maximum_index + 1)]
    pi_floors: list[int] = []
    e_floors: list[int] = []
    combined: list[int] = []
    for n, factorial in enumerate(factorials):
        lower = (factorial * pi_box[0]).numerator // (
            factorial * pi_box[0]
        ).denominator
        upper = (factorial * pi_box[1]).numerator // (
            factorial * pi_box[1]
        ).denominator
        if lower != upper:
            raise RuntimeError(
                f"Machin interval does not certify floor({n}!*pi)"
            )
        pi_floors.append(lower)
        e_floor = sum(factorial // factorials[k] for k in range(n + 1))
        e_floors.append(e_floor)
        combined.append(lower + e_floor)
    digits = [0, 0]
    for n in range(2, maximum_index + 1):
        digit = pi_floors[n] - n * pi_floors[n - 1]
        assert 0 <= digit <= n - 1
        digits.append(digit)
    return factorials, pi_floors, e_floors, combined


def forward_difference(values: list[int], start: int, order: int) -> int:
    return sum(
        (-1) ** (order - r) * comb(order, r) * values[start + r]
        for r in range(order + 1)
    )


def integer_summary(value: int) -> dict:
    return {
        "value": value,
        "decimal_digits": len(str(abs(value))),
        "sha256": integer_sha256(value),
    }


def endpoint_record(
    a: int,
    b: int,
    factorials: list[int],
    combined: list[int],
    digits: list[int],
    s_box: tuple[Fraction, Fraction],
) -> tuple[dict, Fraction, Fraction, Fraction, Fraction]:
    w = forward_difference(factorials, a, b)
    z = forward_difference(combined, a, b)
    assert w > 0
    h = gcd(w, z)
    alpha = -z // h
    beta = w // h
    assert gcd(abs(alpha), beta) == 1

    delta_lo = w * s_box[0] - z
    delta_hi = w * s_box[1] - z
    assert delta_lo <= delta_hi
    value_lo = delta_lo / h
    value_hi = delta_hi / h
    if delta_lo <= 0 <= delta_hi:
        raise RuntimeError(f"unresolved Delta^b x at a={a}, b={b}")
    certified_sign = 1 if delta_lo > 0 else -1

    record = {
        "a": a,
        "b": b,
        "W": w,
        "Z": z,
        "H": h,
        "certified_sign": certified_sign,
        "D_a_b_equals_W_over_a_factorial": w // factorials[a],
        "reduced_endpoint_pair_alpha_beta": [alpha, beta],
        "combined_digit_block_c_equals_d_plus_1": [
            digits[a + r] + 1 for r in range(1, b + 1)
        ],
    }
    if value_lo > 0:
        abs_lo, abs_hi = value_lo, value_hi
    else:
        assert value_hi < 0
        abs_lo, abs_hi = -value_hi, -value_lo
    if delta_lo > 0:
        delta_abs_lo, delta_abs_hi = delta_lo, delta_hi
    else:
        assert delta_hi < 0
        delta_abs_lo, delta_abs_hi = -delta_hi, -delta_lo
    return record, abs_lo, abs_hi, delta_abs_lo, delta_abs_hi


def enriched_record(
    item: tuple[dict, Fraction, Fraction, Fraction, Fraction]
) -> dict:
    record, abs_lo, abs_hi, delta_abs_lo, delta_abs_hi = item
    result = dict(record)
    w = result.pop("W")
    z = result.pop("Z")
    h = result.pop("H")
    sign = result.pop("certified_sign")
    # Recover directed intervals from the already oriented absolute boxes.
    if sign > 0:
        value_lo, value_hi = abs_lo, abs_hi
        delta_lo, delta_hi = delta_abs_lo, delta_abs_hi
    else:
        value_lo, value_hi = -abs_hi, -abs_lo
        delta_lo, delta_hi = -delta_abs_hi, -delta_abs_lo
    result.update(
        {
            "W_Delta_b_factorial": integer_summary(w),
            "Z_Delta_b_combined_numerator": integer_summary(z),
            "H_gcd_W_Z": integer_summary(h),
            "absolute_Delta_b_x_interval": signed_interval_summary(
                delta_lo, delta_hi
            ),
            "primitive_endpoint_interval": signed_interval_summary(
                value_lo, value_hi
            ),
            "log_H_over_log_W_diagnostic": (
                math.log(h) / math.log(w) if h > 1 and w > 1 else 0.0
            ),
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-a", type=int, default=500)
    parser.add_argument("--max-b", type=int, default=30)
    parser.add_argument("--small-b-max", type=int, default=6)
    parser.add_argument("--atan5-last-index", type=int, default=950)
    parser.add_argument("--atan239-last-index", type=int, default=300)
    parser.add_argument("--e-last-index", type=int, default=650)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not (0 <= args.small_b_max <= args.max_b):
        raise ValueError("require 0 <= small-b-max <= max-b")

    maximum_index = args.max_a + args.max_b
    pi_box = pi_interval(args.atan5_last_index, args.atan239_last_index)
    e_box = e_interval(args.e_last_index)
    s_box = e_box[0] + pi_box[0], e_box[1] + pi_box[1]
    factorials, pi_floors, e_floors, combined = factorial_floors(
        maximum_index, pi_box
    )
    digits = [0, 0]
    for n in range(2, maximum_index + 1):
        digits.append(pi_floors[n] - n * pi_floors[n - 1])

    # Definition/telescoping checks require no irrationality assumption.
    for n in range(2, maximum_index + 1):
        assert 0 <= digits[n] <= n - 1
        assert pi_floors[n] == n * pi_floors[n - 1] + digits[n]
        assert combined[n] == n * combined[n - 1] + digits[n] + 1

    all_items: list[tuple[dict, Fraction, Fraction, Fraction, Fraction]] = []
    per_b: dict[int, list[tuple[dict, Fraction, Fraction, Fraction, Fraction]]] = {}
    record_hasher = hashlib.sha256()
    threshold_counts = {
        str(threshold): [0 for _ in range(args.max_b + 1)]
        for threshold in (Fraction(1), Fraction(1, 10**4), Fraction(1, 10**8), Fraction(1, 10**12))
    }
    for b in range(args.max_b + 1):
        items: list[tuple[dict, Fraction, Fraction, Fraction, Fraction]] = []
        first_a = max(1, b - 1)
        for a in range(first_a, args.max_a + 1):
            item = endpoint_record(
                a, b, factorials, combined, digits, s_box
            )
            record, abs_lo, abs_hi, _, _ = item
            items.append(item)
            all_items.append(item)
            w = record["W"]
            z = record["Z"]
            h = record["H"]
            record_hasher.update(f"{a},{b},{w},{z},{h};".encode())
            for threshold in threshold_counts:
                q = Fraction(threshold)
                if abs_hi < q:
                    threshold_counts[threshold][b] += 1
        per_b[b] = items

    def certified_minimum(
        items: list[tuple[dict, Fraction, Fraction, Fraction, Fraction]]
    ) -> dict:
        winner = min(items, key=lambda item: float(item[2]))
        competing_lower: Fraction | None = None
        for item in items:
            if item is winner:
                continue
            assert winner[2] < item[1]
            if competing_lower is None or item[1] < competing_lower:
                competing_lower = item[1]
        assert competing_lower is not None
        result = enriched_record(winner)
        result["unique_minimum_certified_by_disjoint_intervals"] = True
        result["winner_abs_upper_decimal_diagnostic"] = decimal_fraction(winner[2])
        result["smallest_competing_abs_lower_decimal_diagnostic"] = decimal_fraction(
            competing_lower
        )
        return result

    minima_by_b = [certified_minimum(per_b[b]) for b in range(args.max_b + 1)]
    global_minimum = certified_minimum(all_items)
    selected_parameters = [(8, 2), (151, 2), (346, 3), (457, 0)]
    selected_records = []
    for wanted_a, wanted_b in selected_parameters:
        match = next(
            item
            for item in per_b[wanted_b]
            if item[0]["a"] == wanted_a
        )
        selected_records.append(enriched_record(match))

    # Check the determinant polynomial recurrence D_{a,b} on the whole box.
    for a in range(1, args.max_a + 1):
        d_prev2 = 1
        if args.max_b == 0:
            continue
        d_prev1 = a
        assert forward_difference(factorials, a, 1) == factorials[a] * d_prev1
        for b in range(2, args.max_b + 1):
            value = (a + b - 1) * d_prev1 + (b - 1) * d_prev2
            assert forward_difference(factorials, a, b) == factorials[a] * value
            d_prev2, d_prev1 = d_prev1, value

    result = {
        "description": "Exact finite scan of canonical-factorial-digit entire-G (a,b,0) rays",
        "scan_box": {
            "a_maximum": args.max_a,
            "b_maximum": args.max_b,
            "small_fixed_b_reported_in_detail": [0, args.small_b_max],
            "admissible_a_minimum_for_b": "max(1,b-1)",
            "number_of_endpoint_records": len(all_items),
        },
        "rational_interval_parameters": {
            "atan_1_over_5_last_index": args.atan5_last_index,
            "atan_1_over_239_last_index": args.atan239_last_index,
            "e_taylor_last_index": args.e_last_index,
            "pi_interval_width_sha256": fraction_sha256(pi_box[1] - pi_box[0]),
            "e_plus_pi_interval_width_sha256": fraction_sha256(s_box[1] - s_box[0]),
        },
        "canonical_digit_certificate": {
            "definition": "d_n=floor(n!*pi)-n*floor((n-1)!*pi)",
            "certified_through_index": maximum_index,
            "all_digits_in_0_through_n_minus_1": True,
            "digit_vector_sha256": vector_sha256(digits),
            "pi_factorial_floor_vector_sha256": vector_sha256(pi_floors),
            "combined_C_vector_sha256": vector_sha256(combined),
            "digit_prefix_n_2_through_30": digits[2:31],
        },
        "all_endpoint_intervals_certified_nonzero": True,
        "all_D_recurrence_checks_passed": True,
        "small_fixed_b_minima": minima_by_b[: args.small_b_max + 1],
        "all_b_minimum_summaries": [
            {
                "a": item["a"],
                "b": item["b"],
                "H_gcd_W_Z": item["H_gcd_W_Z"],
                "absolute_Delta_b_x_interval": item["absolute_Delta_b_x_interval"],
                "primitive_endpoint_interval": item["primitive_endpoint_interval"],
                "unique_minimum_certified_by_disjoint_intervals": item[
                    "unique_minimum_certified_by_disjoint_intervals"
                ],
            }
            for item in minima_by_b
        ],
        "global_minimum_in_scan_box": global_minimum,
        "selected_endpoint_records": selected_records,
        "certified_counts_strictly_below_threshold_by_b": threshold_counts,
        "record_stream_a_b_W_Z_H_sha256": record_hasher.hexdigest(),
        "warning": (
            "The endpoint formula and uniform boundedness theorem are all-degree. "
            "The displayed minima, nonvanishing checks, and threshold counts are "
            "finite-box certificates only and imply no tail nonvanishing or decay."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
