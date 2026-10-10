"""Original bounded arithmetic reconnaissance for the new linear center.

These small cases do not instantiate the proportional asymptotic domain.
The exact complete rational lift, not a pure logarithmic companion, is used.
"""
from fractions import Fraction as Q
from math import factorial, comb, gcd, lcm, log
from functools import reduce
import json
import sympy as sp


def full_lift(n, b):
    d=b-1
    qp=[Q(1)]
    for _ in range(n):
        new=[Q(0)]*(len(qp)+2)
        for j,a in enumerate(qp):
            new[j]+=a;new[j+1]-=a;new[j+2]+=a/2
        qp=new
    maxjet=2*n+d
    ainv=[Q(1),Q(1)]
    for j in range(2,maxjet):
        ainv.append(ainv[-1]-ainv[-2]/2)
    fcoef=[Q(0)]+[2*ainv[j-1]/j for j in range(1,maxjet+1)]
    hq=[];acc=Q(0)
    for j in range(maxjet+1):
        acc+=Q(1,factorial(j))+fcoef[j];hq.append(acc)
    ecoef=[sum((a/Q(factorial(k-j)) for j,a in enumerate(qp) if j<=k),Q(0))
           for k in range(n+d+1)]
    T=sp.Matrix(b,b,lambda i,j:ecoef[n+i-j] if n+i-j>=0 else 0)
    fp=[];fq=[]
    for i in range(b):
        r=n+i
        fp.append(factorial(n)*sum((a*comb(n+r-j,n) for j,a in enumerate(qp) if j<=r),Q(0)))
        fq.append(sum((a*Q(factorial(n+r-j),factorial(r-j))*hq[n+r-j]
                       for j,a in enumerate(qp) if j<=r),Q(0)))
    H=T.inv()*sp.Matrix.hstack(sp.Matrix(fp),sp.Matrix(fq))
    S=sp.zeros(b,b)
    for j in range(b):
        for k in range(j,b):
            S[j,k]=(-1)**(k-j)*comb(n+k-j-1,k-j)*factorial(k)//factorial(j)
    Z=sp.zeros(b+1,b)
    for j in range(b):Z[j,j]=-1;Z[j+1,j]=1
    Psi=Z*S*H;Psi[0,1]+=1
    db=lcm(*(int(x.q) for x in Psi))
    U=[int(Psi[j,0]*db) for j in range(b+1)]
    V=[int(Psi[j,1]*db) for j in range(b+1)]
    assert sum(U)==0 and sum(V)==db
    assert reduce(gcd,U+V)==1
    return U,V,db


def at(coef,x):
    ans=0
    for a in reversed(coef):ans=ans*x+a
    return ans


def primeval(a,p):
    if a==0:return None
    ans=0
    while a%p==0:a//=p;ans+=1
    return ans


out=[]
for n,b in [(12,4),(20,5),(30,7)]:
    U,V,db=full_lift(n,b)
    gfix=reduce(gcd,[at(P,x) for P in [U,V] for x in range(b+1)])
    assert factorial(b)%gfix==0 and db%gfix==0
    tdata=[]
    for t in [1,2,3,4,7,15]:
        u,v=at(U,-t),at(V,-t);gg=gcd(u,v)
        tdata.append(dict(t=t,gcd=str(gg),q=str(abs(u)//gg),
                          q_log=float(log(abs(u)//gg)),
                          vp_gcd={str(p):primeval(gg,p) for p in [2,3,5,7,11]}))
    primes=[]
    for p in [2,3,5,7,11]:
        roots=[x for x in range(p) if at(U,x)%p==0 and at(V,x)%p==0]
        primes.append(dict(p=p,common_roots=roots,
                           u_content_vp=primeval(reduce(gcd,U),p),
                           v_content_vp=primeval(reduce(gcd,V),p),
                           d_B_vp=primeval(db,p)))
    out.append(dict(n=n,b=b,proportional_domain_instantiated=False,
                    U=[str(x) for x in U],V=[str(x) for x in V],d_B=str(db),
                    gfix=str(gfix),u_content=str(reduce(gcd,U)),
                    v_content=str(reduce(gcd,V)),negative_evaluations=tdata,
                    small_prime_common_roots=primes))
with open('negative_evaluation_content_probe.json','w') as f:
    json.dump(out,f,indent=2)
for r in out:
    print(json.dumps(dict(n=r['n'],b=r['b'],gfix=r['gfix'],
                         content_digits=[len(r['u_content']),len(r['v_content'])],
                         roots=r['small_prime_common_roots'],
                         negative_q_logs=[(x['t'],round(x['q_log'],3)) for x in r['negative_evaluations']])) )
