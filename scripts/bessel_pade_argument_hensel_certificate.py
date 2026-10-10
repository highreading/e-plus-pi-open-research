#!/usr/bin/env python3
"""Exact certificate for the Padé-argument Hensel no-go."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def scale(a: list[int], c: int) -> list[int]:
    return trim([c * x for x in a])


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def derivative(a: list[int]) -> list[int]:
    if len(a) == 1:
        return [0]
    return [i * a[i] for i in range(1, len(a))]


def evaluate(a: list[int], x: int, modulus: int | None = None) -> int:
    value = 0
    if modulus is None:
        for c in reversed(a):
            value = value * x + c
        return value
    for c in reversed(a):
        value = (value * x + c) % modulus
    return value


def q_polynomials(limit: int) -> list[list[int]]:
    polys = [[1]]
    if limit == 0:
        return polys
    polys.append([2, -1])
    for n in range(2, limit + 1):
        polys.append(add(scale(polys[-1], 4 * n - 2), [0, 0] + polys[-2]))
    return polys


def sequence_triplet(n: int, modulus: int | None = None) -> tuple[int, int, int]:
    # q_n=Q_n(1), p_n=Q_n(-1), d_n=Q_n'(1).
    q0, q1 = 1, 1
    p0, p1 = 1, 3
    d0, d1 = 0, -1
    if n == 0:
        return q0, p0, d0
    if n == 1:
        return q1, p1, d1
    for k in range(2, n + 1):
        c = 4 * k - 2
        old_q0 = q0
        q0, q1 = q1, c * q1 + q0
        p0, p1 = p1, c * p1 + p0
        d0, d1 = d1, c * d1 + 2 * old_q0 + d0
        if modulus is not None:
            q0 %= modulus
            q1 %= modulus
            p0 %= modulus
            p1 %= modulus
            d0 %= modulus
            d1 %= modulus
    return q1, p1, d1


def q_value_at_x(n: int, x: int, modulus: int) -> int:
    q0, q1 = 1 % modulus, (2 - x) % modulus
    if n == 0:
        return q0
    if n == 1:
        return q1
    x2 = x * x % modulus
    for k in range(2, n + 1):
        q0, q1 = q1, ((4 * k - 2) * q1 + x2 * q0) % modulus
    return q1


def valuation(x: int, p: int) -> int:
    if x == 0:
        raise ValueError("valuation requested for zero")
    a = 0
    while x % p == 0:
        x //= p
        a += 1
    return a


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/bessel_pade_argument_hensel_certificate.json"),
    )
    args = parser.parse_args()

    polynomial_limit = 14
    polys = q_polynomials(polynomial_limit)
    wronskian_checks = []
    recurrence_checks = 0
    for n, qpoly in enumerate(polys):
        ppoly = [((-1) ** k) * c for k, c in enumerate(qpoly)]
        lhs = add(
            add(mul(derivative(ppoly), qpoly), scale(mul(ppoly, derivative(qpoly)), -1)),
            scale(mul(ppoly, qpoly), -1),
        )
        rhs = [0] * (2 * n) + [(-1) ** (n + 1)]
        assert trim(lhs) == trim(rhs)
        assert evaluate(qpoly, 1) == sequence_triplet(n)[0]
        assert evaluate(qpoly, -1) == sequence_triplet(n)[1]
        if n >= 2:
            expected = add(scale(polys[n - 1], 4 * n - 2), [0, 0] + polys[n - 2])
            assert qpoly == expected
            recurrence_checks += 1
        wronskian_checks.append(n)

    inverse_limit = 80
    inverse_checks = 0
    height_checks = 0
    for n in range(inverse_limit + 1):
        qn, pn, dn = sequence_triplet(n)
        assert (pn * dn - (-1) ** n) % qn == 0
        inverse_checks += 1
        # The coefficient ratio is strictly below one, so c_{n,0} is maximal.
        if n:
            c = 1
            for j in range(n + 1, 2 * n + 1):
                c *= j
            prev = c
            for k in range(n):
                numerator = prev * (n - k)
                denominator = (k + 1) * (2 * n - k)
                assert numerator % denominator == 0
                nxt = numerator // denominator
                assert nxt < prev
                prev = nxt
        height_checks += 1

    examples = [(8, 13, 2), (18, 7, 3), (361, 7, 4), (1359, 11, 5)]
    hensel_records = []
    for n, p, expected_a in examples:
        exact_q, _, _ = sequence_triplet(n)
        assert valuation(exact_q, p) == expected_a
        modulus = p ** (2 * expected_a)
        qn, pn, dn = sequence_triplet(n, modulus)
        assert qn == exact_q % modulus
        assert (pn * dn - (-1) ** n) % modulus % (p**expected_a) == 0
        xi = (1 - ((-1) ** n) * pn * qn) % modulus
        assert q_value_at_x(n, xi, modulus) == 0
        displacement = (xi - 1) % modulus
        assert displacement != 0
        assert valuation(displacement, p) == expected_a
        hensel_records.append(
            {
                "n": n,
                "p": p,
                "valuation": expected_a,
                "modulus": modulus,
                "root_mod_p_to_2a": xi,
                "root_displacement_mod_p_to_2a": displacement,
                "Q_at_root_mod_p_to_2a": 0,
            }
        )

    payload = {
        "description": "Exact finite regression certificate for the Padé-argument Hensel no-go",
        "polynomial_wronskian_degrees": wronskian_checks,
        "polynomial_recurrence_checks": recurrence_checks,
        "full_modulus_inverse_checks": inverse_checks,
        "coefficient_height_checks": height_checks,
        "hensel_examples": hensel_records,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
