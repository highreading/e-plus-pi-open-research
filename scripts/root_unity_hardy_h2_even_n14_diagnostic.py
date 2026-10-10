#!/usr/bin/env python3
"""Exact even-parity saturation plus H2 quotient diagnostic at n=14."""

import itertools
import json
import math
import sys

import mpmath as mp
import sympy as sp

ROOT = "/content/drive/MyDrive/e_pi_research_20260826/scripts"
sys.path.insert(0, ROOT)
import root_unity_gaussian_global_saturation_certificate as gg
import root_unity_hardy_h2_saturated_circle_certificate as h


def context(m, n, D):
    M = m * (n + 1)
    moments = gg.nd.logistic_moments(M + n + 10)
    interpolation, beta, labels = gg.nd.interpolation_data(m, n, D, moments)
    Q = gg.nd.universal_Q(m, n)
    corrected = gg.nd.corrected_Q_map(beta, Q, n, D)
    pairs = list(itertools.combinations(range(D + 1), 2))
    rem = gg.nd.cleared_remainders(
        m, n, D, Q, interpolation, labels, sp.eye(D + 1)
    )
    rows = []
    for first, second in pairs:
        pair = gg.nd.exp_wronskian(rem[first], rem[second])
        rows.append([value for freq in pair for value in freq])
    return {
        "m": m,
        "n": n,
        "D": D,
        "nu": D + 1,
        "M": M,
        "Q": Q,
        "corrected_map": corrected,
        "pairs": pairs,
        "global_map": sp.Matrix(rows),
    }


def hardy_object(n, D, basis):
    obj = h.SaturatedHardyRow.__new__(h.SaturatedHardyRow)
    obj.m = 2
    obj.n = n
    obj.target_degree = 2
    obj.D = D
    obj.nu = D + 1
    obj.M = 2 * (n + 1)
    obj.zero_order = 2 * obj.M
    obj.global_degree = 2 * n
    obj.basis = basis
    obj.rank = basis.nrows()
    obj.slot_count = basis.ncols()
    obj.endpoint_matrix = gg.k2.endpoint_rows(basis, obj.m, n)
    assert all(
        obj.endpoint_matrix[r, d] == 0
        for r in range(obj.rank)
        for d in range(1, obj.endpoint_matrix.cols, 2)
    )
    assert all(
        obj.endpoint_matrix[r, d] == 0
        for r in range(obj.rank)
        for d in range(3, obj.endpoint_matrix.cols)
    )
    assert int(obj.endpoint_matrix[:, [0, 2]].rank()) == 2
    obj.scales = [
        max(abs(int(basis[r, c])) for c in range(obj.slot_count))
        for r in range(obj.rank)
    ]
    obj.row_squared_norms = [
        sum(int(basis[r, c]) ** 2 for c in range(obj.slot_count))
        for r in range(obj.rank)
    ]
    maximum = obj.zero_order + h.DERIVATIVE_TAIL
    facts = [math.factorial(j) for j in range(maximum + 1)]
    obj.origin_derivatives = []
    digits = 0
    for r in range(obj.rank):
        derivatives = []
        for order in range(maximum + 1):
            terms = []
            for freq in range(2 * obj.m + 1):
                rate = freq - obj.m
                offset = freq * (obj.global_degree + 1)
                for degree in range(min(obj.global_degree, order) + 1):
                    coefficient = int(basis[r, offset + degree])
                    if coefficient:
                        terms.append(
                            coefficient
                            * facts[order]
                            // facts[order - degree]
                            * rate ** (order - degree)
                        )
            value = sum(terms)
            if order < obj.zero_order and terms:
                digits = max(digits, len(str(max(abs(x) for x in terms))))
            derivatives.append(value)
        assert all(x == 0 for x in derivatives[: obj.zero_order])
        assert any(derivatives[obj.zero_order :])
        obj.origin_derivatives.append(derivatives)
    obj.exact_zero_cancellation_summand_decimal_digits = digits
    obj.endpoint_basis = mp.matrix(obj.rank, 2)
    for r in range(obj.rank):
        obj.endpoint_basis[r, 0] = (
            mp.mpf(int(obj.endpoint_matrix[r, 0])) / obj.scales[r]
        )
        obj.endpoint_basis[r, 1] = (
            mp.mpf(int(obj.endpoint_matrix[r, 2])) / obj.scales[r]
        )
    return obj


def main():
    h.RSS_LIMIT_KIB = 12 * 1024 * 1024
    mp.mp.dps = h.WORK_DPS
    n, D = 14, 7
    ctx = context(2, n, D)
    even = gg.parity_block(ctx, 2, 0)
    obj = hardy_object(n, D, even["saturated_lll"])
    rows = []
    for label, index, endpoint in obj.endpoint_choices():
        rows.append(h.endpoint_diagnostic(obj, label, index, endpoint))
    print(json.dumps({"rank": obj.rank, "D": D, "n": n, "rows": rows},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

