#!/usr/bin/env python3
"""Personally authored NEW mod27 positive-unit three-coefficient interface.

No eta/scalar350 rerun; no remote code, network or credentials.
Original-domain application depends on the separate locality proof audit.
"""
from pathlib import Path
from functools import lru_cache
from math import comb, factorial
import hashlib
import json
import resource
import time

MOD, BAND = 27, 18
OUT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (45, 50))
G = [1, 0]
for r in range(1, 100):
    G.append(((4*r+2)*G[-1]+4*G[-2]) % MOD)
C = [sum((-1)**(k-r)*comb(k,r)*G[r] for r in range(k+1)) % MOD
     for k in range(BAND+1)]
TERMS = {}
for difference in range(-BAND, BAND+1):
    items = []
    for k, coefficient in enumerate(C):
        if not coefficient or abs(difference) > k:
            continue
        for cross in range(k+1):
            if (k-cross+difference) % 2:
                continue
            left, right = (k-cross+difference)//2, (k-cross-difference)//2
            if min(left, right) < 0:
                continue
            weight = coefficient*comb(k,cross)*comb(k-cross,left)*2**cross % MOD
            items.append((k,left+cross,weight))
    TERMS[difference] = items

@lru_cache(maxsize=60000)
def binomial(n, k):
    return comb(n,k) % MOD if n >= k >= 0 else 0

def entry(i, j):
    if abs(i-j) > BAND:
        return 0
    return sum(weight*binomial(i-offset+k,k)
               for k,offset,weight in TERMS[i-j] if i >= offset) % MOD

def solve_unit(matrix, rhs):
    rows = [list(row)+[rhs[i] % MOD] for i,row in enumerate(matrix)]
    for col in range(len(rows)):
        pivot = next(i for i in range(col,len(rows)) if rows[i][col] % 3)
        rows[col], rows[pivot] = rows[pivot], rows[col]
        inverse = pow(rows[col][col],-1,MOD)
        rows[col] = [a*inverse % MOD for a in rows[col]]
        for i in range(len(rows)):
            if i == col or not rows[i][col]:
                continue
            factor = rows[i][col]
            rows[i] = [(a-factor*b) % MOD for a,b in zip(rows[i],rows[col])]
    return [row[-1] for row in rows]

J3, J2 = [[1,2,2],[2,0,0],[2,0,2]], [[1,2],[2,0]]
INV = {}
for width, block in ((3,J3),(2,J2)):
    columns = [solve_unit(block,[int(i==j) for i in range(width)])
               for j in range(width)]
    INV[width] = list(map(list, zip(*columns)))

def apply_c(vector, inverse=False):
    answer, start = [], 0
    while start < len(vector):
        width = min(3,len(vector)-start)
        assert width in (2,3)
        block = INV[width] if inverse else (J3 if width==3 else J2)
        answer.extend(sum(block[i][j]*vector[start+j] for j in range(width)) % MOD
                      for i in range(width))
        start += width
    return answer

def band_matrix(start, stop):
    return [[(j-start,entry(i,j)) for j in range(max(start,i-BAND),min(stop,i+BAND+1))
             if entry(i,j)] for i in range(start,stop)]

def apply_b(rows, vector):
    return [sum(value*vector[j] for j,value in row) % MOD for row in rows]

def solve_three_terms(rows, rhs):
    term = apply_c(rhs,True)
    result = term.copy()
    for order in (1,2):
        delta = [(a-b) % MOD for a,b in zip(apply_b(rows,term),apply_c(term))]
        term = [(-a) % MOD for a in apply_c(delta,True)]
        assert all(a % 3**order == 0 for a in term)
        result = [(a+b) % MOD for a,b in zip(result,term)]
    assert apply_b(rows,result) == [a % MOD for a in rhs]
    return result

def local_data(n, width):
    start = n-width
    assert n % 3 == 2 and start % 3 == 0 and width >= 62
    rows = band_matrix(start,n)
    for i,row in enumerate(rows):
        basis = [int(j==i) for j in range(width)]
        leading = apply_c(basis)
        actual = dict(row)
        assert all(actual.get(j,0) % 3 == leading[j] % 3 for j in range(width))
    u, ratio = {}, 1
    for a in range(n-1,n-10,-1):
        u[a] = ratio*pow(-2,a,MOD) % MOD
        ratio = ratio*a % MOD
    assert ratio == 0
    uh = [0]*width
    for i in range(n-9,n):
        uh[i-start] = sum((-1)**(i-a)*binomial(i,i-a)*u[a]
                         for a in range(n-9,i+1)) % MOD
    b = [entry(i,n) for i in range(start,n)]
    zu, zb = solve_three_terms(rows,uh), solve_three_terms(rows,b)
    h_values, v_values = [], []
    for a in (n-5,n-4,n-3):
        h_values.append(sum((-1)**(j-a)*binomial(j,j-a)*
                            (binomial(n,n-j)+zb[j-start]) for j in range(a,n)) % MOD)
        v_values.append(sum((-1)**(j-a)*binomial(j,j-a)*zu[j-start]
                            for j in range(a,n)) % MOD)
    assert all(h % 3 == 0 for h in h_values)
    assert all(v % 9 == 0 for v in v_values)
    rho = [(-f*(2*(h % 9)//3+v//9)) % 3
           for f,h,v in zip((2,2,1),h_values,v_values)]
    g0 = 2*rho[0] % 3
    g1 = 2*(rho[1]-g0) % 3
    g2 = 2*(rho[2]-g1) % 3
    endpoint_low = [(g0+g1+g2)%3,(2*g0+2*g1+g2)%3,(g0+g2)%3]
    return {'n_positive_unit_representative':n,'width':width,'start':start,
            'h_mod27':h_values,'h_mod9':[h%9 for h in h_values],
            'v_mod27':v_values,'paid_h_div3':True,'paid_v_div9':True,
            'rho_mod3':rho,'g0_g1_g2_mod3':[g0,g1,g2],
            'endpoint_low_by_i_mod3':endpoint_low,
            'endpoint_difference_by_i_mod3_given_c0':[(-e)%3 for e in endpoint_low],
            'z_u_top5_mod27':zu[-5:],'z_b_top5_mod27':zb[-5:],
            'band_nonzero_entries':sum(len(row) for row in rows),
            'three_term_solution_residuals_zero':True}

def validate():
    for r in range(70):
        exact = sum(factorial(k)*comb(r,k)*comb(r+k,k)*(-2)**(r-k)
                    for k in range(r+1)) % MOD
        assert exact == G[r]
    for r in range(100):
        assert sum(C[k]*comb(r,k) for k in range(min(r,BAND)+1)) % MOD == G[r]
    checks = []
    for n in (11,14,17):
        T = [[comb(i+j,i)*G[i+j] % MOD for j in range(n)] for i in range(n)]
        left = [[sum((-1)**(i-a)*comb(i,a)*T[a][j] for a in range(i+1)) % MOD
                 for j in range(n)] for i in range(n)]
        full = [[sum((-1)**(j-a)*comb(j,a)*left[i][a] for a in range(j+1)) % MOD
                 for j in range(n)] for i in range(n)]
        kernel = [[entry(i,j) for j in range(n)] for i in range(n)]
        assert full == kernel
        rows = [[(j,value) for j,value in enumerate(row) if value] for row in kernel]
        for rhs in ([int(i==n-1) for i in range(n)],[entry(i,n) for i in range(n)]):
            assert solve_three_terms(rows,rhs) == solve_unit(full,rhs)
        checks.append({'n':n,'direct_finite_pascal_equal':True,'two_full_unit_solves_equal':True})
    return checks

def main():
    began = time.monotonic()
    checks = validate()
    first, wider, periodic = local_data(245,62), local_data(245,65), local_data(974,62)
    fields = ('h_mod9','v_mod27','rho_mod3','g0_g1_g2_mod3','endpoint_low_by_i_mod3')
    assert all(first[k] == wider[k] == periodic[k] for k in fields)
    data = {'status':'PASS','scope':'NEW three-coefficient positive-unit interface, conditional original-domain use on A1turn21 locality and factorial-unit proof',
            'modulus':MOD,'bandwidth':BAND,'neumann_terms':3,
            'small_exact_validations':checks,'primary':first,'wider_boundary':wider,
            'periodic_representative':periodic,'eta_division_repeated':False,
            'old350_scalar_repeated':False,'original_full_matrix_constructed':False,
            'small_signed_producer_order6_assumed':False,
            'actual_Q_over27_evaluated':False,'primitive_denominator_calculated':False,
            'whole_error_calculated':False,'irrationality_proved':False,
            'elapsed_seconds':round(time.monotonic()-began,3),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    artifact = OUT/'ternary_second_producer_jet_artifact.json'
    artifact.write_text(json.dumps(data,indent=2)+'\n')
    receipt = dict(data,artifact_sha256=hashlib.sha256(artifact.read_bytes()).hexdigest())
    (OUT/'ternary_second_producer_jet_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    main()
