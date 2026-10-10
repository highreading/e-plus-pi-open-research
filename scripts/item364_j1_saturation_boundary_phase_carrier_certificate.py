#!/usr/bin/env python3
"""Deterministic exact replay for Item 364.

The checker constructs the two tied-phase saturation-boundary carrier
pairs from the exact Item 218 terminating periods.  It verifies the
all-s h=2 degenerate identity, the complete fixed-h exclusion through
h=8, and the order-one height comparison used in the scoped barrier.
There is no prime scan or collision census.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item364_j1_saturation_boundary_phase_carrier_certificate.json"

DEPENDENCIES = {
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "results/item218_j1_common_log_certificate.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "scripts/item360_j1_full_gate_transverse_period_certificate.py":
        "84cabfb296a0892e620f252a1c413648c30664c8667245bd6fe444095bcad7e0",
    "results/item360_j1_full_gate_transverse_period_certificate.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_root_audit.json":
        "7a23e487b4d70d63f9785339344bdc00ae0e8350bcf1d8b1fcf6228c230e5138",
    "manifests/item360_j1_full_gate_transverse_period_manifest.json":
        "92f88a56162f3803b8699922da921333f5225c41a32d14c87641dd53c3f8b55b",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify_dependencies()
ITEM218 = load_module(
    "item364_pinned_item218",
    ROOT / "scripts/item218_j1_common_log_certificate.py",
)


def normalized_sum_fraction(
    kernel: list[int],
    a_value: Fraction,
    q_value: Fraction,
    odd: bool,
) -> Fraction:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = Fraction(1)
    answer = Fraction(0)
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer += ratio * kernel[degree]
        if t_value == maximum_t:
            break
        numerator = a_value + t_value + (1 if odd else 0)
        denominator = q_value + a_value + t_value + (2 if odd else 1)
        if denominator == 0:
            raise ZeroDivisionError((a_value, q_value, t_value))
        ratio *= -numerator / denominator
    return answer


def phase_values(h_value: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if h_value < 1 or h_value % 3 == 0:
        raise ValueError("phase values are used only on potentially prime h rays")
    sigma = Fraction(-(4 * h_value + 3), 6)
    kernel_0 = ITEM218.kernel_integer(h_value, 1)
    kernel_1 = ITEM218.kernel_integer(h_value, 4)
    return (
        normalized_sum_fraction(kernel_0, sigma, 2 * sigma, True),
        normalized_sum_fraction(kernel_0, Fraction(h_value), 2 * sigma, True),
        normalized_sum_fraction(kernel_1, sigma, 2 * sigma - 1, False),
        normalized_sum_fraction(kernel_1, Fraction(h_value), 2 * sigma - 1, True),
    )


def prime_factorization(value: int) -> dict[int, int]:
    value = abs(value)
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def phase_carrier_replay() -> dict[str, Any]:
    expected = {
        1: (2, 4),
        2: (2, 13744),
        4: (14, 2),
        5: (2, 8),
        7: (26, 4),
        8: (2, 1),
    }
    rows = []
    digest = hashlib.sha256()
    for h_value, expected_carriers in expected.items():
        x_value, y_value, u_value, v_value = phase_values(h_value)
        carrier_xy = math.gcd(abs(x_value.numerator), abs(y_value.numerator))
        carrier_uv = math.gcd(abs(u_value.numerator), abs(v_value.numerator))
        if (carrier_xy, carrier_uv) != expected_carriers:
            raise AssertionError((h_value, carrier_xy, carrier_uv))

        factors_xy = prime_factorization(carrier_xy)
        factors_uv = prime_factorization(carrier_uv)
        compatible = []
        for label, factors in (("xy", factors_xy), ("uv", factors_uv)):
            for prime in factors:
                residual = prime - 4 * h_value - 3
                if residual >= 6 and residual % 6 == 0:
                    compatible.append((label, prime, residual // 6))
        if compatible:
            raise AssertionError((h_value, "unexpected tied boundary candidate", compatible))

        row = {
            "classification": "PREDECLARED FIXED-h ALL-s CONTROL; NOT A PRIME SCAN",
            "h": h_value,
            "sigma": fraction_record(Fraction(-(4 * h_value + 3), 6)),
            "phase_values": {
                "X": fraction_record(x_value),
                "Y": fraction_record(y_value),
                "U": fraction_record(u_value),
                "V": fraction_record(v_value),
            },
            "carrier_xy": carrier_xy,
            "carrier_xy_factorization": factors_xy,
            "carrier_uv": carrier_uv,
            "carrier_uv_factorization": factors_uv,
            "compatible_actual_primes": compatible,
        }
        rows.append(row)
        digest.update((json.dumps(row, sort_keys=True) + "\n").encode("ascii"))

    # h=3 and h=6 have p divisible by 3 on every tied row; p>3.
    for h_value in (3, 6):
        for s_value in (1, 2, 7):
            tied = 4 * h_value + 6 * s_value + 3
            if tied <= 3 or tied % 3:
                raise AssertionError((h_value, s_value, tied))

    return {
        "classification": "EXACT FIXED-h ALL-s CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "row_digest_sha256": digest.hexdigest(),
        "composite_h_rays": [3, 6],
        "conclusion": "neither saturation boundary occurs on any actual tied row with 1<=h<=8",
    }


def h2_degenerate_replay() -> dict[str, Any]:
    kernel_1 = ITEM218.kernel_integer(2, 4)
    if kernel_1 != [1, 0, -4, 0, 6, 0, -4, 0, 1]:
        raise AssertionError(kernel_1)

    u_value = ITEM218.normalized_sum_symbolic(kernel_1, 1, 0, 2, -1, False)
    v_value = ITEM218.normalized_sum_symbolic(kernel_1, 0, 2, 2, -1, True)
    expected_u_num = (Fraction(108), Fraction(320), Fraction(256))
    expected_u_den = (Fraction(18), Fraction(81), Fraction(81))
    if ITEM218.pmul(u_value[0], expected_u_den) != ITEM218.pmul(
        expected_u_num, u_value[1]
    ):
        raise AssertionError("h=2 u identity")
    if v_value[0] != (Fraction(0),):
        raise AssertionError("h=2 v is not identically zero")

    phase_u = phase_values(2)[2]
    if phase_u != Fraction(13744, 5103):
        raise AssertionError(phase_u)
    if prime_factorization(859) != {859: 1} or 859 % 6 != 1:
        raise AssertionError("859 arithmetic")

    return {
        "classification": "PROVED SYMBOLIC ALL-s DEGENERATE-FACE IDENTITY",
        "kernel": "K1=(1-z^2)^4",
        "v": "0 identically",
        "u": "4(64s^2+80s+27)/(9(3s+1)(3s+2))",
        "tied_phase_u": fraction_record(phase_u),
        "only_large_numerator_prime": 859,
        "residue_obstruction": "actual p=6s+11 is 5 mod 6, whereas 859 is 1 mod 6",
        "conclusion": "u=v=0 never occurs on the actual h=2 ray",
    }


def comparison_barrier_replay() -> dict[str, Any]:
    controls = [
        (9, 1, 1, 13),
        (12, 2, 1, 17),
        (34, 8, 2, 47),
        (30, 4, 4, 43),
    ]
    rows = []
    for M_value, h_value, s_value, prime in controls:
        if M_value != 3 * h_value + 4 * s_value + 2:
            raise AssertionError("M tie")
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError("p tie")
        if 12 * h_value < M_value:
            raise AssertionError("not in comparison bulk")
        if not (4 * h_value < prime <= 18 * h_value):
            raise AssertionError("comparison interval")
        comparison = math.factorial(18 * h_value) // math.factorial(4 * h_value)
        if comparison % prime:
            raise AssertionError("comparison divisibility")
        rows.append((M_value, h_value, s_value, prime))

    return {
        "classification": "EXACT COMPARISON FAMILY FOR SCOPED METHOD BARRIER",
        "carrier": "C_h=(18h)!/(4h)!=(4h+1)_(14h)",
        "first_order_recurrence": (
            "C_(h+1)/C_h=product_(j=1)^18(18h+j)"
            "/product_(j=1)^4(4h+j)"
        ),
        "height": "log C_h=O(h log(h+2))",
        "bulk": "M/12<=h<=M/3 gives 4h<p=(3M-h)/2<18h",
        "bulk_raw_chebyshev_mass": "M/8+o(M)",
        "bulk_capacity_per_6M": "1/48",
        "declared_rows": rows,
        "scope": (
            "generic pointwise height and recurrence order alone cannot prove zero-rate; "
            "no resemblance to the actual phase carriers is asserted"
        ),
    }


def capacity_replay() -> dict[str, Any]:
    if Fraction(1, 6) / 6 != Fraction(1, 36):
        raise AssertionError("full cell normalization")
    if Fraction(1, 8) / 6 != Fraction(1, 48):
        raise AssertionError("comparison bulk normalization")
    return {
        "raw_fixed_j1_mass_per_M": "1/6",
        "full_fixed_j1_ceiling_per_6M": "1/36",
        "boundary_components_additive": False,
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item364-j1-saturation-boundary-phase-carrier-v1",
        "classification": "PROVED_PHASE_CARRIERS_AND_SCOPED_RECURRENCE_HEIGHT_BARRIER",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "proved_formulae": {
            "tied_phase": "sigma_h=-(4h+3)/6 and s=sigma_h mod p",
            "xy_localization": "x=y=0 implies p divides G_h^(0)=gcd(num X_h,num Y_h)",
            "uv_localization": "u=v=0 implies p divides G_h^(1)=gcd(num U_h,num V_h)",
            "h2": "v=0 identically, while u=4(64s^2+80s+27)/(9(3s+1)(3s+2))",
            "fixed_h": (
                "if a phase pair is not exactly zero, a fixed h has only finitely "
                "many boundary primes; exact-zero phase rays are stratified separately"
            ),
            "pointwise_height": "log max(G_h^(0),G_h^(1),1)=O(h log(h+2))",
        },
        "phase_carrier_replay": phase_carrier_replay(),
        "h2_degenerate_replay": h2_degenerate_replay(),
        "comparison_barrier_replay": comparison_barrier_replay(),
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "exact tied-phase specialization of all four boundary periods",
                "two primitive fixed-h gcd carrier implications",
                "complete all-s boundary exclusion for 1<=h<=8",
                "the h=2 degenerate-face identity and exclusion",
                "fixed-finite-h zero-rate and the pointwise O(h log h) height bound",
                "generic recurrence-height comparison barrier",
            ],
            "finite_only": [
                "six predeclared fixed-h carrier controls",
                "four predeclared comparison rows",
                "no prime scan or collision census",
            ],
            "open": [
                "classification of exact-zero phase pairs and whether either boundary occurs with unbounded h",
                "weighted zero density for the two actual phase-carrier gcd sequences",
                "a target-specific unit Casoratian, large-prime-factor, or average-gcd theorem",
                "any strict fixed-j1 capacity reduction",
            ],
        },
        "scope_warning": (
            "The comparison family closes only generic height/recurrence-order reasoning. "
            "It does not rule out target-specific arithmetic of the actual carrier pairs. "
            "The two boundary components are subsets of one full gate and are not additive."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
