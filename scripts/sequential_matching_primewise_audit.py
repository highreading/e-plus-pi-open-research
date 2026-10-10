#!/usr/bin/env python3
"""Replay and factor the item-140 sequential matching ledger.

This script is deliberately read-only with respect to the research archive.
It verifies every parity-compatible candidate in the stored N <= 6m scan,
then emits exact primewise decompositions for both the content maximizer and
the analytically smallest stored match at each 1 <= m <= 100.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
PINNED_INPUT = (
    "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json",
    "7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def factor_over_primes(value: int, primes: list[int]) -> tuple[dict[int, int], int]:
    remainder = abs(value)
    factors: dict[int, int] = {}
    for prime in primes:
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
        if remainder == 1:
            break
    return factors, remainder


def factor_small(value: int) -> dict[int, int]:
    """Complete deterministic trial factorization for the small match factors."""
    remainder = abs(value)
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= remainder:
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
        prime = 3 if prime == 2 else prime + 2
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def factor_product(factors: dict[int, int]) -> int:
    return math.prod(prime**exponent for prime, exponent in factors.items())


def vp(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("valuation of zero is not needed in this certificate")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def beta_pairs(maximum_n: int) -> list[tuple[int, int]]:
    pairs = [(1, 1), (3, 1)]
    for index in range(2, maximum_n + 1):
        p0, q0 = pairs[-2]
        p1, q1 = pairs[-1]
        multiplier = 4 * index - 2
        pairs.append((multiplier * p1 + p0, multiplier * q1 + q0))
    return pairs[: maximum_n + 1]


def candidate_values(
    row: dict[str, object], index: int, pair: tuple[int, int]
) -> tuple[int, int, int, int, int]:
    content = int(row["extra_content"])
    a_value = int(row["primitive_positive_form"]["a"])
    b_value = int(row["primitive_positive_form"]["b"])
    epsilon = int(row["primitive_positive_form"]["epsilon"])
    p_beta, q_beta = pair
    delta = math.gcd(b_value, q_beta)
    b0 = b_value // delta
    q0 = q_beta // delta
    p_star = b0 * p_beta - epsilon * q0 * a_value
    if p_star == 0:
        raise AssertionError((row["m"], index, "unexpected zero P-star"))
    final_content = math.gcd(abs(p_star), delta)
    return content, delta, final_content, p_star, q_beta


def primewise_decomposition(
    row: dict[str, object],
    index: int,
    pair: tuple[int, int],
    content_factors: dict[int, int],
) -> dict[str, object]:
    content, delta, final_content, p_star, q_beta = candidate_values(
        row, index, pair
    )
    delta_factors = factor_small(delta)
    final_factors = factor_small(final_content)
    assert factor_product(delta_factors) == delta
    assert factor_product(final_factors) == final_content

    u_value = int(row["U"]["value"])
    v_value = int(row["V"]["value"])
    b_value = int(row["primitive_positive_form"]["b"])
    assert math.gcd(abs(u_value), abs(v_value)) == content
    assert abs(v_value) == content * b_value

    support = sorted(set(content_factors) | set(delta_factors) | set(final_factors))
    ledger = []
    for prime in support:
        u_exp = vp(u_value, prime)
        v_exp = vp(v_value, prime)
        kappa = min(u_exp, v_exp)
        beta = v_exp - kappa
        t_exp = vp(q_beta, prime)
        delta_exp = vp(delta, prime)
        gamma = vp(final_content, prime)
        p_star_exp = vp(p_star, prime)
        assert kappa == content_factors.get(prime, 0)
        assert beta == vp(b_value, prime)
        assert delta_exp == min(beta, t_exp)
        expected_gamma = (
            min(beta, p_star_exp) if beta == t_exp and beta > 0 else 0
        )
        assert gamma == expected_gamma
        ledger.append(
            {
                "p": prime,
                "vp_U": u_exp,
                "vp_V": v_exp,
                "kappa_vp_c": kappa,
                "beta_vp_b": beta,
                "t_vp_qN": t_exp,
                "d_vp_Delta": delta_exp,
                "vp_P_star": p_star_exp,
                "gamma_vp_g": gamma,
                "total_exponent": kappa + delta_exp + gamma,
            }
        )

    total = content * delta * final_content
    assert total <= abs(v_value) * q_beta
    assert (abs(v_value) * q_beta) % total == 0
    assert (q_beta * q_beta) % (delta * final_content) == 0
    return {
        "N": index,
        "c": str(content),
        "Delta": str(delta),
        "g": str(final_content),
        "c_Delta_g": str(total),
        "c_factorization": {str(p): e for p, e in content_factors.items()},
        "Delta_factorization": {str(p): e for p, e in delta_factors.items()},
        "g_factorization": {str(p): e for p, e in final_factors.items()},
        "primewise_ledger": ledger,
    }


def block_summary(rows: list[dict[str, object]], lo: int, hi: int) -> dict[str, object]:
    block = [row for row in rows if lo <= int(row["m"]) <= hi]
    return {
        "m": [lo, hi],
        "count": len(block),
        "mean_c_rate": math.fsum(float(row["c_rate"]) for row in block) / len(block),
        "mean_matching_rate": math.fsum(
            float(row["matching_rate"]) for row in block
        )
        / len(block),
        "mean_total_rate": math.fsum(float(row["total_rate"]) for row in block)
        / len(block),
        "max_matching_rate": max(float(row["matching_rate"]) for row in block),
        "max_total_rate": max(float(row["total_rate"]) for row in block),
        "mean_K_after_Cartier_rate": math.fsum(
            float(row["clearing_reservoir"]["K_after_Cartier_rate"])
            for row in block
        )
        / len(block),
        "mean_forced_primitive_b_divisor_rate": math.fsum(
            float(row["clearing_reservoir"]["forced_divisor_of_primitive_b_rate"])
            for row in block
        )
        / len(block),
        "mean_K_captured_in_c_Delta_rate": math.fsum(
            float(row["clearing_reservoir"]["captured_rate"])
            for row in block
        )
        / len(block),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    relative, expected_hash = PINNED_INPUT
    input_path = args.archive / relative
    actual_hash = sha256(input_path)
    assert actual_hash == expected_hash, (actual_hash, expected_hash)
    scan = json.loads(input_path.read_text(encoding="utf-8"))
    rows_in = scan["rows"]
    assert len(rows_in) == 100
    maximum_n = max(6 * int(row["m"]) for row in rows_in)
    beta = beta_pairs(maximum_n)
    all_primes = primes_upto(6 * len(rows_in))

    candidate_transcript = hashlib.sha256()
    candidate_count = 0
    candidates_delta_nontrivial = 0
    candidates_g_nontrivial = 0
    selected_rows: list[dict[str, object]] = []
    selected_n_counter: Counter[int] = Counter()
    selected_matching_prime_counter: Counter[int] = Counter()
    selected_g_prime_counter: Counter[int] = Counter()
    all_candidate_g_prime_counter: Counter[int] = Counter()
    c_prime_counter: Counter[int] = Counter()
    all_c_support_within_6m = True
    largest_selected_matching_prime = 1
    largest_candidate_g = {"g": 1, "m": 1, "N": 1, "Delta": 1}

    for row in rows_in:
        m_value = int(row["m"])
        content = int(row["extra_content"])
        sharp_clearing = int(row["sharp_clearing"]["value"])
        cartier_product = int(row["cartier_product"]["value"])
        dyadic_clearing = 2 ** (9 * m_value + 5)
        assert sharp_clearing % dyadic_clearing == 0
        k_value = sharp_clearing // dyadic_clearing
        k_after_cartier = k_value // math.gcd(k_value, cartier_product)
        k_for_primitive_b = k_after_cartier // math.gcd(k_after_cartier, content)
        c_factors, c_remainder = factor_over_primes(
            content, [prime for prime in all_primes if prime <= 6 * m_value]
        )
        assert c_remainder == 1, (m_value, c_remainder)
        assert factor_product(c_factors) == content
        all_c_support_within_6m &= all(prime <= 6 * m_value for prime in c_factors)
        for prime in c_factors:
            c_prime_counter[prime] += 1

        epsilon = int(row["epsilon"])
        required_parity = 0 if epsilon == 1 else 1
        best_total = -1
        best_tuple: tuple[int, int, int] | None = None
        admissible = 0
        for index in range(1, 6 * m_value + 1):
            if index % 2 != required_parity:
                continue
            admissible += 1
            candidate_count += 1
            c_value, delta, final_content, _, q_beta = candidate_values(
                row, index, beta[index]
            )
            assert c_value == content
            assert (q_beta * q_beta) % (delta * final_content) == 0
            candidates_delta_nontrivial += int(delta > 1)
            candidates_g_nontrivial += int(final_content > 1)
            if final_content > 1:
                for prime in factor_small(final_content):
                    all_candidate_g_prime_counter[prime] += 1
            if final_content > int(largest_candidate_g["g"]):
                largest_candidate_g = {
                    "g": final_content,
                    "m": m_value,
                    "N": index,
                    "Delta": delta,
                }
            total = content * delta * final_content
            candidate_transcript.update(
                f"{m_value}:{index}:{content}:{delta}:{final_content}:{total}\n".encode(
                    "ascii"
                )
            )
            if total > best_total:
                best_total = total
                best_tuple = (index, delta, final_content)
        assert admissible == int(row["candidate_scan"]["admissible_count"])
        assert best_tuple is not None
        stored_max = row["maximum_total_content_in_window"]
        assert best_tuple == (
            int(stored_max["N"]),
            int(stored_max["delta"]),
            int(stored_max["final_content"]),
        )
        assert best_total == int(stored_max["total_content"])

        n_max = best_tuple[0]
        n_min = int(row["minimum_positive_match"]["N"])
        maximum_decomposition = primewise_decomposition(
            row, n_max, beta[n_max], c_factors
        )
        minimum_decomposition = primewise_decomposition(
            row, n_min, beta[n_min], c_factors
        )
        stored_minimum = row["minimum_positive_match"]
        assert int(minimum_decomposition["Delta"]) == int(stored_minimum["delta"])
        assert int(minimum_decomposition["g"]) == int(
            stored_minimum["final_content"]
        )
        selected_n_counter[n_max] += 1
        delta_factors = {
            int(p): int(e)
            for p, e in maximum_decomposition["Delta_factorization"].items()
        }
        g_factors = {
            int(p): int(e)
            for p, e in maximum_decomposition["g_factorization"].items()
        }
        for prime in delta_factors:
            selected_matching_prime_counter[prime] += 1
            largest_selected_matching_prime = max(largest_selected_matching_prime, prime)
        for prime in g_factors:
            selected_g_prime_counter[prime] += 1

        matching_rate = math.log(best_tuple[1] * best_tuple[2]) / (6 * m_value)
        c_rate = math.log(content) / (6 * m_value)
        total_rate = math.log(best_total) / (6 * m_value)
        _, delta_max, _, _, q_beta_max = candidate_values(
            row, n_max, beta[n_max]
        )
        b_value = int(row["primitive_positive_form"]["b"])
        assert b_value % k_for_primitive_b == 0
        captured_k = math.gcd(k_after_cartier, content * q_beta_max)
        assert (content * delta_max) % captured_k == 0
        assert abs(total_rate - float(stored_max["log_per_n"])) < 2e-14
        selected_rows.append(
            {
                "m": m_value,
                "epsilon": epsilon,
                "c_rate": c_rate,
                "matching_rate": matching_rate,
                "total_rate": total_rate,
                "clearing_reservoir": {
                    "K_after_Cartier": str(k_after_cartier),
                    "K_after_Cartier_rate": math.log(k_after_cartier)
                    / (6 * m_value),
                    "forced_divisor_of_primitive_b": str(k_for_primitive_b),
                    "forced_divisor_of_primitive_b_rate": math.log(
                        k_for_primitive_b
                    )
                    / (6 * m_value),
                    "captured_in_c_Delta_at_content_maximizer": str(captured_k),
                    "captured_rate": math.log(captured_k) / (6 * m_value),
                },
                "content_maximizer": maximum_decomposition,
                "minimum_positive_match": minimum_decomposition,
            }
        )

    frequent_indices = [
        {"N": index, "count": count}
        for index, count in sorted(
            selected_n_counter.items(), key=lambda item: (-item[1], item[0])
        )
    ]
    block_summaries = [
        block_summary(selected_rows, lo, hi)
        for lo, hi in ((1, 20), (21, 40), (41, 60), (61, 80), (81, 100))
    ]
    largest_matching_row = max(selected_rows, key=lambda row: row["matching_rate"])
    largest_total_row = max(selected_rows, key=lambda row: row["total_rate"])

    payload = {
        "schema": "item163-sequential-matching-primewise-audit-v1",
        "status": "PASS",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": sha256(Path(__file__)),
        },
        "classification": {
            "PROVED_FINITE": [
                "Every parity-compatible candidate 1 <= N <= 6m for 1 <= m <= 100 was replayed from the pinned exact coordinates.",
                "The stored content maximizer and its c, Delta, g values agree at every m.",
                "The primewise sequential law kappa=min(vp(U),vp(V)), d=min(beta,t), and gamma=0 unless beta=t>0 was verified for both stored distinguished candidates at every m.",
                "For every replayed candidate, Delta*g divides q_N^2 and c*Delta*g divides abs(V)*q_N.",
                "Every c_m in the finite scope factors completely over primes p <= 6m.",
            ],
            "EXPERIMENTAL": [
                "Block means, repeated maximizing indices, and prime frequencies below are finite diagnostics only.",
                "The finite matching increment is small compared with the required theorem-scale deficit, but this is not an asymptotic upper bound.",
            ],
            "OPEN": [
                "Any positive asymptotic lower bound for Delta*g after full c-division.",
                "Any theorem placing enough shared prime mass between b_m and q_N at the moving scale N asymptotic to m/log m.",
                "Any asymptotic upper or lower bound for the actual total c*Delta*g strong enough to decide the route.",
            ],
        },
        "pinned_input": {"path": relative, "sha256": actual_hash},
        "candidate_scope": {
            "m": [1, 100],
            "N": "parity-compatible 1 <= N <= 6m",
            "candidate_count": candidate_count,
            "canonical_exact_ledger_sha256": candidate_transcript.hexdigest(),
            "delta_nontrivial_count": candidates_delta_nontrivial,
            "g_nontrivial_count": candidates_g_nontrivial,
        },
        "finite_support_checks": {
            "all_c_support_within_p_le_6m": all_c_support_within_6m,
            "largest_prime_in_selected_Delta": largest_selected_matching_prime,
        },
        "selected_index_frequencies": frequent_indices,
        "selected_Delta_prime_row_frequencies": [
            {"p": prime, "rows": count}
            for prime, count in sorted(
                selected_matching_prime_counter.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ],
        "selected_g_prime_row_frequencies": [
            {"p": prime, "rows": count}
            for prime, count in sorted(
                selected_g_prime_counter.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ],
        "all_candidate_g_prime_frequencies": [
            {"p": prime, "candidates": count}
            for prime, count in sorted(
                all_candidate_g_prime_counter.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ],
        "largest_candidate_g": largest_candidate_g,
        "c_prime_row_frequencies": [
            {"p": prime, "rows": count}
            for prime, count in sorted(
                c_prime_counter.items(), key=lambda item: (-item[1], item[0])
            )
        ],
        "block_summaries": block_summaries,
        "largest_selected_matching_rate": {
            "m": largest_matching_row["m"],
            "N": largest_matching_row["content_maximizer"]["N"],
            "rate": largest_matching_row["matching_rate"],
        },
        "largest_selected_total_rate": {
            "m": largest_total_row["m"],
            "N": largest_total_row["content_maximizer"]["N"],
            "rate": largest_total_row["total_rate"],
        },
        "rows": selected_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.write_bytes(encoded)
    print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
