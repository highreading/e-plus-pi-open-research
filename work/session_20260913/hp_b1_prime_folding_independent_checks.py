"""Selected exact HP prime-folding checks; no scan or asymptotic inference."""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json


def add(a,b):
    return [(a[k] if k<len(a) else 0)+(b[k] if k<len(b) else 0) for k in range(max(len(a),len(b)))]


def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c


def objects(n):
    ps=[[F(1)],[F(-1,2),F(1)]]
    for k in range(1,n):ps.append(add(mul(ps[-1],[F(-1,2),F(1)]),[F(k*k,4*(4*k*k-1))*v for v in ps[-2]]))
    ps=ps[:n+1]
    K=[[F(0)]*(n+1) for _ in range(n+1)]
    for k,pk in enumerate(ps):
        norm=F(2*(-1)**k,(2*k+1)*comb(2*k,k)**2)
        for a,v in enumerate(pk):
            for b,w in enumerate(pk):K[a][b]+=v*w/norm
    Cstar=[];t=[];aa=[]
    moments=[sum((F(2*comb(k,j)*(-1)**(j//2),(j+1)*2**k) for j in range(0,k+1,2)),F(0)) for k in range(n)]
    Fseries=[F(0)]+moments
    for j in (0,1):
        cs=[-sum((K[a][b]/factorial(n+b+1-j) for b in range(n+1)),F(0)) for a in range(n+1)]
        Cstar.append(cs);t.append(-sum(cs))
        C=list(reversed(cs));g=sum(mul(C,Fseries)[:n+1])
        aa.append(-sum((F(1,factorial(k)) for k in range(n-j+1)),F(0))-g)
    X=(1+t[1])*aa[0]-(1+t[0])*aa[1];Y=t[1]-t[0]
    return dict(K=K,X=X,Y=Y,q=(X/Y).denominator if Y else None)


def red(v,p):
    v=F(v)
    assert v.denominator%p
    return v.numerator*pow(v.denominator,-1,p)%p


def legendre_z(k):
    return [(-1)**j*comb(k,j)*comb(k+j,j) for j in range(k+1)]


def harmonic(j,p):
    return sum(pow(k,-1,p) for k in range(1,j+1))%p


def run():
    boundary=[]
    for p in [3,5,7,11]:
        n=p-1;data=objects(n);chi=(-1)**((p-1)//2)
        for a in range(p):
            for b in range(p):
                expected=chi*pow(2,-1,p)*((-1)**b*comb(p-1,b) if a+b==p-1 else 0)%p
                assert red(data['K'][a][b]/p,p)==expected
        delta=red(data['Y'],p)
        assert delta==(-chi*pow(2,-1,p))%p and data['q']%p
        assert data['X'].denominator%p
        boundary.append(dict(n=n,p=p,delta_mod_p=delta,q=str(data['q']),prime_excluded=True))
    defects=[]
    for p,k in [(5,0),(5,1),(7,0),(7,2),(11,1),(11,4)]:
        low=legendre_z(k);high=legendre_z(p-1-k)
        for j,c in enumerate(high):
            difference=c-(low[j] if j<len(low) else 0)
            assert difference%p==0
            if j<=k:
                predicted=low[j]*(harmonic(k-j,p)-harmonic(k+j,p))%p
            else:
                predicted=(-1)**k*factorial(k+j)*factorial(j-k-1)*pow(factorial(j)**2,-1,p)%p
            assert difference//p%p==predicted
        defects.append(dict(p=p,k=k,degree=p-1-k,all_coefficients_checked=True))
    offsets=[]
    for p,h in [(5,2),(7,2),(11,2),(13,2),(7,3),(11,3)]:
        n=p-h;m=h-2;data=objects(n);low=objects(m)['K']
        E=[];Klow=[]
        for b in range(n+1):
            kn=sum(data['K'][a][b] for a in range(n+1))
            km=sum(low[a][b] for a in range(m+1)) if b<=m else F(0)
            E.append(red((kn-km)/p,p));Klow.append(red(km,p))
        gate=sum(Klow[b]*(-1)**(h-b)*(h-b)*factorial(h-b-2) for b in range(h-1))
        gate+=sum((1-d)*E[h-1+d]*pow(factorial(d),-1,p) for d in range(p-2*h+2))
        assert gate%p==red(data['Y'],p)
        qq=data['q']; exponent=0
        if qq:
            while qq%p==0:exponent+=1;qq//=p
        offsets.append(dict(n=n,p=p,h=h,delta_gate_mod_p=gate%p,X_mod_p=red(data['X'],p),q=str(data['q']),valuation_q=exponent))
    return dict(status='PASS',scope='Selected exact checks support symbolic proofs; no prime scan or uniform nonvanishing inferred.',
                n_equals_p_minus_one=boundary,explicit_harmonic_defects=defects,fixed_offset_gates=offsets)


if __name__=='__main__':
    data=run();Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(dict(status=data['status'],boundary_cases=len(data['n_equals_p_minus_one']),harmonic_defects=len(data['explicit_harmonic_defects']),offset_checks=len(data['fixed_offset_gates']))))
