"""Bounded auxiliary evaluation of the new complete fifth moment formulas.

This is coordinator-authored code. It evaluates claimed exact polynomial
inputs, not an original growing-dimensional inverse or infinite theorem.
"""
import json,math,resource,time
from pathlib import Path
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;start=time.monotonic();MOD=512
P=(34,31,7,5,48,12,4,4,32,8,56,8)
DV=(112,102,10,124,16,24,56,0,96,16,80,96)
BETA=(113,74,78,72,120,80,112)
def choose(x,k):
    if k<0:return 0
    if x<0:return (-1)**k*math.comb(k-x-1,k)
    return math.comb(x,k) if k<=x else 0
def fg(s,x,coeff):
    return choose(s+3,3)*sum(coeff[r]*choose(x,r-s) for r in range(s,12)) if 0<=s<=11 else 0
def z(s,x):return BETA[-s-1] if -7<=s<=-1 else fg(s,x,DV)
def u(s,x):return (fg(s,x,P)+x*fg(s,x-1,P)+x*fg(s+1,x-1,P))%64
def vv(s,x):return (z(s,x)+x*z(s,x-1)+x*z(s+1,x-1))%128
ut=np.array([[u(s,r) for s in range(-1,12)] for r in range(128)],dtype=np.int64)
vt=np.array([[vv(s,r) for s in range(-8,12)] for r in range(128)],dtype=np.int64)
pref=np.ones(MOD,dtype=np.int64)
for i in range(1,MOD):pref[i]=int(pref[i-1])*(i if i%2 else 1)%MOD
assert int(pref[-1])==1
inv=np.ones(MOD,dtype=np.int64)
inv[-1]=pow(int(pref[-1]),-1,MOD)
for i in range(MOD-1,0,-1):inv[i-1]=int(inv[i])*(i if i%2 else 1)%MOD
def valfact(x):
    x=np.asarray(x,dtype=np.int64);res=np.zeros_like(x);x=x//2
    while np.any(x):res+=x;x=x//2
    return res
def oddfact(x,inverse=False):
    x=np.asarray(x,dtype=np.int64);res=np.ones_like(x);pr=inv if inverse else pref
    while np.any(x):res=res*pr[x%MOD]%MOD;x=x//2
    return res
def binom(n,k):
    n,k=np.broadcast_arrays(np.asarray(n,dtype=np.int64),np.asarray(k,dtype=np.int64))
    valid=(k>=0)&(k<=n);kk=np.where(valid,k,0)
    v=valfact(n)-valfact(kk)-valfact(n-kk)
    assert np.all(v>=0)
    un=oddfact(n)*oddfact(kk,True)%MOD*oddfact(n-kk,True)%MOD
    value=np.where(valid & (v<9),un*np.left_shift(1,np.minimum(v,9))%MOD,0)
    return value,v

receipts=[]
for dd in range(1,64,2):
    cc=4002*dd+2532;bb=128*dd+81;nn=4002*bb;A=2*nn
    j=np.arange(bb,dtype=np.int64);r=j%128;ll=bb-1-j
    ww,wdepth=binom(nn+2,j)
    ff=np.zeros(bb,dtype=np.int64);gg=ff.copy()
    for s in range(-8,12):
        mm,_=binom(A+ll,ll-s)
        if s>=-1:ff=(ff+ut[r,s+1]*mm)%64
        gg=(gg+vt[r,s+8]*mm)%128
    rawx=ww*ff%64;rawdiff=ww*gg%128
    assert np.all(rawx%4==0),dd
    assert np.all(rawdiff%8==0),dd
    xx=rawx//2;yy_minus_x=rawdiff//4
    ns=int(np.sum(xx*xx))%64;delta=int(np.sum(xx*yy_minus_x))%64
    _,we=binom(nn+2,bb);assert int(we)>=6
    t=np.arange(dd+1,dtype=np.int64)
    _,v1=binom(cc,t);_,v2=binom(2*cc+1+dd-t,dd-t)
    ev=v1+v2;c1=int(np.sum(ev==1));c2=int(np.sum(ev==2));pred=(24*c1+32*c2)%64
    assert ns==pred,(dd,ns,pred)
    assert delta%32==0,(dd,delta)
    aa=(cc-2)//4;v=dd//4;commonzero=bool(v&(aa+1))
    if commonzero:assert ns%32==0
    highweight=np.where(wdepth>=4,xx*yy_minus_x%64,0)
    assert not np.any(highweight)
    receipts.append({'auxiliary_D':dd,'C':cc,'b':bb,'n':nn,
        'norm_mod64':ns,'fifth_discrepancy':delta//32,'raw_H_minus_N_mod64':delta,
        'commonzero_bit_condition':commonzero,'count_C1':c1,'count_C2':c2,
        'norm_count_matches':True,'high_weight_mixed_exclusion_matches':True,
        'actual_endpoint_weight_depth':int(we)})
report={'auxiliary_odd_D_range':[1,63],'evaluated_cases':len(receipts),
    'fifth_discrepancy_values':sorted(set(r['fifth_discrepancy'] for r in receipts)),
    'truezero_fifth_values':sorted(set(r['fifth_discrepancy'] for r in receipts if r['commonzero_bit_condition'])),
    'all_norm_count_checks_pass':True,'all_mixed_high_weight_checks_pass':True,
    'receipt':receipts,'cpu_bounded':True,'wall_seconds':time.monotonic()-start,
    'scope':'Finite auxiliary polynomial/moment evaluations only; none are original power-9 exponents. '
       'No infinite alignment, original-domain population or final primitive denominator theorem.'}
(OUT/'binary_fifth_auxiliary_contraction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='receipt'}))
