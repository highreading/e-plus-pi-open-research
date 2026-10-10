#!/usr/bin/env python3
"""Deterministic exact replay for Item 356.

This checker determines the complete pointwise multiplicative relation
lattice of the four Item 353 residue functions, verifies its canonical
Fermat-quotient carry, and tests the resulting entropy-product compression
on the five predeclared rows.  It performs no prime scan.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item356_j1_fermat_multiplicative_collapse_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item353_j1_chosen_prime_first_digit_obstruction_report.md":
        "8b2bf4ab2df535e8016860fafdcaea40092a7a3c5dfdd59b84efd7e7a1e9fd7c",
    "scripts/item353_j1_chosen_prime_first_digit_obstruction_certificate.py":
        "3f35b8604b0210a66ddb1e8d740132c65f3fa0a74d8e3ddbf0e9785a0f9a62cf",
    "results/item353_j1_chosen_prime_first_digit_obstruction_certificate.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_certificate_replay.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_root_replay.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_ledger_delta.json":
        "2919c43ac141c0d2a0151d79f92bb05c52f67f9acee54c6bd2c2b86704088219",
    "results/item353_j1_chosen_prime_first_digit_obstruction_self_audit.json":
        "3597dc8a65064d3e6ff2d4ba3cb2120a0811d3e81ea2b0e422223bb020852dd0",
    "results/item353_j1_chosen_prime_first_digit_obstruction_root_audit.json":
        "61a15a35404078cf0d468cf7cb26610ddbcc2e03a33c1658ff3800c57cf43a0a",
    "manifests/item353_j1_chosen_prime_first_digit_obstruction_manifest.json":
        "0cea5de54d196d51869968f79dbe0f1a22781c05484effb5d913a9a25ec912f8",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM353 = load_module(
    "item356_pinned_item353",
    ROOT / "scripts/item353_j1_chosen_prime_first_digit_obstruction_certificate.py",
)


def fermat_quotient(unit: int, prime: int) -> int:
    if unit % prime == 0:
        raise ValueError("Fermat quotient requires a p-unit")
    return ((pow(unit, prime - 1, prime * prime) - 1) // prime) % prime


def scalar_weights(n: int, r: int, prime: int) -> list[int]:
    exponent = prime - r
    inverse_two = pow(2, -1, prime)
    return [
        -(n - 1) * (n - 2) * inverse_two % prime,
        -(3 - 2 * n) * exponent * inverse_two % prime,
        -exponent * inverse_two % prime,
        -exponent * (exponent - 1) * inverse_two % prime,
    ]


def multiplicative_constant(n: int, r: int, prime: int) -> int:
    b0, b1, _, b3 = scalar_weights(n, r, prime)
    if b0 == 0 or b1 == 0:
        raise ValueError("degenerate edge")
    return b0 * b3 * pow(b1, -2, prime) % prime


def symbolic_relation_audit() -> dict[str, Any]:
    E, n, x = S.symbols("E n x", nonzero=True)
    divisor_matrix = S.Matrix(
        [
            [E, E - 1, E - 1, E - 2],  # a root of G
            [0, 1, 0, 2],               # a root of 1-3x+3x^2
            [0, 0, 2, 0],               # the root x=1/3
            [-n, -n + 1, -n + 1, -n + 2],  # x=0
        ]
    )
    nullspace = divisor_matrix.nullspace()
    if len(nullspace) != 1:
        raise AssertionError("multiplicative relation rank")
    generator = nullspace[0]
    normalized = [S.simplify(value / generator[0]) for value in generator]
    if normalized != [1, -2, 0, 1]:
        raise AssertionError(("multiplicative relation generator", normalized))

    G = 1 - 4 * x + 6 * x**2 - 4 * x**3
    Q = 1 - 3 * x + 3 * x**2
    L = 1 - 3 * x
    if S.discriminant(G, x) != -16 or S.discriminant(Q, x) != -3:
        raise AssertionError("squarefreeness discriminants")
    resultants = [S.resultant(G, Q, x), S.resultant(G, L, x), S.resultant(Q, L, x)]
    if resultants != [1, 5, 3]:
        raise AssertionError(("support resultants", resultants))

    return {
        "divisor_columns": ["R0", "R1", "R2a", "R2b"],
        "divisor_rows": ["root_of_G", "root_of_Q", "root_1_over_3", "zero"],
        "generic_rank": 3,
        "integer_relation_lattice_generator": [1, -2, 0, 1],
        "unique_relation": "R0*R2b=R1^2",
        "support_resultants": [1, 5, 3],
        "valid_for_actual_primes": "p>=13, so all displayed supports are disjoint and squarefree where required",
    }


def entropy_product_mod_p2(coordinates: list[list[int]], prime: int) -> int:
    modulus = prime * prime
    output = 1
    for coordinate in coordinates:
        for residue in coordinate:
            if residue:
                output = output * pow(residue, residue, modulus) % modulus
    return output


def row_control(h: int, s: int, prime: int) -> dict[str, Any]:
    n = 2 * h
    r = 2 * s + 1
    coordinates = ITEM353.weighted_kummer_residues(h, s, prime)
    chosen_digits = ITEM353.chosen_prime_digits(h, s, prime)
    correction_sum = sum(
        ITEM353.fermat_correction(value, prime)
        for coordinate in coordinates
        for value in coordinate
    ) % prime
    entropy_product = entropy_product_mod_p2(coordinates, prime)
    entropy_quotient = fermat_quotient(entropy_product, prime)
    if entropy_quotient != correction_sum:
        raise AssertionError("entropy-product Fermat quotient")

    coordinate_sum_residues = [sum(values) % prime for values in coordinates]
    if coordinate_sum_residues != [
        value["residue_digit"] for value in chosen_digits["coordinates"]
    ]:
        raise AssertionError("coordinate sum residues")

    if n == 2:
        if any(coordinates[0]):
            raise AssertionError("n=2 zero first coordinate")
        return {
            "classification": "PRESELECTED EXACT ZERO-RATE EDGE CONTROL; NOT A PRIME SCAN",
            "h": h,
            "s": s,
            "p": prime,
            "n": n,
            "r": r,
            "degenerate_weight": "b0=0",
            "entropy_product_mod_p2": entropy_product,
            "entropy_Fermat_quotient": entropy_quotient,
            "Fermat_correction_sum": correction_sum,
            "full_original_collision_claimed": False,
        }

    kappa = multiplicative_constant(n, r, prime)
    pointwise_nonzero_checks = 0
    carry_values = []
    for y0, y1, y2, y3 in zip(*coordinates):
        if (y0 * y3 - kappa * y1 * y1) % prime != 0:
            raise AssertionError("pointwise weighted multiplicative relation")
        if y0 and y1 and y3:
            difference_over_p = (y0 * y3 - kappa * y1 * y1) // prime
            common_residue = y0 * y3 % prime
            lhs = (
                fermat_quotient(y0, prime)
                + fermat_quotient(y3, prime)
                - fermat_quotient(kappa, prime)
                - 2 * fermat_quotient(y1, prime)
            ) % prime
            rhs = -difference_over_p * pow(common_residue, -1, prime) % prime
            if lhs != rhs:
                raise AssertionError(("canonical multiplicative carry", lhs, rhs))
            carry_values.append(rhs)
            pointwise_nonzero_checks += 1

    t0, t1, _, t3 = coordinate_sum_residues
    summed_relation_defect = (t0 * t3 - kappa * t1 * t1) % prime
    if summed_relation_defect == 0:
        raise AssertionError("declared sum unexpectedly preserves pointwise relation")

    entropy_exponent_sum = sum(
        value for coordinate in coordinates for value in coordinate if value
    )
    return {
        "classification": "PRESELECTED EXACT BULK CONTROL; NOT A PRIME SCAN",
        "h": h,
        "s": s,
        "M": 3 * h + 4 * s + 2,
        "p": prime,
        "n": n,
        "r": r,
        "kappa": kappa,
        "pointwise_relation": "y0*y2b=kappa*y1^2",
        "pointwise_nonzero_carry_checks": pointwise_nonzero_checks,
        "distinct_canonical_carry_values": len(set(carry_values)),
        "coordinate_sum_residues": coordinate_sum_residues,
        "summed_relation_defect": summed_relation_defect,
        "pointwise_relation_survives_summation": False,
        "entropy_product_mod_p2": entropy_product,
        "entropy_exponent_sum": entropy_exponent_sum,
        "entropy_Fermat_quotient": entropy_quotient,
        "Fermat_correction_sum": correction_sum,
        "full_original_collision_claimed": False,
    }


def direct_controls() -> list[dict[str, Any]]:
    rows = [
        (1, 1, 13),
        (2, 1, 17),
        (8, 2, 47),
        (4, 4, 43),
        (2, 6, 47),
    ]
    output = [row_control(*row) for row in rows]
    expected_bulk = [
        (1, 10),
        (6, 8),
        (37, 24),
        (26, 45),
    ]
    actual_bulk = [(row["kappa"], row["summed_relation_defect"]) for row in output[1:]]
    if actual_bulk != expected_bulk:
        raise AssertionError(("declared kappa and summed defects", actual_bulk))
    return output


def theorem_and_capacity() -> dict[str, Any]:
    return {
        "complete_multiplicative_lattice": {
            "unweighted": "R0*R2b=R1^2 and every integer multiplicative relation is a power of this one",
            "weighted_bulk":
                "for n>2, y0*y2b=kappa*y1^2 with kappa=(n-1)(n-2)(E-1)/((2n-3)^2 E)",
            "rank": "the four pointwise functions have multiplicative rank 3",
            "edge": "n=2 makes b0=0 and has zero-rate fixed-M support",
        },
        "Fermat_quotient_consequence": {
            "formal_phase_rank":
                "multiplicativity reduces four nonzero pointwise quotient phases to exactly three",
            "canonical_carry":
                "canonical residue reduction adds a varying quotient carry to q(y0)+q(y2b)-2q(y1)-q(kappa)",
            "coefficient_obstruction":
                "the first correction is sum y*q(y), not an unweighted sum q(y); eliminating q(y2b) leaves three nonzero varying coefficient functions plus the carry",
            "summation_obstruction":
                "the unique pointwise product relation does not survive the four additive Kummer sums",
        },
        "entropy_product": {
            "exact_compression":
                "sum_(nu,x) y_(nu,x) q_p(y_(nu,x)) = q_p(product_(nu,x) y_(nu,x)^(y_(nu,x))) mod p",
            "height": "log P <=4(p-1)^2 log(p-1)=O(p^2 log p)",
            "why_not_admissible":
                "the residue-dependent exponents and quadratic-logarithmic height do not define a bounded-degree rational-function norm or a positive-rate factor localization theorem",
        },
        "capacity": {
            "raw_support": "all actual rows outside a zero-rate n=2 edge",
            "new_forced_condition": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
            "booking": 0,
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item356-j1-fermat-multiplicative-collapse-obstruction-certificate-v1",
        "item": 356,
        "date": "2026-09-01",
        "status": "PROVED_COMPLETE_POINTWISE_MULTIPLICATIVE_LATTICE_AND_SCOPED_COLLAPSE_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic_relation_audit": symbolic_relation_audit(),
        "theorem_and_capacity": theorem_and_capacity(),
        "direct_controls": direct_controls(),
        "self_audit": {
            "ordinary_collision_direction_preserved": True,
            "pointwise_relation_promoted_to_sum_relation": False,
            "canonical_q_multiplicativity_used_without_carry": False,
            "entropy_product_called_bounded_height": False,
            "finite_controls_used_as_density_evidence": False,
            "ledger_booking_without_asymptotic_theorem": False,
        },
        "classification": {
            "PROVED": [
                "complete pointwise multiplicative relation lattice",
                "exact canonical Fermat-quotient carry for the unique relation",
                "three-phase coefficient obstruction",
                "failure of the pointwise relation after Kummer summation",
                "one-quotient entropy-product identity and its O(p^2 log p) height ceiling",
                "scoped multiplicativity-only collapse no-go",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "five predeclared rows; no prime scan or density inference"
            ],
            "OPEN": [
                "special additive identities among the summed Kummer coordinates",
                "a bounded-height factorization of the entropy product",
                "weighted nonconcentration for the surviving three-phase correction",
                "a second condition forced by full-collision information",
                "W_b(M)=o(M), any fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 356,
                "pointwise_multiplicative_rank": 3,
                "summed_relation": False,
                "bounded_height_collapse": False,
                "booking": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

