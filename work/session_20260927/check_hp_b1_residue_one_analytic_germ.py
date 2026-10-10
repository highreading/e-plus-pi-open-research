"""Exact index-disk polynomial certificate modulo 27; no degree/prime samples."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def fall(a,b,k):
    out=[F(1)]
    for j in range(k):out=mul(out,[F(a-j),F(b)])
    return out

def D(a,b):
    out=[F(0)]
    for r in range(9):out=add(out,fall(a,b,r))
    return out

H=A=KP=BP=[F(0)]
for b in range(12):
    for c in range((11-b)//2+1):
        R=b+2*c;s=b+c
        coef=F((-1)**b,2**c*factorial(b)*factorial(c))
        hterm=scale(mul(fall(1,3,R),fall(1,3,s)),coef)
        H=add(H,hterm)
        A=add(A,mul(hterm,D(2-R,6)))
        kterm=scale(mul(mul(fall(2,3,R),fall(2,3,s)),[F(4-R),F(6)]),coef)
        KP=add(KP,kterm)
        BP=add(BP,mul(kterm,D(3-R,6)))
# 1/(X+1)=1/(2+3Y), modulo27, as an integral restricted series.
inv=[F(1,2),F(-3,4),F(9,8)]
K=mul(KP,inv);B=mul(BP,inv)
C=add(mul(K,A),scale(mul(H,B),-1))

def residue(a,mod):
    out=[]
    for x in a:
        assert x.denominator%3, 'Every coefficient must be 3-integral'
        out.append(x.numerator*pow(x.denominator,-1,mod)%mod)
    return trim(out)

assert residue(H,9)==[0]
assert residue(H,27)==[0,9,9]
assert residue(K,9)==[0,3]
assert residue(A,3)==[0]
assert residue(A,9)==[3,6]
assert residue(B,3)==[1]
assert residue(C,27)==[0,0,9]
# Exact values and derivatives need no infinite numerical differentiation:
# H'(1)=-3/2, K'(1)=4, A(1)=3, B(1)=10.
derivative=4*3-F(-3,2)*10
assert derivative==27
out={
    'scope':'All coefficients of the analytic index germ modulo27; no degree/prime sample',
    'outer_cutoff':'b+2c<12; omitted terms Gauss valuation>=3',
    'inner_cutoff':'r<9 in D(X)=sum(X)_r; omitted terms Gauss valuation>=3',
    'all_checks_pass':True,
    'H_mod9':residue(H,9),'H_mod27':residue(H,27),'K_mod9':residue(K,9),
    'A_mod9':residue(A,9),
    'A_mod3':residue(A,3),'B_mod3':residue(B,3),
    'C_mod27':residue(C,27),
    'C_index_derivative_at1':str(derivative),
    'max_polynomial_degree_checked':len(C)-1,
}
(BASE/'hp_b1_residue_one_analytic_germ_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
