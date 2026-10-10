"""Exact certificate for the odd matching-gcd localization theorem.

The proof is in sources/critical_fourier_odd_matching_gcd_localization.md.
All arithmetic in this script is exact.  No floating-point value is used.
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
    for j, x in enumerate(left):
        for h, y in enumerate(right):
            value[j + h] = gadd(value[j + h], gmul(x, y))
    return value


def fourier_polynomial(n: int, k: int) -> list[Gaussian]:
    """Return G_{n,k}(y) in increasing coefficient order."""
    assert n > 0 and n % 2 == 0 and k > n
    ell = k - n - 1
    first = [
        (((-1) ** (n - j)) * math.comb(n, j), 0)
        for j in range(n + 1)
    ]
    second = [
        gscale(
            math.comb(n, j),
            gmul(gpow((1, 1), j), gpow((1, -1), n - j)),
        )
        for j in range(n + 1)
    ]
    third = [(math.comb(2 * ell, j), 0) for j in range(2 * ell + 1)]
    phase = gpow((0, -1), n)
    return [
        gmul(phase, coefficient)
        for coefficient in polymul(polymul(first, second), third)
    ]


def exponential_pair(n: int) -> tuple[int, int]:
    """Return the primitive pair p_n,q_n with q_n e-p_n>0."""
    p_previous, p_current = 1, 3
    q_previous, q_current = 1, 1
    if n == 0:
        return p_previous, q_previous
    if n == 1:
        return p_current, q_current
    for index in range(2, n + 1):
        multiplier = 2 * (2 * index - 1)
        p_previous, p_current = (
            p_current,
            multiplier * p_current + p_previous,
        )
        q_previous, q_current = (
            q_current,
            multiplier * q_current + q_previous,
        )
    assert math.gcd(p_current, q_current) == 1
    return p_current, q_current


def valuation_integer(value: int, prime: int) -> int:
    assert value != 0 and prime > 1
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def valuation_fraction(value: Fraction, prime: int) -> int:
    assert value
    return valuation_integer(value.numerator, prime) - valuation_integer(
        value.denominator, prime
    )


def factor_small(value: int) -> dict[str, int]:
    """Trial factor the deliberately small d and g values in this file."""
    value = abs(value)
    factors: dict[str, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            factors[str(divisor)] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[str(value)] = 1
    return factors


def sha256_decimal(value: int) -> str:
    return hashlib.sha256(str(value).encode("ascii")).hexdigest()


def exact_case(n: int, k: int, expected_d: int, expected_g: int) -> dict[str, object]:
    coefficients = fourier_polynomial(n, k)
    K = k - 1
    assert len(coefficients) == 2 * K + 1
    center = K
    c0_real, c0_imaginary = coefficients[center]
    assert c0_imaginary == 0 and c0_real > 0
    c0 = c0_real

    lcm_value = 1
    for index in range(1, K + 1):
        lcm_value = math.lcm(lcm_value, index)

    t_value = 0
    for index in range(1, K + 1):
        real, imaginary = coefficients[center + index]
        sine = (0, 1, 0, -1)[index % 4]
        cosine = (1, 0, -1, 0)[index % 4]
        n_value = real * sine - imaginary * (1 - cosine)
        t_value += (lcm_value // index) * n_value

    S = Fraction(t_value, lcm_value)
    ratio = Fraction(4 * t_value, lcm_value * c0)
    A, B = ratio.numerator, ratio.denominator
    assert math.gcd(abs(A), B) == 1 and B > 0

    p_value, q_value = exponential_pair(n)
    d = math.gcd(q_value, B)
    q_zero, b_zero = q_value // d, B // d
    M = q_zero * A - b_zero * p_value
    common_coefficient = q_value * B // d
    g = math.gcd(abs(M), common_coefficient)
    assert g == math.gcd(abs(M), d)
    assert math.gcd(abs(M), q_zero * b_zero) == 1
    assert d == expected_d and g == expected_g

    local_records: list[dict[str, object]] = []
    for prime_text in factor_small(d):
        prime = int(prime_text)
        alpha = valuation_integer(q_value, prime)
        beta = valuation_integer(B, prime)
        actual = valuation_integer(g, prime)
        if alpha != beta:
            predicted = 0
            normalized_valuation: int | None = None
        else:
            assert alpha > 0
            normalized = (
                4
                * (q_value // (prime**alpha))
                * (prime**alpha)
                * S
                / c0
                - p_value
            )
            normalized_valuation = valuation_fraction(normalized, prime)
            predicted = min(alpha, normalized_valuation)
        assert actual == predicted
        local_records.append(
            {
                "prime": prime,
                "v_q": alpha,
                "v_B": beta,
                "v_g": actual,
                "normalized_congruence_valuation": normalized_valuation,
            }
        )

    return {
        "n": n,
        "k": k,
        "K": K,
        "p_n": str(p_value),
        "q_n": str(q_value),
        "A": str(A),
        "B": str(B),
        "M": str(M),
        "d": str(d),
        "g": str(g),
        "d_factorization": factor_small(d),
        "g_factorization": factor_small(g),
        "local_records": local_records,
        "decimal_lengths": {
            "A": len(str(abs(A))),
            "B": len(str(B)),
            "M": len(str(abs(M))),
        },
        "decimal_sha256": {
            "A": sha256_decimal(A),
            "B": sha256_decimal(B),
            "M": sha256_decimal(M),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/critical_fourier_odd_matching_gcd_certificate.json"
        ),
    )
    arguments = parser.parse_args()

    specifications = [
        (2, 10, 7, 7),
        (4, 40, 1001, 143),
        (8, 110, 169, 169),
        (18, 1004, 343, 343),
        (26, 851, 3443, 313),
        (72, 190, 17479, 227),
        (92, 443, 78287, 647),
        (64, 798, 937, 937),
    ]
    records = [exact_case(*specification) for specification in specifications]
    output = {
        "description": (
            "Exact counterexamples and local valuation checks for the odd "
            "critical-Fourier matching content"
        ),
        "case_count": len(records),
        "cases": records,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
