#!/usr/bin/env python3
"""Independent exact audit of the full polynomial-C factorial-digit HP box.

Let

    G(z) = 3 + sum_{n>=2} d_n z^n/n!,
    d_n = floor(n! pi) - n floor((n-1)! pi).

For every (a,b,c) with a+b+c <= T this program constructs, in ordinary
monomial coefficients, the integer jet matrix for

    A + B exp + C G = O(z^(a+b+c+1)),   B(1)=C(1).

It computes its exact rational kernel, reduces the endpoint pair, and checks
an independent block/tail formula.  Pi is enclosed with

    pi = 4 (atan(1/2) + atan(1/3)),

rather than by floating point.  Numerical decimal strings are diagnostics;
all ranks, identities, signs, and comparisons are exact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


sys.set_int_max_str_digits(0)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    return sha256_text(",".join(str(value) for value in values))


def matrix_sha256(matrix: sp.Matrix) -> str:
    payload = f"{matrix.rows}x{matrix.cols}:" + ",".join(
        str(int(value)) for value in matrix
    )
    return sha256_text(payload)


def fraction_sha256(value: Fraction) -> str:
    return sha256_text(f"{value.numerator}/{value.denominator}")


def atan_inverse_interval(
    inverse: int, last_index: int
) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if index & 1 else 1)
            * Fraction(
                1,
                (2 * index + 1) * inverse ** (2 * index + 1),
            )
            for index in range(last_index + 1)
        ),
        Fraction(),
    )
    first_omitted = Fraction(
        1,
        (2 * last_index + 3) * inverse ** (2 * last_index + 3),
    )
    if last_index & 1:
        return partial, partial + first_omitted
    return partial - first_omitted, partial


def pi_interval() -> tuple[Fraction, Fraction]:
    half = atan_inverse_interval(2, 256)
    third = atan_inverse_interval(3, 192)
    return (
        4 * (half[0] + third[0]),
        4 * (half[1] + third[1]),
    )


def e_interval(last_index: int = 256) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(index)) for index in range(last_index + 1)),
        Fraction(),
    )
    # A deliberately simple strict upper bound for the positive tail.
    return partial, partial + Fraction(
        1, last_index * math.factorial(last_index)
    )


def decimal_fraction(value: Fraction, digits: int = 35) -> str:
    mp.mp.dps = digits + 20
    return mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)


def factorial_fall(value: int, order: int) -> int:
    if order > value:
        return 0
    return math.factorial(value) // math.factorial(value - order)


def primitive_integer_kernel(matrix: sp.Matrix) -> list[int]:
    nullspace = matrix.nullspace()
    if len(nullspace) != 1:
        raise AssertionError(
            f"expected nullity one, obtained nullity {len(nullspace)}"
        )
    vector = nullspace[0]
    common_denominator = 1
    for entry in vector:
        common_denominator = math.lcm(
            common_denominator, int(entry.as_numer_denom()[1])
        )
    integers = [int(entry * common_denominator) for entry in vector]
    content = 0
    for entry in integers:
        content = math.gcd(content, abs(entry))
    integers = [entry // content for entry in integers]
    for entry in integers:
        if entry:
            if entry < 0:
                integers = [-value for value in integers]
            break
    if matrix * sp.Matrix(integers) != sp.zeros(matrix.rows, 1):
        raise AssertionError("primitive vector does not lie in the kernel")
    return integers


def canonical_endpoint_pair(alpha: int, beta: int) -> tuple[int, int] | None:
    if alpha == 0 and beta == 0:
        return None
    content = math.gcd(abs(alpha), abs(beta))
    alpha //= content
    beta //= content
    if beta < 0 or (beta == 0 and alpha < 0):
        alpha, beta = -alpha, -beta
    return alpha, beta


def exact_digit_data(
    maximum_index: int, pi_box: tuple[Fraction, Fraction]
) -> tuple[list[int], list[int], list[int]]:
    factorials = [math.factorial(index) for index in range(maximum_index + 1)]
    pi_floors: list[int] = []
    for index, factorial in enumerate(factorials):
        lower = factorial * pi_box[0]
        upper = factorial * pi_box[1]
        floor_lower = lower.numerator // lower.denominator
        floor_upper = upper.numerator // upper.denominator
        if floor_lower != floor_upper:
            raise AssertionError(f"pi interval does not certify floor({index}! pi)")
        pi_floors.append(floor_lower)

    g_jets = [3, 0]
    for index in range(2, maximum_index + 1):
        digit = pi_floors[index] - index * pi_floors[index - 1]
        if not 0 <= digit <= index - 1:
            raise AssertionError("invalid canonical factorial digit")
        g_jets.append(digit)

    combined_jets = [1 + value for value in g_jets]
    partial_integers: list[int] = []
    for index, factorial in enumerate(factorials):
        partial_integers.append(
            sum(
                factorial // factorials[j] * combined_jets[j]
                for j in range(index + 1)
            )
        )
    # For n>=1 this equals floor(n!e)+floor(n!pi).  At n=0 it is the
    # integral Taylor numerator 4, which is the quantity needed below.
    return g_jets, combined_jets, partial_integers


def full_matrix(
    a: int, b: int, c: int, g_jets: list[int]
) -> sp.Matrix:
    order = a + b + c + 1
    column_count = a + b + c + 3
    rows: list[list[int]] = []
    for k in range(order):
        row = [0] * column_count
        if k <= a:
            row[k] = math.factorial(k)
        b_offset = a + 1
        for j in range(min(b, k) + 1):
            row[b_offset + j] = factorial_fall(k, j)
        c_offset = b_offset + b + 1
        for j in range(min(c, k) + 1):
            row[c_offset + j] = factorial_fall(k, j) * g_jets[k - j]
        rows.append(row)

    endpoint = [0] * column_count
    b_offset = a + 1
    for j in range(b + 1):
        endpoint[b_offset + j] = 1
    c_offset = b_offset + b + 1
    for j in range(c + 1):
        endpoint[c_offset + j] = -1
    rows.append(endpoint)
    return sp.Matrix(rows)


def block_matrix_and_tail_row(
    a: int,
    b: int,
    c: int,
    g_jets: list[int],
    combined_jets: list[int],
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    rows: list[list[int]] = []
    y: list[int] = []
    for k in range(a + 1, a + b + c + 1):
        row: list[int] = []
        for j in range(b):
            falling = factorial_fall(k, j)
            row.append(falling * (k - j - 1))
        for j in range(c):
            falling = factorial_fall(k, j)
            if not falling:
                row.append(0)
                continue
            n = k - j
            q_n = -g_jets[0] if n == 0 else n * g_jets[n - 1] - g_jets[n]
            row.append(falling * q_n)
        rows.append(row)
        y.append(combined_jets[k])

    tail_row: list[int] = []
    for j in range(b):
        tail_row.append(factorial_fall(a, j))
    for j in range(c):
        if j > a:
            tail_row.append(0)
        else:
            tail_row.append(factorial_fall(a, j) * g_jets[a - j])
    return sp.Matrix(rows), sp.Matrix(y), sp.Matrix([tail_row])


def absolute_interval(
    alpha: int, beta: int, s_box: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction, int]:
    first = Fraction(alpha) + beta * s_box[0]
    second = Fraction(alpha) + beta * s_box[1]
    lower, upper = min(first, second), max(first, second)
    if lower <= 0 <= upper:
        raise AssertionError("endpoint interval does not determine a nonzero sign")
    if lower > 0:
        return lower, upper, 1
    return -upper, -lower, -1


def interval_json(
    lower: Fraction, upper: Fraction, sign: int
) -> dict[str, object]:
    return {
        "certified_sign": sign,
        "lower_sha256": fraction_sha256(lower),
        "upper_sha256": fraction_sha256(upper),
        "lower_decimal_diagnostic": decimal_fraction(lower),
        "upper_decimal_diagnostic": decimal_fraction(upper),
    }


def detailed_interval(lower: Fraction, upper: Fraction) -> dict[str, str]:
    return {
        "lower_numerator": str(lower.numerator),
        "lower_denominator": str(lower.denominator),
        "upper_numerator": str(upper.numerator),
        "upper_denominator": str(upper.denominator),
        "lower_decimal_diagnostic": decimal_fraction(lower, 50),
        "upper_decimal_diagnostic": decimal_fraction(upper, 50),
    }


def minimum_certificate(
    internal_records: list[dict[str, object]], predicate
) -> dict[str, object]:
    candidates = [record for record in internal_records if predicate(record)]
    winner = min(
        candidates,
        key=lambda record: (record["abs_lower"] + record["abs_upper"]) / 2,
    )
    others = [record for record in candidates if record is not winner]
    runner_up = min(others, key=lambda record: record["abs_lower"])
    if not winner["abs_upper"] < runner_up["abs_lower"]:
        raise AssertionError("intervals do not certify a unique minimum")
    return {
        "winner": list(winner["triple"]),
        "reduced_endpoint_pair": [str(value) for value in winner["pair"]],
        "absolute_interval": detailed_interval(
            winner["abs_lower"], winner["abs_upper"]
        ),
        "runner_up_by_exact_lower_bound": list(runner_up["triple"]),
        "strict_separation_certified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=18)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/independent_factorial_digit_full_polynomial_T18.json"
        ),
    )
    args = parser.parse_args()
    if args.max_total < 4:
        raise ValueError("max-total must be at least 4")

    pi_box = pi_interval()
    e_box = e_interval()
    s_box = (e_box[0] + pi_box[0], e_box[1] + pi_box[1])
    g_jets, combined_jets, partial_integers = exact_digit_data(
        args.max_total, pi_box
    )

    records: list[dict[str, object]] = []
    internal_nonzero: list[dict[str, object]] = []
    zero_endpoint_records: list[dict[str, object]] = []
    block_singular_triples: list[list[int]] = []
    schur_checks = 0

    for total in range(args.max_total + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                matrix = full_matrix(a, b, c, g_jets)
                kernel = primitive_integer_kernel(matrix)
                if matrix.cols != matrix.rows + 1:
                    raise AssertionError("matrix is not of bordered nullity-one size")

                b_offset = a + 1
                c_offset = b_offset + b + 1
                alpha_raw = sum(kernel[:b_offset])
                beta_raw = sum(kernel[b_offset:c_offset])
                gamma_raw = sum(kernel[c_offset:])
                if beta_raw != gamma_raw:
                    raise AssertionError("kernel violates endpoint equality")
                endpoint_pair = canonical_endpoint_pair(alpha_raw, beta_raw)

                block, y, tail_row = block_matrix_and_tail_row(
                    a, b, c, g_jets, combined_jets
                )
                block_det = int(block.det())
                if block_det == 0:
                    block_singular_triples.append([a, b, c])
                if (block_det == 0) != (beta_raw == 0):
                    raise AssertionError(
                        "block singularity is not equivalent to beta=0"
                    )

                record: dict[str, object] = {
                    "a": a,
                    "b": b,
                    "c": c,
                    "total": total,
                    "full_matrix_shape": [matrix.rows, matrix.cols],
                    "full_row_rank": True,
                    "nullity": 1,
                    "matrix_sha256": matrix_sha256(matrix),
                    "primitive_kernel_sha256": vector_sha256(kernel),
                    "raw_endpoint_pair": [str(alpha_raw), str(beta_raw)],
                    "endpoint_pair_is_zero": endpoint_pair is None,
                    "block_determinant": str(block_det),
                    "block_is_singular": block_det == 0,
                }

                if endpoint_pair is None:
                    zero_record = {
                        "triple": [a, b, c],
                        "primitive_A": [str(value) for value in kernel[:b_offset]],
                        "primitive_B": [
                            str(value) for value in kernel[b_offset:c_offset]
                        ],
                        "primitive_C": [str(value) for value in kernel[c_offset:]],
                    }
                    zero_endpoint_records.append(zero_record)
                    record["reduced_endpoint_pair"] = None
                    record["absolute_endpoint_interval"] = None
                else:
                    alpha, beta = endpoint_pair
                    record["reduced_endpoint_pair"] = [str(alpha), str(beta)]
                    abs_lower, abs_upper, sign = absolute_interval(
                        alpha, beta, s_box
                    )
                    record["absolute_endpoint_interval"] = interval_json(
                        abs_lower, abs_upper, sign
                    )
                    internal_nonzero.append(
                        {
                            "triple": (a, b, c),
                            "pair": endpoint_pair,
                            "abs_lower": abs_lower,
                            "abs_upper": abs_upper,
                        }
                    )

                if block_det != 0:
                    if b + c == 0:
                        correction = sp.Rational(0)
                    else:
                        solution_to_positive_y = block.inv() * y
                        correction = (tail_row * solution_to_positive_y)[0]
                    z_formula = sp.Rational(partial_integers[a] * block_det) + (
                        sp.Rational(block_det) * correction
                    )
                    if z_formula.q != 1:
                        raise AssertionError("adjugate endpoint numerator is not integral")
                    W = math.factorial(a) * block_det
                    Z = int(z_formula)
                    formula_pair = canonical_endpoint_pair(-Z, W)
                    if formula_pair != endpoint_pair:
                        raise AssertionError("block endpoint formula disagrees with kernel")
                    record["block_endpoint_formula_matches"] = True
                    record["block_W_sha256"] = sha256_text(str(W))
                    record["block_Z_sha256"] = sha256_text(str(Z))
                else:
                    record["block_endpoint_formula_matches"] = None

                # Stable-range Schur reduction: the first b rows of the U
                # block have determinant kappa_b D_{a,b}, and eliminating
                # them leaves a c-by-c exact digit-residual determinant.
                if b >= 1 and a >= max(1, b - 1):
                    U0 = block[:b, :b]
                    det_u0 = int(U0.det())
                    difference = sum(
                        (-1) ** (b - r)
                        * math.comb(b, r)
                        * math.factorial(a + r)
                        for r in range(b + 1)
                    )
                    D_ab = difference // math.factorial(a)
                    kappa = math.prod(math.factorial(j) for j in range(b))
                    if det_u0 != kappa * D_ab:
                        raise AssertionError("fixed-b U-block determinant mismatch")
                    if c:
                        V0 = block[:b, b:]
                        U1 = block[b:, :b]
                        V1 = block[b:, b:]
                        schur = V1 - U1 * U0.inv() * V0
                        if sp.Rational(det_u0) * schur.det() != block_det:
                            raise AssertionError("Schur determinant identity failed")
                    elif det_u0 != block_det:
                        raise AssertionError("c=0 determinant reduction failed")
                    record["stable_range_schur_reduction_matches"] = True
                    schur_checks += 1
                else:
                    record["stable_range_schur_reduction_matches"] = None

                records.append(record)

    expected_count = math.comb(args.max_total + 3, 3)
    if len(records) != expected_count:
        raise AssertionError("triple count mismatch")

    minima = {
        "all_nonzero_endpoints": minimum_certificate(
            internal_nonzero, lambda record: True
        ),
        "nonconstant_C_only": minimum_certificate(
            internal_nonzero, lambda record: record["triple"][2] > 0
        ),
    }

    result = {
        "description": (
            "Independent exact full-polynomial-C canonical-factorial-digit "
            "Hermite-Pade audit"
        ),
        "status": "exact finite certificate; not an all-degree rank theorem",
        "parameters": {
            "max_total": args.max_total,
            "triple_count": len(records),
            "vanishing_order": "a+b+c+1",
            "endpoint_constraint": "B(1)=C(1)",
            "coefficient_basis": "ordinary monomials",
        },
        "independent_interval_method": {
            "pi_identity": "pi=4*(atan(1/2)+atan(1/3))",
            "atan_half_last_index": 256,
            "atan_third_last_index": 192,
            "e_last_index": 256,
            "pi_lower_sha256": fraction_sha256(pi_box[0]),
            "pi_upper_sha256": fraction_sha256(pi_box[1]),
            "s_lower_sha256": fraction_sha256(s_box[0]),
            "s_upper_sha256": fraction_sha256(s_box[1]),
        },
        "digit_certificate": {
            "G_jets_0_through_T": g_jets,
            "combined_jets_0_through_T": combined_jets,
            "G_jet_vector_sha256": vector_sha256(g_jets),
            "combined_jet_vector_sha256": vector_sha256(combined_jets),
            "partial_integer_vector_sha256": vector_sha256(partial_integers),
        },
        "exact_scan_summary": {
            "all_full_row_rank": True,
            "all_nullity_one": True,
            "zero_endpoint_count": len(zero_endpoint_records),
            "zero_endpoint_records": zero_endpoint_records,
            "block_singular_triples": block_singular_triples,
            "stable_range_schur_checks": schur_checks,
            "all_nonsingular_block_endpoint_formulas_match": True,
        },
        "minima": minima,
        "records": records,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result["exact_scan_summary"], indent=2, sort_keys=True))
    print(json.dumps(result["minima"], indent=2, sort_keys=True))
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
