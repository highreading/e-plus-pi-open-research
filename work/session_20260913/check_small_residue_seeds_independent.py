"""Independent exact seed certificate, ONLY k=0..6 and requested primes.

No factorization or large-degree approximant is computed.
MD uses a factorial-normalized Appell Wronskian.
b uses integer derivative constraints at 1 and primitive cofactors.
V uses S/W coefficient reconstruction.
Pe uses the original Qhat times truncated exponential.
"""
from fractions import Fraction
from functools import reduce
from math import comb, factorial, gcd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
PRIMES = (3, 5, 7, 11, 13)


def falling(a, b):
    return factorial(a) // factorial(a - b) if 0 <= b <= a else 0


def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, last = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % last == 0
                a[i][j] = numerator // last
        for i in range(k + 1, n):
            a[i][k] = 0
        last = pivot
    return sign * a[-1][-1]


def divide_monic(num, den):
    a = [Fraction(x) for x in num]
    d = len(den) - 1
    assert den[-1] == 1
    q = [Fraction(0)] * (len(a) - d)
    for j in range(len(a) - 1, d - 1, -1):
        q[j - d] = a[j]
        for i in range(d + 1):
            a[j - d + i] -= q[j - d] * den[i]
    assert all(x == 0 for x in a)
    return q


def seed(k):
    if k == 0:
        return dict(k=0, MD=1, b=[1], V=[1], V1=1, Pe1=1,
                    constraint_rank_certificate=1)
    appell = [
        sum(comb(k, h) * falling(d, 2*h) for h in range(d//2 + 1))
        for d in range(2*k + 1)
    ]
    wronskian = [
        [falling(d, j) * appell[d-j] for j in range(k + 1)]
        for d in range(k, 2*k + 1)
    ]
    vandermonde = 1
    for i in range(k + 1):
        for j in range(i + 1, k + 1):
            vandermonde *= j - i
    wd = det_bareiss(wronskian)
    assert wd % vandermonde == 0
    MD = wd // vandermonde
    assert MD

    constraints = [
        [sum(comb(k, h) * falling(k+j, i+2*h)
             for h in range(k + 1)) for j in range(k + 1)]
        for i in range(k)
    ]
    cofactors = [
        (-1)**j * det_bareiss(
            [[row[c] for c in range(k + 1) if c != j]
             for row in constraints])
        for j in range(k + 1)
    ]
    content = reduce(gcd, map(abs, cofactors))
    assert content > 0
    b = [x // content for x in cofactors]
    assert all(sum(x*y for x, y in zip(row, b)) == 0
               for row in constraints)

    U = [factorial(k+j)*b[j] for j in range(k + 1)]
    S = [0] * (3*k + 1)
    for h in range(k + 1):
        for j in range(k + 1):
            S[j+2*h] += comb(k, h)*U[j]
    W_over_tk = [Fraction(S[k+r], factorial(r))
                 for r in range(2*k + 1)]
    assert all(x.denominator == 1 for x in W_over_tk)
    V = divide_monic(
        W_over_tk, [(-1)**(k-j)*comb(k, j) for j in range(k+1)])
    assert all(x.denominator == 1 for x in V)
    V = [int(x) for x in V]
    assert reduce(gcd, map(abs, V)) == 1
    V1 = sum(V)
    assert V1
    orientation = 1 if V1 * MD > 0 else -1
    b = [orientation*x for x in b]
    V = [orientation*x for x in V]
    S = [orientation*x for x in S]
    V1 *= orientation

    Q = [comb(3*k-j, k)*S[3*k-j] for j in range(2*k+1)]
    Pe_coeff = [sum((Fraction(Q[j], factorial(r-j))
                     for j in range(r+1)), Fraction(0))
                for r in range(2*k+1)]
    assert all(x.denominator == 1 for x in Pe_coeff)
    Pe1 = int(sum(Pe_coeff))
    return dict(k=k, MD=MD, b=b, V=V, V1=V1, Pe1=Pe1,
                Qhat=Q, Pe_coefficients=[int(x) for x in Pe_coeff],
                constraint_rank_certificate=content)


calculated = [seed(k) for k in range(7)]
atlas = json.loads((BASE / "small_residue_exact_seeds.json").read_text())
atlas_by_k = {row["k"]: row for row in atlas["seeds"]}
checks = []
for row in calculated:
    reference = atlas_by_k[row["k"]]
    for field in ("MD", "b", "V", "V1", "Pe1"):
        assert row[field] == reference[field], (row["k"], field)
    for p in PRIMES:
        if 2*row["k"] >= p:
            continue
        md, pe = row["MD"] % p, row["Pe1"] % p
        checks.append(dict(p=p, k=row["k"], MD_mod_p=md,
                           Pe_mod_p=pe, V1_mod_p=row["V1"] % p,
                           seed_gate_unit=bool(md and pe)))

good = {str(p): [row["k"] for row in checks
                if row["p"] == p and row["seed_gate_unit"]]
        for p in PRIMES}
base_good = {str(p): sorted(set(good[str(p)]) | {0, p-1}
                           | ({1} if p != 5 else set()))
             for p in PRIMES}
out = dict(
    scope="Only k=0..6, p in3,5,7,11,13, and2k<p; no factorization.",
    methods=["integer Appell Wronskian",
             "primitive integer derivative-constraint kernel",
             "S/W coefficient reconstruction",
             "Qhat times truncated exponential"],
    atlas_fields_independently_equal=["MD", "b", "V", "V1", "Pe1"],
    exact_seeds=calculated, modular_checks=checks,
    positive_good_residues=good,
    good_with_reviewed_zero_plusminus_one=base_good,
    theorem_dependency="Positive-residue transfer: FULL PASS in raw_positive_residue_transfer_independent_review.md.",
    status="PASS")
path = BASE / "small_residue_seeds_independent_certificate.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(dict(modular_checks=checks,
                      positive_good_residues=good,
                      combined_good_residues=base_good), indent=2))
print("PASS:", path)
