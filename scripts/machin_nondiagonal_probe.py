#!/usr/bin/env python3
"""Bounded exact scan of dimension-balanced non-diagonal Machin systems.

For degree bounds (a,b,c), the vanishing order is set to
M=a+b+c+1, so the Taylor equations plus C(1)=B(1) leave expected nullity
one.  This is a finite diagnostic only; it proves no rank or asymptotic
statement outside the scanned box.
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

from mixed_hermite_pade_probe import f_coefficient, s_interval

sys.set_int_max_str_digits(0)


def lcm_many(values: list[int]) -> int:
    return reduce(math.lcm, values, 1)


def vector_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode()
    ).hexdigest()


def fraction_sha256(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def power_of_ten(k: int) -> Fraction:
    return Fraction(10**k) if k >= 0 else Fraction(1, 10 ** (-k))


def scientific(value: Fraction, digits: int = 10) -> dict:
    if value == 0:
        return {"zero": True, "fraction_sha256": fraction_sha256(value)}
    if value < 0:
        raise ValueError("scientific summary expects a nonnegative value")
    exponent = len(str(value.numerator)) - len(str(value.denominator))
    if value < power_of_ten(exponent):
        exponent -= 1
    scaled = value / power_of_ten(exponent)
    prefix_integer = (scaled.numerator * 10**digits) // scaled.denominator
    return {
        "base10_exponent": exponent,
        "mantissa_lower_prefix": (
            f"{prefix_integer // 10**digits}."
            f"{prefix_integer % 10**digits:0{digits}d}"
        ),
        "fraction_sha256": fraction_sha256(value),
    }


def primitive_solution(a: int, b: int, c: int) -> tuple[int, list[int] | None]:
    M = a + b + c + 1
    variables = a + b + c + 3
    rows: list[list[sp.Rational]] = []
    for k in range(M):
        row = [sp.Rational(0) for _ in range(variables)]
        if k <= a:
            row[k] = 1
        b_offset = a + 1
        for j in range(b + 1):
            if j <= k:
                row[b_offset + j] = sp.Rational(1, math.factorial(k - j))
        c_offset = b_offset + b + 1
        for j in range(c + 1):
            if j <= k:
                row[c_offset + j] = f_coefficient("machin", k - j)
        rows.append(row)

    endpoint = [sp.Rational(0) for _ in range(variables)]
    b_offset = a + 1
    for j in range(b + 1):
        endpoint[b_offset + j] = -1
    c_offset = b_offset + b + 1
    for j in range(c + 1):
        endpoint[c_offset + j] = 1
    rows.append(endpoint)

    basis = sp.Matrix(rows).nullspace()
    if len(basis) != 1:
        return len(basis), None
    vector = basis[0]
    denominator = lcm_many([int(entry.q) for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return 1, integers if first > 0 else [-x for x in integers]


def canonical_record(
    a: int,
    b: int,
    c: int,
    coefficients: list[int],
    s_lo: Fraction,
    s_hi: Fraction,
) -> tuple[dict, Fraction | None]:
    M = a + b + c + 1
    a_values = coefficients[: a + 1]
    b_offset = a + 1
    b_values = coefficients[b_offset : b_offset + b + 1]
    c_values = coefficients[b_offset + b + 1 :]
    raw_a = sum(a_values)
    raw_b = sum(b_values)
    raw_c = sum(c_values)
    base = {
        "a": a,
        "b": b,
        "c": c,
        "total_degree_budget": a + b + c,
        "M": M,
        "nullity": 1,
        "polynomial_vector_sha256": vector_sha256(coefficients),
        "primitive_polynomial_height_decimal_digits": len(
            str(max(map(abs, coefficients)))
        ),
        "endpoint_match_verified": raw_c == raw_b,
        "endpoint_B_nonzero": raw_b != 0,
    }
    if raw_c != raw_b:
        raise RuntimeError(f"endpoint mismatch at {(a, b, c)}")
    if raw_b == 0:
        return base, None

    endpoint_gcd = gcd(abs(raw_a), abs(raw_b))
    alpha = raw_a // endpoint_gcd
    beta = raw_b // endpoint_gcd
    H_B = Fraction(max(map(abs, b_values)), endpoint_gcd)
    H_C = Fraction(max(map(abs, c_values)), endpoint_gcd)
    K_E = M - b
    K_G = M - c
    o_G = K_G if K_G % 2 else K_G + 1
    exp_bound = H_B * (b + 1) * Fraction(
        K_E + 1, K_E * math.factorial(K_E)
    )
    machin_bound = H_C * (c + 1) * Fraction(16, o_G * 5**o_G)
    total_bound = exp_bound + machin_bound

    endpoint_interval = sorted(
        (Fraction(alpha) + beta * s_lo, Fraction(alpha) + beta * s_hi)
    )
    lo, hi = endpoint_interval
    if lo > 0:
        abs_lo, abs_hi = lo, hi
    elif hi < 0:
        abs_lo, abs_hi = -hi, -lo
    else:
        abs_lo = abs_hi = None
    if abs_hi is not None and abs_hi > total_bound:
        raise RuntimeError(f"tail bound failed at {(a, b, c)}")

    base.update(
        {
            "raw_endpoint_gcd_decimal_digits": len(str(endpoint_gcd)),
            "primitive_endpoint_A_decimal_digits": len(str(abs(alpha))),
            "primitive_endpoint_B_decimal_digits": len(str(abs(beta))),
            "K_E": K_E,
            "K_G": K_G,
            "o_K_G": o_G,
            "effective_B_height": scientific(H_B),
            "effective_C_height": scientific(H_C),
            "exponential_tail_upper_bound": scientific(exp_bound),
            "machin_tail_upper_bound": scientific(machin_bound),
            "total_tail_upper_bound": scientific(total_bound),
            "total_tail_bound_below_one": total_bound < 1,
            "endpoint_form_certified_nonzero": abs_lo is not None,
            "endpoint_form_absolute_lower": (
                scientific(abs_lo) if abs_lo is not None else None
            ),
            "endpoint_form_absolute_upper_sha256": (
                fraction_sha256(abs_hi) if abs_hi is not None else None
            ),
            "endpoint_form_absolute_below_one": (
                abs_hi < 1 if abs_hi is not None else None
            ),
        }
    )
    return base, total_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_total < 0:
        raise ValueError("max-total must be nonnegative")
    s_lo, s_hi = s_interval()

    records: list[dict] = []
    best: dict[int, tuple[Fraction, tuple[int, int, int]]] = {}
    best_interior: dict[int, tuple[Fraction, tuple[int, int, int]]] = {}
    for total in range(args.max_total + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                nullity, coefficients = primitive_solution(a, b, c)
                if coefficients is None:
                    records.append(
                        {
                            "a": a,
                            "b": b,
                            "c": c,
                            "total_degree_budget": total,
                            "M": total + 1,
                            "nullity": nullity,
                            "canonical_line": False,
                        }
                    )
                    continue
                record, bound = canonical_record(
                    a, b, c, coefficients, s_lo, s_hi
                )
                record["canonical_line"] = True
                records.append(record)
                if bound is not None and (
                    total not in best or bound < best[total][0]
                ):
                    best[total] = (bound, (a, b, c))
                if (
                    bound is not None
                    and a >= 1
                    and b >= 1
                    and c >= 1
                    and (
                        total not in best_interior
                        or bound < best_interior[total][0]
                    )
                ):
                    best_interior[total] = (bound, (a, b, c))

    summary = [
        {
            "total_degree_budget": total,
            "best_total_tail_bound_triple": list(triple),
            "best_total_tail_bound": scientific(bound),
        }
        for total, (bound, triple) in sorted(best.items())
    ]
    interior_summary = [
        {
            "total_degree_budget": total,
            "best_total_tail_bound_triple": list(triple),
            "best_total_tail_bound": scientific(bound),
        }
        for total, (bound, triple) in sorted(best_interior.items())
    ]
    result = {
        "scan": (
            "all nonnegative degree triples with a+b+c<=max_total and "
            "dimension-balanced M=a+b+c+1"
        ),
        "max_total": args.max_total,
        "triple_count": len(records),
        "finite_scope_warning": (
            "This bounded exact scan establishes no rank, slope, or asymptotic "
            "theorem outside the listed triples."
        ),
        "best_by_total_degree_budget": summary,
        "best_interior_triple_by_total_degree_budget": interior_summary,
        "records": records,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
