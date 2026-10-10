#!/usr/bin/env python3
"""Exact valid-prime counterexample to trace-quotient target injectivity."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


k, n = sp.symbols("k n", integer=True)


def recurrence_expressions(source: Path) -> dict[int, sp.Expr]:
    payload = json.loads(source.read_text(encoding="utf-8"))
    raw = payload["symbolic"]["coefficient_recurrence"]
    return {
        int(shift): sp.sympify(value, locals={"k": k, "n": n})
        for shift, value in raw.items()
    }


def recurrence_values(
    expressions: dict[int, sp.Expr], index: int, exponent: int
) -> dict[int, int]:
    return {
        shift: int(value.subs({k: index, n: exponent}))
        for shift, value in expressions.items()
    }


def target_matrix(m: int, expressions: dict[int, sp.Expr]) -> list[list[Fraction]]:
    exponent = 6 * m
    target = 4 * m
    columns: list[list[Fraction]] = []
    for initial_index in range(3):
        values = [Fraction(int(index == initial_index)) for index in range(3)]
        for row in range(target):
            coefficients = recurrence_values(expressions, row, exponent)
            pivot = coefficients[3]
            assert pivot != 0
            total = Fraction(0)
            for shift in range(-4, 3):
                coefficient_index = row + shift
                if 0 <= coefficient_index < len(values):
                    total += coefficients[shift] * values[coefficient_index]
            values.append(-total / pivot)
        columns.append(values[target : target + 3])
    return [[columns[column][row] for column in range(3)] for row in range(3)]


def trace_initial(m: int) -> list[int]:
    t, z = sp.symbols("t z")
    phi = t**3 - 2 * t**2 + 2 * t
    a = -2 + 3 * t - t**2
    remainder = sp.Poly(a ** (6 * m), t, domain=sp.QQ[z]).rem(
        sp.Poly(phi - z, t, domain=sp.QQ[z])
    )
    trace = sp.Poly(remainder.coeff_monomial(t**2), z, domain=sp.QQ)
    return [int(trace.nth(index)) for index in range(3)]


def denominator_series(order: int, cutoff: int) -> list[Fraction]:
    values = [Fraction(1, 2**order)]
    previous = Fraction(0)
    for degree in range(cutoff):
        current = values[degree]
        following = (
            2 * (degree + order) * current
            - (degree - 1 + 2 * order) * previous
        ) / (2 * (degree + 1))
        values.append(following)
        previous = current
    return values


def inverse_cubic_coefficient(exponent: int, degree: int) -> Fraction:
    denominator = denominator_series(degree + 1, degree)
    answer = Fraction(0)
    for left_degree in range(exponent + 1):
        for right_degree in range(exponent + 1):
            numerator_degree = left_degree + right_degree
            if numerator_degree > degree:
                continue
            numerator = (
                (-1) ** (exponent - left_degree)
                * math.comb(exponent, left_degree)
                * 2 ** (exponent - right_degree)
                * (-1) ** right_degree
                * math.comb(exponent, right_degree)
            )
            answer += numerator * denominator[degree - numerator_degree]
    return answer


def reduce_fraction(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def matrix_vector_mod(
    matrix: list[list[int]], vector: list[int], prime: int
) -> list[int]:
    return [
        sum(row[column] * vector[column] for column in range(3)) % prime
        for row in matrix
    ]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    column = 0
    while rank < len(work) and column < len(work[0]):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            column += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][entry] - factor * work[rank][entry]) % prime
                for entry in range(len(work[0]))
            ]
        rank += 1
        column += 1
    return rank


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recurrence-json",
        type=Path,
        default=Path("results/inverse_cubic_log_residue_certificate_m12.json"),
    )
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    m = 2
    prime = 112291
    source_bytes = arguments.recurrence_json.read_bytes()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    expressions = recurrence_expressions(arguments.recurrence_json)
    exponent = 6 * m
    forward_pivots = [
        recurrence_values(expressions, row, exponent)[3] for row in range(4 * m)
    ]
    forward_pivot_residues = [value % prime for value in forward_pivots]
    forward_pivots_are_units = all(forward_pivot_residues)
    rational_matrix = target_matrix(m, expressions)
    common_denominator = math.lcm(
        *(value.denominator for row in rational_matrix for value in row)
    )
    reduced_matrix = [
        [reduce_fraction(value, prime) for value in row] for row in rational_matrix
    ]
    reduced_rank = rank_mod_prime(reduced_matrix, prime)

    trace = [value % prime for value in trace_initial(m)]
    trace_image = matrix_vector_mod(reduced_matrix, trace, prime)
    extra_kernel_vector = [
        -reduced_matrix[0][1] % prime,
        reduced_matrix[0][0],
        0,
    ]
    extra_image = matrix_vector_mod(reduced_matrix, extra_kernel_vector, prime)
    nonproportional_minor = (
        extra_kernel_vector[0] * trace[1] - extra_kernel_vector[1] * trace[0]
    ) % prime

    distinguished_initial_rational = [
        inverse_cubic_coefficient(exponent, degree) for degree in range(3)
    ]
    distinguished_initial = [
        reduce_fraction(value, prime) for value in distinguished_initial_rational
    ]
    distinguished_target_from_matrix = matrix_vector_mod(
        reduced_matrix, distinguished_initial, prime
    )
    distinguished_target_direct = [
        reduce_fraction(inverse_cubic_coefficient(exponent, 4 * m + offset), prime)
        for offset in range(3)
    ]

    passed = (
        sp.isprime(prime)
        and prime > 6 * m
        and forward_pivots_are_units
        and common_denominator % prime != 0
        and reduced_rank == 1
        and trace_image == [0, 0, 0]
        and extra_image == [0, 0, 0]
        and nonproportional_minor != 0
        and distinguished_target_from_matrix == distinguished_target_direct
        and distinguished_target_direct != [0, 0, 0]
    )
    result = {
        "schema": "inverse-cubic-trace-quotient-rank-drop-v1",
        "recurrence_source": str(arguments.recurrence_json).replace("\\", "/"),
        "recurrence_source_sha256": source_sha256,
        "m": m,
        "n": exponent,
        "prime": prime,
        "prime_is_prime": bool(sp.isprime(prime)),
        "prime_is_fresh": prime > 6 * m,
        "forward_pivot_residues_mod_prime": forward_pivot_residues,
        "all_forward_pivots_are_units_mod_prime": forward_pivots_are_units,
        "rational_target_matrix": [
            [fraction_string(value) for value in row] for row in rational_matrix
        ],
        "target_matrix_common_denominator": str(common_denominator),
        "target_matrix_common_denominator_factorization": {
            str(factor): power for factor, power in sp.factorint(common_denominator).items()
        },
        "reduced_target_matrix": reduced_matrix,
        "reduced_rank": reduced_rank,
        "reduced_kernel_dimension": 3 - reduced_rank,
        "trace_initial_vector": trace,
        "trace_target_image": trace_image,
        "extra_kernel_vector": extra_kernel_vector,
        "extra_kernel_target_image": extra_image,
        "trace_extra_nonproportional_minor": nonproportional_minor,
        "distinguished_initial_vector": distinguished_initial,
        "distinguished_target_from_matrix": distinguished_target_from_matrix,
        "distinguished_target_direct": distinguished_target_direct,
        "passed": bool(passed),
        "scope": (
            "counterexample to target injectivity after quotienting by the trace line; "
            "not a common-zero counterexample for the distinguished inverse branch"
        ),
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    print(
        f"m={m}; p={prime}; rank={reduced_rank}; "
        f"distinguished_nonzero={distinguished_target_direct != [0, 0, 0]}; "
        f"passed={passed}; sha256={digest}"
    )
    if not passed:
        raise SystemExit(1)
    if arguments.output:
        arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
