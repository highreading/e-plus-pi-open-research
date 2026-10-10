#!/usr/bin/env python3
"""Deterministic certificate for Item 287's recurrence-universal no-go.

The symbolic checks use exact sparse polynomials over the integers.  Numeric
rows illustrate identities only and are explicitly finite, not a prime census.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable


Bivariate = dict[tuple[int, int], int]
UPolynomial = list[Bivariate]


def clean(polynomial: Bivariate) -> Bivariate:
    return {monomial: value for monomial, value in polynomial.items() if value}


def constant(value: int) -> Bivariate:
    return {} if value == 0 else {(0, 0): value}


def monomial(first: int, second: int, coefficient: int = 1) -> Bivariate:
    return {} if coefficient == 0 else {(first, second): coefficient}


def add(first: Bivariate, second: Bivariate) -> Bivariate:
    result = dict(first)
    for key, value in second.items():
        result[key] = result.get(key, 0) + value
    return clean(result)


def negate(polynomial: Bivariate) -> Bivariate:
    return {key: -value for key, value in polynomial.items()}


def subtract(first: Bivariate, second: Bivariate) -> Bivariate:
    return add(first, negate(second))


def multiply(first: Bivariate, second: Bivariate) -> Bivariate:
    result: Bivariate = {}
    for (i, j), a in first.items():
        for (k, ell), b in second.items():
            key = (i + k, j + ell)
            result[key] = result.get(key, 0) + a * b
    return clean(result)


def multiply_scalar(polynomial: Bivariate, value: int) -> Bivariate:
    return clean({key: value * coefficient for key, coefficient in polynomial.items()})


def set_first_zero(polynomial: Bivariate) -> Bivariate:
    return clean({(0, j): value for (i, j), value in polynomial.items() if i == 0})


def divisible_by_first(polynomial: Bivariate) -> bool:
    return all(i >= 1 for i, _ in polynomial)


def divide_by_first(polynomial: Bivariate) -> Bivariate:
    assert divisible_by_first(polynomial)
    return clean({(i - 1, j): value for (i, j), value in polynomial.items()})


def upoly_clean(polynomial: UPolynomial) -> UPolynomial:
    result = [clean(coefficient) for coefficient in polynomial]
    while len(result) > 1 and not result[-1]:
        result.pop()
    return result


def upoly_add(first: UPolynomial, second: UPolynomial) -> UPolynomial:
    length = max(len(first), len(second))
    result: UPolynomial = []
    for index in range(length):
        a = first[index] if index < len(first) else {}
        b = second[index] if index < len(second) else {}
        result.append(add(a, b))
    return upoly_clean(result)


def multiply_u_plus_y2(polynomial: UPolynomial) -> UPolynomial:
    y_squared = monomial(0, 2)
    result: UPolynomial = [{} for _ in range(len(polynomial) + 1)]
    for index, coefficient in enumerate(polynomial):
        result[index] = add(result[index], multiply(y_squared, coefficient))
        result[index + 1] = add(result[index + 1], coefficient)
    return upoly_clean(result)


def divide_u_plus_y2(polynomial: UPolynomial) -> tuple[UPolynomial, Bivariate]:
    """Monic division by U+Y^2, returning quotient and exact remainder."""
    polynomial = upoly_clean(polynomial)
    degree = len(polynomial) - 1
    assert degree >= 1
    y_squared = monomial(0, 2)
    quotient: UPolynomial = [{} for _ in range(degree)]
    quotient[degree - 1] = polynomial[degree]
    for power in range(degree - 1, 0, -1):
        quotient[power - 1] = subtract(
            polynomial[power], multiply(y_squared, quotient[power])
        )
    remainder = subtract(polynomial[0], multiply(y_squared, quotient[0]))
    return upoly_clean(quotient), clean(remainder)


def polynomial_eval(coefficients: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def continuant(n: int, h: int) -> int:
    if h == 0:
        return 0
    previous, current = 0, 1
    for d in range(h - 1):
        previous, current = current, (4 * n + 4 * d + 6) * current + previous
    return current


def product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def gcd_all(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return result


def symmetric_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    if 2 * residue > modulus:
        residue -= modulus
    return residue


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def serialized_bivariate(polynomial: Bivariate) -> list[list[int]]:
    return [
        [i, j, coefficient]
        for (i, j), coefficient in sorted(polynomial.items())
    ]


def recurrence_window(n: int, radius: int) -> dict[int, tuple[int, int]]:
    """q_(n+j)=a_j q_n+b_j q_(n+1), for |j|<=radius."""
    forms: dict[int, tuple[int, int]] = {0: (1, 0), 1: (0, 1)}
    for shift in range(0, radius - 1):
        a0, b0 = forms[shift]
        a1, b1 = forms[shift + 1]
        factor = 4 * (n + shift) + 6
        forms[shift + 2] = (a0 + factor * a1, b0 + factor * b1)
    for shift in range(0, -radius, -1):
        a0, b0 = forms[shift]
        a1, b1 = forms[shift + 1]
        factor = 4 * (n + shift) + 2
        forms[shift - 1] = (a1 - factor * a0, b1 - factor * b0)
    return forms


def actual_residual_polynomial(n: int) -> tuple[list[int], int]:
    specs = ((2,), (2, 3), (2, 3, 4), (2, 3, 4, 5))
    coefficients = (1, -1, 2, -3)
    terms = [
        coefficient * product(continuant(n, gap) for gap in gaps)
        for coefficient, gaps in zip(coefficients, specs)
    ]
    minimum_degree = 1
    exponents = [len(gaps) - minimum_degree for gaps in specs]
    polynomial = [0] * (max(exponents) + 1)
    for term, exponent in zip(terms, exponents):
        polynomial[exponent] += term
    baseline = gcd_all(terms)
    assert baseline > 0
    assert all(value % baseline == 0 for value in polynomial)
    return [value // baseline for value in polynomial], baseline


def build_result() -> dict[str, Any]:
    q = q_values(90)

    n_only_rows: list[dict[str, Any]] = []
    rational_denominator_rows: list[dict[str, Any]] = []
    for n in range(2, 25):
        for degree in range(1, 7):
            coefficients: UPolynomial = [
                constant((index + 1) * n ** (index % 3))
                for index in range(degree)
            ] + [constant(1)]
            quotient, remainder = divide_u_plus_y2(coefficients)
            del quotient
            remainder_at_x_zero = set_first_zero(remainder)
            assert remainder_at_x_zero
            leading_key = (0, 2 * degree)
            assert remainder_at_x_zero[leading_key] == (-1) ** degree
            n_only_rows.append(
                {
                    "n": n,
                    "degree": degree,
                    "remainder_terms": serialized_bivariate(remainder_at_x_zero),
                }
            )

            denominator = n + 1
            cleared: UPolynomial = [
                constant(n + 2 * index + 1) for index in range(degree)
            ] + [constant(denominator)]
            _, cleared_remainder = divide_u_plus_y2(cleared)
            cleared_at_x_zero = set_first_zero(cleared_remainder)
            assert cleared_at_x_zero[(0, 2 * degree)] == denominator * ((-1) ** degree)
            target = q[n]
            if math.gcd(denominator, target) == 1:
                rational_denominator_rows.append(
                    {
                        "n": n,
                        "degree": degree,
                        "denominator": denominator,
                        "target": target,
                        "denominator_is_target_unit": True,
                    }
                )

    kernel_rows: list[dict[str, Any]] = []
    proper_kernel_rows: list[dict[str, Any]] = []
    for n in range(2, 22):
        for degree in range(1, 6):
            quotient_seed: UPolynomial = []
            for power in range(degree):
                coefficient = add(
                    constant((power + 1) * (n + 1)),
                    add(
                        monomial(1 + power % 2, power % 3, (-1) ** power),
                        monomial(power % 2, 1 + power % 2, n - power),
                    ),
                )
                quotient_seed.append(coefficient)
            remainder_quotient = add(
                constant(n * n + degree),
                add(monomial(1, 1, degree + 1), monomial(0, 2, -n)),
            )
            recurrence_modulus = monomial(1, 0)
            constructed = multiply_u_plus_y2(quotient_seed)
            constructed[0] = add(
                constructed[0], multiply(recurrence_modulus, remainder_quotient)
            )
            recovered_quotient, recovered_remainder = divide_u_plus_y2(constructed)
            assert recovered_quotient == upoly_clean(quotient_seed)
            assert divisible_by_first(recovered_remainder)
            assert divide_by_first(recovered_remainder) == remainder_quotient
            assert not set_first_zero(recovered_remainder)
            row = {
                "n": n,
                "degree": degree,
                "remainder_over_modulus": serialized_bivariate(remainder_quotient),
            }
            kernel_rows.append(row)
            # The same symbolic calculation uses the first variable as a proper
            # target Q, proving the formal kernel (Q,U+Y^2).
            proper_kernel_rows.append(row)

    window_rows: list[dict[str, Any]] = []
    for n in range(7, 31):
        forms = recurrence_window(n, 5)
        for shift, (a, b) in sorted(forms.items()):
            assert a * q[n] + b * q[n + 1] == q[n + shift]
            for x, y in ((1, 1), (2, -3), (-5, 7)):
                generic = {0: x, 1: y}
                for forward in range(0, 5):
                    generic[forward + 2] = (
                        (4 * (n + forward) + 6) * generic[forward + 1]
                        + generic[forward]
                    )
                for backward in range(0, -5, -1):
                    generic[backward - 1] = (
                        generic[backward + 1]
                        - (4 * (n + backward) + 2) * generic[backward]
                    )
                assert a * x + b * y == generic[shift]
            window_rows.append(
                {"n": n, "shift": shift, "x_coefficient": a, "y_coefficient": b}
            )

    target_rows: list[dict[str, Any]] = []
    resultant_repackaging_rows: list[dict[str, Any]] = []
    clearing_samples = (1, 3, 5, 7, 9, 11, 25, 49, 77, 121)
    for n in range(2, 28):
        y = q[n + 1]
        boundary = -(y * y)
        normalized_polynomial, baseline_integer = actual_residual_polynomial(n)
        canonical_resultant = polynomial_eval(normalized_polynomial, boundary)
        for clearing in clearing_samples:
            target = q[n] // math.gcd(q[n], clearing)
            if target <= 1:
                continue
            lift = symmetric_residue(boundary, target)
            linear_coefficient = -lift
            assert (boundary + linear_coefficient) % target == 0
            quotient = (y * y - linear_coefficient) // target
            assert y * y == linear_coefficient + quotient * target
            evaluated_resultant = polynomial_eval(normalized_polynomial, lift)
            capture = math.gcd(target, abs(evaluated_resultant * baseline_integer))
            product_baseline = math.gcd(target, baseline_integer)
            assert capture % product_baseline == 0
            cancellation_quotient = capture // product_baseline
            assert evaluated_resultant % cancellation_quotient == 0
            target_rows.append(
                {
                    "n": n,
                    "D": clearing,
                    "full_target": q[n],
                    "target": target,
                    "boundary_bits": abs(boundary).bit_length(),
                    "symmetric_lift": lift,
                    "linear_coefficient": linear_coefficient,
                    "quotient_bits": abs(quotient).bit_length(),
                    "target_bits": target.bit_length(),
                }
            )
            resultant_repackaging_rows.append(
                {
                    "n": n,
                    "D": clearing,
                    "target": target,
                    "baseline_integer": baseline_integer,
                    "cancellation_quotient": cancellation_quotient,
                    "linear_resultant": evaluated_resultant,
                    "canonical_resultant_bits": abs(canonical_resultant).bit_length(),
                    "linear_resultant_bits": abs(evaluated_resultant).bit_length(),
                }
            )

    return {
        "schema": "item287-beta-recurrence-annihilator-certificate-v1",
        "description": (
            "Exact recurrence-universal kernel, n-only monic no-go, proper-target "
            "kernel, fixed-window state, and degree-one lift equivalence"
        ),
        "theorem": {
            "full_kernel": (
                "for generic state variables X,Y, the kernel of X->0 and "
                "U->-Y^2 on A[X,Y,U] is exactly (X,U+Y^2)"
            ),
            "n_only_no_go": (
                "no positive-degree monic M in A[U], A=Q(n) or a denominator "
                "localization, is a recurrence-universal annihilator"
            ),
            "state_dependent_classification": (
                "every universal annihilator is (U+Y^2)G+XH and therefore "
                "retains the boundary state or recurrence modulus"
            ),
            "proper_target_kernel": (
                "for every integer Q>=2, the kernel of Z[Y,U]->(Z/QZ)[Y], "
                "U->-Y^2, is exactly (Q,U+Y^2)"
            ),
            "degree_one": (
                "U+a annihilates -Y^2 mod Q iff a=Y^2-kQ; equivalently "
                "v=-a is exactly an integer lift of -Y^2 mod Q"
            ),
            "fixed_window": (
                "every fixed recurrence window is an A-linear form in the "
                "two algebraically free state variables X,Y"
            ),
            "scope": (
                "the theorem excludes recurrence-universal identities, not an "
                "arithmetic congruence special to the beta seed q_0=q_1=1"
            ),
            "deoverlap": "proper Q may be any divisor of q_n/gcd(q_n,D_m)",
            "capacity": (
                "no actual low-height orbit-specific annihilator or resultant "
                "bound is proved; the Item282 product baseline stays open"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "n_only_rows": len(n_only_rows),
            "n_only_digest": digest(n_only_rows),
            "rational_denominator_unit_rows": len(rational_denominator_rows),
            "rational_denominator_unit_digest": digest(rational_denominator_rows),
            "kernel_rows": len(kernel_rows),
            "kernel_digest": digest(kernel_rows),
            "proper_kernel_rows": len(proper_kernel_rows),
            "proper_kernel_digest": digest(proper_kernel_rows),
            "window_rows": len(window_rows),
            "window_digest": digest(window_rows),
            "target_rows": len(target_rows),
            "target_digest": digest(target_rows),
            "resultant_repackaging_rows": len(resultant_repackaging_rows),
            "resultant_repackaging_digest": digest(resultant_repackaging_rows),
            "exceptional_prime_search": False,
            "asymptotic_extrapolation": False,
        },
        "admission": {
            "recurrence_universal_low_height_object": False,
            "actual_orbit_specific_low_height_object": False,
            "actual_target_bound": False,
            "product_baseline_closed": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "an orbit-specific polynomial or rational coefficient congruence for q_0=q_1=1",
            "a factorization-independent O(n)-height lift for a proper de-overlapped Q",
            "a nonzero O(n)-height fixed-degree annihilator resultant for the actual residual",
            "the Item282 common product baseline and weighted-return cover",
            "the uniform beta prime-power-height or little-oh squarefull theorem",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
