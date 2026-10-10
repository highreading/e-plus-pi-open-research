from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from math import factorial
import json

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/worker2-dyadic-analytic-tail-and-precision-v1.md'
raw = path.read_bytes()
expected_payload = '3b220a9384536f55319370fb83bde92220ecf1b8ea1e296bd0a6a6662f42d7ab'
expected_file = '69d7d01eb3dd684ffbb530f2f76f4530d3b378ab0eace8673d9e1257232e75a7'
marker = raw.index(b'Content SHA256: ')
header_end = raw.index(b'\n', marker)
assert raw[marker:header_end].decode() == 'Content SHA256: ' + expected_payload
payload_start = raw.index(b'\n\n', marker) + 2
payload = raw[payload_start:]
assert sha256(raw).hexdigest() == expected_file
assert sha256(payload).hexdigest() == expected_payload

def falling(x, length):
    out = 1
    for t in range(length):
        out *= x - t
    return out

def d_nonnegative(x):
    assert x >= 0
    return sum(falling(x, j) for j in range(x + 1))

# Only R <= 2 can contribute at X=1; subsequent kernels vanish exactly.
rows = []
H = K = A = B = Fraction(0)
for R in range(3):
    for c in range(R // 2 + 1):
        b = R - 2*c
        s = b+c
        epsilon = Fraction((-1)**b, 2**c * factorial(b) * factorial(c))
        h = epsilon * falling(1,R) * falling(1,s)
        k = Fraction(2) if R == 0 else epsilon * falling(1,R-1) * falling(2,s) * (4-R)
        H += h
        K += k
        A += h*d_nonnegative(2-R)
        B += k*d_nonnegative(3-R)
        rows.append({'b':b,'c':c,'h':str(h),'k':str(k)})
assert (H,K,A,B) == (0,0,3,10)
assert K*A-H*B == 0

arrays = {1:[0,216,32,768,512],3:[652,296,544,128],5:[564,184,672,768,512],7:[824,808,480,128]}
normalized = {}
for a, coeffs in arrays.items():
    divisor = 4 if a in (3,5) else 8
    assert all(v % divisor == 0 for v in coeffs)
    quotient = [v // divisor for v in coeffs]
    if a == 1:
        assert quotient[0] == 0
        quotient = quotient[1:]
    normalized[a] = {'modulus':1024//divisor,'coefficients':quotient}
assert normalized[1]['coefficients'] == [27,4,96,64]
assert normalized[3]['coefficients'] == [163,74,136,32]
assert normalized[5]['coefficients'] == [141,46,168,192,128]
assert normalized[7]['coefficients'] == [103,101,60,16]
outer_bound = Fraction(5*55,16)-7
inner_bound = Fraction(7*20,8)-3
assert outer_bound == Fraction(163,16) and outer_bound > 10
assert inner_bound == Fraction(29,2) and inner_bound > 10
print(json.dumps({'file_bytes':len(raw),'file_sha256':sha256(raw).hexdigest(),'payload_byte_offset':payload_start,'payload_bytes':len(payload),'payload_sha256':sha256(payload).hexdigest(),'identity_verified':True,'specialization_terms':rows,'H_K_A_B_at_1':[str(v) for v in (H,K,A,B)],'normalized_congruences':normalized,'outer_bound_at_55':str(outer_bound),'inner_bound_at_20':str(inner_bound)},indent=2))