"""Predeclared synthetic collisions: local identities, not canonical raw degrees."""
import sys,json
from pathlib import Path
from math import comb,factorial
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
x,t=s.symbols('x t')
clean=s.cancel
def coeffs(f,count):
    return [s.expand(s.series(f,x,0,count).removeO()).coeff(x,j) for j in range(count)]
def monic_from_pairs(pairs):
    # The second component is a constant multiple of the analytic C column.
    # Removing log(x)*C from every row leaves precisely these rational entries.
    rows=[]
    for r in range(4):
        row=[]
        for a,b in pairs:
            row.append(clean(s.diff(a,x,r)+sum(comb(r,j)*s.diff(b,x,r-j)*(-1)**(j-1)*factorial(j-1)/x**j for j in range(1,r+1))))
        rows.append(row)
    W=s.Matrix(rows[:3]);co=(-s.Matrix([rows[3]])*W.inv()).applyfunc(clean)
    euler=[clean(x*co[0,2]),clean(x*x*co[0,1]),clean(x**3*co[0,0])]
    assert all(s.limit(f,x,0).is_finite for f in euler)
    return euler,clean(W.det())
def kernel(euler,m,logs):
    bc=[coeffs(f,m+1) for f in euler]
    I=[s.expand(bc[0][j]*t*(t-1)+bc[1][j]*t+bc[2][j]+(t*(t-1)*(t-2) if j==0 else 0)) for j in range(m+1)]
    aa=s.symbols('a:'+str(m+1));bb=s.symbols('b:'+str(m+1)) if logs else [0]*(m+1)
    eq=[]
    for k in range(m+1):
        if logs:eq.append(sum(I[k-r].subs(t,r)*bb[r] for r in range(k+1)))
        eq.append(sum(I[k-r].subs(t,r)*aa[r]+s.diff(I[k-r],t).subs(t,r)*bb[r] for r in range(k+1)))
    vv=list(aa)+(list(bb) if logs else [])
    mat,_=s.linear_eq_to_matrix(eq,vv)
    return mat,I[0]
def pairjet(pair,m,logs):
    a,b=pair
    return coeffs(a,m+1)+(coeffs(b,m+1) if logs else [])
def valuation(f):
    nu,de=s.fraction(clean(f))
    def order(poly):return min(v[0] for v,c in s.Poly(poly,x).terms())
    return order(nu)-order(de)
cases=[
 ('ordinary_double',[(1+x*x,0),(x+x**3,0),(x**4/(1-x),0)],5,False,2),
 ('ordinary_triple',[(1+x*x,0),(x+x**3,0),(x**5/(1-x),0)],5,False,3),
 ('origin_M4',[(x,0),(x**3,0),(x**4/(1-x),0)],4,False,3),
 ('origin_M10',[(x,0),(x**3,0),(x**10/(1-x),0)],4,False,3),
 ('log_h1_repeated0',[(0,1),(x*x,0),(1,0)],4,True,1),
 ('log_h1_repeated1',[(0,x),(1,0),(x,0)],4,True,1),
 ('log_h2_distinct',[(x/(1-x),x*x),(1,0),(x*x,0)],4,True,2),
 ('log_h3_high4',[(0,1),(x**4,0),(1,0)],4,True,3),
]
result=[]
for name,pairs,m,logs,h in cases:
    pairs=[(s.sympify(a),s.sympify(b)) for a,b in pairs]
    euler,W=monic_from_pairs(pairs)
    mat,I=kernel(euler,m,logs)
    jets=s.Matrix.hstack(*(s.Matrix(pairjet(pair,m,logs)) for pair in pairs))
    dim=2 if name=='origin_M10' else 3
    assert len(mat.nullspace())==dim and jets.rank()==dim and mat*jets==s.zeros(mat.rows,3)
    if logs:assert valuation(W)==h-2
    elif name.startswith('ordinary'):assert valuation(W)==h
    elif name=='origin_M4':assert valuation(W)==3*1-1+h
    else:assert valuation(W)==3*3-1+h
    # Verify the principal-part cutoff with all monomials of the operator,
    # using linearity. Only powers through h+1 of a,b may matter.
    # A polynomial unit factor in Q tests the effect of inverse-unit tails.
    qq=x**h*(1+x)
    cut=h+1
    for a,b in pairs:
        ac=sum(v*x**j for j,v in enumerate(coeffs(a,cut+1)))
        bc=sum(v*x**j for j,v in enumerate(coeffs(b,cut+1)))
        for derivative in range(3):
            ga=clean(s.diff(a-ac,x,derivative)+sum(comb(derivative,j)*s.diff(b-bc,x,derivative-j)*(-1)**(j-1)*factorial(j-1)/x**j for j in range(1,derivative+1)))
            gb=s.diff(b-bc,x,derivative)
            # Multiplication by any polynomial N cannot lower this order.
            assert ga==0 or valuation(ga/qq)>=0
            assert gb==0 or valuation(gb/qq)>=0
    result.append({'case':name,'indicial':str(s.factor(I)),'finite_jet_dimension':dim,
                   'actual_germ_span_equals_finite_kernel':True,'all_principal_parts_use_cutoff_h_plus_1':True})
out={'status':'PASS','scope':'Synthetic local germs only; no claim these are canonical raw-family exceptional degrees. Log h2/h3 controls exceed the rational raw cubic restriction h<=1 and test the more general local proof.','cases':result}
(HERE/'raw_unconditional_local_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
