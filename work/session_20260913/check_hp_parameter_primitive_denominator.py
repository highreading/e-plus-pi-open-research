"""Exact controls of derived parameter leading coefficient and actual q valuations."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'math_packages'))
import sympy as S

b, t, u = S.symbols('b t u')

def monic(k, x):
    return S.expand(S.I**k*S.legendre(k, -S.I*(2*x-1))/S.binomial(2*k,k))

def norm(k):
    return 2*(-1)**k/((2*k+1)*S.binomial(2*k,k)**2)

def moment(k):
    return sum(S.binomial(k,j)*(-1)**(j//2)*S.Rational(2, (j+1)*2**k)
               for j in range(0,k+1,2))

def integrate(poly):
    return sum(c*moment(k) for (k,),c in S.Poly(poly,t).terms())

def endpoints(n):
    polys=[monic(k,t) for k in range(n+1)]
    V=0; J=0
    for k,pk in enumerate(polys):
        pk1=pk.subs(t,1)
        second=S.cancel((pk1-pk)/(1-t))
        V+=pk*pk1/norm(k)
        J+=pk*integrate(second)/norm(k)
    scale=(b+1)/2
    V=S.expand(scale*V.subs(t,1+scale*(t-1)))
    J=S.expand(scale*J.subs(t,1+scale*(t-1)))
    def ell(P,j):
        return S.expand(sum(c/S.factorial(n+k+1-j) for (k,),c in S.Poly(P,t).terms()))
    ts=[ell(V,j) for j in (0,1)]
    aa=[-sum(1/S.factorial(k) for k in range(n-j+1))+ell(J,j) for j in (0,1)]
    return S.expand((1+ts[1])*aa[0]-(1+ts[0])*aa[1]),S.expand(ts[1]-ts[0])

def vp(x,p):
    x=int(x)
    if not x:
        return None
    a=0
    while x%p==0:
        a+=1; x//=p
    return a

rows=[]
for n in (1,2,4):
    X,Y=endpoints(n)
    U=S.factorial(n)*S.assoc_laguerre(n,n,1)
    V=S.factorial(n)*S.assoc_laguerre(n-1,n+1,1)
    T=S.expand(n*U**2-n*U*V+V**2)
    lc=(-1)**(n+1)*T/(n*2**(2*n+2)*S.factorial(n)**4)
    assert T>0 and S.denom(T)==1
    assert S.Poly(X,b).degree()==2*n+1
    assert S.Poly(X,b).LC()==lc
    assert X.subs(b,-1)==-1/S.factorial(n) and Y.subs(b,-1)==0
    p=int(S.nextprime(2*n+1))
    while int(T)%p==0:
        p=int(S.nextprime(p))
    controls=[]
    for value,expected in ((S.Rational(1,p),n),(S.Rational(1,p*p),2*n),(S.Integer(p-1),1)):
        assert Y.subs(b,value)!=0
        ratio=S.cancel(X.subs(b,value)/Y.subs(b,value))
        valuation=vp(S.denom(ratio),p)
        assert valuation>=expected
        controls.append({'beta':str(value),'p':p,'actual_vp_q':valuation,'proved_lower_bound':expected})
    rows.append({'n':n,'U':str(U),'V':str(V),'T':str(T),'leading_X':str(lc),
                 'degree_X':S.Poly(X,b).degree(),'degree_Y':S.Poly(Y,b).degree(),
                 'actual_reduced_denominator_controls':controls})

out={'status':'all exact controls passed','rows':rows,
     'scope':'finite normalization controls only; the all-degree proof is in the accompanying note'}
Path(__file__).with_name('hp_parameter_primitive_denominator_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
