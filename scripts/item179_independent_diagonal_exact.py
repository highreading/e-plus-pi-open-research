from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

sys.set_int_max_str_digits(0)


def falling(k: int, j: int) -> int:
    return 0 if j > k else math.factorial(k) // math.factorial(k - j)


def tau(k: int) -> int:
    if k == 0 or k % 4 == 0:
        return 0
    q, r = divmod(k, 4)
    if r in (1, 2):
        return (-1) ** q * 2 * math.factorial(k - 1) // 4**q
    return (-1) ** q * math.factorial(k - 1) // 4**q


def primitive(vec) -> list[int]:
    entries = list(vec)
    den = math.lcm(*[x.denominator for x in entries])
    out = [int(x * den) for x in entries]
    g = reduce(gcd, [abs(x) for x in out if x])
    out = [x // g for x in out]
    if next(x for x in out if x) < 0:
        out = [-x for x in out]
    return out


def high_matrix(n: int, maximal: bool) -> list[list[int]]:
    rows = []
    stop = 3 * n + (2 if maximal else 1)
    for k in range(n + 1, stop):
        rows.append(
            [falling(k, j) for j in range(n + 1)]
            + [falling(k, j) * tau(k - j) for j in range(n + 1)]
        )
    if not maximal:
        rows.append([-1] * (n + 1) + [1] * (n + 1))
    return rows


def null_vector(matrix: list[list[int]]) -> tuple[list[Fraction], int]:
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivots: list[int] = []
    prow = 0
    for col in range(cols):
        pivot = next((r for r in range(prow, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[prow], a[pivot] = a[pivot], a[prow]
        pv = a[prow][col]
        a[prow] = [x / pv for x in a[prow]]
        for r in range(prow + 1, rows):
            if a[r][col]:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[prow])]
        pivots.append(col)
        prow += 1
        if prow == rows:
            break
    free = [c for c in range(cols) if c not in pivots]
    if len(free) != 1:
        raise ValueError((rows, cols, prow, free))
    v = [Fraction(0) for _ in range(cols)]
    v[free[0]] = 1
    for r in range(prow - 1, -1, -1):
        col = pivots[r]
        v[col] = -sum(a[r][j] * v[j] for j in range(col + 1, cols))
    return v, prow


def bareiss_det(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def val2(x: int) -> int:
    x = abs(x)
    return 0 if x == 0 else (x & -x).bit_length() - 1


def reconstruct(n: int, bc: list[int]) -> tuple[list[int], int, int]:
    b, c = bc[: n + 1], bc[n + 1 :]
    a = []
    for k in range(n + 1):
        jet = sum(
            falling(k, j) * (b[j] + tau(k - j) * c[j])
            for j in range(k + 1)
        )
        a.append(Fraction(-jet, math.factorial(k)))
    den = math.lcm(*[x.denominator for x in a])
    raw = [int(den * x) for x in a] + [den * x for x in b] + [den * x for x in c]
    g = reduce(gcd, [abs(x) for x in raw if x])
    raw = [x // g for x in raw]
    if next(x for x in raw if x) < 0:
        raw = [-x for x in raw]
    return raw, den, g


def derivative(n: int, triple: list[int], k: int) -> int:
    b = triple[n + 1 : 2 * n + 2]
    c = triple[2 * n + 2 :]
    return sum(falling(k, j) * (b[j] + tau(k - j) * c[j]) for j in range(n + 1))


def one(n: int, maximal: bool) -> dict:
    m = high_matrix(n, maximal)
    ns, rank = null_vector(m)
    bc = primitive(ns)
    tri, reconstruction_denominator, full_triple_gcd = reconstruct(n, bc)
    a = tri[: n + 1]
    b = tri[n + 1 : 2 * n + 2]
    c = tri[2 * n + 2 :]
    first = 3 * n + (2 if maximal else 1)
    endpoint = [sum(a), sum(b), sum(c)]
    compatibility_det = None
    if maximal:
        square = m + [[-1] * (n + 1) + [1] * (n + 1)]
        compatibility_det = bareiss_det(square)
    return {
        "n": n,
        "maximal": maximal,
        "matrix_shape": [len(m), len(m[0])],
        "rank": rank,
        "endpoint_A_B_C": endpoint,
        "endpoint_mismatch_B_minus_C": endpoint[1] - endpoint[2],
        "compatibility_determinant": compatibility_det,
        "compatibility_determinant_v2": None if compatibility_det is None else val2(compatibility_det),
        "first_free_index": first,
        "first_free_derivative": derivative(n, tri, first),
        "exact_normalization": "primitive integral full triple; first nonzero coefficient positive",
        "primitive_BC_before_A_reconstruction": bc,
        "A_reconstruction_lcm_denominator": reconstruction_denominator,
        "full_triple_gcd_before_final_reduction": full_triple_gcd,
        "endpoint_denominator_after_final_reduction": 1,
        "triple_height_digits": len(str(max(abs(x) for x in tri))),
        "triple": tri,
    }


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=12)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    obj = {
        "maximal_independent": [one(n, True) for n in range(1, args.nmax + 1)],
        "endpoint_matched": [one(n, False) for n in range(1, args.nmax + 1)],
    }
    args.output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
