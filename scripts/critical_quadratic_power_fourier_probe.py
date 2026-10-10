"""Exact finite checks for the critical quadratic-power Fourier formulas.

This script is computational validation only; the theorem is proved in
sources/critical_quadratic_power_fourier_barrier.md.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from math import comb, gcd, lcm

import mpmath as mp


Gaussian = tuple[int, int]


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] + b[0], a[1] + b[1]


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(c: int, a: Gaussian) -> Gaussian:
    return c * a[0], c * a[1]


def gpow(a: Gaussian, exponent: int) -> Gaussian:
    out = (1, 0)
    base = a
    power = exponent
    while power:
        if power & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        power >>= 1
    return out


def polymul(left: list[Gaussian], right: list[Gaussian]) -> list[Gaussian]:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = gadd(out[i + j], gmul(a, b))
    return out


def fourier_polynomial(n: int, k: int) -> list[Gaussian]:
    assert n % 2 == 0 and k > n
    ell = k - n - 1
    first = [(((-1) ** (n - j)) * comb(n, j), 0) for j in range(n + 1)]
    second = [
        gscale(comb(n, j), gmul(gpow((1, 1), j), gpow((1, -1), n - j)))
        for j in range(n + 1)
    ]
    third = [(comb(2 * ell, j), 0) for j in range(2 * ell + 1)]
    out = polymul(polymul(first, second), third)
    phase = gpow((0, -1), n)
    return [gmul(phase, coefficient) for coefficient in out]


def check_case(n: int, k: int) -> dict[str, object]:
    coefficients = fourier_polynomial(n, k)
    degree = 2 * k - 2
    assert len(coefficients) == degree + 1
    center = k - 1

    for m in range(1, k):
        negative = coefficients[center - m]
        positive = coefficients[center + m]
        assert negative == (positive[0], -positive[1])

    c_zero = coefficients[center]
    assert c_zero[1] == 0 and c_zero[0] > 0
    c_zero_integer = c_zero[0]

    lcm_value = 1
    for m in range(1, k):
        lcm_value = lcm(lcm_value, m)

    t_value = 0
    for m in range(1, k):
        a_m, b_m = coefficients[center + m]
        sine = (0, 1, 0, -1)[m % 4]
        cosine = (1, 0, -1, 0)[m % 4]
        n_m = a_m * sine - b_m * (1 - cosine)
        t_value += (lcm_value // m) * n_m

    primitive_content = gcd(abs(4 * t_value), lcm_value * c_zero_integer)
    primitive_b = lcm_value * c_zero_integer // primitive_content
    assert gcd(abs(4 * t_value // primitive_content), primitive_b) == 1
    assert primitive_b <= lcm_value * c_zero_integer

    gamma = (1 + math.sqrt(2)) / 2
    assert math.log(c_zero_integer) <= degree * math.log(2) + n * math.log(gamma) + 1e-12
    assert math.log(lcm_value) <= (k - 1) * math.log(16) + 1e-12

    mp.mp.dps = 70
    direct = mp.quad(
        lambda x: x**n * (1 - x) ** n / (1 + x * x) ** k,
        [0, 1],
    )
    reconstructed = (
        mp.mpf(t_value) / (mp.mpf(2) ** degree * lcm_value)
        + mp.mpf(c_zero_integer) * mp.pi / (mp.mpf(2) ** degree * 4)
    )
    relative_error = abs(direct - reconstructed) / direct
    assert relative_error < mp.mpf("1e-55")

    return {
        "n": n,
        "k": k,
        "C0": str(c_zero_integer),
        "Lk": str(lcm_value),
        "T": str(t_value),
        "primitive_content": str(primitive_content),
        "primitive_B": str(primitive_b),
        "relative_error": mp.nstr(relative_error, 8),
    }


def main() -> None:
    cases: list[dict[str, object]] = []
    for n in range(2, 22, 2):
        for k in sorted({n + 1, n + 2, (3 * n + 1) // 2, 2 * n}):
            if k > n:
                cases.append(check_case(n, k))
    print(
        json.dumps(
            {
                "status": "pass",
                "role": "finite computational validation only",
                "case_count": len(cases),
                "cases": cases,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
