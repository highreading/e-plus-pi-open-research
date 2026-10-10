"""Second CLOSED prime list, using one full Wronskian per background.

The inverse last row supplies every needed normalized cofactor.
For a bad prime retain the first exact witness only; for a good prime
retain every residue certificate. No large-degree approximant is built.
"""
import hashlib
import json
from math import comb, factorial
from pathlib import Path

BASE = Path(__file__).resolve().parent
PRIMES = (47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


def choose(n, j):
    if n >= 0:
        return comb(n, j) if 0 <= j <= n else 0
    return (-1)**j * comb(j-n-1, j) if j >= 0 else 0


def ff(n, j):
    result = 1
    for h in range(j):
        result *= n-h
    return result


def rf(n, j):
    result = 1
    for h in range(j):
        result *= n+h
    return result


def det_solve(matrix, rhs, p):
    """Forward elimination plus back substitution; rhs=None only det."""
    A = [[v % p for v in row] for row in matrix]
    b = [v % p for v in rhs] if rhs is not None else None
    det = 1
    pivots = []
    n = len(A)
    for j in range(n):
        row = next((r for r in range(j, n) if A[r][j]), None)
        if row is None:
            return 0, None, pivots
        if row != j:
            A[j], A[row] = A[row], A[j]
            if b is not None:
                b[j], b[row] = b[row], b[j]
            det = -det
        pivot = A[j][j]
        det = det*pivot % p
        pivots.append([j, row, pivot])
        inv = pow(pivot, -1, p)
        for r in range(j+1, n):
            ratio = A[r][j]*inv % p
            for col in range(j, n):
                A[r][col] = (A[r][col]-ratio*A[j][col]) % p
            if b is not None:
                b[r] = (b[r]-ratio*b[j]) % p
    if b is None:
        return det, None, pivots
    solution = [0]*n
    for j in range(n-1, -1, -1):
        solution[j] = (
            b[j]-sum(A[j][i]*solution[i] for i in range(j+1, n))
        )*pow(A[j][j], -1, p) % p
    assert all(sum(matrix[j][i]*solution[i] for i in range(n)) % p == rhs[j] % p
               for j in range(n))
    return det, solution, pivots


def full_and_cofactors(k, background, p):
    assert k >= 1 and 2*k < p
    degrees = list(range(k, 2*k+1))
    appell = [
        sum(choose(background, h)*ff(d, 2*h) for h in range(d//2+1)) % p
        for d in range(2*k+1)
    ]
    W = [[ff(d, j)*appell[d-j] % p if j <= d else 0
          for j in range(k+1)] for d in degrees]
    transpose = [list(row) for row in zip(*W)]
    rhs = [0]*k + [1]
    wd, inverse_row, pivots = det_solve(transpose, rhs, p)
    delta = 1
    for j in range(1, k+1):
        delta = delta*factorial(j) % p
    assert delta
    D = wd*pow(delta, -1, p) % p
    C = [
        (-1)**(i+k)*D*factorial(i)*factorial(k-i)*inverse_row[i] % p
        for i in range(k+1)
    ] if D else None

    # Independently check D by rectangular Jacobi--Trudi and hook product.
    complete = [appell[d]*pow(factorial(d), -1, p) % p for d in range(2*k+1)]
    JT = [[complete[k-i+j] if k-i+j >= 0 else 0
           for j in range(k+1)] for i in range(k+1)]
    jt_det, _, jt_pivots = det_solve(JT, None, p)
    hook = 1
    for i in range(k+1):
        for j in range(k):
            hook = hook*(2*k-i-j) % p
    assert hook and jt_det*hook % p == D
    return D, C, {
        "background": background, "k": k, "Appell_degrees": degrees,
        "Wronskian_matrix": W, "Wronskian_determinant": wd,
        "Vandermonde": delta, "transpose_elimination_pivots": pivots,
        "inverse_last_row": inverse_row, "cofactor_values_gamma_i": C,
        "Jacobi_Trudi_matrix": JT, "Jacobi_Trudi_determinant": jt_det,
        "Jacobi_Trudi_pivots": jt_pivots, "hook_product": hook,
        "full_augmented_value": D,
        "determinant_formulas_agree": True,
        "inverse_row_residual_checked": bool(D),
    }


def positive(k, p):
    if not k:
        return {"D": 1, "E": 1, "source": "empty positive seed"}
    D, C, certificate = full_and_cofactors(k, k, p)
    if not D:
        return {"D": D, "E": None, "matrix_certificate": certificate}
    B = [(-1)**(k-l)*comb(k, l)*C[l] % p for l in range(k+1)]
    high = [
        sum(comb(k, h)*rf(k+l+1, 2*h)*B[l+2*h]
            for h in range((k-l)//2+1)) % p
        for l in range(k+1)
    ]
    V = [
        sum(comb(k+l-r-1, l-r)*high[l] for l in range(r, k+1)) % p
        for r in range(k+1)
    ]
    rhs = [0]*(2*k+1)
    for l, coefficient in enumerate(B):
        degree = k+l
        for h in range(degree//2+1):
            rhs[degree-2*h] = (
                rhs[degree-2*h] + comb(k, h)*ff(degree, 2*h)*coefficient
            ) % p
    divisor = [(-1)**(k-j)*comb(k, j) % p for j in range(k+1)]
    product = [0]*(2*k+1)
    for i, u in enumerate(V):
        for j, v in enumerate(divisor):
            product[i+j] = (product[i+j]+u*v) % p
    assert product == rhs and sum(V) % p == D
    border = [
        sum(comb(k+s, s)*ff(k+r, s) for s in range(k+r+1)) % p
        for r in range(k+1)
    ]
    E = sum(u*v for u, v in zip(V, border)) % p
    return {"D": D, "E": E, "scaled_B": B, "scaled_high_W": high,
            "scaled_V": V, "border": border,
            "differential_identity_checked": True,
            "matrix_certificate": certificate}


def negative(k, p):
    if not k:
        return {"D": 1, "E": 1, "source": "reviewed n+1 theorem"}
    b = -k-1
    D, C, certificate = full_and_cofactors(k, b, p)
    if not D:
        return {"D": D, "E": None, "matrix_certificate": certificate}
    J = [
        factorial(h)*sum(
            (-1)**(k-i)*choose(b+i, i-h)*sum(
                choose(b, u)*rf(b+i+1, 2*u)*choose(b, i+2*u)*C[i+2*u]
                for u in range((k-i)//2+1)
            ) for i in range(h, k+1)
        ) % p
        for h in range(k+1)
    ]
    A = [
        sum((-1)**s*comb(k, s)*comb(s, h)*ff(b, s-h) for s in range(h, k+1)) % p
        for h in range(k+1)
    ]
    assert J[0] == D
    r = p-k-1
    alternate_J = [
        factorial(h)*sum(
            comb(r+i, r+h)*sum(
                comb(r, u)*rf(r+i+1, 2*u)*(-1)**(r-i-2*u)
                *comb(r, i+2*u)*C[i+2*u]
                for u in range((k-i)//2+1)
            ) for i in range(h, k+1)
        ) % p
        for h in range(k+1)
    ]
    assert alternate_J == J
    values = [
        sum(comb(r+s, s)*ff(r+v, s) for s in range(k+1)) % p
        for v in range(k+1)
    ]
    alternate_A = [
        sum((-1)**(h-v)*comb(h, v)*values[v] for v in range(h+1))
        *pow(factorial(h), -1, p) % p
        for h in range(k+1)
    ]
    assert alternate_A == A
    E = sum(u*v for u, v in zip(A, J)) % p
    return {"D": D, "E": E, "J": J, "A": A,
            "negative_finite_functional_cross_checks": True,
            "matrix_certificate": certificate}


def classify(primes):
    results = []
    for p in primes:
        tested = []
        for residue in range(p):
            if residue <= (p-1)//2:
                branch, k = "positive", residue
                seed = positive(k, p)
            else:
                branch, k = "negative", p-1-residue
                seed = negative(k, p)
            status = "determinant_zero" if not seed["D"] else (
                "endpoint_zero" if not seed["E"] else "good"
            )
            record = {
                "p": p, "residue": residue, "branch": branch, "k": k,
                "status": status,
                "endpoint_over_V1": seed["E"]*pow(seed["D"], -1, p) % p if seed["D"] else None,
                **seed,
            }
            tested.append(record)
            if status != "good":
                break
        good = len(tested) == p and tested[-1]["status"] == "good"
        results.append({
            "p": p, "all_residues_good": good,
            "number_of_residues_tested_before_stopping": len(tested),
            "complete_classes": tested if good else None,
            "first_bad_witness": None if good else tested[-1],
            "no_classification_of_untested_residues": not good,
        })
    return results


if __name__ == "__main__":
    results = classify(PRIMES)
    payload = {
        "predeclared_primes": list(PRIMES),
        "scope": "Second closed finite list. Full residue certificates for uniform-good primes; first exact witness only for other primes.",
        "theorem_dependencies": [
            "raw_positive_residue_transfer_independent_review.md",
            "raw_negative_residue_transfer_independent_review.md",
        ],
        "all_internal_exact_cross_checks_passed": True,
        "results": results,
    }
    target = BASE / "raw_second_predeclared_uniform_seed_certificate.json"
    target.write_text(json.dumps(payload, indent=2) + "\n")
    summary = []
    for row in results:
        witness = row["first_bad_witness"]
        summary.append({
            "p": row["p"], "all_residues_good": row["all_residues_good"],
            "tested": row["number_of_residues_tested_before_stopping"],
            "first_bad": {key: witness[key] for key in ("residue", "branch", "k", "status", "D", "E")}
            if witness else None,
        })
    print(json.dumps(summary, indent=2))
    print("certificate_sha256", hashlib.sha256(target.read_bytes()).hexdigest())
