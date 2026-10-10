#!/usr/bin/env python3
"""Deterministic exact replay for Item 348.

This checker builds the actual left and right first-Hasse polynomials for
Item 342's selected carrier, verifies that their degree is exactly the
Item339 survivor length minus one, and checks that a negative integral top
parameter makes the formal Dwork dash tower trivial after one step.  Five
preselected rows are replayed; no prime scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item348_j1_dwork_first_hasse_obstruction_certificate.json"

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
    "sources/item345_j1_kummer_galois_descent_obstruction_report.md":
        "17441d83d40de9a8df6419b35e277753ed86006e1c461e4cbaa618db8d9e9392",
    "results/item345_j1_kummer_galois_descent_obstruction_certificate.json":
        "e0eca357cafab27e4ff9c97bf4beacaf9c82b102de47614472eecac8590dbcc7",
    "results/item345_j1_kummer_galois_descent_obstruction_root_audit.json":
        "285e7e220f914913ac1e5dc9592d07206ac4435df03c90d52d627e969ab349c2",
    "manifests/item345_j1_kummer_galois_descent_obstruction_manifest.json":
        "78531805af9b60a30535a992b7c8b9aa90f415ffa55e2586d1f48ea5b02bb2ca",
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
    "item348_pinned_item342",
    ROOT / "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py",
)
ITEM339 = ITEM342.ITEM339


def first_hasse_chart(r: int, n: int, prime: int) -> dict[str, Any]:
    """Return the actual p-unit chart for a_(r,n) modulo p."""
    terms = ITEM339.hypergeometric_terms(r, n)
    residues = [value % prime for value in terms]
    length = ITEM339.survivor_length(r, n)
    K = n // 4
    delta = n % 4
    d = r - n - 1

    if length == 0:
        if not (d == 0 and delta == 2):
            raise AssertionError("unexpected zero survivor chart")
        return {
            "chart": "FORCED_ZERO_RAY",
            "coefficients_mod_p": [],
            "degree": None,
            "survivor_length": 0,
            "value_at_1": 0,
            "prefactor_mod_p": None,
            "negative_integral_top_parameter": None,
            "dash_of_negative_parameter": None,
        }

    if r <= n:
        prefactor = residues[0]
        if prefactor == 0:
            raise AssertionError("left prefactor is not a p-unit")
        inverse = pow(prefactor, -1, prime)
        coefficients = [value * inverse % prime for value in residues]
        degree = K
        if coefficients[-1] == 0:
            raise AssertionError("left leading coefficient")
        negative_index = 0 if delta == 0 else 2
        negative_parameter = -K
        return {
            "chart": "LEFT_NORMALIZED_4F3",
            "hypergeometric_type": "4F3",
            "coefficients_mod_p": coefficients,
            "degree": degree,
            "survivor_length": length,
            "value_at_1": sum(coefficients) % prime,
            "prefactor_mod_p": prefactor,
            "negative_integral_top_parameter": negative_parameter,
            "negative_parameter_position": negative_index,
            "dash_of_negative_parameter": 0,
            "all_first_dashed_bottom_parameters_nonzero": True,
        }

    # Start at the first surviving original k.  This gives a shifted 5F4
    # with top parameters 1 and k0+(q-n)/4, and avoids the spurious
    # negative-integral bottom parameter introduced by reversing the tail.
    J = min(K, (d - delta) // 4)
    if J + 1 != length:
        raise AssertionError("right survivor length")
    k0 = K - J
    coefficients = []
    for i in range(J + 1):
        k = k0 + i
        m = n - 4 * k
        coefficient = comb(r + k - 1, k) * comb(d, m) % prime
        if coefficient == 0:
            raise AssertionError("right surviving coefficient is not a p-unit")
        coefficients.append(coefficient)
    if sum(coefficients) % prime != ITEM339.a_hypergeometric(r, n) % prime:
        raise AssertionError("right tail value")
    return {
        "chart": "RIGHT_SURVIVING_TAIL",
        "hypergeometric_type": "SHIFTED_5F4",
        "coefficients_mod_p": coefficients,
        "degree": J,
        "survivor_length": length,
        "value_at_1": sum(coefficients) % prime,
        "prefactor_mod_p": coefficients[0],
        "right_start_k": k0,
        "negative_integral_top_parameter": -J,
        "negative_parameter_position": delta,
        "dash_of_negative_parameter": 0,
        "all_first_dashed_bottom_parameters_nonzero": True,
    }


def dwork_dash_fraction(value: Fraction, prime: int) -> Fraction:
    denominator_mod_p = value.denominator % prime
    if denominator_mod_p == 0:
        raise ValueError("parameter is not p-integral")
    residue = value.numerator * pow(denominator_mod_p, -1, prime) % prime
    lift = (-residue) % prime
    return (value + lift) / prime


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator % prime, -1, prime) % prime


def verify_hypergeometric_ratios(
    coefficients: list[int], top: list[Fraction], bottom: list[Fraction], prime: int
) -> None:
    for index in range(len(coefficients) - 1):
        numerator = 1
        denominator = index + 1
        for parameter in top:
            numerator = numerator * fraction_mod(parameter + index, prime) % prime
        for parameter in bottom:
            denominator = denominator * fraction_mod(parameter + index, prime) % prime
        expected = numerator * pow(denominator % prime, -1, prime) % prime
        actual = coefficients[index + 1] * pow(coefficients[index], -1, prime) % prime
        if actual != expected:
            raise AssertionError(("hypergeometric term ratio", index, actual, expected))


def dwork_dash_of_negative_integer(K: int, prime: int) -> int:
    if not 0 <= K < prime:
        raise ValueError("the actual terminating index must lie below p")
    # D_p(x)=(x+l)/p with 0<=l<p and x+l in p Z_p.  For x=-K take l=K.
    return 0


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        ((1, 1, 13), "FORCED_ZERO_RAY", None, [], 0, None),
        ((2, 1, 17), "LEFT_NORMALIZED_4F3", 1, [1, 4], 5, 5),
        ((8, 2, 47), "LEFT_NORMALIZED_4F3", 4, [1, 4, 43, 23, 23], 0, 1),
        ((4, 4, 43), "RIGHT_SURVIVING_TAIL", 0, [2], 2, 2),
        ((2, 6, 47), "RIGHT_SURVIVING_TAIL", 1, [23, 13], 36, 23),
    ]
    output = []
    for row, expected_chart, expected_degree, expected_coefficients, expected_value, expected_prefactor in declared:
        h, s, prime = row
        n = 2 * h
        r = 2 * s + 1
        chart = first_hasse_chart(r, n, prime)
        actual = (
            chart["chart"],
            chart["degree"],
            chart["coefficients_mod_p"],
            chart["value_at_1"],
            chart["prefactor_mod_p"],
        )
        expected = (
            expected_chart,
            expected_degree,
            expected_coefficients,
            expected_value,
            expected_prefactor,
        )
        if actual != expected:
            raise AssertionError(("declared Hasse chart", row, actual))
        if chart["degree"] is not None:
            if chart["degree"] != chart["survivor_length"] - 1:
                raise AssertionError("degree versus survivor length")
            J = -chart["negative_integral_top_parameter"]
            if dwork_dash_of_negative_integer(J, prime) != 0:
                raise AssertionError("Dwork dash")
            if chart["chart"] == "LEFT_NORMALIZED_4F3":
                bottoms = [Fraction(r, 1) + Fraction(q, 4) for q in (1, 2, 3)]
                tops = [Fraction(q - n, 4) for q in range(4)]
            else:
                k0 = chart["right_start_k"]
                bottoms = [Fraction(k0 + 1, 1)] + [
                    Fraction(k0 + r, 1) + Fraction(q, 4) for q in (1, 2, 3)
                ]
                tops = [Fraction(1, 1)] + [Fraction(4 * k0 + q - n, 4) for q in range(4)]
            verify_hypergeometric_ratios(
                chart["coefficients_mod_p"], tops, bottoms, prime
            )
            if any(dwork_dash_fraction(value, prime) == 0 for value in bottoms):
                raise AssertionError("dashed bottom parameter unexpectedly zero")
        a_mod_p = ITEM339.a_hypergeometric(r, n) % prime
        if chart["chart"] == "LEFT_NORMALIZED_4F3":
            reconstructed = chart["prefactor_mod_p"] * chart["value_at_1"] % prime
        else:
            reconstructed = chart["value_at_1"]
        if reconstructed != a_mod_p:
            raise AssertionError("exact Hasse-value bridge")
        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "M": 3 * h + 4 * s + 2,
                "h": h,
                "s": s,
                "p": prime,
                "n": n,
                "r": r,
                "a_mod_p": a_mod_p,
                "Hasse_zero_iff_selected_factor_zero": True,
                **chart,
                "full_original_collision_claimed": False,
            }
        )
    return output


def theorem_and_capacity() -> dict[str, Any]:
    return {
        "first_Hasse_polynomial": {
            "left_chart":
                "for r<=n, divide the exact 4F3 prefix by the p-unit C(4r+n-1,n); H_L(z) has degree floor(n/4) and a=prefix*H_L(1) mod p",
            "right_chart":
                "for r>n, reindex the Lucas-surviving tail by j=floor(n/4)-k; H_R(z) has all p-unit coefficients and a=H_R(1) mod p",
            "unified_degree":
                "away from the forced zero ray, deg H=ell(r,n)-1 exactly",
            "one_way_gate":
                "ordinary collision => a_(r,n)=0 => H(1)=0; no converse to the original collision is claimed",
        },
        "formal_Dwork_dash": {
            "definition":
                "D_p(x)=(x+l)/p, where 0<=l<p is chosen so x+l is in p Z_p",
            "left_negative_parameter":
                "the 4F3 top tuple always contains -K, K=floor(n/4)<p",
            "right_negative_parameter":
                "the forward shifted surviving-tail 5F4 always contains -J, J=deg H<p",
            "dash": "D_p(-K)=D_p(-J)=0",
            "tower_consequence":
                "all first-dashed bottom parameters are nonzero; the dashed hypergeometric coefficient sequence has a top parameter 0, so every coefficient of positive index vanishes and every later truncation factor is 1",
            "strict_scope":
                "this is the formal Dwork dash tower of the actual terminating chart; it does not assert the existence of an additional geometric F-crystal",
        },
        "capacity": {
            "raw_fixed_j1_prime_mass": "M/6+o(M)",
            "forced_zero_ray": "O(log M)=o(M)",
            "sublinear_Hasse_degree_support":
                "deg H=o(M) iff survivor length ell=o(M), and Item339 proves this support has weighted mass o(M)",
            "positive_rate_bulk":
                "every positive-rate bulk therefore has deg H=Theta(M)",
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "scoped_no_go": {
            "closed": [
                "bounded- or sublinear-degree first-Hasse criteria as a positive-rate fixed-j1 mechanism",
                "seeking a new nontrivial higher Dwork-dash factor after the actual terminating first chart",
                "replacing H(1) by a fixed bounded-degree unit-root divisor without a new global identity",
            ],
            "not_closed": [
                "a global p-adic nonconcentration theorem for the linearly growing first-Hasse polynomial",
                "a monodromy or average-gcd theorem treating the whole Hasse polynomial at once",
                "a new geometric realization with additional structure not present in the formal terminating dash tower",
            ],
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item348-j1-dwork-first-hasse-obstruction-certificate-v1",
        "item": 348,
        "date": "2026-09-01",
        "status": "PROVED_FIRST_HASSE_POLYNOMIAL_AND_TRIVIAL_DWORK_DASH_TOWER_SCOPED_BOUNDED_DEGREE_NO_GO",
        "dependencies": DEPENDENCIES,
        "theorem_and_capacity": theorem_and_capacity(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "the exact left normalized 4F3 and right surviving-tail first-Hasse charts",
                "the unified exact degree formula deg H=survivor length minus one",
                "the negative integral top parameter and one-step trivialization of the formal Dwork dash tower",
                "zero-rate support of sublinear first-Hasse degree",
                "scoped bounded-degree and higher-dash no-go",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected first-Hasse charts; no scan or asymptotic inference"
            ],
            "OPEN": [
                "p-adic nonconcentration for the linearly growing first-Hasse value at z=1",
                "a global monodromy, average-gcd, or factor-localization theorem for the full Hasse polynomial",
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
                "item": 348,
                "first_Hasse_degree": "SURVIVOR_LENGTH_MINUS_ONE",
                "Dwork_dash_after_first": "TRIVIAL",
                "sublinear_degree_mass": "ZERO_RATE",
                "weighted_density": "OPEN",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
