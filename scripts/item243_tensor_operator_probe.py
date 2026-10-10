#!/usr/bin/env python3
"""Exact tensor-companion test for the Item 243 gauged E recurrence."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.fields import field


HERE = Path(__file__).resolve().parent
K, n = field("n", QQ)


SPECS = {
    "x": (4, 15),
    "y": (3, 14),
    "u": (5, 15),
    "v": (3, 16),
}


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ground(value):
    if isinstance(value, Fraction):
        return QQ(value.numerator, value.denominator)
    if isinstance(value, (tuple, list)):
        return QQ(value[0], value[1])
    return QQ(value)


def evaluate(coefficients, argument):
    answer = K.zero
    for coefficient in reversed(coefficients):
        answer = answer * argument + ground(coefficient)
    return answer


def recurrence_blocks(data, residue, name):
    order, degree = SPECS[name]
    flat = data["recurrences"][f"r{residue}_{name}"]
    return [
        flat[shift * (degree + 1) : (shift + 1) * (degree + 1)]
        for shift in range(order + 1)
    ]


def companion(blocks, argument):
    order = len(blocks) - 1
    leading = evaluate(blocks[-1], argument)
    matrix = [[K.zero for _ in range(order)] for _ in range(order)]
    for row in range(order - 1):
        matrix[row][row + 1] = K.one
    for column in range(order):
        matrix[-1][column] = -evaluate(blocks[column], argument) / leading
    return matrix


def row_times(row, matrix):
    return [
        sum((row[index] * matrix[index][column] for index in range(len(row))), K.zero)
        for column in range(len(matrix[0]))
    ]


def diagonal_rows(blocks, maximum_shift=3):
    rows = [[K.one] + [K.zero] * (len(blocks) - 2)]
    for shift in range(maximum_shift):
        rows.append(row_times(rows[-1], companion(blocks, n + shift)))
    return rows


def residual_recurrence():
    item237 = load("item243_item237_exact", "item237_j1_algebraic_residual_certificate.py")
    return item237.recurrence_polynomials()


def rho(h):
    return (
        h
        * (4 * h + 1)
        * (4 * h + 5)
        * (4 * h + 7)
        * (4 * h + 9)
        * (4 * h + 11)
        * (4 * h + 15) ** 2
        / (
            864
            * (h + 1)
            * (h + 2)
            * (2 * h + 1) ** 2
            * (2 * h + 3)
            * (2 * h + 5) ** 2
            * (4 * h + 3)
        )
    )


def outer(left, right):
    return [a * b for a in left for b in right]


def identity(size):
    return [
        [K.one if row == column else K.zero for column in range(size)]
        for row in range(size)
    ]


def matmul(left, right):
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(len(right))),
                K.zero,
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def relation_blocks(relations, residue, key, orders, degree):
    flat = relations["relations"][f"r{residue}_{key}"]
    answer = []
    cursor = 0
    for order in orders:
        current = []
        for _ in range(order + 1):
            current.append(flat[cursor : cursor + degree + 1])
            cursor += degree + 1
        answer.append(current)
    if cursor != len(flat):
        raise AssertionError((cursor, len(flat)))
    return answer


def add_scaled(target, source, scalar):
    for index, value in enumerate(source):
        target[index] += scalar * value


def verify_residue(residue):
    data = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    rows = {
        name: diagonal_rows(recurrence_blocks(data, residue, name))
        for name in SPECS
    }
    recurrence = residual_recurrence()
    h = 3 * n + residue
    rho_product = K.one
    xv = [K.zero] * (SPECS["x"][0] * SPECS["v"][0])
    uy = [K.zero] * (SPECS["u"][0] * SPECS["y"][0])
    term_summaries = []
    for shift in range(4):
        h_shift = h + 3 * shift
        coefficient = evaluate(recurrence[shift], h) * rho_product
        xv_weight = coefficient * h_shift / (4 * h_shift + 3)
        uy_weight = coefficient * 9 * (4 * h_shift + 1) / (2 * (4 * h_shift + 3))
        add_scaled(xv, outer(rows["x"][shift], rows["v"][shift]), xv_weight)
        add_scaled(uy, outer(rows["u"][shift], rows["y"][shift]), uy_weight)
        term_summaries.append(
            {
                "shift": shift,
                "rho_product_numerator_degree": rho_product.numer.degree(),
                "rho_product_denominator_degree": rho_product.denom.degree(),
            }
        )
        rho_product *= rho(h_shift)
    nonzero_xv = [index for index, value in enumerate(xv) if value]
    nonzero_uy = [index for index, value in enumerate(uy) if value]
    return {
        "residue": residue,
        "xv_dimension": len(xv),
        "uy_dimension": len(uy),
        "xv_nonzero_coordinates": nonzero_xv,
        "uy_nonzero_coordinates": nonzero_uy,
        "verified_zero": not nonzero_xv and not nonzero_uy,
        "term_summaries": term_summaries,
    }


def verify_joint_residue(residue):
    recurrences = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    relations = json.loads((HERE / "item243_cross_reconstruct.json").read_text())
    x_blocks = recurrence_blocks(recurrences, residue, "x")
    v_blocks = recurrence_blocks(recurrences, residue, "v")
    (xu_x, xu_u) = relation_blocks(relations, residue, "xu", (1, 1), 7)
    (yv_y, yv_v) = relation_blocks(relations, residue, "yv", (0, 2), 12)

    def joint_matrix(argument):
        x_matrix = companion(x_blocks, argument)
        matrix = [row + [K.zero] for row in x_matrix]
        denominator = evaluate(xu_u[1], argument)
        matrix.append(
            [
                -evaluate(xu_x[0], argument) / denominator,
                -evaluate(xu_x[1], argument) / denominator,
                K.zero,
                K.zero,
                -evaluate(xu_u[0], argument) / denominator,
            ]
        )
        return matrix

    def y_row(argument):
        denominator = evaluate(yv_y[0], argument)
        return [-evaluate(polynomial, argument) / denominator for polynomial in yv_v]

    recurrence = residual_recurrence()
    h = 3 * n + residue
    rho_product = K.one
    total = [K.zero] * 15
    joint_product = identity(5)
    v_product = identity(3)
    term_summaries = []
    for shift in range(4):
        h_shift = h + 3 * shift
        coefficient = evaluate(recurrence[shift], h) * rho_product
        x_row = joint_product[0]
        u_row = joint_product[4]
        v_row = v_product[0]
        shifted_y_row = row_times(y_row(n + shift), v_product)
        add_scaled(
            total,
            outer(x_row, v_row),
            coefficient * h_shift / (4 * h_shift + 3),
        )
        add_scaled(
            total,
            outer(u_row, shifted_y_row),
            coefficient * 9 * (4 * h_shift + 1) / (2 * (4 * h_shift + 3)),
        )
        term_summaries.append(
            {
                "shift": shift,
                "joint_product_numerator_max_degree": max(
                    value.numer.degree() for row in joint_product for value in row
                ),
                "v_product_numerator_max_degree": max(
                    value.numer.degree() for row in v_product for value in row
                ),
            }
        )
        joint_product = matmul(joint_matrix(n + shift), joint_product)
        v_product = matmul(companion(v_blocks, n + shift), v_product)
        rho_product *= rho(h_shift)
    nonzero = [index for index, value in enumerate(total) if value]
    return {
        "residue": residue,
        "joint_dimension": len(total),
        "nonzero_coordinates": nonzero,
        "verified_zero": not nonzero,
        "term_summaries": term_summaries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--residue", type=int, choices=(1, 2))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--independent", action="store_true")
    args = parser.parse_args()
    residues = [args.residue] if args.residue else [1, 2]
    result = {
        "classification": "PROVED_EXACT_AMBIENT_COVECTOR_NO_GO",
        "theorem": (
            "The gauged order-three defect covector is not the zero covector "
            "on the full 15-dimensional joint companion space in either "
            "nonzero residue. Closure therefore cannot be obtained by the "
            "naive one-step ambient annihilation; the transported order-six "
            "relation is genuinely needed."
        ),
        "scope_warning": (
            "Nonzero ambient coordinates do not refute vanishing on the one "
            "actual hypergeometric orbit."
        ),
        "residues": [],
    }
    for residue in residues:
        current = verify_residue(residue) if args.independent else verify_joint_residue(residue)
        if not args.independent and not current["nonzero_coordinates"]:
            raise AssertionError((residue, "unexpected zero ambient covector"))
        result["residues"].append(current)
        print(json.dumps(current), flush=True)
    output = args.output or HERE / "item243_tensor_operator_probe.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output)}))


if __name__ == "__main__":
    main()
