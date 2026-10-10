#!/usr/bin/env python3
"""Exact identities and sharply labelled diagnostics for two cubic kernels.

The proved part is rational arithmetic.  Floating-point saddle and primitive-form
tables are diagnostics only; the accompanying note states the boundary precisely.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from math import comb, gcd, lcm
from pathlib import Path

import mpmath as mp
import sympy as sp


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction())


def cross(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]


def determinant(rows: list[list[Fraction]]) -> Fraction:
    return dot(rows[0], cross(rows[1], rows[2]))


def primitive_pair(first: Fraction, second: Fraction) -> tuple[int, int, int, int]:
    denominator = lcm(first.denominator, second.denominator)
    p_value = first.numerator * (denominator // first.denominator)
    q_value = second.numerator * (denominator // second.denominator)
    content = gcd(abs(p_value), abs(q_value))
    if content == 0:
        content = 1
    return p_value // content, q_value // content, denominator, content


# ---------------------------------------------------------------------------
# Q(x)=1+x^3.


def cubic_base_polynomial_integral(exponent: int) -> Fraction:
    quotient, residue = divmod(exponent, 3)
    total = Fraction()
    for offset in range(quotient):
        degree = 3 * (quotient - 1 - offset) + residue
        total += Fraction((-1) ** offset, degree + 1)
    return total


def cubic_monomial_reduction(exponent: int, power: int) -> tuple[Fraction, Fraction, int]:
    """Return rational endpoint, base-period scale, and residue modulo three."""
    endpoint = Fraction()
    scale = Fraction(1)
    for level in range(power, 1, -1):
        endpoint += scale * Fraction(1, 3 * (level - 1) * 2 ** (level - 1))
        scale *= Fraction(3 * (level - 1) - exponent - 1, 3 * (level - 1))
    quotient, residue = divmod(exponent, 3)
    endpoint += scale * cubic_base_polynomial_integral(exponent)
    scale *= (-1) ** quotient
    return endpoint, scale, residue


def cubic_coordinates(n_value: int, power: int) -> tuple[Fraction, Fraction, Fraction]:
    """J=R+(L/3)log(2)+(E/(3 sqrt(3)))pi for Q=1+x^3."""
    rational = Fraction()
    periods = [Fraction(), Fraction(), Fraction()]
    for offset in range(n_value + 1):
        coefficient = Fraction((-1) ** offset * comb(n_value, offset))
        endpoint, scale, residue = cubic_monomial_reduction(n_value + offset, power)
        rational += coefficient * endpoint
        periods[residue] += coefficient * scale
    logarithmic = periods[0] - periods[1] + periods[2]
    pi_sqrt_coordinate = periods[0] + periods[1]
    return rational, logarithmic, pi_sqrt_coordinate


def cubic_field_collapse_record(n_value: int, power: int) -> dict[str, object]:
    data = [cubic_coordinates(n_value, power + shift) for shift in range(3)]
    rational = [entry[0] for entry in data]
    logarithmic = [entry[1] for entry in data]
    pi_sqrt = [entry[2] for entry in data]
    u_vector = cross(logarithmic, pi_sqrt)
    v_vector = cross(logarithmic, rational)
    det_value = determinant([logarithmic, pi_sqrt, rational])
    return {
        "n": n_value,
        "k": power,
        "determinant": str(det_value),
        "u_dot_L": str(dot(u_vector, logarithmic)),
        "u_dot_E": str(dot(u_vector, pi_sqrt)),
        "u_dot_R": str(dot(u_vector, rational)),
        "v_dot_L": str(dot(v_vector, logarithmic)),
        "v_dot_R": str(dot(v_vector, rational)),
        "v_dot_E": str(dot(v_vector, pi_sqrt)),
        "predicted_uR": str(det_value),
        "predicted_vE": str(-det_value),
    }


# ---------------------------------------------------------------------------
# Q(x)=(1+x)(1+x^2)=1+x+x^2+x^3.


def trim(polynomial: list[Fraction]) -> list[Fraction]:
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def poly_add(
    left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)
) -> list[Fraction]:
    output = [Fraction()] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += scale * value
    return trim(output)


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction()] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return trim(output)


def poly_derivative(polynomial: list[Fraction]) -> list[Fraction]:
    return [Fraction(index) * polynomial[index] for index in range(1, len(polynomial))] or [Fraction()]


def mixed_divmod_q(polynomial: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Divide by the monic polynomial 1+x+x^2+x^3."""
    remainder = polynomial[:]
    quotient = [Fraction()] * max(1, len(remainder) - 3)
    while len(remainder) >= 4:
        shift = len(remainder) - 4
        leading = remainder[-1]
        quotient[shift] = leading
        for index in range(4):
            remainder[shift + index] -= leading
        trim(remainder)
    return trim(quotient), trim(remainder)


def mixed_remainder(polynomial: list[Fraction]) -> list[Fraction]:
    return mixed_divmod_q(polynomial)[1]


def poly_evaluate(polynomial: list[Fraction], value: Fraction) -> Fraction:
    output = Fraction()
    for coefficient in reversed(polynomial):
        output = output * value + coefficient
    return output


MIXED_Q = [Fraction(1)] * 4
MIXED_Q_PRIME = [Fraction(1), Fraction(2), Fraction(3)]
MIXED_Q_PRIME_INVERSE = [Fraction(), Fraction(-1, 4), Fraction(1, 4)]


def mixed_coordinates(n_value: int, power: int) -> tuple[Fraction, Fraction, Fraction]:
    """H=R+(L/4)log(2)+(E/8)pi for Q=(1+x)(1+x^2)."""
    numerator = [Fraction()] * n_value + [
        Fraction((-1) ** offset * comb(n_value, offset))
        for offset in range(n_value + 1)
    ]
    rational = Fraction()
    for level in range(power, 1, -1):
        reduced = mixed_remainder(numerator)
        primitive = mixed_remainder(poly_mul(reduced, MIXED_Q_PRIME_INVERSE))
        primitive = [-value / Fraction(level - 1) for value in primitive]
        lowered_numerator = poly_add(
            numerator, poly_mul(poly_derivative(primitive), MIXED_Q), Fraction(-1)
        )
        lowered_numerator = poly_add(
            lowered_numerator,
            poly_mul(primitive, MIXED_Q_PRIME),
            Fraction(level - 1),
        )
        numerator, remainder = mixed_divmod_q(lowered_numerator)
        if remainder != [0]:
            raise AssertionError((n_value, power, level, remainder))
        # Q(1)=4 and Q(0)=1.
        rational += poly_evaluate(primitive, Fraction(1)) / 4 ** (level - 1)
        rational -= poly_evaluate(primitive, Fraction())

    polynomial_part, remainder = mixed_divmod_q(numerator)
    rational += sum(
        (coefficient / Fraction(index + 1) for index, coefficient in enumerate(polynomial_part)),
        Fraction(),
    )
    remainder += [Fraction()] * (3 - len(remainder))
    a_value, b_value, c_value = remainder[:3]
    logarithmic = a_value - b_value + 3 * c_value
    pi_coordinate = a_value + b_value - c_value
    return rational, logarithmic, pi_coordinate


def mixed_log_cancel_form(n_value: int, power: int) -> dict[str, object]:
    first = mixed_coordinates(n_value, power)
    second = mixed_coordinates(n_value, power + 1)
    rational = second[1] * first[0] - first[1] * second[0]
    pi_coefficient = (second[1] * first[2] - first[1] * second[2]) / 8
    p_value, q_value, denominator, content = primitive_pair(rational, pi_coefficient)
    return {
        "n": n_value,
        "k": power,
        "R0": str(first[0]),
        "L0": str(first[1]),
        "E0": str(first[2]),
        "R1": str(second[0]),
        "L1": str(second[1]),
        "E1": str(second[2]),
        "A": str(rational),
        "B": str(pi_coefficient),
        "primitive_p": p_value,
        "primitive_q": q_value,
        "pair_lcm_denominator": denominator,
        "pair_content_before_primitive_reduction": content,
    }


def symbolic_checks() -> dict[str, bool]:
    x_value, exponent, level = sp.symbols("x m j")
    cubic_common_numerator = sp.expand(
        3 * (level - 1)
        - ((exponent + 1) * (1 + x_value**3) - 3 * (level - 1) * x_value**3)
        - (3 * level - exponent - 4) * (1 + x_value**3)
    )
    mixed_q = 1 + x_value + x_value**2 + x_value**3
    inverse_identity = sp.rem(
        sp.diff(mixed_q, x_value) * (x_value**2 - x_value) / 4,
        mixed_q,
        domain=sp.QQ,
    )
    return {
        "cubic_monomial_lowering_identity": cubic_common_numerator == 0,
        "mixed_Qprime_inverse_mod_Q": sp.expand(inverse_identity - 1) == 0,
        "mixed_Q_at_one_is_four": mixed_q.subs(x_value, 1) == 4,
    }


def numerical_integral_checks() -> list[dict[str, object]]:
    mp.mp.dps = 80
    output = []
    for n_value, power in ((4, 3), (6, 5), (8, 6), (12, 9)):
        cubic = cubic_coordinates(n_value, power)
        cubic_formula = (
            mp.mpf(cubic[0].numerator) / cubic[0].denominator
            + (mp.mpf(cubic[1].numerator) / cubic[1].denominator) * mp.log(2) / 3
            + (mp.mpf(cubic[2].numerator) / cubic[2].denominator)
            * mp.pi
            / (3 * mp.sqrt(3))
        )
        cubic_integral = mp.quad(
            lambda value: value**n_value
            * (1 - value) ** n_value
            / (1 + value**3) ** power,
            [0, 1],
        )
        mixed = mixed_coordinates(n_value, power)
        mixed_formula = (
            mp.mpf(mixed[0].numerator) / mixed[0].denominator
            + (mp.mpf(mixed[1].numerator) / mixed[1].denominator) * mp.log(2) / 4
            + (mp.mpf(mixed[2].numerator) / mixed[2].denominator) * mp.pi / 8
        )
        mixed_integral = mp.quad(
            lambda value: value**n_value
            * (1 - value) ** n_value
            / (1 + value + value**2 + value**3) ** power,
            [0, 1],
        )
        output.append(
            {
                "n": n_value,
                "k": power,
                "cubic_absolute_error": mp.nstr(abs(cubic_formula - cubic_integral), 8),
                "mixed_absolute_error": mp.nstr(abs(mixed_formula - mixed_integral), 8),
            }
        )
    return output


def saddle_record(kappa_value: float) -> dict[str, object]:
    mp.mp.dps = 60
    kappa = mp.mpf(kappa_value)
    mixed_q = lambda value: (1 + value) * (1 + value**2)
    head_phase = lambda value: (
        mp.log(value) + mp.log(1 - value) - kappa * mp.log(mixed_q(value))
    )
    tail_phase = lambda value: (
        (3 * kappa - 2) * mp.log(value)
        + mp.log(1 - value)
        - kappa * mp.log(mixed_q(value))
    )
    head_derivative = lambda value: (
        1 / value
        - 1 / (1 - value)
        - kappa * (1 + 2 * value + 3 * value**2) / mixed_q(value)
    )
    endpoint_epsilon = mp.mpf("1e-40")
    head_saddle = mp.findroot(
        head_derivative,
        (endpoint_epsilon, 1 - endpoint_epsilon),
        solver="bisect",
        tol=mp.mpf("1e-45"),
    )
    head_rate = head_phase(head_saddle)
    if abs(3 * kappa - 2) < mp.mpf("1e-12"):
        tail_saddle = mp.mpf(0)
        tail_rate = mp.mpf(0)
    else:
        tail_derivative = lambda value: (
            (3 * kappa - 2) / value
            - 1 / (1 - value)
            - kappa * (1 + 2 * value + 3 * value**2) / mixed_q(value)
        )
        tail_saddle = mp.findroot(
            tail_derivative,
            (endpoint_epsilon, 1 - endpoint_epsilon),
            solver="bisect",
            tol=mp.mpf("1e-45"),
        )
        tail_rate = tail_phase(tail_saddle)
    return {
        "kappa": mp.nstr(kappa, 20),
        "head_saddle": mp.nstr(head_saddle, 20),
        "head_rate": mp.nstr(head_rate, 20),
        "tail_saddle_after_inversion": mp.nstr(tail_saddle, 20),
        "tail_rate": mp.nstr(tail_rate, 20),
        "raw_head_minus_tail_log_rate_not_a_period_form_rate": mp.nstr(
            head_rate - tail_rate, 20
        ),
    }


def boundary_diagnostics(max_n: int) -> list[dict[str, object]]:
    mp.mp.dps = max(120, max_n * 2)
    output = []
    for n_value in range(6, max_n + 1, 6):
        power = 2 * n_value // 3 + 1
        record = mixed_log_cancel_form(n_value, power)
        p_value = int(record["primitive_p"])
        q_value = int(record["primitive_q"])
        form = abs(mp.mpf(p_value) + mp.mpf(q_value) * mp.pi)
        normalized = abs(mp.pi + mp.mpf(p_value) / q_value)
        record.update(
            {
                "log_abs_primitive_form_over_n": mp.nstr(mp.log(form) / n_value, 18),
                "log_abs_normalized_error_over_n": mp.nstr(
                    mp.log(normalized) / n_value, 18
                ),
                "log_abs_q_over_n": mp.nstr(mp.log(abs(q_value)) / n_value, 18),
                "primitive_pair_max_bits": max(
                    abs(p_value).bit_length(), abs(q_value).bit_length()
                ),
            }
        )
        output.append(record)
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "cubic_and_mixed_cubic_kernel_certificate.json",
    )
    parser.add_argument("--boundary-max-n", type=int, default=60)
    args = parser.parse_args()

    symbolic = symbolic_checks()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    field_records = [cubic_field_collapse_record(n, 2 * n // 3 + 1) for n in (6, 12, 18)]
    for record in field_records:
        if (
            record["u_dot_L"] != "0"
            or record["u_dot_E"] != "0"
            or record["v_dot_L"] != "0"
            or record["v_dot_R"] != "0"
            or record["u_dot_R"] != record["predicted_uR"]
            or record["v_dot_E"] != record["predicted_vE"]
        ):
            raise AssertionError(record)
    numerical = numerical_integral_checks()
    if any(
        mp.mpf(record[key]) > mp.mpf("1e-65")
        for record in numerical
        for key in ("cubic_absolute_error", "mixed_absolute_error")
    ):
        raise AssertionError(numerical)

    result = {
        "schema": "cubic-and-mixed-cubic-kernel-v1",
        "symbolic_checks": symbolic,
        "exact_cubic_Q_1_plus_x3_field_collapse_checks": field_records,
        "exact_integral_numeric_cross_checks": numerical,
        "mixed_kernel_inversion_and_saddle_diagnostics": [
            saddle_record(value) for value in (2 / 3, 0.7, 0.75, 0.8, 0.9, 1.0)
        ],
        "mixed_kernel_boundary_primitive_diagnostics": boundary_diagnostics(
            args.boundary_max_n
        ),
        "warnings": [
            "The Q=1+x^3 coefficient-field obstruction and determinant collapse are exact theorems in the source note.",
            "The mixed-kernel Hermite recurrence, inversion identity, universal clearing, and determinant/content formulas are exact.",
            "The raw inversion tail rate is not the pi-coordinate rate: rational Hermite boundary terms survive on the half-line.",
            "Floating saddle values and finite primitive scans are diagnostics, not proofs of an asymptotic or nonvanishing theorem.",
            "Observed shrinking primitive mixed-kernel forms are not promoted to a theorem: oscillatory log residues and endpoint determinant content remain uncontrolled.",
            "Nothing in this certificate proves or disproves that e+pi is transcendental.",
        ],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
