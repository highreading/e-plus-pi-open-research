import json
import math
from functools import reduce
import sympy as s

y = s.symbols('y')
D = [1, 0]
for n in range(2, 33):
    D.append((n-1)*(D[-1]+D[-2]))
mu = [s.Integer(D[2*r]) for r in range(17)]
c = [(mu[r]-(-1)**r)/2 for r in range(17)]
km = [-s.factorial(2*r)-s.factorial(2*r+2)+s.Rational(4, 2*r+1) for r in range(16)]

def value(poly, moments):
    return s.expand(sum(a*moments[idx[0]] for idx, a in s.Poly(s.expand(poly), y).terms()))

def rho0(poly):
    return value(poly, c)

def kap(poly):
    return value(poly, km)

def gcdv(v):
    return reduce(math.gcd, [abs(int(a)) for a in v], 0)

def cv(poly, n):
    return s.Matrix([s.expand(poly).coeff(y, i) for i in range(n)])

def ell(j):
    return s.expand(sum((-1)**(j-r)*s.binomial(2*j, j-r)*s.binomial(2*j+2*r, 2*j)*y**r for r in range(j+1)))

H = {}
U = {}
for m in range(2, 9):
    gram = s.Matrix([[c[i+j] for j in range(m)] for i in range(m)])
    H[m] = gram.det()
    if m <= 7:
        coefficients = gram.inv()*s.Matrix([-c[m+i] for i in range(m)])
        U[m] = s.expand(H[m]*(y**m+sum(coefficients[i]*y**i for i in range(m))))
T = {m: U[m].subs(y, -1) for m in U}
checks = {
    'normalized_moments_integral': all(s.denom(a) == 1 for a in c),
    'moment_content_one': gcdv(c) == 1,
    'normalized_U_integral': all(s.denom(a) == 1 for m in U for a in cv(U[m], m+1)),
    'normalized_norms': all(rho0(U[m]**2) == H[m]*H[m+1] for m in U),
    'initial_H': H[2] == -1 and H[3] == -6416,
    'initial_U': U[2] == -y*y+4*y+117 and s.expand(U[3]-(6416*y-596592)*U[2]-41165056) == 0,
    'initial_endpoint': T[2] == 112 and T[3] == -26371840,
    'normalized_recurrence': all(s.expand(H[m]**2*U[m+1]-(H[m]*H[m+1]*y-rho0(y*U[m]**2))*U[m]+H[m+1]**2*U[m-1]) == 0 for m in range(3, 7)),
    'endpoint_recurrence': all(H[m]**2*T[m+1]+(H[m]*H[m+1]+rho0(y*U[m]**2))*T[m]+H[m+1]**2*T[m-1] == 0 for m in range(3, 7))
}
checks['endpoint_atom_cancellation'] = all(2**m*T[m] == s.Matrix([[mu[i+j] for j in range(m+1)] for i in range(m)]+[[(-1)**j for j in range(m+1)]]).det() for m in range(2, 8))
with open('LOW_PROJECTION_IDENTITY_RECEIPT.json') as handle:
    previous = json.load(handle)
for k in (2, 4):
    L = s.ilcm(*list(range(1, 6*k-4, 2)))
    E = s.Matrix([[L*kap(y**i*U[j]) for j in range(k, 2*k)] for i in range(k-1)])
    cof = s.Matrix([(-1)**r*E[:, [j for j in range(k) if j != r]].det() for r in range(k)])
    t = cof/gcdv(cof)
    Q = s.expand(sum(t[j-k]*U[j] for j in range(k, 2*k)))
    q = cv(Q, 2*k)
    B = s.Matrix.hstack(*[cv(ell(j), 2*k) for j in range(2*k)])
    Delta = B.det()
    v = Delta*B.inv()*q
    g, G = gcdv(q), gcdv(v)
    M = gcdv([H[j]*H[j+1]*t[j-k] for j in range(k, 2*k)])
    endpoint = sum(t[j-k]*T[j] for j in range(k, 2*k))
    Mend = math.gcd(M, abs(int(endpoint)))
    z = v/G
    if z[-1] < 0:
        z = -z
    Lambda, zeta = gcdv(v[:k-1]), gcdv(z[:k-1])
    checks['k'+str(k)] = {
        'recomputed_t_primitive': gcdv(t) == 1,
        'actual_kernel': all(rho0(y**i*Q) == 0 for i in range(k)) and all(kap(y**i*Q) == 0 for i in range(k-1)),
        'normalized_pairings': all(rho0(Q*U[j]) == H[j]*H[j+1]*t[j-k] for j in range(k, 2*k)),
        'endpoint_sum': endpoint == Q.subs(y, -1),
        'g_divides_Mend': Mend % g == 0,
        'theta_divides_Delta': G % g == 0 and Delta % (G//g) == 0,
        'Lambda_equals_G_zeta': Lambda == G*zeta,
        'endpoint_divisibility_bound': (Delta*Mend*zeta) % Lambda == 0,
        'same_primitive_projection_content': str(zeta) == previous['k'+str(k)]['zeta'],
        'zeta': str(zeta),
        'M_over_g': str(M//g),
        'Mend_over_g': str(Mend//g)
    }
    if k == 2:
        checks['k2']['same_primitive_vector'] = [int(a) for a in z] == previous['k2']['z']

def false_flags(obj, prefix=''):
    if isinstance(obj, dict):
        return [flag for name, item in obj.items() for flag in false_flags(item, prefix+'/'+name)]
    return [prefix] if obj is False or obj is s.false else []

checks['false_flags'] = false_flags(checks)
assert not checks['false_flags'], checks['false_flags']
with open('LOW_PROJECTION_NORMALIZED_ENDPOINT_RECEIPT.json', 'w') as handle:
    json.dump(checks, handle, indent=2)
print(json.dumps(checks, indent=2))
