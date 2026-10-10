#!/usr/bin/env python3
"""Exact checks for the fixed-target positive common-kernel gap theorem."""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd, lcm
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
    # sign=1 evaluates at i; sign=-1 evaluates at -i.
    powers = [(1, 0), (0, sign), (-1, 0), (0, -sign)]
    real = sum(coefficient * powers[k % 4][0]
               for k, coefficient in enumerate(poly))
    imag = sum(coefficient * powers[k % 4][1]
               for k, coefficient in enumerate(poly))
    return real, imag


def divide_by_one_plus_x2(poly: list[int]) -> tuple[list[int], tuple[int, int]]:
    work = list(poly)
    quotient = [0] * (len(poly) - 2)
    for k in range(len(poly) - 1, 1, -1):
        leading = work[k]
        quotient[k - 2] = leading
        work[k] -= leading
        work[k - 2] -= leading
    return quotient, (work[0], work[1])


def e_interval(cutoff: int) -> tuple[Fraction, Fraction]:
    lower = sum((Fraction(1, factorial(k)) for k in range(cutoff + 1)),
                Fraction(0))
    # For j>=0, (cutoff+1+j)! >= (cutoff+1)! (cutoff+2)^j.
    upper = lower + Fraction(cutoff + 2,
                             factorial(cutoff + 1) * (cutoff + 1))
    return lower, upper


def witness(n: int) -> list[int]:
    assert n >= 3 and n % 4 == 3
    # H_n+H_{n+2}, where H_k=x^k+k*x^(k-1).
    poly = [0] * (n + 3)
    poly[n - 1] = n
    poly[n] = 1
    poly[n + 1] = n + 2
    poly[n + 2] = 1
    return poly


def witness_record(n: int, der: list[int]) -> dict:
    poly = witness(n)
    assert all(coefficient >= 0 for coefficient in poly)
    assert A_value(poly, der) == 2
    assert B_value(poly) == 0
    assert gaussian_value(poly, 1) == (2, 0)
    assert gaussian_value(poly, -1) == (2, 0)

    numerator = list(poly)
    numerator[0] -= 2
    quotient, remainder = divide_by_one_plus_x2(numerator)
    assert remainder == (0, 0)
    rational_coordinate = 4 * sum(
        (Fraction(coefficient, k + 1)
         for k, coefficient in enumerate(quotient)), Fraction(0))
    D = rational_coordinate.denominator
    N = rational_coordinate.numerator
    content = gcd(2 * D, abs(N))
    assert content == gcd(2, abs(N))
    assert 2 % content == 0

    cap = 1
    for k in range(1, n + 2):
        cap = lcm(cap, k)
    assert cap % D == 0

    return {
        "n": n,
        "degree": n + 2,
        "rational_coordinate": [N, D],
        "clearing_lcm_digits": len(str(cap)),
        "exact_denominator_digits": len(str(D)),
        "content": content,
        "primitive_pair_a_s_plus_b": [2 * D // content, N // content],
    }


def main() -> None:
    maximum_n = 203
    der = derangements(maximum_n + 2)

    # u_n=A(x^n)=(-1)^n !n obeys u_n+n*u_{n-1}=1.
    for n in range(1, maximum_n + 3):
        u_n = (-1) ** n * der[n]
        u_previous = (-1) ** (n - 1) * der[n - 1]
        assert u_n + n * u_previous == 1

    lower_e, upper_e = e_interval(30)
    assert lower_e > Fraction(65, 24) - Fraction(1, factorial(5))
    # A direct useful enclosure: 65/24 is the partial sum through k=4.
    partial_four = sum((Fraction(1, factorial(k)) for k in range(5)),
                       Fraction(0))
    assert partial_four == Fraction(65, 24)
    assert lower_e > partial_four
    assert upper_e < 3
    assert 5 < 2 * lower_e and 2 * upper_e < 6
    assert lower_e - Fraction(5, 2) > Fraction(5, 24)

    checked = []
    selected = []
    selected_n = {3, 7, 11, 15, 19, 23, 27, 31, 51, 83, 123, 163, 203}
    max_denominator_digits = 0
    for n in range(3, maximum_n + 1, 4):
        record = witness_record(n, der)
        checked.append(n)
        max_denominator_digits = max(max_denominator_digits,
                                     record["exact_denominator_digits"])
        if n in selected_n:
            selected.append(record)

    result = {
        "status": "exact fixed-target primitive gap verified",
        "theorem": {
            "raw_gap": "L(F) >= frac(a*e) for fixed nonzero integer a",
            "content_divisibility": "gcd(a*D,N) divides a when gcd(D,N)=1",
            "primitive_gap": "L_primitive >= frac(a*e)/abs(a)",
            "a_equals_2_gap": "L_primitive >= e-5/2 > 5/24",
        },
        "e_interval": {
            "lower": [lower_e.numerator, lower_e.denominator],
            "upper": [upper_e.numerator, upper_e.denominator],
        },
        "witness_family": "F_n=H_n+H_(n+2), H_k=x^k+k*x^(k-1), n=3 mod 4",
        "witness_n_checked": checked,
        "selected_witness_records": selected,
        "maximum_exact_denominator_digits": max_denominator_digits,
        "scope": "Rules out every fixed nonzero target; does not treat targets a_n growing with degree.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
