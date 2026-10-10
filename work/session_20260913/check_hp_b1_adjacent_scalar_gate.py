"""Two pre-existing degrees only: n=2,8; no canonical solve or scan."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def legendre_integer(n):
    out=[[1],[ -2,4]]
    for k in range(2,n+1):
        nxt=mul(out[-1],[-2*(2*k-1),4*(2*k-1)])
        for j,x in enumerate(out[-2]):nxt[j]+=4*(k-1)*x
        nxt=[x/k for x in nxt]
        assert all(x.denominator==1 for x in nxt)
        out.append([int(x) for x in nxt])
    return out[:n+1]

def moment(j):
    return sum((F(2*comb(j,r)*(-1)**(r//2),2**j*(r+1))
                for r in range(0,j+1,2)),F(0))

def second(poly):
    return sum((a*sum((moment(r) for r in range(j)),F(0))
                for j,a in enumerate(poly)),F(0))

def H(k):
    poly=[F(1)]
    for _ in range(k):poly=mul(poly,[1,-1,F(1,2)])
    value=factorial(k)*sum((poly[j]/factorial(k-j) for j in range(k+1)),F(0))
    derivative=factorial(k)*sum((poly[j]/factorial(k-1-j) for j in range(k)),F(0))
    assert value.denominator==derivative.denominator==1
    return int(value),int(derivative)

def vp(v,p):
    if v==0:return None
    v=F(v)
    a,b=abs(v.numerator),v.denominator
    out=0
    while a%p==0:a//=p;out+=1
    while b%p==0:b//=p;out-=1
    return out

rows=[]
for n in (2,8):
    polys=legendre_integer(n+1)
    P=[sum(poly) for poly in polys]
    Q=[second(poly) for poly in polys]
    for k in range(1,n+2):
        assert Q[k]==8*sum((F(P[j-1]*P[k-j],j) for j in range(1,k+1)),F(0))
    ell=lambda poly,j:sum((F(a,factorial(n+k+1-j)) for k,a in enumerate(poly)),F(0))
    t=[sum((F((-1)**k*(2*k+1),2**(2*k+1))*P[k]*ell(polys[k],j)
             for k in range(n+1)),F(0)) for j in (0,1)]
    E=lambda k:sum((F(1,factorial(j)) for j in range(k+1)),F(0))
    a=[-E(n-j)+sum((F((-1)**k*(2*k+1),2**(2*k+1))*Q[k]*ell(polys[k],j)
                   for k in range(n+1)),F(0)) for j in (0,1)]
    delta=t[1]-t[0]
    X=(1+t[1])*a[0]-(1+t[0])*a[1]
    h,_=H(n)
    hp,dp=H(n+1)
    K=F((n+1)*hp+dp,n+1)
    assert K.denominator==1
    K=int(K)
    R=[ell(polys[k],1) for k in (n,n+1)]
    T=[sum((a*E(n+j) for j,a in enumerate(polys[k])),F(0)) for k in (n,n+1)]
    assert R[0]==F(2**n*h,factorial(n)**2)
    assert R[1]==F(2**(n+1)*K,(n+1)*factorial(n)**2)
    Delta=(n+1)*P[n+1]*h-2*P[n]*K
    assert delta==F((-1)**n*Delta,2**(n+3)*factorial(n)**2)
    M=factorial(2*n+1)
    A=[M*(Q[k]+T[k-n]) for k in (n,n+1)]
    assert all(v.denominator==1 for v in A)
    A=list(map(int,A))
    N=2*K*A[0]-(n+1)*h*A[1]
    ratio=F(N,M*Delta)
    assert ratio==X/delta
    assert vp(Delta,3)==0
    assert vp(delta,3)==-2*vp(factorial(n),3)
    rows.append(dict(n=n,P_n=P[n],P_next=P[n+1],H_n=h,K_next=K,
                     Delta=Delta,M=M,A=A,N=N,
                     endpoint_ratio=str(ratio),actual_q=ratio.denominator,
                     v3_delta=vp(delta,3),v3_M=vp(M,3),v3_N=vp(N,3),
                     v3_actual_q=vp(ratio.denominator,3),
                     full_kernel_ratio_matches=True,all_identity_checks=True))
out=dict(scope="Only the previously used degrees2 and8; exact scalar sums, no solve.",
         all_checks_pass=True,rows=rows)
Path(__file__).with_name("hp_b1_adjacent_scalar_gate_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
