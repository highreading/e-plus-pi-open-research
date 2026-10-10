"""Exact normalization controls using only the already saved n=1,2 cofactors."""
from pathlib import Path
import json
import sympy as s

z, t, phi = s.symbols("z t phi", real=True)
saved = {1: [-2, 3, -1], 2: [940, -1944, 1117, -162, 49]}
out = {}
for n, w in saved.items():
    W = s.expand(sum(w[r]*t**(n+r) for r in range(2*n+1)))
    V, rem = s.div(W, t**n*(t-1)**n, t)
    assert rem == 0
    T = s.expand(sum(s.factorial(n+r)*w[r]*t**r for r in range(2*n+1)))
    S0 = s.expand(sum(s.factorial(r)*w[r]*t**(n+r) for r in range(2*n+1)))
    U, rem = s.div(S0, (1+t*t)**n, t)
    assert s.degree(rem, t) < n
    assert s.expand(s.diff((1+t*t)**n*U, t, n)-T) == 0
    for j in range(n+1):
        assert s.Poly(U, t).nth(j) % s.factorial(n+j) == 0
    Q = s.expand(sum(s.factorial(n+r)*w[r]*z**(2*n-r)/s.factorial(n)
                     for r in range(2*n+1)))
    trunc = lambda p: s.expand(sum(s.Poly(p, z).nth(j)*z**j for j in range(2*n+1)))
    Pe = trunc(Q*sum(z**j/s.factorial(j) for j in range(2*n+1)))
    Pa = trunc(Q*sum((-1)**j*z**(2*j+1)/s.Integer(2*j+1) for j in range(n)))
    assert all(c.q == 1 for c in s.Poly(Pe, z).all_coeffs()+s.Poly(Pa, z).all_coeffs())
    Z = Q.subs(z, 1)
    Re = Z*s.E-Pe.subs(z, 1)
    # Exact integral: integral_0^1 exp(1-t)t^k dt=k!(e-sum_(j=0)^k1/j!).
    Re_int = sum(w[r]*s.factorial(n+r)*(s.E-sum(s.Rational(1, s.factorial(j))
                   for j in range(n+r+1)))/s.factorial(n) for r in range(2*n+1))
    assert s.simplify(Re-Re_int) == 0
    arc_t = 1-s.sqrt(2)*(s.cos(phi)+s.I*s.sin(phi))
    arc_p = s.expand_complex(U.subs(t, arc_t)).as_real_imag()[0]
    F = 2*s.sqrt(2)*s.cos(phi)-2
    Ra_arc = s.simplify((-1)**n*s.integrate(s.expand_trig(s.expand(F**n*arc_p)),
                             (phi, -s.pi/4, s.pi/4))/2)
    Ra = Z*s.pi/4-Pa.subs(z, 1)
    assert s.simplify(Ra-Ra_arc) == 0
    out[str(n)] = {"V": str(V), "U": str(U), "Qhat": str(Q),
                   "Pe": str(Pe), "Pa": str(Pa), "Z": str(Z),
                   "exponential_error": str(Re), "arctangent_error": str(Ra),
                   "arc_error": str(Ra_arc), "all_assertions_passed": True}

target = Path(__file__).with_name("raw_dual_error_integrals_existing_checks.json")
target.write_text(json.dumps({"scope": "Already saved n=1,2 cofactors only; no new canonical solve.",
                              "checks": out}, indent=2)+"\n")
print(json.dumps({"saved": str(target), "all_assertions_passed": True}))
