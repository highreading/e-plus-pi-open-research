"""Independent modular controls for selected already-declared seeds.

No factorization and no extension of the fixed seed degree range 0..6.
Uses normalized integer Appell Wronskians, a polynomial differential
identity, and an independent truncated-Q exponential endpoint.
"""
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).parent
ATLAS = {r["k"]: r for r in json.loads((ROOT / "small_residue_exact_seeds.json").read_text())["seeds"]}
PAIRS = [(1, 5), (2, 5), (2, 7), (3, 7), (3, 13), (4, 11), (5, 11), (6, 13)]

def falling(a, b):
    return factorial(a) // factorial(a-b) if a >= b else 0

def det_mod(a, p):
    a = [row[:] for row in a]
    out = 1
    for j in range(len(a)):
        piv = next((i for i in range(j, len(a)) if a[i][j] % p), None)
        if piv is None:
            return 0
        if piv != j:
            a[j], a[piv] = a[piv], a[j]
            out = -out
        u = a[j][j] % p
        out = out*u % p
        inv = pow(u, -1, p)
        for i in range(j+1, len(a)):
            v = a[i][j]*inv % p
            for k in range(j, len(a)):
                a[i][k] = (a[i][k]-v*a[j][k]) % p
    return out % p

def augmented_wronskian(degrees, k, p):
    if not degrees:
        return 1
    matrix = [[sum(comb(k, h)*falling(d, 2*h)*falling(d-2*h, j)
                   for h in range(min(k, d//2)+1)) % p
               for j in range(len(degrees))] for d in degrees]
    vand = 1
    for i in range(len(degrees)):
        for j in range(i+1, len(degrees)):
            vand = vand*(degrees[j]-degrees[i]) % p
    assert vand != 0
    return det_mod(matrix, p)*pow(vand, -1, p) % p

def convolution(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    return c

def monic_division(a, b, p):
    r = [x % p for x in a]
    out = [0]*(len(a)-len(b)+1)
    for j in range(len(out)-1, -1, -1):
        out[j] = r[j+len(b)-1]
        for h in range(len(b)):
            r[j+h] = (r[j+h]-out[j]*b[h]) % p
    assert all(x == 0 for x in r)
    return out

rows = []
for k, p in PAIRS:
    assert 2*k < p
    degrees = list(range(k, 2*k+1))
    md = augmented_wronskian(degrees, k, p)
    ms = [augmented_wronskian([d for d in degrees if d != 2*k-j], k, p)
          for j in range(k+1)]
    assert md == ATLAS[k]["MD"] % p
    assert ms == [x % p for x in ATLAS[k]["M"]]
    b = [((-1)**(k-j)*comb(k, j)*ms[k-j]) % p for j in range(k+1)]
    assert b == [x % p for x in ATLAS[k]["b"]]

    # Differential reconstruction: (t-1)^k V=(1+D^2)^k(t^k b).
    rhs = [0]*(2*k+1)
    for j, bj in enumerate(b):
        for h in range(k+1):
            d = k+j-2*h
            if d >= 0:
                rhs[d] = (rhs[d]+comb(k, h)*falling(k+j, 2*h)*bj) % p
    den = [((-1)**(k-j)*comb(k, j)) % p for j in range(k+1)]
    v = monic_division(rhs, den, p)
    assert v == [x % p for x in ATLAS[k]["V"]]
    assert sum(v) % p == md
    pe_border = sum(v[r]*sum(comb(k+j, j)*falling(k+r, j)
                            for j in range(k+r+1))
                    for r in range(k+1)) % p

    # Independently reconstruct Q from U and S, then truncate Q exp.
    u = [(factorial(k+j)*b[j]) % p for j in range(k+1)]
    dpoly = [comb(k, j//2) % p if j % 2 == 0 else 0 for j in range(2*k+1)]
    s = convolution(u, dpoly, p)
    q = [0]*(2*k+1)
    for degree in range(k, 3*k+1):
        q[3*k-degree] = comb(degree, k)*s[degree] % p
    pe_trunc = sum(q[j]*sum(pow(factorial(h), -1, p)
                           for h in range(2*k-j+1))
                   for j in range(2*k+1)) % p
    assert pe_border == pe_trunc == ATLAS[k]["Pe1"] % p
    rows.append({"k": k, "p": p, "MD_mod_p": md, "M_mod_p": ms,
                 "b_mod_p": b, "V_mod_p": v, "Pe_border_mod_p": pe_border,
                 "Pe_truncated_Q_exp_mod_p": pe_trunc,
                 "unit_seed": bool(md and pe_border), "all_checks_pass": True})

out = {"scope": "Selected modular verification of fixed existing seed atlas; no factorization or extended degree scan.",
       "pairs": PAIRS, "checks": rows, "all_checks_pass": True}
(ROOT / "positive_residue_selected_seeds_independent_checks.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
