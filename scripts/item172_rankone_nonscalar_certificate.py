#!/usr/bin/env python3
"""Exact checks for Item 172's non-scalar kappa=1 analysis.

The uniform statements are proved in the companion report.  This checker
specializes the scalar-free determinant carry tower to the kappa=1 cell,
replays a small set of exact Hasse controls, and classifies the frozen
m<=250 census.  All density conclusions drawn from the census itself are
explicitly labelled experimental.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from fractions import Fraction
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
DEFAULT_CENSUS = (
    HERE / "item164_third_layer_extended_census_m250.json"
    if (HERE / "item164_third_layer_extended_census_m250.json").exists()
    else HERE.parent / "results" / "item164_third_layer_extended_census_m250.json"
)
DEFAULT_ITEM163 = HERE / "item163_deeper_digits_certificate.py"
DEFAULT_OUTPUT = (
    HERE / "item172_rankone_nonscalar_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item172_rankone_nonscalar_certificate.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generalized_binomial_row(exponent: int, degree: int, p: int) -> list[int]:
    if not (0 <= degree < p):
        raise ValueError((exponent, degree, p))
    row = [1]
    value = 1
    for k in range(1, degree + 1):
        value = value * (exponent - k + 1) % p
        value = value * pow(k, -1, p) % p
        row.append(value)
    return row


def four_section_coefficient(
    linear_exponent: int, four_exponent: int, degree: int, p: int
) -> int:
    linear = generalized_binomial_row(linear_exponent, degree, p)
    four = generalized_binomial_row(
        four_exponent, min(four_exponent, degree // 4), p
    )
    total = 0
    for v, choose_four in enumerate(four):
        k = degree - 4 * v
        total += (-1 if (v + k) & 1 else 1) * choose_four * linear[k]
    return total % p


def rank_one_scalars(p: int, s: int) -> tuple[int, int]:
    """Cartier scalar residues modulo p on kappa=1, independent of j."""
    if not (0 <= s <= (p - 3) // 3):
        raise ValueError((p, s))
    r = p - 3 * s - 3
    h = 2 * s + 1
    degree = 3 * s + 2
    return (
        four_section_coefficient(r - h, h, degree, p),
        four_section_coefficient(r - h + 1, h - 1, degree, p),
    )


def kappa_one_coordinates(m: int, p: int) -> tuple[int, int] | None:
    if not (p < 2 * m and p <= 4 * m + 1 < p * p):
        return None
    a, _ = divmod(6 * m, p)
    b, _ = divmod(4 * m + 1, p)
    if 2 * a - 3 * b != 1 or b % 2 != 1:
        return None
    j = (b - 1) // 2
    s = (j + 1) * p - (2 * m + 1)
    if not (j >= 1 and 0 <= s <= (p - 3) // 3 and s % 2 == j % 2):
        raise AssertionError((m, p, a, b, j, s))
    if 2 * m + 1 != (j + 1) * p - s:
        raise AssertionError((m, p, j, s))
    return j, s


def frozen_kappa_one(census: dict[str, Any]) -> dict[str, Any]:
    forced: dict[tuple[int, int], dict[str, Any]] = {}
    for source in census["forced_rows"]:
        m, p = int(source["m"]), int(source["p"])
        cell = kappa_one_coordinates(m, p)
        if cell is None:
            continue
        j, s = cell
        if int(source["delta"]) != 0 or "rank_one" not in str(source["source"]):
            raise AssertionError(("kappa=1 classification", source, j, s))
        gamma0, gamma1 = rank_one_scalars(p, s)
        forced[(m, p)] = {
            "m": m,
            "p": p,
            "j": j,
            "s": s,
            "gamma0": gamma0,
            "gamma1": gamma1,
            "simultaneous_scalar_zero": gamma0 == gamma1 == 0,
            "A0": int(source["A0"]),
        }

    p2: dict[tuple[int, int], dict[str, Any]] = {}
    for source in census["p2_candidates"]:
        key = int(source["m"]), int(source["p"])
        if key not in forced:
            continue
        digits = [int(value) for value in source["A_digits_after_forced_power"]]
        row = {
            **forced[key],
            "A_digits": digits,
            "B0": int(source["B0_after_forced_power"]),
            "p3_gate": bool(source["p3_gate"]),
        }
        if row["A0"] != 0 or digits[0] != 0:
            raise AssertionError(("p2 normalization", row))
        p2[key] = row

    p3: dict[tuple[int, int], dict[str, Any]] = {}
    for source in census["p3_survivors"]:
        key = int(source["m"]), int(source["p"])
        if key in p2:
            p3[key] = p2[key]

    scalar_zero = [row for row in forced.values() if row["simultaneous_scalar_zero"]]
    a0_zero = list(p2.values())
    nonscalar_a0_zero = [row for row in a0_zero if not row["simultaneous_scalar_zero"]]
    nonscalar_p3 = [row for row in p3.values() if not row["simultaneous_scalar_zero"]]

    by_ps: dict[tuple[int, int], list[dict[str, Any]]] = collections.defaultdict(list)
    for row in forced.values():
        by_ps[(row["p"], row["s"])].append(row)
    j_dependence_controls = []
    for (p, s), rows in sorted(by_ps.items()):
        values = {int(row["A0"]) for row in rows}
        if len(values) < 2:
            continue
        zero_rows = [row for row in rows if int(row["A0"]) == 0]
        nonzero_rows = [row for row in rows if int(row["A0"]) != 0]
        if zero_rows and nonzero_rows:
            j_dependence_controls.append(
                {
                    "p": p,
                    "s": s,
                    "gamma": [rows[0]["gamma0"], rows[0]["gamma1"]],
                    "zero_rows": [
                        {"m": row["m"], "j": row["j"], "A0": row["A0"]}
                        for row in zero_rows
                    ],
                    "first_nonzero_rows": [
                        {"m": row["m"], "j": row["j"], "A0": row["A0"]}
                        for row in nonzero_rows[:3]
                    ],
                }
            )

    return {
        "forced": forced,
        "p2": p2,
        "p3": p3,
        "summary": {
            "forced_kappa_one_rows": len(forced),
            "simultaneous_scalar_zero_rows": len(scalar_zero),
            "A0_zero_rows": len(a0_zero),
            "nonscalar_A0_zero_rows": len(nonscalar_a0_zero),
            "p3_gate_rows": len(p3),
            "nonscalar_p3_gate_rows": len(nonscalar_p3),
            "same_p_s_groups_with_zero_and_nonzero_A0": len(j_dependence_controls),
        },
        "first_nonscalar_A0_zero_rows": nonscalar_a0_zero[:30],
        "p3_rows": list(p3.values()),
        "j_dependence_controls": j_dependence_controls,
    }


def affine_search(
    forced: dict[tuple[int, int], dict[str, Any]],
    survivors: set[tuple[int, int]],
) -> dict[str, Any]:
    """Finite diagnostic for p=A*s+B; never promoted to a classification."""
    candidates = []
    residue_refinements = []
    identity_failures = []
    rows = list(forced.values())
    for a in range(1, 13):
        for b in range(-20, 21):
            on_line = [row for row in rows if row["p"] == a * row["s"] + b]
            if not on_line:
                continue
            for row in on_line:
                # From 2m+1=(j+1)p-s and p=as+b.
                if (2 * a * row["m"] + a - b) % row["p"]:
                    identity_failures.append(
                        {"a": a, "b": b, "m": row["m"], "p": row["p"]}
                    )
            distinct_primes = len({row["p"] for row in on_line})
            if len(on_line) >= 8 and distinct_primes >= 3:
                candidates.append(
                    {
                        "equation": f"p={a}*s+({b})",
                        "row_count": len(on_line),
                        "distinct_prime_count": distinct_primes,
                        "all_A0_zero": all(row["A0"] == 0 for row in on_line),
                        "all_p3": all((row["m"], row["p"]) in survivors for row in on_line),
                        "A0_zero_count": sum(row["A0"] == 0 for row in on_line),
                        "p3_count": sum(
                            (row["m"], row["p"]) in survivors for row in on_line
                        ),
                        "divisor_linear_form": f"{2*a}*m+({a-b})",
                    }
                )
            for modulus in (4, 8, 12, 20):
                for residue in range(modulus):
                    refined = [row for row in on_line if row["p"] % modulus == residue]
                    refined_distinct = len({row["p"] for row in refined})
                    if len(refined) < 4 or refined_distinct < 2:
                        continue
                    residue_refinements.append(
                        {
                            "equation": f"p={a}*s+({b})",
                            "residue_condition": f"p={residue} mod {modulus}",
                            "row_count": len(refined),
                            "distinct_prime_count": refined_distinct,
                            "all_A0_zero": all(row["A0"] == 0 for row in refined),
                            "all_p3": all(
                                (row["m"], row["p"]) in survivors for row in refined
                            ),
                            "A0_zero_count": sum(row["A0"] == 0 for row in refined),
                            "p3_count": sum(
                                (row["m"], row["p"]) in survivors for row in refined
                            ),
                            "divisor_linear_form": f"{2*a}*m+({a-b})",
                        }
                    )
    if identity_failures:
        raise AssertionError(identity_failures[:3])
    candidates.sort(
        key=lambda row: (
            not row["all_A0_zero"],
            -row["A0_zero_count"],
            -row["row_count"],
            row["equation"],
        )
    )
    residue_refinements.sort(
        key=lambda row: (
            not row["all_A0_zero"],
            -row["A0_zero_count"],
            -row["row_count"],
            row["equation"],
            row["residue_condition"],
        )
    )
    return {
        "search_box": {"1<=A<=": 12, "-20<=B<=": 20},
        "minimum_rows": 8,
        "minimum_distinct_primes": 3,
        "candidate_count": len(candidates),
        "all_A0_zero_candidates": [row for row in candidates if row["all_A0_zero"]],
        "all_p3_candidates": [row for row in candidates if row["all_p3"]],
        "first_candidates": candidates[:30],
        "residue_refined_all_A0_zero_candidates": [
            row for row in residue_refinements if row["all_A0_zero"]
        ],
        "residue_refined_all_p3_candidates": [
            row for row in residue_refinements if row["all_p3"]
        ],
        "first_residue_refinements": residue_refinements[:40],
        "thin_identity_failures": len(identity_failures),
        "interpretation": "EXPERIMENTAL_FINITE_SEARCH_ONLY",
    }


def quantitative_tail_checks() -> dict[str, Any]:
    """Exact cell-width identity and a summable comparison for the j tail."""
    rows = []
    for cutoff in (1, 2, 5, 10, 50, 100, 1000):
        partial = math.fsum(
            2.0 / ((3 * j + 2) * (j + 1))
            for j in range(cutoff + 1, 200_001)
        )
        comparison_remainder = 2.0 / (3 * (cutoff + 1))
        if partial >= comparison_remainder:
            raise AssertionError(("tail comparison", cutoff, partial, comparison_remainder))
        rows.append(
            {
                "J": cutoff,
                "truncated_tail_through_200000": partial,
                "proved_infinite_tail_upper_bound": comparison_remainder,
                "chebyshev_prime_cutoff_ratio": 6.0 / (3 * cutoff + 5),
            }
        )
    for j in range(1, 10_000):
        width = Fraction(6, 3 * j + 2) - Fraction(2, j + 1)
        if width != Fraction(2, (3 * j + 2) * (j + 1)):
            raise AssertionError(("cell width", j, width))
        if width > Fraction(2, 3 * j * (j + 1)):
            raise AssertionError(("cell comparison", j, width))
    return {
        "cell_width_identity": "6/(3j+2)-2/(j+1)=2/((3j+2)(j+1))",
        "tail_bound": "sum_{j>J} width_j < 2/(3(J+1))",
        "uniform_elementary_tail": "j>J implies p<6m/(3J+5), hence log-prime tail <= theta(6m/(3J+5))=O(m/J)",
        "checks": rows,
    }


def exact_hasse_controls(
    archive: Path,
    item163_path: Path,
    frozen: dict[str, Any],
) -> list[dict[str, Any]]:
    item163 = load_module("item172_item163", item163_path)
    extended_path = archive / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
    extended = item163.load_module("item172_extended", extended_path)

    controls = [(6, 7), (17, 19), (36, 19), (99, 107), (103, 109), (206, 107)]
    rows = []
    for m, p in controls:
        source = frozen["forced"].get((m, p))
        if source is None:
            raise AssertionError(("missing frozen control", m, p))
        precision = 3
        l0, x0, e0, bands0 = item163.coordinates_mod(
            extended, m, 4 * m + 1, p, precision
        )
        l1, x1, e1, bands1 = item163.coordinates_mod(
            extended, m, 4 * m + 2, p, precision
        )
        a_digits, a_raw, a_carries = item163.determinant_digits_by_carry(
            l1, x0, l0, x1, p, precision
        )
        b_digits, b_raw, b_carries = item163.determinant_digits_by_carry(
            l1, e0, l0, e1, p, precision
        )
        determinant_a = (l1 * x0 - l0 * x1) % (p**precision)
        determinant_b = (l1 * e0 - l0 * e1) % (p**precision)
        if a_digits != item163.p_digits(determinant_a, p, precision):
            raise AssertionError(("A carry", m, p))
        if b_digits != item163.p_digits(determinant_b, p, precision):
            raise AssertionError(("B carry", m, p))
        if a_digits[0] != 0 or b_digits[0] != 0:
            raise AssertionError(("forced determinant digit", m, p, a_digits, b_digits))
        if a_digits[1] != source["A0"]:
            raise AssertionError(("frozen A0", m, p, a_digits, source["A0"]))
        p2_source = frozen["p2"].get((m, p))
        if p2_source is not None:
            if a_digits[2] != p2_source["A_digits"][1] or b_digits[1] != p2_source["B0"]:
                raise AssertionError(("frozen higher gate", m, p, a_digits, b_digits))
        rows.append(
            {
                "m": m,
                "p": p,
                "j": source["j"],
                "s": source["s"],
                "gamma": [source["gamma0"], source["gamma1"]],
                "coordinate_digits": {
                    "L0": item163.p_digits(l0, p, precision),
                    "L1": item163.p_digits(l1, p, precision),
                    "X0": item163.p_digits(x0, p, precision),
                    "X1": item163.p_digits(x1, p, precision),
                    "E0": item163.p_digits(e0, p, precision),
                    "E1": item163.p_digits(e1, p, precision),
                },
                "A_determinant_digits": a_digits,
                "A_raw_convolutions": a_raw,
                "A_carries": a_carries,
                "B_determinant_digits": b_digits,
                "B_raw_convolutions": b_raw,
                "B_carries": b_carries,
                "Hasse_band_indices": sorted(set(bands0) | set(bands1)),
                "A0": a_digits[1],
                "A1": a_digits[2],
                "B0": b_digits[1],
                "p3_gate": a_digits[1] == a_digits[2] == b_digits[1] == 0,
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--census", type=Path, default=DEFAULT_CENSUS)
    parser.add_argument("--item163-script", type=Path, default=DEFAULT_ITEM163)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    extended_path = (
        args.archive / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
    )
    base_path = args.archive / "scripts" / "lifted_endpoint_hasse_certificate.py"
    for path in (args.census, args.item163_script, extended_path, base_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    census = json.loads(args.census.read_text(encoding="utf-8"))
    frozen = frozen_kappa_one(census)
    hasse_controls = exact_hasse_controls(args.archive, args.item163_script, frozen)
    affine = affine_search(frozen["forced"], set(frozen["p3"]))
    tail_checks = quantitative_tail_checks()

    dependence = frozen["j_dependence_controls"]
    witness = next(
        (
            row
            for row in dependence
            if row["p"] == 107 and row["s"] == 15
        ),
        None,
    )
    if witness is None or witness["gamma"] != [2, 75]:
        raise AssertionError(("missing non-scalar j-dependence witness", witness))
    witness_rows = {
        (row["m"], row["j"], row["A0"])
        for row in witness["zero_rows"] + witness["first_nonzero_rows"]
    }
    if (99, 1, 0) not in witness_rows or (206, 3, 65) not in witness_rows:
        raise AssertionError(("incorrect j-dependence witness", witness_rows))

    output = {
        "schema": "item172-kappa1-nonscalar-v1",
        "status": {
            "cell_and_scalar_formulas": "PROVED_IN_COMPANION_REPORT",
            "scalar_free_A0_A1_B0_carry_gate": "PROVED_IN_COMPANION_REPORT",
            "fixed_polynomial_and_affine_loci_are_thin": "PROVED_IN_COMPANION_REPORT",
            "positive_mass_nonscalar_family": "OPEN",
            "finite_census": "EXPERIMENTAL_EXACT_FINITE_ONLY",
        },
        "inputs": {
            "results/item164_third_layer_extended_census_m250.json": sha256(args.census),
            "scripts/item163_deeper_digits_certificate.py": sha256(args.item163_script),
            "scripts/lifted_endpoint_hasse_extended_certificate.py": sha256(extended_path),
            "scripts/lifted_endpoint_hasse_certificate.py": sha256(base_path),
        },
        "frozen_census": {
            "summary": frozen["summary"],
            "first_nonscalar_A0_zero_rows": frozen["first_nonscalar_A0_zero_rows"],
            "p3_rows": frozen["p3_rows"],
            "j_dependence_controls": frozen["j_dependence_controls"],
        },
        "exact_hasse_carry_controls": hasse_controls,
        "distinguished_nonscalar_j_dependence_witness": witness,
        "affine_p_equals_A_s_plus_B_search": affine,
        "quantitative_cell_tail": tail_checks,
        "scope": {
            "standing_prime_range": "p < 2m and p <= 4m+1 < p^2",
            "cartier_scalar_fields": "canonical residues modulo p",
            "proved_thin_class": (
                "For fixed j, any zero set contained in finitely many congruences "
                "F(j,s)=0 mod p for fixed nonzero integer polynomials has log-weight "
                "O_j(log m); finite unions in j have zero rate, and the convergent "
                "cell tail then gives zero rate for such a bandwise certificate."
            ),
            "not_covered": (
                "The actual high-degree Hasse/Bockstein cancellation depends on j, p, "
                "and s and is not proved to lie in this fixed-polynomial class."
            ),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(frozen["summary"], sort_keys=True))
    print(json.dumps({
        "hasse_controls": len(hasse_controls),
        "affine_all_A0_zero": len(affine["all_A0_zero_candidates"]),
        "affine_all_p3": len(affine["all_p3_candidates"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
