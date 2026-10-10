#!/usr/bin/env python3
"""Portable exact certificate for Item 270.

All symbolic checks use only the Python standard library.  The optional
bounded sequence replay is EXACT FINITE ONLY and is not used as asymptotic
evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item270_all_shift_contiguous_module_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item270_all_shift_contiguous_module_certificate.json"
)


def trim(a: list[Fraction] | list[int]) -> list[Fraction]:
    out = list(map(Fraction, a))
    while out and out[-1] == 0:
        out.pop()
    return out


def padd(*values: list[Fraction] | list[int]) -> list[Fraction]:
    size = max((len(value) for value in values), default=0)
    out = [Fraction(0)] * size
    for value in values:
        for index, coefficient in enumerate(value):
            out[index] += Fraction(coefficient)
    return trim(out)


def pscale(value: list[Fraction] | list[int], scalar: Fraction | int) -> list[Fraction]:
    return trim([Fraction(scalar) * Fraction(coefficient) for coefficient in value])


def pmul(left: list[Fraction] | list[int], right: list[Fraction] | list[int]) -> list[Fraction]:
    if not left or not right:
        return []
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += Fraction(left_value) * Fraction(right_value)
    return trim(out)


def pdivmod(left: list[Fraction] | list[int], right: list[Fraction] | list[int]) -> tuple[list[Fraction], list[Fraction]]:
    dividend = trim(left)
    divisor = trim(right)
    if not divisor:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(dividend) - len(divisor) + 1)
    while dividend and len(dividend) >= len(divisor):
        offset = len(dividend) - len(divisor)
        coefficient = dividend[-1] / divisor[-1]
        quotient[offset] += coefficient
        for index, value in enumerate(divisor):
            dividend[offset + index] -= coefficient * value
        dividend = trim(dividend)
    return trim(quotient), dividend


def pdivexact(left: list[Fraction] | list[int], right: list[Fraction] | list[int]) -> list[Fraction]:
    quotient, remainder = pdivmod(left, right)
    if remainder:
        raise AssertionError((left, right, remainder))
    return quotient


def pgcd(left: list[Fraction] | list[int], right: list[Fraction] | list[int]) -> list[Fraction]:
    a_value, b_value = trim(left), trim(right)
    while b_value:
        _, remainder = pdivmod(a_value, b_value)
        a_value, b_value = b_value, remainder
    return pscale(a_value, 1 / a_value[-1]) if a_value else []


def primitive(value: list[Fraction] | list[int]) -> list[int]:
    coefficients = list(map(Fraction, value))
    denominator = 1
    for coefficient in coefficients:
        denominator = math.lcm(denominator, coefficient.denominator)
    integers = [int(coefficient * denominator) for coefficient in coefficients]
    common = 0
    for integer in integers:
        common = math.gcd(common, abs(integer))
    if common:
        integers = [integer // common for integer in integers]
    if integers and integers[-1] < 0:
        integers = [-integer for integer in integers]
    return integers


def conv(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return out


def determinant_bareiss_polynomial(matrix: list[list[list[int] | list[Fraction]]]) -> list[Fraction]:
    rows = [[trim(entry) for entry in row] for row in matrix]
    size = len(rows)
    previous = [Fraction(1)]
    sign = 1
    for column in range(size - 1):
        pivot = next((index for index in range(column, size) if rows[index][column]), None)
        if pivot is None:
            return []
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign = -sign
        pivot_value = rows[column][column]
        for i in range(column + 1, size):
            for j in range(column + 1, size):
                numerator = padd(
                    pmul(pivot_value, rows[i][j]),
                    pscale(pmul(rows[i][column], rows[column][j]), -1),
                )
                rows[i][j] = pdivexact(numerator, previous)
            rows[i][column] = []
        previous = pivot_value
    return pscale(rows[-1][-1], sign)


def rational_nullspace(matrix: list[list[int | Fraction]]) -> tuple[int, list[list[Fraction]], list[int]]:
    rows = [list(map(Fraction, row)) for row in matrix]
    row_count, column_count = len(rows), len(rows[0])
    rank = 0
    pivots: list[int] = []
    for column in range(column_count):
        pivot = next((index for index in range(rank, row_count) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][column]
        rows[rank] = [value / divisor for value in rows[rank]]
        for index in range(row_count):
            if index != rank and rows[index][column]:
                multiplier = rows[index][column]
                rows[index] = [
                    value - multiplier * pivot_value
                    for value, pivot_value in zip(rows[index], rows[rank])
                ]
        pivots.append(column)
        rank += 1
    free = [column for column in range(column_count) if column not in pivots]
    basis: list[list[Fraction]] = []
    for free_column in free:
        vector = [Fraction(0)] * column_count
        vector[free_column] = 1
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -rows[row_index][free_column]
        basis.append(vector)
    return rank, basis, pivots


def normalize_vector(vector: list[Fraction]) -> list[int]:
    denominator = 1
    for value in vector:
        denominator = math.lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in vector]
    common = 0
    for value in integers:
        common = math.gcd(common, abs(value))
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    return integers if first > 0 else [-value for value in integers]


def bivariate_add(*values: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def bivariate_mul(
    left: dict[tuple[int, int], Fraction], right: dict[tuple[int, int], Fraction]
) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for (x_left, s_left), coefficient_left in left.items():
        for (x_right, s_right), coefficient_right in right.items():
            monomial = (x_left + x_right, s_left + s_right)
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient_left * coefficient_right
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def bivariate_scale(
    value: dict[tuple[int, int], Fraction], scalar: int | Fraction
) -> dict[tuple[int, int], Fraction]:
    return {monomial: Fraction(scalar) * coefficient for monomial, coefficient in value.items() if coefficient}


def bivariate_dx(value: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    return {
        (x_degree - 1, s_degree): x_degree * coefficient
        for (x_degree, s_degree), coefficient in value.items()
        if x_degree
    }


def bx(coefficients: list[int]) -> dict[tuple[int, int], Fraction]:
    return {(degree, 0): Fraction(coefficient) for degree, coefficient in enumerate(coefficients) if coefficient}


def bs(coefficients: list[int]) -> dict[tuple[int, int], Fraction]:
    return {(0, degree): Fraction(coefficient) for degree, coefficient in enumerate(coefficients) if coefficient}


def adjacent_polynomials() -> tuple[list[Fraction], list[Fraction], list[Fraction], list[Fraction]]:
    a_value = [3, 100, 75]
    b_value = [4, 11, 6]
    c_value = [998, 1525, 575]
    d_value = [81, 123, 46]
    current_common = pmul([1, 1], [3, 2])
    future_common = pmul([4, 3], [5, 3])
    return (
        pscale(pmul(current_common, a_value), 16),
        pscale(pmul(current_common, b_value), -320),
        pscale(pmul(future_common, c_value), 3),
        pscale(pmul(future_common, d_value), -60),
    )


def verify_adjacent_telescoping() -> str:
    Q = bx([1, 1, 1, 1])
    Q_prime = bx([1, 2, 3])
    x = bx([0, 1])
    x3 = bx([0, 0, 0, 1])
    one_minus_x = bx([1, -1])
    one_minus_x_cubed = bivariate_mul(one_minus_x, bivariate_mul(one_minus_x, one_minus_x))
    p0, p1, p2, p3 = map(bs, adjacent_polynomials())
    target = bivariate_add(
        bivariate_mul(bivariate_mul(x3, one_minus_x_cubed), bivariate_add(bivariate_mul(p0, Q), p1)),
        bivariate_mul(bivariate_mul(Q, Q), bivariate_add(bivariate_mul(p2, Q), p3)),
    )
    n_rows = [
        [7464, 16818, 12555, 3105], [14886, 33549, 25065, 6210],
        [22140, 49988, 37455, 9315], [30318, 68723, 51685, 12900],
        [18120, 41250, 31245, 7875], [16458, 38439, 29775, 7650],
        [5364, 12720, 10025, 2625], [-894, -1375, -525],
    ]
    N: dict[tuple[int, int], Fraction] = {}
    for x_degree, row in enumerate(n_rows):
        for s_degree, coefficient in enumerate(row):
            if coefficient:
                N[(x_degree, s_degree)] = Fraction(coefficient)
    derivative_part = bivariate_mul(bivariate_mul(x, one_minus_x), Q)
    K = bivariate_add(
        bivariate_mul(bs([1, 2]), bivariate_mul(bivariate_mul(x, one_minus_x), Q_prime)),
        bivariate_mul(bs([-5, -3]), bivariate_mul(one_minus_x, Q)),
        bivariate_mul(bs([5, 3]), bivariate_mul(x, Q)),
    )
    telescoper = bivariate_add(bivariate_mul(derivative_part, bivariate_dx(N)), bivariate_mul(K, N))
    if telescoper != target:
        raise AssertionError("adjacent telescoping identity")
    return hashlib.sha256((repr(sorted(target.items())) + repr(sorted(N.items()))).encode("ascii")).hexdigest()


def window_reduction_matrix(degree: int, infinity_degree: int = 13) -> tuple[list[list[Fraction]], int]:
    """Relation-plus-certificate matrix for v_s,v_{s+1},v_{s+2}.

    A certificate is R=NQ/[x^8(1-x)^8].  infinity_degree=13 is exact;
    11 is the deliberately truncated diagnostic.
    """
    Q = [1, 1, 1, 1]
    one_minus = [1, -1]
    Q2 = conv(Q, Q)
    Q4 = conv(Q2, Q2)
    one_minus_3 = [1]
    for _ in range(3):
        one_minus_3 = conv(one_minus_3, one_minus)
    one_minus_6 = conv(one_minus_3, one_minus_3)
    x3, x6 = [0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1]
    weights = [
        conv(conv(x6, one_minus_6), Q), conv(x6, one_minus_6),
        conv(conv(conv(x3, one_minus_3), Q2), Q), conv(conv(x3, one_minus_3), Q2),
        conv(Q4, Q), Q4,
    ]
    # Keep the full three-layer numerator range even in the deliberately
    # truncated diagnostic, so the two matrices differ only in columns.
    x_bound = 18
    keys = [(x_degree, s_degree) for x_degree in range(x_bound) for s_degree in range(degree + 1)]
    row_index = {key: index for index, key in enumerate(keys)}
    observation_columns = 6 * (degree + 1)
    certificate_columns = (infinity_degree + 1) * degree
    matrix = [[Fraction(0)] * (observation_columns + certificate_columns) for _ in keys]
    for observation, weight in enumerate(weights):
        for s_degree in range(degree + 1):
            column = observation * (degree + 1) + s_degree
            for x_degree, coefficient in enumerate(weight):
                if coefficient:
                    matrix[row_index[(x_degree, s_degree)]][column] += coefficient
    x = [0, 1]
    Q_prime = [1, 2, 3]
    derivative_prefactor = conv(conv(x, one_minus), Q)
    K0 = padd(
        conv(conv(x, one_minus), Q_prime),
        pscale(conv(one_minus, Q), -8),
        pscale(conv(x, Q), 8),
    )
    P = [-3, 5, 5, 5]
    for x_degree in range(infinity_degree + 1):
        for s_degree in range(degree):
            column = observation_columns + x_degree * degree + s_degree
            if x_degree:
                derivative = conv(derivative_prefactor, [0] * (x_degree - 1) + [x_degree])
                for output_degree, coefficient in enumerate(derivative):
                    if coefficient:
                        matrix[row_index[(output_degree, s_degree)]][column] -= coefficient
            for output_degree, coefficient in enumerate([0] * x_degree + list(K0)):
                if coefficient:
                    matrix[row_index[(output_degree, s_degree)]][column] -= coefficient
            for output_degree, coefficient in enumerate([0] * x_degree + P):
                if coefficient:
                    matrix[row_index[(output_degree, s_degree + 1)]][column] -= coefficient
    return matrix, observation_columns


EXPECTED_SYZYGIES = [
    [
        [840, 13280, 20360, 7920], [-9504, -34848, -38016, -12672],
        [149580, 295740, 190590, 40590], [-256860, -483396, -305520, -64944],
        [514920, 617055, 246105, 32670], [-831096, -993093, -394929, -52272],
    ],
    [
        [4752, 124320, 197168, 77600], [-93120, -341440, -372480, -124160],
        [1589880, 3178860, 2080686, 450450], [-2716200, -5209200, -3346680, -720720],
        [3794112, 4548240, 1814643, 240975], [-6123600, -7319790, -2911950, -385560],
    ],
]


def verify_three_layer_syzygies() -> tuple[str, dict[str, Any]]:
    matrix, observation_columns = window_reduction_matrix(3, 13)
    rank, basis, pivots = rational_nullspace(matrix)
    normalized = [normalize_vector(vector) for vector in basis]
    observed = [
        [vector[observation * 4 : (observation + 1) * 4] for observation in range(6)]
        for vector in normalized
    ]
    if rank != 64 or len(basis) != 2 or observed != EXPECTED_SYZYGIES:
        raise AssertionError((rank, observed))
    for vector in normalized:
        for row in matrix:
            if sum(Fraction(coefficient) * value for coefficient, value in zip(row, vector)):
                raise AssertionError("syzygy certificate")
    truncated, _ = window_reduction_matrix(3, 11)
    truncated_rank, truncated_basis, _ = rational_nullspace(truncated)
    if truncated_rank != 60 or truncated_basis:
        raise AssertionError((truncated_rank, len(truncated_basis)))
    digest = hashlib.sha256((repr(normalized) + repr(pivots)).encode("ascii")).hexdigest()
    return digest, {
        "full_matrix_shape": [len(matrix), len(matrix[0])],
        "rank": rank,
        "nullity": len(basis),
        "certificate_numerator_x_degree": 13,
        "truncated_x_degree_11_shape": [len(truncated), len(truncated[0])],
        "truncated_rank": truncated_rank,
        "truncated_nullity": len(truncated_basis),
    }


def basis_independence_determinant() -> tuple[list[int], str]:
    Q = [1, 1, 1, 1]
    one_minus = [1, -1]
    x3 = [0, 0, 0, 1]
    base = conv(x3, conv(conv(one_minus, one_minus), one_minus))
    columns: list[list[list[int] | list[Fraction]]] = []
    for target in (conv(base, Q), base, conv(conv(Q, Q), Q)):
        columns.append([[target[x_degree] if x_degree < len(target) else 0] for x_degree in range(12)])
    x = [0, 1]
    Q_prime = [1, 2, 3]
    derivative_prefactor = conv(conv(x, one_minus), Q)
    K0 = padd(
        conv(conv(x, one_minus), Q_prime),
        pscale(conv(one_minus, Q), -5),
        pscale(conv(x, Q), 5),
    )
    P = [-3, 5, 5, 5]
    for numerator_degree in range(8):
        constant = [Fraction(0)] * 12
        linear = [Fraction(0)] * 12
        if numerator_degree:
            derivative = conv(derivative_prefactor, [0] * (numerator_degree - 1) + [numerator_degree])
            for degree, coefficient in enumerate(derivative):
                constant[degree] += coefficient
        for degree, coefficient in enumerate([0] * numerator_degree + list(K0)):
            constant[degree] += coefficient
        for degree, coefficient in enumerate([0] * numerator_degree + P):
            linear[degree] += coefficient
        columns.append(
            [[-constant[degree], -linear[degree]] if linear[degree] else [-constant[degree]] for degree in range(12)]
        )
    rows = [[columns[column][row] for column in range(11)] for row in range(12)]
    minor = rows[:11]  # omit x^11
    determinant = determinant_bareiss_polynomial(minor)
    expected_factor = pmul(
        pmul(pmul([1, 1], pmul([1, 2], [1, 2])), pmul([3, 2], [5, 3])),
        pmul([4, 3], [27, 23]),
    )
    expected = pscale(expected_factor, 30720)
    if determinant != expected:
        raise AssertionError((primitive(determinant), primitive(expected)))
    digest = hashlib.sha256(repr(rows).encode("ascii")).hexdigest()
    return primitive(determinant), digest


def transfer_certificate() -> dict[str, Any]:
    syzygies = EXPECTED_SYZYGIES
    A, B, C, D = adjacent_polynomials()
    k00, k01 = syzygies[0][4], syzygies[0][5]
    k10, k11 = syzygies[1][4], syzygies[1][5]
    future_determinant = padd(pmul(k00, k11), pscale(pmul(k01, k10), -1))
    future_factor = pmul([2, 1], pmul(pmul([7, 3], [7, 3]), pmul([8, 3], [8, 3])))
    if future_determinant != pscale(future_factor, 17091):
        raise AssertionError(primitive(future_determinant))

    current_eliminant_0 = padd(pmul(k11, syzygies[0][0]), pscale(pmul(k01, syzygies[1][0]), -1))
    current_eliminant_1 = padd(pmul(k11, syzygies[0][1]), pscale(pmul(k01, syzygies[1][1]), -1))
    determinant_numerator = padd(pmul(A, current_eliminant_1), pscale(pmul(B, current_eliminant_0), -1))
    determinant_denominator = pmul(D, future_determinant)
    common = pgcd(determinant_numerator, determinant_denominator)
    numerator_reduced = pdivexact(determinant_numerator, common)
    denominator_reduced = pdivexact(determinant_denominator, common)
    numerator_factor = pmul(
        pmul([5, 2], [50, 23]),
        pmul(pmul([3, 2], pmul([1, 1], [1, 1])), [1, 2]),
    )
    denominator_factor = pmul(
        pmul([8, 3], [7, 3]),
        pmul(pmul([2, 1], [5, 3]), pmul([4, 3], [27, 23])),
    )
    numerator_scalar = pdivexact(numerator_reduced, numerator_factor)[0]
    denominator_scalar = pdivexact(denominator_reduced, denominator_factor)[0]
    if numerator_scalar / denominator_scalar != Fraction(512, 9):
        raise AssertionError((numerator_scalar, denominator_scalar))

    # Reduced denominators for the third row z0 of T_s.  The first two rows
    # are (0,0,1) and the adjacent relation.  These exact gcds prove that no
    # nonlinear apparent factor survives in the transfer entries.
    expected_z_denominators = [
        [60480, 212008, 304382, 229095, 95355, 20817, 1863],
        [15120, 41662, 44849, 23637, 6111, 621],
        [3024, 6518, 5059, 1692, 207],
    ]
    z_denominators: list[list[int]] = []
    for coordinate, adjacent in enumerate((A, B, C)):
        current_0 = syzygies[0][coordinate] if coordinate < 2 else syzygies[0][2]
        current_1 = syzygies[1][coordinate] if coordinate < 2 else syzygies[1][2]
        y0 = padd(pmul(D, current_0), pscale(pmul(syzygies[0][3], adjacent), -1))
        y1 = padd(pmul(D, current_1), pscale(pmul(syzygies[1][3], adjacent), -1))
        numerator = pscale(padd(pmul(k11, y0), pscale(pmul(k01, y1), -1)), -1)
        reduced = primitive(pdivexact(determinant_denominator, pgcd(numerator, determinant_denominator)))
        z_denominators.append(reduced)
    if z_denominators != expected_z_denominators:
        raise AssertionError(z_denominators)

    linear_factors = [
        [1, 1], [1, 2], [2, 1], [2, 3], [2, 5],
        [3, 4], [3, 5], [3, 7], [3, 8], [23, 27], [23, 50],
    ]
    return {
        "future_minor": {
            "exact": "17091(s+2)(3s+7)^2(3s+8)^2",
            "fixed_factorization": "17091=3^4*211",
        },
        "transfer_determinant": (
            "(512/9)(s+1)^2(2s+1)(2s+3)(2s+5)(23s+50)/"
            "((s+2)(3s+4)(3s+5)(3s+7)(3s+8)(23s+27))"
        ),
        "reduced_z0_row_denominators": z_denominators,
        "exceptional_linear_factor_pairs_a_b": linear_factors,
        "fixed_exceptional_primes": [2, 3, 5, 211],
    }


def g_pair_mod(s_value: int, prime: int) -> tuple[int, int]:
    terminal_degree = 3 * s_value + 2
    coefficients = [0] * (terminal_degree + 1)
    coefficients[0] = 1
    for degree in range(terminal_degree):
        def coefficient(index: int) -> int:
            return coefficients[index] if index >= 0 else 0
        right = (
            (5 * s_value + 3) * (coefficient(degree) + coefficient(degree - 1) + coefficient(degree - 2))
            + (degree - 3 * s_value) * coefficient(degree - 3)
        ) % prime
        denominator = degree + 1
        if denominator % prime == 0:
            raise AssertionError("nonunit coefficient recurrence")
        coefficients[degree + 1] = right * pow(denominator, -1, prime) % prime
    return sum(coefficients[max(0, terminal_degree - 3) : terminal_degree + 1]) % prime, coefficients[terminal_degree]


def finite_sequence_replay() -> str:
    digest = hashlib.sha256()
    values: list[tuple[int, int]] = []
    for s_value in range(18):
        # The modulus is larger than all recurrence denominators, so this is
        # an exact finite identity check in F_p, not asymptotic evidence.
        pair = g_pair_mod(s_value, 1000003)
        values.append(pair)
        digest.update((repr((s_value, pair)) + "\n").encode("ascii"))
    for s_value in range(16):
        for relation in EXPECTED_SYZYGIES:
            total = 0
            observations = values[s_value] + values[s_value + 1] + values[s_value + 2]
            for polynomial, observation in zip(relation, observations):
                total += sum(coefficient * s_value**degree for degree, coefficient in enumerate(polynomial)) * observation
            if total % 1000003:
                raise AssertionError((s_value, total))
    if g_pair_mod(299, 2399) != (0, 0) or g_pair_mod(300, 2399) != (2105, 1694):
        raise AssertionError("actual-family witness")
    return digest.hexdigest()


def certificate() -> dict[str, Any]:
    adjacent_hash = verify_adjacent_telescoping()
    syzygy_hash, syzygy_data = verify_three_layer_syzygies()
    basis_determinant, basis_hash = basis_independence_determinant()
    transfer = transfer_certificate()
    finite_hash = finite_sequence_replay()
    far_terms = [
        Fraction(1, 45), Fraction(2, 35), Fraction(1, 230), Fraction(1, 44),
        Fraction(1, 90), Fraction(11, 2185), Fraction(1, 460), Fraction(1, 1485),
    ]
    far_coefficient = sum(far_terms, Fraction(0))
    if far_coefficient != Fraction(1139587, 9085230):
        raise AssertionError(far_coefficient)
    body: dict[str, Any] = {
        "schema": "item270-all-shift-contiguous-module-certificate-v1",
        "labels": {
            "rank_three_module": "PROVED over Q(s) by exact twisted-de-Rham reduction",
            "forward_backward_windows": "PROVED where shifted actual rows and determinant factors are defined",
            "bounded_sequence_replay": "EXACT FINITE ONLY",
            "collision_forced_extra_codimension": 0,
            "new_route1_rate": 0,
        },
        "kernel": {
            "Q": "1+x+x^2+x^3",
            "Phi": "Q^2/(x^3(1-x)^3)",
            "w": "1/(x^2(1-x)^3)",
            "state": "X_s=(g0(s),g1(s),g0(s+1))",
            "adjacent_telescoping_sha256": adjacent_hash,
        },
        "basis": {
            "dimension_over_Q(s)": 3,
            "determinant": "30720(s+1)(2s+1)^2(2s+3)(3s+4)(3s+5)(23s+27)",
            "determinant_coefficients_low_to_high": basis_determinant,
            "matrix_sha256": basis_hash,
        },
        "three_layer_reduction": {
            **syzygy_data,
            "full_certificate_sha256": syzygy_hash,
            "syzygy_observation_polynomials_low_to_high": EXPECTED_SYZYGIES,
            "infinity_boundary": (
                "N has degree 13 because NQ/[x^8(1-x)^8] may be constant at infinity; "
                "degree 11 gives the certified false nullity zero"
            ),
        },
        "transfer": transfer,
        "all_window_theorem": {
            "forward": "X_(s+n)=T_(s+n-1)...T_s X_s",
            "backward": "X_(s-n)=T_(s-n)^(-1)...T_(s-1)^(-1)X_s where defined",
            "common_gate": "g0(s)=g1(s)=0 gives X_s=(0,0,u); every bounded window is one line parameterized by u",
            "fixed_M_container": "a(s+h)+b=0 mod p implies p | a(2M+1)-ah-b",
            "exceptional_log_weight": "O_L(log M) for every fixed window radius L",
        },
        "actual_family": {
            "phase_shift": "(s,b,r,j,M)->(s+h,b-5h,r+3h mod 4,j+h,M+h(p-1)/2)",
            "nonpropagation_witness": {
                "current_M_s_p_j_b": [2249, 299, 2399, 1, 900],
                "current_g0_g1": [0, 0],
                "next_M_s_j_b": [3448, 300, 2, 895],
                "next_g0_g1": [2105, 1694],
            },
            "far_capacity_exact_per_M": str(far_coefficient),
            "far_capacity_decimal_per_M": format(float(far_coefficient), ".15f"),
            "gap_for_comparison_per_M": "0.1177979020",
        },
        "finite_replay": {
            "label": "EXACT FINITE ONLY",
            "range": "s=0..17 modulo 1000003 plus the declared p=2399 witness",
            "sha256": finite_hash,
        },
        "booking": {
            "item149_first_copy_already_booked": True,
            "new_independent_valuation_copy": 0,
            "new_weighted_zero_theorem": 0,
            "new_route1_rate": 0,
            "far_raw_ceiling_after_item270": "unchanged",
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "output": str(args.output), "payload_sha256": result["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
