#!/usr/bin/env python3
"""Exact replay for Item 390's fresh primitive-saturation height theorem.

The theorem itself has a p-adic exact-differential proof.  This replay
certifies the only nontrivial real-variable inequality used in its global
height bound, using rational Sturm arithmetic, and cross-checks the two
integral log-residue normalizations by independent exact formulas.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


Poly = list[Fraction]  # coefficients in ascending order


def trim(poly: Poly) -> Poly:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    result = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def divide_with_remainder(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    if denominator == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0) for _ in range(len(numerator) - len(denominator) + 1)]
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] -= coefficient * value
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def evaluate(poly: Poly, point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def sturm_sequence(poly: Poly) -> list[Poly]:
    sequence = [trim(poly), derivative(poly)]
    while sequence[-1] != [0]:
        _, remainder = divide_with_remainder(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append(scale(remainder, Fraction(-1)))
    return sequence


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def signs_and_variations(sequence: list[Poly], point: Fraction) -> tuple[list[int], int]:
    signs = [sign(evaluate(poly, point)) for poly in sequence]
    nonzero = [value for value in signs if value]
    variations = sum(left != right for left, right in zip(nonzero, nonzero[1:]))
    return signs, variations


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def normalized_log_pair_recurrence(m_value: int) -> tuple[int, int]:
    """Scalar recurrence normalization from the frozen large-prime theorem."""
    target = 4 * m_value + 1
    coefficient = [1]
    for degree in range(target):
        rhs = (20 * m_value - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += 2 * (10 * degree + 10 - 20 * m_value) * coefficient[degree - 1]
        if degree >= 2:
            rhs += 4 * (10 * m_value - 5 * degree - 6) * coefficient[degree - 2]
        if degree >= 3:
            rhs += 8 * (degree + 1 - 4 * m_value) * coefficient[degree - 3]
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise ArithmeticError((m_value, degree, rhs, divisor))
        coefficient.append(quotient)
    ell0 = coefficient[target - 1] - 2 * coefficient[target - 2] + 2 * coefficient[target - 3]
    ell1 = coefficient[target]
    return ell0, ell1


def negative_binomial_coefficient(power: int, half_degree: int) -> int:
    """Coefficient magnitude in (1+y^2)^(-power)."""
    return math.comb(power + half_degree - 1, half_degree)


def normalized_log_pair_coefficients(m_value: int) -> tuple[int, int]:
    """Direct coefficient extraction from the two rational functions."""
    target0 = 4 * m_value
    ell0 = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(2):
            residual = target0 - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                ell0 += base * (-1) ** half * negative_binomial_coefficient(4 * m_value + 1, half)

    target1 = 4 * m_value + 1
    ell1 = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(5):
            residual = target1 - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                ell1 += (
                    base
                    * math.comb(4, plus_degree)
                    * (-1) ** half
                    * negative_binomial_coefficient(4 * m_value + 2, half)
                )
    return ell0, ell1


def build_payload() -> dict[str, object]:
    radius = Fraction(541, 1000)
    height_base = 136

    # For c=cos(theta), A=|1-r exp(i theta)|^2 and
    # B=|1+r^2 exp(2 i theta)|^2.
    variable_a = [1 + radius * radius, -2 * radius]
    variable_b = [(1 - radius * radius) ** 2, Fraction(0), 4 * radius * radius]
    positivity_polynomial = add(
        scale(multiply(variable_b, variable_b), height_base * radius**4),
        scale(multiply(multiply(variable_a, variable_a), variable_a), Fraction(-1)),
    )
    sequence = sturm_sequence(positivity_polynomial)
    left_signs, left_variations = signs_and_variations(sequence, Fraction(-1))
    right_signs, right_variations = signs_and_variations(sequence, Fraction(1))
    no_roots = left_variations == right_variations
    positive_witness = evaluate(positivity_polynomial, Fraction(0)) > 0
    endpoint_positive = (
        evaluate(positivity_polynomial, Fraction(-1)) > 0
        and evaluate(positivity_polynomial, Fraction(1)) > 0
    )
    positivity_certified = no_roots and positive_witness and endpoint_positive
    if not positivity_certified:
        raise AssertionError("fixed-circle positivity certificate failed")

    fixed_factor_0 = (1 + radius) / (1 - radius * radius)
    fixed_factor_1 = (1 / radius) * (1 + radius) ** 4 / (1 - radius * radius) ** 2
    if not fixed_factor_0 < 3 or not fixed_factor_1 < 21:
        raise AssertionError("fixed prefactor bound failed")

    normalization_rows = []
    for m_value in range(1, 13):
        recurrence_pair = normalized_log_pair_recurrence(m_value)
        coefficient_pair = normalized_log_pair_coefficients(m_value)
        if recurrence_pair != coefficient_pair:
            raise AssertionError((m_value, recurrence_pair, coefficient_pair))
        normalization_rows.append(
            {
                "m": m_value,
                "lambda0": str(recurrence_pair[0]),
                "lambda1": str(recurrence_pair[1]),
                "gcd": str(math.gcd(abs(recurrence_pair[0]), abs(recurrence_pair[1]))),
            }
        )

    getcontext().prec = 50
    rigorous_rate = Decimal(height_base).ln() / Decimal(6)
    booked_rate = Decimal("0.1365141682948128184504238226")
    threshold = Decimal("1.1561471519642446123307302239")
    inherited_full_content_ceiling = Decimal("1.99566316016")

    generator = Path(__file__)
    return {
        "schema": "item390-mixed-cubic-fresh-primitive-saturation-v1",
        "generator": generator.name,
        "generator_sha256": hashlib.sha256(generator.read_bytes()).hexdigest(),
        "actual_family": {
            "N": "6m",
            "K0": "4m+1",
            "K1": "4m+2",
            "lambda0": "2^(2m) L0",
            "lambda1": "2^(2m+2) L1",
            "fresh_factor": "c_{m,>6m}=product_{p>6m} p^{v_p(c_m)}",
            "saturation_identity": "for every row with (U_m,V_m) nonzero, v_p(c_m)=min(v_p(lambda0),v_p(lambda1)) for every p>6m; frozen saddle nonvanishing covers all sufficiently large m",
            "carrier_identity": "on those rows c_{m,>6m}=(gcd(|lambda0|,|lambda1|))_{>6m}",
        },
        "fixed_circle_certificate": {
            "radius": fraction_text(radius),
            "height_base": height_base,
            "polynomial_definition": "P(c)=136*r^4*((1-r^2)^2+4*r^2*c^2)^2-(1+r^2-2*r*c)^3",
            "polynomial_coefficients_ascending": [fraction_text(value) for value in positivity_polynomial],
            "degree": len(positivity_polynomial) - 1,
            "sturm_length": len(sequence),
            "sturm_degrees": [len(poly) - 1 for poly in sequence],
            "left_endpoint_signs": left_signs,
            "right_endpoint_signs": right_signs,
            "left_variations": left_variations,
            "right_variations": right_variations,
            "real_roots_in_closed_interval": 0,
            "P_at_zero": fraction_text(evaluate(positivity_polynomial, Fraction(0))),
            "P_at_minus_one": fraction_text(evaluate(positivity_polynomial, Fraction(-1))),
            "P_at_plus_one": fraction_text(evaluate(positivity_polynomial, Fraction(1))),
            "positivity_certified": positivity_certified,
            "conclusion": "max_{|z|=r} r^(-4)*|(1-z)^6/(1+z^2)^4| < 136",
        },
        "fixed_prefactors": {
            "lambda0_bound": fraction_text(fixed_factor_0),
            "lambda0_integer_upper": 3,
            "lambda1_bound": fraction_text(fixed_factor_1),
            "lambda1_integer_upper": 21,
            "global_bound": "max(|lambda0|,|lambda1|) < 21*136^m",
        },
        "capacity": {
            "rigorous_large_prime_fresh_ceiling_exact": "log(136)/6",
            "rigorous_large_prime_fresh_ceiling_decimal": str(rigorous_rate),
            "inherited_full_content_ceiling_decimal": str(inherited_full_content_ceiling),
            "component_ceiling_decrease_decimal": str(inherited_full_content_ceiling - rigorous_rate),
            "booked_plus_large_prime_fresh_decimal": str(booked_rate + rigorous_rate),
            "threshold_decimal": str(threshold),
            "remaining_margin_if_only_these_two_sources_decimal": str(threshold - booked_rate - rigorous_rate),
            "route1_booking_delta": "0",
        },
        "normalization_crosscheck": {
            "range": "1<=m<=12",
            "methods": ["scalar integer recurrence", "direct rational coefficient extraction"],
            "all_equal": True,
            "rows": normalization_rows,
            "warning": "The finite rows certify normalization/replay only; they are not a prime-support scan.",
        },
        "scope": {
            "proved": [
                "all-depth primitive saturation at every p>6m on every nonzero row",
                "exact global large-prime carrier on those rows",
                "uniform exponential height ceiling for all sufficiently large rows",
            ],
            "not_proved": [
                "c_{m,>6m}=1",
                "control of undeclared primes p<=6m",
                "a beta matching or multi-parent ceiling",
                "Route 1 closure or irrationality of e+pi",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    rendered = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
