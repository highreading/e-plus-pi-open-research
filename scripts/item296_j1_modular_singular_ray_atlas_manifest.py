#!/usr/bin/env python3
"""Build the deterministic manifest for the sealed Item 296 package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMARY = {
    "sources/item296_j1_modular_singular_ray_atlas_report.md": "portable exact theorem and scope report",
    "scripts/item296_j1_modular_singular_ray_atlas_certificate.py": "deterministic exact atlas checker",
    "scripts/item296_j1_modular_singular_ray_atlas_manifest.py": "deterministic package manifest builder",
    "results/item296_j1_modular_singular_ray_atlas_certificate.json": "canonical deterministic result",
    "results/item296_j1_modular_singular_ray_atlas_certificate.replay.json": "byte-identical deterministic replay",
    "results/item296_j1_modular_singular_ray_atlas_ledger.json": "strict proof, scope, open, and capacity ledger"
}

DEPENDENCIES = (
    "scripts/item293_j1_E_gate_density_no_go_certificate.py",
    "results/item293_j1_E_gate_density_no_go_certificate.json",
)


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
    for relative in DEPENDENCIES:
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        dependencies[relative] = digest(path)

    expected_dependencies = {
        "scripts/item293_j1_E_gate_density_no_go_certificate.py": (
            "2aaa465558d224e1115764fd399a33e07cbc411d57085eefdfcf149ccbb14657"
        ),
        "results/item293_j1_E_gate_density_no_go_certificate.json": (
            "7af9fd9fe5e6bff2a0402c142479bbca0632c9b5e0f8591a29b41741e1be81f7"
        ),
    }
    if dependencies != expected_dependencies:
        raise AssertionError(("dependency hashes", dependencies))

    canonical = files[
        "results/item296_j1_modular_singular_ray_atlas_certificate.json"
    ]["sha256"]
    replay = files[
        "results/item296_j1_modular_singular_ray_atlas_certificate.replay.json"
    ]["sha256"]
    if canonical != replay:
        raise AssertionError("canonical/replay mismatch")

    report_path = root / "sources/item296_j1_modular_singular_ray_atlas_report.md"
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
        "schema": "item296-j1-modular-singular-ray-atlas-manifest-v1",
        "files": files,
        "dependencies": dependencies,
        "canonical_command_from_archive_root": (
            "python scripts/item296_j1_modular_singular_ray_atlas_certificate.py "
            "--output results/item296_j1_modular_singular_ray_atlas_certificate.json"
        ),
        "replay_command_from_archive_root": (
            "python scripts/item296_j1_modular_singular_ray_atlas_certificate.py "
            "--output results/item296_j1_modular_singular_ray_atlas_certificate.replay.json"
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
            "complete_linear_factor_atlas": "PROVED",
            "primitive_core_congruence_atlas": "PROVED",
            "regular_same_characteristic_transport": "PROVED",
            "unrestricted_state_zero_hyperplane": "PROVED; NARROW SCOPE",
            "pinned_actual_E_orbit_nonvanishing_or_density": "OPEN",
            "retained_conditional_capacity_per_6m": "1/36",
            "booking": "zero new rate, divisibility exponent, and capacity reduction",
        },
    }

    output = arguments.output or (
        root / "manifests/item296_j1_modular_singular_ray_atlas_manifest.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    hash_list = arguments.hash_list or (
        root / "results/item296_j1_modular_singular_ray_atlas_hashes.sha256"
    )
    listed = dict(files)
    listed["manifests/item296_j1_modular_singular_ray_atlas_manifest.json"] = {
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
