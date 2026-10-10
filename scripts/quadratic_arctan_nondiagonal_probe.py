#!/usr/bin/env python3
"""Exact bounded non-diagonal scan for the quadratic arctan pullbacks.

For degree bounds (a,b,c), impose

    A+B exp(z)+C F_p(z) = O(z^M),  C(1)=B(1),
    M=a+b+c+1,

where F_p(z)=4*atan((p-1)z/(p-z^2)).  The equations are dimension balanced.
All linear algebra and endpoint sign/size certifications are exact.
The scan is finite and has no asymptotic implication.
"""

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

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from mobius_arctan_hp_probe import (
    e_plus_pi_interval,
    floor_log10_positive,
    signed_interval_record,
)
from quadratic_arctan_pullback_probe import derivative_jets

sys.set_int_max_str_digits(0)


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def f_coefficient(jets: list[Fraction], k: int) -> sp.Rational:
    value = jets[k]
    return sp.Rational(value.numerator, value.denominator * math.factorial(k))


def endpoint_abs_interval(
    alpha: int, beta: int, s_interval: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction] | None:
    lo, hi = sorted(
        (
            Fraction(alpha) + beta * s_interval[0],
            Fraction(alpha) + beta * s_interval[1],
        )
    )
    if lo > 0:
        return lo, hi
    if hi < 0:
        return -hi, -lo
    return None


def solve(
    p: int,
    a: int,
    b: int,
    c: int,
    s_interval: tuple[Fraction, Fraction],
) -> tuple[dict, Fraction | None]:
    order = a + b + c + 1
    jets = derivative_jets(p, order)
    rows: list[list[sp.Rational]] = []
    for k in range(a + 1, order):
        row: list[sp.Rational] = []
        for j in range(b + 1):
            row.append(
                sp.Rational(1, math.factorial(k - j)) if j <= k else sp.Rational(0)
            )
        for j in range(c + 1):
            row.append(f_coefficient(jets, k - j) if j <= k else sp.Rational(0))
        rows.append(row)
    rows.append([sp.Rational(-1)] * (b + 1) + [sp.Rational(1)] * (c + 1))
    matrix = sp.Matrix(rows)
    domain = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain.rank()
    nullspace = domain.nullspace()
    nullity = nullspace.shape[0]
    base = {
        "p": p,
        "a": a,
        "b": b,
        "c": c,
        "total_degree_budget": a + b + c,
        "zero_order": order,
        "high_endpoint_shape": list(matrix.shape),
        "rank": rank,
        "nullity": nullity,
    }
    if nullity != 1:
        return base, None

    bc = primitive_integer_vector(nullspace.to_Matrix().row(0).T)
    b_values = bc[: b + 1]
    c_values = bc[b + 1 :]
    a_values: list[sp.Rational] = []
    for k in range(a + 1):
        value = sp.Rational(0)
        for j in range(min(b, k) + 1):
            value += sp.Rational(b_values[j], math.factorial(k - j))
        for j in range(min(c, k) + 1):
            value += c_values[j] * f_coefficient(jets, k - j)
        a_values.append(-value)
    triple = primitive_integer_vector(
        sp.Matrix(a_values + list(map(sp.Rational, b_values)) + list(map(sp.Rational, c_values)))
    )
    a_int = triple[: a + 1]
    b_int = triple[a + 1 : a + b + 2]
    c_int = triple[a + b + 2 :]
    assert sum(b_int) == sum(c_int)
    raw_alpha = sum(a_int)
    raw_beta = sum(b_int)
    endpoint_gcd = gcd(abs(raw_alpha), abs(raw_beta))
    alpha = raw_alpha // endpoint_gcd if endpoint_gcd else 0
    beta = raw_beta // endpoint_gcd if endpoint_gcd else 0
    absolute = endpoint_abs_interval(alpha, beta, s_interval)

    first_free = sp.Rational(0)
    for j in range(b + 1):
        if j <= order:
            first_free += sp.Rational(b_int[j], math.factorial(order - j))
    for j in range(c + 1):
        if j <= order:
            first_free += c_int[j] * f_coefficient(jets, order - j)

    base.update(
        {
            "primitive_triple_height_digits": len(str(max(map(abs, triple)))),
            "primitive_triple_sha256": hashlib.sha256(
                json.dumps(triple, separators=(",", ":")).encode()
            ).hexdigest(),
            "raw_endpoint_pair": [raw_alpha, raw_beta],
            "endpoint_gcd": endpoint_gcd,
            "reduced_endpoint_pair": [alpha, beta],
            "endpoint_B_nonzero": beta != 0,
            "all_three_degree_bounds_attained": bool(
                a_int[-1] and b_int[-1] and c_int[-1]
            ),
            "endpoint_interval_certificate": signed_interval_record(
                alpha, beta, *s_interval
            ),
            "first_free": {
                "index": order,
                "numerator": int(first_free.p),
                "denominator": int(first_free.q),
                "nonzero": bool(first_free),
            },
        }
    )
    return base, absolute[1] if absolute is not None else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--max-total", type=int, default=15)
    parser.add_argument(
        "--fixed-bc-max-a",
        type=int,
        default=-1,
        help="if nonnegative, also continue the b=c=0 ray through this a",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_total < 0:
        raise ValueError("max-total must be nonnegative")
    s_interval = e_plus_pi_interval()
    records: list[dict] = []
    best: list[dict] = []
    best_exact_degree: list[dict] = []
    below_one: list[dict] = []
    for p in args.p:
        for total in range(args.max_total + 1):
            candidates: list[tuple[Fraction, tuple[int, int, int]]] = []
            exact_candidates: list[tuple[Fraction, tuple[int, int, int]]] = []
            for a in range(total + 1):
                for b in range(total - a + 1):
                    c = total - a - b
                    record, upper = solve(p, a, b, c, s_interval)
                    records.append(record)
                    if upper is not None and record.get("endpoint_B_nonzero"):
                        candidates.append((upper, (a, b, c)))
                        if record.get("all_three_degree_bounds_attained"):
                            exact_candidates.append((upper, (a, b, c)))
                        if upper < 1:
                            below_one.append(
                                {
                                    "p": p,
                                    "degrees": [a, b, c],
                                    "all_three_degree_bounds_attained": record.get(
                                        "all_three_degree_bounds_attained"
                                    ),
                                    "upper_fraction_sha256": hashlib.sha256(
                                        f"{upper.numerator}/{upper.denominator}".encode()
                                    ).hexdigest(),
                                    "floor_log10_abs_upper": floor_log10_positive(upper),
                                }
                            )
            if candidates:
                upper, degrees = min(candidates)
                best.append(
                    {
                        "p": p,
                        "total_degree_budget": total,
                        "degrees": list(degrees),
                        "floor_log10_abs_upper": floor_log10_positive(upper),
                        "upper_fraction_sha256": hashlib.sha256(
                            f"{upper.numerator}/{upper.denominator}".encode()
                        ).hexdigest(),
                    }
                )
            if exact_candidates:
                upper, degrees = min(exact_candidates)
                best_exact_degree.append(
                    {
                        "p": p,
                        "total_degree_budget": total,
                        "degrees": list(degrees),
                        "floor_log10_abs_upper": floor_log10_positive(upper),
                        "upper_fraction_sha256": hashlib.sha256(
                            f"{upper.numerator}/{upper.denominator}".encode()
                        ).hexdigest(),
                    }
                )
    result = {
        "family": "F_p(z)=4*atan((p-1)z/(p-z^2))",
        "scan": "all nonnegative (a,b,c) with a+b+c<=max_total",
        "max_total": args.max_total,
        "p_values": args.p,
        "record_count": len(records),
        "best_by_p_and_total": best,
        "best_with_all_three_degree_bounds_attained": best_exact_degree,
        "certified_endpoint_forms_below_one": below_one,
        "fixed_b_equals_c_equals_zero": [
            {
                "p": p,
                "a": a,
                "reduced_endpoint_pair": record.get("reduced_endpoint_pair"),
                "certified_sign": record.get(
                    "endpoint_interval_certificate", {}
                ).get("certified_sign"),
                "floor_log10_abs": record.get(
                    "endpoint_interval_certificate", {}
                ).get("single_certified_base10_decade"),
            }
            for p in args.p
            for a in range(args.fixed_bc_max_a + 1)
            for record, _upper in [solve(p, a, 0, 0, s_interval)]
        ],
        "fixed_b_equals_c_equals_zero_max_a": args.fixed_bc_max_a,
        "records": records,
        "warning": "Finite exact diagnostic only; no all-degree or asymptotic claim.",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
