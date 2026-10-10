#!/usr/bin/env python3
"""Independent audit probe for Item 259's all-jet resolvent.

This implementation does not import the root draft checker.  It works with
exact rational truncated series and explicitly tests the (p,z)^N filtration:
the coefficient of z^j must vanish modulo p^(N-j).
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
            r = numerator // 2
            if 2 * r == numerator and r >= 1 and r % 2 == 1 and r % 3 != 0:
                m = s - 1
                d = r + 4
                assert p == 6 * m + 2 * d + 1
                yield p, r, s, m, d


def frac_mod(value: F, modulus: int) -> int:
    denominator = value.denominator % modulus
    assert math.gcd(denominator, modulus) == 1
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def add(left: list[F], right: list[F]) -> list[F]:
    return [x + y for x, y in zip(left, right)]


def scale(value: F, series: list[F]) -> list[F]:
    return [value * x for x in series]


def mul(left: list[F], right: list[F]) -> list[F]:
    size = len(left)
    out = [F(0) for _ in range(size)]
    for i, x in enumerate(left):
        for j, y in enumerate(right[: size - i]):
            out[i + j] += x * y
    return out


def inverse(series: list[F]) -> list[F]:
    size = len(series)
    assert series[0] != 0
    out = [F(0) for _ in range(size)]
    out[0] = 1 / series[0]
    for n in range(1, size):
        out[n] = -sum((series[k] * out[n - k] for k in range(1, n + 1)), F(0))
        out[n] /= series[0]
    return out


def p_minus_z(series: list[F], p: int) -> list[F]:
    """Return f(p-z) through total (p,z)-degree N-1."""
    size = len(series)
    out = [F(0) for _ in range(size)]
    for degree, coefficient in enumerate(series):
        for z_degree in range(degree + 1):
            out[z_degree] += (
                coefficient
                * math.comb(degree, z_degree)
                * p ** (degree - z_degree)
                * (-1) ** z_degree
            )
    return out


def quotient_zero(series: list[F], p: int) -> bool:
    size = len(series)
    return all(
        frac_mod(coefficient, p ** (size - degree)) == 0
        for degree, coefficient in enumerate(series)
    )


def quotient_equal(left: list[F], right: list[F], p: int) -> bool:
    return quotient_zero(add(left, scale(F(-1), right)), p)


def reciprocal_linear(unit: int, size: int) -> list[F]:
    return [F(1, unit ** (degree + 1)) for degree in range(size)]


def resolvent_series(m: int, d: int, c: F, q: int, size: int) -> list[F]:
    a = 2 * m + d
    out = [F(0) for _ in range(size)]
    for k in range(m + 1):
        denominator = a + q + k
        coefficient = F(math.comb(m, k), 1) * c**k
        for degree in range(size):
            out[degree] += coefficient / denominator ** (degree + 1)
    return out


def transfer_series(
    m: int, d: int, c: F, size: int
) -> tuple[list[F], list[F]]:
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    endpoint = (1 + c) ** length
    one = [F(1)] + [F(0) for _ in range(size - 1)]
    A = one
    E = [F(0) for _ in range(size)]
    for q in range(length):
        denominator_inverse = reciprocal_linear(b + q, size)
        numerator = [F(a + q), F(-1)] + [F(0) for _ in range(size - 2)]
        lam = scale(-1 / c, mul(numerator, denominator_inverse))
        mu = scale(endpoint / c, denominator_inverse)
        E = add(mul(lam, E), mu)
        A = mul(lam, A)
    return A, E


def exact_value(m: int, d: int, c: F, q: int, z: F) -> F:
    a = 2 * m + d
    return sum(
        (
            F(math.comb(m, k), 1) * c**k / (a + q + k - z)
            for k in range(m + 1)
        ),
        F(0),
    )


def exact_transfer(m: int, d: int, c: F, z: F) -> tuple[F, F]:
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


def exact_probe() -> dict[str, object]:
    recurrence = 0
    reflection = 0
    multiplier = 0
    affine = 0
    records: list[str] = []
    for m in range(0, 8):
        for d in range(3, 16, 2):
            p = 6 * m + 2 * d + 1
            length = m + 1
            a = 2 * m + d
            b = 3 * m + d + 1
            for c in (F(-2), F(-1, 2), F(4, 3)):
                ci = 1 / c
                for z in (F(0), F(2, 11), F(-3, 13)):
                    for q in range(length):
                        lhs = (
                            (a + q - z) * exact_value(m, d, c, q, z)
                            + c * (b + q - z) * exact_value(m, d, c, q + 1, z)
                        )
                        assert lhs == (1 + c) ** length
                        recurrence += 1
                    A, E = exact_transfer(m, d, c, z)
                    Ai, Ei = exact_transfer(m, d, ci, p - z)
                    X = exact_value(m, d, c, 0, z)
                    Y = exact_value(m, d, ci, 0, p - z)
                    XL = exact_value(m, d, c, length, z)
                    assert XL == A * X + E
                    assert XL == -(c**m) * Y
                    reflection += 1
                    assert A * Ai == 1
                    multiplier += 1
                    unit = c ** (-m) / A
                    assert Ei == unit * E
                    assert c ** (-m) * X + Ai * Y + Ei == 0
                    affine += 1
                    records.append(f"{m},{d},{c},{z},{A},{E}\n")
    return {
        "recurrence_equalities": recurrence,
        "reflection_equalities": reflection,
        "multiplier_equalities": multiplier,
        "affine_equalities": affine,
        "digest_sha256": hashlib.sha256("".join(records).encode("ascii")).hexdigest(),
    }


def quotient_probe(
    p: int, r: int, s: int, m: int, d: int, maximum_level: int
) -> dict[str, int]:
    checks = 0
    free_target_checks = 0
    involution_checks = 0
    for c in (F(-2), F(-1, 2), F(4, 3)):
        ci = 1 / c
        for level in range(1, maximum_level + 1):
            one = [F(1)] + [F(0) for _ in range(level - 1)]
            zero = [F(0) for _ in range(level)]
            A, E = transfer_series(m, d, c, level)
            Ai_plain, Ei_plain = transfer_series(m, d, ci, level)
            Ai = p_minus_z(Ai_plain, p)
            Ei = p_minus_z(Ei_plain, p)
            X_actual = resolvent_series(m, d, c, 0, level)
            Y_plain = resolvent_series(m, d, ci, 0, level)
            Y_actual = p_minus_z(Y_plain, p)
            XL = resolvent_series(m, d, c, m + 1, level)

            # Exact identities interpreted in R/(p,z)^N.
            assert quotient_equal(XL, add(mul(A, X_actual), E), p)
            assert quotient_equal(XL, scale(-(c**m), Y_actual), p)
            assert quotient_equal(mul(A, Ai), one, p)
            unit = scale(c ** (-m), inverse(A))
            assert quotient_equal(Ei, mul(unit, E), p)
            checks += 4

            # The first functional row may be solved for Y for an arbitrary
            # X-class.  The second row then vanishes by the unit row identity.
            X_free = [
                F((degree + 2) * (m + 2), degree + 1) for degree in range(level)
            ]
            Y_free = scale(
                -(c ** (-m)),
                add(mul(A, X_free), E),
            )
            row_one = add(add(mul(A, X_free), scale(c**m, Y_free)), E)
            row_two = add(
                add(scale(c ** (-m), X_free), mul(Ai, Y_free)),
                Ei,
            )
            assert quotient_equal(row_one, zero, p)
            assert quotient_equal(row_two, zero, p)
            free_target_checks += 2

            # z -> p-z is an automorphism of the filtered quotient; its
            # coordinate matrix has diagonal (-1)^j and its square is one.
            arbitrary = [
                F((degree + 3) * (d + 1), 2 * degree + 1)
                for degree in range(level)
            ]
            assert quotient_equal(p_minus_z(p_minus_z(arbitrary, p), p), arbitrary, p)
            involution_checks += 1

            # Direct coefficient formula for every ordinary jet precision.
            JL = resolvent_series(m, d, c, m + 1, level)
            Jrecip = resolvent_series(m, d, ci, 0, level)
            for order in range(level):
                rhs = F(0)
                for h in range(level - order):
                    rhs += (
                        math.comb(order + h, h)
                        * p**h
                        * Jrecip[order + h]
                    )
                rhs *= (-1) ** (order + 1) * c**m
                assert frac_mod(JL[order] - rhs, p ** (level - order)) == 0
                checks += 1

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "quotient_identity_checks": checks,
        "arbitrary_target_solution_checks": free_target_checks,
        "filtered_involution_checks": involution_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=251)
    parser.add_argument("--max-level", type=int, default=7)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item259_all_jet_resolvent_audit_probe.json",
    )
    args = parser.parse_args()
    assert args.bound >= 43
    assert 1 <= args.max_level <= 10

    exact = exact_probe()
    rows = [
        quotient_probe(*row, args.max_level)
        for row in actual_rows(args.bound)
    ]
    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['d']},"
            f"{row['quotient_identity_checks']},"
            f"{row['arbitrary_target_solution_checks']},"
            f"{row['filtered_involution_checks']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()
    result = {
        "schema": "item259-all-jet-resolvent-independent-audit-v1",
        "imports_draft_checker": False,
        "verdict": "PASS_WITH_RING_AND_SCOPE_CLARIFICATIONS",
        "exact_probe": exact,
        "filtered_quotient_probe": {
            "prime_bound": args.bound,
            "maximum_level": args.max_level,
            "actual_rows": len(rows),
            "quotient_identity_checks": sum(
                row["quotient_identity_checks"] for row in rows
            ),
            "arbitrary_target_solution_checks": sum(
                row["arbitrary_target_solution_checks"] for row in rows
            ),
            "filtered_involution_checks": sum(
                row["filtered_involution_checks"] for row in rows
            ),
            "first_rows": rows[:8],
            "digest_sha256": digest,
            "scope": "independent bounded probe of exact identities; no density inference",
        },
        "audit_findings": {
            "resolvent_recurrence": "pass",
            "exact_reflection": "pass",
            "multiplier_involution": "pass",
            "affine_identity": "pass",
            "every_filtered_quotient": "pass",
            "ordinary_jet_formula": "pass",
            "formal_target_freedom": "pass",
            "required_clarification": (
                "c must first be an indeterminate C for iota to be a ring "
                "automorphism; after specialization, it is an isomorphism between "
                "the paired c and c^-1 systems"
            ),
            "scope_clarification": (
                "target freedom is freedom in the solution module generated by "
                "the recurrence/reflection relations, not a claim that the explicit "
                "binomial resolvent assumes arbitrary arithmetic values"
            ),
        },
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
