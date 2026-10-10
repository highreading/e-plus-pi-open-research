"""Independent all-residue modular certificate for assigned primes 101,109.

One transposed Jacobi--Trudi matrix and its first inverse column produce
all hook-normalized cofactors. No import from the source seed checker.
Positive endpoints use original S -> Q -> truncated exp; negative endpoints
use the original positive-index tail and full positive-index endpoint border.
"""
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).parent
PRIMES = (101, 109)
source_path = BASE / "raw_third_predeclared_uniform_seed_certificate.json"
source_bytes = source_path.read_bytes()
source = {row["p"]: row for row in json.loads(source_bytes)["results"]}


def det_solve_jordan(matrix, rhs, p):
    """Gauss--Jordan, unit pivots; verify original equation exactly."""
    n = len(matrix)
    aug = [[v % p for v in row]+[rhs[i] % p]
           for i, row in enumerate(matrix)]
    determinant = 1
    steps = []
    for j in range(n):
        row = next((i for i in range(j, n) if aug[i][j]), None)
        if row is None:
            return 0, None, steps
        if row != j:
            aug[row], aug[j] = aug[j], aug[row]
            determinant = -determinant
        pivot = aug[j][j]
        determinant = determinant*pivot % p
        steps.append([j, row, pivot])
        inv = pow(pivot, -1, p)
        aug[j] = [v*inv % p for v in aug[j]]
        for i in range(n):
            if i != j:
                mult = aug[i][j]
                if mult:
                    aug[i] = [(u-mult*v) % p for u, v in zip(aug[i], aug[j])]
    solution = [row[-1] for row in aug]
    assert all(aug[i][j] == (i == j) for i in range(n) for j in range(n))
    residual = [(sum(row[j]*solution[j] for j in range(n))-rhs[i]) % p
                for i, row in enumerate(matrix)]
    assert residual == [0]*n
    return determinant, solution, steps


def hook(partition, p):
    ans = 1
    for i, width in enumerate(partition):
        for j in range(width):
            length = width-j+sum(other > j for other in partition[i+1:])
            assert 1 <= length < p
            ans = ans*length % p
    return ans


def ff(n, r):
    ans = 1
    for j in range(r):
        ans *= n-j
    return ans


def rf(n, r):
    ans = 1
    for j in range(r):
        ans *= n+j
    return ans


def convolution(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] = (out[i+j]+u*v) % p
    return out


def full_and_cofactors(k, b, p):
    assert 1 <= k and 2*k < p
    complete = [sum(comb(b % p, u)*pow(factorial(d-2*u), -1, p)
                    for u in range(d//2+1)) % p for d in range(2*k+1)]
    # The transpose of ordinary Jacobi--Trudi for (k^(k+1)).
    matrix = [[complete[k+i-j] for j in range(k+1)] for i in range(k+1)]
    determinant, column, pivots = det_solve_jordan(matrix, [1]+[0]*k, p)
    assert determinant and column is not None
    full_hook = hook((k,)*(k+1), p)
    D = full_hook*determinant % p
    hooks = [hook((k+1,)*(k-i)+(k,)*i, p) for i in range(k+1)]
    # Delete row0 and column(k-i); its transpose is JT(gamma_i).
    C = [hooks[i]*(-1)**(k-i)*determinant*column[k-i] % p
         for i in range(k+1)]
    # Two direct cofactor determinants check both endpoint orientations.
    # They are not used to produce C.
    direct = []
    for i in (0, k):
        deleted = k-i
        minor = [[matrix[row][col] for col in range(k+1) if col != deleted]
                 for row in range(1, k+1)]
        md, _, _ = det_solve_jordan(minor, [0]*k, p)
        assert hooks[i]*md % p == C[i]
        direct.append(dict(index=i, direct_JT_minor=md, value=C[i]))
    certificate = dict(complete_coefficients=complete, determinant=determinant,
                       inverse_first_column=column, full_hook=full_hook,
                       cofactor_hooks=hooks, elimination_pivots=pivots,
                       matrix_sha256=hashlib.sha256(json.dumps(matrix).encode()).hexdigest(),
                       inverse_residual_zero=True, direct_edge_minors=direct)
    return D, C, certificate


def positive(k, p):
    if not k:
        return dict(D=1, E=1, C=[1], source="reviewed empty positive seed")
    D, C, matrix_certificate = full_and_cofactors(k, k, p)
    B = [(-1)**(k-j)*comb(k, j)*C[j] % p for j in range(k+1)]
    U = [factorial(k+j)*B[j] % p for j in range(k+1)]
    dpoly = [comb(k, j//2) if j % 2 == 0 else 0 for j in range(2*k+1)]
    S = convolution(U, dpoly, p)
    Q = [0]*(2*k+1)
    for d in range(k, 3*k+1):
        Q[3*k-d] = comb(d, k)*S[d] % p
    E = sum(Q[j]*sum(pow(factorial(h), -1, p) for h in range(2*k-j+1))
            for j in range(2*k+1)) % p
    return dict(D=D, E=E, C=C, scaled_B=B, scaled_Q=Q,
                matrix_certificate=matrix_certificate)


def endpoint_border(r, j, p):
    return sum(comb(r+s, s)*ff(r+j, s) for s in range(r+j+1)) % p


def negative(k, p):
    if not k:
        return dict(D=1, E=1, C=[1], source="reviewed n+1 unit theorem")
    D, C, matrix_certificate = full_and_cofactors(k, -k-1, p)
    r = p-k-1
    low_b = [(-1)**(r-i)*comb(r, i)*C[i] % p for i in range(k+1)]
    low_w = [sum(comb(r, u)*rf(r+i+1, 2*u)*low_b[i+2*u]
                 for u in range((k-i)//2+1)) % p for i in range(k+1)]
    J = [factorial(h)*sum(comb(r+i, r+h)*low_w[i]
                         for i in range(h, k+1)) % p for h in range(k+1)]
    assert J[0] == D
    toy_v = [sum(J[h]*pow(factorial(h), -1, p)*comb(h, j)*(-1)**(h-j)
                 for h in range(j, k+1)) % p for j in range(k+1)]
    E = sum(toy_v[j]*endpoint_border(r, j, p) for j in range(k+1)) % p
    return dict(D=D, E=E, C=C, J=J, low_b=low_b, low_w=low_w,
                Taylor_representative=toy_v, matrix_certificate=matrix_certificate)


start = time.monotonic()
certificates = []
for p in PRIMES:
    expected_prime = source[p]
    assert expected_prime["all_residues_good"]
    original = {row["residue"]: row for row in expected_prime["complete_classes"]}
    assert set(original) == set(range(p))
    rows = []
    for residue in range(p):
        if residue <= (p-1)//2:
            branch, k = "positive", residue
            computed = positive(k, p)
        else:
            branch, k = "negative", p-1-residue
            computed = negative(k, p)
        expected = original[residue]
        assert (branch, k) == (expected["branch"], expected["k"])
        assert computed["D"] == expected["D"] and computed["E"] == expected["E"]
        if k:
            assert computed["C"] == expected["matrix_certificate"]["cofactor_values_gamma_i"]
        if branch == "positive" and k:
            assert computed["scaled_B"] == expected["scaled_B"]
        if branch == "negative" and k:
            assert computed["J"] == expected["J"]
        assert computed["D"] and computed["E"]
        computed.update(residue=residue, branch=branch, k=k,
                        endpoint_over_V1=computed["E"]*pow(computed["D"], -1, p) % p,
                        all_source_values_match=True, both_seeds_units=True)
        rows.append(computed)
    certificate = dict(p=p, residue_count=len(rows), all_residues_verified=True,
                       classes=rows)
    certificates.append(certificate)
    print(json.dumps(dict(p=p, residue_count=len(rows), all_residues_verified=True,
                          D=[c["D"] for c in rows], E=[c["E"] for c in rows])), flush=True)

payload = dict(scope="All residues at only the assigned primes 101 and109.",
               source_sha256=hashlib.sha256(source_bytes).hexdigest(),
               primes=list(PRIMES), all_checks_pass=True, atlas=certificates)
(BASE / "uniform_101_109_independent_certificate.json").write_text(json.dumps(payload, indent=2)+"\n")
print("all_checks_pass; elapsed_seconds", time.monotonic()-start, flush=True)
