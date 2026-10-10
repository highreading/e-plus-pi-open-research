#!/usr/bin/env python3
"""Deterministic exact replay for Item 345.

The checker analyzes the Galois orbit of Item 342's chosen-prime Kummer
lift.  It constructs the lift as an integral group-ring element, reduces it
modulo the cyclotomic polynomial, checks its stabilizer and absolute norm on
five preselected rows, and records the split-prime trace/norm dichotomy.
No prime scan or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from math import gcd
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item345_j1_kummer_galois_descent_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item342_j1_finite_field_fourier_weil_barrier_report.md":
        "843bb85381c98adf0a5b64801ce099e4c3c9119d5933704d97bbd492f1b8029b",
    "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py":
        "130cfd5d2ac7c31546ef177c3f751abcc236ca92dc253a59914d487187c1fbac",
    "results/item342_j1_finite_field_fourier_weil_barrier_certificate.json":
        "4cf10e1d035dcd18a134e5f1b00e54a34ae1b3833a2863b54212da9fcccf49d9",
    "results/item342_j1_finite_field_fourier_weil_barrier_certificate_replay.json":
        "4cf10e1d035dcd18a134e5f1b00e54a34ae1b3833a2863b54212da9fcccf49d9",
    "results/item342_j1_finite_field_fourier_weil_barrier_root_audit.json":
        "aa6b260f78ae094b20a1b6b041c75131514b5ded51f016e6950671c472280835",
    "manifests/item342_j1_finite_field_fourier_weil_barrier_manifest.json":
        "85ca4a73d9009acc3dc8d7102325f74156a11bf13e618dc1a88c06fd352b8a54",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM342 = load_module(
    "item345_pinned_item342",
    ROOT / "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py",
)


def primitive_log_table(prime: int) -> tuple[int, dict[int, int]]:
    generator = int(S.primitive_root(prime))
    return generator, {
        pow(generator, exponent, prime): exponent for exponent in range(prime - 1)
    }


def group_ring_lift(h: int, s: int, prime: int) -> dict[str, Any]:
    """Construct Item342's T as a polynomial in zeta_(p-1)."""
    n = 2 * h
    r = 2 * s + 1
    exponent = prime - r
    modulus = prime - 1
    generator, logarithm = primitive_log_table(prime)

    def g_value(value: int) -> int:
        return (1 - 4 * value + 6 * value**2 - 4 * value**3) % prime

    def theta_g(value: int) -> int:
        return (-4 * value + 12 * value**2 - 12 * value**3) % prime

    def theta2_g(value: int) -> int:
        return (-4 * value + 24 * value**2 - 36 * value**3) % prime

    data = [
        (
            (n - 1) * (n - 2),
            lambda value: pow(value, modulus - n, prime)
            * pow(g_value(value), exponent, prime),
        ),
        (
            (3 - 2 * n) * exponent,
            lambda value: pow(value, modulus - n, prime)
            * theta_g(value)
            * pow(g_value(value), exponent - 1, prime),
        ),
        (
            exponent,
            lambda value: pow(value, modulus - n, prime)
            * theta2_g(value)
            * pow(g_value(value), exponent - 1, prime),
        ),
        (
            exponent * (exponent - 1),
            lambda value: pow(value, modulus - n, prime)
            * pow(theta_g(value), 2, prime)
            * pow(g_value(value), exponent - 2, prime),
        ),
    ]
    outer = -pow(2, -1, prime) % prime
    counts = [0] * modulus
    for scalar, function in data:
        scalar_mod = outer * (scalar % prime) % prime
        if scalar_mod == 0:
            continue
        for value in range(1, prime):
            term = function(value) % prime
            if term:
                counts[logarithm[scalar_mod * term % prime]] += 1

    X = S.symbols("X")
    cyclotomic = S.Poly(S.cyclotomic_poly(modulus, X), X, domain=S.ZZ)
    polynomial = S.Poly(
        sum(coefficient * X**index for index, coefficient in enumerate(counts)),
        X,
        domain=S.ZZ,
    )
    reduced = polynomial.rem(cyclotomic)

    stabilizer = []
    for multiplier in range(1, modulus):
        if gcd(multiplier, modulus) != 1:
            continue
        conjugate = S.Poly(
            sum(
                coefficient * X ** ((index * multiplier) % modulus)
                for index, coefficient in enumerate(counts)
            ),
            X,
            domain=S.ZZ,
        ).rem(cyclotomic)
        if conjugate == reduced:
            stabilizer.append(multiplier)

    absolute_norm = abs(
        int(S.resultant(cyclotomic.as_expr(), reduced.as_expr(), X))
    )
    reduction = sum(
        coefficient * pow(generator, index, prime)
        for index, coefficient in enumerate(counts)
    ) % prime
    expected_target = ITEM342.ITEM339.a_hypergeometric(r, n) % prime
    if reduction != expected_target:
        raise AssertionError("group-ring lift does not reduce to Item339 target")

    return {
        "M": 3 * h + 4 * s + 2,
        "h": h,
        "s": s,
        "p": prime,
        "n": n,
        "r": r,
        "primitive_root": generator,
        "cyclotomic_degree": int(S.totient(modulus)),
        "reduced_polynomial_coefficients_high_to_low": [
            int(value) for value in reduced.all_coeffs()
        ],
        "stabilizer_multipliers": stabilizer,
        "orbit_degree": int(S.totient(modulus)) // len(stabilizer),
        "target_mod_p": reduction,
        "absolute_norm": absolute_norm,
        "norm_divisible_by_p": absolute_norm % prime == 0,
        "term_count_before_cyclotomic_reduction": sum(counts),
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        ((1, 1, 13), 4, 6877, 0, True),
        ((2, 1, 17), 8, 19103121, 8, True),
        ((8, 2, 47), 22, 2075473882824195408557, 0, True),
        ((4, 4, 43), 12, 2592733605337, 2, False),
        ((2, 6, 47), 22, 1905718768398368001644003, 36, True),
    ]
    output = []
    for row, expected_orbit, expected_norm, expected_target, expected_norm_gate in declared:
        record = group_ring_lift(*row)
        if record["stabilizer_multipliers"] != [1]:
            raise AssertionError(("declared stabilizer", row))
        actual = (
            record["orbit_degree"],
            record["absolute_norm"],
            record["target_mod_p"],
            record["norm_divisible_by_p"],
        )
        expected = (
            expected_orbit,
            expected_norm,
            expected_target,
            expected_norm_gate,
        )
        if actual != expected:
            raise AssertionError(("declared orbit/norm control", row, actual))
        record["classification"] = "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN"
        record["full_original_collision_claimed"] = False
        output.append(record)
    return output


def split_prime_descent_theorem() -> dict[str, Any]:
    return {
        "setup": {
            "field": "K_p=Q(zeta_(p-1))",
            "Galois_group": "(Z/(p-1)Z)^x",
            "splitting":
                "p is unramified and p=1 mod (p-1), hence splits completely in K_p",
            "chosen_prime":
                "the Teichmueller embedding fixes one prime P above p, and the selected gate is T in P",
            "decomposition_group": "D(P/p)={1}",
        },
        "additive_descent": {
            "theorem":
                "for every nontrivial subgroup H, Tr_(K/K^H)(P) is not contained in P intersect K^H; the same failure holds for nontrivial additive character/idempotent projections",
            "reason":
                "complete splitting identifies O_K/p with a product of F_p coordinates; vanishing of one coordinate does not force an orbit sum to vanish",
            "consequence":
                "no nontrivial additive Galois averaging is target-forced by the chosen-prime gate",
        },
        "multiplicative_descent": {
            "theorem":
                "N_(K/K^H)(T) lies in P intersect K^H whenever T lies in P",
            "false_positives":
                "the norm can be divisible by p because a different split-prime coordinate vanishes even when the selected target is nonzero",
            "height_identity":
                "if d=[K:Q], h=|H|, and every conjugate of T is at most B, each relative-norm conjugate is at most B^h and its absolute norm bound is B^(h*d/h)=B^d",
            "Item342_value": "B=21 sqrt(p), d=phi(p-1)",
            "consequence":
                "passing through any subfield does not improve the black-box absolute norm bound (21 sqrt(p))^phi(p-1)",
        },
        "stabilizer_dichotomy": {
            "orbit_degree": "[Q(T):Q]=|Gal(K/Q):Stab(T)|",
            "bounded_degree_requirement":
                "a degree-D descent requires a stabilizer of size at least phi(p-1)/D",
            "not_forced":
                "chosen-prime membership alone imposes no equality between Galois coordinates and therefore forces no nontrivial stabilizer",
            "finite_witness":
                "both preselected selected-carrier zeros p=13 and p=47 have trivial stabilizer; this is exact finite evidence against automatic descent, not a density theorem",
        },
    }


def capacity_and_scope() -> dict[str, Any]:
    return {
        "capacity_first": {
            "support": "the split-prime theorem applies to every actual Item342 row",
            "raw_fixed_j1_prime_mass": "M/6+o(M)",
            "additive_projection_excluded_mass": 0,
            "norm_height_gain": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "scoped_no_go": {
            "closed": [
                "nontrivial Galois traces or bounded-character additive projections justified only by the chosen-prime gate",
                "relative norms through bounded-index or bounded-degree subfields combined only with Item342's conjugate bound",
                "claiming automatic rational descent from the formal Teichmueller construction or from selected-carrier vanishing alone",
            ],
            "not_closed": [
                "a new theorem proving a large stabilizer specifically on all or almost all selected-zero rows",
                "special cancellation giving a genuinely smaller relative or absolute norm",
                "p-adic chosen-prime nonconcentration without Galois descent",
                "an additional original-collision condition that forces descent beyond the selected factor",
            ],
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item345-j1-kummer-galois-descent-obstruction-certificate-v1",
        "item": 345,
        "date": "2026-09-01",
        "status": "PROVED_SPLIT_PRIME_DESCENT_DICHOTOMY_AND_SCOPED_GALOIS_PROJECTION_NO_GO",
        "dependencies": DEPENDENCIES,
        "split_prime_descent_theorem": split_prime_descent_theorem(),
        "capacity_and_scope": capacity_and_scope(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "complete splitting and trivial decomposition group at the chosen Teichmueller prime",
                "non-preservation of the gate by every nontrivial additive Galois projection",
                "preservation by relative norms and invariance of the black-box absolute norm height under subfield factorization",
                "the exact stabilizer/orbit criterion for bounded-degree descent",
                "scoped Galois projection and subfield-norm no-go",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected group-ring stabilizer and norm controls; no scan or asymptotic inference",
                "two carrier-zero controls have trivial stabilizer, and two nonzero controls are norm false positives",
            ],
            "OPEN": [
                "a large-stabilizer or special-descent theorem on a weighted-full set of selected-zero rows",
                "special relative-norm cancellation below the black-box height",
                "chosen-prime p-adic nonconcentration",
                "W_b(M)=o(M), any fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 345,
                "decomposition_group": "TRIVIAL",
                "additive_descent": "NOT_GATE_FORCED",
                "norm_descent": "GATE_PRESERVING_BUT_NO_HEIGHT_GAIN",
                "weighted_density": "OPEN",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
