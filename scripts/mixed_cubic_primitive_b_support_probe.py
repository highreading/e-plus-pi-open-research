#!/usr/bin/env python3
"""Strip primes <= C*m from the actual primitive mixed-cubic coefficient."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SYNC = HERE / "mixed_cubic_positive_match_exact_scan.py"


def load_sync():
    spec = importlib.util.spec_from_file_location("mixed_sync_b_support", SYNC)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SYNC}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MOD = load_sync()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, action="append", required=True)
    parser.add_argument("--factor", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = []
    for m_value in args.m:
        u_value, v_value, content, _, _ = MOD.exact_pi_pair(m_value)
        del u_value
        primitive_b = abs(v_value) // content
        cofactor = primitive_b
        factors = {}
        for prime in MOD.primes_upto(args.factor * m_value):
            exponent = 0
            while cofactor % prime == 0:
                cofactor //= prime
                exponent += 1
            if exponent:
                factors[str(prime)] = exponent
        row = {
            "m": m_value,
            "cutoff": args.factor * m_value,
            "primitive_b_bits": primitive_b.bit_length(),
            "primitive_b_log_per_6m": MOD.log_int(primitive_b) / (6 * m_value),
            "small_prime_factors": factors,
            "cofactor": str(cofactor),
            "cofactor_bits": cofactor.bit_length(),
            "cofactor_log_per_6m": MOD.log_int(cofactor) / (6 * m_value),
            "cofactor_is_one": cofactor == 1,
        }
        rows.append(row)
        print(
            m_value,
            row["primitive_b_log_per_6m"],
            row["cofactor_log_per_6m"],
            row["cofactor_bits"],
            flush=True,
        )
    payload = {
        "schema": "mixed-cubic-primitive-b-support-probe-v1",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "coordinate_source": {
            "filename": SYNC.name,
            "sha256": hashlib.sha256(SYNC.read_bytes()).hexdigest(),
        },
        "warning": "finite exact support diagnostic only",
        "cutoff_rule": f"primes <= {args.factor}m",
        "rows": rows,
    }
    if args.output:
        encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode(
            "utf-8"
        )
        args.output.write_bytes(encoded)
        print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
