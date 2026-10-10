"""Exact small counterexample certificates, not a degree scan."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "math_packages"))
import sympy as s

x = s.symbols("x")
Q = [s.Integer(1), x]
for k in range(1, 9):
    Q.append(s.expand(x * Q[-1] + s.Rational(k*k, 4*k*k-1) * Q[-2]))
F = [sum(c*x**d/s.factorial(d) for (d,), c in s.Poly(q, x).terms())
     for q in Q]

out = {"scope": "Exact counterexamples n=4,5 only; no eventual claim", "cases": []}
for n, node_sets, expected in [
    (4, [[s.Rational(j,8) for j in (1,2,3)],
         [s.Rational(j,8) for j in (5,6,7)]], [-1,1]),
    (5, [[s.Rational(j,32) for j in (1,2,3,4)],
         [s.Rational(j,1024) for j in (1020,1021,1022,1023)]], [1,-1]),
]:
    fs = F[n+1:2*n]
    W = s.wronskian(fs, x)
    cert = {"n": n, "degrees": list(range(n+1,2*n)),
            "wronskian_0": str(W.subs(x,0)),
            "wronskian_1": str(W.subs(x,1)), "collocation": []}
    for nodes, sign in zip(node_sets, expected):
        det = s.det(s.Matrix([[f.subs(x,a) for f in fs] for a in nodes]))
        assert s.sign(det) == sign
        assert 0 < nodes[0] < nodes[-1] < 1
        assert all(a < b for a,b in zip(nodes,nodes[1:]))
        cert["collocation"].append({"nodes": list(map(str,nodes)),
                                    "determinant": str(det), "sign": sign})
    out["cases"].append(cert)

for k, f in enumerate(F):
    ode = s.diff(x*x*s.diff(f,x,2),x,2) + s.diff(x*x*s.diff(f,x),x)
    assert s.expand(ode-k*(k+1)*f) == 0
    if 1 <= k < 9:
        assert s.expand(F[k+1]-s.integrate(f,(x,0,x))
                        -s.Rational(k*k,4*k*k-1)*F[k-1]) == 0
out["differential_identity_controls"] = list(range(10))
out["status"] = "passed"
(HERE / "raw_arctan_borel_chebyshev_checks.json").write_text(
    json.dumps(out, indent=2)+"\n")
print("Exact n=4 and odd n=5 full-block counterexamples and identity controls passed.")
