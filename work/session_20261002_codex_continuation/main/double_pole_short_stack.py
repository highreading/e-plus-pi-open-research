"""Bounded exact receipt for the newly gated rank-two period construction."""
from pathlib import Path
from math import factorial, gcd, lcm
import json
import sympy as sp
import mpmath as mp

ROOT=Path(__file__).resolve().parent
y=sp.Symbol('y')
D=[1]
for n in range(1,70): D.append(n*D[-1]+(-1)**n)
alpha=[sp.Integer(2),sp.Integer(-2)]
for r in range(30): alpha.append(sp.Rational(8,2*r+1)-2*alpha[-1]-alpha[-2])
def nu(r): return (-1)**r*(1-2*r)
def rational(r): return alpha[r]-factorial(2*r)
for r in range(24):
    poly,rem=sp.div(y**r,(1+y)**2)
    aa=rem.coeff(y,1);bb=rem.coeff(y,0)
    independent=8*sum((poly.coeff(y,j)/sp.Integer(2*j+1) for j in range(max(0,sp.degree(poly,y)+1))),sp.Integer(0))+2*(bb-aa) if poly else 2*(bb-aa)
    assert independent==alpha[r] and aa+bb==nu(r)
def primitive(coeffs):
    clear=lcm(*(int(x.q) for x in coeffs));ints=[int(clear*x) for x in coeffs]
    content=gcd(*ints)
    vals=[x//content for x in ints]
    if next(x for x in reversed(vals) if x)<0:vals=[-x for x in vals]
    return vals,clear,content
mp.mp.dps=1000
rows=[]
for k in range(2,9):
    C=sp.Matrix(k,2*k,lambda i,j:D[2*(i+j)]-nu(i+j))
    R=sp.Matrix(k,2*k,lambda i,j:rational(i+j))
    V=sp.Matrix(k,2*k,lambda i,j:nu(i+j))
    assert C.rank()==k and V.rank()==min(2,k)
    val=[C.col_join(R+t*V).det() for t in range(4)]
    b2=(val[2]-2*val[1]+val[0])/2
    b1=val[1]-val[0]-b2
    bs=[val[0],b1,b2]
    assert val[3]==bs[0]+3*bs[1]+9*bs[2]
    vecs=C.nullspace();assert len(vecs)==k
    Q=sp.Matrix.hstack(*vecs);assert C*Q==sp.zeros(k,k)
    hv=[((R+t*V)*Q).det() for t in range(3)]
    h2=(hv[2]-2*hv[1]+hv[0])/2;hs=[hv[0],hv[1]-hv[0]-h2,h2]
    pp,clear,content=primitive(bs)
    L=lcm(*range(1,6*k-6,2))
    F=lambda n:sp.prod(factorial(j) for j in range(n))
    divisors=[2**(k*(k-1))*F(k-2+j)**2 for j in range(3)]
    assert all((int(b*L**k)%int(divisor)==0) for b,divisor in zip(bs,divisors))
    assert primitive(hs)[0]==pp
    change=sp.eye(k)
    if k>1:change[0,1]=3
    change[0,0]=2
    assert (R*Q*change).det()==2*hs[0]
    S=mp.e+mp.pi
    full=sum(mp.mpf(int(a))*S**i for i,a in enumerate(pp))
    if pp[2]:
        disc=pp[1]**2-4*pp[0]*pp[2]
        roots=[(-mp.mpf(pp[1])+sign*mp.sqrt(mp.mpf(disc)))/(2*pp[2]) for sign in [-1,1]] if disc>=0 else []
    else:
        disc=None;roots=[-mp.mpf(pp[0])/pp[1]]
    rows.append({'k':k,'matching_rank':k,'period_rank':min(2,k),'stack_rational_coefficients':list(map(str,bs)),
        'formal_clearer':str(clear),'complete_integer_content':str(content),'primitive_coefficients':list(map(str,pp)),
        'primitive_height_bits':max(abs(a).bit_length() for a in pp),'exact_kernel_primitive_polynomial_match':True,
        'simultaneous_forced_content_divisors':list(map(str,divisors)),'exact_rank_two_factorial_content_checks':True,
        'exact_nonunimodular_basis_scaling_match':True,'discriminant':str(disc),
        'diagnostic_roots':[mp.nstr(z,65) for z in roots],
        'diagnostic_nearest_root_error':mp.nstr(min((abs(z-S) for z in roots),default=mp.inf),35),
        'diagnostic_log_abs_primitive_evaluation':mp.nstr(mp.log(abs(full)),35)})
    print('DOUBLE_POLE',k,'height_bits',rows[-1]['primitive_height_bits'],'log_form',mp.nstr(mp.log(abs(full)),12),flush=True)
(ROOT/'DOUBLE_POLE_SHORT_STACK_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_EXACT_QUADRATIC_PERIOD_INTERFACE','moment_partial_fraction_checks':24,'k1_exception':'D0=nu0=D2=nu1=1, so the matching row is zero and the fixed-width stack vanishes. The arbitrary degree-one matched family is elementary, not a nonzero quadratic-stack case.','rows':rows,'scope':'Exact moments, matching kernel, degree-two coefficient and FINAL primitive-content receipts. Root/error values are finite diagnostics, not an infinite smallness or irrationality proof.'},indent=2)+'\n')
