"""Exact checks restricted to n=4,6,8,10, b=floor(n/2).
Run from the workspace root. No numerical observation is an asymptotic claim.
"""
import json
from pathlib import Path
from functools import reduce
from math import gcd, factorial
import sympy as s
import mpmath as mp

OUT = Path('work/session_20261001_astra/agent2')
t = s.Symbol('t')

def moment(poly):
    poly = s.Poly(s.expand(poly.subs(t, (1+s.I*t)/2)), t)
    return s.simplify(sum(c*s.Rational(2,k+1) for (k,),c in poly.terms() if k%2 == 0))

def ell(poly,n,j):
    return sum(c/s.factorial(n+k+1-j) for (k,),c in s.Poly(poly,t).terms())

def f_coeff(k):
    if k <= 0:
        return s.S.Zero
    re, im = 1,0
    for _ in range(k):
        re,im = re-im,re+im
    return s.Rational(4*im,k*2**k)

def atan_bounds(q,N=220):
    value=sum(((-1)**k)*s.Rational(1,(2*k+1)*q**(2*k+1)) for k in range(N))
    other=value+((-1)**N)*s.Rational(1,(2*N+1)*q**(2*N+1))
    return min(value,other),max(value,other)

def decimal(x):
    return mp.mpf(str(s.numer(x)))/mp.mpf(str(s.denom(x)))

mp.mp.dps=100
al,au=atan_bounds(5)
bl,bu=atan_bounds(239)
pi_lo,pi_hi=16*al-4*bu,16*au-4*bl
e_lo=sum(s.Rational(1,factorial(k)) for k in range(301))
e_hi=e_lo+s.Rational(1,300*factorial(300))
records=[]
for n in (4,6,8,10):
    b=n//2
    ps=[s.S.One,t-s.Rational(1,2)]
    for k in range(1,n+b):
        ps.append(s.expand((t-s.Rational(1,2))*ps[-1]+s.Rational(k*k,4*(4*k*k-1))*ps[-2]))
    hs=[s.Rational(2*(-1)**k,(2*k+1)*s.binomial(2*k,k)**2) for k in range(n+1)]
    V=s.expand(sum(ps[k].subs(t,1)*ps[k]/hs[k] for k in range(n+1)))
    high=[[ell(ps[n+l],n,j) for j in range(b+1)] for l in range(1,b)]
    v=[ell(V,n,j) for j in range(b+1)]
    mat=s.Matrix(high+[[1+x for x in v]])
    B=[(-1)**(b+j)*mat[:,[k for k in range(b+1) if k!=j]].det() for j in range(b+1)]
    assert mat*s.Matrix(B)==s.zeros(b,1)
    rank=mat.rank()
    assert rank==b
    cstar=s.expand(-sum(sum(B[j]*ell(ps[k],n,j) for j in range(b+1))*ps[k]/hs[k] for k in range(n+1)))
    C=[cstar.coeff(t,n-j) for j in range(n+1)]
    A=[-sum(B[j]/s.factorial(k-j) for j in range(min(k,b)+1))-sum(C[j]*f_coeff(k-j) for j in range(k+1)) for k in range(n+1)]
    Y=sum(B)
    X=sum(A)
    assert Y!=0 and sum(C)==Y
    M=2*n+b+1
    for k in range(n+1,M):
        assert sum(B[j]/s.factorial(k-j) for j in range(b+1))+sum(C[j]*f_coeff(k-j) for j in range(n+1))==0
    erow=[s.S.One]*(b+1)
    Dv=s.Matrix(high+[erow,v]).det()
    assert Y==-Dv
    # Rational part of the projection H_n=pi*V-Q.
    Q=0
    for k in range(n+1):
        quotient=s.cancel((ps[k].subs(t,1)-ps[k])/(1-t))
        Q+=moment(quotient)*ps[k]/hs[k]
    Q=s.expand(Q)
    arow=[-sum(s.Rational(1,factorial(k)) for k in range(n-j+1))+ell(Q,n,j) for j in range(b+1)]
    assert sum(B[j]*arow[j] for j in range(b+1))==X
    # These rational determinants give the complete pi and e companions.
    rational_pi=s.Matrix(high+[erow,arow]).det()
    rational_e=s.Matrix(high+[v,arow]).det()
    assert rational_pi+rational_e==X
    all_coeff=A+B+C
    clearer=s.ilcm(*[s.denom(x) for x in all_coeff])
    ints=[int(x*clearer) for x in all_coeff]
    content=reduce(gcd,map(abs,ints))
    ints=[x//content for x in ints]
    ai=ints[:n+1]
    bi=ints[n+1:n+b+2]
    ci=ints[n+b+2:]
    Yi=sum(bi)
    Xi=sum(ai)
    if Yi<0:
        ai,bi,ci=[[-x for x in block] for block in (ai,bi,ci)]
        Xi,Yi=-Xi,-Yi
    endpoint_gcd=gcd(abs(Xi),Yi)
    p,q=Xi//endpoint_gcd,Yi//endpoint_gcd
    assert gcd(abs(p),q)==1 and s.Rational(p,q)==X/Y
    Llo=p+q*(e_lo+pi_lo)
    Lhi=p+q*(e_hi+pi_hi)
    assert Llo>Lhi-1 and Llo<Lhi
    assert Llo>0 or Lhi<0
    rel=decimal(s.Rational(p,q))+mp.e+mp.pi
    rec={'n':n,'b':b,'rank':rank,'order_required':M,'all_original_high_rows_zero':True,'projection_endpoint_and_complete_tail_checks':True,'cofactor_Y':str(Y),'D_V':str(Dv),'primitive_full_triple':{'A':ai,'B':bi,'C':ci},'primitive_endpoint_X':Xi,'primitive_endpoint_Y':Yi,'endpoint_gcd':endpoint_gcd,'p':p,'q':q,'q_digits':len(str(q)),'rational_pi_companion':str(-rational_pi/Y),'rational_e_companion':str(-rational_e/Y),'integer_form_interval':[str(Llo),str(Lhi)],'relative_error_decimal_finite_evidence':mp.nstr(rel,35),'integer_form_decimal_finite_evidence':mp.nstr(q*rel,35)}
    records.append(rec)
    print(json.dumps({k:rec[k] for k in ('n','b','rank','q_digits','endpoint_gcd','relative_error_decimal_finite_evidence','integer_form_decimal_finite_evidence')}))
certificate={'scope':'Exactly n=4,6,8,10. Exact finite certificates; decimals are finite evidence only. No growing-degree conclusion is inferred.','pi_interval_method':'Machin identity with 220 alternating terms for each arctangent','e_interval_method':'Terms 0 through 300 and geometric tail bound 1/(300*300!)','records':records}
(OUT/'growing_regime_certificates.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('Wrote work/session_20261001_astra/agent2/growing_regime_certificates.json')
