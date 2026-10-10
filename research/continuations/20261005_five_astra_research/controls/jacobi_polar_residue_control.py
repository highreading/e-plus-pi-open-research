"""Coordinator-authored finite rational certificate, not a moving-degree theorem."""
import hashlib
import json
import resource
from fractions import Fraction as Q
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
ROOT = Path(__file__).resolve().parent

def val_int(a):
    if not a:
        return None
    v = 0
    while a % 3 == 0:
        a //= 3
        v += 1
    return v

def val(q):
    return None if not q else val_int(q.numerator) - val_int(q.denominator)

def mod(q, depth):
    if val_int(q.denominator) != 0:
        raise ArithmeticError('Nonintegral residue')
    modulus = 3**depth
    return q.numerator * pow(q.denominator, -1, modulus) % modulus

records = []
for b in range(3):
    astar = Q(243, 4)
    sstar = Q(247 + 8*b, 8)
    pole = 122 + 2*b
    start = pole + 1
    choose = Q(1)
    numerator = Q(1)
    denominator = Q(1)
    for i in range(start):
        choose *= (sstar - i) / (i + 1)
        numerator *= astar + 2*b - 2*i
        if i != pole:
            denominator *= 2*(pole - i)
    term = (-1)**start * choose * Q(12, 527)**start * numerator / denominator
    initial = term
    total = Q(0)
    terms = []
    for u in range(start, 281):
        terms.append({'u': u, 'valuation': val(term)})
        total += term
        term *= -(sstar-u)/(u+1) * (astar+2*b-2*u)/(2*(pole-u)) * Q(12, 527)
    v = val(total)
    if v is not None and v < 0:
        raise ArithmeticError('Negative valuation in finite residue sum')
    records.append({'b': b, 'start': start, 'stop': 280,
                    'initial_valuation': val(initial),
                    'finite_sum_valuation': v,
                    'first_nonzero_unit_mod27': mod(total/Q(3)**v, 3) if v is not None else None,
                    'finite_sum_mod3pow143': str(mod(total,143)),
                    'next_term_valuation': val(term),
                    'exact_sum_sha256': hashlib.sha256(str(total).encode()).hexdigest(),
                    'term_valuations': terms})
assert [r['initial_valuation'] for r in records] == [133,136,134]
report = {'scope': 'Exact fixed rational sums at A=243/4 for b=0,1,2; no original-index transfer.',
          'tail_dependency': 'A1 turn29 inequality (8) bounds every term u>=281 at depth>=143.',
          'status': 'PASS', 'records': records}
(ROOT/'jacobi_polar_residue_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','records':[{k:r[k] for k in ('b','initial_valuation','finite_sum_valuation','first_nonzero_unit_mod27','next_term_valuation')} for r in records]}))
