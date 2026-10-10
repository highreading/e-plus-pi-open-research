#!/usr/bin/env python3
"""Deterministic exact replay for Item 423.

The report extends Item 420 from constant coordinate combinations to every
same-index combination with fixed polynomial coefficients in m.  The
analytic saddle lemma is stated and proved in the report.  This replay pins
its canonical/work dependencies and certifies the exact algebraic facts
that prevent the only possible second cancellation: the integration-by-
parts identity, the critical-point ratio polynomial, and its negative
discriminant.  It also checks exact coefficient rows and the unchanged
capacity arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


Poly = list[Fraction]  # ascending coefficients


DEPENDENCIES = {
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_certificate.json":
        "bcea1e6be723e48e3d1ca63bc5644b208059e5138799108ea403b0ba5d789075",
    "sources/item420_normalized_contour_extension_report.md":
        "eebbcd02c654d6be1ca6ae50e427931abc16aae773300b4d1f32dc8f2291a414",
    "results/item420_normalized_contour_extension_certificate.json":
        "ddac30da2c3c7ebca84cce7c412f99c05b6d6281a5598c2346f33b50efe18095",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(poly: Poly) -> Poly:
    answer = poly[:]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left: Poly, right: Poly) -> Poly:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(poly: Poly, scalar: Fraction | int) -> Poly:
    return trim([Fraction(scalar) * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def power(poly: Poly, exponent: int) -> Poly:
    answer: Poly = [Fraction(1)]
    base = poly[:]
    value = exponent
    while value:
        if value & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        value //= 2
    return answer


def derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def divide_with_remainder(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    if denominator == [0]:
        raise ZeroDivisionError
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] -= coefficient * value
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    size = len(work)
    answer = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        pivot_value = work[column][column]
        answer *= pivot_value
        for entry in range(column, size):
            work[column][entry] /= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor:
                for entry in range(column, size):
                    work[row][entry] -= factor * work[column][entry]
    return answer


def resultant(left: Poly, right: Poly) -> Fraction:
    left = trim(left)
    right = trim(right)
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    matrix = [[Fraction(0)] * size for _ in range(size)]
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    for row in range(right_degree):
        for index, value in enumerate(left_descending):
            matrix[row][row + index] = value
    for local_row in range(left_degree):
        row = right_degree + local_row
        for index, value in enumerate(right_descending):
            matrix[row][local_row + index] = value
    return determinant(matrix)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def negative_binomial(power_value: int, half_degree: int) -> int:
    return math.comb(power_value + half_degree - 1, half_degree)


def lambda_pair(m_value: int) -> tuple[int, int]:
    target_zero = 4 * m_value
    lambda_zero = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(2):
            residual = target_zero - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                lambda_zero += base * (-1) ** half * negative_binomial(4 * m_value + 1, half)

    target_one = 4 * m_value + 1
    lambda_one = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(5):
            residual = target_one - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                lambda_one += (
                    base
                    * math.comb(4, plus_degree)
                    * (-1) ** half
                    * negative_binomial(4 * m_value + 2, half)
                )
    return lambda_zero, lambda_one


def q_constant_term(m_value: int) -> int:
    target = 4 * m_value + 1
    raw = 0
    q_terms = {0: -1, 2: -4, 4: 1}
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for q_degree, q_coefficient in q_terms.items():
            residual = target - numerator_degree - q_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                raw += (
                    base
                    * q_coefficient
                    * (-1) ** half
                    * negative_binomial(4 * m_value + 2, half)
                )
    if raw % 2:
        raise AssertionError((m_value, raw))
    return raw // 2


def ratio_resultant() -> dict[str, object]:
    # P is the critical polynomial.  At P(y)=0,
    # t=q(y)/f0(y)=(y^4-4y^2-1)/(2y(1+y^2)(1+y)).
    critical: Poly = [Fraction(-2), Fraction(-1), Fraction(-6), Fraction(3)]
    ratio_numerator: Poly = [Fraction(-1), Fraction(0), Fraction(-4), Fraction(0), Fraction(1)]
    ratio_denominator = multiply(
        scale([Fraction(0), Fraction(1)], 2),
        multiply([Fraction(1), Fraction(0), Fraction(1)], [Fraction(1), Fraction(1)]),
    )

    # Interpolate Res_y(P, numerator-t*denominator), a cubic in t, from
    # four exact evaluations.  The target identity fixes the normalization.
    target: Poly = [Fraction(176), Fraction(-3520), Fraction(6400), Fraction(-5120)]
    evaluations: dict[str, str] = {}
    for t_value in range(4):
        right = add(ratio_numerator, scale(ratio_denominator, -t_value))
        observed = resultant(critical, right)
        expected = sum(target[index] * Fraction(t_value) ** index for index in range(4))
        if observed != expected:
            raise AssertionError((t_value, observed, expected))
        evaluations[str(t_value)] = fraction_text(observed)

    # target=-16*(320t^3-400t^2+220t-11).
    normalized: Poly = [Fraction(-11), Fraction(220), Fraction(-400), Fraction(320)]
    if target != scale(normalized, -16):
        raise AssertionError("resultant normalization")
    a, b, c, d = [int(value) for value in reversed(normalized)]
    discriminant = (
        b * b * c * c
        - 4 * a * c * c * c
        - 4 * b * b * b * d
        - 27 * a * a * d * d
        + 18 * a * b * c * d
    )
    if discriminant != -3_460_300_800:
        raise AssertionError(discriminant)

    # Neither the ratio numerator nor denominator vanishes at a critical
    # point.  This also prevents degree loss in the resultant map.
    numerator_resultant = resultant(critical, ratio_numerator)
    denominator_resultant = resultant(critical, ratio_denominator)
    if numerator_resultant != 176 or denominator_resultant != 5120:
        raise AssertionError((numerator_resultant, denominator_resultant))

    return {
        "critical_polynomial_coefficients_ascending": [fraction_text(value) for value in critical],
        "ratio": "q/f0=(y^4-4y^2-1)/(2y(1+y^2)(1+y))",
        "resultant_identity": "Res_y(P,q_numerator-t*q_denominator)=-16*(320t^3-400t^2+220t-11)",
        "exact_resultant_checks_t_0_to_3": evaluations,
        "normalized_ratio_polynomial_coefficients_ascending": [fraction_text(value) for value in normalized],
        "normalized_ratio_polynomial_discriminant": str(discriminant),
        "resultant_P_ratio_numerator": fraction_text(numerator_resultant),
        "resultant_P_ratio_denominator": fraction_text(denominator_resultant),
        "conclusion": "the ratio q(alpha)/f0(alpha) at either dominant nonreal critical point is nonreal",
    }


def exact_rows() -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    examples = [
        ([Fraction(1)], [Fraction(0)]),
        ([Fraction(0)], [Fraction(1)]),
        ([Fraction(-5)], [Fraction(2)]),
        ([Fraction(1), Fraction(-5)], [Fraction(0), Fraction(2)]),
        ([Fraction(7), Fraction(3), Fraction(-10)], [Fraction(-2), Fraction(4)]),
    ]
    for m_value in range(1, 25):
        lambda_zero, lambda_one = lambda_pair(m_value)
        difference = 2 * lambda_one - 5 * lambda_zero
        q_value = q_constant_term(m_value)
        if q_value != m_value * difference:
            raise AssertionError((m_value, q_value, difference))
        example_values = []
        for a_poly, b_poly in examples:
            a_value = sum(value * m_value**index for index, value in enumerate(a_poly))
            b_value = sum(value * m_value**index for index, value in enumerate(b_poly))
            direct = a_value * lambda_zero + b_value * lambda_one
            s_value = a_value + Fraction(5, 2) * b_value
            decomposed = s_value * lambda_zero + Fraction(1, 2) * b_value * difference
            if direct != decomposed or direct.denominator != 1:
                raise AssertionError((m_value, a_poly, b_poly))
            example_values.append(str(direct.numerator))
        rows.append({
            "m": m_value,
            "lambda0": str(lambda_zero),
            "lambda1": str(lambda_one),
            "D=2lambda1-5lambda0": str(difference),
            "CT(qH^m)": str(q_value),
            "five_polynomial_combination_values": example_values,
        })
    return rows


def capacity() -> dict[str, str]:
    root = Path(__file__).resolve().parents[1]
    item418 = json.loads(
        (root / "results/item418_normalized_large_carrier_certificate.json").read_text(encoding="utf-8")
    )
    inherited = item418["capacity"]
    getcontext().prec = 80
    rho = Decimal(inherited["rho_star_decimal"])
    forced = Decimal(inherited["forced_Item200_rate_per_m"])
    normalized_base = rho / forced.exp()
    ceiling = normalized_base.ln() / Decimal(6)
    if abs(ceiling - Decimal(inherited["Item418_sharp_circular_component_ceiling"])) > Decimal("1e-70"):
        raise AssertionError("capacity mismatch")
    return {
        "rho_star": str(rho),
        "forced_C_F_per_m": str(forced),
        "normalized_polynomial_combination_root_base": str(normalized_base),
        "unchanged_strictly_large_component_ceiling": str(ceiling),
        "component_ceiling_delta": "0",
        "booked_lower_bound_delta": "0",
        "global_total_content_ceiling_delta": "0",
        "frozen_deficit_delta": "0",
    }


def build_payload() -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    dependencies: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        observed = sha256(root / relative)
        if observed != expected:
            raise AssertionError((relative, observed, expected))
        dependencies[relative] = observed

    ratio = ratio_resultant()
    rows = exact_rows()
    capacity_record = capacity()
    core = {
        "ratio_resultant": ratio,
        "capacity": capacity_record,
        "leading_degree_trichotomy": {
            "definition": "S=A+5B/2; s=deg S, b=deg B",
            "s>b-1": "lambda0 saddle dominates",
            "s<b-1": "D saddle dominates",
            "s=b-1": "leading amplitude is f0(alpha)*(lead(S)+lead(B)*q(alpha)/(2f0(alpha))); it cannot vanish because the ratio is nonreal",
        },
    }
    witness_sha = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return {
        "schema": "item423-polynomial-bezout-no-go-v1",
        "item": 423,
        "status": "ROOT_AUDITED_CANONICAL_SCOPED_BEZOUT_HEIGHT_NO_GO_NO_BOOKING",
        "generator": Path(__file__).name,
        "generator_sha256": sha256(Path(__file__)),
        "dependency_sha256": dependencies,
        "exact_ratio_resultant": ratio,
        "exact_coefficient_rows": rows,
        "capacity": capacity_record,
        "theorem_pinned_to_report": {
            "statement": "for every nonzero pair A,B in Q[m], limsup |A(m)lambda0,m+B(m)lambda1,m|^(1/m)=rho_star",
            "normalized_statement": "after clearing one fixed denominator, the corresponding integer combination of mu0,m and mu1,m has limsup root rho_star*exp(-C_F)",
            "scope": "same-index fixed-degree polynomial Bezout combinations only; no claim for shifts, growing degree, adaptive coefficients, resultants of two combinations, or the gcd itself",
        },
        "strict_claims": {
            "PROVED": [
                "the unique first saddle cancellation extends exactly through D=2lambda1-5lambda0=CT(qH^m)/m",
                "q(alpha)/f0(alpha) is nonreal at the dominant saddles",
                "every nonzero same-index polynomial-coefficient combination retains root base rho_star",
                "normalization by F_m gives root base rho_star*exp(-C_F)",
                "zero component-ceiling, booking, global-ceiling, and deficit delta",
            ],
            "SCOPED_NO_GO": [
                "bounded-degree polynomial-in-m Bezout coefficients cannot improve Item418 by ordinary absolute height of one combination",
            ],
            "OPEN": [
                "the actual normalized gcd and weighted zero density",
                "growing-degree or adaptive low-height coefficients",
                "joint two-combination resultants or subresultants",
                "shift recurrences and finite-field common-zero structure",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "witness_sha256": witness_sha,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--replay", type=Path)
    arguments = parser.parse_args()
    payload = (json.dumps(build_payload(), indent=2, sort_keys=True) + "\n").encode("utf-8")
    if arguments.replay is not None and arguments.replay.read_bytes() != payload:
        raise SystemExit("replay mismatch")
    arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
