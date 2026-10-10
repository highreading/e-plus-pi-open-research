#!/usr/bin/env python3
"""Deterministic certificate for Item 331.

The checker verifies the fixed rational constant-term kernel, the exact
integer numerator of the tied Cartier digit, the actual fixed-m residue
classes, and the fixed-target divisor localization.  Prime counts are
finite diagnostics only.  The all-prime and Chebyshev-mass proofs are in
the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item331_j2_global_cartier_concentration_certificate.json"

DEPENDENCIES = {
    "sources/item328_j2_cartier_digit_frobenius_break_report.md":
        "18a7344f27dba7e036938b474389cc047196c4c0e868507f988cc4436b292526",
    "scripts/item328_j2_cartier_digit_frobenius_break_certificate.py":
        "cb89184298d97a056628dfa0adb15a9ac0a65763b9e64268bf0ab9810842bf63",
    "results/item328_j2_cartier_digit_frobenius_break_certificate.json":
        "5b372bd499c433695ab0dd487c78b6426386c500aaf249fe9944431d6e363b46",
    "manifests/item328_j2_cartier_digit_frobenius_break_manifest.json":
        "6ced1b65ae0397806d255fb9b11b75e8325dae8f8062ee0f008707ffbe605ba2",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def primes_up_to(bound: int) -> list[int]:
    if bound < 2:
        return []
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:bound + 1:prime] = b"\x00" * (((bound - start) // prime) + 1)
    return [value for value in range(2, bound + 1) if sieve[value]]


def actual_rows(bound: int) -> Iterable[tuple[int, int, int]]:
    for prime in primes_up_to(bound):
        if prime < 11:
            continue
        for s in range(1, (prime - 3) // 6 + 1):
            r = (prime - 6 * s - 3) // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                yield prime, r, s


def legendre_two(prime: int) -> int:
    value = pow(2, (prime - 1) // 2, prime)
    if value == 1:
        return 1
    if value == prime - 1:
        return -1
    raise AssertionError((prime, value, "Legendre value"))


def coefficient(n: int, q: int, index: int) -> int:
    """Integer coefficient of (1-x)^n(1+x)^(n+q)."""
    return sum(
        (-1) ** j * math.comb(n, j) * math.comb(n + q, index - j)
        for j in range(max(0, index - (n + q)), min(n, index) + 1)
    )


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    result = [1]
    factor = base[:]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, factor)
        remaining >>= 1
        if remaining:
            factor = multiply(factor, factor)
    return result


def central_numerator(m: int) -> int:
    """A_m=8^m H_m, an integer."""
    return sum(8 ** (m - j) * math.comb(2 * j, j) for j in range(m + 1))


def expected_residue_class(m: int, epsilon: int) -> int:
    if epsilon not in (-1, 1):
        raise ValueError(epsilon)
    if m % 2 == 0:
        return 7 if epsilon == 1 else 3
    return 1 if epsilon == 1 else 5


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def kernel_replay(m_max: int, d_max: int) -> dict[str, Any]:
    # A=(1-x)^3(1+x)^5 and B=(1-x)(1+x)^2.
    A = multiply([1, -3, 3, -1], [1, 5, 10, 10, 5, 1])
    B = multiply([1, -1], [1, 2, 1])
    rows: list[tuple[Any, ...]] = []
    checks = 0
    for m in range(m_max + 1):
        for d in range(1, d_max + 1, 2):
            n = 3 * m + d
            q = 2 * m + d
            p_symbol = 6 * m + 2 * d + 1
            direct = coefficient(n, q, p_symbol)
            kernel = multiply(polynomial_power(A, m), polynomial_power(B, d))
            if kernel[p_symbol] != direct:
                raise AssertionError((m, d, direct, kernel[p_symbol], "constant-term kernel"))
            reciprocal = coefficient(n, q, q - 1)
            if direct != (-1) ** n * reciprocal:
                raise AssertionError((m, d, direct, reciprocal, "reciprocity"))
            rows.append((m, d, n, q, p_symbol, direct, reciprocal))
            checks += 2
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "m_max_inclusive": m_max,
        "odd_d_max_inclusive": d_max,
        "rows": len(rows),
        "identity_checks": checks,
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:8],
    }


def actual_replay(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[Any, ...]] = []
    for prime, r, s in actual_rows(prime_max):
        m = s - 1
        d = r + 4
        n = 3 * m + d
        q = 2 * m + d
        if prime != 6 * m + 2 * d + 1 or prime != 2 * n + 1:
            raise AssertionError((prime, r, s, m, d, n, q, "tied phase"))
        c_mod = coefficient(n, q, prime) % prime
        epsilon = legendre_two(prime)
        numerator = central_numerator(m)
        scaled = pow(8, m, prime) * c_mod % prime
        expected = (pow(8, m, prime) - epsilon * numerator) % prime
        if scaled != expected:
            raise AssertionError((prime, r, s, scaled, expected, "numerator collapse"))
        rows.append((prime, r, s, m, d, n, q, epsilon, numerator, c_mod))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "actual_rows": len(rows),
        "numerator_collapse_checks": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:10],
    }


def fixed_ray_replay(m_max: int, prime_max: int) -> dict[str, Any]:
    targets = [
        Fraction(-2, 1), Fraction(-1, 1), Fraction(0, 1),
        Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3),
    ]
    primes = primes_up_to(prime_max)
    rows: list[tuple[Any, ...]] = []
    divisor_checks = 0
    concentration_by_sign = {"plus": 0, "minus": 0}
    m_zero_plus_zeros = 0
    m_zero_minus_twos = 0
    for m in range(m_max + 1):
        numerator = central_numerator(m)
        eight_m = 8 ** m
        s = m + 1
        for epsilon in (1, -1):
            residue_class = expected_residue_class(m, epsilon)
            for prime in primes:
                if prime < 6 * m + 11 or prime % 8 != residue_class:
                    continue
                r_numerator = prime - 6 * m - 9
                if r_numerator % 2:
                    raise AssertionError((m, epsilon, prime, "nonintegral r"))
                r = r_numerator // 2
                if r < 1 or r % 2 != 1 or r % 3 == 0:
                    raise AssertionError((m, epsilon, prime, r, "not an actual row"))
                d = r + 4
                n = 3 * m + d
                q = 2 * m + d
                c_mod = coefficient(n, q, prime) % prime
                if legendre_two(prime) != epsilon:
                    raise AssertionError((m, epsilon, prime, "wrong Legendre sign"))
                expected = (eight_m - epsilon * numerator) * pow(eight_m, -1, prime) % prime
                if c_mod != expected:
                    raise AssertionError((m, epsilon, prime, c_mod, expected, "ray concentration"))
                concentration_by_sign["plus" if epsilon == 1 else "minus"] += 1
                if m == 0 and epsilon == 1:
                    if c_mod != 0:
                        raise AssertionError((prime, c_mod, "m=0 plus zero"))
                    m_zero_plus_zeros += 1
                if m == 0 and epsilon == -1:
                    if c_mod != 2 % prime:
                        raise AssertionError((prime, c_mod, "m=0 minus two"))
                    m_zero_minus_twos += 1
                for target in targets:
                    u, v = target.numerator, target.denominator
                    target_mod = u * pow(v, -1, prime) % prime
                    divisor = v * (eight_m - epsilon * numerator) - u * eight_m
                    if (c_mod == target_mod) != (divisor % prime == 0):
                        raise AssertionError((m, epsilon, prime, u, v, divisor, "divisor dichotomy"))
                    divisor_checks += 1
                rows.append((m, epsilon, residue_class, prime, r, d, c_mod, numerator))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "m_max_inclusive": m_max,
        "prime_max_inclusive": prime_max,
        "fixed_targets": [[value.numerator, value.denominator] for value in targets],
        "actual_fixed_ray_rows": len(rows),
        "concentration_by_legendre_sign": concentration_by_sign,
        "fixed_target_divisor_checks": divisor_checks,
        "m_zero_plus_zero_rows": m_zero_plus_zeros,
        "m_zero_minus_two_rows": m_zero_minus_twos,
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:12],
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item331-j2-global-cartier-concentration-v1",
        "classification": "PROVED identities with EXACT FINITE REPLAY ONLY diagnostics",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "parameters": {
            "prime_max_inclusive": args.prime_max,
            "fixed_ray_prime_max_inclusive": args.fixed_ray_prime_max,
            "fixed_ray_m_max_inclusive": args.fixed_ray_m_max,
            "kernel_m_max_inclusive": args.kernel_m_max,
            "kernel_odd_d_max_inclusive": args.kernel_d_max,
        },
        "proved_formulae": {
            "constant_term": "c_(6m+2d+1)=CT_x x^-1 (A(x)/x^6)^m (B(x)/x^2)^d",
            "A_polynomial": "(1-x)^3(1+x)^5",
            "B_polynomial": "(1-x)(1+x)^2",
            "central_numerator": "A_m=sum_(j=0)^m 8^(m-j) binom(2j,j)=8^m H_m",
            "cartier_collapse": "8^m c_p = 8^m-epsilon A_m (mod p)",
            "fixed_target_divisor": "p | v(8^m-epsilon A_m)-u8^m for target u/v",
            "ray_classes_mod_8": {
                "m_even_epsilon_plus": 7,
                "m_even_epsilon_minus": 3,
                "m_odd_epsilon_plus": 1,
                "m_odd_epsilon_minus": 5,
            },
        },
        "kernel_replay": kernel_replay(args.kernel_m_max, args.kernel_d_max),
        "actual_replay": actual_replay(args.prime_max),
        "fixed_ray_replay": fixed_ray_replay(args.fixed_ray_m_max, args.fixed_ray_prime_max),
        "strict_ledger": {
            "new_booking": 0,
            "new_capacity_reduction": 0,
            "ordinary_j2_ceiling_per_6M": "1/105",
            "actual_affine_target_weighted_density": "OPEN",
        },
        "scope_warning": (
            "The PNT-in-progressions mass theorem is proved in the report, not inferred from this finite replay. "
            "Coefficient-only concentration does not impose the old determinant gate or the moving Theta target."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime-max", type=int, default=257)
    parser.add_argument("--fixed-ray-prime-max", type=int, default=997)
    parser.add_argument("--fixed-ray-m-max", type=int, default=12)
    parser.add_argument("--kernel-m-max", type=int, default=5)
    parser.add_argument("--kernel-d-max", type=int, default=11)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.prime_max < 11 or args.fixed_ray_prime_max < 11:
        raise ValueError("prime caps must be at least 11")
    if args.fixed_ray_m_max < 0 or args.kernel_m_max < 0:
        raise ValueError("m caps must be nonnegative")
    if args.kernel_d_max < 1 or args.kernel_d_max % 2 == 0:
        raise ValueError("kernel d cap must be positive and odd")
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
