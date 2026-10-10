"""Exact second-kind normalization control at the already saved n=2."""
from pathlib import Path
import json
import sympy as s

base = Path(__file__).parent
item = json.loads((base / "raw_dual_error_integrals_existing_checks.json").read_text())["checks"]["2"]
z, t, a = s.symbols("z t a")
n = 2
U = s.sympify(item["U"], locals={"t": t})
V = s.sympify(item["V"], locals={"t": t})
V1 = V.subs(t, 1)
q = s.expand(z**n*U.subs(t, 1/z))
v = q/(s.factorial(n)*V1)
az = s.Poly(s.expand((1+z*z)**n*sum(z**j/s.factorial(j) for j in range(2*n+1))), z)
mu = lambda p: s.expand(sum(c*az.nth(2*n-k[0]) if k[0] <= 2*n else 0 for k,c in s.Poly(p,z).terms()))
Cq = s.factor(sum(mu(z**k*q)/a**(k+1) for k in range(2*n+1)))
assert s.cancel(Cq-(1850/a**3+204/a**4+1176/a**5)) == 0
dd = s.cancel((U.subs(t,a)-U.subs(t,z))/(a-z))
assert mu(q*dd) == 0
assert s.expand(q*U.subs(t,z)-z**n*q*q.subs(z,1/z)) == 0
assert mu(q*U.subs(t,z)) == 1850*1176
B = s.expand(sum(mu(z**(n+r)*q)/(s.factorial(n)*V1)*z**r for r in range(n+1)))
assert s.expand(B-(1+s.Rational(102,925)*z+s.Rational(588,925)*z*z)) == 0
assert s.cancel(Cq-s.factorial(n)*V1*a**(-n-1)*B.subs(z,1/a)) == 0
orig = (1+t*t)**n*t**n*v.subs(z,1/t)/(1-t)**(n+1)
inverted = s.cancel(orig.subs(t,1/z)*(-1/z**2))
target = -(1+z*z)**n*v/(z**(2*n+1)*(z-1)**(n+1))
assert s.cancel(inverted-target) == 0
assert s.cancel(s.diff(1/(z-a),a,n)-s.factorial(n)/(z-a)**(n+1)) == 0
Ra = s.sympify(item["arctangent_error"])
connection = s.factorial(2*n+1)*Ra/(s.factorial(n)*V1)
out = {"scope":"Frozen n=2 only; no new canonical solve or scan.",
       "Cq":str(Cq), "B":str(B), "positive_circle_quadratic":str(mu(q*U.subs(t,z))),
       "v_at_minus_one":str(v.subs(z,-1)), "B_at_minus_one":str(B.subs(z,-1)),
       "connection_scalar":str(connection), "all_assertions_passed":True}
target = base / "raw_dual_second_kind_existing_checks.json"
target.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"saved":str(target),"all_assertions_passed":True}))
