#!/usr/bin/env python3
"""Exact factor-support probe for the item-133 post-Cartier content.

This is a diagnostic helper.  It never promotes finite factorization data to
an asymptotic statement.  Coordinates are recomputed from the archived exact
rational Hermite reduction.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SYNC = HERE / "mixed_cubic_positive_match_exact_scan.py"


def load_sync():
    spec = importlib.util.spec_from_file_location("mixed_sync", SYNC)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SYNC}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MOD = load_sync()


def valuation(value: int, prime: int) -> int:
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def row(m_value: int, prime_factor: int) -> dict[str, object]:
    u_value, v_value, content, sharp_clearing, cartier = MOD.exact_pi_pair(m_value)
    bound = max(2, prime_factor * m_value)
    small_factors: dict[str, int] = {}
    remainder = content
    for prime in MOD.primes_upto(bound):
        exponent = valuation(remainder, prime)
        if exponent:
            small_factors[str(prime)] = exponent
            remainder //= prime**exponent
    return {
        "m": m_value,
        "content": str(content),
        "content_bits": content.bit_length(),
        "content_log_per_6m": MOD.log_int(content) / (6 * m_value),
        "trial_bound": bound,
        "factors_at_most_bound": small_factors,
        "cofactor": str(remainder),
        "cofactor_bits": remainder.bit_length(),
        "cofactor_is_one": remainder == 1,
        "vp_u_minus_vp_cartier_for_small_primes": {
            str(prime): [valuation(abs(u_value), prime), valuation(abs(v_value), prime)]
            for prime in MOD.primes_upto(6 * m_value)
            if u_value % prime == 0 or v_value % prime == 0
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-m", type=int, default=1)
    parser.add_argument("--max-m", type=int, default=36)
    parser.add_argument("--prime-factor", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = []
    for m_value in range(args.min_m, args.max_m + 1):
        result = row(m_value, args.prime_factor)
        rows.append(result)
        print(
            m_value,
            result["content_log_per_6m"],
            result["factors_at_most_bound"],
            "cofactor_bits",
            result["cofactor_bits"],
            flush=True,
        )
    if args.output:
        payload = {
            "schema": "mixed-cubic-content-factor-probe-v1",
            "generator": {
                "filename": Path(__file__).name,
                "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            },
            "coordinate_source": {
                "filename": SYNC.name,
                "sha256": hashlib.sha256(SYNC.read_bytes()).hexdigest(),
            },
            "warning": "finite exact diagnostic only",
            "rows": rows,
        }
        encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode(
            "utf-8"
        )
        args.output.write_bytes(encoded)
        print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
