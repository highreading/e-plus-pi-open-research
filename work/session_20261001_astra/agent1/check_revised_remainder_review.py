"""Independent symbolic and exact-constant controls. No HP indices or prime scans."""
import json
from hashlib import sha256
from pathlib import Path
import sympy as sp

BASE = Path('work/session_20261001_astra/agent1')
ROOT = Path('work/session_20261001_astra')
checks = {}
def verify(name, condition):
    checks[name] = bool(condition)
    assert checks[name], name

t,z = sp.symbols('t z')
verify('CD_subtraction_sign', sp.cancel(1/(1-t)-1/(1-z)-(t-z)/((1-t)*(1-z))) == 0)
U,p,A,B,h,v,vnext = sp.symbols('U p A B h v vnext', nonzero=True)
verify('W_reference_factor', sp.cancel((v*U-vnext*p)/(h*(1-t))/U-(v/h)*(1-(vnext/v)*(p/U))/(1-t)) == 0)
verify('V_reference_minus_sign', sp.cancel((U*A-p*B)/(h*(t-1))/U+(A/h)*(1-(B/A)*(p/U))/(1-t)) == 0)
k = sp.symbols('k', integer=True, nonnegative=True)
I,C = sp.symbols('I C', positive=True)
hnorm = 2*(-1)**k/((2*k+1)*C**2)
Av = 2*(-1)**k*I/C**2
verify('Legendre_square_theta_scalar', sp.cancel(Av/hnorm-(2*k+1)*I) == 0)
theta,AA,hh = sp.symbols('theta AA hh', positive=True)
verify('mu_over_nu', sp.cancel((theta/AA)/(AA/hh)-theta*hh/AA**2) == 0)

rat = sp.Rational
adj = rat(11,20)+rat(1,12)/rat(9,20)
cW,cV = rat(740,513),rat(1340,513)
verify('adjacent_ratio_397_over_540', adj == rat(397,540))
verify('strict_high_row_improvement', adj < rat(3,4))
verify('high_row_product_ratio', adj/rat(3,4) == rat(397,405))
verify('endpoint_b_upper', rat(1,2)+rat(1,12)/rat(1,2) == rat(2,3))
verify('alpha_upper_from_recurrence', rat(1,12)/rat(1,2) == rat(1,6))
verify('FW_lower', (1-rat(1,6)*rat(20,9))/rat(21,20) == rat(340,567))
verify('FW_upper', (1+rat(1,6)*rat(20,9))/rat(19,20) == cW)
verify('FV_lower', 1/rat(21,20) == rat(20,21))
verify('FV_upper', (1+rat(2,3)*rat(20,9))/rat(19,20) == cV)
verify('special_majorant_ratio', cW/cV == rat(37,67))
c,bb,x,y = sp.symbols('c bb x y', real=True)
comparison = (1+c*x)**2+(c*y)**2-((1-bb*x)**2+(bb*y)**2)
verify('direct_reference_comparison_identity', sp.expand(comparison-2*(c+bb)*x-(c*c-bb*bb)*(x*x+y*y)) == 0)
verify('direct_reference_lower', rat(17,27)/rat(67,27) == rat(17,67))
verify('reference_zero_ratio_lower', (1-rat(1,6)/rat(1,2))/2 == rat(1,3))

ss = (sp.sqrt(2)-1)**2
aa = (1+sp.sqrt(2))/4
verify('scalar_characteristic_identity', sp.simplify(16*aa**2*ss-1) == 0)
verify('scalar_convex_weights', sp.simplify(1/(2*aa)+ss-1) == 0)
verify('scalar_lower_initial_value', sp.simplify(aa*(1-ss)-rat(1,2)) == 0)
verify('s_less_than_one_fifth', ss < rat(1,5))
verify('a_less_than_five_eighths', aa < rat(5,8))
n = sp.symbols('n', positive=True)
verify('central_binomial_upper_induction', sp.expand(4*(n+1)**2*(3*n+1)-(2*n+1)**2*(3*n+4)-n) == 0)
verify('central_binomial_lower_induction', sp.expand((2*n+1)**2-4*n*(n+1)-1) == 0)
verify('norm_lower_margin', sp.cancel(2*(3*n+1)/(2*n+1)-2-2*n/(2*n+1)) == 0)
verify('norm_upper_margin', sp.cancel(4-8*n/(2*n+1)-4/(2*n+1)) == 0)

# Check Gaussian normalization and all factors in the companion ratio.
d = sp.symbols('d', integer=True, positive=True)
ga = sp.symbols('ga', positive=True)
S = d*(d-1)/2
old_gaussian_prefactor = (sp.pi/ga)**(d/2)*(2*ga)**(-S)/(2*sp.pi)**d
new_gaussian_prefactor = (2*sp.pi)**(-d/2)*(2*ga)**(-d*d/2)
verify('Gaussian_normalization', sp.simplify(old_gaussian_prefactor/new_gaussian_prefactor-1) == 0)
b = sp.symbols('b', integer=True, positive=True)
rho,gap,Qrad = sp.symbols('rho gap Qrad', positive=True)
Cd = lambda j: j**(sp.Rational(1,2)*j)*rho**(-j*(j-1)/2)*gap**(-j*(j+1)/2)
Cr = ((b+1)**((b+1)/2)/b**(b/2))*rho**(-b)*gap**(-(b+1))
verify('companion_C_ratio', sp.simplify(Cd(b+1)/Cd(b)/Cr-1) == 0)
Jratio = (2*sp.pi)**(-rat(1,2))*Qrad**(-((b+1)**2-b**2)/2)*sp.factorial(b+1)
combined = Jratio*sp.factorial(b)/sp.factorial(b+1)
expected = sp.factorial(b)/(sp.sqrt(2*sp.pi)*Qrad**(b+rat(1,2)))
verify('companion_Gaussian_and_outside_factorials', sp.simplify(combined/expected-1) == 0)
E,R = sp.symbols('E R', positive=True)
verify('companion_contour_factor', sp.simplify((E/(R+1))**(b+1)/E**b-E/(R+1)**(b+1)) == 0)

# Uniform n>=40 controls, with no sampled n or factorial evaluation.
verify('disk_gap_exponent_21', sp.cancel(21-(20+40/n)-(n-40)/n) == 0)
verify('root_correction_exponent_41_over_20', sp.cancel(rat(41,20)-(2+2/n)-(n-40)/(20*n)) == 0)
verify('sqrt_dimension_bound_21_over_40', sp.cancel(rat(21,40)-(rat(1,2)+1/n)-(n-40)/(40*n)) == 0)
verify('cV_less_than_three', cV < 3)
verify('remaining_amplitude_less_than_one', 3*rat(5,8)/2 < 1)
verify('remaining_sqrt_factor_less_than_one', rat(4,8)*rat(21,40) < 1)
verify('combined_exponent_95_over_4', rat(1,2)+21+rat(41,20)+rat(1,5) == rat(95,4))
verify('explicit_constant_below_exp26', rat(95,4) < 26)
verify('companion_radius_constant', rat(20,8) == rat(5,2))

# Quadratic slack, including both parities and the scalar prefactor.
m = sp.symbols('m', integer=True, positive=True)
Nb = (b-1)*(b-2)/2
verify('quadratic_count_even', sp.expand(Nb.subs(b,m)-((2*m)**2/8-3*(2*m)/4+1)) == 0)
verify('quadratic_count_odd', sp.expand(Nb.subs(b,m)-((2*m+1)**2/8-(2*m+1)+rat(15,8))) == 0)
verify('general_quadratic_count', sp.expand(Nb-b*b/2*(1-3/b+2/b**2)) == 0)
verify('slack_lower_prefactor', 2*cW/cV == rat(74,67))

paths = [
 'agent2/ACTUAL_PROJECTION_REMAINDER.md',
 'agent2/ACTUAL_PROJECTION_REMAINDER_REPORT.md',
 'agent3/GAUSSIAN_VANDERMONDE_BOUND.md',
 'GROWING_HIGH_ROW_SLACK_DRAFT.md',
 'GROWING_HIGH_ROW_SLACK_CHECKS.json',
 'agent4/ADDITIONAL_GROWING_REVIEW.md',
 'agent2/GROWING_CONTENT_CORRECTION_SUMMARY.md',
]
result = {
 'status':'PASS_INDEPENDENT_SYMBOLIC_AND_CONSTANT_CHECKS',
 'scope':'Formal identities and exact rational/algebraic constants only; no actual HP indices, degree scan, prime scan, or numerical quadrature.',
 'check_count':len(checks),
 'checks':checks,
 'explicit_n_ge_40_verdict':'PASS: the displayed exp(26) constant remains valid; an exp(95/4) envelope follows from the independent proof.',
 'input_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
 'checker_sha256':sha256((BASE/'check_revised_remainder_review.py').read_bytes()).hexdigest(),
 'proof_dependencies':'Unrestricted analytic inequalities, all-size determinant bounds, and divergence of the positive bounding expression are proved in the accompanying review, not inferred from finite checks.',
 'actual_form_growth_or_nonvanishing_proved':False,
}
output = BASE/'revised_remainder_independent_checks.json'
output.write_text(json.dumps(result,indent=2)+'\n')
assert json.loads(output.read_text()) == result
print(json.dumps({'status':result['status'],'check_count':len(checks),'explicit_n_ge_40_verdict':result['explicit_n_ge_40_verdict'],'certificate':str(output)},indent=2))
