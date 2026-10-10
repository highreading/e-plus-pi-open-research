"""Independent exact all-residue verification at the fixed primes 23,43.

No import from the source checker. Determinants use integer Bareiss on
Jacobi--Trudi matrices; positive endpoints use Q times truncated exp;
negative endpoints use the original positive-index upper tail and a
Taylor polynomial with the required jets. No factorization or actual
large-degree approximant is constructed.
"""
from math import comb, factorial
from pathlib import Path
from functools import lru_cache
import hashlib
import json

BASE = Path(__file__).parent
PRIMES = (23, 43)
source_path = BASE / "raw_predeclared_residue_seed_atlas.json"
source_bytes = source_path.read_bytes()
source = {row["p"]: row for row in json.loads(source_bytes)["atlas"]}

def det_bareiss(mat):
    n = len(mat)
    if n == 0:
        return 1
    a = [row[:] for row in mat]
    sign, previous = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
        for i in range(k+1, n):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]

def ff(n, r):
    v = 1
    for j in range(r):
        v *= n-j
    return v

def rf(n, r):
    v = 1
    for j in range(r):
        v *= n+j
    return v

@lru_cache(None)
def aug(partition, background, p):
    if not partition:
        return 1
    size = len(partition)
    bound = partition[0]+size-1
    assert bound < p
    b = background % p
    complete = [sum(comb(b, h)*pow(factorial(d-2*h), -1, p)
                    for h in range(d//2+1)) % p
                for d in range(bound+1)]
    matrix = [[complete[partition[i]-i+j] if partition[i]-i+j >= 0 else 0
               for j in range(size)] for i in range(size)]
    hook = 1
    for i, width in enumerate(partition):
        for j in range(width):
            arm = width-j-1
            leg = sum(other > j for other in partition[i+1:])
            hook *= arm+leg+1
    assert hook % p
    return det_bareiss(matrix)*hook % p

def conv(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    return c

def endpoint_border(n, j, p):
    return sum(comb(n+s, s)*ff(n+j, s) for s in range(n+j+1)) % p

def positive(k, p):
    if k == 0:
        return dict(D=1, E=1, C=[1])
    D = aug((k,)*(k+1), k, p)
    C = [aug((k+1,)*j+(k,)*(k-j), k, p) for j in range(k+1)]
    B = [(-1)**(k-j)*comb(k, j)*C[k-j] % p for j in range(k+1)]
    U = [factorial(k+j)*B[j] % p for j in range(k+1)]
    dpoly = [comb(k, j//2) if j % 2 == 0 else 0 for j in range(2*k+1)]
    S = conv(U, dpoly, p)
    Q = [0]*(2*k+1)
    for degree in range(k, 3*k+1):
        Q[3*k-degree] = comb(degree, k)*S[degree] % p
    E = sum(Q[j]*sum(pow(factorial(h), -1, p) for h in range(2*k-j+1))
            for j in range(2*k+1)) % p
    return dict(D=D, E=E, C=C, scaled_B=B, scaled_Q=Q)

def negative(k, p):
    if k == 0:
        return dict(D=1, E=1, C=[1], source="reviewed n+1 unit theorem")
    r = p-k-1
    D = aug((k,)*(k+1), -k-1, p)
    C = [aug((k+1,)*(k-i)+(k,)*i, -k-1, p) for i in range(k+1)]
    low_b = [(-1)**(r-i)*comb(r, i)*C[i] % p for i in range(k+1)]
    low_w = [sum(comb(r, u)*rf(r+i+1, 2*u)*low_b[i+2*u]
                 for u in range((k-i)//2+1)) % p for i in range(k+1)]
    jets = [factorial(h)*sum(comb(r+i, r+h)*low_w[i]
                            for i in range(h, k+1)) % p for h in range(k+1)]
    assert jets[0] == D
    # Degree-k Taylor representative at t=1 has exactly the needed jets.
    toy_v = [sum(jets[h]*pow(factorial(h), -1, p)*comb(h, j)*(-1)**(h-j)
                 for h in range(j, k+1)) % p for j in range(k+1)]
    # This is the original border at r, with its full finite summation;
    # no negative-binomial endpoint formula is used.
    E = sum(toy_v[j]*endpoint_border(r, j, p) for j in range(k+1)) % p
    return dict(D=D, E=E, C=C, low_b=low_b, low_w=low_w, J=jets,
                Taylor_representative=toy_v)

certificates = []
for p in PRIMES:
    original = {row["residue"]: row for row in source[p]["classes"]}
    assert set(original) == set(range(p))
    rows = []
    for residue in range(p):
        if residue <= (p-1)//2:
            branch, k = "positive", residue
            row = positive(k, p)
        else:
            branch, k = "negative", p-1-residue
            row = negative(k, p)
        expected = original[residue]
        assert (branch, k) == (expected["branch"], expected["k"])
        assert row["D"] == expected["D"]
        assert row["C"] == expected["C"]
        assert row["E"] == expected["E"]
        if branch == "negative" and k:
            assert row["J"] == expected["J"]
        assert row["D"] != 0 and row["E"] != 0
        row.update(residue=residue, branch=branch, k=k,
                   endpoint_over_V1=row["E"]*pow(row["D"], -1, p) % p,
                   all_source_values_match=True, both_seeds_units=True)
        rows.append(row)
    certificates.append(dict(p=p, residue_count=len(rows), all_residues_verified=True,
                             classes=rows))

payload = dict(scope="All residues at the two fixed primes 23 and43, using independent exact algorithms.",
               source_sha256=hashlib.sha256(source_bytes).hexdigest(),
               primes=list(PRIMES), all_checks_pass=True, atlas=certificates)
(BASE / "uniform_23_43_independent_certificate.json").write_text(json.dumps(payload, indent=2)+"\n")
print(json.dumps([dict(p=row["p"], residue_count=row["residue_count"],
                       all_residues_verified=row["all_residues_verified"],
                       D=[c["D"] for c in row["classes"]],
                       E=[c["E"] for c in row["classes"]])
                  for row in certificates], indent=2))
