#!/usr/bin/env python3
"""Exact Newton-sign certificate for the Item 243 forward cofactor."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.set_int_max_str_digits(0)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


special = load(
    "item243_newton_specialization", "item243_defect_specialization_probe.py"
)


def recurrence_blocks(data, residue, name, order, degree):
    flat = data["recurrences"][f"r{residue}_{name}"]
    return [
        flat[shift * (degree + 1) : (shift + 1) * (degree + 1)]
        for shift in range(order + 1)
    ]


def relation_blocks(data, residue, key, orders, degree):
    flat = data["relations"][f"r{residue}_{key}"]
    answer = []
    cursor = 0
    for order in orders:
        part = []
        for _ in range(order + 1):
            part.append(flat[cursor : cursor + degree + 1])
            cursor += degree + 1
        answer.append(part)
    return answer


def primitive_data(residue):
    recurrences = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    relations = json.loads((HERE / "item243_cross_reconstruct.json").read_text())
    x_lead = recurrence_blocks(recurrences, residue, "x", 4, 15)[-1]
    v_lead = recurrence_blocks(recurrences, residue, "v", 3, 16)[-1]
    xu_x, xu_u = relation_blocks(relations, residue, "xu", (1, 1), 7)
    yv_y, yv_v = relation_blocks(relations, residue, "yv", (0, 2), 12)
    return x_lead, v_lead, xu_u[1], yv_y[0]


def common_denominators(residue):
    x_lead, v_lead, xu_lead, y_lead = primitive_data(residue)

    def joint_den(argument):
        return special.evaluate(x_lead, argument) * special.evaluate(xu_lead, argument)

    def v_den(argument):
        return special.evaluate(v_lead, argument)

    def y_den(argument):
        return special.evaluate(y_lead, argument)

    def rho_den(h):
        return Fraction(
            864
            * (h + 1)
            * (h + 2)
            * (2 * h + 1) ** 2
            * (2 * h + 3)
            * (2 * h + 5) ** 2
            * (4 * h + 3)
        )

    def defect_den(argument):
        h = 3 * argument + residue
        answer = Fraction(1)
        for shift in range(3):
            answer *= rho_den(h + 3 * shift)
            answer *= joint_den(argument + shift)
            answer *= v_den(argument + shift)
        for shift in range(4):
            answer *= 4 * (h + 3 * shift) + 3
            answer *= y_den(argument + shift)
        return answer

    def orbit_den(initial, shift):
        answer = defect_den(initial + shift)
        for step in range(shift):
            answer *= joint_den(initial + step)
            answer *= v_den(initial + step)
        return answer

    return orbit_den


def determinant(matrix):
    rows = [row[:] for row in matrix]
    answer = Fraction(1)
    for column in range(len(rows)):
        source = next((row for row in range(column, len(rows)) if rows[row][column]), None)
        if source is None:
            return Fraction(0)
        if source != column:
            rows[column], rows[source] = rows[source], rows[column]
            answer = -answer
        pivot = rows[column][column]
        answer *= pivot
        for row in range(column + 1, len(rows)):
            if not rows[row][column]:
                continue
            multiplier = rows[row][column] / pivot
            for entry in range(column, len(rows)):
                rows[row][entry] -= multiplier * rows[column][entry]
    return answer


def cofactor_value(initial, system, orbit_den):
    joint_matrix, v_matrix, defect = system
    joint_product = special.identity(5)
    v_product = special.identity(3)
    columns = []
    for shift in range(6):
        row = special.bilinear_row_times(
            defect(initial + shift), joint_product, v_product
        )
        denominator = orbit_den(initial, shift)
        columns.append([value * denominator for value in row])
        joint_product = special.matmul(joint_matrix(initial + shift), joint_product)
        v_product = special.matmul(v_matrix(initial + shift), v_product)
    matrix = [
        [columns[column][coordinate] for column in range(6)]
        for coordinate in range(6)
    ]
    return determinant(matrix)


def digest_fractions(values):
    digest = hashlib.sha256()

    def update_integer(value):
        sign = 0 if value == 0 else 1 if value > 0 else 2
        magnitude = abs(value)
        payload = magnitude.to_bytes(max(1, (magnitude.bit_length() + 7) // 8), "big")
        digest.update(bytes([sign]))
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)

    for index, value in enumerate(values):
        digest.update(index.to_bytes(8, "big"))
        update_integer(value.numerator)
        update_integer(value.denominator)
    return digest.hexdigest()


def fraction_fingerprint(value):
    return {
        "numerator_bits": abs(value.numerator).bit_length(),
        "denominator_bits": value.denominator.bit_length(),
        "sha256": digest_fractions([value]),
        "sign": 0 if not value else 1 if value > 0 else -1,
    }


def residue_certificate(residue, degree_bound, progress):
    system = special.build_system(residue)
    orbit_den = common_denominators(residue)
    values = []
    for initial in range(degree_bound + 2):
        values.append(cofactor_value(initial, system, orbit_den))
        if progress and (initial + 1) % progress == 0:
            print(
                json.dumps(
                    {
                        "stage": "values",
                        "residue": residue,
                        "completed": initial + 1,
                        "required": degree_bound + 2,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    value_digest = digest_fractions(values)
    differences = values
    leading = []
    for order in range(degree_bound + 2):
        leading.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]
        if progress and (order + 1) % progress == 0:
            print(
                json.dumps(
                    {
                        "stage": "differences",
                        "residue": residue,
                        "completed": order + 1,
                        "required": degree_bound + 2,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    if leading[-1]:
        raise AssertionError(
            {
                "residue": residue,
                "failure": "degree-bound-failure",
                "terminal_difference": fraction_fingerprint(leading[-1]),
            }
        )
    nonzero = leading[:-1]
    signs = {1 if value > 0 else -1 if value < 0 else 0 for value in nonzero}
    if 1 in signs and -1 in signs:
        raise AssertionError((residue, "mixed-newton-signs", signs))
    if not any(nonzero):
        raise AssertionError((residue, "zero-cofactor"))
    nonzero_sign = 1 if 1 in signs else -1
    return {
        "residue": residue,
        "degree_bound": degree_bound,
        "values_checked": len(values),
        "terminal_difference_order": degree_bound + 1,
        "terminal_difference_zero": True,
        "newton_coefficients": len(nonzero),
        "positive_coefficients": sum(value > 0 for value in nonzero),
        "negative_coefficients": sum(value < 0 for value in nonzero),
        "zero_coefficients": sum(not value for value in nonzero),
        "common_nonzero_sign": nonzero_sign,
        "value_stream_sha256": value_digest,
        "newton_stream_sha256": digest_fractions(leading),
        "conclusion": (
            "The forward cofactor is a nonzero one-sign linear combination of "
            "binomial(n,k), hence has no zero at any integer n>=0."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree-bound", type=int, default=1806)
    parser.add_argument("--progress", type=int, default=100)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item243_forward_cofactor_newton_certificate.json",
    )
    args = parser.parse_args()
    result = {
        "item": 243,
        "classification": "SYMBOLIC_EXACT_NEWTON_SIGN",
        "basis_identity": (
            "F(n)=sum_(k=0)^d Delta^k F(0)*binomial(n,k), deg(F)<=d"
        ),
        "residues": [
            residue_certificate(residue, args.degree_bound, args.progress)
            for residue in (1, 2)
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
