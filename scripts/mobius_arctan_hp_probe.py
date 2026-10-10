#!/usr/bin/env python3
"""Exact endpoint-matched Hermite--Pade probe for an integral-jet pi pullback.

The auxiliary function is

    F(z) = 4*atan(z/(2-z)) = 4*integral_0^z dt/(t^2-2t+2),

so F(1)=pi and every derivative F^(k)(0) is an integer.  For each n this
script first solves the *integral* high-jet-plus-endpoint system for B,C,
then reconstructs A, clears the low coefficients by n!, and makes the full
polynomial triple primitive.  It separately removes gcd(A(1),B(1)) at the
endpoint, since that gcd need not divide the polynomial triple.

All linear algebra and all sign tests are exact.  Decimal-looking output is
limited to certified base-10 decades.  The finite calculation is diagnostic;
it is not an all-degree rank, nonvanishing, or asymptotic theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as FQ
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

sys.set_int_max_str_digits(0)


def falling(k: int, j: int) -> int:
    if j > k:
        return 0
    return math.factorial(k) // math.factorial(k - j)


def f_jet(k: int) -> int:
    """Return F^(k)(0), using the exact residue-class formula."""
    if k == 0:
        return 0
    q, r = divmod(k - 1, 4)
    if r == 0:
        value = sp.Rational(2 * math.factorial(4 * q), 4**q)
    elif r == 1:
        value = sp.Rational(2 * math.factorial(4 * q + 1), 4**q)
    elif r == 2:
        value = sp.Rational(math.factorial(4 * q + 2), 4**q)
    else:
        return 0
    assert value.q == 1
    return int(((-1) ** q) * value)


def high_matrix(n: int) -> sp.Matrix:
    """Integral equations on B,C: jets n+1..3n and C(1)=B(1)."""
    width = 2 * (n + 1)
    rows: list[list[int]] = []
    for k in range(n + 1, 3 * n + 1):
        row = [0] * width
        for j in range(n + 1):
            row[j] = falling(k, j)
            row[n + 1 + j] = falling(k, j) * f_jet(k - j)
        rows.append(row)
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return sp.Matrix(rows)


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def e_interval(last_index: int = 1200) -> tuple[FQ, FQ]:
    partial = sum((FQ(1, math.factorial(k)) for k in range(last_index + 1)), FQ())
    return partial, partial + FQ(1, last_index * math.factorial(last_index))


def atan_interval(inv: int, last_index: int) -> tuple[FQ, FQ]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * FQ(1, (2 * k + 1) * inv ** (2 * k + 1))
            for k in range(last_index + 1)
        ),
        FQ(),
    )
    omitted = FQ(1, (2 * last_index + 3) * inv ** (2 * last_index + 3))
    return (partial, partial + omitted) if last_index & 1 else (partial - omitted, partial)


def e_plus_pi_interval() -> tuple[FQ, FQ]:
    e_lo, e_hi = e_interval()
    a_lo, a_hi = atan_interval(5, 1700)
    b_lo, b_hi = atan_interval(239, 400)
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    return e_lo + 16 * a_lo - 4 * b_hi, e_hi + 16 * a_hi - 4 * b_lo


def pow10(k: int) -> FQ:
    return FQ(10**k) if k >= 0 else FQ(1, 10 ** (-k))


def floor_log10_positive(x: FQ) -> int:
    assert x > 0
    k = len(str(x.numerator)) - len(str(x.denominator))
    while x < pow10(k):
        k -= 1
    while x >= pow10(k + 1):
        k += 1
    return k


def signed_interval_record(a: int, b: int, s_lo: FQ, s_hi: FQ) -> dict:
    endpoints = sorted((FQ(a) + b * s_lo, FQ(a) + b * s_hi))
    lo, hi = endpoints
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
            "lower_fraction_sha256": hashlib.sha256(
                f"{lo.numerator}/{lo.denominator}".encode()
            ).hexdigest(),
            "upper_fraction_sha256": hashlib.sha256(
                f"{hi.numerator}/{hi.denominator}".encode()
            ).hexdigest(),
        }
    lower_decade = floor_log10_positive(abs_lo)
    upper_decade = floor_log10_positive(abs_hi)
    return {
        "certified_sign": sign,
        "interval_contains_zero": False,
        "floor_log10_abs_lower": lower_decade,
        "floor_log10_abs_upper": upper_decade,
        "single_certified_base10_decade": lower_decade if lower_decade == upper_decade else None,
        "lower_fraction_sha256": hashlib.sha256(
            f"{lo.numerator}/{lo.denominator}".encode()
        ).hexdigest(),
        "upper_fraction_sha256": hashlib.sha256(
            f"{hi.numerator}/{hi.denominator}".encode()
        ).hexdigest(),
    }


def reconstruct_triple(n: int, bc: list[int]) -> tuple[list[int], int, int]:
    b = bc[: n + 1]
    c = bc[n + 1 :]
    a_rational: list[sp.Rational] = []
    for k in range(n + 1):
        jet = 0
        for j in range(min(k, n) + 1):
            jet += falling(k, j) * b[j]
            jet += falling(k, j) * f_jet(k - j) * c[j]
        a_rational.append(sp.Rational(-jet, math.factorial(k)))
    low_clear = math.factorial(n)
    preprimitive = (
        [int(low_clear * x) for x in a_rational]
        + [low_clear * x for x in b]
        + [low_clear * x for x in c]
    )
    common = reduce(gcd, (abs(x) for x in preprimitive if x))
    primitive = [x // common for x in preprimitive]
    first = next(x for x in primitive if x)
    if first < 0:
        primitive = [-x for x in primitive]
    return primitive, low_clear, common


def first_free_coefficient(n: int, triple: list[int]) -> sp.Rational:
    a = triple[: n + 1]
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    value = sp.Rational(0)
    for j in range(n + 1):
        if k >= j:
            value += sp.Rational(b[j], math.factorial(k - j))
            value += sp.Rational(c[j] * f_jet(k - j), math.factorial(k - j))
    # A has degree n and contributes nothing here.
    return value


def cofactor_content(matrix: sp.Matrix, primitive_kernel: list[int]) -> tuple[int, int]:
    """Return gcd of signed maximal cofactors, and the sampled column."""
    # For a full-row-rank r by r+1 matrix, its signed cofactor vector is an
    # integer multiple of the primitive kernel vector.  One determinant gives
    # the multiplier, which is the common gcd of all signed cofactors.
    for j, coordinate in enumerate(primitive_kernel):
        if coordinate:
            minor = matrix[:, :j].row_join(matrix[:, j + 1 :])
            determinant = int(DomainMatrix.from_Matrix(minor).det())
            signed = determinant if j % 2 == 0 else -determinant
            assert signed % coordinate == 0
            content = abs(signed // coordinate)
            assert content > 0
            return content, j
    raise RuntimeError("zero kernel vector")


def valuation(value: int, prime: int) -> int:
    assert value
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def binary_digit_sum(value: int) -> int:
    return value.bit_count()


def odd_part_factorial(value: int) -> int:
    answer = math.factorial(value)
    return answer >> valuation(answer, 2) if answer else 1


def forced_jet_cofactor_divisor(n: int) -> int:
    """The proved Gamma_n factor coming from the retained high C columns."""
    answer = 1
    # The n-1 smallest C-column divisors correspond to j=2,...,n, or
    # t=n-j=0,...,n-2.
    for t in range(0, n - 1):
        q = (t + 1) // 4
        dyadic_exponent = 2 * q + 1 - binary_digit_sum(q)
        answer *= (2**dyadic_exponent) * odd_part_factorial(t)
    return answer


def forced_factorial_cofactor_divisor(n: int) -> int:
    """The proved Lambda_n factor coming from all retained high columns."""
    return math.prod(math.factorial(j) for j in range(n)) ** 2


def forced_residual_row_cofactor_divisor(n: int) -> int:
    """The proved Omega*_n factor remaining after all column extractions."""
    answer = 1
    for s in range(1, n):
        d = (s - 1) // 4
        dyadic_exponent = 2 * d - binary_digit_sum(d)
        answer *= (2**dyadic_exponent) * odd_part_factorial(s - 1)
    return answer


def forced_cofactor_divisor(n: int) -> int:
    """The proved product Lambda_n*Gamma_n*Omega*_n for every cofactor."""
    return (
        forced_factorial_cofactor_divisor(n)
        * forced_jet_cofactor_divisor(n)
        * forced_residual_row_cofactor_divisor(n)
    )


def record(n: int, s_lo: FQ, s_hi: FQ) -> dict:
    matrix = high_matrix(n)
    domain_matrix = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain_matrix.rank()
    nullspace = domain_matrix.nullspace()
    nullity = nullspace.shape[0]
    if nullity != 1:
        return {
            "n": n,
            "high_matrix_shape": list(matrix.shape),
            "high_matrix_rank": rank,
            "high_matrix_nullity": nullity,
            "warning": "No unique projective high-jet solution; triple not recorded.",
        }
    bc = primitive_integer_vector(nullspace.to_Matrix().row(0).T)
    content, sampled_column = cofactor_content(matrix, bc)
    forced_factorial_content = forced_factorial_cofactor_divisor(n)
    forced_jet_content = forced_jet_cofactor_divisor(n)
    forced_residual_row_content = forced_residual_row_cofactor_divisor(n)
    forced_content = forced_cofactor_divisor(n)
    assert content % forced_content == 0
    remaining_content = content // forced_content
    remaining_factorization = {
        str(prime): exponent
        for prime, exponent in sorted(sp.factorint(remaining_content).items())
    }
    triple, low_clear, full_common = reconstruct_triple(n, bc)
    a = triple[: n + 1]
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    assert sum(c) == sum(b)
    endpoint_a = sum(a)
    endpoint_b = sum(b)
    endpoint_pair_gcd = gcd(abs(endpoint_a), abs(endpoint_b))
    if endpoint_pair_gcd:
        reduced_a = endpoint_a // endpoint_pair_gcd
        reduced_b = endpoint_b // endpoint_pair_gcd
    else:
        reduced_a = reduced_b = 0
    free = first_free_coefficient(n, triple)
    return {
        "n": n,
        "high_matrix_shape": list(matrix.shape),
        "high_matrix_rank": rank,
        "high_matrix_nullity": 1,
        "primitive_integral_high_kernel_BC": {
            "B": bc[: n + 1],
            "C": bc[n + 1 :],
        },
        "maximal_cofactor_common_content": content,
        "maximal_cofactor_common_content_decimal_digits": len(str(content)),
        "maximal_cofactor_common_content_v2": valuation(content, 2),
        "proved_forced_common_cofactor_divisor": forced_content,
        "proved_forced_common_cofactor_divisor_decimal_digits": len(str(forced_content)),
        "proved_forced_common_cofactor_divisor_v2": valuation(forced_content, 2),
        "proved_factorial_component_Lambda_n": forced_factorial_content,
        "proved_factorial_component_Lambda_n_decimal_digits": len(
            str(forced_factorial_content)
        ),
        "proved_factorial_component_Lambda_n_v2": valuation(
            forced_factorial_content, 2
        ),
        "proved_jet_component_Gamma_n": forced_jet_content,
        "proved_jet_component_Gamma_n_decimal_digits": len(str(forced_jet_content)),
        "proved_jet_component_Gamma_n_v2": valuation(forced_jet_content, 2),
        "proved_residual_row_component_Omega_star_n": forced_residual_row_content,
        "proved_residual_row_component_Omega_star_n_decimal_digits": len(
            str(forced_residual_row_content)
        ),
        "proved_residual_row_component_Omega_star_n_v2": valuation(
            forced_residual_row_content, 2
        ),
        "remaining_common_cofactor_content_after_forced_divisor_decimal_digits": len(
            str(remaining_content)
        ),
        "remaining_common_cofactor_content_after_forced_divisor": remaining_content,
        "remaining_common_cofactor_content_after_forced_divisor_v2": valuation(
            remaining_content, 2
        ),
        "remaining_common_cofactor_content_after_forced_divisor_prime_factorization": remaining_factorization,
        "cofactor_column_used_to_recover_content": sampled_column,
        "low_coefficient_universal_clear_factor_n_factorial": low_clear,
        "full_common_factor_removed_after_n_factorial_scaling": full_common,
        "primitive_polynomial_triple": {"A": a, "B": b, "C": c},
        "primitive_polynomial_max_coefficient_decimal_digits": len(
            str(max(map(abs, triple)))
        ),
        "primitive_polynomial_vector_sha256": hashlib.sha256(
            json.dumps(triple, separators=(",", ":")).encode()
        ).hexdigest(),
        "endpoint_from_primitive_polynomials": {
            "A": endpoint_a,
            "B": endpoint_b,
            "C": sum(c),
        },
        "endpoint_pair_gcd_removed": endpoint_pair_gcd,
        "primitive_endpoint_pair": {"A": reduced_a, "B": reduced_b},
        "endpoint_form": "A + B*(e+pi)",
        "endpoint_interval_certificate": signed_interval_record(
            reduced_a, reduced_b, s_lo, s_hi
        ),
        "first_unconstrained_taylor_coefficient": {
            "index": 3 * n + 1,
            "numerator": int(free.p),
            "denominator": int(free.q),
            "nonzero": bool(free),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    s_lo, s_hi = e_plus_pi_interval()
    result = {
        "construction": "endpoint-matched type-I Hermite--Pade for 1, exp(z), and 4*atan(z/(2-z))",
        "auxiliary_value": "F(1)=pi",
        "enforced_condition": "A+B*exp+C*F has zero jets 0..3n and C(1)=B(1)",
        "records": [record(n, s_lo, s_hi) for n in range(1, args.max_n + 1)],
        "warning": (
            "Finite exact diagnostics only. They prove no all-degree rank, "
            "endpoint nonvanishing, smallness, irrationality, or transcendence statement."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
