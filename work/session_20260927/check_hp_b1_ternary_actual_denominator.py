"""Exact identities at frozen n=2,8; no new canonical solve or degree scan."""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "session_20260913"

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def coeffs(k):
    out=[F(1)]
    for _ in range(k): out=mul(out,[1,-1,F(1,2)])
    return out

def falling(n,s):
    return factorial(n)//factorial(n-s)

def integer_legendre(k):
    # Direct Rodrigues coefficients, independent of the old recurrence.
    a=coeffs(k)
    out=[2**k*a[k-j]*factorial(k+j)/
         (factorial(k)*factorial(j)) for j in range(k+1)]
    assert all(x.denominator==1 for x in out)
    return [int(x) for x in out]

def E(k): return sum((F(1,factorial(j)) for j in range(k+1)),F(0))
def D(k): return factorial(k)*E(k)
def vp(x,p):
    x=F(x)
    if x==0:return None
    u,v=abs(x.numerator),x.denominator
    d=0
    while u%p==0:u//=p;d+=1
    while v%p==0:v//=p;d-=1
    return d
def mod(x,p):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,p)%p

frozen=json.loads((OLD/"hp_b1_adjacent_scalar_gate_checks.json").read_text())
rows=[]
for old in frozen["rows"]:
    n=old["n"]
    assert n in (2,8)
    a,an=coeffs(n),coeffs(n+1)
    H=sum((falling(n,s)*a[s] for s in range(n+1)),F(0))
    K=2+sum((falling(n,s-1)*(2*n+2-s)*an[s]
             for s in range(1,n+2)),F(0))
    A=sum((falling(n,s)*a[s]*D(2*n-s) for s in range(n+1)),F(0))
    B=2*D(2*n+1)+sum((falling(n,s-1)*(2*n+2-s)*an[s]*D(2*n+1-s)
                        for s in range(1,n+2)),F(0))
    C=K*A-H*B
    pol=[integer_legendre(k) for k in range(n+2)]
    P=[sum(x) for x in pol]
    Q=[8*sum((F(P[j-1]*P[k-j],j) for j in range(1,k+1)),F(0))
       for k in range(n+2)]
    T=[sum((x*E(n+j) for j,x in enumerate(pol[k])),F(0)) for k in (n,n+1)]
    assert T[0]==F(2**n,factorial(n)**2)*A
    assert T[1]==F(2**(n+1),(n+1)*factorial(n)**2)*B
    assert int(H)==old["H_n"] and int(K)==old["K_next"]
    assert [mod(x,3) for x in (H,K,A,B,C)]==[1,2,0,1,2]
    Qpart=2*K*Q[n]-(n+1)*H*Q[n+1]
    full=Qpart+F(2**(n+1),factorial(n)**2)*C
    Delta=(n+1)*P[n+1]*H-2*P[n]*K
    ratio=full/Delta
    assert str(ratio)==old["endpoint_ratio"]
    assert ratio.denominator==old["actual_q"]
    assert factorial(2*n+1)*full==old["N"]
    assert vp(C,2)==1
    assert vp(full,2)==n+2-2*vp(factorial(n),2)
    assert vp(ratio.denominator,2)==max(0,vp(Delta,2)-vp(full,2))
    assert vp(ratio.denominator,2)>=2*vp(factorial(n),2)-n//2
    for k in (n,n+1):
        assert P[k]==sum(2**(k-j)*comb(k,2*j)*comb(2*j,j)
                         for j in range(k//2+1))
    if n>=5:
        assert vp(full,3)==-2*vp(factorial(n),3)
        assert vp(ratio.denominator,3)==2*vp(factorial(n),3)
        assert vp(F(factorial(n)**2,2**(n+1))*Qpart,3)>=1
    rows.append(dict(n=n,H=str(H),K=str(K),A=str(A),B=str(B),C=str(C),
                     surviving_residues=[mod(x,3) for x in (H,K,A,B,C)],
                     full_numerator=str(full),actual_endpoint=str(ratio),
                     actual_q=ratio.denominator,v3_q=vp(ratio.denominator,3),
                     v2_C=vp(C,2),v2_full_numerator=vp(full,2),
                     v2_Delta=vp(Delta,2),v2_actual_q=vp(ratio.denominator,2),
                     v3_old_N=vp(factorial(2*n+1)*full,3),
                     old_frozen_values_match=True))

# A single exact residue-state recurrence verifies the all-block digit pattern.
d=[1]
for r in (1,2):d.append((r*d[-1]+1)%3)
assert d==[1,2,2]
assert (0*d[-1]+1)%3==d[0]
weights=[1,2,1]
assert sum(weights)%3==1
assert sum(w*d[(1-s)%3] for s,w in enumerate(weights))%3==0
assert 2*d[2]%3==1
out=dict(scope="Frozen n=2,8 identities only; symbolic modulo-3 state, no scan.",
         all_checks_pass=True,D_residue_cycle=d,rows=rows)
(HERE/"hp_b1_ternary_actual_denominator_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
