"""Bounded exact rational evaluation of the proposed high-sector reduction.

Personally authored; no network, subprocess, credential access, or remote code.
Agreement of two inverses does not itself audit the source continuation theorem.
"""
from fractions import Fraction
from math import comb,factorial
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
H=-95;N=-190;M=190
fac=[factorial(i) for i in range(762)]

def choose(a,s):
    if s<0:return 0
    if a>=0:return comb(a,s) if s<=a else 0
    return (-1)**s*comb(-a+s-1,s)

def vp(a,p):
    if a==0:return None
    v=0;a=abs(a)
    while a%p==0:a//=p;v+=1
    return v

def record(x):
    x=Fraction(x)
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),
            'v2':None if x==0 else vp(x.numerator,2)-vp(x.denominator,2)}

central={};central_summands=0
for ell in range(190,381):
    j=ell//2
    if ell%2==0:
        prefactor=1
        for t in range(1,j+1):prefactor*=2*H+2*t-1
        for t in range(j):prefactor*=H-t
        total=sum((Fraction((1<<s)*fac[s]**2,fac[2*s])*choose(H-j,s)*choose(H+j,s)
                   for s in range(j-95+1)),Fraction())
    else:
        prefactor=1
        for t in range(j+1):prefactor*=2*H+2*t+1
        for t in range(j+1):prefactor*=H-t
        total=sum((Fraction((1<<s)*fac[s]**2,fac[2*s+1])*choose(H-j-1,s)*choose(H+j,s)
                   for s in range(j-95+1)),Fraction())
    central_summands+=j-95+1
    central[ell]=prefactor*total
assert central_summands==9216
force=[]
for i in range(190,381):
    value=sum((comb(i,ell)*(fac[i-190]//fac[ell-190])*central[ell]
               for ell in range(190,i+1)),Fraction())
    force.append(value)
g=[(-1)**m*force[m] for m in range(M+1)]

# Direct ordinary polynomial multiplication: (2+2t+t^2)^190 / 2^190.
poly=[1]
for _ in range(190):
    out=[0]*(min(len(poly)+2,M+1))
    for i,x in enumerate(poly):
        for shift,c in ((0,2),(1,2),(2,1)):
            if i+shift<len(out):out[i+shift]+=c*x
    poly=out
a=[Fraction(x,1<<190) for x in poly]
convolution=[fac[m]*sum((a[m-j]*g[j]/fac[j] for j in range(m+1)),Fraction()) for m in range(M+1)]

# Independent inverse via q(z)*phi'(z)=H*q'(z)*phi(z).
# q(z)=1-2z+2z^2-z^3+z^4/4; phi=q^H.
qdp=[0,-2,4,-6,6];lam=[1]
for t in range(M):
    value=0
    for i in range(1,min(4,t+1)+1):
        value+=qdp[i]*(H*comb(t,i-1)-(comb(t,i) if i<=t else 0))*lam[t-i+1]
    lam.append(value)
triangular=[]
for m in range(M+1):
    p=g[m]-sum(((-1)**s*lam[s]*comb(m,s)*triangular[m-s] for s in range(1,m+1)),Fraction())
    triangular.append(p)
assert triangular==convolution
assert all(triangular[m]+sum(((-1)**s*lam[s]*comb(m,s)*triangular[m-s]
                             for s in range(1,m+1)),Fraction())==g[m] for m in range(M+1))
Z=triangular[M]
assert all(triangular[m]==triangular[0]*(fac[189]//fac[189-m]) for m in range(190))
assert triangular[190]==0
result={'status':'PASS','scope':'Exact finite high-sector arithmetic conditional on the independently audited continuation/contact/force identity; not an e+pi proof or full scalar residual',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'h':H,'n':N,'b':'-95/2001','target':380,'central_indices':[190,380],
        'central_summands':central_summands,'crosschecked_coefficients':M+1,'exact_inverse_residuals':M+1,
        'Z':record(Z),'zero_limit':Z==0,'central':{str(k):record(v) for k,v in central.items()},
        'force':{str(190+i):record(v) for i,v in enumerate(force)},
        'solution':{str(190+i):record(v) for i,v in enumerate(triangular)},
        'polynomial_coefficients':[record(v) for v in a],
        'symbol_coefficients':[str(v) for v in lam]}
(ROOT/'binary_limit_rational_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
receipt={k:result[k] for k in ('status','source_sha256','h','n','b','target','central_summands','crosschecked_coefficients','exact_inverse_residuals','Z','zero_limit')}
receipt.update({'artifact_sha256':hashlib.sha256((ROOT/'binary_limit_rational_certificate.json').read_bytes()).hexdigest(),
                'exact_additional_law_verified':'p_(190+m)=B190*(189)_falling_m for0<=m<=189; p380=0',
                'scope':result['scope']})
(ROOT/'binary_limit_rational_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','zero_limit','Z','central_summands','crosschecked_coefficients')}))
