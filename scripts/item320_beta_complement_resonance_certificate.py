#!/usr/bin/env python3
"""Exact deterministic replay for Item 320.

The universal sub-half-linear theorem is proved by the symbolic estimates
recorded in the report and proof object.  Declared rows below are exact
algebra controls only; they are not a half-bound scan or finite promotion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


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
        raise ValueError("Item 320 coordinates use n>=5")
    m = n - 2
    word = [7] + [4 * index + 2 for index in range(2, m + 2)]

    q_prefix = [1]
    before_previous, previous = 0, 1
    for value in word:
        before_previous, previous = previous, value * previous + before_previous
        q_prefix.append(previous)

    p_prefix = [0]
    before_previous, previous = 1, 0
    for value in word:
        before_previous, previous = previous, value * previous + before_previous
        p_prefix.append(previous)

    q_values = beta_q(n)
    assert q_prefix == q_values[1 : n + 1]
    assert q_prefix[m] == q_values[n - 1]
    assert q_prefix[m + 1] == q_values[n]

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
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
        "d": q_values[n - 3],
        "e": q_values[n - 4],
    }


def validate_digits(digits: list[int], data: dict[str, Any]) -> None:
    assert len(digits) == data["m"]
    assert 0 <= digits[0] <= 6
    for index in range(1, data["m"]):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0


def ostrowski_digits(value: int, data: dict[str, Any]) -> list[int]:
    if not 0 <= value < data["a"]:
        raise ValueError("Ostrowski input must lie in [0,a)")
    digits = [0] * data["m"]
    remainder = value
    for index in range(data["m"] - 1, -1, -1):
        digits[index], remainder = divmod(remainder, data["Q"][index])
    assert remainder == 0
    validate_digits(digits, data)
    return digits


def prefix_objects(digits: list[int], data: dict[str, Any]) -> dict[str, Any]:
    validate_digits(digits, data)
    extended_digits = digits + [0]
    errors: list[int] = []
    represented: list[int] = []
    coefficients: list[int] = []

    for length in range(data["m"] + 2):
        use = min(length, data["m"] + 1)
        r_value = sum(
            extended_digits[index] * data["Q"][index] for index in range(use)
        )
        z_value = sum(
            extended_digits[index] * data["P"][index] for index in range(use)
        )
        represented.append(r_value)
        coefficients.append(z_value)
        errors.append(
            r_value * data["P"][length] - z_value * data["Q"][length]
        )

    assert errors[0] == 0
    assert errors[1] == digits[0]
    for index in range(1, data["m"] + 1):
        assert errors[index + 1] == (
            data["word"][index] * errors[index]
            + errors[index - 1]
            + (-1) ** index * extended_digits[index]
        )

    truncated_u: list[int | None] = [None]
    for length in range(1, data["m"] + 1):
        tails = [
            continuant(data["word"][index + 1 : length])
            for index in range(length - 1)
        ]
        u_value = sum(
            digits[index] * (-1) ** (length + 1 + index) * tails[index]
            for index in range(length - 1)
        )
        assert u_value == (-1) ** (length + 1) * errors[length] - digits[
            length - 1
        ]
        truncated_u.append(u_value)

    return {
        "R_prefix": represented,
        "Z_prefix": coefficients,
        "E_prefix": errors,
        "U_truncated": truncated_u,
    }


def exact_prefix_controls() -> dict[str, Any]:
    declarations = {
        5: [1, 36, 497],
        6: [7, 1001, 9044],
        7: [71, 18089, 199479],
        8: [1001, 398959, 5195511],
        9: [18089, 10391023, 156064824],
    }
    rows: list[dict[str, Any]] = []
    for n, values in declarations.items():
        data = coordinates(n)
        for value in values:
            digits = ostrowski_digits(value, data)
            objects = prefix_objects(digits, data)
            for length in range(1, data["m"] + 1):
                prefix_digits = digits[: length - 1]
                if len(prefix_digits) >= 2:
                    for index in range(1, len(prefix_digits)):
                        assert 0 <= prefix_digits[index] <= data["word"][index]
                        if prefix_digits[index] == data["word"][index]:
                            assert prefix_digits[index - 1] == 0
                assert objects["R_prefix"][length - 1] < data["Q"][length - 1]
            rows.append(
                {
                    "n": n,
                    "R": value,
                    "digits": digits,
                    "E_digest": digest(objects["E_prefix"]),
                    "U_digest": digest(objects["U_truncated"]),
                    "recurrence": True,
                    "truncated_u_boundary_digit_retained": True,
                }
            )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_target_boundary": False,
        "half_bound_scan": False,
    }


def casoratian_controls() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    q_values = beta_q(16)
    for n in (6, 8, 10, 12, 14, 16):
        data = coordinates(n)
        for depth in range(0, min(5, data["m"] - 1)):
            index = data["m"] - depth
            earlier = n - depth - 2
            casoratian = (
                q_values[earlier] * q_values[n]
                - q_values[earlier + 1] * q_values[n - 1]
            )
            gamma = Fraction(casoratian, data["b"])
            direct = Fraction(
                data["Q"][index - 1] * data["b"]
                - data["a"] * data["Q"][index],
                data["b"],
            )
            assert gamma == direct
            lower = Fraction(
                (4 * depth + 3) * data["Q"][index - 1], 4 * n - 2
            )
            upper = Fraction(
                (4 * depth + 5) * data["Q"][index - 1], 4 * n - 1
            )
            assert lower < gamma < upper
            rows.append(
                {
                    "n": n,
                    "depth": depth,
                    "casoratian": casoratian,
                    "gamma_numerator": gamma.numerator,
                    "gamma_denominator": gamma.denominator,
                    "sharp_bounds": True,
                }
            )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_all_depth_bounds": False,
    }


def canonical_complement_controls() -> dict[str, Any]:
    q_values = beta_q(14)
    rows: list[dict[str, Any]] = []
    for n in range(5, 15):
        a_value = q_values[n - 1]
        b_value = q_values[n]
        c_value = q_values[n - 2]
        d_value = q_values[n - 3]
        signed = centered(a_value * a_value, b_value)
        kappa = (a_value * a_value - signed) // b_value
        complement = c_value - kappa
        assert 2 * d_value < complement < 4 * d_value
        leading = complement // d_value
        assert leading == (2 if n <= 8 else 3)
        rows.append(
            {
                "n": n,
                "t": complement,
                "d": d_value,
                "leading_digit": leading,
                "interior_markov_digit": True,
            }
        )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_canonical_complement_theorem": False,
    }


def factorial_threshold_controls() -> dict[str, Any]:
    declarations = [
        (0, 1, 20),
        (1, 4, 80),
        (2, 5, 300),
    ]
    rows: list[dict[str, Any]] = []
    for numerator, denominator, n in declarations:
        depth = (numerator * n) // denominator
        s_value = n - depth - 2
        factorial_lower = (1 << (s_value - 1)) * math.factorial(s_value)
        power_bound = (4 * n) ** (depth + 2)
        assert factorial_lower > power_bound
        rows.append(
            {
                "lambda": f"{numerator}/{denominator}",
                "n": n,
                "L": depth,
                "s": s_value,
                "threshold_inequality": True,
            }
        )
    return {
        "rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_define_N_lambda": False,
        "universal_existence_proof": (
            "log(2^(s-1)s!)-(L+2)log(4n)="
            "(1-2lambda)n log n+O_lambda(n)"
        ),
    }


def small_index_audit() -> dict[str, Any]:
    q_values = beta_q(5)
    expected = {
        2: (1, 7, 0, 1),
        3: (7, 71, 1, -22),
        4: (71, 1001, 5, 36),
        5: (1001, 18089, 55, 7106),
    }
    rows: list[dict[str, int]] = []
    for n, (a_value, b_value, kappa, signed) in expected.items():
        assert q_values[n - 1] == a_value
        assert q_values[n] == b_value
        assert centered(a_value * a_value, b_value) == signed
        assert (a_value * a_value - signed) // b_value == kappa
        assert 2 * abs(signed) >= a_value
        rows.append(
            {
                "n": n,
                "a": a_value,
                "b": b_value,
                "kappa": kappa,
                "signed_remainder": signed,
            }
        )
    return {"rows": rows, "status": "EXACT BASES; NO HALF-BOUND FAILURE"}


def proof_object() -> dict[str, Any]:
    return {
        "target_boundary": (
            "only an exact Item316 target gives E_(m+1)=sigma Q_m and "
            "E_m=sigma kappa; arbitrary digit states do not"
        ),
        "prefix_recurrence": (
            "E_(j+1)=w_(j+1)E_j+E_(j-1)+(-1)^j delta_(j+1)"
        ),
        "item295_reconciliation": (
            "g_m=Q_(m-1)-sigma E_m=c-kappa=t_n and "
            "sigma E_(m-1)=a-Akappa=h"
        ),
        "canonical_complement": (
            "2d<t_n<4d; its previous-scale leading digit is 2 for n=5..8 "
            "and 3 for every n>=9"
        ),
        "casoratian_center": (
            "gamma_(m-r)=C_(r+1)(n-r-2)/q_n and its relative bounds are "
            "(4r+3)/(4n-2) and (4r+5)/(4n-1)"
        ),
        "uniform_deviation": (
            "|z_(m-r)|<(4n)^(r+1); factorial q-growth dominates uniformly "
            "for r<=floor(lambda n), every rational lambda<1/2; one explicit "
            "threshold is ceil(max(8,exp((4log(4)+4)/(1-2lambda))))"
        ),
        "exact_truncation_defect": (
            "G_(m-r)=g_(m-r)+(-1)^(r+1)epsilon delta_(m-r)>0 and "
            "|U_truncated|=Q_(m-r-1)-G_(m-r)"
        ),
        "scope": (
            "excludes only inherited exact-target closure for literal prefix/"
            "complement descent of limsup depth/n<1/2"
        ),
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item320-beta-complement-resonance-certificate-v1",
        "item": 320,
        "date_beijing": "2026-08-31",
        "status": "PROVED_SCOPED_SUB_HALF_LINEAR_COMPLEMENT_DESCENT_NO_GO",
        "proof": proof_object(),
        "exact_replay_controls": {
            "prefix_recurrence_and_boundary_digit": exact_prefix_controls(),
            "casoratian_centers": casoratian_controls(),
            "canonical_complement": canonical_complement_controls(),
            "factorial_thresholds": factorial_threshold_controls(),
            "small_indices": small_index_audit(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "half_bound_scan": False,
            "actual_counterexample_search": False,
        },
        "strict_labels": {
            "all_prefix_recurrence": "PROVED",
            "canonical_top_complement": "PROVED",
            "casoratian_center_and_bounds": "PROVED",
            "sub_half_linear_literal_descent": "PROVED SCOPED NO-GO",
            "lambda_at_least_one_half_or_full_depth": "OPEN",
            "exact_all_digit_exclusion": "OPEN",
            "centered_half_bound": "OPEN",
            "bounded_controls": "EXACT FINITE ONLY",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "item295_one_step": "reconciled exactly; not claimed as new",
            "item282_resonance": (
                "same Casoratian family in reverse real-center orientation; "
                "no de-overlapped overlap or capacity consequence"
            ),
            "proper_target": "not constructed or bounded",
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
                "item": 320,
                "status": certificate["status"],
                "complement_resonance": "PROVED",
                "literal_sub_half_linear_descent": "PROVED_SCOPED_NO_GO",
                "centered_half_bound": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

