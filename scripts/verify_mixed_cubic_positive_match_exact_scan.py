#!/usr/bin/env python3
"""Verify the structural and exact-comparison layer of an enhanced scan.

Expected certificate schema (v2)
--------------------------------

The verifier deliberately does not import either computational source.  It
checks a JSON object with these required high-level fields::

    {
      "schema": "mixed-cubic-positive-match-exact-scan-v2",
      "generator": {"filename": "...", "sha256": "..."},
      "scope": {
        "m": [1, 100],
        "parity_compatible_N": "1 <= N <= 6m"
      },
      "all_positive_matches_in_scope_have_exact_lower_bound_gt_one": true,
      "rows": [...]
    }

Each row must contain m, n=6m, epsilon in {-1,1}, and a
minimum_positive_match object.  Its lower_bound must expose the canonical
positive rational as decimal strings ``numerator`` and ``denominator``, as
well as digit counts and SHA-256 of the ASCII string ``numerator/denominator``.
The verifier checks the raw integer inequality numerator > denominator > 0;
it never relies on a decimal logarithm or a stored Boolean.

This is a *structural witness verifier*.  A single stored minimum per row is
enough only when the pinned generator is independently replayed (or another
certificate binds the exhaustive candidate stream).  It cannot, by itself,
prove that an omitted candidate did not have a smaller lower bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    # Exact witnesses can legitimately exceed Python's default 4300-digit
    # conversion guard.  The certificate is local and its size is bounded by
    # the filesystem before parsing, so disable the guard for this audit.
    sys.set_int_max_str_digits(0)


EXPECTED_SCHEMA = "mixed-cubic-positive-match-exact-scan-v2"
EXPECTED_SCOPE = {"m": [1, 100], "parity_compatible_N": "1 <= N <= 6m"}

# These are the audited revisions.  A deliberate source change must update
# both this verifier and the enhanced certificate, making the trust boundary
# visible in review.
EXPECTED_PINS = {
    "scanner": {
        "root": "archive",
        "path": "scripts/mixed_cubic_positive_match_exact_scan.py",
        "sha256": "fc1888eb7a123c7efd177d25e85686765e720fb1538f2eb95e4cf098640eafa5",
    },
    "archive_kernel": {
        "root": "archive",
        "path": "scripts/cubic_and_mixed_cubic_kernel_certificate.py",
        "sha256": "64491ef73bafac79e5239f75988e04f69377bb52df283a78ad7aaa8dad377229",
    },
    "archive_cartier_reference": {
        "root": "archive",
        "path": "scripts/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.py",
        "sha256": "81d9fa515ba39719d17a5f35456e3749d34f8d857a0411b97fff228c39a36d6d",
    },
}

POSITIVE_DECIMAL = re.compile(r"[1-9][0-9]*\Z")
SHA256_HEX = re.compile(r"[0-9a-f]{64}\Z")


class VerificationError(ValueError):
    """Raised when the enhanced certificate violates its specification."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_positive_decimal(value: Any, label: str) -> int:
    require(isinstance(value, str), f"{label} must be a decimal string")
    require(POSITIVE_DECIMAL.fullmatch(value) is not None, f"invalid {label}")
    return int(value)


def verify_pin_set(workspace_root: Path, archive_root: Path) -> dict[str, str]:
    """Verify the revisions pinned by this independent verifier."""
    roots = {"workspace": workspace_root, "archive": archive_root}
    verified: dict[str, str] = {}
    for role, expected in EXPECTED_PINS.items():
        digest = expected["sha256"]
        target = roots[expected["root"]] / Path(expected["path"])
        require(target.is_file(), f"pinned file is missing: {target}")
        actual = sha256_file(target)
        require(actual == digest, f"pinned file hash mismatch for {role}: {actual}")
        verified[role] = actual
    return verified


def verify_fraction_witness(value: Any, label: str) -> tuple[int, int]:
    require(isinstance(value, dict), f"{label} must be an object")
    numerator_text = value.get("numerator")
    denominator_text = value.get("denominator")
    numerator = parse_positive_decimal(numerator_text, f"{label}.numerator")
    denominator = parse_positive_decimal(denominator_text, f"{label}.denominator")
    require(numerator > denominator > 0, f"{label} does not prove a value > 1")
    require(math.gcd(numerator, denominator) == 1, f"{label} is not canonical")
    require(
        value.get("numerator_digits") == len(numerator_text),
        f"wrong numerator digit count in {label}",
    )
    require(
        value.get("denominator_digits") == len(denominator_text),
        f"wrong denominator digit count in {label}",
    )
    encoded = f"{numerator_text}/{denominator_text}".encode("ascii")
    expected_digest = hashlib.sha256(encoded).hexdigest()
    require(value.get("sha256") == expected_digest, f"fraction hash mismatch in {label}")
    return numerator, denominator


def verify_certificate(
    payload: Any, workspace_root: Path, archive_root: Path
) -> dict[str, Any]:
    require(isinstance(payload, dict), "top-level JSON value must be an object")
    require(payload.get("schema") == EXPECTED_SCHEMA, "wrong certificate schema")
    require(payload.get("scope") == EXPECTED_SCOPE, "scope is not the audited m<=100,N<=6m scope")
    pins = verify_pin_set(workspace_root, archive_root)
    generator = payload.get("generator")
    require(isinstance(generator, dict), "generator pin must be an object")
    require(
        generator.get("filename") == Path(EXPECTED_PINS["scanner"]["path"]).name,
        "wrong generator filename",
    )
    require(
        generator.get("sha256") == EXPECTED_PINS["scanner"]["sha256"],
        "generator hash is not the audited revision",
    )

    rows = payload.get("rows")
    require(isinstance(rows, list), "rows must be an array")
    require(len(rows) == 100, "the certificate must contain exactly 100 rows")
    require(
        [row.get("m") if isinstance(row, dict) else None for row in rows]
        == list(range(1, 101)),
        "rows must cover m=1,...,100 exactly once and in order",
    )

    witness_digests: list[str] = []
    for expected_m, row in enumerate(rows, 1):
        require(isinstance(row, dict), f"row {expected_m} must be an object")
        require(row.get("n") == 6 * expected_m, f"wrong n in row m={expected_m}")
        epsilon = row.get("epsilon")
        require(epsilon in (-1, 1), f"invalid epsilon in row m={expected_m}")
        minimum = row.get("minimum_positive_match")
        require(isinstance(minimum, dict), f"missing minimum in row m={expected_m}")
        index = minimum.get("N")
        require(
            isinstance(index, int) and not isinstance(index, bool),
            f"N must be an integer in row m={expected_m}",
        )
        require(1 <= index <= 6 * expected_m, f"N outside scope in row m={expected_m}")
        require(
            (index % 2 == 0) == (epsilon == 1),
            f"N/epsilon parity mismatch in row m={expected_m}",
        )
        verify_fraction_witness(
            minimum.get("lower_bound"),
            f"rows[{expected_m - 1}].minimum_positive_match.lower_bound",
        )
        require(
            minimum.get("lower_bound_gt_one") is True,
            f"stored comparison flag is not true in row m={expected_m}",
        )
        candidate_scan = row.get("candidate_scan")
        require(
            isinstance(candidate_scan, dict),
            f"missing candidate scan metadata in row m={expected_m}",
        )
        require(
            candidate_scan.get("admissible_count") == 3 * expected_m,
            f"wrong parity-compatible candidate count in row m={expected_m}",
        )
        transcript_hash = candidate_scan.get("canonical_fraction_transcript_sha256")
        require(
            isinstance(transcript_hash, str)
            and SHA256_HEX.fullmatch(transcript_hash) is not None,
            f"invalid candidate transcript hash in row m={expected_m}",
        )
        witness_digests.append(minimum["lower_bound"]["sha256"])

    aggregate = payload.get(
        "all_positive_matches_in_scope_have_exact_lower_bound_gt_one"
    )
    require(aggregate is True, "top-level aggregate comparison must be true")
    stream = "\n".join(witness_digests).encode("ascii")
    return {
        "schema": EXPECTED_SCHEMA,
        "rows_verified": 100,
        "m_range": [1, 100],
        "all_raw_numerators_exceed_denominators": True,
        "minimum_witness_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "pinned_inputs_verified": pins,
        "logical_boundary": (
            "Stored row minima are verified exactly. Exhaustiveness over every "
            "candidate N still relies on replay of the pinned generator unless "
            "per-candidate witnesses are also supplied."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    parser.add_argument(
        "--archive-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        report = verify_certificate(
            payload,
            args.workspace_root.resolve(),
            args.archive_root.resolve(),
        )
    except (OSError, json.JSONDecodeError, VerificationError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
