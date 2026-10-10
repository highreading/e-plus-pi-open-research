import json
from fractions import Fraction as F
from math import factorial

primes = [5, 7, 11, 13, 17, 19]
fields = ('H', 'K', 'A', 'B', 'C')
polys = [[1], [-2, 4]]
for k in range(2, max(primes) + 1):
    coeff = [0] * (k + 1)
    for j, a in enumerate(polys[k-1]):
        coeff[j] -= 2 * (2*k-1) * a
        coeff[j+1] += 4 * (2*k-1) * a
    for j, a in enumerate(polys[k-2]):
        coeff[j] += 4 * (k-1) * a
    assert all(a % k == 0 for a in coeff)
    polys.append([a // k for a in coeff])
facts = [factorial(j) for j in range(2*max(primes)+1)]
S = []
s = F(0)
for a in facts:
    s += F(1, a)
    S.append(s)
exact = {}
for n in range(max(primes)):
    f = F(facts[n]**2, 2**n)
    def rt(k):
        R = sum((F(a, facts[n+j]) for j, a in enumerate(polys[k])), F(0))
        T = sum((a*S[n+j] for j, a in enumerate(polys[k])), F(0))
        return R, T
    R0, T0 = rt(n)
    R1, T1 = rt(n+1)
    H, A = f*R0, f*T0
    K, B = f*F(n+1, 2)*R1, f*F(n+1, 2)*T1
    exact[n] = dict(zip(fields, (H, K, A, B, K*A-H*B)))
expected = {}
for p in primes:
    for n in range(p):
        vals = {}
        for key, value in exact[n].items():
            assert value.denominator % p != 0, (p, n, key, str(value))
            vals[key] = value.numerator * pow(value.denominator, -1, p) % p
        expected[p, n] = vals
assert len(expected) == 72

base = 'work/session_20260927/'
with open(base+'hp_b1_uniform_prime_independent_certificate.json', encoding='utf-8') as f:
    independent = json.load(f)
seen = set()
diffs = []
for block in independent['seeds']:
    p = block['p']
    for row in block['rows']:
        n = row['r']
        assert (p, n) not in seen
        seen.add((p, n))
        for key in fields:
            actual = row['values'][key]
            if actual != expected[p, n][key]:
                diffs.append([p, n, key, actual, expected[p, n][key]])
    zeros = [n for n in range(p) if expected[p, n]['C'] == 0]
    if block['zero_residues'] != zeros:
        diffs.append(['zero_residues', p, block['zero_residues'], zeros])
assert seen == set(expected)
print(json.dumps({'independent_certificate': {'covered_rows': len(seen), 'compared_scalar_fields': 5*len(seen), 'differences': diffs, 'pass': not diffs}, 'recomputed_C_seeds': {str(p): [expected[p,n]['C'] for n in range(p)] for p in primes}}, ensure_ascii=False))

with open(base+'hp_b1_predeclared_prime_seed_certificate.json', encoding='utf-8') as f:
    predeclared = json.load(f)
coverage = set()
pre_diffs = []
matched_records = [0]
def walk(obj, inherited_p=None, location='$'):
    if isinstance(obj, dict):
        p = obj.get('p', obj.get('prime', inherited_p))
        if isinstance(p, str) and p.isdecimal():
            p = int(p)
        if not isinstance(p, int) or p not in primes:
            p = inherited_p
        n = obj.get('r', obj.get('n', obj.get('residue')))
        vals = obj.get('values', obj)
        if p in primes and isinstance(n, int) and (p,n) in expected and isinstance(vals, dict) and all(k in vals for k in fields):
            matched_records[0] += 1
            coverage.add((p,n))
            for key in fields:
                if vals[key] != expected[p,n][key]:
                    pre_diffs.append([location, p, n, key, vals[key], expected[p,n][key]])
        for key, value in obj.items():
            walk(value, p, location+'.'+str(key))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            walk(value, inherited_p, location+'['+str(i)+']')
walk(predeclared)
def shape(obj, depth=0):
    if depth >= 4:
        return type(obj).__name__
    if isinstance(obj, dict):
        return {str(k): shape(v, depth+1) for k,v in obj.items()}
    if isinstance(obj, list):
        return {'length': len(obj), 'first': shape(obj[0], depth+1) if obj else None}
    return obj
result = {'covered_rows': len(coverage), 'matched_records': matched_records[0], 'differences': pre_diffs, 'complete_comparison_pass': coverage == set(expected) and not pre_diffs}
if coverage != set(expected):
    result['unmatched_rows'] = sorted(set(expected)-coverage)
    result['schema_for_followup'] = shape(predeclared)
print(json.dumps({'predeclared_certificate': result, 'scope': 'Exact finite seed verification only; no infinite residue-class or analytic-tail conclusion is inferred.'}, ensure_ascii=False))