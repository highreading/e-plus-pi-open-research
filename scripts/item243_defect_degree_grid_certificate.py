#!/usr/bin/env python3
"""Exact degree-grid theorem for the Item 243 ambient defect recurrence.

For each residue, the seven transported defect covectors are rational vectors
R_j(n) in Q(n)^15.  A common denominator B_j(n) clears every coordinate of
column j, yielding polynomial columns A_j=B_j R_j.  The signed six-by-six
cofactors of the first six coordinate rows give a seven-column relation.
Every coordinate numerator in that relation has degree at most 2240.  Exact
vanishing at 2241 regular integer arguments therefore proves the relation in
Q(n), not just on a finite sample.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


special = load(
    "item243_degree_grid_specialization",
    "item243_defect_specialization_probe.py",
)


def actual_degree(flat, block_degree):
    answer = -1
    for offset in range(0, len(flat), block_degree + 1):
        block = flat[offset : offset + block_degree + 1]
        for degree, pair in enumerate(block):
            if pair[0]:
                answer = max(answer, degree)
    return answer


def degree_ledger():
    recurrences = json.loads(
        (HERE / "item243_univariate_recurrence_probe.json").read_text()
    )["recurrences"]
    relations = json.loads(
        (HERE / "item243_cross_reconstruct.json").read_text()
    )["relations"]
    observed = {
        "x_recurrence_polynomial_degree": max(
            actual_degree(recurrences[f"r{residue}_x"], 15)
            for residue in (1, 2)
        ),
        "v_recurrence_polynomial_degree": max(
            actual_degree(recurrences[f"r{residue}_v"], 16)
            for residue in (1, 2)
        ),
        "xu_relation_polynomial_degree": max(
            actual_degree(relations[f"r{residue}_xu"], 7)
            for residue in (1, 2)
        ),
        "yv_relation_polynomial_degree": max(
            actual_degree(relations[f"r{residue}_yv"], 12)
            for residue in (1, 2)
        ),
    }
    declared = {
        "x_recurrence_polynomial_degree": 15,
        "v_recurrence_polynomial_degree": 16,
        "xu_relation_polynomial_degree": 7,
        "yv_relation_polynomial_degree": 12,
    }
    if any(observed[key] > value for key, value in declared.items()):
        raise AssertionError((observed, declared))

    # A joint transition has a common denominator equal to the product of
    # the x-leading and xu-leading polynomials: degree at most 15+7=22.
    joint_degree = 15 + 7
    v_degree = 16
    y_degree = 12
    rho_degree = 8
    scalar_degree = 1
    recurrence_degree = 16

    # The four defect terms use shifts k=0,1,2,3.  One common denominator
    # contains three rho denominators, four scalar denominators, three joint
    # transition denominators, three v transition denominators, and four y
    # denominators.
    defect_denominator_degree = (
        3 * rho_degree
        + 4 * scalar_degree
        + 3 * joint_degree
        + 3 * v_degree
        + 4 * y_degree
    )
    if defect_denominator_degree != 190:
        raise AssertionError(defect_denominator_degree)

    # For either xv or uy, after lifting a term to that common denominator,
    # the polynomial numerator has degree at most 206.  The formula below
    # checks both families and all four shifts.
    lifted_term_degrees = []
    for shift in range(4):
        xv_num = recurrence_degree + rho_degree * shift + scalar_degree + joint_degree * shift + v_degree * shift
        xv_den = rho_degree * shift + scalar_degree + joint_degree * shift + v_degree * shift
        uy_num = recurrence_degree + rho_degree * shift + scalar_degree + joint_degree * shift + y_degree + v_degree * shift
        uy_den = rho_degree * shift + scalar_degree + joint_degree * shift + y_degree + v_degree * shift
        lifted_term_degrees.extend(
            [
                xv_num + defect_denominator_degree - xv_den,
                uy_num + defect_denominator_degree - uy_den,
            ]
        )
    defect_numerator_degree = max(lifted_term_degrees)
    if defect_numerator_degree != 206:
        raise AssertionError(defect_numerator_degree)

    # Transporting the base defect through j joint/v transitions adds 38j
    # to both its common numerator and denominator degrees.
    column_numerator_degrees = [
        defect_numerator_degree + (joint_degree + v_degree) * shift
        for shift in range(7)
    ]
    column_denominator_degrees = [
        defect_denominator_degree + (joint_degree + v_degree) * shift
        for shift in range(7)
    ]
    relation_numerator_degree = sum(column_numerator_degrees)
    if relation_numerator_degree != 2240:
        raise AssertionError(relation_numerator_degree)
    return {
        "observed_input_degrees": observed,
        "declared_input_upper_bounds": declared,
        "joint_transition_common_degree": joint_degree,
        "v_transition_common_degree": v_degree,
        "y_row_common_degree": y_degree,
        "rho_numerator_denominator_degree": rho_degree,
        "defect_common_denominator_degree": defect_denominator_degree,
        "defect_common_numerator_degree": defect_numerator_degree,
        "orbit_column_numerator_degrees": column_numerator_degrees,
        "orbit_column_denominator_degrees": column_denominator_degrees,
        "cofactor_relation_coordinate_numerator_degree_bound": relation_numerator_degree,
        "required_regular_roots": relation_numerator_degree + 1,
    }


def prove_residue(residue, maximum, progress):
    system = special.build_system(residue)
    digest = hashlib.sha256()
    for initial in range(maximum + 1):
        current = special.prove_specialization_with_system(
            residue, initial, system, compact=True
        )
        if current["projection_rank"] != 6 or current["nonzero_coordinates"]:
            raise AssertionError(current)
        row = [residue, initial, 6, current["nonzero_coordinates"]]
        digest.update(json.dumps(row, separators=(",", ":")).encode("ascii"))
        digest.update(b"\n")
        if progress and (initial + 1) % progress == 0:
            print(
                json.dumps(
                    {
                        "residue": residue,
                        "completed": initial + 1,
                        "required": maximum + 1,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    return {
        "residue": residue,
        "initial_index_min": 0,
        "initial_index_max": maximum,
        "regular_exact_rows": maximum + 1,
        "projection_rank_everywhere": 6,
        "nonzero_coordinate_rows": 0,
        "row_stream_sha256": digest.hexdigest(),
    }


def certificate(progress):
    ledger = degree_ledger()
    bound = ledger["cofactor_relation_coordinate_numerator_degree_bound"]
    residues = [prove_residue(residue, bound, progress) for residue in (1, 2)]
    return {
        "item": 243,
        "classification": "PROVED_EXACT_DEGREE_GRID_IDENTITY",
        "theorem": (
            "For each residue h=3n+r, r in {1,2}, the seven transported "
            "ambient defect covectors satisfy the signed six-row cofactor "
            "relation identically over Q(n)."
        ),
        "logical_basis": (
            "Every cleared coordinate numerator has degree at most 2240; "
            "the exact relation vanishes at 2241 regular consecutive integer "
            "arguments with projection rank six."
        ),
        "scope_warning": (
            "This proves ambient rational closure. Propagation of actual defect "
            "zeros still requires a leading-cofactor nonvanishing audit at all "
            "nonnegative integer indices."
        ),
        "degree_ledger": ledger,
        "residue_certificates": residues,
        "capacity_booking": 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", type=int, default=100)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item243_defect_degree_grid_certificate.json",
    )
    args = parser.parse_args()
    result = certificate(args.progress)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "rows": sum(
                    entry["regular_exact_rows"]
                    for entry in result["residue_certificates"]
                ),
            },
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
