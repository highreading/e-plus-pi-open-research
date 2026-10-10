"""Coordinator-authored check of the proposed four-digit carry support."""
from pathlib import Path
import resource,json
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
p=29;L=p**4;b=687936;N=191112
x=np.arange(L,dtype=np.int64)
def count(q,base_shift=-1):
    lower=(b-x-q)%L
    complement=382220+base_shift+q
    borrow=np.zeros(L,dtype=np.int64);carry=borrow.copy();total=borrow.copy()
    for i in range(4):
        power=p**i
        borrow=((N//power%p)-x//power%p-borrow<0).astype(np.int64)
        carry=(lower//power%p+(complement//power%p)+carry>=p).astype(np.int64)
        total+=borrow+carry
    return total
mins={q:int(count(q).min()) for q in range(-60,88)}
base=count(0,0)
selected=(x<=b)&(base==2)
v=b-x[selected]
e=(x[selected]>N).astype(np.int64)
u=((382219+v)//L)
minus2=count(-2)
vp=np.zeros(L,dtype=np.int64)
z=x.copy();active=(z%p==0)&(z!=0)
for k in range(1,5):
    active=(x%(p**k)==0)
    vp+=active
vp[0]=4
report={
'p':p,'cases_per_laurent_power':L,'powers_tested':[-60,87],
'minimum_for_nonnegative_powers':min(mins[q] for q in range(88)),
'minimum_q0':mins[0],'minimum_q_minus1':mins[-1],
'minimum_negative_range':min(mins[q] for q in range(-60,1)),
'minimum_q_minus2_with_j_factor':int((minus2+vp).min()),
'base_supported_low_coordinates':int(selected.sum()),
'base_support_nonzero_residue_above2':int((x[selected]%p>2).sum()),
'high_factor_e_plus_u_violations':int((e+u!=1).sum()),
'boundary_lower_high_borrow_violations':int(((v+31)>=L).sum()),
'every_test_passes':False,'finite_digit_verification_only':True}
report['every_test_passes']=(report['minimum_for_nonnegative_powers']>=2 and mins[0]>=3 and mins[-1]>=3 and report['minimum_negative_range']>=1 and report['minimum_q_minus2_with_j_factor']>=3 and report['base_support_nonzero_residue_above2']==0 and report['high_factor_e_plus_u_violations']==0 and report['boundary_lower_high_borrow_violations']==0)
assert report['every_test_passes'],report
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
