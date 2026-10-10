#!/usr/bin/env python3
"""Finite exact nonzero scan for slope-10 ray determinants.

For each admissible odd 3 <= b <= max_b and both parities, evaluate the
closed two-state determinant at m=-b/10 in F_1000000007.  Since every
recurrence denominator has absolute value below 3*max_b and the default
max_b is 2001, a nonzero modular value rigorously proves that the
corresponding rational determinant is nonzero.  This remains a finite scan,
not a uniform theorem in b.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


MODULUS = 1_000_000_007


def multiply_by_w(coefficients: list[int]) -> list[int]:
    output = [0] * (len(coefficients) + 3)
    for index, value in enumerate(coefficients):
        output[index] = (output[index] + value) % MODULUS
        output[index + 1] = (output[index + 1] - value) % MODULUS
        output[index + 2] = (output[index + 2] + value) % MODULUS
        output[index + 3] = (output[index + 3] - value) % MODULUS
    return output


def class_sums(
    intercept: int,
    weight: list[int],
    inverse: list[int],
    inverse_ten: int,
) -> dict[int, int]:
    singular_index = 3 * intercept - 5
    formal_m = -intercept * inverse_ten % MODULUS
    output: dict[int, int] = {}
    for residue_class in {(intercept - 1) % 4, 1, 3}:
        residue = 1
        total = weight[residue_class] if residue_class < len(weight) else 0
        index = residue_class
        while index + 4 < len(weight):
            first = index - singular_index
            inverse_first = inverse[first] if first > 0 else -inverse[-first] % MODULUS
            residue = (
                residue
                * (-(4 * formal_m + intercept - 1 - index))
                * inverse_first
                % MODULUS
            )
            index += 4
            total = (total + weight[index] * residue) % MODULUS
        output[residue_class] = total
    return output


def run_scan(max_b: int) -> dict[str, object]:
    assert 3 <= max_b < MODULUS // 3
    inverse = [0] * (3 * max_b + 10)
    inverse[1] = 1
    for value in range(2, len(inverse)):
        inverse[value] = (
            MODULUS - (MODULUS // value) * inverse[MODULUS % value] % MODULUS
        )
    inverse_ten = pow(10, MODULUS - 2, MODULUS)

    weight = [1]
    stream_hash = hashlib.sha256()
    intercept_count = 0
    zero_rows: list[dict[str, object]] = []
    for exponent in range(1, max_b):
        weight = multiply_by_w(weight)
        if exponent % 2 == 0:
            continue
        intercept = exponent + 2
        if intercept > max_b:
            break
        if intercept % 5 == 0:
            continue
        # weight=W^(b-2); one further multiplication gives W^(b-1).
        lower_weight = weight
        upper_weight = multiply_by_w(weight)
        lower_sums = class_sums(intercept, lower_weight, inverse, inverse_ten)
        upper_sums = class_sums(intercept, upper_weight, inverse, inverse_ten)
        anchor_class = (intercept - 1) % 4
        determinants = []
        for other_class in (1, 3):  # even-m row, then odd-m row
            determinant = (
                upper_sums[anchor_class] * lower_sums[other_class]
                - upper_sums[other_class] * lower_sums[anchor_class]
            ) % MODULUS
            determinants.append(determinant)
        intercept_count += 1
        stream_hash.update(
            f"{intercept}:{determinants[0]}:{determinants[1]}\n".encode()
        )
        for parity, value in enumerate(determinants):
            if value == 0:
                zero_rows.append(
                    {
                        "intercept": intercept,
                        "parity": "even" if parity == 0 else "odd",
                    }
                )

    return {
        "modulus": MODULUS,
        "max_b": max_b,
        "admissible_odd_intercepts_checked": intercept_count,
        "parity_rows_checked": 2 * intercept_count,
        "determinant_zero_residues": zero_rows,
        "stream_sha256": stream_hash.hexdigest(),
        "conclusion": (
            "Every checked rational determinant is nonzero because its "
            "modular image is nonzero."
        ),
        "warning": "Finite exact scan; not a uniform theorem in the intercept b.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=2001)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "moving_ray_determinant_nonzero_scan_b2001.json",
    )
    args = parser.parse_args()
    payload = run_scan(args.max_b)
    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
