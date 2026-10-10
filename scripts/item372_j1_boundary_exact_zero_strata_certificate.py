#!/usr/bin/env python3
"""Deterministic exact replay for Item 372.

The checker verifies the terminal-term 3-adic separation for the tied
characteristic-zero values X_h and U_h on predeclared symbolic controls.
The all-h theorem is the elementary valuation argument recorded in the
report.  There is no prime scan, boundary census, or density inference.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item372_j1_boundary_exact_zero_strata_certificate.json"

DEPENDENCIES = {
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "results/item218_j1_common_log_certificate.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item364_j1_saturation_boundary_phase_carrier_report.md":
        "2c18f6ac22220e553349e44a723e200d20f4f3c89cfec5cd83812db260834e92",
    "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py":
        "ef9046fc4d7071779a73bf6e1bfd7d312789b994bd3274eec2a78d818d027b07",
    "results/item364_j1_saturation_boundary_phase_carrier_certificate.json":
        "ca1987d1688789dbf0e64f3eec2c4b771b9873f829e61d1b5f62302f47443926",
    "results/item364_j1_saturation_boundary_phase_carrier_root_audit.json":
        "fa6170a0c014cee655ba00c5288905344a969aa22b141d44b64ae4a2d3219a89",
    "manifests/item364_j1_saturation_boundary_phase_carrier_manifest.json":
        "bd0c5435fe4d0b7266d81b4f97dfacf8b2fca55fb2c95770e7cb853c2f77426c",
    "sources/item368_j1_boundary_whipple_rank_obstruction_report.md":
        "34bfdc2b2e4035ae78c0147d0a22f442e7f0fd148103e5eeee44d62042768cc6",
    "scripts/item368_j1_boundary_whipple_rank_obstruction_certificate.py":
        "f9d72b05fd24d62aa58fbca72221ff246a4d270b1eefb9023351cfd1aff932c5",
    "results/item368_j1_boundary_whipple_rank_obstruction_certificate.json":
        "8814c95cca55bf80b735668813909ed7e0f85ff30a1926a0df4b5b0c6f3c396d",
    "results/item368_j1_boundary_whipple_rank_obstruction_root_audit.json":
        "f20929fc3aa756419cf4263b439d90e6c44084c63f9acf64a4540134e3198321",
    "manifests/item368_j1_boundary_whipple_rank_obstruction_manifest.json":
        "eec70fc17c33e4ec7d3f8851a423debcca5abb333bbbe58decd3ab14736fd11a",
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
ITEM364 = load_module(
    "item372_pinned_item364",
    ROOT / "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py",
)


def v3_integer(value: int) -> int:
    if value == 0:
        raise ValueError("v3(0) is infinite and handled separately")
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        answer += 1
        value //= 3
    return answer


def v3_fraction(value: Fraction) -> int:
    if value == 0:
        raise ValueError("v3(0) is infinite and handled separately")
    return v3_integer(value.numerator) - v3_integer(value.denominator)


def pochhammer(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def normalized_terms(
    kernel: list[int],
    a_value: Fraction,
    b_value: Fraction,
    odd: bool,
) -> list[Fraction]:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    answer = []
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer.append(
            ((-1) ** t_value)
            * pochhammer(a_value, t_value)
            / pochhammer(b_value, t_value)
            * kernel[degree]
        )
    return answer


def terminal_ratio(
    kernel_coefficient: int,
    a_value: Fraction,
    b_value: Fraction,
    t_value: int,
    terminal: int,
) -> Fraction:
    sign = -1 if (terminal - t_value) % 2 else 1
    return (
        sign * kernel_coefficient
        * pochhammer(b_value + t_value, terminal - t_value)
        / pochhammer(a_value + t_value, terminal - t_value)
    )


def separation_record(
    label: str,
    kernel: list[int],
    a_value: Fraction,
    b_value: Fraction,
    odd: bool,
    expected_sum: Fraction,
) -> dict[str, Any]:
    terms = normalized_terms(kernel, a_value, b_value, odd)
    terminal = len(terms) - 1
    terminal_degree = 2 * terminal + 1 if odd else 2 * terminal
    if kernel[terminal_degree] != 1:
        raise AssertionError((label, terminal, terminal_degree, "terminal coefficient"))
    if terms[-1] == 0:
        raise AssertionError((label, terminal, "zero terminal term"))
    if sum(terms, Fraction(0)) != expected_sum:
        raise AssertionError((label, "phase sum"))

    terminal_valuation = v3_fraction(terms[-1])
    earlier = []
    for t_value, term in enumerate(terms[:-1]):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        if term == 0:
            earlier.append(
                {
                    "t": t_value,
                    "kernel_coefficient": kernel[degree],
                    "zero_term": True,
                }
            )
            continue
        ratio = terminal_ratio(
            kernel[degree], a_value, b_value, t_value, terminal
        )
        if ratio != term / terms[-1]:
            raise AssertionError((label, t_value, "terminal ratio"))
        ratio_valuation = v3_fraction(ratio)
        if ratio_valuation < terminal - t_value:
            raise AssertionError(
                (label, t_value, ratio_valuation, terminal - t_value)
            )
        if v3_fraction(term) <= terminal_valuation:
            raise AssertionError((label, t_value, "terminal not unique"))
        earlier.append(
            {
                "t": t_value,
                "kernel_coefficient": kernel[degree],
                "zero_term": False,
                "ratio_to_terminal_v3": ratio_valuation,
                "proved_lower_bound": terminal - t_value,
            }
        )

    if expected_sum == 0 or v3_fraction(expected_sum) != terminal_valuation:
        raise AssertionError((label, expected_sum, terminal_valuation))
    return {
        "label": label,
        "terminal_index": terminal,
        "terminal_degree": terminal_degree,
        "terminal_coefficient": 1,
        "terminal_v3": terminal_valuation,
        "sum_v3": v3_fraction(expected_sum),
        "sum_nonzero": True,
        "earlier_terms": earlier,
    }


def exact_zero_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 7, 8, 10, 11)
    rows = []
    for h_value in controls:
        if h_value % 3 == 0:
            raise AssertionError((h_value, "control is not potentially prime"))
        sigma = Fraction(-(4 * h_value + 3), 6)
        a_x = sigma + 1
        b_x = 3 * sigma + 2

        # Structural valuation residues.  The numerator of each A/sigma
        # factor is congruent to -h modulo 3; B and 3sigma have 3-unit
        # denominators, hence nonnegative valuation.
        for offset in range(h_value + 3):
            if v3_fraction(a_x + offset) != -1:
                raise AssertionError((h_value, offset, "A_x valuation"))
            if v3_fraction(sigma + offset) != -1:
                raise AssertionError((h_value, offset, "sigma valuation"))
            if v3_fraction(b_x + offset) < 0:
                raise AssertionError((h_value, offset, "B_x valuation"))
            if v3_fraction(3 * sigma + offset) < 0:
                raise AssertionError((h_value, offset, "3sigma valuation"))

        kernel_0 = ITEM364.ITEM218.kernel_integer(h_value, 1)
        kernel_1 = ITEM364.ITEM218.kernel_integer(h_value, 4)
        x_value, _, u_value, _ = ITEM364.phase_values(h_value)
        x_record = separation_record(
            "X", kernel_0, a_x, b_x, True, x_value
        )
        u_record = separation_record(
            "U", kernel_1, sigma, 3 * sigma, False, u_value
        )
        rows.append(
            {
                "h": h_value,
                "h_mod_3": h_value % 3,
                "X": x_record,
                "U": u_record,
            }
        )

    return {
        "classification": "EXACT PREDECLARED SUMMAND CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "all_h_lemma": {
            "X": (
                "for t<h, v3(T_t/T_h)>=h-t because every A_x+j has "
                "v3=-1 while B_x+j and the integer kernel coefficient have v3>=0"
            ),
            "U": (
                "for t<n=h+2, v3(S_t/S_n)>=n-t because every sigma+j has "
                "v3=-1 while 3sigma+j and the integer kernel coefficient have v3>=0"
            ),
            "ultrametric_consequence": (
                "the terminal term is uniquely lowest, so the full rational sum "
                "has its finite valuation and is nonzero"
            ),
        },
        "global_conclusion": "X_h!=0 and U_h!=0 for every h>=1 with 3 not dividing h",
        "exact_zero_sets": {"Z0": "empty", "Z1": "empty"},
    }


def capacity_replay() -> dict[str, Any]:
    if Fraction(1, 6) / 6 != Fraction(1, 36):
        raise AssertionError("fixed-j1 normalization")
    return {
        "former_target": (
            "sum log(p_h)*(exact-zero indicator + nonzero-carrier divisibility indicator)=o(M)"
        ),
        "sharpened_target": (
            "sum log(p_h)*1_(p_h divides mathfrak_G0(h)*mathfrak_G1(h))=o(M)"
        ),
        "exact_zero_indicator": 0,
        "weighted_divisibility_proved": False,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_shared_fixed_j1_ceiling_per_6M": "1/36",
    }


def build_result() -> dict[str, Any]:
    return {
        "item": 372,
        "schema": "item372-j1-boundary-exact-zero-strata-v1",
        "classification": "PROVED_BOTH_EXACT_ZERO_PHASE_STRATA_EMPTY",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "exact_zero_replay": exact_zero_replay(),
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "unique terminal-term 3-adic minimality for X_h on every potentially prime ray",
                "unique terminal-term 3-adic minimality for U_h on every potentially prime ray",
                "X_h and U_h are nonzero over Q for all h>=1 with 3 not dividing h",
                "Z0 and Z1 are empty",
                "the exact weighted target is now pure nonzero-carrier divisibility",
                "zero booking and retention of the shared 1/36 ceiling",
            ],
            "finite_only": [
                "eight predeclared exact summand controls",
                "no prime scan, boundary census, or extrapolation",
            ],
            "open": [
                "weighted zero density or average gcd for the nonzero primitive carriers",
                "modular occurrence or nonoccurrence of either boundary for unbounded h",
                "the nonboundary full-gate chart and any strict fixed-j1 capacity reduction",
            ],
        },
        "scope_warning": (
            "This is a characteristic-zero theorem. A nonzero rational phase value can "
            "still vanish modulo an actual tied prime, so no weighted modular mass is booked."
        ),
        "verdict": (
            "Both exact-zero phase strata are globally empty by unique terminal-term "
            "3-adic minimality; only nonzero-carrier divisibility remains, with no ledger change."
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
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "Z0": result["exact_zero_replay"]["exact_zero_sets"]["Z0"],
                "Z1": result["exact_zero_replay"]["exact_zero_sets"]["Z1"],
                "new_booking": result["capacity_replay"]["new_booking"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
