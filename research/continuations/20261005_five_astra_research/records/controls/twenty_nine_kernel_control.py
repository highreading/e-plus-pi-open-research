"""Coordinator bounded Newton-kernel construction and compression checks."""
import functools
import json
import math
import resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
OUT = Path(__file__).resolve().parent
p=29
n=2791829217
b=1395217

@functools.lru_cache(maxsize=100000)
def choose(a,k):
    if k<0:
        return 0
    if a>=0:
        return math.comb(a,k) if k<=a else 0
    return (-1)**k*math.comb(k-a-1,k)

def evaluate(coeff,x,mod):
    return sum(c*choose(x,r) for r,c in enumerate(coeff))%mod

def newton(values,mod):
    result=[]
    row=[x%mod for x in values]
    while row:
        result.append(row[0])
        row=[(row[i+1]-row[i])%mod for i in range(len(row)-1)]
    return result

ds=[0]
for s in range(1,59):
    v=sum(choose(n,s-u)*choose(s-u,u)*pow(2,-u,p**3)
          for u in range(s//2+1))
    ds.append((-1)**s*math.factorial(s)*v%p**3)
assert all(x%p==0 for x in ds)
assert all(choose(n,v)%p==0 for v in range(1,p))

mom=[0]*58
mom[0]=1
for t in range(1,29):
    mom[t]=p*(7*(8*pow(20,t,p)-20*pow(8,t,p))*pow(12*t,-1,p)%p)
g=[]
rising=1
for i in range(58):
    if i:
        rising=rising*(n+i)%p**2
    g.append((-1)**i*rising*sum(choose(i,t)*mom[t] for t in range(i+1))%p**2)
assert all(c%p==0 for c in g[29:])
h0=[(-1)**i*math.factorial(i)%p for i in range(29)]
assert [c%p for c in g[:29]]==h0

def compressed_l(s,coeff,x):
    result=(-1)**s*choose(x,s)*evaluate(coeff,x-s,p)
    if s==29:
        result+=(n//p)%p*evaluate(coeff,x,p)*choose(b+28-x,29)
    return result%p

def full_l(s,coeff,x):
    result=(-1)**s*choose(x,s)*evaluate(coeff,x-s,p)
    for v in range(1,s+1):
        nv=choose(n,v)%p
        if not nv:
            continue
        interior=0
        for r,eta in enumerate(coeff):
            for i in range(r+1):
                interior+=eta*choose(x-s+v,r-i)*choose(v+i-1,i)*choose(b-1-x+s,v+i)
        result+=(-1)**(s-v)*choose(x,s-v)*nv*interior
    return result%p

tests=0
for x in range(-2,61):
    for s in range(1,30):
        assert compressed_l(s,h0,x)==full_l(s,h0,x)
        tests+=1

ha_values=[]
for x in range(58):
    correction=sum(ds[s]*compressed_l(s,h0,x) for s in range(1,30))
    ha_values.append((evaluate(g,x,p**2)-correction)%p**2)
ha=newton(ha_values,p**2)

fr=[1]
for r in range(1,60):
    fr.append(fr[-1]*(b+r)%p**4)
ch=[sum(fr[r]*choose(2*n,r-h) for r in range(h,60))%p**4 for h in range(60)]
assert all(v%p**2==0 for v in ch[2:])
assert ch[0]%p**2==(1-2*n)%p**2 and ch[1]%p**2==(-1)%p**2

aq_values=[]
for x in range(58):
    total=0
    for s in range(1,59):
        for v in range(1,s+1):
            weight=ds[s]*choose(n,v)%p**3
            if not weight:
                continue
            cb=ch[0]*choose(b-x+s-1,v-1)-ch[1]*choose(b-x+s,v-1)
            total+=weight*(-1)**(s+v+1)*choose(x,s-v)*cb
    aq_values.append(total%p**3)
assert all(x%p==0 for x in aq_values)
aq=newton(aq_values,p**3)
ap=[(x//p)%p for x in aq]
assert all(x==0 for x in ap[29:])
ap=ap[:29]
for x in range(-2,61):
    expected=9*(choose(b-x+28,28)+choose(b-x+29,28))%p
    assert evaluate(ap,x,p)==expected
    for s in range(1,30):
        assert compressed_l(s,ap,x)==full_l(s,ap,x)
        tests+=1

hq_values=[]
for x in range(58):
    correction=p*sum(ds[s]*compressed_l(s,ap,x) for s in range(1,30))
    hq_values.append((aq_values[x]-correction)%p**3)
hq=newton(hq_values,p**3)

report={'status':'PASS','p':p,'n':n,'b':b,
        'operator_comparisons':tests,
        'hA_newton_mod841':ha,'hQ_newton_mod24389':hq,
        'boundary_c_h0_to59_mod707281':ch,
        'contact_d_s1_to58_mod24389':ds[1:],
        'leading_aQ_div29_newton_mod29':ap,
        'boundary_simplification_pass':True,'leading_contact_identity_pass':True,
        'scope':'Bounded coefficient construction and integer evaluation checks at the fixed representative. Degree/parameter transfer uses separately stated mathematical inputs; RC table and Gamma0 not computed.'}
(OUT/'twenty_nine_kernel_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','operator_comparisons','hA_newton_mod841','hQ_newton_mod24389','scope')}))
