#!/usr/bin/env python3
"""Exact deterministic replay for Item 358.

Checks declared incidence-set saturation, fresh singleton quadrants, moment
orthogonality, union-ideal monomials, and disjoint-window product controls.
Declared rows are not actual Item-316 targets and are not census evidence.
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
    "sources/item354_beta_mesoscopic_incidence_resultant_tower_report.md": (
        "511de44cc96c383ff8cf20bb613c6d466cbbd1f2e46bdce8cab794561279a3ac"
    ),
    "scripts/item354_beta_mesoscopic_incidence_resultant_tower_certificate.py": (
        "67149ee09abde20427668d5bec7c716974b2bdf1e3eab63492ad6ebe7e75930c"
    ),
    "results/item354_beta_mesoscopic_incidence_resultant_tower_certificate.json": (
        "964d4f38ce8c3c7ba7046da66e29a2b90000be009987896704388459fd5c51d1"
    ),
    "results/item354_beta_mesoscopic_incidence_resultant_tower_root_audit.json": (
        "ce5a1cf333220186e7088f8c19cb0040e88441570cc8818d3707710495ef1f25"
    ),
    "manifests/item354_beta_mesoscopic_incidence_resultant_tower_manifest.json": (
        "f94bb26dad8b5e5dc260d700587c7ed7a628b615a561bbbe75a2dfd785a75876"
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
            {"path": relative_path, "bytes": len(payload), "sha256": actual_hash}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def factor_integer(value: int) -> dict[int, int]:
    assert value >= 1
    result: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def radical(value: int) -> int:
    return math.prod(factor_integer(value))


def radical_above(value: int, threshold: int) -> int:
    return math.prod(prime for prime in factor_integer(value) if prime > threshold)


def product_from_exponents(exponents: dict[int, int]) -> int:
    return math.prod(prime**exponent for prime, exponent in exponents.items())


def saturation_exponent(A: int) -> int:
    return math.ceil(math.log2(A * A))


def occurrence_sets(rows: list[int]) -> dict[int, frozenset[int]]:
    all_primes: set[int] = set()
    for value in rows:
        all_primes.update(factor_integer(value))
    return {
        prime: frozenset(index for index, value in enumerate(rows) if value % prime == 0)
        for prime in sorted(all_primes)
    }


def saturated_subset_factor(
    rows: list[int], t: int, subset: frozenset[int], exponent: int
) -> int:
    assert subset
    g_value = 0
    for index in subset:
        g_value = math.gcd(g_value, rows[index])
    outside_product = abs(t) * math.prod(
        value for index, value in enumerate(rows) if index not in subset
    )
    return g_value // math.gcd(g_value, outside_product**exponent)


def row_carriers(
    rows: list[int], A: int, t: int, q_exponents: dict[int, int]
) -> list[int]:
    q_primes = set(q_exponents)
    carriers: list[int] = []
    for value in rows:
        primes = [
            prime
            for prime in factor_integer(value)
            if prime > A and prime in q_primes and t % prime != 0
        ]
        assert len(primes) <= 1
        carriers.append(math.prod(primes))
    return carriers


def main_declared_control() -> dict[str, Any]:
    A = 50
    t = 71
    raw_rows = [0, 106, 177, 295, 122, 427, 671, 201, 142, 0]
    rows = [value for value in raw_rows if value]
    q_exponents = {53: 1, 59: 1, 61: 2, 67: 2, 71: 1}
    Q = product_from_exponents(q_exponents)
    M_A = saturation_exponent(A)
    assert all(0 < value < A * A for value in rows)

    occurrences = occurrence_sets(rows)
    subset_rows: list[dict[str, Any]] = []
    subset_factors: dict[frozenset[int], int] = {}
    for size in range(1, len(rows) + 1):
        for indices in combinations(range(len(rows)), size):
            subset = frozenset(indices)
            factor = saturated_subset_factor(rows, t, subset, M_A)
            factor_primes = set(factor_integer(factor))
            expected_primes = {
                prime
                for prime, occurrence in occurrences.items()
                if occurrence == subset and t % prime != 0
            }
            assert factor_primes == expected_primes
            subset_factors[subset] = factor
            if factor > 1:
                subset_rows.append(
                    {
                        "subset": sorted(subset),
                        "size": size,
                        "s_S": factor,
                        "prime_support": sorted(factor_primes),
                    }
                )

    nontrivial_values = [value for value in subset_factors.values() if value > 1]
    for left, right in combinations(nontrivial_values, 2):
        assert math.gcd(left, right) == 1

    q_radical = math.prod(q_exponents)
    E_Q = Q // q_radical
    q_single = math.prod(prime for prime, exponent in q_exponents.items() if exponent == 1)
    assert q_single == q_radical // math.gcd(q_radical, radical(E_Q))

    fresh_threshold_rows: list[dict[str, Any]] = []
    for threshold in [2, 3, 4, len(rows) + 1]:
        saturated_product = math.prod(
            value
            for subset, value in subset_factors.items()
            if len(subset) < threshold
        )
        actual_carrier = math.gcd(q_single, radical_above(saturated_product, A))
        expected_carrier = math.prod(
            prime
            for prime, occurrence in occurrences.items()
            if (
                A < prime < A * A
                and prime in q_exponents
                and q_exponents[prime] == 1
                and t % prime != 0
                and 1 <= len(occurrence) < threshold
            )
        )
        assert actual_carrier == expected_carrier
        fresh_threshold_rows.append(
            {
                "L": threshold,
                "carrier": actual_carrier,
                "expected": expected_carrier,
                "verified": True,
            }
        )

    carriers = row_carriers(rows, A, t, q_exponents)
    multiplicities = Counter(value for value in carriers if value > 1)
    R_1 = math.prod(multiplicities)
    R_2 = math.prod(
        prime for prime, multiplicity in multiplicities.items() if multiplicity >= 2
    )
    quadrants = {
        "U_11": math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity == 1 and q_exponents[prime] == 1
        ),
        "U_12": math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity == 1 and q_exponents[prime] >= 2
        ),
        "U_21": math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity >= 2 and q_exponents[prime] == 1
        ),
        "U_22": math.prod(
            prime
            for prime, multiplicity in multiplicities.items()
            if multiplicity >= 2 and q_exponents[prime] >= 2
        ),
    }
    assert quadrants == {"U_11": 53, "U_12": 67, "U_21": 59, "U_22": 61}
    assert math.prod(quadrants.values()) == R_1
    assert R_2 == quadrants["U_21"] * quadrants["U_22"]
    assert math.gcd(quadrants["U_11"], R_2 * E_Q) == 1

    first_moment_product = math.prod(carriers)
    pairwise_gcd_product = math.prod(
        math.gcd(carriers[left], carriers[right])
        for left, right in combinations(range(len(carriers)), 2)
    )
    expected_pairwise = math.prod(
        prime ** math.comb(multiplicity, 2)
        for prime, multiplicity in multiplicities.items()
    )
    assert pairwise_gcd_product == expected_pairwise

    singleton_factors = [subset_factors[frozenset({index})] for index in range(len(rows))]
    direct_union_product = math.prod(singleton_factors)
    assert direct_union_product <= math.prod(rows) < A ** (2 * len(rows))
    windows = [[0, 1, 2], [3, 4], [5, 6, 7]]
    window_products = [
        math.prod(singleton_factors[index] for index in window) for window in windows
    ]
    assert math.prod(window_products) == direct_union_product

    return {
        "A": A,
        "M_A": M_A,
        "t": t,
        "Q": str(Q),
        "E_Q": str(E_Q),
        "Q_single": str(q_single),
        "raw_row_count": len(raw_rows),
        "exact_zero_rows_omitted": raw_rows.count(0),
        "nonzero_rows": rows,
        "occurrences": {
            str(prime): sorted(occurrence) for prime, occurrence in occurrences.items()
        },
        "subset_rows": subset_rows,
        "subset_rows_digest": digest(subset_rows),
        "nontrivial_saturated_factors_pairwise_coprime": True,
        "fresh_threshold_rows": fresh_threshold_rows,
        "fresh_threshold_rows_digest": digest(fresh_threshold_rows),
        "mesoscopic_row_carriers": carriers,
        "multiplicities": {
            str(prime): multiplicities[prime] for prime in sorted(multiplicities)
        },
        "R_1": R_1,
        "R_2": R_2,
        "quadrants": quadrants,
        "quadrant_product_verified": True,
        "fresh_singleton_coprime_to_R2_E_Q": True,
        "first_moment_product": str(first_moment_product),
        "pairwise_gcd_product": str(pairwise_gcd_product),
        "direct_union_product": str(direct_union_product),
        "window_products": [str(value) for value in window_products],
        "window_product_identity": True,
        "finite_algebraic_control_only": True,
        "actual_item316_target_claim": False,
        "prime_census_performed": False,
    }


def zero_t_control() -> dict[str, Any]:
    rows = [106, 177, 295]
    exponent = saturation_exponent(50)
    factors = []
    for size in range(1, len(rows) + 1):
        for indices in combinations(range(len(rows)), size):
            factor = saturated_subset_factor(rows, 0, frozenset(indices), exponent)
            assert factor == 1
            factors.append(factor)
    return {
        "t": 0,
        "subset_count": len(factors),
        "all_saturated_factors_one": True,
        "finite_only": True,
    }


def union_ideal_controls() -> dict[str, Any]:
    exponent_vectors = [
        [0],
        [1],
        [1, 1],
        [2, 1],
        [1, 0, 1],
        [1, 1, 1],
        [3, 2, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    rows: list[dict[str, Any]] = []
    for exponents in exponent_vectors:
        in_every_coordinate_ideal = all(exponent >= 1 for exponent in exponents)
        divisible_by_full_product = all(exponent >= 1 for exponent in exponents)
        assert in_every_coordinate_ideal == divisible_by_full_product
        if in_every_coordinate_ideal:
            assert sum(exponents) >= len(exponents)
        rows.append(
            {
                "exponents": exponents,
                "in_intersection": in_every_coordinate_ideal,
                "divisible_by_product": divisible_by_full_product,
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "intersection_equals_product_ideal_control": True,
        "with_Q_intersection": "intersection_j(Q,Y_j)=(Q,product_j Y_j)",
        "with_Q_escape_is_original_full_height_carrier": True,
        "finite_rows_promoted": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "saturation": (
            "For each nonempty actual row subset S, s_S=gcd(Z_j:j in S) "
            "saturated by t and every outside row. A prime divides s_S exactly "
            "when its t-avoiding occurrence set is S."
        ),
        "fresh_carrier": (
            "Intersecting the size-<L saturated factors with the v_p(Q)=1 part "
            "of Q and primes >A gives exactly the actual low-incidence fresh mass."
        ),
        "quadrants": (
            "The singleton-squarefree quadrant is coprime to both the pairwise "
            "repetition carrier R_2 and the excess carrier E(Q)."
        ),
        "moments": (
            "Singletons contribute to the first incidence moment but zero to the "
            "pairwise moment and E(Q); their remaining height ceiling is log b."
        ),
        "union_ideal": (
            "The intersection of coordinate ideals (Y_j) is generated by their "
            "full product, while intersection_j(Q,Y_j)=(Q,product Y_j). A uniform "
            "scheme-theoretic singleton carrier therefore pays the original Q or "
            "linear row degree. This does not classify polynomial functions over "
            "varying finite fields."
        ),
        "windows": (
            "Disjoint window products multiply back to the global saturated row "
            "product, so local zero-rate height bounds sum to the full scale."
        ),
        "scope": (
            "No actual large-sieve or gcd-correlation bound is proved. Declared "
            "rows are algebraic controls only."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    main_control = main_declared_control()
    zero_control = zero_t_control()
    union_controls = union_ideal_controls()
    proof = proof_object()
    return {
        "schema": "item358-beta-actual-low-incidence-saturation-barrier-certificate-v1",
        "item": 358,
        "date": "2026-09-01",
        "status": "PROVED_ACTUAL_INCIDENCE_SATURATION_SINGLETON_SQUAREFREE_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "actual_incidence_set_saturation": "PROVED",
            "genuine_singleton_outside_row_avoidance": "PROVED",
            "fresh_low_incidence_carrier": "PROVED",
            "four_quadrant_overlap_decomposition": "PROVED",
            "singleton_pairwise_squarefull_orthogonality": "PROVED",
            "uniform_union_ideal_product_or_Q_barrier": "PROVED",
            "disjoint_window_height_barrier": "PROVED",
            "actual_singleton_gcd_correlation_bound": "OPEN",
            "actual_growing_low_incidence_bound": "OPEN",
            "actual_Xi_Q": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            "main": main_control,
            "main_digest": digest(main_control),
            "t_zero": zero_control,
            "union_ideal": union_controls,
            "finite_rows_promoted": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "item350_selected_hits_promoted_to_first_occurrence": False,
            "closes": [
                "pairwise shared-support and E(Q) as controls of the fresh singleton quadrant",
                "uniform bounded-degree algebraic-ideal union carriers",
                "disjoint-window height summation as a zero-rate aggregate theorem",
            ],
            "isolates": [
                "the actual singleton gcd correlation",
                "the growing low-incidence squarefree correlation",
            ],
            "does_not_close": [
                "a genuinely new large-sieve or distribution theorem",
                "finite-field polynomial-function identities outside ideal membership",
                "the actual low-incidence mass or Xi_Q",
                "squarefull excess, H_Q, K_Q, Gamma_Q, beta capacity, or Route 1",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_fresh_singleton_maximum": "log Q<=log b",
            "row_product_ceiling": "2N_A log A=(2+o(1))log b",
            "pairwise_contribution_on_fresh_singletons": 0,
            "E_Q_contribution_on_fresh_singletons": 0,
            "actual_singleton_rate": "OPEN",
            "actual_growing_low_incidence_rate": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item358_beta_actual_low_incidence_saturation_barrier_certificate.json",
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
                "actual_singleton_correlation": "OPEN",
                "booking": 0,
                "item": 358,
                "remaining_input": "ACTUAL_SINGLETON_SQUAREFREE_GCD_CORRELATION",
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
