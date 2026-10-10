"""New symbolic controls for the fixed-weight Christoffel research.
No HP systems, degree sweep, prime scan, or earlier checker execution.
"""
import json
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
R = s.Rational
checks = {}
def verify(name, value):
    checks[name] = bool(value)
    assert checks[name], name

t,bprev,bcur,bnext = s.symbols('t bprev bcur bnext')
P,Pprev = s.symbols('P Pprev')
beta = bprev*(bcur-R(1,2))
beta_next = bcur*(bnext-R(1,2))
Pnext = (t-R(1,2))*P+beta*Pprev
Pnext2 = (t-R(1,2))*Pnext+beta_next*P
qprev = (P+bprev*Pprev)/t
qcur = (Pnext+bcur*P)/t
qnext = (Pnext2+bnext*Pnext)/t
ahat = R(1,2)+bcur-bnext
betahat = beta*bcur/bprev
verify('Christoffel_three_term_recurrence', s.cancel(qnext-(t-ahat)*qcur-betahat*qprev)==0)
verify('transformed_recurrence_beta_simplification', s.cancel(betahat-bcur*(bcur-R(1,2)))==0)

# Exact transformed second-kind functions and the mass pi-2.
A,v,alpha,pi,h = s.symbols('A v alpha pi h')
Ahat = 2*bcur*A
vhat = (bcur+alpha)*v
vhat_next = ((bnext+R(1,2))*alpha+beta_next)*v
w0 = pi*A-v
w1 = pi*bcur*A-alpha*v
what = w1+bcur*w0-2*Ahat
verify('rational_second_kind_mass_shift', s.expand((pi-2)*Ahat-what-vhat)==0)
verify('transformed_Wronskian', s.expand(2*bcur*bnext*A*vhat-Ahat*vhat_next-bcur*A*v*(bcur-alpha))==0)
verify('relative_reference_scalar', s.cancel((vhat/Ahat)/(v/A)-(1+alpha/bcur)/2)==0)
verify('reference_pi_approximant_adjacent_average', s.cancel(2+what/Ahat-(w1/(bcur*A)+w0/A)/2)==0)
verify('transformed_nu_exact_factor_two', s.cancel(Ahat/(bcur*h)-2*A/h)==0)

# Rank-one relations to the balanced reference functions.
U = s.symbols('U')
P2 = (t-R(1,2))*U+beta_next*P
q0 = (U+bcur*P)/t
q1 = (P2+bnext*U)/t
Vbal = (bcur*A*P-A*U)/(h*(1-t))
Wbal = (v*U-alpha*v*P)/(h*(1-t))
Vhat = (2*bcur*bnext*A*q0-Ahat*q1)/(bcur*h*(1-t))
What = (vhat*q1-vhat_next*q0)/(bcur*h*(1-t))
verify('rank_one_endpoint_kernel_relation', s.cancel(t*Vhat-Vbal-2*A*U/h)==0)
verify('rank_one_projection_remainder_relation', s.cancel(t*What-Wbal+vhat*U/(bcur*h))==0)

# New uniform bounds; unrestricted proofs accompany the certificate.
verify('balanced_endpoint_interval_lower_induction', R(1,2)+R(1,16)/R(11,18)>=R(3,5))
verify('balanced_endpoint_interval_upper_induction', R(1,2)+R(1,15)/R(3,5)==R(11,18))
verify('transformed_diagonal_lower', R(1,2)+R(3,5)-R(11,18)==R(22,45))
verify('transformed_diagonal_upper', R(1,2)+R(11,18)-R(3,5)==R(23,45))
verify('transformed_beta_upper', R(1,15)*R(11,18)/R(3,5)==R(11,162))
verify('transformed_ratio_disk_gap', R(22,45)-R(1,20)==R(79,180))
verify('transformed_second_kind_ratio_upper', R(11,162)/R(22,45)==R(5,36))
rmax = R(180,79)
amax = R(5,36)
bmax = R(11,18)
cW = R(2080,1501)
cV = R(3780,1501)
verify('transformed_W_shape_upper', (1+amax*rmax)/R(19,20)==cW)
verify('transformed_W_shape_lower', (1-amax*rmax)/R(21,20)==R(360,553))
verify('transformed_V_shape_upper', (1+bmax*rmax)/R(19,20)==cV)
verify('direct_transformed_reference_lower', (1-amax*rmax)/(1+bmax*rmax)==R(2,7))
verify('transformed_special_majorant_ratio', cW/cV==R(104,189))
verify('relative_majorant_constant_against_balanced', (cW/cV)/R(37,67)==R(6968,6993))
high = R(1,20)+R(23,45)+R(11,162)*rmax
verify('transformed_high_row_ratio', high==R(1131,1580))
verify('transformed_high_row_strict_bound', high<R(397,540))
verify('zero_value_divided_difference_lower', 1-R(1,12)/R(1,2)**2==R(2,3))

# Coefficient norm comparison, derived from alternating coefficients.
verify('coefficient_norm_ratio_lower', (R(3,2)-R(11,18))/(2*R(11,18))==R(8,11))
verify('coefficient_norm_ratio_upper', (R(14,9)-R(3,5))/(2*R(3,5))==R(43,54))

# The new Rodrigues polynomial has an extra derivative/factorial shift.
n,j,l,b = s.symbols('n j l b', integer=True)
k = n+1
verify('weighted_complete_tail_derivative_index', s.expand(k+1+l-(j+1)-(n+1+l-j))==0)
verify('weighted_combined_polynomial_degree', s.expand((2*n+3)-(n+2-b)-1-(n+b))==0)
verify('one_extra_companion_factorial_index', s.expand((n+2-b)-(n+1-b))==1)

# Complete cofactor quotient: the rational shift is 2, not zero.
A0,A1,Z0,Z1,K,wP,wU,ep = s.symbols('A0 A1 Z0 Z1 K wP wU ep')
d = A1*Z1-A0*Z0
vP = (pi-2)*A0-wP
vU = (pi-2)*A1-wU
principal = (vP*Z0-vU*Z1)/d
companion = -ep-K/d
ratio_XY = -2-(wU*Z1-wP*Z0)/d+K/d
verify('full_weighted_quotient_and_shift', s.cancel(-principal-companion-(ep+pi+ratio_XY))==0)

# A second complete decomposition uses the actual normalized B vector.
la = s.symbols('lambda_full_U_tail')
hw = A1*vP-A0*vU
lc = (A0*la-hw)/A1
verify('actual_B_normalized_complete_remainder', s.cancel((vP*la-vU*lc)/hw-(la+vU)/A1)==0)

# Explicit n>=40 companion envelope: constants only, no degree sample.
verify('new_root_correction_exponent', R(3)+R(3,40)==R(123,40))
verify('new_companion_constant_exponent', R(1,2)+21+R(123,40)+R(1,5)+1==R(1031,40))
verify('new_companion_constant_below_exp26', R(1031,40)<26)
verify('transformed_cV_less_than_three', cV<3)
verify('remaining_amplitude_less_than_two', 3*R(5,8)<2)
verify('uniform_geometric_factor_at_threshold', R(18,40)<R(1,2))
verify('constant_power_bound', 3**26<2**42)
verify('uniform_companion_envelope_below_one', R(4,40**2)==R(1,400))

# Same primitive pair with the balanced selector: the clearer gain cancels.
F,g,Y = s.symbols('F g Y', nonzero=True)
verify('identical_pair_reduced_denominator', s.cancel((n+1)*F*Y/((n+1)*g)-F*Y/g)==0)

result = {
    'status':'PASS_FIXED_WEIGHT_CHRISTOFFEL_CONTROLS',
    'scope':'New formal Christoffel, second-kind, rank-one, constant and complete-tail controls only. No HP system, degree sweep, prime scan, or previous checker execution.',
    'check_count':len(checks),
    'checks':checks,
    'new_uniform_constants':{
        'disk_radius':'1/20',
        'q_n_over_q_next_modulus_upper_for_n_ge_2':'180/79',
        'transformed_alpha_modulus_upper_for_n_ge_2':'5/36',
        'W_shape_upper':'2080/1501',
        'V_shape_upper':'3780/1501',
        'direct_W_over_V_lower_multiplier':'2/7',
        'high_adjacent_ratio_for_k_ge_3':'1131/1580',
        'coefficient_norm_ratio_interval':'[8/11,43/54]'
    },
    'limits':[
        'Polynomial Gram nonsingularity is proved from the signed Christoffel norms, not from these finite checks.',
        'Weighted contact determinants and actual endpoint gcds are not bounded by this certificate.',
        'A smaller reference scalar or cofactor bound does not prove a smaller primitive form.',
        'The selector imposing the missing balanced equation gives identical primitive forms.'
    ]
}
out = BASE/'fixed_weight_christoffel_checks.json'
assert not out.exists(), 'Preserve any existing output and inspect before replacing it.'
out.write_text(json.dumps(result,indent=2)+'\n')
assert json.loads(out.read_text())==result
print(json.dumps(result,indent=2))
