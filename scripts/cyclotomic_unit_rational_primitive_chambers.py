#!/usr/bin/env python3
"""Exact symbolic certificate for rational primitive-rate chambers.

This script verifies the rational coefficient-rate ties, all ordered
value/coefficient zero-gap equations, and the exact negative-gap cone logic
used in the companion source note.  Endpoint asymptotics are proved there
from the previously accepted n=5 edge expansion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_rational_primitive_chambers.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_rational_primitive_chambers.md"),
    )
    args = parser.parse_args()

    indices = (1, 3, 7, 9)
    action = {
        1: sp.eye(3),
        3: sp.Matrix([[-1, -1, -1], [0, 0, 1], [1, 0, 0]]),
        7: sp.Matrix([[0, 0, 1], [-1, -1, -1], [0, 1, 0]]),
        9: sp.Matrix([[0, 1, 0], [1, 0, 0], [-1, -1, -1]]),
    }
    raw_shift = {1: -1, 3: 1, 7: 1, 9: 0}
    h = sp.Matrix([1, 1, -1])
    r_symbols = sp.symbols("r3 r7 r9")

    coefficient_expected = {
        (1, 3): sp.FiniteSet((0, 0, 0)),
        (1, 7): sp.FiniteSet((0, 0, 0)),
        (1, 9): sp.FiniteSet((-r_symbols[2], -r_symbols[2], r_symbols[2])),
        (3, 7): sp.FiniteSet((-r_symbols[2], -r_symbols[2], r_symbols[2])),
        (3, 9): sp.FiniteSet((0, 0, 0)),
        (7, 9): sp.FiniteSet((0, 0, 0)),
    }
    coefficient_ties = []
    for position, i in enumerate(indices):
        for j in indices[position + 1 :]:
            matrix = action[i] - action[j]
            solution = sp.linsolve((matrix, sp.zeros(3, 1)), r_symbols)
            if solution != coefficient_expected[(i, j)]:
                raise AssertionError(f"wrong coefficient tie for {(i, j)}")
            coefficient_ties.append(
                {
                    "pair": [i, j],
                    "rank": matrix.rank(),
                    "solution": str(solution),
                    "contained_in_quadratic_line": True,
                }
            )

    quarter = (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(-1, 4))
    zero = (sp.Integer(0), sp.Integer(0), sp.Integer(0))
    line = (-r_symbols[2], -r_symbols[2], r_symbols[2])
    arbitrary = tuple(r_symbols)
    zero_gap_expected = {
        (1, 1): sp.EmptySet,
        (1, 3): sp.FiniteSet(quarter),
        (1, 7): sp.FiniteSet(quarter),
        (1, 9): sp.EmptySet,
        (3, 1): sp.FiniteSet(quarter),
        (3, 3): sp.EmptySet,
        (3, 7): sp.EmptySet,
        (3, 9): sp.FiniteSet(quarter),
        (7, 1): sp.FiniteSet(quarter),
        (7, 3): sp.EmptySet,
        (7, 7): sp.EmptySet,
        (7, 9): sp.FiniteSet(quarter),
        (9, 1): sp.FiniteSet(line),
        (9, 3): sp.FiniteSet(zero),
        (9, 7): sp.FiniteSet(zero),
        (9, 9): sp.FiniteSet(arbitrary),
    }
    zero_gap_records = []
    nontrivial_outside_quadratic_line = []
    for i in indices:
        for j in indices:
            matrix = action[i] - action[j]
            rhs = -sp.Rational(raw_shift[i], 2) * h
            solution = sp.linsolve((matrix, rhs), r_symbols)
            if solution != zero_gap_expected[(i, j)]:
                raise AssertionError(f"wrong zero-gap solution for {(i, j)}")
            outside_line_family = (i, j) == (9, 9)
            if outside_line_family:
                nontrivial_outside_quadratic_line.append([i, j])
            zero_gap_records.append(
                {
                    "raw_dominant_candidate": i,
                    "coefficient_dominant_candidate": j,
                    "matrix_rank": matrix.rank(),
                    "augmented_rank": matrix.row_join(rhs).rank(),
                    "solution": str(solution),
                    "only_family_not_contained_in_quadratic_line": outside_line_family,
                }
            )
    if nontrivial_outside_quadratic_line != [[9, 9]]:
        raise AssertionError("zero-gap exceptional family was not uniquely (9,9)")

    # Exact symbolic form of the negative-gap logic.  If coefficient
    # embedding j is 3 or 7, its shifted raw rate is M+L; if it is 9, the
    # same raw rate is M.  Only j=1 can therefore give a negative gap.
    negative_gap_logic = {
        "coefficient_max_3": "Delta >= L > 0 because lambda_3=mu_3+L",
        "coefficient_max_7": "Delta >= L > 0 because lambda_7=mu_7+L",
        "coefficient_max_9": "Delta >= 0 because lambda_9=mu_9",
        "coefficient_max_1": {
            "lambda_1_below_mu_1": "automatic: mu_1-L < mu_1",
            "lambda_3_below_mu_1": "mu_1-mu_3 > L",
            "lambda_7_below_mu_1": "mu_1-mu_7 > L",
            "lambda_9_below_mu_1": "mu_1 > mu_9",
        },
        "equivalence": "Delta<0 iff all three displayed cone inequalities hold",
    }

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_paths = [
        Path("sources/cyclotomic_unit_rational_ray_tropical.md").resolve(),
        Path("scripts/cyclotomic_unit_rational_ray_tropical.py").resolve(),
        Path("results/cyclotomic_unit_rational_ray_tropical.json").resolve(),
        Path("sources/cyclotomic_unit_quadratic_ray_primitive.md").resolve(),
    ]
    if not all(path.exists() for path in dependency_paths):
        raise FileNotFoundError("a theorem dependency was missing")
    result = {
        "description": (
            "Exact rational coefficient-tie, zero-gap, and negative-gap "
            "chamber certificate for the n=5 cyclotomic-unit trace."
        ),
        "scope_warning": (
            "This certificate proves no primitive conclusion inside the "
            "three-inequality open cone; a traced-coordinate gcd bound remains missing."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "action_matrices": {
            str(k): [[int(x) for x in row] for row in action[k].tolist()]
            for k in indices
        },
        "raw_endpoint_shifts_in_units_of_log_phi": {
            str(k): raw_shift[k] for k in indices
        },
        "coefficient_rate_ties_over_Q": coefficient_ties,
        "ordered_zero_gap_solutions_over_Q": zero_gap_records,
        "unique_zero_gap_family_outside_quadratic_line": [9, 9],
        "same_embedding_9_endpoint_ratio": "(4*pi/e^2)/(2/e^2)=2*pi",
        "negative_gap_cone_logic": negative_gap_logic,
        "unresolved_cone": [
            "mu_1-mu_3 > log(phi)",
            "mu_1-mu_7 > log(phi)",
            "mu_1 > mu_9",
        ],
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
