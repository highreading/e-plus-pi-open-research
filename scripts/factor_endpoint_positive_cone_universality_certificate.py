#!/usr/bin/env python3
"""Exact algebraic certificate for factor-endpoint cone universality.

The infinite-dimensional positive-extension and convex-duality arguments
are proved in the companion source note.  This script verifies all concrete
polynomial identities, quotient remainders, moment sequences, and order-unit
data used by that proof with integer and rational arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


H_ORDER_UNIT = [3, 8, 3]
H_TARGET_ZERO = [68, 16, 68, 16]  # (1+x^2)(68+16x)


def fraction_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def derangement(n: int) -> int:
    if n == 0:
        return 1
    previous, current = 1, 0
    for k in range(2, n + 1):
        previous, current = current, (k - 1) * (previous + current)
    return current


def a_monomial(n: int) -> int:
    return (-1) ** n * derangement(n)


def f_from_h(h: list[int]) -> list[int]:
    f = [0] * (len(h) + 2)
    for k, value in enumerate(h):
        f[k] += value
        f[k + 1] -= 2 * value
        f[k + 2] += value
    return f


def real_h_at_i(h: list[int]) -> int:
    return sum(
        (1 if k % 4 == 0 else -1 if k % 4 == 2 else 0) * value
        for k, value in enumerate(h)
    )


def target_from_h(h: list[int]) -> int:
    return sum(
        (2 if k % 4 == 1 else -2 if k % 4 == 3 else 0) * value
        for k, value in enumerate(h)
    )


def divide_extension(h: list[int]) -> tuple[list[int], list[int]]:
    """Divide F-a by 1+x^2; return quotient and degree<2 remainder."""
    f = f_from_h(h)
    target = target_from_h(h)
    remainder = f[:]
    remainder[0] -= target
    quotient = [0] * (len(remainder) - 2)
    for degree in range(len(remainder) - 1, 1, -1):
        quotient[degree - 2] = remainder[degree]
        remainder[degree - 2] -= remainder[degree]
        remainder[degree] = 0
    return quotient, remainder[:2]


def output_data(h: list[int]) -> dict[str, object]:
    f = f_from_h(h)
    r_value = real_h_at_i(h)
    target = target_from_h(h)
    a_value = sum(coefficient * a_monomial(k) for k, coefficient in enumerate(f))
    alpha = a_value - target
    b_value = sum(
        (-1) ** k * math.factorial(k) * coefficient
        for k, coefficient in enumerate(f)
    )
    quotient, remainder = divide_extension(h)
    correction = sum(
        (Fraction(4 * coefficient, k + 1) for k, coefficient in enumerate(quotient)),
        Fraction(0),
    )
    return {
        "r": r_value,
        "a": target,
        "A": a_value,
        "alpha": alpha,
        "B": b_value,
        "Q": quotient,
        "remainder": remainder,
        "I": correction,
        "c": correction - b_value,
        "F": f,
    }


def polynomial_hash(coefficients: list[int]) -> str:
    payload = ",".join(str(value) for value in coefficients).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def monomial_extension_record(maximum_n: int = 256) -> dict[str, object]:
    maximum_alpha_digits = 0
    last_records = []
    for n in range(maximum_n + 1):
        h = [0] * (n + 1)
        h[n] = 1
        data = output_data(h)
        r_value = 1 if n % 4 == 0 else -1 if n % 4 == 2 else 0
        target = 2 if n % 4 == 1 else -2 if n % 4 == 3 else 0
        assert data["r"] == r_value
        assert data["a"] == target
        # F-a=(1+x^2)Q-2*r*x for every real polynomial H, by evaluation
        # at i and -i.  Verify it coefficientwise on a basis prefix.
        assert data["remainder"] == [0, -2 * r_value]

        expected_A = (
            (n * n + 5 * n + 5) * ((-1) ** n) * derangement(n)
            - (n + 3)
        )
        assert data["A"] == expected_A
        expected_B = (
            (-1) ** n
            * (n * n + 5 * n + 5)
            * math.factorial(n)
        )
        assert data["B"] == expected_B
        expected_alpha = expected_A - target
        assert data["alpha"] == expected_alpha
        maximum_alpha_digits = max(maximum_alpha_digits, len(str(abs(expected_alpha))))
        if n >= maximum_n - 3:
            last_records.append(
                {
                    "n": n,
                    "r": r_value,
                    "a": target,
                    "alpha_digits": len(str(abs(expected_alpha))),
                    "alpha_sign": 1 if expected_alpha > 0 else -1,
                }
            )

    return {
        "checked_through_n": maximum_n,
        "remainder_identity": "F-a=(1+x^2)Q-2*r*x",
        "A_formula": "(n^2+5n+5)*(-1)^n*!n-(n+3)",
        "B_formula": "(-1)^n*(n^2+5n+5)*n!",
        "maximum_alpha_digits": maximum_alpha_digits,
        "last_records": last_records,
    }


def order_unit_record() -> dict[str, object]:
    data = output_data(H_ORDER_UNIT)
    assert data["r"] == 0
    assert data["alpha"] == 0
    assert data["a"] == 16
    assert data["B"] == 41
    assert data["I"] == -44
    assert data["c"] == -85
    # 3+8x+3x^2 >= 3 on [0,1].
    return {
        "H": H_ORDER_UNIT,
        "H_hash": polynomial_hash(H_ORDER_UNIT),
        "pointwise_lower_bound": 3,
        "output": {"a": 16, "c": -85},
        "common_constraints": {"r": 0, "alpha": 0},
    }


def target_zero_record() -> dict[str, object]:
    data = output_data(H_TARGET_ZERO)
    assert data["r"] == 0
    assert data["alpha"] == 0
    assert data["a"] == 0
    assert data["A"] == 0
    assert data["B"] == -36
    assert data["I"] == 96
    assert data["c"] == 132
    # H=(1+x^2)(68+16x)>0 on [0,1].
    return {
        "H": H_TARGET_ZERO,
        "factorization": "(1+x^2)*(68+16*x)",
        "strictly_positive_lower_bound": 68,
        "output": {"a": 0, "c": 132},
        "common_constraints": {"r": 0, "alpha": 0},
    }


def constraint_independence_record() -> dict[str, object]:
    one = output_data([1])
    x = output_data([0, 1])
    matrix = [
        [int(one["r"]), int(x["r"])],
        [int(one["alpha"]), int(x["alpha"])],
    ]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    assert matrix == [[1, 0], [2, -6]]
    assert determinant == -6
    return {"matrix_on_basis_1_x": matrix, "determinant": determinant}


def periodic_moment_record() -> dict[str, object]:
    rows = []
    for n in range(4):
        h = [0] * (n + 1)
        h[n] = 1
        rows.append([real_h_at_i(h), target_from_h(h)])
    assert rows == [[1, 0], [0, 2], [-1, 0], [0, -2]]
    # beta*a_n+gamma*r_n has values gamma,2beta,-gamma,-2beta.
    # A convergent periodic sequence forces beta=gamma=0.
    return {
        "rows_r_a_for_n_mod_4": rows,
        "linear_combination_cycle": ["gamma", "2*beta", "-gamma", "-2*beta"],
        "convergence_solution": {"beta": 0, "gamma": 0},
    }


def build_certificate() -> dict[str, object]:
    return {
        "title": "Factor-endpoint positive output cone universality",
        "arithmetic": "exact integer and rational checks",
        "definitions": {
            "r": "Re H(i)",
            "a": "2 Im H(i)",
            "alpha": "A((1-x)^2 H)-a",
            "c": "-B((1-x)^2 H)+4 integral(Q_H)",
            "division": "(1-x)^2 H-a=(1+x^2)Q_H-2*r*x",
            "kernel_identity": (
                "J=(e+pi)*a+c+e*alpha-4*log(2)*r"
            ),
        },
        "constraint_independence": constraint_independence_record(),
        "strict_positive_order_unit": order_unit_record(),
        "strict_positive_target_zero_direction": target_zero_record(),
        "monomial_extension_audit": monomial_extension_record(),
        "periodic_moment_audit": periodic_moment_record(),
        "proved_in_companion_note": {
            "real_output_cone": "{(0,0)} union {(a,c): (e+pi)*a+c>0}",
            "primitive_integer_outputs": (
                "all primitive (q,k) in Z^2 with q*(e+pi)+k>0"
            ),
            "lower_approximant_realizability": (
                "every coprime q>0,p with p/q<e+pi has primitive output (q,-p)"
            ),
            "logical_equivalence": (
                "an infinite shrinking realized family exists iff e+pi is irrational"
            ),
        },
        "scope": (
            "algebraic inputs are machine checked; positive extension, moment duality, "
            "finite-dimensional bipolarity, and rational lifting are proved in the note"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "factor_endpoint_positive_cone_universality_certificate.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
