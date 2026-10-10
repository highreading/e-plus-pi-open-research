"""Independent exact check at the single predeclared d=2; no degree scan.

Normal forms use explicit filtered monic generators and direct polynomial
division, independently of the source checker's Groebner reducer.
"""
from pathlib import Path
import sys
import json
sys.path.insert(0, str(Path(__file__).parent / "math_packages"))
import sympy as S

b, g, e, h = S.symbols("beta gamma eta zeta")
E1 = b**3-22*b**2+3*b*g+132*b-18*g-224
E0 = -2*b**3+b**2*g+36*b**2-18*b*g-180*b+g**2+54*g+288
F = [S.expand(E1), S.expand(E0)]
F.append(S.expand((g*F[0]-b*F[1])/2))
F.append(S.expand(g*F[1]-b*F[2]))
key = lambda m: (m[0]+2*m[1], m[0])
lead = []
for f in F:
    poly = S.Poly(f,b,g)
    m = max(poly.monoms(),key=key)
    assert poly.coeff_monomial(m)==1
    lead.append(m)
assert lead == [(3,0),(2,1),(1,2),(0,3)]

def nf(q):
    p, r = S.Poly(S.expand(q),b,g), S.Integer(0)
    while p.as_expr()!=0:
        m = max(p.monoms(),key=key)
        c = p.coeff_monomial(m)
        for f,v in zip(F,lead):
            if all(x>=y for x,y in zip(m,v)):
                p = S.Poly(S.expand(p.as_expr()-c*b**(m[0]-v[0])*g**(m[1]-v[1])*f),b,g)
                break
        else:
            term=c*b**m[0]*g**m[1]
            r += term
            p = S.Poly(p.as_expr()-term,b,g)
    return S.expand(r)

# Direct confluence certificate, all six pairs only in this fixed degree.
for i in range(4):
    for j in range(i+1,4):
        m=tuple(max(x,y) for x,y in zip(lead[i],lead[j]))
        sp=b**(m[0]-lead[i][0])*g**(m[1]-lead[i][1])*F[i]-b**(m[0]-lead[j][0])*g**(m[1]-lead[j][1])*F[j]
        assert nf(sp)==0

basis=[1,b,g,b*b,b*g,g*g]
def lam(q): return S.Poly(nf(q),b,g).coeff_monomial(g*g)
def coords(q):
    p=S.Poly(nf(q),b,g)
    return S.Matrix([p.coeff_monomial(x) for x in basis])
def mult(q): return S.Matrix.hstack(*(coords(q*x) for x in basis))
G=S.Matrix([[lam(x*y) for y in basis] for x in basis])
assert G.det()==2
inv=G.inv()
Euler=nf(sum(basis[i]*inv[i,j]*basis[j] for i in range(6) for j in range(6)))
assert Euler==5*b*b-14*b*g+54*b+6*g*g-21*g-104
Jac=S.det(S.Matrix([E1,E0]).jacobian([b,g]))
assert nf(Jac-2*Euler)==0
H=S.Matrix([[mult(x*y).trace() for y in basis] for x in basis])
assert H==G*mult(Euler)
assert H.det()==2**15*751*318737
for x in (b,g): assert mult(x).T*G==G*mult(x)

# Direct two-copy reduction of the actual Bezout tensor and Casimir.
rows=[]
for f in [E1,E0]:
    feg=f.subs(b,e)
    rows.append([S.cancel((f-feg)/(b-e)), S.cancel((feg-feg.subs(g,h))/(g-h))])
Bez=S.expand(S.det(S.Matrix(rows)))
def tensor_nf(q):
    # First copy may be reduced while eta,zeta are coefficient symbols.
    q=nf(q)
    q=nf(q.xreplace({b:e,g:h,e:b,h:g}))
    return S.expand(q.xreplace({b:e,g:h,e:b,h:g}))
Cas=sum(basis[i]*basis[j].subs({b:e,g:h})*inv[i,j] if hasattr(basis[j],"subs") else basis[i]*basis[j]*inv[i,j] for i in range(6) for j in range(6))
assert tensor_nf(Bez-2*Cas)==0
assert tensor_nf((b-e)*Bez)==0 and tensor_nf((g-h)*Bez)==0

# Independent elimination: direct quotient identities plus dimensions.
f=b**6-38*b**5+589*b**4-4714*b**3+20344*b*b-44304*b+37120
q=b**5-32*b**4+397*b**3-2336*b*b+6416*b-6336
assert nf(f)==0 and nf(12*g-q)==0
assert S.Poly(mult(b).charpoly(b).as_expr()-f,b).is_zero
assert S.gcd(f,S.diff(f,b))==1

# Verify the note's full displayed Sturm chain against signed remainders.
chain=[f,
3*b**5-95*b**4+1178*b**3-7071*b*b+20344*b-22152,
38*b**4-1169*b**3+12285*b*b-54256*b+86808,
-20015*b**3+306665*b*b-1543584*b+2560696,
-2243999*b*b+25532744*b-72357832,
1173253*b-153256292,S.Integer(1)]
standard=[f,S.diff(f,b)]
while S.degree(standard[-1],b)>0:
    standard.append(-S.rem(standard[-2],standard[-1],b))
ratios=[]
for actual,display in zip(standard,chain):
    ratio=S.cancel(display/actual)
    assert not ratio.has(b) and ratio>0
    ratios.append(str(ratio))
plus=[int(S.sign(S.LC(S.Poly(v,b)))) for v in chain]
minus=[s*(-1)**S.degree(v,b) for s,v in zip(plus,chain)]
changes=lambda a:sum(x!=y for x,y in zip(a,a[1:]))
assert changes(minus)==4 and changes(plus)==2

out={"scope":"single predeclared d=2, independent direct filtered division and signed remainder arithmetic",
     "monic_leading_terms":[list(x) for x in lead],"all_s_pairs":"pass",
     "gram":[list(map(str,G.row(i))) for i in range(6)],"gram_determinant":str(G.det()),
     "euler":str(Euler),"actual_bezout_equals_twice_casimir":"pass",
     "trace_determinant":str(H.det()),"trace_factorization":"pass",
     "jacobian_normalization":"pass","elimination_and_characteristic_polynomial":"pass",
     "displayed_sturm_positive_scalings":ratios,"real_roots":2,"nonreal_roots":4,
     "status":"pass"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
