#!/usr/bin/env python3
"""Certify a continued-fraction prefix for e + pi using exact rationals.

If two rational endpoints L < e+pi < U have the same continued-fraction
prefix, that prefix is certified.  Adjacent convergents bracketing [L,U] then
give a Farey lower bound for the denominator of any rational in the interval.

This proves only a finite rational-denominator exclusion, not irrationality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)


def e_interval(n: int) -> tuple[F, F]:
    partial = sum((F(1, math.factorial(k)) for k in range(n + 1)), F())
    return partial, partial + F(1, n * math.factorial(n))


def atan_interval(inv: int, last_index: int) -> tuple[F, F]:
    partial = sum(
        ((-1 if k & 1 else 1) * F(1, (2 * k + 1) * inv ** (2 * k + 1))
         for k in range(last_index + 1)),
        F(),
    )
    next_abs = F(1, (2 * last_index + 3) * inv ** (2 * last_index + 3))
    # The alternating-series remainder has the sign of the first omitted term.
    return (partial, partial + next_abs) if last_index & 1 else (partial - next_abs, partial)


def e_plus_pi_interval(n_e: int, n5: int, n239: int) -> tuple[F, F]:
    e_lo, e_hi = e_interval(n_e)
    a_lo, a_hi = atan_interval(5, n5)
    b_lo, b_hi = atan_interval(239, n239)
    # Machin's identity: pi = 16 atan(1/5) - 4 atan(1/239).
    return e_lo + 16 * a_lo - 4 * b_hi, e_hi + 16 * a_hi - 4 * b_lo


def common_cf_state(lo: F, hi: F, wanted: int) -> tuple[list[int], F, F, str]:
    digits: list[int] = []
    for _ in range(wanted):
        a = lo.numerator // lo.denominator
        b = hi.numerator // hi.denominator
        if a != b:
            return digits, lo, hi, "terminal_tail_floors_differ"
        if lo == a or hi == a:
            return digits, lo, hi, "rational_endpoint_terminated"
        digits.append(a)
        lo, hi = 1 / (hi - a), 1 / (lo - a)
    return digits, lo, hi, "requested_limit_reached"


def common_cf(lo: F, hi: F, wanted: int) -> list[int]:
    return common_cf_state(lo, hi, wanted)[0]


def convergents(digits: list[int]) -> list[tuple[int, int]]:
    p_prev2, p_prev1, q_prev2, q_prev1 = 0, 1, 1, 0
    result = []
    for a in digits:
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        result.append((p, q))
        p_prev2, p_prev1, q_prev2, q_prev1 = p_prev1, p, q_prev1, q
    return result


def sha_fraction(value: F) -> str:
    canonical = f"{value.numerator}/{value.denominator}".encode()
    return hashlib.sha256(canonical).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-e", type=int, default=700)
    parser.add_argument("--n5", type=int, default=1150)
    parser.add_argument("--n239", type=int, default=250)
    parser.add_argument("--digits", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    lo, hi = e_plus_pi_interval(args.n_e, args.n5, args.n239)
    assert lo < hi
    digits, tail_lo, tail_hi, stop_reason = common_cf_state(lo, hi, args.digits)
    conv = convergents(digits)
    if len(conv) < 2:
        raise RuntimeError("interval did not certify two continued-fraction digits")
    (p, q), (p_prev, q_prev) = conv[-1], conv[-2]
    bracket_lo, bracket_hi = sorted((F(p, q), F(p_prev, q_prev)))
    assert bracket_lo < lo < hi < bracket_hi
    determinant = abs(p * q_prev - p_prev * q)
    assert determinant == 1
    farey_denominator_lower_bound = q + q_prev

    # If the exact terminal tail interval contains its first integer c, then
    # [digits;c] is the rational of smallest denominator in the original open
    # interval. Indeed, any positive reduced tail u/v above c-1 has u >= c
    # and v >= 1, while the inverse continued-fraction map has reduced
    # denominator q*u+q_prev*v. Equality is attained at u/v=c.
    tail_floor_lo = tail_lo.numerator // tail_lo.denominator
    tail_floor_hi = tail_hi.numerator // tail_hi.denominator
    interior_tail_integer = tail_floor_lo + 1
    has_interior_integer_tail = (
        F(interior_tail_integer) > tail_lo and F(interior_tail_integer) < tail_hi
    )
    if has_interior_integer_tail:
        simple_p = interior_tail_integer * p + p_prev
        simple_q = interior_tail_integer * q + q_prev
        simple_fraction = F(simple_p, simple_q)
        assert lo < simple_fraction < hi
        denominator_lower_bound = simple_q
    else:
        simple_p = simple_q = None
        denominator_lower_bound = farey_denominator_lower_bound

    record = {
        "parameters": vars(args) | {"output": str(args.output) if args.output else None},
        "python": platform.python_version(),
        "certified_partial_quotient_count": len(digits),
        "common_prefix_stop_reason": stop_reason,
        "partial_quotient_prefix_40": digits[:40],
        "partial_quotients_sha256": hashlib.sha256(
            json.dumps(digits, separators=(",", ":")).encode()
        ).hexdigest(),
        "exact_interval": {
            "lower_sha256": sha_fraction(lo),
            "upper_sha256": sha_fraction(hi),
            "width_numerator_digits": len(str((hi - lo).numerator)),
            "width_denominator_digits": len(str((hi - lo).denominator)),
        },
        "last_two_convergents": [
            {"p": p_prev, "q": q_prev},
            {"p": p, "q": q},
        ],
        "cross_determinant_absolute_value": determinant,
        "farey_denominator_lower_bound": farey_denominator_lower_bound,
        "terminal_tail_interval": {
            "lower_floor": tail_floor_lo,
            "upper_floor": tail_floor_hi,
            "contains_first_interior_integer": has_interior_integer_tail,
            "first_interior_integer": interior_tail_integer if has_interior_integer_tail else None,
        },
        "smallest_denominator_rational_in_exact_open_interval": (
            {"p": simple_p, "q": simple_q} if has_interior_integer_tail else None
        ),
        "rational_denominator_lower_bound": denominator_lower_bound,
        "lower_bound_decimal_digits": len(str(denominator_lower_bound)),
        "claim": (
            "If e+pi is rational in lowest terms, its denominator is at least "
            "the displayed rational_denominator_lower_bound."
        ),
        "warning": "No finite continued-fraction prefix proves irrationality or transcendence.",
    }
    encoded = json.dumps(record, indent=2, sort_keys=True).encode()
    rendered = encoded.decode() + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
