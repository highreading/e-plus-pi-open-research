from fractions import Fraction
from math import factorial
import json

MOD = 25

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    return trim(out)

def scale(p, a):
    return trim([a * x for x in p])

def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)

def falling(a, k):
    out = [1]
    for i in range(k):
        out = mul(out, add(a, [-i]))
    return out

def qpower_coefficient(a, t):
    # Exact coefficient of z^t in (1-z+z^2/2)^a,
    # as a rational polynomial in the indeterminate r.
    out = [0]
    for v in range(t // 2 + 1):
        u = t - 2 * v
        weight = Fraction((-1) ** u, (2 ** v) * factorial(u) * factorial(v))
        out = add(out, scale(falling(a, u + v), weight))
    return out

def reduce_poly(p):
    out = []
    for x in p:
        x = Fraction(x)
        assert x.denominator % 5 != 0, ('nonintegral coefficient', x)
        out.append(x.numerator * pow(x.denominator, -1, MOD) % MOD)
    return trim(out)

def radd(*polys):
    out = [0]
    for p in polys:
        out = add(out, p)
    return reduce_poly(out)

def rmul(*polys):
    out = [1]
    for p in polys:
        out = reduce_poly(mul(out, p))
    return out

def rscale(p, a):
    return reduce_poly(scale(p, a))

def rsum(polys):
    out = [0]
    for p in polys:
        out = radd(out, p)
    return out

m = [0, 5]
n = [-1, 5]
cm = [reduce_poly(qpower_coefficient(m, t)) for t in range(11)]
cn = [reduce_poly(qpower_coefficient(n, t)) for t in range(10)]
fm = [reduce_poly(falling(m, t)) for t in range(11)]
fn = [reduce_poly(falling(n, t)) for t in range(11)]

def exponential(offset):
    # e_(10r+offset): start at e_(5u)=1, u=2r+q,
    # then apply the original recurrence inside the block.
    q, s = divmod(offset, 5)
    out = [1]
    for k in range(1, s + 1):
        out = radd(rmul([5 * q + k, 10], out), [1])
    return out

h = rsum(rmul(fm[t], cm[t]) for t in range(10))
u_m = rsum(rmul(fm[t + 1], cm[t]) for t in range(9))
j = radd(h, rsum(rmul(fn[t], cm[t]) for t in range(10)))
k = radd(rmul(n, h), rscale(u_m, 2),
         rsum(rmul(fn[t + 1], cm[t]) for t in range(9)))
h_n = rsum(rmul(fn[t], cn[t]) for t in range(10))
u_n = rsum(rmul(fn[t + 1], cn[t]) for t in range(9))
J_n = radd(rmul(n, h_n), u_n)
A = rsum(rmul(fn[t], cn[t], exponential(-2 - t)) for t in range(10))
B = radd(rscale(exponential(-1), 4),
         rscale(rsum(rmul(fn[t - 1], add(scale(m, 2), [-t]),
                          cm[t], exponential(-1 - t))
                     for t in range(1, 11)), 2))
S_0 = radd(rmul(m, j, j), rscale(rmul(h, k), -1))
W_0 = radd(rmul(j, J_n), rscale(rmul(k, h_n), -1))
C = radd(rmul(radd(rmul(m, j), rscale(h, -1)), J_n),
         rscale(rmul(m, radd(k, rscale(j, -1)), h_n), -1))
F = radd(rscale(rmul(A, S_0), 2), rscale(rmul(B, C), -1),
         rscale(rmul(h, W_0), -2))

actual = {'h': h, 'u_m': u_m, 'j': j, 'k': k, 'h_n': h_n,
          'J_n': J_n, 'A': A, 'B': B, 'S_0': S_0,
          'W_0': W_0, 'C': C, 'F': F}
expected = {'h': [1, 0, 5], 'u_m': [0, 5], 'j': [2, 10, 10],
            'k': [-2, 10, -10], 'h_n': [0, 20],
            'J_n': [-2, 0, -10], 'A': [-7, -15, 15],
            'B': [5, 5], 'S_0': [2, 10, 20],
            'W_0': [-4, -5, 10], 'C': [2, 5, 20], 'F': [20]}
checks = {name: actual[name] == reduce_poly(p) for name, p in expected.items()}
residuals = {name: radd(actual[name], rscale(p, -1))
             for name, p in expected.items()}
print(json.dumps({'modulus': MOD,
                  'coefficient_order': 'increasing powers of the indeterminate r',
                  'actual': actual, 'checks': checks, 'residuals': residuals,
                  'all_passed': all(checks.values()),
                  'scope': 'coefficientwise polynomial identities; no endpoint samples or file writes'},
                 sort_keys=True))
assert all(checks.values())