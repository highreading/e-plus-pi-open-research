#!/usr/bin/env python3
"""Personally authored bounded signed-producer scalar arithmetic.

Uses mathematical formulas from A1turn20 as untrusted specifications.
No network, secrets, external code, or original-size contact matrix is used.
Finite validation is separate from the original-domain proof audit.
"""
from pathlib import Path
from functools import lru_cache
from math import comb, factorial
import hashlib
import json
import resource
import time

MOD = 3**8
OUT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (100, 110))

def moments(length, modulus=MOD):
    g = [1, 0]
    for r in range(1, length):
        g.append(((4*r+2)*g[-1]+4*g[-2]) % modulus)
    return g

G = moments(100)
C = [sum((-1)**(k-r)*comb(k,r)*G[r] for r in range(k+1)) % MOD
     for k in range(42)]

# Expansion by the numbers of z, w and 2zw numerator factors.
TERMS = {}
for d in range(-41, 42):
    terms = []
    for k, ck in enumerate(C):
        if not ck or abs(d) > k:
            continue
        for cross in range(k+1):
            if (k-cross+d) % 2:
                continue
            left = (k-cross+d)//2
            right = (k-cross-d)//2
            if min(left, right) < 0:
                continue
            weight = ck*comb(k,cross)*comb(k-cross,left)*2**cross % MOD
            terms.append((k, left+cross, weight))
    TERMS[d] = terms

@lru_cache(maxsize=120000)
def small_binomial(top, low):
    return comb(top,low) % MOD if top >= low >= 0 else 0

def entry(i, j):
    if abs(i-j) > 41:
        return 0
    return sum(weight*small_binomial(i-offset+k,k)
               for k,offset,weight in TERMS[i-j] if i >= offset) % MOD

J3 = [[1,2,2], [2,0,0], [2,0,2]]
J2 = [[1,2], [2,0]]

def solve_full(matrix, rhs):
    size = len(matrix)
    rows = [list(row)+[rhs[i] % MOD] for i,row in enumerate(matrix)]
    for col in range(size):
        pivot = next(i for i in range(col,size) if rows[i][col] % 3)
        rows[col], rows[pivot] = rows[pivot], rows[col]
        inv = pow(rows[col][col], -1, MOD)
        rows[col] = [x*inv % MOD for x in rows[col]]
        for i in range(size):
            if i == col or not rows[i][col]:
                continue
            mult = rows[i][col]
            rows[i] = [(x-mult*y) % MOD for x,y in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]

INV3 = list(map(list, zip(*(solve_full(J3,[int(i==j) for i in range(3)])
                          for j in range(3)))))
INV2 = list(map(list, zip(*(solve_full(J2,[int(i==j) for i in range(2)])
                          for j in range(2)))))

def c_apply(vec, inverse=False):
    size = len(vec)
    result = []
    pos = 0
    while pos < size:
        width = min(3, size-pos)
        assert width in (2,3)
        block = (INV3 if inverse else J3) if width==3 else (INV2 if inverse else J2)
        result.extend(sum(block[r][j]*vec[pos+j] for j in range(width)) % MOD
                      for r in range(width))
        pos += width
    return result

def band_matrix(start, stop):
    rows = []
    for i in range(start,stop):
        row = [(j-start, entry(i,j))
               for j in range(max(start,i-41), min(stop,i+42))]
        rows.append([(j,v) for j,v in row if v])
    return rows

def apply_band(rows, vec):
    return [sum(v*vec[j] for j,v in row) % MOD for row in rows]

def neumann(rows, rhs):
    term = c_apply(rhs, inverse=True)
    total = term.copy()
    order_checks = []
    for order in range(1,8):
        full = apply_band(rows,term)
        zero = c_apply(term)
        delta = [(a-b) % MOD for a,b in zip(full,zero)]
        term = [(-x) % MOD for x in c_apply(delta,inverse=True)]
        order_checks.append(all(x % (3**order)==0 for x in term))
        total = [(a+b) % MOD for a,b in zip(total,term)]
    assert all(order_checks)
    assert apply_band(rows,total) == [x % MOD for x in rhs]
    return total

def terminal_data(n, width):
    start = n-width
    assert n%3==2 and start%3==0 and width>=350
    rows = band_matrix(start,n)
    # Verify the exact leading lift against the absolute finite block alignment.
    for i,row in enumerate(rows):
        basis = [0]*width
        basis[i] = 1
        leading = c_apply(basis)
        assert all(v%3 == leading[j]%3 for j,v in row)
        present = {j for j,v in row}
        assert all(leading[j]%3 == 0 for j in range(width) if j not in present)
    u = {}
    ratio = 1
    for a in range(n-1, n-19, -1):
        u[a] = ratio*pow(-2,a,MOD) % MOD
        ratio = ratio*a % MOD
    assert ratio % MOD == 0  # the next and all earlier entries vanish.
    uh = [0]*width
    for i in range(n-18,n):
        uh[i-start] = sum((-1)**(i-a)*small_binomial(i,i-a)*u[a]
                          for a in range(n-18,i+1)) % MOD
    b = [entry(i,n) for i in range(start,n)]
    zu, zb = neumann(rows,uh), neumann(rows,b)
    eta = -sum(a*z for a,z in zip(uh,zu)) % MOD
    uh_h = sum(uh[i]*(small_binomial(n,n-start-i)+zb[i])
               for i in range(width)) % MOD
    chi = 3*(n*uh_h-4*pow(-2,n-2,MOD)) % MOD
    assert eta%9==3 and chi%3==0
    xi = ((chi//3)*pow(eta//3,-1,3**7)) % (3**7)
    e = (n+60-3*n*(n+zb[-1])-xi*zu[-1]) % (3**7)
    paid = e % (3**6) == 0
    scalar = e//(3**6) if paid else None
    return {'n_residue_representative':n, 'width':width, 'start':start,
            'eta_mod_6561':eta, 'eta_mod9':eta%9,
            'chi_mod6561':chi, 'chi_mod9':chi%9,
            'xi_mod2187':xi, 'xi_mod3':xi%3,
            'top_e_mod2187':e, 'order6_division_paid':paid,
            'jet_scalar_mod3':scalar,
            'z_u_top_mod6561':zu[-1], 'z_b_top_mod6561':zb[-1],
            'band_nonzero_entries':sum(len(row) for row in rows),
            'eight_term_solution_residual_zero':True,
            'jet_eight_residues':([0]*6+[2*scalar%3,scalar]) if paid else None,
            'terminal_seven_detector':([0]*6+[2*scalar%3]) if paid else None}

def validate():
    # Independently sum the exact factorial moment formula at new bounded orders.
    for r in range(66):
        value = sum(factorial(k)*comb(r,k)*comb(r+k,k)*(-2)**(r-k)
                    for k in range(r+1)) % MOD
        assert value == G[r]
    for r in range(100):
        assert sum(C[k]*comb(r,k) for k in range(min(r,41)+1)) % MOD == G[r]
    checks = []
    for n in (23,26,29):
        T = [[comb(i+j,i)*G[i+j] % MOD for j in range(n)] for i in range(n)]
        # Two direct finite inverse-Pascal multiplications, not the rational kernel.
        left = [[sum((-1)**(i-a)*comb(i,a)*T[a][j] for a in range(i+1)) % MOD
                 for j in range(n)] for i in range(n)]
        transformed = [[sum((-1)**(j-a)*comb(j,a)*left[i][a]
                            for a in range(j+1)) % MOD
                        for j in range(n)] for i in range(n)]
        kernel = [[entry(i,j) for j in range(n)] for i in range(n)]
        assert transformed == kernel
        rows = [[(j,v) for j,v in enumerate(row) if v] for row in kernel]
        for rhs in ([int(i==n-1) for i in range(n)], [entry(i,n) for i in range(n)]):
            assert neumann(rows,rhs) == solve_full(transformed,rhs)
        checks.append({'n':n,'full_pascal_matrix_equal':True,
                       'two_full_unit_solves_equal':True})
    return checks

def main():
    began = time.monotonic()
    checks = validate()
    first = terminal_data(86996,350)
    # A wider boundary and a different representative check actual stated locality.
    wider = terminal_data(86996,353)
    periodic = terminal_data(86996+3**11,350)
    fields = ('eta_mod_6561','chi_mod6561','xi_mod2187','top_e_mod2187')
    assert all(first[k] == wider[k] == periodic[k] for k in fields)
    paid = first['order6_division_paid']
    data = {'status':'PASS' if paid else 'FAIL_ORDER6_SOURCE_INTERFACE',
            'scope':'NEW bounded actual signed-producer first-jet evaluator; original-domain band/period theorem still needs independent proof audit',
            'modulus':MOD,'moments_through':41,'bandwidth':41,
            'small_exact_validations':checks,
            'primary':first,'wider_boundary':wider,'periodic_representative':periodic,
            'original_full_matrix_constructed':False,'old_producer_regenerated':False,
            'actual_inverse_contraction_evaluated':False,
            'primitive_denominator_calculated':False,'whole_error_calculated':False,
            'irrationality_proved':False,'elapsed_seconds':round(time.monotonic()-began,3),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    artifact = OUT/'ternary_actual_producer_jet_artifact.json'
    artifact.write_text(json.dumps(data,indent=2)+'\n')
    receipt = dict(data)
    receipt['artifact_sha256'] = hashlib.sha256(artifact.read_bytes()).hexdigest()
    (OUT/'ternary_actual_producer_jet_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    main()
