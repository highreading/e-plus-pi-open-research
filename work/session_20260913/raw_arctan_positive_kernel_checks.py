"""Exact algebraic controls for the raw positive kernel; no degree scan."""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json


def add(a,b):return [(a[k] if k<len(a) else F(0))+(b[k] if k<len(b) else F(0)) for k in range(max(len(a),len(b)))]
def mul(a,b):
    ans=[F(0)]*(len(a)+len(b)-1)
    for j,v in enumerate(a):
        for k,w in enumerate(b):ans[j+k]+=v*w
    return ans
def moment(k):return F((-1)**(k//2),k+1) if k%2==0 else F(0)
def integrate(poly):return sum((v/F(k+1) for k,v in enumerate(poly)),F(0))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def pairadd(a,b):return [a[0]+b[0],a[1]+b[1]]
def pairscale(a,b):return [b*a[0],b*a[1]]


def check(n):
    qs=[[F(1)],[F(0),F(1)]]
    for k in range(1,n+1):qs.append(add([F(0)]+qs[-1],[F(k*k,4*k*k-1)*v for v in qs[-2]]))
    hs=[F((-1)**k*2**(2*k),(2*k+1)*comb(2*k,k)**2) for k in range(n+1)]
    vs=[]
    for q in qs:
        quotient=[sum(q[j] for j in range(k+1,len(q))) for k in range(len(q)-1)]
        rational=-dot(quotient,[moment(k) for k in range(len(quotient))])
        vs.append([rational,sum(q)/4])
    weights=[]
    for d in range(n+2):
        w=pairscale(vs[n],qs[n+1][d]/hs[n])
        if d<=n:w=pairadd(w,pairscale(vs[n+1],-qs[n][d]/hs[n]))
        weights.append(w)
    assert [sum(w[i] for w in weights) for i in range(2)]==[F(1),F(0)]
    # Independently compute H_n through the orthogonal projection.
    H=[[F(0),F(0)] for _ in range(n+1)]
    for k in range(n+1):
        for d,c in enumerate(qs[k]):H[d]=pairadd(H[d],pairscale(vs[k],c/hs[k]))
    partial=[F(0),F(0)]
    for d in range(n+2):
        partial=pairadd(partial,weights[d])
        expected=[F(1),F(0)] if d>n else [1-H[d][0],-H[d][1]]
        assert partial==expected
    B=[F((-1)**j*(j+1)) for j in range(n+1)]
    PB=[F(0)]*(n+1)
    for j,b in enumerate(B):
        degree=n-j
        for k in range(degree+1):PB[k]+=b*F((-1)**k*comb(degree,k),factorial(degree))
    for d in (0,1,n,2*n+1):
        expected=sum((b/F(factorial(n+d+1-j)) for j,b in enumerate(B)),F(0))
        actual=sum((v/F(factorial(d)*(k+d+1)) for k,v in enumerate(PB)),F(0))
        assert actual==expected
    # Integral P_B e^x = Q(1)e-Q(0), Q=sum(-1)^r P_B^(r).
    Q=[F(0)]*(n+1)
    for k,v in enumerate(PB):
        for r in range(k+1):Q[k-r]+=(-1)**r*v*F(factorial(k),factorial(k-r))
    value=[-Q[0],sum(Q),F(0)]  # constant, e, pi
    for d,w in enumerate(weights):
        polynomial_tail=[F(1,factorial(k)) for k in range(d)]
        mass=integrate(mul(PB,polynomial_tail)) if d else F(0)
        value[0]-=w[0]*mass;value[2]-=w[1]*mass
    # Independently reconstruct C and A from the actual Taylor equations.
    K=[[sum((qs[k][a]*qs[k][b]/hs[k] for k in range(max(a,b),n+1)),F(0))
        for b in range(n+1)] for a in range(n+1)]
    Cstar=[-sum((B[j]*K[a][d]/factorial(n+d+1-j)
                 for j in range(n+1) for d in range(n+1)),F(0)) for a in range(n+1)]
    C=Cstar[::-1]
    E=[F(1,factorial(k)) for k in range(n+1)]
    atan=[F(0)]+[moment(k) for k in range(n)]
    X=-sum(mul(B,E)[:n+1])-sum(mul(C,atan)[:n+1])
    assert value==[X,sum(B),sum(C)/4]
    return dict(n=n,positive_weight_sum_exact=True,projection_coefficients_exact=True,
                beta_borel_identity_exact=True,whole_integral_constant_e_pi_components_exact=True,
                scope='Arbitrary test B, not an asymptotic or matched-family scan.')


if __name__=='__main__':
    data=dict(status='PASS',checks=[check(n) for n in (1,2,5)])
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
