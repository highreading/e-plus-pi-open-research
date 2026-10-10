"""All-parameter operator identity plus one frozen n=2 -> 4 normalization control.

No canonical degree is constructed. The exact input triples were already saved.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "math_packages"))
import sympy as s

n, r, t, z = s.symbols("n r t z")
a = list(s.symbols("a0:8"))
b = list(s.symbols("b0:8"))
c = list(s.symbols("c0:8"))
gamma, delta = s.symbols("gamma delta")
a[7], a[6] = s.Integer(0), -n * gamma
b[7], b[6] = gamma, delta - 2 * n * gamma
c[7], c[6], c[0] = gamma, delta, s.Integer(0)

def at(arr, i):
    return arr[i] if 0 <= i < len(arr) else s.Integer(0)

def jk_monomial(k):
    return t**k / s.prod(r + j for j in range(1, k + 1))

def d2jk_monomial(k):
    assert k >= 1
    return r / t if k == 1 else jk_monomial(k - 2)

direct = s.Integer(0)
for j, arr in enumerate((a, b, c)):
    theta_factor = s.prod(n - r - u for u in range(j))
    for d, coef in enumerate(arr):
        if coef != 0:
            direct += coef * theta_factor * d2jk_monomial(7 + j - d)

V = []
for k in range(8):
    V.append(
        at(a, 5-k) + (n+k)*at(b, 6-k)
        + (n+k)*(n+k-1)*at(c, 7-k)
        - t*(at(b, 5-k) + 2*(n+k)*at(c, 6-k))
        + t*t*at(c, 5-k)
    )
assert V[7] == 0
legendre_form = gamma*(r*(r+1)-r*r/t) + delta*r*(t-1)
legendre_form += sum(V[k]*jk_monomial(k) for k in range(7))
assert s.cancel(direct-legendre_form) == 0
W0 = a[5]-b[5]*t+c[5]*t*t
assert s.expand(V[0] - (-gamma*n*(n+1)+delta*n*(1-2*t)+W0)) == 0

saved = json.loads((HERE / "raw_accessory_scaling_probe.json").read_text())
cases = {case["n"]: case for case in saved["cases"]}

def frozen_triple(degree):
    result = []
    for name in ("A", "B", "C"):
        arr = cases[degree]["exact_polynomial_input"][name]
        result.append(sum(s.Rational(v)*z**(len(arr)-j-1) for j,v in enumerate(arr)))
    scale = result[1].subs(z, 1)
    result = [s.expand(v/scale) for v in result]
    assert result[1].subs(z,1) == 1 and result[2].subs(z,1) == 4
    return result

def kmatrix(triple):
    A, B, C = triple
    D = 1+z*z
    return s.Matrix([
        [D**2*A, B, C],
        [D**2*s.diff(A,z)+D*C, B+s.diff(B,z), s.diff(C,z)],
        [D**2*s.diff(A,z,2)+2*D*s.diff(C,z)-2*z*C,
         B+2*s.diff(B,z)+s.diff(B,z,2), s.diff(C,z,2)],
    ])

old = frozen_triple(2)
new = frozen_triple(4)
K = kmatrix(old)
Knext = kmatrix(new)
Q = s.cancel(K.det()/z**5)
Qnext = s.cancel(Knext.det()/z**11)
assert s.Poly(Q,z).degree() == s.Poly(Qnext,z).degree() == 3
raw = Knext*K.adjugate()
N = raw.applyfunc(lambda f: s.cancel(f/z**5))
caps = [[6,7,7],[5,6,6],[4,5,5]]
degrees = [[s.Poly(N[i,j],z).degree() for j in range(3)] for i in range(3)]
assert all(degrees[i][j] <= caps[i][j] for i in range(3) for j in range(3))
assert all(N[i,2].subs(z,0) == 0 for i in range(3))
assert (N*K-Q*Knext).applyfunc(s.cancel) == s.zeros(3)
assert s.cancel(N.det()-z**6*Q**2*Qnext) == 0

N0,N1,N2 = list(N[0,:])
A=s.Poly(N0+N1+N2,z); B=s.Poly(N1+2*N2,z); C=s.Poly(N2,z)
assert A.nth(7)==0 and B.nth(7)==C.nth(7)
assert A.nth(6)==-2*C.nth(7)
assert B.nth(6)==C.nth(6)-4*C.nth(7)

def Jpoly(f, k):
    f=s.Poly(s.expand(f),t)
    return sum(v*s.factorial(j[0])/s.factorial(j[0]+k)*t**(j[0]+k)
               for j,v in f.terms())

vv=[]
for k in range(7):
    def coeff(poly,degree):
        return poly.nth(degree) if degree>=0 else s.Integer(0)
    vv.append(coeff(A,5-k)+(2+k)*coeff(B,6-k)+(2+k)*(1+k)*coeff(C,7-k)
              -t*(coeff(B,5-k)+2*(2+k)*coeff(C,6-k))+t*t*coeff(C,5-k))
def dop(f):
    return s.expand(C.nth(7)*(t*(t-1)*s.diff(f,t,2)+(2*t-1)*s.diff(f,t))
                    +C.nth(6)*t*(t-1)*s.diff(f,t)
                    +sum(vv[k]*Jpoly(f,k) for k in range(7)))
def reflected(Bp,degree):
    bp=s.Poly(Bp,z)
    return sum(bp.nth(j)*t**(degree-j)/s.factorial(degree-j) for j in range(degree+1))
oldp=[s.Poly(f,z) for f in old]
newp=[s.Poly(f,z) for f in new]
aa,aa1,cc,cc1=oldp[0].nth(2),oldp[0].nth(1),oldp[2].nth(2),oldp[2].nth(1)
dd,dd1,ff,ff1=newp[0].nth(4),newp[0].nth(3),newp[2].nth(4),newp[2].nth(3)
xi=aa*cc1-aa1*cc+cc*cc
mm0=aa*ff-cc*dd
mm1=aa*ff1+aa1*ff-cc*dd1-cc1*dd
bbeta=oldp[1].nth(1)/oldp[1].nth(2)
assert s.cancel(C.nth(7)/s.Poly(Q,z).nth(3)-mm0/xi)==0
assert s.cancel(C.nth(6)/s.Poly(Q,z).nth(3)-(mm1+bbeta*mm0)/xi)==0
Pold=reflected(old[1],2);Pnext=reflected(new[1],4)
lhs=sum(s.Poly(Q,z).nth(d)*Jpoly(Pnext,3-d) for d in range(4))
assert s.expand(lhs-dop(Pold)) == 0

out={
    "status":"passed",
    "scope":"Symbolic arbitrary-n/arbitrary-monomial identity, plus frozen normalized n=2 -> 4; zero new degree constructions",
    "symbolic_legendre_volterra_identity":True,
    "symbolic_centered_identity":True,
    "frozen_degrees":[2,4],
    "numerator_degree_matrix":[[int(x) for x in row] for row in degrees],
    "direct_matrix_identity":True,
    "determinant_identity":True,
    "origin_last_column_divisibility":True,
    "infinity_cancellations":True,
    "actual_reflected_polynomial_identity":True,
    "direct_leading_minor_identities":True,
    "normalized_gamma_exact":str(C.nth(7)/s.Poly(Q,z).nth(3)),
    "normalized_delta_exact":str(C.nth(6)/s.Poly(Q,z).nth(3)),
    "Q_exact":list(map(str,s.Poly(Q,z).all_coeffs())),
    "first_row_N_exact":[list(map(str,s.Poly(v,z).all_coeffs())) for v in (N0,N1,N2)],
}
(HERE / "raw_direct_two_degree_transfer_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k not in ("Q_exact","first_row_N_exact")},indent=2))
