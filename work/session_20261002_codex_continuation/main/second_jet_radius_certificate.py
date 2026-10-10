"""New exact two-jet omitted-value certificate by two Schur steps."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json

ROOT=Path('[private local path removed]')
SESSION=ROOT/'work/session_20261002_codex_continuation'
spec=importlib.util.spec_from_file_location('elliptic_interval_definitions',ROOT/'scripts/pullback_hyperbolic_radius_bound.py')
defs=importlib.util.module_from_spec(spec);spec.loader.exec_module(defs)

def atan_bounds(inv,last):
    x=Q(1,inv);partial=sum((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(last+1))
    next_term=(-1)**(last+1)*x**(2*last+3)/Q(2*last+3)
    return min(partial,partial+next_term),max(partial,partial+next_term)

def Hprime_bounds(last):
    z=(Q(1,2),Q(1,2));power=(Q(1),Q(0));coef=Q(1);partial=(Q(0),Q(0))
    for k in range(1,last+1):
        coef*=Q((2*k-1)**2,(2*k)**2)
        partial=defs.cadd(partial,(k*coef*power[0],k*coef*power[1]))
        power=defs.cmul(power,z)
    r=Q(71,100);tail=r**last*((last+1)-last*r)/(1-r)**2
    return partial[0]-tail,partial[0]+tail,partial[1]-tail,partial[1]+tail

def mul(x,y):
    candidates=[a*b for a in x for b in y];return min(candidates),max(candidates)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))
def scale(x,y):return mul(x,(y,y))
def rec(x):
    # Retain compact rational outward enclosures instead of huge intermediary denominators.
    return [defs.fraction_record(Q(defs.decimal_outward(q,30,j==1))) for j,q in enumerate(x)]

p5l,p5h=atan_bounds(5,100);p239l,p239h=atan_bounds(239,100)
pil,pih=16*p5l-4*p239h,16*p5h-4*p239l
Al,Ah,Bl,Bh,_=defs.elliptic_h_interval(180)
Pl,Ph,Ql,Qh=Hprime_bounds(180)
C=(Al*Al-Bh*Bh,Ah*Ah-Bl*Bl)
a=scale(mul((pil,pih),C),2)
t=div((Bl,Bh),(Al,Ah))
ell=sub((Q(1),Q(1)),div(add(mul((Al,Ah),(Ql,Qh)),mul((Bl,Bh),(Pl,Ph))),C))
assert 0<ell[0]<ell[1]<1
R=Q(3475103224038694,10**15);s=1/R
x=div((R,R),a);y=scale(t,R)
# First-jet bound makes j=1 the only possible integer at this radius.
assert a[0]*t[0]>1 and a[1]*t[1]<2
j0_square=1/t[0]
j2_den=2*(1+t[1])/a[1]-t[1]
assert R*R>j0_square and R*R>1/j2_den
one=(Q(1),Q(1));one_minus_x2=sub(one,mul(x,x))
factor=div((R*R,R*R),scale(mul(a,one_minus_x2),2))
# |k+ell|<=1/factor reduces the possible integral second derivatives.
cap=(1/factor[1],1/factor[0])
assert 1+ell[0]>cap[1] and 2-ell[1]>cap[1]
Z=div(sub(y,x),scale(sub(one,mul(x,y)),s))
proofs={}
for k in [-1,0]:
    B=mul(factor,add(ell,(Q(k),Q(k))))
    if B[0]<=-1 or B[1]>=1:raise AssertionError('Bounded Schur pair needed')
    capacity=div(add(B,(s,s)),add(one,scale(B,s)))
    assert Z[0]>capacity[1],k
    proofs[str(k)]={'B_interval':rec(B),'largest_allowed_target_interval':rec(capacity),'target_lower_gt_capacity_upper':True}
record=dict(status='PASS_NEW_EXACT_SECOND_JET_RADIUS_CERTIFICATE',scope='Rational interval rejection at one radius; restriction to that subdisk excludes all larger radii',strict_radius_upper=defs.fraction_record(R),strict_radius_upper_decimal=defs.decimal_outward(R,15,True),ell_interval=rec(ell),a_interval=rec(a),t_interval=rec(t),Hprime_real_interval=rec((Pl,Ph)),Hprime_imag_interval=rec((Ql,Qh)),only_first_derivative=1,only_second_derivative_candidates=[-1,0],Schur_target_interval=rec(Z),rejections=proofs)
(SESSION/'main/SECOND_JET_RADIUS_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],record['strict_radius_upper_decimal'])
