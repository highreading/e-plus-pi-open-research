#!/usr/bin/env python3
"""Portable exact certificate for Item 268.

The checker uses only the Python standard library.  Bounded recurrence and
row-map checks are labelled EXACT FINITE ONLY; no common-zero scan is made.
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
    HERE / "item268_cross_b_contiguous_obstruction_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item268_cross_b_contiguous_obstruction_certificate.json"
)


# Bivariate polynomials are dictionaries (x_degree,s_degree) -> Fraction.
Poly = dict[tuple[int, int], Fraction]


def poly_add(*values: Poly) -> Poly:
    result: Poly = {}
    for value in values:
        for monomial, coefficient in value.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def poly_scale(value: Poly, scalar: int | Fraction) -> Poly:
    scalar = Fraction(scalar)
    return {monomial: scalar * coefficient for monomial, coefficient in value.items() if scalar * coefficient}


def poly_mul(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (x_left, s_left), coefficient_left in left.items():
        for (x_right, s_right), coefficient_right in right.items():
            monomial = (x_left + x_right, s_left + s_right)
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient_left * coefficient_right
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def poly_dx(value: Poly) -> Poly:
    return {
        (x_degree - 1, s_degree): x_degree * coefficient
        for (x_degree, s_degree), coefficient in value.items()
        if x_degree
    }


def poly_x(coefficients: list[int]) -> Poly:
    return {(degree, 0): Fraction(coefficient) for degree, coefficient in enumerate(coefficients) if coefficient}


def poly_s(coefficients: list[int]) -> Poly:
    return {(0, degree): Fraction(coefficient) for degree, coefficient in enumerate(coefficients) if coefficient}


def multiply_univariate(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            result[i + j] += a_value * b_value
    return result


def fraction_poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    while result and result[-1] == 0:
        result.pop()
    return result


def fraction_poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    while result and result[-1] == 0:
        result.pop()
    return result


def quadratic_substitute(coefficients: list[int], linear: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(coefficients[0])]
    answer = fraction_poly_add(answer, [Fraction(coefficients[1]) * value for value in linear])
    square = fraction_poly_mul(linear, linear)
    answer = fraction_poly_add(answer, [Fraction(coefficients[2]) * value for value in square])
    return answer


def contiguous_polynomials() -> tuple[list[int], list[int], list[int], list[int]]:
    a_value = [3, 100, 75]
    b_value = [4, 11, 6]
    c_value = [998, 1525, 575]
    d_value = [81, 123, 46]
    p0 = [16 * value for value in multiply_univariate([3, 5, 2], a_value)]
    p1 = [-320 * value for value in multiply_univariate([3, 5, 2], b_value)]
    p2 = [3 * value for value in multiply_univariate([20, 27, 9], c_value)]
    p3 = [-60 * value for value in multiply_univariate([20, 27, 9], d_value)]
    return p0, p1, p2, p3


def verify_telescoping_identity() -> str:
    Q = poly_x([1, 1, 1, 1])
    Q_prime = poly_x([1, 2, 3])
    x = poly_x([0, 1])
    x3 = poly_x([0, 0, 0, 1])
    one_minus_x = poly_x([1, -1])
    one_minus_x_cubed = poly_mul(one_minus_x, poly_mul(one_minus_x, one_minus_x))
    p0_list, p1_list, p2_list, p3_list = contiguous_polynomials()
    p0, p1, p2, p3 = map(poly_s, (p0_list, p1_list, p2_list, p3_list))

    # Numerator of the period combination over x^5(1-x)^6.
    target = poly_add(
        poly_mul(poly_mul(x3, one_minus_x_cubed), poly_add(poly_mul(p0, Q), p1)),
        poly_mul(poly_mul(Q, Q), poly_add(poly_mul(p2, Q), p3)),
    )

    n_rows = [
        [7464, 16818, 12555, 3105],
        [14886, 33549, 25065, 6210],
        [22140, 49988, 37455, 9315],
        [30318, 68723, 51685, 12900],
        [18120, 41250, 31245, 7875],
        [16458, 38439, 29775, 7650],
        [5364, 12720, 10025, 2625],
        [-894, -1375, -525],
    ]
    N: Poly = {}
    for x_degree, row in enumerate(n_rows):
        for s_degree, coefficient in enumerate(row):
            if coefficient:
                N[(x_degree, s_degree)] = Fraction(coefficient)

    # Numerator of theta(R_s)+s R_s theta(log Phi), same denominator.
    derivative_part = poly_mul(poly_mul(x, one_minus_x), Q)
    K = poly_add(
        poly_mul(poly_s([1, 2]), poly_mul(poly_mul(x, one_minus_x), Q_prime)),
        poly_mul(poly_s([-5, -3]), poly_mul(one_minus_x, Q)),
        poly_mul(poly_s([5, 3]), poly_mul(x, Q)),
    )
    telescoper = poly_add(poly_mul(derivative_part, poly_dx(N)), poly_mul(K, N))
    if telescoper != target:
        difference = poly_add(telescoper, poly_scale(target, -1))
        raise AssertionError(sorted(difference.items()))
    serial = repr(sorted(target.items())) + "\n" + repr(sorted(N.items()))
    return hashlib.sha256(serial.encode("ascii")).hexdigest()


def g_pair_exact(s_value: int) -> tuple[int, int]:
    k_value = 3 * s_value + 2
    coefficients = [0] * (k_value + 1)
    coefficients[0] = 1
    for n_value in range(k_value):
        def A(index: int) -> int:
            return coefficients[index] if index >= 0 else 0

        right = (
            (5 * s_value + 3) * (A(n_value) + A(n_value - 1) + A(n_value - 2))
            + (n_value - 3 * s_value) * A(n_value - 3)
        )
        if right % (n_value + 1):
            raise AssertionError((s_value, n_value, right))
        coefficients[n_value + 1] = right // (n_value + 1)
    g1 = coefficients[k_value]
    g0 = sum(coefficients[max(0, k_value - 3) : k_value + 1])
    return g0, g1


def g_pair_binomial(s_value: int) -> tuple[int, int]:
    k_value = 3 * s_value + 2
    answers = []
    for a_value in (1, 0):  # g0 then g1
        exponent = 2 * s_value + a_value
        denominator_power = 5 * s_value + 3 + a_value
        total = 0
        for index in range(min(exponent, k_value // 4) + 1):
            degree = k_value - 4 * index
            total += (
                (-1) ** index
                * math.comb(exponent, index)
                * math.comb(denominator_power + degree - 1, degree)
            )
        answers.append(total)
    return answers[0], answers[1]


def rational_rank_and_nullspace(matrix: list[list[int]]) -> tuple[int, list[Fraction], list[int]]:
    rows = [list(map(Fraction, row)) for row in matrix]
    column_count = len(rows[0])
    rank = 0
    pivots: list[int] = []
    for column in range(column_count):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for index in range(len(rows)):
            if index != rank and rows[index][column]:
                scale = rows[index][column]
                rows[index] = [value - scale * pivot_value for value, pivot_value in zip(rows[index], rows[rank])]
        pivots.append(column)
        rank += 1
    free = [column for column in range(column_count) if column not in pivots]
    if len(free) != 1:
        raise AssertionError((rank, free))
    vector = [Fraction(0)] * column_count
    vector[free[0]] = 1
    for row_index, pivot_column in enumerate(pivots):
        vector[pivot_column] = -rows[row_index][free[0]]
    return rank, vector, pivots


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
    if first < 0:
        integers = [-value for value in integers]
    return integers


def determinant(matrix: list[list[int]]) -> int:
    rows = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        pivot = next((index for index in range(column, len(rows)) if rows[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result = -result
        pivot_value = rows[column][column]
        result *= pivot_value
        rows[column] = [value / pivot_value for value in rows[column]]
        for index in range(column + 1, len(rows)):
            scale = rows[index][column]
            rows[index] = [value - scale * pivot_entry for value, pivot_entry in zip(rows[index], rows[column])]
    if result.denominator != 1:
        raise AssertionError(result)
    return result.numerator


def resultant(left: list[int], right: list[int]) -> int:
    left_high = list(reversed(left))
    right_high = list(reversed(right))
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    matrix = []
    for offset in range(right_degree):
        matrix.append([0] * offset + left_high + [0] * (size - offset - len(left_high)))
    for offset in range(left_degree):
        matrix.append([0] * offset + right_high + [0] * (size - offset - len(right_high)))
    return determinant(matrix)


def g_pair_mod(s_value: int, prime: int) -> tuple[int, int, tuple[int, int, int, int]]:
    k_value = 3 * s_value + 2
    coefficients = [0] * (k_value + 1)
    coefficients[0] = 1
    for n_value in range(k_value):
        def A(index: int) -> int:
            return coefficients[index] if index >= 0 else 0

        right = (
            (5 * s_value + 3) * (A(n_value) + A(n_value - 1) + A(n_value - 2))
            + (n_value - 3 * s_value) * A(n_value - 3)
        ) % prime
        if (n_value + 1) % prime == 0:
            raise AssertionError((s_value, prime, n_value, "nonunit recurrence denominator"))
        coefficients[n_value + 1] = right * pow(n_value + 1, -1, prime) % prime
    terminal = tuple(coefficients[k_value - 3 : k_value + 1])
    return sum(terminal) % prime, coefficients[k_value], terminal  # type: ignore[return-value]


def sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for value in range(2, math.isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [value for value, flag in enumerate(flags) if flag]


def finite_affected_rows(max_M: int) -> tuple[int, int, str]:
    primes = sieve(2 * max_M + 20)
    far_rows = 0
    boundary_rows = 0
    digest = hashlib.sha256()
    for M in range(25, max_M + 1):
        for j_value in range(1, 2 * M + 1):
            upper = 6 * M // (3 * j_value + 2)
            for prime in primes:
                if prime > upper:
                    break
                s_value = (j_value + 1) * prime - (2 * M + 1)
                if s_value < 0 or prime <= 3 * s_value + 2:
                    continue
                q_value = 1 if prime >= 5 * s_value + 4 else 2
                b_value = q_value * prime - 5 * s_value - 4
                if b_value > 3 * s_value + 4 or 5 * b_value < M:
                    continue
                far_rows += 1
                is_boundary = prime <= 3 * s_value + 5
                if is_boundary:
                    boundary_rows += 1
                    c_value = prime - 3 * s_value
                    if c_value not in (3, 4, 5) or (3 * j_value + 2) * prime != 6 * M + 3 - c_value:
                        raise AssertionError((M, j_value, prime, s_value, c_value))
                else:
                    b_next = b_value - 5
                    s_next = s_value + 1
                    q_next = 1 if prime >= 5 * s_next + 4 else 2
                    if q_next != q_value or b_next != q_next * prime - 5 * s_next - 4:
                        raise AssertionError((M, j_value, prime, s_value, q_value, b_value))
                    if b_next < 0 or b_next > 3 * s_next + 4 or prime <= 3 * s_next + 2:
                        raise AssertionError((M, j_value, prime, s_value, "adjacent not stable"))
                    M_next = M + (prime - 1) // 2
                    if 2 * M_next + 1 != (j_value + 2) * prime - s_next:
                        raise AssertionError((M, j_value, prime, s_value, M_next))
                digest.update((repr((M, j_value, prime, s_value, q_value, b_value, is_boundary)) + "\n").encode("ascii"))
    return far_rows, boundary_rows, digest.hexdigest()


def certificate(max_M: int) -> dict[str, Any]:
    if max_M < 200:
        raise ValueError("canonical finite replay requires max_M>=200")

    telescoping_hash = verify_telescoping_identity()
    p0, p1, p2, p3 = contiguous_polynomials()
    expected = p0 + p1 + p2 + p3

    # Exact sequence reconstruction and degree<=4 uniqueness matrix.
    pairs = []
    for s_value in range(26):
        recurrence_pair = g_pair_exact(s_value)
        if s_value <= 18 and recurrence_pair != g_pair_binomial(s_value):
            raise AssertionError((s_value, recurrence_pair, g_pair_binomial(s_value)))
        pairs.append(recurrence_pair)
    matrix = []
    for s_value in range(25):
        values = [pairs[s_value][0], pairs[s_value][1], pairs[s_value + 1][0], pairs[s_value + 1][1]]
        row = []
        for value in values:
            row.extend(value * s_value**degree for degree in range(5))
        matrix.append(row)
    rank, null_vector, pivots = rational_rank_and_nullspace(matrix)
    normalized = normalize_vector(null_vector)
    expected_common = 0
    for value in expected:
        expected_common = math.gcd(expected_common, abs(value))
    expected_primitive = [value // expected_common for value in expected]
    if next(value for value in expected_primitive if value) < 0:
        expected_primitive = [-value for value in expected_primitive]
    if rank != 19 or normalized != expected_primitive:
        raise AssertionError((rank, normalized, expected_primitive))
    for row in matrix:
        if sum(value * coefficient for value, coefficient in zip(row, expected)) != 0:
            raise AssertionError("contiguous identity failed on exact sequence")
    matrix_hash = hashlib.sha256((repr(matrix) + "\n" + repr(pivots)).encode("ascii")).hexdigest()

    resultant_current = resultant([3, 100, 75], [4, 11, 6])
    resultant_adjacent = resultant([998, 1525, 575], [81, 123, 46])
    if resultant_current != -3051 or resultant_adjacent != 1564:
        raise AssertionError((resultant_current, resultant_adjacent))

    # Exact phase substitution s=-(b+4)/5 and relocation b'=b-5.
    s_of_b = [Fraction(-4, 5), Fraction(-1, 5)]
    a_of_b = quadratic_substitute([3, 100, 75], s_of_b)
    b0_of_b = quadratic_substitute([4, 11, 6], s_of_b)
    c_of_b = quadratic_substitute([998, 1525, 575], s_of_b)
    d_of_b = quadratic_substitute([81, 123, 46], s_of_b)
    if a_of_b != list(map(Fraction, [-29, 4, 3])):
        raise AssertionError(a_of_b)
    if [100 * value for value in b0_of_b] != list(map(Fraction, [-96, -28, 24])):
        raise AssertionError(b0_of_b)
    if c_of_b != list(map(Fraction, [146, -121, 23])):
        raise AssertionError(c_of_b)
    if [100 * value for value in d_of_b] != list(map(Fraction, [1204, -988, 184])):
        raise AssertionError(d_of_b)
    # Replace b by b'+5 in the adjacent coefficients.
    b_from_b_prime = [Fraction(5), Fraction(1)]
    c_of_b_prime = quadratic_substitute([146, -121, 23], b_from_b_prime)
    d100_of_b_prime = quadratic_substitute([1204, -988, 184], b_from_b_prime)
    if c_of_b_prime != list(map(Fraction, [116, 109, 23])):
        raise AssertionError(c_of_b_prime)
    if d100_of_b_prime != list(map(Fraction, [864, 852, 184])):
        raise AssertionError(d100_of_b_prime)
    phase_substitution_hash = hashlib.sha256(
        repr((a_of_b, b0_of_b, c_of_b_prime, d100_of_b_prime)).encode("ascii")
    ).hexdigest()

    # Exact far coefficient from Item 266's finite-j interval algebra.
    far_terms = [
        Fraction(1, 45), Fraction(2, 35), Fraction(1, 230), Fraction(1, 44),
        Fraction(1, 90), Fraction(11, 2185), Fraction(1, 460), Fraction(1, 1485),
    ]
    far_coefficient = sum(far_terms, Fraction(0))
    if far_coefficient != Fraction(1139587, 9085230):
        raise AssertionError(far_coefficient)

    # Mandatory actual-family nonpropagation witness.
    current_g0, current_g1, current_terminal = g_pair_mod(299, 2399)
    next_g0, next_g1, next_terminal = g_pair_mod(300, 2399)
    if (current_g0, current_g1, current_terminal) != (0, 0, (7, 2392, 0, 0)):
        raise AssertionError((current_g0, current_g1, current_terminal))
    if (next_g0, next_g1) != (2105, 1694):
        raise AssertionError((next_g0, next_g1, next_terminal))
    s_value = 299
    c_value = (575 * s_value * s_value + 1525 * s_value + 998) % 2399
    d_value = (46 * s_value * s_value + 123 * s_value + 81) % 2399
    adjacent_coefficients = (c_value, (-20 * d_value) % 2399)
    if adjacent_coefficients != (966, 128):
        raise AssertionError(adjacent_coefficients)
    if (adjacent_coefficients[0] * next_g0 + adjacent_coefficients[1] * next_g1) % 2399:
        raise AssertionError("adjacent line witness")
    if 2 * 3448 + 1 != 3 * 2399 - 300 or 2399 - 5 * 300 - 4 != 895:
        raise AssertionError("cross-j witness")
    if not (5 * 900 >= 2249 and 5 * 895 >= 3448):
        raise AssertionError("far witness endpoints")

    far_rows, boundary_rows, affected_hash = finite_affected_rows(max_M)

    body: dict[str, Any] = {
        "schema": "item268-cross-b-contiguous-obstruction-certificate-v1",
        "labels": {
            "affected_mass": "PROVED: full far coefficient up to zero-rate boundary",
            "adjacent_identity": "PROVED by exact constant-term telescoping",
            "phase_relocation": "PROVED",
            "degree_le_4_uniqueness": "PROVED only in the explicitly declared linear polynomial ansatz",
            "bounded_replay": "EXACT FINITE ONLY",
            "higher_degree_or_nonlinear_invariant": "OPEN",
            "new_route1_rate": 0,
        },
        "affected_capacity": {
            "exact_per_M": str(far_coefficient),
            "decimal_per_M": format(far_coefficient.numerator / far_coefficient.denominator, ".15f"),
            "boundary": "p=3s+c, c in {3,4,5}; product divides (6M)(6M-1)(6M-2), hence O(log M)",
        },
        "telescoping": {
            "identity": "16(s+1)(2s+3)(a*g0-20*b0*g1)+3(3s+4)(3s+5)(c*g0_next-20*d*g1_next)=0",
            "polynomials": {
                "a": "75s^2+100s+3",
                "b0": "6s^2+11s+4",
                "c": "575s^2+1525s+998",
                "d": "46s^2+123s+81",
            },
            "symbolic_identity_sha256": telescoping_hash,
        },
        "phase_map": {
            "adjacent": "(s,b,r)->(s+1,b-5,r+3 mod 4)",
            "cross_j": "(M,j)->(M+(p-1)/2,j+1)",
            "current_b_functional": "5(3b^2+4b-29)g0-4(6b^2-7b-24)g1",
            "adjacent_b_prime_functional": "5(23b'^2+109b'+116)g0_next-4(46b'^2+213b'+216)g1_next",
            "phase_substitution_sha256": phase_substitution_hash,
        },
        "resultants": {
            "Res(a,b0)": resultant_current,
            "factorization_current": "-3^3*113",
            "Res(c,d)": resultant_adjacent,
            "factorization_adjacent": "2^2*17*23",
        },
        "degree_le_4_ansatz": {
            "matrix_shape": [len(matrix), len(matrix[0])],
            "rank": rank,
            "nullity": 1,
            "primitive_generator": expected_primitive,
            "matrix_sha256": matrix_hash,
            "scope": "linear adjacent identities with four Q[s] coefficients of degree at most 4",
        },
        "mandatory_nonpropagation_witness": {
            "current_row_M_s_p_j_q_b_r": [2249, 299, 2399, 1, 1, 900, 3],
            "current_g0_g1_mod_p": [current_g0, current_g1],
            "current_terminal_mod_p": list(current_terminal),
            "adjacent_row_M_s_p_j_q_b_r": [3448, 300, 2399, 2, 1, 895, 2],
            "adjacent_g0_g1_mod_p": [next_g0, next_g1],
            "adjacent_terminal_mod_p": list(next_terminal),
            "adjacent_line_coefficients_mod_p": list(adjacent_coefficients),
        },
        "finite_affected_replay": {
            "label": "EXACT FINITE ONLY",
            "M_range": [25, max_M],
            "far_rows": far_rows,
            "boundary_rows": boundary_rows,
            "row_sha256": affected_hash,
            "purpose": "verify phase-preserving adjacency and boundary identity; not scan common zeros",
        },
        "height_and_overlap": {
            "cross_layer_height": "log|V_s|=O(s), hence the inherited all-layer product is O(M^2)",
            "dependence": "the adjacent line is exactly proportional to a current-layer linear combination",
            "item149": "first post-Cartier copy already booked; no second booking from the transported line",
            "A1_implication": False,
            "new_rate_booking": 0,
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-M", type=int, default=240)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_M)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "output": str(args.output), "payload_sha256": result["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
