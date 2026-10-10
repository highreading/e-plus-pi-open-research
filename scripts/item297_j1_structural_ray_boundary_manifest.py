#!/usr/bin/env python3
"""Build the deterministic manifest for the sealed Item 297 package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMARY = {
    "sources/item297_j1_structural_ray_boundary_report.md": (
        "portable exact boundary-renormalization theorem and scope report"
    ),
    "scripts/item297_j1_structural_ray_boundary_certificate.py": (
        "deterministic exact boundary and overlap checker"
    ),
    "scripts/item297_j1_structural_ray_boundary_manifest.py": (
        "deterministic package manifest builder"
    ),
    "results/item297_j1_structural_ray_boundary_certificate.json": (
        "canonical deterministic result"
    ),
    "results/item297_j1_structural_ray_boundary_certificate.replay.json": (
        "byte-identical deterministic replay"
    ),
    "results/item297_j1_structural_ray_boundary_ledger.json": (
        "strict proof, scope, open, and capacity ledger"
    ),
}

DEPENDENCIES = {
    "scripts/item222_j1_phase_resultant_certificate.py": (
        "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b"
    ),
    "scripts/item229_j1_fixed_h_theta_certificate.py": (
        "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f"
    ),
    "scripts/item237_j1_algebraic_residual_certificate.py": (
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf"
    ),
    "results/item237_j1_algebraic_residual_certificate.json": (
        "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b"
    ),
    "scripts/item296_j1_modular_singular_ray_atlas_certificate.py": (
        "caa3bc55969e300a3426bd078d78f2ab6003a3e0fae5f65b802c7ca610554646"
    ),
    "results/item296_j1_modular_singular_ray_atlas_certificate.json": (
        "909da750976707960c8ba3b01a4e0456d970134bfa32d6e3235472dad4a7a0ab"
    ),
}


def digest(path: Path) -> str:
    answer = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            answer.update(block)
    return answer.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--hash-list", type=Path)
    arguments = parser.parse_args()
    root = arguments.archive.resolve()

    files = {}
    for relative, role in PRIMARY.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        files[relative] = {"role": role, "sha256": digest(path)}

    dependencies = {}
    for relative, expected in DEPENDENCIES.items():
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        observed = digest(path)
        if observed != expected:
            raise AssertionError(("dependency hash", relative, observed, expected))
        dependencies[relative] = observed

    canonical = files[
        "results/item297_j1_structural_ray_boundary_certificate.json"
    ]["sha256"]
    replay = files[
        "results/item297_j1_structural_ray_boundary_certificate.replay.json"
    ]["sha256"]
    if canonical != replay:
        raise AssertionError("canonical/replay mismatch")

    report_path = root / "sources/item297_j1_structural_ray_boundary_report.md"
    report_text = report_path.read_text(encoding="utf-8")
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
        "schema": "item297-j1-structural-ray-boundary-manifest-v2",
        "files": files,
        "dependencies": dependencies,
        "canonical_command_from_archive_root": (
            "python scripts/item297_j1_structural_ray_boundary_certificate.py "
            "--output results/item297_j1_structural_ray_boundary_certificate.json"
        ),
        "replay_command_from_archive_root": (
            "python scripts/item297_j1_structural_ray_boundary_certificate.py "
            "--output results/item297_j1_structural_ray_boundary_certificate.replay.json"
        ),
        "determinism": {
            "canonical_replay_byte_identical": True,
            "sha256": canonical,
            "randomness": False,
            "timestamps_in_output": False,
            "host_paths_in_output": False,
            "actual_prime_scan": False,
        },
        "report_text_audit": delimiter_audit,
        "strict_labels": {
            "boundary_renormalization": "PROVED",
            "all_H_pochhammer_and_denominator_audit": "PROVED",
            "all_H_gauge_valuation_audit": "PROVED",
            "fixed_core_overlap_table": "PROVED",
            "actual_orbit_reduced_relations": "PROVED",
            "generic_lower_order_recurrence": "REFUTED BY POLE CANCELLATION",
            "actual_E_nonvanishing_or_weighted_density": "OPEN",
            "retained_conditional_capacity_per_6m": "1/36",
            "booking": "zero new rate, divisibility exponent, and capacity reduction",
        },
    }

    output = arguments.output or (
        root / "manifests/item297_j1_structural_ray_boundary_manifest.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    hash_list = arguments.hash_list or (
        root / "results/item297_j1_structural_ray_boundary_hashes.sha256"
    )
    listed = dict(files)
    listed["manifests/item297_j1_structural_ray_boundary_manifest.json"] = {
        "sha256": digest(output)
    }
    lines = [f"{data['sha256']}  {relative}" for relative, data in sorted(listed.items())]
    hash_list.write_text("\n".join(lines) + "\n", encoding="ascii", newline="\n")
    print(
        json.dumps(
            {
                "output": str(output),
                "hash_list": str(hash_list),
                "primary_files": len(files),
                "dependencies": len(dependencies),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
