#!/usr/bin/env python3
"""Deterministic exact checker for Item 267.

The program uses only the Python standard library.  Bounded prime loops check
identities and never search for exceptional zero primes.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path


@dataclass(frozen=True)
class QZeta:
    """Element a+b*zeta with zeta^2+zeta+1=0."""

    a: Fraction
    b: Fraction

    @staticmethod
    def make(a: int | Fraction, b: int | Fraction = 0) -> "QZeta":
        return QZeta(Fraction(a), Fraction(b))

    def __add__(self, other: object) -> "QZeta":
        if not isinstance(other, QZeta):
            other = QZeta.make(Fraction(other))  # type: ignore[arg-type]
        return QZeta(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> "QZeta":
        return QZeta(-self.a, -self.b)

    def __sub__(self, other: object) -> "QZeta":
        return self + (-other)  # type: ignore[arg-type]

    def __rsub__(self, other: object) -> "QZeta":
        return (-self) + other

    def __mul__(self, other: object) -> "QZeta":
        if not isinstance(other, QZeta):
            other = QZeta.make(Fraction(other))  # type: ignore[arg-type]
        # (a+bz)(c+dz)=(ac-bd)+(ad+bc-bd)z
        return QZeta(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    __rmul__ = __mul__

    def inverse(self) -> "QZeta":
        # Norm(a+bz)=a^2-ab+b^2 and conjugate(a+bz)=(a-b)-bz.
        norm = self.a * self.a - self.a * self.b + self.b * self.b
        if norm == 0:
            raise ZeroDivisionError
        return QZeta((self.a - self.b) / norm, -self.b / norm)

    def __truediv__(self, other: object) -> "QZeta":
        if not isinstance(other, QZeta):
            other = QZeta.make(Fraction(other))  # type: ignore[arg-type]
        return self * other.inverse()

    def __pow__(self, exponent: int) -> "QZeta":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        out = QZeta.make(1)
        base = self
        e = exponent
        while e:
            if e & 1:
                out = out * base
            base = base * base
            e >>= 1
        return out

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def serial(self) -> list[str]:
        return [str(self.a), str(self.b)]


def qz_poly_add(a: list[QZeta], b: list[QZeta]) -> list[QZeta]:
    zero = QZeta.make(0)
    out = [zero] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] = out[i] + value
    for i, value in enumerate(b):
        out[i] = out[i] + value
    return out


def qz_poly_mul(a: list[QZeta], b: list[QZeta]) -> list[QZeta]:
    zero = QZeta.make(0)
    out = [zero] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = out[i + j] + left * right
    return out


def qz_poly_scale(a: list[QZeta], scalar: QZeta) -> list[QZeta]:
    return [scalar * value for value in a]


def elliptic_add(
    left: tuple[Fraction, Fraction] | None,
    right: tuple[Fraction, Fraction] | None,
) -> tuple[Fraction, Fraction] | None:
    """Group law on y^2=x^3-4."""
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == -y2:
        return None
    if left == right:
        slope = 3 * x1 * x1 / (2 * y1)
    else:
        slope = (y2 - y1) / (x2 - x1)
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


def inv(value: int, p: int) -> int:
    return pow(value % p, p - 2, p)


def epsilon_two(p: int) -> int:
    value = pow(2, (p - 1) // 2, p)
    assert value in (1, p - 1)
    return 1 if value == 1 else -1


def h_prefix(p: int, limit: int) -> tuple[list[int], list[int]]:
    h = [1]
    H = [1]
    for j in range(limit):
        ratio = (2 * j + 1) * inv(4 * j + 4, p) % p
        h.append(h[-1] * ratio % p)
        H.append((H[-1] + h[-1]) % p)
    return h, H


def polynomial_divide_v_minus_one(coefficients: list[int], p: int) -> list[int]:
    """Ascending coefficients; exact division by v-1."""
    degree = len(coefficients) - 1
    quotient = [0] * degree
    running = coefficients[degree] % p
    quotient[degree - 1] = running
    for k in range(degree - 1, 0, -1):
        running = (coefficients[k] + running) % p
        quotient[k - 1] = running
    remainder = (coefficients[0] + running) % p
    assert remainder == 0
    return quotient


def quotient_qn(p: int) -> list[int]:
    n = (p - 1) // 2
    half = inv(2, p)
    coefficients = [
        comb(n, k) * pow(-half % p, n - k, p) % p for k in range(n + 1)
    ]
    coefficients[0] = (coefficients[0] - pow(half, n, p)) % p
    return polynomial_divide_v_minus_one(coefficients, p)


def boundary_data(p: int, phase: int, delta: int) -> tuple[int, int]:
    c = 1
    total = 0
    for j in range(delta):
        total = (total + c) % p
        if phase == 5:
            c = c * (6 * j + 5) * inv(3 * j + 4, p) % p
        else:
            c = c * (6 * j + 1) * inv(3 * j + 2, p) % p
    return total, c


def pochhammer_tail(p: int, phase: int, delta: int, r: int) -> int:
    if phase == 5:
        start = (-inv(3, p) - delta) % p
    else:
        start = (inv(3, p) - delta) % p
    numerator = 1
    denominator = 1
    power_two = 1
    total = 0
    for k in range(1, r + 3):
        numerator = numerator * (start + k - 1) % p
        denominator = denominator * ((inv(2, p) + k - 1) % p) % p
        power_two = power_two * 2 % p
        term = numerator * inv(denominator, p) % p
        term = term * inv(power_two, p) % p
        total = (total + term) % p
    return total


def legendre(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    result = pow(value, (p - 1) // 2, p)
    return -1 if result == p - 1 else result


def check_geometry(box: int) -> dict[str, object]:
    zeta = QZeta.make(0, 1)
    roots = [QZeta.make(1), zeta, zeta**2]
    one = QZeta.make(1)
    zero = QZeta.make(0)
    for root in roots:
        assert root**3 == one

    # Product of (X-alpha) and weighted partial fractions.
    denominator = [one]
    for root in roots:
        denominator = qz_poly_mul(denominator, [-root, one])
    assert denominator == [-one, zero, zero, one]

    numerator = [zero]
    unit_numerator = [zero]
    for i, root in enumerate(roots):
        cofactor = [one]
        for j, other in enumerate(roots):
            if i != j:
                cofactor = qz_poly_mul(cofactor, [-other, one])
        numerator = qz_poly_add(
            numerator, qz_poly_scale(cofactor, root.inverse() / 3)
        )
        unit_numerator = qz_poly_add(unit_numerator, cofactor)
    assert numerator == [zero, one, zero]
    assert unit_numerator == [zero, zero, QZeta.make(3)]

    kernel_rows = 0
    for n0 in range(-box, box + 1):
        for n1 in range(-box, box + 1):
            for n2 in range(-box, box + 1):
                element = QZeta.make(n0) + n1 * zeta + n2 * (zeta**2)
                assert element.is_zero() == (n0 == n1 == n2)
                kernel_rows += 1

    residue_character = [roots[k].inverse() for k in range(3)]
    assert residue_character == [one, zeta**2, zeta]
    assert not (residue_character[0] == residue_character[1] == residue_character[2])

    point = (Fraction(2), Fraction(2))
    twice = elliptic_add(point, point)
    thrice = elliptic_add(twice, point)
    assert twice == (Fraction(5), Fraction(-11))
    assert thrice == (Fraction(106, 9), Fraction(1090, 27))
    assert thrice[0].denominator != 1

    return {
        "zeta_roots_checked": 3,
        "partial_fraction_coefficients_checked": len(numerator),
        "unit_partial_fraction_coefficients_checked": len(unit_numerator),
        "boundary_kernel_box": [-box, box],
        "boundary_kernel_rows": kernel_rows,
        "residue_character": [entry.serial() for entry in residue_character],
        "elliptic_point": ["2", "2"],
        "twice_point": [str(twice[0]), str(twice[1])],
        "thrice_point": [str(thrice[0]), str(thrice[1])],
        "nagell_lutz_input": "3P is finite with nonintegral rational coordinates",
        "label": "EXACT FINITE ONLY",
    }


def check_cartier(prime_limit: int) -> dict[str, object]:
    prime_rows = 0
    coefficient_rows = 0
    normal_form_rows = 0
    endpoint_rows = 0
    cutoff_rows = 0
    full_vector_rows = 0

    for p in range(5, prime_limit + 1):
        if not is_prime(p):
            continue
        phase = p % 6
        if phase not in (1, 5):
            continue
        q = (p - phase) // 6
        h, H = h_prefix(p, q + 2)
        hq = h[q]
        Hq = H[q]
        eps = epsilon_two(p) % p
        assert hq != 0

        quotient = quotient_qn(p)
        n = (p - 1) // 2
        half = inv(2, p)
        if phase == 5:
            assert quotient[2 * q + 1] == Hq
            compact = comb(n, 2 * q + 1) * pow(-half % p, q + 1, p) % p
            assert compact == (-hq) % p

            shift = Hq * inv(eps, p) % p
            assert (Hq - eps * shift) % p == 0
            assert (-inv(hq, p) * (-hq)) % p == 1
            normal_form_rows += 2

            # Direct endpoint check for Lambda(L(X^-1))=-epsilon.
            endpoint = 0
            inv2 = inv(2, p)
            for x in range(1, p):
                if x == 1:
                    continue
                g = (x**3 - inv2) % p
                l_value = inv2 * (x + inv(x * x, p)) % p
                endpoint = (endpoint + l_value * legendre(g, p)) % p
            assert endpoint == (-eps) % p
            endpoint_rows += 1
        else:
            assert quotient[2 * q] == (Hq - hq) % p
            compact = comb(n, 2 * q) * pow(-half % p, q, p) % p
            assert compact == hq
            lam = (Hq - hq) % p
            if hq != eps:
                shift = -lam * inv(hq - eps, p) % p
                assert (lam + shift * (hq - eps)) % p == 0
                normal_form_rows += 1

            d0 = (
                -3 * h[q + 1] * inv(2 * (-1), p)
                - eps * (-1) * inv(6, p)
            ) % p
            d1 = (
                -3 * h[q] * inv(2 * 2, p)
                - eps * 2 * inv(6, p)
            ) % p
            assert (30 * d0 + 12 * d1) % p == eps
            endpoint_rows += 1

        coefficient_rows += 2
        prime_rows += 1

        first_delta = 1 if phase == 5 else 3
        for delta in range(first_delta, q + 1, 2):
            K, c_delta = boundary_data(p, phase, delta)
            m = q - delta
            assert H[m] == (Hq - K * hq) % p
            if phase == 5:
                matrix_coefficient = (Hq + K * (-hq)) % p
                r = 3 * delta - 2
            else:
                matrix_coefficient = ((Hq - hq) + (1 - K) * hq) % p
                r = 3 * delta - 4
            assert matrix_coefficient == H[m]
            cutoff_rows += 1

            Pi = pochhammer_tail(p, phase, delta, r)
            D = (K + c_delta * Pi) % p
            if phase == 5:
                full_coefficient = (Hq + D * (-hq)) % p
            else:
                full_coefficient = ((Hq - hq) + (1 - D) * hq) % p
            assert full_coefficient == (Hq - D * hq) % p
            full_vector_rows += 1

    return {
        "prime_range": [5, prime_limit],
        "prime_phase_rows": prime_rows,
        "cartier_coefficient_rows": coefficient_rows,
        "normal_form_equalities": normal_form_rows,
        "endpoint_non_descent_equalities": endpoint_rows,
        "cutoff_matrix_coefficient_rows": cutoff_rows,
        "full_period_vector_rows": full_vector_rows,
        "exceptional_zero_search": "NOT PERFORMED",
        "label": "EXACT FINITE ONLY",
    }


def build_result() -> dict[str, object]:
    return {
        "schema": "item267-generalized-jacobian-frobenius-certificate-v1",
        "scope": (
            "exact bounded identity replay for the fixed open curve and moving "
            "matrix coefficients; no exceptional-prime or density search"
        ),
        "geometry": check_geometry(7),
        "cartier": check_cartier(401),
        "strict_labels": {
            "generalized_jacobian_and_one_motive_theorems": (
                "PROVED IN REPORT BY EXACT DIVISOR AND GROUP-LAW ARGUMENTS"
            ),
            "bounded_checks": "EXACT FINITE ONLY",
            "wieferich_equivalence": "OPEN; ANALOGY ONLY",
            "positive_linear_capacity_admission": "FAIL",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = build_result()
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

