from pathlib import Path
from hashlib import sha256
import json

path = Path('work/astra_review_registry/candidates/w3-b2-residue-one-digit-refinement-v1.md')
data = path.read_bytes()
file_hash = sha256(data).hexdigest()
assert file_hash == 'abf4a96f85c710bbe1dc63be6e6e0b845e9c747784832e8449dac5621876ca25'
start = data.index(b'UNREVIEWED CANDIDATE. Author: worker_3.')
payload = data[start:]
payload_hash = sha256(payload).hexdigest()
assert payload_hash == '67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e'

def digit_sum(n, p):
    total = 0
    while n:
        n, digit = divmod(n, p)
        total += digit
    return total

def factorial_valuation(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total

m_values = set(range(1, 513))
for base in (3, 5):
    for exponent in range(1, 13):
        for shift in (-1, 0, 1):
            m = base**exponent + shift
            if m >= 1:
                m_values.add(m)

forced_bound_checks = 0
for m in sorted(m_values):
    n = 5*m + 1
    s3 = digit_sum(n, 3)
    s5 = digit_sum(n, 5)
    assert s5 == digit_sum(m, 5) + 1
    assert 3**s3 <= 9*n*n
    # Square the five-adic digit bound to avoid floating-point radicals.
    assert 5**(s5 - 1) <= (n - 1)**4
    # Square the product bound; (9*sqrt(5))**2 = 405.
    assert 3**(2*s3) * 5**s5 <= 405*n**4*(n - 1)**4
    v3 = factorial_valuation(n, 3)
    v5 = factorial_valuation(n, 5)
    assert 2*v3 == n - s3
    assert 4*v5 == n - s5
    if n <= 5001:
        eta = int(n % 3 == 1)
        forced_factor = 3**(2*v3 + eta) * 5**(2*v5)
        assert forced_factor**2 * 405*n**4*(n - 1)**4 >= 3**(2*eta)*45**n
        forced_bound_checks += 1

samples = []
for n in (6, 11, 16, 26, 126, 626, 3126):
    samples.append({'n': n, 'eta': int(n % 3 == 1), 's3': digit_sum(n, 3), 's5': digit_sum(n, 5), 'v3_factorial': factorial_valuation(n, 3), 'v5_factorial': factorial_valuation(n, 5)})

print(json.dumps({'file_bytes': len(data), 'file_sha256': file_hash, 'payload_start': start, 'payload_bytes': len(payload), 'payload_sha256': payload_hash, 'digit_cases_passed': len(m_values), 'forced_denominator_bound_cases_passed': forced_bound_checks, 'samples': samples, 'scope': 'Provenance and finite corroboration of digit inequalities only; no endpoint reconstruction or registry approval.'}, indent=2))