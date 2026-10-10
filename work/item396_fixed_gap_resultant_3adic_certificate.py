#!/usr/bin/env python3
"""Exact replay for Item 396's logarithmic gap corridor and height no-go.

Canonical Item 148 already proves the all-gap 3-adic resultant theorem.
This replay independently verifies that inherited input, then records the
new Item-396 consequence: an explicit logarithmically widening exclusion
corridor and a zero-capacity theorem for exponential fixed-gap height
comparisons.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, ROUND_FLOOR, getcontext
from fractions import Fraction
from pathlib import Path


Poly = list[int]  # ascending coefficients


def trim(poly: Poly) -> Poly:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(left: Poly, right: Poly) -> Poly:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_scale(poly: Poly, scalar: int) -> Poly:
    return trim([scalar * value for value in poly])


def poly_multiply(left: Poly, right: Poly) -> Poly:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def poly_evaluate(poly: Poly, value: int) -> int:
    answer = 0
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def poly_shift(poly: Poly, shift: int) -> Poly:
    """Return poly(q+shift), exactly."""
    result = [0]
    for degree, coefficient in enumerate(poly):
        term = [
            coefficient * math.comb(degree, target) * shift ** (degree - target)
            for target in range(degree + 1)
        ]
        result = poly_add(result, term)
    return trim(result)


def linear(constant: int, coefficient: int = 1) -> Poly:
    return [constant, coefficient]


def v3(integer: int) -> int:
    if integer == 0:
        raise ValueError("v3(0)")
    value = abs(integer)
    valuation = 0
    while value % 3 == 0:
        value //= 3
        valuation += 1
    return valuation


def v3_factorial(integer: int) -> int:
    answer = 0
    divisor = 3
    while divisor <= integer:
        answer += integer // divisor
        divisor *= 3
    return answer


def rational_v3(value: Fraction) -> int:
    return v3(value.numerator) - v3(value.denominator)


def rational_unit_mod(value: Fraction, modulus: int = 27) -> int:
    numerator = value.numerator
    denominator = value.denominator
    numerator_power = v3(numerator)
    denominator_power = v3(denominator)
    if numerator_power != denominator_power:
        raise ValueError((value, numerator_power, denominator_power))
    numerator //= 3**numerator_power
    denominator //= 3**denominator_power
    return numerator % modulus * pow(denominator % modulus, -1, modulus) % modulus


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def is_prime_by_trial_division(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1 if divisor == 2 else 2
    return True


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def multiply_truncated(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    answer = [Fraction(0)] * (min(degree, len(left) + len(right) - 2) + 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            if first + second <= degree:
                answer[first + second] += left_value * right_value
    return answer


def generalized_power(
    base: list[Fraction], exponent: Fraction, degree: int
) -> list[Fraction]:
    increment = base[:]
    increment[0] -= 1
    answer = [Fraction(0)] * (degree + 1)
    power = [Fraction(1)]
    for index in range(degree + 1):
        multiplier = generalized_binomial(exponent, index)
        for target, value in enumerate(power):
            answer[target] += multiplier * value
        power = multiply_truncated(power, increment, degree)
    return answer


def full_and_tail(q_value: int, shift: int) -> tuple[Fraction, Fraction]:
    """Frozen exact definitions of C_s(q), T_s(q)."""
    degree = q_value - 1
    m_residue = Fraction(-q_value, 6)
    r_value = 4 * m_residue + shift
    if shift == 0:
        exponent = 2 * m_residue + q_value - 1
        translated = generalized_power(
            [Fraction(1), Fraction(1), Fraction(1, 2)], exponent, degree
        )
        translated = multiply_truncated(translated, [Fraction(2), Fraction(1)], degree)
        adjustment = Fraction(1)

        def low_coefficient(index: int) -> Fraction:
            answer = Fraction(0)
            if index % 2 == 0:
                answer += generalized_binomial(exponent, index // 2)
            if index >= 1 and (index - 1) % 2 == 0:
                answer += generalized_binomial(exponent, (index - 1) // 2)
            return answer

    elif shift == 1:
        exponent = 2 * m_residue + q_value - 2
        translated = generalized_power(
            [Fraction(1), Fraction(1), Fraction(1, 2)], exponent, degree
        )
        translated = multiply_truncated(
            translated,
            [Fraction(math.comb(4, index) * 2 ** (4 - index)) for index in range(5)],
            degree,
        )
        adjustment = Fraction(1, 2)

        def low_coefficient(index: int) -> Fraction:
            return sum(
                Fraction(math.comb(4, first))
                * generalized_binomial(exponent, (index - first) // 2)
                for first in range(5)
                if index >= first and (index - first) % 2 == 0
            )

    else:
        raise ValueError(shift)

    negative_power = generalized_power([Fraction(1), Fraction(1)], -r_value - 1, degree)
    full = multiply_truncated(negative_power, translated, degree)[degree] * adjustment
    tail = Fraction(0)
    for h_value in range(q_value):
        low_index = q_value - 1 - h_value
        tail += low_coefficient(low_index) * generalized_binomial(
            Fraction(-h_value - 1), degree
        )
    return full, tail


# Ratio functions from the relative-precision defect expansion.
C_A = [-9504, 10278, -2103, -524, 75, 18]
C_B = [-162, 405, -669, 314, -57, 9]
T_A = [-288, 1530, -889, -624, 150, 54, 3]
T_B = [216, -102, 227, -12, -30, 18, 3]

C_RATIO_NUM = poly_multiply(poly_multiply([0, 1], [3, 1]), C_A)
C_RATIO_DEN = poly_multiply(poly_multiply(linear(-3, 2), linear(-15, 4)), C_B)
T_RATIO_NUM = poly_multiply([9, 1], T_A)
T_RATIO_DEN = poly_scale(poly_multiply(linear(-3, 2), T_B), 2)


def c_ratio(q_value: int) -> Fraction:
    return Fraction(poly_evaluate(C_RATIO_NUM, q_value), poly_evaluate(C_RATIO_DEN, q_value))


def t_ratio(q_value: int) -> Fraction:
    return Fraction(poly_evaluate(T_RATIO_NUM, q_value), poly_evaluate(T_RATIO_DEN, q_value))


def build_payload() -> dict[str, object]:
    # Symbolic period 18 modulo 27.
    c_period_numerator = poly_add(
        poly_multiply(poly_shift(C_RATIO_NUM, 18), C_RATIO_DEN),
        poly_scale(poly_multiply(C_RATIO_NUM, poly_shift(C_RATIO_DEN, 18)), -1),
    )
    t_period_numerator = poly_add(
        poly_multiply(poly_shift(T_RATIO_NUM, 18), T_RATIO_DEN),
        poly_scale(poly_multiply(T_RATIO_NUM, poly_shift(T_RATIO_DEN, 18)), -1),
    )
    if any(coefficient % 27 for coefficient in c_period_numerator):
        raise AssertionError("C-ratio period identity failed")
    if any(coefficient % 27 for coefficient in t_period_numerator):
        raise AssertionError("T-ratio period identity failed")

    # All denominator factors are 3-adic units for q not divisible by 3.
    denominator_unit_table = []
    for residue in (1, 2):
        c_denominator = poly_evaluate(C_RATIO_DEN, residue) % 3
        t_denominator = poly_evaluate(T_RATIO_DEN, residue) % 3
        if c_denominator == 0 or t_denominator == 0:
            raise AssertionError("ratio denominator is not a 3-adic unit")
        denominator_unit_table.append(
            {
                "q_mod_3": residue,
                "C_ratio_denominator_mod_3": c_denominator,
                "T_ratio_denominator_mod_3": t_denominator,
            }
        )

    representatives = {1: 19, 5: 5, 7: 7, 11: 11, 13: 13, 17: 17}
    residue_rows = []
    for residue, representative in representatives.items():
        c_value = rational_unit_mod(c_ratio(representative))
        t_value = rational_unit_mod(t_ratio(representative))
        difference = (t_value - c_value) % 27
        if difference % 3 != 0 or difference % 9 == 0:
            raise AssertionError((residue, c_value, t_value, difference))
        residue_rows.append(
            {
                "q_mod_18": residue,
                "representative": representative,
                "C1_over_C0_mod_27": c_value,
                "T1_over_T0_mod_27": t_value,
                "difference_mod_27": difference,
                "difference_over_3_mod_9": (difference // 3) % 9,
            }
        )

    # Exact normalization checks against the untruncated coefficient definitions.
    normalization_rows = []
    for q_value in (1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47):
        c0, t0 = full_and_tail(q_value, 0)
        c1, t1 = full_and_tail(q_value, 1)
        resultant = c0 * t1 - c1 * t0
        predicted_valuation = (
            1
            - (q_value - 1)
            - v3_factorial(q_value - 1)
            - (q_value - 1) // 2
            - v3_factorial((q_value - 1) // 2)
        )
        actual_valuation = rational_v3(resultant)
        if actual_valuation != predicted_valuation:
            raise AssertionError((q_value, actual_valuation, predicted_valuation))
        ratio_check = None
        if q_value >= 5:
            exact_c_ratio = c1 / c0
            exact_t_ratio = t1 / t0
            ratio_check = {
                "exact_C_ratio_mod_27": rational_unit_mod(exact_c_ratio),
                "defect_C_ratio_mod_27": rational_unit_mod(c_ratio(q_value)),
                "exact_T_ratio_mod_27": rational_unit_mod(exact_t_ratio),
                "defect_T_ratio_mod_27": rational_unit_mod(t_ratio(q_value)),
            }
            if ratio_check["exact_C_ratio_mod_27"] != ratio_check["defect_C_ratio_mod_27"]:
                raise AssertionError((q_value, "C ratio"))
            if ratio_check["exact_T_ratio_mod_27"] != ratio_check["defect_T_ratio_mod_27"]:
                raise AssertionError((q_value, "T ratio"))
        normalization_rows.append(
            {
                "q": q_value,
                "resultant_nonzero": resultant != 0,
                "actual_v3": actual_valuation,
                "predicted_v3": predicted_valuation,
                "ratio_normalization": ratio_check,
            }
        )

    # Exact radical-carrier minimality witnesses.  A common 2,3-supported
    # denominator is used so that the primitive cubic carriers are integers.
    def cubic_case(q_value: int, prime: int, m_value: int) -> dict[str, object]:
        if prime != 6 * m_value + q_value or not is_prime_by_trial_division(prime):
            raise AssertionError((q_value, prime, m_value))
        c0_value, t0_value = full_and_tail(q_value, 0)
        c1_value, t1_value = full_and_tail(q_value, 1)
        fractions = (c0_value, t0_value, c1_value, t1_value)
        common_denominator = 1
        for value in fractions:
            common_denominator = math.lcm(common_denominator, value.denominator)
        integers = [int(value * common_denominator) for value in fractions]
        c0_integer, t0_integer, c1_integer, t1_integer = integers
        exponent = 2 * m_value + q_value - 1
        x_value = pow(2, exponent, prime)
        k_value = pow(4, q_value - 1, prime)
        reduced = [value % prime for value in integers]
        c0_mod, t0_mod, c1_mod, t1_mod = reduced
        lambda_values = [
            (c0_mod * x_value - t0_mod) % prime,
            (c1_mod * x_value - t1_mod) % prime,
        ]
        cubic_values = [
            (t0_mod**3 - k_value * c0_mod**3) % prime,
            (t1_mod**3 - k_value * c1_mod**3) % prime,
        ]
        rho_value = (c0_mod * t1_mod - c1_mod * t0_mod) % prime
        primitive_cubic_values = []
        for c_integer, t_integer in ((c0_integer, t0_integer), (c1_integer, t1_integer)):
            content = math.gcd(abs(c_integer), abs(t_integer))
            carrier = (t_integer**3 - 4 ** (q_value - 1) * c_integer**3) // content**2
            primitive_cubic_values.append(carrier % prime)
        if [value == 0 for value in cubic_values] != [
            value == 0 for value in primitive_cubic_values
        ]:
            raise AssertionError("primitive cubic normalization changed radical support")
        return {
            "q": q_value,
            "p": prime,
            "m": m_value,
            "common_denominator": common_denominator,
            "C0_T0_C1_T1_mod_p": [
                fraction_mod(c0_value, prime),
                fraction_mod(t0_value, prime),
                fraction_mod(c1_value, prime),
                fraction_mod(t1_value, prime),
            ],
            "cleared_C0_T0_C1_T1_mod_p": reduced,
            "X_mod_p": x_value,
            "K_mod_p": k_value,
            "cleared_lambda0_lambda1_mod_p": lambda_values,
            "cleared_U0_U1_mod_p": cubic_values,
            "primitive_W0_W1_mod_p": primitive_cubic_values,
            "cleared_rho_mod_p": rho_value,
        }

    determinant_only_case = cubic_case(5, 11, 1)
    one_cubic_case = cubic_case(5, 677, 112)
    nonbijective_case = cubic_case(1, 7, 1)
    if determinant_only_case["cleared_rho_mod_p"] != 0 or not all(
        determinant_only_case["cleared_lambda0_lambda1_mod_p"]
    ):
        raise AssertionError("determinant-only witness failed")
    if one_cubic_case["cleared_U0_U1_mod_p"][0] != 0 or one_cubic_case[
        "cleared_lambda0_lambda1_mod_p"
    ][1] == 0:
        raise AssertionError("one-cubic-row witness failed")
    if nonbijective_case["cleared_U0_U1_mod_p"] != [0, 0] or nonbijective_case[
        "cleared_rho_mod_p"
    ] == 0 or nonbijective_case["cleared_lambda0_lambda1_mod_p"] == [0, 0]:
        raise AssertionError("nonbijective two-row witness failed")

    # Deterministic sample rows for the explicit moving corridor.  These are
    # diagnostics for the closed formula; the proof is the monotone exact
    # inequality recorded in the payload and in the report.
    getcontext().prec = 120
    height_base = 62208
    corridor_rows = []
    for decimal_exponent in (20, 50, 100, 200, 500):
        m_value = 10**decimal_exponent
        logarithm_m = Decimal(m_value).ln()
        corridor_real = (
            logarithm_m
            - Decimal(4) * logarithm_m.ln()
            - Decimal(129).ln()
        ) / Decimal(height_base).ln()
        q_bound = int(corridor_real.to_integral_value(rounding=ROUND_FLOOR))
        exact_height = 0 if q_bound < 1 else 129 * q_bound**3 * height_base**q_bound
        if q_bound >= 1 and not exact_height < 6 * m_value:
            raise AssertionError((decimal_exponent, q_bound, exact_height))
        corridor_rows.append(
            {
                "m": f"10^{decimal_exponent}",
                "Q_m": q_bound,
                "top_gap_exact_height_below_6m": q_bound < 1 or exact_height < 6 * m_value,
            }
        )

    generator = Path(__file__)
    return {
        "schema": "item396-logarithmic-gap-corridor-v2",
        "generator": generator.name,
        "generator_sha256": hashlib.sha256(generator.read_bytes()).hexdigest(),
        "provenance": {
            "inherited_input": "Canonical Item 148: uniform nonvanishing and exact v3 valuation of R_q.",
            "no_new_credit_for_item148": True,
            "new_item396_results": [
                "the explicit logarithmically widening fresh-prime exclusion corridor",
                "zero normalized Chebyshev capacity for every fixed-gap carrier used only through an exponential ordinary-height comparison",
            ],
        },
        "theorem": {
            "admissible_gaps": "q>=1 odd and 3 does not divide q",
            "resultant": "R_q=C0(q)T1(q)-C1(q)T0(q)",
            "exact_valuation": "v3(R_q)=1-(q-1)-v3((q-1)!)-(q-1)/2-v3(((q-1)/2)!)",
            "conclusion": "R_q is nonzero for every admissible q",
        },
        "defect_lemma": {
            "precision": "relative modulo 27",
            "C_expansion": "Only terms with h+a<=2 survive after scaling by binom(2alpha,q-1); every omitted term has relative v3>=3.",
            "T_expansion": "Only pole-tail deficits h<=2 survive after scaling by binom(alpha,(q-1)/2); every omitted term has relative v3>=3.",
            "C_ratio_numerator_coefficients_ascending": C_RATIO_NUM,
            "C_ratio_denominator_coefficients_ascending": C_RATIO_DEN,
            "T_ratio_numerator_coefficients_ascending": T_RATIO_NUM,
            "T_ratio_denominator_coefficients_ascending": T_RATIO_DEN,
        },
        "period_certificate": {
            "period": 18,
            "modulus": 27,
            "C_cross_difference_coefficients_divisible_by_27": True,
            "T_cross_difference_coefficients_divisible_by_27": True,
            "C_cross_difference_quotient_coefficients": [
                coefficient // 27 for coefficient in c_period_numerator
            ],
            "T_cross_difference_quotient_coefficients": [
                coefficient // 27 for coefficient in t_period_numerator
            ],
            "denominator_unit_table": denominator_unit_table,
            "residue_rows": residue_rows,
        },
        "normalization_crosscheck": {
            "finite_rows_are_not_the_proof": True,
            "purpose": "Cross-check the symbolic defect normalization against the frozen exact coefficient definitions.",
            "rows": normalization_rows,
        },
        "unconditional_height_corollary": {
            "resultant_numerator_bound": "|num(R_q)|<=129*q^3*62208^q",
            "exclusion": "p=6m+q>129*q^3*62208^q implies p does not divide both lambda0 and lambda1",
            "capacity_proof": [
                "The exclusion inequality is impossible when q>m, because then p<7q<129*q^3*62208^q.",
                "When q<=m, p<=7m, so the inequality forces q<log(7m/129)/log(62208).",
                "There are O(log m) such gaps and each possible prime has log p=O(log m), hence total logarithmic mass O((log m)^2)=o(m).",
            ],
            "normalized_chebyshev_capacity": "0",
        },
        "moving_gap_corridor": {
            "definition": "Q_m=floor((log(m)-4*log(log(m))-log(129))/log(62208)) when the numerator is positive",
            "exact_implication": "Every prime 6m<p<=6m+Q_m does not divide both lambda0 and lambda1.",
            "proof_chain": [
                "For q<=Q_m, 62208^q<=m/(129*(log m)^4).",
                "Positivity of Q_m implies q<log m, hence q^3<=(log m)^3.",
                "Therefore 129*q^3*62208^q<=m/log m<6m<p.",
            ],
            "asymptotic_width": "(log m-4 log log m+O(1))/log(62208)",
            "diagnostic_rows": corridor_rows,
        },
        "method_class_no_go": {
            "hypothesis": "A nonzero carrier N_q has |N_q|<=A*q^C*B^q with A>0, C>=0, B>1, and exclusions use only p>A*q^C*B^q.",
            "conclusion": "At row m the height comparison can operate only on O(log m) gaps, apart from finitely many q.",
            "weighted_mass": "O((log m)^2)=o(m)",
            "normalized_chebyshev_capacity": "0",
        },
        "primitive_cubic_radical_carrier": {
            "bijective_class": "q congruent to 5 mod 6, hence p congruent to 2 mod 3",
            "definition": "After a common 2,3-supported clearing c_s=D*C_s, t_s=D*T_s and g_s=gcd(c_s,t_s), W_s=(t_s^3-4^(q-1)c_s^3)/g_s^2.",
            "theorem": "For each s, p divides actual lambda_s iff p divides W_s; hence common actual support equals p|gcd(W0,W1). This is radical/first-digit only.",
            "proof": "X^3=4^(q-1) mod p and cubing is an automorphism of F_p; dividing by g_s^2 leaves one copy of any common p-content.",
            "sharp_boundary": "For q congruent to 1 mod 6, the two cubic rows can select distinct cube roots, so rho is additionally necessary.",
            "minimality_witnesses": {
                "determinant_alone_fails": determinant_only_case,
                "one_cubic_row_alone_fails": one_cubic_case,
                "two_cubic_rows_fail_in_nonbijective_class": nonbijective_case,
            },
        },
        "scope": {
            "proved": [
                "logarithmically widening fresh-prime exclusion corridor",
                "zero capacity of the exponential-height-only fixed-gap carrier method class",
                "minimal primitive cubic radical carrier in each admissible mod-6 class",
                "independent replay of inherited Item-148 all-gap nonvanishing, with no new credit",
            ],
            "not_proved": [
                "the final power-of-two congruence at candidate divisors of R_q",
                "c_{m,>6m}=1",
                "weighted zero density for all moving gaps",
                "a Route-1 booking or irrationality of e+pi",
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
