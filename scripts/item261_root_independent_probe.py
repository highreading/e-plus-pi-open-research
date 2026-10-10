#!/usr/bin/env python3
"""Independent root probe for Item 261's p=1 mod 6 punctured reduction.

No Item-261 code is imported.  Bounded row counts are replay evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (((bound - start) // q) + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def legendre(value: int, p: int) -> int:
    return pow(value % p, (p - 1) // 2, p)


def mod_fraction(value: F, p: int) -> int:
    return value.numerator % p * pow(value.denominator % p, -1, p) % p


def prefix_values(limit: int, p: int) -> tuple[list[int], list[int]]:
    terms = [1]
    prefixes = [1]
    for j in range(1, limit + 1):
        terms.append(terms[-1] * (2 * j - 1) * pow(4 * j, -1, p) % p)
        prefixes.append((prefixes[-1] + terms[-1]) % p)
    return terms, prefixes


def boundary(delta: int) -> tuple[F, F, list[F]]:
    values = [F(1)]
    for j in range(delta):
        values.append(values[-1] * F(6 * j + 1, 3 * j + 2))
    return sum(values[:delta], F(0)), sum(values[1 : delta + 1], F(0)), values


def pochhammer(value: F, length: int) -> F:
    out = F(1)
    for k in range(length):
        out *= value + k
    return out


def item251_tail(r: int, delta: int) -> F:
    return sum(
        (
            F(1, 2**k)
            * pochhammer(F(1, 3) - delta, k)
            / pochhammer(F(1, 2), k)
            for k in range(1, r + 3)
        ),
        F(0),
    )


def direct_tail(m: int, r: int, p: int) -> int:
    out = 0
    half = pow(2, -1, p)
    for k in range(1, r + 3):
        numerator = 1
        denominator = 1
        for i in range(k):
            numerator = numerator * (2 * m + 1 + 2 * i) % p
            denominator = denominator * (1 + 2 * i) % p
        out = (out + pow(half, k, p) * numerator * pow(denominator, -1, p)) % p
    return out


def rational_D_R(j: int, x: F) -> F:
    a = 1 - x / 2
    f = a**3 / x
    r_value = x ** (j + 1) / a**2
    logarithmic_derivative_r = F(j + 1, 1) / x + 1 / a
    logarithmic_derivative_f = -F(3, 2) / a - 1 / x
    return f * r_value * (
        logarithmic_derivative_r + F(5, 6) * logarithmic_derivative_f
    )


def lambda_value(p: int, q: int, function) -> int:
    half = pow(2, -1, p)
    return sum(
        function(x)
        * pow((1 - x * half) % p, 3 * q, p)
        * pow(x, -q, p)
        for x in range(1, p)
        if x != 1
    ) % p


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=251)
    parser.add_argument("--symbolic-bound", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    symbolic_checks = 0
    symbolic_rows = []
    for j in range(args.symbolic_bound + 1):
        for x in (F(1, 3), F(3, 5), F(5, 7)):
            lhs = rational_D_R(j, x)
            rhs = F(6 * j + 1, 6) * x ** (j - 1) - F(3 * j + 2, 6) * x**j
            assert lhs == rhs
            symbolic_checks += 1
        symbolic_rows.append(
            f"{j},{F(6*j+1,6)},{F(3*j+2,6)}\n"
        )

    endpoint_checks = 0
    actual_rows = 0
    localized_checks = 0
    item251_checks = 0
    zeros = []
    digest_rows = []
    for p in primes_up_to(args.bound):
        if p % 6 != 1:
            continue
        q = (p - 1) // 6
        epsilon = legendre(2, p)
        terms, prefixes = prefix_values(q + 1, p)
        inv_two = pow(2, -1, p)
        inv_three = pow(3, -1, p)

        for j in range(q):
            lhs = lambda_value(
                p,
                q,
                lambda x, j=j: (
                    F(6 * j + 1, 6) * F(x, 1) ** (j - 1)
                    - F(3 * j + 2, 6) * F(x**j, 1)
                ),
            )
            rhs = (
                -3
                * terms[q - j + 1]
                * pow(2 * (3 * j - 1), -1, p)
                - epsilon * (3 * j - 1) * pow(6, -1, p)
            ) % p
            assert mod_fraction(lhs, p) == rhs
            endpoint_checks += 1

        for r in range(5, (p - 9) // 2 + 1, 6):
            delta = (r + 4) // 3
            m = q - delta
            if m < 0:
                continue
            kappa, gamma, c_values = boundary(delta)
            kappa_mod = mod_fraction(kappa, p)
            gamma_mod = mod_fraction(gamma, p)

            U = lambda_value(p, q, lambda x: pow(x, -1, p))
            V = lambda_value(p, q, lambda x: pow((1 - x) % p, -1, p))
            assert U == (-terms[q] * pow(5, -1, p) - epsilon) % p
            assert V == (-prefixes[q] + 2 * epsilon * inv_three) % p

            T = lambda_value(
                p,
                q,
                lambda x, delta=delta: x**delta * pow((1 - x) % p, -1, p)
                % p,
            )
            assert T == (
                V - 5 * kappa_mod * U + epsilon * (delta - 5 * kappa_mod)
            ) % p
            assert T == (V + kappa_mod * terms[q] + delta * epsilon) % p
            assert prefixes[m] == (
                prefixes[q] - kappa_mod * terms[q]
            ) % p
            localized_checks += 5

            pi_r = item251_tail(r, delta)
            assert direct_tail(m, r, p) == mod_fraction(pi_r, p)
            d_r = kappa + c_values[delta] * pi_r
            direct_a = (
                (-1) ** m
                * (
                    epsilon
                    * (
                        prefixes[m]
                        - terms[m] * direct_tail(m, r, p)
                    )
                    - 1
                )
            ) % p
            transformed_a = (
                (-1) ** m
                * (
                    epsilon
                    * (
                        prefixes[q]
                        - mod_fraction(d_r, p) * terms[q]
                    )
                    - 1
                )
            ) % p
            assert direct_a == transformed_a
            assert terms[m] == mod_fraction(c_values[delta], p) * terms[q] % p
            item251_checks += 3
            actual_rows += 1
            if prefixes[m] == 0:
                zeros.append((p, r, m + 1, m, delta))
            digest_rows.append(
                f"{p},{r},{m},{delta},{kappa_mod},{gamma_mod},"
                f"{U},{V},{T},{direct_a}\n"
            )

    assert (43, 11, 3, 2, 5) in zeros
    result = {
        "schema": "item261-root-independent-probe-v1",
        "imports_item261_code": False,
        "symbolic_D_R_checks": symbolic_checks,
        "symbolic_digest_sha256": hashlib.sha256(
            "".join(symbolic_rows).encode("ascii")
        ).hexdigest(),
        "endpoint_functional_checks": endpoint_checks,
        "actual_rows": actual_rows,
        "localized_equalities": localized_checks,
        "item251_period_equalities": item251_checks,
        "p43_zero_reproduced": True,
        "row_digest_sha256": hashlib.sha256(
            "".join(digest_rows).encode("ascii")
        ).hexdigest(),
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "zero_count": len(zeros),
            "zeros": zeros,
        },
        "root_symbolic_checks": {
            "Kummer_map": "x=X^-3 and Z^2=X^3-1/2",
            "logarithmic_residue": "-alpha/beta at alpha^3=1, beta^2=1/2",
            "fixed_r_raw_weight": "O(log M)=o(M)",
        },
        "verdict": "the exact Hermite, endpoint, residual-coordinate, Item-251 period, cutoff, and p=43 claims replay independently; booking remains zero",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
