#!/usr/bin/env python3
"""Independent deterministic audit of the valid m-ray Cartier formulas."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

from mixed_cubic_valid_mray_cartier_gcd_probe import x_value, y_value


SAMPLES = (
    # Small baseline cases.
    (17, 1),
    (19, 1),
    (29, 2),
    (31, 2),
    # Exceptional rank-resonance family p=10m+3 (so 5q-9=3p).
    (23, 2),
    (43, 4),
    (53, 5),
    # Large q (including q very close to p).
    (101, 1),
    (151, 1),
    (1009, 1),
    # More balanced and small-q rays.
    (211, 20),
    (211, 34),
    (1009, 100),
    (1009, 160),
)


def multiply_by_short_base(
    polynomial: list[int], base: tuple[int, ...], degree: int, prime: int
) -> list[int]:
    answer = [0] * (degree + 1)
    for i, left in enumerate(polynomial):
        if left == 0:
            continue
        for j, right in enumerate(base):
            if i + j <= degree:
                answer[i + j] = (answer[i + j] + left * right) % prime
    return answer


def short_power(
    base: tuple[int, ...], exponent: int, degree: int, prime: int
) -> list[int]:
    answer = [1] + [0] * degree
    for _ in range(exponent):
        answer = multiply_by_short_base(answer, base, degree, prime)
    return answer


def negative_binomial_coefficients(
    q: int, degree: int, prime: int, argument_sign: int = 1
) -> list[int]:
    answer = [1]
    for index in range(degree):
        answer.append(
            answer[-1]
            * (q + index)
            * pow(index + 1, -1, prime)
            * argument_sign
            % prime
        )
    return answer


def coefficient_with_denominator(
    base: tuple[int, ...],
    exponent: int,
    q: int,
    degree: int,
    prime: int,
    argument_sign: int = 1,
) -> int:
    polynomial = short_power(base, exponent, degree, prime)
    denominator = negative_binomial_coefficients(q, degree, prime, argument_sign)
    return sum(
        polynomial[index] * denominator[degree - index]
        for index in range(degree + 1)
    ) % prime


def original_lambda(m: int, p: int, s: int) -> int:
    q = p - 6 * m
    exponent = 2 * m + q - 1 - s
    degree = 4 * m + s
    polynomial = short_power((1, 0, 1), exponent, degree, p)
    for _ in range(1 + 3 * s):
        polynomial = multiply_by_short_base(polynomial, (1, 1), degree, p)
    denominator = negative_binomial_coefficients(q, degree, p)
    return sum(
        polynomial[index] * denominator[degree - index]
        for index in range(degree + 1)
    ) % p


def endpoint_residues(m: int, p: int, s: int) -> tuple[int, int]:
    q = p - 6 * m
    exponent = 2 * m + q - 1 - s
    c = coefficient_with_denominator((1, 1, 1, 1), exponent, q, q - 1, p)
    # At z=1+h, P(1+h)=4+6h+4h^2+h^3.  Since q is odd,
    # (1-z)^(-q)=(-h)^(-q) contributes a minus sign.
    r = -coefficient_with_denominator(
        (4, 6, 4, 1), exponent, q, q - 1, p, argument_sign=-1
    )
    return c, r % p


def direct_coefficient_windows(m: int, p: int) -> tuple[list[int], list[int]]:
    q = p - 6 * m
    exponent = p - 4 * m - 3
    degree = p - 1
    p_power = short_power((1, 1, 1, 1), exponent, degree, p)
    def window(index_shift: int) -> list[int]:
        answer = []
        for r in range(1, 9):
            target = p - index_shift - r
            if target < 0:
                answer.append(0)
                continue
            value = 0
            for j in range(min(6 * m, target) + 1):
                value += (-1) ** j * math.comb(6 * m, j) * p_power[target - j]
            answer.append(value % p)
        return answer

    return window(6 * m), window(0)


def mod_fraction(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("work/mixed_cubic_valid_mray_cartier_audit.json"),
    )
    arguments = parser.parse_args()
    rows = []
    all_pass = True
    for p, m in SAMPLES:
        q = p - 6 * m
        assert q > 0 and q % 2 == 1 and q % 3 != 0
        assert all(p % divisor for divisor in range(2, math.isqrt(p) + 1))

        transformed_x = [mod_fraction(x_value(m, p % 4, r), p) for r in range(1, 9)]
        transformed_y = [mod_fraction(y_value(m, p % 4, r), p) for r in range(1, 9)]
        direct_x, direct_y = direct_coefficient_windows(m, p)
        x_match = transformed_x == direct_x and transformed_y == direct_y

        l1 = (transformed_x[0] - transformed_y[7]) % p
        l2 = (
            transformed_x[1]
            + transformed_x[2]
            + transformed_x[3]
            - transformed_y[4]
            - transformed_y[5]
            - transformed_y[6]
        ) % p

        lambda_values = [original_lambda(m, p, s) for s in range(3)]
        weighted_values = []
        endpoint_rows = []
        for s in range(3):
            c, r = endpoint_residues(m, p, s)
            weighted = pow(2, 2 * m + 2 * s, p) * (2 * c + r) % p
            weighted_values.append(weighted)
            endpoint_rows.append({"s": s, "c": c, "r": r})

        residue_match = lambda_values == weighted_values
        l1_match = lambda_values[2] == pow(2, 2 * m + 4, p) * l1 % p
        l2_match = lambda_values[1] == pow(2, 2 * m + 2, p) * (l1 + l2) % p
        passed = x_match and residue_match and l1_match and l2_match
        all_pass &= passed
        rows.append(
            {
                "p": p,
                "m": m,
                "q": q,
                "p_mod_4": p % 4,
                "rank_resonance_p_eq_10m_plus_3": p == 10 * m + 3,
                "x_window": transformed_x,
                "y_window": transformed_y,
                "L1": l1,
                "L2": l2,
                "lambda_0_1_2": lambda_values,
                "endpoint_residues": endpoint_rows,
                "x_formula_matches_direct_polynomial": x_match,
                "weighted_residue_matches_original_lambda": residue_match,
                "lambda2_matches_scaled_L1": l1_match,
                "lambda1_matches_scaled_L1_plus_L2": l2_match,
                "passed": passed,
            }
        )

    result = {
        "schema": "mixed-cubic-valid-mray-cartier-audit-v1",
        "all_pass": all_pass,
        "sample_count": len(rows),
        "rows": rows,
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    arguments.output.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"samples={len(rows)}; all_pass={all_pass}; sha256={digest}")
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
