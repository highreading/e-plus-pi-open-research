"""Exact checks at only the two predeclared fixed Schur seeds k=1,2.

This constructs no actual canonical Hermite--Pade degree.
Run with /opt/homebrew/bin/python3.12.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "math_packages"))
import sympy as sp

x = sp.Symbol("x")


def augmented_schur(partition, background):
    length = len(partition)
    degrees = [partition[length - 1 - i] + i for i in range(length)]
    appell = [
        sum(
            sp.binomial(background, h)
            * sp.factorial(d)
            / sp.factorial(d - 2 * h)
            * x ** (d - 2 * h)
            for h in range(d // 2 + 1)
        )
        for d in degrees
    ]
    wronskian = sp.Matrix(
        [[sp.diff(poly, x, j) for j in range(length)] for poly in appell]
    ).det()
    vandermonde = sp.prod(
        degrees[j] - degrees[i]
        for i in range(length)
        for j in range(i + 1, length)
    )
    return sp.Poly(sp.expand(wronskian / vandermonde), x, domain=sp.ZZ).as_expr()


expected = {
    1: {
        "D": x**2 + 4,
        "C": [x**2 - 4, x],
        "J": [5, -2],
        "A": [3, -1],
        "E": 17,
    },
    2: {
        "D": x**6 + 18*x**4 + 432*x**2 - 1296,
        "C": [
            x**6 - 18*x**4 + 216*x**2 + 2592,
            x**5 - 12*x**3 + 72*x,
            x**4 + 108,
        ],
        "J": [-845, -471, 1308],
        "A": [19, -8, 1],
        "E": -10979,
    },
}

results = []
for k in (1, 2):
    b = -k - 1
    full = augmented_schur([k] * (k + 1), b)
    cofactors = [
        augmented_schur([k + 1] * (k - i) + [k] * i, b)
        for i in range(k + 1)
    ]
    constants = [poly.subs(x, 1) for poly in cofactors]
    derivatives = []
    border = []
    for h in range(k + 1):
        derivatives.append(sp.factorial(h) * sum(
            (-1)**(k - i) * sp.binomial(b + i, i - h) * sum(
                sp.binomial(b, u)
                * sp.rf(b + i + 1, 2*u)
                * sp.binomial(b, i + 2*u)
                * constants[i + 2*u]
                for u in range((k - i)//2 + 1)
            )
            for i in range(h, k + 1)
        ))
        border.append(sum(
            (-1)**s * sp.binomial(k, s) * sp.binomial(s, h)
            * sp.ff(b, s - h)
            for s in range(h, k + 1)
        ))
    endpoint = sum(a*j for a, j in zip(border, derivatives))
    control = expected[k]
    checks = {
        "full_polynomial": full == control["D"],
        "cofactor_polynomials": cofactors == control["C"],
        "derivative_seeds": derivatives == control["J"],
        "border_seeds": border == control["A"],
        "endpoint_seed": endpoint == control["E"],
        "zeroth_derivative_normalization": derivatives[0] == full.subs(x, 1),
    }
    assert all(checks.values()), (k, checks)
    results.append({
        "k": k,
        "background": b,
        "D_polynomial": str(full),
        "C_polynomials": [str(poly) for poly in cofactors],
        "D_at_one": int(full.subs(x, 1)),
        "C_at_one": [int(value) for value in constants],
        "J": [int(value) for value in derivatives],
        "A": [int(value) for value in border],
        "E": int(endpoint),
        "checks": checks,
    })

assert results[1]["D_at_one"] % 7 == 2
assert results[1]["E"] % 7 == 4
payload = {
    "scope": "Only fixed small partition seeds k=1,2; no actual degree solve or prime scan.",
    "all_passed": True,
    "results": results,
}
(BASE / "raw_negative_residue_fixed_seed_checks.json").write_text(
    json.dumps(payload, indent=2) + "\n"
)
print(json.dumps(payload, indent=2))
