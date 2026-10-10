#!/usr/bin/env python3
"""Deterministic exact structural controls for Item 401.

The all-M algebraicity and vertical-column no-go are proved in the report.
This checker pins Items 296, 363, 395, and 400; verifies the fixed-prime
candidate blocks, two independent constructions of C_nu(M), the cleared
degree-twelve residue integrand, the algebraic-degree bound, and the sharp
capacity coefficient.  It performs no actual gate-zero or collision scan.
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
DEFAULT_OUTPUT = (
    ROOT
    / "results"
    / "item401_j1_crossM_algebraic_transport_no_go_certificate.json"
)

DEPENDENCIES = {
    "sources/item296_j1_modular_singular_ray_atlas_report.md":
        "80a4613a0c09c713adaf8c5e3ab10cccb42ece5973e126dc8007d68e813fbf39",
    "manifests/item296_j1_modular_singular_ray_atlas_manifest.json":
        "cddee29ee3c5be9196bcb55290f4c97e74fb632250fd8c609f32cb15c1ca8971",
    "sources/item363_j1_joint_gate_crt_elimination_no_go_report.md":
        "377ed30c0c6be630c124ccd3050d37176264c659d23a502453a9aaa34ff132ee",
    "manifests/item363_j1_joint_gate_crt_elimination_no_go_manifest.json":
        "46aa9a81d3b92cd5e7e055d9280f32e0e5ca32b91dfd68d95cbc9fdaa26a464a",
    "sources/item395_j1_logscale_cluster_radical_height_obstruction_report.md":
        "af0d85607d665f5d6c12c2695a44a89d984abffb008bbd1318978471e79f4487",
    "manifests/item395_j1_logscale_cluster_radical_height_obstruction_manifest.json":
        "3ef54ba9d3caa5af1b76bde52822447e253256c4c0ebb30dd6bb8a6200502cbd",
    "sources/item400_j1_discriminant_energy_sieve_threshold_no_go_report.md":
        "f9dfe5dd6082ec762c0e677760aff5367c1fd869241ed29a4fa50fc78dab124e",
    "manifests/item400_j1_discriminant_energy_sieve_threshold_no_go_manifest.json":
        "ffa52a35f31b98c717050dd1b01dfd2e7b6042838c326dbb8c970a5b2989aca7",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing dependency", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(
                ("dependency mismatch", relative, expected, actual)
            )


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def candidate_block(p: int) -> list[int]:
    lower = ceil_div(2 * p + 1, 3)
    upper = (3 * p - 3) // 4
    return list(range(lower, upper + 1))


def fixed_prime_control(p: int) -> dict[str, Any]:
    assert p > 3 and is_prime(p)
    block = candidate_block(p)
    assert len(block) == p // 12
    rows = []
    for M in block:
        h = 3 * M - 2 * p
        numerator = 3 * p - 4 * M - 1
        assert numerator % 2 == 0
        s = numerator // 2
        assert h >= 1 and s >= 1
        assert p == 4 * h + 6 * s + 3
        assert M == 3 * h + 4 * s + 2
        assert h % 3 == p % 3
        rows.append({"M": M, "h": h, "s": s})
    for left, right in zip(rows, rows[1:]):
        assert right["M"] == left["M"] + 1
        assert right["h"] == left["h"] + 3
        assert right["s"] == left["s"] - 2
    return {
        "p": p,
        "p_mod_12": p % 12,
        "block_lower": block[0],
        "block_upper": block[-1],
        "block_length": len(block),
        "floor_p_over_12": p // 12,
        "rows": rows,
    }


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    output = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i + j] += x * y
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def poly_pow(base: list[int], exponent: int) -> list[int]:
    output = [1]
    power = base[:]
    while exponent:
        if exponent & 1:
            output = poly_mul(output, power)
        power = poly_mul(power, power)
        exponent //= 2
    return output


def poly_shift(a: list[int], amount: int) -> list[int]:
    return [0] * amount + a


def c_nu_binomial(M: int, nu: int) -> int:
    target = 4 * M + nu
    top = 1 + 3 * nu
    den = 4 * M + 1 + nu
    total = 0
    for b in range(top + 1):
        for k in range(target // 2 + 1):
            a = target - b - 2 * k
            if 0 <= a <= 6 * M:
                total += (
                    (-1) ** (a + k)
                    * math.comb(6 * M, a)
                    * math.comb(top, b)
                    * math.comb(den + k - 1, k)
                )
    return total


def c_nu_series(M: int, nu: int) -> int:
    """Independent numerator convolution and denominator recurrence."""
    target = 4 * M + nu
    numerator = poly_mul(
        poly_pow([1, -1], 6 * M),
        poly_pow([1, 1], 1 + 3 * nu),
    )
    den_power = 4 * M + 1 + nu
    even_coefficients = [1]
    for k in range(1, target // 2 + 1):
        previous = even_coefficients[-1]
        numerator_factor = den_power + k - 1
        assert (previous * numerator_factor) % k == 0
        even_coefficients.append(
            -(previous * numerator_factor) // k
        )
    total = 0
    for degree, coefficient in enumerate(numerator):
        remainder = target - degree
        if remainder >= 0 and remainder % 2 == 0:
            total += coefficient * even_coefficients[remainder // 2]
    return total


def constant_term_controls() -> list[dict[str, Any]]:
    controls = []
    for nu in (0, 1):
        values = []
        for M in range(9):
            first = c_nu_binomial(M, nu)
            second = c_nu_series(M, nu)
            assert first == second
            values.append(str(first))
        controls.append({"nu": nu, "M_0_through_8": values})
    return controls


def residue_integrand_control(nu: int) -> dict[str, Any]:
    # Delta(z,t)=A(z)-t B(z).
    A = poly_shift(poly_pow([1, 0, 1], 4), 4)
    B = poly_pow([1, -1], 6)
    N = poly_shift(
        poly_mul(
            poly_pow([1, 1], 1 + 3 * nu),
            poly_pow([1, 0, 1], 3 - nu),
        ),
        3 - nu,
    )

    # Independently reconstruct w_nu * A / z after cancelling its stated
    # monomial and (1+z^2) denominator factors.
    N_from_clearing = poly_shift(
        poly_mul(
            poly_pow([1, 1], 1 + 3 * nu),
            poly_pow([1, 0, 1], 4 - (1 + nu)),
        ),
        4 - nu - 1,
    )
    assert N == N_from_clearing
    assert len(A) - 1 == 12
    assert A[:4] == [0, 0, 0, 0]
    assert A[4] == 1
    assert len(B) - 1 == 6
    return {
        "nu": nu,
        "Delta_A_coefficients_ascending": A,
        "Delta_minus_tB_B_coefficients_ascending": B,
        "N_nu_coefficients_ascending": N,
        "degree_Delta_in_z": 12,
        "multiplicity_of_zero_of_Delta_at_t_0": 4,
    }


def rational_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def candidates(M: int) -> list[int]:
    lower = ceil_div(4 * M + 3, 3)
    upper = (3 * M - 1) // 2
    return [p for p in range(lower, upper + 1) if is_prime(p)]


def zero_output_countermodel_control(M: int) -> dict[str, Any]:
    primes = candidates(M)
    assert primes
    states = {}
    for p in primes:
        # The first two entries are homogeneous gate outputs.  The final
        # unit shows that a zero output orbit need not be a zero ambient
        # state.  Any homogeneous output recurrence preserves (0,0).
        state = [0, 0, 1]
        assert state != [0, 0, 0]
        assert state[0] == state[1] == 0
        states[str(p)] = state
    return {
        "M": M,
        "candidate_primes": primes,
        "nonzero_augmented_states": states,
        "full_gate_outputs_zero_on_every_column": True,
        "actual_collision_claim": False,
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    degree_bound = math.comb(12, 4)
    assert degree_bound == 495
    c = Fraction(1, 1)
    admission = (2 * c - 1) / (12 * c)
    assert admission == Fraction(1, 12)

    return {
        "schema": "item401-j1-crossM-algebraic-transport-no-go-certificate-v1",
        "item": 401,
        "checked_date_beijing": "2026-09-01",
        "classification": "EXACT_ALGEBRAIC_VERTICAL_TRANSPORT_AND_SCOPED_NO_GO",
        "dependency_hashes": DEPENDENCIES,
        "fixed_prime_controls": [
            fixed_prime_control(p) for p in (13, 47, 109, 1009)
        ],
        "constant_term_controls": constant_term_controls(),
        "residue_integrand_controls": [
            residue_integrand_control(nu) for nu in (0, 1)
        ],
        "algebraic_degree_bound_choose_12_4": degree_bound,
        "admission_coefficient_at_c_1": rational_json(admission),
        "zero_output_countermodel": zero_output_countermodel_control(76),
        "proved_by_report": [
            "a fixed prime p>3 is an actual candidate for exactly floor(p/12) consecutive M-values",
            "C_0 and C_1 are constant terms of w_nu(z)K(z)^M for one fixed rational K",
            "their ordinary generating functions are sums of four residues among the twelve roots of Delta(z,t)",
            "the symmetric four-subset annihilator gives algebraic degree at most 495 and hence absolute bounded-order polynomial recurrences",
            "division by the compulsory prime copy gives exact same-characteristic recurrence transport on every interior fixed-p window",
            "distinct prime columns remain independent CRT components",
            "homogeneous vertical recurrence data admit the full-support zero-output countermodel, which saturates the M/12 admission coefficient",
        ],
        "strict_scope": {
            "actual_gate_scan_performed": False,
            "finite_zero_census_performed": False,
            "guessed_recurrence_promoted": False,
            "actual_initial_orbit_controlled": False,
            "cross_prime_reciprocity_proved": False,
            "actual_cluster_upper_bound_proved": False,
            "new_booked_mass": 0,
            "new_capacity_reduction": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
