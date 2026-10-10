from fractions import Fraction as F
from math import factorial, comb
import json

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,m):
    b=[F(1)]
    for _ in range(m): b=mul(b,a)
    return b

def leg(m):
    u=power([1,-2,2],m)
    return [u[m+d]*F(factorial(m+d),factorial(m)*factorial(d)) for d in range(m+1)]

def aux(m):
    u=power([1,-1,F(1,2)],m)
    h=[F(factorial(m),factorial(j))*u[m-j] for j in range(m+1)]
    h0=sum(h); h1=sum(j*x for j,x in enumerate(h)); h2=sum(j*(j-1)*x for j,x in enumerate(h))
    return h0,m*h0+h1,m*(m-1)*h0+2*m*h1+h2

def moment(j):
    return sum((F(2*comb(j,k)*(-1)**(k//2),(k+1)*2**j) for k in range(0,j+1,2)),F(0))

def valuation(x):
    x=F(x)
    if not x: return None
    a,b=abs(x.numerator),x.denominator
    v=0
    while a%3==0: a//=3;v+=1
    while b%3==0: b//=3;v-=1
    return v

def residue(x):
    x=F(x)
    if x.denominator%3==0: return None
    return x.numerator*pow(x.denominator,-1,3)%3

def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]

rows=[]
for n in (4,5,7,8,10,11):
    ls=[leg(m) for m in range(n+2)]
    P,U=ls[n:n+2];a,b=sum(P),sum(U)
    k=(n+1)**2;f=F(2**n,factorial(n)**2)
    h,J,K=aux(n);eta,J1,K1=aux(n+1)
    S=J1*J1-eta*K1
    C=(J1-eta)*J-(K1-J1)*h
    W=J1*J-K1*h
    E=[];acc=F(0)
    for j in range(2*n+4):
        acc+=F(1,factorial(j));E.append(acc)
    def T(poly,j=0): return sum((x*E[n+d-j] for d,x in enumerate(poly)),F(0))
    def w(poly): return sum((sum(poly[i+1:])*moment(i) for i in range(len(poly)-1)),F(0))
    wp,wu=w(P),w(U)
    ps,us=wp+T(P),wu+T(U)
    D=k*b*C-2*a*S
    terms=[2*ps*S,-k*us*C,-2*f*eta*W]
    X=sum(terms)
    assert D.denominator==1 and D!=0
    ratio=X/D
    gamma=F((-1)**n,4*(n+1)**3*factorial(n)**4)
    # Independent raw reconstruction from the sum of orthogonal kernels.
    kernel=[[sum((F((-1)**m*(2*m+1),2**(2*m+1))*ls[m][i]*ls[m][j] for m in range(max(i,j),n+1)),F(0)) for j in range(n+1)] for i in range(n+1)]
    projected=[[-sum((kernel[i][d]/factorial(n+d+1-j) for d in range(n+1)),F(0)) for i in range(n+1)] for j in range(3)]
    alpha=[sum((x/factorial(n+d+1-j) for d,x in enumerate(U)),F(0)) for j in range(3)]
    B=cross(alpha,[1-sum(v) for v in projected])
    Q=[sum(B[j]*projected[j][i] for j in range(3)) for i in range(n+1)]
    CP=list(reversed(Q))
    be=mul(B,[F(1,factorial(j)) for j in range(2*n+3)])
    cf=mul(CP,[F(0)]+[moment(j) for j in range(2*n+2)])
    A=[-be[j]-cf[j] for j in range(n+1)]
    assert all(be[j]+cf[j]==0 for j in range(n+1,2*n+3))
    assert sum(B)==sum(CP)==gamma*D
    assert sum(A)==gamma*X
    assert sum(A)/sum(B)==ratio
    r=valuation(factorial(n))
    assert valuation(ratio.denominator)==max(0,2*r+valuation(D)-valuation(X/f))
    if n%3==1:
        assert residue(X/f)==1 and valuation(D)>=1
    if n==8:
        assert ratio.denominator==546183462792492116839296000
    rows.append({'n':n,'D':str(D),'X':str(X),'X_over_f':str(X/f),'reduced_ratio':str(ratio),'raw_A_endpoint':str(sum(A)),'raw_B_endpoint':str(sum(B)),'v3_n_factorial':r,'v3_D':valuation(D),'v3_X_over_f':valuation(X/f),'v3_q':valuation(ratio.denominator),'v3_S_C_W':[valuation(z) for z in (S,C,W)],'v3_normalized_numerator_terms':[valuation(z/f) for z in terms],'normalized_numerator_residue':residue(X/f),'v3_TP_over_f':valuation(T(P)/f),'v3_kTU_over_f':valuation(k*T(U)/f),'raw_reconstruction_checks':True})
print(json.dumps({'scope':'Six prescribed exact indices only; no general valuation theorem inferred','rows':rows},indent=2))