#!/usr/bin/env python3
"""Build the deterministic manifest for the Item 243 closure package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMARY = {
    "sources/item243_order6_gauge_closure_report.md": "portable proof report",
    "scripts/item243_order6_gauge_closure_certificate.py": "deterministic theorem assembler/checker",
    "scripts/item243_order6_gauge_closure_manifest.py": "deterministic package manifest builder",
    "results/item243_order6_gauge_closure_certificate.json": "canonical deterministic result",
    "results/item243_order6_gauge_closure_certificate.replay.json": "byte-identical portable replay",
    "results/item243_order6_gauge_closure_ledger.json": "strict proof, finite-only, open, and zero-booking ledger",
}

SUPPORTING_SCRIPTS = (
    "item243_defect_degree_grid_certificate.py",
    "item243_defect_specialization_probe.py",
    "item243_forward_cofactor_newton_certificate.py",
    "item243_forward_cofactor_origin_certificate.py",
    "item243_transition_pole_factor_probe.py",
    "item243_gosper_endpoint_audit.py",
    "item243_initial_layers_probe.py",
    "item243_tensor_operator_probe.py",
    "item243_defect_orbit_probe.py",
    "item243_gosper_direct_probe.py",
    "item243_cross_gosper_probe.py",
    "item243_univariate_recurrence_probe.py",
    "item243_cross_reconstruct.py",
    "item237_residual_probe.py",
)

SUPPORTING_RESULTS = (
    "item243_defect_degree_grid_certificate.json",
    "item243_forward_cofactor_newton_certificate.json",
    "item243_forward_cofactor_origin_certificate.json",
    "item243_transition_pole_factor_probe.json",
    "item243_gosper_endpoint_audit.json",
    "item243_initial_layers_probe.json",
    "item243_tensor_operator_probe.json",
    "item243_defect_orbit_probe.json",
    "item243_univariate_recurrence_probe.json",
    "item243_cross_reconstruct.json",
    "item243_direct_r1_x.json",
    "item243_direct_r1_v.json",
    "item243_direct_r2_x.json",
    "item243_direct_r2_v.json",
    "item243_cross_gosper_r1_xu.json",
    "item243_cross_gosper_r1_yv.json",
    "item243_cross_gosper_r2_xu.json",
    "item243_cross_gosper_r2_yv.json",
)

DEPENDENCIES = (
    "scripts/item222_j1_phase_resultant_certificate.py",
    "scripts/item229_j1_fixed_h_theta_certificate.py",
    "scripts/item231_j1_second_phase_coefficient_certificate.py",
    "scripts/item236_j1_phase_cokernel_certificate.py",
    "scripts/item237_j1_algebraic_residual_certificate.py",
    "results/item237_j1_algebraic_residual_certificate.json",
)


def digest(path):
    answer = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            answer.update(block)
    return answer.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.archive.resolve()
    files = dict(PRIMARY)
    for name in SUPPORTING_SCRIPTS:
        files[f"scripts/{name}"] = "supporting exact checker or reconstruction source"
    for name in SUPPORTING_RESULTS:
        files[f"results/{name}"] = "supporting exact certificate/input"
    encoded = {}
    for relative, role in files.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        encoded[relative] = {"role": role, "sha256": digest(path)}
    dependencies = {}
    for relative in DEPENDENCIES:
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        dependencies[relative] = digest(path)
    canonical = encoded["results/item243_order6_gauge_closure_certificate.json"]["sha256"]
    replay = encoded["results/item243_order6_gauge_closure_certificate.replay.json"]["sha256"]
    if canonical != replay:
        raise AssertionError("canonical/replay mismatch")
    report_text = (root / "sources/item243_order6_gauge_closure_report.md").read_text(
        encoding="utf-8"
    )
    delimiter_audit = {
        "inline_open": report_text.count(r"\("),
        "inline_close": report_text.count(r"\)"),
        "display_open": report_text.count(r"\["),
        "display_close": report_text.count(r"\]"),
        "forbidden_control_characters": [
            ord(character)
            for character in report_text
            if ord(character) < 32 and character not in "\n\r\t"
        ],
    }
    if delimiter_audit["inline_open"] != delimiter_audit["inline_close"]:
        raise AssertionError(("unbalanced inline math", delimiter_audit))
    if delimiter_audit["display_open"] != delimiter_audit["display_close"]:
        raise AssertionError(("unbalanced display math", delimiter_audit))
    if delimiter_audit["forbidden_control_characters"]:
        raise AssertionError(("control characters", delimiter_audit))
    result = {
        "schema": "item243-order6-gauge-closure-manifest-v1",
        "files": encoded,
        "dependencies": dependencies,
        "canonical_command_from_archive_root": (
            "python scripts/item243_order6_gauge_closure_certificate.py "
            "--output results/item243_order6_gauge_closure_certificate.json"
        ),
        "replay_command_from_archive_root": (
            "python scripts/item243_order6_gauge_closure_certificate.py "
            "--output results/item243_order6_gauge_closure_certificate.replay.json"
        ),
        "determinism": {
            "canonical_replay_byte_identical": True,
            "sha256": canonical,
            "randomness": False,
            "timestamps_in_output": False,
            "host_paths_in_output": False,
        },
        "report_text_audit": delimiter_audit,
        "strict_labels": {
            "actual_order6_defect_closure": "PROVED",
            "all_h_gauged_E_recurrence": "PROVED",
            "all_h_gauge_identity": "PROVED",
            "ambient_one_step_covector_no_go": "PROVED",
            "finite_field_orbits": "EXACT FINITE ONLY",
            "moving_prime_nonvanishing": "OPEN; NOT PROVED",
            "positive_Route1_rate": "OPEN; NOT PROVED",
            "booking": "zero new rate, divisibility exponent, and capacity reduction",
        },
    }
    output = args.output or root / "manifests/item243_order6_gauge_closure_manifest.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output), "files": len(encoded)}, sort_keys=True))


if __name__ == "__main__":
    main()
