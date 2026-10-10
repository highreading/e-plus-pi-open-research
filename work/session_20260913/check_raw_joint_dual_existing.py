"""Exact joint-dual controls using only the previously saved n=1,2 vectors."""
from pathlib import Path
import json
import sympy as s

t, x, z = s.symbols("t x z")
saved = {1: [-2, 3, -1], 2: [940, -1944, 1117, -162, 49]}
out = {}
for n, w in saved.items():
    W = s.expand(sum(w[r]*t**(n+r) for r in range(2*n+1)))
    V, rem = s.div(W, t**n*(t-1)**n, t)
    assert rem == 0
    S0 = s.expand(sum(s.factorial(r)*w[r]*t**(n+r) for r in range(2*n+1)))
    U, rem = s.div(S0, (1+t*t)**n, t)
    assert s.degree(rem, t) < n
    q = s.expand(sum(s.Poly(U, t).nth(n-j)*z**j for j in range(n+1)))
    H = sum(s.binomial(n, h)*x**(2*h)/s.factorial(2*h) for h in range(n+1))
    applied = s.expand(sum(s.Poly(q, z).nth(j)*s.diff(H, x, j) for j in range(n+1)))
    assert s.expand(applied-(x-1)**n*V.subs(t, x)) == 0
    a = s.Poly(s.expand((1+z*z)**n*sum(z**j/s.factorial(j) for j in range(2*n+1))), z)
    coeff = lambda k: a.nth(k) if k >= 0 else s.S.Zero
    moment = lambda k: coeff(2*n-k)
    mu = lambda p: s.expand(sum(c*moment(k[0]) for k, c in s.Poly(p, z).terms()))
    for k in range(2*n+4):
        assert moment(k) == s.diff(H, x, k).subs(x, 1)
        target = 0 if k < n else s.factorial(k)*s.diff(V, t, k-n).subs(t, 1)/s.factorial(k-n)
        assert s.expand(mu(z**k*q)-target) == 0
        assert moment(k+3)+(k+2)*moment(k+2)+moment(k+1)+(k-2*n)*moment(k) == 0
    assert mu(q*q) == s.factorial(n)*U.subs(t, 0)*V.subs(t, 1)
    item = {"H": str(H), "q": str(q), "quadratic_value": str(mu(q*q)),
            "all_joint_and_Pearson_controls_pass": True}
    if n == 2:
        A = s.Matrix(n+1, n+1, lambda i, j: coeff(n+i-j))
        qvec = s.Matrix([s.Poly(q, z).nth(j) for j in range(n+1)])
        assert A*qvec == s.Matrix([s.factorial(n)*V.subs(t, 1), 0, 0])
        assert A.inv()[0, 0] == s.Rational(588, 925)
        assert s.Matrix([[2, 1], [1, 2]]).inv()[0, 0] == s.Rational(2, 3)
        assert s.discriminant(V, t) < 0
        arc = 4704*x*x-1380*s.sqrt(2)*x-2266
        assert arc.subs(x, 1/s.sqrt(2)) == -1294
        assert 2438**2 > 2*1380**2
        assert mu(q*q) == -218300
        item.update({"A": str(A), "A_inverse_00": str(A.inv()[0, 0]),
                     "V_endpoint_to_leading": str(V.subs(t, 1)/s.Poly(V, t).LC()),
                     "arc_at_outer_endpoint": "-1294", "arc_at_center": "2438-1380*sqrt(2)>0"})
    out[str(n)] = item

target = Path(__file__).with_name("raw_joint_dual_existing_checks.json")
target.write_text(json.dumps({"scope": "Only already saved n=1,2; no new solve or scan.",
                              "checks": out}, indent=2)+"\n")
print(json.dumps({"saved": str(target), "all_assertions_passed": True}))
