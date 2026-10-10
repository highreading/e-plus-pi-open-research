#!/usr/bin/env python3
"""Exact contiguous support scan for gcd(2^(2m)L0, 2^(2m+2)L1).

The normalized Taylor coefficients are computed by a scalar integer
recurrence.  After taking the exact gcd, every prime at most 6m is removed.
Any remaining factor would be a genuine fresh-prime obstruction.  A bounded
scan with remainder one is finite evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(flags) if flag]


def normalized_log_pair(m_value: int) -> tuple[int, int]:
    """Return (2^(2m)L0, 2^(2m+2)L1) exactly."""
    target = 4 * m_value + 1
    coefficient = [1]
    for degree in range(target):
        rhs = (20 * m_value - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += (
                2
                * (10 * degree + 10 - 20 * m_value)
                * coefficient[degree - 1]
            )
        if degree >= 2:
            rhs += (
                4
                * (10 * m_value - 5 * degree - 6)
                * coefficient[degree - 2]
            )
        if degree >= 3:
            rhs += (
                8
                * (degree + 1 - 4 * m_value)
                * coefficient[degree - 3]
            )
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise ArithmeticError((m_value, degree, rhs, divisor))
        coefficient.append(quotient)

    ell0 = (
        coefficient[target - 1]
        - 2 * coefficient[target - 2]
        + 2 * coefficient[target - 3]
    )
    ell1 = coefficient[target]
    return ell0, ell1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=2_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = primes_upto(6 * args.max_m)
    fresh_rows = []
    maxima = {
        "ell0_bits": {"bits": 0, "m": 0},
        "ell1_bits": {"bits": 0, "m": 0},
        "gcd_bits": {"bits": 0, "m": 0},
    }
    for m_value in range(1, args.max_m + 1):
        ell0, ell1 = normalized_log_pair(m_value)
        common = math.gcd(abs(ell0), abs(ell1))
        remainder = common
        for prime in primes:
            if prime > 6 * m_value:
                break
            while remainder % prime == 0:
                remainder //= prime
        if remainder != 1:
            fresh_rows.append(
                {
                    "m": m_value,
                    "residual_after_primes_at_most_6m": str(remainder),
                    "residual_bits": remainder.bit_length(),
                }
            )
            print("FRESH", fresh_rows[-1], flush=True)

        for name, value in (
            ("ell0_bits", abs(ell0).bit_length()),
            ("ell1_bits", abs(ell1).bit_length()),
            ("gcd_bits", common.bit_length()),
        ):
            if value > maxima[name]["bits"]:
                maxima[name] = {"bits": value, "m": m_value}
        if m_value % 250 == 0:
            print("progress", m_value, flush=True)

    payload = {
        "schema": "mixed-cubic-log-residue-exact-support-scan-v2",
        "generator": Path(__file__).name,
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "max_m": args.max_m,
        "tested_m": args.max_m,
        "normalization": {
            "ell0": "2^(2m) L0",
            "ell1": "2^(2m+2) L1",
        },
        "fresh_rows": fresh_rows,
        "all_gcd_prime_factors_at_most_6m": not fresh_rows,
        "maxima": maxima,
        "warning": "finite exact scan only",
    }
    rendered = json.dumps(payload, indent=2) + "\n"
    print(rendered)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()

