"""Exact convention controls restricted to the two previously saved dual triples."""
import json
import math
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "math_packages"))
import sympy as sp

z, t = sp.symbols("z t")
D = 1 + z**2
old = json.loads((BASE / "raw_dual_error_integrals_existing_checks.json").read_text())["checks"]
known = json.loads((BASE / "raw_dual_quadratic_independent_controls.json").read_text())["checks"]

def content(poly):
    return math.gcd(*[abs(int(x)) for x in poly.all_coeffs()])

def v2(a):
    if a == 0:
        return math.inf
    a = abs(int(a))
    return (a & -a).bit_length() - 1

def gaussian_v2(value):
    value = sp.expand(value)
    a, b = [int(x) for x in value.as_real_imag()]
    if a == b == 0:
        return math.inf
    if v2(a) != v2(b):
        return min(v2(a), v2(b))
    return v2(a) + 0.5

rows = {}
for ns in ("1", "2"):
    n, row = int(ns), old[ns]
    m = 2 * n
    Q, P, T = [
        sp.Poly(sp.sympify(row[name], locals={"z": z}), z)
        for name in ("Qhat", "Pe", "Pa")
    ]
    E = sp.Poly(
        sp.expand(D * (Q.as_expr() * T.diff().as_expr() - Q.diff().as_expr() * T.as_expr())
                  - Q.as_expr() ** 2), z
    )
    p = [P.nth(m-j) for j in range(3)]
    e = [E.nth(2*m-j) for j in range(3)]
    K = sp.Poly(
        -p[0]*e[0]*z**2
        + ((2*p[0]-p[1])*e[0]-p[0]*e[1])*z
        - (p[0]+p[2])*e[0] + (3*p[0]-p[1])*e[1] - p[0]*e[2], z
    )
    assert K.as_expr() == sp.sympify(known[ns]["K"], locals={"z": z})
    cQ, cP, cE, cK = map(content, (Q, P, E, K))
    assert cK == cP * cE
    R = math.factorial(2*n) // math.factorial(n)
    assert R % cQ == R % cP == 0
    assert (2**(4*n) * cQ**2) % cE == 0
    assert (2**(4*n) * R**3) % cK == 0
    Q0 = Q.as_expr() / 2**v2(cQ)
    shifted = sp.Poly(sp.expand(Q0.subs(z, sp.I + 2*sp.I*t)), t)
    sigma = min(gaussian_v2(a) for a in shifted.all_coeffs())
    assert v2(cE) == 2*v2(cQ) + 2*sigma
    V = sp.sympify(row["V"], locals={"t": t})
    Wshift = sp.Poly(sp.expand(t**n * (t+1)**n * V.subs(t, t+1)), t)
    from_shift = sum(
        sp.Integer(math.factorial(k)//math.factorial(n))*Wshift.nth(k)*z**(3*n-k)
        for k in range(n, 3*n+1)
    )
    assert sp.expand(from_shift-P.as_expr()) == 0
    rows[ns] = {
        "p_top": [int(a) for a in p],
        "e_top": [int(a) for a in e],
        "K": str(K.as_expr()),
        "contents_Q_P_E_K": [cQ, cP, cE, cK],
        "R": R,
        "dyadic_sigma": sigma,
        "shifted_W_formula": True,
        "all_assertions_passed": True,
    }

output = {
    "scope": "Only frozen n=1,2 polynomials; no new canonical solve or index scan.",
    "checks": rows,
}
(BASE / "raw_dual_quadratic_content_existing_checks.json").write_text(
    json.dumps(output, indent=2) + "\n"
)
print(json.dumps(output, indent=2))

