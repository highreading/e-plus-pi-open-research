"""Fixed exact controls for the new local theorem; no index scan."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial,comb,gcd
import json

def add(a,b):
    return [(a[k] if k<len(a) else Q(0))+(b[k] if k<len(b) else Q(0)) for k in range(max(len(a),len(b)))]
def mul(a,b):
    v=[Q(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):v[j+k]+=x*y
    return v
def derivative(a):return [k*a[k] for k in range(1,len(a))] or [Q(0)]
def scale(a,c):return [x*c for x in a]
@lru_cache(None)
def H(n):
    v=[Q(1)]
    for _ in range(n):v=mul(v,[Q(1),Q(-1),Q(1,2)])
    out=[factorial(n)*v[n-j]/factorial(j) for j in range(n+1)]
    assert all(x.denominator==1 for x in out)
    return out
def ev(a):return sum(a,Q())
def h(n):return int(ev(H(n)))
def j(n):return int(n*ev(H(n))+ev(derivative(H(n))))
def valuation(v,p):
    v=Q(v)
    if v==0:return None
    a,b=abs(v.numerator),v.denominator;ans=0
    while a%p==0:a//=p;ans+=1
    while b%p==0:b//=p;ans-=1
    return ans

rows=[]
for n in [1,2,4,8]:
    hn=H(n);hn1=H(n+1);d=derivative(hn);dd=derivative(d)
    raising=add(mul([Q(0),Q(1,2)],dd),mul([n+1,-1],add(d,scale(hn,-1))))
    assert all(x==0 for x in add(raising,scale(hn1,-1)))
    lowering=scale(add(add(hn,scale(d,-1)),scale(dd,Q(1,2))),n+1)
    assert all(x==0 for x in add(lowering,scale(derivative(hn1),-1)))
    assert j(n+1)==(n+1)*(ev(dd)+(n-1)*(ev(d)-ev(hn)))
    rows.append({'n':n,'both_polynomial_differential_identities_and_special_gate':True})

for p,a,u in [(3,1,1),(3,1,2),(3,2,1),(5,1,1),(5,2,1),(7,1,1),(7,2,1),(11,1,1),(5,1,3)]:
    n=1+p**a*u
    assert u%p
    hn=h(n);jn1=j(n+1);hdd=int(ev(derivative(derivative(H(n)))))
    assert (hdd-3*(n-1))%p**(a+1)==0
    assert (jn1-8*(n-1))%p**(a+1)==0
    assert valuation(jn1,p)==a and valuation(gcd(hn,jn1),p)==a
    checked=0
    for b in range(n+1):
        for c in range(n+1):
            r=b+2*c;s=b+c;R=r+2
            if s<2 or R>n or s>n:continue
            term=Q((-1)**b*factorial(n)*comb(n,s)*comb(s,c),2**c*factorial(n-R))
            assert valuation(term,p)>=2*a
            checked+=1
    rows.append({'p':p,'a':a,'u':u,'n':n,'second_derivative_and_unit_eight_lifts':True,'exact_common_valuation':a,'high_binomial_terms_checked':checked})

# Complete fixed-prime root tables, not a longer degree-prefix scan.
table=[(r,h(r),j(r+1)) for r in range(5)]
assert [r for r,hh,jj in table[:3] if hh%3==jj%3==0]==[1]
assert [r for r,hh,jj in table if hh%5==jj%5==0]==[1,4]
rows.append({'complete_residue_tables':{'mod3_roots':[1],'mod5_roots':[1,4]},'exact_values':table})

coeff=[Q(1),Q(1)]
for r in range(2,15):coeff.append(coeff[-1]-coeff[-2]/2)
partial=sum(((-1)**r*factorial(r)*coeff[r] for r in range(15)),Q())
assert partial==-591174425 and valuation(partial,5)==2
assert valuation(factorial(15),5)==3
rows.append({'fixed_padic_constant_C5':{'exact_fifteen_term_sum':int(partial),'residue_mod125':int(partial)%125,'valuation':2,'all_remaining_terms_divisible_by125':True}})

for p,m in [(3,3),(3,9),(5,5),(5,25)]:
    a=valuation(m,p)
    assert (j(m)-2*m)%p**(a+1)==0 and valuation(j(m),p)==a
    rows.append({'p':p,'m':m,'unit_two_lift':True})
assert valuation(gcd(h(24),j(25)),5)==2
rows.append({'n':24,'additional_odd_gcd_factor_is_not_squarefree':{'p':5,'valuation':2}})

result={'status':'PASS; fixed exact controls, all-index proof is in hp_special_gcd_unit_lift.md','rows':rows}
Path(__file__).with_name('hp_special_gcd_unit_lift_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
