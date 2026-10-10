#!/usr/bin/env python3
"""Pure-Fraction specialization test for the Item 243 order-six candidate.

This does not prove a rational-function identity when it vanishes.  Conversely,
one regular specialization with a nonzero unsolved coordinate rigorously
refutes the projected order-six candidate as a global ambient recurrence.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item237 = load("item243_spec_item237", "item237_j1_algebraic_residual_certificate.py")


SPECS = {"x": (4, 15), "v": (3, 16)}


def q(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, (tuple, list)):
        return Fraction(value[0], value[1])
    return Fraction(value)


def evaluate(coefficients, argument):
    answer = Fraction(0)
    for coefficient in reversed(coefficients):
        answer = answer * argument + q(coefficient)
    return answer


def recurrence_blocks(data, residue, name):
    order, degree = SPECS[name]
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
    if cursor != len(flat):
        raise AssertionError((cursor, len(flat)))
    return answer


def identity(size):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def matmul(left, right):
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def row_times(row, matrix):
    return [
        sum((row[k] * matrix[k][j] for k in range(len(row))), Fraction(0))
        for j in range(len(matrix[0]))
    ]


def companion(blocks, argument):
    order = len(blocks) - 1
    leading = evaluate(blocks[-1], argument)
    if not leading:
        raise ZeroDivisionError(("companion-leading", argument))
    matrix = [[Fraction(0) for _ in range(order)] for _ in range(order)]
    for row in range(order - 1):
        matrix[row][row + 1] = Fraction(1)
    for column in range(order):
        matrix[-1][column] = -evaluate(blocks[column], argument) / leading
    return matrix


def rho(h):
    return Fraction(
        h
        * (4 * h + 1)
        * (4 * h + 5)
        * (4 * h + 7)
        * (4 * h + 9)
        * (4 * h + 11)
        * (4 * h + 15) ** 2,
        864
        * (h + 1)
        * (h + 2)
        * (2 * h + 1) ** 2
        * (2 * h + 3)
        * (2 * h + 5) ** 2
        * (4 * h + 3),
    )


def outer(left, right):
    return [a * b for a in left for b in right]


def add_scaled(target, source, scalar):
    for index, value in enumerate(source):
        target[index] += scalar * value


def bilinear_row_times(row, joint, v_matrix):
    matrix = [row[3 * i : 3 * i + 3] for i in range(5)]
    answer = [[Fraction(0) for _ in range(3)] for _ in range(5)]
    for j in range(5):
        for l in range(3):
            answer[j][l] = sum(
                (
                    matrix[i][k] * joint[i][j] * v_matrix[k][l]
                    for i in range(5)
                    for k in range(3)
                ),
                Fraction(0),
            )
    return [value for current in answer for value in current]


def solve_square(matrix, right):
    size = len(matrix)
    rows = [matrix[row][:] + [right[row]] for row in range(size)]
    for column in range(size):
        source = next((row for row in range(column, size) if rows[row][column]), None)
        if source is None:
            raise ArithmeticError(("singular-projection", column))
        rows[column], rows[source] = rows[source], rows[column]
        pivot = rows[column][column]
        rows[column] = [entry / pivot for entry in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                rows[row][entry] - multiplier * rows[column][entry]
                for entry in range(size + 1)
            ]
    return [rows[row][-1] for row in range(size)]


def build_system(residue):
    recurrences = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    relations = json.loads((HERE / "item243_cross_reconstruct.json").read_text())
    x_blocks = recurrence_blocks(recurrences, residue, "x")
    v_blocks = recurrence_blocks(recurrences, residue, "v")
    xu_x, xu_u = relation_blocks(relations, residue, "xu", (1, 1), 7)
    yv_y, yv_v = relation_blocks(relations, residue, "yv", (0, 2), 12)
    recurrence = item237.recurrence_polynomials()

    def joint_matrix(argument):
        x_matrix = companion(x_blocks, argument)
        matrix = [row + [Fraction(0)] for row in x_matrix]
        denominator = evaluate(xu_u[1], argument)
        if not denominator:
            raise ZeroDivisionError(("xu", argument))
        matrix.append(
            [
                -evaluate(xu_x[0], argument) / denominator,
                -evaluate(xu_x[1], argument) / denominator,
                Fraction(0),
                Fraction(0),
                -evaluate(xu_u[0], argument) / denominator,
            ]
        )
        return matrix

    def y_row(argument):
        denominator = evaluate(yv_y[0], argument)
        if not denominator:
            raise ZeroDivisionError(("yv", argument))
        return [-evaluate(polynomial, argument) / denominator for polynomial in yv_v]

    def v_matrix(argument):
        return companion(v_blocks, argument)

    def defect(argument):
        h = 3 * argument + residue
        joint_product = identity(5)
        v_product = identity(3)
        answer = [Fraction(0)] * 15
        gauge = Fraction(1)
        for shift in range(4):
            coefficient = evaluate(recurrence[shift], h) * gauge
            x_row = joint_product[0]
            u_row = joint_product[4]
            vv_row = v_product[0]
            shifted_y = row_times(y_row(argument + shift), v_product)
            h_shift = h + 3 * shift
            add_scaled(
                answer,
                outer(x_row, vv_row),
                coefficient * Fraction(h_shift, 4 * h_shift + 3),
            )
            add_scaled(
                answer,
                outer(u_row, shifted_y),
                coefficient * Fraction(9 * (4 * h_shift + 1), 2 * (4 * h_shift + 3)),
            )
            joint_product = matmul(joint_matrix(argument + shift), joint_product)
            v_product = matmul(v_matrix(argument + shift), v_product)
            gauge *= rho(h + 3 * shift)
        return answer

    return joint_matrix, v_matrix, defect


def prove_specialization_with_system(residue, initial, system, compact=False):
    joint_matrix, v_matrix, defect = system
    joint_product = identity(5)
    v_product = identity(3)
    rows = []
    for shift in range(7):
        rows.append(bilinear_row_times(defect(initial + shift), joint_product, v_product))
        if shift < 6:
            joint_product = matmul(joint_matrix(initial + shift), joint_product)
            v_product = matmul(v_matrix(initial + shift), v_product)
    matrix = [[rows[shift][coordinate] for shift in range(6)] for coordinate in range(6)]
    right = [-rows[6][coordinate] for coordinate in range(6)]
    coefficients = solve_square(matrix, right) + [Fraction(1)]
    checks = [
        sum((coefficients[shift] * rows[shift][coordinate] for shift in range(7)), Fraction(0))
        for coordinate in range(15)
    ]
    nonzero = [index for index, value in enumerate(checks) if value]
    result = {
        "classification": "EXACT_SINGLE_SPECIALIZATION",
        "residue": residue,
        "initial_index": initial,
        "projection_rank": 6,
        "nonzero_coordinates": nonzero,
        "global_logical_force": (
            "refutes the global projected order-six candidate" if nonzero
            else "none: a zero specialization is finite evidence only"
        ),
    }
    if not compact:
        result["coordinate_checks"] = [
            [value.numerator, value.denominator] for value in checks
        ]
        result["candidate_coefficients"] = [
            [value.numerator, value.denominator] for value in coefficients
        ]
    return result


def prove_specialization(residue, initial):
    return prove_specialization_with_system(residue, initial, build_system(residue))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int, choices=(1, 2))
    parser.add_argument("initial", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = prove_specialization(args.residue, args.initial)
    output = args.output or HERE / f"item243_defect_specialization_r{args.residue}_n{args.initial}.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key not in {"coordinate_checks", "candidate_coefficients"}}, sort_keys=True))
    print(json.dumps({"output": str(output)}))


if __name__ == "__main__":
    main()
