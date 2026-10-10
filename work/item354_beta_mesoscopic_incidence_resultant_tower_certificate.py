#!/usr/bin/env python3
"""Deterministic exact replay for Item 354.

The replay verifies declared incidence/resultant, layer-cake, matching,
height, and squarefull-separation controls.  Declared carrier rows are
finite algebraic controls, not actual Item-316 targets and not census data.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "sources/item265_beta_squarefull_capacity_report.md": (
        "c41d8d2c813d4952ce5a038f291b932817c28ae5b0b1512df0a6bf0ba92a8daa"
    ),
    "results/item265_beta_squarefull_capacity_certificate.json": (
        "42548c5127392c6475be7440a883b378657d15d762fc1f165d8b3e546ce9c32c"
    ),
    "results/item265_root_audit.json": (
        "72e5f43c554e326d101d1b2c55de76f277a5a817eaa6b0fc2837dd8f6bbee24a"
    ),
    "manifests/item265_beta_squarefull_capacity_manifest.json": (
        "8bc1b3087300865dc6a54300a262cfa62c50f1b8031494dc362e87ecc18a6063"
    ),
    "sources/item343_beta_quotient_radical_excess_capacity_report.md": (
        "0fb48e3bbf30d05bcf40d2e4dc9b04e2e80893e6c4fee925d9c6b99b25126c66"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_certificate.json": (
        "c700ffaa6898bd50e4d6b790dea307ec883ecab6374e07a7c62622eb5ba7d57b"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_root_audit.json": (
        "1788b3f5247b132c8ea8f8133d64d9fadcd716013b041964be46b7c71c9747e4"
    ),
    "manifests/item343_beta_quotient_radical_excess_capacity_manifest.json": (
        "eddaff62ba519ece9bac2c881b04b0a0ec3f5dc5d06d780ac03a4b0b7dc69439"
    ),
    "sources/item346_beta_t_avoiding_radical_localization_report.md": (
        "2ad742c14d0adbc74da6c46394ed89f68cec8888a3c9d22ee4f230a4e16548a5"
    ),
    "results/item346_beta_t_avoiding_radical_localization_certificate.json": (
        "29a20d6ede62db23658d66db8e57af4a2982c9b66fd12d104f0070b3280aefab"
    ),
    "results/item346_beta_t_avoiding_radical_localization_root_audit.json": (
        "c9273d7e187ee2c9b4b91bffc65769f1a29f937613c36960e4ed5871c5782089"
    ),
    "manifests/item346_beta_t_avoiding_radical_localization_manifest.json": (
        "5029cf3483fdf6cce4bbc0d454bca362bb2796104ca36b353d0161e374915530"
    ),
    "sources/item350_beta_mesoscopic_first_hit_crt_no_go_report.md": (
        "a028d87765b16bf921a219e43314c8020b635e052cf3a653a9213389d81ce532"
    ),
    "scripts/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.py": (
        "ae4be8e7e4675a30efe01cc1e7e40d57e63bd49590c34aaf9f8c97996038073f"
    ),
    "results/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.json": (
        "9c30d1c23b741e0e5b7e38ab39b16658f225f9846894b8a2b657bfa4eb145950"
    ),
    "results/item350_beta_mesoscopic_first_hit_crt_no_go_root_audit.json": (
        "e965a5131ebc4ff9a54b7ae8369b2855e562ebfa9190517817b7d2fd2af7e162"
    ),
    "manifests/item350_beta_mesoscopic_first_hit_crt_no_go_manifest.json": (
        "19e6e4ab0dfe99b7e6587e66006caa99bd39c368c574fec69762d1aee5cc3b21"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    archive_root = Path(__file__).resolve().parent.parent
    rows: list[dict[str, Any]] = []
    for relative_path, expected_hash in DEPENDENCY_HASHES.items():
        path = archive_root / relative_path
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        assert actual_hash == expected_hash, (
            relative_path,
            actual_hash,
            expected_hash,
        )
        rows.append(
            {
                "path": relative_path,
                "bytes": len(payload),
                "sha256": actual_hash,
            }
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def radical(value: int) -> int:
    result = 1
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result *= prime
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result *= remaining
    return result


def gcd_many(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, value)
    return result


def build_q(exponents: dict[int, int]) -> int:
    return math.prod(prime**exponent for prime, exponent in exponents.items())


def declared_patterns() -> list[dict[str, Any]]:
    return [
        {
            "name": "mixed_cliques_and_squarefull_split",
            "A": 50,
            "t": 2,
            "q_exponents": {53: 1, 59: 2, 61: 1, 67: 3, 71: 1},
            "row_carriers": [1, 53, 59, 61, 59, 67, 67, 1, 67, 71, 61],
        },
        {
            "name": "singleton_blind_spot",
            "A": 20,
            "t": 2,
            "q_exponents": {23: 1, 29: 1, 31: 1, 37: 1, 41: 1, 43: 1},
            "row_carriers": [23, 1, 29, 31, 37, 1, 41, 43],
        },
        {
            "name": "squarefree_doubleton_full_pair_layer",
            "A": 50,
            "t": 2,
            "q_exponents": {53: 1, 59: 1, 61: 1, 67: 1},
            "row_carriers": [53, 59, 61, 67, 53, 59, 61, 67],
        },
    ]


def verify_pattern(pattern: dict[str, Any]) -> dict[str, Any]:
    name = pattern["name"]
    A = pattern["A"]
    t = pattern["t"]
    q_exponents = pattern["q_exponents"]
    rows = pattern["row_carriers"]
    Q = build_q(q_exponents)

    for prime, exponent in q_exponents.items():
        assert is_prime(prime) and exponent >= 1
    for carrier in rows:
        if carrier == 1:
            continue
        assert is_prime(carrier)
        assert A < carrier < A * A
        assert Q % carrier == 0
        assert math.gcd(carrier, t) == 1

    multiplicities = Counter(carrier for carrier in rows if carrier > 1)
    active_count = sum(multiplicities.values())
    support_primes = sorted(multiplicities)
    R_1 = math.prod(support_primes)

    previous_lcm = 1
    first_hit_factors: list[int] = []
    for carrier in rows:
        factor = carrier // math.gcd(carrier, previous_lcm)
        first_hit_factors.append(factor)
        previous_lcm = math.lcm(previous_lcm, carrier)
    assert math.prod(first_hit_factors) == R_1 == previous_lcm
    for left, right in combinations(first_hit_factors, 2):
        assert math.gcd(left, right) == 1

    row_product = math.prod(rows)
    resultant_rows: list[dict[str, Any]] = []
    R_layers: list[int] = []
    for order in range(1, active_count + 1):
        aggregate_gcd_product = math.prod(
            gcd_many(tuple(rows[index] for index in subset))
            for subset in combinations(range(len(rows)), order)
        )
        formula_product = math.prod(
            prime ** math.comb(multiplicity, order)
            for prime, multiplicity in multiplicities.items()
            if multiplicity >= order
        )
        assert aggregate_gcd_product == formula_product
        radical_layer = math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity >= order
        )
        assert radical(aggregate_gcd_product) == radical_layer
        assert radical_layer**order <= row_product < A ** (2 * active_count)
        R_layers.append(radical_layer)
        resultant_rows.append(
            {
                "r": order,
                "G_r": str(aggregate_gcd_product),
                "R_r": str(radical_layer),
                "formula_verified": True,
                "exact_integer_height_check": (
                    f"R_r^r<={row_product}<A^(2N_A)"
                ),
            }
        )
    assert math.prod(R_layers) == row_product
    for index in range(len(R_layers) - 1):
        assert R_layers[index] % R_layers[index + 1] == 0

    selected_pairs: list[tuple[int, int]] = []
    pair_product = 1
    for prime in support_primes:
        locations = [index for index, carrier in enumerate(rows) if carrier == prime]
        if len(locations) >= 2:
            selected_pairs.append((locations[0], locations[1]))
            pair_product *= math.gcd(rows[locations[0]], rows[locations[1]])
    flattened = [index for pair in selected_pairs for index in pair]
    assert len(flattened) == len(set(flattened))
    R_2 = math.prod(
        prime for prime, multiplicity in multiplicities.items() if multiplicity >= 2
    )
    assert pair_product == R_2

    q_radical = radical(Q)
    excess = Q // q_radical
    powerful_supported_radical = math.prod(
        prime for prime, exponent in q_exponents.items() if exponent >= 2
    )
    assert excess % powerful_supported_radical == 0

    threshold_rows: list[dict[str, Any]] = []
    for threshold in sorted({2, 3, active_count + 1}):
        low_fresh = math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity < threshold and q_exponents[prime] == 1
        )
        high_fresh = math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity >= threshold and q_exponents[prime] == 1
        )
        active_powerful = math.prod(
            prime
            for prime in support_primes
            if q_exponents[prime] >= 2
        )
        assert R_1 == low_fresh * high_fresh * active_powerful
        assert excess % active_powerful == 0
        assert high_fresh**threshold <= row_product
        threshold_rows.append(
            {
                "L": threshold,
                "S_less_L_fresh": str(low_fresh),
                "R_L_fresh": str(high_fresh),
                "active_powerful_radical": str(active_powerful),
                "support_partition_verified": True,
                "squarefull_deoverlap_verified": True,
            }
        )

    return {
        "name": name,
        "A": A,
        "Q": str(Q),
        "E_Q": str(excess),
        "t": t,
        "row_count": len(rows),
        "active_count": active_count,
        "exact_zero_or_inactive_rows": rows.count(1),
        "row_carriers": rows,
        "multiplicities": {str(prime): multiplicities[prime] for prime in support_primes},
        "R_1": str(R_1),
        "R_2": str(R_2),
        "first_hit_factors": first_hit_factors,
        "first_hit_factors_digest": digest(first_hit_factors),
        "resultant_rows": resultant_rows,
        "resultant_rows_digest": digest(resultant_rows),
        "layer_cake_verified": True,
        "disjoint_pair_matching": selected_pairs,
        "disjoint_pair_matching_product": str(pair_product),
        "threshold_rows": threshold_rows,
        "threshold_rows_digest": digest(threshold_rows),
        "finite_algebraic_control_only": True,
        "actual_item316_target_claim": False,
        "density_claim": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "actual_input": (
            "After exact-zero omission and t-avoidance, each mesoscopic row "
            "carrier C_j is 1 or one prime A<p<A^2 dividing Q."
        ),
        "tower": (
            "If nu_p counts actual row incidences, the aggregate r-wise gcd "
            "product is product_p p^binom(nu_p,r), and its radical is R_r."
        ),
        "layer_cake": (
            "The first-hit product is R_1 and product_j C_j=product_r R_r."
        ),
        "capacity": (
            "R_r^r divides the row product, which is below A^(2N_A); hence "
            "log R_r<2N_A log A/r. The r=2 ceiling remains one full copy."
        ),
        "growing_threshold": (
            "R_1=S_<L R_L. Therefore Xi_Q=o(log b) iff some L(n)->infinity "
            "makes the actual low-incidence carrier S_<L zero rate."
        ),
        "squarefull_separation": (
            "The radical supported on v_p(Q)>=2 divides E(Q)=Q/rad(Q); the "
            "fresh missing statistic is low-incidence support with v_p(Q)=1."
        ),
        "scope": (
            "Declared controls are not actual targets. No theorem forcing or "
            "excluding actual singleton/doubleton configurations is claimed."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    patterns = [verify_pattern(pattern) for pattern in declared_patterns()]
    proof = proof_object()
    return {
        "schema": "item354-beta-mesoscopic-incidence-resultant-tower-certificate-v1",
        "item": 354,
        "date": "2026-09-01",
        "status": "PROVED_INCIDENCE_RESULTANT_TOWER_LOW_MULTIPLICITY_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "actual_incidence_clique_identity": "PROVED",
            "first_hit_product_equals_R_1": "PROVED",
            "complete_r_wise_gcd_resultant_tower": "PROVED",
            "layer_cake_product_identity": "PROVED",
            "multiplicity_layer_height_bound": "PROVED",
            "pairwise_layer_full_one_copy_ceiling": "PROVED",
            "growing_low_incidence_equivalence": "PROVED",
            "squarefull_deoverlap_inequality": "PROVED",
            "actual_low_incidence_weighted_bound": "OPEN",
            "actual_Xi_Q": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            "patterns": patterns,
            "patterns_digest": digest(patterns),
            "pattern_count": len(patterns),
            "finite_rows_promoted": False,
            "prime_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "first_occurrence_claim_from_item350_formal_CRT": False,
            "closes": [
                "pairwise gcds of first-hit factors as a source of new information",
                "the complete pairwise shared-support carrier as a zero-rate theorem",
                "every fixed order r>=2 specialized common-divisor hierarchy by itself",
            ],
            "isolates": [
                "actual low-incidence squarefree support at a growing threshold",
                "the old Item265 excess carrier E(Q)",
            ],
            "does_not_close": [
                "the actual low-incidence statistic or Xi_Q",
                "squarefull excess, H_Q, K_Q, or Gamma_Q",
                "the half-bound, beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_Xi_Q_maximum": "log rad(Q)<=log Q<=log b",
            "pairwise_R_2_ceiling": "N_A log A=(1+o(1))log b",
            "R_r_ceiling": "2N_A log A/r",
            "growing_high_multiplicity_tail_rate": 0,
            "actual_low_incidence_rate": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item354_beta_mesoscopic_incidence_resultant_tower_certificate.json",
    )
    args = parser.parse_args()
    result = build_certificate()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path(__file__).resolve().parent.parent / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "actual_Xi_Q": "OPEN",
                "booking": 0,
                "item": 354,
                "remaining_input": "ACTUAL_GROWING_LOW_INCIDENCE_SQUAREFREE_MASS",
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
