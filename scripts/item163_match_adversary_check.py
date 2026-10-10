#!/usr/bin/env python3
"""Adversarial replay of the sequential mixed-cubic/Bessel matching ledger.

The checker is read-only with respect to the Desktop archive.  It replays all
15,150 parity-compatible candidates in the frozen m<=100, N<=6m scan, checks
the exact c*Delta*g normalization prime by prime, and records diagnostics that
distinguish finite plateaus from an asymptotic synchronization mechanism.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parents[1]
OUTPUT = Path("work/item163_match_adversary_certificate.json")

PINNED = {
    "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json":
        "7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96",
    "sources/modp2_bounded_jet_and_sequential_mass_adversary.md":
        "2f228328337b558e04fc3786416b546f5cdb1d13f8ea07f8f8d12caef929bad3",
    "sources/mixed_cubic_equal_valuation_crt_reduction.md":
        "56b2b3297e5c2d780ad8c7dd5c8605f7c8fdba51fca7786d2669758b3ed1ba93",
    "sources/bessel_denominator_zero_gap_smooth_radical_barrier.md":
        "dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc",
    "sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md":
        "c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de",
    "results/mixed_cubic_matching_factor_two_and_classification_barrier_certificate.json":
        "8591bc62937f6e07eea35cd903e2cc32f3e72d970f59e584cc1768da349898a2",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vp(value: int, prime: int) -> int:
    value = abs(value)
    out = 0
    while value and value % prime == 0:
        value //= prime
        out += 1
    return out


FACTOR_CACHE: dict[int, dict[int, int]] = {1: {}}


def factor_odd(value: int) -> dict[int, int]:
    """Deterministic trial factorization for the exact replay."""
    value = abs(value)
    if value in FACTOR_CACHE:
        return FACTOR_CACHE[value]
    original = value
    factors: dict[int, int] = {}
    assert value % 2 == 1
    prime = 3
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    FACTOR_CACHE[original] = factors
    return factors


def beta_pairs(limit: int) -> tuple[list[int], list[int]]:
    p_values = [1, 3]
    q_values = [1, 1]
    for index in range(2, limit + 1):
        p_values.append((4 * index - 2) * p_values[-1] + p_values[-2])
        q_values.append((4 * index - 2) * q_values[-1] + q_values[-2])
    return p_values, q_values


def shift_polynomial(blocks: list[tuple[int, int]]) -> dict[int, int]:
    """Coefficients of product_p (1+S^p)^(2k_p)."""
    coefficients = {0: 1}
    for prime, order in blocks:
        updated: dict[int, int] = {}
        for old_shift, old_coefficient in coefficients.items():
            for index in range(2 * order + 1):
                new_shift = old_shift + index * prime
                updated[new_shift] = updated.get(new_shift, 0) + (
                    old_coefficient * math.comb(2 * order, index)
                )
        coefficients = updated
    return coefficients


getcontext().prec = 80


def log_decimal(value: int) -> Decimal:
    assert value > 0
    return Decimal(value).ln()


def decimal_string(value: Decimal, places: int = 30) -> str:
    return format(value, f".{places}f")


def rate(value: int, denominator: int) -> Decimal:
    return log_decimal(value) / Decimal(denominator)


def main() -> None:
    for relative, expected in PINNED.items():
        actual = sha256(ARCHIVE / relative)
        assert actual == expected, (relative, actual, expected)

    scan = json.loads(
        (ARCHIVE / "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")
        .read_text(encoding="utf-8")
    )
    rows = scan["rows"]
    assert scan["schema"] == "mixed-cubic-positive-match-exact-scan-v2"
    assert [int(row["m"]) for row in rows] == list(range(1, 101))

    p_beta, q_beta = beta_pairs(600)
    for index in range(1, 601):
        assert p_beta[index] % 2 == q_beta[index] % 2 == 1
        assert math.gcd(p_beta[index], q_beta[index]) == 1
        determinant = (
            p_beta[index] * q_beta[index - 1]
            - p_beta[index - 1] * q_beta[index]
        )
        assert determinant == 2 * (-1) ** (index - 1)

    # Multi-index forced-divisor replay.  Distinct primes let the archived
    # all-even antiperiod divisors combine by coprimality.  Other shift
    # blocks preserve each divisibility because their coefficients are
    # integral and all operators commute.
    multi_index_cases = [
        [(3, 1)],
        [(5, 2), (7, 3)],
        [(3, 1), (5, 1), (7, 2), (11, 5), (13, 6)],
    ]
    multi_index_replay: list[dict[str, object]] = []
    multi_index_value_checks = 0
    log3_over_6 = Decimal(3).ln() / Decimal(6)
    for blocks in multi_index_cases:
        assert len({prime for prime, _ in blocks}) == len(blocks)
        assert all(prime > 2 * order for prime, order in blocks)
        coefficients = shift_polynomial(blocks)
        span = sum(2 * order * prime for prime, order in blocks)
        divisor = math.prod(prime**order for prime, order in blocks)
        assert max(coefficients) == span
        assert log_decimal(divisor) <= log3_over_6 * Decimal(span)
        for base_index in range(11):
            aggregate_q = sum(
                coefficient * q_beta[base_index + shift]
                for shift, coefficient in coefficients.items()
            )
            assert aggregate_q % divisor == 0
            multi_index_value_checks += 1
        multi_index_replay.append(
            {
                "blocks": [
                    {"p": prime, "k": order} for prime, order in blocks
                ],
                "span_W": span,
                "forced_divisor_D": divisor,
                "log_D_over_W": decimal_string(
                    log_decimal(divisor) / Decimal(span)
                ),
                "log_3_over_6_ceiling": decimal_string(log3_over_6),
                "base_indices_checked": [0, 10],
            }
        )

    candidate_count = 0
    equal_candidate_count = 0
    equal_prime_slots = 0
    nontrivial_g_count = 0
    g_prime_slots = 0
    outside_events: list[dict[str, int]] = []
    outside_g_events: list[dict[str, int]] = []
    delta_prime_frequency: Counter[int] = Counter()
    g_prime_frequency: Counter[int] = Counter()
    optimizing_groups: defaultdict[tuple[int, int, int], list[int]] = defaultdict(list)
    optimizing_rows: list[dict[str, object]] = []
    largest_delta = (0, 0, 0, 0)  # value,m,N,g
    largest_g = (0, 0, 0, 0)      # value,m,N,Delta

    for row in rows:
        m_value = int(row["m"])
        a_value = int(row["primitive_positive_form"]["a"])
        b_value = int(row["primitive_positive_form"]["b"])
        epsilon = int(row["primitive_positive_form"]["epsilon"])
        content = int(row["extra_content"])
        raw_v = abs(int(row["V"]["value"]))
        assert raw_v == content * b_value
        assert math.gcd(abs(a_value), b_value) == 1

        best_total = -1
        best_data: tuple[int, int, int] | None = None
        row_g_candidates = 0
        for index in range(1, 6 * m_value + 1):
            if (-1) ** index != epsilon:
                continue
            candidate_count += 1
            p_value, q_value = p_beta[index], q_beta[index]
            delta = math.gcd(b_value, q_value)
            b0, q0 = b_value // delta, q_value // delta
            p_star = b0 * p_value - epsilon * q0 * a_value
            final_content = math.gcd(abs(p_star), delta)
            total = content * delta * final_content

            # Exact global capacity envelope and sequential divisor check.
            assert delta % final_content == 0
            assert (delta * delta) % (delta * final_content) == 0
            assert (b_value * b_value) % (delta * final_content) == 0
            assert (q_value * q_value) % (delta * final_content) == 0
            assert (raw_v * q_value) % total == 0

            factors_delta = factor_odd(delta)
            factors_g = factor_odd(final_content)
            equal_ceiling = 1
            for prime, exponent in factors_delta.items():
                delta_prime_frequency[prime] += 1
                beta_exp = vp(b_value, prime)
                q_exp = vp(q_value, prime)
                assert exponent == min(beta_exp, q_exp)
                if beta_exp == q_exp:
                    equal_ceiling *= prime**exponent
                    equal_prime_slots += 1
                if prime > 6 * m_value:
                    outside_events.append(
                        {
                            "m": m_value,
                            "N": index,
                            "p": prime,
                            "vp_Delta": exponent,
                            "vp_g": factors_g.get(prime, 0),
                        }
                    )

            if equal_ceiling > 1:
                equal_candidate_count += 1
            assert equal_ceiling % final_content == 0

            if final_content > 1:
                nontrivial_g_count += 1
                row_g_candidates += 1
                for prime, exponent in factors_g.items():
                    g_prime_frequency[prime] += 1
                    g_prime_slots += 1
                    assert vp(b_value, prime) == vp(q_value, prime) > 0
                    if prime > 6 * m_value:
                        outside_g_events.append(
                            {
                                "m": m_value,
                                "N": index,
                                "p": prime,
                                "vp_g": exponent,
                            }
                        )

            if delta > largest_delta[0]:
                largest_delta = (delta, m_value, index, final_content)
            if final_content > largest_g[0]:
                largest_g = (final_content, m_value, index, delta)

            if total > best_total:
                best_total = total
                best_data = (index, delta, final_content)

        assert best_data is not None
        best_index, best_delta, best_g = best_data
        stored = row["maximum_total_content_in_window"]
        assert int(stored["N"]) == best_index
        assert int(stored["delta"]) == best_delta
        assert int(stored["final_content"]) == best_g
        assert int(stored["total_content"]) == best_total

        optimizing_groups[(best_index, best_delta, best_g)].append(m_value)
        optimizing_rows.append(
            {
                "m": m_value,
                "N": best_index,
                "Delta": best_delta,
                "g": best_g,
                "c_rate": rate(content, 6 * m_value),
                "Delta_rate": rate(best_delta, 6 * m_value),
                "g_rate": rate(best_g, 6 * m_value),
                "matching_rate": rate(best_delta * best_g, 6 * m_value),
                "total_rate": rate(best_total, 6 * m_value),
                "row_nontrivial_g_candidates": row_g_candidates,
            }
        )

    assert candidate_count == 15150
    assert equal_candidate_count == 6057
    assert equal_prime_slots == 7393
    assert nontrivial_g_count == 234
    assert g_prime_slots == 236
    assert not outside_g_events
    assert largest_delta == (596038519, 92, 544, 1)
    assert largest_g == (1133, 91, 455, 12463)

    # Exhaust the abstract local exponent states.  This verifies that a final
    # digit is possible only on the equal-positive valuation diagonal and
    # that Delta*g never exceeds gcd(b,q)^2.
    exponent_cases = 0
    for beta_exp in range(9):
        for q_exp in range(9):
            delta_exp = min(beta_exp, q_exp)
            possible_g = (
                range(beta_exp + 1)
                if beta_exp == q_exp and beta_exp > 0
                else (0,)
            )
            for g_exp in possible_g:
                assert delta_exp + g_exp <= 2 * min(beta_exp, q_exp)
                if g_exp > 0:
                    assert beta_exp == q_exp > 0
                exponent_cases += 1

    # Sharpness and non-forcing examples at N=2: the same primitive positive
    # coefficient b=q_2 can have either g=q_2 or g=1.
    assert (p_beta[2], q_beta[2]) == (19, 7)
    sharp_a, sharp_b = 19, 7
    sharp_delta = math.gcd(sharp_b, q_beta[2])
    sharp_p_star = sharp_b // sharp_delta * p_beta[2] - sharp_a
    sharp_g = math.gcd(abs(sharp_p_star), sharp_delta)
    assert math.gcd(sharp_a, sharp_b) == 1
    assert sharp_delta * sharp_g == q_beta[2] ** 2

    thin_a, thin_b = 20, 7
    thin_delta = math.gcd(thin_b, q_beta[2])
    thin_p_star = thin_b // thin_delta * p_beta[2] - thin_a
    thin_g = math.gcd(abs(thin_p_star), thin_delta)
    assert math.gcd(thin_a, thin_b) == 1
    assert (thin_delta, thin_g) == (7, 1)

    barrier = json.loads(
        (
            ARCHIVE
            / "results/mixed_cubic_matching_factor_two_and_classification_barrier_certificate.json"
        ).read_text(encoding="utf-8")
    )
    constants = barrier["analytic_constants"]["values"]
    theta = Decimal(constants["d_over_2"])
    threshold = Decimal(constants["h_minus_d_over_2"])
    rank_one_rate = (
        -4 * Decimal(2).ln() + 6 * Decimal(3).ln() - Decimal(3)
    ) / Decimal(6)
    remaining_after_rank_one = threshold - rank_one_rate
    one_copy_capture_fraction = remaining_after_rank_one / theta
    doubled_capture_fraction = remaining_after_rank_one / (2 * theta)

    block_summaries: list[dict[str, object]] = []
    for start in range(1, 101, 10):
        block = optimizing_rows[start - 1 : start + 9]
        mean_matching = sum(
            (item["matching_rate"] for item in block), Decimal(0)
        ) / Decimal(len(block))
        block_summaries.append(
            {
                "m_range": [start, start + 9],
                "mean_best_matching_rate": decimal_string(mean_matching),
                "maximum_best_matching_rate": decimal_string(
                    max(item["matching_rate"] for item in block)
                ),
                "distinct_optimizing_N": sorted(
                    {int(item["N"]) for item in block}
                ),
            }
        )

    last_twenty = optimizing_rows[-20:]
    last_twenty_means = {}
    for key in ("c_rate", "Delta_rate", "g_rate", "matching_rate", "total_rate"):
        last_twenty_means[key] = decimal_string(
            sum((item[key] for item in last_twenty), Decimal(0)) / Decimal(20)
        )
    last_twenty_max = max(last_twenty, key=lambda item: item["total_rate"])

    repeated_groups = []
    for (index, delta, final_content), m_values in sorted(
        optimizing_groups.items(), key=lambda item: (-len(item[1]), item[0])
    ):
        if len(m_values) < 4:
            continue
        repeated_groups.append(
            {
                "N": index,
                "Delta": delta,
                "g": final_content,
                "count": len(m_values),
                "m_values": m_values,
                "fixed_index_capacity_qN_squared_digits": len(
                    str(q_beta[index] ** 2)
                ),
            }
        )

    payload = {
        "schema": "item163-sequential-matching-adversary-v1",
        "status": "PASS",
        "pinned_inputs": PINNED,
        "proved_replay": {
            "candidate_count": candidate_count,
            "stored_row_maxima_replayed": len(rows),
            "beta_wronskian_checks": 600,
            "abstract_exponent_cases": exponent_cases,
            "multi_index_antiperiod_value_checks": multi_index_value_checks,
            "multi_index_antiperiod_replay": multi_index_replay,
            "capacity_envelope": (
                "Delta*g divides gcd(b,q_N)^2, hence log(Delta*g) <= "
                "2*min(log b,log q_N); c*Delta*g divides abs(V)*q_N"
            ),
            "fixed_index_no_go": (
                "For bounded N, Delta*g <= q_N^2 is bounded, so its rate "
                "per 6m tends to zero. More generally N*log(N)=o(m) "
                "implies log(Delta*g)=o(m)."
            ),
            "positive_mass_floor": (
                "If a squarefree prime family S is forced into Delta, then "
                "product(S) divides q_N and sum(log p for p in S) <= log q_N."
            ),
            "multi_index_span_no_go": (
                "For distinct blocks (1+S^p)^(2k_p), p>2k_p, the forced "
                "raw-Q divisor D=product p^k has span W=sum 2*k*p and "
                "log D <= (log 3/6)*W. If W=O(m/log m), even optimistically "
                "granting primitive survival and full g-doubling gives o(m)."
            ),
            "sharpness_example": {
                "N": 2,
                "p_N": 19,
                "q_N": 7,
                "saturating_primitive_pair": {
                    "a": sharp_a,
                    "b": sharp_b,
                    "Delta": sharp_delta,
                    "g": sharp_g,
                    "Delta_times_g": sharp_delta * sharp_g,
                },
                "same_b_nonforcing_pair": {
                    "a": thin_a,
                    "b": thin_b,
                    "Delta": thin_delta,
                    "g": thin_g,
                },
            },
        },
        "rate_capacity_at_balanced_beta_scale": {
            "theta_log_q_per_6m": decimal_string(theta),
            "rank_one_rate": decimal_string(rank_one_rate),
            "remaining_weight_after_rank_one": decimal_string(
                remaining_after_rank_one
            ),
            "minimum_fraction_of_total_qN_log_height_if_Delta_alone_supplies_remainder":
                decimal_string(one_copy_capture_fraction),
            "minimum_fraction_if_every_synchronized_digit_is_doubled_by_g":
                decimal_string(doubled_capture_fraction),
            "interpretation": (
                "Necessary capacity conditions only; neither fraction is "
                "proved attainable or impossible for the actual coordinates."
            ),
        },
        "finite_exact_diagnostics": {
            "scope": {"m": [1, 100], "N": "parity-compatible, 1<=N<=6m"},
            "equal_level_candidates": equal_candidate_count,
            "candidates_with_g_gt_1": nontrivial_g_count,
            "conditional_g_hit_fraction": decimal_string(
                Decimal(nontrivial_g_count) / Decimal(equal_candidate_count)
            ),
            "equal_prime_slots": equal_prime_slots,
            "g_prime_slots": g_prime_slots,
            "prime_slot_hit_fraction": decimal_string(
                Decimal(g_prime_slots) / Decimal(equal_prime_slots)
            ),
            "largest_Delta": {
                "value": largest_delta[0],
                "m": largest_delta[1],
                "N": largest_delta[2],
                "g": largest_delta[3],
                "factorization": factor_odd(largest_delta[0]),
            },
            "largest_g": {
                "value": largest_g[0],
                "m": largest_g[1],
                "N": largest_g[2],
                "Delta": largest_g[3],
                "factorization": factor_odd(largest_g[0]),
            },
            "Delta_prime_frequency": dict(sorted(delta_prime_frequency.items())),
            "g_prime_frequency": dict(sorted(g_prime_frequency.items())),
            "outside_p_gt_6m_Delta_events": outside_events,
            "outside_p_gt_6m_g_events": outside_g_events,
            "block_best_matching_rates": block_summaries,
            "last_twenty_mean_rates": last_twenty_means,
            "last_twenty_maximum_total_rate": {
                key: (
                    decimal_string(value)
                    if isinstance(value, Decimal)
                    else value
                )
                for key, value in last_twenty_max.items()
            },
            "repeated_fixed_index_maximizers_count_at_least_4": repeated_groups,
        },
        "classification": {
            "PROVED": [
                "The separate capacity envelope Delta*g | gcd(b,q_N)^2.",
                "A bounded (or N*log N=o(m)) beta-index family has zero exponential matching rate.",
                "Any squarefree positive-mass prime family forced into Delta must consume the same logarithmic mass inside q_N.",
                "Primitivity and positivity alone do not force g and do not improve the q_N^2 envelope.",
                "Products of distinct certified all-even antiperiod blocks have forced-divisor rate at most (log 3/6) times their forward shift span.",
            ],
            "EXPERIMENTAL": [
                "All finite frequencies and decreasing block rates in m<=100.",
                "Only ten candidate-prime events with p>6m entered Delta, and none entered g, in the exact scan.",
                "Repeated fixed-index plateaus dominate the late finite maxima.",
            ],
            "OPEN": [
                "Any positive asymptotic lower bound for actual log(Delta_m*g_m)/(6m), or any nontrivial upper bound below the universal 2*log(q_N) capacity.",
                "A positive-density actual prime family simultaneously dividing b_m and q_N at saddle-compatible N.",
                "Exclusion or construction of exponentially small ordinary CRT representatives; abundance and synchronization of first-level singular primes; and, separately, an exponential contribution from deeper all-lift/Wieferich branches.",
            ],
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUTPUT.write_bytes(encoded)
    print(json.dumps({"status": "PASS", "output": str(OUTPUT), "sha256": hashlib.sha256(encoded).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
