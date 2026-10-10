"""Finite coefficientwise dyadic disk calculation; NOT an index sample."""
from math import factorial,ceil
from functools import lru_cache
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent
PREC=10
MOD=2**PREC
CUTOFF=ceil(16*(PREC+7)/5)

def vp(a):
    if not a:return 100000
    return (abs(a)&-abs(a)).bit_length()-1

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b,mod=None):
    c=[0]*max(len(a),len(b))
    for j,x in enumerate(a):c[j]+=x
    for j,x in enumerate(b):c[j]+=x
    if mod:c=[x%mod for x in c]
    return trim(c)

def mul(a,b,mod=None):
    c=[0]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    if mod:c=[x%mod for x in c]
    return trim(c)

@lru_cache(None)
def fall(a,b,k):
    if not k:return [1]
    return mul(fall(a,b,k-1),[a-k+1,b])

@lru_cache(None)
def D(a,b):
    out=[0]
    for j in range(2*PREC):out=add(out,fall(a,b,j),MOD)
    return out

def divided(a,den,sgn):
    shift=vp(den)
    assert all(x%2**shift==0 for x in a), (shift,min(map(vp,a)))
    odd=den//2**shift
    inv=pow(odd,-1,MOD)*sgn
    return trim([(x//2**shift*inv)%MOD for x in a])

rows=[]
for residue in [1,3,5,7]:
    H=[0];K=[0];A=[0];B=[0]
    for b in range(CUTOFF):
        for c in range((CUTOFF-1-b)//2+1):
            R=b+2*c;s=b+c
            den=2**c*factorial(b)*factorial(c)
            h=divided(mul(fall(residue,8,R),fall(residue,8,s)),den,(-1)**b)
            if R:
                kval=mul(mul(fall(residue,8,R-1),fall(residue+1,8,s)),[2*residue+2-R,16])
                k=divided(kval,den,(-1)**b)
            else:k=[2]
            H=add(H,h,MOD);K=add(K,k,MOD)
            A=add(A,mul(h,D(2*residue-R,16),MOD),MOD)
            B=add(B,mul(k,D(2*residue+1-R,16),MOD),MOD)
    C=add(mul(K,A,MOD),[-x for x in mul(H,B,MOD)],MOD)
    rows.append({'residue_mod8':residue,'H':H,'K':K,'A':A,'B':B,'C':C,'v2_gauss_C':min(map(vp,C))})
result={'precision':PREC,'modulus':MOD,'outer_R_less_than':CUTOFF,'inner_D_r_less_than':2*PREC,'scope':'All polynomial coefficients on four odd disks; tails proved coefficientwise; no claim about roots inferred yet.','rows':rows}
(BASE/'hp_b1_odd_dyadic_germs_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
