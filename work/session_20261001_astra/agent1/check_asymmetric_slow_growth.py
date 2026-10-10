"""Necessary symbolic controls for the asymmetric slow-growth derivation.
No HP degree evaluations, prime computations, or previous audit reruns.
"""
import json
from hashlib import sha256
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
protected_names = [
    'check_actual_companion_independent.py',
    'actual_companion_independent_checks.json',
    'actual_companion_independent_stdout.txt',
    'asymmetric_formal_evidence.json',
]
protected = {name: (BASE/name).read_bytes() for name in protected_names}
checks = {}

def verify(name, value):
    checks[name] = bool(value)
    assert checks[name], name

n = s.symbols('n', integer=True, positive=True)
b = s.symbols('b', integer=True, positive=True)
r,i,j = s.symbols('r i j', integer=True, nonnegative=True)
a,c = 2*n,n
M = a+b+c
verify('high_moment_weight_index', s.expand(a+r+1-(c-i)-1-(n+r+i)) == 0)
verify('contact_M_high_row_count', s.expand(M-a-1-(n+b-1)) == 0)
verify('contact_M_kernel_dimension_lower_bound', s.expand((b+1)+(n+1)-(n+b-1)-1) == 2)
verify('contact_M_plus_one_kernel_dimension_lower_bound', s.expand((b+1)+(n+1)-(n+b)-1) == 1)
verify('projected_high_constraint_count_for_b_ge_2', s.expand((n+b-1)-(n+1)) == b-2)
verify('complete_logarithmic_tail_exponent', s.expand(n+(M-a-1)-(2*n+b-1)) == 0)

# Coefficients of (1-z+z^2/2) F'(z)=2.
# D_m denotes F^(m)(0); the recurrence has integer coefficients.
m = s.symbols('m', integer=True, positive=True)
Dprev,Dcur,Dnext = s.symbols('Dprev Dcur Dnext')
coefficient_equation = Dnext-m*Dcur+m*(m-1)*Dprev/2
recurrence_rhs = m*Dcur-s.binomial(m,2)*Dprev
verify('integer_F_derivative_recurrence', s.simplify(coefficient_equation.subs(Dnext,recurrence_rhs)) == 0)

# Exact endpoint bookkeeping before any projection or normalization.
e,pi,YB,YC,Ebeta,Sgamma = s.symbols('e pi YB YC Ebeta Sgamma')
X = -Ebeta-Sgamma
complete_tail = e*YB-Ebeta+pi*YC-Sgamma
verify('endpoint_matching_preserves_e_plus_pi', s.expand(complete_tail-(X+(e+pi)*YB)-pi*(YC-YB)) == 0)

# Weighted CD formulas: the rational shift sigma_n is indispensable.
A,B,wp,wu,TP,TU,shift = s.symbols('A B wp wu TP TU shift')
h = A*wu-B*wp
u = (A*TU-B*TP)/h
x = (wp*TU-wu*TP)/h+shift*u
T_D = (wu*TP-wp*TU)/h
w = e-T_D-(pi-shift)*u
verify('weighted_CD_rational_endpoint_shift', s.cancel(w-(e+x-pi*u)) == 0)
Y = -u
verify('matched_CD_quotient_shift', s.cancel(x/Y+shift-(wp*TU-wu*TP)/(B*TP-A*TU)) == 0)
verify('weighted_Wronskian_endpoint_normalization', s.cancel((wu*A-wp*B)/h-1) == 0)

# Any rational selector row can be represented by factorial functionals
# of a polynomial. This abstract four-column control supplements the
# all-size Vandermonde proof; it is not an HP index calculation.
k0 = s.symbols('k0')
Vand = s.Matrix([[s.prod(k0+col-hh for hh in range(row))
                  for col in range(4)] for row in range(4)])
verify('selector_factorial_Vandermonde_control', s.expand(Vand.det()) == 12)

# All dimension factors in the elementary inverse estimate remain visible.
idx = s.symbols('idx', integer=True, nonnegative=True)
verify('weighted_Gram_dyadic_determinant_scale', s.simplify(n*(n+1)+2*s.summation(idx,(idx,0,n))-2*n*(n+1)) == 0)
radius = s.sqrt(2)/2
ratio = (2*n)**(b-1)*radius**(2*n+b-1)/(2**(-n)*(s.sqrt(2)*n)**(b-1))
verify('post_clearing_logarithmic_tail_budget', s.simplify(s.powsimp(ratio,force=True)-1) == 0)

# The actual reduced endpoint normalization, including its final gcd.
Delta,g,X0,Y0,R0 = s.symbols('Delta g X0 Y0 R0', positive=True)
verify('primitive_error_scaling_positive_endpoint', s.cancel((Delta*Y0/g)*R0/Y0-Delta*R0/g) == 0)

for name,data in protected.items():
    assert (BASE/name).read_bytes() == data, ('protected artifact changed',name)
result = {
    'status':'PASS_ASYMMETRIC_SYMBOLIC_CONTROLS',
    'scope':'Formal indexing, endpoint normalization, derivative recurrence, an abstract selector determinant, and error-budget factors. No numerical HP indices or prime scans.',
    'checks':checks,
    'check_count':len(checks),
    'protected_artifacts_unchanged':{name:sha256(data).hexdigest() for name,data in protected.items()},
    'checker_sha256':sha256((BASE/'check_asymmetric_slow_growth.py').read_bytes()).hexdigest(),
    'not_established':['Weighted Gram nonsingularity','Reduced-system endpoint rank','Uniform inverse conditioning of exponential size','A favorable actual endpoint gcd or reduced denominator','Nonzero shrinking primitive forms'],
    'proof_scope':'The unrestricted moment reduction and uniform inequalities require the accompanying written proofs. Symbolic checks do not establish the listed open properties.'
}
out = BASE/'asymmetric_slow_growth_checks.json'
assert not out.exists(), 'Preserve any existing certificate and inspect it before proceeding.'
out.write_text(json.dumps(result,indent=2)+'\n')
assert json.loads(out.read_text()) == result
print(json.dumps(result,indent=2))
