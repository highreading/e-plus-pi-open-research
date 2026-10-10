"""Independent integer controls for the ten selected arithmetic manuscripts.

Author: /root/literature_map.  This file uses standard-library integer and
rational arithmetic only.  It does not import or run any archived program.
Finite checks support normalization/sign bookkeeping, not infinite proofs.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial, comb, gcd, lcm
from itertools import combinations
import json
import hashlib
import time

OUT = Path(__file__).resolve().parent

def det(A):
    """Bareiss elimination with row pivots and checked exact division."""
    n=len(A)
    if n==0:
        return 1
    a=[list(r) for r in A]
    assert all(len(r)==n for r in a)
    sign=1
    previous=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if pivot is None:
                return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        d=a[k][k]
        for i in range(k+1,n):
            x=a[i][k]
            for j in range(k+1,n):
                value=d*a[i][j]-x*a[k][j]
                q,r=divmod(value,previous)
                assert r==0
                a[i][j]=q
            a[i][k]=0
        previous=d
    return sign*a[-1][-1]

def row(k,degree,fac):
    B=[fac[k]//fac[k-j] for j in range(degree+1)]
    C=[]
    for j in range(degree+1):
        r=k-j
        assert r>0
        C.append(0 if r%2==0 else (-1)**((r-1)//2)*(fac[k]//r))
    return B+C

def content(values):
    d=0
    for v in values:
        d=gcd(d,abs(v))
    return d

def omitted_row_minors(A):
    return [det(A[:r]+A[r+1:]) for r in range(len(A))]

def vp(n,p):
    if n==0:
        return 'infinity'
    n=abs(n)
    e=0
    while n%p==0:
        n//=p
        e+=1
    return e

def tau(r):
    return Fraction(0) if r<=0 or r%2==0 else Fraction((-1)**((r-1)//2),r)

def one_degree(n,p=None,m=None,nu=None):
    fac=[factorial(k) for k in range(3*n+1)]
    X=[row(k,n-1,fac) for k in range(n,3*n+1)]
    u=[(-1)**r*v for r,v in enumerate(omitted_row_minors(X))]
    F=content(u)
    assert F>0
    w=[v//F for v in u]
    assert content(w)==1
    assert all(sum(w[i]*X[i][j] for i in range(2*n+1))==0 for j in range(2*n))
    H=[row(k,n,fac) for k in range(n+1,3*n+1)]
    Be=[1]*(n+1)+[0]*(n+1)
    Ce=[0]*(n+1)+[1]*(n+1)
    E=det(H+[Be,Ce])
    Q=[0]*(2*n+1)
    for i,k in enumerate(range(n,3*n+1)):
        Q[3*n-k]=fac[k]//fac[n]*w[i]
    Z=sum(Q)
    assert E==(-1)**n*F*Z and Z!=0
    Pe=[]
    Pa=[]
    for d in range(2*n+1):
        j=3*n-d
        pe=sum((fac[j]//fac[n])*comb(k,j)*w[k-n] for k in range(j,3*n+1))
        pa=sum((fac[j]//fac[n])*comb(k,j)*fac[k-j-1]*(-1)**((k-j-1)//2)*w[k-n]
               for k in range(j+1,3*n+1) if (k-j)%2==1)
        Pe.append(pe)
        Pa.append(pa)
    N=sum(Pe)+4*sum(Pa)
    endpoint_gcd=gcd(abs(N),abs(Z))
    q=abs(Z)//endpoint_gcd
    cQ=content(Q)
    assert Z%cQ==0
    dII=abs(Z)//cQ
    J=H+[[c-4*b for b,c in zip(Be,Ce)]]
    Arow=[]
    for kind in ['B','C']:
        for j in range(n+1):
            value=-fac[n]*sum((Fraction(1,fac[t-j]) if kind=='B' else tau(t-j))
                               for t in range(j,n+1))
            assert value.denominator==1
            Arow.append(value.numerator)
    DeltaA=det(J+[Arow])
    DeltaB=det(J+[Be])
    assert DeltaB==-E
    assert DeltaA==(-1)**n*fac[n]*F*N
    assert gcd(abs(DeltaA),fac[n]*abs(DeltaB))==fac[n]*F*endpoint_gcd
    assert Fraction(DeltaA,fac[n]*DeltaB)==Fraction(-N,Z)
    # A second route builds the actual integer finite-difference matrix.
    G=[[sum((-1)**(n-s)*comb(n,s)*X[r+s][n+j] for s in range(n+1))
        for j in range(n)] for r in range(n+1)]
    Vprod=1
    for j in range(n):
        Vprod*=fac[j]
    theta=content(omitted_row_minors(G))
    assert F==Vprod*theta
    L=lcm(*range(1,3*n+1))
    ZZ=[]
    for r in range(n+1):
        rr=[]
        for j in range(n):
            a,b=divmod(L*G[r][j],fac[n+r])
            assert b==0
            rr.append(a)
        ZZ.append(rr)
    delta=omitted_row_minors(ZZ)
    Theta=content(delta)
    c=[fac[2*n]//fac[n+r] for r in range(n+1)]
    h=content([c[r]*delta[r] for r in range(n+1)])
    R=fac[2*n]//fac[n]
    assert h>0 and Theta>0
    ww=[]
    for t in range(2*n+1):
        value=(-1)**t*sum(comb(n,t-r)*c[r]*delta[r] for r in range(n+1) if 0<=t-r<=n)
        a,b=divmod(value,h)
        assert b==0
        ww.append(a)
    assert ww==w
    P=[0]*(2*n+1)
    for r in range(n+1):
        for s in range(n+1):
            P[2*n-r-s]+=(-1)**(r+s)*comb(n,s)*delta[r]*fac[n+r+s]//fac[n+r]
    assert all(h*Q[j]==R*P[j] for j in range(2*n+1))
    assert content(P)==Theta
    K=sum(P)
    assert h*Z==R*K
    assert cQ*h==R*Theta
    assert dII==abs(K)//Theta and K%Theta==0
    D=None
    eta=None
    if n<=7:
        D=content(det([[rr[j] for j in cols] for rr in H])
                  for cols in combinations(range(2*n+2),2*n))
        GH=[[sum((-1)**(n+1-s)*comb(n+1,s)*H[r+s][n+1+j] for s in range(n+2))
             for j in range(n+1)] for r in range(n-1)]
        eta=1 if n==1 else content(det([[rr[j] for j in cols] for rr in GH])
                                  for cols in combinations(range(n+1),n-1))
        for large in [11,17,23,31]:
            if large>3*n:
                assert vp(D,large)==vp(eta,large)
                assert vp(F,large)==vp(theta,large)
                assert vp(D,large)<=vp(F,large)
    local=None
    if p is not None:
        assert nu>=1 and 3*m<p and n==m*p**nu
        expectedF=2*n*(n-m)//(p-1)-2*nu*n
        expectedR=(n-m)//(p-1)
        assert vp(delta[-1],p)==0 and vp(h,p)==0 and vp(Theta,p)==0
        assert vp(F,p)==expectedF and vp(cQ,p)==expectedR
        assert vp(Z,p)==expectedR+vp(K,p)
        if n>p:
            assert N%p!=0 and vp(q,p)==vp(Z,p)
        else:
            assert n==p
            ep=Fraction(delta[-1],h)
            assert ep.denominator%p!=0
            epmod=ep.numerator*pow(ep.denominator,-1,p)%p
            chi=(-1)**((p-1)//2)
            assert sum(Pe)%p==epmod
            assert sum(Pa)%p==2*chi*epmod%p
            assert N%p==(1+8*chi)*epmod%p
        local={'p':p,'m':m,'nu':nu,'vF':vp(F,p),'vcQ':vp(cQ,p),'vK':vp(K,p),
               'vZ':vp(Z,p),'vN':vp(N,p),'vq':vp(q,p),'vdII':vp(dII,p),
               'delta_n_mod_p':delta[-1]%p,'h_mod_p':h%p,'Theta_mod_p':Theta%p}
    return {'n':n,'F':str(F),'D':str(D) if D is not None else None,
            'eta':str(eta) if eta is not None else None,'theta':str(theta),
            'signed_cofactor_vector_u':[str(x) for x in u],'primitive_w':[str(x) for x in w],
            'Qhat_coefficients_low_to_high':[str(x) for x in Q],
            'Pe_coefficients_low_to_high':[str(x) for x in Pe],
            'Pa_coefficients_low_to_high':[str(x) for x in Pa],
            'Z':str(Z),'N':str(N),'endpoint_gcd':str(endpoint_gcd),'q':str(q),'cQ':str(cQ),'dII':str(dII),
            'E':str(E),'DeltaA':str(DeltaA),'DeltaB':str(DeltaB),'L':str(L),
            'normalized_Z_matrix':[[str(x) for x in r] for r in ZZ],
            'delta':[str(x) for x in delta],'h':str(h),'Theta':str(Theta),'R':str(R),'K':str(K),
            'all_checked_equalities_passed':True,'saturated_prime_control':local}

def A(n):
    return sum(comb(n,2*j)*comb(2*j,j)*2**(n-j) for j in range(n//2+1))

started=time.monotonic()
rows=[]
for n,p,m,nu in [(7,7,1,1),(25,5,1,2)]:
    r=one_degree(n,p,m,nu)
    rows.append(r)
    print(json.dumps({'n':n,'checks_passed':True,'local':r['saturated_prime_control']},ensure_ascii=False),flush=True)
ray=[]
for m,p in [(1,3),(7,5)]:
    q2=(2**(p-1)-1)//p
    expected=Fraction(A(m))*(1+Fraction(m*p*q2,2))
    diff=Fraction(A(m*p))-expected
    assert diff.denominator%p!=0 and diff.numerator%(p*p)==0
    ray.append({'m':m,'p':p,'A_m':str(A(m)),'A_mp':str(A(m*p)),
                'A_mp_mod_p2':A(m*p)%(p*p),'q_p_2':q2,'all_m_mod_p2_identity_checked':True})
# Linear algebra counterexample to the unsupported implication
# "augmented shared core is saturated => original high content is a unit".
# It is explicitly not an actual Taylor-family counterexample.
p=5
e=4
toyH=[[0,1,0,0],[p**e,0,0,0]]
toycore=[[p**e,0,0,0,1,0]]
toyD=content(det([[rr[j] for j in cols] for rr in toyH]) for cols in combinations(range(4),2))
toyzeta=content(toycore[0])
assert toyD==p**e and toyzeta==1
report={'author':'/root/literature_map','scope':'Independent finite integer controls only; infinite proofs are in the Chinese report.',
        'archived_research_code_imported_or_executed':False,'network_used':False,
        'elapsed_seconds':time.monotonic()-started,'degrees':rows,'coefficient_ray_mod_p2_controls':ray,
        'generic_nonimplication_counterexample':{'actual_Taylor_family_example':False,'p':p,'e':e,
              'H':toyH,'augmented_shared_core':toycore,'high_content':toyD,'augmented_content':toyzeta},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'all_assertions_passed':True}
(OUT/'INDEPENDENT_EXACT_CONTROLS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_assertions_passed':True,'elapsed_seconds':report['elapsed_seconds'],'output':str(OUT/'INDEPENDENT_EXACT_CONTROLS.json')},ensure_ascii=False))
