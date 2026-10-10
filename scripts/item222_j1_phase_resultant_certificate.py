#!/usr/bin/env python3
"""Deterministic exact certificate for Item 222.

The checker verifies the all-h phase specialization of Item 218's j=1
eliminant, its integer clearing and unit ledger, a bounded P-recurrence
obstruction, and a declared finite diagonal supercongruence check.
It uses the Python standard library only.
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
    HERE / "item222_j1_phase_resultant_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item222_j1_phase_resultant_certificate.json"
)
RANK_MODULUS = 1_000_000_007


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value, flag in enumerate(flags) if flag]


def convolve(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return answer


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    answer = [1]
    factor = base
    while exponent:
        if exponent & 1:
            answer = convolve(answer, factor)
        exponent >>= 1
        if exponent:
            factor = convolve(factor, factor)
    return answer


def kernel_integer(h_value: int, extra: int) -> list[int]:
    """Coefficients of (1-z)^(2h)(1+z)^extra."""
    answer = []
    for degree in range(2 * h_value + extra + 1):
        value = 0
        for right_degree in range(extra + 1):
            left_degree = degree - right_degree
            if 0 <= left_degree <= 2 * h_value:
                value += (
                    math.comb(extra, right_degree)
                    * (-1) ** left_degree
                    * math.comb(2 * h_value, left_degree)
                )
        answer.append(value)
    return answer


def rising(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def normalized_sum_fraction(
    kernel: list[int], a_value: Fraction, q_value: Fraction, odd: bool
) -> Fraction:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    answer = Fraction(0)
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        numerator = rising(a_value + (1 if odd else 0), t_value)
        denominator = rising(q_value + a_value + (2 if odd else 1), t_value)
        answer += (-1) ** t_value * kernel[degree] * numerator / denominator
    return answer


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def phase_fraction_and_integer(h_value: int) -> tuple[Fraction, dict[str, int]]:
    if h_value < 1 or h_value % 3 == 0:
        raise ValueError("phase specialization requires h>=1 and 3 not dividing h")
    s_phase = Fraction(-(4 * h_value + 3), 6)
    kernel_0 = kernel_integer(h_value, 1)
    kernel_1 = kernel_integer(h_value, 4)
    x_value = normalized_sum_fraction(kernel_0, s_phase, 2 * s_phase, True)
    y_value = normalized_sum_fraction(kernel_0, Fraction(h_value), 2 * s_phase, True)
    u_value = normalized_sum_fraction(kernel_1, s_phase, 2 * s_phase - 1, False)
    v_value = normalized_sum_fraction(kernel_1, Fraction(h_value), 2 * s_phase - 1, True)
    eliminant = (
        Fraction(h_value, 4 * h_value + 3) * x_value * v_value
        + Fraction(9 * (4 * h_value + 1), 2 * (4 * h_value + 3)) * u_value * y_value
    )

    d_x = 3**h_value * product([2 * index + 1 - 4 * h_value for index in range(h_value)])
    d_y = product([3 * index + 3 - h_value for index in range(h_value)])
    d_u = 3 ** (h_value + 2) * product(
        [2 * index - 4 * h_value - 3 for index in range(h_value + 2)]
    )
    d_v = product([3 * index - h_value for index in range(h_value + 1)])
    scaled = {
        "X": x_value * d_x,
        "Y": y_value * d_y,
        "U": u_value * d_u,
        "V": v_value * d_v,
    }
    if any(value.denominator != 1 for value in scaled.values()):
        raise AssertionError((h_value, scaled, "nonintegral clearing"))
    x_integer, y_integer, u_integer, v_integer = (
        int(scaled[name]) for name in ("X", "Y", "U", "V")
    )
    a_integer = (
        2 * h_value * x_integer * v_integer * d_u * d_y
        + 9 * (4 * h_value + 1) * u_integer * y_integer * d_x * d_v
    )
    common_denominator = 2 * (4 * h_value + 3) * d_x * d_y * d_u * d_v
    if eliminant != Fraction(a_integer, common_denominator):
        raise AssertionError((h_value, eliminant, a_integer, common_denominator))
    return eliminant, {
        "A": a_integer,
        "common_denominator": common_denominator,
        "Dx": d_x,
        "Dy": d_y,
        "Du": d_u,
        "Dv": d_v,
        "X": x_integer,
        "Y": y_integer,
        "U": u_integer,
        "V": v_integer,
    }


def kernel_mod(h_value: int, extra: int, prime: int) -> list[int]:
    choose = [1] * (2 * h_value + 1)
    for degree in range(1, 2 * h_value + 1):
        choose[degree] = (
            choose[degree - 1]
            * (2 * h_value - degree + 1)
            * pow(degree, -1, prime)
            % prime
        )
    for degree in range(1, 2 * h_value + 1, 2):
        choose[degree] = -choose[degree] % prime
    return [
        sum(
            math.comb(extra, right_degree) * choose[degree - right_degree]
            for right_degree in range(extra + 1)
            if 0 <= degree - right_degree < len(choose)
        )
        % prime
        for degree in range(2 * h_value + extra + 1)
    ]


def normalized_sum_mod(
    kernel: list[int], a_value: int, q_value: int, odd: bool, prime: int
) -> int:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = 1
    answer = 0
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer = (answer + ratio * kernel[degree]) % prime
        if t_value < maximum_t:
            numerator = a_value + t_value + (1 if odd else 0)
            denominator = q_value + a_value + t_value + (2 if odd else 1)
            ratio = -ratio * numerator * pow(denominator % prime, -1, prime) % prime
    return answer


def phase_mod(h_value: int, prime: int) -> tuple[int, tuple[int, int, int, int]]:
    if h_value % 3 == 0:
        raise ValueError(h_value)
    s_phase = -(4 * h_value + 3) * pow(6, -1, prime) % prime
    kernel_0 = kernel_mod(h_value, 1, prime)
    kernel_1 = kernel_mod(h_value, 4, prime)
    x_value = normalized_sum_mod(kernel_0, s_phase, 2 * s_phase, True, prime)
    y_value = normalized_sum_mod(kernel_0, h_value, 2 * s_phase, True, prime)
    u_value = normalized_sum_mod(kernel_1, s_phase, 2 * s_phase - 1, False, prime)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * s_phase - 1, True, prime)
    eliminant = (
        h_value * pow(4 * h_value + 3, -1, prime) * x_value * v_value
        + 9
        * (4 * h_value + 1)
        * pow(2 * (4 * h_value + 3), -1, prime)
        * u_value
        * y_value
    ) % prime
    return eliminant, (x_value, y_value, u_value, v_value)


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    determinant = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if matrix[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant
        pivot_value = matrix[column][column]
        determinant = determinant * pivot_value % prime
        inverse_pivot = pow(pivot_value, -1, prime)
        for row in range(column + 1, size):
            if matrix[row][column]:
                multiplier = matrix[row][column] * inverse_pivot % prime
                for inner_column in range(column, size):
                    matrix[row][inner_column] = (
                        matrix[row][inner_column]
                        - multiplier * matrix[column][inner_column]
                    ) % prime
    return determinant % prime


def recurrence_obstruction(order: int, degree: int) -> list[dict[str, int]]:
    column_count = (order + 1) * (degree + 1)
    answer = []
    for residue_class in (1, 2):
        values = [
            phase_mod(3 * index + residue_class, RANK_MODULUS)[0]
            for index in range(column_count + order)
        ]
        matrix = [
            [
                pow(index, power, RANK_MODULUS) * values[index + shift] % RANK_MODULUS
                for shift in range(order + 1)
                for power in range(degree + 1)
            ]
            for index in range(column_count)
        ]
        determinant = determinant_mod(matrix, RANK_MODULUS)
        if determinant == 0:
            raise AssertionError((residue_class, "recurrence matrix singular"))
        answer.append(
            {
                "h_mod_3": residue_class,
                "matrix_size": column_count,
                "determinant_mod_1000000007": determinant,
            }
        )
    return answer


def factorial_table(prime: int) -> list[int]:
    answer = [1] * prime
    for value in range(1, prime):
        answer[value] = answer[value - 1] * value % prime
    return answer


def normalized_diagonal_q(prime: int, h_value: int) -> tuple[int, int]:
    factorial = factorial_table(prime)

    def fact(index: int) -> int:
        return factorial[index]

    kernel_0 = kernel_mod(h_value, 1, prime)
    kernel_1 = kernel_mod(h_value, 4, prime)
    x_value = normalized_sum_mod(kernel_0, h_value, 2 * h_value, True, prime)
    y_value = x_value
    u_value = normalized_sum_mod(kernel_1, h_value, 2 * h_value - 1, False, prime)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * h_value - 1, True, prime)
    sign = prime - 1 if h_value % 2 else 1
    a_base = (
        sign
        * fact(2 * h_value)
        * fact(h_value)
        * pow(fact(3 * h_value + 1), -1, prime)
    ) % prime
    b_base = a_base
    c_base = (
        -sign
        * fact(2 * h_value - 1)
        * fact(h_value - 1)
        * pow(fact(3 * h_value - 1), -1, prime)
    ) % prime
    d_base = (
        sign
        * fact(2 * h_value - 1)
        * fact(h_value)
        * pow(fact(3 * h_value), -1, prime)
    ) % prime
    return (
        (2 * a_base * x_value - b_base * y_value) % prime,
        (2 * c_base * u_value - d_base * v_value) % prime,
    )


def diagonal_supercongruence_integer(prime: int, h_value: int) -> int:
    """The coefficient whose p^2 divisibility is equivalent to H1(T)=H1(T+1)."""
    weight = convolve(
        convolve(
            polynomial_power([1, -1], 2 * h_value + 1),
            polynomial_power([1, 1], 4),
        ),
        polynomial_power([1, 0, 1], 2 * h_value - 1),
    )
    target = 8 * h_value + 3
    answer = 0
    for degree, coefficient in enumerate(weight):
        residual = target - degree
        if residual >= 0 and residual % 2 == 0:
            index = residual // 2
            if 0 <= index <= prime:
                answer += coefficient * math.comb(prime, index)
    return answer


def diagonal_finite_check(prime_max: int) -> dict[str, Any]:
    rows = []
    for prime in primes_upto(prime_max):
        if prime < 13 or prime % 10 != 3:
            continue
        h_value = (prime - 3) // 10
        eliminant, components = phase_mod(h_value, prime)
        q0, q1 = normalized_diagonal_q(prime, h_value)
        super_integer = diagonal_supercongruence_integer(prime, h_value)
        super_zero = super_integer % (prime * prime) == 0
        if (eliminant == 0) != super_zero:
            # x is nonzero on the declared finite range, so the exact product
            # reduction makes these equivalent here.
            raise AssertionError((prime, h_value, eliminant, super_zero, components[0]))
        rows.append((prime, h_value, eliminant, q0, q1, int(super_zero)))
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    expected = (77, 40, 37, 40, 0, 0)
    observed = (
        len(rows),
        sum(row[1] % 2 for row in rows),
        sum(1 - row[1] % 2 for row in rows),
        sum(row[2] == 0 for row in rows),
        sum(row[3] == 0 for row in rows),
        sum(row[4] == 0 for row in rows),
    )
    if prime_max == 2000 and observed != expected:
        raise AssertionError((observed, expected))
    return {
        "label": "FINITE; no extrapolation",
        "prime_max": prime_max,
        "rows": len(rows),
        "odd_h_rows": sum(row[1] % 2 for row in rows),
        "even_h_rows": sum(1 - row[1] % 2 for row in rows),
        "eliminant_zero_rows": sum(row[2] == 0 for row in rows),
        "odd_h_eliminant_zero_rows": sum(row[1] % 2 and row[2] == 0 for row in rows),
        "even_h_eliminant_zero_rows": sum(not row[1] % 2 and row[2] == 0 for row in rows),
        "Q0_zero_rows": sum(row[3] == 0 for row in rows),
        "Q1_zero_rows": sum(row[4] == 0 for row in rows),
        "common_Q_zero_rows": sum(row[3] == row[4] == 0 for row in rows),
        "p_squared_supercongruence_rows": sum(row[5] for row in rows),
        "row_sha256": hashlib.sha256(payload).hexdigest(),
        "first_rows": [list(row) for row in rows[:8]],
    }


def certificate(exact_h_max: int, diagonal_prime_max: int) -> dict[str, Any]:
    if exact_h_max < 40 or diagonal_prime_max < 2000:
        raise ValueError("canonical bounds require exact_h_max>=40 and diagonal_prime_max>=2000")
    exact_rows = []
    nonzero_count = 0
    for h_value in range(1, exact_h_max + 1):
        if h_value % 3 == 0:
            continue
        eliminant, integers = phase_fraction_and_integer(h_value)
        if integers["A"]:
            nonzero_count += 1
        exact_rows.append(
            (
                h_value,
                integers["A"],
                integers["common_denominator"],
                eliminant.numerator,
                eliminant.denominator,
            )
        )
    exact_payload = "".join(",".join(map(str, row)) + "\n" for row in exact_rows).encode("ascii")
    recurrence = recurrence_obstruction(order=8, degree=8)
    diagonal = diagonal_finite_check(diagonal_prime_max)

    return {
        "item": 222,
        "arithmetic": "exact integers and fractions plus finite-field rank certificates; Python standard library only",
        "proved_all_h_phase_specialization": {
            "domain": "h>=1 and 3 does not divide h; actual rows have p=6s+4h+3 prime",
            "phase_root": "s_* = -(4h+3)/6, with s congruent to s_* modulo p",
            "formula": "E*_h=h*x*v/(4h+3)+9(4h+1)*u*y/(2(4h+3))",
            "components": {
                "x": "Odd((1-z)^(2h)(1+z); s_*, 2s_*)",
                "y": "Odd((1-z)^(2h)(1+z); h, 2s_*)",
                "u": "Even((1-z)^(2h)(1+z)^4; s_*, 2s_*-1)",
                "v": "Odd((1-z)^(2h)(1+z)^4; h, 2s_*-1)",
            },
            "integer_denominators": {
                "Dx": "3^h product_(i=0)^(h-1)(2i+1-4h)",
                "Dy": "product_(i=0)^(h-1)(3i+3-h)",
                "Du": "3^(h+2) product_(i=0)^(h+1)(2i-4h-3)",
                "Dv": "product_(i=0)^h(3i-h)",
            },
            "integer_eliminant": "A_h=2h*X*V*Du*Dy+9(4h+1)*U*Y*Dx*Dv",
            "exact_relation": "E*_h=A_h/[2(4h+3)DxDyDuDv]",
            "unit_audit": (
                "every linear factor is nonzero with absolute value <p; zeros in Dy or Dv occur only when 3|h, "
                "which makes p>3 composite; 2 and 3 are p-units"
            ),
            "necessary_condition": "every simultaneous j=1 common-log zero satisfies p|A_h",
            "exact_check_h_max": exact_h_max,
            "exact_check_rows": len(exact_rows),
            "exact_check_nonzero_A_rows": nonzero_count,
            "exact_row_sha256": hashlib.sha256(exact_payload).hexdigest(),
            "first_A_values": [{"h": row[0], "A_h": row[1]} for row in exact_rows[:8]],
        },
        "proved_bounded_recurrence_no_go": {
            "sequence": "E*_(3n+1) and E*_(3n+2), reduced modulo 1000000007",
            "ansatz": "sum_(k=0)^r P_k(n) E*_(3(n+k)+c)=0 with r<=8 and deg(P_k)<=8",
            "method": "the maximal 81-column evaluation matrix is square and has nonzero determinant",
            "modulus": RANK_MODULUS,
            "certificates": recurrence,
            "scope": "rules out only this bounded-order, bounded-degree polynomial-coefficient recurrence family",
        },
        "proved_diagonal_reduction": {
            "diagonal": "s=h, p=10h+3",
            "simplification": "x=y, A=B, Q0=A*x, and E=(3h+1)x(v+3u)/(2h)",
            "coefficient": (
                "S_(p,h)=[z^(8h+3)](1-z)^(2h+1)(1+z)^4(1+z^2)^(2h-1+p)"
            ),
            "bridge": "S_(p,h)/p = H1(8h+3)-H1(8h+2) modulo p",
            "consequence": "p^2|S_(p,h) implies E=0; if x is a unit the two conditions are equivalent",
            "open_supercongruence": "for every prime p=10h+3 with odd h, prove p^2|S_(p,h)",
            "open_original_coordinate": "prove x!=0 modulo p (equivalently Q0!=0) on every admissible diagonal prime",
        },
        "finite_diagonal_check": diagonal,
        "height_ledger": {
            "uniform_bound": (
                "with M_h=(h+3)2^(2h+4)(21h)^(h+2), |A_h|<=47h*M_h^4"
            ),
            "asymptotic": "when A_h is nonzero, log|A_h|=O(h log h)",
            "method_consequence": (
                "individual resultant heights summed over h<=m/3 are superlinear and do not bound the j=1 prime-log mass by o(m)"
            ),
            "thin_strip": "h=o(m/log m) has at most o(m) row log-weight, independently of A_h",
        },
        "rate_ledger": {
            "actual_new_usable_coefficient": 0,
            "j1_cell_if_fully_excluded_per_m": "1/6",
            "j1_cell_if_fully_excluded_per_6m": "1/36",
            "reason": "phase localization and scoped recurrence obstruction do not exclude unbounded-h primes",
        },
        "labels": {
            "PROVED": [
                "all-h phase-specialized rational eliminant and integer clearing",
                "complete phase denominator/unit audit",
                "necessary divisibility p|A_h",
                "no recurrence in the declared order<=8, degree<=8 ansatz",
                "exact diagonal reduction to the p^2 coefficient supercongruence",
                "O(h log h) individual height bound and its scoped rate insufficiency",
            ],
            "FINITE": [
                "exact A_h checks through the declared h bound",
                "diagonal parity pattern and original-coordinate nonzeros through the declared prime bound",
            ],
            "OPEN": [
                "the odd-diagonal supercongruence for all primes",
                "all-prime nonvanishing of either original diagonal coordinate",
                "higher-order or higher-degree recurrences for E*_h",
                "a weighted exceptional-prime bound for unbounded h",
                "any positive Route-1 rate gain from j=1",
            ],
        },
        "verdict": (
            "PROVED a uniform all-h phase resultant and a bounded-recurrence/height obstruction; "
            "the exact diagonal reduction isolates an apparent odd-prime supercongruence but it remains OPEN. "
            "No positive Route-1 rate gain is obtained."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-h-max", type=int, default=80)
    parser.add_argument("--diagonal-prime-max", type=int, default=2000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.exact_h_max, args.diagonal_prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "exact_rows": result["proved_all_h_phase_specialization"]["exact_check_rows"],
                "diagonal_rows": result["finite_diagonal_check"]["rows"],
                "recurrence_determinants": result["proved_bounded_recurrence_no_go"]["certificates"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
