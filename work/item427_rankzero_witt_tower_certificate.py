#!/usr/bin/env python3
"""Deterministic replay for Item 427's all-level rank-zero Witt tower.

The companion report proves the uniform p-adic determinantal theorem.
This standard-library checker pins Item 424 and the canonical inputs,
reconstructs the exact two-stream p-adic carrier from the archived U,V
integers on every ordinary q=p rank-zero row through m=100, verifies the
all-level digit recursion, and checks the explicitly labelled ambient model.

Finite row counts are never promoted to density statements.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, ROUND_CEILING, getcontext
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item427_rankzero_witt_tower"

DEPENDENCIES = {
    "sources/item424_small_prime_witt_escape_report.md":
        "3a48bafbdd8f1971d5734dfaf7f1553b0d10939d3a93d9feef0cc19f1babe73f",
    "scripts/item424_small_prime_witt_escape_certificate.py":
        "93bb653f6a3a518179a6bc3d66f3c0b8431512d60a89bd1a26c55973e96b5053",
    "results/item424_small_prime_witt_escape_certificate.json":
        "8511bdb52f40a001ecbcf6f3720b473c9d063311a66c8b7ae9ca72808ec879fc",
    "results/item424_small_prime_witt_escape_ledger_delta.json":
        "82118485d8f7e116a72625796843b548e8ce32e2bbff313de0ae81220f5337cb",
    "results/item424_small_prime_witt_escape_root_audit.json":
        "1583de9d74ccf55ea4b44072c0f841dbf5b24705c3213eeb0d004d3ea9fbe1ba",
    "results/item424_small_prime_witt_escape_hashes.sha256":
        "e4f794c7183ab6ef77b11465108e078e381abb4b9df550a108c996929fd00382",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "results/item418_normalized_large_carrier_ledger_delta.json":
        "853301f7014dfde6c5edb0cdc8525ef81fcb3c921d8a777155932f8af651d869",
    "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json":
        "7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def valuation_integer(value: int, prime: int) -> int:
    assert value != 0
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def valuation_fraction(value: Fraction, prime: int) -> int:
    assert value
    return valuation_integer(value.numerator, prime) - valuation_integer(
        value.denominator, prime
    )


def mod_fraction(value: Fraction, prime: int) -> int:
    assert value.denominator % prime
    return (
        value.numerator % prime
        * pow(value.denominator % prime, -1, prime)
        % prime
    )


def padic_digits(value: Fraction, prime: int, count: int) -> list[int]:
    assert valuation_fraction(value, prime) >= 0
    digits: list[int] = []
    remainder = value
    for _ in range(count):
        digit = mod_fraction(remainder, prime)
        digits.append(digit)
        remainder = (remainder - digit) / prime
    return digits


def lcm_through(limit: int) -> int:
    value = 1
    for factor in range(2, limit + 1):
        value = math.lcm(value, factor)
    return value


def cartier_defect(modulus: int, numerator_degree: int, pole_order: int) -> int:
    remainder = numerator_degree % modulus
    target = pole_order % modulus
    if target == 0:
        return 2 * remainder
    return 2 * remainder + 3 * (modulus - target)


def ordinary_rank_zero(m_value: int, prime: int) -> bool:
    return (
        cartier_defect(prime, 6 * m_value, 4 * m_value + 1) <= prime - 2
        and cartier_defect(prime, 6 * m_value, 4 * m_value + 2) <= prime - 2
    )


def top_power(m_value: int, prime: int) -> int:
    bound = 4 * m_value + 1
    if prime > bound:
        return prime
    power = prime
    while power * prime <= bound:
        power *= prime
    return power


def booked_rank_one(m_value: int, prime: int) -> bool:
    if prime == 2 or prime >= 2 * m_value:
        return False
    power = top_power(m_value, prime)
    return (
        cartier_defect(power, 6 * m_value, 4 * m_value + 1)
        <= 2 * power - 2
        and cartier_defect(power, 6 * m_value, 4 * m_value + 2)
        <= 2 * power - 2
    )


def cartier_product(m_value: int) -> int:
    return math.prod(
        prime
        for prime in primes_up_to(6 * m_value)
        if prime != 2 and ordinary_rank_zero(m_value, prime)
    )


def clearing_data(m_value: int) -> tuple[int, int, int]:
    pole_order = 4 * m_value + 1
    middle = math.prod(
        prime
        for prime in primes_up_to(3 * m_value - 1)
        if 2 * m_value < prime < 3 * m_value
    )
    k_value = lcm_through(pole_order) // middle
    d_sharp = 2 ** (9 * m_value + 5) * k_value
    return middle, k_value, d_sharp


def scan_rows() -> dict[int, dict[str, object]]:
    payload = json.loads(
        (ROOT / "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")
        .read_text(encoding="utf-8")
    )
    return {int(row["m"]): row for row in payload["rows"]}


def fraction_record(value: Fraction) -> dict[str, object]:
    encoded = f"{value.numerator}/{value.denominator}".encode("ascii")
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "sha256": sha256_bytes(encoded),
    }


def tower_record(
    m_value: int, prime: int, rows: dict[int, dict[str, object]], digit_count: int = 6
) -> dict[str, object]:
    """Reconstruct the full shifted two-stream Witt carrier from U,V."""
    assert prime != 2
    assert ordinary_rank_zero(m_value, prime)
    assert prime * prime > 4 * m_value + 1

    row = rows[m_value]
    u_value = int(row["U"]["value"])
    v_value = int(row["V"]["value"])
    content = math.gcd(abs(u_value), abs(v_value))
    assert content == int(row["extra_content"])

    g_value = cartier_product(m_value)
    assert g_value == int(row["cartier_product"]["value"])
    assert valuation_integer(g_value, prime) == 1
    _, k_clearing, d_sharp = clearing_data(m_value)
    b_value = (
        valuation_integer(k_clearing, prime) if k_clearing % prime == 0 else 0
    )
    assert b_value in (0, 1)

    # A=UG/D, B=VG/D.  The full first-divided determinants are
    # K=A/p and X=8B/p^2; the anisotropic second minor is J=pX=8B/p.
    kappa_full = Fraction(u_value * g_value, d_sharp * prime)
    xi_full = Fraction(8 * v_value * g_value, d_sharp * prime**2)
    shifted_second = prime * xi_full
    assert valuation_fraction(kappa_full, prime) >= 0
    assert valuation_fraction(xi_full, prime) >= 0

    v_kappa = valuation_fraction(kappa_full, prime)
    v_xi = valuation_fraction(xi_full, prime)
    v_shifted = valuation_fraction(shifted_second, prime)
    assert v_shifted == v_xi + 1

    v_u = valuation_integer(u_value, prime) if u_value % prime == 0 else 0
    v_v = valuation_integer(v_value, prime) if v_value % prime == 0 else 0
    v_c = valuation_integer(content, prime) if content % prime == 0 else 0
    depth = v_c - b_value
    assert depth >= 0
    assert v_u == b_value + v_kappa
    assert v_v == b_value + v_shifted
    assert depth == min(v_kappa, v_shifted)

    count = max(digit_count, depth + 3)
    kappa_digits = padic_digits(kappa_full, prime, count)
    xi_digits = padic_digits(xi_full, prime, count)
    shifted_digits = padic_digits(shifted_second, prime, count + 1)
    assert shifted_digits == [0] + xi_digits[:count]

    for level in range(1, depth + 2):
        digit_gate = (
            all(digit == 0 for digit in kappa_digits[:level])
            and all(digit == 0 for digit in xi_digits[: level - 1])
        )
        assert (depth >= level) == digit_gate

    quotient = (4 * m_value + 1) // prime
    assert quotient % 2 == 0
    j_value = quotient // 2
    s_numerator = (2 * j_value + 1) * prime - (4 * m_value + 1)
    assert s_numerator % 2 == 0
    s_value = s_numerator // 2
    assert 1 <= s_value <= (prime - 3) // 6

    return {
        "m": m_value,
        "p": prime,
        "cell_j": j_value,
        "row_s": s_value,
        "clearing_depth_b": b_value,
        "booked_Item149_member": booked_rank_one(m_value, prime),
        "v_p_U": v_u,
        "v_p_V": v_v,
        "v_p_c": v_c,
        "tower_depth_d_equals_v_p_c_minus_b": depth,
        "v_p_K": v_kappa,
        "v_p_X": v_xi,
        "v_p_pX": v_shifted,
        "K_digits": kappa_digits,
        "X_digits": xi_digits,
        "generating_series_coefficients_K_n_X_n_minus_1": [
            [kappa_digits[index], 0 if index == 0 else xi_digits[index - 1]]
            for index in range(count)
        ],
        "K": fraction_record(kappa_full),
        "X": fraction_record(xi_full),
    }


def finite_census(rows: dict[int, dict[str, object]]) -> dict[str, object]:
    depth_distribution: dict[int, int] = {}
    booked_depth_distribution: dict[int, int] = {}
    layer_counts: dict[int, int] = {}
    booked_layer_counts: dict[int, int] = {}
    stream: list[str] = []

    for m_value in range(1, 101):
        for prime in primes_up_to(6 * m_value):
            if prime == 2 or not ordinary_rank_zero(m_value, prime):
                continue
            if prime * prime <= 4 * m_value + 1:
                continue
            record = tower_record(m_value, prime, rows)
            depth = int(record["tower_depth_d_equals_v_p_c_minus_b"])
            depth_distribution[depth] = depth_distribution.get(depth, 0) + 1
            for level in range(1, depth + 1):
                layer_counts[level] = layer_counts.get(level, 0) + 1
            if record["booked_Item149_member"]:
                assert record["clearing_depth_b"] == 1
                booked_depth_distribution[depth] = (
                    booked_depth_distribution.get(depth, 0) + 1
                )
                for level in range(1, depth + 1):
                    booked_layer_counts[level] = (
                        booked_layer_counts.get(level, 0) + 1
                    )
            stream.append(
                ":".join(
                    str(record[key])
                    for key in (
                        "m",
                        "p",
                        "cell_j",
                        "row_s",
                        "clearing_depth_b",
                        "v_p_U",
                        "v_p_V",
                        "tower_depth_d_equals_v_p_c_minus_b",
                        "v_p_K",
                        "v_p_X",
                    )
                )
            )

    return {
        "range": "1<=m<=100",
        "warning": "exact finite replay only; no density inference",
        "incidence_count": sum(depth_distribution.values()),
        "depth_distribution": {
            str(key): value for key, value in sorted(depth_distribution.items())
        },
        "booked_overlap_depth_distribution": {
            str(key): value
            for key, value in sorted(booked_depth_distribution.items())
        },
        "layer_support_counts": {
            str(key): value for key, value in sorted(layer_counts.items())
        },
        "booked_overlap_layer_support_counts": {
            str(key): value for key, value in sorted(booked_layer_counts.items())
        },
        "stream_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
    }


def ambient_independence() -> dict[str, object]:
    """Check the endpoint-lattice model; this is not an actual-family model."""
    stream: list[str] = []
    for prime in (3, 5, 11):
        for kappa_depth in range(5):
            for xi_depth in range(5):
                kappa_unit = 1 if prime == 3 else 2
                xi_unit = 2 if prime != 3 else 1
                kappa = prime**kappa_depth * kappa_unit
                xi = prime**xi_depth * xi_unit

                # Coordinates are (R,L/p,E).  Recover L=p in both rows.
                row_zero = (0, 1, 0)
                row_one = (-kappa, 1, -prime * xi)
                delta_rl = (
                    row_one[1] * row_zero[0] - row_zero[1] * row_one[0]
                )
                delta_le = (
                    row_one[1] * row_zero[2] - row_zero[1] * row_one[2]
                )
                assert delta_rl == kappa
                assert delta_le == prime * xi
                depth = min(kappa_depth, 1 + xi_depth)
                assert min(
                    valuation_integer(delta_rl, prime),
                    valuation_integer(delta_le, prime),
                ) == depth
                stream.append(
                    f"{prime}:{kappa_depth}:{xi_depth}:{kappa_unit}:"
                    f"{xi_unit}:{depth}"
                )
    return {
        "classification": "AMBIENT ENDPOINT-LATTICE MODEL, NOT ACTUAL FAMILY",
        "symbolic_rows_R_L_over_p_E": ["(0,1,0)", "(-K,1,-pX)"],
        "symbolic_minors": ["Delta_RL=K", "Delta_LE=pX"],
        "conclusion": (
            "K and X, hence all of their p-adic digit streams, are arbitrary "
            "under rank-zero endpoint divisibility alone"
        ),
        "checked_parameter_tuples": len(stream),
        "stream_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
    }


def capacity() -> dict[str, object]:
    getcontext().prec = 80
    item418 = json.loads(
        (ROOT / "results/item418_normalized_large_carrier_ledger_delta.json")
        .read_text(encoding="utf-8")
    )
    outside_large = Decimal(
        item418["admission_residual_outside_this_component"]["decimal"]
    )
    full_layer = Decimal("0.3895079179997942811851475804")
    booked_layer = full_layer - Decimal(1) / Decimal(3)
    return {
        "Item418_outside_large_admission_residual": str(outside_large),
        "per_layer_support_ceilings": {
            "whole_ordinary_rank_zero_support": {
                "exact": "C_F/6",
                "decimal": str(full_layer),
            },
            "booked_overlap": {
                "exact": "(C_F-2)/6",
                "decimal": str(booked_layer),
            },
        },
        "minimum_perfectly_saturated_layers_to_reach_residual": {
            "whole_ordinary_rank_zero_support": int(
                (outside_large / full_layer).to_integral_value(
                    rounding=ROUND_CEILING
                )
            ),
            "booked_overlap_alone": int(
                (outside_large / booked_layer).to_integral_value(
                    rounding=ROUND_CEILING
                )
            ),
        },
        "one_whole_layer_residual": str(outside_large - full_layer),
        "two_whole_layer_optimistic_capacity_minus_residual": str(
            2 * full_layer - outside_large
        ),
        "all_level_warning": (
            "Each layer is supported inside P_m, but without a depth or "
            "weighted-zero theorem the infinite layer cake has no finite "
            "ceiling derived from support alone."
        ),
        "small_component_ceiling_delta": 0,
        "booked_lower_bound_delta": 0,
        "global_total_content_ceiling_delta": 0,
        "frozen_deficit_delta": 0,
    }


def build_payload() -> dict[str, object]:
    dependencies = verify_dependencies()
    rows = scan_rows()
    witnesses = {
        "first_gate_stopped_by_unshifted_X_digit": tower_record(13, 11, rows),
        "X_first_digits_zero_but_next_K_digit_stops": tower_record(24, 11, rows),
        "tower_reaches_depth_two_then_K_digit_stops": tower_record(89, 19, rows),
    }

    first = witnesses["first_gate_stopped_by_unshifted_X_digit"]
    assert first["K_digits"][:2] == [0, 4]
    assert first["X_digits"][0] == 8
    assert first["tower_depth_d_equals_v_p_c_minus_b"] == 1

    second = witnesses["X_first_digits_zero_but_next_K_digit_stops"]
    assert second["K_digits"][:2] == [0, 10]
    assert second["X_digits"][:3] == [0, 0, 8]
    assert second["tower_depth_d_equals_v_p_c_minus_b"] == 1

    third = witnesses["tower_reaches_depth_two_then_K_digit_stops"]
    assert third["K_digits"][:3] == [0, 0, 6]
    assert third["X_digits"][:3] == [0, 0, 12]
    assert third["tower_depth_d_equals_v_p_c_minus_b"] == 2

    return {
        "schema": "item427-rankzero-all-level-witt-tower-v1",
        "item": 427,
        "status": "WORK_ONLY_UNAUDITED_ALL_LEVEL_THEOREM_SCOPED_AMBIENT_NO_GO_NO_BOOKING",
        "dependency_sha256": dependencies,
        "actual_family_all_level_theorem": {
            "scope": "odd p in P_m with p^2>4m+1; omitted q>p support has logarithmic mass o(m)",
            "Bockstein_rows": (
                "Y_s=(R_s,L_s/p,E_s)=(-pR(eta_s),-L(eta_s),-pE(eta_s))"
            ),
            "determinantal_ideal": (
                "I_m,p=(Delta_RL,Delta_LE)=(K,pX)="
                "(A_m/p,8B_m/p) in Z_p"
            ),
            "exact_depth": (
                "v_p(c_m)-b_m,p=v_p(I_m,p)="
                "min(v_p(K),1+v_p(X)), b_m,p=v_p(K_m)"
            ),
            "digit_generating_series": (
                "G_m,p(z)=dig_p(K)(z)e_1+z dig_p(X)(z)e_2; "
                "ord_z G_m,p=v_p(c_m)-b_m,p"
            ),
            "level_n_gate": (
                "depth>=n iff K digits 0..n-1 and X digits 0..n-2 all vanish"
            ),
            "tower_classification": (
                "one forced Jordan delay on the X stream, followed by genuinely "
                "new paired digits; no further resonance follows from the proved hypotheses"
            ),
        },
        "exact_actual_family_witnesses": witnesses,
        "ambient_independence_model": ambient_independence(),
        "capacity": capacity(),
        "finite_replay": finite_census(rows),
        "strict_scope": {
            "proved_actual_family": [
                "one determinantal ideal captures every ordinary rank-zero content depth simultaneously",
                "the shifted two-stream digit recursion and exact level-n gate",
                "the three displayed actual rows showing successive new gates",
                "the layer-cake decomposition and per-layer capacity bounds",
            ],
            "proved_ambient_only": [
                "arbitrary independent K and X digit streams are compatible with rank-zero endpoint divisibility",
            ],
            "open": [
                "an actual-family relation or weighted-density theorem for the paired digit streams",
                "a finite aggregate depth bound",
                "the q>p zero-rate initial-scaling tail as an exact local formula",
                "non-rank-zero small-prime content",
                "Route 1 and irrationality of e+pi",
            ],
        },
    }


def canonical_json(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()

    encoded = canonical_json(build_payload())
    if args.replay is not None:
        assert encoded == args.replay.read_bytes(), "replay differs from pinned certificate"
    args.output.write_bytes(encoded)


if __name__ == "__main__":
    main()
