#!/usr/bin/env python3
"""NEW joint contact-row saturation and binary-force archived-data fields.
No producer, whole-form enclosure or old denominator computation is rerun.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial, gcd
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
sys.set_int_max_str_digits(500000)
C = Path(__file__).resolve().parent
started = time.monotonic()
source = C/'complete_endpoint_3375_certificate.json'
data = json.loads(source.read_text())
n = int(data['n'])
assert n == 3375
m, N = n+1, n+2
nf = factorial(n)

def rational(value):
    return Fraction(int(value['numerator']), int(value['denominator'])) if isinstance(value, dict) else Fraction(int(value))
def integer(value):
    value = rational(value) if isinstance(value, dict) else Fraction(value)
    assert value.denominator == 1
    return value.numerator
def dot(a, b):
    return sum(x*y for x, y in zip(a, b))
def cross(a, b):
    return [a[(i+1)%3]*b[(i+2)%3] - a[(i+2)%3]*b[(i+1)%3] for i in range(3)]
def valuation2(value):
    assert value
    value = abs(value)
    return (value & -value).bit_length()-1

state = data['moment_states']
moments = {k: integer(factorial(k)*rational(state[str(k)]['moment'])) for k in range(n-2, n+3)}
forces = {k: integer(factorial(k)*rational(state[str(k)]['omega'])) for k in range(n, n+3)}
A, B, D = moments[n], moments[n-1], moments[n+1]
X, Y, Z = m*A, m*n*B, 2*D-m*A
J = [[m*N*A, n*m*N*B, n*(n-1)*m*N*moments[n-2]],
     [N*D, m*N*A, n*m*N*B],
     [moments[n+2], N*D, m*N*A]]
columns = [[J[i][j] for i in range(3)] for j in range(3)]
adj = [cross(columns[1], columns[2]), cross(columns[2], columns[0]), cross(columns[0], columns[1])]
detJ = dot(J[0], [adj[i][0] for i in range(3)])
raw = [[sum(seed[k]*adj[k][i] for k in range(3)) for i in range(3)]
       for seed in ([-1, n, -n*m], [0, 0, 1])]
contents = [gcd(*map(abs, row)) for row in raw]
rows = [[entry//content for entry in row] for row, content in zip(raw, contents)]
L = [n*J[i][0]+J[i][1] for i in range(3)]
raw_cross = cross(*raw)
assert raw_cross == [detJ*entry for entry in L]
primitive_cross = cross(*rows)
sigma = gcd(*map(abs, primitive_cross))
contentL = gcd(*map(abs, L))
assert sigma*contents[0]*contents[1] == abs(detJ)*contentL

sieve = bytearray(b'\x01')*(N+1)
sieve[:2] = b'\x00\x00'
for p in range(2, int(N**0.5)+1):
    if sieve[p]:
        for k in range(p*p, N+1, p):
            sieve[k] = 0
primes = [p for p in range(2, N+1) if sieve[p]]
def largepart(value):
    value = abs(value)
    assert value
    for p in primes:
        while value % p == 0:
            value //= p
    return value

sigma_large = largepart(sigma)
assert largepart(contentL) == 1
tau, tau1, rho, rho1 = [rational(data[key]) for key in ('tau_n','tau_n1','rho_n','rho_n1')]
h, ell = integer(nf*tau), integer(nf*tau1)
h1 = integer(Fraction(m,2)*(h+ell))
En = int(data['fixed_exponential_seed'])
b0, b1 = forces[n]-En*h-A, forces[n+1]-En*h1-D
Kcal = h*b1-h1*b0-2*nf**3
v, w = [2*N,N,m], [0,N,2*n+3]
H = [integer(Fraction(m,2)*(h*v[i]+ell*w[i])) for i in range(3)]
U = [m*N*(forces[n]-moments[n]), N*(forces[n+1]-moments[n+1]), forces[n+2]-moments[n+2]]
Q = [integer(2*nf*factorial(m)*(rho*v[i]+rho1*w[i])) for i in range(3)]
Cv = [U[i]-En*H[i]+Q[i] for i in range(3)]
Rvalues, Cvalues = [dot(row,H) for row in rows], [dot(row,Cv) for row in rows]
joint = largepart(gcd(*map(abs, Rvalues+Cvalues)))
saturated = joint//gcd(joint, sigma_large)
boundary_gcd = largepart(gcd(abs(ell),abs(Z),abs(Y-2*X),abs(Kcal)))
assert boundary_gcd % saturated == 0

binary_fields = []
for endpoint, row, content, Rvalue, Cvalue in zip((0,3),rows,contents,Rvalues,Cvalues):
    alpha, beta = dot(row,v), dot(row,w)
    Uvalue = dot(row,U)
    field = {'endpoint':endpoint, 'raw_contact_content_v2':valuation2(content),
             'alpha_v2':valuation2(alpha), 'beta_v2':valuation2(beta),
             'G_v2':valuation2(gcd(abs(alpha),abs(beta))), 'R_v2':valuation2(Rvalue),
             'complete_exterior_exponential_projection_v2':valuation2(Uvalue),
             'complete_seed_and_log_restored_C_v2':valuation2(Cvalue)}
    assert field['raw_contact_content_v2'] == (5 if endpoint==0 else 0)
    assert (field['alpha_v2'],field['beta_v2'],field['G_v2'],field['R_v2'],
            field['complete_exterior_exponential_projection_v2'],field['complete_seed_and_log_restored_C_v2']) == (1,4,1,1691,5,5)
    binary_fields.append(field)

artifact = {'status':'PASS',
    'scope':'NEW exact joint contact-row cross-product/saturation identities and complete-force binary fields from retained original3375 artifact',
    'n':n, 'producer_regenerated':False, 'whole_error_enclosure_regenerated':False,
    'old_denominator_extraction_regenerated':False,
    'raw_cross_product_residual_zero':True, 'integer_saturation_identity_passed':True,
    'primitive_contact_cross_content_bits':sigma.bit_length(),
    'large_contact_saturation_bits':sigma_large.bit_length(),
    'large_shared_column_content':str(largepart(contentL)),
    'actual_joint_large_gcd':str(joint), 'joint_saturated_quotient':str(saturated),
    'actual_boundary_gcd_large':str(boundary_gcd), 'saturated_divisibility_passed':True,
    'binary_fields':binary_fields,
    'infinite_family_theorem_independently_proved':False,
    'endpoint_exclusive_product_bound_proved':False, 'irrationality_proved':False,
    'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'report_sha256':hashlib.sha256((C.parent/'responses/A3_turn8.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-started,3)}
out = C/'endpoint3375_joint_saturation_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt = dict(artifact)
receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256'] = hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint3375_joint_saturation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
