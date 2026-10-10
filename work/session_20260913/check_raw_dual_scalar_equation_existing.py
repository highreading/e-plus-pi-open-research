"""Audit control from frozen n=1,2 dual polynomials; no new canonical solve."""
from pathlib import Path
import json
import sympy as s

base = Path(__file__).parent
data = json.loads((base / "raw_dual_error_integrals_existing_checks.json").read_text())["checks"]
z = s.symbols("z")
D = 1+z*z
atan_derivatives = [None]+[s.diff(s.atan(z), z, j) for j in range(1, 4)]
out = {}
for ns, item in data.items():
    n = int(ns)
    Q, P, T = [s.sympify(item[key], locals={"z": z}) for key in ("Qhat", "Pe", "Pa")]
    exp_row = lambda r: s.expand(sum(s.binomial(r, j)*(-1)**(r-j)*s.diff(P, z, j) for j in range(r+1)))
    third_row = lambda r: s.cancel(D**3*(s.diff(T, z, r)-sum(s.binomial(r, j)*s.diff(Q, z, r-j)*atan_derivatives[j] for j in range(1, r+1))))
    rows = [[s.diff(Q, z, r), exp_row(r), third_row(r)] for r in range(4)]
    minor = lambda inds: s.expand(s.Matrix([rows[j] for j in inds]).det())
    N012, N013, N023, N123 = [minor(inds) for inds in ((0,1,2), (0,1,3), (0,2,3), (1,2,3))]
    K = s.cancel(N012/(D*z**(6*n)))
    assert s.Poly(K, z).degree() <= 2 and K != 0
    coeffs = [s.cancel(-N123/z**(6*n-2)), s.cancel(N023/z**(6*n-2)),
              s.cancel(-N013/z**(6*n-2)), s.cancel(N012/z**(6*n-2))]
    assert all(s.Poly(A, z).get_domain().is_ZZ for A in coeffs)
    A0, A1, A2, A3 = coeffs
    assert s.expand(A3-z*z*D*K) == 0
    assert s.expand(A2+z*((6*n-z)*D-2*z*s.diff(D,z))*K+z*z*D*s.diff(K,z)) == 0
    assert s.expand(sum(coeffs[r]*s.diff(Q,z,r) for r in range(4))) == 0
    assert s.expand(sum(coeffs[r]*exp_row(r) for r in range(4))) == 0
    assert s.cancel(sum(coeffs[r]*third_row(r) for r in range(4))) == 0
    M = 3*n+1
    g = s.series(P*s.exp(-z)-Q, z, 0, M+5).removeO().expand()
    h = s.series(T-Q*s.atan(z), z, 0, M+5).removeO().expand()
    order = lambda f: min(k[0] for k, c in s.Poly(f, z).terms() if c != 0)
    leadg, leadh = g.coeff(z,M), h.coeff(z,M)
    assert leadg != 0 or leadh != 0
    combination = s.expand(leadh*g-leadg*h)
    v = order(K)
    assert min(order(g),order(h)) == M
    assert order(combination) == M+1+v
    if v == 0:
        assert A1.subs(z,0) == 3*n*(3*n+1)*K.subs(z,0)
    b, c = s.degree(P,z), s.degree(Q,z)
    Vinf = s.expand(T+Q*sum((-1)**j/z**(2*j+1)/s.Integer(2*j+1) for j in range(4)))
    Vinf = s.expand(Vinf-s.expand(Vinf).coeff(z,c)/s.Poly(Q,z).LC()*Q)
    d = max(term.as_powers_dict().get(z,0) for term in s.Add.make_args(Vinf))
    assert b+c+d == 6*n+s.degree(K,z)-3
    klead = s.Poly(K,z).LC()
    assert s.Poly(A1,z).nth(s.degree(K,z)+3) == -(c+d-1)*klead
    assert s.Poly(A0,z).nth(s.degree(K,z)+2) == c*d*klead
    out[ns] = {"K": str(K), "origin_orders": [0, M, M+1+v],
               "infinity_degrees": [int(b), int(c), int(d)],
               "coefficient_degrees_A3_to_A0": [int(s.degree(A,z)) for A in reversed(coeffs)],
               "all_assertions_passed": True}

target = base / "raw_dual_scalar_equation_existing_checks.json"
target.write_text(json.dumps({"scope": "Frozen n=1,2 only; no canonical solve or scan.", "checks": out}, indent=2)+"\n")
print(json.dumps({"saved": str(target), "all_assertions_passed": True}))
