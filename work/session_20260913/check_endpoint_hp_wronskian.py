"""Bounded exact validation of the new HP Wronskian formula.

Uses four frozen archive rows, not a new degree scan. The all-degree proof
is in endpoint_hp_continuation.md; finite checks are not that proof.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import gcd, lcm
import json, sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from item306_j2_normalized_m_bridge_certificate import p_trim,p_add,p_sub,p_mul,p_scale,p_divmod,p_eval,P_ZERO,P_ONE,Rat

def der(p):return p_trim([i*p[i] for i in range(1,len(p))])
def det(matrix):
    out=0
    for perm in permutations(range(3)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        val=sign
        for i,j in enumerate(perm):val=val*matrix[i][j]
        out=out+val
    return out
def pdet(matrix):
    return det([[Rat(p) for p in row] for row in matrix]).num
def root_count(p):
    if p==P_ZERO:return None
    seq=[p,der(p)]
    if seq[-1]==P_ZERO:return 0
    while len(seq[-1])>1:
        r=p_scale(p_divmod(seq[-2],seq[-1])[1],-1)
        if r==P_ZERO:break
        seq.append(p_scale(r,1/abs(r[-1])))
    def changes(x):
        signs=[]
        for row in seq:
            v=p_eval(row,x)
            if v:signs.append(1 if v>0 else -1)
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    return changes(0)-changes(1)
def primitive(p):
    den=lcm(*(v.denominator for v in p));values=[int(v*den) for v in p]
    common=gcd(*values)
    return [v//common for v in values]

D=p_trim([2,-2,1]);Dp=der(D);f=Rat(4,D);fp=Rat(p_scale(Dp,-4),p_mul(D,D))
rows=json.loads((ROOT/'results/item179_independent_diagonal_certificate.json').read_text())['exact_rational']['endpoint_matched']
out=[]
for n in [2,3,6,8]:
    row=rows[n-1];tri=list(map(F,row['triple']));A,B,C=[p_trim(tri[i*(n+1):(i+1)*(n+1)]) for i in range(3)]
    Ap,Bp,Cp=map(der,[A,B,C]);App,Bpp,Cpp=map(der,[Ap,Bp,Cp])
    B1=p_add(Bp,B);B2=p_add(p_add(Bpp,p_scale(Bp,2)),B)
    K=p_sub(p_mul(B,Cp),p_mul(B1,C))
    Wpoly=pdet([[A,B,C],[Ap,B1,Cp],[App,B2,Cpp]])
    term=p_add(p_scale(p_mul(C,p_sub(p_mul(B,Cpp),p_mul(B2,C))),-1),p_scale(p_mul(Cp,K),2))
    N=p_sub(p_add(p_mul(p_mul(D,D),Wpoly),p_scale(p_mul(D,term),4)),p_scale(p_mul(p_mul(Dp,C),K),4))
    matrix=[[Rat(A),Rat(B),Rat(C)],
            [Rat(Ap)+Rat(C)*f,Rat(B1),Rat(Cp)],
            [Rat(App)+2*Rat(Cp)*f+Rat(C)*fp,Rat(B2),Rat(Cpp)]]
    direct=det(matrix)*Rat(p_mul(D,D))
    assert direct==Rat(N)
    assert all(v==0 for v in N[:3*n-1]) and len(N)<=3*n+3
    cubic=p_trim(N[3*n-1:])
    out.append({'n':n,'direct_identity':True,'forcing_degree':len(cubic)-1,
                'forcing_primitive_low_to_high':primitive(cubic),
                'roots_in_0_1':{'B':root_count(B),'C':root_count(C),'K':root_count(K),'forcing':root_count(cubic)},
                'endpoint_nonzero':{'B':bool(p_eval(B,1)),'C':bool(p_eval(C,1)),'K':bool(p_eval(K,1))},
                'K_at_zero':str(p_eval(K,0))})
target=Path(__file__).with_name('endpoint_hp_wronskian_checks.json')
target.write_text(json.dumps({'classification':'exact finite validation, not the all-degree proof','rows':out},indent=2)+'\n')
print(json.dumps(out,indent=2))
