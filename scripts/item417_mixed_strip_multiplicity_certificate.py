#!/usr/bin/env python3
"""Deterministic certificate for work Item 417.

The uniform arguments are in the companion report.  This replay verifies
the pinned canonical dependencies, reconstructs the exact residue integers,
and checks the squarefree Cartier-zero tower on finite normalization rows.
The finite rows are not used to infer an asymptotic theorem.
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
STEM = "item417_mixed_strip_multiplicity"
MAX_M = 160
SELECTED_M = {2, 5, 6, 9, 17, 30, 60, 100, 140, 160}

DEPENDENCIES = {
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md":
        "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_certificate.json":
        "af731cf70e9a6d40cab380d38d5b404786cefef196eb42f743634b8d390cb29e",
    "manifests/item415_marked_selector_compulsory_strip_manifest.json":
        "8ae673cec3d739af76f3e73eaeb9266868431a77ab9bcaffd72a42cf522780b1",
    "results/item415_marked_selector_compulsory_strip_root_audit.json":
        "123576c914528abdc1e3ffa3993e5161c56f92ac21e4ec33b9c6f450edfa653c",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_certificate.json":
        "bcea1e6be723e48e3d1ca63bc5644b208059e5138799108ea403b0ba5d789075",
    "results/item418_normalized_large_carrier_root_audit.json":
        "530eb0827398480fcff5c8afb564c174d6f9cab8f6be00f5e965ed796eb29c63",
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


ALL_PRIMES = primes_up_to(6 * MAX_M)


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


def cartier_defect(modulus: int, numerator_degree: int, pole_order: int) -> int:
    remainder = numerator_degree % modulus
    target = pole_order % modulus
    if target == 0:
        return 2 * remainder
    return 2 * remainder + 3 * (modulus - target)


def level_is_rank_zero(m_value: int, prime_power: int) -> bool:
    return (
        cartier_defect(prime_power, 6 * m_value, 4 * m_value + 1)
        <= prime_power - 2
        and cartier_defect(prime_power, 6 * m_value, 4 * m_value + 2)
        <= prime_power - 2
    )


def qualifying_levels_for_row(
    m_value: int, prime: int, pole_order: int
) -> list[int]:
    levels: list[int] = []
    prime_power = prime
    while prime_power <= 6 * m_value:
        if (
            cartier_defect(prime_power, 6 * m_value, pole_order)
            <= prime_power - 2
        ):
            levels.append(prime_power)
        prime_power *= prime
    return levels


def qualifying_levels(m_value: int, prime: int) -> list[int]:
    """Levels at which both adjacent rows are simultaneously rank zero."""
    row_zero = set(qualifying_levels_for_row(m_value, prime, 4 * m_value + 1))
    row_one = set(qualifying_levels_for_row(m_value, prime, 4 * m_value + 2))
    return sorted(row_zero & row_one)


def ordinary_forced_primes(m_value: int) -> list[int]:
    return [
        prime for prime in ALL_PRIMES
        if prime > 2 and prime <= 6 * m_value
        and level_is_rank_zero(m_value, prime)
    ]


def tower_primes(
    m_value: int,
) -> tuple[list[int], dict[int, dict[str, list[int]]]]:
    levels: dict[int, dict[str, list[int]]] = {}
    for prime in ALL_PRIMES:
        if prime == 2 or prime > 6 * m_value:
            continue
        row_zero = qualifying_levels_for_row(m_value, prime, 4 * m_value + 1)
        row_one = qualifying_levels_for_row(m_value, prime, 4 * m_value + 2)
        if row_zero and row_one:
            levels[prime] = {
                "row_0": row_zero,
                "row_1": row_one,
                "simultaneous": sorted(set(row_zero) & set(row_one)),
            }
    return sorted(levels), levels


def valuation(value: int, prime: int) -> int:
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def finite_normalization() -> dict[str, object]:
    selected_rows: list[dict[str, object]] = []
    stream: list[str] = []
    ordinary_incidences = 0
    extra_incidences = 0
    extra_exact_one_incidences = 0
    rows_with_extra = 0
    maximum_extra_count = 0

    for m_value in range(1, MAX_M + 1):
        lambda_zero, lambda_one = residue_integers(m_value)
        ordinary = ordinary_forced_primes(m_value)
        tower, level_map = tower_primes(m_value)
        extra = sorted(set(tower) - set(ordinary))
        assert set(ordinary) <= set(tower)
        assert all(prime * prime <= 6 * m_value for prime in extra)

        ordinary_product = product(ordinary)
        extra_product = product(extra)
        tower_product = ordinary_product * extra_product
        assert lambda_zero % tower_product == 0
        assert lambda_one % tower_product == 0

        exact_one = [
            prime for prime in extra
            if min(valuation(lambda_zero, prime), valuation(lambda_one, prime)) == 1
        ]
        ordinary_incidences += len(ordinary)
        extra_incidences += len(extra)
        extra_exact_one_incidences += len(exact_one)
        if extra:
            rows_with_extra += 1
        maximum_extra_count = max(maximum_extra_count, len(extra))

        stream.append(
            ":".join(map(str, (
                m_value,
                lambda_zero,
                lambda_one,
                ordinary_product,
                extra_product,
                ",".join(map(str, extra)),
                ",".join(map(str, exact_one)),
            )))
        )
        if m_value in SELECTED_M:
            selected_rows.append({
                "m": m_value,
                "ordinary_F_primes": ordinary,
                "extra_tower_primes": extra,
                "extra_witness_levels": {
                    str(prime): level_map[prime] for prime in extra
                },
                "extra_exact_one_primes": exact_one,
                "lambda_0_bit_length": abs(lambda_zero).bit_length(),
                "lambda_1_bit_length": abs(lambda_one).bit_length(),
                "tower_divisibility_verified": True,
                "finite_normalization_only": True,
            })

    return {
        "range": f"1<=m<={MAX_M}",
        "rows": MAX_M,
        "ordinary_F_prime_incidences": ordinary_incidences,
        "extra_tower_prime_incidences": extra_incidences,
        "extra_tower_exact_one_incidences": extra_exact_one_incidences,
        "rows_with_extra_tower_factor": rows_with_extra,
        "maximum_extra_prime_count_on_one_row": maximum_extra_count,
        "selected_rows": selected_rows,
        "normalization_stream_sha256": sha256_bytes(
            "\n".join(stream).encode("ascii")
        ),
        "warning": "finite incidence counts and valuation patterns are exact finite diagnostics only",
    }


def exact_counterexamples() -> dict[str, object]:
    rows = []
    for m_value, prime, purpose in (
        (2, 11, "ordinary F_m has exact multiplicity one"),
        (9, 13, "ordinary F_m intersect Item149 rank-one support still has exact multiplicity one"),
        (5, 5, "new higher-level tower factor has exact multiplicity one"),
    ):
        lambda_zero, lambda_one = residue_integers(m_value)
        levels = qualifying_levels(m_value, prime)
        rows.append({
            "m": m_value,
            "p": prime,
            "purpose": purpose,
            "qualifying_prime_power_levels": levels,
            "ordinary_F_member": prime in ordinary_forced_primes(m_value),
            "lambda_0": str(lambda_zero),
            "lambda_1": str(lambda_one),
            "v_p_lambda_0": valuation(lambda_zero, prime),
            "v_p_lambda_1": valuation(lambda_one, prime),
            "lambda_0_over_p_mod_p": lambda_zero // prime % prime,
            "lambda_1_over_p_mod_p": lambda_one // prime % prime,
        })
    assert rows[0]["v_p_lambda_0"] == rows[0]["v_p_lambda_1"] == 1
    assert rows[1]["v_p_lambda_0"] == rows[1]["v_p_lambda_1"] == 1
    assert rows[2]["qualifying_prime_power_levels"] == [25]
    assert rows[2]["ordinary_F_member"] is False
    assert rows[2]["v_p_lambda_0"] == rows[2]["v_p_lambda_1"] == 1
    return {
        "rows": rows,
        "conclusion": (
            "neither the ordinary F factor nor a higher-level rank-zero "
            "Cartier witness supplies a uniform second p-adic digit"
        ),
    }


def capacity_record() -> dict[str, object]:
    getcontext().prec = 60
    pi_value = Decimal(
        "3.14159265358979323846264338327950288419716939937510582097494"
    )
    forced_rate = (
        -Decimal(4) * Decimal(2).ln()
        + pi_value / Decimal(3).sqrt()
        + Decimal(3) * Decimal(3).ln()
    )
    item415_ceiling = (Decimal(136).ln() - forced_rate) / Decimal(6)
    item418_ceiling = Decimal(
        "0.42877388533865786894576038290962190825322503544392"
    )
    return {
        "Item415_strictly_large_component_ceiling": str(item415_ceiling),
        "current_Item418_strictly_large_component_ceiling": str(item418_ceiling),
        "extra_tower_support_bound": "p<=sqrt(6m)",
        "extra_tower_log_bound": "log(E_m)<=sqrt(6m)*log(sqrt(6m))=o(m)",
        "new_strictly_large_component_ceiling": str(item418_ceiling),
        "strictly_large_component_ceiling_delta": 0,
        "booking_delta": 0,
        "global_total_content_ceiling_delta": 0,
        "frozen_deficit_delta": 0,
    }


def build_certificate() -> dict[str, object]:
    dependencies = verify_dependencies()
    finite = finite_normalization()
    counterexamples = exact_counterexamples()
    capacity = capacity_record()
    witness = json.dumps(
        {"finite": finite, "counterexamples": counterexamples, "capacity": capacity},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "schema": "item417-mixed-strip-multiplicity-v1",
        "item": 417,
        "status": "CANONICAL_ROOT_AUDITED_ZERO_ASYMPTOTIC_DELTA",
        "dependency_sha256": dependencies,
        "finite_normalization": finite,
        "exact_counterexamples": counterexamples,
        "capacity": capacity,
        "theorems_proved_in_report": {
            "tower_divisor": (
                "if each adjacent row has some (not necessarily equal) q=p^e "
                "with its defect at most q-2, then p divides both exact "
                "residue integers; F_m times the de-overlapped extra "
                "squarefree tower product divides both coordinates"
            ),
            "thin_extra_support": (
                "every extra tower prime requires e>=2 and hence p<=sqrt(6m), "
                "so its total logarithm is o(m)"
            ),
            "nested_no_go": (
                "Cartier iterates after a zero image remain zero, so multiple "
                "qualifying levels do not constitute independent p-adic digits"
            ),
            "multiplicity_counterexamples": (
                "the actual rows (m,p)=(2,11),(9,13),(5,5) have exact common "
                "valuation one in the declared ordinary/extra cases"
            ),
        },
        "labels": {
            "PROVED": [
                "de-overlapped squarefree all-level Cartier-zero tower divisor",
                "extra support is at most sqrt(6m) and has zero exponential rate",
                "no uniform F_m squared divisibility in the actual family",
                "a higher-level tower witness need not give a second digit",
                "the current Item418 component ceiling and every central ledger quantity are unchanged",
            ],
            "EXACT_FINITE_ONLY": [
                "all incidence counts and valuation histograms through m=160",
            ],
            "OPEN": [
                "any positive-linear-mass higher-multiplicity theorem from an integral lift",
                "additional arithmetic common factors not forced by degree-zero Cartier images",
                "weighted o(m) for the fully normalized large-prime carrier",
                "Route 1 and irrationality of e+pi",
            ],
            "NOT_CLAIMED": [
                "completeness among all possible arithmetic common factors",
                "one p-adic digit for every qualifying Cartier level",
                "positive Route-1 mass or an irrationality proof",
            ],
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=HERE / f"{STEM}_certificate.json"
    )
    parser.add_argument(
        "--replay",
        type=Path,
        help="Optional certificate whose bytes must equal the generated payload.",
    )
    args = parser.parse_args()
    certificate = build_certificate()
    payload = (json.dumps(certificate, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if args.replay is not None:
        assert args.replay.read_bytes() == payload
    args.output.write_bytes(payload)


if __name__ == "__main__":
    main()
