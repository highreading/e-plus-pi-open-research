#!/usr/bin/env python3
"""Build the deterministic manifest for the Item 293 E-gate package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMARY = {
    "sources/item293_j1_E_gate_density_no_go_report.md": "portable recurrence, height, and scoped no-go report",
    "scripts/item293_j1_E_gate_density_no_go_certificate.py": "deterministic symbolic checker",
    "scripts/item293_j1_E_gate_density_no_go_manifest.py": "deterministic package manifest builder",
    "results/item293_j1_E_gate_density_no_go_certificate.json": "canonical deterministic result",
    "results/item293_j1_E_gate_density_no_go_certificate.replay.json": "byte-identical deterministic replay",
    "results/item293_j1_E_gate_density_no_go_ledger.json": "strict proof, scope, open, and capacity ledger",
}

DEPENDENCIES = (
    "scripts/item222_j1_phase_resultant_certificate.py",
    "scripts/item229_j1_fixed_h_theta_certificate.py",
    "scripts/item237_j1_algebraic_residual_certificate.py",
    "results/item237_j1_algebraic_residual_certificate.json",
    "scripts/item243_order6_gauge_closure_certificate.py",
    "results/item243_order6_gauge_closure_certificate.json",
    "scripts/item288_j1_large_prime_redundancy_certificate.py",
    "results/item288_j1_large_prime_redundancy_certificate.json",
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

    canonical = files["results/item293_j1_E_gate_density_no_go_certificate.json"]["sha256"]
    replay = files["results/item293_j1_E_gate_density_no_go_certificate.replay.json"]["sha256"]
    if canonical != replay:
        raise AssertionError("canonical/replay mismatch")

    report_path = root / "sources/item293_j1_E_gate_density_no_go_report.md"
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
        "schema": "item293-j1-E-gate-density-no-go-manifest-v1",
        "files": files,
        "dependencies": dependencies,
        "canonical_command_from_archive_root": (
            "python scripts/item293_j1_E_gate_density_no_go_certificate.py "
            "--output results/item293_j1_E_gate_density_no_go_certificate.json"
        ),
        "replay_command_from_archive_root": (
            "python scripts/item293_j1_E_gate_density_no_go_certificate.py "
            "--output results/item293_j1_E_gate_density_no_go_certificate.replay.json"
        ),
        "determinism": {
            "canonical_replay_byte_identical": True,
            "sha256": canonical,
            "randomness": False,
            "timestamps_in_output": False,
            "host_paths_in_output": False,
            "prime_search": False,
        },
        "report_text_audit": delimiter_audit,
        "strict_labels": {
            "primitive_integral_E_recurrence": "PROVED",
            "rational_sign_theorem": "PROVED",
            "large_prime_part_algebraic_bridge": "PROVED",
            "holonomy_height_information_class_no_go": "PROVED; NARROW SCOPE",
            "sequence_specific_weighted_o_H": "OPEN",
            "retained_conditional_capacity_per_6m": "1/36",
            "booking": "zero new rate, divisibility exponent, and capacity reduction",
        },
    }

    output = arguments.output or root / "manifests/item293_j1_E_gate_density_no_go_manifest.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    hash_list = arguments.hash_list or root / "results/item293_j1_E_gate_density_no_go_hashes.sha256"
    listed = dict(files)
    listed["manifests/item293_j1_E_gate_density_no_go_manifest.json"] = {
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
