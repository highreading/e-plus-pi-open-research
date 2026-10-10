"""Closed modular Schur-seed certificate for the eight predeclared primes.

All Appell degrees are <p. No actual large-degree approximant is built.
Two determinant formulas and two positive endpoint reconstructions are
checked independently. Uses only Python exact integers and finite fields.
"""
import hashlib
import json
from math import comb, factorial
from pathlib import Path

BASE = Path(__file__).resolve().parent
PRIMES = (17, 19, 23, 29, 31, 37, 41, 43)


def binomial(n, r):
    if r < 0:
        return 0
    if n >= 0:
        return comb(n, r) if r <= n else 0
    return (-1)**r * comb(r - n - 1, r)


def falling(n, r):
    value = 1
    for j in range(r):
        value *= n - j
    return value


def rising(n, r):
    value = 1
    for j in range(r):
        value *= n + j
    return value


def determinant_mod(matrix, p):
    rows = [[x % p for x in row] for row in matrix]
    result = 1
    pivots = []
    for j in range(len(rows)):
        pivot_row = next((i for i in range(j, len(rows)) if rows[i][j]), None)
        if pivot_row is None:
            return 0, pivots
        if pivot_row != j:
            rows[j], rows[pivot_row] = rows[pivot_row], rows[j]
            result = -result
        pivot = rows[j][j]
        pivots.append({"column": j, "row": pivot_row, "value": pivot})
        result = result * pivot % p
        inverse = pow(pivot, -1, p)
        for i in range(j + 1, len(rows)):
            ratio = rows[i][j] * inverse % p
            for col in range(j, len(rows)):
                rows[i][col] = (rows[i][col] - ratio * rows[j][col]) % p
    return result % p, pivots


DETERMINANTS = []
CACHE = {}


def schur_seed(partition, background, p):
    partition = tuple(partition)
    if not partition:
        return 1
    cache_key = (partition, background, p)
    if cache_key in CACHE:
        return CACHE[cache_key]
    size = len(partition)
    degrees = [partition[size - 1 - i] + i for i in range(size)]
    assert max(degrees) < p
    appell = [
        sum(binomial(background, h) * falling(d, 2*h)
            for h in range(d//2 + 1)) % p
        for d in range(max(degrees) + 1)
    ]
    wronskian = [
        [(falling(d, j) * appell[d-j]) % p if j <= d else 0
         for j in range(size)]
        for d in degrees
    ]
    vandermonde = 1
    for i in range(size):
        for j in range(i + 1, size):
            vandermonde = vandermonde * (degrees[j] - degrees[i]) % p
    assert vandermonde
    wd, pivots = determinant_mod(wronskian, p)
    result = wd * pow(vandermonde, -1, p) % p

    # Independently form Jacobi--Trudi and multiply the direct hook product.
    complete = [appell[d] * pow(factorial(d), -1, p) % p
                for d in range(len(appell))]
    jt = []
    for i in range(size):
        row = []
        for j in range(size):
            degree = partition[i] - i + j
            row.append(complete[degree] if degree >= 0 else 0)
        jt.append(row)
    hooks = 1
    for i, width in enumerate(partition):
        for j in range(width):
            below = sum(partition[l] > j for l in range(i + 1, size))
            hooks = hooks * (width - j + below) % p
    assert hooks
    jd, jpivots = determinant_mod(jt, p)
    assert jd * hooks % p == result
    certificate = {
        "p": p,
        "background": background,
        "partition": list(partition),
        "Appell_degrees": degrees,
        "Wronskian_matrix": wronskian,
        "Wronskian_determinant": wd,
        "Vandermonde": vandermonde,
        "Wronskian_pivots": pivots,
        "Jacobi_Trudi_matrix": jt,
        "Jacobi_Trudi_determinant": jd,
        "hook_product": hooks,
        "Jacobi_Trudi_pivots": jpivots,
        "augmented_value": result,
        "two_formulas_agree": True,
    }
    DETERMINANTS.append(certificate)
    CACHE[cache_key] = result
    return result


def border(n, r):
    return sum(comb(n+s, s) * falling(n+r, s) for s in range(n+r+1))


def positive_seed(k, p):
    if k == 0:
        return {"D": 1, "E": 1, "C": [1], "scaled_V": [1],
                "two_endpoint_reconstructions_agree": True}
    full = schur_seed([k]*(k+1), k, p)
    cofactors = [
        schur_seed([k+1]*j + [k]*(k-j), k, p)
        for j in range(k+1)
    ]
    # B_l = D*b_l/V(1); no division by the potentially zero full seed.
    B = [(-1)**(k-l) * comb(k, l) * cofactors[k-l] % p
         for l in range(k+1)]
    high = [
        sum(comb(k, u) * rising(k+l+1, 2*u) * B[l+2*u]
            for u in range((k-l)//2+1)) % p
        for l in range(k+1)
    ]
    scaled_V = [
        sum(comb(k+l-r-1, l-r) * high[l] for l in range(r, k+1)) % p
        for r in range(k+1)
    ]
    # Independent exact differential reconstruction:
    # (t-1)^k * scaled_V = (1+d_t²)^k [t^k B(t)].
    rhs = [0]*(2*k+1)
    for l, coefficient in enumerate(B):
        degree = k+l
        for h in range(min(k, degree//2)+1):
            rhs[degree-2*h] = (
                rhs[degree-2*h] + comb(k, h)*falling(degree, 2*h)*coefficient
            ) % p
    divisor = [(-1)**(k-j)*comb(k, j) % p for j in range(k+1)]
    remainder = rhs[:]
    quotient = [0]*(k+1)
    for degree in range(2*k, k-1, -1):
        lead = remainder[degree]
        quotient[degree-k] = lead
        for j in range(k+1):
            remainder[degree-k+j] = (
                remainder[degree-k+j] - lead*divisor[j]
            ) % p
    assert not any(remainder)
    assert quotient == scaled_V
    assert sum(scaled_V) % p == full
    endpoint = sum(v*border(k, r) for r, v in enumerate(scaled_V)) % p
    return {"D": full, "E": endpoint, "C": cofactors, "scaled_B": B,
            "scaled_high_W": high, "scaled_V": scaled_V,
            "two_endpoint_reconstructions_agree": True}


def negative_seed(k, p):
    if k == 0:
        # The already proved n+1 unit theorem supplies this residue.
        return {"D": 1, "E": 1, "C": [1], "J": [1], "A": [1],
                "source": "reviewed all-index n+1 theorem"}
    b = -k-1
    full = schur_seed([k]*(k+1), b, p)
    cofactors = [
        schur_seed([k+1]*(k-i) + [k]*i, b, p)
        for i in range(k+1)
    ]
    J = []
    A = []
    for h in range(k+1):
        J.append(factorial(h)*sum(
            (-1)**(k-i)*binomial(b+i, i-h)*sum(
                binomial(b, u)*rising(b+i+1, 2*u)
                *binomial(b, i+2*u)*cofactors[i+2*u]
                for u in range((k-i)//2+1)
            )
            for i in range(h, k+1)
        ) % p)
        A.append(sum(
            (-1)**s*comb(k, s)*comb(s, h)*falling(b, s-h)
            for s in range(h, k+1)
        ) % p)
    endpoint = sum(a*j for a, j in zip(A, J)) % p
    assert J[0] == full
    # Independent residue representative uses only nonnegative binomials.
    # These are coefficients of the finite endpoint functional, not an
    # actual approximant at degree r.
    r = p-k-1
    J_nonnegative = [
        factorial(h)*sum(
            comb(r+i, r+h)*sum(
                comb(r, u)*rising(r+i+1, 2*u)
                *(-1)**(r-i-2*u)*comb(r, i+2*u)*cofactors[i+2*u]
                for u in range((k-i)//2+1)
            )
            for i in range(h, k+1)
        ) % p
        for h in range(k+1)
    ]
    assert J_nonnegative == J
    values = [
        sum(comb(r+s, s)*falling(r+v, s) for s in range(k+1)) % p
        for v in range(k+1)
    ]
    A_differences = [
        sum((-1)**(h-v)*comb(h, v)*values[v] for v in range(h+1))
        * pow(factorial(h), -1, p) % p
        for h in range(k+1)
    ]
    assert A_differences == A
    return {"D": full, "E": endpoint, "C": cofactors, "J": J, "A": A,
            "nonnegative_J_cross_check": True,
            "finite_difference_border_cross_check": True}


atlas = []
for p in PRIMES:
    classes = []
    for residue in range(p):
        if residue <= (p-1)//2:
            branch, k = "positive", residue
            seed = positive_seed(k, p)
        else:
            branch, k = "negative", p-1-residue
            seed = negative_seed(k, p)
        D, E = seed["D"], seed["E"]
        status = "determinant_zero" if not D else (
            "endpoint_zero" if not E else "good"
        )
        classes.append({
            "residue": residue, "branch": branch, "k": k,
            "status": status,
            "endpoint_over_V1": E*pow(D, -1, p) % p if D else None,
            **seed,
        })
    assert len(classes) == p
    atlas.append({
        "p": p,
        "all_residues_good": all(row["status"] == "good" for row in classes),
        "determinant_zero_residues": [
            row["residue"] for row in classes if row["status"] == "determinant_zero"
        ],
        "endpoint_zero_residues": [
            row["residue"] for row in classes if row["status"] == "endpoint_zero"
        ],
        "classes": classes,
    })

payload = {
    "predeclared_primes": list(PRIMES),
    "scope": "Fixed modular Schur seeds only; Appell degrees <p. No actual large-degree approximants.",
    "theorem_dependency": "Negative all-index reduction pending independent review at generation.",
    "all_determinant_cross_checks_passed": True,
    "all_positive_endpoint_cross_checks_passed": True,
    "all_negative_endpoint_cross_checks_passed": True,
    "atlas": atlas,
    "determinant_certificates": DETERMINANTS,
}
target = BASE / "raw_predeclared_residue_seed_atlas.json"
target.write_text(json.dumps(payload, indent=2) + "\n")
summary = [
    {key: row[key] for key in ("p", "all_residues_good",
                               "determinant_zero_residues", "endpoint_zero_residues")}
    for row in atlas
]
print(json.dumps(summary, indent=2))
print("certificate_sha256", hashlib.sha256(target.read_bytes()).hexdigest())
print("determinants", len(DETERMINANTS))
