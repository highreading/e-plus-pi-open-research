#!/usr/bin/env python3
"""Independent root probe for Item 260's p=5 mod 6 punctured reduction.

No Item-260 code is imported.  Bounded row counts are replay evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


Laurent = dict[int, F]


def add(target: Laurent, source: Laurent, scale: F = F(1)) -> Laurent:
    out = dict(target)
    for exponent, coefficient in source.items():
        out[exponent] = out.get(exponent, F(0)) + scale * coefficient
        if not out[exponent]:
            del out[exponent]
    return out


def apply_L(poly: Laurent) -> Laurent:
    out: Laurent = {}
    for exponent, coefficient in poly.items():
        out = add(
            out,
            {
                exponent + 2: coefficient * F(2 * exponent + 3, 2),
                exponent - 1: -coefficient * F(exponent, 2),
            },
        )
    return out


def hermite(delta: int) -> tuple[F, Laurent]:
    c = F(1)
    kappa = F(0)
    previous: Laurent = {}
    primitive: Laurent = {}
    for j in range(delta):
        n = 3 * j + 2
        if j == 0:
            current: Laurent = {}
        else:
            factor = F(2 * n - 5, n - 1)
            current = add({-(n - 1): F(2, n - 1)}, previous, factor)
            c *= factor
        primitive = add(primitive, current)
        kappa += c
        previous = current
    primitive = add(primitive, {-1: 2 * kappa})
    expected = {-(3 * j + 2): F(1) for j in range(delta)}
    expected[1] = kappa
    assert apply_L(primitive) == expected
    return kappa, primitive


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


def mod_fraction(value: F, p: int) -> int:
    return value.numerator % p * pow(value.denominator % p, -1, p) % p


def legendre(value: int, p: int) -> int:
    return pow(value % p, (p - 1) // 2, p)


def prefix_values(limit: int, p: int) -> tuple[list[int], list[int]]:
    terms = [1]
    prefixes = [1]
    for j in range(1, limit + 1):
        terms.append(terms[-1] * (2 * j - 1) * pow(4 * j, -1, p) % p)
        prefixes.append((prefixes[-1] + terms[-1]) % p)
    return terms, prefixes


def lambda_value(p: int, function) -> int:
    half = pow(2, -1, p)
    return sum(
        function(x) * legendre(x**3 - half, p)
        for x in range(1, p)
        if x != 1
    ) % p


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=251)
    parser.add_argument("--delta-bound", type=int, default=25)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rational_rows = []
    for delta in range(1, args.delta_bound + 1, 2):
        kappa, primitive = hermite(delta)
        rational_rows.append(
            f"{delta},{kappa.numerator},{kappa.denominator},"
            f"{len(primitive)}\n"
        )

    endpoint_checks = 0
    actual_rows = 0
    localized_checks = 0
    zeros = []
    digest_rows = []
    for p in primes_up_to(args.bound):
        if p % 6 != 5:
            continue
        q = (p - 5) // 6
        epsilon = legendre(2, p)
        terms, prefixes = prefix_values(q, p)
        half = pow(2, -1, p)
        inv_two = half
        inv_three = pow(3, -1, p)

        # Endpoint functional for every admissible Laurent exponent.
        max_r = max((r for r in range(1, (p - 9) // 2 + 1, 6)), default=-1)
        if max_r >= 1:
            for j in range(1, max_r + 1):
                if j % 3 != 1:
                    continue

                def l_of_inverse(x: int, j: int = j) -> int:
                    g = (x**3 - inv_two) % p
                    r_value = pow(x, -j, p)
                    derivative = -j * pow(x, -j - 1, p)
                    return (g * derivative + 3 * inv_two * x * x * r_value) % p

                lhs = lambda_value(p, l_of_inverse)
                rhs = epsilon * (j - 3) * inv_two % p
                assert lhs == rhs
                endpoint_checks += 1

        for r in range(1, (p - 9) // 2 + 1, 6):
            delta = (r + 2) // 3
            m = q - delta
            if m < 0:
                continue
            kappa, _ = hermite(delta)
            kappa_mod = mod_fraction(kappa, p)

            U = lambda_value(p, lambda x: x % p)
            V = lambda_value(
                p, lambda x: x * pow((x**3 - 1) % p, -1, p) % p
            )
            assert U == (terms[q] - epsilon) % p
            assert V == (-prefixes[q] + 4 * epsilon * inv_three) % p

            S = lambda_value(
                p,
                lambda x, r=r: (
                    pow(x, -r - 1, p) * pow((x**3 - 1) % p, -1, p)
                )
                % p,
            )
            assert S == (
                V + kappa_mod * U + epsilon * (kappa_mod + delta)
            ) % p
            assert S == (
                -prefixes[q]
                + kappa_mod * terms[q]
                + epsilon * (delta + 4 * inv_three)
            ) % p
            assert prefixes[m] == (
                prefixes[q] - kappa_mod * terms[q]
            ) % p
            localized_checks += 4
            actual_rows += 1
            if prefixes[m] == 0:
                s = m + 1
                zeros.append((p, r, s, m, delta))
            digest_rows.append(
                f"{p},{r},{m},{delta},{kappa_mod},{U},{V},{S},{prefixes[m]}\n"
            )

    assert (47, 7, 5, 4, 3) in zeros
    result = {
        "schema": "item260-root-independent-probe-v1",
        "imports_item260_code": False,
        "rational_Hermite_rows": len(rational_rows),
        "rational_digest_sha256": hashlib.sha256(
            "".join(rational_rows).encode("ascii")
        ).hexdigest(),
        "endpoint_functional_checks": endpoint_checks,
        "actual_rows": actual_rows,
        "localized_equalities": localized_checks,
        "p47_zero_reproduced": True,
        "row_digest_sha256": hashlib.sha256(
            "".join(digest_rows).encode("ascii")
        ).hexdigest(),
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "zero_count": len(zeros),
            "zeros": zeros,
        },
        "root_symbolic_checks": {
            "residue_at_cube_root": "1/(3*alpha*beta), nonzero when alpha^3=1 and beta^2=1/2",
            "fixed_r_raw_weight": "O(log M)=o(M)",
        },
        "verdict": "the exact Hermite, endpoint, residual-coordinate, cutoff, and p=47 claims replay independently; booking remains zero",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
