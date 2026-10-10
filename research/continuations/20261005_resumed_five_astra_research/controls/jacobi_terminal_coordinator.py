"""Coordinator checks exact terminal algebra, including original monomial inverse.

All rational inputs are bounded auxiliary values; no infinite branch is inferred.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent
x,y=sp.symbols('x y')

def vp_int(a,p=3):
    if a==0:return None
    v=0
    while a%p==0:a//=p;v+=1
    return v

def vp(a):
    a=Q(a)
    return None if a==0 else vp_int(a.numerator)-vp_int(a.denominator)

def residue(a,mod):
    a=Q(a)
    assert a.denominator%3
    return a.numerator*pow(a.denominator,-1,mod)%mod

def fixed_coefficients():
    A=Q(243,4);aa=Q(25);a=3*aa
    beta=3*(2*A*A+4*A+1)/((4*A+1)*(4*A+5))
    gamma=3*A*A*(A+1)*(3*A+1)/((4*A+1)**2*(4*A-1)*(4*A+3))
    rho=A*(3*A+1)/((4*A+1)*(4*A+3))
    z=(4*A+1)/2;e=(A+1)*(3*A+1)/(2*(4*A+1));B=2*A+2*e
    q0=-1-beta;k=aa*(A+74)
    c=q0*q0-a*q0+k-k*gamma*(z-1)/2
    d=a-2*q0-k*B/2;ee=1-k*(z+1)/2
    data=[('C',c,1,9,7),('rho',rho,4,27,7),('D',d,0,27,1),
          ('E',ee,0,27,4),('rho_D',rho*d,4,27,7),('rho2_E',rho*rho*ee,8,27,7)]
    results=[]
    for name,value,depth,mod,expected in data:
        actualdepth=vp(value);actualres=residue(value/Q(3**depth),mod)
        assert actualdepth==depth and actualres==expected,(name,actualdepth,actualres)
        results.append({'name':name,'valuation':actualdepth,'normalized_modulus':mod,'normalized_residue':actualres})
    return results

def cartier():
    z=sp.Symbol('z');f=(1+z)**3*(1-z);g=(1+z)**2*(1-z)
    u=1+z;v=(1+z)**2
    def modpoly(p):return sp.Poly(p,z, modulus=3)
    def extract(p,d):
        pp=sp.Poly(sp.expand(p),z)
        return modpoly(sum(pp.nth(k)*z**((k-d)//3) for k in range(d,pp.degree()+1,3)))
    assert extract(g*f*f,2)==modpoly(g)
    expected={'G':[v,g,None],'U':[u,v,0],'V':[u,2*v,0]}
    rows=[]
    for name,s in [('G',g),('U',u),('V',v)]:
        for digit in range(3):
            got=extract(s*g*f**digit,digit)
            exp=expected[name][digit]
            if exp is not None:assert got==modpoly(exp),(name,digit)
            rows.append({'state':name,'digit':digit,'output':str(got.as_expr())})
    # Exact low-digit fraction recurrence.
    rr=247;digits=[]
    for _ in range(16):
        dd=2*rr%3;digits.append(dd);rr=(rr-8*dd)//3
    assert digits==[2,1,1,1]+[1,0]*6,digits
    return {'identities':rows,'resonant_low_digits':digits}

def jacobi(s,A):
    return sp.Poly(sp.expand(sum(sp.binomial(s+A,k)*sp.binomial(sp.Rational(2*s-1,2),s-k)*x**k*(x-1)**(s-k) for k in range(s+1))),x)

def exact_inverse_checks():
    rows=[]
    for A in (3,9,15):
        m=(A+1)//2;h=7;r0=sp.Rational(A+71,3)
        js=jacobi(m,A);jm=jacobi(m-1,A);jn=jacobi(m+1,A)
        kap=js.LC();p=js.as_expr()/kap;pn=jn.as_expr()/jn.LC()
        a=sp.cancel(pn.subs(x,r0)/p.subs(x,r0));aa=a/3
        beta=sp.Rational(3*(2*A*A+4*A+1),(4*A+1)*(4*A+5))
        gamma=sp.Rational(3*A*A*(A+1)*(3*A+1),(4*A+1)**2*(4*A-1)*(4*A+3))
        rho=sp.Rational(A*(3*A+1),(4*A+1)*(4*A+3))
        assert sp.cancel(pn-((x-beta)*p-gamma*jm.as_expr()/jm.LC()))==0
        qhat=(x-beta)*js.as_expr()-rho*jm.as_expr()
        assert sp.cancel(qhat-kap*pn)==0
        zz,rem=sp.div(qhat-a*js.as_expr(),3*x-(A+71),x)
        assert rem==0
        divided=sp.cancel((js.as_expr()*zz.subs(x,y)-zz*js.as_expr().subs(x,y))/(x-y))
        epoly=sp.Poly(sp.expand(zz*zz.subs(x,y)+aa*divided),x,y)
        hm=sp.Rational(2**(4*A+3)*factorial(A+1)*factorial(3*A+1)*factorial(2*A+1)**2,
                       (4*A+3)*factorial(4*A+2)**2)
        nm=9*kap*kap*hm
        uu=sp.Rational(comb(6*m,3*m),comb(2*m,m))
        unitformula=sp.Rational(2**(2*A+3)*(3*A+2),(A+1))*3/(4*A+3)/uu
        assert nm==unitformula
        moment0=sp.Rational(2*4**A*factorial(A)**2,factorial(2*A+1))
        moments=[moment0]
        for i in range(2*m+1):moments.append(moments[-1]*sp.Rational(2*i+1,2*i+2*A+3))
        # The norm is independently evaluated by its entire polynomial.
        square=sp.Poly(sp.expand(p*p),x)
        assert sum(square.nth(i)*moments[i] for i in range(square.degree()+1))==hm
        gram=sp.Matrix(m+1,m+1,lambda i,j:-sp.Rational(3**(h+1),2)*(moments[i+j+1]-r0*moments[i+j]))
        scalar=2*sp.Rational(3**2,3**h)/(aa*nm)
        candidate=sp.Matrix(m+1,m+1,lambda i,j:scalar*epoly.coeff_monomial(x**i*y**j))
        assert gram*candidate==sp.eye(m+1),('inverse',A)
        z=sp.Rational(4*A+1,2);e=sp.Rational((A+1)*(3*A+1),2*(4*A+1));B=2*A+2*e
        q0=-1-beta;k=aa*(A+74)
        c=q0*q0-a*q0+k-k*gamma*(z-1)/2
        d=a-2*q0-k*B/2;ee=1-k*(z+1)/2
        X=js.eval(-1);Y=jm.eval(-1);phi=c*X*X+rho*d*X*Y+rho*rho*ee*Y*Y
        assert epoly.eval({x:-1,y:-1})==phi/(A+74)**2,('endpoint',A)
        rows.append({'A':A,'m':m,'h_auxiliary':h,'exact_norm_integral':True,
                     'normalized_norm_identity':True,'original_monomial_inverse_identity':True,
                     'endpoint_quadratic_identity':True})
    return rows

def main():
    out={'status':'EXACT_TERMINAL_ALGEBRA_PASS','fixed_coefficient_check':fixed_coefficients(),
         'cartier_polynomial_check':cartier(),'auxiliary_gram_checks':exact_inverse_checks(),
         'scope':'Finite rational and polynomial identities. No infinite endpoint-unit population or actual residual-transfer assertion.'}
    (OUT/'jacobi_terminal_algebra_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
