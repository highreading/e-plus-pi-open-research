#!/usr/bin/env python3
"""Exact probe for the valid-prime m-ray Cartier obstruction.

For p=6m+q and epsilon=p mod 4, the two necessary common-zero
conditions are represented by rational numbers L1(m,epsilon),
L2(m,epsilon).  This script computes them exactly and tests the conjectural
experimental certificate after clearing their least common denominator D:

    gcd(D L1, D L2) | (6m)!.

The corrected A/B sums contain no p: p only selects epsilon.  Their exact
identification with Lambda_1,Lambda_2 makes the final pair epsilon-independent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= Fraction(value - index, index + 1)
    return answer


def coefficient_value(m: int, epsilon: int, r: int, index_shift: int) -> Fraction:
    """Represent [z^(p-index_shift-r)]G_m modulo p without p."""

    bottom = 4 * m + 2
    residue = (epsilon - index_shift - r) % 4
    answer = Fraction(0)
    for j in range(residue, 10 * m + 4, 4):
        top = Fraction(16 * m + 8 - index_shift - r - j, 4)
        answer += (
            (-1) ** j
            * math.comb(10 * m + 3, j)
            * generalized_binomial(top, bottom)
        )
    return answer


def x_value(m: int, epsilon: int, r: int) -> Fraction:
    """Represent A_r=[z^(p-6m-r)]G_m modulo p."""

    return coefficient_value(m, epsilon, r, 6 * m)


def y_value(m: int, epsilon: int, r: int) -> Fraction:
    """Represent B_r=[z^(p-r)]G_m modulo p."""

    return coefficient_value(m, epsilon, r, 0)


def obstruction_pair(m: int, epsilon: int) -> tuple[Fraction, Fraction]:
    a = {r: x_value(m, epsilon, r) for r in range(1, 9)}
    b = {r: y_value(m, epsilon, r) for r in range(1, 9)}
    first = a[1] - b[8]
    second = a[2] + a[3] + a[4] - b[5] - b[6] - b[7]
    return first, second


def fixed_m_lambda(m: int, s: int) -> int:
    """Compute the exact p-independent Lambda_s coefficient."""

    target = 4 * m + s
    plus_power = 1 + 3 * s
    denominator_power = 4 * m + 1 + s
    # Build (1-z)^(6m) once by the exact adjacent-binomial recurrence.
    minus = [1]
    for degree in range(min(target, 6 * m)):
        minus.append(-minus[-1] * (6 * m - degree) // (degree + 1))

    plus = [math.comb(plus_power, degree) for degree in range(plus_power + 1)]
    numerator = [0] * (target + 1)
    for left_degree, left in enumerate(minus):
        for right_degree, right in enumerate(plus):
            if left_degree + right_degree <= target:
                numerator[left_degree + right_degree] += left * right

    # Coefficients of (1+z^2)^(-denominator_power), indexed by z^(2h).
    denominator = [1]
    for half in range(target // 2):
        denominator.append(
            -denominator[-1]
            * (denominator_power + half)
            // (half + 1)
        )

    return sum(
        numerator[target - 2 * half] * value
        for half, value in enumerate(denominator)
    )


def obstruction_pair_via_lambda(m: int) -> tuple[Fraction, Fraction]:
    lambda_1 = fixed_m_lambda(m, 1)
    lambda_2 = fixed_m_lambda(m, 2)
    first = Fraction(lambda_2, 2 ** (2 * m + 4))
    second = Fraction(lambda_1, 2 ** (2 * m + 2)) - first
    return first, second


def common_integral_numerator(left: Fraction, right: Fraction) -> tuple[int, int]:
    denominator = math.lcm(left.denominator, right.denominator)
    left_integer = left.numerator * (denominator // left.denominator)
    right_integer = right.numerator * (denominator // right.denominator)
    return math.gcd(abs(left_integer), abs(right_integer)), denominator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=30)
    parser.add_argument(
        "--direct-window-check-max-m",
        type=int,
        default=20,
        help="also verify the slower corrected A/B sums through this m",
    )
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    rows = []
    all_divide_factorial = True
    all_denominators_powers_of_two = True
    all_direct_window_checks_pass = True
    for m in range(1, arguments.max_m + 1):
        factorial = math.factorial(6 * m)
        lambda_pair = obstruction_pair_via_lambda(m)
        for epsilon in (1, 3):
            left, right = lambda_pair
            direct_match = None
            if m <= arguments.direct_window_check_max_m:
                direct_match = obstruction_pair(m, epsilon) == lambda_pair
                all_direct_window_checks_pass &= direct_match
            common, denominator = common_integral_numerator(left, right)
            divides = common != 0 and factorial % common == 0
            power_of_two = denominator > 0 and denominator & (denominator - 1) == 0
            all_divide_factorial &= divides
            all_denominators_powers_of_two &= power_of_two
            rows.append(
                {
                    "m": m,
                    "epsilon": epsilon,
                    "common_numerator_gcd": str(common),
                    "common_denominator": str(denominator),
                    "gcd_divides_6m_factorial": divides,
                    "denominator_is_power_of_two": power_of_two,
                    "direct_corrected_windows_match_lambda_pair": direct_match,
                }
            )

    result = {
        "schema": "mixed-cubic-valid-mray-cartier-gcd-probe-v3",
        "max_m": arguments.max_m,
        "direct_window_check_max_m": arguments.direct_window_check_max_m,
        "all_gcds_divide_6m_factorial": all_divide_factorial,
        "all_common_denominators_are_powers_of_two": all_denominators_powers_of_two,
        "all_direct_corrected_window_checks_pass": all_direct_window_checks_pass,
        "rows": rows,
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    print(
        f"m=1..{arguments.max_m}; "
        f"gcd|(6m)!: {all_divide_factorial}; "
        f"2-power denominators: {all_denominators_powers_of_two}; "
        f"direct A/B checks: {all_direct_window_checks_pass}; "
        f"sha256={digest}"
    )
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        # Write the exact bytes whose digest was printed.  Text-mode writes on
        # Windows translate LF to CRLF and would otherwise change the file hash.
        arguments.output.write_bytes(payload.encode("utf-8"))


if __name__ == "__main__":
    main()
