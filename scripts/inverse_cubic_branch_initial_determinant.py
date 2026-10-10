#!/usr/bin/env python3
"""Item-156 certificate for the branch-initial determinant.

This extends, and does not replace, the frozen item-155 distinguished/trace
transversality certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


t, z, u = sp.symbols("t z u")
n = sp.symbols("n", integer=True, positive=True)
m_symbol = sp.symbols("m", integer=True, positive=True)

phi = t**3 - 2 * t**2 + 2 * t
A = -2 + 3 * t - t**2


def wedge(left: list[sp.Expr], right: list[sp.Expr]) -> list[sp.Expr]:
    return [
        sp.factor(left[i] * right[j] - left[j] * right[i])
        for i in range(3)
        for j in range(i + 1, 3)
    ]


def symbolic_checks() -> dict[str, object]:
    phi_prime = sp.diff(phi, t)
    log_derivative = (
        n * sp.diff(A, t) / A - sp.diff(phi_prime, t) / phi_prime
    ) / phi_prime
    log_at_zero = sp.factor(log_derivative.subs(t, 0))
    second_ratio = sp.factor(
        (
            sp.diff(log_derivative, t).subs(t, 0) / phi_prime.subs(t, 0)
            + log_at_zero**2
        )
        / 2
    )
    expected_log = 1 - 3 * n / 4
    expected_second = (9 * n**2 - 41 * n + 36) / 32

    alpha = 1 + sp.I
    shifted_phi = sp.cancel(phi.subs(t, alpha + u) / u)
    branch_ratios = []
    for degree in range(3):
        analytic_part = A.subs(t, alpha + u) ** n / shifted_phi ** (degree + 1)
        coefficient = sp.simplify(
            sp.diff(analytic_part, u, degree).subs(u, 0) / sp.factorial(degree)
        )
        branch_ratios.append(sp.factor(coefficient / alpha**n))

    expected_branch_ratios = [
        -(1 + sp.I) / 4,
        (3 * n - 4) / 16 - sp.I * (n + 2) / 16,
        (-n**2 + 25 * n - 36) / 128
        + sp.I * (7 * n**2 - 21 * n - 6) / 128,
    ]
    branch_ratio_checks = [
        sp.simplify(actual - expected) == 0
        for actual, expected in zip(branch_ratios, expected_branch_ratios)
    ]
    distinguished_ratios = sp.Matrix(
        [
            1,
            1 - 3 * n / 4,
            (9 * n**2 - 41 * n + 36) / 32,
        ]
    )
    alpha_ratios = sp.Matrix(expected_branch_ratios)
    conjugate_ratios = alpha_ratios.conjugate().subs(sp.conjugate(n), n)
    normalized_initial_determinant = sp.factor(
        sp.Matrix.hstack(
            distinguished_ratios, alpha_ratios, conjugate_ratios
        ).det()
    )
    expected_normalized_determinant = (
        -sp.I * n * (n - 2) * (2 * n - 1) / 64
    )
    initial_determinant_check = (
        sp.simplify(
            normalized_initial_determinant - expected_normalized_determinant
        )
        == 0
    )

    n_value = 6 * m_symbol
    distinguished = [
        32,
        32 - 24 * n_value,
        9 * n_value**2 - 41 * n_value + 36,
    ]
    even_vector = [
        -32,
        24 * n_value - 32,
        -n_value**2 + 25 * n_value - 36,
    ]
    odd_vector = [
        -32,
        -8 * n_value - 16,
        7 * n_value**2 - 21 * n_value - 6,
    ]
    even_wedge = wedge(even_vector, distinguished)
    odd_wedge = wedge(odd_vector, distinguished)
    expected_even_wedge = [
        0,
        -3072 * m_symbol * (3 * m_symbol - 1),
        1536 * m_symbol * (3 * m_symbol - 1) * (9 * m_symbol - 2),
    ]
    expected_odd_wedge = [
        512 * (12 * m_symbol - 1),
        -192 * (96 * m_symbol**2 - 62 * m_symbol + 5),
        384
        * (2 * m_symbol - 1)
        * (3 * m_symbol - 1)
        * (9 * m_symbol - 1),
    ]
    even_wedge_checks = [
        sp.factor(actual - expected) == 0
        for actual, expected in zip(even_wedge, expected_even_wedge)
    ]
    odd_wedge_checks = [
        sp.factor(actual - expected) == 0
        for actual, expected in zip(odd_wedge, expected_odd_wedge)
    ]

    quadratic = 96 * m_symbol**2 - 62 * m_symbol + 5
    quadratic_under_12m_equals_1 = sp.factor(
        quadratic.subs(m_symbol, sp.Rational(1, 12))
    )
    passed = (
        sp.simplify(log_at_zero - expected_log) == 0
        and sp.simplify(second_ratio - expected_second) == 0
        and all(branch_ratio_checks)
        and initial_determinant_check
        and all(even_wedge_checks)
        and all(odd_wedge_checks)
        and quadratic_under_12m_equals_1 == sp.Rational(1, 2)
    )
    return {
        "distinguished_log_derivative_at_zero": str(log_at_zero),
        "distinguished_second_coefficient_ratio": str(second_ratio),
        "alpha_branch_ratios_degrees_0_1_2": [str(value) for value in branch_ratios],
        "alpha_branch_ratio_checks": branch_ratio_checks,
        "normalized_three_branch_initial_determinant": str(
            normalized_initial_determinant
        ),
        "actual_three_branch_initial_determinant": (
            "-I*2^(2n-7)*n*(n-2)*(2n-1)"
        ),
        "three_branch_initial_determinant_check": initial_determinant_check,
        "fresh_prime_initial_rank_degeneracy": "p=2n-1=12m-1 only",
        "even_wedge": [str(value) for value in even_wedge],
        "even_wedge_checks": even_wedge_checks,
        "odd_wedge": [str(value) for value in odd_wedge],
        "odd_wedge_checks": odd_wedge_checks,
        "odd_case_quadratic_under_12m_equals_1": str(
            quadratic_under_12m_equals_1
        ),
        "passed": bool(passed),
    }


def trace_initial_by_remainder(m: int) -> list[int]:
    remainder = sp.Poly(A ** (6 * m), t, domain=sp.QQ[z]).rem(
        sp.Poly(phi - z, t, domain=sp.QQ[z])
    )
    trace = sp.Poly(remainder.coeff_monomial(t**2), z, domain=sp.QQ)
    return [int(trace.nth(index)) for index in range(3)]


def closed_vectors(m: int) -> tuple[list[int], list[int], list[int]]:
    n_value = 6 * m
    distinguished = [
        32,
        32 - 24 * n_value,
        9 * n_value**2 - 41 * n_value + 36,
    ]
    even_vector = [
        -32,
        24 * n_value - 32,
        -n_value**2 + 25 * n_value - 36,
    ]
    odd_vector = [
        -32,
        -8 * n_value - 16,
        7 * n_value**2 - 21 * n_value - 6,
    ]
    phase = m % 4
    conjugate = (
        even_vector
        if phase == 0
        else odd_vector
        if phase == 1
        else [-value for value in even_vector]
        if phase == 2
        else [-value for value in odd_vector]
    )
    distinguished_scale = Fraction(2) ** (6 * m - 6)
    conjugate_scale = Fraction(2) ** (3 * m - 6)
    distinguished_actual = [
        distinguished_scale * value for value in distinguished
    ]
    trace = [
        distinguished_actual[index] + conjugate_scale * conjugate[index]
        for index in range(3)
    ]
    assert all(value.denominator == 1 for value in trace)
    return distinguished, conjugate, [int(value) for value in trace]


def integer_wedge(left: list[int], right: list[int]) -> list[int]:
    return [
        left[i] * right[j] - left[j] * right[i]
        for i in range(3)
        for j in range(i + 1, 3)
    ]


def sample_check(m: int) -> dict[str, object]:
    distinguished, conjugate, trace_closed = closed_vectors(m)
    trace_direct = trace_initial_by_remainder(m)
    minors = integer_wedge(trace_closed, distinguished)
    actual_gcd = math.gcd(*(abs(value) for value in minors))
    expected_gcd = (
        2 ** (3 * m)
        if m % 2
        else 3 * 2 ** (3 * m + 4) * m * (3 * m - 1)
    )
    passed = trace_closed == trace_direct and actual_gcd == expected_gcd
    return {
        "m": m,
        "parity": "odd" if m % 2 else "even",
        "distinguished_scaled_initial_vector": distinguished,
        "conjugate_scaled_initial_vector": conjugate,
        "trace_initial_vector": trace_closed,
        "trace_matches_cubic_remainder": trace_closed == trace_direct,
        "wedge_minors": [str(value) for value in minors],
        "wedge_gcd": str(actual_gcd),
        "expected_wedge_gcd": str(expected_gcd),
        "passed": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=20)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    symbolic = symbolic_checks()
    samples = [sample_check(m) for m in range(1, arguments.max_m + 1)]
    all_pass = bool(symbolic["passed"] and all(row["passed"] for row in samples))
    result = {
        "schema": "inverse-cubic-branch-initial-determinant-v1",
        "depends_on_item155": {
            "role": "frozen distinguished/trace transversality theorem",
            "note_sha256": (
                "d68ab07fda6997cf5ea3b1b5c7e41ba08b8f0080d5272166a22454758c677be7"
            ),
            "certificate_sha256": (
                "f9cbc89307edc0282ccc54b8b4043f2dede09ea7c15b39634394bc4f08aeb05f"
            ),
            "json_sha256": (
                "49e2dc9215377bb54c42033c83bb29deaf43fa800f52ae118cc28d1736a95dd7"
            ),
        },
        "theorem": {
            "odd_m_wedge_gcd": "2^(3m)",
            "even_m_wedge_gcd": "3*2^(3m+4)*m*(3m-1)",
            "fresh_prime_consequence": (
                "the distinguished and trace branch series are independent mod every "
                "prime p>6m; a distinguished target triple zero forces rank <=1 for "
                "target evaluation on the span of the three genuine inverse branches"
            ),
            "degenerate_ray_caveat": (
                "at p=12m-1 the rational arbitrary-initial-coordinate transfer is not "
                "reduced; the intrinsic genuine-branch statement still applies"
            ),
            "scope": "rank-drop reduction, not a fresh-prime nonvanishing proof",
        },
        "symbolic": symbolic,
        "sample_max_m": arguments.max_m,
        "samples": samples,
        "all_pass": all_pass,
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    print(
        f"symbolic={symbolic['passed']}; samples={all(row['passed'] for row in samples)}; "
        f"m=1..{arguments.max_m}; sha256={digest}"
    )
    if not all_pass:
        raise SystemExit(1)
    if arguments.output:
        arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
