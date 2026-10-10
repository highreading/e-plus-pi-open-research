"""One predeclared exact degree d=2. No prime or degree scan."""
from pathlib import Path
import json
import sympy as S

d=2
z,b,g=S.symbols("z beta gamma")
D=1+z*z
Lco=[-d*(d-1)*z+2*d*d*(d-1)-d*b,
     (2*d-2)*z*z+b*z+g,
     -((z+3*d+2)*D-4*z*z),z*D]
def P(f):
    return S.expand(sum(Lco[j]*sum(S.binomial(j,k)*S.diff(f,z,k)
                       for k in range(j+1)) for j in range(4)))
B=z**d
for r in range(1,d+1):
    B=S.expand(B+P(B).coeff(z,d+2-r)/r*z**(d-r))
E=[S.factorial(d)*P(B).coeff(z,j) for j in (1,0)]
lex=S.groebner(E,g,b)
f=S.Poly(lex.polys[-1].as_expr(),b).monic().as_expr()
st=S.sturm(f,b)
lc=[int(S.sign(S.LC(S.Poly(a,b)))) for a in st]
deg=[int(S.degree(a,b)) for a in st]
minus=[s*(-1)**k for s,k in zip(lc,deg)]
def changes(v): return sum(a!=bb for a,bb in zip(v,v[1:]))
assert changes(minus)-changes(lc)==2
assert S.gcd(f,S.diff(f,b))==1

gb=S.groebner(E,b,g,order=lambda m:(m[0]+2*m[1],m[0]),domain=S.QQ)
basis=sorted([b**a*g**j for a in range(d+1) for j in range(d+1-a)],
             key=lambda q:(S.degree(q,b)+2*S.degree(q,g),S.degree(q,b)))
exps=[S.Poly(q,b,g).monoms()[0] for q in basis]
def nf(q): return S.expand(gb.reduce(S.expand(q))[1])
def lam(q): return S.Poly(nf(q),b,g).coeff_monomial(g**d)
def mul(q):
    cols=[]
    for x in basis:
        pp=S.Poly(nf(q*x),b,g)
        cols.append(S.Matrix([pp.coeff_monomial(exp) for exp in exps]))
    return S.Matrix.hstack(*cols)
G=S.Matrix([[lam(x*y) for y in basis] for x in basis])
assert abs(G.det())==2
Gi=G.inv()
ee=nf(sum(basis[i]*Gi[i,j]*basis[j]
          for i in range(len(basis)) for j in range(len(basis))))
jac=S.det(S.Matrix(E).jacobian([b,g]))
assert nf(ee-(-1)**d*jac/S.factorial(d))==0
for x in basis:
    assert mul(x).trace()==lam(ee*x)
for x in [b,g]:
    assert mul(x).T*G==G*mul(x)
H=S.Matrix([[mul(x*y).trace() for y in basis] for x in basis])
assert H==G*mul(ee)
out={
 "scope":"single predeclared degree d=2; exact Sturm and symbolic algebra controls",
 "degree":d,"E1_E0":[str(S.expand(x)) for x in E],
 "beta_eliminant":str(f),
 "sturm_degrees":deg,"sturm_leading_signs":lc,
 "sturm_signs_at_minus_infinity":minus,
 "sturm_variations_at_minus_infinity":changes(minus),
 "sturm_variations_at_plus_infinity":changes(lc),
 "real_root_count":2,"nonreal_root_count":4,
 "eliminant_discriminant":str(S.factor(S.discriminant(f,b))),
 "triangular_basis":[str(x) for x in basis],
 "frobenius_gram":[[str(v) for v in G.row(i)] for i in range(G.rows)],
 "frobenius_gram_determinant":str(G.det()),
 "euler_element":str(ee),
 "trace_discriminant":str(H.det()),
 "trace_factorization":"pass","jacobian_euler_identity":"pass",
 "coordinate_self_adjointness":"pass","status":"pass"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
