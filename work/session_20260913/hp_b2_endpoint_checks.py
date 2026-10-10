"""Selected exact degree-two HP normalization checks; no asymptotic inference."""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json


def add(a,b):
    return [(a[k] if k<len(a) else F(0))+(b[k] if k<len(b) else F(0))
            for k in range(max(len(a),len(b)))]


def mul(a,b):
    ans=[F(0)]*(len(a)+len(b)-1)
    for j,v in enumerate(a):
        for k,w in enumerate(b):ans[j+k]+=v*w
    return ans


def moment(k):
    return sum((F(2*comb(k,j)*(-1)**(j//2),(j+1)*2**k)
                for j in range(0,k+1,2)),F(0))


def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))


def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def check(n):
    ps=[[F(1)],[F(-1,2),F(1)]]
    for k in range(1,n+1):
        ps.append(add(mul(ps[-1],[F(-1,2),F(1)]),
                      [F(k*k,4*(4*k*k-1))*v for v in ps[-2]]))
    norms=[F(2*(-1)**k,(2*k+1)*comb(2*k,k)**2) for k in range(n+1)]
    K=[[sum((ps[k][i]*ps[k][j]/norms[k] for k in range(max(i,j),n+1)),F(0))
        for j in range(n+1)] for i in range(n+1)]
    ell=lambda poly,j:sum((v/factorial(n+k+1-j) for k,v in enumerate(poly)),F(0))
    aa=[ell(ps[n+1],j) for j in range(3)]
    cs=[[-sum((K[i][k]/factorial(n+k+1-j) for k in range(n+1)),F(0))
         for i in range(n+1)] for j in range(3)]
    tt=[-sum(c) for c in cs]
    ep=[1+t for t in tt]
    B=[aa[1]*ep[2]-aa[2]*ep[1],aa[2]*ep[0]-aa[0]*ep[2],aa[0]*ep[1]-aa[1]*ep[0]]
    assert dot(aa,B)==dot(ep,B)==0
    Cstar=[sum((B[j]*cs[j][k] for j in range(3)),F(0)) for k in range(n+1)]
    C=list(reversed(Cstar));Y=sum(B)
    assert sum(C)==Y
    seriesF=[F(0)]+[moment(k) for k in range(2*n+2)]
    seriesE=[F(1,factorial(k)) for k in range(2*n+3)]
    Be=mul(B,seriesE);CF=mul(C,seriesF)
    A=[-Be[k]-CF[k] for k in range(n+1)]
    assert all(Be[k]+CF[k]==0 for k in range(n+1,2*n+3))
    X=sum(A)
    # Compute H_n through second-kind integrals v_k = p_k(1)*pi - q_k.
    # Coefficients are stored as rational-plus-pi pairs.
    Hrat=[F(0)]*(n+1);Hpi=[F(0)]*(n+1)
    for k,pk in enumerate(ps[:n+1]):
        endpoint=sum(pk)
        # (p_k(1)-p_k(t))/(1-t) = sum_{j>=1} p_{k,j}(1+...+t^(j-1)).
        quotient=[sum(pk[j] for j in range(i+1,k+1)) for i in range(k)]
        q=dot(quotient,[moment(i) for i in range(k)])
        for i,v in enumerate(pk):
            Hrat[i]-=v*q/norms[k];Hpi[i]+=v*endpoint/norms[k]
    assert Hpi==[sum(row) for row in K]
    wrat=[-sum((F(1,factorial(k)) for k in range(n-j+1)),F(0))-ell(Hrat,j)
          for j in range(3)]
    wpi=[-ell(Hpi,j) for j in range(3)]
    assert wpi==[-t for t in tt]
    assert dot(B,wrat)==X and dot(B,wpi)==Y
    # Identity (11), separately for the rational, e, and pi components.
    delta=lambda v:v[1]-v[0]
    theta=lambda v:v[2]-v[1]
    S=lambda v,w:theta(v)*delta(w)-delta(v)*theta(w)
    assert Y==-S(aa,tt)
    assert X==S(aa,wrat)+det(aa,tt,wrat)
    assert Y==S(aa,[F(1)]*3)+det(aa,tt,[F(1)]*3)
    assert Y==S(aa,wpi)+det(aa,tt,wpi)
    return dict(n=n,rank_two=any(B),B0_nonzero=bool(B[0]),
                normalized_Y=str(Y/B[0]) if B[0] else None,
                endpoint_q=str((X/Y).denominator) if Y else None,
                original_high_rows_verified=True,whole_remainder_identity_verified=True)


if __name__=='__main__':
    data=dict(status='PASS',scope='Four preselected exact degrees; no matrix scan or asymptotic inference.',
              cases=[check(n) for n in (2,3,8,16)])
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
