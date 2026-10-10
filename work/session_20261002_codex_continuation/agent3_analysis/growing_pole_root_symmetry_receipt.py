"""New root/symmetry diagnostics using the actual stack, without content rechecks."""
import json
import math
from pathlib import Path
import sympy as sp

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parent/'main'/'GENERAL_POLE_SHORT_STACK_CERTIFICATE.json'
rows=json.loads(SOURCE.read_text())['rows']
z=sp.Symbol('z')
root_counts=[]
for row in rows:
    coefficients=[sp.Integer(v) for v in row['primitive_coefficients']]
    polynomial=sp.Poly(sum(v*z**j for j,v in enumerate(coefficients)),z)
    root_counts.append({'m':row['m'],'k':row['k'],
                        'real_roots':int(polynomial.count_roots(-sp.oo,sp.oo)),
                        'degree':polynomial.degree(),
                        'discriminant_sign':int(sp.sign(polynomial.discriminant()))})

E,P=sp.symbols('E P')
m=k=3
d=m-1
jet=[sp.binomial(d,j)*sp.rf(sp.Rational(1,2),d-j)/sp.rf(sp.Rational(1,2),d)
     for j in range(m)]
weight=sp.Rational(4**m,int(sp.binomial(2*d,d)))
def mu_h(r):
    return sum(sp.binomial(r,j)*sp.subfactorial(2*j) for j in range(r+1))
def nu_h(r):
    return sp.factorial(r)*jet[r] if r<m else sp.Integer(0)
def kernel_integral(power):
    if power>=0:
        return sum(sp.binomial(power,j)/sp.Integer(2*j+1) for j in range(power+1))
    s=-power
    value=P/4
    for ell in range(2,s+1):
        value=sp.Rational(1,2*(ell-1)*2**(ell-1))+sp.Rational(2*ell-3,2*(ell-1))*value
    return value
def sigma_h(r):
    exponential=sum(sp.binomial(r,j)*(E*sp.subfactorial(2*j)-sp.factorial(2*j))
                    for j in range(r+1))
    return exponential+weight*kernel_integral(r-m)
upper_low=sp.Matrix(k,k,lambda i,j:mu_h(i+j)-nu_h(i+j))
upper_high=sp.Matrix(k,k,lambda i,j:mu_h(i+j+k)-nu_h(i+j+k))
lower_low=sp.Matrix(k,k,lambda i,j:sigma_h(i+j))
lower_high=sp.Matrix(k,k,lambda i,j:sigma_h(i+j+k))
effective=lower_low-lower_high*upper_high.inv()*upper_low
determinant=sp.Poly(sp.expand(effective.det()),E,P)
adjugate=effective.adjugate()
numerator=sp.Poly(sp.expand(adjugate[0,1]-adjugate[1,0]),E,P)

e_lo=sum(sp.Rational(1,math.factorial(j)) for j in range(81))
e_hi=e_lo+sp.Rational(1,80*math.factorial(80))
def atan_interval(q,terms=100):
    low=sum(sp.Rational((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms))
    return low,low+sp.Rational(1,(2*terms+1)*q**(2*terms+1))
five_lo,five_hi=atan_interval(5)
large_lo,large_hi=atan_interval(239)
p_lo=16*five_lo-4*large_hi
p_hi=16*five_hi-4*large_lo
def bound(poly):
    ec=(e_lo+e_hi)/2; pc=(p_lo+p_hi)/2
    er=(e_hi-e_lo)/2; pr=(p_hi-p_lo)/2
    x,y=sp.symbols('x y')
    centered=sp.Poly(poly.as_expr().subs({E:ec+x,P:pc+y}).expand(),x,y)
    center=centered.coeff_monomial(1)
    radius=sum(abs(coefficient)*er**i*pr**j
               for (i,j),coefficient in centered.terms() if i+j)
    return center-radius,center+radius
n_lo,n_hi=bound(numerator)
d_lo,d_hi=bound(determinant)
assert n_lo>0 and d_lo>0
ratio_lo=n_lo/d_hi; ratio_hi=n_hi/d_lo
assert sp.Rational(55575,10000)<ratio_lo<ratio_hi<sp.Rational(55577,10000)
receipt={
    'scope':'Original exact root counts from supplied primitive coefficients and failed natural effective-jet symmetry. No moment/content certificate audit.',
    'root_coefficient_source':str(SOURCE),
    'root_counts':root_counts,
    'natural_effective_jet_case':{'m':3,'k':3,'coordinate':'normalized Taylor h=y+1',
       'H01_minus_H10_positive':True,
       'certified_rational_interval':['55575/10000','55577/10000'],
       'cofactor_numerator_polynomial':str(numerator.as_expr()),
       'effective_schur_determinant_polynomial':str(determinant.as_expr()),
       'e_bound':'factorial sum through80 plus tail<=1/(80*80!)',
       'pi_bound':'Machin 16atan(1/5)-4atan(1/239),100 alternating terms each'},
    'not_claimed':['universal absence of another symmetrizer','nonreal actual roots','actual primitive content estimate']}
(OUT/'GROWING_POLE_ROOT_SYMMETRY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'root_count_cases':len(root_counts),'actual_natural_symmetry_counterexample':'PASS',
                  'H01_minus_H10_interval':receipt['natural_effective_jet_case']['certified_rational_interval']}))
