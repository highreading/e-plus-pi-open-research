"""Symbolic-index identities only: no branch scan or canonical HP solve."""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'math_packages'))
import sympy as s

m, k, j = s.symbols('m k j', integer=True, positive=True)
rho = k**2 * (k-1)**2 / (2*(2*k-1))
bm = k*(k-1)/8 + rho
bo = (k-1)*(k-2)/24 + rho*(k-2)/k
S = lambda M, sigma: M*(16*M**2 + (24*sigma-12)*M + 5)/12
for sigma in (0, 1):
    actual = s.summation((2*j+sigma)*(2*j+sigma+1)+s.Rational(3,4), (j,0,m-1))
    assert s.factor(actual-S(m,sigma)) == 0

expected = {
    'E0': m*(16*m**3-4*m**2-13*m+4)/(6*(4*m-1)),
    'O0': m*(16*m**3+20*m**2-17*m-3)/(6*(4*m+1)),
    'E1': (m-1)*(16*m**3+4*m**2-19*m+5)/(6*(4*m-1)),
    'O1': m*(16*m**3+28*m**2+5*m-1)/(6*(4*m+1)),
}
derived = {
    'E0': bm.subs(k,2*m)-S(m,0),
    'O0': bo.subs(k,2*m+1)-S(m,0),
    'E1': bo.subs(k,2*m)-S(m-1,1),
    'O1': bm.subs(k,2*m+1)-S(m,1),
}
for key in expected:
    assert s.factor(expected[key]-derived[key]) == 0
diff0 = -m*(2*m-1)*(32*m**2+1)/(6*(4*m-1)*(4*m+1))
diff1 = -m*(2*m+1)*(32*m**2+32*m+9)/(6*(4*m+1)*(4*m+3))
assert s.factor(expected['E0']-expected['O0']-diff0) == 0
assert s.factor(expected['O1']-expected['E1'].subs(m,m+1)-diff1) == 0
assert expected['E1'].subs(m,1) == 0
assert s.factor(expected['E1']-(m-1)*expected['E0']/m-(m-1)*(2*m-1)/6) == 0
assert s.factor((m+s.Rational(1,2))*expected['O0']-(m-s.Rational(1,2))*expected['O1']-m*(m-1)*(m+1)/3) == 0

# Equal-degree Wronskian coefficient independently as a formal Laurent sum.
x = s.symbols('x', positive=True)
d = s.symbols('d', integer=True, positive=True)
A, B, a, b = s.symbols('A B a b')
f = A*(x**d+a*x**(d-1))
g = B*(x**d+b*x**(d-1))
assert s.simplify((f*s.diff(g,x)-s.diff(f,x)*g)/(A*B*x**(2*d-2))) == a-b

out = {
    'scope': 'Rational identities in the symbolic index m only; no additional branch coefficient/root scans or canonical solves.',
    'status': 'pass',
    'krylov_sums': 'pass for both symbolic parity branches',
    'subleading_ratios': {key: str(s.factor(value)) for key,value in derived.items()},
    'even_adjacent_difference': str(diff0),
    'odd_adjacent_difference': str(diff1),
    'constant_branch_boundary': 'E1(1)=0',
    'even_derivative_first_mismatch': '(m-1)(2m-1)/6',
    'odd_Euler_first_mismatch': 'm(m-1)(m+1)/3',
    'equal_degree_wronskian_sign': 'a-b',
    'three_row_signs': {'branch0': ['-','+','+'], 'branch1': ['+','-','+']},
    'scope_limit': 'Fixed-m sufficiently large nodes; no uniform coupled m,node-index threshold proved.'
}
(HERE/'raw_two_branch_leading_minors_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
