#!/usr/bin/env python3
"""Deterministic replay for Item 424's first-Witt small-prime bridge.

The uniform statements are proved in the companion report.  This checker
pins the relevant archive inputs, verifies the exact normalization bridge on
all ordinary rank-zero rows with p^2 > 4m+1 through m=100, and independently
reconstructs the three displayed endpoint-error witnesses over Q.

Finite counts are normalization evidence only; no density inference is made.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item424_small_prime_witt_escape"

DEPENDENCIES = {
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md":
        "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md":
        "5e2c92f87075cbe3ac8af3191d8df7485ac6efd13609ede5f82819e355ae5f96",
    "results/item393_mixed_cubic_small_prime_strata_ceiling_ledger.json":
        "a0164b487490dc62449f9f23ea11542c9fe8c557b8d64aa4c1f0e775072ff9b7",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_ledger_delta.json":
        "4a357f5936b4a66fc884171272e614fc55f1a9e23995db1924a20b089bbe629a",
    "sources/item417_mixed_strip_multiplicity_report.md":
        "40397f0f04482162933f129e43e57ca4de4244b06755ba728e19ab551a8b534e",
    "results/item417_mixed_strip_multiplicity_ledger_delta.json":
        "39be69d2d935d3115ff69d64fe642f7cc99626991eb0fafa30bad9c4f95de60d",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_ledger_delta.json":
        "853301f7014dfde6c5edb0cdc8525ef81fcb3c921d8a777155932f8af651d869",
    "sources/witt_endpoint_first_lift.md":
        "08b390b6bcfdaa61c34dc73c582bcbb464d6da4013769775f1eac01a83887424",
    "sources/item421_small_prime_primitive_layer_report.md":
        "5ceb1c8f249f0c62c15cf1db51da7e7dc1247412c10779a731e98e32624bc18c",
    "results/item421_small_prime_primitive_layer_certificate.json":
        "0ddc3480824da0443a149079f9791476f45028c56eb9e776682ea51abc0e2aa5",
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


def normalized_bridge(
    m_value: int, prime: int, rows: dict[int, dict[str, object]]
) -> dict[str, object]:
    """Return the two first-Witt determinant digits from exact U,V data."""
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

    _, k_value, d_sharp = clearing_data(m_value)
    clearing_depth = valuation_integer(k_value, prime) if k_value % prime == 0 else 0
    assert clearing_depth in (0, 1)
    assert u_value % prime**clearing_depth == 0
    assert v_value % prime ** (clearing_depth + 1) == 0

    g_unit = (g_value // prime) % prime
    d_unit = (d_sharp // prime**clearing_depth) % prime
    common_unit = g_unit * pow(d_unit, -1, prime) % prime

    # Since U=D*A/G and V=D*B/G,
    #   A/p = (U/p^b)*(G/p)/(D/p^b),
    #   8B/p^2 = 8*(V/p^(b+1))*(G/p)/(D/p^b).
    kappa = (
        (u_value // prime**clearing_depth) % prime * common_unit
    ) % prime
    xi = (
        8
        * (v_value // prime ** (clearing_depth + 1))
        % prime
        * common_unit
    ) % prime

    content_depth = valuation_integer(content, prime) if content % prime == 0 else 0
    h_member = booked_rank_one(m_value, prime)
    postbooking_depth = content_depth - int(h_member)
    assert postbooking_depth >= 0
    assert (content_depth >= clearing_depth + 1) == (kappa == 0)
    if kappa != 0:
        assert content_depth == clearing_depth
    if kappa == 0 and xi != 0:
        assert content_depth == clearing_depth + 1

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
        "clearing_depth_b": clearing_depth,
        "booked_Item149_member": h_member,
        "v_p_U": valuation_integer(u_value, prime) if u_value % prime == 0 else 0,
        "v_p_V": valuation_integer(v_value, prime) if v_value % prime == 0 else 0,
        "v_p_c": content_depth,
        "postbooking_depth": postbooking_depth,
        "kappa_A_over_p_mod_p": kappa,
        "xi_8B_over_p_squared_mod_p": xi,
        "escape_gate": kappa == 0,
        "xi_stops_at_first_escape_layer": kappa == 0 and xi != 0,
    }


# Exact polynomial/Hermite machinery for the three displayed witnesses.


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


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


def poly_power(poly: list[Fraction], exponent: int) -> list[Fraction]:
    output = [Fraction(1)]
    base = poly[:]
    while exponent:
        if exponent & 1:
            output = poly_mul(output, base)
        exponent >>= 1
        if exponent:
            base = poly_mul(base, base)
    return output


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction(index) * poly[index] for index in range(1, len(poly))] or [
        Fraction()
    ]


def primitive_zero(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction()] + [
        value / Fraction(index + 1) for index, value in enumerate(poly)
    ]


def evaluate(poly: list[Fraction], point: Fraction) -> Fraction:
    output = Fraction()
    for coefficient in reversed(poly):
        output = output * point + coefficient
    return output


Q = [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
Q_PRIME = derivative(Q)
Q_PRIME_INVERSE_MOD_Q = [Fraction(), Fraction(-1, 4), Fraction(1, 4)]
U_POLY = [Fraction(), Fraction(1), Fraction(-1)]


def divmod_q(poly: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    remainder = poly[:]
    quotient = [Fraction()] * max(1, len(remainder) - 3)
    while len(remainder) >= 4:
        shift = len(remainder) - 4
        leading = remainder[-1]
        quotient[shift] = leading
        for index in range(4):
            remainder[shift + index] -= leading
        trim(remainder)
    return trim(quotient), trim(remainder)


def remainder_mod_q(poly: list[Fraction]) -> list[Fraction]:
    return divmod_q(poly)[1]


def mixed_coordinates(
    numerator: list[Fraction], denominator_power: int
) -> tuple[Fraction, Fraction, Fraction]:
    current = numerator[:]
    rational = Fraction()
    for level in range(denominator_power, 1, -1):
        reduced = remainder_mod_q(current)
        primitive = remainder_mod_q(poly_mul(reduced, Q_PRIME_INVERSE_MOD_Q))
        primitive = [-value / Fraction(level - 1) for value in primitive]
        lowered = poly_add(
            current, poly_mul(derivative(primitive), Q), Fraction(-1)
        )
        lowered = poly_add(
            lowered, poly_mul(primitive, Q_PRIME), Fraction(level - 1)
        )
        current, remainder = divmod_q(lowered)
        assert remainder == [0]
        rational += evaluate(primitive, Fraction(1)) / 4 ** (level - 1)
        rational -= evaluate(primitive, Fraction())

    polynomial_part, remainder = divmod_q(current)
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


def mod_fraction(value: Fraction, prime: int) -> int:
    assert value.denominator % prime
    return (
        value.numerator % prime
        * pow(value.denominator % prime, -1, prime)
        % prime
    )


def fraction_record(value: Fraction) -> dict[str, object]:
    encoded = f"{value.numerator}/{value.denominator}".encode("ascii")
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "sha256": sha256_bytes(encoded),
    }


def direct_witt_witness(
    m_value: int, prime: int, rows: dict[int, dict[str, object]]
) -> dict[str, object]:
    n_value = 6 * m_value
    pole_orders = (4 * m_value + 1, 4 * m_value + 2)
    assert ordinary_rank_zero(m_value, prime)
    assert prime * prime > pole_orders[0]

    omega_vectors: list[tuple[Fraction, Fraction, Fraction]] = []
    eta_vectors: list[tuple[Fraction, Fraction, Fraction]] = []
    error_vectors: list[list[int]] = []
    factor_rows: list[dict[str, object]] = []

    for pole_order in pole_orders:
        a_value, r_value = divmod(n_value, prime)
        b_value, t_value = divmod(pole_order, prime)
        if t_value == 0:
            h_value = b_value
            p_poly = poly_power(U_POLY, r_value)
        else:
            h_value = b_value + 1
            p_poly = poly_mul(
                poly_power(U_POLY, r_value), poly_power(Q, prime - t_value)
            )
        assert len(trim(p_poly[:])) - 1 <= prime - 2

        t_poly = primitive_zero(p_poly)
        assert derivative(t_poly) == trim(p_poly[:])

        # eta=F^(p-1) F' T dx, for F=u^a/Q^h.
        logarithmic_numerator = poly_add(
            poly_mul(derivative(U_POLY), Q),
            poly_mul(U_POLY, Q_PRIME),
            Fraction(-h_value, a_value),
        )
        logarithmic_numerator = [
            Fraction(a_value) * value for value in logarithmic_numerator
        ]
        eta_numerator = poly_mul(
            poly_mul(
                poly_power(U_POLY, a_value * prime - 1),
                logarithmic_numerator,
            ),
            t_poly,
        )

        omega = mixed_coordinates(poly_power(U_POLY, n_value), pole_order)
        eta = mixed_coordinates(eta_numerator, h_value * prime + 1)
        omega_vectors.append(omega)
        eta_vectors.append(eta)

        boundary = (
            evaluate(poly_power(U_POLY, a_value * prime), Fraction(1))
            * evaluate(t_poly, Fraction(1))
            - evaluate(poly_power(U_POLY, a_value * prime), Fraction())
            * evaluate(t_poly, Fraction())
        )
        assert boundary == 0
        assert omega[0] == -prime * eta[0]
        assert omega[1] == -prime * eta[1]
        assert omega[2] == -prime * eta[2]

        direct_error = [
            mod_fraction(omega[0], prime),
            mod_fraction(omega[1] / prime, prime),
            mod_fraction(omega[2] / prime, prime),
        ]
        eta_error = [
            (-mod_fraction(prime * eta[0], prime)) % prime,
            (-mod_fraction(eta[1], prime)) % prime,
            (-mod_fraction(eta[2], prime)) % prime,
        ]
        assert direct_error == eta_error
        error_vectors.append(direct_error)
        factor_rows.append(
            {
                "a": a_value,
                "h": h_value,
                "degree_P": len(trim(p_poly[:])) - 1,
                "P_coefficients": [int(value) for value in p_poly],
                "T_coefficient_sha256": sha256_bytes(
                    ",".join(
                        f"{value.numerator}/{value.denominator}" for value in t_poly
                    ).encode("ascii")
                ),
                "boundary": 0,
            }
        )

    kappa = (
        error_vectors[1][1] * error_vectors[0][0]
        - error_vectors[0][1] * error_vectors[1][0]
    ) % prime
    xi = (
        error_vectors[1][1] * error_vectors[0][2]
        - error_vectors[0][1] * error_vectors[1][2]
    ) % prime

    r0, l0, e0 = omega_vectors[0]
    r1, l1, e1 = omega_vectors[1]
    a_form = l1 * r0 - l0 * r1
    b_form = (l1 * e0 - l0 * e1) / 8
    assert kappa == mod_fraction(a_form / prime, prime)
    assert xi == mod_fraction(8 * b_form / prime**2, prime)

    normalized = normalized_bridge(m_value, prime, rows)
    assert normalized["kappa_A_over_p_mod_p"] == kappa
    assert normalized["xi_8B_over_p_squared_mod_p"] == xi

    return {
        "row": {"m": m_value, "p": prime},
        "rank_zero_factors": factor_rows,
        "first_Witt_error_vectors_R_L_over_p_E_over_p": error_vectors,
        "kappa_A_over_p_mod_p": kappa,
        "xi_8B_over_p_squared_mod_p": xi,
        "v_p_A": valuation_fraction(a_form, prime),
        "v_p_B": valuation_fraction(b_form, prime),
        "A": fraction_record(a_form),
        "B": fraction_record(b_form),
        "normalization": normalized,
        "exact_Bockstein_identity": "omega_s=d(F_s^p*T_s)-p*eta_s, with zero endpoint boundary",
    }


def finite_census(rows: dict[int, dict[str, object]]) -> dict[str, object]:
    all_stream: list[str] = []
    booked_stream: list[str] = []
    counts = {
        "ordinary_rank_zero_q_equals_p_incidences": 0,
        "ordinary_rank_zero_escape_gate_vanishes": 0,
        "ordinary_rank_zero_escape_stopped_by_xi": 0,
        "booked_overlap_incidences": 0,
        "booked_overlap_postbooking_escape_gate_vanishes": 0,
        "booked_overlap_escape_stopped_by_xi": 0,
    }
    depth_distribution: dict[str, int] = {}
    first_booked_escape: dict[str, object] | None = None

    for m_value in range(1, 101):
        for prime in primes_up_to(6 * m_value):
            if prime == 2 or not ordinary_rank_zero(m_value, prime):
                continue
            if prime * prime <= 4 * m_value + 1:
                continue
            record = normalized_bridge(m_value, prime, rows)
            counts["ordinary_rank_zero_q_equals_p_incidences"] += 1
            if record["escape_gate"]:
                counts["ordinary_rank_zero_escape_gate_vanishes"] += 1
            if record["xi_stops_at_first_escape_layer"]:
                counts["ordinary_rank_zero_escape_stopped_by_xi"] += 1
            depth_key = str(record["v_p_c"])
            depth_distribution[depth_key] = depth_distribution.get(depth_key, 0) + 1
            all_stream.append(
                ":".join(
                    str(record[key])
                    for key in (
                        "m",
                        "p",
                        "cell_j",
                        "row_s",
                        "clearing_depth_b",
                        "v_p_c",
                        "kappa_A_over_p_mod_p",
                        "xi_8B_over_p_squared_mod_p",
                    )
                )
            )

            if record["booked_Item149_member"]:
                assert record["clearing_depth_b"] == 1
                counts["booked_overlap_incidences"] += 1
                if record["escape_gate"]:
                    counts[
                        "booked_overlap_postbooking_escape_gate_vanishes"
                    ] += 1
                    if first_booked_escape is None:
                        first_booked_escape = record
                if record["xi_stops_at_first_escape_layer"]:
                    counts["booked_overlap_escape_stopped_by_xi"] += 1
                booked_stream.append(all_stream[-1])

    assert first_booked_escape is not None
    return {
        "range": "1<=m<=100",
        "warning": "exact finite normalization only; no density inference",
        "counts": counts,
        "v_p_c_distribution_on_all_rows": dict(
            sorted(depth_distribution.items(), key=lambda item: int(item[0]))
        ),
        "first_booked_escape": first_booked_escape,
        "all_row_stream_sha256": sha256_bytes("\n".join(all_stream).encode("ascii")),
        "booked_row_stream_sha256": sha256_bytes(
            "\n".join(booked_stream).encode("ascii")
        ),
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
    # Pinned canonical Item 415 value, written as a finite certified decimal.
    full_rank_zero_layer = Decimal("0.3895079179997942811851475804")
    booked_overlap_layer = full_rank_zero_layer - Decimal(1) / Decimal(3)
    return {
        "Item418_outside_large_admission_residual": str(outside_large),
        "whole_ordinary_rank_zero_first_Witt_layer": {
            "exact": "C_F/6, C_F=-4log(2)+pi/sqrt(3)+3log(3)",
            "decimal": str(full_rank_zero_layer),
            "residual_even_after_perfect_saturation": str(
                outside_large - full_rank_zero_layer
            ),
        },
        "booked_rank_zero_overlap_first_escape_layer": {
            "exact": "(C_F-2)/6",
            "decimal": str(booked_overlap_layer),
            "residual_even_after_perfect_saturation": str(
                outside_large - booked_overlap_layer
            ),
        },
        "interpretation": (
            "These are support ceilings for one radical/Witt layer, not "
            "proved masses and not bounds for arbitrary deeper valuations."
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
        "Item200_factor_without_content": direct_witt_witness(2, 11, rows),
        "upper_small_prime_escape": direct_witt_witness(9, 47, rows),
        "booked_second_layer_escape": direct_witt_witness(13, 11, rows),
    }

    assert witnesses["Item200_factor_without_content"]["kappa_A_over_p_mod_p"] == 4
    assert witnesses["Item200_factor_without_content"]["v_p_A"] == 1
    assert witnesses["upper_small_prime_escape"]["kappa_A_over_p_mod_p"] == 0
    assert witnesses["upper_small_prime_escape"]["xi_8B_over_p_squared_mod_p"] == 31
    assert witnesses["booked_second_layer_escape"]["kappa_A_over_p_mod_p"] == 0
    assert witnesses["booked_second_layer_escape"]["xi_8B_over_p_squared_mod_p"] == 8
    assert witnesses["booked_second_layer_escape"]["normalization"]["v_p_c"] == 2
    assert witnesses["booked_second_layer_escape"]["normalization"][
        "postbooking_depth"
    ] == 1

    return {
        "schema": "item424-small-prime-first-witt-escape-v1",
        "item": 424,
        "status": "ROOT_AUDITED_CANONICAL_EXACT_BRIDGE_CAPACITY_SCREEN_NO_BOOKING",
        "dependency_sha256": dependencies,
        "theorem_replayed": {
            "scope": (
                "odd ordinary rank-zero primes p with p^2>4m+1; "
                "this contains every positive-rate part of the rank-zero support"
            ),
            "first_error_vector": (
                "W_s=(R_s,L_s/p,E_s/p) mod p="
                "(-pR(eta_s),-L(eta_s),-E(eta_s)) mod p"
            ),
            "eta_definition": (
                "P_s=T_s', eta_s=F_s^(p-1)F_s'T_s dx, and "
                "omega_s=d(F_s^pT_s)-p eta_s"
            ),
            "gate": (
                "with b=v_p(K_m), v_p(c_m)>=b+1 iff "
                "kappa=det((W_0)_{R,L},(W_1)_{R,L})=0 mod p"
            ),
            "stop_digit": (
                "if kappa=0 and xi=det((W_0)_{L,E},(W_1)_{L,E})!=0, "
                "then v_p(c_m)=b+1"
            ),
            "booked_overlap": (
                "on P_m intersect H_m in the q=p range, b=1 and the exact "
                "postbooking escape w_{m,p}>=1 is equivalent to kappa=0"
            ),
        },
        "exact_actual_family_witnesses": witnesses,
        "finite_bridge_census": finite_census(rows),
        "capacity": capacity(),
        "strict_scope": {
            "proved": [
                "a genuine integral first-Witt error vector retaining the rational endpoint error omitted by lambda_s/F_m",
                "the exact mod-p bridge for the first rank-zero escape layer",
                "the exact depth-two classification at (m,p)=(13,11)",
                "support ceilings for one whole rank-zero Witt layer and for its booked overlap",
            ],
            "open": [
                "positive weighted density of kappa-zero rows",
                "an upper bound for multiplicities after kappa vanishes",
                "higher Witt error vectors on the xi-zero subbranch",
                "the non-rank-zero and non-Cartier small-prime remainder",
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
