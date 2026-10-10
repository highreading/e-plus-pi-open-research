"""Coordinator-authored bounded complete-force difference receipt.

The infinite central sums are reduced modulo2^64 with a factorial-tail proof.
This is a finite audit; it is not a proof for all contact words or actual indices.
"""
from pathlib import Path
from math import comb,factorial
from fractions import Fraction as F
import hashlib,json

ROOT=Path(__file__).resolve().parent
PREC=64;MOD=1<<PREC;STOP=96

def vi(x):
    if not x:return None
    x=abs(x);v=0
    while x%2==0:x//=2;v+=1
    return v

def L(n):return n-n.bit_count()
def bc(x,s):
    if s<0:return 0
    if x>=0:return comb(x,s) if s<=x else 0
    return (-1)**s*comb(-x+s-1,s)

def res(x):
    x=F(x);assert x.denominator%2
    return x.numerator*pow(x.denominator,-1,MOD)%MOD

def falling(x,m):
    out=1
    for a in range(m):out*=x-a
    return out

def central(h,ell):
    j=ell//2;odd=ell%2;degree=j+odd
    pref=1
    for t in range(odd,j+1):
        if not odd and t==0:continue
        pref*=2*h+2*t+(-1 if not odd else 1)
    if odd:
        # Odd formula has t=0,...,j rather than the even1,...,j range.
        pref=1
        for t in range(j+1):pref*=2*h+2*t+1
    pref*=falling(h,degree)
    value=0
    for s in range(STOP):
        a=F((1<<s)*factorial(s)**2,factorial(2*s+odd))
        assert vi(a.numerator)-vi(a.denominator)==L(s)
        value+=res(a)*bc(h-j-odd,s)*bc(h+j,s)
    # For s>=STOP, L(s)>=L(STOP)>=PREC. All remaining factors are integral.
    assert L(STOP)>=PREC
    return pref*value%MOD

def force(k):
    h,n=32*k+1,64*k+2
    B=[central(h,ell) for ell in range(32)]
    out=[]
    for i in range(32):
        value=sum(comb(i,ell)*falling(n+i,i-ell)*B[ell] for ell in range(i+1))
        out.append((-1)**i*value%MOD)
    return out

if __name__=='__main__':
    scalar_cases=0
    for i in range(257):
        for ell in range(i+1):
            val=L(i)-L(ell)+L((ell+1)//2)
            assert val>=L(i//2);scalar_cases+=1
    pairs=[(1,3),(3,5),(-1,1),(-3,-1),(1,1+(1<<12)),(-3,-3+(1<<18))]
    cases=[];cache={}
    for k,kp in pairs:
        for z in (k,kp):
            if z not in cache:cache[z]=force(z)
        ell=vi(k-kp);rows=[]
        for i,(a,b) in enumerate(zip(cache[k],cache[kp])):
            expected=ell+5+L(i//2)-(max(1,i).bit_length()-1)
            d=(a-b)%MOD;observed=vi(d)
            assert expected<PREC
            assert observed is None or observed>=expected
            rows.append({'i':i,'bound':expected,'observed_depth':observed,
                         'observed_at_least64':d==0})
        cases.append({'k':k,'k_prime':kp,'parameter_difference_depth':ell,'rows':rows})
        print(json.dumps({'k':k,'k_prime':kp,'all32_complete_force_bounds_pass':True}),flush=True)
    for s in range(124,8193):
        W=max(0,(s-3+3)//4);beta=5+W-((4*W+3).bit_length()-1)
        c=(s+4)//128;delta=beta-L(c-1)
        assert 128*delta>=15*s+460
    out={'status':'PASS','scope':'Finite factorial scalar and complete first-force parameter differences; no all-word or relative norm theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'modulus':str(MOD),'central_sum_stop':STOP,'tail_minimum_depth':L(STOP),
         'factorial_scalar_checks':scalar_cases,'cases':cases,'linear_cutoff_checks':8069,
         'auxiliary_parameter_note':'b1 and b3 with n4002b do not have k=(2001b-1)/32 in Z2. They cannot audit a theorem restricted to k in Z2. The finite pairs here use integral odd k and complete continued central forces.'}
    dest=ROOT/'weighted_force_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:v for k,v in out.items() if k!='cases'}
    receipt['pair_count']=len(cases);receipt['coefficient_checks']=sum(len(c['rows']) for c in cases)
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'weighted_force_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
