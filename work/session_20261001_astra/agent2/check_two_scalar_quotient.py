"""Exact contraction checks at the four frozen indices; no HP solve or scan."""
import hashlib
import json
from functools import reduce
from math import gcd
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent2')
SOURCE = BASE / 'growing_regime_certificates.json'
source_bytes = SOURCE.read_bytes()
frozen = json.loads(source_bytes)
assert [r['n'] for r in frozen['records']] == [4, 6, 8, 10]
t = s.Symbol('t')
E, PI = s.symbols('E PI')

def monic(k):
    integer_legendre = sum(s.binomial(k,j)*s.binomial(2*k-2*j,k)*(2*t-1)**(k-2*j) for j in range(k//2+1))
    return s.expand(integer_legendre/(2**k*s.binomial(2*k,k)))

def ell(poly,n,j):
    return sum(c/s.factorial(n+k+1-j) for (k,),c in s.Poly(poly,t).terms())

def partial_row(poly,n,b):
    return [sum(c*sum(s.Rational(1,s.factorial(r)) for r in range(n+k-j+1)) for (k,),c in s.Poly(poly,t).terms()) for j in range(b+1)]

def moment(poly):
    result = 0
    for (k,),c in s.Poly(poly,t).terms():
        mu = sum(s.binomial(k,j)*s.I**j*s.Rational(2,j+1)/2**k for j in range(0,k+1,2))
        result += c*mu
    return s.simplify(result)

records=[]
for old in frozen['records']:
    n,b=old['n'],old['b']
    assert b==n//2
    ps=[monic(k) for k in range(n+b+1)]
    h=s.Rational(2*(-1)**n,(2*n+1)*s.binomial(2*n,n)**2)
    A0,A1=ps[n].subs(t,1),ps[n+1].subs(t,1)
    high=s.Matrix([[ell(ps[n+l],n,j) for j in range(b+1)] for l in range(1,b)])
    integer_rows=[]
    row_contents=[]
    row_product=s.S.One
    for l in range(1,b):
        factor=s.factorial(2*n+2*l)
        row=[s.cancel(factor*high[l-1,j]) for j in range(b+1)]
        assert all(x.is_Integer for x in row)
        content=reduce(gcd,[abs(int(x)) for x in row])
        assert content>0
        integer_rows.append([x/content for x in row])
        row_contents.append(content)
        row_product*=factor
    primitive_rows=s.Matrix(integer_rows)
    minors={}
    for i in range(b+1):
        for j in range(i+1,b+1):
            cols=[k for k in range(b+1) if k not in (i,j)]
            minors[i,j]=(-1)**(i+j+1)*primitive_rows[:,cols].det()
    minor_content=reduce(gcd,[abs(int(x)) for x in minors.values()])
    assert minor_content>0
    primitive_minors={ij:x/minor_content for ij,x in minors.items()}
    gamma=s.prod(row_contents)*minor_content/row_product
    def Bbar(x,y):
        return s.expand(sum(m*(x[i]*y[j]-x[j]*y[i]) for (i,j),m in primitive_minors.items()))
    def Bform(x,y):
        return s.expand(gamma*Bbar(x,y))
    e=[s.S.One]*(b+1)
    TU=partial_row(ps[n+1],n,b)
    TP=partial_row(ps[n],n,b)
    Z0=-Bbar(e,TU)
    Z1=-Bbar(e,TP)
    ZK=Bbar(TU,TP)
    z0,z1=gamma*Z0,gamma*Z1
    assert z0==-s.Matrix(high.tolist()+[e,TU]).det()
    assert z1==-s.Matrix(high.tolist()+[e,TP]).det()
    assert z0.is_Rational and z1.is_Rational
    d=s.cancel(A1*z1-A0*z0)
    DV=s.cancel(d/h)
    assert DV==s.Rational(old['D_V'])
    assert -DV==s.Rational(old['cofactor_Y'])
    Vpoly=s.expand(sum(ps[k].subs(t,1)*ps[k]/s.Rational(2*(-1)**k,(2*k+1)*s.binomial(2*k,k)**2) for k in range(n+1)))
    vrow=[ell(Vpoly,n,j) for j in range(b+1)]
    assert Bform(e,vrow)==DV
    w0=moment(s.cancel((ps[n]-A0)/(t-1)))
    w1=moment(s.cancel((ps[n+1]-A1)/(t-1)))
    v0=A0*PI-w0
    v1=A1*PI-w1
    assert s.expand(A1*v0-A0*v1)==h
    arow=[A1*E-x for x in TU]
    crow=[A0*E-x for x in TP]
    assert s.expand(Bform(e,arow)-z0)==0
    assert s.expand(Bform(e,crow)-z1)==0
    assert all(s.expand((-A0*arow[j]+A1*crow[j])/h-vrow[j])==0 for j in range(b+1))
    wrow=[s.expand((v0*arow[j]-v1*crow[j])/h) for j in range(b+1)]
    DW=s.expand((v0*z0-v1*z1)/h)
    T=s.expand(-Bform(arow,crow)/h)
    assert s.expand(Bform(e,wrow)-DW)==0
    assert s.expand(Bform(vrow,wrow)-T)==0
    assert s.expand(Bform(arow,crow)-E*d-gamma*ZK)==0
    rpi=s.cancel((w1*z1-w0*z0)/d)
    re=s.cancel(-gamma*ZK/d)
    assert rpi==s.Rational(old['rational_pi_companion'])
    assert re==s.Rational(old['rational_e_companion'])
    assert s.expand(DW/DV-(rpi-PI))==0
    assert s.expand(T/DV-(re-E))==0
    actual_x_over_y=s.Rational(sum(old['primitive_full_triple']['A']),sum(old['primitive_full_triple']['B']))
    assert actual_x_over_y==-rpi-re==s.Rational(old['p'],old['q'])
    assert int(s.denom(actual_x_over_y))==old['q']
    # Validate the existing B vector in the reduced rows without solving them.
    Bsaved=s.Matrix(old['primitive_full_triple']['B'])
    assert high*Bsaved==s.zeros(b-1,1)
    assert sum((1+vrow[j])*Bsaved[j] for j in range(b+1))==0
    eta=None if z0==0 else s.cancel(z1/z0)
    separation=s.cancel(abs(d)/(A0*abs(z0)+A1*abs(z1)))
    rec={
        'n':n,'b':b,'z0':str(z0),'z1':str(z1),
        'product_sign':int(s.sign(z0*z1)),
        'sign_condition':bool(z0*z1<=0 and (z0!=0 or z1!=0)),
        'eta':None if eta is None else str(eta),
        'pole':str(A0/A1),'projective_pole_separation':str(separation),
        'A0':str(A0),'A1':str(A1),'h_n':str(h),
        'second_kind_rational_parts':[str(w0),str(w1)],
        'D_V':str(DV),'row_contents':row_contents,'minor_content':minor_content,
        'common_high_scale_gamma':str(gamma),
        'primitive_high_minors':{str(i)+','+str(j):str(m) for (i,j),m in primitive_minors.items()},
        'primitive_contractions':{'Z0':str(Z0),'Z1':str(Z1),'K':str(ZK),'d':str(A1*Z1-A0*Z0)},
        'rational_pi_companion':str(rpi),'rational_e_companion':str(re),
        'p':old['p'],'q':old['q'],
        'all_identity_and_frozen_endpoint_checks_pass':True
    }
    records.append(rec)
    print(json.dumps({key:rec[key] for key in ('n','b','z0','z1','product_sign','eta','projective_pole_separation')}))
assert SOURCE.read_bytes()==source_bytes
certificate={
    'scope':'Only the existing frozen n=4,6,8,10 controls. Exact rational determinant contractions; no new canonical solve, additional degree, or prime scan.',
    'source_sha256':hashlib.sha256(source_bytes).hexdigest(),
    'source_unchanged':True,
    'checker_sha256':hashlib.sha256((BASE/'check_two_scalar_quotient.py').read_bytes()).hexdigest(),
    'records':records,
    'first_failed_sign_condition':next((r['n'] for r in records if not r['sign_condition']),None)
}
(BASE/'two_scalar_quotient_evidence.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('All exact identity checks passed; evidence saved. First failed sign condition:',certificate['first_failed_sign_condition'])
