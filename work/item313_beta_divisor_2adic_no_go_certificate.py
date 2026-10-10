#!/usr/bin/env python3
"""Exact deterministic replay for Item 313.

The all-length statements are proved by the symbolic induction recorded in
the certificate.  The bounded rows below are fixed algebra controls only;
they are not a divisibility scan or finite promotion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


Matrix = tuple[tuple[int, int], tuple[int, int]]
I2: Matrix = ((1, 0), (0, 1))
J2: Matrix = ((0, 1), (1, 0))
E11: Matrix = ((1, 0), (0, 0))


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def reduce_matrix(matrix: Matrix, modulus: int) -> Matrix:
    return tuple(
        tuple(entry % modulus for entry in row) for row in matrix
    )  # type: ignore[return-value]


def matrix(coefficient: int) -> Matrix:
    return ((coefficient, 1), (1, 0))


def coefficient(index: int) -> int:
    return 4 * index - 2


def transfer(start: int, length: int) -> Matrix:
    result = I2
    for index in range(start, start + length):
        result = matmul(result, matrix(coefficient(index)))
    return result


def nilpotent(start: int) -> Matrix:
    epsilon = -1 if start % 2 else 1
    return ((1, -epsilon), (epsilon, -1))


def scaled_add_identity(scale: int, value: Matrix) -> Matrix:
    return tuple(
        tuple(I2[row][column] + scale * value[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def continuant(values: list[int]) -> int:
    before_previous = 0
    previous = 1
    for value in values:
        before_previous, previous = previous, value * previous + before_previous
    return previous


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is not used")
    absolute = abs(value)
    return (absolute & -absolute).bit_length() - 1


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append(coefficient(index) * values[-1] + values[-2])
    return values


def centered(value: int, odd_modulus: int) -> int:
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def base_residue_proof() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    expected = {
        0: ((5, 12), (4, 13)),
        1: ((5, 4), (12, 13)),
        2: ((5, 12), (4, 13)),
        3: ((5, 4), (12, 13)),
    }
    for residue in range(4):
        actual = reduce_matrix(transfer(residue, 4), 16)
        target = reduce_matrix(scaled_add_identity(4, nilpotent(residue)), 16)
        assert actual == expected[residue] == target
        rows.append(
            {
                "start_mod_4": residue,
                "F_4_mod_16": actual,
                "equals_I_plus_4N": True,
            }
        )
    return {
        "exhaustive_residue_classes": rows,
        "why_exhaustive": "B_(r+4)=B_r+16",
        "row_digest": digest(rows),
        "role": "EXACT BASE FOR SYMBOLIC DOUBLING INDUCTION",
    }


def shift_linearization_proof() -> dict[str, Any]:
    assert reduce_matrix(matmul(J2, E11), 2) == ((0, 0), (1, 0))
    assert reduce_matrix(matmul(E11, J2), 2) == ((0, 1), (0, 0))
    return {
        "coefficient_shift": "B_(r+h+i)-B_(r+i)=4h",
        "multilinear_reduction_mod_8h": (
            "4h*sum_(i=0)^(h-1) J^i E11 J^(h-1-i)"
        ),
        "summand_counts_for_4_divides_h": {
            "E12": "h/2, even",
            "E21": "h/2, even",
        },
        "conclusion": "F_h(r+h)=F_h(r) mod 8h",
        "double_step": (
            "F_(2h)=F_h(r)F_h(r+h)=I+2hN_r mod 8h because N_r^2=0"
        ),
        "odd_multiple_step": (
            "F_(uh)=(I+hN_r)^u=I+uhN_r mod 4h for odd u"
        ),
        "status": "PROVED SYMBOLICALLY",
    }


def fixed_transfer_controls() -> dict[str, Any]:
    declared = [(2, 4), (3, 8), (5, 12), (7, 16), (3, 24), (8, 40)]
    rows: list[dict[str, Any]] = []
    for start, length in declared:
        scale = length & -length
        modulus = 4 * scale
        actual = reduce_matrix(transfer(start, length), modulus)
        target = reduce_matrix(
            scaled_add_identity(length, nilpotent(start)), modulus
        )
        assert actual == target
        shifted = transfer(start + scale, scale)
        original = transfer(start, scale)
        assert all(
            (shifted[row][column] - original[row][column]) % (8 * scale) == 0
            for row in range(2)
            for column in range(2)
        )
        rows.append(
            {
                "start": start,
                "length": length,
                "2adic_scale": scale,
                "modulus": modulus,
                "transfer_identity": True,
                "shift_identity_at_scale": True,
            }
        )
    return {
        "declared_rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_all_length_statement": False,
    }


def denominator_shift_controls() -> dict[str, Any]:
    declared = [(2, 4), (3, 8), (6, 12), (7, 16), (11, 24), (4, 40)]
    q_values = beta_q(max(j + length for j, length in declared))
    rows: list[dict[str, Any]] = []
    for j, length in declared:
        left = q_values[j + length] - q_values[j]
        bracket = q_values[j] + (-1) ** (j + 1) * q_values[j - 1]
        scale = length & -length
        assert bracket % 4 == 2
        assert (left - length * bracket) % (4 * scale) == 0
        assert v2(left) == v2(length) + 1
        rows.append(
            {
                "j": j,
                "length": length,
                "v2_length": v2(length),
                "v2_q_shift": v2(left),
                "bracket_mod_4": bracket % 4,
            }
        )
    return {
        "declared_rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_valuation_lemma": False,
    }


def four_continuant_controls() -> dict[str, Any]:
    declared = [
        (2, 4, 2),
        (3, 8, 2),
        (3, 8, 6),
        (5, 12, 4),
        (7, 16, 8),
        (8, 24, 22),
        (3, 40, 18),
    ]
    rows: list[dict[str, Any]] = []
    for start, length, prefix_length in declared:
        word = [coefficient(index) for index in range(start, start + length)]
        c_value = continuant(word)
        h_value = continuant(word[:prefix_length])
        y_value = continuant(word[:-2])
        theta_value = continuant(word[prefix_length + 1 : -1])
        difference = c_value * theta_value - h_value * y_value
        scale = length & -length
        assert difference % (2 * scale) == scale
        assert v2(difference) == v2(length)
        rows.append(
            {
                "start": start,
                "length": length,
                "prefix_length": prefix_length,
                "theta_empty": prefix_length == length - 2,
                "v2_difference": v2(difference),
                "v2_length": v2(length),
            }
        )
    return {
        "declared_rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_valuation_lemma": False,
    }


def parity_and_base_audit() -> dict[str, Any]:
    q_values = beta_q(8)
    assert [value % 8 for value in q_values[:8]] == [1, 1, 7, 7, 1, 1, 7, 7]
    for length in range(0, 12, 2):
        word = [coefficient(3 + offset) for offset in range(length)]
        assert continuant(word) % 4 == 1

    polynomial_at_10 = 2 * 10**3 + 7 * 10**2 - 20 * 10 - 97
    assert polynomial_at_10 == 2403
    assert 6 * 10**2 + 20 * 10 - 11 > 0

    q_values = beta_q(4)
    expected = {
        2: (1, 1, 1),
        3: (7, 1, 22),
        4: (71, 7, 36),
    }
    base_rows: list[dict[str, int]] = []
    for n, (a_value, c_value, remainder_size) in expected.items():
        b_value = q_values[n]
        assert (q_values[n - 1], q_values[n - 2]) == (a_value, c_value)
        signed = centered(a_value * a_value, b_value)
        assert abs(signed) == remainder_size
        assert 2 * c_value * remainder_size >= a_value
        base_rows.append(
            {
                "n": n,
                "a": a_value,
                "c": c_value,
                "R_actual": remainder_size,
            }
        )
    return {
        "q_mod_8_period": [1, 1, 7, 7],
        "even_length_even_entry_continuant_mod_4": 1,
        "L_equals_2_polynomial_at_10": polynomial_at_10,
        "small_bases": base_rows,
        "label": "PROVED RESIDUE INDUCTIONS AND EXACT BASES",
    }


def proof_object() -> dict[str, Any]:
    return {
        "hypothetical_branch": (
            "C=Dhat_k divides a and C>2cQ_k; j=k+1, V=q_j, "
            "U=q_(j+1), L=n-j-1"
        ),
        "overlap_identity": (
            "with a=UX+VZ, c=UY+VW, C=B_nX+Y, g=a/C and eta=B_ng-U, "
            "VZ=gY+eta X"
        ),
        "strict_approximation": (
            "0<Z/X-eta/V=gY/(VX)<1/(2V^2); L=2 is excluded first, "
            "and L>=4 makes X>B_(n-1)Y>=2gVY"
        ),
        "rational_endpoint_audit": (
            "0/1 and the terminal convergent are excluded; the alternate "
            "penultimate has error 1/(X(X-X_-)) and cannot meet Legendre "
            "because X>2X_-"
        ),
        "euler_output": (
            "an even canonical prefix length ell gives gY=dTheta and "
            "the exact identity aHY=V C Theta"
        ),
        "parity_bridge": (
            "C|a makes L even; if L=2 the size condition fails; if "
            "L=2 mod 4 then q_(j+L)/q_j=-1 mod 8 while the four even-length "
            "continuants give only 1 or 5 mod 8; hence 4|L"
        ),
        "transfer_theorem": (
            "F_L(r)=I+L N_r mod 4*2^v2(L), N_r^2=0, by the exact h=4 "
            "base, multilinear shift lemma, doubling, and odd-block power"
        ),
        "valuation_contradiction": (
            "v2(q_(j+L)-q_j)=v2(L)+1 but "
            "v2(C Theta-HY)=v2(L); (a-V)HY=V(C Theta-HY) is impossible"
        ),
        "theorem": (
            "Dhat_k>2q_(n-2)Q_k implies Dhat_k does not divide q_(n-1) "
            "for n>=5 and 1<=k<n-2"
        ),
        "actual_consequence": "R_actual>=q_(n-1)/(2q_(n-2)) for n>=2",
        "not_proved": [
            "R_actual>=q_(n-1)/2",
            "the intermediate-window exclusion",
            "any beta capacity reduction",
        ],
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item313-beta-divisor-2adic-no-go-certificate-v1",
        "item": 313,
        "date_beijing": "2026-08-31",
        "status": "PROVED_SCOPED_DIVISOR_EXCLUSION",
        "proof": proof_object(),
        "symbolic_transfer_induction": {
            "base": base_residue_proof(),
            "shift_and_doubling": shift_linearization_proof(),
        },
        "exact_replay_controls": {
            "transfer": fixed_transfer_controls(),
            "denominator_shift": denominator_shift_controls(),
            "four_continuants": four_continuant_controls(),
            "parity_and_bases": parity_and_base_audit(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "divisibility_scan": False,
            "half_bound_scan": False,
        },
        "strict_labels": {
            "all_length_transfer_congruence": "PROVED",
            "denominator_shift_valuation": "PROVED",
            "four_continuant_valuation": "PROVED",
            "item311_divisor_exclusion": "PROVED",
            "weaker_actual_bound": "PROVED",
            "centered_half_bound": "OPEN",
            "intermediate_window": "OPEN",
            "bounded_controls": "EXACT FINITE ONLY",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "closes": "only the Item305/Item311 Legendre-classified multiplier window",
            "does_not_close": "R_actual>=a/2 or the intermediate window",
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
                "item": 313,
                "status": certificate["status"],
                "divisor_exclusion": "PROVED",
                "weaker_actual_bound": "PROVED",
                "centered_half_bound": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
