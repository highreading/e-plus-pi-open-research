"""Independent exact replay of Item237's defining differential identity.

No archived Python module is imported. Only the published factor data are
read; the old stored zero flag is not used. Fraction polynomial operations
recompute all coefficients of the cleared numerator.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import json

ROOT=Path(__file__).resolve().parents[2]
def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return p or [Q(0)]
def plus(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def times(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def scalar(a,t):return trim([x*t for x in a])
def power(a,n):
    out=[Q(1)]
    for _ in range(n):out=times(out,a)
    return out
def derivative(a):return trim([i*a[i] for i in range(1,len(a))])
def shift(a,t):
    out=[Q(0)]
    for x in reversed(a):out=plus(times(out,[Q(t),Q(1)]),[x])
    return out
def evaluate(a,t):
    out=0
    for x in reversed(a):out=out*t+x
    return out

record=json.loads((ROOT/'results/item237_j1_algebraic_residual_certificate.json').read_text())
factors=record['all_h_recurrence']['factored_coefficients']
P=[]
for ent in factors:
    row=scalar(list(map(Q,ent['remaining_core_low_to_high'])),Q(ent['scalar']))
    for numerator,denominator in ent['linear_factor_roots_numerator_denominator']:
        row=times(row,[Q(-numerator),Q(denominator)])
    P.append(row)
assert list(map(len,P))==[17]*4
D=list(map(Q,[6,14,7,2]));N=list(map(Q,[432,2064,4440,5376,4044,1860,486,48]))
T=list(map(Q,[2,2,1]));Y=list(map(Q,[0,1,1]));J=scalar(times(Y,T),3)
assert plus(scalar(times([Q(1),Q(2)],T),3),scalar(times(Y,derivative(T)),-2))==D
initial_A=list(map(Q,[Q(20,3),Q(14,3),Q(4,3)]))
initial_B=list(map(Q,[2,-5,-3]))
ua_num=scalar(times(times(T,T),initial_A),Q(3,2))
ub_num=scalar(times(times(T,T),initial_B),Q(3,2))
derived_N=plus(times(ub_num,times(D,D)),scalar(times(J,plus(times(derivative(ua_num),D),scalar(times(ua_num,derivative(D)),-1))),Q(1,2)))
assert derived_N==N
D_powers=[power(D,n) for n in range(36)]
T_powers=[power(T,n) for n in range(13)]
total=[Q(0)];summaries=[]
for k in range(4):
    numerator=N[:];den_degree=3;block=[Q(0)]
    for degree,coefficient in enumerate(P[k]):
        block=plus(block,scalar(times(numerator,D_powers[35-den_degree]),coefficient))
        if degree<16:
            # ((theta-6k)/2)(num/D^a); theta=J/D*d/dy.
            differentiated=plus(times(derivative(numerator),D),scalar(times(numerator,derivative(D)),-den_degree))
            numerator=scalar(plus(times(J,differentiated),scalar(times(numerator,D_powers[2]),-6*k)),Q(1,2))
            den_degree+=2
    u=6-2*k
    x_power_numerator=scalar(times([Q(0)]*(3*u)+[Q(1)],power([Q(1),Q(1)],3*u)),4**u)
    cleared=times(times(block,x_power_numerator),T_powers[12-2*u])
    total=plus(total,cleared)
    summaries.append({'k':k,'block_degree':len(block)-1,'cleared_block_degree':len(cleared)-1})
assert total==[0]

# The y=-1 branch: expand N(z-1),D(z-1), and the local X derivative.
Nminus=shift(N,-1);Dminus=shift(D,-1)
assert Dminus==list(map(Q,[-3,6,1,2]))
assert Nminus==list(map(Q,[54,-144,258,-240,354,-48,150,48]))
local_derivative=plus(scalar(times([Q(1),Q(-2)],[Q(1),Q(0),Q(1)]),3),scalar(times([Q(0),Q(0),Q(1)],[Q(1),Q(-1)]),-4))
assert local_derivative==scalar(Dminus,-1)
assert evaluate(D,-1)==-3 and evaluate(T,-1)==1

leading=[p[-1] for p in P]
assert leading==[Q(-64,531441),Q(-9856,19683),Q(-413233,729),Q(1)]
f=[-64,-266112,-301246857,531441]
residues=[evaluate(f,x)%7 for x in range(7)]
assert 0 not in residues and f[-1]%7
d,c,b,a=f
disc=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
assert disc<0
assert isqrt(-disc)**2!=-disc
assert (-disc)%3==0 and isqrt((-disc)//3)**2!=(-disc)//3
result={'classification':'independent exact polynomial proof replay',
        'imports_archived_python':False,'uses_stored_zero_flag':False,
        'degrees':[len(p)-1 for p in P],'leading_coefficients':list(map(str,leading)),
        'cleared_polynomial_is_exactly_zero':True,'blocks':summaries,
        'theta_parameter_identity':True,'parametric_N_derivation':True,
        'common_denominator':'D(y)^35*(y^2+2y+2)^12',
        'negative_one_branch_N':list(map(str,Nminus)),'negative_one_branch_D':list(map(str,Dminus)),
        'local_X_derivative_polynomial_identity':True,
        'clearing_denominator_at_y_minus_one':str(evaluate(D,-1)**35*evaluate(T,-1)**12),
        'limiting_cubic_coefficients_low_to_high':f,'cubic_residues_mod_7':residues,
        'cubic_discriminant':str(disc),'minus_discriminant_not_square':True,
        'minus_discriminant_over_3_not_square':True}
target=Path(__file__).with_name('recurrence_dependency_independent_checks.json')
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
