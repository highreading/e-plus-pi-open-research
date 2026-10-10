#!/usr/bin/env python3
"""Personally authored new finite audit of compatible second lower symbols.

Also checks the newly disputed low Gram arithmetic, using exact finite sums.
No remote code, credentials, network or original-size arrays.
"""
from math import factorial, prod
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
ROOT = Path(__file__).resolve().parent
p, modulus = 29, 29**3
n = p * (7 + 24 * p)
inv2 = pow(2, -1, modulus)
a = [2, 1]
for s in range(2, 121):
    a.append((a[-1] - inv2 * a[-2]) % modulus)
c = [1, n % modulus]
for s in range(1, 120):
    c.append(((s + n) * c[s] - s * (n + (s - 1) * inv2) * c[s - 1]) % modulus)
direct, predicted, literal_direct, literal_predicted = [], [], [], []
for s in range(1, 121):
    first = (7 * factorial(s - 1) * a[s]) % modulus if s < 29 else (-7 if s == 29 else 0)
    residual = (c[s] - p * first) % modulus
    assert residual % (p * p) == 0
    ds = residual // (p * p)
    if s < 29:
        qs = factorial(s - 1) * a[s] % p
        convolution = sum(a[r] * a[s-r] * pow(r * (s-r), -1, p) for r in range(1, s)) % p
        expect = (24 * qs + 49 * pow(2, -1, p) * factorial(s) * convolution) % p
    elif s == 29:
        expect = 4
    elif s <= 58:
        r = s - 29
        expect = factorial(r - 1) * (7 * pow(21, r, p) + 4 * pow(9, r, p)) % p
    else:
        expect = 0
    assert ds == expect, (s, ds, expect)
    direct.append(ds); predicted.append(expect)
    literal = (7 * factorial(s-1) * (21**s + 9**s)) if s < 29 else (-7 if s == 29 else 0)
    residual_old = (c[s] - p * literal) % modulus
    assert residual_old % (p*p) == 0
    old = residual_old // (p*p)
    old_expect = (expect - 7 * factorial(s) * pow(9, s-1, p)) % p if s < 29 else expect
    assert old == old_expect
    literal_direct.append(old); literal_predicted.append(old_expect)
products = [prod(range(k+1, k+8)) % p for k in range(8)]
squares = [x*x % p for x in products]
low_sum = sum(squares) % p
k34 = (factorial(7) * pow(factorial(15), -1, p))**2 * (7*7-3*3) * low_sum % p
li, lii = 27*k34*10 % p, 27*k34*19 % p
assert (low_sum, k34, li, lii) == (9, 12, 21, 8)
artifact = {
    'status': 'PASS', 'scope': 'NEW finite compatible second-lower recurrence audit and disputed low coefficient correction only',
    'prime': p, 'n_residue_mod_p3': n, 'symbol_checks': 120, 'literal_lift_checks': 120,
    'second_symbols_s1_to120': direct, 'literal_second_symbols_s1_to120': literal_direct,
    'low_products': products, 'low_squares': squares, 'low_sum_mod29': low_sum,
    'K34_mod29': k34, 'L_I_L_II_mod29': [li, lii],
    'complete_next_column_evaluated': False, 'next_norm_evaluated': False, 'irrationality_proved': False,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
target = ROOT / 'lower29_second_lift_certificate.json'
target.write_text(json.dumps(artifact, indent=2) + '\n')
receipt = {k:v for k,v in artifact.items() if 's1_to120' not in k}
receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
(ROOT / 'lower29_second_lift_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
