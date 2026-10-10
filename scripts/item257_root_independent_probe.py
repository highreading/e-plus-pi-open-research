#!/usr/bin/env python3
"""Independent root probe for Item 257's new row and height claims.

No Item-257 code is imported.  Bounded counts are replay evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
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


def valuation_2(value: int) -> int:
    assert value
    return (value & -value).bit_length() - 1


def reduced_numerator(k: int) -> tuple[int, int]:
    numerator = sum(math.comb(2 * j, j) * 8 ** (k - j) for j in range(k + 1))
    shift = k.bit_count()
    assert valuation_2(numerator) == shift
    reduced = numerator >> shift
    denominator = 1 << (3 * k - shift)
    assert reduced & 1
    assert denominator <= reduced
    assert reduced * reduced < 2 * denominator * denominator
    return reduced, denominator


def s_values(global_index: int) -> list[int]:
    return [
        s
        for s in range(1, max(0, (2 * global_index - 7) // 14) + 1)
        if s % 5 == 3 * (global_index - 1) % 5
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-bound", type=int, default=1200)
    parser.add_argument("--prime-bound", type=int, default=3000)
    parser.add_argument("--prefix-bound", type=int, default=300)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    prime_set = set(primes_up_to(args.prime_bound))
    map_checks = 0
    map_digest_rows: list[str] = []
    for global_index in range(1, args.global_bound + 1):
        forward: set[int] = set()
        for s in s_values(global_index):
            assert (4 * global_index + 2 * s + 1) % 5 == 0
            p = (4 * global_index + 2 * s + 1) // 5
            r = (2 * global_index - 14 * s - 7) // 5
            assert p == 2 * r + 6 * s + 3
            assert r >= 1 and r % 2 == 1
            assert p % 4 == (2 * (s - 1) + 3) % 4
            if p in prime_set:
                assert p > 7 and r % 3
                forward.add(p)
            map_checks += 1
        converse = {
            p
            for p in prime_set
            if p > 7
            and 5 * p >= 4 * global_index + 3
            and 7 * p <= 6 * global_index
        }
        assert forward == converse
        map_digest_rows.append(
            f"{global_index}:{','.join(map(str, sorted(forward)))}\n"
        )

    numerators = []
    prefix_digest_rows: list[str] = []
    for k in range(args.prefix_bound + 1):
        numerator, denominator = reduced_numerator(k)
        numerators.append(numerator)
        prefix_digest_rows.append(f"{k},{numerator},{denominator}\n")

    # Independently replay a smaller exact H-zero census and container divisibility.
    zero_rows: list[tuple[int, int, int]] = []
    for p in primes_up_to(args.prime_bound):
        if p < 11:
            continue
        term = 1
        prefix = 1
        for k in range((p - 11) // 6 + 1):
            if k:
                term = term * (2 * k - 1) * pow(4 * k, -1, p) % p
                prefix = (prefix + term) % p
            s = k + 1
            if (5 * p - 2 * s - 1) % 4:
                continue
            global_index = (5 * p - 2 * s - 1) // 4
            assert p in {
                q
                for q in prime_set
                if q > 7
                and 5 * q >= 4 * global_index + 3
                and 7 * q <= 6 * global_index
            }
            if prefix == 0:
                numerator, denominator = reduced_numerator(k)
                assert math.gcd(denominator, p) == 1
                assert numerator % p == 0
                zero_rows.append((p, k, global_index))

    raw = 2 / 35
    largest_factor_coefficient = 3 * math.log(2) / 7
    quadratic_coefficient = 3 * math.log(2) / 490
    assert largest_factor_coefficient > raw
    assert quadratic_coefficient > 0

    result = {
        "schema": "item257-root-independent-probe-v1",
        "imports_item257_code": False,
        "global_map_checks": map_checks,
        "global_map_digest_sha256": hashlib.sha256(
            "".join(map_digest_rows).encode("ascii")
        ).hexdigest(),
        "prefix_rows": args.prefix_bound + 1,
        "prefix_digest_sha256": hashlib.sha256(
            "".join(prefix_digest_rows).encode("ascii")
        ).hexdigest(),
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.prime_bound,
            "H_zero_rows": len(zero_rows),
            "first_20": zero_rows[:20],
            "zero_digest_sha256": hashlib.sha256(
                "".join(f"{p},{k},{m}\n" for p, k, m in zero_rows).encode("ascii")
            ).hexdigest(),
        },
        "constant_checks": {
            "raw_2_over_35": format(raw, ".15f"),
            "largest_factor_3log2_over7": format(
                largest_factor_coefficient, ".15f"
            ),
            "product_3log2_over490": format(quadratic_coefficient, ".15f"),
            "largest_factor_exceeds_raw": True,
        },
        "verdict": "root replay supports the exact row map, numerator reduction, container divisibility, and scoped zero booking",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

