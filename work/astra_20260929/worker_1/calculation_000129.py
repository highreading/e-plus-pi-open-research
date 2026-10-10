from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from math import comb, factorial, gcd, inf
import json

root = Path('[private local path removed]')
candidate = root / 'work/astra_review_registry/candidates/worker4-b2-five-adic-residue-two-conditional-content-v1.md'
data = candidate.read_bytes()
expected = '2c26bae0fb61072731e91f2bcb1cbca24f0ad4281c0323753d425900c5986932'
# Identify the registered payload independently of the presentation header.
starts = [0] + [i + 1 for i, value in enumerate(data) if value == 10]
matches = {}
for start in starts:
    suffix = data[start:]
    for payload in (suffix, suffix.rstrip(b'\n'), suffix + b'\n'):
        if sha256(payload).hexdigest() == expected:
            matches[payload] = start
assert len(matches) == 1, 'Registered payload not uniquely identified'
payload, payload_start = next(iter(matches.items()))
print(json.dumps({'provenance': {'file_sha256': sha256(data).hexdigest(), 'payload_sha256': expected, 'payload_start': payload_start, 'payload_bytes': len(payload)}}))
print(payload.decode('utf-8'))

samples = [7, 12, 27]
maximum = max(samples)
fac = [factorial(j) for j in range(2 * maximum + 4)]
e = [1]
for j in range(1, len(fac)):
    e.append(j * e[-1] + 1)
E = [Q(e[j], fac[j]) for j in range(len(fac))]

# Original Rodrigues polynomial, expanded with integer convolution.
powers = [[1]]
for m in range(1, maximum + 2):
    out = [0] * (len(powers[-1]) + 2)
    for j, value in enumerate(powers[-1]):
        out[j] += value
        out[j + 1] -= 2 * value
        out[j + 2] += 2 * value
    powers.append(out)
Lpoly = [[comb(m + d, m) * powers[m][m + d] for d in range(m + 1)] for m in range(len(powers))]

mu = []
real, imaginary = 1, 0
for j in range(maximum + 2):
    real, imaginary = real - imaginary, real + imaginary
    mu.append(Q(2 * imaginary, 2**j * (j + 1)))

def val(value):
    value = Q(value)
    if not value:
        return inf
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % 5 == 0:
        numerator //= 5
        result += 1
    while denominator % 5 == 0:
        denominator //= 5
        result -= 1
    return result

def content(poly):
    return min(map(val, poly))

def multiply(left, right):
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out

def ell(poly, n, shift):
    return sum((Q(coefficient, fac[n + d + 1 - shift]) for d, coefficient in enumerate(poly)), Q(0))

def partial_exp(poly, n, shift):
    return sum((coefficient * E[n + d - shift] for d, coefficient in enumerate(poly)), Q(0))

def cross(left, right):
    return [left[1]*right[2]-left[2]*right[1], left[2]*right[0]-left[0]*right[2], left[0]*right[1]-left[1]*right[0]]

def contracted_difference(poly, n, shift):
    # Apply ell in s to (V(t)-V(s))/(t-s), retaining t coefficients.
    out = [Q(0)] * (len(poly) - 1)
    for d in range(1, len(poly)):
        for exponent_s in range(d):
            out[d - 1 - exponent_s] += Q(poly[d], fac[n + exponent_s + 1 - shift])
    return out

rows = []
for n in samples:
    P, U = Lpoly[n], Lpoly[n + 1]
    a, b = sum(P), sum(U)
    G = Q((-1)**n * 2**(2*n + 3), n + 1)
    f = Q(2**n, fac[n]**2)
    r = val(fac[n])
    precision_loss = 0
    power = 5
    while power <= n:
        precision_loss += 1
        power *= 5
    assert val(n + 1) == val(G) == 0
    alpha = [ell(U, n, j) for j in range(3)]
    tp = [partial_exp(P, n, j) for j in range(3)]
    tu = [partial_exp(U, n, j) for j in range(3)]
    assert all(val(value / f) >= 0 for value in tp + tu)
    tau = [(a * tu[j] - b * tp[j]) / G for j in range(3)]
    beta = cross(alpha, [1 + value for value in tau])
    assert content(alpha) >= -2*r
    assert content([1 + value for value in tau]) >= -2*r
    assert content(beta) >= -4*r

    projected_kernels = []
    for shift in range(3):
        left = multiply(P, contracted_difference(U, n, shift))
        right = multiply(U, contracted_difference(P, n, shift))
        assert len(left) == len(right)
        kernel = [(x-y)/G for x, y in zip(left, right)]
        assert all(value == 0 for value in kernel[n+1:])
        kernel = kernel[:n+1]
        assert all(val(fac[n]**2 * value) >= 0 for value in kernel)
        projected_kernels.append(kernel)
    qpoly = [-sum((beta[j] * projected_kernels[j][d] for j in range(3)), Q(0)) for d in range(n+1)]
    Cpoly = list(reversed(qpoly))
    Apoly = []
    for degree in range(n+1):
        exp_part = sum((beta[j] / fac[degree-j] for j in range(min(2,degree)+1)), Q(0))
        moment_part = sum((Cpoly[j] * mu[degree-j-1] for j in range(degree)), Q(0))
        Apoly.append(-exp_part-moment_part)

    cA, cB, cC = map(content, (Apoly, beta, Cpoly))
    endpoint_A, endpoint_B = sum(Apoly), sum(beta)
    assert endpoint_B == sum(Cpoly)
    # These endpoint valuations are the published conditional inputs;
    # the new calculation checks the full coefficient normalization.
    assert val(endpoint_A) == -6*r
    assert val(endpoint_B) == -4*r
    assert cB == -4*r
    assert cC >= -6*r
    assert cA >= -6*r-precision_loss
    nu = min(cA,cB,cC)
    assert -6*r-precision_loss <= nu <= -6*r
    loss = -6*r-nu

    all_coefficients = Apoly + beta + Cpoly
    clearing = 1
    for value in all_coefficients:
        clearing = clearing // gcd(clearing,value.denominator) * value.denominator
    integral_coefficients = [value*clearing for value in all_coefficients]
    assert all(value.denominator == 1 for value in integral_coefficients)
    common_content = 0
    for value in integral_coefficients:
        common_content = gcd(common_content,abs(value.numerator))
    scale = Q(clearing,common_content)
    primitive = [value*scale for value in all_coefficients]
    assert all(value.denominator == 1 for value in primitive)
    primitive_content = 0
    for value in primitive:
        primitive_content = gcd(primitive_content,abs(value.numerator))
    assert primitive_content == 1
    assert val(scale) == -nu
    primitive_A, primitive_B = endpoint_A*scale, endpoint_B*scale
    assert primitive_A.denominator == primitive_B.denominator == 1
    endpoint_gcd = gcd(abs(primitive_A.numerator),abs(primitive_B.numerator))
    assert val(primitive_A) == loss
    assert val(primitive_B) == 2*r+loss
    assert val(endpoint_gcd) == loss
    assert 0 <= loss <= precision_loss
    rows.append({'n':n, 'r':r, 'floor_log5_n':precision_loss, 'coefficient_valuations':{'A':cA,'B':cB,'C':cC,'full':nu}, 'primitive_extra_loss_c':loss, 'primitive_endpoint_valuations':{'A':val(primitive_A),'B':val(primitive_B),'gcd':val(endpoint_gcd)}, 'primitive_endpoint_gcd':str(endpoint_gcd), 'projected_kernel_valuations':[content(poly) for poly in projected_kernels], 'full_primitive_coefficient_gcd':primitive_content})
print(json.dumps({'independent_coefficient_checks':rows,'all_assertions_passed':True}))