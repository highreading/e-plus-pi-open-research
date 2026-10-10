from pathlib import Path
from hashlib import sha256
from math import gcd
import json

path = Path('work/astra_review_registry/candidates/worker3-algebraic-dyadic-root-depth-obstruction-v1.md')
raw = path.read_bytes()
expected = '3efb8a94a32696dc881df697f9d4aa6995eb2935c5fc12341db35ef6f7d2cf1d'
marker = b'UNVERIFIED CANDIDATE FOR INDEPENDENT REVIEW.'
assert raw.count(marker) == 1
start = raw.index(marker)
body = raw[start:]
variants = [('exact_body', body)]
if body.endswith(b'\n'):
    variants.append(('body_without_one_terminal_newline', body[:-1]))
hashes = [{'representation': name, 'bytes': len(data), 'sha256': sha256(data).hexdigest()} for name, data in variants]
matches = [item for item in hashes if item['sha256'] == expected]
print(json.dumps({'file_bytes': len(raw), 'file_sha256': sha256(raw).hexdigest(), 'body_offset': start, 'payload_checks': hashes, 'registered_payload_matched': bool(matches)}, sort_keys=True))
assert matches, 'Registered payload was not identified'

def v2_integer(m):
    m = abs(m)
    assert m != 0
    return (m & -m).bit_length() - 1

rational_checks = 0
integer_equalities = 0
for a in range(-15, 16):
    for b in range(1, 16, 2):
        if gcd(a, b) != 1:
            continue
        for n in range(1, 129):
            m = b*n-a
            if m == 0:
                integer_equalities += 1
                continue
            depth = v2_integer(m)
            assert 2**depth <= abs(m) <= (b+abs(a))*n
            rational_checks += 1

# Construct t modulo 2^80 with 4t^2+t-1=0; alpha=1+8t then satisfies alpha^2=17.
t = 0
for k in range(80):
    modulus = 1 << (k+1)
    if (4*t*t+t-1) % modulus:
        t += 1 << k
    assert (4*t*t+t-1) % modulus == 0
alpha_mod = 1+8*t
precision = 83
assert (alpha_mod*alpha_mod-17) % (1 << precision) == 0
quadratic_checks = 0
for n in range(1, 1025):
    difference = (n-alpha_mod) % (1 << precision)
    assert difference != 0, 'Insufficient precision for this integer'
    depth = v2_integer(difference)
    value = n*n-17
    assert value != 0
    assert depth <= v2_integer(value)
    assert 2**depth <= abs(value) <= 18*n*n
    quadratic_checks += 1

# Arbitrary annihilating polynomials may have extraneous integer zeros.
assert 3*2*2-7*2+2 == 0
assert 3*2-1 != 0
print(json.dumps({'rational_nonzero_checks': rational_checks, 'rational_integer_equalities_excluded': integer_equalities, 'quadratic_root_checks': quadratic_checks, 'extraneous_integer_zero_checked': True, 'scope': 'Finite arithmetic corroboration only; the general proof is the independent derivation in the accompanying note.'}, sort_keys=True))