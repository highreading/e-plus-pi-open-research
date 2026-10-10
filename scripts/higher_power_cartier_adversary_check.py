#!/usr/bin/env python3
"""Exact replay of the examples in higher_power_cartier_adversary.md.

This is deliberately read-only with respect to the frozen Desktop archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vp(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("zero coordinate")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def row_at(rows: list[dict[str, object]], m_value: int) -> dict[str, object]:
    return next(row for row in rows if int(row["m"]) == m_value)


def beta_pair(index: int) -> tuple[int, int]:
    p_values = [1, 3]
    q_values = [1, 1]
    for n_value in range(2, index + 1):
        p_values.append((4 * n_value - 2) * p_values[-1] + p_values[-2])
        q_values.append((4 * n_value - 2) * q_values[-1] + q_values[-2])
    return p_values[index], q_values[index]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    args = parser.parse_args()
    result_dir = args.archive / "results"

    scan_path = result_dir / "mixed_cubic_positive_match_exact_scan_m100_N6m.json"
    rank1_path = result_dir / "mixed_cubic_small_prime_rank_one_cartier_certificate.json"
    rank2_path = result_dir / "mixed_cubic_rank_two_cartier_certificate.json"
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    rank1 = json.loads(rank1_path.read_text(encoding="utf-8"))
    rank2 = json.loads(rank2_path.read_text(encoding="utf-8"))

    # Rank-one prime-power-layer counterexample: p^2 is the top layer, but
    # the post-G content contains only one copy of p.
    scan3 = row_at(scan["rows"], 3)
    cert3 = row_at(rank1["rows"], 3)
    forced3 = next(row for row in cert3["forced_primes"] if row["p"] == 3)
    val3 = next(
        row for row in cert3["sharp_normalized_valuation_checks"] if row["p"] == 3
    )
    assert forced3["top_prime_power_layer"] == 9
    assert forced3["denominator_exponent"] == 2
    assert (val3["vp_u"], val3["vp_v"]) == (1, 3)
    assert vp(int(scan3["extra_content"]), 3) == 1

    # A first-Cartier rank-zero prime loses one digit to G_m; the surviving
    # post-G content again has exactly one p digit.
    scan9 = row_at(scan["rows"], 9)
    cert9 = row_at(rank1["rows"], 9)
    forced9 = next(row for row in cert9["forced_primes"] if row["p"] == 13)
    val9 = next(
        row for row in cert9["sharp_normalized_valuation_checks"] if row["p"] == 13
    )
    assert forced9["rank_zero_certified"] is True
    assert (val9["vp_u"], val9["vp_v"]) == (1, 2)
    g9 = int(scan9["cartier_product"]["value"])
    assert vp(g9, 13) == 1
    assert vp(int(scan9["U"]["value"]) * g9, 13) == 2
    assert vp(int(scan9["V"]["value"]) * g9, 13) == 3
    assert vp(int(scan9["extra_content"]), 13) == 1

    # Rank-two determinant zero, again with only one surviving content digit.
    scan4 = row_at(scan["rows"], 4)
    cert4 = row_at(rank2["index_rows"], 4)
    rank2_47 = next(row for row in cert4["vanishing_rank_two_rows"] if row["p"] == 7)
    assert rank2_47["determinant"] == 0
    assert (rank2_47["vp_u"], rank2_47["vp_v"]) == (1, 2)
    assert vp(int(scan4["extra_content"]), 7) == 1

    # Sequential ledger and normalization example.
    scan6 = row_at(scan["rows"], 6)
    content6 = int(scan6["extra_content"])
    a6 = int(scan6["primitive_positive_form"]["a"])
    b6 = int(scan6["primitive_positive_form"]["b"])
    epsilon6 = int(scan6["primitive_positive_form"]["epsilon"])
    raw_v6 = abs(int(scan6["V"]["value"]))
    assert raw_v6 == content6 * b6
    p4, q4 = beta_pair(4)
    delta = math.gcd(b6, q4)
    b0, q0 = b6 // delta, q4 // delta
    p_star = b0 * p4 - epsilon6 * q0 * a6
    final_gcd = math.gcd(abs(p_star), delta)
    assert (p4, q4) == (2721, 1001)
    assert delta == 91
    assert math.gcd(raw_v6, q4) == 1001  # wrong if called Delta_m
    assert final_gcd == 7
    assert [vp(value, 7) for value in (content6, delta, final_gcd)] == [1, 1, 1]

    rank1_valuations = [
        min(int(check["vp_u"]), int(check["vp_v"]))
        for row in rank1["rows"]
        for check in row["sharp_normalized_valuation_checks"]
    ]
    rank2_valuations = [
        min(int(check["vp_u"]), int(check["vp_v"]))
        for row in rank2["index_rows"]
        for check in row["vanishing_rank_two_rows"]
    ]

    payload = {
        "input_hashes": {
            scan_path.name: sha256(scan_path),
            rank1_path.name: sha256(rank1_path),
            rank2_path.name: sha256(rank2_path),
        },
        "rank_one_p2_counterexample": {
            "m": 3,
            "p": 3,
            "top_layer": 9,
            "vp_U": val3["vp_u"],
            "vp_V": val3["vp_v"],
            "vp_c": vp(int(scan3["extra_content"]), 3),
            "U": scan3["U"]["value"],
            "V": scan3["V"]["value"],
            "c": scan3["extra_content"],
        },
        "rank_zero_post_G_counterexample": {
            "m": 9,
            "p": 13,
            "vp_G": vp(g9, 13),
            "vp_X": vp(int(scan9["U"]["value"]) * g9, 13),
            "vp_Y": vp(int(scan9["V"]["value"]) * g9, 13),
            "vp_U": val9["vp_u"],
            "vp_V": val9["vp_v"],
            "vp_c": vp(int(scan9["extra_content"]), 13),
        },
        "rank_two_counterexample": {
            "m": 4,
            "p": 7,
            "determinant_mod_p": rank2_47["determinant"],
            "vp_U": rank2_47["vp_u"],
            "vp_V": rank2_47["vp_v"],
            "vp_c": vp(int(scan4["extra_content"]), 7),
        },
        "sequential_ledger_example": {
            "m": 6,
            "N": 4,
            "p_N": p4,
            "q_N": q4,
            "c": content6,
            "correct_Delta": delta,
            "incorrect_raw_gcd_V_qN": math.gcd(raw_v6, q4),
            "P_star": p_star,
            "g": final_gcd,
            "vp7_c_Delta_g": [
                vp(content6, 7),
                vp(delta, 7),
                vp(final_gcd, 7),
            ],
        },
        "finite_diagnostics": {
            "rank_one_forced_rows": len(rank1_valuations),
            "rank_one_rows_with_vp_c_exactly_1": sum(
                value == 1 for value in rank1_valuations
            ),
            "rank_two_vanishing_rows": len(rank2_valuations),
            "rank_two_rows_with_vp_c_exactly_1": sum(
                value == 1 for value in rank2_valuations
            ),
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
