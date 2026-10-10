#!/usr/bin/env python3
"""Portable exact certificate for Item 286.

This checker performs no collision census.  It certifies the elementary
phase, diagonal-modulus, and conditional-exponent calculations and records
the hypothesis audit against frozen archive dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = ROOT / "results" / "item286_j1_frobenius_sieve_applicability_certificate.json"

DEPENDENCIES = {
    "sources/item264_j1_weighted_gate_report.md": "767005f8fad07b1fa633bfdd23436e36c7cdef346d032030390c437f207c9344",
    "sources/item273_j1_fixed_incidence_report.md": "3100dc1beef7508ccc317b86d7ae9e9ac464f990b6934aa7422f7f0186402943",
    "scripts/item273_j1_fixed_incidence_certificate.py": "4f26bc7616b61922ab00e6ab69ad0d9c38e36070295c9aa900e7bbbc0dbe0511",
    "sources/item275_j1_grassmannian_report.md": "a00e7ba707d57348037f10cded3db0a7fbbc8baa1ea9edcb8103e227ebaa5995",
    "scripts/item275_j1_grassmannian_certificate.py": "e75ea09a4d6c57cbb7c5fc971072f3b203f4faa4d9d363384fa288f62070c1bb",
    "sources/item279_j1_bounded_cluster_report.md": "533383bdd073c2950ae5ff65e9c2888a80242c58317c6ca89306bd2d1864a28e",
    "sources/item281_j1_isolated_fitting_norm_report.md": "fcd8f91426edf31a8de5b90dbc986ae04c08865ddfe448fc9e240410c5c1fd80",
    "sources/item284_j1_parameter_norm_report.md": "bc8b84ab59f2e8aed790237d8e57191c78e4c5811d198137ab5ceb6d68a23889",
    "sources/route1_targeted_literature_note_items259_265.md": "b695c350feb8362b9f7d3349c27d7949c8beda3a8dceb3dd660ae63c11e15a31",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def dependency_audit() -> dict[str, Any]:
    checked: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
        checked[relative] = actual
    return {"count": len(checked), "sha256": checked}


def phase_audit() -> dict[str, Any]:
    # From M=3h+4s+2 and p=4h+6s+3:
    # 4M+1=3p-2s and p=(4M+2s+1)/3.
    coefficient_identity = {
        "h": 4 * 3 - 3 * 4,
        "s": 4 * 4 - 3 * 6,
        "constant": 4 * 2 + 1 - 3 * 3,
    }
    if coefficient_identity != {"h": 0, "s": -2, "constant": 0}:
        raise AssertionError(coefficient_identity)
    lower = Fraction(4, 3)
    lower_constant = Fraction(3, 3)
    upper = Fraction(3, 2)
    upper_constant = Fraction(-1, 2)
    length_slope = upper - lower
    length_constant = upper_constant - lower_constant
    if (length_slope, length_constant) != (Fraction(1, 6), Fraction(-3, 2)):
        raise AssertionError((length_slope, length_constant))
    # (M-9)/6 = M/6-3/2.
    return {
        "phase_identity": "4M+1=3p-2s",
        "candidate_interval": ["(4M+3)/3", "(3M-1)/2"],
        "exact_interval_length": "(M-9)/6",
        "length_slope": str(length_slope),
        "raw_log_mass_per_M": "1/6",
        "raw_capacity_per_6M": "1/36",
    }


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(flags) if flag]


def diagonal_modulus_audit() -> dict[str, Any]:
    # General proof: for distinct primes p and ell, (a,b)=(p,p) is zero
    # modulo p and nonzero modulo ell.  The bounded replay only checks the
    # constructor; no arithmetic gate values are sampled.
    primes = primes_upto(97)
    pairs = 0
    digest = hashlib.sha256()
    for p in primes:
        for ell in primes:
            if ell == p:
                continue
            a = b = p
            if a % p or b % p:
                raise AssertionError((p, ell, "not p-zero"))
            if a % ell == 0 or b % ell == 0:
                raise AssertionError((p, ell, "unexpected auxiliary zero"))
            digest.update(f"{p},{ell},{a % ell},{b % ell}\n".encode("ascii"))
            pairs += 1
    return {
        "all_prime_proof": "for p!=ell, the witness (a,b)=(p,p) is p-zero and ell-nonzero",
        "constructor_replay_label": "EXACT FINITE ONLY; no collision census",
        "constructor_replay_pairs": pairs,
        "constructor_replay_sha256": digest.hexdigest(),
    }


def conditional_exponent_audit() -> dict[str, Any]:
    # If P(L) >> L/log L and L=q^(1/(2A)), then both numerator terms in
    # Kowalski's bound are O(q^d), and division gives
    # q^(d-1/(2A))*log q.
    rows = []
    for a in range(1, 13):
        l_exponent = Fraction(1, 2 * a)
        error_exponent = Fraction(-1, 2) + a * l_exponent
        saving = l_exponent
        if error_exponent != 0 or saving <= 0:
            raise AssertionError((a, l_exponent, error_exponent))
        rows.append({
            "A": a,
            "L_exponent": str(l_exponent),
            "second_numerator_relative_exponent": str(error_exponent),
            "power_saving": str(saving),
        })
    return {
        "assumptions": [
            "Kowalski Theorem 3.1 and Proposition 3.3 apply",
            "target is an exact integral zero of conjugacy-invariant coefficients and hence auxiliary-local at every ell",
            "the complements Omega(ell) have uniformly positive relative density",
            "the auxiliary-prime set has positive density",
        ],
        "choice": "L=q^(1/(2A))",
        "conclusion": "|target| << q^(d-1/(2A)) log q",
        "symbolic_integer_A_checks": rows,
        "horizontal_capacity_threshold": "N(M)=o(M/log M) implies W(M)=o(M)",
    }


def hypothesis_audit() -> list[dict[str, str]]:
    rows = [
        ("fixed finite-field base U/F_q", "MISSING", "candidate p varies with the characteristic"),
        ("lisse fixed-rank auxiliary-ell sheaves", "MISSING", "difference matrices are not pi_1 representations"),
        ("compatible integral system", "MISSING", "no ell-independent Frobenius polynomials"),
        ("uniform cohomological complexity/conductor", "MISSING", "fixed rational poles do not prove it"),
        ("geometric and arithmetic monodromy", "MISSING", "no endpoint-state monodromy group"),
        ("cross-ell linear disjointness", "MISSING", "no product-surjectivity theorem"),
        ("fixed conjugacy-stable full-gate condition", "MISSING", "Pluecker incidence has no Frobenius class"),
        ("collision-to-all-auxiliary-ell implication", "MISSING", "recognition is diagonal modulo p"),
        ("uniform local density", "MISSING", "codimension is not equidistribution"),
    ]
    if any(status != "MISSING" for _, status, _ in rows):
        raise AssertionError(rows)
    return [
        {"criterion": criterion, "status": status, "reason": reason}
        for criterion, status, reason in rows
    ]


def certificate() -> dict[str, Any]:
    body: dict[str, Any] = {
        "schema": "item286-j1-frobenius-sieve-applicability-certificate-v1",
        "labels": {
            "kowalski_large_sieve_statement": "LITERATURE THEOREM under cited hypotheses",
            "current_archive_applicability": "PROVED NOT ESTABLISHED",
            "fixed_field_mismatch": "PROVED scoped obstruction",
            "diagonal_modulus_mismatch": "PROVED scoped obstruction",
            "conditional_exact_zero_bridge": "PROVED conditional calculation",
            "collision_census_performed": False,
            "new_route1_rate": 0,
        },
        "dependencies": dependency_audit(),
        "phase": phase_audit(),
        "diagonal_modulus": diagonal_modulus_audit(),
        "conditional_bridge": conditional_exponent_audit(),
        "hypothesis_audit": hypothesis_audit(),
        "available_archive_objects": {
            "item273": "rank-at-most-eight rational translation module with fixed singular support",
            "item275": "rank-six exterior square and fixed stratified flag incidence; natural kernel line non-horizontal",
            "item281": "all-branch normalized gcd/Fitting recognition",
            "item284": "exact CRT recognition only",
        },
        "scope": {
            "excluded": "application of Kowalski's fixed-field Frobenius sieve from the currently sealed finite module and recognition identities alone",
            "not_excluded": [
                "a new compatible system over a fixed or arithmetic base",
                "a direct horizontal Chebotarev or large-sieve theorem",
                "an exact-zero conjugacy-invariant or rigorously framed auxiliary-local bridge special to the actual state",
            ],
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "count_needed_for_zero_log_mass": "o(M/log M)",
            "new_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": result["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
