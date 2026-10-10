"""Coordinator-authored fixed four-digit carry/unit computation."""
import math,json,resource
from pathlib import Path
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
out=Path(__file__).resolve().parent
p=29;L=p**4;b=687936;N=191112
x=np.arange(L,dtype=np.int64);v=(b-x)%L;e=(x>N).astype(np.int64)
fac=[math.factorial(i)%p for i in range(p)]
inv=[pow(t,-1,p) for t in fac];fa=np.array(fac);fi=np.array(inv)
def low_counts(c):
    borrow=np.zeros(L,dtype=np.int64);carry=np.zeros(L,dtype=np.int64)
    count=np.zeros(L,dtype=np.int64);unit=np.ones(L,dtype=np.int64)
    for i in range(4):
        power=p**i;nd=N//power%p;xd=x//power%p;vd=v//power%p;cd=c//power%p
        borrow=(nd-xd-borrow<0).astype(np.int64)
        carry=(cd+vd+carry>=p).astype(np.int64)
        count+=borrow+carry
        # Factorial residues of every low digit, with carries already encoded
        # by the ordinary integer upper/difference before digit extraction.
        ud=(c+v)//power%p;rd=((N-x)%L)//power%p
        unit=unit*fa[nd]*fa[ud]*fi[xd]*fi[rd]*fi[vd]*fi[cd]%p
    return count,unit
c0,u0=low_counts(382220);cm,um=low_counts(382219)
assert int(c0.min())>=2 and int(cm.min())>=2
assert int(c0[b+1:].min())>=3 and int(cm[b+1:].min())>=3
h0=np.array([sum((-1)**i*math.factorial(i)*math.comb(d,i) for i in range(d+1))%p for d in range(p)])
cc=((c0==2)*u0-h0[x%p]*(cm==2)*um)%p
cc[x>b]=0
kappa=[int(np.sum(cc[e==j]**2))%p for j in (0,1)]
def B(v):return math.comb(v+6,6)%p if 0<=v<=22 else 0
psi0=[];psi1=[]
for d in range(p):
    psi0.append(sum(math.comb(3,t)**2*(7+d-t)**2*B(d-t)**2 for t in range(4))%p)
    psi1.append(sum(math.comb(3,t)**2*(3-t)**2*B(d-t)**2 for t in range(4))%p)
mult=[(kappa[0]*psi0[d]+kappa[1]*psi1[d])%p for d in range(p)]
report={'p':p,'low_digit_cases':L,'kappa0':kappa[0],'kappa1':kappa[1],
    'base_norm_low_multipliers_d0to28':mult,'base_norm_multiplier_zeros':[d for d,t in enumerate(mult) if t==0],
    'minimum_low_carries_tau0':int(c0.min()),'minimum_low_carries_tau_minus1':int(cm.min()),
    'minimum_extra_range_carries_tau0':int(c0[b+1:].min()),
    'minimum_extra_range_carries_tau_minus1':int(cm[b+1:].min()),
    'every_case_carry_assertions_pass':True,
    'actual_norm_cross_multiplier_K01_not_computed':True,'finite_certificate_only':True}
(out/'twenty_nine_low_constants_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
