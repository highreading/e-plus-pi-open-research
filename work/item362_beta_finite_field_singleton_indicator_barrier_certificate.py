#!/usr/bin/env python3
"""Exact deterministic replay for Item 362.

Checks finite-field singleton indicators, unique reduced degrees, the exact
candidate loop, integer-height dilation, the first quotient/Fermat bridge,
and declared triangular-load controls.  No target or prime census is run.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
from itertools import combinations, product
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
    "sources/item358_beta_actual_low_incidence_saturation_barrier_report.md": (
        "681c9f9cbe926978c78f632084c8be83439c2ac3f5e50f2c2697a49f2f0da68d"
    ),
    "scripts/item358_beta_actual_low_incidence_saturation_barrier_certificate.py": (
        "c997c7f3739fe5dc98ee2e48c3ebfd1a67e74289e175d52bc8d5adfb1f9565bf"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_certificate.json": (
        "4da88e55dec36f3c130def549007c8ae1509ff0a029dfed9ff25f67a78c2ffa3"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_root_audit.json": (
        "a1a48f7d7080834ebf3be56b47d8056733e88e1913e8f6ea784f97a5eb2d9172"
    ),
    "manifests/item358_beta_actual_low_incidence_saturation_barrier_manifest.json": (
        "4ba799fe2fc8cb6063034d844f91bcaec6c3fc84d043b1f46c675fce400acfb1"
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


def add_term(
    coefficients: dict[tuple[int, ...], int],
    exponents: tuple[int, ...],
    coefficient: int,
    p: int,
) -> None:
    value = (coefficients.get(exponents, 0) + coefficient) % p
    if value:
        coefficients[exponents] = value
    else:
        coefficients.pop(exponents, None)


def singleton_complement_coefficients(
    p: int, row_count: int, include_t: bool
) -> dict[tuple[int, ...], int]:
    """Unique reduced coefficients of 1 minus the singleton indicator."""
    assert p >= 3 and row_count >= 1
    variable_count = row_count + int(include_t)
    coefficients: dict[tuple[int, ...], int] = {}
    add_term(coefficients, (0,) * variable_count, 1, p)
    t_offset = int(include_t)
    for missing_row in range(row_count):
        exponents = [0] * variable_count
        if include_t:
            exponents[0] = p - 1
        for row in range(row_count):
            if row != missing_row:
                exponents[t_offset + row] = p - 1
        add_term(coefficients, tuple(exponents), -1, p)
    full = [0] * variable_count
    if include_t:
        full[0] = p - 1
    for row in range(row_count):
        full[t_offset + row] = p - 1
    add_term(coefficients, tuple(full), row_count, p)
    return coefficients


def low_incidence_complement_coefficients(
    p: int, row_count: int, threshold: int
) -> dict[tuple[int, ...], int]:
    """Reduced coefficients for 1 minus t-away incidence 1..L-1."""
    assert 2 <= threshold <= row_count + 1
    coefficients: dict[tuple[int, ...], int] = {}
    add_term(coefficients, (0,) * (row_count + 1), 1, p)
    row_indices = range(row_count)
    for zero_count in range(1, threshold):
        for zero_set_tuple in combinations(row_indices, zero_count):
            zero_set = set(zero_set_tuple)
            for added_count in range(zero_count + 1):
                for added_tuple in combinations(zero_set_tuple, added_count):
                    support = (set(row_indices) - zero_set) | set(added_tuple)
                    exponents = [p - 1] + [0] * row_count
                    for row in support:
                        exponents[row + 1] = p - 1
                    # Complement contributes minus the indicator expansion.
                    add_term(
                        coefficients,
                        tuple(exponents),
                        -((-1) ** added_count),
                        p,
                    )
    return coefficients


def total_degree(coefficients: dict[tuple[int, ...], int]) -> int:
    return max(sum(exponents) for exponents in coefficients)


def individual_degrees(
    coefficients: dict[tuple[int, ...], int]
) -> list[int]:
    variable_count = len(next(iter(coefficients)))
    return [
        max(exponents[index] for exponents in coefficients)
        for index in range(variable_count)
    ]


def singleton_indicator_mod(p: int, t: int, rows: list[int]) -> int:
    indicator = 0
    for missing_row in range(len(rows)):
        term = (1 - pow(rows[missing_row], p - 1, p)) % p
        for row, value in enumerate(rows):
            if row != missing_row:
                term = term * pow(value, p - 1, p) % p
        indicator = (indicator + term) % p
    return pow(t, p - 1, p) * indicator % p


def singleton_complement_mod(p: int, t: int, rows: list[int]) -> int:
    return (1 - singleton_indicator_mod(p, t, rows)) % p


def singleton_complement_integer(p: int, t: int, rows: list[int]) -> int:
    assert p >= 3 and rows and all(value >= 1 for value in rows)
    exponent = p - 1
    indicator = 0
    for missing_row in range(len(rows)):
        term = 1 - rows[missing_row] ** exponent
        term *= math.prod(
            value**exponent
            for row, value in enumerate(rows)
            if row != missing_row
        )
        indicator += term
    return 1 - abs(t) ** exponent * indicator


def low_incidence_complement_mod(
    p: int, t: int, rows: list[int], threshold: int
) -> int:
    zero_count = sum(value % p == 0 for value in rows)
    indicator = int(t % p != 0 and 1 <= zero_count < threshold)
    return (1 - indicator) % p


def reduced_degree_controls() -> dict[str, Any]:
    cases = [
        {"p": 5, "N": 2},
        {"p": 3, "N": 3},
        {"p": 7, "N": 4},
    ]
    rows: list[dict[str, Any]] = []
    for case in cases:
        p = case["p"]
        row_count = case["N"]
        with_t = singleton_complement_coefficients(p, row_count, True)
        row_only = singleton_complement_coefficients(p, row_count, False)
        expected_with_t = (
            (row_count + 1) * (p - 1)
            if row_count % p
            else row_count * (p - 1)
        )
        expected_row_only = (
            row_count * (p - 1)
            if row_count % p
            else (row_count - 1) * (p - 1)
        )
        assert total_degree(with_t) == expected_with_t
        assert total_degree(row_only) == expected_row_only
        assert individual_degrees(with_t) == [p - 1] * (row_count + 1)
        lower_degree = row_count * (p - 1)
        rows.append(
            {
                **case,
                "with_t_total_degree": total_degree(with_t),
                "row_only_total_degree": total_degree(row_only),
                "unconditional_with_t_lower_degree": lower_degree,
                "binary_multiplication_depth_lower_bound": math.ceil(
                    math.log2(lower_degree)
                ),
                "coefficient_digest": digest(
                    sorted((list(key), value) for key, value in with_t.items())
                ),
            }
        )

    truth_tables = []
    for p, row_count in [(3, 2), (5, 2)]:
        checked = 0
        zeros = 0
        for values in product(range(p), repeat=row_count + 1):
            t = values[0]
            row_values = list(values[1:])
            complement = singleton_complement_mod(p, t, row_values)
            expected_zero = t != 0 and sum(value == 0 for value in row_values) == 1
            assert (complement == 0) == expected_zero
            assert complement in (0, 1)
            checked += 1
            zeros += int(expected_zero)
        truth_tables.append(
            {"p": p, "N": row_count, "points": checked, "zero_points": zeros}
        )

    p = 3
    row_count = 3
    threshold = 3
    low_coefficients = low_incidence_complement_coefficients(
        p, row_count, threshold
    )
    guaranteed_lower = (row_count - threshold + 2) * (p - 1)
    assert total_degree(low_coefficients) >= guaranteed_lower
    low_points = 0
    for values in product(range(p), repeat=row_count + 1):
        t = values[0]
        row_values = list(values[1:])
        expected = low_incidence_complement_mod(p, t, row_values, threshold)
        evaluated = 0
        for exponents, coefficient in low_coefficients.items():
            term = coefficient
            for value, exponent in zip(values, exponents):
                term = term * pow(value, exponent, p) % p
            evaluated = (evaluated + term) % p
        assert evaluated == expected
        low_points += 1

    return {
        "degree_cases": rows,
        "degree_cases_digest": digest(rows),
        "truth_tables": truth_tables,
        "truth_tables_digest": digest(truth_tables),
        "low_incidence": {
            "p": p,
            "N": row_count,
            "L": threshold,
            "points": low_points,
            "proved_degree_lower": guaranteed_lower,
            "actual_reduced_degree": total_degree(low_coefficients),
        },
        "unique_reduced_representative_used": True,
        "prime_census_performed": False,
    }


def triangular_load_control() -> dict[str, Any]:
    digits = [3, 2, 8, 9, 4, 11]
    weights = [0, 0, 5, 7, 4, 6]
    loads = [weights[index] * digits[index - 1] - digits[index] for index in range(2, 6)]
    reconstructed = digits[:2]
    for index, load in enumerate(loads, start=2):
        reconstructed.append(weights[index] * reconstructed[index - 1] - load)
    assert reconstructed == digits
    for p in [3, 5, 7]:
        assert singleton_complement_mod(p, 2, loads) == singleton_complement_mod(
            p, 2, [abs(value) for value in loads]
        )
    return {
        "digits": digits,
        "weights": weights,
        "loads": loads,
        "reconstructed": reconstructed,
        "integral_triangular_inverse_verified": True,
        "odd_prime_sign_invariance_verified": True,
        "actual_target_or_canonical_box_claim": False,
    }


def candidate_loop_control() -> dict[str, Any]:
    A = 10
    t = 17
    rows = [22, 33, 26, 34]
    q_exponents = {11: 1, 13: 1, 17: 1, 19: 2}
    assert all(0 < value < A * A for value in rows)
    q_single_primes = [p for p, exponent in q_exponents.items() if exponent == 1]
    candidate_rows: list[dict[str, Any]] = []
    carrier = 1
    for p in q_single_primes:
        assert A < p < A * A
        complement = singleton_complement_integer(p, t, rows)
        occurrence = sum(value % p == 0 for value in rows)
        expected_hit = t % p != 0 and occurrence == 1
        gcd_value = math.gcd(p, complement)
        assert gcd_value == (p if expected_hit else 1)
        if expected_hit:
            assert complement >= p ** (p - 1)
        carrier *= gcd_value
        candidate_rows.append(
            {
                "p": p,
                "occurrence": occurrence,
                "t_avoiding": t % p != 0,
                "phi_mod_p": complement % p,
                "gcd_p_phi": gcd_value,
                "integer_phi": str(complement),
                "hit_height_lower_verified": (not expected_hit)
                or complement >= p ** (p - 1),
            }
        )
    assert carrier == 13
    return {
        "A": A,
        "t": t,
        "rows": rows,
        "Q_exponents": {str(p): exponent for p, exponent in q_exponents.items()},
        "Q_single_primes": q_single_primes,
        "candidate_rows": candidate_rows,
        "candidate_rows_digest": digest(candidate_rows),
        "exact_singleton_squarefree_carrier": carrier,
        "expected_carrier": 13,
        "finite_algebraic_control_only": True,
    }


def quotient_bridge_control() -> dict[str, Any]:
    control_rows: list[dict[str, Any]] = []
    for p in [3, 5, 7, 11]:
        t = 1
        rows = [p, p - 1]
        singleton_index = 0
        other_product = p - 1
        complement = singleton_complement_integer(p, t, rows)
        fermat_quotient = ((other_product ** (p - 1) - 1) // p) % p
        assert fermat_quotient == 1
        assert complement % (p * p) == (
            1 - pow(other_product, p - 1, p * p)
        ) % (p * p)
        assert (complement // p) % p == p - 1
        valuation = 0
        remaining = complement
        while remaining % p == 0:
            valuation += 1
            remaining //= p
        assert valuation == 1
        control_rows.append(
            {
                "p": p,
                "rows": rows,
                "integer_phi": str(complement),
                "phi_mod_p2": complement % (p * p),
                "fermat_quotient_mod_p": fermat_quotient,
                "phi_over_p_mod_p": (complement // p) % p,
                "p_adic_valuation": valuation,
            }
        )
    return {
        "symbolic_family": "t=1, rows=(p,p-1) for every odd prime p",
        "binomial_identity_mod_p2": "(p-1)^(p-1)=1+p (mod p^2)",
        "fermat_quotient_mod_p": 1,
        "phi_over_p_mod_p": "-1",
        "p_adic_valuation": 1,
        "control_rows": control_rows,
        "control_rows_digest": digest(control_rows),
        "universal_p2_lift_refuted_for_every_odd_p": True,
        "actual_item316_target_claim": False,
    }


def frobenius_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for p in [3, 5, 7]:
        values = [pow(value, p, p) - value for value in range(p)]
        assert all(value % p == 0 for value in values)
        rows.append(
            {
                "p": p,
                "Y_to_p_minus_Y_zero_function": True,
                "zero_test_degree": p - 1,
                "binary_powering_depth_lower_bound": math.ceil(math.log2(p - 1)),
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "function_kernel_relation": "Y^p-Y reduces to zero",
        "reduced_singleton_class_unchanged_by_kernel_additions": True,
        "integer_frobenius_gate_height_multiplies_log_size_by_p": True,
    }


def proof_object() -> dict[str, Any]:
    return {
        "unique_reduction": (
            "Evaluation identifies F_p-valued functions with the quotient by "
            "T^p-T and Y_i^p-Y_i; every class has one representative of "
            "individual degrees at most p-1, and reduction never raises total degree."
        ),
        "degree": (
            "The t-away singleton complement has reduced degree (N+1)(p-1) "
            "when p does not divide N and N(p-1) otherwise. Each variable has "
            "degree p-1. The incidence-<L complement contains a monomial of "
            "degree (N-L+2)(p-1); with external t-avoidance the analogous "
            "row-only lower bound is (N-L+1)(p-1)."
        ),
        "recurrence": (
            "The signed loads x_j=w_j d_(j-1)-d_j are integral triangular "
            "coordinates of determinant a unit modulo every p. Composition with "
            "the linear map and its inverse proves invariance of reduced functional "
            "degree. Before the target and canonical box are imposed, a uniform "
            "recurrence-only substitution cannot lower the reduced row degree."
        ),
        "actual_loop": (
            "On the actual nonzero cofactor word, the product over p dividing "
            "Q^[1] in (A,A^2) of gcd(p,Phi_p(t,Z)) is exactly U_11."
        ),
        "height": (
            "At a t-avoiding singleton, the canonical integer lift is positive "
            "and at least p^(p-1). Since p>A, aggregating hit-specific lifts "
            "dilates the target mass by at least A rather than compressing it."
        ),
        "quotient": (
            "At singleton row j, Phi_p/p modulo p is minus the Fermat quotient "
            "of t times the product of the other rows. No second p-adic digit "
            "is forced by the indicator identity."
        ),
        "scope": (
            "This closes bounded-degree exact polynomial-function carriers and "
            "their canonical reduced integer lifts. It does not close a new "
            "target-specific cancellation, large-sieve, or Fermat-quotient theorem."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    degrees = reduced_degree_controls()
    triangular = triangular_load_control()
    candidate = candidate_loop_control()
    quotient = quotient_bridge_control()
    frobenius = frobenius_controls()
    proof = proof_object()
    return {
        "schema": "item362-beta-finite-field-singleton-indicator-barrier-certificate-v1",
        "item": 362,
        "date": "2026-09-01",
        "status": "PROVED_FINITE_FIELD_INDICATOR_DEGREE_HEIGHT_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "unique_reduced_singleton_indicator": "PROVED",
            "minimal_total_and_individual_degree": "PROVED",
            "growing_low_incidence_degree_lower_bound": "PROVED",
            "triangular_recurrence_degree_preservation_before_target": "PROVED",
            "actual_candidate_loop_identity": "PROVED",
            "canonical_lift_height_dilation": "PROVED",
            "first_quotient_fermat_bridge": "PROVED",
            "universal_second_digit": "REFUTED_BY_ALL_ODD_PRIME_CONSTRUCTION",
            "actual_singleton_zero_density": "OPEN",
            "actual_target_specific_finite_field_cancellation": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            "reduced_degrees": degrees,
            "triangular_load": triangular,
            "candidate_loop": candidate,
            "quotient_bridge": quotient,
            "frobenius": frobenius,
            "controls_digest": digest(
                {
                    "degrees": degrees,
                    "triangular": triangular,
                    "candidate": candidate,
                    "quotient": quotient,
                    "frobenius": frobenius,
                }
            ),
            "finite_rows_promoted": False,
            "prime_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "item350_selected_hits_promoted_to_first_occurrence": False,
            "closes": [
                "bounded-degree exact finite-field polynomial-function singleton indicators",
                "bounded multiplication-depth indicators without a p-power primitive",
                "canonical reduced-lift height as a compression of singleton mass",
                "Y^p-Y kernel additions as a way to lower the reduced degree",
            ],
            "does_not_close": [
                "target-specific cancellation after imposing the exact endpoint and canonical box",
                "an arbitrary F-crystal or Cartier-state dimension theorem",
                "a new large-sieve or monodromy theorem",
                "distribution of the moving Fermat quotients",
                "the actual singleton mass, growing low incidence, or Xi_Q",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_singleton_squarefree_maximum": "log Q<=log b",
            "positive_mass_requires_distinct_rows": "Omega(n)",
            "minimum_t_away_indicator_degree": "N(p-1)>=NA",
            "positive_mass_indicator_degree": "Omega(n^2)",
            "per_hit_integer_lift_height": "at least (p-1)log p>=A log p",
            "aggregate_height_dilation": "at least A*log U_11",
            "actual_singleton_rate": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item362_beta_finite_field_singleton_indicator_barrier_certificate.json",
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
                "actual_singleton_zero_density": "OPEN",
                "booking": 0,
                "item": 362,
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
