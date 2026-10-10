#!/usr/bin/env python3
"""Replay the bounded-jet no-go and the sequential c*Delta*g ledger.

This checker is read-only with respect to the Desktop archive.  The abstract
differential examples are represented by their exact endpoint coordinates
Z_q=(qR,L,E); the accompanying note proves that the displayed triples are
realized by explicit rational differentials satisfying the same pole/degree
hypotheses as the top-layer relative Cartier lemma.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]

PINNED = {
    "sources/mixed_cubic_coordinates_and_synchronization_audit.md":
        "e92fbc62665c3a6395e05987fae4456c542aace66743c8ed8bd8b201853739b0",
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md":
        "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
    "sources/mixed_cubic_rank_two_cartier_determinant.md":
        "9b34e9088d73a828af12b548f34e669f181d586c212edbf8e80c16ee37c83962",
    "sources/higher_power_cartier_actual_valuation_analysis.md":
        "b7c01630150063a03b3c8d00374aa0b7a3f21b34e1f13e49a7ec736736b4de0b",
    "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json":
        "7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96",
    "results/mixed_cubic_small_prime_rank_one_cartier_certificate.json":
        "10991033ef60dece85f588cdc676a29bd5d1503ad2a28eb718c020f81dbdd6c3",
    "results/mixed_cubic_rank_two_cartier_certificate.json":
        "1fbc73c50ca83cdbbabef090460a944218dc1074a573b32555e4a009f2cb1b02",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vp(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        return 10**9
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def minor_a(z0: tuple[int, int, int], z1: tuple[int, int, int]) -> int:
    """Return q*A=L1*(qR0)-L0*(qR1)."""
    return z1[1] * z0[0] - z0[1] * z1[0]


def minor_8b(z0: tuple[int, int, int], z1: tuple[int, int, int]) -> int:
    """Return 8*B=L1*E0-L0*E1."""
    return z1[1] * z0[2] - z0[1] * z1[2]


def sequential_exponents(
    u: int, v: int, t: int, p_star_valuation: int
) -> tuple[int, int, int, int]:
    """Return exponents (c, Delta, g, total) for one prime.

    u=vp(U), v=vp(V), t=vp(q_N).  The p_star valuation is used only
    in the equal-positive primitive-coefficient case.
    """
    c = min(u, v)
    beta = v - c
    delta = min(beta, t)
    if beta == t and beta > 0:
        g = min(beta, p_star_valuation)
    else:
        g = 0
    return c, delta, g, c + delta + g


def beta_pair(index: int) -> tuple[int, int]:
    p_values = [1, 3]
    q_values = [1, 1]
    for n_value in range(2, index + 1):
        p_values.append((4 * n_value - 2) * p_values[-1] + p_values[-2])
        q_values.append((4 * n_value - 2) * q_values[-1] + q_values[-2])
    return p_values[index], q_values[index]


def row_at(rows: list[dict[str, object]], m_value: int) -> dict[str, object]:
    return next(row for row in rows if int(row["m"]) == m_value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    args = parser.parse_args()

    for relative, expected in PINNED.items():
        actual = sha256(args.archive / relative)
        assert actual == expected, (relative, actual, expected)

    # Explicit endpoint-coordinate models.  rho=x^(q-1)dx,
    # lambda=dx/(4(1+x)), epsilon=dx/(2(1+x^2)) have respective
    # Z_q triples (1,0,0), (0,1,0), (0,0,1).
    jet_rows: list[dict[str, int]] = []
    for prime in (3, 5, 11):
        for target in (1, 2, 4, 7):
            safety = target + 5
            z0 = (1, 1, 1)
            z1 = (1 + prime**target, 1, 1 + prime**safety)
            assert tuple(value % prime for value in z0) == tuple(
                value % prime for value in z1
            )
            assert vp(minor_a(z0, z1), prime) == target
            assert vp(minor_8b(z0, z1), prime) == safety

            # Rank-zero version: both reductions are zero; after one
            # squarefree G digit is removed, the A-side has target digits.
            rz0 = tuple(prime * value for value in z0)
            rz1 = (
                prime + prime**target,
                prime,
                prime + prime**safety,
            )
            rank_zero_a = vp(minor_a(rz0, rz1), prime)
            rank_zero_b = vp(minor_8b(rz0, rz1), prime)
            assert rank_zero_a == target + 1
            assert rank_zero_b == safety + 1
            assert rank_zero_a - 1 == target
            jet_rows.append(
                {
                    "p": prime,
                    "target_post_G_digits": target,
                    "rank_one_vp_qA": target,
                    "rank_zero_vp_qA": rank_zero_a,
                }
            )

    # Fixed-precision indistinguishability: these two lifts agree mod p^J,
    # but their qA determinants have valuations J and J+k.
    precision_rows: list[dict[str, int]] = []
    for prime in (3, 7):
        for precision in (1, 2, 4):
            jump = 3
            common_safety = precision + jump + 5
            z0 = (1, 1, 1)
            z_short = (
                1 + prime**precision,
                1,
                1 + prime**common_safety,
            )
            z_long = (
                1 + prime ** (precision + jump),
                1,
                1 + prime**common_safety,
            )
            assert all(
                (left - right) % (prime**precision) == 0
                for left, right in zip(z_short, z_long)
            )
            assert vp(minor_a(z0, z_short), prime) == precision
            assert vp(minor_a(z0, z_long), prime) == precision + jump
            precision_rows.append(
                {
                    "p": prime,
                    "precision": precision,
                    "short_vp_qA": precision,
                    "long_vp_qA": precision + jump,
                }
            )

    # Exhaust all small exponent ledgers and verify both the piecewise law
    # and c*Delta*g | |V|*q_N prime by prime.
    ledger_cases = 0
    for u in range(7):
        for v in range(7):
            for t in range(7):
                for pstar in range(7):
                    c, delta, g, total = sequential_exponents(u, v, t, pstar)
                    beta = v - c
                    assert delta == min(beta, t)
                    if beta != t or beta == 0:
                        assert g == 0
                    else:
                        assert g == min(beta, pstar)
                    assert total <= v + t
                    assert delta + g <= 2 * min(beta, t)
                    ledger_cases += 1

    # Replay the exact m=6,N=4 overlap and raw-normalization trap.
    scan = json.loads(
        (args.archive / "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")
        .read_text(encoding="utf-8")
    )
    rank1 = json.loads(
        (args.archive / "results/mixed_cubic_small_prime_rank_one_cartier_certificate.json")
        .read_text(encoding="utf-8")
    )
    rank2 = json.loads(
        (args.archive / "results/mixed_cubic_rank_two_cartier_certificate.json")
        .read_text(encoding="utf-8")
    )

    actual_counterexamples: list[dict[str, int | str]] = []
    for m_value, prime, branch in (
        (3, 3, "top_layer_q=p^2"),
        (9, 13, "rank_zero_after_G"),
    ):
        scan_row = row_at(scan["rows"], m_value)
        rank1_row = row_at(rank1["rows"], m_value)
        check = next(
            item
            for item in rank1_row["sharp_normalized_valuation_checks"]
            if int(item["p"]) == prime
        )
        assert min(int(check["vp_u"]), int(check["vp_v"])) == 1
        assert vp(int(scan_row["extra_content"]), prime) == 1
        actual_counterexamples.append(
            {
                "m": m_value,
                "p": prime,
                "branch": branch,
                "vp_U": int(check["vp_u"]),
                "vp_V": int(check["vp_v"]),
                "vp_c": 1,
            }
        )

    scan4 = row_at(scan["rows"], 4)
    rank2_row4 = row_at(rank2["index_rows"], 4)
    check47 = next(
        item
        for item in rank2_row4["vanishing_rank_two_rows"]
        if int(item["p"]) == 7
    )
    assert int(check47["determinant"]) == 0
    assert min(int(check47["vp_u"]), int(check47["vp_v"])) == 1
    assert vp(int(scan4["extra_content"]), 7) == 1
    actual_counterexamples.append(
        {
            "m": 4,
            "p": 7,
            "branch": "rank_two_determinant_zero",
            "vp_U": int(check47["vp_u"]),
            "vp_V": int(check47["vp_v"]),
            "vp_c": 1,
        }
    )

    row6 = row_at(scan["rows"], 6)
    content = int(row6["extra_content"])
    raw_v = abs(int(row6["V"]["value"]))
    a_value = int(row6["primitive_positive_form"]["a"])
    b_value = int(row6["primitive_positive_form"]["b"])
    epsilon_sign = int(row6["primitive_positive_form"]["epsilon"])
    p4, q4 = beta_pair(4)
    delta_value = math.gcd(b_value, q4)
    b0, q0 = b_value // delta_value, q4 // delta_value
    p_star = b0 * p4 - epsilon_sign * q0 * a_value
    g_value = math.gcd(abs(p_star), delta_value)
    assert raw_v == content * b_value
    assert (p4, q4) == (2721, 1001)
    assert (delta_value, g_value) == (91, 7)
    assert math.gcd(raw_v, q4) == 1001
    assert content * delta_value * g_value <= raw_v * q4
    assert (raw_v * q4) % (content * delta_value * g_value) == 0

    # Recompute the exact rank-one rate and the certified remaining target.
    getcontext().prec = 70
    rank_one_rate = (
        -4 * Decimal(2).ln() + 6 * Decimal(3).ln() - Decimal(3)
    ) / 6
    threshold_lower = Decimal(
        "1.1561471519642446123307302238571333988967248706278756"
    )
    threshold_upper = Decimal(
        "1.1561471519642446123307302238571333988967248706278757"
    )
    deficit_lower = threshold_lower - rank_one_rate
    deficit_upper = threshold_upper - rank_one_rate

    payload = {
        "status": "PASS",
        "pinned_inputs": PINNED,
        "bounded_jet_models_checked": len(jet_rows),
        "fixed_precision_models_checked": len(precision_rows),
        "sequential_exponent_cases_checked": ledger_cases,
        "actual_uniform_p2_counterexamples": actual_counterexamples,
        "rank_one_rate": str(rank_one_rate),
        "certified_optimal_remaining_weight_interval": [
            str(deficit_lower),
            str(deficit_upper),
        ],
        "sequential_overlap_example": {
            "m": 6,
            "N": 4,
            "c": content,
            "Delta": delta_value,
            "g": g_value,
            "wrong_raw_gcd": math.gcd(raw_v, q4),
            "c_Delta_g_divides_absV_qN": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
