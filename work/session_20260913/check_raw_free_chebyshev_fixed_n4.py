"""Exact controls restricted to the predeclared free-model n=4 block.

No canonical Hermite-Pade system is solved and no larger degree is scanned.
"""
from pathlib import Path
import json
import sympy as s

x, y = s.symbols("x y")

def free(k):
    return s.expand(sum(s.binomial(k-h, h)*(2*x)**(k-2*h)/s.factorial(k-2*h)
                        for h in range(k//2+1)))

def borel(poly):
    p = s.Poly(poly, x)
    return s.expand(sum(c*x**j[0]/s.factorial(j[0]) for j, c in p.terms()))

def averaging(poly):
    p = s.Poly(poly, x)
    return s.expand(sum(c*x**j[0]*s.binomial(2*j[0], j[0])/4**j[0]
                        for j, c in p.terms()))

f = {j: free(j) for j in (5, 6, 7)}
ordered = [f[5], f[7], f[6]]
wronskians = [s.factor(s.det(s.Matrix([
    [s.diff(ordered[c], x, row) for c in range(q)] for row in range(q)
]))) for q in (1, 2, 3)]
T = (8*y**7+60*y**6+4860*y**5+95400*y**4-769500*y**3
     +1148175*y**2+4961250*y-1488375)
W2 = 32*x**3*(2*x**8+80*x**6+1605*x**4+4410*x**2+11025)/4725
W3 = -32*x*T.subs(y, x*x)/212625
assert s.expand(wronskians[1]-W2) == 0
assert s.expand(wronskians[2]-W3) == 0
assert T.subs(y, 0) < 0 and T.subs(y, 1) == 3951878
# This is the all-interval positivity certificate used in the proof.
positive_remainder = s.expand(s.diff(T, y) + 2308500*y*y - 2296350*y - 4961250)
assert all(c >= 0 for c in s.Poly(positive_remainder, y).all_coeffs())
assert 4961250-12150 > 0

identities = {}
for j in (5, 6, 7):
    Lf = x*x*s.diff(f[j], x, 4)+4*x*s.diff(f[j], x, 3)+(x*x+2)*s.diff(f[j], x, 2)+3*x*s.diff(f[j], x)
    assert s.expand(Lf-j*(j+2)*f[j]) == 0
    actual = borel(s.expand(s.I**(-j)*s.legendre(j, s.I*x)))
    # Only lower rows required by these three exact identities are formed.
    rhs = sum((-1)**h*s.binomial(s.Rational(1, 2), h)*averaging(free(j-2*h))
              for h in range(j//2+1))
    assert s.expand(actual-rhs) == 0
    identities[str(j)] = {"scalar_operator": True, "actual_averaging_identity": True}

output = {
    "scope": "The predeclared free-model n=4 block f5,f6,f7 only; exact rational symbolic controls.",
    "polynomials": {str(j): str(f[j]) for j in f},
    "ordered_basis": [5, 7, 6],
    "wronskians": list(map(str, wronskians)),
    "T_at_zero": str(T.subs(y, 0)), "T_at_one": str(T.subs(y, 1)),
    "T_derivative_positive_certificate": True,
    "identities": identities,
    "all_assertions_passed": True,
}
path = Path(__file__).with_name("raw_free_chebyshev_fixed_n4_checks.json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps({"saved": str(path), "all_assertions_passed": True}))
