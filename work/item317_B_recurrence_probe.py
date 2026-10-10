#!/usr/bin/env python3
"""Discovery-only modular recurrence search for Item317's Gaussian B_s."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


item308 = load(
    "item317_item308",
    HERE / "item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)


P = 998244353
I = pow(3, (P - 1) // 4, P)
if os.environ.get("ITEM317_CONJUGATE") == "1":
    I = -I % P
assert I * I % P == P - 1


def qmod(value):
    return value.numerator % P * pow(value.denominator % P, P - 2, P) % P


def bmod(s):
    real, imag = item308.beta_coefficient(s)
    return (qmod(real) + I * qmod(imag)) % P


def nullspace_vector(matrix):
    if not matrix:
        return None
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivots = []
    row = 0
    for col in range(cols):
        pivot = next((r for r in range(row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inverse = pow(a[row][col], P - 2, P)
        a[row] = [value * inverse % P for value in a[row]]
        for r in range(rows):
            if r != row and a[r][col]:
                scale = a[r][col]
                a[r] = [
                    (left - scale * right) % P
                    for left, right in zip(a[r], a[row])
                ]
        pivots.append(col)
        row += 1
        if row == rows:
            break
    if len(pivots) == cols:
        return None
    free = next(col for col in range(cols) if col not in pivots)
    vector = [0] * cols
    vector[free] = 1
    for r in range(len(pivots) - 1, -1, -1):
        pivot = pivots[r]
        vector[pivot] = -sum(
            a[r][col] * vector[col] for col in range(pivot + 1, cols)
        ) % P
    return vector


def search(values, max_order=12, max_degree=20):
    for order in range(1, max_order + 1):
        for degree in range(0, max_degree + 1):
            columns = (order + 1) * (degree + 1)
            available = len(values) - order
            if available < columns + 5:
                continue
            matrix = []
            for offset in range(available):
                n = offset + 1
                row = []
                for shift in range(order + 1):
                    power = 1
                    for _ in range(degree + 1):
                        row.append(values[offset + shift] * power % P)
                        power = power * n % P
                matrix.append(row)
            vector = nullspace_vector(matrix)
            if vector is not None:
                print("FOUND", order, degree, vector, flush=True)
                return order, degree, vector
        print("order_done", order, flush=True)
    return None


def main():
    count = int(os.environ.get("ITEM317_ROWS", "120"))
    values = []
    for s in range(1, count + 1):
        values.append(bmod(s))
        if s % 10 == 0:
            print("rows", s, flush=True)
    print("searching", flush=True)
    print(search(values), flush=True)


if __name__ == "__main__":
    main()
