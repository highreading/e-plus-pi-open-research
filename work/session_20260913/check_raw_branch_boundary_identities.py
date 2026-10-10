"""Closed symbolic controls of boundary determinant and Green identities.

Uses only sizes 2,3,4 and generic symbolic band coefficients. This is
not a new root diagnostic, HP degree construction, or asymptotic probe.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "math_packages"))
import sympy as s

x, y, seed = s.symbols("x y seed")
aa = [s.Integer(0)] + list(s.symbols("a1:6", nonzero=True))
dd = list(s.symbols("d0:4"))


def band(i, j):
    if i == j:
        return dd[i]
    if abs(i-j) == 1:
        return -aa[max(i,j)]
    if abs(i-j) == 2:
        return aa[min(i,j)+1] * aa[min(i,j)+2]
    return s.Integer(0)


def rows(z):
    rr = [s.Matrix([[1, 0]]), s.Matrix([[seed, 1]])]
    for j in range(3):
        val = (z-dd[j])*rr[j] + aa[j+1]*rr[j+1]
        if j >= 1:
            val += aa[j]*rr[j-1]
        if j >= 2:
            val -= aa[j]*aa[j-1]*rr[j-2]
        rr.append(val/(aa[j+1]*aa[j+2]))
    return rr


def zero_matrix(M):
    return all(s.cancel(v) == 0 for v in M)


rx, ry = rows(x), rows(y)
checks = []
for N in (2, 3):
    K = s.Matrix(N, N, band)
    P = s.Matrix.vstack(rx[N], rx[N+1])
    prod = s.prod(aa[j+1]*aa[j+2] for j in range(N))
    assert s.cancel((K-x*s.eye(N)).det()-prod*P.det()) == 0
    checks.append({"identity": "adjacent Casoratian", "size": N, "passed": True})

    Gamma = s.Matrix([[aa[N-1]*aa[N], 0], [-aa[N], aa[N]*aa[N+1]]])
    Ex = s.Matrix.vstack(rx[N-2], rx[N-1])
    Ey = s.Matrix.vstack(ry[N-2], ry[N-1])
    Py = s.Matrix.vstack(ry[N], ry[N+1])
    W = Ex.T*Gamma*Py-P.T*Gamma.T*Ey
    G = s.zeros(2)
    for j in range(N):
        G += rx[j].T*ry[j]
    assert zero_matrix(W-(y-x)*G)
    checks.append({"identity": "matrix Green form", "size": N, "passed": True})

for k in (3, 4):
    top = s.Matrix(k-1, k, lambda i,j: band(i,j)-(x if i == j else 0))
    prod = s.prod(aa[j+1]*aa[j+2] for j in range(k-1))
    for branch, bnd, sign in (
        (0, [-seed, 1]+[0]*(k-2), -1),
        (1, [1]+[0]*(k-1), 1),
    ):
        M = s.Matrix.vstack(top, s.Matrix([bnd]))
        assert s.cancel(M.det()-sign*prod*rx[k][branch]) == 0
        checks.append({"identity": "individual boundary pencil", "size": k,
                       "branch": branch, "passed": True})

out = {"scope": "Generic symbolic identities only; no root or HP scan.",
       "checks": checks}
(HERE / "raw_branch_boundary_identity_checks.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
