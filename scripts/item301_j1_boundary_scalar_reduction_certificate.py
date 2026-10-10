#!/usr/bin/env python3
"""Exact Item 301 boundary-scalar reduction and de-overlap certificate.

The theorem is symbolic.  The finite all-integer replay checks its algebraic
formulas for consecutive H only; it performs no actual-row prime scan.
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
if item297.get("schema") != "item297-j1-structural-ray-boundary-v2":
    raise AssertionError("Item297 v2 is not admitted")


def convolve(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return answer


def kernel(h_value: int, extra: int) -> list[int]:
    left = [(-1) ** degree * math.comb(2 * h_value, degree) for degree in range(2 * h_value + 1)]
    right = [math.comb(extra, degree) for degree in range(extra + 1)]
    return convolve(left, right)


Complex = tuple[Fraction, Fraction]


def cadd(left: Complex, right: Complex) -> Complex:
    return left[0] + right[0], left[1] + right[1]


def csub(left: Complex, right: Complex) -> Complex:
    return left[0] - right[0], left[1] - right[1]


def cmul(left: Complex, right: Complex) -> Complex:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cscale(value: Complex, scalar: Fraction) -> Complex:
    return value[0] * scalar, value[1] * scalar


def cpow(value: Complex, exponent: int) -> Complex:
    answer: Complex = (Fraction(1), Fraction(0))
    factor = value
    while exponent:
        if exponent & 1:
            answer = cmul(answer, factor)
        exponent >>= 1
        if exponent:
            factor = cmul(factor, factor)
    return answer


def direct_components(h_value: int) -> tuple[Fraction, Fraction, Fraction, int]:
    k0 = kernel(h_value, 1)
    k1 = kernel(h_value, 4)
    x_value = sum(
        Fraction((-1) ** t * k0[2 * t + 1], t + 1) for t in range(h_value + 1)
    )
    y_value = sum(
        Fraction((-1) ** t * (h_value + 1) * k0[2 * t + 1], h_value + t + 1)
        for t in range(h_value + 1)
    )
    u_value = Fraction(k1[0]) + Fraction(1, 3) * sum(
        (-1) ** t * k1[2 * t] for t in range(1, h_value + 3)
    )
    v_value = sum((-1) ** t * k1[2 * t + 1] for t in range(h_value + 2))
    return x_value, y_value, u_value, v_value


def closed_xuv(h_value: int) -> tuple[Fraction, Fraction, int]:
    if h_value % 2 == 0:
        e_value = (-1) ** (h_value // 2) * 2**h_value
        x_value = Fraction(4 * (e_value - 1), 2 * h_value + 1) + Fraction(
            1, h_value + 1
        )
        return x_value, Fraction(2 - 4 * e_value, 3), 0
    d_value = (-1) ** ((h_value - 1) // 2) * 2**h_value
    x_value = Fraction(
        -(2 * d_value + 2 * h_value + 3),
        (2 * h_value + 1) * (h_value + 1),
    )
    return x_value, Fraction(2, 3), 4 * d_value


def j_moment(n_value: int) -> Complex:
    # Integral from 0 to 1 of [u(1-iu)]^n du, expanded exactly.
    answer: Complex = (Fraction(0), Fraction(0))
    minus_i: Complex = (Fraction(0), Fraction(-1))
    for degree in range(n_value + 1):
        term = cscale(
            cpow(minus_i, degree),
            Fraction(math.comb(n_value, degree), n_value + degree + 1),
        )
        answer = cadd(answer, term)
    return answer


def y_from_quadratic_moment(h_value: int) -> Fraction:
    power = cpow((Fraction(1), Fraction(-1)), 2 * h_value + 1)
    j_value = j_moment(2 * h_value)
    integral = cadd(
        cscale(power, Fraction(-1, 2 * (2 * h_value + 1))),
        cscale(j_value, Fraction(3, 2)),
    )
    return 2 * (h_value + 1) * integral[1]


def exact_replay(h_max: int = 80) -> dict[str, Any]:
    rows = []
    previous_j = j_moment(0)
    one_minus_i: Complex = (Fraction(1), Fraction(-1))
    one_minus_two_i: Complex = (Fraction(1), Fraction(-2))
    imaginary_unit: Complex = (Fraction(0), Fraction(1))
    for n_value in range(1, 2 * h_max + 1):
        current_j = j_moment(n_value)
        left = cmul(
            cpow(one_minus_i, n_value),
            one_minus_two_i,
        )
        right = csub(
            cscale(previous_j, Fraction(n_value)),
            cscale(cmul(imaginary_unit, current_j), Fraction(4 * n_value + 2)),
        )
        if left != right:
            raise AssertionError(("J recurrence", n_value, left, right))
        previous_j = current_j

    for h_value in range(1, h_max + 1):
        direct_x, direct_y, direct_u, direct_v = direct_components(h_value)
        closed_x, closed_u, closed_v = closed_xuv(h_value)
        moment_y = y_from_quadratic_moment(h_value)
        if (direct_x, direct_u, direct_v) != (closed_x, closed_u, closed_v):
            raise AssertionError(("XUV", h_value))
        if direct_y != moment_y:
            raise AssertionError(("Y moment", h_value, direct_y, moment_y))
        rows.append(
            [
                h_value,
                direct_x.numerator,
                direct_x.denominator,
                direct_y.numerator,
                direct_y.denominator,
                direct_u.numerator,
                direct_u.denominator,
                direct_v,
            ]
        )
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "EXACT REPLAY; NOT THE LOGICAL BASIS OF THE ALL-H PROOF",
        "consecutive_H": [1, h_max],
        "rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "actual_prime_scan": False,
    }


def symbolic_reduction() -> dict[str, Any]:
    return {
        "classification": "PROVED ALL-H ROOT-OF-UNITY AND INTEGRAL REDUCTION",
        "root_filters": {
            "even": "sum_t (-1)^t K_(2t)=[K(i)+K(-i)]/2",
            "odd": "sum_t (-1)^t K_(2t+1)=[K(i)-K(-i)]/(2i)",
            "K1_values": "K1(i)=-4(-2i)^H and K1(-i)=-4(2i)^H",
        },
        "even_H": {
            "e_H": "(-1)^(H/2)2^H",
            "U": "(2-4e_H)/3",
            "V": "0",
            "X": "4(e_H-1)/(2H+1)+1/(H+1)",
            "B_mod_p": "6(2e_H-1)Y",
            "unit_proof": (
                "p=8m+3 gives (2/p)=-1; Euler yields e_H^2=-1/2. "
                "If 2e_H-1=0, then 1/4=-1/2, forcing p=3, impossible."
            ),
            "zero_equivalence": "B_H=0 mod p iff Y=0 mod p",
        },
        "odd_H": {
            "d_H": "(-1)^((H-1)/2)2^H",
            "U": "2/3",
            "V": "4d_H",
            "X": "-(2d_H+2H+3)/[(2H+1)(H+1)]",
            "Euler_reduction": (
                "p=8m+7 gives d_H^2=1/2; H=-3/4 mod p then gives "
                "d_H X=8+12d_H"
            ),
            "B_mod_p": "-6(Y+4+6d_H)",
            "zero_equivalence": "B_H=0 mod p iff Y=-4-6d_H mod p",
        },
        "X_integral_derivation": {
            "filter": "X=(1/i) integral_0^1 [K0(iu)-K0(-iu)]du",
            "antiderivative": (
                "with w=1-iu, integral K0(iu)du = i[2w^(2H+1)/(2H+1)"
                "-w^(2H+2)/(2H+2)] from w=1 to 1-i"
            ),
            "parity": "substitution (1-i)^(2H)=(-2i)^H gives the displayed X",
        },
        "residual_Y": {
            "integral": (
                "Y=2(H+1) Im integral_0^1 u^(2H)(1-iu)^(2H)(1+iu)du"
            ),
            "quadratic_moment": (
                "for q=u(1-iu), J_n=integral_0^1 q^n du: "
                "Y=-(H+1)Im((1-i)^(2H+1))/(2H+1)+3(H+1)Im(J_(2H))"
            ),
            "exact_recurrence": (
                "J_0=1 and (1-i)^n(1-2i)=nJ_(n-1)-i(4n+2)J_n for n>=1"
            ),
            "scope": (
                "Y remains one explicit sequence-specific moment. No nonvanishing "
                "or weighted-density claim is inferred from this representation."
            ),
        },
    }


def deoverlap_theorem() -> dict[str, Any]:
    drops = item297["reduced_actual_ray_relations"][
        "normalized_coefficient_drops_by_s_then_p"
    ]
    q0_drops = {
        str(s_value): sorted(
            int(prime) for prime, indices in rows.items() if 0 in indices
        )
        for s_value, rows in drops.items()
    }
    expected = {"2": [19, 103423], "4": [15131], "6": []}
    if q0_drops != expected:
        raise AssertionError(("Q0 drop audit", q0_drops))
    return {
        "classification": "PROVED EXACT ACTUAL-RECURRENCE DE-OVERLAP",
        "definition": (
            "L_j=(Q_j/p)B_(h+3j)+sum_(k=1,k!=j)^3 Q_k E_(h+3k), s=2j"
        ),
        "identity": "L_j=-Q_0(h)E_h on every valid actual orbit",
        "unit_rows": (
            "if Q_0 is a p-unit, L_j=0 iff E_h=0, so the boundary-neighbor "
            "condition is exactly the old target gate and adds no codimension"
        ),
        "Q0_drop_rows_by_s": q0_drops,
        "drop_rows": (
            "when Q_0=0 mod p, the recurrence makes L_j=0 automatically and "
            "therefore L_j imposes no condition on E_h"
        ),
        "s6_scope": (
            "on s=6, L_3 uses B_(h+9) and the two neighboring actual values "
            "E_(h+3),E_(h+6), but the identity still makes it a re-encoding, "
            "not an independent gate"
        ),
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item301-j1-boundary-scalar-reduction-v1",
        "item": 301,
        "title": "exact boundary-scalar reduction and actual-gate de-overlap",
        "dependencies": DEPENDENCIES,
        "capacity_first": {
            "union_boundary_diagonal_raw_chebyshev_mass": "~2H",
            "retained_conditional_j1_capacity_per_6m": "1/36",
            "admission_rule": "only an all-H identity or weighted zero-density can matter",
        },
        "symbolic_reduction": symbolic_reduction(),
        "actual_recurrence_deoverlap": deoverlap_theorem(),
        "exact_replay": exact_replay(),
        "strict_labels": {
            "X_U_V_closed_forms": "PROVED ALL H",
            "B_parity_reduction": "PROVED ALL ACTUAL BOUNDARY PRIMES",
            "Y_moment_representation": "PROVED ALL H; RESIDUAL",
            "actual_recurrence_deoverlap": "PROVED",
            "Y_or_E_nonvanishing_or_weighted_density": "OPEN",
            "actual_prime_scan": "NONE",
            "new_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_booking": 0,
            "retained_conditional_j1_capacity_per_6m": "1/36",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item301_j1_boundary_scalar_reduction_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item301_j1_boundary_scalar_reduction_certificate.json"
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
