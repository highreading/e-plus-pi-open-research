#!/usr/bin/env python3
"""Deterministic exact replay for Item 351.

The checker verifies the all-window Hasse--Taylor rank formula, the exact
Frobenius coefficient-window identity, the local order-three contiguous
recurrence, and one declared actual selected-zero control inherited from
Item 339.  It performs no prime scan and makes no density inference from
the finite control.
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
DEFAULT_OUTPUT = HERE / "item351_j1_companion_window_rank_obstruction_certificate.json"

# The executable identities use Item 342's pinned transitive Item 339
# implementation; Item 348 is pinned as the theorem source for the Hasse chart.
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
    "results/item348_j1_dwork_first_hasse_obstruction_certificate_replay.json":
        "ea9904c4411af6d8dc0199d347872bae361c591ab911db1fb19e5f1cb19d7de4",
    "results/item348_j1_dwork_first_hasse_obstruction_root_replay.json":
        "ea9904c4411af6d8dc0199d347872bae361c591ab911db1fb19e5f1cb19d7de4",
    "results/item348_j1_dwork_first_hasse_obstruction_ledger_delta.json":
        "7c68f01bbeac0c89fae9868ca23cf4df364194318e7ef8f1654423ce23be5490",
    "results/item348_j1_dwork_first_hasse_obstruction_root_audit.json":
        "75d75ae87a086d7d7e0a608a6216196f6f48296f090d8ff56cea320a31638ac3",
    "manifests/item348_j1_dwork_first_hasse_obstruction_manifest.json":
        "8a6835132fd4bd0c3e10d8abc216d9b7019cf73ec70f4691276d9849d9ad6aa9",
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
    "item351_pinned_item342",
    ROOT / "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py",
)
ITEM339 = ITEM342.ITEM339


def polynomial_multiply_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] = (output[i + j] + x * y) % prime
    return output


def polynomial_power_mod(base: list[int], exponent: int, prime: int) -> list[int]:
    output = [1]
    factor = [x % prime for x in base]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply_mod(output, factor, prime)
        exponent //= 2
        if exponent:
            factor = polynomial_multiply_mod(factor, factor, prime)
    return output


def normalized_left_hasse(r: int, n: int, prime: int) -> list[int]:
    terms = [value % prime for value in ITEM339.hypergeometric_terms(r, n)]
    if not terms or terms[0] == 0 or any(value == 0 for value in terms):
        raise AssertionError("declared left Hasse chart must have p-unit terms")
    inverse = pow(terms[0], -1, prime)
    return [value * inverse % prime for value in terms]


def hasse_taylor_coordinates(coefficients: list[int], prime: int) -> list[int]:
    degree = len(coefficients) - 1
    return [
        sum(comb(k, order) * coefficients[k] for k in range(order, degree + 1))
        % prime
        for order in range(degree + 1)
    ]


def pascal_minor(width: int) -> list[list[int]]:
    # Rows are Hasse derivative orders; columns are monomials z^k.
    return [[comb(column, row) if row <= column else 0 for column in range(width + 1)]
            for row in range(width + 1)]


def determinant_bareiss(matrix: list[list[int]]) -> int:
    if not matrix:
        return 1
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    denominator = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (j for j in range(pivot_index + 1, size) if work[j][pivot_index] != 0),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for i in range(pivot_index + 1, size):
            for j in range(pivot_index + 1, size):
                work[i][j] = (
                    work[i][j] * pivot
                    - work[i][pivot_index] * work[pivot_index][j]
                ) // denominator
        denominator = pivot
        for i in range(pivot_index + 1, size):
            work[i][pivot_index] = 0
    return sign * work[-1][-1]


def recurrence_residual(r: int, index: int, values: dict[int, int], prime: int) -> int:
    return (
        index * values[index]
        - 4 * (index + r - 1) * values.get(index - 1, 0)
        + 6 * (index + 2 * r - 2) * values.get(index - 2, 0)
        - 4 * (index + 3 * r - 3) * values.get(index - 3, 0)
    ) % prime


def declared_actual_control() -> dict[str, Any]:
    h, s, prime = 8, 2, 47
    n, r = 2 * h, 2 * s + 1
    coefficients = normalized_left_hasse(r, n, prime)
    expected_coefficients = [1, 4, 43, 23, 23]
    if coefficients != expected_coefficients:
        raise AssertionError("declared Hasse polynomial")
    taylor = hasse_taylor_coordinates(coefficients, prime)
    expected_taylor = [0, 16, 15, 21, 23]
    if taylor != expected_taylor:
        raise AssertionError(("declared Hasse--Taylor coordinates", taylor))

    expected_n_shifts = {
        -6: 2, -5: 9, -4: 9, -3: 15, -2: 39, -1: 21,
        0: 0, 1: 20, 2: 8, 3: 29, 4: 12, 5: 35, 6: 3,
    }
    actual_n_shifts = {
        shift: ITEM339.a_hypergeometric(r, n + shift) % prime
        for shift in expected_n_shifts
    }
    if actual_n_shifts != expected_n_shifts:
        raise AssertionError(("declared n-shift window", actual_n_shifts))

    expected_r_shifts = {
        -4: 15, -3: 33, -2: 14, -1: 43,
        0: 0, 1: 33, 2: 33, 3: 1, 4: 2,
    }
    actual_r_shifts = {
        shift: ITEM339.a_hypergeometric(r + shift, n) % prime
        for shift in expected_r_shifts
    }
    if actual_r_shifts != expected_r_shifts:
        raise AssertionError(("declared r-shift window", actual_r_shifts))

    values = {index: ITEM339.a_hypergeometric(r, index) % prime for index in range(n + 7)}
    if any(recurrence_residual(r, index, values, prime) for index in range(1, n + 7)):
        raise AssertionError("exact contiguous recurrence")

    frobenius_polynomial = polynomial_power_mod([1, -4, 6, -4], prime - r, prime)
    frobenius_window = {
        index: frobenius_polynomial[index] % prime for index in range(n - 6, n + 7)
    }
    reciprocal_window = {index: values[index] for index in range(n - 6, n + 7)}
    if frobenius_window != reciprocal_window:
        raise AssertionError("sub-p Frobenius coefficient-window identity")

    # Three consecutive zeros at indices q,q+1,q+2 would propagate
    # backwards because 4(q+2+3r-3) is a unit for q+2<2n+3.
    backward_coefficients = {
        upper: 4 * (upper + 3 * r - 3) % prime
        for upper in range(3, 2 * n + 3)
    }
    if any(value == 0 for value in backward_coefficients.values()):
        raise AssertionError("three-zero backward coefficient")

    return {
        "classification": "ONE PREDECLARED ACTUAL SELECTED-ZERO CONTROL; NOT A PRIME SCAN",
        "full_original_collision_claimed": False,
        "h": h,
        "s": s,
        "M": 3 * h + 4 * s + 2,
        "p": prime,
        "n": n,
        "r": r,
        "H_coefficients_mod_p": coefficients,
        "Hasse_Taylor_coordinates_at_1": taylor,
        "root_at_1": True,
        "root_at_1_is_simple": True,
        "n_shift_values_mod_p": actual_n_shifts,
        "r_shift_values_mod_p": actual_r_shifts,
        "Frobenius_window_equals_reciprocal_window": True,
        "recurrence_checked_indices": [1, n + 6],
        "three_consecutive_zero_propagation_coefficients_nonzero": True,
    }


def all_window_rank_controls() -> list[dict[str, Any]]:
    output = []
    for width in [0, 1, 2, 3, 4, 8, 12]:
        determinant = determinant_bareiss(pascal_minor(width))
        if determinant != 1:
            raise AssertionError(("Pascal determinant", width, determinant))
        output.append(
            {
                "classification": "DECLARED SYMBOLIC PASCAL-MINOR CONTROL",
                "width": width,
                "determinant": determinant,
                "rank": width + 1,
            }
        )
    return output


def theorem_and_capacity() -> dict[str, Any]:
    return {
        "Hasse_Taylor_all_window_theorem": {
            "coordinates":
                "H^[m](1)=sum_(k=m)^J C(k,m)c_k; H(z)=sum_m H^[m](1)(z-1)^m",
            "rank":
                "for every 0<=w<=J<p, the first w+1 coordinate rows have rank w+1; the leading Pascal minor has determinant 1",
            "forced_condition_rank":
                "H(1)=0 supplies only coordinate m=0; a second vanishing is an additional multiplicity condition, not a transfer consequence",
            "resultant_form":
                "H(1)=H^[1](1)=0 iff (z-1)^2 divides H; higher windows are equivalent to higher powers of z-1",
        },
        "Frobenius_and_contiguous_window": {
            "Frobenius":
                "G^(p-r)=G(u^p)G^(-r), so [u^m]G^(p-r)=a_(r,m) for every 0<=m<p",
            "recurrence":
                "m a_(r,m)=4(m+r-1)a_(r,m-1)-6(m+2r-2)a_(r,m-2)+4(m+3r-3)a_(r,m-3)",
            "local_module":
                "away from zero-rate endpoints, every sublinear n-window is transferred inside this nonsingular three-coordinate state; the transfer adds no zero equation",
            "three_zero_theorem":
                "three consecutive coefficient zeros below index 2n+3 propagate to a_(r,0)=0 and are impossible",
            "strict_scope":
                "the actual initial-value orbit is one special state; any extra congruence on that orbit requires new global arithmetic input",
        },
        "actual_row_companions": {
            "fixed_M_step": "(h,s,p)->(h+4q,s-3q,p-2q)",
            "bounded_prime_tuple_capacity":
                "for each fixed nonzero q, simultaneous primality of p and p-2q has O(M/log^2 M) rows and O(M/log M)=o(M) logarithmic mass by upper-bound sieve",
            "consequence":
                "a bounded collection of neighboring actual-prime rows is zero-rate and cannot control isolated selected rows",
        },
        "capacity": {
            "maximum_if_a_forced_codimension_two_gate_and_zero_density_were_proved":
                "at most the retained fixed-j1 ceiling 1/36 per 6M",
            "new_forced_independent_condition": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
            "booking": 0,
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item351-j1-companion-window-rank-obstruction-certificate-v1",
        "item": 351,
        "date": "2026-09-01",
        "status": "PROVED_ALL_WINDOW_HASSE_TAYLOR_RANK_AND_SCOPED_COMPANION_TRANSFER_NO_GO",
        "dependencies": DEPENDENCIES,
        "theorem_and_capacity": theorem_and_capacity(),
        "all_window_rank_controls": all_window_rank_controls(),
        "declared_actual_control": declared_actual_control(),
        "self_audit": {
            "ordinary_collision_direction_preserved": True,
            "selected_zero_promoted_to_full_collision": False,
            "actual_control_used_as_density_evidence": False,
            "ambient_rank_theorem_confused_with_actual_orbit_nonvanishing": False,
            "bounded_neighbor_prime_pairs_credited_to_isolated_rows": False,
            "geometric_F_crystal_claimed": False,
            "ledger_booking_without_mass_theorem": False,
        },
        "classification": {
            "PROVED": [
                "all-window Hasse--Taylor/Pascal rank and multiplicity criterion",
                "sub-p Frobenius coefficient-window identity",
                "exact order-three differential-contiguous recurrence",
                "impossibility of three consecutive coefficient zeros in the target local range",
                "zero-rate capacity of bounded neighboring actual-prime pairs",
                "scoped no-go for deriving a second condition from the existing selected equation and transfer identities alone",
            ],
            "EXACT_FINITE_ONLY": [
                "one predeclared p=47 selected-zero row and seven symbolic Pascal minors; no prime scan"
            ],
            "OPEN": [
                "any second companion condition forced by the full original collision through information not present in the selected gate",
                "multiple-root weighted density for the actual Hasse polynomial",
                "global arithmetic of the actual initial-value orbit",
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
                "item": 351,
                "Hasse_Taylor_window_rank": "FULL",
                "second_forced_companion": "NOT_DERIVED",
                "bounded_actual_neighbor_mass": "ZERO_RATE",
                "booking": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
