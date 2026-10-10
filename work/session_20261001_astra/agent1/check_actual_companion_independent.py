"""Independent retained-data audit and formal companion controls.
No author program execution, canonical system, new index, or prime scan.
"""
import json
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
ROOT = Path('work/session_20261001_astra/agent2')
names = ['ACTUAL_COMPANION_CONDITIONING.md',
         'ACTUAL_COMPANION_CONDITIONING_REPORT.md',
         'extract_companion_conditioning.py',
         'companion_conditioning_extraction.json',
         'conditioning_monotonicity_witness.json',
         'two_scalar_quotient_evidence.json',
         'TWO_SCALAR_DETERMINANT_QUOTIENT.md']
protected = {name:(ROOT/name).read_bytes() for name in names}
source = json.loads(protected['two_scalar_quotient_evidence.json'])
extraction = json.loads(protected['companion_conditioning_extraction.json'])
witness = json.loads(protected['conditioning_monotonicity_witness.json'])
assert extraction['source_sha256'] == sha256(protected['two_scalar_quotient_evidence.json']).hexdigest()
assert extraction['script_sha256'] == sha256(protected['extract_companion_conditioning.py']).hexdigest()
assert extraction['source_unchanged_during_execution'] is True
assert [r['n'] for r in source['records']] == [4,6,8,10]
assert [r['n'] for r in extraction['records']] == [4,6,8,10]

def ratio(a,b):
    return str(Q(a,b)) if b else None

summaries = []
matrices = {}
row_count = 0
for old, saved in zip(source['records'], extraction['records']):
    n,b = old['n'],old['b']
    size = b+1
    assert saved['n'] == n and saved['b'] == b and b == n//2
    # Accumulate column sums and signed masses directly from sparse edges.
    N = [[0]*size for _ in range(size)]
    kap = [0]*size
    pos = [0]*size
    neg = [0]*size
    expected_keys = {f'{i},{j}' for i in range(size) for j in range(i+1,size)}
    assert set(old['primitive_high_minors']) == expected_keys
    content = 0
    for key,value in old['primitive_high_minors'].items():
        i,j = map(int,key.split(','))
        a = Q(value)
        assert a.denominator == 1
        a = a.numerator
        content = gcd(content,abs(a))
        N[i][j],N[j][i] = a,-a
        kap[i] -= a
        kap[j] += a
        if a >= 0:
            pos[i] += a
            neg[j] += a
        else:
            neg[i] -= a
            pos[j] -= a
    assert content == 1
    assert saved['primitive_antisymmetric_matrix'] == [[str(x) for x in row] for row in N]
    assert sum(kap) == 0
    assert len(saved['rows']) == size
    eligible = []
    for j,entry in enumerate(saved['rows']):
        total = pos[j]+neg[j]
        net = pos[j]-neg[j]
        lost = total-abs(net)
        assert net == -kap[j] and lost == 2*min(pos[j],neg[j])
        fields = {
            'j':j, 'kappa_j':str(kap[j]), 'row_signed_sum':str(net),
            'row_absolute_sum':str(total), 'positive_mass':str(pos[j]),
            'negative_mass':str(neg[j]), 'cancelled_mass':str(lost),
            'eligible':kap[j] != 0,
            'eligible_denominator_abs_kappa':str(abs(kap[j])) if kap[j] else None,
            'eligible_ratio':ratio(total,abs(kap[j])),
            'surviving_fraction':ratio(abs(net),total),
            'cancelled_fraction':ratio(lost,total),
            'cancelled_mass_over_net':ratio(lost,abs(net)),
            'minority_over_majority':ratio(min(pos[j],neg[j]),max(pos[j],neg[j]))
        }
        assert entry == fields, (n,j,'row-field mismatch')
        if kap[j]:
            eligible.append((Q(total,abs(kap[j])),j))
        row_count += 1
    C = min(v for v,j in eligible)
    minimizers = [j for v,j in eligible if v == C]
    assert saved['C_min'] == str(C)
    assert saved['minimizing_rows'] == minimizers
    assert saved['eligible_rows'] == [j for v,j in eligible]
    assert len(eligible) == size and 1 < C < 2
    P = abs(N[1][0])
    H = sum(abs(a) for a in N[1][2:])
    margin = P-H
    dominance = saved['row_one_first_entry_dominance']
    assert dominance['pivot_column'] == 0
    for key,value in [('pivot_absolute_value',P),('remaining_absolute_mass',H),('dominance_margin',margin)]:
        assert dominance[key] == str(value)
    assert dominance['strict_dominance'] == (margin > 0)
    assert dominance['remaining_over_pivot'] == ratio(H,P)
    assert dominance['triangle_condition_bound'] == ratio(P+H,margin)
    assert margin > 0 and Q(saved['rows'][1]['eligible_ratio']) <= Q(P+H,margin)
    A0,A1 = Q(old['A0']),Q(old['A1'])
    Z0,Z1 = Q(old['primitive_contractions']['Z0']),Q(old['primitive_contractions']['Z1'])
    d,K = Q(old['primitive_contractions']['d']),Q(old['primitive_contractions']['K'])
    assert A0 > 0 and A1 > 0 and d == A1*Z1-A0*Z0 and d != 0
    Delta = abs(d)/(A0*abs(Z0)+A1*abs(Z1))
    assert Delta == Q(old['projective_pole_separation']) == Q(saved['projective_separation_Delta']) == 1
    assert saved['preserved_companion_data'] == {
        'Z0':str(Z0),'Z1':str(Z1),'d':str(d),'K_tail':str(K),
        'rational_e_companion':old['rational_e_companion']}
    assert -K/d == Q(old['rational_e_companion'])
    assert saved['actual_reduced_p'] == str(old['p'])
    assert saved['actual_reduced_q'] == str(old['q'])
    assert old['q'] > 0 and gcd(abs(old['p']),old['q']) == 1
    # Consistency of retained endpoint coordinates, not a new quotient audit.
    assert Q(old['p'],old['q']) == -Q(old['rational_pi_companion'])-Q(old['rational_e_companion'])
    summaries.append({'n':n,'b':b,'rows_verified':size,'C':str(C),
                      'minimizers':minimizers,'row_one_margin':str(margin),
                      'row_one_triangle_bound':ratio(P+H,margin),
                      'actual_q_preserved':str(old['q']),'Delta':str(Delta)})
    matrices[n] = N

assert row_count == 18
assert extraction['all_four_row_one_dominance_tests_pass'] is True
assert witness == extraction['first_rejected_monotonicity_witness']
assert (witness['n'],witness['b'],witness['row'],witness['left_column'],witness['right_column']) == (4,2,0,1,2)
N4 = matrices[4]
left,right = N4[0][1],N4[0][2]
assert (left,right) == (-1510,1515)
assert witness['left_entry'] == str(left) and witness['right_entry'] == str(right)
assert witness['absolute_increase'] == str(abs(right)-abs(left)) == '5'
assert abs(right) > abs(left)

# Universal alternating algebra in the span of evec, tau_U, tau_P.
# This is an abstract basis, not an HP degree specialization.
A0,A1,Z0,Z1,K,ep = s.symbols('A0 A1 Z0 Z1 K ep')
NN = s.Matrix([[0,-Z0,-Z1],[Z0,0,K],[Z1,-K,0]])
evec,tU,tP = [s.eye(3)[:,j] for j in range(3)]
beta = A0*tU-A1*tP
dd = A1*Z1-A0*Z0
arow = ep*A1*evec-tU
crow = ep*A0*evec-tP
formal = {
 'normalization_e_N_beta':s.expand((evec.T*NN*beta)[0]-dd) == 0,
 'beta_full_tail_identity':beta == A1*crow-A0*arow,
 'full_tail_alternating_sign':s.expand((arow.T*NN*crow)[0]-(ep*dd+K)) == 0,
 'normalized_tail_contraction':s.expand((arow.T*NN*beta)[0]-A1*(ep*dd+K)) == 0
}
k,l,j,b = s.symbols('k l j b', integer=True)
formal['essential_derivative_index'] = s.expand(k+l-(j+1)-((k-1)+l-j)) == 0
formal['degree_after_two_factors'] = s.expand(2*k-(k-b)-1-((k-1)+b)) == 0
r = s.symbols('r', integer=True, nonnegative=True)
formal['beta_integral_constant'] = s.cancel(1/(r+1)-1/(r+2)-1/((r+1)*(r+2))) == 0
x = s.symbols('x', real=True)
S = s.Function('S')(x)
formal['integration_by_parts_sign'] = s.simplify(s.diff(s.exp(-x)*S,x)-s.exp(-x)*(s.diff(S,x)-S)) == 0
assert all(formal.values()),formal
for name,original in protected.items():
    assert (ROOT/name).read_bytes() == original, ('input changed',name)
result = {
 'status':'PASS_INDEPENDENT_COMPANION_CONTROLS',
 'scope':'All fields of 18 rows in the four existing extractions; saved counterexample only; eight formal companion controls. No author program executed, canonical system solved, new index evaluated, or prime scanned.',
 'records':summaries,'monotonicity_witness_verified':witness,
 'formal_controls':formal,
 'inputs_unchanged':True,
 'input_sha256':{name:sha256(data).hexdigest() for name,data in protected.items()},
 'checker_sha256':sha256((BASE/'check_actual_companion_independent.py').read_bytes()).hexdigest(),
 'limits':'The unrestricted kernel, Rodrigues, divisibility, integral and norm statements require the written proofs. No uniform bound on C, lambda or G_lambda is inferred from retained records.'
}
out = BASE/'actual_companion_independent_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
assert json.loads(out.read_text()) == result
print(json.dumps({'status':result['status'],'row_count':row_count,'formal_control_count':len(formal),'records':summaries,'inputs_unchanged':True},indent=2))
