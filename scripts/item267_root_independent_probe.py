#!/usr/bin/env python3
"""Independent root audit for Item 267.

This deliberately rebuilds the elliptic group-law, cubic-character, Cartier
coefficient, normal-form, endpoint, and moving-cutoff checks without importing
the Item-267 checker.  Prime loops are identity checks, not a zero census.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


class Eisenstein:
    """a+b*z with z^2+z+1=0."""

    def __init__(self, a: int | Fraction, b: int | Fraction = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: object) -> "Eisenstein":
        if not isinstance(other, Eisenstein):
            other = Eisenstein(other)  # type: ignore[arg-type]
        return Eisenstein(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> "Eisenstein":
        return Eisenstein(-self.a, -self.b)

    def __sub__(self, other: object) -> "Eisenstein":
        return self + (-other)  # type: ignore[arg-type]

    def __rsub__(self, other: object) -> "Eisenstein":
        return (-self) + other

    def __mul__(self, other: object) -> "Eisenstein":
        if not isinstance(other, Eisenstein):
            other = Eisenstein(other)  # type: ignore[arg-type]
        return Eisenstein(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> "Eisenstein":
        result = Eisenstein(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Eisenstein):
            try:
                other = Eisenstein(other)  # type: ignore[arg-type]
            except (TypeError, ValueError):
                return False
        return self.a == other.a and self.b == other.b


def poly_add(left: list[Eisenstein], right: list[Eisenstein]) -> list[Eisenstein]:
    size = max(len(left), len(right))
    out = [Eisenstein(0) for _ in range(size)]
    for i, value in enumerate(left):
        out[i] = out[i] + value
    for i, value in enumerate(right):
        out[i] = out[i] + value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(left: list[Eisenstein], right: list[Eisenstein]) -> list[Eisenstein]:
    out = [Eisenstein(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = out[i + j] + a * b
    return out


def elliptic_add(
    left: tuple[Fraction, Fraction] | None,
    right: tuple[Fraction, Fraction] | None,
) -> tuple[Fraction, Fraction] | None:
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == -y2:
        return None
    slope = (
        3 * x1 * x1 / (2 * y1)
        if left == right
        else (y2 - y1) / (x2 - x1)
    )
    x3 = slope * slope - x1 - x2
    y3 = slope * (x1 - x3) - y1
    assert y3 * y3 == x3 * x3 * x3 - 4
    return x3, y3


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def inv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def eps2(p: int) -> int:
    value = pow(2, (p - 1) // 2, p)
    return 1 if value == 1 else -1


def half_coefficients(p: int, q: int) -> tuple[list[int], list[int]]:
    h = [1]
    total = [1]
    for j in range(q + 1):
        h.append(h[-1] * (2 * j + 1) * inv(4 * j + 4, p) % p)
        total.append((total[-1] + h[-1]) % p)
    return h, total


def direct_quotient(p: int) -> list[int]:
    n = (p - 1) // 2
    half = inv(2, p)
    numerator = [
        comb(n, k) * pow(-half % p, n - k, p) % p
        for k in range(n + 1)
    ]
    numerator[0] = (numerator[0] - pow(half, n, p)) % p
    quotient = [0] * n
    carry = numerator[-1]
    quotient[-1] = carry
    for k in range(n - 1, 0, -1):
        carry = (numerator[k] + carry) % p
        quotient[k - 1] = carry
    assert (numerator[0] + carry) % p == 0
    return quotient


def boundary_prefix(p: int, phase: int, delta: int) -> int:
    term = 1
    total = 0
    for j in range(delta):
        total = (total + term) % p
        if phase == 5:
            term = term * (6 * j + 5) * inv(3 * j + 4, p) % p
        else:
            term = term * (6 * j + 1) * inv(3 * j + 2, p) % p
    return total


def legendre(a: int, p: int) -> int:
    a %= p
    if not a:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def geometry_checks() -> dict[str, object]:
    z = Eisenstein(0, 1)
    roots = [Eisenstein(1), z, z**2]
    assert all(root**3 == 1 for root in roots)
    product = [Eisenstein(1)]
    for root in roots:
        product = poly_mul(product, [-root, Eisenstein(1)])
    assert product == [Eisenstein(-1), Eisenstein(0), Eisenstein(0), Eisenstein(1)]

    weighted = [Eisenstein(0)]
    unweighted = [Eisenstein(0)]
    for i, root in enumerate(roots):
        cofactor = [Eisenstein(1)]
        for j, other in enumerate(roots):
            if i != j:
                cofactor = poly_mul(cofactor, [-other, Eisenstein(1)])
        weighted = poly_add(
            weighted, [c * (root**2) * Fraction(1, 3) for c in cofactor]
        )
        unweighted = poly_add(unweighted, cofactor)
    assert weighted == [Eisenstein(0), Eisenstein(1)]
    assert unweighted == [Eisenstein(0), Eisenstein(0), Eisenstein(3)]

    kernel_rows = 0
    for n0 in range(-9, 10):
        for n1 in range(-9, 10):
            for n2 in range(-9, 10):
                value = Eisenstein(n0) + n1 * z + n2 * (z**2)
                assert (value == 0) == (n0 == n1 == n2)
                kernel_rows += 1

    point = (Fraction(2), Fraction(2))
    twice = elliptic_add(point, point)
    thrice = elliptic_add(twice, point)
    assert twice == (Fraction(5), Fraction(-11))
    assert thrice == (Fraction(106, 9), Fraction(1090, 27))
    assert thrice is not None and thrice[0].denominator > 1
    return {
        "cubic_roots": 3,
        "kernel_box_rows": kernel_rows,
        "twice_point": ["5", "-11"],
        "thrice_point": ["106/9", "1090/27"],
        "nagell_lutz_obstruction": "finite rational 3P has nonintegral coordinates",
    }


def arithmetic_checks(limit: int) -> dict[str, object]:
    prime_rows = 0
    quotient_rows = 0
    normal_rows = 0
    endpoint_rows = 0
    cutoff_rows = 0
    resonant_rows = 0
    for p in range(5, limit + 1):
        if not is_prime(p) or p % 6 not in (1, 5):
            continue
        phase = p % 6
        q = (p - phase) // 6
        h, H = half_coefficients(p, q + 1)
        hq, Hq = h[q], H[q]
        epsilon = eps2(p) % p
        quotient = direct_quotient(p)
        n = (p - 1) // 2
        half = inv(2, p)
        assert hq
        if phase == 5:
            assert quotient[2 * q + 1] == Hq
            compact = comb(n, 2 * q + 1) * pow(-half % p, q + 1, p) % p
            assert compact == -hq % p
            shift = Hq * inv(epsilon, p) % p
            assert (Hq - epsilon * shift) % p == 0
            assert (-inv(hq, p) * compact) % p == 1
            normal_rows += 2
            endpoint = 0
            for x in range(1, p):
                if x == 1:
                    continue
                value = inv(2, p) * (x + inv(x * x, p)) % p
                endpoint = (endpoint + value * legendre(x**3 - inv(2, p), p)) % p
            assert endpoint == -epsilon % p
        else:
            assert quotient[2 * q] == (Hq - hq) % p
            compact = comb(n, 2 * q) * pow(-half % p, q, p) % p
            assert compact == hq
            lam = (Hq - hq) % p
            if hq == epsilon:
                resonant_rows += 1
            else:
                shift = -lam * inv(hq - epsilon, p) % p
                assert (lam + shift * (hq - epsilon)) % p == 0
                normal_rows += 1
            d0 = (-3 * h[q + 1] * inv(-2, p) + epsilon * inv(6, p)) % p
            d1 = (-3 * h[q] * inv(4, p) - 2 * epsilon * inv(6, p)) % p
            assert (30 * d0 + 12 * d1) % p == epsilon
        endpoint_rows += 1
        quotient_rows += 2
        first = 1 if phase == 5 else 3
        for delta in range(first, q + 1, 2):
            K = boundary_prefix(p, phase, delta)
            m = q - delta
            if phase == 5:
                coefficient = (Hq - K * hq) % p
            else:
                coefficient = ((Hq - hq) + (1 - K) * hq) % p
            assert coefficient == H[m]
            cutoff_rows += 1
        prime_rows += 1
    return {
        "prime_limit": limit,
        "prime_phase_rows": prime_rows,
        "quotient_coordinate_rows": quotient_rows,
        "normal_form_rows": normal_rows,
        "resonant_p1_rows": resonant_rows,
        "endpoint_rows": endpoint_rows,
        "cutoff_rows": cutoff_rows,
        "zero_census_performed": False,
        "label": "EXACT FINITE ONLY",
    }


def main() -> None:
    payload = {
        "schema": "item267-root-independent-probe-v1",
        "scope": "independent exact identity replay; no exceptional-prime search",
        "geometry": geometry_checks(),
        "arithmetic": arithmetic_checks(509),
        "booking": {
            "new_route1_rate": 0,
            "new_j2_capacity_reduction": 0,
        },
    }
    output = Path(__file__).resolve().parents[1] / "results" / "item267_root_independent_probe.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
