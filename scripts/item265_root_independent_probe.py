#!/usr/bin/env python3
"""Independent root-side arithmetic probe for Item 265.

All bounded loops are identity checks only.  They are not evidence for an
asymptotic squarefull estimate or for the absence of exceptional primes.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


def denominators(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def reverse_bessel_value(n: int, x: int) -> int:
    return sum(
        math.factorial(2 * n - k)
        // (math.factorial(k) * math.factorial(n - k))
        * x**k
        for k in range(n + 1)
    )


def transfer(d: int, n: int) -> int:
    if d == 0:
        return 0
    left, right = 0, 1
    for offset in range(d - 1):
        left, right = right, (4 * n + 4 * offset + 6) * right + left
    return right


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            out[divisor] = out.get(divisor, 0) + 1
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def check_sequence() -> dict[str, int]:
    q = denominators(120)
    reverse_rows = 0
    product_rows = 0
    transfer_rows = 0
    gcd_rows = 0
    for n in range(31):
        assert reverse_bessel_value(n, -1) == q[n]
        reverse_rows += 1
    for n in range(2, 121):
        lower = math.factorial(2 * n) // (2 * math.factorial(n))
        upper = 4 ** (n - 1) * math.factorial(n)
        assert lower < q[n] < upper
        product_rows += 1
    for n in range(41):
        for d in range(1, 17):
            rhs = transfer(d, n) * q[n + 1]
            rhs += transfer(d - 1, n + 1) * q[n]
            assert rhs == q[n + d]
            assert math.gcd(q[n], q[n + d]) == math.gcd(q[n], transfer(d, n))
            transfer_rows += 1
            gcd_rows += 1
    return {
        "reverse_bessel_specializations": reverse_rows,
        "strict_product_bounds": product_rows,
        "transfer_identities": transfer_rows,
        "gcd_identities": gcd_rows,
    }


def check_powerful_part() -> dict[str, int]:
    exponent_rows = 0
    for exponents in itertools.product(range(8), repeat=4):
        e_exp = sum(max(v - 1, 0) for v in exponents)
        squarefull_exp = sum(v if v >= 2 else 0 for v in exponents)
        assert e_exp <= squarefull_exp <= 2 * e_exp
        exponent_rows += 1

    q = denominators(11)
    factored_rows = 0
    for n in range(2, 12):
        fac = factor(q[n])
        radical = math.prod(fac)
        excess = q[n] // radical
        squarefull = math.prod(p**v for p, v in fac.items() if v >= 2)
        assert q[n] % radical == 0
        assert squarefull % excess == 0
        assert excess * excess % squarefull == 0
        factored_rows += 1
    return {
        "abstract_exponent_vectors": exponent_rows,
        "factored_sequence_values": factored_rows,
    }


def check_overlap_normalization(bound: int = 11) -> dict[str, int]:
    rows = 0
    for matching in range(2 * bound + 1):
        for denominator in range(bound + 1):
            for q_exp in range(bound + 1):
                if matching > 2 * q_exp:
                    continue
                quotient = max(matching - 2 * denominator, 0)
                normalized_square = 2 * max(q_exp - denominator, 0)
                assert quotient <= normalized_square
                rows += 1
    return {"primewise_overlap_inequalities": rows}


def check_singleton_envelope() -> dict[str, int]:
    rows = 0
    # Four block indices and one prime are enough to test the sorted-level
    # inequality prime by prime; additivity then gives the general statement.
    for heights in itertools.product(range(6), repeat=4):
        total = sum(heights)
        singleton = max(heights)
        pair_overlap = sum(
            min(heights[i], heights[j])
            for i in range(4)
            for j in range(i + 1, 4)
        )
        assert singleton <= total <= singleton + pair_overlap
        rows += 1
    return {"singleton_envelope_vectors": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = {
        "schema": "item265-root-independent-probe-v1",
        "scope": (
            "independent bounded identity checks only; no exceptional-prime "
            "search and no finite-to-asymptotic inference"
        ),
        "checks": {
            "sequence": check_sequence(),
            "powerful_part": check_powerful_part(),
            "overlap": check_overlap_normalization(),
            "singleton": check_singleton_envelope(),
        },
        "strict_labels": {
            "bounded_checks": "EXACT FINITE ONLY",
            "global_squarefull_little_oh": "OPEN",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
        },
    }
    Path(args.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
