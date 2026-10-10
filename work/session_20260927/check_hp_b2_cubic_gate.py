"""All-index symbolic identities; no canonical degree or prime scan."""
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parent / "session_20260913" / "math_packages"))
import sympy as s

n, h, u, v, t = s.symbols("n h u v t")
T = s.Matrix([
    [-n, n, s.Rational(1, 2)],
    [n+1, -n-1, (n+1)/2],
    [n*(n+1), n+1, -(n+1)*(n+2)/2],
])
r0 = s.Matrix([[1, 0, 0], [n, 1, 0]])
r1 = s.Matrix([[n+1, 1, 0], [n*(n+1), 2*(n+1), 1]]) * T
k = n+2
r2 = s.Matrix([
    [k*(k-1), 2*k, 1],
    [k*(k-1)*(k-2)+2*k, 3*k*(k-1), 2*k],
]) * T.subs(n, n+1) * T
state = s.Matrix([h, u, v])
B = s.Matrix([list(r0*state), list(r1*state), list(r2*state)])
I01 = B[[0, 1], :].det()
I02 = B[[0, 2], :].det()
I12 = B[[1, 2], :].det()
D = 2*(n+1)*h*h-2*h*u-(n-1)*u*u-u*v
E = (-2*n*(n+2)*h*h+4*n*h*u+(n+2)*h*v
     +(n*n-2*n-1)*u*u+n*u*v)
C = u**3+(n-2)*h*u*u+4*h*h*u-2*(n+2)*h**3
P = t**3-(2*n+2)*t*t+(n+2)**2*t-2*(n+1)*(n+2)
first = s.Matrix.vstack(r0[0, :], r1[0, :], r2[0, :])
second = s.Matrix.vstack(r0[1, :], r1[1, :], r2[1, :])
eq = lambda x: s.factor(x) == 0
checks = {
    "transition_determinant": eq(T.det()-(n+1)**4/2),
    "first_minor": eq(I01-(n+1)*D),
    "second_minor": eq(I02-(n+2)*(2*n+3)*E),
    "homogeneous_elimination": eq(u*E+(n*u+(n+2)*h)*D+(n+1)*C),
    "third_minor_boundary": eq(
        I12.subs({h:0, u:0})-(n+1)*(n+2)**2*(2*n+3)*v*v),
    "first_column_isomorphism": eq(
        first.det()+(n+1)**2*(n+2)*(2*n+3)),
    "cubic_pencil": eq(
        (second-t*first).det()-(n+1)**2*(n+2)*(2*n+3)*P),
    "cubic_discriminant": eq(
        s.discriminant(P, t)-4*(n+2)*(2*n**3-12*n*n-35*n-22)),
    "cubic_shift": eq(h**3*P.subs(t, n+u/h)-C),
    "cubic_at_zero": eq(P.subs(t, 0)+2*(n+1)*(n+2)),
    "cubic_at_one": eq(P.subs(t, 1)+(n*n+4*n+1)),
    "cubic_at_n": eq(P.subs(t, n)+2*(n+2)),
}
assert all(checks.values()), checks
result = {
    "scope": "Formal n,h,u,v,t; no degree or prime scan",
    "all_checks_pass": all(checks.values()),
    "checks": checks,
}
(BASE / "hp_b2_cubic_gate_symbolic_checks.json").write_text(
    json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
