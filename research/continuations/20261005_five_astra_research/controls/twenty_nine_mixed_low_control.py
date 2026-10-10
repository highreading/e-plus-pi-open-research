"""Coordinator-authored original-binomial low mixed constants, vectorized."""
import json,math,resource
from pathlib import Path
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
p=29;mod=p**4;lowb=687936;lowN=191112;b=lowb+mod;n=2001*b
out=Path(__file__).resolve().parent
xall=np.arange(mod,dtype=np.int64);v=(lowb-xall)%mod
borrow=np.zeros(mod,dtype=np.int64);carry=borrow.copy();carries=borrow.copy()
for i in range(4):
    pp=p**i
    borrow=((lowN//pp%p)-xall//pp%p-borrow<0).astype(np.int64)
    carry=(v//pp%p+(382220//pp%p)+carry>=p).astype(np.int64)
    carries+=borrow+carry
x=xall[(xall<=lowb)&(carries==2)];e=(x>lowN).astype(np.int64)
pref=np.ones(mod,dtype=np.int64)
for i in range(1,mod):pref[i]=int(pref[i-1])*(i if i%p else 1)%mod
ipref=np.ones(mod,dtype=np.int64);ipref[-1]=pow(int(pref[-1]),-1,mod)
for i in range(mod-1,0,-1):ipref[i-1]=int(ipref[i])*(i if i%p else 1)%mod
def fval(a):
    a=np.asarray(a,dtype=np.int64);val=np.zeros_like(a);a=a//p
    while np.any(a):val+=a;a=a//p
    return val
def funit(a,inverse=False):
    a=np.asarray(a,dtype=np.int64);unit=np.ones_like(a);pre=ipref if inverse else pref
    while np.any(a):
        unit=unit*pre[a%mod]%mod
        unit=np.where((a//mod)%2,(-unit)%mod,unit)
        a=a//p
    return unit
def binom(a,k):
    a,k=np.broadcast_arrays(np.asarray(a,dtype=np.int64),np.asarray(k,dtype=np.int64))
    val=fval(a)-fval(k)-fval(a-k)
    assert np.all(val>=0)
    unit=funit(a)*funit(k,True)%mod*funit(a-k,True)%mod
    power=np.where(val<4,p**np.minimum(val,4),0)
    return unit*power%mod,val
W,wval=binom(n+2,x)
base,bval=binom(2*n+b-x,b-x)
baseprod=W*base%mod
assert np.all(baseprod%(p**2)==0)
F0=7;ell=np.where(e==0,8,3);high=(F0*ell)%p
hiinv=np.array([pow(int(t),-1,p) for t in high],dtype=np.int64)
c=(baseprod//p**2)%p*hiinv%p
assert [int(np.sum(c[e==i]**2))%p for i in (0,1)]==[11,18]
qvals=np.arange(-31,1,dtype=np.int64)
k=b-x[:,None]-qvals[None,:]
Bj,bjval=binom(2*n+b-x[:,None]-1,k)
prod=W[:,None]*Bj%mod
A=np.zeros(32,dtype=np.int64);B=A.copy()
A[31]=2;B[31]=2;A[30]=1;B[30]=3;B[29]=1
for h in range(2,31):
    f=-6*(-1)**h*math.factorial(h-2)*p**2
    for a in range(h+1):
        c0=f*math.comb(h,a)%mod;q=a-h
        A[q+31]=(A[q+31]+c0)%mod
        B[q+31]=(B[q+31]+c0)%mod
        B[q+30]=(B[q+30]+c0)%mod
coeff=(A[None,:]+x[:,None]*B[None,:])%mod
terms=prod*coeff%mod
assert np.all(terms%p**3==0)
y=np.sum(terms,axis=1)%mod
assert np.all(y%p**3==0)
xi=(y//p**3)%p*hiinv%p
g=[int(np.sum(c[e==i]*xi[e==i]))%p for i in (0,1)]
report={'p':p,'representative_h':1,'representative_b':b,'representative_n':n,
'low_supported_cases':len(x),'boundary_q_range':[-31,0],
'original_binomial_modulus':mod,'kappa':[11,18],'mixed_low_constants_g0_g1':g,
'candidate_proportional_constants':[26,3],'candidate_matches':g==[26,3],
'every_boundary_monomial_in_p3':True,'complete_fixed_boundary_included':True,
'first_contact_on_old_support_omitted_under_prior_proof':True,
'finite_low_constant_calculation_only':True,'second_depth_alignment_not_established':True}
(out/'twenty_nine_mixed_low_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
