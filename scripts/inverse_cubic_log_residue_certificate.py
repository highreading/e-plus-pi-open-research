#!/usr/bin/env python3
"""Exact certificate for the inverse-cubic log-residue recurrence.

The symbolic checks are identities over QQ(n,t).  The finite sample rows
independently compare the inverse-cubic coefficients, the fixed Lambda_s
coefficients, and the resulting eight-term recurrence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


t, z, n = sp.symbols("t z n")
k_symbol = sp.symbols("k", integer=True)
phi = t**3 - 2 * t**2 + 2 * t
phi_prime = sp.diff(phi, t)
A = -2 + 3 * t - t**2


def denominator_series(order: int, cutoff: int) -> list[Fraction]:
    """Coefficients of (t^2-2t+2)^(-order)."""

    values = [Fraction(1, 2**order)]
    previous = Fraction(0)
    for degree in range(cutoff):
        current = values[degree]
        following = (
            2 * (degree + order) * current
            - (degree - 1 + 2 * order) * previous
        ) / (2 * (degree + 1))
        values.append(following)
        previous = current
    return values


def inverse_cubic_coefficient(exponent: int, degree: int) -> Fraction:
    """Return [t^degree] A(t)^exponent/R(t)^(degree+1)."""

    denominator = denominator_series(degree + 1, degree)
    answer = Fraction(0)
    # A=(-1+t)(2-t); this avoids any symbolic series computation.
    for left_degree in range(exponent + 1):
        for right_degree in range(exponent + 1):
            numerator_degree = left_degree + right_degree
            if numerator_degree > degree:
                continue
            numerator = (
                (-1) ** (exponent - left_degree)
                * math.comb(exponent, left_degree)
                * 2 ** (exponent - right_degree)
                * (-1) ** right_degree
                * math.comb(exponent, right_degree)
            )
            answer += numerator * denominator[degree - numerator_degree]
    return answer


def fixed_lambda(m: int, shift: int) -> int:
    target = 4 * m + shift
    short_degree = 1 + 3 * shift
    denominator_order = 4 * m + 1 + shift
    answer = 0
    for h in range(target // 2 + 1):
        numerator_degree = target - 2 * h
        numerator = 0
        for j in range(short_degree + 1):
            remaining = numerator_degree - j
            if 0 <= remaining <= 6 * m:
                numerator += (
                    math.comb(short_degree, j)
                    * (-1) ** remaining
                    * math.comb(6 * m, remaining)
                )
        answer += (
            (-1) ** h
            * math.comb(denominator_order + h - 1, h)
            * numerator
        )
    return answer


def symbolic_checks() -> tuple[dict[str, object], dict[int, sp.Expr]]:
    field = sp.QQ.frac_field(z, n)
    modulus = sp.Poly(phi - z, t, domain=field)

    def reduce_algebraic(expression: sp.Expr) -> sp.Expr:
        numerator, denominator = sp.fraction(sp.cancel(expression))
        numerator_poly = sp.Poly(numerator, t, domain=field)
        denominator_poly = sp.Poly(denominator, t, domain=field)
        inverse = sp.invert(denominator_poly, modulus)
        return sp.cancel((numerator_poly * inverse).rem(modulus).as_expr())

    raw_log_derivative = (
        n * sp.diff(A, t) / A - sp.diff(phi_prime, t) / phi_prime
    ) / phi_prime
    log_derivative = reduce_algebraic(raw_log_derivative)
    ratios = [sp.Integer(1)]
    for _ in range(3):
        # The explicit z derivative is essential after reduction modulo
        # phi(t)-z.  Omitting it produces a false differential equation.
        ratios.append(
            reduce_algebraic(
                sp.diff(ratios[-1], z)
                + sp.diff(ratios[-1], t) / phi_prime
                + ratios[-1] * log_derivative
            )
        )

    matrix = sp.Matrix(
        [
            [sp.Poly(ratios[column], t).coeff_monomial(t**row) for column in range(4)]
            for row in range(3)
        ]
    )
    rank_three_determinant = sp.factor(matrix[:, :3].det())
    nullspace = matrix.nullspace()
    assert len(nullspace) == 1
    ode_coefficients = [sp.factor(value / nullspace[0][-1]) for value in nullspace[0]]
    null_residuals = [
        sp.factor(value)
        for value in matrix * sp.Matrix(ode_coefficients)
    ]

    # Check the ODE against unreduced total derivatives on the actual branch.
    raw_ratios = [sp.Integer(1)]
    for _ in range(3):
        raw_ratios.append(
            sp.cancel(
                sp.diff(raw_ratios[-1], t) / phi_prime
                + raw_ratios[-1] * raw_log_derivative
            )
        )
    ode_residual = sp.factor(
        sum(
            ode_coefficients[order].subs(z, phi) * raw_ratios[order]
            for order in range(4)
        )
    )

    common_denominator = sp.lcm(
        [sp.denom(sp.cancel(value)) for value in ode_coefficients]
    )
    ode_polynomials = [
        sp.Poly(sp.cancel(common_denominator * value), z)
        for value in ode_coefficients
    ]
    recurrence: dict[int, sp.Expr] = {}
    for derivative_order, polynomial in enumerate(ode_polynomials):
        for (z_power,), coefficient in polynomial.terms():
            shift = derivative_order - z_power
            falling = sp.prod(
                k_symbol - z_power + j for j in range(1, derivative_order + 1)
            )
            recurrence[shift] = recurrence.get(shift, 0) + coefficient * falling
    recurrence = {shift: sp.factor(value) for shift, value in recurrence.items()}

    record = {
        "ode_identity_residual": str(ode_residual),
        "nullspace_residuals": [str(value) for value in null_residuals],
        "rank_three_determinant": str(rank_three_determinant),
        "rank_three_determinant_nonzero": rank_three_determinant != 0,
        "ode_coefficients_order_0_through_3": [
            str(value) for value in ode_coefficients
        ],
        "coefficient_recurrence": {
            str(shift): str(recurrence[shift]) for shift in sorted(recurrence)
        },
        "recurrence_min_shift": min(recurrence),
        "recurrence_max_shift": max(recurrence),
        "passed": (
            ode_residual == 0
            and all(value == 0 for value in null_residuals)
            and rank_three_determinant != 0
        ),
    }
    return record, recurrence


def sample_checks(
    max_m: int, recurrence: dict[int, sp.Expr]
) -> tuple[list[dict[str, object]], bool]:
    rows = []
    all_pass = True
    for m in range(1, max_m + 1):
        exponent = 6 * m
        cutoff = 4 * m + 6
        coefficients = [
            inverse_cubic_coefficient(exponent, degree) for degree in range(cutoff + 1)
        ]
        scaling_checks = []
        for shift in range(5):
            degree = 4 * m + shift
            scaling_checks.append(
                fixed_lambda(m, shift)
                == coefficients[degree] * 2 ** (2 * m + 2 * shift + 1)
            )

        recurrence_checks = []
        for index in range(cutoff - max(recurrence) + 1):
            total = Fraction(0)
            for shift, expression in recurrence.items():
                coefficient_index = index + shift
                value = (
                    coefficients[coefficient_index]
                    if 0 <= coefficient_index < len(coefficients)
                    else Fraction(0)
                )
                factor = int(expression.subs({n: exponent, k_symbol: index}))
                total += factor * value
            recurrence_checks.append(total == 0)
        passed = all(scaling_checks) and all(recurrence_checks)
        all_pass &= passed
        rows.append(
            {
                "m": m,
                "scaling_checks_s_0_through_4": scaling_checks,
                "recurrence_rows_checked": len(recurrence_checks),
                "passed": passed,
            }
        )
    return rows, all_pass


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=12)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    symbolic, recurrence = symbolic_checks()
    samples, samples_pass = sample_checks(arguments.max_m, recurrence)
    result = {
        "schema": "inverse-cubic-log-residue-certificate-v2",
        "symbolic": symbolic,
        "sample_max_m": arguments.max_m,
        "samples": samples,
        "all_pass": bool(symbolic["passed"] and samples_pass),
        "warning": (
            "The certificate proves the ODE and recurrence, not the required "
            "nonvanishing of three consecutive target coefficients."
        ),
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    print(
        f"symbolic={symbolic['passed']}; samples={samples_pass}; "
        f"m=1..{arguments.max_m}; sha256={digest}"
    )
    if not result["all_pass"]:
        raise SystemExit(1)
    if arguments.output:
        arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
