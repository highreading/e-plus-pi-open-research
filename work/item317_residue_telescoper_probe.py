#!/usr/bin/env python3
"""Discovery-only continuous telescoper search for Item317's residue form."""

from __future__ import annotations

import json
import os
import time

import sympy as S


s, t = S.symbols("s t")
q = t**2 - 2 * t + 2
n0 = (
    4
    - S.Rational(4, 3) * t
    - S.Rational(8, 3) * t**2
    + S.Rational(16, 3) * t**3
    - 3 * t**4
    + t**5
)
n1 = (
    S.Rational(80, 3) * t
    - S.Rational(224, 3) * t**2
    + S.Rational(256, 3) * t**3
    - 46 * t**4
    + 10 * t**5
)

operators = [
    9
    * (2 * s + 1)
    * (6 * s + 5)
    * (6 * s + 7)
    * (6 * s + 11)
    * (6 * s + 13)
    * (660 * s**2 + 2920 * s + 3039),
    24
    * s
    * (6 * s + 11)
    * (6 * s + 13)
    * (
        1697520 * s**4
        + 10905280 * s**3
        + 24360488 * s**2
        + 22368528 * s
        + 7001703
    ),
    768
    * s
    * (s + 1)
    * (2 * s + 3)
    * (6 * s + 13)
    * (3960 * s**3 + 20820 * s**2 + 33034 * s + 14047),
    4096
    * s
    * (s + 1)
    * (s + 2)
    * (2 * s + 3)
    * (2 * s + 5)
    * (660 * s**2 + 1600 * s + 779),
]

ratio = t**3 / ((1 - t) ** 2 * q**2)
target = S.factor(
    sum(
        operators[j] * ratio**j * (n0 + (s + j) * n1)
        for j in range(4)
    )
)
log_derivative = (
    (3 * s + S.Rational(1, 2)) / t
    + (2 * s + 6) / (1 - t)
    - (2 * s + 1) * S.diff(q, t) / q
)

degree = 20
unknowns = S.symbols("c:{}".format(degree + 1))
polynomial = sum(unknowns[j] * t**j for j in range(degree + 1))
K = t * polynomial / ((1 - t) ** 5 * q**5)
equation = S.cancel(S.diff(K, t) + log_derivative * K - target)
numerator = S.Poly(equation.as_numer_denom()[0], t)
print("equation_degree", numerator.degree(), "unknowns", len(unknowns), flush=True)
started = time.time()
solution = S.solve(numerator.all_coeffs(), unknowns, dict=True, simplify=False)
print("solve_seconds", round(time.time() - started, 3), "solutions", len(solution), flush=True)
if not solution:
    raise RuntimeError("no continuous certificate")
P = S.factor(polynomial.subs(solution[0]))
print("P_degree", S.degree(P, t), "chars", len(str(P)), flush=True)
print("P_BEGIN", flush=True)
print(P, flush=True)
print("P_END", flush=True)
identity = S.cancel(
    S.diff(t * P / ((1 - t) ** 5 * q**5), t)
    + log_derivative * t * P / ((1 - t) ** 5 * q**5)
    - target
)
print("identity_zero", identity == 0, flush=True)
export_path = os.environ.get("ITEM317_EXPORT_DATA")
if export_path:
    poly_t = S.Poly(P, t)
    payload = {
        "schema": "item317_residue_telescoper_data_v1",
        "certificate_P_degree_t": int(poly_t.degree()),
        "certificate_P_degree_s": int(S.degree(P, s)),
        "certificate_P_coefficients_descending_t": [
            str(S.factor(coefficient)) for coefficient in poly_t.all_coeffs()
        ],
        "operators_factored": [str(S.factor(operator)) for operator in operators],
        "certificate_K": str(S.factor(t * P / ((1 - t) ** 5 * q**5))),
    }
    with open(export_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print("exported", export_path, flush=True)
