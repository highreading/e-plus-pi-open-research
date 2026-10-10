"""One fixed limiting-operator certificate. No canonical degree is solved.

The saved approximate vectors are treated as exact dyadic rationals.
Every asserted enclosure below uses outward-rounded mpmath interval arithmetic.
The proof of the analytic quadrature and infinite-tail bounds is in the note.
"""
import json
import math
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "math_packages"))
from mpmath import iv

iv.dps = 100
L, J, M, TERMS = 64, 128, 512, 24
R = iv.mpf(4) / 3
ONE, ZERO = iv.mpf(1), iv.mpf(0)
a = iv.sqrt(3) / 2
gamma = a / 2
ii = iv.mpc(0, 1)

def upper(x):
    return x.b

def cab(z):
    """A rigorous scalar upper bound for the complex modulus."""
    return upper(abs(z.real)) + upper(abs(z.imag))

def widen(z, eps):
    rad = iv.mpf([-1, 1]) * eps
    return iv.mpc(z.real + rad, z.imag + rad)

def exact_complex(pair):
    return iv.mpc(iv.mpf(pair[0][0])/pair[0][1],
                  iv.mpf(pair[1][0])/pair[1][1])

raw = json.loads((BASE/"raw_odd_limit_certificate_vectors.json").read_text())
assert raw["L"] == L
f = [[exact_complex(z) for z in col] for col in raw["solutions"]]
assert all(len(col) == 2*L for col in f)

# Outward intervals for the exact M-point periodic trapezoidal coefficients.
# Symmetry in theta permits paired cosine quadrature.
fc = [[[iv.mpc(0) for _ in range(2)] for _ in range(2)]
      for _ in range(J+1)]
series_error = iv.mpf(2) / math.factorial(2*TERMS)
for node in range(M//2 + 1):
    theta = 2*iv.pi*node/M
    ct = iv.cos(theta)
    y = iv.sqrt(3)*ct
    t = (1+ii*y)/(1-ii*y)
    power = iv.mpc(1)
    c, s = iv.mpc(0), iv.mpc(0)
    for j in range(TERMS):
        c += power/math.factorial(2*j)
        s += power/math.factorial(2*j+1)
        power *= t
    c, s = widen(c, series_error), widen(s, series_error)
    F = [[c, t*s], [s, c]]
    weight = 1 if node in (0, M//2) else 2
    prev, cur = ONE, ct
    for k in range(J+1):
        cosine = ONE if k == 0 else cur
        for u in range(2):
            for v in range(2):
                fc[k][u][v] += weight*cosine*F[u][v]/M
        if k >= 1:
            prev, cur = cur, 2*ct*cur-prev
    if node % 64 == 0:
        print(f"validated quadrature nodes {node}/{M//2}", flush=True)

alias = 32*R**(-(M-J))/(1-R**(-M))
for k in range(J+1):
    for u in range(2):
        for v in range(2):
            fc[k][u][v] = widen(fc[k][u][v], alias)

# The complete limiting endpoint vector has a known geometric tail.
v = []
for r in range(J+1):
    v.extend([iv.sqrt(iv.mpf(2)/3)*(ii/iv.sqrt(3))**r,
              iv.mpc(0)])

def rhs(column, r, channel):
    if column < 2:
        return gamma if r == 0 and channel == column else iv.mpc(0)
    return v[2*r+channel]

errors = []
Efs = []
for col in range(3):
    ef = [[iv.mpc(0), iv.mpc(0)] for _ in range(J+1)]
    for r in range(J+1):
        for s in range(L):
            C = fc[abs(r-s)]
            for u in range(2):
                ef[r][u] += C[u][0]*f[col][2*s] + C[u][1]*f[col][2*s+1]
    Efs.append(ef)
    residual_l1 = ZERO
    for r in range(J):
        low = ef[r-1] if r else [iv.mpc(0), iv.mpc(0)]
        high = ef[r+1]
        tf = [(ef[r][1]+ii*a*(low[1]+high[1]))/2,
              (ef[r][0]-ii*a*(low[0]+high[0]))/2]
        for u in range(2):
            residual_l1 += cab(rhs(col, r, u)-tf[u])
    weighted_f = sum(
        R**(s-(L-1))*(cab(f[col][2*s])+cab(f[col][2*s+1]))
        for s in range(L)
    )
    # The tail of A0 E f from position J is bounded by the tail of E f
    # from J-1, because A0 has bandwidth one and norm at most one.
    tail_ef = 16*weighted_f*R**(-(J-L))/iv.sqrt(1-R**(-2))
    tail_rhs = iv.mpf(3)**(-iv.mpf(J)/2) if col == 2 else ZERO
    residual = residual_l1+tail_ef+tail_rhs
    error = 12*residual  # rigorous ||(A0 E)^(-1)|| < 12
    assert error < iv.mpf(1)/10**7
    errors.append(upper(error))
    print(f"solution {col}: error <= {error}", flush=True)

# Exact finite-support testing, then inflate by the solved-vector errors.
# W=outside row -1 of F(J), V=Jb W with Jb=[[0,i],[-i,0]].
top = []
bottom = []
for col in range(3):
    wf = [iv.mpc(0), iv.mpc(0)]
    for s in range(L):
        C = fc[s+1]
        for u in range(2):
            wf[u] += C[u][0]*f[col][2*s]+C[u][1]*f[col][2*s+1]
    test = [ii*wf[1], -ii*wf[0]]
    top.append([widen(z, 3*errors[col]) for z in test])  # ||V||<=e<3
    b = sum(iv.mpc(v[2*s].real,-v[2*s].imag)*f[col][2*s]
            for s in range(L))
    bottom.append(widen(b, errors[col]))  # ||v||=1

D2 = [[top[j][i]+(1 if i == j else 0) for j in range(2)]
      for i in range(2)]
D3 = [D2[0]+[top[2][0]], D2[1]+[top[2][1]], bottom]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def det3(A):
    return sum((-1)**j*A[0][j]*det2(
        [[A[r][k] for k in range(3) if k != j] for r in (1,2)])
        for j in range(3))

d2, d3 = det2(D2), det3(D3)
assert d2.real > iv.mpf(62)/100
assert d2.real < iv.mpf(63)/100
assert d3.real > -iv.mpf(136)/100
assert d3.real < -iv.mpf(135)/100
assert abs(d2.imag) < iv.mpf(1)/10**6
assert abs(d3.imag) < iv.mpf(1)/10**6
ratio = d2/d3
assert ratio.real > -iv.mpf(47)/100
assert ratio.real < -iv.mpf(45)/100

result = {
    "status": "PASS",
    "fixed_parameters": {"L":L, "output_cutoff":J, "quadrature_nodes":M,
                         "Taylor_terms":TERMS, "interval_decimal_precision":iv.dps},
    "method":"outward interval quadrature + analytic alias bound + full half-line residual",
    "solution_error_intervals":[str(x) for x in errors],
    "alias_bound":str(alias),
    "D2":[[str(z) for z in row] for row in D2],
    "D3":[[str(z) for z in row] for row in D3],
    "det_D2":str(d2), "det_D3":str(d3), "ratio":str(ratio),
    "certified_real_bounds":{"det_D2":["0.62","0.63"],
                            "det_D3":["-1.36","-1.35"],
                            "ratio":["-0.47","-0.45"]},
    "new_canonical_degrees_solved":0,
}
(BASE/"raw_odd_limit_interval_certificate.json").write_text(
    json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2), flush=True)
