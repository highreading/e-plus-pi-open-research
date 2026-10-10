#!/usr/bin/env python3
"""Exact Gaussian numerator and moving-prime residue certificate for Item 304.

No actual-row prime scan is performed.  The checker replays the characteristic-
zero Gaussian recurrence and records the symbolic finite-field derivation.
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
DEPENDENCIES = {
    "item297_j1_structural_ray_boundary_certificate.py": (
        "6baec559198b0055096717f3e2fb7551707a17b64f520e499e585c73a4441cb5"
    ),
    "item297_j1_structural_ray_boundary_certificate.json": (
        "aa84dde588a119c67b868266ca536699b3675d2e53cb62ad8f1df66705ca7e6b"
    ),
    "item301_j1_boundary_scalar_reduction_certificate.py": (
        "a333101b2112abe4dc59c1c7d2f2237e41f7a6546606eb7283d55854140a56e4"
    ),
    "item301_j1_boundary_scalar_reduction_certificate.json": (
        "f25813facfe8befb751fdbcd1c5f521c23379162bd44244356c8b2568d9fc784"
    ),
}


def resolve(name: str) -> Path:
    for path in (HERE / name, HERE.parent / "scripts" / name, HERE.parent / "results" / name):
        if path.is_file():
            return path
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for dependency_name, expected_hash in DEPENDENCIES.items():
    observed = sha256(resolve(dependency_name))
    if observed != expected_hash:
        raise RuntimeError(("dependency hash", dependency_name, observed, expected_hash))


item297 = json.loads(
    resolve("item297_j1_structural_ray_boundary_certificate.json").read_text(
        encoding="utf-8"
    )
)
item301 = json.loads(
    resolve("item301_j1_boundary_scalar_reduction_certificate.json").read_text(
        encoding="utf-8"
    )
)
if item297.get("schema") != "item297-j1-structural-ray-boundary-v2":
    raise AssertionError("Item297 v2 not admitted")
if item301.get("schema") != "item301-j1-boundary-scalar-reduction-v1":
    raise AssertionError("Item301 not admitted")


GaussianInt = tuple[int, int]
GaussianRat = tuple[Fraction, Fraction]


def gadd(left, right):
    return left[0] + right[0], left[1] + right[1]


def gsub(left, right):
    return left[0] - right[0], left[1] - right[1]


def gmul(left, right):
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gscale(value, scalar):
    return value[0] * scalar, value[1] * scalar


def gpow(value, exponent: int):
    answer = (type(value[0])(1), type(value[0])(0))
    factor = value
    while exponent:
        if exponent & 1:
            answer = gmul(answer, factor)
        exponent >>= 1
        if exponent:
            factor = gmul(factor, factor)
    return answer


def gaussian_numerator(n_value: int) -> GaussianInt:
    total: GaussianInt = (0, 0)
    one_plus_i: GaussianInt = (1, 1)
    for index in range(1, n_value + 1):
        total = gadd(
            total,
            gscale(gpow(one_plus_i, index), math.comb(2 * index, index)),
        )
    return gadd((2, 0), gmul((2, 1), total))


def j_direct(n_value: int) -> GaussianRat:
    total: GaussianRat = (Fraction(0), Fraction(0))
    minus_i: GaussianRat = (Fraction(0), Fraction(-1))
    for index in range(n_value + 1):
        total = gadd(
            total,
            gscale(
                gpow(minus_i, index),
                Fraction(math.comb(n_value, index), n_value + index + 1),
            ),
        )
    return total


def j_from_numerator(n_value: int, numerator: GaussianInt) -> GaussianRat:
    scalar = Fraction(math.factorial(n_value) ** 2, 2 * math.factorial(2 * n_value + 1))
    phase = gpow((0, -1), n_value)
    return gscale(gmul(phase, numerator), scalar)


def recurrence_replay(n_max: int = 160) -> dict[str, Any]:
    numerators = [gaussian_numerator(index) for index in range(n_max + 1)]
    if numerators[0] != (2, 0) or numerators[1] != (4, 6):
        raise AssertionError(("initial numerators", numerators[:2]))
    for index in range(1, n_max):
        left = gscale(gsub(numerators[index + 1], numerators[index]), index + 1)
        right = gscale(
            gmul((1, 1), gsub(numerators[index], numerators[index - 1])),
            2 * (2 * index + 1),
        )
        if left != right:
            raise AssertionError(("integer numerator recurrence", index, left, right))
    rows = []
    for index, numerator in enumerate(numerators):
        direct = j_direct(index)
        normalized = j_from_numerator(index, numerator)
        if direct != normalized:
            raise AssertionError(("J normalization", index, direct, normalized))
        rows.append([index, numerator[0], numerator[1]])
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "EXACT CHARACTERISTIC-ZERO REPLAY; NO PRIME SCAN",
        "n_range": [0, n_max],
        "rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def boundary_coefficient_drop_audit() -> dict[str, Any]:
    drops = item297["reduced_actual_ray_relations"][
        "normalized_coefficient_drops_by_s_then_p"
    ]
    answer = {}
    for s_text, rows in drops.items():
        s_value = int(s_text)
        boundary_index = s_value // 2
        answer[str(s_value)] = sorted(
            int(prime) for prime, indices in rows.items() if boundary_index in indices
        )
    expected = {"2": [19], "4": [79], "6": [787067]}
    if answer != expected:
        raise AssertionError(("boundary coefficient drops", answer))
    return {
        "classification": "PROVED BY COMPLETE ITEM297 DROP ATLAS",
        "drops_by_s": answer,
    }


def symbolic_arithmetic_theorem() -> dict[str, Any]:
    return {
        "classification": "PROVED ALL-H MOVING-PRIME GAUSSIAN RESIDUE",
        "integer_numerator": {
            "definition": (
                "N_n=2+(2+i)sum_(k=1)^n C(2k,k)(1+i)^k=A_n+iT_n"
            ),
            "J_normalization": "J_n=(-i)^n(n!)^2 N_n/[2(2n+1)!]",
            "recurrence": (
                "N_0=2, N_1=4+6i; (n+1)(N_(n+1)-N_n)="
                "2(2n+1)(1+i)(N_n-N_(n-1))"
            ),
            "integrality": "A_n,T_n are integers for every n",
        },
        "specialization": {
            "parameters": "n=2H, m=2H+1=(p-1)/2, p=4H+3",
            "factorial_unit": "((2H)!)^2/(4H+1)!=4 mod p",
            "Y_bridge": "2Y_H=-w_H+3(-1)^H T_(2H) mod p",
            "truncated_binomial": (
                "S_(m-1)=sum_(k=1)^(m-1)C(2k,k)(1+i)^k="
                "(-3-4i)^m-(-4-4i)^m-1 mod p"
            ),
            "Frobenius": (
                "(-3-4i)^m=(-3+4i)/5; (-4-4i)^m=-e_H(1+i) "
                "for even H and d_H(1-i) for odd H"
            ),
            "T_values": "T_(2H)=3e_H for even H and T_(2H)=d_H for odd H",
            "Y_values": "Y_H=4e_H for even H and Y_H=-2d_H for odd H",
            "uniform_boundary": (
                "B_H=-24(1+w_H) mod p, where w_H=e_H for even H and d_H for odd H"
            ),
        },
        "nonvanishing": {
            "Euler": "w_H^2=-1/2 for even H and w_H^2=1/2 for odd H",
            "conclusion": "B_H is nonzero modulo p for every actual boundary prime p>=19",
            "reason": (
                "w_H=-1 would force 1=-1/2 in the even case or 1=1/2 "
                "in the odd case, both impossible for p>=19"
            ),
        },
    }


def capacity_audit() -> dict[str, Any]:
    return {
        "boundary_union_raw_chebyshev_mass": "~2H",
        "retained_conditional_j1_capacity_per_6m": "1/36",
        "actual_gate_identity_from_Item301": "L_j=-Q_0(h)E_h^*",
        "scope": (
            "B_H nonvanishing is not a necessary-zero condition for the pinned "
            "collision. It only forces compensation by neighboring terms when its "
            "coefficient is a unit. This excludes no prime from the union."
        ),
        "boundary_coefficient_drops": boundary_coefficient_drop_audit(),
        "new_linear_log_rate": 0,
        "new_divisibility_exponent": 0,
        "capacity_booked": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item304-j1-boundary-gaussian-residue-v1",
        "item": 304,
        "title": "Gaussian numerator and exact nonzero structural-boundary residue",
        "dependencies": DEPENDENCIES,
        "arithmetic_theorem": symbolic_arithmetic_theorem(),
        "capacity_audit": capacity_audit(),
        "exact_replay": recurrence_replay(),
        "strict_labels": {
            "Gaussian_integer_numerator_recurrence": "PROVED ALL n",
            "moving_prime_specialization": "PROVED ALL ACTUAL BOUNDARIES",
            "B_H_nonvanishing": "PROVED ALL ACTUAL BOUNDARIES",
            "pinned_E_nonvanishing_or_weighted_density": "OPEN",
            "actual_prime_scan": "NONE",
            "capacity_booking": "ZERO",
            "retained_conditional_j1_capacity_per_6m": "1/36",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item304_j1_boundary_gaussian_residue_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item304_j1_boundary_gaussian_residue_certificate.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"output": str(output), "sha256": sha256(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
