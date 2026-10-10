#!/usr/bin/env python3
"""Exact finite checks for the Stein--Robin common-kernel parameterization."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


X = sp.symbols("x")


def stein(polynomial: sp.Expr) -> sp.Expr:
    return sp.expand((1 - X) * sp.diff(polynomial, X) - X * polynomial)


def functional_a(polynomial: sp.Expr) -> sp.Expr:
    polynomial = sp.Poly(sp.expand(polynomial), X)
    if polynomial.is_zero:
        return sp.Integer(0)
    return sp.simplify(
        sum(
            (-1) ** order
            * sp.diff(polynomial.as_expr(), X, order).subs(X, 1)
            for order in range(polynomial.degree() + 1)
        )
    )


def endpoint_zero(polynomial: sp.Expr) -> bool:
    return sp.rem(sp.Poly(stein(polynomial), X), sp.Poly(1 + X**2, X)).is_zero


def inverse_stein(integer_coefficients: list[int]) -> list[int]:
    """Invert T on an integral kernel vector, coefficients ascending."""
    while len(integer_coefficients) > 1 and integer_coefficients[-1] == 0:
        integer_coefficients.pop()
    degree = len(integer_coefficients) - 1
    if degree == 0:
        assert integer_coefficients[0] == 0
        return [0]
    p = [0] * degree
    p[degree - 1] = -integer_coefficients[degree]
    for level in range(degree - 1, 0, -1):
        p_level_plus_one = p[level + 1] if level + 1 < degree else 0
        p[level - 1] = (
            (level + 1) * p_level_plus_one
            - level * p[level]
            - integer_coefficients[level]
        )
    return p


def expression_from_coefficients(coefficients: list[int]) -> sp.Expr:
    return sum(value * X**index for index, value in enumerate(coefficients))


def stein_and_inverse_checks() -> dict[str, object]:
    direct_checks = 0
    inverse_checks = 0
    kernel_vectors = 0
    for degree in range(0, 6):
        for coefficients in itertools.product(range(-1, 2), repeat=degree + 1):
            polynomial = expression_from_coefficients(list(coefficients))
            image = stein(polynomial)
            assert functional_a(image) == 0
            direct_checks += 1

    for degree in range(0, 5):
        for coefficients_tuple in itertools.product(
            range(-2, 3), repeat=degree + 1
        ):
            coefficients = list(coefficients_tuple)
            polynomial = expression_from_coefficients(coefficients)
            if functional_a(polynomial) != 0:
                continue
            recovered = inverse_stein(coefficients[:])
            recovered_polynomial = expression_from_coefficients(recovered)
            assert sp.expand(stein(recovered_polynomial) - polynomial) == 0
            assert all(isinstance(value, int) for value in recovered)
            kernel_vectors += 1
            inverse_checks += 1

    return {
        "direct_integer_box_checks": direct_checks,
        "integral_inverse_kernel_vectors": kernel_vectors,
        "integral_inverse_checks": inverse_checks,
    }


def robin_lattice_checks() -> dict[str, object]:
    alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
    remainder_polynomial = alpha + beta * X + gamma * X**2 + delta * X**3
    remainder = sp.Poly(
        sp.rem(
            sp.Poly(stein(remainder_polynomial), X),
            sp.Poly(1 + X**2, X),
        ),
        X,
    )
    expected_remainder = (
        2 * beta + 2 * gamma - 4 * delta
        + X * (-alpha - beta + 3 * gamma + 3 * delta)
    )
    assert sp.expand(remainder.as_expr() - expected_remainder) == 0

    r_one = 1 + 2 * X + X**3
    r_two = 9 * X - X**2 + 4 * X**3
    assert sp.expand(
        stein(r_one) + (1 + X**2) * (X**2 + 3 * X - 2)
    ) == 0
    assert sp.expand(
        stein(r_two) + (1 + X**2) * (4 * X**2 + 11 * X - 9)
    ) == 0

    filtered = 0
    reverse_checks = 0
    modulus_square = sp.Poly((1 + X**2) ** 2, X)
    for coefficients in itertools.product(range(-1, 2), repeat=6):
        polynomial = expression_from_coefficients(list(coefficients))
        if not endpoint_zero(polynomial):
            continue
        quotient, rem = sp.div(sp.Poly(polynomial, X), modulus_square)
        rem_coefficients = [int(rem.nth(index)) for index in range(4)]
        u_value = rem_coefficients[0]
        numerator = rem_coefficients[1] - 2 * u_value
        assert numerator % 9 == 0
        v_value = numerator // 9
        predicted = u_value * r_one + v_value * r_two
        assert sp.expand(rem.as_expr() - predicted) == 0
        reconstructed = sp.expand(
            modulus_square.as_expr() * quotient.as_expr() + predicted
        )
        assert sp.expand(reconstructed - polynomial) == 0
        filtered += 1
        reverse_checks += 1

    forward_checks = 0
    for u_value in range(-2, 3):
        for v_value in range(-2, 3):
            for q_coefficients in itertools.product(range(-1, 2), repeat=3):
                q_polynomial = expression_from_coefficients(list(q_coefficients))
                polynomial = sp.expand(
                    (1 + X**2) ** 2 * q_polynomial
                    + u_value * r_one
                    + v_value * r_two
                )
                assert endpoint_zero(polynomial)
                forward_checks += 1

    return {
        "symbolic_remainder": str(remainder.as_expr()),
        "filtered_integer_polynomials": filtered,
        "reverse_lattice_checks": reverse_checks,
        "forward_lattice_checks": forward_checks,
        "R1": str(r_one),
        "R2": str(r_two),
    }


def output_coordinate_checks() -> dict[str, object]:
    target = sp.symbols("a", integer=True)
    r_one = 1 + 2 * X + X**3
    r_two = 9 * X - X**2 + 4 * X**3
    checks = 0
    representatives: list[dict[str, object]] = []
    for q_coefficients, u_value, v_value in [
        ((1, -2, 3), 2, -1),
        ((-3, 0, 1, 2), -4, 3),
        ((5,), 0, 1),
        ((0, 1, -1, 1, -1), 7, -2),
    ]:
        q_polynomial = expression_from_coefficients(list(q_coefficients))
        p_polynomial = sp.expand(
            (1 + X**2) ** 2 * q_polynomial
            + u_value * r_one
            + v_value * r_two
        )
        image = stein(p_polynomial)
        quotient, remainder = sp.div(
            sp.Poly(image, X), sp.Poly(1 + X**2, X)
        )
        assert remainder.is_zero
        f_polynomial = sp.expand(target + image)
        assert sp.simplify(functional_a(f_polynomial) - target) == 0
        assert sp.simplify(f_polynomial.subs(X, sp.I) - target) == 0
        assert sp.simplify(f_polynomial.subs(X, -sp.I) - target) == 0

        boundary_zero_sum = sum(
            (-1) ** order
            * sp.diff(f_polynomial, X, order).subs(X, 0)
            for order in range(sp.Poly(f_polynomial, X).degree() + 1)
        )
        assert sp.simplify(boundary_zero_sum - (target + p_polynomial.subs(X, 0))) == 0
        rational_coordinate = sp.integrate(quotient.as_expr(), (X, 0, 1))
        proposed_constant = sp.simplify(
            -target - p_polynomial.subs(X, 0) + 4 * rational_coordinate
        )
        standard_constant = sp.simplify(
            -boundary_zero_sum + 4 * rational_coordinate
        )
        assert sp.simplify(proposed_constant - standard_constant) == 0
        checks += 1
        representatives.append(
            {
                "Q_coefficients_ascending": list(q_coefficients),
                "u": u_value,
                "v": v_value,
                "P": str(p_polynomial),
                "G": str(quotient.as_expr()),
                "constant_coordinate": str(proposed_constant),
            }
        )

    derivative_identity = sp.simplify(
        sp.diff(sp.exp(X) * (1 - X) * sp.Function("P")(X), X)
        - sp.exp(X)
        * (
            (1 - X) * sp.diff(sp.Function("P")(X), X)
            - X * sp.Function("P")(X)
        )
    )
    assert derivative_identity == 0
    return {
        "exact_output_checks": checks,
        "boundary_primitive_identity": True,
        "representative_records": representatives,
    }


def taylor_checks() -> dict[str, object]:
    checks = 0
    records = []
    for degree in range(1, 41):
        target = math.factorial(degree)
        polynomial = sp.expand(
            target
            * sum(
                (1 - X) ** index / math.factorial(index + 1)
                for index in range(degree)
            )
        )
        assert sp.Poly(polynomial, X).domain == sp.ZZ
        residual = sp.expand(target + stein(polynomial))
        assert sp.expand(residual - (1 - X) ** degree) == 0
        endpoint_failure = sp.expand(residual.subs(X, sp.I) - target)
        assert endpoint_failure != 0
        checks += 1
        if degree in [1, 2, 3, 10, 20, 40]:
            records.append(
                {
                    "N": degree,
                    "a_N": target,
                    "P_N": str(polynomial),
                    "endpoint_failure": str(endpoint_failure),
                }
            )
    monomial_cone_checks = 0
    w_value = 1 - sp.I
    for degree in range(2, 201):
        difference = sp.factorial(degree) - sp.re(w_value**degree)
        assert difference > 0
        monomial_cone_checks += 1
    return {
        "telescoping_checks": checks,
        "range": [1, 40],
        "positive_monomial_cone_checks": monomial_cone_checks,
        "positive_monomial_cone_range": [2, 200],
        "representative_records": records,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact diagnostics for the Stein operator, integral inverse, "
            "Robin lattice, output coordinate, and positive Taylor near miss"
        ),
        "stein_kernel": stein_and_inverse_checks(),
        "robin_lattice": robin_lattice_checks(),
        "output_coordinate": output_coordinate_checks(),
        "positive_taylor_truncations": taylor_checks(),
        "status": (
            "finite diagnostic; the all-degree bijection and lattice theorem "
            "are proved symbolically in the companion source; no all-degree "
            "positive Robin correction or arithmetic classification is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "common_kernel_stein_robin_certificate.json"
    )
    parser.add_argument("--output", type=Path, default=default_output)
    arguments = parser.parse_args()
    payload = build_payload()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_bytes(encoded)
    print(f"wrote {arguments.output}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
