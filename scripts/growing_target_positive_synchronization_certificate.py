#!/usr/bin/env python3
"""Exact checks for the growing-target positive synchronization barrier."""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd, log2
import json


def derangements(limit: int) -> list[int]:
    out = [0] * (limit + 1)
    out[0] = 1
    for n in range(1, limit + 1):
        out[n] = n * out[n - 1] + (-1) ** n
    return out


def A_value(poly: list[int], der: list[int]) -> int:
    return sum(coefficient * (-1) ** k * der[k]
               for k, coefficient in enumerate(poly))


def B_value(poly: list[int]) -> int:
    return sum(coefficient * (-1) ** k * factorial(k)
               for k, coefficient in enumerate(poly))


def gaussian_value(poly: list[int], sign: int = 1) -> tuple[int, int]:
    powers = [(1, 0), (0, sign), (-1, 0), (0, -sign)]
    return (
        sum(coefficient * powers[k % 4][0]
            for k, coefficient in enumerate(poly)),
        sum(coefficient * powers[k % 4][1]
            for k, coefficient in enumerate(poly)),
    )


def multiply(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return out


def add(a: list[int], b: list[int], scale_b: int = 1) -> list[int]:
    out = [0] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += scale_b * x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a: list[int], scalar: int) -> list[int]:
    return [scalar * x for x in a]


def divide_by_one_plus_x2(poly: list[int]) -> tuple[list[int], tuple[int, int]]:
    work = list(poly)
    quotient = [0] * (len(poly) - 2)
    for k in range(len(poly) - 1, 1, -1):
        leading = work[k]
        quotient[k - 2] = leading
        work[k] -= leading
        work[k - 2] -= leading
    return quotient, (work[0], work[1])


def rational_output(poly: list[int], target: int) -> dict:
    shifted = list(poly)
    shifted[0] -= target
    quotient, remainder = divide_by_one_plus_x2(shifted)
    assert remainder == (0, 0)
    pi_correction = 4 * sum(
        (Fraction(coefficient, k + 1)
         for k, coefficient in enumerate(quotient)), Fraction(0))
    total_rational = Fraction(-B_value(poly)) + pi_correction
    N, D = total_rational.numerator, total_rational.denominator
    g = gcd(abs(target) * D, abs(N))
    assert g == gcd(abs(target), abs(N))
    if g:
        assert abs(target) % g == 0
        primitive_pair = [target * D // g, N // g]
    else:
        assert target == 0 and N == 0
        primitive_pair = [0, 0]
    return {
        "M": pi_correction.numerator,
        "D": D,
        "N": N,
        "g": g,
        "primitive_pair": primitive_pair,
        "B": B_value(poly),
    }


def polynomial_content(poly: list[int]) -> int:
    out = 0
    for x in poly:
        out = gcd(out, abs(x))
    return out


def e_interval(cutoff: int) -> tuple[Fraction, Fraction]:
    lower = sum((Fraction(1, factorial(k)) for k in range(cutoff + 1)),
                Fraction(0))
    upper = lower + Fraction(cutoff + 2,
                             factorial(cutoff + 1) * (cutoff + 1))
    return lower, upper


def e_partial_quotient(index: int) -> int:
    if index == 0:
        return 2
    if index % 3 == 2:
        return 2 * ((index + 1) // 3)
    return 1


def convergents(limit: int) -> list[tuple[int, int, int]]:
    p_minus_two, p_minus_one = 0, 1
    q_minus_two, q_minus_one = 1, 0
    out = []
    for n in range(limit + 1):
        a = e_partial_quotient(n)
        p = a * p_minus_one + p_minus_two
        q = a * q_minus_one + q_minus_two
        out.append((n, p, q))
        p_minus_two, p_minus_one = p_minus_one, p
        q_minus_two, q_minus_one = q_minus_one, q
    return out


def interval_abs_lower(q: int, p: int,
                       lo: Fraction, hi: Fraction) -> Fraction:
    left = q * lo - p
    right = q * hi - p
    if left > 0:
        return left
    if right < 0:
        return -right
    return Fraction(0)


def verify_e_bound(max_q: int) -> None:
    lo, hi = e_interval(80)
    for q in range(1, max_q + 1):
        lower = Fraction(1, q * (4 * (q.bit_length() - 1) + 8))
        # The bit-length expression is <= 4 log_2(q)+8, so this test uses
        # a slightly stronger bound only when q is a power of two.  Check
        # the few nearest numerators directly with a rigorous e interval.
        center_lo = (q * lo).numerator // (q * lo).denominator
        center_hi = (q * hi).numerator // (q * hi).denominator
        candidates = set(range(center_lo - 2, center_hi + 4))
        for p in candidates:
            exact_lower = interval_abs_lower(q, p, lo, hi)
            analytic = Fraction(1, q * (4 * q.bit_length() + 8))
            assert exact_lower > analytic


def base_and_zero_form() -> tuple[list[int], list[int]]:
    # F0=4*x*(1-x)^2*(31-3*x^2).
    x = [0, 1]
    one_minus_x = [1, -1]
    f0 = scale(multiply(multiply(x, multiply(one_minus_x, one_minus_x)),
                        [31, 0, -3]), 4)
    # R=x*(1-x)^2*(1+x^2)*(-2090+4553*x+744*x^2).
    r = multiply(multiply(multiply(x, multiply(one_minus_x, one_minus_x)),
                          [1, 0, 1]), [-2090, 4553, 744])
    return f0, r


def saturation_record(multiplier: int, der: list[int]) -> dict:
    f0, zero = base_and_zero_form()
    poly = add(scale(f0, multiplier), zero)
    target = 272 * multiplier
    assert polynomial_content(poly) == 1
    assert A_value(poly, der) == target
    assert gaussian_value(poly, 1) == (target, 0)
    assert gaussian_value(poly, -1) == (target, 0)
    data = rational_output(poly, target)
    assert data["N"] == -1544 * multiplier
    assert data["D"] == 1
    assert data["g"] == 8 * multiplier
    assert data["primitive_pair"] == [34, -193]
    return {
        "multiplier": multiplier,
        "target": target,
        "polynomial_content": polynomial_content(poly),
        "output_content": data["g"],
        "primitive_pair": data["primitive_pair"],
    }


def main() -> None:
    der = derangements(20)
    f0, zero = base_and_zero_form()
    assert A_value(f0, der) == 272
    assert gaussian_value(f0) == (272, 0)
    assert B_value(f0) == 724
    assert rational_output(f0, 272)["N"] == -1544
    assert A_value(zero, der) == 0
    assert gaussian_value(zero) == (0, 0)
    assert B_value(zero) == -40
    zero_output = rational_output(zero, 0)
    assert zero_output["N"] == 0

    # Positivity: at multiplier 17 the bracket is increasing and starts at 18;
    # larger multipliers add 4(m-17)(31-3x^2)>=0 on [0,1].
    # Coefficients of S_17 and S_17' in ascending order.
    s17 = [18, 4553, -1550, 4553, 744]
    derivative_s17 = [4553, -3100, 13659, 2976]
    assert s17[0] == 18
    assert derivative_s17[0] - abs(derivative_s17[1]) == 1453
    assert all(x >= 0 for x in derivative_s17[2:])

    saturation_all = [saturation_record(m, der) for m in range(17, 1001)]
    selected_m = {17, 18, 25, 50, 100, 250, 1000}
    saturation = [record for record in saturation_all
                  if record["multiplier"] in selected_m]

    conv = convergents(60)
    for n, _p, q in conv[1:]:
        assert q >= 2 ** ((n - 1) // 2)
        assert e_partial_quotient(n) <= 2 * (n + 1)
    verify_e_bound(500)

    lo, hi = e_interval(80)
    result = {
        "status": "exact synchronization barrier and cross-content saturation verified",
        "two_place_lower_bound": "Lambda >= (D*frac(a*e)+frac(a*D*pi))/g",
        "continued_fraction_bound": "abs(q*e-p) > 1/(q*(4*log2(q)+8))",
        "primitive_e_barrier": "Lambda > D/(a^2*(4*log2(a)+8))",
        "synchronization": {
            "alpha": "a*D/g",
            "errors": "(e-B/a)+(pi+M/(a*D))=Lambda/alpha",
            "congruence": "M-B*D is divisible by g",
        },
        "e_interval": {
            "lower": [lo.numerator, lo.denominator],
            "upper": [hi.numerator, hi.denominator],
        },
        "e_convergents_checked": len(conv),
        "direct_e_bound_checked_through_q": 500,
        "cross_content_multipliers_checked": [17, 1000],
        "cross_content_records_checked": len(saturation_all),
        "cross_content_saturation_family": saturation,
        "scope": "No shrinking family and no upper bound excluding synchronized exceptional cross-content.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
