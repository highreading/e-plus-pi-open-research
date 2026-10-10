"""Symbolic adjacent-content elimination, with no degree/prime scan."""
from pathlib import Path
import json
import sys
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parent / "session_20260913" / "math_packages"))
import sympy as s
n, z = s.symbols("n z")
w = 2*(n+1)/z-2-(n-1)*z
T = s.Matrix([
    [-n, n, s.Rational(1, 2)],
    [n+1, -n-1, (n+1)/2],
    [n*(n+1), n+1, -(n+1)*(n+2)/2],
])
h1, u1, v1 = T*s.Matrix([1, z, w])
f = z**3+(n-2)*z*z+4*z-2*(n+2)
g = (n*n+4*n+2)*z*z-(6*n+4)*z-2*n*n
F = ((2*n+3)*z-n-2)*f-g
A = -(3*n**3+14*n*n+14*n+4)*z-4*n**3+8*n+4
B = (3*n+2)*z*z+(3*n*n-2)*z+4*n*n+12*n+8
Dnext = 2*(n+2)*h1*h1-2*h1*u1-n*u1*u1-u1*v1
eq = lambda value: s.factor(value) == 0
checks = {
    "transport_first": eq(h1-(n+1)*(z*z-2*z+2)/(2*z)),
    "transport_second": eq(u1+(n+1)**2*(z*z-2)/(2*z)),
    "transport_third": eq(v1-(n+1)**2*(n*z*z-2*n+4*z-4)/(2*z)),
    "next_quadratic": eq(Dnext-(n+1)**2*F/(2*z*z)),
    "integral_bezout": eq(A*f+B*g+8*(n+1)**2*(n+2)),
    "resultant": eq(s.resultant(f,g,z)+32*(n+1)**4*(n+2)**2),
}
assert all(checks.values()), checks
result = {
    "scope": "Formal n,z; no canonical degrees or prime scans",
    "all_checks_pass": all(checks.values()), "checks": checks,
}
(BASE / "hp_b2_adjacent_content_symbolic_checks.json").write_text(
    json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
