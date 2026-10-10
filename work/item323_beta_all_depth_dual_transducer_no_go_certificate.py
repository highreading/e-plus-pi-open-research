#!/usr/bin/env python3
"""Exact deterministic replay for Item 323.

The all-index theorems are proved symbolically in the report and encoded in
the proof object below.  Bounded rows are exact regression controls only;
they are never promoted into an exclusion of the original Item-316 target.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "scripts/item316_beta_intermediate_ostrowski_no_go_certificate.py": (
        "b7e25ea7248dbc774da7f3bd98a8665058117de84a2342009f8669bf5438cf6f"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "sources/item320_beta_complement_resonance_report.md": (
        "c8b2fa4194385177a2da1c26682bd155092b2848ecca9d524767eadbeb86b312"
    ),
    "scripts/item320_beta_complement_resonance_certificate.py": (
        "437b3cd05425d0495b4ce0f4e26e2c394ce9badc5c6070516c192837aea1954f"
    ),
    "results/item320_beta_complement_resonance_certificate.json": (
        "89755de7ea6ee90a4d91195d2aef7685fc9d47231a6937d3b73a5c9b8d4637e8"
    ),
    "results/item320_beta_complement_resonance_root_replay.json": (
        "89755de7ea6ee90a4d91195d2aef7685fc9d47231a6937d3b73a5c9b8d4637e8"
    ),
    "manifests/item320_beta_complement_resonance_manifest.json": (
        "3201d306c4a946a635a273f089ceb21d2a8a86da33863022dc7843a319aea6e6"
    ),
    "results/item320_beta_complement_resonance_root_audit.json": (
        "89c84a1cd2eab682a0e98f68c3310852a3216fc0a208dc855e6098011a31bfb6"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    archive_root = Path(__file__).resolve().parent.parent
    rows: list[dict[str, Any]] = []
    for relative_path, expected_hash in DEPENDENCY_HASHES.items():
        path = archive_root / relative_path
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        assert actual_hash == expected_hash, (
            relative_path,
            actual_hash,
            expected_hash,
        )
        rows.append(
            {
                "path": relative_path,
                "bytes": len(payload),
                "sha256": actual_hash,
                "verified": True,
            }
        )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "dependency_count": len(rows),
        "all_dependency_hashes_verified": True,
    }


def continuant(values: list[int]) -> int:
    before_previous = 0
    previous = 1
    for value in values:
        before_previous, previous = previous, value * previous + before_previous
    return previous


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def centered(value: int, odd_modulus: int) -> int:
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 323 coordinates use n>=5")
    m = n - 2
    word = [None, 7] + [4 * index + 2 for index in range(2, m + 1)]
    word.append(4 * n - 2)
    assert len(word) == m + 2

    q_prefix = [0] * (m + 2)
    p_prefix = [0] * (m + 2)
    q_before, q_previous = 0, 1
    p_before, p_previous = 1, 0
    q_prefix[0] = 1
    p_prefix[0] = 0
    for index in range(1, m + 2):
        q_before, q_previous = q_previous, word[index] * q_previous + q_before
        p_before, p_previous = p_previous, word[index] * p_previous + p_before
        q_prefix[index] = q_previous
        p_prefix[index] = p_previous

    q_values = beta_q(n)
    assert q_prefix == q_values[1 : n + 1]
    for index in range(1, m + 2):
        assert (
            q_prefix[index] * p_prefix[index - 1]
            - p_prefix[index] * q_prefix[index - 1]
            == (-1) ** index
        )

    return {
        "n": n,
        "m": m,
        "word": word,
        "Q": q_prefix,
        "P": p_prefix,
        "A": 4 * n - 2,
        "a": q_prefix[m],
        "b": q_prefix[m + 1],
        "c": q_prefix[m - 1],
    }


def validate_digits(digits: list[int], data: dict[str, Any]) -> None:
    m = data["m"]
    assert len(digits) == m + 2
    assert digits[0] == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, m + 1):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0
    assert digits[m + 1] == 0


def ostrowski_digits(value: int, data: dict[str, Any]) -> list[int]:
    if not 0 <= value < data["a"]:
        raise ValueError("Ostrowski input must lie in [0,a)")
    digits = [0] * (data["m"] + 2)
    remainder = value
    for index in range(data["m"], 0, -1):
        digits[index], remainder = divmod(remainder, data["Q"][index - 1])
    assert remainder == 0
    validate_digits(digits, data)
    return digits


def prefix_objects(digits: list[int], data: dict[str, Any]) -> dict[str, Any]:
    validate_digits(digits, data)
    r_prefix: list[int] = []
    z_prefix: list[int] = []
    errors: list[int] = []
    for length in range(data["m"] + 2):
        r_value = sum(
            digits[index] * data["Q"][index - 1]
            for index in range(1, min(length, data["m"] + 1) + 1)
        )
        z_value = sum(
            digits[index] * data["P"][index - 1]
            for index in range(1, min(length, data["m"] + 1) + 1)
        )
        r_prefix.append(r_value)
        z_prefix.append(z_value)
        errors.append(
            r_value * data["P"][length] - z_value * data["Q"][length]
        )

    # delta_(m+1)=0 means the represented value is unchanged at m+1.
    assert r_prefix[data["m"]] == r_prefix[data["m"] + 1]
    assert errors[0] == 0
    assert errors[1] == digits[1]
    for index in range(1, data["m"] + 1):
        assert errors[index + 1] == (
            data["word"][index + 1] * errors[index]
            + errors[index - 1]
            + (-1) ** index * digits[index + 1]
        )
    for length in range(data["m"] + 1):
        assert 0 <= r_prefix[length] < data["Q"][length]
    return {"R": r_prefix, "Z": z_prefix, "E": errors}


def suffix_objects(
    value: int, digits: list[int], data: dict[str, Any]
) -> dict[str, Any]:
    validate_digits(digits, data)
    m = data["m"]
    h_values = [0] * (m + 2)
    n_values = [0] * (m + 2)
    h_values[m] = 1
    h_values[m + 1] = 0
    n_values[m] = 0
    n_values[m + 1] = 0
    for index in range(m, 0, -1):
        h_values[index - 1] = (
            data["word"][index + 1] * h_values[index] + h_values[index + 1]
        )
        n_values[index - 1] = (
            data["word"][index + 1] * n_values[index]
            + n_values[index + 1]
            + digits[index + 1]
        )

    assert h_values[m] == 1
    assert h_values[m - 1] == data["A"]
    l_values = [value * h_values[index] - data["b"] * n_values[index]
                for index in range(m + 2)]
    assert l_values[m] == value
    assert l_values[m + 1] == 0
    for index in range(m, 0, -1):
        assert l_values[index - 1] == (
            data["word"][index + 1] * l_values[index]
            + l_values[index + 1]
            - data["b"] * digits[index + 1]
        )
    return {"H": h_values, "N": n_values, "L": l_values}


def split_audit(
    value: int, digits: list[int], data: dict[str, Any]
) -> dict[str, Any]:
    prefix = prefix_objects(digits, data)
    suffix = suffix_objects(value, digits, data)
    m = data["m"]
    a_values: list[int] = []

    for j in range(m + 1):
        assert data["b"] == (
            suffix["H"][j] * data["Q"][j + 1]
            + suffix["H"][j + 1] * data["Q"][j]
        )
        n_expanded = 0
        alternating = 0
        for h in range(j + 1, m):
            c_value = continuant(data["word"][j + 2 : h + 1])
            assert (
                data["Q"][h] * suffix["H"][j] - data["b"] * c_value
                == (-1) ** (h - j) * data["Q"][j] * suffix["H"][h]
            )
            n_expanded += digits[h + 1] * c_value
            alternating += (
                (-1) ** (h - j) * digits[h + 1] * suffix["H"][h]
            )
        assert suffix["N"][j] == n_expanded
        assert -suffix["H"][j] <= alternating <= suffix["H"][j + 1]
        assert suffix["L"][j] == (
            suffix["H"][j] * prefix["R"][j + 1]
            + data["Q"][j] * alternating
        )
        assert -data["b"] < suffix["L"][j] < data["b"]
        a_values.append(alternating)

    return {
        "H_digest": digest(suffix["H"]),
        "N_digest": digest(suffix["N"]),
        "L_digest": digest(suffix["L"]),
        "A_digest": digest(a_values),
        "unit_strip": True,
        "cross_determinants": True,
    }


def transducer_controls() -> dict[str, Any]:
    declarations = {
        5: [0, 1, 7, 70, 500, 1000],
        6: [0, 6, 7, 100, 1000, 9044, 18088],
        7: [1, 71, 1001, 18089, 199479, 398958],
        9: [7, 1001, 18089, 10391023, 156064824, 312129648],
        13: [1, 71, 18089, 10391023, 781379079653016],
    }
    rows: list[dict[str, Any]] = []
    for n, values in declarations.items():
        data = coordinates(n)
        for value in values:
            digits = ostrowski_digits(value, data)
            row = split_audit(value, digits, data)
            rows.append({"n": n, "R": value, "digits": digits[1:-1], **row})

    # Exhaustive small controls: this is regression only, not a promotion.
    exhaustive: list[dict[str, Any]] = []
    for n in (5, 6):
        data = coordinates(n)
        aggregate = hashlib.sha256()
        for value in range(data["a"]):
            digits = ostrowski_digits(value, data)
            suffix = suffix_objects(value, digits, data)
            assert all(
                -data["b"] < suffix["L"][j] < data["b"]
                for j in range(data["m"] + 1)
            )
            aggregate.update(
                json.dumps(suffix["L"][:-1], separators=(",", ":")).encode()
            )
        exhaustive.append(
            {
                "n": n,
                "R_count": data["a"],
                "aggregate_digest": aggregate.hexdigest(),
                "label": "EXACT FINITE ONLY",
            }
        )
    return {
        "declared_rows": rows,
        "declared_row_digest": digest(rows),
        "exhaustive_small_controls": exhaustive,
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_all_index_unit_strip": False,
        "half_bound_scan": False,
    }


def formal_sign_controls() -> dict[str, Any]:
    """Audit the sign normalization with a formal top boundary.

    The driven state is deliberately rational and is not claimed to equal
    the actual prefix determinant.  It checks only the recurrence/sign map.
    """

    declarations = [(6, 100), (7, 18089), (9, 10391023), (12, 123456789)]
    rows: list[dict[str, Any]] = []
    for n, value in declarations:
        data = coordinates(n)
        value %= data["a"]
        digits = ostrowski_digits(value, data)
        suffix = suffix_objects(value, digits, data)
        for epsilon in (-1, 1):
            sigma = epsilon * ((-1) ** n)
            x_values = [
                Fraction(data["a"] * data["Q"][j], data["b"])
                for j in range(data["m"] + 2)
            ]
            z_values = [Fraction(0) for _ in range(data["m"] + 2)]
            z_values[data["m"] + 1] = Fraction(0)
            z_values[data["m"]] = Fraction(-epsilon * value, data["b"])
            for j in range(data["m"], 0, -1):
                z_values[j - 1] = (
                    z_values[j + 1]
                    - data["word"][j + 1] * z_values[j]
                    - sigma * ((-1) ** j) * digits[j + 1]
                )
            for j in range(data["m"] + 2):
                s_value = Fraction(suffix["L"][j], data["b"])
                assert s_value == -sigma * ((-1) ** j) * z_values[j]
            rows.append(
                {
                    "n": n,
                    "R": value,
                    "epsilon": epsilon,
                    "sigma": sigma,
                    "z_digest": digest(
                        [(z.numerator, z.denominator) for z in z_values]
                    ),
                    "formal_recurrence_sign_match": True,
                    "actual_target_state": False,
                }
            )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY; FORMAL SIGN CONTROL",
        "arbitrary_state_promoted_to_actual": False,
    }


def division_free_controls() -> dict[str, Any]:
    q_values = beta_q(90)
    rows: list[dict[str, Any]] = []
    minimum = None
    minimum_at = None
    for n in range(6, 91):
        a_coefficient = 4 * n - 2
        for j in range(3, n - 1):
            difference = (
                (4 * (n - j) - 5) * q_values[j]
                - a_coefficient * (4 * j + 3)
            )
            assert difference > 0
            if minimum is None or difference < minimum:
                minimum = difference
                minimum_at = (n, j)
        if n in (6, 7, 10, 20, 40, 90):
            rows.append(
                {
                    "n": n,
                    "minimum_difference": min(
                        (4 * (n - j) - 5) * q_values[j]
                        - a_coefficient * (4 * j + 3)
                        for j in range(3, n - 1)
                    ),
                }
            )

    assert minimum == 167 and minimum_at == (6, 3)
    assert 7 * q_values[3] - 22 * 15 == 167
    assert 3 * q_values[4] - 22 * 19 == 2585
    for j in range(4, 90):
        assert (
            (4 * j + 2) * (4 * j + 6) * (4 * j + 3)
            > (4 * j + 10) * (4 * j + 7)
        )
        assert q_values[j + 1] > (4 * j + 2) * q_values[j]
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "global_minimum_control": {"value": minimum, "at": minimum_at},
        "symbolic_increment": "4(q_j-4j-3)>0",
        "symbolic_base_j3": 167,
        "symbolic_base_j4": 2585,
        "label": "EXACT FINITE ONLY CONTROLS FOR A SYMBOLIC INDUCTION",
        "finite_promotion": False,
    }


def bottom_symbolic_audit() -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    # sigma=+1, delta1=0 or 1 from k1 in {0,1}.
    for delta1 in (0, 1):
        for delta2 in range(0, 11):
            markov = not (delta2 == 10 and delta1 != 0)
            e2 = 10 * delta1 - delta2
            k2 = e2
            if markov and k2 >= 0:
                u1 = -e2 - delta2
                assert abs(u1) != 7
                cases.append(
                    {
                        "sigma": 1,
                        "delta1": delta1,
                        "delta2": delta2,
                        "k2": k2,
                        "U1": u1,
                    }
                )
    # sigma=-1 forces delta1=0; every nonnegative k2 is delta2.
    for delta2 in range(0, 11):
        delta1 = 0
        e2 = -delta2
        k2 = delta2
        u1 = -e2 - delta2
        assert u1 == 0 and abs(u1) != 7
        cases.append(
            {
                "sigma": -1,
                "delta1": delta1,
                "delta2": delta2,
                "k2": k2,
                "U1": u1,
            }
        )
    assert {case["U1"] for case in cases} == {0, -10}
    return {
        "cases": cases,
        "case_digest": digest(cases),
        "j1_U0": 0,
        "j2_possible_U1": [-10, 0],
        "earlier_targets": {"j1": [-1, 1], "j2": [-7, 7]},
        "symbolic_fixed_cell_argument": True,
        "bounded_n_scan": False,
    }


def base_audit() -> dict[str, Any]:
    q_values = beta_q(5)
    n = 5
    a_value = q_values[n - 1]
    b_value = q_values[n]
    signed = centered(a_value * a_value, b_value)
    kappa = (a_value * a_value - signed) // b_value
    remainder = abs(signed)
    assert (a_value, b_value, kappa, remainder) == (1001, 18089, 55, 7106)
    assert 2 * remainder - a_value == 13211 > 0
    return {
        "n": n,
        "a": a_value,
        "b": b_value,
        "kappa": kappa,
        "R": remainder,
        "two_R_minus_a": 2 * remainder - a_value,
        "status": "EXACT BASE; NO ITEM316 TARGET",
    }


def proof_object() -> dict[str, Any]:
    return {
        "suffix_transducer": (
            "H_(j-1)=w_(j+1)H_j+H_(j+1), "
            "N_(j-1)=w_(j+1)N_j+N_(j+1)+delta_(j+1), "
            "s_j=(R H_j-b N_j)/b"
        ),
        "continuant_split": (
            "b=H_j Q_(j+1)+H_(j+1)Q_j and "
            "Q_h H_j-b C_(j,h)=(-1)^(h-j)Q_j H_h"
        ),
        "alternating_tail": (
            "A_j=sum_h (-1)^(h-j)delta_(h+1)H_h; "
            "-H_j<=A_j<=H_(j+1) by exact telescoping"
        ),
        "unit_strip": (
            "-b<R H_j-b N_j<b for every canonical word and every depth"
        ),
        "actual_target_bridge": (
            "only under E_(m+1)=sigma Q_m and E_m=sigma kappa, "
            "s_j=-sigma(-1)^j(sigma E_j-aQ_j/b), hence |z_j|<1"
        ),
        "division_free_interior": (
            "(A-w_j-1)Q_(j-1)>A(w_j+1) for n>=6, 3<=j<=n-2"
        ),
        "bottom_cells": (
            "U_0=0; at j=2 the nearest-center and Markov conditions force "
            "U_1 in {0,-10}, never +/-7"
        ),
        "scope": (
            "closes every literal prefix/inherited-target descent depth; "
            "does not exclude the original all-digit target or redigitized/"
            "nonlinear descendants"
        ),
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item323-beta-all-depth-dual-transducer-no-go-v1",
        "item": 323,
        "date_beijing": "2026-08-31",
        "status": "PROVED_SCOPED_ALL_DEPTH_LITERAL_INHERITANCE_NO_GO",
        "dependency_pins": dependency_audit(),
        "proof": proof_object(),
        "exact_replay_controls": {
            "continuant_split_and_unit_strip": transducer_controls(),
            "formal_sign_orientation": formal_sign_controls(),
            "division_free_inequality": division_free_controls(),
            "bottom_symbolic_cells": bottom_symbolic_audit(),
            "structural_base": base_audit(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "half_bound_scan": False,
            "actual_counterexample_search": False,
        },
        "strict_labels": {
            "all_depth_dual_transducer_unit_strip": "PROVED",
            "actual_target_nearest_center_confinement": "PROVED CONDITIONAL",
            "literal_inherited_target_all_depth": "PROVED SCOPED NO-GO",
            "original_all_digit_exclusion": "OPEN",
            "centered_half_bound": "OPEN",
            "redigitized_or_nonlinear_invariant": "OPEN",
            "bounded_controls": "EXACT FINITE ONLY",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "item320": "depth restriction removed only for literal inheritance",
            "item282": "no proper-target return or product content booked",
            "proper_target": "not constructed or bounded",
            "arbitrary_digit_state_promoted_to_actual": False,
            "canonical_files_modified": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "item": 323,
                "status": certificate["status"],
                "all_depth_unit_strip": "PROVED",
                "literal_inheritance_all_depth": "PROVED_SCOPED_NO_GO",
                "original_all_digit_exclusion": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
