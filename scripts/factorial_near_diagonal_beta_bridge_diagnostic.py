#!/usr/bin/env python3
"""Exact diagnostics for the factorial near-diagonal / beta bridge.

This script uses the archive's certified rational Machin interval only to
construct factorial floors of pi.  All bridge, recurrence, content, and
primitive-pair checks are integer exact.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path


sys.set_int_max_str_digits(0)


def sha256_integer(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def compact_integer(value: int) -> dict:
    return {
        "decimal_digits": len(str(abs(value))),
        "sha256": sha256_integer(value),
    }


def load_probe(path: Path):
    spec = importlib.util.spec_from_file_location("varying_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def forward_difference(values: list[int], start: int, order: int) -> int:
    return sum(
        (-1 if (order-r) & 1 else 1)
        * math.comb(order, r)
        * values[start+r]
        for r in range(order+1)
    )


def beta_pairs(maximum: int) -> tuple[list[int], list[int]]:
    q = [1, 1]
    p = [1, 3]
    for n in range(2, maximum+1):
        multiplier = 4*n-2
        q.append(multiplier*q[-1]+q[-2])
        p.append(multiplier*p[-1]+p[-2])
    return p[:maximum+1], q[:maximum+1]


def direct_diagonal_d(n: int) -> int:
    return sum(
        (-1 if k & 1 else 1)
        * math.factorial(2*n-k)
        // (math.factorial(k)*math.factorial(n-k))
        for k in range(n+1)
    )


def local_weights(a: int, b: int) -> list[int]:
    """Return E_{a,b,1},...,E_{a,b,b} by its exact reverse recurrence."""
    weights = [0]*(b+1)
    weights[b] = 1
    for j in range(b-1, 0, -1):
        weights[j] = (
            (a+j+1)*weights[j+1]
            + (-1 if (b-j) & 1 else 1)*math.comb(b, j)
        )
    return weights[1:]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=265)
    parser.add_argument("--atan5-last-index", type=int, default=950)
    parser.add_argument("--atan239-last-index", type=int, default=300)
    parser.add_argument(
        "--archive",
        type=Path,
        default=None,
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
    )
    parser.add_argument("--source", type=Path, default=None)
    args = parser.parse_args()
    if args.max_n < 2:
        raise ValueError("max-n must be at least two")

    if args.archive is None:
        archive = Path(__file__).resolve().parents[1]
        expected = archive / "scripts" / "factorial_digit_entire_varying_b_probe.py"
        if not expected.is_file():
            raise ValueError(
                "cannot infer archive root; pass --archive explicitly"
            )
    else:
        archive = args.archive.resolve()
    probe_path = archive / "scripts" / "factorial_digit_entire_varying_b_probe.py"
    source_path = (
        args.source.resolve()
        if args.source is not None
        else archive / "sources" / "factorial_near_diagonal_beta_bridge.md"
    )
    output_path = (
        args.output.resolve()
        if args.output is not None
        else archive / "results" / "factorial_near_diagonal_beta_bridge_m265.json"
    )
    if not source_path.is_file():
        raise ValueError(f"source note not found: {source_path}")
    probe = load_probe(probe_path)
    pi_box = probe.pi_interval(args.atan5_last_index, args.atan239_last_index)
    factorials, pi_digits, combined, pi_floors = probe.build_canonical_data(
        2*args.max_n, pi_box
    )
    e_floors = [combined[n]-pi_floors[n] for n in range(2*args.max_n+1)]
    p, q = beta_pairs(args.max_n+1)

    primitive_seen: dict[tuple[int, int], list[int]] = {}
    selected_indices = set(range(1, min(args.max_n, 12)+1))
    selected_indices.update(
        n for n in (16, 24, 32, 50, 75, 100, 125, 150, 200, 250, args.max_n)
        if n <= args.max_n
    )
    selected: list[dict] = []
    t_sign_counts = {"negative": 0, "zero": 0, "positive": 0}
    positive_t_indices: list[int] = []
    full_local_cancellations: list[int] = []
    nontrivial_g_indices: list[int] = []
    maximum_log_g_over_log_q: tuple[Decimal, int | None] = (Decimal(-1), None)
    minimum_q_over_g: tuple[int, int] | None = None
    minimum_q_over_g_n_ge_2: tuple[int, int] | None = None

    for n in range(1, args.max_n+1):
        nfac = factorials[n]
        d_direct = direct_diagonal_d(n)
        if d_direct != q[n]:
            raise AssertionError("D_{n,n}=q_n failed")
        if n >= 2:
            if q[n] != (4*n-2)*q[n-1]+q[n-2]:
                raise AssertionError("beta recurrence failed")
        elif q[n] != 1:
            raise AssertionError("beta initial value failed")
        if q[n] % 2 != 1 or math.gcd(p[n], q[n]) != 1:
            raise AssertionError("beta parity/primitivity failed")

        w = forward_difference(factorials, n, n)
        z_e = forward_difference(e_floors, n, n)
        r_pi = forward_difference(pi_floors, n, n)
        z = forward_difference(combined, n, n)
        if w != nfac*q[n]:
            raise AssertionError("W_{n,n}=n!q_n failed")
        if z_e != nfac*p[n]:
            raise AssertionError("e numerator bridge failed")
        if z != z_e+r_pi:
            raise AssertionError("e/pi split failed")

        k_local = z-q[n]*combined[n]
        t_centered = k_local-q[n]
        if z != q[n]*(combined[n]+1)+t_centered:
            raise AssertionError("centered truncation decomposition failed")
        weights = local_weights(n, n)
        local_digits = [pi_digits[n+j]+1 for j in range(1, n+1)]
        if any(weight <= 0 for weight in weights):
            raise AssertionError("nonpositive local weight")
        if sum((n+j-1)*weights[j-1] for j in range(1, n+1)) != q[n]:
            raise AssertionError("centered weight identity failed")
        if sum(weight*digit for weight, digit in zip(weights, local_digits)) != k_local:
            raise AssertionError("local digit expansion failed")
        if sum(
            weight*(digit-(n+j-1))
            for j, (weight, digit) in enumerate(zip(weights, local_digits), 1)
        ) != t_centered:
            raise AssertionError("centered local digit residual failed")

        g = math.gcd(q[n], k_local)
        matched_constant = nfac*p[n]+r_pi
        if g != math.gcd(q[n], t_centered):
            raise AssertionError("centered local gcd failed")
        if g != math.gcd(q[n], matched_constant):
            raise AssertionError("matched beta/pi content failed")
        numerator_free_constant = (
            q[n-1]*r_pi + 2*(-1 if (n+1) & 1 else 1)*nfac
        )
        if g != math.gcd(q[n], numerator_free_constant):
            raise AssertionError("numerator-free beta Wronskian gcd failed")

        d_bar = q[n]//g
        z_bar = z//g
        j = math.gcd(nfac, z_bar)
        h = g*j
        if h != math.gcd(w, z):
            raise AssertionError("full endpoint content failed")
        primitive_p = z//h
        primitive_q = w//h
        if math.gcd(primitive_p, primitive_q) != 1:
            raise AssertionError("primitive pair failed")
        if primitive_q != d_bar*(nfac//j):
            raise AssertionError("primitive denominator split failed")
        if math.gcd(d_bar, j) != 1:
            raise AssertionError("residual factorial divisor is not coprime to D-bar")

        primitive_seen.setdefault((primitive_p, primitive_q), []).append(n)
        if t_centered < 0:
            t_sign_counts["negative"] += 1
        elif t_centered > 0:
            t_sign_counts["positive"] += 1
            positive_t_indices.append(n)
        else:
            t_sign_counts["zero"] += 1
            full_local_cancellations.append(n)
            if z*nfac != w*(combined[n]+1):
                raise AssertionError("collapse identity failed")

        if g > 1:
            nontrivial_g_indices.append(n)

        ratio = q[n]//g
        if minimum_q_over_g is None or ratio < minimum_q_over_g[0]:
            minimum_q_over_g = (ratio, n)
        if n >= 2 and (
            minimum_q_over_g_n_ge_2 is None
            or ratio < minimum_q_over_g_n_ge_2[0]
        ):
            minimum_q_over_g_n_ge_2 = (ratio, n)
        # Decimal logarithms make the archived JSON byte-reproducible rather
        # than depending on the platform libm's last binary digit.
        with localcontext() as context:
            context.prec = 80
            theta = (
                Decimal(g).ln()/Decimal(q[n]).ln()
                if g > 1
                else Decimal(0)
            )
        if theta > maximum_log_g_over_log_q[0]:
            maximum_log_g_over_log_q = (theta, n)

        if n in selected_indices:
            selected.append(
                {
                    "n": n,
                    "q": compact_integer(q[n]),
                    "p": compact_integer(p[n]),
                    "r_pi": compact_integer(r_pi),
                    "centered_residual_T": compact_integer(t_centered),
                    "T_sign": -1 if t_centered < 0 else (1 if t_centered > 0 else 0),
                    "g": g,
                    "J": compact_integer(j),
                    "Q": compact_integer(primitive_q),
                    "q_over_g": compact_integer(ratio),
                }
            )

    for n in range(args.max_n):
        wronskian = p[n]*q[n+1]-p[n+1]*q[n]
        if wronskian != 2*(-1 if n % 2 == 0 else 1):
            raise AssertionError("beta Wronskian failed")

    duplicate_groups = [
        {"indices": indices, "P": compact_integer(pair[0]), "Q": compact_integer(pair[1])}
        for pair, indices in primitive_seen.items()
        if len(indices) > 1
    ]
    result = {
        "status": "finite exact diagnostic; not an irrationality proof",
        "max_n": args.max_n,
        "source": "sources/factorial_near_diagonal_beta_bridge.md",
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "script": "scripts/factorial_near_diagonal_beta_bridge_diagnostic.py",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "archive_probe": "scripts/factorial_digit_entire_varying_b_probe.py",
        "archive_probe_sha256": hashlib.sha256(probe_path.read_bytes()).hexdigest(),
        "replay_parameters": {
            "max_n": args.max_n,
            "atan5_last_index": args.atan5_last_index,
            "atan239_last_index": args.atan239_last_index,
        },
        "checks": {
            "D_n_n_equals_beta_q_n": True,
            "W_n_n_equals_n_factorial_q_n": True,
            "delta_n_floor_factorial_e_equals_n_factorial_p_n": True,
            "Z_total_equals_n_factorial_p_n_plus_R_pi": True,
            "centered_weight_and_digit_residual_identities": True,
            "local_g_equals_gcd_q_T_equals_gcd_q_matched_constant": True,
            "numerator_free_beta_wronskian_gcd": True,
            "full_content_and_denominator_split": True,
            "beta_wronskian": True,
        },
        "actual_pi_diagonal_summary": {
            "T_sign_counts": t_sign_counts,
            "positive_T_indices": positive_t_indices,
            "full_local_cancellation_indices": full_local_cancellations,
            "nontrivial_g_count": len(nontrivial_g_indices),
            "nontrivial_g_indices": nontrivial_g_indices,
            "primitive_duplicate_groups": duplicate_groups,
            "minimum_q_over_g": {
                "value": compact_integer(minimum_q_over_g[0]),
                "n": minimum_q_over_g[1],
            },
            "minimum_q_over_g_n_ge_2": {
                "value": compact_integer(minimum_q_over_g_n_ge_2[0]),
                "n": minimum_q_over_g_n_ge_2[1],
            },
            "maximum_log_g_over_log_q": {
                "value": format(maximum_log_g_over_log_q[0], ".50g"),
                "n": maximum_log_g_over_log_q[1],
            },
        },
        "selected_records": selected,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes((json.dumps(result, indent=2, sort_keys=True)+"\n").encode())
    print(json.dumps(result["actual_pi_diagonal_summary"], indent=2, sort_keys=True))
    print(f"output_sha256={hashlib.sha256(output_path.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

