#!/usr/bin/env python3
"""Deterministic exact replay for Item 370.

Checks sparse-monomial singleton-chart intersections, coefficient-content
capture, and bounded-window support growth.  Declared primes are algebraic
truth controls only; there is no actual prime, target, or half-bound census.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterator


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
    "sources/item333_beta_nonlinear_state_saturation_no_go_report.md": (
        "8f4bc0a6f93cbd4882392ade311d68e25be1ceb282db71cc5e1ef2f70aee75d6"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_certificate.json": (
        "933120c05e0f67663608e9e53354407f4593718c149941942d070f4af3c0a76a"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_root_audit.json": (
        "6ddd4949f5d7f91fdc160634da06079661ebf373ac0f061495a7b41135924ecc"
    ),
    "manifests/item333_beta_nonlinear_state_saturation_no_go_manifest.json": (
        "a1f55058846bdee5f33848f45af06fed8659f8c3402e4af6896540bf468aae77"
    ),
    "sources/item346_beta_t_avoiding_radical_localization_report.md": (
        "2ad742c14d0adbc74da6c46394ed89f68cec8888a3c9d22ee4f230a4e16548a5"
    ),
    "scripts/item346_beta_t_avoiding_radical_localization_certificate.py": (
        "76c020b07d199a7283d7373a3ef677643d3be01adfe7480628f92ccdad7498c0"
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
    "sources/item365_beta_actual_orbit_interpolation_barrier_report.md": (
        "c4e4789cec655f70f1914783e4cf203ed2c64d1b418ef6d28221ec09fde0b201"
    ),
    "scripts/item365_beta_actual_orbit_interpolation_barrier_certificate.py": (
        "40e4cb5a8afbf8018b9c9639d35366411c2c8db30b3302011ee658b62cfad500"
    ),
    "results/item365_beta_actual_orbit_interpolation_barrier_certificate.json": (
        "a8ac3e49a2d0270524c259c552728d7dba548793094ca31ee55298536f079e53"
    ),
    "results/item365_beta_actual_orbit_interpolation_barrier_root_audit.json": (
        "50172f2daa112892c1a20b4f83cd14613681fdcdf1ae713a960071a74fe579e4"
    ),
    "manifests/item365_beta_actual_orbit_interpolation_barrier_manifest.json": (
        "af8b606b81612ded49ab415a43b07d7d986a98084e650a3dc744e031c6e40f85"
    ),
    "sources/item367_beta_uniform_affine_carrier_no_go_report.md": (
        "3827c4e9d9532135fdb2e338397523ce8b2936483b09cf5accbc974002023798"
    ),
    "scripts/item367_beta_uniform_affine_carrier_no_go_certificate.py": (
        "6c9322838eccbca1ac257f7526fbae1a11f77937679b00fc4824aa40006f3a19"
    ),
    "results/item367_beta_uniform_affine_carrier_no_go_certificate.json": (
        "b6fc66168a18237a67e43d75c13dc36666bd5c0fbb444d98fdc0a928bb186d93"
    ),
    "results/item367_beta_uniform_affine_carrier_no_go_root_audit.json": (
        "40dd78454cd16a16581e3fd1f3d1c89c61b4c1e70465f4688f8298c59fa2c843"
    ),
    "manifests/item367_beta_uniform_affine_carrier_no_go_manifest.json": (
        "3d3d7db889f0b39fab5b1e1792bf2332aa8d57a1718c6681dc1cbd5c915c20b1"
    ),
}


Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    root = Path(__file__).resolve().parent.parent
    rows = []
    for relative_path, expected in DEPENDENCY_HASHES.items():
        payload = (root / relative_path).read_bytes()
        actual = hashlib.sha256(payload).hexdigest()
        assert actual == expected, (relative_path, actual, expected)
        rows.append(
            {"path": relative_path, "bytes": len(payload), "sha256": actual}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def exponent_tuples(variable_count: int, max_total_degree: int) -> Iterator[Monomial]:
    for values in itertools.product(range(max_total_degree + 1), repeat=variable_count):
        if sum(values) <= max_total_degree:
            yield values


def in_coordinate_ideal(monomial: Monomial, coordinate: int) -> bool:
    return monomial[coordinate] > 0


def in_all_singleton_ideals(monomial: Monomial) -> bool:
    return all(exponent > 0 for exponent in monomial)


def divisible_by_full_product(monomial: Monomial) -> bool:
    return all(exponent >= 1 for exponent in monomial)


def intersection_controls() -> dict[str, Any]:
    rows = []
    for variable_count in range(1, 7):
        max_degree = variable_count + 2
        monomials = list(exponent_tuples(variable_count, max_degree))
        in_intersection = []
        below_threshold = []
        for monomial in monomials:
            left = all(
                in_coordinate_ideal(monomial, coordinate)
                for coordinate in range(variable_count)
            )
            right = divisible_by_full_product(monomial)
            assert left == right
            if left:
                assert sum(monomial) >= variable_count
                in_intersection.append(monomial)
            if sum(monomial) < variable_count:
                assert not left
                below_threshold.append(monomial)
        rows.append(
            {
                "N": variable_count,
                "max_degree": max_degree,
                "monomials_checked": len(monomials),
                "intersection_monomials": len(in_intersection),
                "degree_below_N_monomials": len(below_threshold),
                "identity": "intersection_j (X_j) = (product_j X_j)",
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def polynomial_content(polynomial: Polynomial) -> int:
    result = 0
    for coefficient in polynomial.values():
        result = math.gcd(result, abs(coefficient))
    return result


def zero_mod_prime(polynomial: Polynomial, prime: int) -> bool:
    return all(coefficient % prime == 0 for coefficient in polynomial.values())


def content_controls() -> dict[str, Any]:
    # Four load variables; total degree two is below the singleton threshold N=4.
    polynomial: Polynomial = {
        (0, 0, 0, 0): 30,
        (2, 0, 0, 0): -60,
        (0, 1, 1, 0): 90,
    }
    content = polynomial_content(polynomial)
    assert content == 30
    rows = []
    for prime in [2, 3, 5, 7, 11]:
        zero = zero_mod_prime(polynomial, prime)
        assert zero == (content % prime == 0)
        rows.append(
            {
                "declared_prime": prime,
                "zero_polynomial_mod_prime": zero,
                "prime_divides_content": content % prime == 0,
            }
        )
    primitive: Polynomial = {
        (0, 0, 0, 0): 1,
        (1, 1, 0, 0): 6,
        (0, 0, 2, 0): -10,
    }
    assert polynomial_content(primitive) == 1
    assert not any(zero_mod_prime(primitive, prime) for prime in [2, 3, 5, 7, 11])
    return {
        "N": 4,
        "degree": 2,
        "content": content,
        "rows": rows,
        "rows_digest": digest(rows),
        "primitive_content": 1,
        "finite_algebra_controls_only": True,
    }


def support_and_recurrence_controls() -> dict[str, Any]:
    rows = []
    for variable_count in range(3, 9):
        window_size = variable_count - 1
        supported_monomial = tuple(
            1 if index < window_size else 0 for index in range(variable_count)
        )
        assert not divisible_by_full_product(supported_monomial)
        product_state = [0] * variable_count
        state_rows = []
        for index in range(variable_count):
            product_state[index] += 1
            state_rows.append(
                {
                    "step": index + 1,
                    "degree": sum(product_state),
                    "support": sum(exponent > 0 for exponent in product_state),
                }
            )
        assert tuple(product_state) == (1,) * variable_count
        rows.append(
            {
                "N": variable_count,
                "bounded_window_support": window_size,
                "window_omits_a_row": True,
                "window_monomial_in_intersection": False,
                "full_product_degree": variable_count,
                "full_product_support": variable_count,
                "product_accumulator": state_rows,
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def portfolio_controls() -> dict[str, Any]:
    rows = []
    for variable_count in range(5, 13):
        # A declared partition into portfolios of at most three charts.
        chart_sets = [
            list(range(start, min(start + 3, variable_count)))
            for start in range(0, variable_count, 3)
        ]
        assert sorted(index for subset in chart_sets for index in subset) == list(
            range(variable_count)
        )
        minimum_degrees = [len(subset) for subset in chart_sets]
        assert sum(minimum_degrees) == variable_count
        rows.append(
            {
                "N": variable_count,
                "chart_sets": chart_sets,
                "portfolio_size": len(chart_sets),
                "minimum_degrees": minimum_degrees,
                "minimum_total_degree_budget": sum(minimum_degrees),
                "full_chart_cover": True,
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def proof_object() -> dict[str, Any]:
    return {
        "endpoint_reduction": (
            "For p|b the Item365 endpoint coefficient is a p-unit, so after "
            "external t-saturation the endpoint quotient has independent load "
            "coordinates X_j. The class assumes a p-independent integral "
            "endpoint-reduced numerator and a denominator that is a unit on "
            "every singleton chart."
        ),
        "singleton_kernel": (
            "The contraction of the j-th localized singleton chart is (X_j). "
            "Therefore the kernel of the product of all chart maps is "
            "intersection_j(X_j)=(product_j X_j)."
        ),
        "low_complexity": (
            "A numerator of load degree less than N, or omitting any active "
            "load, cannot be a nonzero member of the singleton kernel. Modulo "
            "p it must be the zero polynomial."
        ),
        "content_capture": (
            "For a p-independent integer numerator, being the zero polynomial "
            "modulo p is equivalent to p dividing every coefficient. Hence "
            "every actual captured U_11 prime divides the integer coefficient "
            "content. Primitive numerators capture none; the zero numerator "
            "is inadmissible."
        ),
        "portfolio": (
            "If numerator G_l is assigned a set S_l of singleton charts, its "
            "noncontent branch is divisible by product_(j in S_l) X_j and "
            "has load degree at least |S_l|. If every member of a portfolio "
            "covering all N charts remains noncontent, its total degree "
            "budget is at least N; other charts enter content branches."
        ),
        "scope": (
            "This closes generic endpoint-reduced bounded-window and "
            "sublinear-load-degree identities. It does not close accidental "
            "correlations at the unique canonical point or full-support "
            "degree-N recurrences."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    intersections = intersection_controls()
    contents = content_controls()
    recurrences = support_and_recurrence_controls()
    portfolios = portfolio_controls()
    proof = proof_object()
    controls = {
        "intersections": intersections,
        "contents": contents,
        "recurrences": recurrences,
        "portfolios": portfolios,
    }
    return {
        "schema": "item370-beta-q-free-residual-saturation-no-go-certificate-v1",
        "item": 370,
        "date": "2026-09-01",
        "status": "PROVED_Q_FREE_GENERIC_SINGLETON_RESIDUAL_SATURATION",
        "dependencies": dependencies,
        "theorem": {
            "endpoint_reduced_singleton_chart_kernel": "PROVED",
            "rational_p_unit_denominator_reduction": "PROVED",
            "bounded_window_residual_no_go": "PROVED_SCOPED",
            "load_degree_below_N_residual_no_go": "PROVED_SCOPED",
            "bounded_portfolio_total_degree_barrier": "PROVED_SCOPED",
            "coefficient_content_capture": "PROVED",
            "nonzero_sub_beta_actual_residual": "OPEN",
            "canonical_one_point_correlation": "OPEN",
            "full_support_degree_N_residual": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            **controls,
            "controls_digest": digest(controls),
            "finite_rows_promoted": False,
            "actual_prime_or_target_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "closes": [
                "generic endpoint-reduced p-independent q-free residual identities of load degree below N",
                "generic bounded-window residual identities omitting an active row",
                "bounded portfolios whose total noncontent load degree is below the number of covered rows",
                "p-unit rational denominators as an escape from numerator saturation",
                "primitive nonzero numerators in the closed class",
            ],
            "does_not_close": [
                "a correlation holding only at the unique actual canonical point",
                "a full-support numerator of load degree at least N",
                "beta-height product or gcd/radical recurrence states",
                "candidate-dependent CRT constants",
                "the actual U_11 mass, beta capacity, Route 1, or e+pi",
            ],
            "zero_residual_admissible": False,
            "candidate_dependent_constants_admissible": False,
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_singleton_maximum": "log U_11<=log b",
            "closed_class_carrier": "absolute coefficient content of endpoint-reduced numerator",
            "sub_beta_nonzero_content_implication": "would prove log U_11=o(log b)",
            "constructed_nonzero_actual_content_carrier": False,
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item370_beta_q_free_residual_saturation_no_go_certificate.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate()
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "item": certificate["item"],
                "status": certificate["status"],
                "booking": certificate["capacity"]["booking"],
                "actual_nonzero_residual": certificate["theorem"][
                    "nonzero_sub_beta_actual_residual"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
