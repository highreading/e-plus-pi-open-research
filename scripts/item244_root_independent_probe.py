#!/usr/bin/env python3
"""Independent actual-family Abel checks for frozen Item 244."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


ROWS = [
    (17, 2),
    (19, 2),
    (23, 2),
    (29, 2),
    (29, 4),
    (101, 2),
    (101, 16),
    (401, 2),
    (503, 2),
    (809, 2),
    (1009, 2),
]


def trim(values):
    values = list(values)
    while values and values[-1] == 0:
        values.pop()
    return values


def convolution(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right):
            if y:
                out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def binomial_factor(exponent, sign, step, p):
    values = [0] * (step * exponent + 1)
    for k in range(exponent + 1):
        values[step * k] = math.comb(exponent, k) * (sign**k) % p
    return values


def actual_polynomial(p, s, nu):
    r = (p - 6 * s - 3) // 2
    if 2 * r + 6 * s + 3 != p or r < 1:
        raise ValueError((p, s))
    result = binomial_factor(r, -1, 1, p)
    result = convolution(result, binomial_factor(1 + 3 * nu, 1, 1, p), p)
    result = convolution(result, binomial_factor(2 * s - nu, 1, 2, p), p)
    return r, result


def factored_projection(p, s, nu, r):
    a = 1 + 3 * nu
    q = 2 * s - nu
    delta = r % 2
    common = min(r, a)
    gap = abs(r - a)
    if gap < delta:
        return []
    parity = [
        math.comb(gap, 2 * j + delta) % p
        for j in range((gap - delta) // 2 + 1)
    ]
    if r >= a and delta:
        parity = [(-x) % p for x in parity]
    result = binomial_factor(common, -1, 1, p)
    result = convolution(result, binomial_factor(q, 1, 1, p), p)
    return convolution(result, parity, p)


def character_prefixes(p):
    h = (p - 1) // 2
    values = [0] * (h + 1)
    for u in range(h):
        term = pow(2 * u + 1, -1, p)
        values[u + 1] = (values[u] + (term if u % 2 == 0 else -term)) % p
    return values


def coordinate(p, s, nu):
    r, polynomial = actual_polynomial(p, s, nu)
    delta = r % 2
    selected = trim(polynomial[delta::2])
    factored = factored_projection(p, s, nu, r)
    failures = []
    if selected != factored:
        failures.append("parity_factor")
    expected_zero = nu == 0 and r == 1
    if (not selected) != expected_zero:
        failures.append("zero_classification")
    if not selected:
        return {
            "p": p,
            "s": s,
            "nu": nu,
            "r": r,
            "projection_zero": True,
            "sine": 0,
            "bulk": 0,
            "character": 0,
            "old_j": 0,
            "failures": failures,
        }

    lower = (r + 1) // 2
    degree = len(selected) - 1
    prefixes = character_prefixes(p)
    weights = []
    for k, coefficient in enumerate(selected):
        denominator = 2 * (lower + k) + 1
        if not 1 <= denominator < p:
            failures.append("range")
        weights.append(coefficient * pow(denominator, -1, p) % p)

    q_tail = [0] * (degree + 2)
    bulk_state = [0] * (degree + 1)
    for k in range(degree, -1, -1):
        q_tail[k] = (weights[k] - q_tail[k + 1]) % p
        if k < degree:
            denominator = 2 * (lower + k) + 1
            bulk_state[k] = (
                bulk_state[k + 1]
                + q_tail[k + 1] * pow(denominator, -1, p)
            ) % p

    sine = sum(((-1) ** (lower + k)) * value for k, value in enumerate(weights)) % p
    if q_tail[0] != ((-1) ** lower) * sine % p:
        failures.append("q0_sine")
    character = 0
    for k, value in enumerate(weights):
        u = lower + k
        r_u = ((-1) ** u) * prefixes[u] % p
        character += 90 * value * r_u
    character %= p
    bulk = bulk_state[0]
    abel = (90 * prefixes[lower] * sine - 90 * bulk) % p
    if character != abel:
        failures.append("abel")

    chi = -1 if ((p - 1) // 2) % 2 else 1
    old_j = sum(
        (-2 * chi) * ((-1) ** (lower + k)) * value
        for k, value in enumerate(weights)
    ) % p
    if old_j != (-2 * chi * sine) % p:
        failures.append("old_endpoint")

    return {
        "p": p,
        "s": s,
        "nu": nu,
        "r": r,
        "projection_zero": False,
        "projected_degree": degree,
        "sine": sine,
        "bulk": bulk,
        "character": character,
        "old_j": old_j,
        "failures": failures,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = [coordinate(p, s, nu) for p, s in ROWS for nu in (0, 1)]
    failures = [row for row in rows if row["failures"]]
    lookup = {(row["p"], row["s"], row["nu"]): row for row in rows}
    witness_17 = lookup[(17, 2, 1)]
    ratios_19 = [
        lookup[(19, 2, nu)]["bulk"] * pow(lookup[(19, 2, nu)]["sine"], -1, 19) % 19
        for nu in (0, 1)
    ]
    if (witness_17["bulk"], witness_17["character"]) != (9, 7):
        failures.append({"witness_17": witness_17})
    if ratios_19 != [5, 12]:
        failures.append({"ratios_19": ratios_19})

    digest_payload = "\n".join(
        ",".join(
            map(
                str,
                [
                    row["p"], row["s"], row["nu"], row["r"],
                    int(row["projection_zero"]), row["sine"],
                    row["bulk"], row["character"], row["old_j"],
                ],
            )
        )
        for row in rows
    )
    result = {
        "schema": "item244-root-independent-audit-v1",
        "classification": "EXACT_INDEPENDENT_AUDIT",
        "actual_rows": ROWS,
        "coordinate_count": len(rows),
        "maximum_prime": max(p for p, _ in ROWS),
        "zero_projection_count": sum(row["projection_zero"] for row in rows),
        "witness_17": {
            "bulk": witness_17["bulk"],
            "character": witness_17["character"],
        },
        "ratios_19": ratios_19,
        "row_digest": hashlib.sha256(digest_payload.encode("ascii")).hexdigest(),
        "failures": failures,
        "all_pass": not failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
