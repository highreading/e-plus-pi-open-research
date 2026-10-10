"""Exact certificate for the three-adjacent matching-product obstruction.

The all-parameter proof is in
sources/critical_fourier_three_adjacent_matching_product.md.  This script
certifies the finite exact counterexample in its Section 5.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


Gaussian = tuple[int, int]


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(scale: int, value: Gaussian) -> Gaussian:
    return scale * value[0], scale * value[1]


def gpow(base: Gaussian, exponent: int) -> Gaussian:
    value = (1, 0)
    while exponent:
        if exponent & 1:
            value = gmul(value, base)
        base = gmul(base, base)
        exponent //= 2
    return value


def polymul(left: list[Gaussian], right: list[Gaussian]) -> list[Gaussian]:
    value = [(0, 0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            index = left_index + right_index
            value[index] = gadd(
                value[index], gmul(left_value, right_value)
            )
    return value


def fourier_polynomial(n: int, k: int) -> list[Gaussian]:
    ell = k - n - 1
    first = [
        (((-1) ** (n - index)) * math.comb(n, index), 0)
        for index in range(n + 1)
    ]
    second = [
        gscale(
            math.comb(n, index),
            gmul(
                gpow((1, 1), index),
                gpow((1, -1), n - index),
            ),
        )
        for index in range(n + 1)
    ]
    third = [
        (math.comb(2 * ell, index), 0)
        for index in range(2 * ell + 1)
    ]
    phase = gpow((0, -1), n)
    return [
        gmul(phase, coefficient)
        for coefficient in polymul(polymul(first, second), third)
    ]


def valuation(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def decimal_hash(value: int) -> str:
    return hashlib.sha256(str(value).encode("ascii")).hexdigest()


def exact_form(k: int) -> dict[str, object]:
    n = 2
    K = k - 1
    coefficients = fourier_polynomial(n, k)
    assert len(coefficients) == 2 * K + 1
    center = K
    c0, c0_imaginary = coefficients[center]
    assert c0 > 0 and c0_imaginary == 0

    lcm_value = 1
    for index in range(1, K + 1):
        lcm_value = math.lcm(lcm_value, index)

    t_value = 0
    for index in range(1, K + 1):
        real, imaginary = coefficients[center + index]
        sine = (0, 1, 0, -1)[index % 4]
        cosine = (1, 0, -1, 0)[index % 4]
        numerator = real * sine - imaginary * (1 - cosine)
        t_value += (lcm_value // index) * numerator

    ratio = Fraction(4 * t_value, lcm_value * c0)
    A, B = ratio.numerator, ratio.denominator
    assert math.gcd(abs(A), B) == 1

    p_value, q_value = 19, 7
    d = math.gcd(q_value, B)
    M = (q_value // d) * A - (B // d) * p_value
    g = math.gcd(abs(M), d)

    expected = {
        10: (-149056, 135135, -515851),
        11: (-70016, 75075, -273791),
        12: (-1313792, 1684683, -5886503),
    }[k]
    assert (A, B, M) == expected
    assert d == 7 and g == 7
    assert valuation(B, 7) == 1
    assert valuation(M, 7) == 1

    return {
        "n": n,
        "k": k,
        "K": K,
        "p_n": p_value,
        "q_n": q_value,
        "C0": str(c0),
        "T": str(t_value),
        "L": str(lcm_value),
        "A": str(A),
        "B": str(B),
        "M": str(M),
        "d": d,
        "g": g,
        "h": d * g,
        "v7_B": valuation(B, 7),
        "v7_M": valuation(M, 7),
        "decimal_sha256": {
            "C0": decimal_hash(c0),
            "T": decimal_hash(t_value),
            "A": decimal_hash(A),
            "B": decimal_hash(B),
            "M": decimal_hash(M),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_three_adjacent_matching_product_certificate.json"
        ),
    )
    arguments = parser.parse_args()

    records = [exact_form(k) for k in (10, 11, 12)]
    product_h = math.prod(int(record["h"]) for record in records)
    q_value = int(records[0]["q_n"])
    triple_gcd = math.gcd(*(int(record["g"]) for record in records))
    common_band_lower = int(records[0]["K"]) + 2
    common_band_upper = 2 * (int(records[0]["K"]) - int(records[0]["n"]))
    assert not common_band_lower < q_value <= common_band_upper
    q_out = q_value
    assert product_h == q_value**6
    assert triple_gcd == q_value
    assert q_out == q_value
    assert product_h == q_value**5 * triple_gcd
    assert product_h > q_value**5

    output = {
        "description": (
            "Exact three-adjacent counterexample to an unconditional "
            "q_n^5 matching-product bound"
        ),
        "forms": records,
        "common_one_block_interval": {
            "strict_lower_endpoint": common_band_lower,
            "upper_endpoint": common_band_upper,
        },
        "triple_gcd": triple_gcd,
        "q_out": q_out,
        "product_h": product_h,
        "q_n_fifth_power": q_value**5,
        "q_n_sixth_power": q_value**6,
        "q_n_fifth_power_times_triple_gcd": q_value**5 * triple_gcd,
        "product_equals_q_n_fifth_power_times_triple_gcd": (
            product_h == q_value**5 * triple_gcd
        ),
        "product_equals_q_n_sixth_power": product_h == q_value**6,
        "product_exceeds_q_n_fifth_power": product_h > q_value**5,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
