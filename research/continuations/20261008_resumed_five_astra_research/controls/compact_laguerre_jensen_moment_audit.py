"""NEW order2/4 moment correction; reuse previously checked reference D."""
from pathlib import Path
from math import factorial, prod
from itertools import permutations
import datetime
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
R = HERE.parent
k,m = sp.symbols('k m',positive=True,integer=True)


def cycles(permutation):
    seen = set()
    count = 0
    for i in range(len(permutation)):
        if i in seen:
            continue
        count += 1
        q = i
        while q not in seen:
            seen.add(q)
            q = permutation[q]
    return count


def wick_trace_moment(gamma):
    return sp.expand(sum(m**cycles(sigma)*k**cycles(tuple(gamma[sigma[i]] for i in range(len(gamma))))
                         for sigma in permutations(range(len(gamma)))))


T2 = wick_trace_moment((1,0))
T11 = wick_trace_moment((0,1))
T4 = wick_trace_moment((1,2,3,0))
T22 = wick_trace_moment((1,0,3,2))
EA = sp.factor(k*T2-T11)
EB = sp.factor(k*T4-T22)
expected_A = k*m*(k*k-1)
expected_B = k*m*(k*k-1)*(k*k+5*k*m+4*m*m+2)
assert sp.expand(EA-expected_A) == 0
assert sp.expand(EB-expected_B) == 0
assert sp.expand(T4-k*m*(k**3+6*k*k*m+6*k*m*m+m**3+5*k+5*m)) == 0
assert sp.expand(T22-k*m*(k*m*(k+m)**2+4*k*k+10*k*m+4*m*m+2)) == 0


def laguerre_integral(polynomial,variables,alpha):
    return sum(coefficient*prod(factorial(alpha+power) for power in powers)
               for powers,coefficient in sp.Poly(sp.expand(polynomial),*variables).terms())


rows = []
for n in range(2,5):
    alpha = 3*n-1
    dimension = 4*n-1
    z = sp.symbols(f'z0:{n}')
    vandermonde_squared = prod((z[j]-z[i])**2 for i in range(n) for j in range(i+1,n))
    normalizer = factorial(n)*prod(factorial(j)*factorial(alpha+j) for j in range(n))
    direct_normalizer = laguerre_integral(vandermonde_squared,z,alpha)
    assert direct_normalizer == normalizer
    A = n*sum(q*q for q in z)-sum(z)**2
    B = n*sum(q**4 for q in z)-sum(q*q for q in z)**2
    direct_A = sp.Rational(laguerre_integral(vandermonde_squared*A,z,alpha),normalizer)
    direct_B = sp.Rational(laguerre_integral(vandermonde_squared*B,z,alpha),normalizer)
    assert direct_A == EA.subs({k:n,m:dimension})
    assert direct_B == EB.subs({k:n,m:dimension})
    rows.append({'k':n,'m':dimension,'alpha':alpha,'direct_E_A':str(direct_A),
                 'direct_E_B':str(direct_B),'direct_to_Wick_agrees':True})

gain = sp.factor(expected_A.subs(m,4*k-1)**2/expected_B.subs(m,4*k-1))
expected_gain = k*(4*k-1)*(k*k-1)/(85*k*k-37*k+6)
assert sp.simplify(gain-expected_gain) == 0
assert sp.limit(gain/(k*k),k,sp.oo) == sp.Rational(4,85)
C_old = 15*sp.log(2)-sp.Rational(9,2)*sp.log(3)
C_new = C_old+sp.Rational(4,85)
A_critical = (C_new-6+4*sp.log(2))/sp.log(2)

sources = [R/'gates/COMPACT_LAGUERRE_JENSEN_REFINEMENT_GATE_20261009.md',
           HERE/'COORDINATOR_COMPACT_REFERENCE_GRAM_LOWER_BOUND_CANDIDATE.md',
           HERE/'compact_reference_gram_constant_certificate.json']
out = {'status':'PASS','time':datetime.datetime.now().astimezone().isoformat(),
       'scope':'NEW auxiliary Laguerre order2/4 moments; no actual primitive content or original-index computation.',
       'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'Wick_permutations_enumerated_order2':2,'Wick_permutations_enumerated_order4':24,
       'T2':str(T2),'T11':str(T11),'T4':str(T4),'T22':str(T22),
       'E_A':str(EA),'E_B':str(EB),'independent_direct_integral_checks':rows,
       'finite_positive_gain_k_ge2':str(expected_gain),
       'limiting_gain':str(sp.Rational(4,85)),
       'candidate_new_C_H':str(C_new),'new_C_H_decimal_display':str(C_new.evalf(30)),
       'conditional_binary_upper_threshold':str(A_critical),
       'threshold_decimal_display':str(A_critical.evalf(30)),
       'complete_same_H_reference_comparison_external_audit_pending':True,
       'new_Jensen_refinement_external_audit_pending':True,'global_proof':False}
(HERE/'compact_laguerre_jensen_moment_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','new_direct_integrals':len(rows),
                  'E_A':str(EA),'E_B':str(EB),'finite_gain':str(gain),
                  'candidate_C_H':str(C_new.evalf(18)),
                  'conditional_binary_threshold':str(A_critical.evalf(18)),'global_proof':False}))
