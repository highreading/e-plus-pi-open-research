#!/usr/bin/env python3
"""Verify finite support/rate statements from an exact mixed-cubic scan."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=HERE.parent
        / "results"
        / "mixed_cubic_positive_match_exact_scan_m100_N6m.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE.parent
        / "results"
        / "mixed_cubic_content_support_scan_m100.json",
    )
    args = parser.parse_args()
    raw = args.input.read_bytes()
    data = json.loads(raw)
    rows = []
    for record in data["rows"]:
        m_value = int(record["m"])
        remainder = int(record["extra_content"])
        factors: dict[str, int] = {}
        for prime in primes_upto(6 * m_value):
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            if exponent:
                factors[str(prime)] = exponent
        rows.append(
            {
                "m": m_value,
                "residual_after_primes_at_most_6m": str(remainder),
                "largest_prime_factor_if_fully_factored": (
                    max(map(int, factors)) if remainder == 1 else None
                ),
            }
        )
    tail = [record for record in data["rows"] if int(record["m"]) >= 80]
    maximum = max(
        tail,
        key=lambda record: record["maximum_total_content_in_window"]["log_per_n"],
    )
    payload = {
        "schema": "mixed-cubic-content-support-scan-v1",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "input": args.input.name,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "row_count": len(rows),
        "all_m_1_to_100_content_supported_on_primes_at_most_6m": (
            [row["m"] for row in rows] == list(range(1, 101))
            and all(row["residual_after_primes_at_most_6m"] == "1" for row in rows)
        ),
        "maximum_total_content_rate_for_m_at_least_80": {
            "m": maximum["m"],
            "N": maximum["maximum_total_content_in_window"]["N"],
            "log_per_6m": maximum["maximum_total_content_in_window"]["log_per_n"],
        },
        "rows": rows,
        "warning": "Exact finite verification only; no support or rate extrapolation.",
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(json.dumps({key: value for key, value in payload.items() if key != "rows"}, indent=2))
    print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
