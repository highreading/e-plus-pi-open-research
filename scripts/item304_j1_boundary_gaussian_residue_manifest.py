#!/usr/bin/env python3
"""Build the deterministic manifest for the sealed Item 304 package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMARY = {
    "sources/item304_j1_boundary_gaussian_residue_report.md": (
        "portable all-H Gaussian residue theorem and capacity report"
    ),
    "scripts/item304_j1_boundary_gaussian_residue_certificate.py": (
        "deterministic exact Gaussian numerator checker"
    ),
    "scripts/item304_j1_boundary_gaussian_residue_manifest.py": (
        "deterministic package manifest builder"
    ),
    "results/item304_j1_boundary_gaussian_residue_certificate.json": (
        "canonical deterministic result"
    ),
    "results/item304_j1_boundary_gaussian_residue_certificate.replay.json": (
        "byte-identical deterministic replay"
    ),
    "results/item304_j1_boundary_gaussian_residue_ledger.json": (
        "strict proof, scope, open, and capacity ledger"
    ),
}

DEPENDENCIES = {
    "scripts/item297_j1_structural_ray_boundary_certificate.py": (
        "6baec559198b0055096717f3e2fb7551707a17b64f520e499e585c73a4441cb5"
    ),
    "results/item297_j1_structural_ray_boundary_certificate.json": (
        "aa84dde588a119c67b868266ca536699b3675d2e53cb62ad8f1df66705ca7e6b"
    ),
    "scripts/item301_j1_boundary_scalar_reduction_certificate.py": (
        "a333101b2112abe4dc59c1c7d2f2237e41f7a6546606eb7283d55854140a56e4"
    ),
    "results/item301_j1_boundary_scalar_reduction_certificate.json": (
        "f25813facfe8befb751fdbcd1c5f521c23379162bd44244356c8b2568d9fc784"
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
        "results/item304_j1_boundary_gaussian_residue_certificate.json"
    ]["sha256"]
    replay = files[
        "results/item304_j1_boundary_gaussian_residue_certificate.replay.json"
    ]["sha256"]
    if canonical != replay:
        raise AssertionError("canonical/replay mismatch")

    report_path = root / "sources/item304_j1_boundary_gaussian_residue_report.md"
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
        "schema": "item304-j1-boundary-gaussian-residue-manifest-v1",
        "files": files,
        "dependencies": dependencies,
        "canonical_command_from_archive_root": (
            "python scripts/item304_j1_boundary_gaussian_residue_certificate.py "
            "--output results/item304_j1_boundary_gaussian_residue_certificate.json"
        ),
        "replay_command_from_archive_root": (
            "python scripts/item304_j1_boundary_gaussian_residue_certificate.py "
            "--output results/item304_j1_boundary_gaussian_residue_certificate.replay.json"
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
            "Gaussian_integer_numerator_recurrence": "PROVED ALL n",
            "moving_prime_specialization": "PROVED ALL ACTUAL BOUNDARIES",
            "B_H_nonvanishing": "PROVED ALL ACTUAL BOUNDARIES",
            "pinned_E_nonvanishing_or_weighted_density": "OPEN",
            "retained_conditional_capacity_per_6m": "1/36",
            "booking": "zero new rate, divisibility exponent, and capacity reduction",
        },
    }

    output = arguments.output or (
        root / "manifests/item304_j1_boundary_gaussian_residue_manifest.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    hash_list = arguments.hash_list or (
        root / "results/item304_j1_boundary_gaussian_residue_hashes.sha256"
    )
    listed = dict(files)
    listed["manifests/item304_j1_boundary_gaussian_residue_manifest.json"] = {
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
