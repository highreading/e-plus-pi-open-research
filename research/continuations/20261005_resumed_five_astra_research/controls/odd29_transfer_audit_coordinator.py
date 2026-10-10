"""Personally authored odd-prime sign, reset and complete auxiliary transfer audit."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,gcd,lcm
import json,hashlib
import sympy as sp
from scalar_displacement_audit_coordinator import qpower,rational
ROOT=Path(__file__).resolve().parent
p=29;K=2;mod=p**K
def rs(x):
    x=F(x);assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,mod)%mod
def matres(A):return [[rs(x) for x in A.row(i)] for i in range(A.rows)]
def mm(A,B,q=mod):return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*B)] for row in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mpow(A,e,q=mod):
    R=eye(len(A))
    while e:
        if e&1:R=mm(R,A,q)
        A=mm(A,A,q);e//=2
    return R
def rec(n,i,q=mod):
    return [[(2*n+2*i+1)%q,rs(-F((n+i)*(n+3*i-1),2))%q,
             rs(-F((n+i)*(n+i-1)*(1-i),2))%q],[1,0,0],[0,1,0]]
def reset_checks():
    rows=[];Pi=p**K*lcm(p-1,p*p-1,p**3-1)
    for n in (29,203,191110):
        for phase in (2,28,29,mod-1):
            B=eye(3)
            for i in range(phase,phase+mod):B=mm(rec(n,i),B)
            assert mpow(B,3*K+Pi)==mpow(B,3*K)
            small=eye(3)
            for i in range(phase,phase+p):small=mm(rec(n,i,p),small,p)
            rank=sp.Matrix(small).rank() if False else None
            # Test modular rank one by all2x2minors, not rational rank.
            assert any(any(x for x in row) for row in small)
            assert all((small[i][j]*small[k][l]-small[i][l]*small[k][j])%p==0
                       for i in range(3) for k in range(i+1,3) for j in range(3) for l in range(j+1,3))
            rows.append({'n_prefix':n,'phase':phase,'mod29_rank':1,'mod29_trace':sum(small[i][i] for i in range(3))%p,
                         'mod841_power_quotient_pass':True})
    assert mm(rec(29,30,p),rec(29,29,p),p)==[[2,0,0],[1,0,0],[1,0,0]]
    return rows
def units():
    out=[]
    for kk in (1,2):
        q=p**kk;pref=[1]
        for i in range(1,q):pref.append(pref[-1]*(i if i%p else 1)%q)
        def uf(N):
            digits=[];v=N
            while v:digits.append(v%p);v//=p
            sign=sum((h-kk+1)*digits[h] for h in range(kk,len(digits)))%2
            result=(-1)**sign
            for ell in range(len(digits)):
                w=sum(digits[ell+r]*p**r for r in range(kk) if ell+r<len(digits))
                result=result*pref[w]%q
            return result%q
        def dep(N):
            s=0
            while N:N//=p;s+=N
            return s
        checks=0
        for N in list(range(128))+[168,257,840,841,842,1681,1682,1685]:
            js=range(N+1) if N<128 else sorted(set(list(range(65))+[N//2,N-29,N-1,N]))
            for j in js:
                e=dep(N)-dep(j)-dep(N-j)
                got=0 if e>=kk else p**e*uf(N)*pow(uf(j),-1,q)*pow(uf(N-j),-1,q)%q
                assert got==comb(N,j)%q;checks+=1
        assert uf(29)==factorial(29)//29%q
        out.append({'precision':kk,'sign_sensitive_binomial_checks':checks})
    assert comb(58,29)%29==2 and (comb(841,29)//29)%29==1
    return out
def contact():
    n,b=29,4;pol=qpower(n);pp=qpower(n+1);fac=[factorial(i) for i in range(2*n+b+3)]
    def fall(N,s):return F(fac[N],fac[N-s])
    Nt=sp.Matrix(b,b,lambda i,j:rational(sum((pol[s]*fall(n+i,s)*comb(n+i-s,j)
                      for s in range(min(2*n,n+i-j)+1)),F(0))))
    U=sp.Matrix(b,b,lambda i,j:comb(n,j-i) if j>=i else 0)
    A=Nt*U;P0=sp.Matrix(b,b,lambda i,j:comb(n+i,j))
    Lin=sp.Matrix(b,b,lambda i,j:comb(i,j) if j<=i else 0)
    assert P0==Lin*U
    m=57
    H=[[rs(pol[k-j]*F(fac[k],fac[j])) if 0<=k-j<=m else 0 for j in range(b)] for k in range(b)]
    Ktail=[[rs(pol[b+r-j]*F(factorial(b+r),fac[j])) if 1<=b+r-j<=m else 0 for j in range(b)] for r in range(m)]
    def neg(d):return (-1)**d*comb(n+d-1,d) if d>=0 else 0
    Ft=[[-sum(neg(b+v-j)*(comb(n,r-v) if r-v<=n else 0) for v in range(r+1))%mod for r in range(m)] for j in range(b)]
    tail=mm(Ft,Ktail);J=[[(H[i][j]+tail[i][j])%mod for j in range(b)] for i in range(b)]
    assert mm(mm(mm(matres(Lin),matres(U)),J),matres(U))==matres(A)
    E=Nt-P0;assert all(rs(x)%p==0 for x in E)
    Ai=matres(A.inv());word=matres(U.inv()*(P0.inv()-P0.inv()*E*P0.inv()))
    assert word==Ai
    source=[sum((pp[s]*fall(n+i,s)*comb(2*n+i+1-s,b)
                    for s in range(min(2*n+2,n+i)+1)),F(0)) for i in range(1,b-1)]
    def hs(a0,a1,forced):
        v=[F(a0),F(a1)]
        for i in range(1,b-1):
            beta=F((n+i)*(n+3*i-1),2);gamma=F((n+i)*(n+i-1)*(1-i),2)
            v.append((2*n+2*i+1)*v[i]-beta*v[i-1]-(gamma*v[i-2] if i>=2 else 0)+(source[i-1] if forced else 0))
        return sp.Matrix([rational(x) for x in v])
    W=sp.diag(*[comb(n+2,j) for j in range(b+1)])
    C=sp.Matrix(b+1,b,lambda j,k:(j if k==j-1 else 0)-(1 if k==j else 0));R=W*C
    B=R*A.inv()*sp.Matrix.hstack(hs(1,0,False),hs(0,1,False),hs(0,0,True))
    B[b,2]+=W[b,b]
    ell=sp.Matrix([F(factorial(n+2-j),factorial(n+2-b)) for j in range(b+1)])
    S=(ell.T*ell)[0];assert rs(S)%p==2
    assert ell.T*B==sp.Matrix([[0,0,W[b,b]]])
    G=B.T*B-sp.diag(0,0,W[b,b]**2/S)
    gm=matres(G);assert [[x%p for x in row] for row in gm]==[[21,19,0],[19,5,0],[0,0,0]]
    return {'n':n,'b':b,'precision':K,'matrix_factorization_zero':True,'finite_word_inverse_zero':True,
            'true_endpoint_and_projection_charges':True,'auxiliary_projection_scalar_mod29':rs(S)%p,'projected_gram_mod841':gm,
            'scope':'Auxiliary contact system; no original-family relative norm law'}
if __name__=='__main__':
    out={'status':'PASS','scope':'Bounded odd-prime unit, monodromy and auxiliary endpoint-exact contact checks',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'units':units(),'recurrence_quotient':reset_checks(),'contact':contact()}
    (ROOT/'odd29_transfer_audit_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)
