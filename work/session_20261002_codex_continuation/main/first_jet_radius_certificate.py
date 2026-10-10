"""New exact certificate for an integral-first-jet pullback radius ceiling."""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import importlib.util
import json

ROOT=Path('[private local path removed]')
SESSION=ROOT/'work/session_20261002_codex_continuation'
spec=importlib.util.spec_from_file_location('elliptic_interval_definitions',ROOT/'scripts/pullback_hyperbolic_radius_bound.py')
defs=importlib.util.module_from_spec(spec)
spec.loader.exec_module(defs)

def atan_bounds(inv,last):
    x=Q(1,inv)
    partial=sum((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(last+1))
    next_term=(-1)**(last+1)*x**(2*last+3)/Q(2*last+3)
    return min(partial,partial+next_term),max(partial,partial+next_term)

a5l,a5h=atan_bounds(5,100)
a239l,a239h=atan_bounds(239,100)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
Al,Ah,Bl,Bh,tail=defs.elliptic_h_interval(180)
tl,th=Bl/Ah,Bh/Al
al,ah=2*pil*(Al*Al-Bh*Bh),2*pih*(Ah*Ah-Bl*Bl)
assert al*tl>1 and ah*th<2
d1l,d1h=tl-(1-tl)/al,th-(1-th)/ah
d2l,d2h=2*(1+th)/ah-th,2*(1+tl)/al-tl
assert d1l>0 and d1h<tl and d1h<d2l

def upper_sqrt(q,digits=15):
    scale=10**digits
    upper=Q(isqrt(q.numerator*scale*scale//q.denominator)+1,scale)
    assert upper*upper>q
    return upper

bound=upper_sqrt(1/d1l)
assert bound<Q(3644263188060718,10**15)+Q(1,10**15)
record=dict(status='PASS_NEW_EXACT_FIRST_JET_RADIUS_CERTIFICATE',scope='Exact rational enclosures and comparisons only; analytic proof is in companion note',elliptic_last_index=180,atan_last_index=100,closest_lift_interval=[defs.fraction_record(tl),defs.fraction_record(th)],cover_derivative_interval=[defs.fraction_record(al),defs.fraction_record(ah)],pi_interval=[defs.fraction_record(pil),defs.fraction_record(pih)],optimal_j=1,optimal_radius_square_interval=[defs.fraction_record(1/d1h),defs.fraction_record(1/d1l)],strict_radius_upper=defs.fraction_record(bound),strict_radius_upper_decimal=defs.decimal_outward(bound,15,True),checks={'one_lt_a_t_lt_two':True,'j1_beats_j0':True,'j1_beats_j2':True,'all_other_integer_j_reduced_by_monotonicity':True})
(SESSION/'main/FIRST_JET_RADIUS_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],record['strict_radius_upper_decimal'])
