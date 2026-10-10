#!/usr/bin/env python3
"""Deterministic certificate for Item 249's singular j=2 bulk family.

The checker derives the exact coefficient/character-prefix sum, verifies
the coefficient ODE recurrence, and reduces the moving-prime family to a
single universal algebraic-hypergeometric recurrence.  Scans are finite.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item249_j2_singular_bulk_hypergeometric_certificate.json"
ITEM247_SHA256 = "0d0ccdec9c0406834cde31a912702dcc999d1a65a3edcac64040c500cf0fa1f9"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ITEM247_PATH = resolve("item247_j2_bulk_pair_eliminant_certificate.py")
if sha256(ITEM247_PATH) != ITEM247_SHA256:
    raise RuntimeError("Item247 checker hash mismatch")
item247 = load("item249_item247", ITEM247_PATH)
item246 = item247.item246


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def actual_coefficients(s: int) -> tuple[int, ...]:
    """Coefficients of (3-2t-t^2)(1+t)^(2s-1) over Z."""
    exponent = 2 * s - 1
    result = []
    for v in range(exponent + 3):
        result.append(
            3 * (math.comb(exponent, v) if 0 <= v <= exponent else 0)
            - 2 * (math.comb(exponent, v - 1) if 0 <= v - 1 <= exponent else 0)
            - (math.comb(exponent, v - 2) if 0 <= v - 2 <= exponent else 0)
        )
    return tuple(result)


def exact_character_sum(coefficients: tuple[int, ...]) -> Fraction:
    """The closed Item246 triangular functional as one prefix sum at L=1."""
    character_prefix = Fraction(0)
    total = Fraction(0)
    for v, coefficient in enumerate(coefficients):
        denominator = 2 * v + 3
        if v:
            total += (
                ((-1) ** (v - 1))
                * coefficient
                * character_prefix
                / denominator
            )
        character_prefix += Fraction((-1) ** v, denominator)
    return total


def verify_actual_recurrence(s: int) -> tuple[int, ...]:
    exponent = 2 * s - 1
    degree = exponent + 2
    coefficients = actual_coefficients(s)
    if len(coefficients) - 1 != degree:
        raise AssertionError((s, "degree"))
    for v in range(degree):
        current = coefficients[v]
        previous = coefficients[v - 1] if v >= 1 else 0
        previous_2 = coefficients[v - 2] if v >= 2 else 0
        left = 3 * (v + 1) * coefficients[v + 1]
        right = (
            (3 * exponent - v - 2) * current
            + (3 * v - 2 * exponent - 7) * previous
            + (v - exponent - 4) * previous_2
        )
        if left != right:
            raise AssertionError((s, v, "exact coefficient recurrence"))
    direct = item246.functional_fraction(1, coefficients)[0]
    closed = exact_character_sum(coefficients)
    if direct != closed:
        raise AssertionError((s, "exact character-prefix sum"))
    return coefficients


def universal_fraction(degree: int) -> tuple[list[Fraction], list[Fraction], Fraction]:
    """Return universal c_v, h_v, and Theta_degree over Q."""
    algebraic = Fraction(1)
    algebraic_previous = Fraction(0)
    algebraic_previous_2 = Fraction(0)
    coefficients: list[Fraction] = []
    prefixes: list[Fraction] = []
    character_prefix = Fraction(0)
    theta = Fraction(0)
    for v in range(degree + 1):
        coefficient = (
            3 * algebraic - 2 * algebraic_previous - algebraic_previous_2
        )
        coefficients.append(coefficient)
        prefixes.append(character_prefix)
        if v:
            theta += (
                ((-1) ** (v - 1))
                * coefficient
                * character_prefix
                / (2 * v + 3)
            )
        character_prefix += Fraction((-1) ** v, 2 * v + 3)
        algebraic_previous_2, algebraic_previous = (
            algebraic_previous,
            algebraic,
        )
        if v < degree:
            algebraic *= Fraction(-(3 * v + 8), 3 * (v + 1))

    padded = [Fraction(0), Fraction(0)] + coefficients
    for v in range(1, degree + 1):
        left = 9 * v * padded[v + 2]
        right = (
            -3 * (v + 9) * padded[v + 1]
            + (9 * v - 14) * padded[v]
            + (3 * v - 7) * padded[v - 1]
        )
        if left != right:
            raise AssertionError((degree, v, "universal ODE recurrence"))
    return coefficients, prefixes, theta


def universal_mod(p: int) -> dict[str, Any]:
    if p < 5 or p % 3 != 2:
        raise ValueError("require prime candidate p congruent to 2 modulo 3")
    degree = (p - 2) // 3
    if not (degree < p and 2 * degree + 3 < p):
        raise AssertionError((p, degree, "unit range"))
    inverse = [0] * (2 * degree + 4)
    inverse[1] = 1
    for value in range(2, len(inverse)):
        inverse[value] = -(p // value) * inverse[p % value] % p

    algebraic = 1
    algebraic_previous = 0
    algebraic_previous_2 = 0
    coefficients: list[int] = []
    character_prefix = 0
    theta = 0
    for v in range(degree + 1):
        coefficient = (
            3 * algebraic - 2 * algebraic_previous - algebraic_previous_2
        ) % p
        coefficients.append(coefficient)
        if v:
            sign = 1 if v % 2 else -1
            theta = (
                theta
                + sign * coefficient * character_prefix * inverse[2 * v + 3]
            ) % p
        character_prefix = (
            character_prefix
            + (1 if v % 2 == 0 else -1) * inverse[2 * v + 3]
        ) % p
        algebraic_previous_2, algebraic_previous = (
            algebraic_previous,
            algebraic,
        )
        if v < degree:
            algebraic = (
                algebraic
                * (-(3 * v + 8))
                * inverse[3]
                * inverse[v + 1]
            ) % p

    padded = [0, 0] + coefficients
    for v in range(1, degree + 1):
        left = 9 * v * padded[v + 2]
        right = (
            -3 * (v + 9) * padded[v + 1]
            + (9 * v - 14) * padded[v]
            + (3 * v - 7) * padded[v - 1]
        )
        if (left - right) % p:
            raise AssertionError((p, v, "modular universal recurrence"))

    if degree >= 2:
        if coefficients[-1] != p - 1 or coefficients[-2] != (-degree) % p:
            raise AssertionError((p, degree, "terminal coefficients"))
    return {
        "degree": degree,
        "theta": theta,
        "coefficient_digest_sha256": row_digest(
            [(v, value) for v, value in enumerate(coefficients)]
        ),
    }


def prime_sieve(bound: int) -> bytearray:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for divisor in range(2, math.isqrt(bound) + 1):
        if sieve[divisor]:
            start = divisor * divisor
            sieve[start : bound + 1 : divisor] = b"\x00" * (
                (bound - start) // divisor + 1
            )
    return sieve


def singular_primes(bound: int):
    sieve = prime_sieve(bound)
    for p in range(17, bound + 1, 6):
        if sieve[p]:
            s = (p - 5) // 6
            if not (
                s >= 2
                and p == 6 * s + 5
                and s <= (p - 3) // 6
                and (5 * p - 2 * s - 1) % 4 == 0
            ):
                raise AssertionError((p, s, "singular admissibility"))
            yield p, s


def direct_crosscheck(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    for p, s in singular_primes(bound):
        coefficients = verify_actual_recurrence(s)
        modular_coefficients = tuple(value % p for value in coefficients)
        expected = item247.singular_polynomial(p, s)
        if modular_coefficients != expected:
            raise AssertionError((p, s, "actual polynomial"))
        direct = item246.functional_mod(p, 1, modular_coefficients)[0]
        universal = universal_mod(p)
        if direct != universal["theta"]:
            raise AssertionError((p, s, "universal reduction"))
        rows.append(
            (
                p,
                s,
                universal["degree"],
                direct,
                modular_coefficients[-2],
                modular_coefficients[-1],
            )
        )
    return {
        "status": "EXACT FINITE DIRECT CROSSCHECK",
        "prime_max_inclusive": bound,
        "row_count": len(rows),
        "zero_count": sum(row[3] == 0 for row in rows),
        "row_digest_sha256": row_digest(rows),
    }


def rational_replay(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    for p, s in singular_primes(bound):
        degree = (p - 2) // 3
        coefficients = verify_actual_recurrence(s)
        actual = exact_character_sum(coefficients)
        _, _, universal = universal_fraction(degree)
        actual_mod = actual.numerator % p * pow(actual.denominator % p, -1, p) % p
        universal_mod_p = (
            universal.numerator
            % p
            * pow(universal.denominator % p, -1, p)
            % p
        )
        if actual_mod != universal_mod_p:
            raise AssertionError((p, s, "rational universal reduction"))
        rows.append(
            (
                p,
                s,
                degree,
                actual.numerator % p,
                actual.denominator % p,
                universal.numerator % p,
                universal.denominator % p,
                actual_mod,
            )
        )
    return {
        "status": "EXACT FINITE RATIONAL REPLAY",
        "prime_max_inclusive": bound,
        "row_count": len(rows),
        "zero_count": sum(row[-1] == 0 for row in rows),
        "row_digest_sha256": row_digest(rows),
    }


def extended_scan(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    zero_rows: list[dict[str, int]] = []
    for p, s in singular_primes(bound):
        universal = universal_mod(p)
        value = universal["theta"]
        if value == 0:
            zero_rows.append({"p": p, "s": s})
        rows.append((p, s, universal["degree"], value))
    return {
        "status": "EXACT FINITE ONLY",
        "prime_max_inclusive": bound,
        "row_count": len(rows),
        "zero_count": len(zero_rows),
        "zero_rows": zero_rows,
        "row_digest_sha256": row_digest(rows),
    }


def exact_witnesses() -> dict[str, Any]:
    coefficients_3, _, theta_3 = universal_fraction(3)
    if theta_3 != Fraction(-49676, 25515):
        raise AssertionError("boundary theta_3")
    if theta_3.numerator % 11 or theta_3.denominator % 11 == 0:
        raise AssertionError("excluded boundary residue")
    boundary_actual = exact_character_sum(verify_actual_recurrence(1))
    if boundary_actual != Fraction(88, 945):
        raise AssertionError("excluded boundary actual value")
    if boundary_actual.numerator % 11 or boundary_actual.denominator % 11 == 0:
        raise AssertionError("excluded boundary actual residue")
    witnesses: dict[str, Any] = {
        "excluded_boundary_zero": {
            "p": 11,
            "s": 1,
            "degree": 3,
            "admissible": False,
            "reason_excluded": "Item244 requires s>=2",
            "theta_numerator": str(theta_3.numerator),
            "theta_denominator": str(theta_3.denominator),
            "actual_bulk_numerator": str(boundary_actual.numerator),
            "actual_bulk_denominator": str(boundary_actual.denominator),
            "residue_mod_p": 0,
            "terminal_coefficient": str(coefficients_3[-1]),
        }
    }
    for p, s, expected in ((17, 2, 9), (23, 3, 3)):
        universal = universal_mod(p)
        if universal["theta"] != expected:
            raise AssertionError((p, "admissible witness"))
        witnesses[f"admissible_nonzero_p{p}"] = {
            "p": p,
            "s": s,
            "degree": universal["degree"],
            "residue_mod_p": expected,
        }
    return witnesses


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct-prime-max", type=int, default=401)
    parser.add_argument("--rational-prime-max", type=int, default=101)
    parser.add_argument("--scan-prime-max", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (101 <= args.rational_prime_max <= args.direct_prime_max):
        raise ValueError("require 101 <= rational-prime-max <= direct-prime-max")
    if args.scan_prime_max < args.direct_prime_max:
        raise ValueError("scan-prime-max must be at least direct-prime-max")

    direct = direct_crosscheck(args.direct_prime_max)
    rational = rational_replay(args.rational_prime_max)
    scan = extended_scan(args.scan_prime_max)
    witnesses = exact_witnesses()
    result = {
        "schema": "item249-j2-singular-bulk-hypergeometric-v1",
        "item": 249,
        "route": "Route 1A",
        "cell": "normalized common-log j=2 fixed cell, Item247 singular family r=1",
        "parameters": {
            "item244_r": 1,
            "p": "6s+5 prime",
            "s_minimum": 2,
            "L": 1,
            "M": "2s+1=(p-2)/3",
            "n": "2s-1=M-2=(p-8)/3",
            "D1": "(1-t)(1+t)^(2s-1)(3+t)",
        },
        "proved": {
            "exact_coefficients": "d_v=3*C(n,v)-2*C(n,v-1)-C(n,v-2), with out-of-range binomial coefficients zero",
            "exact_coefficient_recurrence": "3(v+1)d_(v+1)=(3n-v-2)d_v+(3v-2n-7)d_(v-1)+(v-n-4)d_(v-2)",
            "exact_bulk_sum": "B1=sum_(v=1)^M (-1)^(v-1)d_v*h_v/(2v+3), h_v=sum_(k=0)^(v-1)(-1)^k/(2k+3)",
            "universal_algebraic_series": "modulo p, d_v equals c_v=[t^v](1-t)(3+t)(1+t)^(-8/3) for every 0<=v<=M",
            "universal_coefficient_recurrence": "9v*c_v=-3(v+9)c_(v-1)+(9v-14)c_(v-2)+(3v-7)c_(v-3), c_0=3 and negative-index terms zero",
            "universal_theta": "B1=Theta_M modulo p, where Theta_m is the p-independent rational recurrence obtained from c_v and h_v",
            "terminal_coefficients": "c_M=-1 and c_(M-1)=-M modulo p",
            "unit_audit": "L=1; M<p, 2M+3<p, v! is a p-unit for v<=M, and every coefficient, prefix, and outer denominator is a p-unit",
            "moving_prime_criterion": "B1=0 modulo p iff p divides the numerator of reduced rational Theta_((p-2)/3)",
        },
        "exact_witnesses": witnesses,
        "finite_direct_crosscheck": direct,
        "finite_rational_replay": rational,
        "finite_extended_scan": scan,
        "scoped_consequence": {
            "proved": "the singular family is a universal moving-index algebraic-hypergeometric numerator problem with no row-dependent coefficient recurrence",
            "boundary_obstruction": "Theta_3 vanishes modulo 11 on the excluded s=1 boundary, so the recurrence does allow exact moving-prime cancellation",
            "not_proved": "no invariant is known that prevents cancellation for every admissible M>=5",
        },
        "status_ledger": {
            "PROVED": [
                "the exact coefficient sum and coefficient ODE recurrence",
                "the universal algebraic-series and p-independent recurrence reduction",
                "the complete denominator-unit and terminal-coefficient audit",
                "the exact excluded-boundary zero and admissible nonzero witnesses",
            ],
            "EXACT_FINITE": [
                "the bounded direct, rational, and extended recurrence scans",
            ],
            "OPEN": [
                "prove or disprove Theta_((p-2)/3) nonzero modulo every prime p=6s+5 with s>=2",
                "factor or control the moving-prime numerator of Theta_M",
                "obtain any Route-1 rate or capacity reduction",
            ],
        },
        "global_interface": "the singular bulk residual belongs only to the stronger Item239 p^3 carry and does not strengthen the ordinary p^2 common-log gate",
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item247_checker": ITEM247_PATH.name,
            "item247_checker_sha256": ITEM247_SHA256,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
