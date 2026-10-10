from fractions import Fraction as F
from math import factorial
import json

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def power(a,n):
    out=[F(1)]
    for _ in range(n): out=mul(out,a)
    return out

def fall(a,t):
    if t>a: return 0
    return factorial(a)//factorial(a-t)

def aux(a):
    c=power([F(1),F(-1),F(1,2)],a)
    ds=[sum((fall(a,t+d)*v for t,v in enumerate(c)),F(0)) for d in range(3)]
    h,u,v=ds
    return h,a*h+u,a*(a-1)*h+2*a*u+v,c,ds

def rod(a):
    p=power([F(1),F(-2),F(2)],a)
    return [p[a+d]*F(factorial(a+d),factorial(d)*factorial(a)) for d in range(a+1)]

def moment(j):
    re,im=1,0
    for _ in range(j+1): re,im=re-im,re+im
    return F(2*im,2**j*(j+1))

def divided_moment(p):
    # Exact synthetic division of p(t)-p(1) by t-1.
    acc=F(0); out=F(0)
    for d in range(len(p)-1,0,-1):
        acc+=p[d]
        out+=acc*moment(d-1)
    return out

def residue(x,mod):
    x=F(x)
    assert x.denominator%5
    return (x.numerator*pow(x.denominator,-1,mod))%mod

def valuation(x):
    x=F(x)
    if not x: return 'infinity'
    a,b=abs(x.numerator),x.denominator
    v=0
    while a%5==0: a//=5; v+=1
    while b%5==0: b//=5; v-=1
    return v

rows=[]
for n in [9,14,19,24,29,34]:
    m=n+1
    hn,Jn,Kn,cn,dn=aux(n)
    h,J,K,cm,dm=aux(m)
    P,U=rod(n),rod(m)
    partial=[F(1)]
    for t in range(1,2*m+1): partial.append(partial[-1]+F(1,factorial(t)))
    TP=sum((v*partial[n+d] for d,v in enumerate(P)),F(0))
    TU=sum((v*partial[n+d] for d,v in enumerate(U)),F(0))
    wp,wu=divided_moment(P),divided_moment(U)
    f=F(2**n,factorial(n)**2)
    S=J*J-h*K
    C=(J-h)*Jn-(K-J)*hn
    W=J*Jn-K*hn
    D=m*m*sum(U)*C-2*sum(P)*S
    X=2*(TP+wp)*S-m*m*(TU+wu)*C-2*f*h*W
    Z=X/(f*m)
    E=2*(TP/f)*(S/m)-(m*TU/f)*C-2*h*(W/m)
    M=2*(wp/f)*(S/m)-(m*wu/f)*C
    assert Z==E+M
    j=J/m; k=K/m
    jj=h+sum((fall(m-1,t)*v for t,v in enumerate(cm)),F(0))
    kk=(m-1)*h+2*dm[1]+sum((fall(m-1,t+1)*v for t,v in enumerate(cm)),F(0))
    assert (j,k)==(jj,kk)
    ee=[factorial(t)*partial[t] for t in range(len(partial))]
    AA=sum((fall(n,t)*cn[t]*ee[2*n-t] for t in range(n+1)),F(0))
    BB=4*ee[2*m-1]+2*sum((fall(m-1,t-1)*cm[t]*(2*m-t)*ee[2*m-1-t] for t in range(1,m+1)),F(0))
    assert AA==TP/f and BB==m*TU/f
    assert E==2*AA*(m*j*j-h*k)-BB*C-2*h*(j*Jn-k*hn)
    q=(-X/D).denominator
    rows.append({'n':n,'E_mod25':residue(E,25),'M_mod25':residue(M,25),'Z_mod25':residue(Z,25),'M_mod125':residue(M,125),'Z_mod125':residue(Z,125),'v5_M':valuation(M),'v5_Z':valuation(Z),'v5_D':valuation(D),'v5_q':valuation(q),'exact_identity_checks':'passed'})
print(json.dumps(rows,indent=2))