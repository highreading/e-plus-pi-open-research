"""Second algorithm, direct defining polynomials modulo p^3, 46 rows."""
import itertools
import json
import math
import resource
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
primes=[5,11,13,17]
prior=json.loads((OUT/'b4_normalized_control.json').read_text())
tables={r['prime']:{a['n']:a['values_mod_p'] for a in r['rows']} for r in prior['extension'] if r['prime'] in primes}
def fall(a,r,mod):
    v=1
    for j in range(r):v=v*(a-j)%mod
    return v
def det(rows,mod):
    ans=0
    for perm in itertools.permutations(range(len(rows))):
        term=math.prod(rows[i][perm[i]] for i in range(len(rows)))
        parity=sum(perm[i]>perm[j] for i in range(len(rows)) for j in range(i+1,len(rows)))
        ans=(ans+(-term if parity%2 else term))%mod
    return ans
records=[];mismatches=[]
for p in primes:
    mod=p**3;outmod=p*p;phi=[1];polys=[]
    for k in range(p+3):
        polys.append([fall(k,j,mod)*phi[j]%mod for j in range(k+1)])
        nxt=[0]*(len(phi)+2)
        for j,a in enumerate(phi):
            nxt[j]=(nxt[j]+a)%mod;nxt[j+1]=(nxt[j+1]-a)%mod
            nxt[j+2]=(nxt[j+2]+a*pow(2,-1,mod))%mod
        phi=nxt
    D=[1]
    for j in range(1,2*p+7):D.append((j*D[-1]+1)%mod)
    def E(k,r):return sum(a*fall(2*k-j,r,mod) for j,a in enumerate(polys[k]))%mod
    def divided(v,k):
        if k%p==0:
            assert v%p==0
            return (v//p)*pow(k//p,-1,outmod)%outmod
        return v*pow(k,-1,outmod)%outmod
    for n in range(p):
        high=[[E(n+l,l+j-1)%outmod if l==1 else divided(E(n+l,l+j-1),n+l) for j in range(5)] for l in (1,2,3)]
        prow=[0]+[sum(E(n,r) for r in range(j))%outmod for j in range(1,5)]
        urow=[0]+[sum(divided(E(n+1,r),n+1) for r in range(1,j+1))%outmod for j in range(1,5)]
        sig=-det(high+[[1]*5,urow],outmod)%outmod
        chi=-det(high+[[1]*5,prow],outmod)%outmod
        kap=det(high+[urow,prow],outmod)
        A=sum(a*D[2*n-j] for j,a in enumerate(polys[n]))%outmod
        M=sum(a*D[2*n-j+1] for j,a in enumerate(polys[n]))%outmod
        h=sum(polys[n])%outmod
        u=sum(a*fall(n-j,1,mod) for j,a in enumerate(polys[n]))%outmod
        V=(sig*A-chi*(M+h-u)-kap)%outmod
        factor=12*(2*n+5)
        raw=[sig,chi,kap,V]
        if factor%p==0:
            assert all(v%p==0 for v in raw)
            vals=[v//p*pow(factor//p,-1,p)%p for v in raw]
        else:vals=[v*pow(factor,-1,p)%p for v in raw]
        expected=tables[p][n]
        if vals!=expected:mismatches.append([p,n,vals,expected])
        assert vals[-1]!=0
        records.append({'prime':p,'n':n,'normalized_contractions':vals,
                        'definition_algorithm_raw_mod_p2':raw})
assert not mismatches,mismatches

def log_interval(x,terms=30):
    # 2 atanh(t), positive rational tail bound.
    t=(x-1)/(x+1)
    lower=2*sum(t**(2*j+1)/F(2*j+1) for j in range(terms))
    rem=2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return lower,lower+rem
ln2=log_interval(F(2))
def lnprime(p):
    exp=p.bit_length()-1
    lo,hi=log_interval(F(p,2**exp))
    return exp*ln2[0]+lo,exp*ln2[1]+hi
def coarse_interval(pair,scale=10**12):
    lo,hi=pair
    return F(lo.numerator*scale//lo.denominator,scale),F((hi.numerator*scale+hi.denominator-1)//hi.denominator,scale)
W=[F(0),F(0)]
for p in primes:
    lo,hi=lnprime(p);W[0]+=2*lo/(p-1);W[1]+=2*hi/(p-1)
sqrt_lower=F(1414213562373,10**12);sqrt_upper=F(1414213562374,10**12)
assert sqrt_lower**2<2<sqrt_upper**2
lo=ln2[0]+log_interval((1+sqrt_lower)/2)[0]
hi=ln2[1]+log_interval((1+sqrt_upper)/2)[1]
Wlo,Whi=coarse_interval(W)
Tlo,Thi=coarse_interval((2*lo,2*hi))
gap=Wlo-Thi
assert gap>F(3,10)
report={'status':'second-algorithm finite certificate, normalized transfer still a written dependency',
        'primes':primes,'rows_checked':len(records),'mismatches':mismatches,
        'all_V_units':True,'W_lower':str(Wlo),'W_upper':str(Whi),
        'tau_lower':str(Tlo),'tau_upper':str(Thi),'gap_lower':str(gap),
        'gap_lower_numeric':float(gap),'rows':records}
(OUT/'b4_independent_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
