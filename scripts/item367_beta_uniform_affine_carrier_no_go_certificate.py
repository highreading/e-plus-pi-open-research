#!/usr/bin/env python3
"""Deterministic exact replay for Item 367.

The checker verifies continued-fraction identities, the elementary
best-approximation lower bound on declared coefficient boxes, and fixed-window
reduction to the (q_{n-1},q_{n-2}) basis.  It performs no prime, target, or
half-bound census.  Declared finite controls are not promoted to actual
Item-316 instances.
"""

from __future__ import annotations

import argparse
import hashlib
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
}


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


def q_sequence(n_max: int) -> list[int]:
    values = [1, 1]
    for n in range(2, n_max + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def rational_continued_fraction(numerator: int, denominator: int) -> list[int]:
    assert numerator > denominator > 0
    values = []
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        values.append(quotient)
        numerator, denominator = denominator, remainder
    return values


def convergents(partials: list[int]) -> list[tuple[int, int]]:
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    rows = []
    for partial in partials:
        p_current = partial * p_previous + p_previous_previous
        q_current = partial * q_previous + q_previous_previous
        rows.append((p_current, q_current))
        p_previous_previous, p_previous = p_previous, p_current
        q_previous_previous, q_previous = q_previous, q_current
    return rows


def cf_identity_controls() -> dict[str, Any]:
    q_values = q_sequence(12)
    rows = []
    for n in range(5, 13):
        m = n - 2
        A = 4 * n - 2
        a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
        weights = [7] + [4 * index + 2 for index in range(2, m + 1)]
        partials = rational_continued_fraction(a, c)
        assert partials == list(reversed(weights))
        assert max(partials) <= A
        assert b == A * a + c
        assert c < a < A * c
        assert b < A * A * c
        convergent_rows = convergents(partials)
        assert convergent_rows[-1] == (a, c)
        rows.append(
            {
                "n": n,
                "capital_A": A,
                "a": str(a),
                "b": str(b),
                "c": str(c),
                "partials": partials,
                "max_partial": max(partials),
                "log_c_over_log_b": math.log(c) / math.log(b),
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def coefficient_box_controls() -> dict[str, Any]:
    q_values = q_sequence(10)
    rows = []
    for n in range(6, 11):
        A = 4 * n - 2
        a, c = q_values[n - 1], q_values[n - 2]
        B = n - 3
        assert 2 * (A + 2) * B * B < c
        minimum_cross = None
        minimum_affine = None
        checked_cross = 0
        checked_affine = 0
        for alpha in range(-B, B + 1):
            for beta in range(-B, B + 1):
                if alpha == 0 and beta == 0:
                    continue
                cross = abs(alpha * a + beta * c)
                assert cross > 0
                assert cross * (A + 2) * B >= c
                minimum_cross = cross if minimum_cross is None else min(minimum_cross, cross)
                checked_cross += 1
                for gamma in range(-B, B + 1):
                    affine = abs(alpha * a + beta * c + gamma)
                    assert affine > 0
                    assert 2 * affine * (A + 2) * B >= c
                    minimum_affine = (
                        affine if minimum_affine is None else min(minimum_affine, affine)
                    )
                    checked_affine += 1
        rows.append(
            {
                "n": n,
                "capital_A": A,
                "B": B,
                "threshold_margin": c - 2 * (A + 2) * B * B,
                "minimum_cross": str(minimum_cross),
                "minimum_affine": str(minimum_affine),
                "cross_pairs_checked": checked_cross,
                "affine_triples_checked": checked_affine,
                "exact_bound_checked": "2(A+2)B*|alpha*a+beta*c+gamma|>=c",
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "finite_coefficient_boxes_only": True,
        "prime_or_target_census_performed": False,
    }


def fixed_window_reduction_controls() -> dict[str, Any]:
    q_values = q_sequence(14)
    rows = []
    for n in range(8, 15):
        a, c = q_values[n - 1], q_values[n - 2]
        coefficients: dict[int, tuple[int, int]] = {
            n: (4 * n - 2, 1),
            n - 1: (1, 0),
            n - 2: (0, 1),
        }
        for index in range(n - 1, n - 5, -1):
            # q_index=(4*index-2)q_(index-1)+q_(index-2).
            high = coefficients[index]
            middle = coefficients[index - 1]
            multiplier = 4 * index - 2
            coefficients[index - 2] = (
                high[0] - multiplier * middle[0],
                high[1] - multiplier * middle[1],
            )
        coordinate_rows = []
        for index in range(n, n - 6, -1):
            alpha, beta = coefficients[index]
            assert alpha * a + beta * c == q_values[index]
            coordinate_rows.append(
                {
                    "q_index": index,
                    "alpha_on_a": alpha,
                    "beta_on_c": beta,
                    "coefficient_max": max(abs(alpha), abs(beta)),
                }
            )
        rows.append(
            {
                "n": n,
                "window": coordinate_rows,
                "window_digest": digest(coordinate_rows),
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "fixed_window_only": True,
    }


def proof_object() -> dict[str, Any]:
    return {
        "actual_family": (
            "For each n satisfying the Item316 target, the canonical word, "
            "actual nonzero loads, t, Q^[1], and U_11 are fixed. A uniform "
            "carrier H_n is independent of the candidate prime."
        ),
        "continued_fraction_bound": (
            "For x=a/c=[w_m;...;w_1] every partial quotient is at most A. "
            "If 0<max(|alpha|,|beta|)<=B<c, Legendre's criterion and the "
            "next-convergent bound q_next<=(A+1)q give "
            "|alpha*a+beta*c|>=c/((A+2)B)."
        ),
        "affine_rational_dichotomy": (
            "If max(|alpha|,|beta|,|gamma|,D)<=B, D>=1, "
            "D*H=alpha*a+beta*c+gamma, and B^2<c/(2(A+2)), then a "
            "nonzero q-dependent component gives |H|>=c/(2(A+2)B^2). "
            "If alpha=beta=0, H=gamma/D is the sole sub-beta residual."
        ),
        "capacity": (
            "For log B=o(log b), log c=log b+O(log n), so every q-dependent "
            "carrier has log|H|=(1+o(1))log b and cannot give zero rate or a "
            "fixed fractional saving. A q-free residual would give zero rate "
            "if the actual implication U_11|H were separately proved."
        ),
        "recurrence_scope": (
            "Fixed q-windows and affine recurrences with sub-beta unrolled "
            "coefficient height reduce to this class. Fixed recurrence order "
            "alone is not closed: an order-one product accumulator has "
            "beta-scale coefficient height."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    cf_rows = cf_identity_controls()
    boxes = coefficient_box_controls()
    windows = fixed_window_reduction_controls()
    proof = proof_object()
    controls = {"cf": cf_rows, "boxes": boxes, "windows": windows}
    return {
        "schema": "item367-beta-uniform-affine-carrier-no-go-certificate-v1",
        "item": 367,
        "date": "2026-09-01",
        "status": "PROVED_SUB_BETA_AFFINE_RATIONAL_CARRIER_DICHOTOMY",
        "dependencies": dependencies,
        "theorem": {
            "actual_cross_n_family_formulated": "PROVED",
            "continued_fraction_linear_form_lower_bound": "PROVED",
            "sub_beta_affine_rational_dichotomy": "PROVED",
            "q_dependent_fixed_fraction_capacity_saving": "PROVED_IMPOSSIBLE_IN_CLASS",
            "q_free_actual_singleton_carrier": "OPEN",
            "arbitrary_fixed_order_recurrence": "OPEN",
            "weighted_singleton_bound": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            **controls,
            "controls_digest": digest(controls),
            "finite_rows_promoted": False,
            "prime_or_target_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "closes": [
                "q-dependent p-independent affine-rational carriers with sub-beta reduced coefficient and denominator height",
                "bounded fixed q-window formulas inside that envelope",
                "bounded-order affine recurrences only when their unrolled coefficient height is sub-beta",
            ],
            "does_not_close": [
                "q-free residual formulas with an actual U_11 divisibility implication",
                "iterated recurrences with beta-scale accumulated coefficients",
                "nonlinear polynomial or gcd/radical formulas outside the affine-rational class",
                "the actual singleton mass, beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_singleton_maximum": "log U_11<=log b",
            "coefficient_envelope": "log B_n=o(log b)",
            "q_dependent_carrier_height": "(1+o(1))*log b",
            "q_free_residual_height": "o(log b), but actual divisibility OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item367_beta_uniform_affine_carrier_no_go_certificate.json",
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
                "q_free_residual": certificate["theorem"][
                    "q_free_actual_singleton_carrier"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
