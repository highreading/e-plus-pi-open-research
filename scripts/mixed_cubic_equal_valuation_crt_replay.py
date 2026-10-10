#!/usr/bin/env python3
"""Finite exact replay of the transverse matching-digit theorem.

The proof is symbolic in mixed_cubic_equal_valuation_crt_reduction.md.
This program independently checks representative ordinary and singular
prime-power branches by recurrence arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def beta_pairs(maximum: int) -> list[tuple[int, int]]:
    pairs = [(1, 1), (3, 1)]
    for index in range(2, maximum + 1):
        pairs.append(
            (
                (4 * index - 2) * pairs[-1][0] + pairs[-2][0],
                (4 * index - 2) * pairs[-1][1] + pairs[-2][1],
            )
        )
    return pairs


def beta_pairs_mod(maximum: int, modulus: int) -> list[tuple[int, int]]:
    pairs = [(1 % modulus, 1 % modulus), (3 % modulus, 1 % modulus)]
    for index in range(2, maximum + 1):
        pairs.append(
            (
                ((4 * index - 2) * pairs[-1][0] + pairs[-2][0]) % modulus,
                ((4 * index - 2) * pairs[-1][1] + pairs[-2][1]) % modulus,
            )
        )
    return pairs


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def roots_mod_prime_power(prime: int, exponent: int) -> list[int]:
    modulus = prime**exponent
    q0, q1 = 1, 1
    roots = [0] if q0 % modulus == 0 else []
    if q1 % modulus == 0:
        roots.append(1)
    for index in range(2, modulus):
        q0, q1 = q1, ((4 * index - 2) * q1 + q0) % modulus
        if q1 == 0:
            roots.append(index)
    return roots


def slope(prime: int, exponent: int, root: int) -> int:
    modulus = prime ** (2 * exponent)
    shift = prime**exponent
    pairs = beta_pairs_mod(root + shift, modulus)
    q_root = pairs[root][1]
    q_shift = pairs[root + shift][1]
    numerator = (-q_shift - q_root) % modulus
    if numerator % shift:
        raise AssertionError((prime, exponent, root, numerator, shift))
    return (numerator // shift) % (prime**exponent)


def ordinary_case(prime: int, exponent: int, root: int, beta: int, a_value: int) -> dict[str, object]:
    modulus = prime**exponent
    delta = slope(prime, exponent, root)
    assert delta % prime
    checks = []
    for epsilon in (-1, 1):
        wanted_parity = 1 if epsilon == -1 else 0
        for j_value in range(1, exponent + 1):
            period = 2 * prime ** (exponent + j_value)
            recurrence_modulus = prime ** (exponent + j_value)
            pairs = beta_pairs_mod(period, recurrence_modulus)
            hits = []
            for index in range(root, period, modulus):
                if index % 2 != wanted_parity:
                    continue
                p_beta, q_beta_residue = pairs[index]
                if q_beta_residue % modulus or q_beta_residue % (prime ** (exponent + 1)) == 0:
                    continue
                local_h = beta * p_beta - epsilon * (q_beta_residue // modulus) * a_value
                if local_h % (prime**j_value) == 0:
                    hits.append(index)
            if len(hits) != 1:
                raise AssertionError((prime, exponent, root, epsilon, j_value, hits))
            checks.append(
                {
                    "epsilon": epsilon,
                    "j": j_value,
                    "period": period,
                    "unique_index": hits[0],
                }
            )
    return {
        "prime": prime,
        "B": exponent,
        "root_mod_p_to_B": root,
        "slope_mod_p_to_B": delta,
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "results"
        / "mixed_cubic_equal_valuation_crt_replay.json",
    )
    args = parser.parse_args()
    cases = []
    # B=1 examples cover several root patterns.  For B=2, choose the unique
    # ordinary descendants of roots modulo p.
    for prime, exponent in ((7, 1), (11, 1), (13, 1), (31, 1), (7, 2), (13, 2)):
        roots = roots_mod_prime_power(prime, exponent)
        ordinary_roots = [root for root in roots if slope(prime, exponent, root) % prime]
        if not ordinary_roots:
            raise AssertionError((prime, exponent, roots))
        root = ordinary_roots[0]
        beta = 2 if prime != 2 else 3
        if beta % prime == 0:
            beta += 1
        a_value = 3
        if a_value % prime == 0:
            a_value = 5
        if math.gcd(a_value, beta * prime**exponent) != 1:
            raise AssertionError((prime, exponent, beta, a_value))
        cases.append(ordinary_case(prime, exponent, root, beta, a_value))

    # The first singular branch: its slope vanishes, so the local matching
    # congruence is constant in the first lift digit (all or no children).
    prime = 79
    exponent = 1
    root = 39
    modulus = prime
    period = 2 * prime ** (exponent + 1)
    pairs = beta_pairs_mod(period, prime**2)
    singular_counts = []
    for epsilon in (-1, 1):
        wanted_parity = 1 if epsilon == -1 else 0
        residues = []
        for index in range(root, period, modulus):
            if index % 2 != wanted_parity:
                continue
            p_beta, q_beta_residue = pairs[index]
            if q_beta_residue % prime or q_beta_residue % (prime**2) == 0:
                continue
            local_h = p_beta - epsilon * (q_beta_residue // modulus)
            residues.append(local_h % prime)
        if len(set(residues)) != 1:
            raise AssertionError((epsilon, residues))
        singular_counts.append(
            {"epsilon": epsilon, "candidate_count": len(residues), "constant_H_mod_p": residues[0]}
        )

    payload = {
        "schema": "mixed-cubic-equal-valuation-crt-replay-v1",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "warning": "finite replay; the theorem is the symbolic congruence proof",
        "ordinary_cases": cases,
        "singular_case": {
            "prime": prime,
            "root": root,
            "slope_mod_p": slope(prime, exponent, root),
            "constant_first_lift_checks": singular_counts,
        },
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(json.dumps({"ordinary_cases": len(cases), "singular": payload["singular_case"]}, indent=2))
    print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
