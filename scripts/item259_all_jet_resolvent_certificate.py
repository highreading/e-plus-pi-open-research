#!/usr/bin/env python3
"""Exact portable checker for Item 259's all-jet resolvent involution.

The script uses only Python's standard library.  Exact rational identities
are separated from bounded actual-row checks, which are finite evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


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


def actual_rows(bound: int):
    for p in primes_up_to(bound):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                m = s - 1
                d = r + 4
                assert p == 6 * m + 2 * d + 1
                yield p, r, s, m, d


def frac_mod(value: F, modulus: int) -> int:
    denominator = value.denominator % modulus
    assert math.gcd(denominator, modulus) == 1
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def jet(m: int, d: int, c: F, q: int, order: int) -> F:
    a = 2 * m + d
    return sum(
        (
            F(math.comb(m, k), (a + q + k) ** (order + 1)) * c**k
            for k in range(m + 1)
        ),
        F(0),
    )


def resolvent(m: int, d: int, c: F, q: int, z: F) -> F:
    a = 2 * m + d
    return sum(
        (F(math.comb(m, k), 1) * c**k / (a + q + k - z) for k in range(m + 1)),
        F(0),
    )


def transfer(m: int, d: int, c: F, z: F) -> tuple[F, F]:
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    endpoint = (1 + c) ** length
    A = F(1)
    E = F(0)
    for q in range(length):
        lam = -F(a + q, 1) + z
        lam /= c * (b + q - z)
        mu = endpoint / (c * (b + q - z))
        E = lam * E + mu
        A = lam * A
    return A, E


def exact_functional_audit() -> dict[str, object]:
    recurrence_checks = 0
    reflection_checks = 0
    multiplier_checks = 0
    affine_checks = 0
    rows: list[str] = []
    for m in range(0, 9):
        for d in range(3, 18, 2):
            p = 6 * m + 2 * d + 1
            length = m + 1
            for c in (F(-2), F(-1, 2), F(3, 2)):
                ci = 1 / c
                for z in (F(0), F(1, 7), F(-2, 9)):
                    # Avoid the finitely many poles in deliberately generic samples.
                    for q in range(length):
                        lhs = (
                            (2 * m + d + q - z) * resolvent(m, d, c, q, z)
                            + c
                            * (3 * m + d + q + 1 - z)
                            * resolvent(m, d, c, q + 1, z)
                        )
                        assert lhs == (1 + c) ** length
                        recurrence_checks += 1

                    A, E = transfer(m, d, c, z)
                    Ai, Ei = transfer(m, d, ci, p - z)
                    X = resolvent(m, d, c, 0, z)
                    Y = resolvent(m, d, ci, 0, p - z)
                    XL = resolvent(m, d, c, length, z)
                    assert XL == A * X + E
                    assert XL == -(c**m) * Y
                    reflection_checks += 1
                    assert A * Ai == 1
                    multiplier_checks += 1
                    assert Ei == c ** (-m) * E / A
                    assert c ** (-m) * X + Ai * Y + Ei == 0
                    affine_checks += 1
                    rows.append(f"{m},{d},{c},{z},{A},{E}\n")

    return {
        "resolvent_recurrence_equalities": recurrence_checks,
        "exact_reflection_equalities": reflection_checks,
        "multiplier_involution_equalities": multiplier_checks,
        "affine_compatibility_equalities": affine_checks,
        "digest_sha256": hashlib.sha256("".join(rows).encode("ascii")).hexdigest(),
    }


def filtered_reflection_audit(
    p: int, r: int, s: int, m: int, d: int, max_level: int
) -> dict[str, int]:
    checks = 0
    c = F(-2)
    for value in (c, 1 / c):
        for level in range(1, max_level + 1):
            for order in range(level):
                rhs = F(0)
                for h in range(level - order):
                    rhs += (
                        math.comb(order + h, h)
                        * p**h
                        * jet(m, d, 1 / value, 0, order + h)
                    )
                rhs *= (-1) ** (order + 1) * value**m
                modulus = p ** (level - order)
                assert frac_mod(jet(m, d, value, m + 1, order) - rhs, modulus) == 0
                checks += 1

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "max_level": max_level,
        "filtered_reflection_congruences": checks,
    }


def triangular_recurrence_audit() -> dict[str, int]:
    checks = 0
    for m in range(0, 9):
        for d in range(3, 18, 2):
            for c in (F(-2), F(-1, 2), F(3, 2)):
                endpoint = (1 + c) ** (m + 1)
                for q in range(m + 1):
                    for order in range(6):
                        lhs = (
                            (2 * m + d + q) * jet(m, d, c, q, order)
                            + c
                            * (3 * m + d + q + 1)
                            * jet(m, d, c, q + 1, order)
                        )
                        rhs = endpoint if order == 0 else (
                            jet(m, d, c, q, order - 1)
                            + c * jet(m, d, c, q + 1, order - 1)
                        )
                        assert lhs == rhs
                        checks += 1
    return {"triangular_jet_recurrence_equalities": checks}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=401)
    parser.add_argument("--max-level", type=int, default=6)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item259_all_jet_resolvent_certificate.json",
    )
    args = parser.parse_args()
    assert args.bound >= 43
    assert 1 <= args.max_level <= 10

    exact = exact_functional_audit()
    triangular = triangular_recurrence_audit()
    rows = [
        filtered_reflection_audit(*values, args.max_level)
        for values in actual_rows(args.bound)
    ]
    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['d']},"
            f"{row['filtered_reflection_congruences']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item259-all-jet-resolvent-certificate-v1",
        "status": "PROVED_AFTER_INDEPENDENT_AUDIT_WITH_RING_AND_SCOPE_CLARIFICATIONS",
        "imports_item_code": False,
        "theorems": {
            "resolvent_recurrence": (
                "(a+q-z)M_q(c;z)+c(b+q-z)M_(q+1)(c;z)=(1+c)^L"
            ),
            "exact_reflection": "M_L(c;z)=-c^m M_0(c^-1;p-z)",
            "multiplier_involution": "A_c(z) A_(c^-1)(p-z)=1",
            "exact_rank": 1,
            "filtered_quotients": "the same row dependence holds in every (p,z)^N quotient",
            "scoped_no_go": (
                "all finite reciprocal denominator-jet towers from these identities "
                "supply no compatibility condition on the target moment"
            ),
            "scope_of_target_freedom": (
                "freedom in the solution module generated by recurrence/reflection; "
                "not a claim that the explicit binomial resolvent assumes arbitrary values"
            ),
        },
        "exact_functional_audit": exact,
        "triangular_recurrence_audit": triangular,
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(rows),
            "maximum_filtered_level": args.max_level,
            "filtered_reflection_congruences": sum(
                row["filtered_reflection_congruences"] for row in rows
            ),
            "first_rows": rows[:8],
            "row_digest_sha256": digest,
            "scope": "bounded replay only; no density or rate inference",
        },
        "OPEN": [
            "arithmetic control of the punctured half-binomial period",
            "an independent period or nonlinear relation outside the reciprocal jet tower",
            "any positive or zero weighted-rate theorem for the actual gate",
            "any new Route-1 exponent or conclusion about e+pi",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
