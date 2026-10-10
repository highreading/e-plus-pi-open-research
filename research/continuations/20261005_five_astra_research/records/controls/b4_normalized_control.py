"""Independent fixed-size normalized b=4 certificate and targeted lift audit.

Uses scalar recurrences and an integral replacement row, distinct from the
earlier defining-polynomial algorithm. Remote code is not executed.
"""
import json
import math
import resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
prior=json.loads((OUT/'b4_certificate_control.json').read_text())

def determinant(rows,mod):
    # Division-free permutation formula: safe over prime squares.
    import itertools
    value=0
    for perm in itertools.permutations(range(len(rows))):
        parity=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        term=1
        for i,j in enumerate(perm):term=term*rows[i][j]%mod
        value=(value+(-term if parity%2 else term))%mod
    return value

def advance(n,state,mod):
    h,u,v,A,M=state;t=n+1;iv2=pow(2,-1,mod)
    return ((-n*h+n*u+v*iv2)%mod,
            t*(h-u+v*iv2)%mod,
            t*(n*h+u-(n+2)*v*iv2)%mod,
            (t*M+h-u+v*iv2)%mod,
            (t**3*A+t*(2*n+3)*M+(n*n+3*n+4)*h-(n+3)*u+(n+2)*v)%mod)

def fall(n,r):
    v=1
    for j in range(r):v*=n-j
    return v

def normalized(n,state,mod):
    h,u,v,A,M=state;iv2=pow(2,-1,mod);k=n+1
    an=(-n*h+n*u+v*iv2)%mod
    alpha=(h-u+v*iv2)%mod
    beta=(n*h+u-(n+2)*v*iv2)%mod
    jets=[an,k*alpha%mod,k*beta%mod]
    for d in range(4):
        jets.append((-(k+d)*jets[d+2]+2*d*jets[d+1]+2*(k-d)*jets[d])%mod)
    eta=[None,alpha,beta,(2*an-k*beta)%mod]
    for d in range(1,4):
        eta.append((-(k+d)*eta[d+2]+2*d*eta[d+1]+2*(k-d)*eta[d])%mod)
    y=[sum(math.comb(j,a)*fall(k,a)*jets[j-a] for a in range(j+1))%mod for j in range(7)]
    ydiv=[None]+[(eta[j]+sum(math.comb(j,a)*fall(k-1,a-1)*jets[j-a] for a in range(1,j+1)))%mod for j in range(1,5)]
    def yy(j):return y[j] if j>=0 else 0
    z=[(yy(j+2)+(j-k-1)*yy(j+1)+(k+1-2*j)*yy(j)+2*j*yy(j-1))%mod for j in range(5)]
    w=[(-k*yy(j+2)+(j*(1-k)+(k+1)**2)*yy(j+1)+(j*(j-1)+2*k*j-(k+1)*(2*k+1))*yy(j)-2*j*(j+k-1)*yy(j-1)+2*j*(j-1)*yy(j-2))%mod for j in range(5)]
    prevjets=[h,u,v,(-n*v+2*n*h)%mod]
    E=[sum(math.comb(j,a)*fall(n,a)*prevjets[j-a] for a in range(j+1))%mod for j in range(4)]
    def J(row):return [row[0]]+[(row[j+1]-row[j])*pow(math.factorial(j),-1,mod)%mod for j in range(4)]
    high=[J(y),J(z),J(w)]
    e=[1,0,0,0,0]
    U=[0]+[ydiv[j+1]*pow(math.factorial(j),-1,mod)%mod for j in range(4)]
    P=[0]+[E[j]*pow(math.factorial(j),-1,mod)%mod for j in range(4)]
    sig=-determinant(high+[e,U],mod)%mod
    chi=-determinant(high+[e,P],mod)%mod
    kap=determinant(high+[U,P],mod)
    V=(sig*A-chi*(M+h-u)-kap)%mod
    return [sig,chi,kap,V]

old_records={a['prime']:a for a in prior['rows']}
target_records=[];comparison_errors=[]
for p,old in old_records.items():
    mod=p*p
    wanted={r+p*j for r in old['V_zeros'] for j in range(p)}
    state=(1,0,0,1,2);target=[];full=[]
    for n in range(max(wanted)+1):
        if n in wanted or n<p:
            vals=normalized(n,state,mod)
            if n in wanted:target.append({'n':n,'values_mod_p2':vals})
            if n<p:
                full.append({'n':n,'values_mod_p':[v%p for v in vals]})
                original=old['rows'][n]['contractions']
                factor=12*(2*n+5)%p
                if [(factor*v)%p for v in vals]!=original:comparison_errors.append([p,n])
        state=advance(n,state,mod)
    rootsets={r:[a['n'] for a in target if a['n']%p==r and a['values_mod_p2'][-1]==0] for r in old['V_zeros']}
    target_records.append({'prime':p,'normalized_mod_p':full,
        'joint_roots_mod_p':[a['n'] for a in full if not any(a['values_mod_p'][:3])],
        'V_roots_mod_p':[a['n'] for a in full if a['values_mod_p'][-1]==0],
        'targeted_rows':target,'surviving_root_lifts':rootsets})
assert not comparison_errors,comparison_errors
assert sum(len(a['targeted_rows']) for a in target_records)==1034
seven=next(a for a in target_records if a['prime']==7)
assert next(a['values_mod_p2'] for a in seven['targeted_rows'] if a['n']==4)==[41,20,48,21]
assert next(a['values_mod_p2'] for a in seven['targeted_rows'] if a['n']==1)==[(-360)%49,1128%49,888%49,(-13248)%49]

# A small, fixed extension is justified by the newly proved normalization:
# the earlier raw test could not see any prime unit because of 2n+5.
extension=[5,11,13,17,23,29,37,41,43,47,53,59,67,79,89,97,103,107,109,113,127,131]
extension_records=[]
for p in extension:
    state=(1,0,0,1,2);rows=[]
    for n in range(p):
        vals=normalized(n,state,p)
        rows.append({'n':n,'values_mod_p':vals})
        state=advance(n,state,p)
    extension_records.append({'prime':p,'rows':rows,
        'joint_roots_mod_p':[a['n'] for a in rows if not any(a['values_mod_p'][:3])],
        'V_roots_mod_p':[a['n'] for a in rows if a['values_mod_p'][-1]==0]})
unit_primes=[a['prime'] for a in target_records+extension_records if not a['V_roots_mod_p']]
report={'status':'finite exact arithmetic; infinite use needs reviewed normalized transfer',
        'targeted_row_count':1034,'old_raw_comparison_errors':comparison_errors,
        'unit_primes':sorted(unit_primes),
        'unit_weight_numeric':sum(2*math.log(p)/(p-1) for p in unit_primes),
        'targeted':target_records,'extension':extension_records}
(OUT/'b4_normalized_control.json').write_text(json.dumps(report,indent=2)+'\n')
brief={k:v for k,v in report.items() if k not in ('targeted','extension')}
brief['root_summary']=[{k:a[k] for k in ('prime','joint_roots_mod_p','V_roots_mod_p','surviving_root_lifts')} for a in target_records]
brief['extension_summary']=[{k:a[k] for k in ('prime','joint_roots_mod_p','V_roots_mod_p')} for a in extension_records]
(OUT/'b4_normalized_summary.json').write_text(json.dumps(brief,indent=2)+'\n')
print(json.dumps(brief,indent=2))
