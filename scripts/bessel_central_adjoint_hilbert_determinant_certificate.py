#!/usr/bin/env python3
"""Exact certificate for the central adjoint/Hilbert determinant no-go."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


RESULT = Path(
    "/content/drive/MyDrive/e_pi_research_20260826/results/"
    "bessel_central_adjoint_hilbert_determinant_certificate.json"
)


def det_fraction(matrix: list[list[Fraction]]) -> Fraction:
    a = [row[:] for row in matrix]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        v = a[col][col]
        out *= v
        for j in range(col, n):
            a[col][j] /= v
        for r in range(col + 1, n):
            v = a[r][col]
            if v:
                for j in range(col, n):
                    a[r][j] -= v * a[col][j]
    return out


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    out = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        v = a[col][col]
        out = out * v % p
        inv = pow(v, -1, p)
        for j in range(col, n):
            a[col][j] = a[col][j] * inv % p
        for r in range(col + 1, n):
            v = a[r][col]
            if v:
                for j in range(col, n):
                    a[r][j] = (a[r][j] - v * a[col][j]) % p
    return out % p


def matvec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def universal_b_fraction(m: int) -> list[Fraction]:
    b = [Fraction(0), Fraction(1)]
    for r in range(1, m):
        b.append(Fraction(2 * r - 1, 2 * r + 1) * (2 * b[r] - b[r - 1]))
    return b


def universal_b_mod(m: int, p: int) -> list[int]:
    b = [0, 1]
    for r in range(1, m):
        b.append(
            (2 * r - 1)
            * pow(2 * r + 1, -1, p)
            * (2 * b[r] - b[r - 1])
            % p
        )
    return b


def t_matrix(m: int, one=1, zero=0):
    t = [[zero for _ in range(m)] for _ in range(m)]
    for r in range(m):
        t[r][r] = one * (2 * r + 1)
        if r >= 1:
            t[r][r - 1] = one * (2 - 4 * r)
        if r >= 2:
            t[r][r - 2] = one * (2 * r - 1)
    return t


def exact_small_checks() -> list[dict]:
    records = []
    for m in range(1, 9):
        b = universal_b_fraction(m)
        k = b[1 : m + 1]
        t = t_matrix(m, Fraction(1), Fraction(0))
        e0 = [Fraction(int(j == 0)) for j in range(m)]
        assert matvec(t, k) == e0

        rho = [Fraction(0) for _ in range(m)]
        if m >= 2:
            rho[m - 2] = Fraction(2 * m - 1)
        rho[m - 1] += Fraction(2 - 4 * m)
        c = [Fraction(1, j + 1) for j in range(m)]
        defect = b[m - 1] - 2 * b[m]
        beta = sum((b[r] / r for r in range(1, m + 1)), Fraction(0))
        assert sum(rho[j] * k[j] for j in range(m)) == (2 * m - 1) * defect
        assert sum(c[j] * k[j] for j in range(m)) == beta

        det_t = det_fraction(t)
        expected_det_t = Fraction(1)
        for r in range(m):
            expected_det_t *= 2 * r + 1
        assert det_t == expected_det_t

        border_rho = [t[r] + [e0[r]] for r in range(m)] + [rho + [Fraction(0)]]
        border_beta = [t[r] + [e0[r]] for r in range(m)] + [c + [Fraction(0)]]
        assert det_fraction(border_rho) == -det_t * (2 * m - 1) * defect
        assert det_fraction(border_beta) == -det_t * beta

        cauchy = [
            [Fraction(1, i + j + 2) for j in range(m)] for i in range(m)
        ]
        rform = [[2 * cauchy[i][j] for j in range(m)] for i in range(m)]
        rform[m - 1][m - 1] -= 1
        det_c = det_fraction(cauchy)
        cauchy_formula = Fraction(1)
        for i in range(m):
            for j in range(i + 1, m):
                cauchy_formula *= (j - i) ** 2
        for i in range(m):
            for j in range(m):
                cauchy_formula /= i + j + 2
        assert det_c == cauchy_formula

        binom = 1
        for r in range(1, m):
            binom = binom * (2 * m - r) // r
        inverse_bottom = (
            det_fraction([row[: m - 1] for row in cauchy[: m - 1]]) / det_c
            if m > 1
            else Fraction(1, 1) / det_c
        )
        assert inverse_bottom == 2 * m * binom**2
        det_r_formula = 2**m * det_c * (1 - m * binom**2)
        assert det_fraction(rform) == det_r_formula

        norm = sum(k[i] * rform[i][j] * k[j] for i in range(m) for j in range(m))
        a = t[1:]
        gamma = 1
        for r in range(1, m):
            gamma *= 2 * r + 1
        size = 2 * m - 1
        kkt = [[Fraction(0) for _ in range(size)] for _ in range(size)]
        for i in range(m):
            for j in range(m):
                kkt[i][j] = rform[i][j]
        for r in range(m - 1):
            for j in range(m):
                kkt[j][m + r] = a[r][j]
                kkt[m + r][j] = a[r][j]
        assert det_fraction(kkt) == (-1) ** (m - 1) * gamma**2 * norm

        records.append(
            {
                "m": m,
                "D_m": str(defect),
                "beta_m": str(beta),
                "k_R_k": str(norm),
                "det_T": str(det_t),
                "gamma": gamma,
                "C_inverse_bottom": str(inverse_bottom),
            }
        )
    return records


def modular_record(p: int) -> dict:
    m = (p - 1) // 2
    b = universal_b_mod(m, p)
    k = b[1 : m + 1]
    defect = (b[m - 1] - 2 * b[m]) % p
    beta = sum(b[r] * pow(r, -1, p) for r in range(1, m + 1)) % p

    cauchy = [[pow(i + j + 2, -1, p) for j in range(m)] for i in range(m)]
    rform = [[2 * cauchy[i][j] % p for j in range(m)] for i in range(m)]
    rform[m - 1][m - 1] = (rform[m - 1][m - 1] - 1) % p
    det_c = det_mod(cauchy, p)
    det_r = det_mod(rform, p)
    binom = 1
    for r in range(1, m):
        binom = binom * (2 * m - r) // r
    bracket = (1 - m * (binom % p) ** 2) % p
    nine_eighths = 9 * pow(8, -1, p) % p
    assert bracket == nine_eighths
    assert det_r == pow(2, m, p) * det_c * bracket % p
    assert det_r != 0

    norm = sum(k[i] * rform[i][j] * k[j] for i in range(m) for j in range(m)) % p
    j_m = sum(k[j] * pow(m + j + 1, -1, p) for j in range(m)) % p
    assert norm == (beta + (2 * m - 1) * defect * j_m) % p

    t = [[x % p for x in row] for row in t_matrix(m)]
    a = t[1:]
    gamma = 1
    for r in range(1, m):
        gamma = gamma * (2 * r + 1) % p
    size = 2 * m - 1
    kkt = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(m):
        for j in range(m):
            kkt[i][j] = rform[i][j]
    for r in range(m - 1):
        for j in range(m):
            kkt[j][m + r] = a[r][j]
            kkt[m + r][j] = a[r][j]
    det_kkt = det_mod(kkt, p)
    expected_kkt = (-1) ** (m - 1) * gamma**2 * norm % p
    assert det_kkt == expected_kkt
    if defect == 0:
        assert norm == beta

    return {
        "p": p,
        "m": m,
        "D_m": defect,
        "beta_m": beta,
        "k_R_k": norm,
        "J_m": j_m,
        "cauchy_determinant": det_c,
        "R_determinant": det_r,
        "determinant_lemma_bracket": bracket,
        "nine_eighths": nine_eighths,
        "KKT_determinant": det_kkt,
        "KKT_expected": expected_kkt,
    }


def main() -> None:
    exact = exact_small_checks()
    modular = [modular_record(p) for p in (5, 7, 11, 13, 17, 19, 79)]
    p5 = next(x for x in modular if x["p"] == 5)
    p79 = next(x for x in modular if x["p"] == 79)
    assert p5["D_m"] != 0 and p5["k_R_k"] == 0
    assert p79["D_m"] == 0 and p79["beta_m"] == 16
    assert p79["k_R_k"] == 16

    payload = {
        "claim_scope": (
            "Exact identities are proved symbolically in the source note. "
            "The finite checks here are consistency checks, not an all-prime proof."
        ),
        "exact_fraction_checks_m_1_through_8": exact,
        "modular_checks": modular,
        "adversarial_p5": {
            "description": "R is nondegenerate but the pre-resonant recurrence line is isotropic",
            "D_m": p5["D_m"],
            "k_R_k": p5["k_R_k"],
        },
        "central_root_p79": {
            "D_m": p79["D_m"],
            "beta_m": p79["beta_m"],
            "k_R_k": p79["k_R_k"],
            "KKT_determinant": p79["KKT_determinant"],
        },
        "verdict": (
            "The Cauchy determinant proves ambient nondegeneracy. "
            "Conditional on resonance, the one-line restricted determinant is beta_m itself."
        ),
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(RESULT)


if __name__ == "__main__":
    main()
