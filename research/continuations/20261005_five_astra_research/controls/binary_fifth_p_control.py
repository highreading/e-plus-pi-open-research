"""Coordinator-authored exact central forcing and a bounded P64 lift.

Uniform parameter substitution is a separate proof obligation.
"""
import json
import math
import resource
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (60,60))
OUT=Path(__file__).resolve().parent
MOD=64
HREF=161
NREF=322
BREF=209
CS=(-1,2,-3,3)

def choose(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)

def rational_mod(x):
    assert x.denominator%2
    return x.numerator*pow(x.denominator,-1,MOD)%MOD

def falling(x,k):
    return math.prod(x-t for t in range(k))

def central(l):
    j=l//2
    if l%2:
        pref=math.prod(2*HREF+2*t+1 for t in range(j+1))*falling(HREF,j+1)
        s=sum(Fraction(2**r*math.factorial(r)**2,math.factorial(2*r+1))
              *choose(HREF-j-1,r)*choose(HREF+j,r) for r in range(8))
    else:
        pref=math.prod(2*HREF+2*t-1 for t in range(1,j+1))*falling(HREF,j)
        s=sum(Fraction(2**r*math.factorial(r)**2,math.factorial(2*r))
              *choose(HREF-j,r)*choose(HREF+j,r) for r in range(8))
    return rational_mod(pref*s)

cen=[central(l) for l in range(15)]
assert not any(cen[7:])
force=[sum(choose(i,l)*math.prod(NREF+t for t in range(l+1,i+1))*cen[l]
           for l in range(i+1))%MOD for i in range(15)]
assert force[14]==0
g=[(-1)**i*f%MOD for i,f in enumerate(force)]
oldg=(2,-9,19,-25,12,-4,16,-16)
assert [v%32 for v in g[:8]]==[v%32 for v in oldg]
assert not any(v%32 for v in g[8:])

E=[[sum(CS[s-1]*sum(choose(i,s-t)*choose(NREF,t)*choose(-t,j-i+s-t)
                      for t in range(s+1)) for s in range(1,5))%MOD
    for j in range(BREF)] for i in range(BREF)]
term=[(-1)**i*sum(c*choose(i,k) for k,c in enumerate(g))%MOD for i in range(BREF)]
result=[0]*BREF
for depth in range(6):
    result=[(r+(-2)**depth*t)%MOD for r,t in zip(result,term)]
    term=[sum(e*t for e,t in zip(row,term))%MOD for row in E]
vals=[(-1)**i*t%MOD for i,t in enumerate(result)]
coeff=[]
while vals:
    coeff.append(vals[0])
    vals=[(vals[i+1]-vals[i])%MOD for i in range(len(vals)-1)]
assert not any(coeff[35:])
old=json.loads((OUT/'binary_fourth_lift_control.json').read_text())['P_newton_mod32']
assert [c%32 for c in coeff[:len(old)]]==old
assert not any(c%32 for c in coeff[len(old):])
last=max(i for i,c in enumerate(coeff) if c)
report={
 'central_reference_h':HREF,'reference_n':NREF,'reference_b':BREF,
 'central_B_mod64':cen,'central_sum_r_cutoff':7,
 'forcing_f_over_R_mod64':force,'g64_newton':g,
 'P64_newton':coeff[:35],'P_last_nonzero_coefficient':last,
 'forcing_reduction_mod32_pass':True,'P_reduction_mod32_pass':True,
 'all_computation_exact_integer_or_odd_denominator_arithmetic':True,
 'fixed_reference_only':True,'uniform_transfer_requires_proof':True,
 'fifth_discrepancy_not_evaluated':True,
}
(OUT/'binary_fifth_p_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
