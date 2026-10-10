#!/usr/bin/env python3
"""Discovery-only exact Q(i) nullspace recovery for the Item317 B operator."""

from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

import sympy as S
from sympy.polys.matrices import DomainMatrix


HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


item308 = load(
    "item317_exact_item308",
    HERE / "item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)


def main():
    values = []
    for s_value in range(1, 43):
        real, imag = item308.beta_coefficient(s_value)
        values.append(S.Rational(real.numerator, real.denominator) + S.I * S.Rational(
            imag.numerator, imag.denominator
        ))
    rows = []
    order, degree = 3, 7
    for offset in range(36):
        n = offset + 1
        row = []
        for shift in range(order + 1):
            for power in range(degree + 1):
                row.append(values[offset + shift] * n**power)
        rows.append(row)
    started = time.time()
    matrix = DomainMatrix.from_list_sympy(len(rows), len(rows[0]), rows).to_field()
    print("domain", matrix.domain, flush=True)
    null = matrix.nullspace()
    print("seconds", round(time.time() - started, 3), "shape", null.shape, flush=True)
    converted = null.to_Matrix()
    vector = list(converted.row(0))
    vector = [S.cancel(value / vector[-1]) for value in vector]
    polynomials = []
    for shift in range(order + 1):
        polynomial = S.factor(
            sum(vector[shift * (degree + 1) + power] * S.Symbol("s") ** power
                for power in range(degree + 1))
        )
        polynomials.append(polynomial)
        print("P", shift, polynomial, flush=True)
    for offset in range(36, len(values) - order):
        n = offset + 1
        residual = S.cancel(
            sum(polynomials[shift].subs({"s": n}) * values[offset + shift]
                for shift in range(order + 1))
        )
        print("validation", n, residual == 0, flush=True)


if __name__ == "__main__":
    main()
