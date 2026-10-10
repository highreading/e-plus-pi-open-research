#!/usr/bin/env python3
"""Exact checks for the direct beta-integral barrier.

For n divisible by 4, the script constructs

    E_n = 1/n! * integral_0^1 x^n(1-x)^n exp(x) dx
        = q_n e - p_n,

and

    J_n = integral_0^1 x^n(1-x)^n/(1+x^2) dx
        = r_n + (-1)^(n/4) 2^(n/2) pi/4.

It computes the primitive integer pi-form obtained from J_n and checks the
exact lower bound for the positive matched sum when n is 0 modulo 8 and the
fixed-sign matched difference when n is 4 modulo 8.  The finite output is
only a verifier for the proof in
sources/direct_integral_linear_forms_audit.md.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd, lcm


def beta_polynomial(n: int) -> list[int]:
    """Ascending coefficients of x^n(1-x)^n."""
    coefficients = [0] * (2 * n + 1)
    for j in range(n + 1):
        coefficients[n + j] = (-1) ** j * comb(n, j)
    return coefficients


def divide_by_one_plus_x_squared(
    coefficients: list[int],
) -> tuple[list[int], int, int]:
    """Return quotient and remainder rho_x*x+rho_0 over Z[x]."""
    remainder = coefficients[:]
    quotient = [0] * max(0, len(coefficients) - 2)
    for degree in range(len(coefficients) - 1, 1, -1):
        value = remainder[degree]
        quotient[degree - 2] = value
        remainder[degree] = 0
        remainder[degree - 2] -= value
    assert all(value == 0 for value in remainder[2:])
    return quotient, remainder[1], remainder[0]


def integral_of_polynomial(coefficients: list[int]) -> Fraction:
    return sum(
        (Fraction(value, degree + 1) for degree, value in enumerate(coefficients)),
        Fraction(0),
    )


def lcm_through(bound: int) -> int:
    answer = 1
    for value in range(1, bound + 1):
        answer = lcm(answer, value)
    return answer


def fraction_record(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def record(n: int) -> dict[str, object]:
    assert n >= 4 and n % 4 == 0

    coefficients = beta_polynomial(n)
    quotient, rho_x, rho = divide_by_one_plus_x_squared(coefficients)
    rational_part = integral_of_polynomial(quotient)

    # The remainder can also be read as (1+i)^n.
    assert rho_x == 0
    assert rho == (-1) ** (n // 4) * 2 ** (n // 2)

    # Endpoint integration by parts for the exponential integral.
    signed_q_numerator = sum(
        (-1) ** j * factorial(n + j) * comb(n, j)
        for j in range(n + 1)
    )
    signed_p_numerator = (-1) ** n * sum(
        comb(n, j) * factorial(n + j) for j in range(n + 1)
    )
    assert signed_q_numerator % factorial(n) == 0
    assert signed_p_numerator % factorial(n) == 0
    q = abs(signed_q_numerator // factorial(n))
    p = abs(signed_p_numerator // factorial(n))
    assert gcd(p, q) == 1

    # Minimal integer multiplier for J_n, followed by primitive reduction.
    initial_multiplier = lcm(
        rational_part.denominator,
        4 // gcd(4, abs(rho)),
    )
    raw_a = initial_multiplier * rational_part
    assert raw_a.denominator == 1
    raw_a_integer = raw_a.numerator
    raw_b = initial_multiplier * rho // 4
    content = gcd(abs(raw_a_integer), abs(raw_b))
    primitive_a = raw_a_integer // content
    primitive_b = raw_b // content
    primitive_multiplier = Fraction(initial_multiplier, content)
    assert gcd(abs(primitive_a), abs(primitive_b)) == 1
    assert (primitive_b > 0) == (rho > 0)

    beta_integral = Fraction(factorial(n) ** 2, factorial(2 * n + 1))
    j_lower = beta_integral / 2
    absolute_rho = abs(rho)

    if rho > 0:
        # L_pi/B_pi = 4 J_n/rho is primitive-invariant.  The pi
        # contribution to a positive matched sum is at least 4*q*J_n/rho.
        match_type = "positive_sum"
        dominance_ratio_upper = None
        exact_matched_lower = Fraction(4 * q, absolute_rho) * j_lower
        coarse_matched_lower = Fraction(
            factorial(n),
            (2 * n + 1) * absolute_rho,
        )
    else:
        # With c=|rho|/4, the matched value per common coefficient is
        # E_n/q-J_n/c.  Replacing e by the rigorous upper bound 3 makes
        # the displayed ratio rational and still proves it is below 1/2.
        match_type = "fixed_sign_difference"
        dominance_ratio_upper = Fraction(
            3 * absolute_rho,
            2 * n * factorial(2 * n - 1),
        )
        assert dominance_ratio_upper < Fraction(1, 2)
        exact_matched_lower = Fraction(2 * q, absolute_rho) * j_lower
        coarse_matched_lower = Fraction(
            factorial(n),
            2 * (2 * n + 1) * absolute_rho,
        )

    assert exact_matched_lower >= coarse_matched_lower

    positive_b = abs(primitive_b)
    matching_gcd = gcd(q, positive_b)
    exponential_weight = positive_b // matching_gcd
    pi_weight = q // matching_gcd
    common_coefficient = exponential_weight * q
    if rho > 0:
        matched_constant = (
            -exponential_weight * p + pi_weight * primitive_a
        )
    else:
        matched_constant = (
            -exponential_weight * p - pi_weight * primitive_a
        )
    final_content = gcd(abs(matched_constant), common_coefficient)
    assert matching_gcd % final_content == 0
    primitive_coarse_lower = coarse_matched_lower / final_content

    universal_denominator = lcm_through(2 * n - 1)
    universal_pi_lower = 4 * universal_denominator * j_lower
    uniform_numerator_factor = 4 if rho > 0 else 2
    fully_primitive_uniform_lower = Fraction(
        uniform_numerator_factor * factorial(n),
        universal_denominator * (2 * n + 1) * 2**n,
    )
    assert primitive_coarse_lower >= fully_primitive_uniform_lower

    return {
        "n": n,
        "rho": str(rho),
        "match_type": match_type,
        "dominance_ratio_upper_using_e_lt_3": (
            None
            if dominance_ratio_upper is None
            else fraction_record(dominance_ratio_upper)
        ),
        "exponential_form": {
            "p": str(p),
            "q": str(q),
            "gcd_p_q": gcd(p, q),
        },
        "pi_rational_part": fraction_record(rational_part),
        "primitive_pi_form": {
            "a": str(primitive_a),
            "b": str(primitive_b),
            "multiplier_of_J": fraction_record(primitive_multiplier),
            "content_removed": str(content),
        },
        "beta_integral": fraction_record(beta_integral),
        "exact_matched_absolute_lower_bound": fraction_record(
            exact_matched_lower
        ),
        "coarse_theorem_lower_bound": fraction_record(
            coarse_matched_lower
        ),
        "coarse_theorem_lower_bound_gt_one": coarse_matched_lower > 1,
        "minimal_matched_form": {
            "exponential_weight": str(exponential_weight),
            "pi_weight": str(pi_weight),
            "constant_coefficient": str(matched_constant),
            "common_e_and_pi_coefficient": str(common_coefficient),
            "final_content": str(final_content),
            "coarse_lower_after_final_content": fraction_record(
                primitive_coarse_lower
            ),
            "uniform_fully_primitive_lower_bound": fraction_record(
                fully_primitive_uniform_lower
            ),
        },
        "universal_lcm_pi_lower_bound": fraction_record(
            universal_pi_lower
        ),
        "universal_lcm_pi_lower_bound_gt_one": universal_pi_lower > 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=64)
    args = parser.parse_args()
    if args.max_n < 4:
        raise SystemExit("--max-n must be at least 4")

    values = list(range(4, args.max_n + 1, 4))
    output = {
        "description": (
            "Exact finite checks for the symmetric beta direct-integral "
            "barrier; the all-index proof is in "
            "sources/direct_integral_linear_forms_audit.md."
        ),
        "records": [record(n) for n in values],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
