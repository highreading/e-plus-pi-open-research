"""Coordinator-authored finite low-row audit, never an original-word proof.

Implements the explicitly displayed short polynomial symbols and finite atoms
in A2 turn1. Every claimed support/payment condition is checked independently.
No external code, credentials, network, or unbounded original exponent is used.
"""
from pathlib import Path
from collections import defaultdict, Counter
from math import comb, factorial
import hashlib, json, time

ROOT=Path(__file__).resolve().parent
p=29;mod=p*p;cut=5044;last=5074;n0=20387;b0=5044
started=time.monotonic()
fact=[factorial(i) for i in range(59)]
fm=[v%p for v in fact[:29]]
fi=[pow(v,-1,p) for v in fm]
harm=[0]
for i in range(1,p):harm.append((harm[-1]+pow(i,-1,p))%p)
ts=[2,1]
for i in range(2,p):ts.append((ts[-1]-15*ts[-2])%p)
cs=[1]+[(p*7*fm[s-1]*ts[s])%mod for s in range(1,p)]+[p*22]

poly=[1]
for _ in range(p):
    nxt=[0]*(len(poly)+2)
    for i,x in enumerate(poly):
        nxt[i]+=x;nxt[i+1]+=2*x;nxt[i+2]+=2*x
    poly=nxt
poly[0]-=1;poly[p]-=2;poly[2*p]-=2
assert all(v%p==0 for v in poly)
ee=[v//p%p for v in poly]
head=[]
for i in range(p):
    xi=sum(comb(i,t)*ee[p-t] for t in range(1,i+1))%p
    ze=sum(comb(i,t)*ee[2*p-t] for t in range(1,i+1))%p
    head.append((2*fact[i]+p*7*fm[i]*(2*harm[i]+14*xi+8*ze))%mod)
head.extend(p*24*fm[i]%mod for i in range(p))

def sg(k):return -1 if k%2 else 1
ret=[]
for h in range(p):
    val=0
    for s in range(h+1,p+1):
        xx=b0+h-s
        dd=sum(sg(i)*fm[i]*comb(xx,i) for i in range(p))%p
        # Original b is odd; its residue b0=5044 is even.
        val+=2*cs[s]*comb(b0+h,s)*sg(1+h-s)*dd
    ret.append(val%mod)

atoms=defaultdict(list)
def add(group,alpha,v,r,coef):
    coef%=mod
    if coef:atoms[group].append((alpha,v,r,coef))
for i in range(58):
    for r in range(i+1):
        add('Z_source0',r+1,-1-r,i-r,-head[i]*sg(r+i)*comb(2*n0+r-1,r))
for i in range(p):
    for s in range(1,p+1):
        add('Z_source1',1,s-1,i+s,-2*fact[i]*sg(i)*cs[s]*comb(i+s,s))
    add('Z_source29',30,-1,i,-2*fact[i]*sg(i)*cs[p]*22)
for h in range(p):add('Z_return',0,h,0,ret[h])
add('Y_return',0,0,0,175);add('Y_return',0,1,0,463)
for h in range(2):
    for s in range(1,p+1):add('Y_source1',0,h+s,s,sg(h)*cs[s])
    add('Y_source29',29,h,0,sg(h)*cs[p]*22)
assert sum(map(len,atoms.values()))<=2000

# Group the two reconstructed branches by their actual low factorial shifts.
# Keep source/return labels separate, and retain every coefficient modulo p^2.
branches=defaultdict(lambda:defaultdict(list))
for group,aa in atoms.items():
    for alpha,v,r,coef in aa:
        branches[(alpha,v)][group].append((r,sg(v)*coef%mod))
        branches[(alpha,v+1)][group].append((r+1,sg(v)*(r+1)*coef%mod))
assert max(r for gg in branches.values() for terms in gg.values() for r,_ in terms)<=58

pascal=[];row=[1]+[0]*58
for ell in range(last+1):
    pascal.append(row[:])
    row=[1]+[(row[i]+row[i-1])%mod for i in range(1,59)]

def digits(v):return (v%p,v//p%p,v//(p*p)%p)
nd=digits(20389)
jd=[digits(ell) for ell in range(last+1)]
stats=Counter();viol=[]
profiles={group:[[0]*(last+1) for _ in range(3)] for group in atoms}
expected_states={(0,0,0),(0,1,1),(1,1,1),(1,1,0)}
def extract(alpha,vprime,ell):
    ad=digits(16384+alpha);bd=digits(cut+vprime)
    w=k=c=e=0;unit=1;lastdig=None
    for aa,bb,jj,nn in zip(ad,bd,jd[ell],nd):
        xx=nn-jj-w;ll=xx%p;w=int(xx<0)
        yy=bb-jj-k;kk=yy%p;k=int(yy<0)
        zz=aa+kk+c;tt=zz%p;c=int(zz>=p)
        e+=w+c
        unit=unit*fm[nn]*fm[tt]*fi[jj]*fi[ll]*fi[aa]*fi[kk]%p
        lastdig=(ll,kk,jj,tt)
    unit=unit*sg(e)%p
    ll,kk,jj,tt=lastdig
    gamma=(harm[ll]+harm[kk]-harm[jj]-harm[tt])%p
    return e,(w,k,c),unit,gamma

for (alpha,vprime),gg in sorted(branches.items()):
    aa=16384+alpha;bb=cut+vprime
    if not (0<bb<20389<aa+bb<p**3):
        viol.append({'kind':'shift_box','alpha':alpha,'vprime':vprime})
    for ell in range(last+1):
        e,state,unit,gamma=extract(alpha,vprime,ell)
        predicted=((0,0,0) if ell<=bb else (0,1,1) if ell<=20389
                   else (1,1,1) if ell<=aa+bb else (1,1,0))
        if state!=predicted or state not in expected_states:
            if len(viol)<30:viol.append({'kind':'interface','alpha':alpha,'vprime':vprime,'ell':ell,'state':state,'predicted':predicted})
        if e>2:continue
        for group,terms in gg.items():
            coef=sum(t*pascal[ell][r] for r,t in terms)%mod
            if not coef:continue
            val=0 if coef%p else 1
            order=e+val
            stats['nonzero_group_rows']+=1
            if order==0:
                stats['unpaid_order_zero']+=1
                if len(viol)<30:viol.append({'kind':'unpaid_order_zero','group':group,'alpha':alpha,'vprime':vprime,'ell':ell,'coef':coef,'e':e})
            if order==1:
                if state!=(0,0,0):
                    stats['non000_leading']+=1
                    if len(viol)<30:viol.append({'kind':'non000_leading','group':group,'alpha':alpha,'vprime':vprime,'ell':ell,'state':state})
                paid=coef//p if e==0 else coef
                if e==0:stats['paid_leading_divisions']+=1
                z=paid*unit%p
                profiles[group][0][ell]=(profiles[group][0][ell]+z)%p
                profiles[group][1][ell]=(profiles[group][1][ell]+z*gamma)%p
            if order==2 and state==(0,1,1):
                assert e>=1
                paid=coef//p if e==1 else coef
                if e==1:stats['paid_011_divisions']+=1
                profiles[group][2][ell]=(profiles[group][2][ell]+paid*unit)%p

zgroups=[g for g in profiles if g.startswith('Z_')]
ygroups=[g for g in profiles if g.startswith('Y_')]
def total(groups,r):return [sum(profiles[g][r][ell] for g in groups)%p for ell in range(last+1)]
a,bb,cc=(total(zgroups,r) for r in range(3))
g,dd,ee011=(total(ygroups,r) for r in range(3))
def values(lo,hi):
    return {'alpha':sum(a[i]*g[i] for i in range(lo,hi))%p,
            'lambda':sum(a[i]*dd[i]+g[i]*bb[i]-a[i]*ee011[i]-g[i]*cc[i] for i in range(lo,hi))%p}
lower=values(0,cut);upper=values(cut,last+1)
coeff={'alpha':(lower['alpha']+upper['alpha'])%p,'delta':upper['alpha'],
       'lambda':(lower['lambda']+upper['lambda'])%p,'mu':0,'chi':0}
cross=[]
for zg in zgroups:
    for yg in ygroups:
        zz=profiles[zg];yy=profiles[yg]
        cross.append({'Z':zg,'Y':yg,
          'alpha':sum(zz[0][i]*yy[0][i] for i in range(last+1))%p,
          'delta':sum(zz[0][i]*yy[0][i] for i in range(cut,last+1))%p,
          'lambda':sum(zz[0][i]*yy[1][i]+yy[0][i]*zz[1][i]-zz[0][i]*yy[2][i]-yy[0][i]*zz[2][i] for i in range(last+1))%p})
payload={'scope':'Finite low dictionary assembly only, conditional on retained original-source and radical premises; not an original high-word evaluation or global irrationality proof.',
  'status':'passed_displayed_payment_and_support_checks' if not viol else 'SPECIFICATION_CHECK_FAILED_DO_NOT_PROMOTE',
  'coefficients':coeff,'lower_subtotal':lower,'upper_subtotal':upper,
  'group_atom_counts':{k:len(v) for k,v in atoms.items()},'unique_shift_pairs':len(branches),
  'stats':dict(stats),'violations':viol,'source_return_crosschecks':cross,
  'symbols':{'c_mod841':cs,'head_mod841':head,'Z_return_mod841':ret},
  'profile_sha256':hashlib.sha256(json.dumps(profiles,sort_keys=True).encode()).hexdigest(),
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'elapsed_seconds':round(time.monotonic()-started,3)}
(ROOT/'prime29_low_observation_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
(ROOT/'prime29_low_observation_profiles.json').write_text(json.dumps(profiles)+'\n')
print(json.dumps({k:payload[k] for k in ['status','coefficients','group_atom_counts','unique_shift_pairs','stats','violations','elapsed_seconds']}),flush=True)
