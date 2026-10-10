#!/usr/bin/env python3
"""New physical32-bit divided-power operator and full finite endpoint solve.

Personally authored higher-layer extension of previously inspected formulas.
No original-length arrays, prefix2^32 table, external code or credentials.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'astra_pro5_resume_20261005' / 'controls'
M, Q = 32, 1 << 32
m = 4 * (M-1)
b, n = 9**18, 4002 * 9**18
h = n // 2

def valuation(x):
    return M if not x else (x & -x).bit_length()-1

def eye(k):
    return [[int(i == j) for j in range(k)] for i in range(k)]

def mm(A, B):
    columns = list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) % Q for col in columns] for row in A]

def transpose(A):
    return [list(x) for x in zip(*A)]

def invert_unit(A):
    k = len(A)
    z = [row[:] + e for row,e in zip(A,eye(k))]
    for i in range(k):
        assert z[i][i] & 1
        u = pow(z[i][i], -1, Q)
        z[i] = [x*u % Q for x in z[i]]
        for j in range(k):
            if i != j:
                f = z[j][i]
                if f:
                    z[j] = [(x-f*y) % Q for x,y in zip(z[j],z[i])]
    assert [row[:k] for row in z] == eye(k)
    return [row[k:] for row in z]

def lowbinom(N, limit, negative=False):
    result, x = [1], 1
    for r in range(1,limit+1):
        numerator = x * ((-N-r+1) if negative else N-r+1)
        assert numerator % r == 0
        x = numerator // r
        result.append(x % Q)
    return result

def symbols():
    out, dp = [0]*(m+1), [1]
    for a in range(M):
        scale = (1 << a)*comb(h,a) % Q
        for s,x in enumerate(dp):
            out[s] = (out[s]+scale*x) % Q
        dp = [sum(comb(s,j)*dp[s-j]*v for j,v in enumerate((0,-1,2,-3,3))
                  if j <= s and 0 <= s-j < len(dp)) % Q for s in range(len(dp)+4)]
    return out

def main():
    started = time.monotonic()
    lam, cc = symbols(), [1]
    for s in range(1,m+1):
        cc.append(-sum(comb(s,t)*lam[t]*cc[s-t] for t in range(1,s+1)) % Q)
    assert all(valuation(lam[s]) >= (s+3)//4 and valuation(cc[s]) >= (s+3)//4 for s in range(1,m+1))
    for k in range(2*m+1):
        assert sum(comb(k,s)*lam[s]*cc[k-s] for s in range(max(0,k-m),min(k,m)+1)) % Q == int(k == 0)
    previous_path = OLD/'original_binary_operator_audit_certificate.json'
    previous = json.loads(previous_path.read_text())
    oldm = previous['operator_degree']
    assert [x % (1 << 20) for x in lam[:oldm+1]] == previous['symbol_coefficients']
    assert [x % (1 << 20) for x in cc[:oldm+1]] == previous['inverse_coefficients']
    assert all(x % (1 << 20) == 0 for x in lam[oldm+1:] + cc[oldm+1:])
    neg, pos = lowbinom(n,3*m-1,True), lowbinom(n,m-1)
    F = [[-sum(neg[d+v]*pos[r-v] for v in range(r+1)) % Q for r in range(m)] for d in range(2*m,0,-1)]
    bcoeff = [lowbinom(b+r,m) for r in range(m)]
    Kbar = [[lam[m+r-t]*bcoeff[r][m+r-t] % Q if 1 <= m+r-t <= m else 0 for t in range(m)] for r in range(m)]
    G = []
    for t in range(m):
        jcoeff = lowbinom(b-m+t,m)
        weights = [cc[s]*jcoeff[s] % Q for s in range(m+1)]
        G.append([sum(weights[s]*F[m+t-s][r] for s in range(m+1)) % Q for r in range(m)])
    S = mm(G,Kbar)
    for i in range(m):
        S[i][i] = (S[i][i]+1) % Q
    assert [[x % 2 for x in row] for row in S] == eye(m)
    inverse = invert_unit(S)
    assert mm(S,inverse) == eye(m) and mm(inverse,S) == eye(m)
    origin, Z = b-3*m, [[0]*m for _ in range(3*m)]
    for i in range(3*m-1,-1,-1):
        j = origin+i
        rhs = [int(j == b-m+t) for t in range(m)]
        weights = [(s,lam[s]*comb(j+s,s) % Q) for s in range(1,min(m,3*m-1-i)+1)]
        Z[i] = [(rhs[t]-sum(w*Z[i+s][t] for s,w in weights)) % Q for t in range(m)]
    assert all(x == 0 for row in Z[:m] for x in row)
    Sadj = mm(transpose(Kbar),mm(transpose(F),Z[m:]))
    for i in range(m):
        Sadj[i][i] = (Sadj[i][i]+1) % Q
    assert Sadj == transpose(S)
    artifact = {
        'status':'PASS', 'scope':'NEW original u0 physical32-bit operator and complete finite endpoint solve; force/head/numerators not yet lifted',
        'precision_bits':M, 'operator_degree':m, 'b':str(b), 'n':str(n),
        'symbol_coefficients':lam, 'inverse_coefficients':cc,
        'S_end':S, 'S_end_inverse':inverse, 'G':G, 'Kbar':Kbar,
        'filtration_checks':2*m, 'inverse_coefficient_residual_checks':2*m+1,
        'inverse_product_entries_checked':2*m*m, 'transpose_entries_checked':m*m,
        'lower_padded_zero_entries_checked':m*m, 'unit_parity_checks':m*m,
        'largest_small_binomial_lower_index':3*m-1, 'largest_matrix_shape':[3*m,m],
        'nonidentity_schur_entries':sum(S[i][j] != int(i==j) for i in range(m) for j in range(m)),
        'old20_bit_operator_reduction_passed':True,
        'original_length_array_allocated':False, 'prefix_2_32_table_allocated':False,
        'original_norm_pair_computed':False, 'irrationality_proved':False,
        'previous_operator_sha256':hashlib.sha256(previous_path.read_bytes()).hexdigest()
    }
    target = ROOT/'original_binary_operator_schur32_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt = {k:v for k,v in artifact.items() if k not in ('symbol_coefficients','inverse_coefficients','S_end','S_end_inverse','G','Kbar')}
    receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    receipt['elapsed_seconds'] = round(time.monotonic()-started,3)
    (ROOT/'original_binary_operator_schur32_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
