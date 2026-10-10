"""Parent-owned bounded comparison: integer binomial sum versus F4 carry rule.

Run only inside the no-network math sandbox. No original matrix is built.
"""
from pathlib import Path
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
receipt = HERE / 'ALL_ORDER_CONTACT_JET_BINARY_FILTER_RECEIPT.json'
assert not receipt.exists()

def fmul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return result

def omega(e):
    return (1, 2, 3)[e % 3]

def trace(a):
    out = a ^ fmul(a, a)
    assert out in (0, 1)
    return out

def coefficient(a, b, k):
    weights = [1, 0]
    for i in range(max(a,b,k).bit_length()+1):
        next_weights = [0, 0]
        for carry, weight in enumerate(weights):
            for ub in range(((a >> i) & 1)+1):
                for vb in range(((b >> i) & 1)+1):
                    s = ub+vb+carry
                    if s % 2 != ((k >> i) & 1):
                        continue
                    next_weights[s//2] ^= fmul(weight, omega(-vb*(1 << i)))
        weights = next_weights
    return fmul(omega(2*b), weights[0])

def digit_value(d, r, j):
    n, k = d+j, r+j
    left = fmul(1 ^ (2 if (r+1) % 2 else 0), coefficient(r,n,k))
    right = fmul(3, coefficient(r+1,n-1,k)) if n % 2 else 0
    return trace(fmul(omega(r+2), left ^ right))

def integer_value(d, r, j):
    n, k = d+j, r+j
    value = 0
    for l in range(j,n+1):
        m = l+r
        eta = (1,0,1)[m % 3] ^ (((m+1) % 2)*(1,0,1)[(m+1) % 3])
        value ^= (math.comb(n,l)*math.comb(l+r,k)*eta) % 2
    return value

ds = (2,8,16,32,48,64,80,96,112)
total = beyond_old_cutoff = derivative_sensitive = 0
for d in ds:
    for r in range(32):
        for j in range(32):
            a, b = digit_value(d,r,j), integer_value(d,r,j)
            assert a == b, (d,r,j,a,b)
            total += 1
            beyond_old_cutoff += r+j >= 16
            n, k = d+j, r+j
            incomplete = trace(fmul(omega(r+2), fmul(1 ^ (2 if (r+1) % 2 else 0), coefficient(r,n,k))))
            derivative_sensitive += incomplete != b
assert total == 9216 and derivative_sensitive > 0
data = {
    'status': 'PASS',
    'comparisons': total,
    'cases_with_r_plus_j_at_least16': beyond_old_cutoff,
    'cases_wrong_if_derivative_term_omitted': derivative_sensitive,
    'd_inputs': list(ds),
    'r_range': [0,31],
    'j_range': [0,31],
    'maximum_integer_binomial_upper_argument': 174,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_note_sha256': hashlib.sha256((HERE/'COORDINATOR_ALL_ORDER_CONTACT_JET_BINARY_FILTER.md').read_bytes()).hexdigest(),
    'scope': 'Independent finite arithmetic authentication of the new all-order source-jet filter, including beyond the old cutoff. The general law is its algebraic derivation; no original-index matrix, attaining growing cofactor, correction flag, final pair, or gcd bound is verified here.',
    'independent_mechanisms': ['Exact integer binomial sum with the contact recurrence', 'Weighted two-carry F4 digit calculation'],
}
receipt.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data),flush=True)
