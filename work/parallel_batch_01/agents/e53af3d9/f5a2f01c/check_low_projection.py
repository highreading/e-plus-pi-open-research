import json
import math
from functools import reduce
import sympy as s

y = s.symbols('y')
# Sufficient for all norms through degree seven and H_8.
D = [1, 0]
for n in range(2, 33):
    D.append((n-1)*(D[-1]+D[-2]))
C = [s.Integer(D[2*r])-(-1)**r for r in range(17)]
F = [s.factorial(2*r) for r in range(17)]
K = [-F[r]-F[r+1]+s.Rational(4, 2*r+1) for r in range(16)]

def value(poly, moments):
    return s.expand(sum(c*moments[idx[0]] for idx, c in s.Poly(s.expand(poly), y).terms()))

def rho(poly):
    return value(poly, C)

def kap(poly):
    return value(poly, K)

def gcd_vector(v):
    return reduce(math.gcd, [abs(int(a)) for a in v], 0)

def ell(j):
    return s.expand(sum((-1)**(j-r)*s.binomial(2*j, j-r)*s.binomial(2*j+2*r, 2*j)*y**r for r in range(j+1)))

def coeff_vector(poly, n):
    return s.Matrix([s.expand(poly).coeff(y, i) for i in range(n)])

def integral_vector(v):
    return all(s.denom(a) == 1 for a in v)

checks = {}
checks['derangement_recurrence'] = all(D[2*r+2] == (2*r+2)*(2*r+1)*D[2*r]-(2*r+1) for r in range(16))
p = {2: y*y-4*y-117}
h = {2: rho(p[2]**2)}
a2 = s.cancel(rho(y*p[2]**2)/h[2])
p[3] = s.expand((y-a2)*p[2]-h[2]/2)
h[3] = rho(p[3]**2)
for m in range(3, 7):
    a = s.cancel(rho(y*p[m]**2)/h[m])
    b = s.cancel(h[m]/h[m-1])
    p[m+1] = s.expand((y-a)*p[m]-b*p[m-1])
    h[m+1] = rho(p[m+1]**2)
H = {m: s.Matrix([[C[a+b] for b in range(m)] for a in range(m)]).det() for m in range(2, 9)}
U = {m: s.expand(H[m]*p[m]) for m in range(2, 8)}
checks['initial_values'] = {'H2': str(H[2]), 'H3': str(H[3]), 'h2': str(h[2]), 'a2': str(a2), 'rho_y_p2_squared': str(rho(y*p[2]**2))}
checks['orthogonality_degrees_2_through_7'] = all(rho(y**i*p[m]) == 0 for m in range(2, 8) for i in range(m))
checks['integer_U_degrees_2_through_7'] = all(integral_vector(coeff_vector(U[m], m+1)) for m in range(2, 8))
checks['norm_identities'] = all(rho(U[m]**2) == H[m]*H[m+1] for m in range(2, 8))
checks['exceptional_initial_step'] = s.expand(U[3]-(12832*y-1193184)*U[2]-329320448) == 0
checks['cleared_recurrence'] = all(s.expand(H[m]**2*U[m+1]-(H[m]*H[m+1]*y-rho(y*U[m]**2))*U[m]+H[m+1]**2*U[m-1]) == 0 for m in range(3, 7))
legendre_checks = []
for r in range(7):
    a = s.Rational((2*r+1)*(2*r+2), 4*(4*r+1)*(4*r+3))
    b = s.Rational((2*r+1)**2, (4*r+1)*(4*r+3))+s.Rational(4*r*r, (4*r+1)*(4*r-1))
    c = s.Rational(8*r*(2*r-1), (4*r+1)*(4*r-1))
    rhs = a*ell(r+1)+b*ell(r)+(c*ell(r-1) if r else 0)
    legendre_checks.append(s.expand(y*ell(r)-rhs) == 0)
checks['legendre_multiplication'] = all(legendre_checks)
# Exactly two instances: boundary counterexample and a nontrivial recurrence reconstruction.
for k in (2, 4):
    L = s.ilcm(*list(range(1, 6*k-4, 2)))
    E = s.Matrix([[L*kap(y**i*U[j]) for j in range(k, 2*k)] for i in range(k-1)])
    cofactor = s.Matrix([(-1)**r*E[:, [j for j in range(k) if j != r]].det() for r in range(k)])
    dE = gcd_vector(cofactor)
    assert dE > 0
    t = cofactor/dE
    Q = s.expand(sum(t[r]*U[k+r] for r in range(k)))
    q = coeff_vector(Q, 2*k)
    B = s.Matrix.hstack(*[coeff_vector(ell(j), 2*k) for j in range(2*k)])
    Delta = B.det()
    v = Delta*B.inv()*q
    assert integral_vector(v)
    g = gcd_vector(q)
    G = gcd_vector(v)
    low = gcd_vector(v[:k-1])
    z = v/G
    if z[-1] < 0:
        z = -z
    zeta = gcd_vector(z[:k-1])
    M = gcd_vector([H[j]*H[j+1]*t[j-k] for j in range(k, 2*k)])
    norm_lcm = s.ilcm(*[abs(H[j]*H[j+1]) for j in range(k, 2*k)])
    W = s.Matrix([[rho(ell(i)*ell(j)) for j in range(2*k)] for i in range(k)]+[[L*kap(ell(i)*ell(j)) for j in range(2*k)] for i in range(k-1)])
    entry = {
        'E_integral': integral_vector(E),
        'reduced_rank': E.rank(),
        'W_rank': W.rank(),
        'right_block_rank': W[:, k-1:].rank(),
        'E_t_zero': E*t == s.zeros(k-1, 1),
        'primitive_t': gcd_vector(t) == 1,
        'W_z_zero': W*z == s.zeros(2*k-1, 1),
        'primitive_z': gcd_vector(z) == 1,
        'pairing_identity': all(rho(Q*U[j]) == H[j]*H[j+1]*t[j-k] for j in range(k, 2*k)),
        'g_divides_M': M % g == 0,
        'M_divides_norm_lcm': norm_lcm % M == 0,
        'G_divisible_by_g': G % g == 0,
        'theta_divides_Delta': Delta % (G//g) == 0,
        'Lambda_equals_G_zeta': low == G*zeta,
        'Lambda_divides_Delta_M_zeta': (Delta*M*zeta) % low == 0,
        'g': str(g), 'G': str(G), 'M': str(M),
        'Lambda': str(low), 'zeta': str(zeta)
    }
    if k == 2:
        Q0 = -2015194+8115147*y-4687490*y*y+79961*y**3
        claimed = [-218267280, 639779668, -60435570, 79961]
        entry['z'] = [int(a) for a in z]
        entry['claimed_z_matches'] = entry['z'] == claimed
        entry['claimed_monomial_kernel'] = all(rho(y**i*Q0) == 0 for i in range(2)) and kap(Q0) == 0
        entry['claimed_basis_identity'] = s.expand(924*Q0-sum(claimed[j]*ell(j) for j in range(4))) == 0
        entry['zeta_factorization'] = {str(a): int(b) for a, b in s.factorint(zeta).items()}
    checks['k'+str(k)] = entry

def false_flags(obj, prefix=''):
    found = []
    if isinstance(obj, dict):
        for name, item in obj.items():
            found += false_flags(item, prefix+'/'+name)
    elif obj is False:
        found.append(prefix)
    return found
checks['false_flags'] = false_flags(checks)
assert not checks['false_flags'], checks['false_flags']
with open('LOW_PROJECTION_IDENTITY_RECEIPT.json', 'w') as handle:
    json.dump(checks, handle, indent=2)
print(json.dumps(checks, indent=2))
