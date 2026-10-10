#!/usr/bin/env python3
"""Finite scan of the exceptional fresh-prime ray p = 10m + 3.

The scalar Taylor recurrence is evaluated modulo p through degrees 4m+1.
This is only a bounded experiment; it does not prove nonvanishing beyond
the reported range.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def prime_flags(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return flags


def exceptional_data(m_value: int) -> dict[str, int | bool]:
    prime = 10 * m_value + 3
    target = 4 * m_value + 1
    inverses = [0] * (target + 1)
    inverses[1] = 1
    for index in range(2, target + 1):
        inverses[index] = (
            prime - (prime // index) * inverses[prime % index] % prime
        )

    inverse_minus_four = pow(prime - 4, prime - 2, prime)
    coefficients = [pow(2, 2 * m_value - 2, prime)]
    for degree in range(target):
        rhs = (20 * m_value - 8 - 10 * degree) * coefficients[degree]
        if degree >= 1:
            rhs += (
                (10 * degree + 10 - 20 * m_value)
                * coefficients[degree - 1]
            )
        if degree >= 2:
            rhs += (
                (10 * m_value - 5 * degree - 6)
                * coefficients[degree - 2]
            )
        if degree >= 3:
            rhs += (
                (degree + 1 - 4 * m_value) * coefficients[degree - 3]
            )
        coefficients.append(
            rhs * inverses[degree + 1] * inverse_minus_four % prime
        )

    f_4m_plus_1 = coefficients[target]
    f_4m = coefficients[target - 1]
    ell_0 = (
        2 * coefficients[target - 1]
        - 2 * coefficients[target - 2]
        + coefficients[target - 3]
    ) % prime
    return {
        "m": m_value,
        "p": prime,
        "ell0_mod_p": ell_0,
        "ell1_over_2_mod_p": f_4m_plus_1,
        "f_4m_mod_p": f_4m,
        "common_log_zero": ell_0 == 0 and f_4m_plus_1 == 0,
        "consecutive_zero": f_4m == 0 and f_4m_plus_1 == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=10_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    flags = prime_flags(10 * args.max_m + 3)
    tested = 0
    common_log_zeros = []
    consecutive_zeros = []
    for m_value in range(1, args.max_m + 1):
        if not flags[10 * m_value + 3]:
            continue
        tested += 1
        row = exceptional_data(m_value)
        if row["common_log_zero"]:
            common_log_zeros.append(row)
        if row["consecutive_zero"]:
            consecutive_zeros.append(row)
        if tested % 500 == 0:
            print("tested", tested, "last_m", m_value, flush=True)

    payload = {
        "schema": "mixed-cubic-exceptional-fresh-prime-scan-v2",
        "generator": Path(__file__).name,
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "max_m": args.max_m,
        "exceptional_ray": "p = 10m + 3 prime",
        "tested_m": tested,
        "common_log_zeros": common_log_zeros,
        "consecutive_taylor_zeros": consecutive_zeros,
        "warning": "finite modular scan only",
    }
    rendered = json.dumps(payload, indent=2) + "\n"
    print(rendered)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()

