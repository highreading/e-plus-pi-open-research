#!/usr/bin/env python3
"""Exact certificate for the inverse-cubic trace-polynomial no-go.

The script independently derives the order-three ODE and its eight-term
coefficient recurrence, constructs the trace polynomial as a cubic
remainder, checks it against direct local residues on all three inverse
branches for small m, and verifies every nontrivial recurrence row.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


t, z, n = sp.symbols("t z n")
k_symbol = sp.symbols("k", integer=True)
m_symbol = sp.symbols("m", integer=True, positive=True)
u = sp.symbols("u")

phi = t**3 - 2 * t**2 + 2 * t
phi_prime = sp.diff(phi, t)
A = -2 + 3 * t - t**2


def derive_recurrence() -> tuple[dict[int, sp.Expr], dict[str, object]]:
    """Derive the exact recurrence from the cubic-field total derivative."""

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
        ratios.append(
            reduce_algebraic(
                sp.diff(ratios[-1], z)
                + sp.diff(ratios[-1], t) / phi_prime
                + ratios[-1] * log_derivative
            )
        )

    matrix = sp.Matrix(
        [
            [
                sp.Poly(ratios[column], t).coeff_monomial(t**row)
                for column in range(4)
            ]
            for row in range(3)
        ]
    )
    nullspace = matrix.nullspace()
    assert len(nullspace) == 1
    ode_coefficients = [
        sp.factor(value / nullspace[0][-1]) for value in nullspace[0]
    ]
    null_residuals = [sp.factor(value) for value in matrix * sp.Matrix(ode_coefficients)]

    # Verify on the unreduced algebraic branch as well as in the quotient.
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
                k_symbol - z_power + j
                for j in range(1, derivative_order + 1)
            )
            recurrence[shift] = recurrence.get(shift, 0) + coefficient * falling
    recurrence = {
        shift: sp.factor(value) for shift, value in recurrence.items()
    }

    expected_lower_edge = (
        5
        * (5 * n - 4)
        * (5 * n - 1)
        * (3 * k_symbol - 2 * n - 10)
        * (3 * k_symbol - 2 * n - 9)
        * (3 * k_symbol - 2 * n - 8)
    )
    lower_edge_matches = sp.factor(recurrence[-4] - expected_lower_edge) == 0
    boundary_pivot = sp.factor(
        recurrence[-4].subs({n: 6 * m_symbol, k_symbol: 4 * m_symbol + 3})
    )

    checks = {
        "ode_identity_residual": str(ode_residual),
        "quotient_nullspace_residuals": [str(value) for value in null_residuals],
        "recurrence_min_shift": min(recurrence),
        "recurrence_max_shift": max(recurrence),
        "lower_edge": str(recurrence[-4]),
        "lower_edge_matches_certified_factorization": lower_edge_matches,
        "boundary_pivot_C_minus_4_at_k_4m_plus_3_n_6m": str(boundary_pivot),
        "passed": (
            ode_residual == 0
            and all(value == 0 for value in null_residuals)
            and min(recurrence) == -4
            and max(recurrence) == 3
            and lower_edge_matches
            and boundary_pivot == 0
        ),
    }
    return recurrence, checks


def trace_polynomial(m: int) -> sp.Poly:
    """Return [t^2] rem_t(A^(6m), phi-z)."""

    domain = sp.QQ[z]
    remainder = sp.Poly(A ** (6 * m), t, domain=domain).rem(
        sp.Poly(phi - z, t, domain=domain)
    )
    return sp.Poly(remainder.coeff_monomial(t**2), z, domain=sp.QQ)


def local_branch_coefficient(m: int, root: sp.Expr, degree: int) -> sp.Expr:
    """Compute Res_root A^(6m) phi^(-degree-1) dt exactly."""

    shifted_phi = sp.cancel(phi.subs(t, root + u) / u)
    analytic_part = A.subs(t, root + u) ** (6 * m) / shifted_phi ** (degree + 1)
    return sp.simplify(
        sp.series(analytic_part, u, 0, degree + 1)
        .removeO()
        .expand()
        .coeff(u, degree)
    )


def sample_check(
    m: int, recurrence: dict[int, sp.Expr], direct_branch_max_m: int
) -> dict[str, object]:
    trace = trace_polynomial(m)
    target = 4 * m
    coefficients = [int(trace.nth(index)) for index in range(trace.degree() + 1)]
    content = math.gcd(*[abs(value) for value in coefficients])

    recurrence_rows = []
    for index in range(trace.degree() + 5):
        total = 0
        for shift, expression in recurrence.items():
            coefficient_index = index + shift
            coefficient = (
                int(trace.nth(coefficient_index))
                if 0 <= coefficient_index <= trace.degree()
                else 0
            )
            factor = int(expression.subs({n: 6 * m, k_symbol: index}))
            total += factor * coefficient
        recurrence_rows.append(total == 0)

    direct_indices: list[int] = []
    direct_checks: list[bool] = []
    if m <= direct_branch_max_m:
        direct_indices = sorted({0, 1, 2, target - 1, target, target + 1, target + 2})
        roots = [sp.Integer(0), 1 + sp.I, 1 - sp.I]
        for degree in direct_indices:
            branch_sum = sp.simplify(
                sum(local_branch_coefficient(m, root, degree) for root in roots)
            )
            expected = trace.nth(degree)
            direct_checks.append(sp.simplify(branch_sum - expected) == 0)

    degree_ok = trace.degree() == target - 1
    leading_ok = trace.LC() == -10 * m
    tail_ok = all(trace.nth(degree) == 0 for degree in range(target, target + 3))
    recurrence_ok = all(recurrence_rows)
    direct_ok = all(direct_checks)
    passed = degree_ok and leading_ok and tail_ok and recurrence_ok and direct_ok
    return {
        "m": m,
        "trace_degree": trace.degree(),
        "trace_leading_coefficient": str(trace.LC()),
        "trace_content": str(content),
        "target": target,
        "target_triple": [str(trace.nth(target + offset)) for offset in range(3)],
        "recurrence_rows_checked": len(recurrence_rows),
        "all_recurrence_rows_pass": recurrence_ok,
        "direct_branch_trace_indices": direct_indices,
        "direct_branch_trace_checks": direct_checks,
        "passed": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=12)
    parser.add_argument("--direct-branch-max-m", type=int, default=4)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    recurrence, symbolic = derive_recurrence()
    samples = [
        sample_check(m, recurrence, arguments.direct_branch_max_m)
        for m in range(1, arguments.max_m + 1)
    ]
    all_pass = bool(symbolic["passed"] and all(row["passed"] for row in samples))
    result = {
        "schema": "inverse-cubic-trace-polynomial-no-go-v1",
        "theorem": {
            "trace_definition": "sum_i A(T_i(z))^(6m)/phi'(T_i(z))",
            "polynomial_remainder_identity": "trace=[t^2]rem_t(A(t)^(6m),phi(t)-z)",
            "degree": "4m-1",
            "leading_coefficient": "-10m",
            "fresh_prime_consequence": (
                "for every prime p>6m the trace is nonzero mod p but all "
                "coefficients from degree 4m onward vanish"
            ),
            "scope": (
                "no-go for recurrence-plus-zero-tail propagation only; "
                "does not rule out branch-specific Cartier arguments"
            ),
        },
        "symbolic": symbolic,
        "sample_max_m": arguments.max_m,
        "direct_branch_max_m": arguments.direct_branch_max_m,
        "samples": samples,
        "all_pass": all_pass,
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    print(
        f"symbolic={symbolic['passed']}; samples={all(row['passed'] for row in samples)}; "
        f"m=1..{arguments.max_m}; direct_branches=1..{arguments.direct_branch_max_m}; "
        f"sha256={digest}"
    )
    if not all_pass:
        raise SystemExit(1)
    if arguments.output:
        arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
