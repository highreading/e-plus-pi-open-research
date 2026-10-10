#!/usr/bin/env python3
"""Exact diagnostics for the equal-valuation part of mixed-cubic matching.

This is exploratory and writes only under work/.  It recomputes the actual
post-Cartier primitive coefficient b_m, the beta pairs (p_N,q_N), and the
local decomposition

    Delta = gcd(b_m,q_N),
    Eeq   = product_{v_l(b_m)=v_l(q_N)>0} l^v_l(q_N),
    g     = gcd(b0*p_N-epsilon*q0*a_m, Delta).

The theorem-level identity behind the diagnostic is g | Eeq | Delta.
No finite scan is promoted to an asymptotic statement.
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
    spec = importlib.util.spec_from_file_location("mixed_sync_equal", SYNC)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SYNC}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MOD = load_sync()


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factor_integer(value: int) -> dict[int, int]:
    """Factor a gcd-sized integer by trial division; residual is prime-tested."""
    value = abs(value)
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            factors[prime] = exponent
        prime = 3 if prime == 2 else prime + 2
    if value > 1:
        factors[value] = 1
    return factors


def equal_part(b_value: int, q_value: int, delta: int) -> tuple[int, dict[str, object]]:
    factors = factor_integer(delta)
    equal = 1
    ledger: dict[str, object] = {}
    for prime, shared_exponent in factors.items():
        b_exponent = valuation(b_value, prime)
        q_exponent = valuation(q_value, prime)
        is_equal = b_exponent == q_exponent
        if is_equal:
            equal *= prime**shared_exponent
        ledger[str(prime)] = {
            "v_b": b_exponent,
            "v_q": q_exponent,
            "v_delta": shared_exponent,
            "equal_positive_level": is_equal,
        }
    return equal, ledger


def target_index(m_value: int, t_value: float) -> int:
    n_value = 6 * m_value
    estimate = max(1, int(t_value * n_value / math.log(max(3, n_value))))
    candidates = range(max(1, estimate // 2), 2 * estimate + 20)
    return min(candidates, key=lambda index: abs(index * math.log(index) / n_value - t_value))


def orient(
    u_value: int, v_value: int, content: int, pi_lower, pi_upper
) -> tuple[int, int, int]:
    a_value, b_value, epsilon, _, _ = MOD.oriented_form_exact(
        u_value, v_value, content, pi_lower, pi_upper
    )
    return a_value, b_value, epsilon


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-m", type=int, default=1)
    parser.add_argument("--max-m", type=int, default=100)
    parser.add_argument("--step", type=int, default=1)
    parser.add_argument("--relative-window", type=float, default=0.20)
    parser.add_argument("--t", type=float, default=2.337062374358973 / 2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.step < 1:
        raise ValueError("--step must be positive")
    m_values = list(range(args.min_m, args.max_m + 1, args.step))
    raw_coordinates = [MOD.exact_pi_pair(m_value) for m_value in m_values]
    maximum_digits = max(
        max(len(str(abs(record[0]))), len(str(abs(record[1]))))
        for record in raw_coordinates
    )
    pi_lower, pi_upper, _ = MOD.machin_pi_bounds(maximum_digits + 40)
    targets = [target_index(m_value, args.t) for m_value in m_values]
    maximum_n = max(
        int(math.ceil((1 + args.relative_window) * target)) + 4
        for target in targets
    )
    beta = MOD.beta_pairs(maximum_n)
    rows: list[dict[str, object]] = []

    for offset, m_value in enumerate(m_values):
        n_value = 6 * m_value
        target = targets[offset]
        u_value, v_value, content, _, _ = raw_coordinates[offset]
        a_value, b_value, epsilon = orient(
            u_value, v_value, content, pi_lower, pi_upper
        )
        start = max(1, int(math.floor((1 - args.relative_window) * target)))
        stop = int(math.ceil((1 + args.relative_window) * target))
        candidates: list[dict[str, object]] = []
        for index in range(start, stop + 1):
            if (-1 if index & 1 else 1) != epsilon:
                continue
            p_beta, q_beta = beta[index]
            delta = math.gcd(b_value, q_beta)
            b0 = b_value // delta
            q0 = q_beta // delta
            p_star = b0 * p_beta - epsilon * q0 * a_value
            final_content = math.gcd(abs(p_star), delta)
            equal, ledger = equal_part(b_value, q_beta, delta)
            if final_content > equal or equal % final_content:
                raise AssertionError((m_value, index, final_content, equal, ledger))
            candidates.append(
                {
                    "N": index,
                    "q_log_per_n": MOD.log_int(q_beta) / n_value,
                    "delta": str(delta),
                    "delta_log_per_n": MOD.log_int(delta) / n_value,
                    "equal_part": str(equal),
                    "equal_part_log_per_n": MOD.log_int(equal) / n_value,
                    "g": str(final_content),
                    "g_log_per_n": MOD.log_int(final_content) / n_value,
                    "c_delta_g_log_per_n": MOD.log_int(content * delta * final_content) / n_value,
                    "c_delta_equal_upper_log_per_n": MOD.log_int(content * delta * equal) / n_value,
                    "local_ledger": ledger,
                }
            )
        best_actual = max(candidates, key=lambda row: row["c_delta_g_log_per_n"])
        best_equal_upper = max(
            candidates, key=lambda row: row["c_delta_equal_upper_log_per_n"]
        )
        row = {
            "m": m_value,
            "target_N": target,
            "parity": "even" if epsilon == 1 else "odd",
            "candidate_count": len(candidates),
            "content_log_per_n": MOD.log_int(content) / n_value,
            "primitive_b_log_per_n": MOD.log_int(b_value) / n_value,
            "best_actual": best_actual,
            "best_equal_level_upper": best_equal_upper,
        }
        rows.append(row)
        print(
            m_value,
            target,
            f"actual={best_actual['c_delta_g_log_per_n']:.6f}",
            f"eq-upper={best_equal_upper['c_delta_equal_upper_log_per_n']:.6f}",
            flush=True,
        )

    payload = {
        "schema": "mixed-cubic-equal-valuation-saddle-window-v1",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "coordinate_source": {
            "filename": SYNC.name,
            "sha256": hashlib.sha256(SYNC.read_bytes()).hexdigest(),
        },
        "warning": "finite exact diagnostic only; no asymptotic claim",
        "parameters": vars(args)
        | {"output": args.output.name if args.output else None},
        "theorem_checked": "g divides the equal-positive-valuation part of gcd(b_m,q_N)",
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
