#!/usr/bin/env python3
"""Exact deterministic replay for Item 324.

The checker derives the two actual Item-321 parity quadrics in rational
coordinates, computes their all-phase resultant, verifies the even-row
Casoratian localization bridge and the odd-row intersection geometry, and
replays one preselected selected-parity witness.  It performs no prime scan.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item324_j1_cross_parity_resultant_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item308_j1_all_s_fixed_divisor_no_go_report.md":
        "4eb8f8c37dfde9d19e57c8df5ff8090bd95f03be59fff7d6aede55d02993bdc8",
    "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py":
        "9b60d380b503c7ac9fed13792fae67735cfcf6b0f376581a0076fde16a82f0b9",
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate.json":
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf",
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate_replay.json":
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf",
    "results/item308_j1_all_s_fixed_divisor_no_go_ledger.json":
        "eb5625613423ad5de16546d6c13860ef8e055867816648646b8a500cb00ad134",
    "manifests/item308_j1_all_s_fixed_divisor_no_go_manifest.json":
        "1c4721f43b5bbdc0c68e4d9fd689562a32a4af4fbbab2a9e7075da96b151b4d5",
    "results/item308_root_audit.json":
        "11feb8105ea46c27d83df2449404297fe74709eceaa8be6a21bd9484cbffba22",
    "sources/item321_fundamental_basis_operator_elimination_no_go_report.md":
        "bb41380371b6e591c4670aeb85d41520b0fb2b7f5f4d377e44bd531b5fa1b5c1",
    "scripts/item321_fundamental_basis_operator_elimination_no_go_certificate.py":
        "d5352d1bbcb77f875dc7e8eadc36c5f43d23f9dd3ccee06449c8fa7834577b1e",
    "results/item321_fundamental_basis_operator_elimination_no_go_certificate.json":
        "c196625c48a6e1f154cbbed29bc938eff53a318f172bb7679ade099aa5da3c35",
    "results/item321_fundamental_basis_operator_elimination_no_go_certificate_replay.json":
        "c196625c48a6e1f154cbbed29bc938eff53a318f172bb7679ade099aa5da3c35",
    "results/item321_fundamental_basis_operator_elimination_no_go_ledger_delta.json":
        "b603ed257a76bcba57f856ed7d1a9bee285764815eaee2753fa051c78003bba4",
    "manifests/item321_fundamental_basis_operator_elimination_no_go_manifest.json":
        "3555ca387f7b20366a4874fc161c9c048500486ec4126e94c1f07b97dcc7237f",
    "results/item321_fundamental_basis_operator_elimination_no_go_root_audit.json":
        "9759809da8c264f9d4975491f5520c44bf78905471272bd688bfe3ce3773eed6",
    "results/item321_fundamental_basis_operator_elimination_no_go_hashes.sha256":
        "e150b31590635b6dc5ed752771423c149a7a1d1bf39bbe9d765e2848ff93d1a0",
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
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM308 = load_module(
    "item324_canonical_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)

A, X, Y, Z, Zbar = S.symbols("A X Y Z Zbar")
M, s = S.symbols("M s", integer=True)
I = S.I


def parity_quadrics() -> dict[str, Any]:
    expected = {
        (0, 0): A**2 + 8 * X**2,
        (0, 1): A**2 - 8 * Y**2,
        (1, 0): A**2 - 4 * (X + Y) ** 2,
        (1, 1): A**2 + 4 * (X - Y) ** 2,
        (2, 0): A**2 - 8 * Y**2,
        (2, 1): A**2 + 8 * X**2,
        (3, 0): A**2 + 4 * (X - Y) ** 2,
        (3, 1): A**2 - 4 * (X + Y) ** 2,
    }
    rows = []
    for residue in range(4):
        delta_zero = (-1) ** (residue * (residue + 1) // 2 + 1)
        row_quadrics = []
        for epsilon in (0, 1):
            q = (
                A**2
                - 2 * delta_zero * (-I) ** residue * Z**2
                - 2 * delta_zero * I**residue * Zbar**2
                - 4 * (-1) ** epsilon * delta_zero * Z * Zbar
            )
            q_xy = S.expand(q.subs({Z: X + I * Y, Zbar: X - I * Y}))
            if S.expand(q_xy - expected[(residue, epsilon)]) != 0:
                raise AssertionError(("quadratic", residue, epsilon))
            row_quadrics.append(q_xy)
        resultant = S.factor(S.resultant(row_quadrics[0], row_quadrics[1], A))
        if S.expand(resultant - 64 * (X**2 + Y**2) ** 2) != 0:
            raise AssertionError(("resultant", residue))
        rows.append(
            {
                "s_mod_4": residue,
                "q_0": str(S.factor(row_quadrics[0])),
                "q_1": str(S.factor(row_quadrics[1])),
                "resultant_in_A": str(resultant),
            }
        )
    return {
        "coordinates": "Z=X+iY, Zbar=X-iY",
        "normalization": "q_(s,epsilon)=D_(s,epsilon)/(9*2^(27s+21))",
        "rows": rows,
        "uniform_identity": (
            "Res_A(q_(r,0),q_(r,1))=64*(X^2+Y^2)^2="
            "64*(Z*Zbar)^2"
        ),
        "unit_audit": (
            "actual p>=13, and every denominator/scaling used for A,Z,q "
            "has rational-prime support contained in {2,3}"
        ),
    }


def fixed_m_and_even_localization() -> dict[str, Any]:
    p_form = (4 * M + 2 * s + 1) / 3
    h_form = (M - 4 * s - 2) / 3
    if S.simplify(p_form.subs(s, s + 3) - p_form - 2) != 0:
        raise AssertionError("p step")
    if S.simplify(h_form.subs(s, s + 3) - h_form + 4) != 0:
        raise AssertionError("h step")

    p_mod_four = {residue: (2 * residue + 3) % 4 for residue in range(4)}
    if p_mod_four != {0: 3, 1: 1, 2: 3, 3: 1}:
        raise AssertionError("p mod 4")

    q_value = 660 * s**2 + 1600 * s + 779
    fixed_container = 330 * M**2 - 235 * M + 18
    identity = S.factor(q_value - 8 * fixed_container)
    expected = 5 * (66 * s - 132 * M + 127) * (4 * M + 2 * s + 1)
    if S.expand(identity - expected) != 0:
        raise AssertionError("Q fixed-M identity")
    u = S.symbols("u", nonnegative=True)
    shifted = S.Poly(S.expand(fixed_container.subs(M, u + 1)), u)
    if shifted.all_coeffs() != [330, 425, 113]:
        raise AssertionError("fixed container positivity")

    return {
        "fixed_M_indexing": {
            "S_M": "s>=1, 4s<=M-5, s congruent to M+1 mod 3",
            "p_s": "(4M+2s+1)/3",
            "h_s": "(M-4s-2)/3",
            "step": "s -> s+3 gives p -> p+2 and h -> h-4",
            "consequence": "h mod 4, hence epsilon=h mod 2, is constant on S_M",
        },
        "actual_p_mod_4": p_mod_four,
        "even_row_argument": [
            "even s gives p congruent to 3 mod 4",
            "q_0=q_1=0 gives X^2+Y^2=0 by the resultant",
            "-1 is nonsquare, so X=Y=0; either quadric then gives A=0",
            "the first row of the actual F_s vanishes, hence W_s=0",
        ],
        "casoratian_localization": (
            "Item321: W_s=0 on an actual row iff h=1 or p divides "
            "Q(s)=660s^2+1600s+779"
        ),
        "division_free_identity": (
            "Q(s)-8*(330M^2-235M+18)="
            "5*(66s-132M+127)*(4M+2s+1)"
        ),
        "fixed_container_nonzero": (
            "330M^2-235M+18=330(M-1)^2+425(M-1)+113>0"
        ),
        "proved_weighted_overlap_bound": (
            "sum over even s with prime p_s dividing both D_(s,0) and "
            "D_(s,1) is O(log M)=o(M)"
        ),
    }


def odd_intersection_geometry() -> dict[str, Any]:
    j = S.symbols("j")
    lines = []
    for u in (-1, 1):
        for v in (-1, 1):
            substitutions = {
                A: 2,
                X: S.Rational(1, 2) * (u - v * j),
                Y: S.Rational(1, 2) * (u + v * j),
            }
            difference_quadric = A**2 - 4 * (X + Y) ** 2
            sum_quadric = A**2 + 4 * (X - Y) ** 2
            reduced = []
            for q in (difference_quadric, sum_quadric):
                value = S.Poly(S.expand(q.subs(substitutions)), j)
                remainder = S.rem(value, S.Poly(j**2 + 1, j)).as_expr()
                reduced.append(S.expand(remainder))
            if reduced != [0, 0]:
                raise AssertionError(("odd intersection", u, v, reduced))
            lines.append(
                {
                    "u": u,
                    "v": v,
                    "representative_(A,X,Y)": [
                        "2",
                        f"({u}-{v}*j)/2",
                        f"({u}+{v}*j)/2",
                    ],
                    "relation": "j^2=-1",
                }
            )
    return {
        "actual_class": "odd s gives p congruent to 1 mod 4",
        "unordered_pair": [
            "A^2-4(X+Y)^2",
            "A^2+4(X-Y)^2",
        ],
        "four_nonzero_projective_intersections": lines,
        "conclusion": (
            "the cross-parity resultant has nonzero intersection states on "
            "odd rows; this is geometry only and asserts no actual prime zero"
        ),
    }


def selected_parity_witness() -> dict[str, Any]:
    s_value, h_value, prime = 2, 8, 47
    M_value = 3 * h_value + 4 * s_value + 2
    if prime != 4 * h_value + 6 * s_value + 3 or M_value != 34:
        raise AssertionError("witness indexing")
    if s_value % 3 != (M_value + 1) % 3 or 4 * s_value > M_value - 5:
        raise AssertionError("witness fixed-M slice")
    aggregate = (
        ITEM308.alpha_coefficient(s_value),
        *ITEM308.beta_coefficient(s_value),
    )
    rows = [ITEM308.integer_form(s_value, epsilon, aggregate) for epsilon in (0, 1)]
    residues = [row["D_s_epsilon"] % prime for row in rows]
    if residues != [0, 19]:
        raise AssertionError(("witness D residues", residues))
    w_h = (-1) ** (h_value // 2) * 2**h_value
    selected_linear_residue = (
        rows[0]["a_s"] + rows[0]["b_s_epsilon"] * w_h
    ) % prime
    if selected_linear_residue != 0:
        raise AssertionError("selected linear residue")
    return {
        "classification": "PRESELECTED EXACT CONTROL; NOT A SCAN",
        "row": {"M": M_value, "s": s_value, "h": h_value, "p": prime},
        "selected_epsilon": 0,
        "selected_linear_form_mod_p": selected_linear_residue,
        "D_0_mod_47": residues[0],
        "D_1_mod_47": residues[1],
        "meaning": (
            "the selected Item308 eliminant/container event need not imply "
            "the unused parity container; this is not asserted to be a full "
            "Item264 two-coordinate collision"
        ),
    }


def build_certificate() -> dict[str, Any]:
    item321 = json.loads(
        (ROOT / "results/item321_fundamental_basis_operator_elimination_no_go_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    if item321["capacity"]["new_linear_log_rate"] != 0:
        raise AssertionError("Item321 ledger")
    if "h=1" not in item321["casoratian"]["basis_failure_localization"]:
        raise AssertionError("Item321 localization")

    return {
        "schema": "item324-j1-cross-parity-resultant-no-go-v1",
        "item": 324,
        "status": "PROVED_CROSS_PARITY_RESULTANT_AND_SCOPED_SELECTED_SLICE_NO_GO",
        "dependencies": DEPENDENCIES,
        "parity_quadrics": parity_quadrics(),
        "fixed_M_and_even_localization": fixed_m_and_even_localization(),
        "odd_intersection_geometry": odd_intersection_geometry(),
        "selected_parity_witness": selected_parity_witness(),
        "capacity": {
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_fixed_j1_ceiling_per_6M": "1/36",
            "even_cross_parity_overlap_mass": "O(log M)=o(M)",
            "actual_selected_one_parity_mass": "UNCONTROLLED",
        },
        "classification": {
            "PROVED": [
                "all-phase cross-parity resultant",
                "even-row simultaneous-parity localization to Item321 Casoratian support",
                "O(log M) fixed-M even-overlap mass",
                "fixed-M parity constancy",
                "exact selected-parity p=47 witness",
            ],
            "EXACT_FINITE_ONLY": [
                "the one declared p=47 replay control; no scan inference",
            ],
            "SCOPED_NO_GO": [
                "a cross-parity resultant cannot bound W_D because the actual fixed-M slice selects one constant parity and the other container is not forced",
                "odd-row resultant geometry has nonzero intersections and supplies no actual-state exclusion",
            ],
            "OPEN": [
                "odd-row actual cross-parity overlap arithmetic",
                "actual selected one-parity weighted mass W_D(M)",
                "full-gate weighted mass W_off(M)",
                "fixed-j1 closure, Route 1, and e+pi",
            ],
        },
        "prime_scans": 0,
        "canonical_files_modified": False,
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
                "item": 324,
                "status": certificate["status"],
                "new_linear_log_rate": 0,
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
