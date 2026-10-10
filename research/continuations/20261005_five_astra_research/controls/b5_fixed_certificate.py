"""Coordinator's fixed 67-row test, two independent algebraic representations."""
import itertools,json,math,resource
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
polys=json.loads((OUT/'b5_symbolic_content_polynomials.json').read_text())
summary=json.loads((OUT/'b5_symbolic_content_summary.json').read_text())
assert summary['common_factor_total_degree']==0
# The sparse integer polynomials are 1152 times the integral seed-valued contractions.
terms=[[(m,Fraction(c)) for m,c in a] for a in polys['quotients']]
def polynomial(a,coords,p):
    return sum(int(c.numerator)*pow(int(c.denominator),-1,p)*math.prod(pow(x,d,p) for x,d in zip(coords,m)) for m,c in a)%p

def advance(n,state,p):
    h,u,v,A,M=state;t=n+1;iv2=pow(2,-1,p)
    return ((-n*h+n*u+v*iv2)%p,t*(h-u+v*iv2)%p,t*(n*h+u-(n+2)*v*iv2)%p,
      (t*M+h-u+v*iv2)%p,(t**3*A+t*(2*n+3)*M+(n*n+3*n+4)*h-(n+3)*u+(n+2)*v)%p)
def fall(n,j,mod):
    value=1
    for a in range(j):value=value*(n-a)%mod
    return value
perms=list(itertools.permutations(range(6)))
signs=[(-1)**sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6)) for perm in perms]
def det(rows,p):return sum(sign*math.prod(rows[i][perm[i]] for i in range(6)) for perm,sign in zip(perms,signs))%p
records=[]
for p in (7,11,13,17,19):
    mod=p*p;phi=[1];Fpolys=[]
    for k in range(p+3):
        Fpolys.append([fall(k,s,mod)*phi[s]%mod for s in range(k+1)])
        nxt=[0]*(len(phi)+2)
        for s,c in enumerate(phi):
            nxt[s]=(nxt[s]+c)%mod;nxt[s+1]=(nxt[s+1]-c)%mod;nxt[s+2]=(nxt[s+2]+c*pow(2,-1,mod))%mod
        phi=nxt
    D=[1]
    for j in range(1,2*p+7):D.append((j*D[-1]+1)%mod)
    def E(k,j):return sum(c*fall(2*k-s,j,mod) for s,c in enumerate(Fpolys[k]))%mod
    def divided(value,k):
        if k%p==0:
            assert value%p==0
            return value//p*pow(k//p,-1,p)%p
        return value*pow(k,-1,p)%p
    def J(vals):return [vals[0]%p]+[(vals[j+1]-vals[j])*pow(math.factorial(j),-1,p)%p for j in range(5)]
    state=(1,0,0,1,2);rows=[]
    for n in range(p):
        h,u,v,A,M=state
        sigma,chi,kappa=[polynomial(a,(n,h,u,v),p)*pow(1152,-1,p)%p for a in terms]
        V=(sigma*A-chi*(M+h-u)-kappa)%p
        F=[E(n+1,j)%p for j in range(6)];G=[E(n+2,j)%p for j in range(6)]
        z=[divided(E(n+2,j+1),n+2) for j in range(6)]
        z2=[divided(E(n+3,j+1),n+3) for j in range(6)]
        high=[J(vals) for vals in (F,z,G,z2)]
        erow=[1]+[0]*5
        prow=[0]+[E(n,j)*pow(math.factorial(j),-1,p)%p for j in range(5)]
        urow=[0]+[divided(E(n+1,j+1),n+1)*pow(math.factorial(j),-1,p)%p for j in range(5)]
        sig2=-det(high+[erow,urow],p)%p;chi2=-det(high+[erow,prow],p)%p;kap2=det(high+[urow,prow],p)
        A2=sum(c*D[2*n-s] for s,c in enumerate(Fpolys[n]))%p
        M2=sum(c*D[2*n-s+1] for s,c in enumerate(Fpolys[n]))%p
        h2=E(n,0)%p;u2=sum(c*fall(n-s,1,mod) for s,c in enumerate(Fpolys[n]))%p
        V2=(sig2*A2-chi2*(M2+h2-u2)-kap2)%p
        left=[sigma,chi,kappa,V];right=[sig2,chi2,kap2,V2]
        assert left==right,(p,n,left,right)
        rows.append({'n':n,'normalized_contractions_and_V':left,'second_algorithm_agrees':True})
        state=advance(n,state,p)
    records.append({'prime':p,'rows':rows,'V_roots':[r['n'] for r in rows if r['normalized_contractions_and_V'][-1]==0],
      'joint_contraction_roots':[r['n'] for r in rows if not any(r['normalized_contractions_and_V'][:3])]})
units=[r['prime'] for r in records if not r['V_roots']]
report={'status':'finite 67-row check; infinite conclusions require normalized transfer and final valuation proof',
 'normalization':'integral replacement basis contractions; sparse 1152 multiple divided only by fixed unit at all selected primes',
 'rows_checked':sum(len(r['rows']) for r in records),'two_independent_algorithms_agree':True,'unit_primes':units,
 'unit_weight_numeric':sum(2*math.log(p)/(p-1) for p in units),'records':records}
(OUT/'b5_fixed_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
brief={k:v for k,v in report.items() if k!='records'};brief['prime_summaries']=[{k:r[k] for k in ('prime','V_roots','joint_contraction_roots')} for r in records]
(OUT/'b5_fixed_certificate_summary.json').write_text(json.dumps(brief,indent=2)+'\n')
print(json.dumps(brief,indent=2))
