#!/usr/bin/env python3
"""Assemble the proved Item 243 actual-family order-six gauge closure."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


INPUTS = (
    "item243_defect_degree_grid_certificate.json",
    "item243_forward_cofactor_newton_certificate.json",
    "item243_forward_cofactor_origin_certificate.json",
    "item243_transition_pole_factor_probe.json",
    "item243_gosper_endpoint_audit.json",
    "item243_initial_layers_probe.json",
    "item243_tensor_operator_probe.json",
    "item243_defect_orbit_probe.json",
    "item237_j1_algebraic_residual_certificate.json",
)


def input_path(name):
    for candidate in (HERE / name, HERE.parent / "results" / name):
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def read(name):
    return json.loads(input_path(name).read_text())


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def certificate():
    degree_grid = read(INPUTS[0])
    newton = read(INPUTS[1])
    origin = read(INPUTS[2])
    poles = read(INPUTS[3])
    endpoints = read(INPUTS[4])
    initials = read(INPUTS[5])
    ambient_no_go = read(INPUTS[6])
    finite_orbits = read(INPUTS[7])
    item237 = read(INPUTS[8])

    require(
        degree_grid["classification"] == "PROVED_EXACT_DEGREE_GRID_IDENTITY",
        "ambient degree-grid classification",
    )
    ledger = degree_grid["degree_ledger"]
    require(ledger["defect_common_numerator_degree"] == 206, "defect degree")
    require(ledger["joint_transition_common_degree"] == 22, "joint degree")
    require(ledger["v_transition_common_degree"] == 16, "v degree")
    require(
        ledger["cofactor_relation_coordinate_numerator_degree_bound"] == 2240,
        "relation degree",
    )
    require(
        all(row["regular_exact_rows"] == 2241 for row in degree_grid["residue_certificates"]),
        "degree-grid row count",
    )
    forward_degree = sum(206 + 38 * shift for shift in range(6))
    require(forward_degree == 1806, "forward cofactor degree derivation")

    require(len(newton["residues"]) == 2, "Newton residues")
    for row in newton["residues"]:
        require(row["degree_bound"] == forward_degree, "Newton degree bound")
        require(row["values_checked"] == forward_degree + 2, "Newton values")
        require(row["terminal_difference_order"] == forward_degree + 1, "terminal order")
        require(row["terminal_difference_zero"] is True, "terminal difference")
        require(row["positive_coefficients"] == 0, "positive Newton coefficient")
        require(row["negative_coefficients"] == 1804, "negative coefficient count")
        require(row["zero_coefficients"] == 3, "zero coefficient count")
        require(row["common_nonzero_sign"] == -1, "Newton sign")
    for row in origin["rows"]:
        require(row["newton_coefficient_index"] == 0, "origin index")
        require(row["strict_sign"] == -1 and row["nonzero"], "origin sign")

    require(
        poles["classification"]
        == "PROVED_EXACT_NO_NONNEGATIVE_TRANSITION_POLES",
        "transition pole theorem",
    )
    require(
        all(
            residue["all_transition_denominators_nonzero_for_n_ge_0"]
            for residue in poles["residues"]
        ),
        "transition divisor",
    )
    require(
        endpoints["classification"] == "PROVED_EXACT_GOSPER_ENDPOINTS",
        "endpoint theorem",
    )
    require(len(endpoints["entries"]) == 8, "endpoint entry count")
    require(
        endpoints["exceptional_bridges"][0]["sum"] == [0, 1],
        "exceptional r2 v bridge",
    )

    gauge_rows = initials["gauge_initial_layer"]["rows"]
    defect_rows = initials["defect_initial_layer"]["rows"]
    require(len(gauge_rows) == 6, "gauge initial count")
    require(len(defect_rows) == 12, "defect initial count")
    require(all(row["difference"] == [0, 1] for row in gauge_rows), "gauge initials")
    require(all(row["defect"] == [0, 1] for row in defect_rows), "defect initials")

    require(
        ambient_no_go["classification"] == "PROVED_EXACT_AMBIENT_COVECTOR_NO_GO",
        "ambient no-go classification",
    )
    require(
        all(len(row["nonzero_coordinates"]) == 15 for row in ambient_no_go["residues"]),
        "ambient no-go coordinates",
    )
    require(finite_orbits["classification"] == "EXACT_FINITE_ONLY", "finite label")
    require(len(finite_orbits["rows"]) == 6, "finite orbit rows")
    require(
        all(row["result"]["order"] == 6 for row in finite_orbits["rows"]),
        "finite orbit order",
    )

    recurrence = item237["all_h_recurrence"]
    require(recurrence["cleared_numerator_zero"] is True, "Item 237 recurrence")
    p3 = recurrence["factored_coefficients"][3]
    require(p3["scalar"].startswith("1/"), "p3 scalar")
    require(all(value > 0 for value in p3["remaining_core_low_to_high"]), "p3 core")
    require(
        all(root[0] < 0 and root[1] > 0 for root in p3["linear_factor_roots_numerator_denominator"]),
        "p3 roots",
    )

    input_hashes = {name: sha256(input_path(name)) for name in INPUTS}
    return {
        "item": 243,
        "classification": "PROVED_EXACT_ACTUAL_FAMILY_ORDER6_GAUGE_CLOSURE",
        "theorems": {
            "actual_defect_recurrence": (
                "For each r=1,2, the actual gauged-recurrence defect delta_r(n) "
                "satisfies an exact rational order-six recurrence for every n>=0."
            ),
            "forward_coefficient": (
                "The cleared forward cofactor C6 has degree <=1806 and C6(n)<0 "
                "for every integer n>=0; every structural multiplier B6 is nonzero."
            ),
            "gauged_E_recurrence": (
                "sum_(k=0)^3 p_k(h)(product_(j=0)^(k-1)rho(h+3j))"
                "E_(h+3k)^*=0 for all h>=1 with 3 not dividing h."
            ),
            "all_h_gauge": (
                "c_h^*=R_h E_h^* for all h>=1 with 3 not dividing h."
            ),
        },
        "degree_and_newton_ledger": {
            "defect_cleared_numerator_degree": 206,
            "transport_increment_per_step": 38,
            "forward_cofactor_degree_bound": "sum_(j=0)^5(206+38j)=1806",
            "ambient_relation_coordinate_degree_bound": 2240,
            "ambient_regular_roots_per_residue": 2241,
            "residues": newton["residues"],
            "origin_rows": origin["rows"],
        },
        "two_initial_layers": {
            "defect_propagation": {
                "required": "six delta initials per residue",
                "proved_count": 12,
                "stream_sha256": initials["defect_initial_layer"]["row_stream_sha256"],
            },
            "gauge_transfer": {
                "required": "three c=R E initials per residue",
                "proved_count": 6,
                "stream_sha256": initials["gauge_initial_layer"]["row_stream_sha256"],
            },
        },
        "logical_chain": [
            "Exact Gosper interior certificates plus the endpoint/pole audit make the x/v and xu/yv transitions valid on the actual finite sums.",
            "The 2241-root degree theorem gives a signed-cofactor relation among seven transported ambient defect covectors.",
            "The degree-1806 Newton certificate and strict negative index-zero coefficient make the forward coefficient nonzero at every n>=0.",
            "The twelve exact defect initials therefore propagate to the all-h gauged E recurrence.",
            "Item 237's proved order-three c recurrence has p3(h)>0, and the six separate gauge initials propagate c_h^*=R_h E_h^*.",
        ],
        "ambient_covector_no_go": "PROVED_EXACT: the one-step defect covector is nonzero in all 15 ambient coordinates in both residues.",
        "finite_field_orbit_evidence": "EXACT_FINITE_ONLY: six order-six orbit specializations modulo 1000000007.",
        "capacity_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction_booked": 0,
            "reason": (
                "The gauge closure removes the algebraic identity barrier but "
                "does not prove moving-row-prime nonvanishing, the simultaneous "
                "endpoint K_h condition, a density estimate, or a radical saving."
            ),
        },
        "strict_scope": {
            "PROVED": [
                "actual-family order-six defect closure in both residues",
                "the all-h gauged E recurrence",
                "the all-h gauge identity c_h^*=R_h E_h^*",
                "the ambient one-step covector no-go",
            ],
            "EXACT_FINITE_ONLY": [
                "the six finite-field orbit samples",
                "all unrelated finite prime/gcd patterns inherited from Items 222/237",
            ],
            "OPEN": [
                "moving-row-prime nonvanishing or exclusion",
                "a unit-localized all-h K/E theorem",
                "any positive Route-1 rate, capacity, density, or radical saving",
                "any conclusion about the irrationality of e+pi",
            ],
        },
        "input_sha256": input_hashes,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item243_order6_gauge_closure_certificate.json",
    )
    args = parser.parse_args()
    result = certificate()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {"output": str(args.output), "classification": result["classification"]},
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
