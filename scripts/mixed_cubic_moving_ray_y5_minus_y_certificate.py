#!/usr/bin/env python3
"""Exact certificate for several moving rays p = 10 m + b.

The proof note derives the residue recurrence.  This script uses only the
Python standard library.  It constructs the two coefficient functionals as
polynomials over Q, forms their 2 by 2 determinant, reduces its primitive
integer numerator on the ray 10m+b=0, completely factors the resulting
integer by trial division, and replays every compatible candidate prime from
the original scalar Taylor recurrence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


Poly = tuple[Fraction, ...]
Vector = tuple[Poly, Poly]


def trim(values: list[Fraction] | tuple[Fraction, ...]) -> Poly:
    result = list(values)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    result = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def scale(poly: Poly, scalar: Fraction | int) -> Poly:
    scalar = Fraction(scalar)
    return trim([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def vector_add(left: Vector, right: Vector) -> Vector:
    return add(left[0], right[0]), add(left[1], right[1])


def vector_scale(vector: Vector, scalar: Fraction | int) -> Vector:
    return scale(vector[0], scalar), scale(vector[1], scalar)


def vector_multiply(vector: Vector, poly: Poly) -> Vector:
    return multiply(vector[0], poly), multiply(vector[1], poly)


def integer_polynomial_power(base: tuple[int, ...], exponent: int) -> list[int]:
    result = [1]
    factor = list(base)
    power = exponent
    while power:
        if power & 1:
            product = [0] * (len(result) + len(factor) - 1)
            for i, left in enumerate(result):
                for j, right in enumerate(factor):
                    product[i + j] += left * right
            result = product
        product = [0] * (2 * len(factor) - 1)
        for i, left in enumerate(factor):
            for j, right in enumerate(factor):
                product[i + j] += left * right
        factor = product
        power >>= 1
    return result


def primitive_integer_polynomial_with_scale(poly: Poly) -> tuple[tuple[int, ...], Fraction]:
    """Return primitive P and scalar u with poly=u*P."""
    common_denominator = 1
    for coefficient in poly:
        common_denominator = math.lcm(common_denominator, coefficient.denominator)
    integer_coefficients = [
        coefficient.numerator * (common_denominator // coefficient.denominator)
        for coefficient in poly
    ]
    content = 0
    for coefficient in integer_coefficients:
        content = math.gcd(content, abs(coefficient))
    assert content
    primitive = [coefficient // content for coefficient in integer_coefficients]
    scalar = Fraction(content, common_denominator)
    if primitive[-1] < 0:
        primitive = [-coefficient for coefficient in primitive]
        scalar = -scalar
    return tuple(primitive), scalar


def primitive_integer_polynomial(poly: Poly) -> tuple[int, ...]:
    return primitive_integer_polynomial_with_scale(poly)[0]


def functional_matrix(intercept: int, parity: int, shift: int = 0) -> tuple[Vector, Vector]:
    """Return the two residue functionals in the (E,O) basis.

    The common residue exponent is n=p-6m+shift.  The two polynomial
    weights are A^shift W^(b+shift-1-s), s=0,1.
    """
    assert intercept % 2 == 1
    assert shift >= 0 and intercept + shift >= 2
    assert parity in (0, 1)
    maximum_degree = 3 * intercept + 5 * shift - 3
    singular_index = 3 * intercept + 5 * shift - 5
    low_zero_class = singular_index % 4
    anchor_class = (intercept + shift - 1) % 4
    high_zero_class = (shift - 1 if parity == 0 else shift + 1) % 4
    other_free_class = (high_zero_class + 2) % 4

    zero: Poly = (Fraction(0),)
    one: Poly = (Fraction(1),)
    residues: dict[int, Vector] = {}
    for residue_class in range(4):
        residues[residue_class] = (zero, zero)
    residues[anchor_class] = (one, zero)
    residues[other_free_class] = (zero, one)
    residues[low_zero_class] = (zero, zero)
    residues[high_zero_class] = (zero, zero)

    for index in range(maximum_degree - 3):
        if index not in residues:
            continue
        first_coefficient = index + 5 - 3 * intercept - 5 * shift
        if first_coefficient == 0:
            # The recurrence forces rho_index=0; the next member of this
            # class is beyond both numerator polynomials.
            residues[index] = (zero, zero)
            continue
        second_coefficient: Poly = (
            Fraction(intercept + shift - 1 - index),
            Fraction(4),
        )
        residues[index + 4] = vector_scale(
            vector_multiply(residues[index], second_coefficient),
            Fraction(-1, first_coefficient),
        )

    functionals: list[Vector] = []
    # W=(1-y)(1+y^2)=1-y+y^2-y^3.
    a_power = integer_polynomial_power((0, -1, -1), shift)
    for exponent in (intercept + shift - 1, intercept + shift - 2):
        numerator = integer_polynomial_power((1, -1, 1, -1), exponent)
        product = [0] * (len(a_power) + len(numerator) - 1)
        for left_index, left_value in enumerate(a_power):
            for right_index, right_value in enumerate(numerator):
                product[left_index + right_index] += left_value * right_value
        numerator = product
        value: Vector = (zero, zero)
        for index, coefficient in enumerate(numerator):
            assert index in residues
            value = vector_add(value, vector_scale(residues[index], coefficient))
        functionals.append(value)

    return functionals[0], functionals[1]


def determinant_polynomial(intercept: int, parity: int, shift: int = 0) -> Poly:
    """Return the determinant of the two residue functionals."""
    first, second = functional_matrix(intercept, parity, shift)

    return add(
        multiply(first[0], second[1]),
        scale(multiply(second[0], first[1]), -1),
    )


def evaluate_ray_constant(primitive: tuple[int, ...], intercept: int) -> int:
    """Return 10^deg P(-b/10) by integer Horner evaluation."""
    degree = len(primitive) - 1
    result = 0
    for index, coefficient in enumerate(primitive):
        result += coefficient * (-intercept) ** index * 10 ** (degree - index)
    return result


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if flags[value]]


def complete_small_factorization(value: int) -> dict[int, int]:
    remaining = abs(value)
    factors: dict[int, int] = {}
    # For the certified intercepts every prime factor is below 100000.
    for prime in primes_upto(100_000):
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        if remaining == 1:
            break
    assert remaining == 1, f"unfactored cofactor {remaining}"
    product = 1
    for prime, exponent in factors.items():
        product *= prime**exponent
    assert product == abs(value)
    return factors


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def inverses_upto(limit: int, prime: int) -> list[int]:
    inverse = [0] * (limit + 1)
    inverse[1] = 1
    for value in range(2, limit + 1):
        inverse[value] = prime - (prime // value) * inverse[prime % value] % prime
    return inverse


def original_log_pair(m_value: int, prime: int) -> tuple[int, int]:
    """Return the original rational residues (L0,L1) modulo prime."""
    target = 4 * m_value + 1
    inverse = inverses_upto(target, prime)
    inverse_minus_four = pow(prime - 4, prime - 2, prime)
    coefficient = [pow(2, 2 * m_value - 2, prime)]
    for degree in range(target):
        rhs = (20 * m_value - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += (10 * degree + 10 - 20 * m_value) * coefficient[degree - 1]
        if degree >= 2:
            rhs += (10 * m_value - 5 * degree - 6) * coefficient[degree - 2]
        if degree >= 3:
            rhs += (degree + 1 - 4 * m_value) * coefficient[degree - 3]
        coefficient.append(
            rhs * inverse[degree + 1] * inverse_minus_four % prime
        )
    target_zero = 4 * m_value
    half_l0 = (
        2 * coefficient[target_zero]
        - 2 * coefficient[target_zero - 1]
        + coefficient[target_zero - 2]
    ) % prime
    half_l1 = coefficient[target_zero + 1]
    return 2 * half_l0 % prime, 2 * half_l1 % prime


def truncated_product(left: list[int], right: list[int], limit: int, prime: int) -> list[int]:
    result = [0] * min(limit + 1, len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        maximum_right = min(len(right), len(result) - left_index)
        for right_index in range(maximum_right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_value * right[right_index]
            ) % prime
    return result


def truncated_power(base: tuple[int, ...], exponent: int, limit: int, prime: int) -> list[int]:
    result = [1]
    factor = [value % prime for value in base]
    power = exponent
    while power:
        if power & 1:
            result = truncated_product(result, factor, limit, prime)
        factor = truncated_product(factor, factor, limit, prime)
        power >>= 1
    if len(result) < limit + 1:
        result.extend([0] * (limit + 1 - len(result)))
    return result


def residue_log_pair(m_value: int, prime: int, intercept: int, shift: int) -> tuple[int, int]:
    """Compute 4(Phi0,Phi1) directly at y=1, independently of (3.3)."""
    n_value = 4 * m_value + intercept + shift
    assert prime - n_value == 6 * m_value - shift >= 0
    target = n_value - 1
    # F(1+x)=x H(x), H=4+10x+10x^2+5x^3+x^4.  Below degree p,
    # H^(-n)=H^(p-n)/4 by Frobenius.
    h_power = truncated_power(
        (4, 10, 10, 5, 1), prime - n_value, target, prime
    )
    maximum_weight_degree = 3 * intercept + 5 * shift - 3
    inverse_four = pow(4, prime - 2, prime)
    residues: list[int] = []
    for index in range(maximum_weight_degree + 1):
        value = 0
        for degree in range(min(index, target) + 1):
            value += math.comb(index, degree) * h_power[target - degree]
        residues.append(value * inverse_four % prime)

    a_power = integer_polynomial_power((0, -1, -1), shift)
    pair: list[int] = []
    for exponent in (intercept + shift - 1, intercept + shift - 2):
        w_power = integer_polynomial_power((1, -1, 1, -1), exponent)
        weight = [0] * (len(a_power) + len(w_power) - 1)
        for left_index, left_value in enumerate(a_power):
            for right_index, right_value in enumerate(w_power):
                weight[left_index + right_index] += left_value * right_value
        phi = sum(coefficient * residues[index] for index, coefficient in enumerate(weight))
        pair.append(4 * phi % prime)
    return pair[0], pair[1]


def certify_intercept(intercept: int, shift: int = 0) -> dict[str, object]:
    singular_index = 3 * intercept + 5 * shift - 5
    parity_rows: list[dict[str, object]] = []
    replay_candidates: set[tuple[int, int]] = set()
    for parity in (0, 1):
        first, second = functional_matrix(intercept, parity, shift)
        determinant = add(
            multiply(first[0], second[1]),
            scale(multiply(second[0], first[1]), -1),
        )
        if determinant == (Fraction(0),):
            # This occurs for b=1, shift=1, odd m.  In that row the second
            # functional is exactly -E, so the nonzero global anchor itself
            # excludes simultaneous vanishing.
            assert (intercept, shift, parity) == (1, 1, 1)
            assert second == ((Fraction(-1),), (Fraction(0),))
            parity_rows.append(
                {
                    "parity": "odd",
                    "mode": "direct_anchor",
                    "second_functional_EO": [[-1], [0]],
                }
            )
            continue
        primitive, determinant_scale = primitive_integer_polynomial_with_scale(determinant)
        scale_numerator_factors = complete_small_factorization(determinant_scale.numerator)
        scale_denominator_factors = complete_small_factorization(determinant_scale.denominator)
        # Every scale factor is a p-unit under the theorem's p>k0 hypothesis.
        assert all(prime <= singular_index for prime in scale_numerator_factors)
        assert all(prime <= singular_index for prime in scale_denominator_factors)
        ray_constant = evaluate_ray_constant(primitive, intercept)
        assert ray_constant != 0
        factors = complete_small_factorization(ray_constant)
        compatible: list[dict[str, int]] = []
        for prime in factors:
            if prime <= singular_index or prime % 10 != intercept % 10:
                continue
            difference = prime - intercept
            if difference <= 0 or difference % 10:
                continue
            m_value = difference // 10
            if m_value % 2 != parity:
                continue
            compatible.append({"prime": prime, "m": m_value})
            replay_candidates.add((m_value, prime))
        parity_rows.append(
            {
                "parity": "even" if parity == 0 else "odd",
                "mode": "determinant",
                "determinant_degree": len(primitive) - 1,
                "determinant_scale": {
                    "numerator": determinant_scale.numerator,
                    "denominator": determinant_scale.denominator,
                    "numerator_factorization": {
                        str(prime): exponent
                        for prime, exponent in scale_numerator_factors.items()
                    },
                    "denominator_factorization": {
                        str(prime): exponent
                        for prime, exponent in scale_denominator_factors.items()
                    },
                },
                "primitive_coefficients_low_to_high": list(primitive),
                "ray_constant": ray_constant,
                "ray_constant_factorization": {
                    str(prime): exponent for prime, exponent in factors.items()
                },
                "compatible_large_candidates": compatible,
            }
        )

    small_cases: list[dict[str, object]] = []
    for m_value in range(1, max(1, (singular_index - intercept) // 10 + 2)):
        prime = 10 * m_value + intercept
        if prime > singular_index or not is_prime(prime):
            continue
        pair = original_log_pair(m_value, prime)
        assert pair != (0, 0)
        small_cases.append({"m": m_value, "prime": prime, "L_pair": list(pair)})

    candidate_cases: list[dict[str, object]] = []
    for m_value, prime in sorted(replay_candidates):
        pair = original_log_pair(m_value, prime)
        assert pair != (0, 0)
        candidate_cases.append({"m": m_value, "prime": prime, "L_pair": list(pair)})

    orientation_replays: list[dict[str, object]] = []
    for parity in (0, 1):
        for m_value in range(1, 200):
            if m_value % 2 != parity:
                continue
            prime = 10 * m_value + intercept
            if not is_prime(prime):
                continue
            original_pair = original_log_pair(m_value, prime)
            residue_pair = residue_log_pair(m_value, prime, intercept, shift)
            assert residue_pair == original_pair
            orientation_replays.append(
                {"parity": "even" if parity == 0 else "odd", "m": m_value,
                 "prime": prime, "L_pair": list(original_pair)}
            )
            break
        else:
            raise AssertionError("orientation replay prime not found")

    return {
        "intercept": intercept,
        "common_exponent_shift": shift,
        "singular_index": singular_index,
        "parity_rows": parity_rows,
        "small_prime_replays": small_cases,
        "large_candidate_replays": candidate_cases,
        "orientation_replays": orientation_replays,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/moving_ray_y5_minus_y_certificate.json",
    )
    args = parser.parse_args()
    specifications = ((1, 1), (3, 0), (7, 0), (9, 0), (11, 0), (13, 0),
                      (17, 0), (19, 0), (21, 0), (23, 0))
    rows = [certify_intercept(intercept, shift) for intercept, shift in specifications]
    payload = {
        "claim": (
            "For every listed intercept b, every m>=1 with p=10m+b prime "
            "has (L0,L1) not congruent to (0,0) modulo p."
        ),
        "intercepts": [intercept for intercept, _ in specifications],
        "rows": rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
