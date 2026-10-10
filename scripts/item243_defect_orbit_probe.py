#!/usr/bin/env python3
"""Finite-field generic orbit rank of the Item 243 target defect covector."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
P = 1000000007


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


linear = load("item243_defect_linear", "item237_residual_probe.py")
item237 = load("item243_defect_item237", "item237_j1_algebraic_residual_certificate.py")


SPECS = {"x": (4, 15), "v": (3, 16)}


def frac_mod(pair):
    return pair[0] % P * pow(pair[1] % P, -1, P) % P


def evaluate(coefficients, argument):
    answer = 0
    for coefficient in reversed(coefficients):
        if isinstance(coefficient, (list, tuple)):
            coefficient = frac_mod(coefficient)
        else:
            coefficient = coefficient.numerator % P * pow(coefficient.denominator % P, -1, P) % P
        answer = (answer * argument + coefficient) % P
    return answer


def blocks(recurrences, residue, name):
    order, degree = SPECS[name]
    flat = recurrences["recurrences"][f"r{residue}_{name}"]
    return [flat[k * (degree + 1) : (k + 1) * (degree + 1)] for k in range(order + 1)]


def relation_blocks(relations, residue, key, orders, degree):
    flat = relations["relations"][f"r{residue}_{key}"]
    answer = []
    cursor = 0
    for order in orders:
        part = []
        for _ in range(order + 1):
            part.append(flat[cursor : cursor + degree + 1])
            cursor += degree + 1
        answer.append(part)
    return answer


def companion(current, argument):
    order = len(current) - 1
    lead = evaluate(current[-1], argument)
    matrix = [[0] * order for _ in range(order)]
    for row in range(order - 1):
        matrix[row][row + 1] = 1
    for column in range(order):
        matrix[-1][column] = -evaluate(current[column], argument) * pow(lead, -1, P) % P
    return matrix


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) % P for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def row_times(row, matrix):
    return [sum(row[k] * matrix[k][j] for k in range(len(row))) % P for j in range(len(matrix[0]))]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def kron(left, right):
    return [
        [left[i][j] * right[k][l] % P for j in range(len(left[0])) for l in range(len(right[0]))]
        for i in range(len(left))
        for k in range(len(right))
    ]


def rho(h):
    numerator = h
    for value in (4 * h + 1, 4 * h + 5, 4 * h + 7, 4 * h + 9, 4 * h + 11):
        numerator = numerator * value % P
    numerator = numerator * pow(4 * h + 15, 2, P) % P
    denominator = 864 * (h + 1) * (h + 2) * (2 * h + 1) ** 2 * (2 * h + 3) * (2 * h + 5) ** 2 * (4 * h + 3)
    return numerator * pow(denominator % P, -1, P) % P


def system(residue):
    recurrences = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    relations = json.loads((HERE / "item243_cross_reconstruct.json").read_text())
    xb = blocks(recurrences, residue, "x")
    vb = blocks(recurrences, residue, "v")
    xu_x, xu_u = relation_blocks(relations, residue, "xu", (1, 1), 7)
    yv_y, yv_v = relation_blocks(relations, residue, "yv", (0, 2), 12)

    def transition(index):
        xm = companion(xb, index)
        jm = [row + [0] for row in xm]
        den = evaluate(xu_u[1], index)
        jm.append([
            -evaluate(xu_x[0], index) * pow(den, -1, P) % P,
            -evaluate(xu_x[1], index) * pow(den, -1, P) % P,
            0,
            0,
            -evaluate(xu_u[0], index) * pow(den, -1, P) % P,
        ])
        return kron(jm, companion(vb, index))

    def e_row(index):
        h = 3 * index + residue
        yden = evaluate(yv_y[0], index)
        yr = [-evaluate(poly, index) * pow(yden, -1, P) % P for poly in yv_v]
        answer = [0] * 15
        answer[0] = h * pow(4 * h + 3, -1, P) % P
        scalar = 9 * (4 * h + 1) * pow(2 * (4 * h + 3), -1, P) % P
        for k in range(3):
            answer[12 + k] = scalar * yr[k] % P
        return answer

    recurrence = item237.recurrence_polynomials()

    def defect(index):
        h = 3 * index + residue
        product = identity(15)
        answer = [0] * 15
        gauge = 1
        for shift in range(4):
            coefficient = evaluate(recurrence[shift], h) * gauge % P
            current = row_times(e_row(index + shift), product)
            answer = [(a + coefficient * b) % P for a, b in zip(answer, current)]
            product = matmul(transition(index + shift), product)
            gauge = gauge * rho(h + 3 * shift) % P
        return answer

    return transition, defect


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=HERE / "item243_defect_orbit_probe.json"
    )
    args = parser.parse_args()
    finite_rows = []
    for residue in (1, 2):
        transition, defect = system(residue)
        for initial in (3, 17, 41):
            product = identity(15)
            orbit_rows = []
            result = None
            for shift in range(21):
                orbit_rows.append(row_times(defect(initial + shift), product))
                transpose = [
                    [orbit_rows[row][column] for row in range(len(orbit_rows))]
                    for column in range(15)
                ]
                vector = linear.null_vector(transpose, P)
                if vector is not None and vector[-1]:
                    result = {"order": shift, "vector": vector}
                    break
                product = matmul(transition(initial + shift), product)
            row = {"residue": residue, "initial": initial, "result": result}
            finite_rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    payload = {
        "item": 243,
        "classification": "EXACT_FINITE_ONLY",
        "field_prime": P,
        "rows": finite_rows,
        "scope_warning": (
            "These six finite-field orbit specializations neither prove a "
            "QQ(n) recurrence nor prove leading-coefficient nonvanishing."
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
