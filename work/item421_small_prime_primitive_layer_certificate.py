#!/usr/bin/env python3
"""Deterministic replay for Item 421's small-prime method boundary.

The uniform conclusions are proved in the companion report.  This script
pins the dependencies, reconstructs the exact residue integers, verifies
three actual-family counterexamples, and checks the stated capacity
arithmetic.  The finite census is normalization evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item421_small_prime_primitive_layer"

DEPENDENCIES = {
    "sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md":
        "5e2c92f87075cbe3ac8af3191d8df7485ac6efd13609ede5f82819e355ae5f96",
    "results/item393_mixed_cubic_small_prime_strata_ceiling_ledger.json":
        "a0164b487490dc62449f9f23ea11542c9fe8c557b8d64aa4c1f0e775072ff9b7",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_ledger_delta.json":
        "4a357f5936b4a66fc884171272e614fc55f1a9e23995db1924a20b089bbe629a",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_ledger_delta.json":
        "853301f7014dfde6c5edb0cdc8525ef81fcb3c921d8a777155932f8af651d869",
    "sources/item417_mixed_strip_multiplicity_report.md":
        "40397f0f04482162933f129e43e57ca4de4244b06755ba728e19ab551a8b534e",
    "results/item417_mixed_strip_multiplicity_certificate.json":
        "11e7046e1f8430ec6961aa0baf9172d75d97c66596fc781849d4722384b03209",
    "manifests/item417_mixed_strip_multiplicity_manifest.json":
        "4dbf5cf3ac5444d22feb6c6e32c01c4f1f08662d0b2e88e5112e8da95f37a147",
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md":
        "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
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
    return [value for value in range(2, limit + 1) if sieve[value]]


def valuation(value: int, prime: int) -> int:
    assert value != 0
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


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
    power = prime
    while power * prime <= 4 * m_value + 1:
        power *= prime
    return power


def booked_rank_one(m_value: int, prime: int) -> bool:
    if prime == 2 or prime >= 2 * m_value:
        return False
    power = top_power(m_value, prime)
    return (
        cartier_defect(power, 6 * m_value, 4 * m_value + 1) <= 2 * power - 2
        and cartier_defect(power, 6 * m_value, 4 * m_value + 2) <= 2 * power - 2
    )


def numerator_zero(m_value: int, degree: int) -> int:
    first = (
        (-1) ** degree * math.comb(6 * m_value, degree)
        if 0 <= degree <= 6 * m_value else 0
    )
    second = (
        (-1) ** (degree - 1) * math.comb(6 * m_value, degree - 1)
        if 1 <= degree <= 6 * m_value + 1 else 0
    )
    return first + second


def numerator_one(m_value: int, degree: int) -> int:
    total = 0
    for shift in range(5):
        source = degree - shift
        if 0 <= source <= 6 * m_value:
            total += (
                math.comb(4, shift)
                * (-1) ** source
                * math.comb(6 * m_value, source)
            )
    return total


def residue_integers(m_value: int) -> tuple[int, int]:
    target_zero = 4 * m_value
    lambda_zero = 0
    for numerator_degree in range(target_zero + 1):
        remainder = target_zero - numerator_degree
        if remainder % 2 == 0:
            half = remainder // 2
            lambda_zero += (
                numerator_zero(m_value, numerator_degree)
                * (-1) ** half
                * math.comb(4 * m_value + half, half)
            )

    target_one = 4 * m_value + 1
    lambda_one = 0
    for numerator_degree in range(target_one + 1):
        remainder = target_one - numerator_degree
        if remainder % 2 == 0:
            half = remainder // 2
            lambda_one += (
                numerator_one(m_value, numerator_degree)
                * (-1) ** half
                * math.comb(4 * m_value + 1 + half, half)
            )
    return lambda_zero, lambda_one


def integer_record(value: int) -> dict[str, object]:
    encoded = str(value).encode("ascii")
    return {
        "value": str(value),
        "digits": len(str(abs(value))),
        "sha256": sha256_bytes(encoded),
    }


def scan_rows() -> dict[int, dict[str, object]]:
    payload = json.loads(
        (ROOT / "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json")
        .read_text(encoding="utf-8")
    )
    return {int(row["m"]): row for row in payload["rows"]}


def row_data(m_value: int, prime: int, rows: dict[int, dict[str, object]]) -> dict[str, object]:
    row = rows[m_value]
    u_value = int(row["U"]["value"])
    v_value = int(row["V"]["value"])
    content = math.gcd(abs(u_value), abs(v_value))
    assert content == int(row["extra_content"])

    f_value = math.prod(
        candidate
        for candidate in primes_up_to(6 * m_value)
        if candidate != 2 and ordinary_rank_zero(m_value, candidate)
    )
    assert f_value == int(row["cartier_product"]["value"])

    lambda_zero, lambda_one = residue_integers(m_value)
    assert lambda_zero % f_value == 0 and lambda_one % f_value == 0
    mu_zero = lambda_zero // f_value
    mu_one = lambda_one // f_value
    f_member = f_value % prime == 0
    h_member = booked_rank_one(m_value, prime)
    residual_depth = valuation(content, prime) - int(h_member)
    mu_depth = min(valuation(mu_zero, prime), valuation(mu_one, prime))
    assert residual_depth >= 0

    return {
        "m": m_value,
        "p": prime,
        "U": integer_record(u_value),
        "V": integer_record(v_value),
        "c": integer_record(content),
        "F": integer_record(f_value),
        "lambda_0": integer_record(lambda_zero),
        "lambda_1": integer_record(lambda_one),
        "mu_0": integer_record(mu_zero),
        "mu_1": integer_record(mu_one),
        "ordinary_Item200_member": f_member,
        "booked_Item149_member": h_member,
        "top_denominator_power": top_power(m_value, prime),
        "ordinary_defects": [
            cartier_defect(prime, 6 * m_value, 4 * m_value + 1),
            cartier_defect(prime, 6 * m_value, 4 * m_value + 2),
        ],
        "v_p_c": valuation(content, prime),
        "post_booking_depth": residual_depth,
        "v_p_lambda": [valuation(lambda_zero, prime), valuation(lambda_one, prime)],
        "v_p_mu": [valuation(mu_zero, prime), valuation(mu_one, prime)],
        "normalized_carrier_depth": mu_depth,
    }


def finite_census(rows: dict[int, dict[str, object]]) -> dict[str, object]:
    escape_stream: list[str] = []
    f_not_content_stream: list[str] = []
    escape_by_zone: dict[str, int] = {}
    maximum_escape_gap = 0

    for m_value in range(1, 101):
        row = rows[m_value]
        u_value = int(row["U"]["value"])
        v_value = int(row["V"]["value"])
        content = math.gcd(abs(u_value), abs(v_value))
        f_value = int(row["cartier_product"]["value"])
        lambda_zero, lambda_one = residue_integers(m_value)
        assert lambda_zero % f_value == 0 and lambda_one % f_value == 0
        mu_zero, mu_one = lambda_zero // f_value, lambda_one // f_value

        for prime in primes_up_to(6 * m_value):
            if prime == 2:
                continue
            f_member = f_value % prime == 0
            h_member = booked_rank_one(m_value, prime)
            content_depth = valuation(content, prime) if content % prime == 0 else 0
            mu_depth = min(
                valuation(mu_zero, prime) if mu_zero % prime == 0 else 0,
                valuation(mu_one, prime) if mu_one % prime == 0 else 0,
            )
            residual_depth = content_depth - int(h_member)
            assert residual_depth >= 0

            if f_member and content_depth == 0:
                f_not_content_stream.append(f"{m_value}:{prime}")
            if residual_depth > mu_depth:
                zone = ("F" if f_member else "notF") + "_" + (
                    "H" if h_member else "notH"
                )
                escape_by_zone[zone] = escape_by_zone.get(zone, 0) + 1
                maximum_escape_gap = max(
                    maximum_escape_gap, residual_depth - mu_depth
                )
                escape_stream.append(
                    f"{m_value}:{prime}:{content_depth}:{int(h_member)}:"
                    f"{int(f_member)}:{residual_depth}:{mu_depth}"
                )

    return {
        "range": "1<=m<=100",
        "warning": "exact finite normalization only; no density inference",
        "F_prime_incidences_absent_from_content": len(f_not_content_stream),
        "F_not_content_stream_sha256": sha256_bytes(
            "\n".join(f_not_content_stream).encode("ascii")
        ),
        "postbooking_depth_exceeds_mu_depth_incidences": len(escape_stream),
        "escape_by_zone": dict(sorted(escape_by_zone.items())),
        "maximum_observed_escape_gap": maximum_escape_gap,
        "escape_stream_sha256": sha256_bytes(
            "\n".join(escape_stream).encode("ascii")
        ),
    }


def abstract_lift_check() -> dict[str, object]:
    checked: list[dict[str, int]] = []
    for prime in (3, 5, 11, 47):
        for depth in range(1, 7):
            # Coordinate order is (R,L,E).  Both pairs have the same
            # nonzero proportional reduction mod p, while the two target
            # minors have the prescribed arbitrary valuation.
            row_zero = (1, 1, 1)
            row_one = (1 + prime ** depth, 1, 1 + prime ** depth)
            rational_minor = row_one[1] * row_zero[0] - row_zero[1] * row_one[0]
            pi_minor = row_one[1] * row_zero[2] - row_zero[1] * row_one[2]
            assert valuation(rational_minor, prime) == depth
            assert valuation(pi_minor, prime) == depth
            assert tuple(value % prime for value in row_zero) == tuple(
                value % prime for value in row_one
            )
            checked.append({"p": prime, "depth": depth})
    return {
        "model": "(R,L,E)_0=(1,1,1), (R,L,E)_1=(1+p^r,1,1+p^r)",
        "conclusion": "the same characteristic-p rank-one datum is compatible with arbitrary common determinant valuation r",
        "checked_pairs": len(checked),
        "checked_sha256": sha256_bytes(
            "\n".join(f"{row['p']}:{row['depth']}" for row in checked).encode("ascii")
        ),
    }


def capacity() -> dict[str, object]:
    getcontext().prec = 80
    item393 = json.loads(
        (ROOT / "results/item393_mixed_cubic_small_prime_strata_ceiling_ledger.json")
        .read_text(encoding="utf-8")
    )
    item418 = json.loads(
        (ROOT / "results/item418_normalized_large_carrier_ledger_delta.json")
        .read_text(encoding="utf-8")
    )
    residual = Decimal(
        item418["admission_residual_outside_this_component"]["decimal"]
    )
    clearing_layer = Decimal(2) / Decimal(3)
    full_layer = Decimal(1)
    cutoff = Decimal(6) * residual
    return {
        "current_safe_small_remainder_ceiling": item393["ceilings"][
            "small_remainder_explicit_safe"
        ],
        "Item418_admission_residual": str(residual),
        "one_full_postbooking_layer_capacity": str(full_layer),
        "one_p_le_4m_layer_capacity": str(clearing_layer),
        "p_le_4m_layer_excess_over_residual": str(clearing_layer - residual),
        "full_layer_excess_over_residual": str(full_layer - residual),
        "squarefree_cutoff_alpha_required_for_alpha_m_support": str(cutoff),
        "cutoff_statement": "a bare squarefree support ceiling p<=alpha*m is admission-decisive only if alpha<6*Item418_residual",
        "Item417_extra_tower_support": "p<=sqrt(6m), hence logarithmic capacity o(m)",
        "small_component_ceiling_delta": 0,
        "booked_lower_bound_delta": 0,
        "global_total_content_ceiling_delta": 0,
        "frozen_deficit_delta": 0,
    }


def build_payload() -> dict[str, object]:
    dependencies = verify_dependencies()
    rows = scan_rows()
    witness_f_not_c = row_data(2, 11, rows)
    witness_upper = row_data(9, 47, rows)
    witness_postbook = row_data(13, 11, rows)

    assert witness_f_not_c["ordinary_Item200_member"]
    assert witness_f_not_c["v_p_c"] == 0
    assert witness_upper["ordinary_Item200_member"]
    assert not witness_upper["booked_Item149_member"]
    assert witness_upper["post_booking_depth"] == 1
    assert witness_upper["normalized_carrier_depth"] == 0
    assert witness_postbook["ordinary_Item200_member"]
    assert witness_postbook["booked_Item149_member"]
    assert witness_postbook["v_p_c"] == 2
    assert witness_postbook["post_booking_depth"] == 1
    assert witness_postbook["normalized_carrier_depth"] == 0

    item417 = json.loads(
        (ROOT / "results/item417_mixed_strip_multiplicity_certificate.json")
        .read_text(encoding="utf-8")
    )
    assert item417["capacity"]["extra_tower_support_bound"] == "p<=sqrt(6m)"

    return {
        "schema": "item421-small-prime-primitive-layer-v1",
        "item": 421,
        "status": "ROOT_AUDITED_CANONICAL_SCOPED_METHOD_NO_GO_NO_BOOKING",
        "dependency_sha256": dependencies,
        "exact_actual_family_witnesses": {
            "Item200_factor_not_content_factor": witness_f_not_c,
            "upper_strip_normalized_carrier_escape": witness_upper,
            "postbooking_second_layer_normalized_carrier_escape": witness_postbook,
        },
        "finite_normalization": finite_census(rows),
        "abstract_characteristic_p_lift_freedom": abstract_lift_check(),
        "inherited_Item417_all_level_boundary": {
            "extra_tower_support_bound": item417["capacity"][
                "extra_tower_support_bound"
            ],
            "extra_tower_log_bound": item417["capacity"][
                "extra_tower_log_bound"
            ],
            "nested_no_go": item417["theorems_proved_in_report"][
                "nested_no_go"
            ],
            "multiplicity_counterexamples": item417["theorems_proved_in_report"][
                "multiplicity_counterexamples"
            ],
        },
        "capacity": capacity(),
        "strict_scope": {
            "closed": [
                "subtracting Item200 F_m from the post-G_m content c_m as an exact divisor",
                "extending Item415's mu-pair all-depth carrier identity from p>6m to every p<=6m",
                "obtaining positive linear mass or a multiplicity bound from the all-level degree-zero Cartier tower alone",
                "treating a full p<=4m squarefree/lcm layer as small enough for the current outside-large admission residual",
            ],
            "open": [
                "a genuine integral Witt/Dwork endpoint carrier for post-booking small-prime depths",
                "a weighted support theorem below the alpha cutoff or a cancellation-aware joint carrier",
                "a quantitative upper bound for the complete p<=6m primitive remainder",
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
