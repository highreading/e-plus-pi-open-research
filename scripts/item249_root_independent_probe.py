#!/usr/bin/env python3
"""Independent exact audit of Item 249; imports no Item 246--249 code."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha_rows(rows: list[tuple[int, ...]]) -> str:
    raw = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


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


def actual_coefficients(s: int) -> list[int]:
    n = 2 * s - 1
    return [
        3 * (math.comb(n, v) if 0 <= v <= n else 0)
        - 2 * (math.comb(n, v - 1) if 0 <= v - 1 <= n else 0)
        - (math.comb(n, v - 2) if 0 <= v - 2 <= n else 0)
        for v in range(n + 3)
    ]


def multiply(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def derivative(a: list[int]) -> list[int]:
    return [i * a[i] for i in range(1, len(a))]


def padded_equal(a: list[int], b: list[int]) -> bool:
    length = max(len(a), len(b))
    return a + [0] * (length - len(a)) == b + [0] * (length - len(b))


def h(v: int) -> Fraction:
    return sum((Fraction((-1) ** k, 2 * k + 3) for k in range(v)), Fraction(0))


def triangular(coefficients: list[int | Fraction]) -> Fraction:
    total = Fraction(0)
    for v in range(1, len(coefficients)):
        for k in range(v):
            total += Fraction(((-1) ** (v - k - 1)) * coefficients[v], (2 * k + 3) * (2 * v + 3))
    return total


def prefix_form(coefficients: list[int | Fraction]) -> Fraction:
    return sum(
        (Fraction(((-1) ** (v - 1)) * coefficients[v], 2 * v + 3) * h(v) for v in range(1, len(coefficients))),
        Fraction(0),
    )


def binomial_series(alpha: Fraction, degree: int) -> list[Fraction]:
    terms = [Fraction(1)]
    for v in range(degree):
        terms.append(terms[-1] * (alpha - v) / (v + 1))
    return terms


def universal_coefficients(degree: int) -> list[Fraction]:
    a = binomial_series(Fraction(-8, 3), degree)
    return [
        3 * a[v]
        - 2 * (a[v - 1] if v >= 1 else 0)
        - (a[v - 2] if v >= 2 else 0)
        for v in range(degree + 1)
    ]


def mod_fraction(value: Fraction, p: int) -> int:
    assert value.denominator % p
    return value.numerator % p * pow(value.denominator % p, -1, p) % p


def audit_s(s: int) -> None:
    n = 2 * s - 1
    coefficients = actual_coefficients(s)
    # Directly reconstruct D=(3-2t-t^2)(1+t)^n.
    expanded = multiply([3, -2, -1], [math.comb(n, v) for v in range(n + 1)])
    assert coefficients == expanded
    # Direct polynomial replay of the logarithmic-derivative identity.
    left = multiply([3, 1, -3, -1], derivative(expanded))
    right = multiply([3 * n - 2, -(2 * n + 4), -(n + 2)], expanded)
    assert padded_equal(left, right)
    # Coefficient recurrence and endpoints.
    for v in range(n + 2):
        dm1 = coefficients[v - 1] if v >= 1 else 0
        dm2 = coefficients[v - 2] if v >= 2 else 0
        assert 3 * (v + 1) * coefficients[v + 1] == (
            (3 * n - v - 2) * coefficients[v]
            + (3 * v - 2 * n - 7) * dm1
            + (v - n - 4) * dm2
        )
    assert coefficients[-1] == -1
    assert coefficients[-2] == -(n + 2)
    assert triangular(coefficients) == prefix_form(coefficients)


def main() -> None:
    for s in range(1, 81):
        audit_s(s)

    boundary_actual = prefix_form(actual_coefficients(1))
    boundary_theta = prefix_form(universal_coefficients(3))
    assert boundary_actual == Fraction(88, 945)
    assert boundary_theta == Fraction(-49676, 25515)
    assert mod_fraction(boundary_actual, 11) == 0
    assert mod_fraction(boundary_theta, 11) == 0

    # Verify the p-independent universal recurrence directly over Q.
    universal = universal_coefficients(160)
    for v in range(0, 160):
        cm1 = universal[v - 1] if v >= 1 else 0
        cm2 = universal[v - 2] if v >= 2 else 0
        assert 9 * (v + 1) * universal[v + 1] == (
            -3 * (v + 10) * universal[v]
            + (9 * v - 5) * cm1
            + (3 * v - 4) * cm2
        )

    rows: list[tuple[int, ...]] = []
    for p in range(17, 1001, 6):
        if not is_prime(p):
            continue
        s = (p - 5) // 6
        m = 2 * s + 1
        assert m == (p - 2) // 3 and m >= 5 and 2 * m + 3 < p
        actual_coeffs = actual_coefficients(s)
        fixed_coeffs = universal_coefficients(m)
        for d, c in zip(actual_coeffs, fixed_coeffs):
            assert d % p == mod_fraction(c, p)
        actual_value = prefix_form(actual_coeffs)
        theta = prefix_form(fixed_coeffs)
        actual_residue = mod_fraction(actual_value, p)
        theta_residue = mod_fraction(theta, p)
        assert actual_residue == theta_residue
        assert mod_fraction(fixed_coeffs[-1], p) == p - 1
        assert mod_fraction(fixed_coeffs[-2], p) == (-m) % p
        rows.append((p, s, m, actual_residue))

    result = {
        "schema": "item249-root-independent-probe-v1",
        "imports_item_code": False,
        "exact_s_rows_checked": 80,
        "prime_max_inclusive": 1000,
        "prime_rows": len(rows),
        "zero_count": sum(value == 0 for _, _, _, value in rows),
        "row_digest_sha256": sha_rows(rows),
        "boundary": {
            "p": 11,
            "s": 1,
            "actual": [boundary_actual.numerator, boundary_actual.denominator],
            "theta": [boundary_theta.numerator, boundary_theta.denominator],
            "both_zero_mod_p": True,
        },
        "checks": [
            "direct polynomial expansion",
            "direct logarithmic-derivative polynomial identity",
            "exact row recurrence and terminal coefficients",
            "triangular sum equals prefix sum",
            "universal rational recurrence through degree 160",
            "termwise finite-field reduction and functional equality",
            "complete denominator-unit inequalities on sampled prime rows",
        ],
    }
    output = HERE / "item249_root_independent_probe.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
