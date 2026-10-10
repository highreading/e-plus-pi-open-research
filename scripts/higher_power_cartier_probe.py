#!/usr/bin/env python3
"""Exact finite probe for higher powers in the actual mixed-cubic content.

This script uses only the Python standard library.  Its primary inputs are
the frozen exact U_m,V_m data for 1 <= m <= 100 and the frozen valuation
maps for m=150,200.  It also reads the archived rank-two Cartier certificate.

The output is a finite diagnostic.  In particular, an observed equality of
valuations is labelled EXPERIMENTAL and is never promoted to a theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("valuation(0) is not used in this probe")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def lcm_exponent(limit: int, prime: int) -> int:
    exponent = 0
    power = prime
    while power <= limit:
        exponent += 1
        power *= prime
    return exponent


def d_value(n_value: int, power: int, modulus: int) -> int:
    remainder_n = n_value % modulus
    remainder_k = power % modulus
    if remainder_k == 0:
        return 2 * remainder_n
    return 2 * remainder_n + 3 * (modulus - remainder_k)


def rank_one_rows(m_value: int) -> list[dict[str, Any]]:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    rows: list[dict[str, Any]] = []
    for prime in primes_upto(2 * m_value - 1):
        if prime == 2:
            continue
        exponent = lcm_exponent(power, prime)
        layer = prime**exponent
        d0 = d_value(n_value, power, layer)
        d1 = d_value(n_value, power + 1, layer)
        if d0 <= 2 * layer - 2 and d1 <= 2 * layer - 2:
            first_d0 = d_value(n_value, power, prime)
            first_d1 = d_value(n_value, power + 1, prime)
            rows.append(
                {
                    "p": prime,
                    "e": exponent,
                    "q": layer,
                    "d0": d0,
                    "d1": d1,
                    "rank_zero_at_first_cartier": (
                        first_d0 <= prime - 2 and first_d1 <= prime - 2
                    ),
                }
            )
    return rows


def factor_over_bound(value: int, bound: int) -> tuple[dict[int, int], int]:
    remainder = abs(value)
    factors: dict[int, int] = {}
    for prime in primes_upto(bound):
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
    return factors, remainder


def beta_pairs(maximum_n: int) -> list[tuple[int, int]]:
    pairs = [(1, 1), (3, 1)]
    for index in range(2, maximum_n + 1):
        p0, q0 = pairs[-2]
        p1, q1 = pairs[-1]
        multiplier = 4 * index - 2
        pairs.append((multiplier * p1 + p0, multiplier * q1 + q0))
    return pairs[: maximum_n + 1]


def synchronization_values(
    a_value: int,
    b_value: int,
    epsilon: int,
    p_beta: int,
    q_beta: int,
) -> tuple[int, int]:
    delta = math.gcd(b_value, q_beta)
    b0 = b_value // delta
    q0 = q_beta // delta
    p_star = b0 * p_beta - epsilon * q0 * a_value
    return delta, math.gcd(abs(p_star), delta)


# The following exact Hermite code is an independent standard-library replay
# of the archived normalization on a small prefix.


def trim(polynomial: list[Fraction]) -> list[Fraction]:
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def poly_add(
    left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)
) -> list[Fraction]:
    output = [Fraction()] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += scale * value
    return trim(output)


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction()] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return trim(output)


def poly_derivative(polynomial: list[Fraction]) -> list[Fraction]:
    return [
        Fraction(index) * polynomial[index] for index in range(1, len(polynomial))
    ] or [Fraction()]


def mixed_divmod_q(
    polynomial: list[Fraction],
) -> tuple[list[Fraction], list[Fraction]]:
    remainder = polynomial[:]
    quotient = [Fraction()] * max(1, len(remainder) - 3)
    while len(remainder) >= 4:
        shift = len(remainder) - 4
        leading = remainder[-1]
        quotient[shift] = leading
        for index in range(4):
            remainder[shift + index] -= leading
        trim(remainder)
    return trim(quotient), trim(remainder)


def mixed_remainder(polynomial: list[Fraction]) -> list[Fraction]:
    return mixed_divmod_q(polynomial)[1]


def poly_evaluate(polynomial: list[Fraction], value: Fraction) -> Fraction:
    output = Fraction()
    for coefficient in reversed(polynomial):
        output = output * value + coefficient
    return output


MIXED_Q = [Fraction(1)] * 4
MIXED_Q_PRIME = [Fraction(1), Fraction(2), Fraction(3)]
MIXED_Q_PRIME_INVERSE = [Fraction(), Fraction(-1, 4), Fraction(1, 4)]


def mixed_coordinates(
    n_value: int, power: int
) -> tuple[Fraction, Fraction, Fraction]:
    numerator = [Fraction()] * n_value + [
        Fraction((-1) ** offset * math.comb(n_value, offset))
        for offset in range(n_value + 1)
    ]
    rational = Fraction()
    for level in range(power, 1, -1):
        reduced = mixed_remainder(numerator)
        primitive = mixed_remainder(poly_mul(reduced, MIXED_Q_PRIME_INVERSE))
        primitive = [-value / Fraction(level - 1) for value in primitive]
        lowered = poly_add(
            numerator, poly_mul(poly_derivative(primitive), MIXED_Q), Fraction(-1)
        )
        lowered = poly_add(
            lowered,
            poly_mul(primitive, MIXED_Q_PRIME),
            Fraction(level - 1),
        )
        numerator, remainder = mixed_divmod_q(lowered)
        if remainder != [0]:
            raise AssertionError((n_value, power, level, remainder))
        rational += poly_evaluate(primitive, Fraction(1)) / 4 ** (level - 1)
        rational -= poly_evaluate(primitive, Fraction())
    polynomial_part, remainder = mixed_divmod_q(numerator)
    rational += sum(
        (
            coefficient / Fraction(index + 1)
            for index, coefficient in enumerate(polynomial_part)
        ),
        Fraction(),
    )
    remainder += [Fraction()] * (3 - len(remainder))
    a_value, b_value, c_value = remainder[:3]
    return rational, a_value - b_value + 3 * c_value, a_value + b_value - c_value


def lcm_upto(limit: int) -> int:
    result = 1
    for value in range(2, limit + 1):
        result = math.lcm(result, value)
    return result


def cartier_product(m_value: int) -> int:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    result = 1
    for prime in primes_upto(n_value):
        if prime == 2:
            continue
        if (
            d_value(n_value, power, prime) <= prime - 2
            and d_value(n_value, power + 1, prime) <= prime - 2
        ):
            result *= prime
    return result


def exact_pi_pair(m_value: int) -> tuple[int, int, int]:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    r0, l0, e0 = mixed_coordinates(n_value, power)
    r1, l1, e1 = mixed_coordinates(n_value, power + 1)
    a_form = l1 * r0 - l0 * r1
    b_form = (l1 * e0 - l0 * e1) / 8
    middle_product = math.prod(
        prime
        for prime in primes_upto(3 * m_value - 1)
        if 2 * m_value < prime < 3 * m_value
    )
    clearing = 2 ** (9 * m_value + 5) * lcm_upto(power) // middle_product
    x_value = clearing * a_form
    y_value = clearing * b_form
    if x_value.denominator != 1 or y_value.denominator != 1:
        raise AssertionError((m_value, "nonintegral clearing"))
    common_cartier = cartier_product(m_value)
    if x_value.numerator % common_cartier or y_value.numerator % common_cartier:
        raise AssertionError((m_value, "Cartier divisor"))
    u_value = x_value.numerator // common_cartier
    v_value = y_value.numerator // common_cartier
    return u_value, v_value, math.gcd(abs(u_value), abs(v_value))


def digest_matches(value: int, record: dict[str, Any]) -> bool:
    return hashlib.sha256(str(value).encode("ascii")).hexdigest() == record["sha256"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--recompute-through", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    results = args.archive / "results"
    scan_path = results / "mixed_cubic_positive_match_exact_scan_m100_N6m.json"
    probe_paths = [
        results / "mixed_cubic_content_factor_m150.json",
        results / "mixed_cubic_content_factor_m200.json",
    ]
    rank_two_path = results / "mixed_cubic_rank_two_cartier_certificate.json"

    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    full_records: dict[int, dict[str, Any]] = {}
    digest_failures: list[dict[str, Any]] = []
    for row in scan["rows"]:
        m_value = int(row["m"])
        u_value = int(row["U"]["value"])
        v_value = int(row["V"]["value"])
        content = int(row["extra_content"])
        if not digest_matches(u_value, row["U"]):
            digest_failures.append({"m": m_value, "field": "U"})
        if not digest_matches(v_value, row["V"]):
            digest_failures.append({"m": m_value, "field": "V"})
        if math.gcd(abs(u_value), abs(v_value)) != content:
            digest_failures.append({"m": m_value, "field": "gcd"})
        full_records[m_value] = {
            "u": u_value,
            "v": v_value,
            "content": content,
            "row": row,
        }

    valuation_records: dict[int, dict[str, Any]] = {}
    for path in probe_paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for row in data["rows"]:
            valuation_records[int(row["m"])] = {
                "content": int(row["content"]),
                "vp_map": {
                    int(prime): tuple(map(int, pair))
                    for prime, pair in row[
                        "vp_u_minus_vp_cartier_for_small_primes"
                    ].items()
                },
                "content_factors": {
                    int(prime): int(exponent)
                    for prime, exponent in row["factors_at_most_bound"].items()
                },
                "cofactor": int(row["cofactor"]),
            }

    recomputation_rows = []
    for m_value in range(1, min(args.recompute_through, 100) + 1):
        recomputed = exact_pi_pair(m_value)
        frozen = full_records[m_value]
        agrees = recomputed == (frozen["u"], frozen["v"], frozen["content"])
        recomputation_rows.append({"m": m_value, "agrees": agrees})
        if not agrees:
            raise AssertionError((m_value, recomputed))

    factor_rows: dict[int, dict[int, int]] = {}
    support_failures = []
    for m_value, record in full_records.items():
        factors, remainder = factor_over_bound(record["content"], 6 * m_value)
        factor_rows[m_value] = factors
        if remainder != 1:
            support_failures.append({"m": m_value, "remainder": str(remainder)})
    for m_value, record in valuation_records.items():
        factor_rows[m_value] = record["content_factors"]
        if record["cofactor"] != 1:
            support_failures.append(
                {"m": m_value, "remainder": str(record["cofactor"])}
            )

    def local_pair(m_value: int, prime: int) -> tuple[int, int]:
        if m_value in full_records:
            record = full_records[m_value]
            return valuation(record["u"], prime), valuation(record["v"], prime)
        return valuation_records[m_value]["vp_map"].get(prime, (0, 0))

    rank_one_audit = []
    normalization_cache: dict[int, tuple[int, int, int]] = {}
    for m_value in sorted(full_records | valuation_records):
        for row in rank_one_rows(m_value):
            prime = int(row["p"])
            vp_u, vp_v = local_pair(m_value, prime)
            vp_c = min(vp_u, vp_v)
            lift_digit_u = None
            normalized_qA_lift_digit = None
            if m_value in full_records:
                u_value = int(full_records[m_value]["u"])
                lift_digit_u = (u_value // prime) % prime
                if m_value not in normalization_cache:
                    power = 4 * m_value + 1
                    middle_product = math.prod(
                        test_prime
                        for test_prime in primes_upto(3 * m_value - 1)
                        if 2 * m_value < test_prime < 3 * m_value
                    )
                    clearing = (
                        2 ** (9 * m_value + 5)
                        * lcm_upto(power)
                        // middle_product
                    )
                    normalization_cache[m_value] = (
                        clearing,
                        cartier_product(m_value),
                        power,
                    )
                clearing, common_cartier, _ = normalization_cache[m_value]
                delta = 1 if bool(row["rank_zero_at_first_cartier"]) else 0
                clearing_unit = (clearing // int(row["q"])) % prime
                cartier_unit = (common_cartier // (prime**delta)) % prime
                normalized_qA_lift_digit = (
                    lift_digit_u
                    * cartier_unit
                    * pow(clearing_unit, -1, prime)
                ) % prime
            rank_one_audit.append(
                row
                | {
                    "m": m_value,
                    "vp_u": vp_u,
                    "vp_v": vp_v,
                    "vp_c": vp_c,
                    "proved_bounds_hold": vp_u >= 1 and vp_v >= int(row["e"]) + 1,
                    "second_digit_present": vp_c >= 2,
                    "difference_equals_lcm_exponent": vp_v - vp_u == int(row["e"]),
                    "U_over_p_mod_p": lift_digit_u,
                    "normalized_qA_over_first_forced_power_mod_p": (
                        normalized_qA_lift_digit
                    ),
                }
            )

    rank_two = json.loads(rank_two_path.read_text(encoding="utf-8"))
    rank_two_audit = []
    for index_row in rank_two["index_rows"]:
        m_value = int(index_row["m"])
        for row in index_row["vanishing_rank_two_rows"]:
            vp_u = int(row["vp_u"])
            vp_v = int(row["vp_v"])
            exponent = int(row["denominator_exponent"])
            rank_two_audit.append(
                {
                    "m": m_value,
                    "p": int(row["p"]),
                    "e": exponent,
                    "vp_u": vp_u,
                    "vp_v": vp_v,
                    "vp_c": min(vp_u, vp_v),
                    "rank_zero_at_first_cartier": bool(
                        row["rank_zero_at_first_cartier"]
                    ),
                    "ray_labels": row["ray_labels"],
                    "second_digit_present": min(vp_u, vp_v) >= 2,
                    "difference_equals_lcm_exponent": vp_v - vp_u == exponent,
                }
            )

    raw_equal_failures = []
    raw_equal_test_count = 0
    raw_equal_common_count = 0
    primitive_pattern_failures = []
    common_prime_rows = []
    for m_value in sorted(full_records | valuation_records):
        power = 4 * m_value + 1
        for prime in primes_upto(power):
            if prime == 2:
                continue
            vp_u, vp_v = local_pair(m_value, prime)
            exponent = lcm_exponent(power, prime)
            raw_equal_test_count += 1
            if vp_v - vp_u != exponent:
                raw_equal_failures.append(
                    {
                        "m": m_value,
                        "p": prime,
                        "e": exponent,
                        "vp_u": vp_u,
                        "vp_v": vp_v,
                    }
                )
            vp_c = min(vp_u, vp_v)
            if vp_c:
                raw_equal_common_count += 1
                primitive_u = vp_u - vp_c
                primitive_v = vp_v - vp_c
                common_prime_rows.append(
                    {
                        "m": m_value,
                        "p": prime,
                        "e": exponent,
                        "vp_c": vp_c,
                        "vp_primitive_u": primitive_u,
                        "vp_primitive_v": primitive_v,
                    }
                )
                if primitive_u != 0 or primitive_v != exponent:
                    primitive_pattern_failures.append(common_prime_rows[-1])

    # Check the exact primitive (a,b) and the two synchronization records that
    # are actually serialized for every m in the m<=100 scan.
    beta = beta_pairs(600)
    synchronization_checks = []
    primitive_coordinate_failures = []
    for m_value, record in full_records.items():
        row = record["row"]
        content = record["content"]
        stored_a = int(row["primitive_positive_form"]["a"])
        stored_b = int(row["primitive_positive_form"]["b"])
        epsilon = int(row["epsilon"])
        if abs(stored_a) != abs(record["u"] // content):
            primitive_coordinate_failures.append({"m": m_value, "field": "a"})
        if stored_b != abs(record["v"] // content):
            primitive_coordinate_failures.append({"m": m_value, "field": "b"})
        for label in ("minimum_positive_match", "maximum_total_content_in_window"):
            selected = row[label]
            index = int(selected["N"])
            delta, g_value = synchronization_values(
                stored_a, stored_b, epsilon, *beta[index]
            )
            synchronization_checks.append(
                {
                    "m": m_value,
                    "record": label,
                    "N": index,
                    "delta_agrees": delta == int(selected["delta"]),
                    "g_agrees": g_value == int(selected["final_content"]),
                }
            )

    lifted_by_prime: dict[int, dict[str, Any]] = {}
    for row in rank_one_audit:
        prime = int(row["p"])
        stats = lifted_by_prime.setdefault(
            prime,
            {
                "p": prime,
                "incidences": 0,
                "second_digit_incidences": 0,
                "second_digit_m_residues_mod_p": set(),
                "sharp_m_residues_mod_p": set(),
            },
        )
        stats["incidences"] += 1
        if row["second_digit_present"]:
            stats["second_digit_incidences"] += 1
            stats["second_digit_m_residues_mod_p"].add(int(row["m"]) % prime)
        else:
            stats["sharp_m_residues_mod_p"].add(int(row["m"]) % prime)
    residue_diagnostics = []
    for prime in sorted(lifted_by_prime):
        stats = lifted_by_prime[prime]
        if stats["incidences"] >= 4:
            residue_diagnostics.append(
                stats
                | {
                    "second_digit_m_residues_mod_p": sorted(
                        stats["second_digit_m_residues_mod_p"]
                    ),
                    "sharp_m_residues_mod_p": sorted(stats["sharp_m_residues_mod_p"]),
                }
            )

    # A concrete Hensel-style pattern search.  Group rows with the same
    # (p,e,m mod q,rank-zero) residual labels and test whether the normalized
    # next digit is affine in t=floor(m/q).  No invariance is assumed.
    affine_groups = []
    grouped_digits: dict[tuple[int, int, int, bool], list[tuple[int, int, int]]] = {}
    for row in rank_one_audit:
        if int(row["m"]) > 100:
            continue
        digit = row["normalized_qA_over_first_forced_power_mod_p"]
        if digit is None:
            continue
        prime = int(row["p"])
        layer = int(row["q"])
        m_value = int(row["m"])
        key = (
            prime,
            int(row["e"]),
            m_value % layer,
            bool(row["rank_zero_at_first_cartier"]),
        )
        grouped_digits.setdefault(key, []).append(
            (m_value // layer, int(digit), m_value)
        )
    for key, points in sorted(grouped_digits.items()):
        prime, exponent, residue, rank_zero = key
        if len(points) < 3:
            continue
        distinct: dict[int, int] = {}
        consistent = True
        for t_value, digit, _ in points:
            reduced_t = t_value % prime
            if reduced_t in distinct and distinct[reduced_t] != digit:
                consistent = False
            distinct[reduced_t] = digit
        affine = False
        slope = None
        intercept = None
        if consistent and len(distinct) >= 2:
            items = sorted(distinct.items())
            t0, y0 = items[0]
            t1, y1 = items[1]
            slope = ((y1 - y0) * pow((t1 - t0) % prime, -1, prime)) % prime
            intercept = (y0 - slope * t0) % prime
            affine = all(
                (slope * t_value + intercept) % prime == digit
                for t_value, digit in items
            )
        affine_groups.append(
            {
                "p": prime,
                "e": exponent,
                "m_mod_q": residue,
                "rank_zero": rank_zero,
                "point_count": len(points),
                "distinct_t_mod_p_count": len(distinct),
                "affine_mod_p": affine,
                "slope": slope if affine else None,
                "intercept": intercept if affine else None,
                "points_t_digit_m": points,
            }
        )

    rank_one_second = [row for row in rank_one_audit if row["second_digit_present"]]
    rank_one_sharp = [row for row in rank_one_audit if not row["second_digit_present"]]
    rank_one_m100 = [row for row in rank_one_audit if int(row["m"]) <= 100]
    rank_one_m100_second = [row for row in rank_one_m100 if row["second_digit_present"]]
    rank_one_m100_sharp = [row for row in rank_one_m100 if not row["second_digit_present"]]
    rank_two_second = [row for row in rank_two_audit if row["second_digit_present"]]
    rank_two_sharp = [row for row in rank_two_audit if not row["second_digit_present"]]
    rank_two_m100 = [row for row in rank_two_audit if int(row["m"]) <= 100]
    rank_two_m100_second = [row for row in rank_two_m100 if row["second_digit_present"]]
    rank_two_m100_sharp = [row for row in rank_two_m100 if not row["second_digit_present"]]
    all_content_incidences = sum(len(factors) for factors in factor_rows.values())
    higher_content_incidences = sum(
        1 for factors in factor_rows.values() for exponent in factors.values() if exponent >= 2
    )

    def value_distribution(rows: list[dict[str, Any]]) -> dict[str, int]:
        distribution: dict[str, int] = {}
        for row in rows:
            key = str(int(row["vp_c"]))
            distribution[key] = distribution.get(key, 0) + 1
        return dict(sorted(distribution.items(), key=lambda item: int(item[0])))

    payload = {
        "schema": "higher-power-cartier-actual-coordinates-v1",
        "warning": "Finite exact diagnostic only; experimental equalities are not theorems.",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": sha256(Path(__file__)),
        },
        "inputs": [
            {"filename": path.name, "sha256": sha256(path)}
            for path in [scan_path, *probe_paths, rank_two_path]
        ],
        "scope": {
            "full_exact_U_V_indices": sorted(full_records),
            "valuation_only_indices": sorted(valuation_records),
            "independent_Hermite_recomputation_through_m": min(
                args.recompute_through, 100
            ),
        },
        "proved_or_exactly_replayed": {
            "all_stored_integer_digests_and_gcds_pass": not digest_failures,
            "digest_or_gcd_failures": digest_failures,
            "all_independent_Hermite_recomputations_pass": all(
                row["agrees"] for row in recomputation_rows
            ),
            "Hermite_recomputation_rows": recomputation_rows,
            "all_content_factorizations_close_over_primes_at_most_6m": not support_failures,
            "support_failures": support_failures,
            "rank_one_proved_bounds_hold_on_every_frozen_incidence": all(
                row["proved_bounds_hold"] for row in rank_one_audit
            ),
            "rank_two_archived_rows_replayed": len(rank_two_audit),
            "primitive_coordinates_match_U_over_c_and_V_over_c": not primitive_coordinate_failures,
            "primitive_coordinate_failures": primitive_coordinate_failures,
            "serialized_Delta_g_records_recompute_exactly": all(
                row["delta_agrees"] and row["g_agrees"]
                for row in synchronization_checks
            ),
            "serialized_Delta_g_record_count": len(synchronization_checks),
        },
        "experimental_actual_coordinate_pattern": {
            "candidate_statement_tested_and_refuted": (
                "The tempting equality v_p(V_m)-v_p(U_m)="
                "v_p(lcm(1,...,4m+1)), equivalently equality of the two "
                "reconstructed raw valuations, fails on the frozen grid."
            ),
            "tested_prime_index_pairs": raw_equal_test_count,
            "failure_count": len(raw_equal_failures),
            "failures": raw_equal_failures[:20],
            "common_odd_prime_incidences": raw_equal_common_count,
            "candidate_primitive_consequence_also_refuted": (
                "The consequent candidate that every tested odd common prime "
                "leaves a p-unit primitive U-coordinate and lcm-exponent "
                "primitive V-coordinate also fails."
            ),
            "primitive_consequence_failure_count": len(primitive_pattern_failures),
            "primitive_consequence_failures": primitive_pattern_failures[:20],
            "status": "REFUTED AS A UNIVERSAL PATTERN BY EXACT FINITE DATA",
        },
        "rank_one_higher_power_summary": {
            "incidence_count": len(rank_one_audit),
            "vp_c_exactly_one_count": len(rank_one_sharp),
            "vp_c_at_least_two_count": len(rank_one_second),
            "difference_equals_e_count": sum(
                bool(row["difference_equals_lcm_exponent"]) for row in rank_one_audit
            ),
            "universal_p_squared_lift_is_refuted_by_frozen_actual_rows": bool(
                rank_one_sharp
            ),
            "first_sharp_examples": rank_one_sharp[:12],
            "first_lifted_examples": rank_one_second[:12],
            "m_1_to_100_census": {
                "incidence_count": len(rank_one_m100),
                "vp_c_exactly_one_count": len(rank_one_m100_sharp),
                "vp_c_at_least_two_count": len(rank_one_m100_second),
                "vp_c_distribution": value_distribution(rank_one_m100),
                "rank_zero_distribution": value_distribution(
                    [row for row in rank_one_m100 if row["rank_zero_at_first_cartier"]]
                ),
                "non_rank_zero_distribution": value_distribution(
                    [row for row in rank_one_m100 if not row["rank_zero_at_first_cartier"]]
                ),
                "large_prime_lifts_p_at_least_29": [
                    row
                    for row in rank_one_m100_second
                    if int(row["p"]) >= 29
                ],
            },
            "proved_single_coordinate_lift_criterion": (
                "For p in H_m, the proved v_p(V_m)>=e_p+1 implies "
                "p^2|c_m iff p^2|U_m.  If delta is 1 when p is in the "
                "rank-zero Cartier product and 0 otherwise, then exactly "
                "v_p(U_m)=v_p(q_p A_m)-delta, so the criterion is "
                "q_p A_m=0 mod p^(2+delta)."
            ),
            "normalized_next_digit_affine_search": {
                "grouping": "fixed (p,e,m mod q,rank-zero), at least three frozen m values",
                "group_count": len(affine_groups),
                "affine_group_count": sum(
                    bool(group["affine_mod_p"]) for group in affine_groups
                ),
                "groups": affine_groups,
                "status": (
                    "FINITE PATTERN SEARCH: the affine guess fails in all but "
                    "the reported exceptional group; no conjecture is asserted"
                ),
            },
            "fixed_prime_residue_diagnostics": residue_diagnostics,
        },
        "rank_two_higher_power_summary": {
            "vanishing_incidence_count": len(rank_two_audit),
            "vp_c_exactly_one_count": len(rank_two_sharp),
            "vp_c_at_least_two_count": len(rank_two_second),
            "difference_equals_e_count": sum(
                bool(row["difference_equals_lcm_exponent"]) for row in rank_two_audit
            ),
            "universal_p_squared_lift_is_refuted_by_frozen_actual_rows": bool(
                rank_two_sharp
            ),
            "first_sharp_examples": rank_two_sharp[:12],
            "first_lifted_examples": rank_two_second[:12],
            "m_1_to_100_census": {
                "vanishing_incidence_count": len(rank_two_m100),
                "vp_c_exactly_one_count": len(rank_two_m100_sharp),
                "vp_c_at_least_two_count": len(rank_two_m100_second),
                "vp_c_distribution": value_distribution(rank_two_m100),
            },
        },
        "all_actual_content_factor_summary": {
            "prime_incidences": all_content_incidences,
            "prime_incidences_with_exponent_at_least_two": higher_content_incidences,
            "per_index_factorizations": [
                {
                    "m": m_value,
                    "factors": {str(p): e for p, e in sorted(factor_rows[m_value].items())},
                }
                for m_value in sorted(factor_rows)
            ],
        },
        "data_availability_for_Delta_and_g": {
            "exact_statement": (
                "The m<=100 scan serializes exact primitive a_m,b_m and exact "
                "Delta_m,g_m only for two selected N values per m.  The exact "
                "primitive coordinates and beta recurrence suffice to recompute "
                "Delta,g for any other finite N, but those candidate ledgers are "
                "not individually serialized in the scan."
            ),
            "selected_record_checks": synchronization_checks,
        },
        "open_barrier": (
            "The data refute an automatic p^2 lift on both the rank-one and "
            "rank-two Cartier sets.  The experimental raw equal-valuation law "
            "organizes the observed powers but does not predict v_p(U_m), hence "
            "does not itself supply a second digit or an exponential excess-mass bound."
        ),
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "rank_one_m_1_to_100": payload["rank_one_higher_power_summary"][
                    "m_1_to_100_census"
                ]
                | {"large_prime_lifts_p_at_least_29": "see JSON"},
                "rank_two_m_1_to_100": payload["rank_two_higher_power_summary"][
                    "m_1_to_100_census"
                ],
                "affine_groups_passing": sum(
                    bool(group["affine_mod_p"]) for group in affine_groups
                ),
                "affine_groups_tested": len(affine_groups),
                "raw_equal_valuation_candidate_failures": len(raw_equal_failures),
                "output_sha256": hashlib.sha256(encoded).hexdigest(),
            },
            indent=2,
            default=str,
        )
    )


if __name__ == "__main__":
    main()
