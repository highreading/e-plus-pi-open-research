"""Second algorithm: direct polynomial coefficients, without state recurrence."""
import itertools
import json
import math
import resource
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
source=json.loads((OUT/'b3_control.json').read_text())
primes=[7,19,31,61,71,73,83,101]


def falling(a,k,mod):
    value=1
    for j in range(k):value=value*(a-j)%mod
    return value


def determinant(rows,p):
    value=0
    for perm in itertools.permutations(range(4)):
        term=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        for i in range(4):term=term*rows[i][perm[i]]%p
        value=(value+term)%p
    return value


audits=[]
for p in primes:
    mod=p*p
    phi=[1]
    coefficients=[]
    # H_k = sum_s (k)_s [z^s]phi(z)^k x^(k-s).
    for k in range(p+2):
        coefficients.append([(falling(k,j,mod)*phi[j])%mod for j in range(k+1)])
        nxt=[0]*(len(phi)+2)
        for j,a in enumerate(phi):
            nxt[j]=(nxt[j]+a)%mod
            nxt[j+1]=(nxt[j+1]-a)%mod
            nxt[j+2]=(nxt[j+2]+a*pow(2,-1,mod))%mod
        phi=nxt
    D=[1]
    for k in range(1,2*p+6):D.append((k*D[-1]+1)%mod)
    def Hder(k,d):
        return sum(a*falling(k-j,d,mod) for j,a in enumerate(coefficients[k]))%mod
    def E(k,d):
        return sum(a*falling(2*k-j,d,mod) for j,a in enumerate(coefficients[k]))%mod
    def exact_division_residue(value,k):
        if k%p==0:
            assert value%p==0
            return (value//p)*pow(k//p,-1,p)%p
        return value*pow(k,-1,p)%p
    expected=next(r for r in source['rows'] if r['prime']==p)['seeds']
    mismatches=[]
    rows=[]
    for n in range(p):
        state=[Hder(n,d)%p for d in range(3)]
        state += [sum(a*D[2*n-j+t] for j,a in enumerate(coefficients[n]))%p for t in (0,1)]
        raw=[E(n+1,d)%p for d in range(4)]
        raw2=[exact_division_residue(E(n+2,d),n+2) for d in range(1,5)]
        prow=[0]+[sum(E(n,d) for d in range(j))%p for j in range(1,4)]
        urow=[0]+[sum(exact_division_residue(E(n+1,d),n+1) for d in range(1,j+1))%p for j in range(1,4)]
        e=[1]*4
        sigma=-determinant([raw,raw2,e,urow],p)%p
        chi=-determinant([raw,raw2,e,prow],p)%p
        kappa=determinant([raw,raw2,urow,prow],p)
        V=(sigma*state[3]-chi*(state[4]+state[0]-state[1])-kappa)%p
        actual={'r':n,'state':state,'contractions':[sigma,chi,kappa,V]}
        if actual!=expected[n]:mismatches.append({'r':n,'actual':actual,'expected':expected[n]})
        rows.append(actual)
    assert not mismatches,(p,mismatches)
    zeros=[r['r'] for r in rows if r['contractions'][-1]==0]
    assert not zeros,(p,zeros)
    audits.append({'prime':p,'rows_checked':p,'mismatches':mismatches,'V_zero_set':zeros,'algorithm':'direct defining polynomials modulo p^2, exact integer division before mod p'})


def log_bounds(q):
    q=F(q);power=0
    while q>=2:q/=2;power+=1
    def core(a):
        y=(a-1)/(a+1)
        lo=2*sum(y**(2*j+1)/F(2*j+1) for j in range(25))
        return lo,lo+2*y**51/(51*(1-y*y))
    lo,hi=core(q);l2,h2=core(F(2))
    return lo+power*l2,hi+power*h2

Wlo=Whi=F(0)
for p in primes:
    a,b=log_bounds(p);Wlo+=2*a/F(p-1);Whi+=2*b/F(p-1)
scale=10**12;rt=math.isqrt(2*scale*scale)
taulo=2*log_bounds(1+F(rt,scale))[0]
tauhi=2*log_bounds(1+F(rt+1,scale))[1]
assert Wlo>tauhi
lo=lambda a:F((a*scale).numerator//(a*scale).denominator,scale)
hi=lambda a:F(-((-(a*scale).numerator)//(a*scale).denominator),scale)
report={'status':'PASS','rows_checked':sum(primes),'prime_audits':audits,
        'rational_bounds':{'W8_lower':str(lo(Wlo)),'W8_upper':str(hi(Whi)),
                           'tau_lower':str(lo(taulo)),'tau_upper':str(hi(tauhi)),
                           'gap_lower':str(lo(Wlo-tauhi))},
        'W8_numeric':float(Wlo),'gap_lower_numeric':float(Wlo-tauhi),
        'certificate_scope':'All-index exclusion requires the transfer proof, complete endpoint normalization and inherited fixed-b whole-error theorem.'}
(OUT/'b3_certificate_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='prime_audits'},indent=2))
