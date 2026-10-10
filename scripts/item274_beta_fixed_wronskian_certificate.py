#!/usr/bin/env python3
"""Deterministic certificate for Item 274's fixed-length determinant no-go.

All computations are exact and standard-library only.  Bounded checks replay
the algebraic identities; no singleton-prime or exceptional-zero scan occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


Poly = tuple[int, ...]  # coefficients in increasing degree
Pair = tuple[Poly, Poly]  # coefficients of (q_N, q_(N+1))


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def p_add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return trim(tuple(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ))


def p_neg(poly: Poly) -> Poly:
    return tuple(-value for value in poly)


def p_sub(left: Poly, right: Poly) -> Poly:
    return p_add(left, p_neg(right))


def p_scale(poly: Poly, scalar: int) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def p_mul(left: Poly, right: Poly) -> Poly:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(tuple(result))


def p_eval(poly: Poly, value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def p_degree(poly: Poly) -> int:
    return len(trim(poly)) - 1


def p_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (0,)
    return trim(tuple(index * poly[index] for index in range(1, len(poly))))


def pair_add(left: Pair, right: Pair) -> Pair:
    return p_add(left[0], right[0]), p_add(left[1], right[1])


def pair_sub(left: Pair, right: Pair) -> Pair:
    return p_sub(left[0], right[0]), p_sub(left[1], right[1])


def pair_scale(left: Pair, scalar: int) -> Pair:
    return p_scale(left[0], scalar), p_scale(left[1], scalar)


def pair_poly_scale(left: Pair, scalar: Poly) -> Pair:
    return p_mul(left[0], scalar), p_mul(left[1], scalar)


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def reverse_bessel(n: int) -> list[int]:
    return [
        math.factorial(2 * n - k) // (math.factorial(k) * math.factorial(n - k))
        for k in range(n + 1)
    ]


def integer_poly_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def integer_poly_sub(left: list[int], right: list[int]) -> list[int]:
    return integer_poly_add(left, [-value for value in right])


def integer_poly_mul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def integer_poly_derivative(poly: list[int]) -> list[int]:
    return [index * poly[index] for index in range(1, len(poly))] or [0]


def integer_poly_eval(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def shift_pairs(radius: int) -> dict[int, Pair]:
    pairs: dict[int, Pair] = {
        0: ((1,), (0,)),
        1: ((0,), (1,)),
    }
    for index in range(1, radius):
        multiplier = (4 * index + 2, 4)  # 4N+4i+2
        pairs[index + 1] = pair_add(pair_poly_scale(pairs[index], multiplier), pairs[index - 1])
    for index in range(0, -radius, -1):
        multiplier = (4 * index + 2, 4)
        pairs[index - 1] = pair_sub(pairs[index + 1], pair_poly_scale(pairs[index], multiplier))
    return pairs


def jet_pairs(window: int, order: int) -> dict[tuple[int, int], Pair]:
    shifts = shift_pairs(window + order + 2)
    jets: dict[tuple[int, int], Pair] = {}
    for index in range(-window - order - 1, window + 1):
        jets[index, 0] = shifts[index]
    for derivative_order in range(order):
        for index in range(-window - order + derivative_order, window + 1):
            jets[index, derivative_order + 1] = pair_add(
                pair_add(jets[index, derivative_order], jets[index - 1, derivative_order]),
                pair_scale(jets[index - 1, derivative_order - 1], -2 * derivative_order)
                if derivative_order
                else ((0,), (0,)),
            )
    return jets


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def determinant_coefficients(matrix: list[list[Pair]]) -> list[Poly]:
    """Coefficients C_k of det(A*F+B*G)=sum C_k F^k G^(s-k)."""
    size = len(matrix)
    coefficients: list[Poly] = [(0,) for _ in range(size + 1)]
    for permutation in itertools.permutations(range(size)):
        term: list[Poly] = [(1,)]
        for row, column in enumerate(permutation):
            a_poly, b_poly = matrix[row][column]
            next_term: list[Poly] = [(0,) for _ in range(len(term) + 1)]
            for f_power, coefficient in enumerate(term):
                next_term[f_power] = p_add(next_term[f_power], p_mul(coefficient, b_poly))
                next_term[f_power + 1] = p_add(next_term[f_power + 1], p_mul(coefficient, a_poly))
            term = next_term
        sign = permutation_sign(permutation)
        for f_power, coefficient in enumerate(term):
            coefficients[f_power] = p_add(coefficients[f_power], p_scale(coefficient, sign))
    return [trim(poly) for poly in coefficients]


def direct_determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    total = 0
    for permutation in itertools.permutations(range(size)):
        product = permutation_sign(permutation)
        for row, column in enumerate(permutation):
            product *= matrix[row][column]
        total += product
    return total


def evaluate_pair(pair: Pair, n: int, f_value: int, g_value: int) -> int:
    return p_eval(pair[0], n) * f_value + p_eval(pair[1], n) * g_value


def check_reverse_bessel(max_n: int) -> dict[str, Any]:
    q = q_values(max_n + 2)
    rows: list[list[int]] = []
    polynomial_checks = 0
    for n in range(1, max_n + 1):
        a_n = reverse_bessel(n)
        a_previous = reverse_bessel(n - 1)
        left = [2 * value for value in integer_poly_derivative(a_n)]
        right = integer_poly_sub(a_n, [0] + a_previous)
        assert left == right
        assert integer_poly_eval(a_n, -1) == q[n]
        assert 2 * integer_poly_eval(integer_poly_derivative(a_n), -1) == q[n] + q[n - 1]
        rows.append([n, q[n], q[n - 1], integer_poly_eval(integer_poly_derivative(a_n), -1)])
        polynomial_checks += 1
    digest = hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    ).hexdigest()
    return {
        "differential_polynomial_identities": polynomial_checks,
        "specialization_identities": 2 * polynomial_checks,
        "row_digest": digest,
        "label": "EXACT FINITE ONLY replay of all-degree coefficient proof",
    }


def check_jet_and_shift_reduction(window: int, order: int) -> dict[str, Any]:
    q = q_values(80)
    pairs = shift_pairs(window + order + 2)
    jets = jet_pairs(window, order)
    shift_checks = 0
    jet_checks = 0
    rows: list[list[Any]] = []
    for n in range(window + order + 2, 55):
        for index in range(-window - order, window + order + 1):
            assert evaluate_pair(pairs[index], n, q[n], q[n + 1]) == q[n + index]
            shift_checks += 1

        jet_values: dict[tuple[int, int], int] = {}
        for index in range(-window - order, window + 1):
            polynomial = reverse_bessel(n + index)
            for derivative_order in range(order + 1):
                if derivative_order:
                    polynomial = integer_poly_derivative(polynomial)
                jet_values[index, derivative_order] = (
                    2**derivative_order * integer_poly_eval(polynomial, -1)
                )
                if (index, derivative_order) in jets:
                    assert evaluate_pair(jets[index, derivative_order], n, q[n], q[n + 1]) == jet_values[index, derivative_order]
                    jet_checks += 1
        for derivative_order in range(order):
            for index in range(-window, window + 1):
                left = jet_values[index, derivative_order + 1]
                right = jet_values[index, derivative_order] + jet_values[index - 1, derivative_order]
                if derivative_order:
                    right -= 2 * derivative_order * jet_values[index - 1, derivative_order - 1]
                assert left == right
                jet_checks += 1
        rows.append([
            n,
            *[p_degree(jets[index, derivative_order][coordinate])
              for index in range(-window, window + 1)
              for derivative_order in range(order + 1)
              for coordinate in (0, 1)],
        ])
    digest = hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    ).hexdigest()
    max_degree = max(
        p_degree(poly)
        for index in range(-window, window + 1)
        for derivative_order in range(order + 1)
        for poly in jets[index, derivative_order]
    )
    assert max_degree <= window + order
    return {
        "window": window,
        "jet_order": order,
        "shift_equalities": shift_checks,
        "jet_equalities": jet_checks,
        "maximum_reduced_polynomial_degree": max_degree,
        "row_digest": digest,
        "label": "EXACT FINITE ONLY replay; general reduction is by the displayed integral recursions",
    }


def check_determinant_expansion() -> dict[str, Any]:
    pairs = shift_pairs(8)
    jets = jet_pairs(3, 3)
    matrices: list[tuple[str, list[list[Pair]]]] = []
    matrices.append((
        "hankel_unit_branch",
        [[pairs[0], pairs[1]], [pairs[1], pairs[2]]],
    ))
    zero: Pair = ((0,), (0,))
    matrices.append((
        "formal_q_squared_branch",
        [[pairs[0], pairs[1]], [zero, pairs[0]]],
    ))
    matrices.append((
        "three_by_three_jet_mix",
        [
            [jets[0, 0], jets[1, 1], pair_add(jets[-1, 2], pair_poly_scale(jets[0, 0], (1, 1)))],
            [jets[1, 0], jets[0, 1], jets[2, 2]],
            [jets[-1, 1], pair_add(jets[0, 2], jets[1, 0]), jets[1, 3]],
        ],
    ))

    q = q_values(75)
    outputs: list[dict[str, Any]] = []
    for name, matrix in matrices:
        coefficients = determinant_coefficients(matrix)
        size = len(matrix)
        equality_checks = 0
        for n in range(8, 60):
            direct = direct_determinant([
                [evaluate_pair(entry, n, q[n], q[n + 1]) for entry in row]
                for row in matrix
            ])
            expanded = sum(
                p_eval(coefficients[power], n)
                * q[n] ** power
                * q[n + 1] ** (size - power)
                for power in range(size + 1)
            )
            assert direct == expanded
            equality_checks += 1
        first_nonzero = next(
            (index for index, coefficient in enumerate(coefficients) if coefficient != (0,)),
            None,
        )
        outputs.append({
            "name": name,
            "size": size,
            "first_nonzero_q_power": first_nonzero,
            "coefficient_degrees": [p_degree(poly) if poly != (0,) else None for poly in coefficients],
            "coefficient_hash": hashlib.sha256(str(coefficients).encode("ascii")).hexdigest(),
            "exact_equality_checks": equality_checks,
        })
    assert outputs[0]["first_nonzero_q_power"] == 0
    assert outputs[1]["first_nonzero_q_power"] == 2
    return {
        "examples": outputs,
        "homogeneity": "degree equals determinant size in (q_N,q_(N+1))",
        "integrality": True,
        "label": "symbolic coefficient construction plus EXACT FINITE ONLY value replay",
    }


def check_pade(max_n: int) -> dict[str, Any]:
    rows: list[list[int]] = []
    for n in range(1, max_n + 1):
        p_poly = reverse_bessel(n)
        q_poly = [(-1) ** index * value for index, value in enumerate(p_poly)]
        wronskian = integer_poly_sub(
            integer_poly_sub(
                integer_poly_mul(integer_poly_derivative(p_poly), q_poly),
                integer_poly_mul(p_poly, integer_poly_derivative(q_poly)),
            ),
            integer_poly_mul(p_poly, q_poly),
        )
        expected = [0] * (2 * n) + [(-1) ** (n + 1)]
        assert wronskian == expected
        q_value = integer_poly_eval(q_poly, 1)
        p_value = integer_poly_eval(p_poly, 1)
        derivative_value = integer_poly_eval(integer_poly_derivative(q_poly), 1)
        assert (p_value * derivative_value - (-1) ** n) % q_value == 0
        assert math.gcd(p_value, q_value) == 1
        assert math.gcd(derivative_value, q_value) == 1
        assert max(abs(value) for value in q_poly) == math.factorial(2 * n) // math.factorial(n)
        rows.append([n, q_value, p_value, derivative_value])
    digest = hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    ).hexdigest()
    return {
        "polynomial_wronskian_checks": max_n,
        "full_modulus_unit_checks": 2 * max_n,
        "coefficient_height_checks": max_n,
        "row_digest": digest,
        "label": "EXACT FINITE ONLY replay of all-degree Padé proof",
    }


def check_overlap_box(limit: int) -> dict[str, Any]:
    checks = 0
    digest_rows: list[list[int]] = []
    for power in range(1, limit + 1):
        for t in range(limit + 1):
            for reservoir in range(limit + 1):
                for extra in range(limit + 1):
                    determinant_valuation = power * t + extra
                    quotient_valuation = determinant_valuation - min(
                        determinant_valuation, power * reservoir
                    )
                    required = power * max(t - reservoir, 0)
                    assert quotient_valuation >= required
                    digest_rows.append([
                        power, t, reservoir, extra,
                        quotient_valuation, required,
                    ])
                    checks += 1
    digest = hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in digest_rows).encode("ascii")
    ).hexdigest()
    return {
        "exponent_box_limit": limit,
        "valuation_inequalities": checks,
        "row_digest": digest,
        "general_identity": "qbar^k divides D/gcd(D,D_m^k) whenever q^k divides D",
        "label": "EXACT FINITE ONLY replay of the primewise algebraic proof",
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item274-beta-fixed-wronskian-certificate-v1",
        "strict_labels": {
            "fixed_jet_two_generator_reduction": "PROVED",
            "fixed_determinant_homogeneous_expansion": "PROVED",
            "singleton_depth_dichotomy": "PROVED SCOPED NO-GO",
            "pade_wronskian": "PROVED UNIT-BRANCH BLINDNESS",
            "clearing_reservoir_deoverlap": "PROVED",
            "uniform_prime_power_height_O_N": "OPEN; NOT PROVED",
            "bounded_checks": "EXACT FINITE ONLY",
            "exceptional_singleton_search": "NONE",
            "positive_linear_capacity_admission": "FAIL",
            "booking": "zero new Route-1 rate and zero new beta capacity reduction",
        },
        "reverse_bessel": check_reverse_bessel(24),
        "jet_and_shift_reduction": check_jet_and_shift_reduction(3, 3),
        "determinant_expansion": check_determinant_expansion(),
        "pade_wronskian": check_pade(16),
        "reservoir_overlap": check_overlap_box(8),
        "theorem": {
            "admissible_class": "fixed determinant size/window/jet order and fixed-degree rational polynomial coefficients after a fixed common denominator",
            "form": "D_N=sum_(k=0)^s C_k(N) q_N^k q_(N+1)^(s-k), C_k in Z[N]",
            "degree_bound": "deg C_k <= s*(d+L+J)",
            "residual_branch": "first coefficient k=0 gives only O_D(log N) log-valuation away from finitely many integer roots",
            "forced_branch": "first coefficient k>=1 gives D_N=q_N^k*E_N; nonzero height is at least q_N^k",
            "deoverlap": "qbar_(m,N)^k divides D_N/gcd(D_N,D_m^k)",
            "scope_limit": "not an impossibility theorem for growing-length auxiliaries, new functions, or every use of a fixed determinant",
        },
        "admission": {
            "target": "v_p(q_N)*log(p)=O(N) uniformly on matching-range primes",
            "target_proved": False,
            "smallest_missing_global_input": "uniform approximation measure for canonical p-adic zeros or a growing-length sub-main-height auxiliary reaching singleton depth",
            "new_capacity_reduction": 0,
        },
        "open": [
            "the uniform O(N) prime-power height target or a sufficient little-oh variant",
            "a growing-length auxiliary with sub-main height and the required local order",
            "uniform rational-integer approximation of the canonical p-adic zeros",
            "the actual moving correlation with the clearing divisor and transverse matching factor",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
