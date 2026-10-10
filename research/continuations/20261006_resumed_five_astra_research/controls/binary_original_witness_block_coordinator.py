#!/usr/bin/env python3
"""New direct original-row/block audit using a small odd-product table.
No remote code is executed. No network, keys or huge binomial integers.
This arithmetic does not import the Gram transport implementation.
"""
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
C = Path(__file__).resolve().parent
start = time.monotonic()
source = C / 'binary_short_moment_certificate.json'
data = json.loads(source.read_text())
b, n = int(data['b']), int(data['n'])
a, N = 2*n, n+2
Af, Ae = data['short_first_numerator'], data['short_exponential_numerator']
assert len(Af) == 82 and len(Ae) == 78
jstar = 1416173266667008
punit = 12
mod = 1 << punit
prefix = [1]*mod
for k in range(1, mod):
    prefix[k] = prefix[k-1]*(k if k & 1 else 1) % mod
assert prefix[-1] == 1

# An entire residue cycle of odd factors has product one modulo 2^12.
def factorial_unit(v):
    result = 1
    while v:
        result = result*prefix[v % mod] % mod
        v >>= 1
    return result

def choose_parts(top, lower):
    if lower < 0 or lower > top:
        return None
    val = lower.bit_count() + (top-lower).bit_count() - top.bit_count()
    unit = factorial_unit(top)*pow(factorial_unit(lower), -1, mod)*pow(factorial_unit(top-lower), -1, mod) % mod
    return val, unit

# Corroborate the bounded odd-factorial/binomial evaluator independently.
from math import comb
small_checks = 0
for top in range(80):
    for lower in range(top+1):
        val, unit = choose_parts(top, lower)
        exact = comb(top, lower)
        assert exact % (1 << val) == 0
        assert (exact >> val) % mod == unit
        small_checks += 1

atom_checks = 0
def coordinate(j, A, order):
    global atom_checks
    wval, wunit = choose_parts(N, j)
    result = 0
    for r, coeff in enumerate(A):
        lower = b-j-r
        part = choose_parts(a+order-1+lower, lower)
        if part is None:
            continue
        val, unit = part
        val += wval
        # Only combined valuations matter. Every relevant atom is >=8,
        # so twelve unit bits suffice for twenty physical coordinate bits.
        assert val >= 8
        atom_checks += 1
        if val < 20:
            result += coeff*wunit*unit*(1 << val)
    return result % (1 << 20)

rows = []
for low in [0, 1]:
    for h in range(8):
        j = jstar ^ (low << 6) ^ ((h & 1) << 38) ^ (((h >> 1) & 1) << 41) ^ (((h >> 2) & 1) << 52)
        assert 0 <= j <= b
        first, second = coordinate(j, Af, 81), coordinate(j, Ae, 77)
        kval, kunit = choose_parts(N, j)
        kval2, kunit2 = choose_parts(a+b-j-1, b-j)
        kval += kval2
        assert kval == 10
        assert first % 512 == 0 and first % 1024 == 512
        assert second % 1024 == 0
        rows.append({'low_toggle': low, 'high_toggle': h, 'j': str(j), 'first_mod2_20': first, 'second_mod2_20': second, 'K_valuation': kval, 'K_odd_unit_mod2_12': kunit*kunit2 % mod})
assert rows[0]['j'] == str(jstar) and rows[0]['first_mod2_20'] % 1024 == 512
alphas = []
for low in [0, 1]:
    octet = [r for r in rows if r['low_toggle'] == low]
    inv = pow(octet[0]['K_odd_unit_mod2_12'], -1, mod)
    weights = [(r['K_odd_unit_mod2_12']*inv % mod)**2 for r in octet]
    sigma = sum(weights) % mod
    assert sigma % 16 == 8
    alpha = sigma//8
    alphas.append(alpha)
assert alphas[0] == alphas[1]
first0 = rows[0]['first_mod2_20']//512
first1 = rows[8]['first_mod2_20']//512
assert (first1-first0) % 2 == 0
z = ((first1-first0)//2) % 256
norm = sum(r['first_mod2_20']**2 for r in rows) % (1 << 30)
assert norm % (1 << 22) == 0
normalized_norm = (norm >> 22) % 256
assert normalized_norm & 1
predicted_norm = alphas[0]*(first0*first0+2*first0*z+2*z*z) % 256
assert normalized_norm == predicted_norm
artifact = {'status':'PASS','scope':'NEW direct physical original jstar coordinate and sixteen-row block with independent small-table odd-factorial arithmetic',
    'b':str(b),'n':str(n),'jstar':str(jstar),'first_witness_mod1024':rows[0]['first_mod2_20']%1024,
    'second_witness_mod1024':rows[0]['second_mod2_20']%1024,'rows':rows,
    'odd_product_table_entries':mod,'independent_small_binomial_checks':small_checks,'atom_checks':atom_checks,
    'normalized_octet_weights_mod512':alphas,'normalized_gram_matrix_mod256':[[alphas[0]%256,alphas[0]%256],[alphas[0]%256,2*alphas[0]%256]],
    'normalized_gram_determinant_odd':True,'block_norm_mod2_30':norm,'block_norm_valuation':22,
    'block_norm_div2_22_mod256':normalized_norm,'predicted_quadratic_value_mod256':predicted_norm,
    'first_physical_content_exact':9,'second_physical_content_lower_bound':10,
    'global_norm_upper_bound_claimed':False,'shared_Gram_transport_imported':False,'all_prime_final_gcd_evaluated':False,
    'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,3)}
out = C/'binary_original_witness_block_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt = {k:v for k,v in artifact.items() if k!='rows'}
receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256'] = hashlib.sha256(out.read_bytes()).hexdigest()
(C/'binary_original_witness_block_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
