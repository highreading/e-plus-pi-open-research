#!/usr/bin/env python3
"""Exact arithmetic audit for the constrained raw-arctangent family.

For degree n, the high Taylor equations and C(1)=4B(1) form an integer
matrix J_n with 2n+1 rows and 2n+2 columns in the coefficients of B,C.
This script checks the determinant identities used in
``sources/raw_arctan_endpoint_arithmetic.md`` and records scale-invariant
endpoint arithmetic.  All linear algebra is exact over Q.

The direct determinant checks are intentionally limited to modest n.  The
closed formula for v_2(Delta_B) is an all-n theorem; the finite endpoint
patterns printed by this program are *not* extrapolated.
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

sys.set_int_max_str_digits(0)


def valuation_int(value: int, prime: int) -> int | None:
    """Return v_prime(value), using None for zero."""
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def lcm_many(values: list[int]) -> int:
    """LCM with the one-element case that sympy.ilcm does not accept."""
    return reduce(math.lcm, values, 1)


def v2_factorial(k: int) -> int:
    return k - k.bit_count()


def cumulative_factorial_valuation(q: int) -> int:
    return sum(v2_factorial(j) for j in range(q))


def g_value(q: int) -> int:
    return q * (q - 1) // 2 + cumulative_factorial_valuation(q)


def bordered_value(q: int) -> int:
    h = q - 1
    parity_term = h if h % 2 == 0 else h + 1
    return (
        h * (h - 1) // 2
        + cumulative_factorial_valuation(h)
        + parity_term
    )


def delta_b_v2_formula(n: int) -> int:
    """The proved all-degree formula for v_2(Delta_B)."""
    if n == 0:
        return 0
    common = (
        sum(v2_factorial(k) for k in range(n + 1, 2 * n + 1))
        + cumulative_factorial_valuation(n)
    )
    if n % 2 == 0:
        r = n // 2
        return common + 3 * g_value(r) + bordered_value(r + 1)
    r = (n - 1) // 2
    return (
        common
        + 2 * g_value(r + 1)
        + g_value(r)
        + bordered_value(r + 1)
    )


def tau(r: int) -> int:
    if r <= 0 or r % 2 == 0:
        return 0
    return (-1) ** ((r - 1) // 2) * math.factorial(r - 1)


def atan_coefficient(r: int) -> sp.Rational:
    if r <= 0 or r % 2 == 0:
        return sp.Rational(0)
    return sp.Rational((-1) ** ((r - 1) // 2), r)


def jet_row(k: int, n: int) -> list[int]:
    """k! times the coefficient row for B exp(z)+C atan(z)."""
    m = n + 1
    row: list[int] = []
    for a in range(m):
        row.append(math.factorial(k) // math.factorial(k - a))
    for a in range(m):
        falling = math.factorial(k) // math.factorial(k - a)
        row.append(falling * tau(k - a))
    return row


def high_matrix(n: int) -> sp.Matrix:
    m = n + 1
    rows = [jet_row(k, n) for k in range(n + 1, 3 * n + 1)]
    rows.append([-4] * m + [1] * m)
    return sp.Matrix(rows)


def primitive_polynomial_solution(n: int) -> list[int]:
    """Return primitive integral coefficients A|B|C, with fixed sign."""
    m = n + 1
    basis = high_matrix(n).nullspace()
    if len(basis) != 1:
        raise RuntimeError(f"n={n}: expected nullity one, got {len(basis)}")
    vector = basis[0]
    denominator = lcm_many([int(entry.q) for entry in vector])
    bc = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in bc if x))
    bc = [x // common for x in bc]

    a_coefficients: list[sp.Rational] = []
    for k in range(m):
        value = sp.Rational(0)
        for j in range(k + 1):
            value += bc[j] * sp.Rational(1, math.factorial(k - j))
            value += bc[m + j] * atan_coefficient(k - j)
        a_coefficients.append(-value)

    clear = lcm_many([int(entry.q) for entry in a_coefficients])
    full = [int(entry * clear) for entry in a_coefficients] + [clear * x for x in bc]
    common = reduce(gcd, (abs(x) for x in full if x))
    full = [x // common for x in full]
    first = next(x for x in full if x)
    return full if first > 0 else [-x for x in full]


def endpoint_a_row(n: int) -> list[int]:
    """The integral row n! A(1), as a functional of B,C."""
    m = n + 1
    nf = math.factorial(n)
    row: list[int] = []
    for j in range(m):
        value = -nf * sum(
            (sp.Rational(1, math.factorial(r)) for r in range(n - j + 1)),
            sp.Rational(0),
        )
        if value.q != 1:
            raise RuntimeError("exponential endpoint row did not clear")
        row.append(int(value))
    for j in range(m):
        value = -nf * sum(
            (atan_coefficient(r) for r in range(n - j + 1)),
            sp.Rational(0),
        )
        if value.q != 1:
            raise RuntimeError("arctangent endpoint row did not clear")
        row.append(int(value))
    return row


def rational_sha256(value: sp.Rational) -> str:
    payload = f"{int(value.p)}/{int(value.q)}".encode()
    return hashlib.sha256(payload).hexdigest()


def vector_sha256(values: list[int]) -> str:
    payload = json.dumps(values, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def finite_record(n: int, determinant_check_through: int) -> dict:
    m = n + 1
    coefficients = primitive_polynomial_solution(n)
    a_coefficients = coefficients[:m]
    b_coefficients = coefficients[m : 2 * m]
    c_coefficients = coefficients[2 * m :]
    endpoint_a = sum(a_coefficients)
    endpoint_b = sum(b_coefficients)
    endpoint_c = sum(c_coefficients)
    if endpoint_c != 4 * endpoint_b or endpoint_b == 0:
        raise RuntimeError(f"n={n}: endpoint constraint/nonvanishing failed")
    endpoint_gcd = gcd(abs(endpoint_a), abs(endpoint_b))
    primitive_a = endpoint_a // endpoint_gcd
    primitive_b = endpoint_b // endpoint_gcd

    M = 3 * n + 1
    first = sp.Rational(0)
    for j in range(m):
        first += b_coefficients[j] * sp.Rational(1, math.factorial(M - j))
        first += c_coefficients[j] * atan_coefficient(M - j)

    delta_b_formula = delta_b_v2_formula(n)
    result = {
        "n": n,
        "delta_B_v2_all_n_formula": delta_b_formula,
        "polynomial_vector_sha256": vector_sha256(coefficients),
        "polynomial_max_coefficient_decimal_digits": len(
            str(max(abs(x) for x in coefficients))
        ),
        "raw_endpoint_gcd_decimal_digits": len(str(endpoint_gcd)),
        "raw_endpoint_gcd_v2": valuation_int(endpoint_gcd, 2),
        "primitive_endpoint_A_decimal_digits": len(str(abs(primitive_a))),
        "primitive_endpoint_B_decimal_digits": len(str(abs(primitive_b))),
        "primitive_endpoint_A_v2": valuation_int(primitive_a, 2),
        "primitive_endpoint_B_v2": valuation_int(primitive_b, 2),
        "primitive_endpoint_B_v2_observed_pattern_value": (
            n + 2 * ((n + 2) // 4)
        ),
        "primitive_endpoint_B_matches_observed_pattern": (
            valuation_int(primitive_b, 2) == n + 2 * ((n + 2) // 4)
        ),
        "first_unconstrained_index": M,
        "first_unconstrained_coefficient_nonzero": first != 0,
        "first_unconstrained_coefficient_numerator_v2": valuation_int(int(first.p), 2),
        "first_unconstrained_coefficient_denominator_v2": valuation_int(int(first.q), 2),
        "first_unconstrained_coefficient_sha256": rational_sha256(first),
    }

    if n <= determinant_check_through:
        J = high_matrix(n)
        u_b = [1] * m + [0] * m
        u_a = endpoint_a_row(n)
        u_M = jet_row(M, n)
        delta_b = int(J.col_join(sp.Matrix([u_b])).det())
        delta_a = int(J.col_join(sp.Matrix([u_a])).det())
        delta_M = int(J.col_join(sp.Matrix([u_M])).det())
        if valuation_int(delta_b, 2) != delta_b_formula:
            raise RuntimeError(f"n={n}: Delta_B valuation formula mismatch")
        if sp.Rational(delta_a, math.factorial(n) * delta_b) != sp.Rational(
            endpoint_a, endpoint_b
        ):
            raise RuntimeError(f"n={n}: endpoint cofactor identity mismatch")
        if sp.Rational(delta_M, math.factorial(M) * delta_b) != first / endpoint_b:
            raise RuntimeError(f"n={n}: first-coefficient cofactor identity mismatch")
        result["direct_determinant_crosscheck"] = {
            "delta_B_v2": valuation_int(delta_b, 2),
            "delta_A_v2": valuation_int(delta_a, 2),
            "delta_M_v2": valuation_int(delta_M, 2),
            "delta_B_sha256": hashlib.sha256(str(delta_b).encode()).hexdigest(),
            "delta_A_sha256": hashlib.sha256(str(delta_a).encode()).hexdigest(),
            "delta_M_sha256": hashlib.sha256(str(delta_M).encode()).hexdigest(),
            "endpoint_ratio_identity_verified": True,
            "first_coefficient_ratio_identity_verified": True,
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=30)
    parser.add_argument("--determinant-check-through", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_n < 0 or args.determinant_check_through < 0:
        raise ValueError("degree bounds must be nonnegative")

    records = [
        finite_record(n, args.determinant_check_through)
        for n in range(args.max_n + 1)
    ]
    result = {
        "construction": "constrained raw-arctangent endpoint family",
        "all_n_theorem": (
            "delta_B_v2_all_n_formula is proved in the accompanying source note"
        ),
        "finite_scope_warning": (
            "All primitive-endpoint and first-unconstrained-coefficient patterns "
            "in these records are exact only for 0<=n<=max_n and are not theorems "
            "beyond that range."
        ),
        "max_n": args.max_n,
        "determinant_check_through": args.determinant_check_through,
        "records": records,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
