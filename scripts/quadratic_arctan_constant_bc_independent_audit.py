#!/usr/bin/env python3
"""Finite exact checks for the constant-B,C quadratic pullback ray.

This script is supplemental evidence only.  The no-decay result is proved by
the arguments in the associated independent audit, not by the finite scan.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


sys.set_int_max_str_digits(0)


def lcm_upto(n: int) -> int:
    value = 1
    for k in range(1, n + 1):
        value = math.lcm(value, k)
    return value


def c_values(p: int, maximum_m: int) -> list[int]:
    if maximum_m < 0:
        return []
    result = [1]
    if maximum_m == 0:
        return result
    result.append(-p * p + 5 * p - 1)
    middle = p * p - 4 * p + 1
    for _m in range(2, maximum_m + 1):
        result.append(-middle * result[-1] - p * p * result[-2])
    return result


def pi_truncation(p: int, a: int) -> Fraction:
    maximum_m = (a - 1) // 2
    if maximum_m < 0:
        return Fraction(0)
    sequence = c_values(p, maximum_m)
    return sum(
        (
            Fraction(
                4 * (p - 1) * sequence[m],
                p ** (2 * m + 1) * (2 * m + 1),
            )
            for m in range(maximum_m + 1)
        ),
        Fraction(),
    )


def record(p: int, a: int) -> dict:
    exponential = sum((Fraction(1, math.factorial(k)) for k in range(a + 1)), Fraction())
    pi_part = pi_truncation(p, a)
    combined = exponential + pi_part
    q = exponential.denominator
    d = pi_part.denominator
    Q = combined.denominator
    joint = math.lcm(Q, d)
    assert joint % q == 0
    assert q <= Q * d
    if a >= 1:
        maximum_m = (a - 1) // 2
        displayed_common_denominator = p ** (2 * maximum_m + 1) * lcm_upto(2 * maximum_m + 1)
        assert displayed_common_denominator % d == 0
    else:
        displayed_common_denominator = 1
        assert d == 1
    return {
        "p": p,
        "a": a,
        "q_a": q,
        "D_p_a": d,
        "Q_p_a": Q,
        "lcm_Q_D_over_q": joint // q,
        "displayed_common_denominator_over_D": displayed_common_denominator // d,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--max-a", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = [record(p, a) for p in args.p for a in range(args.max_a + 1)]
    result = {
        "scope": "Finite exact denominator checks only; not the proof of the asymptotic theorem.",
        "p_values": args.p,
        "max_a": args.max_a,
        "record_count": len(records),
        "all_assertions_passed": True,
        "records": records,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
