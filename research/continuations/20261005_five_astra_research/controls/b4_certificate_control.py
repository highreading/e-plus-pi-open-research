"""Bounded new (n,4,n) residue certificate, using defining polynomials."""
import json
import math
import resource
from pathlib import Path
import sympy as sy

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
primes=[7,19,31,61,71,73,83,101]
x,z=sy.symbols('x z')


def H(k):
    phi=sy.Poly((1-z+z*z/2)**k,z)
    return sum(math.factorial(k)//math.factorial(k-j)*phi.nth(j)*x**(k-j) for j in range(k+1))

def E(k,r):return sy.diff(x**k*H(k),x,r).subs(x,1)
rows0=[[E(l,l+j-1)/(l if l>=2 else 1) for j in range(5)] for l in (1,2,3)]
p0=[0,1,1,1,1];u0=[0,1,3,3,3];e0=[1]*5
sig0=-sy.Matrix(rows0+[e0,u0]).det()
chi0=-sy.Matrix(rows0+[e0,p0]).det()
kap0=sy.Matrix(rows0+[u0,p0]).det()
V0=sig0-3*chi0-kap0
assert (sig0,chi0,kap0,V0)==(960,-3360,-480,11520)


def fall(a,r,mod):
    v=1
    for j in range(r):v=v*(a-j)%mod
    return v

def determinant(rows,p):
    a=[r[:] for r in rows];value=1
    for j in range(len(a)):
        pivot=next((i for i in range(j,len(a)) if a[i][j]%p),None)
        if pivot is None:return 0
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];value=-value
        entry=a[j][j]%p;value=value*entry%p
        inv=pow(entry,-1,p)
        for i in range(j+1,len(a)):
            f=a[i][j]*inv%p
            for k in range(j+1,len(a)):a[i][k]=(a[i][k]-f*a[j][k])%p
    return value%p

records=[]
for p in primes:
    mod=p*p;phi=[1];coeff=[]
    for k in range(p+3):
        coeff.append([fall(k,j,mod)*phi[j]%mod for j in range(k+1)])
        nxt=[0]*(len(phi)+2)
        for j,a in enumerate(phi):
            nxt[j]=(nxt[j]+a)%mod;nxt[j+1]=(nxt[j+1]-a)%mod
            nxt[j+2]=(nxt[j+2]+a*pow(2,-1,mod))%mod
        phi=nxt
    D=[1]
    for j in range(1,2*p+7):D.append((j*D[-1]+1)%mod)
    def Ed(k,r):return sum(a*fall(2*k-j,r,mod) for j,a in enumerate(coeff[k]))%mod
    def div(v,k):
        if k%p==0:
            assert v%p==0
            return v//p*pow(k//p,-1,p)%p
        return v*pow(k,-1,p)%p
    rows=[]
    for n in range(p):
        high=[[Ed(n+l,l+j-1)%p if l==1 else div(Ed(n+l,l+j-1),n+l) for j in range(5)] for l in (1,2,3)]
        prow=[0]+[sum(Ed(n,r) for r in range(j))%p for j in range(1,5)]
        urow=[0]+[sum(div(Ed(n+1,r),n+1) for r in range(1,j+1))%p for j in range(1,5)]
        A=sum(a*D[2*n-j] for j,a in enumerate(coeff[n]))%p
        M=sum(a*D[2*n-j+1] for j,a in enumerate(coeff[n]))%p
        h=sum(coeff[n])%p
        hd=sum(a*fall(n-j,1,mod) for j,a in enumerate(coeff[n]))%p
        sig=-determinant(high+[[1]*5,urow],p)%p
        chi=-determinant(high+[[1]*5,prow],p)%p
        kap=determinant(high+[urow,prow],p)
        V=(sig*A-chi*(M+h-hd)-kap)%p
        rows.append({'r':n,'contractions':[sig,chi,kap,V]})
    records.append({'prime':p,'V_zeros':[r['r'] for r in rows if r['contractions'][-1]==0],
                    'joint_contraction_zeros':[r['r'] for r in rows if not any(r['contractions'][:3])],
                    'rows':rows})
units=[r['prime'] for r in records if not r['V_zeros']]
report={'b':4,'rows_checked':sum(primes),'exact_seed':[int(a) for a in (sig0,chi0,kap0,V0)],
        'unit_primes':units,'unit_weight_numeric':sum(2*math.log(p)/(p-1) for p in units),
        'rows':records,'status':'finite evidence; requires all-index transfer and complete quotient'}
(OUT/'b4_certificate_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
print(json.dumps({r['prime']:{'V_zeros':r['V_zeros'],'joint_zeros':r['joint_contraction_zeros']} for r in records}))
