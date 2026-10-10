from pathlib import Path
import hashlib, json, itertools, sys
root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/fixed-size-factorial-determinant-finite-jet-factorization-v1.md'
raw = path.read_bytes()
marker = b'STATUS AND SCOPE\n'
start = raw.index(marker)
payload = raw[start:]
expected = '6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3'
actual = hashlib.sha256(payload).hexdigest()
print(json.dumps({'candidate_bytes': len(raw), 'payload_start': start, 'whole_file_sha256': hashlib.sha256(raw).hexdigest(), 'payload_sha256': actual, 'payload_matches_assignment': actual == expected}))
assert actual == expected, 'Candidate payload does not match the assigned immutable hash'
note = root / 'work/astra_20260929/worker_2/note_000052.md'
note_hash = hashlib.sha256(note.read_bytes()).hexdigest()
print(json.dumps({'note_000052_sha256': note_hash, 'matches_reading_ledger': note_hash == '97a8018d5b0db87b652ee232e109df1674a9f7faa0528c2a2688dd8161081929'}))
sys.path.insert(0, '[private local path removed]')
import sympy as s
from sympy.functions.combinatorial.numbers import stirling

def det_by_permutations(rows):
    d = len(rows)
    total = 0
    for perm in itertools.permutations(range(d)):
        inversions = sum(perm[i] > perm[j] for i in range(d) for j in range(i+1,d))
        total += (-1)**inversions * s.prod(rows[i][perm[i]] for i in range(d))
    return s.expand(total)

results = []
for d in range(1,5):
    xs = s.symbols('x0:'+str(d))
    rows = [[s.ff(x,j+1)-s.ff(x,j) for j in range(d)] for x in xs]
    determinant = s.Poly(det_by_permutations(rows), *xs)
    vand = s.prod(xs[j]-xs[i] for i in range(d) for j in range(i+1,d))
    quotient, remainder = determinant.div(s.Poly(vand,*xs))
    assert remainder.is_zero
    highest = sum(coef*s.prod(x**power for x,power in zip(xs,mon)) for mon,coef in quotient.terms() if sum(mon)==d)
    assert s.expand(highest-s.prod(xs)) == 0
    assert quotient.total_degree() == d
    N = s.Symbol('N')
    translated = s.Poly(s.expand(quotient.as_expr().subs({x:N+x+1 for x in xs}, simultaneous=True)),N)
    assert translated.coeff_monomial(N**d) == 1
    lam = s.Rational(-2,3)
    moment_rows = []
    for x in xs:
        row = []
        for j in range(d):
            moment = sum(s.binomial(j,h)*x**(j-h)*sum(stirling(h,a,kind=2)*lam**a for a in range(h+1)) for h in range(j+1))
            row.append(moment)
        moment_rows.append(row)
    assert s.expand(det_by_permutations(moment_rows)-vand) == 0
    results.append({'d':d, 'vandermonde_division_exact':True, 'quotient_degree':d, 'leading_homogeneous_part_correct':True, 'common_translation_leading_coefficient':1, 'poisson_moment_determinant_correct':True})
print(json.dumps({'independent_symbolic_checks':results, 'scope':'Finite checks of the exact determinant identities; the general proof and uniform tail audit are supplied in the note.'}))