#!/usr/bin/env python3
"""Deterministic certificate for Item 201.

This companion checks exact integer identities used in the comparable-gap
analysis of the beta transfer continuant.  The all-index asymptotic and the
portfolio deductions are proved in the report; finite loops here are
regression checks and are never promoted to asymptotic evidence.

The installed archive layout is

    scripts/item201_comparable_gap_certificate.py
    sources/item199_matching_gain_report.md
    scripts/item199_matching_gain_certificate.py
    results/mixed_cubic_positive_match_exact_scan_m100_N6m.json

For staging, the three inputs may be supplied explicitly.  Their serialized
names remain archive-relative, so canonical and installed replays are byte
stable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any


DEFAULT_ARCHIVE = Path(__file__).resolve().parent.parent
INPUT_REL = Path("results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")
UPSTREAM_REPORT_REL = Path("sources/item199_matching_gain_report.md")
UPSTREAM_CHECKER_REL = Path("scripts/item199_matching_gain_certificate.py")

THETA_DECIMAL = "1.168531187179486497926964890273"
RESIDUAL_GAP_DECIMAL = "0.019632983669431793880306401240"
ALPHA_CRITICAL_DECIMAL = "0.0168014203513219247791020171289"
ALPHA_CRITICAL_NUMERATOR = 168014203513219247791020171289
ALPHA_CRITICAL_DENOMINATOR = 10**31


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


@lru_cache(maxsize=None)
def continuant(n: int, h: int) -> int:
    if h < 0:
        raise ValueError("h must be nonnegative")
    if h == 0:
        return 0
    previous, current = 0, 1
    for j in range(1, h):
        previous, current = current, (4 * n + 4 * j + 2) * current + previous
    return current


@lru_cache(maxsize=None)
def spine_product(n: int, h: int) -> int:
    product = 1
    for j in range(1, h):
        product *= 4 * n + 4 * j + 2
    return product


def matching_edge_sum(n: int, h: int) -> Fraction:
    """Sum 1/(a_j*a_(j+1)) over the path edges, in closed form."""
    if h <= 2:
        return Fraction(0, 1)
    return Fraction(1, 8) * (
        Fraction(1, 2 * n + 3) - Fraction(1, 2 * n + 2 * h - 1)
    )


def odd_part(value: int) -> int:
    if value <= 0:
        raise ValueError("odd_part expects a positive integer")
    while value % 2 == 0:
        value //= 2
    return value


def matching_data(a: int, b: int, epsilon: int, pn: int, qn: int) -> dict[str, int]:
    delta = math.gcd(b, qn)
    b0 = b // delta
    q0 = qn // delta
    pstar = b0 * pn - epsilon * q0 * a
    g = math.gcd(abs(pstar), delta)
    total = delta * g
    if b * b % total != 0 or qn * qn % total != 0:
        raise AssertionError(("local-square-capacity", delta, g))
    return {"delta": delta, "g": g, "total": total}


def update_maximum(
    current: dict[str, Any] | None,
    value: int,
    row: dict[str, Any],
) -> dict[str, Any]:
    candidate = dict(row)
    candidate["value"] = str(value)
    if current is None:
        return candidate
    current_value = int(current["value"])
    candidate_key = (int(candidate["m"]), int(candidate["N"]), int(candidate["M"]))
    current_key = (int(current["m"]), int(current["N"]), int(current["M"]))
    if value > current_value or (value == current_value and candidate_key < current_key):
        return candidate
    return current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--input-file", type=Path)
    parser.add_argument("--upstream-report", type=Path)
    parser.add_argument("--upstream-checker", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--symbolic-n-limit", type=int, default=160)
    parser.add_argument("--symbolic-h-factor", type=int, default=2)
    parser.add_argument("--triple-n-limit", type=int, default=60)
    parser.add_argument("--triple-gap-limit", type=int, default=24)
    parser.add_argument("--nearest-n-limit", type=int, default=1000)
    parser.add_argument("--m-limit", type=int, default=100)
    args = parser.parse_args()

    input_path = args.input_file or (args.archive / INPUT_REL)
    upstream_report = args.upstream_report or (args.archive / UPSTREAM_REPORT_REL)
    upstream_checker = args.upstream_checker or (args.archive / UPSTREAM_CHECKER_REL)
    for required in (input_path, upstream_report, upstream_checker):
        if not required.is_file():
            raise FileNotFoundError(required)

    maximum_symbolic_index = args.symbolic_n_limit * (1 + args.symbolic_h_factor)
    p_symbolic, q_symbolic = beta_pairs(maximum_symbolic_index)

    product_checks = 0
    correction_checks = 0
    determinant_checks = 0
    displacement_checks = 0
    for n in range(1, args.symbolic_n_limit + 1):
        for h in range(1, args.symbolic_h_factor * n + 1):
            c = continuant(n, h)
            product = spine_product(n, h)
            if c < product:
                raise AssertionError(("spine-lower-bound", n, h))
            product_checks += 1

            edge_sum = matching_edge_sum(n, h)
            correction = Fraction(c - product, product)
            if correction < edge_sum:
                raise AssertionError(("first-correction-lower", n, h))
            if edge_sum < 1:
                upper = edge_sum + edge_sum * edge_sum / (1 - edge_sum)
                if correction > upper:
                    raise AssertionError(("matching-expansion-upper", n, h))
            correction_checks += 1

            determinant = p_symbolic[n] * q_symbolic[n + h] - p_symbolic[n + h] * q_symbolic[n]
            expected = 2 * (-1 if n % 2 == 0 else 1) * c
            if determinant != expected:
                raise AssertionError(("transfer-determinant", n, h))
            determinant_checks += 1

            tail = continuant(n + 1, h - 1)
            transfer = c * q_symbolic[n + 1] + tail * q_symbolic[n]
            if transfer != q_symbolic[n + h]:
                raise AssertionError(("q-transfer", n, h))
            if h >= 2:
                if not (0 < tail < c):
                    raise AssertionError(("tail-capacity", n, h))
                if not (
                    c * q_symbolic[n + 1]
                    < q_symbolic[n + h]
                    < c * (q_symbolic[n + 1] + q_symbolic[n])
                ):
                    raise AssertionError(("displacement-sandwich", n, h))
            displacement_checks += 1

    triple_gcd_checks = 0
    for n in range(1, args.triple_n_limit + 1):
        for r in range(1, args.triple_gap_limit + 1):
            for s in range(1, args.triple_gap_limit + 1):
                a_edge = odd_part(continuant(n, r))
                outer_edge = odd_part(continuant(n, r + s))
                c_edge = odd_part(continuant(n + r, s))
                triple_gcd = math.gcd(a_edge, math.gcd(outer_edge, c_edge))
                pair_gcds = {
                    math.gcd(a_edge, outer_edge),
                    math.gcd(a_edge, c_edge),
                    math.gcd(outer_edge, c_edge),
                }
                if pair_gcds != {triple_gcd}:
                    raise AssertionError(("odd-transfer-clique", n, r, s))
                if math.lcm(a_edge, outer_edge, c_edge) != (
                    a_edge * outer_edge * c_edge // (triple_gcd * triple_gcd)
                ):
                    raise AssertionError(("three-edge-lcm", n, r, s))
                triple_gcd_checks += 1

    nearest_formula_checks = 0
    for n in range(1, args.nearest_n_limit + 1):
        left = 2 * n + 3
        right = 2 * n + 7
        outer = (2 * n + 5) * (8 * n * n + 40 * n + 43)
        if continuant(n, 2) != 2 * left:
            raise AssertionError(("nearest-left", n))
        if continuant(n + 2, 2) != 2 * right:
            raise AssertionError(("nearest-right", n))
        if continuant(n, 4) != 4 * outer:
            raise AssertionError(("nearest-outer", n))
        if not (
            math.gcd(left, right) == 1
            and math.gcd(left, outer) == 1
            and math.gcd(right, outer) == 1
        ):
            raise AssertionError(("nearest-capacity-coprimality", n))
        nearest_formula_checks += 1

    example_n, example_r, example_s = 20, 10, 10
    example_edges = [
        odd_part(continuant(example_n, example_r)),
        odd_part(continuant(example_n, example_r + example_s)),
        odd_part(continuant(example_n + example_r, example_s)),
    ]
    example_common = math.gcd(example_edges[0], math.gcd(example_edges[1], example_edges[2]))
    if example_common != 355:
        raise AssertionError(("comparable-transfer-example", example_common))

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    rows = [row for row in payload["rows"] if int(row["m"]) <= args.m_limit]
    if not rows:
        raise RuntimeError("no actual mixed-cubic rows in selected scope")
    max_index = max(6 * int(row["m"]) for row in rows)
    p_actual, q_actual = beta_pairs(max_index)

    actual_local_checks = 0
    actual_pair_checks = 0
    positive_common_total_pairs = 0
    positive_common_g_pairs = 0
    near_critical_pairs = 0
    near_critical_positive_total_pairs = 0
    near_critical_positive_g_pairs = 0
    maximum_common_total: dict[str, Any] | None = None
    maximum_common_g: dict[str, Any] | None = None
    near_critical_maximum: dict[str, Any] | None = None
    local_by_m: dict[int, dict[int, dict[str, int]]] = {}

    for row in rows:
        m = int(row["m"])
        a = int(row["primitive_positive_form"]["a"])
        b = int(row["primitive_positive_form"]["b"])
        epsilon = int(row["epsilon"])
        valid = [
            n
            for n in range(1, 6 * m + 1)
            if (1 if n % 2 == 0 else -1) == epsilon
        ]
        local: dict[int, dict[str, int]] = {}
        for n in valid:
            datum = matching_data(a, b, epsilon, p_actual[n], q_actual[n])
            if datum["g"] < 1 or datum["delta"] % datum["g"] != 0:
                raise AssertionError(("g-divides-delta", m, n))
            local[n] = datum
            actual_local_checks += 1
        local_by_m[m] = local

        for position, n in enumerate(valid):
            for other in valid[position + 1 :]:
                datum_n = local[n]
                datum_other = local[other]
                common_total = math.gcd(datum_n["total"], datum_other["total"])
                common_g = math.gcd(datum_n["g"], datum_other["g"])
                actual_pair_checks += 1
                row_key = {
                    "m": m,
                    "N": n,
                    "M": other,
                    "h": other - n,
                    "delta_N": str(datum_n["delta"]),
                    "g_N": str(datum_n["g"]),
                    "delta_M": str(datum_other["delta"]),
                    "g_M": str(datum_other["g"]),
                }
                if common_total > 1:
                    positive_common_total_pairs += 1
                    maximum_common_total = update_maximum(
                        maximum_common_total, common_total, row_key
                    )
                if common_g > 1:
                    positive_common_g_pairs += 1
                    maximum_common_g = update_maximum(maximum_common_g, common_g, row_key)

                gap = other - n
                above_critical = (
                    gap * ALPHA_CRITICAL_DENOMINATOR
                    >= n * ALPHA_CRITICAL_NUMERATOR
                )
                below_one_fiftieth = 50 * gap < n
                if above_critical and below_one_fiftieth:
                    near_critical_pairs += 1
                    if common_total > 1:
                        near_critical_positive_total_pairs += 1
                        near_critical_maximum = update_maximum(
                            near_critical_maximum, common_total, row_key
                        )
                    if common_g > 1:
                        near_critical_positive_g_pairs += 1

    row4 = local_by_m[4]
    triple_counterexample = math.gcd(
        row4[2]["total"], math.gcd(row4[4]["total"], row4[16]["total"])
    )
    if triple_counterexample != 7:
        raise AssertionError(("nonconsecutive-triple-counterexample", triple_counterexample))

    row40 = local_by_m[40]
    synchronized_pair = math.gcd(row40[40]["total"], row40[132]["total"])
    if synchronized_pair != 39601:
        raise AssertionError(("finite-synchronized-pair", synchronized_pair))

    row99 = local_by_m[99]
    seven_support = sorted(n for n, datum in row99.items() if datum["total"] % 7 == 0)
    for n in seven_support:
        if n + 2 in row99 and n + 4 in row99:
            if all(row99[u]["total"] % 7 == 0 for u in (n, n + 2, n + 4)):
                raise AssertionError(("nearest-triple-seven", n))

    result: dict[str, Any] = {
        "schema": "item201_comparable_gap_certificate_v1",
        "theorem_boundary": {
            "proved_by_report": [
                "uniform sharp product asymptotic C_h(N)=4^(h-1)*Gamma(N+h+1/2)/Gamma(N+3/2)*(1+O_A(1/N)) for h<=A*N",
                "for h/N->alpha and N*log(N)/(6m)->theta, log(C_h(N))/(6m)->theta*alpha",
                "a common sequential block has rate below the residual gap whenever alpha<G/theta",
                "the beta-height displacement strictly exceeds log(C_h(N)) and has the same theta*alpha leading rate",
                "for pure pair recycling the normalized net is below -log(4*N+2)/(6*m)<0, an exact polynomial deficit",
                "odd pairwise gcds among the three transfer continuants of any index triple all equal their triple gcd",
                "under global triple-gcd-one, aggregate reuse is edge-prime-disjoint, divides the lcm of edge continuants, and cannot exceed the unique CRT modulus",
                "a forest reuse portfolio cannot beat its aggregate beta-index displacement",
            ],
            "finite_not_inference": [
                "all exact loop counts and actual-row examples below",
                "the absence of final matching in the near-critical finite bin",
                "the size of common transfer gcds in sampled triples",
            ],
            "open": [
                "an asymptotic upper bound for gcd(q_N,q_(N+h)) or the common odd gcd of comparable-gap transfer continuants",
                "multi-parent packing in which one later index reuses pair-specific primes with two or more earlier indices",
                "a positive-rate lower bound for a single-index or comparable-gap actual matching factor",
                "prime supports occurring at only one selected index",
                "any conclusion about irrationality, rationality, or transcendence of e+pi",
            ],
            "frozen_saddle": {
                "relation": "N*log(N)/(6m) -> theta",
                "theta_decimal": THETA_DECIMAL,
                "residual_gap_decimal": RESIDUAL_GAP_DECIMAL,
                "critical_alpha_decimal": ALPHA_CRITICAL_DECIMAL,
                "sharp_rate_formula": "theta_N*(t+(t*log(4)+(1+t)*log(1+t)-t)/log(N)-log(4*N)/(N*log(N))+O_A(1/(N^2*log(N))))",
                "limiting_rate": "theta*alpha",
                "frozen_model_critical_shift_coefficient": "0.02343207425662527824161143175394746984/log(N)",
            },
        },
        "inputs": {
            "actual_rows": {
                "relative_path": INPUT_REL.as_posix(),
                "sha256": sha256_file(input_path),
                "rows_used": len(rows),
            },
            "upstream_report": {
                "relative_path": UPSTREAM_REPORT_REL.as_posix(),
                "sha256": sha256_file(upstream_report),
            },
            "upstream_checker": {
                "relative_path": UPSTREAM_CHECKER_REL.as_posix(),
                "sha256": sha256_file(upstream_checker),
            },
        },
        "portability_contract": {
            "default_archive_resolution": "parent of the script directory",
            "explicit_staging_inputs_supported": True,
            "serialized_input_paths": "archive-relative",
            "embedded_host_absolute_paths": False,
            "embedded_timestamps": False,
            "embedded_python_or_platform_version": False,
            "runtime_sensitive_floating_fields": False,
            "manifest_paths": "archive-relative",
        },
        "exact_symbolic_replay": {
            "scope": {
                "N_range": f"1 <= N <= {args.symbolic_n_limit}",
                "h_range": f"1 <= h <= {args.symbolic_h_factor}*N",
            },
            "spine_product_checks": product_checks,
            "matching_correction_checks": correction_checks,
            "transfer_determinant_checks": determinant_checks,
            "beta_displacement_sandwich_checks": displacement_checks,
            "odd_transfer_triple_gcd_checks": triple_gcd_checks,
            "nearest_triple_formula_and_coprimality_checks": nearest_formula_checks,
            "failures": 0,
            "comparable_transfer_example": {
                "N": example_n,
                "first_gap": example_r,
                "second_gap": example_s,
                "odd_edge_continuants": [str(value) for value in example_edges],
                "common_pairwise_gcd": str(example_common),
                "lcm": str(math.lcm(*example_edges)),
                "lcm_identity": "lcm(A,B,C)=A*B*C/H^2",
            },
        },
        "actual_mixed_cubic_finite_replay": {
            "scope": "all parity-compatible indices and all pairs for 1<=m<=100",
            "local_checks": actual_local_checks,
            "pair_checks": actual_pair_checks,
            "pairs_with_common_total_above_one": positive_common_total_pairs,
            "pairs_with_common_g_above_one": positive_common_g_pairs,
            "maximum_common_total_row": maximum_common_total,
            "maximum_common_g_row": maximum_common_g,
            "near_critical_bin": {
                "lower_h_over_N_inclusive": ALPHA_CRITICAL_DECIMAL,
                "upper_h_over_N_exclusive": "0.02",
                "pair_checks": near_critical_pairs,
                "pairs_with_common_total_above_one": near_critical_positive_total_pairs,
                "pairs_with_common_g_above_one": near_critical_positive_g_pairs,
                "maximum_common_total_row": near_critical_maximum,
            },
            "nonconsecutive_triple_counterexample": {
                "m": 4,
                "indices": [2, 4, 16],
                "common_total": str(triple_counterexample),
                "totals": [str(row4[n]["total"]) for n in (2, 4, 16)],
            },
            "finite_synchronized_pair": {
                "m": 40,
                "N": 40,
                "M": 132,
                "h_over_N": "23/10",
                "common_total": str(synchronized_pair),
                "N_data": {key: str(value) for key, value in row40[40].items()},
                "M_data": {key: str(value) for key, value in row40[132].items()},
            },
            "row_99_prime_7_support": {
                "support_size": len(seven_support),
                "first_indices": seven_support[:12],
                "last_indices": seven_support[-12:],
                "nearest_consecutive_parity_triples": 0,
            },
            "failures": 0,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "symbolic_checks": product_checks + triple_gcd_checks + nearest_formula_checks,
                "actual_pair_checks": actual_pair_checks,
                "sha256": sha256_file(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
