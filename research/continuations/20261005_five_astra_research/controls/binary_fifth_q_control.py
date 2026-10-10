"""Coordinator-authored bounded fifth-Q polynomial and boundary checks.

No returned code is executed. Every operation is elementary exact integer
algebra at a fixed reference size. Infinite parameter transfer is separate.
"""
import json
import math
import resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
OUT = Path(__file__).resolve().parent
BREF = 81
MOD = 128
CS = (-1, 2, -3, 3)

def choose(x, k):
    if k < 0:
        return 0
    if x >= 0:
        return math.comb(x, k) if k <= x else 0
    return (-1)**k * math.comb(k-x-1, k)

def entry(n, i, j):
    return sum(CS[s-1] * sum(choose(i, s-t) * choose(n, t)
               * choose(-t, j-i+s-t) for t in range(s+1))
               for s in range(1, 5))

def newton(values, modulus):
    values = [v % modulus for v in values]
    result = []
    while values:
        result.append(values[0])
        values = [(values[i+1]-values[i]) % modulus
                  for i in range(len(values)-1)]
    return result

eref = [[entry(2, i, j) % MOD for j in range(BREF)]
        for i in range(BREF)]
initial = (10, 2, 24, 15)
term = [(-1)**i * sum(v*choose(i, k) for k, v in enumerate(initial)) % MOD
        for i in range(BREF)]
result = [0]*BREF
for depth in range(6):
    result = [(r + 2*(-2)**depth*t) % MOD for r, t in zip(result, term)]
    term = [sum(a*t for a, t in zip(row, term)) % MOD for row in eref]
qvalues = [((-1)**i*r + 64*(1+choose(i, 7))) % MOD
           for i, r in enumerate(result)]
qcoeff = newton(qvalues, MOD)
assert not any(qcoeff[24:])
old = json.loads((OUT/'binary_fourth_lift_control.json').read_text())
oldq = old['Q_newton_mod64']
assert [c % 64 for c in qcoeff[:len(oldq)]] == oldq
assert not any(c % 64 for c in qcoeff[len(oldq):])

factorials = [1]
for s in range(1, 7):
    factorials.append(factorials[-1]*(BREF+s) % MOD)
assert factorials == [1,82,22,56,24,16,112]
# n=322 has C=2, the required low residue; this is a bounded reference.
boundary = [sum(factorials[t]*choose(644, t-s) for t in range(s, 7)) % MOD
            for s in range(7)]
assert boundary == [69,106,54,56,120,80,112]
aref = [(-1)**i*sum(entry(322, i, BREF+s)*boundary[s]
                   for s in range(7)) % 64 for i in range(BREF)]
acoeff = newton(aref, 64)
assert acoeff[:4] == [42,2,24,47]
assert not any(acoeff[4:])

tvalues = [sum(choose(k-i+3, 3)*choose(k, 3)
               for k in range(i, BREF)) for i in range(BREF)]
tc = newton([(t-choose(i, 7)) % 2 for i, t in enumerate(tvalues)], 2)
assert not any(tc)

p = old['P_newton_mod32']
def j32(x):
    return sum(c*choose(s+3, 3)*choose(x+4, s+4)
               for s, c in enumerate(p))
degree = max(s+4 for s, c in enumerate(p) if c)
jcert = newton([(j32(8*s)-2-20*s) % 32
                for s in range(degree+1)], 32)
assert not any(jcert)

report = {
 'reference_n': 2, 'reference_b': BREF, 'boundary_reference_n': 322,
 'Q_newton_mod128': qcoeff[:24], 'Q_degree_bound': 23,
 'Q_reduction_mod64_pass': True,
 'factorial_residues_mod128': factorials, 'boundary_values_mod128': boundary,
 'a64_newton': acoeff[:4], 'a64_higher_coefficients_zero': True,
 'Newton_certificate_T_choose3_minus_choose7_mod2': tc[:8],
 'J32_composition_degree_bound': degree,
 'Newton_certificate_J32_8s_minus2_minus20s_mod32': jcert,
 'finite_reference_operations_pass': True,
 'polynomial_coefficient_identity_certificates_only': True,
 'infinite_parameter_transfer_not_checked': True,
 'actual_fifth_mixed_discrepancy_not_evaluated': True,
}
(OUT/'binary_fifth_q_control.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
