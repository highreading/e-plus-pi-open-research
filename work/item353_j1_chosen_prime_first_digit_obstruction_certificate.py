#!/usr/bin/env python3
"""Deterministic exact replay for Item 353.

This checker expands the four de-aliased Kummer coordinates at the chosen
completely split prime through p^2, verifies the carry-plus-Fermat-correction
formula on the five predeclared Item 342 rows, and checks the exact maximal
interpolation degree of the universal Teichmueller correction.  No prime scan
or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item353_j1_chosen_prime_first_digit_obstruction_certificate.json"

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
    "sources/item348_j1_dwork_first_hasse_obstruction_report.md":
        "1ec4af9e7f1f6a08eab869b3e091778c26c0645bc38e692b57252da2e31de67a",
    "scripts/item348_j1_dwork_first_hasse_obstruction_certificate.py":
        "13ef13c792f9f3a00f29a1baff3eb25c592106a0b5802da2158c1f4d72b0172b",
    "results/item348_j1_dwork_first_hasse_obstruction_certificate.json":
        "ea9904c4411af6d8dc0199d347872bae361c591ab911db1fb19e5f1cb19d7de4",
    "results/item348_j1_dwork_first_hasse_obstruction_root_audit.json":
        "75d75ae87a086d7d7e0a608a6216196f6f48296f090d8ff56cea320a31638ac3",
    "manifests/item348_j1_dwork_first_hasse_obstruction_manifest.json":
        "8a6835132fd4bd0c3e10d8abc216d9b7019cf73ec70f4691276d9849d9ad6aa9",
    "sources/item351_j1_companion_window_rank_obstruction_report.md":
        "8aca8f37c81547f44793e4276ed87847ff17cd4a67fe1617821591efdcc3795f",
    "scripts/item351_j1_companion_window_rank_obstruction_certificate.py":
        "ea1c2b337f5d506ef1bd26bf40dffd97c08e08ee360bcb2abd43cb76d697bcf2",
    "results/item351_j1_companion_window_rank_obstruction_certificate.json":
        "1bf092c3778ac6377de00ef6d087c2e68d107bbd2041f150f462bce0326bd07b",
    "results/item351_j1_companion_window_rank_obstruction_certificate_replay.json":
        "1bf092c3778ac6377de00ef6d087c2e68d107bbd2041f150f462bce0326bd07b",
    "results/item351_j1_companion_window_rank_obstruction_root_replay.json":
        "1bf092c3778ac6377de00ef6d087c2e68d107bbd2041f150f462bce0326bd07b",
    "results/item351_j1_companion_window_rank_obstruction_ledger_delta.json":
        "1118768b36150ca0ec73859921690b530a4ad01e53a5f43f3acf5c1758e7073a",
    "results/item351_j1_companion_window_rank_obstruction_self_audit.json":
        "d5b5f5f63bfe22d510a5b9231a61abec88397bde94899b1511c2c645972ccd3b",
    "results/item351_j1_companion_window_rank_obstruction_root_audit.json":
        "8151a963aa85895910a8de1d5a81d8567c93b653c0fb7a766819b07522da3974",
    "manifests/item351_j1_companion_window_rank_obstruction_manifest.json":
        "67c1cdbd98e16e1b63828ba2fa74cb0f7afd21e00b6551cdc775e296c7468ab1",
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
    "item353_pinned_item342",
    ROOT / "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py",
)
ITEM339 = ITEM342.ITEM339


def teichmueller_mod_p2(residue: int, prime: int) -> int:
    residue %= prime
    if residue == 0:
        return 0
    return pow(residue, prime, prime * prime)


def fermat_correction(residue: int, prime: int) -> int:
    """delta_p(a)=(a^p-a)/p mod p for the canonical 0<=a<p."""
    residue %= prime
    if residue == 0:
        return 0
    return ((pow(residue, prime, prime * prime) - residue) // prime) % prime


def weighted_kummer_residues(h: int, s: int, prime: int) -> list[list[int]]:
    """Return y_(nu,x) after absorbing all Teichmueller scalar weights."""
    n = 2 * h
    r = 2 * s + 1
    exponent = prime - r
    inverse_two = pow(2, -1, prime)
    output = [[] for _ in range(4)]
    for x in range(1, prime):
        G = (1 - 4 * x + 6 * x * x - 4 * x * x * x) % prime
        theta_G = (-4 * x + 12 * x * x - 12 * x * x * x) % prime
        theta2_G = (-4 * x + 24 * x * x - 36 * x * x * x) % prime
        x_minus_n = pow(x, prime - 1 - n, prime)
        functions = [
            x_minus_n * pow(G, exponent, prime) % prime,
            x_minus_n * theta_G * pow(G, exponent - 1, prime) % prime,
            x_minus_n * theta2_G * pow(G, exponent - 1, prime) % prime,
            x_minus_n * theta_G * theta_G * pow(G, exponent - 2, prime) % prime,
        ]
        weights = [
            -(n - 1) * (n - 2) * inverse_two,
            -(3 - 2 * n) * exponent * inverse_two,
            -exponent * inverse_two,
            -exponent * (exponent - 1) * inverse_two,
        ]
        for index, (weight, function) in enumerate(zip(weights, functions)):
            output[index].append(weight * function % prime)
    return output


def coordinate_digits(residues: list[int], prime: int) -> dict[str, int]:
    ordinary_sum = sum(residues)
    residue_digit = ordinary_sum % prime
    internal_carry = (ordinary_sum - residue_digit) // prime
    correction = sum(fermat_correction(value, prime) for value in residues) % prime
    first_digit = (internal_carry + correction) % prime
    teich_sum = sum(teichmueller_mod_p2(value, prime) for value in residues) % (prime * prime)
    if teich_sum != residue_digit + prime * first_digit:
        raise AssertionError("coordinate first-digit formula")
    return {
        "residue_digit": residue_digit,
        "first_quotient_digit": first_digit,
        "ordinary_internal_carry": internal_carry,
        "Fermat_correction_sum_mod_p": correction,
        "nonzero_terms": sum(value != 0 for value in residues),
    }


def chosen_prime_digits(h: int, s: int, prime: int) -> dict[str, Any]:
    n = 2 * h
    r = 2 * s + 1
    coordinate_residues = weighted_kummer_residues(h, s, prime)
    coordinates = [coordinate_digits(values, prime) for values in coordinate_residues]
    residue_sum = sum(value["residue_digit"] for value in coordinates)
    target_residue = residue_sum % prime
    cross_coordinate_carry = (residue_sum - target_residue) // prime
    first_digit = (
        cross_coordinate_carry
        + sum(value["first_quotient_digit"] for value in coordinates)
    ) % prime
    teich_total = sum(
        teichmueller_mod_p2(value, prime)
        for coordinate in coordinate_residues
        for value in coordinate
    ) % (prime * prime)
    if teich_total != target_residue + prime * first_digit:
        raise AssertionError("total first-digit formula")
    actual_target = ITEM339.a_hypergeometric(r, n) % prime
    if target_residue != actual_target:
        raise AssertionError("selected-target bridge")
    return {
        "coordinate_order": ["R0", "R1", "R2a", "R2b"],
        "coordinates": coordinates,
        "target_residue": target_residue,
        "cross_coordinate_carry": cross_coordinate_carry,
        "first_quotient_digit": first_digit,
        "Teichmueller_total_mod_p2": teich_total,
        "valuation_if_target_zero_and_first_digit_nonzero":
            1 if target_residue == 0 and first_digit != 0 else None,
    }


def interpolation_polynomial(prime: int) -> list[int]:
    """Unique degree <=p-1 polynomial for delta_p on F_p."""
    coefficients = [0] * prime
    # The indicator of a is 1-(X-a)^(p-1).
    for a in range(prime):
        value = fermat_correction(a, prime)
        coefficients[0] = (coefficients[0] + value) % prime
        for degree in range(prime):
            term = comb(prime - 1, degree) * pow(-a, prime - 1 - degree, prime)
            coefficients[degree] = (coefficients[degree] - value * term) % prime
    return coefficients


def maximal_degree_controls() -> list[dict[str, Any]]:
    output = []
    for prime in [13, 17, 43, 47]:
        coefficients = interpolation_polynomial(prime)
        degree = max(index for index, value in enumerate(coefficients) if value)
        expected_leading = (prime - 1) // 2
        if degree != prime - 1 or coefficients[-1] != expected_leading:
            raise AssertionError(("maximal correction degree", prime))
        for residue in range(prime):
            evaluated = sum(
                coefficient * pow(residue, degree_index, prime)
                for degree_index, coefficient in enumerate(coefficients)
            ) % prime
            if evaluated != fermat_correction(residue, prime):
                raise AssertionError(("correction interpolation", prime, residue))
        output.append(
            {
                "classification": "DECLARED EXACT FIELD-FUNCTION CONTROL; NOT A PRIME SCAN",
                "p": prime,
                "interpolation_degree": degree,
                "leading_coefficient": coefficients[-1],
                "expected_leading_coefficient": "(p-1)/2",
            }
        )
    return output


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        ((1, 1, 13), [0, 2, 0, 11], [0, 2, 1, 3], 0, 1, 7, 91),
        ((2, 1, 17), [9, 12, 2, 2], [8, 2, 12, 10], 8, 1, 16, 280),
        ((8, 2, 47), [41, 31, 13, 9], [9, 34, 36, 3], 0, 2, 37, 1739),
        ((4, 4, 43), [19, 24, 31, 14], [9, 39, 33, 38], 2, 2, 35, 1507),
        ((2, 6, 47), [10, 37, 30, 6], [43, 31, 41, 15], 36, 1, 37, 1775),
    ]
    output = []
    for row, expected_residues, expected_digits, expected_target, expected_cross, expected_digit, expected_mod_p2 in declared:
        h, s, prime = row
        result = chosen_prime_digits(h, s, prime)
        coordinate_residue_digits = [value["residue_digit"] for value in result["coordinates"]]
        coordinate_first_digits = [value["first_quotient_digit"] for value in result["coordinates"]]
        actual = (
            coordinate_residue_digits,
            coordinate_first_digits,
            result["target_residue"],
            result["cross_coordinate_carry"],
            result["first_quotient_digit"],
            result["Teichmueller_total_mod_p2"],
        )
        expected = (
            expected_residues,
            expected_digits,
            expected_target,
            expected_cross,
            expected_digit,
            expected_mod_p2,
        )
        if actual != expected:
            raise AssertionError(("declared chosen-prime digit", row, actual))
        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "full_original_collision_claimed": False,
                "h": h,
                "s": s,
                "M": 3 * h + 4 * s + 2,
                "p": prime,
                "n": 2 * h,
                "r": 2 * s + 1,
                **result,
            }
        )
    return output


def theorem_and_capacity() -> dict[str, Any]:
    return {
        "chosen_prime_first_digit": {
            "localization":
                "because p splits completely in Q(zeta_(p-1)), the chosen completion is Q_p and [a]=a+p delta_p(a) mod p^2",
            "correction": "delta_p(a)=(a^p-a)/p=a q_p(a) mod p for 0<=a<p",
            "absorbed_coordinates":
                "all four Teichmueller scalar weights multiply into y_(nu,x), so T=sum_(nu,x)[y_(nu,x)] exactly",
            "zero_row_formula":
                "if H(1)=0, T/p = (sum canonical y)/p + sum delta_p(y) mod p",
            "interpretation": "ordinary carry plus Fermat-quotient correction",
        },
        "maximal_degree_theorem": {
            "interpolant": "the unique F_p polynomial representing delta_p has exact degree p-1",
            "leading_coefficient": "(p-1)/2",
            "proof_key":
                "the leading coefficient is -sum_a delta_p(a); pairing a and p-a gives sum a^p=0 mod p^2 and hence sum delta_p(a)=-(p-1)/2 mod p",
            "scoped_conductor_no_go":
                "for the canonical integer residue section, a direct polynomial-phase treatment of the universal first correction cannot have bounded degree or bounded polynomial conductor; changing section, rational compression, or special composed cancellation remains open",
        },
        "valuation": {
            "not_forced":
                "H(1)=0 forces v_pfrak(T)>=1 but does not force v_pfrak(T)>=2; the predeclared p=13 and p=47 selected-zero controls both have valuation exactly 1",
            "ordinary_gate_warning":
                "even a theorem about the quotient digit would not exclude the ordinary mod-p selected zero unless the original collision supplied an additional p^2 gate",
        },
        "capacity": {
            "raw_support_reached": "all actual fixed-j1 rows, raw mass M/6+o(M)",
            "theoretical_ceiling_per_6M": "1/36",
            "new_forced_condition": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item353-j1-chosen-prime-first-digit-obstruction-certificate-v1",
        "item": 353,
        "date": "2026-09-01",
        "status": "PROVED_EXACT_CHOSEN_PRIME_FIRST_DIGIT_AND_MAXIMAL_DEGREE_SCOPED_NO_GO",
        "dependencies": DEPENDENCIES,
        "theorem_and_capacity": theorem_and_capacity(),
        "maximal_degree_controls": maximal_degree_controls(),
        "direct_controls": direct_controls(),
        "self_audit": {
            "ordinary_collision_direction_preserved": True,
            "selected_zero_promoted_to_full_collision": False,
            "mod_p2_theorem_credited_to_ordinary_mod_p_gate": False,
            "Gross_Koblitz_factorization_claimed_without_additive_character": False,
            "maximal_universal_degree_promoted_to_no_special_composition_theorem": False,
            "section_dependent_split_promoted_to_invariant_conductor_theorem": False,
            "finite_controls_used_as_density_evidence": False,
            "ledger_booking_without_weighted_theorem": False,
        },
        "classification": {
            "PROVED": [
                "exact chosen-prime Teichmueller expansion through p^2",
                "four-coordinate carry-plus-Fermat-correction formula",
                "exact maximal degree p-1 of the universal correction function",
                "selected zero does not formally force a second valuation digit",
                "scoped bounded-degree/conductor first-correction no-go",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected Kummer-coordinate digit controls and four exact field-function controls; no prime scan"
            ],
            "OPEN": [
                "special cancellation or factorization after composing delta_p with the actual four functions",
                "chosen-prime nonconcentration of the zeroth target digit",
                "a justified Gauss-sum/Gross--Koblitz factorization with positive-rate arithmetic reach",
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
                "item": 353,
                "chosen_prime_first_digit": "EXACT",
                "universal_correction_degree": "p-1",
                "selected_zero_forces_second_digit": False,
                "booking": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
