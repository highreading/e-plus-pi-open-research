"""Own offline rational checks; no original research program is imported.

These examples refute general inference rules, not this archive's actual K_N.
The symbolic all-parameter proofs are given in the accompanying report.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, isqrt, prod
import json

OUT = Path(__file__).resolve().parent

def transpose(A):
    return [list(r) for r in zip(*A)]

def multiply(A, B):
    BT = transpose(B)
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in BT] for row in A]

def inverse(A):
    n = len(A)
    M = [[F(x) for x in r] + [F(i == j) for j in range(n)]
         for i, r in enumerate(A)]
    for j in range(n):
        k = next(i for i in range(j, n) if M[i][j])
        M[j], M[k] = M[k], M[j]
        p = M[j][j]
        M[j] = [v/p for v in M[j]]
        for i in range(n):
            if i != j:
                p = M[i][j]
                M[i] = [x-p*y for x, y in zip(M[i], M[j])]
    return [r[n:] for r in M]

def determinant(A):
    n = len(A)
    M = [[F(x) for x in r] for r in A]
    d = F(1)
    for j in range(n):
        k = next((i for i in range(j, n) if M[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            M[k], M[j] = M[j], M[k]
            d = -d
        p = M[j][j]
        d *= p
        for i in range(j+1, n):
            q = M[i][j]/p
            M[i] = [x-q*y for x, y in zip(M[i], M[j])]
    return d

def norm2(v):
    return sum((x*x for x in v), F(0))

def dot(v, w):
    return sum((x*y for x, y in zip(v, w)), F(0))

def serial(x):
    if isinstance(x, F):
        return f'{x.numerator}/{x.denominator}'
    if isinstance(x, list):
        return [serial(v) for v in x]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    return x

examples = []
for t in [F(0), F(1,2), F(1,10), F(1,100)]:
    a, b = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    Z = [[F(1),F(0)],[F(0),a],[F(0),b],[F(0),F(0)],
         [F(0),F(0)],[F(0),F(0)]]
    U = [[r[1]] for r in Z]
    H = multiply(transpose(Z), Z)
    J = multiply(transpose(U), Z)
    G = multiply(multiply(J, inverse(H)), transpose(J))
    assert H == [[F(1),F(0)],[F(0),F(1)]] and G == [[F(1)]]
    assert a*a+b*b == 1
    examples.append({'example':'full_Gram_does_not_bound_retained_Gram',
        't':t,'ambient_dimension':6,'retained_coordinate_indices':[0,2,3,4],
        'H':H,'J':J,'G':G,'full_U_Gram':multiply(transpose(U),U),
        'good_tail_eta_squared':F(0),'denominator_tail_alpha_squared':a*a,
        'residual_T_D_Gram':[[b*b]],'all_actual_archive_matrices_used':False})

for m in [2,10,100]:
    a,b = F(m*m-1,m*m+1),F(2*m,m*m+1)
    assert a*a+b*b == 1
    # O_g=a e1+b e2, O_D=b e1-a e2; retained space contains e1 only
    # in this plane. Subtracting the retained good direction kills O_D.
    sharp = 1-a*a/(1-b*b)
    assert sharp == 0
    examples.append({'example':'positive_retention_can_vanish_after_good_subtraction',
        'm':m,'eta_squared':b*b,'alpha_squared':a*a,
        'before_good_subtraction_Gram':b*b,'after_good_subtraction_Gram':F(0),
        'sharp_lower_formula':sharp,'all_actual_archive_matrices_used':False})

for M in [1,10,100]:
    V = [[F(3,5),F(0)],[F(0),F(3,5)],
         [F(4,5),F(0)],[F(0),F(4,5)]]
    T = [[F(-4,5),F(0)],[F(0),F(-4,5)],
         [F(3,5),F(0)],[F(0),F(3,5)]]
    Je = [[F(M if i<2 else 1) if i==j else F(0)
           for j in range(4)] for i in range(4)]
    metric = multiply(transpose(Je),Je)
    endpoint = multiply(Je,V)[2:4]
    metric_on_kernel = multiply(multiply(transpose(V),metric),V)
    d = determinant(endpoint)**2/determinant(metric_on_kernel)
    assert multiply(transpose(T),T)==[[F(1),F(0)],[F(0),F(1)]]
    assert multiply(transpose(T),V)==[[F(0),F(0)],[F(0),F(0)]]
    assert d == F(256,(9*M*M+16)**2)
    examples.append({'example':'energy_conditioning_does_not_bound_physical_endpoint_angle',
        'M':M,'T_Gram':multiply(transpose(T),T),'M_e':metric,
        'physical_endpoint_angle_squared':d,'all_actual_archive_matrices_used':False})

R=[F(1,2),F(1)];u=[F(4),F(-1)];v=[F(1),F(1)]
w=[r*x for r,x in zip(R,u)];good=[r*x for r,x in zip(R,v)]
mu_pair=sum((r*r*x*y for r,x,y in zip(R,u,v)),F(0))
assert mu_pair==0 and dot(u,good)==1 and dot(w,good)==0
examples.append({'example':'one_power_and_two_power_weight_are_different',
    'R':R,'mu_orthogonality_pairing':mu_pair,
    'naive_one_power_good_pairing':dot(u,good),
    'corrected_polynomial_weight_good_pairing':dot(w,good),
    'remaining_cross_pairing_with_Sigma_ab_equal_one_half':F(1),
    'all_actual_archive_matrices_used':False})

H=[[F(2),F(1)],[F(1),F(2)]];J=[[F(1),F(0)]];h=[[F(3)]]
G=multiply(multiply(J,inverse(H)),transpose(J))
lift=multiply(multiply(multiply(inverse(H),transpose(J)),inverse(G)),h)
energy=multiply(multiply(transpose(lift),H),lift)[0][0]
single=[[F(3)],[F(0)]];difference=[[x[0]-y[0]] for x,y in zip(single,lift)]
single_energy=multiply(multiply(transpose(single),H),single)[0][0]
diff_energy=multiply(multiply(transpose(difference),H),difference)[0][0]
assert lift==[[F(3)],[F(-3,2)]] and energy==F(27,2)
assert diff_energy==single_energy-energy
examples.append({'example':'minimum_energy_and_Pythagoras_exact_identity',
    'H':H,'J':J,'h':h,'G':G,'minimum_energy_lift':lift,
    'minimum_energy':energy,'single_energy':single_energy,
    'difference_energy':diff_energy,'all_actual_archive_matrices_used':False})

for n in [1,5,20]:
    q=2**n;p=q-1;A=[[F(1),F(1,q)],[F(0),F(1)]]
    assert determinant(A)==1 and gcd(p,q)==1
    assert q*(F(1)-F(p,q))==1
    examples.append({'example':'uniform_conditioning_and_small_error_do_not_give_primitive_shrinkage',
        'n':n,'A':A,'rational_target':1,'p':p,'q':q,
        'relative_error':F(1,q),'primitive_integer_form':1,
        'rigorous_sigma_min_lower':F(1,2),'rigorous_sigma_max_upper':F(2),
        'all_actual_archive_matrices_used':False})

def log_unit_interval(x, terms=40):
    assert 1 <= x <= 2
    z=(x-1)/(x+1)
    lower=2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lower,lower+tail

ln2=log_unit_interval(F(2))
def positive_integer_log(p):
    k=p.bit_length()-1
    a,b=log_unit_interval(F(p,2**k))
    return a+k*ln2[0],b+k*ln2[1]

primes=[3,7,23,43,71,83,101,109,127,151]
Llow,Lhigh=F(3,2)*ln2[0],F(3,2)*ln2[1]
for p in primes:
    a,b=positive_integer_log(p)
    Llow+=a/F(p-1);Lhigh+=b/F(p-1)
scale=10**50;s=isqrt(5*scale*scale)
assert s*s < 5*scale*scale < (s+1)*(s+1)
phi_low=F(scale+s,2*scale);phi_high=F(scale+s+1,2*scale)
lnphi_low=log_unit_interval(phi_low)[0]
lnphi_high=log_unit_interval(phi_high)[1]
margin_low=Llow-5*lnphi_high;margin_high=Lhigh-5*lnphi_low
assert margin_low>F(3,200)
assert prod(primes)==25839289479611181
def bounded_rational_interval(a,b):
    den=10**30
    lo=F((a.numerator*den)//a.denominator,den)
    hi=F(-((-b.numerator*den)//b.denominator),den)
    assert lo<=a<=b<=hi
    return [lo,hi]

margin_interval=bounded_rational_interval(margin_low,margin_high)
assert margin_interval[0]>F(3,200)
rate={'primes':primes,'prime_product':prod(primes),'series_terms':40,
      'L_interval':bounded_rational_interval(Llow,Lhigh),
      'phi_interval':[phi_low,phi_high],
      'L_minus_5_log_phi_interval':margin_interval,
      'output_intervals_outward_rounded_rational_denominator':10**30,
      'required_lower_margin':F(3,200),'strict_margin_verified':True,
      'actual_prime_transfers_or_saddle_inputs_recomputed':False,
      'parent_main_review_204_inputs_are_separately_inherited':True}
(OUT/'independent_exact_general_interface_examples.json').write_text(
    json.dumps(serial({'reviewer':'/root/proof_inventory','examples':examples,
                       'finite_examples_are_not_actual_K_N_counterexamples':True}),
               ensure_ascii=False,indent=2)+'\n')
(OUT/'independent_exact_raw_exclusion_rate_margin.json').write_text(
    json.dumps(serial(rate),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'exact_general_examples':len(examples),'assertions':'passed',
                 'strict_margin_gt_3_over_200':True,'approximate_margin':float(margin_low),
                 'original_programs_imported':0,'network_used':False}))
