#!/usr/bin/env python3
"""Deterministic certificate for Item 199.

The theorem-facing part is exact integer algebra.  For the beta numerator and
denominator pair

    p_0=1, p_1=3, q_0=q_1=1,
    x_n=(4n-2)x_{n-1}+x_{n-2},

define the transfer continuant C_h(N) by

    C_0=0, C_1=1,
    C_{j+1}=(4N+4j+2)C_j+C_{j-1}.

Then

    p_N q_{N+h}-p_{N+h}q_N = 2(-1)^(N+1) C_h(N).

For an actual primitive mixed-cubic pair (a,b,epsilon), this script also
reconstructs the sequential factors Delta and g and checks

    gcd(Delta_N g_N, Delta_M g_M)
      = gcd(Delta_N,Delta_M) gcd(g_N,g_M)
      | C_{M-N}(N)

on a deterministic finite replay.  The report contains the all-index proof;
the replay is an exact regression certificate, not its evidentiary basis.
The h=2 specialization at two successive gaps also gives the all-index
three-term theorem gcd(T_N,T_(N+2),T_(N+4))=1 for T_N=Delta_N*g_N.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEFAULT_ARCHIVE = Path(__file__).resolve().parent.parent
INPUT_REL = Path("results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def beta_pairs(limit: int) -> tuple[list[int], list[int]]:
    p = [1, 3]
    q = [1, 1]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        p.append(coefficient * p[-1] + p[-2])
        q.append(coefficient * q[-1] + q[-2])
    return p[: limit + 1], q[: limit + 1]


def continuant(n: int, h: int) -> int:
    if h < 0:
        raise ValueError("h must be nonnegative")
    if h == 0:
        return 0
    previous, current = 0, 1
    for j in range(1, h):
        previous, current = current, (4 * n + 4 * j + 2) * current + previous
    return current


def matching_data(a: int, b: int, epsilon: int, pn: int, qn: int) -> dict[str, int]:
    delta = math.gcd(b, qn)
    b0 = b // delta
    q0 = qn // delta
    pstar = b0 * pn - epsilon * q0 * a
    g = math.gcd(abs(pstar), delta)
    return {
        "delta": delta,
        "g": g,
        "total": delta * g,
        "pstar": pstar,
        "b0": b0,
        "q0": q0,
    }


def update_maximum(current: dict[str, Any] | None, candidate: dict[str, Any]) -> dict[str, Any]:
    if current is None:
        return candidate
    left = int(candidate["common_total"])
    right = int(current["common_total"])
    if left > right:
        return candidate
    if left == right and (candidate["m"], candidate["N"], candidate["M"]) < (
        current["m"],
        current["N"],
        current["M"],
    ):
        return candidate
    return current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--m-limit", type=int, default=100)
    parser.add_argument("--full-pair-m-limit", type=int, default=30)
    parser.add_argument("--gap-max", type=int, default=20)
    parser.add_argument("--identity-n-limit", type=int, default=240)
    parser.add_argument("--identity-h-limit", type=int, default=60)
    args = parser.parse_args()

    input_path = args.archive / INPUT_REL
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = [row for row in payload["rows"] if int(row["m"]) <= args.m_limit]
    if not rows:
        raise RuntimeError("no input rows in selected scope")

    max_index = max(6 * int(row["m"]) for row in rows)
    identity_limit = args.identity_n_limit + args.identity_h_limit
    pseq, qseq = beta_pairs(max(max_index, identity_limit))

    identity_checks = 0
    transfer_checks = 0
    height_checks = 0
    for n in range(args.identity_n_limit + 1):
        for h in range(1, args.identity_h_limit + 1):
            c = continuant(n, h)
            determinant = pseq[n] * qseq[n + h] - pseq[n + h] * qseq[n]
            expected = 2 * (-1 if n % 2 == 0 else 1) * c
            if determinant != expected:
                raise AssertionError(("determinant", n, h))
            identity_checks += 1

            transfer_q = c * qseq[n + 1] + continuant(n + 1, h - 1) * qseq[n]
            transfer_p = c * pseq[n + 1] + continuant(n + 1, h - 1) * pseq[n]
            if transfer_q != qseq[n + h] or transfer_p != pseq[n + h]:
                raise AssertionError(("transfer", n, h))
            transfer_checks += 1

            ceiling = (4 * n + 4 * h - 1) ** (h - 1)
            if c > ceiling:
                raise AssertionError(("height", n, h, c, ceiling))
            height_checks += 1

    local_checks = 0
    diagonal_failures = 0
    pair_checks = 0
    decomposition_checks = 0
    divisibility_checks = 0
    determinant_divisibility_checks = 0
    positive_common_total_pairs = 0
    positive_common_g_pairs = 0
    consecutive_triple_checks = 0
    nontrivial_consecutive_triples = 0
    common_total_histogram: dict[str, int] = {}
    maximum_common: dict[str, Any] | None = None
    maximum_common_g: dict[str, Any] | None = None
    common_g_examples: list[dict[str, Any]] = []

    for row in rows:
        m = int(row["m"])
        a = int(row["primitive_positive_form"]["a"])
        b = int(row["primitive_positive_form"]["b"])
        epsilon = int(row["epsilon"])
        nmax = 6 * m
        valid = [n for n in range(1, nmax + 1) if (1 if n % 2 == 0 else -1) == epsilon]
        local: dict[int, dict[str, int]] = {}
        for n in valid:
            datum = matching_data(a, b, epsilon, pseq[n], qseq[n])
            if datum["g"] > 1 and math.gcd(datum["g"], datum["b0"] * datum["q0"]) != 1:
                diagonal_failures += 1
            if datum["g"] < 1 or datum["delta"] % datum["g"] != 0:
                raise AssertionError(("g-divides-delta", m, n))
            local[n] = datum
            local_checks += 1

        for i, n in enumerate(valid):
            if m <= args.full_pair_m_limit:
                partners = valid[i + 1 :]
            else:
                partners = [u for u in valid[i + 1 :] if u - n <= args.gap_max]
            for u in partners:
                h = u - n
                dn = local[n]
                du = local[u]
                common_total = math.gcd(dn["total"], du["total"])
                decomposed = math.gcd(dn["delta"], du["delta"]) * math.gcd(dn["g"], du["g"])
                if common_total != decomposed:
                    raise AssertionError(("decomposition", m, n, u))
                decomposition_checks += 1

                c = continuant(n, h)
                if c % common_total != 0:
                    raise AssertionError(("continuant-divisibility", m, n, u, common_total))
                divisibility_checks += 1

                determinant = abs(pseq[n] * qseq[u] - pseq[u] * qseq[n])
                if determinant != 2 * c or determinant % common_total != 0:
                    raise AssertionError(("determinant-divisibility", m, n, u))
                determinant_divisibility_checks += 1

                pair_checks += 1
                if common_total > 1:
                    positive_common_total_pairs += 1
                    key = str(common_total)
                    common_total_histogram[key] = common_total_histogram.get(key, 0) + 1
                common_g = math.gcd(dn["g"], du["g"])
                if common_g > 1:
                    positive_common_g_pairs += 1
                    common_g_row = {
                        "m": m,
                        "N": n,
                        "M": u,
                        "h": h,
                        "delta_N": str(dn["delta"]),
                        "g_N": str(dn["g"]),
                        "delta_M": str(du["delta"]),
                        "g_M": str(du["g"]),
                        "common_g": str(common_g),
                        "common_total": str(common_total),
                        "continuant_mod_common_total": c % common_total,
                    }
                    if len(common_g_examples) < 20:
                        common_g_examples.append(common_g_row)
                    if maximum_common_g is None or common_g > int(maximum_common_g["common_g"]):
                        maximum_common_g = common_g_row
                maximum_common = update_maximum(
                    maximum_common,
                    {
                        "m": m,
                        "N": n,
                        "M": u,
                        "h": h,
                        "delta_N": str(dn["delta"]),
                        "g_N": str(dn["g"]),
                        "delta_M": str(du["delta"]),
                        "g_M": str(du["g"]),
                        "common_g": str(common_g),
                        "common_total": str(common_total),
                        "continuant_digits": len(str(c)),
                    },
                )

        valid_set = set(valid)
        for n in valid:
            if n + 2 not in valid_set or n + 4 not in valid_set:
                continue
            triple_common = math.gcd(local[n]["total"], local[n + 2]["total"])
            triple_common = math.gcd(triple_common, local[n + 4]["total"])
            if triple_common != 1:
                nontrivial_consecutive_triples += 1
                raise AssertionError(("consecutive-triple", m, n, triple_common))
            consecutive_triple_checks += 1

    if diagonal_failures:
        raise AssertionError(("valuation-diagonal", diagonal_failures))

    top_common_values = sorted(
        ((int(value), count) for value, count in common_total_histogram.items()),
        key=lambda item: (-item[1], item[0]),
    )[:20]

    result: dict[str, Any] = {
        "schema": "item199_matching_gain_certificate_v1",
        "theorem_boundary": {
            "proved_by_report": [
                "beta two-index transfer determinant identity for all N>=0 and h>=1",
                "exact primewise valuation-diagonal decomposition of the common sequential factor",
                "gcd(Delta_N*g_N,Delta_M*g_M) divides C_(M-N)(N)",
                "using N*log(N)/(6m)->theta=d/2, sublinear h=o(N) gives common rate at most (theta+o(1))*h/N=o(1)",
                "three consecutive parity-compatible indices N,N+2,N+4 have common sequential factor exactly 1",
            ],
            "not_proved": [
                "an upper bound for a single-index Delta_N*g_N",
                "a no-go for shifts comparable with N",
                "a bound on matching factors that occur at only one index",
                "irrationality or rationality of e+pi",
            ],
            "saddle_normalization_audit": {
                "relation": "N*log(N)/(6m) -> theta=d/2",
                "theta_decimal": "1.168531187179486497926964890273",
                "continuant_log_ceiling": "(h-1)*log(4*N+4*h-1)",
                "normalized_ceiling_for_h_o_N": "(theta+o(1))*h/N",
                "residual_gap_decimal": "0.019632983669431793880306401240",
                "necessary_h_over_N_for_residual_capacity": "0.0168014203513219247791020171289",
            },
        },
        "input": {
            "relative_path": INPUT_REL.as_posix(),
            "sha256": sha256_file(input_path),
            "rows_used": len(rows),
            "m_limit": args.m_limit,
        },
        "portability_contract": {
            "default_archive_resolution": "parent of the script directory",
            "embedded_host_absolute_paths": False,
            "embedded_timestamps": False,
            "embedded_python_or_platform_version": False,
            "runtime_sensitive_floating_fields": False,
            "manifest_paths": "archive-relative",
        },
        "symbolic_integer_replay": {
            "N_limit": args.identity_n_limit,
            "h_limit": args.identity_h_limit,
            "determinant_identity_checks": identity_checks,
            "transfer_identity_checks": transfer_checks,
            "continuant_height_checks": height_checks,
            "failures": 0,
        },
        "actual_mixed_cubic_replay": {
            "scope": {
                "N_range": "1 <= N <= 6m with (-1)^N=epsilon_m",
                "all_pairs_for_m_at_most": args.full_pair_m_limit,
                "maximum_even_gap_for_larger_m": args.gap_max,
            },
            "local_matching_checks": local_checks,
            "valuation_diagonal_failures": diagonal_failures,
            "pair_checks": pair_checks,
            "decomposition_checks": decomposition_checks,
            "continuant_divisibility_checks": divisibility_checks,
            "determinant_divisibility_checks": determinant_divisibility_checks,
            "failures": 0,
            "pairs_with_common_total_above_one": positive_common_total_pairs,
            "pairs_with_common_g_above_one": positive_common_g_pairs,
            "consecutive_parity_triple_checks": consecutive_triple_checks,
            "nontrivial_consecutive_parity_triples": nontrivial_consecutive_triples,
            "maximum_common_total_row": maximum_common,
            "maximum_common_g_row": maximum_common_g,
            "first_common_g_examples": common_g_examples,
            "most_frequent_positive_common_totals": [
                {"value": str(value), "count": count} for value, count in top_common_values
            ],
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "pair_checks": pair_checks,
        "positive_common_total_pairs": positive_common_total_pairs,
        "positive_common_g_pairs": positive_common_g_pairs,
        "maximum_common_total": maximum_common["common_total"] if maximum_common else None,
        "sha256": sha256_file(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
