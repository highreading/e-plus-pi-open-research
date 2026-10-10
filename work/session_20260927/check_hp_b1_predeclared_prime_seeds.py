"""Closed residue list p=5,7,11,13,17,19. Scalar seeds, no HP degree solve."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

PRIMES=(5,7,11,13,17,19)
HERE=Path(__file__).resolve().parent

def product(a,b,modulus=None):
    c=[0]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    if modulus:c=[x%modulus for x in c]
    return c

def local_modular(n,p):
    a=[1]
    for _ in range(n):a=product(a,[1,-1,pow(2,-1,p)],p)
    b=product(a,[1,-1,pow(2,-1,p)],p)
    d=[1]
    for j in range(1,2*n+2):d.append((j*d[-1]+1)%p)
    ff=[1]
    for j in range(1,n+1):ff.append(ff[-1]*(n-j+1)%p)
    H=sum(ff[s]*a[s] for s in range(n+1))%p
    A=sum(ff[s]*a[s]*d[2*n-s] for s in range(n+1))%p
    K=(2+sum(ff[s-1]*(2*n+2-s)*b[s] for s in range(1,n+2)))%p
    B=(2*d[2*n+1]+sum(ff[s-1]*(2*n+2-s)*b[s]*d[2*n+1-s]
                        for s in range(1,n+2)))%p
    return H,K,A,B,(K*A-H*B)%p

def direct_rational(n):
    # A distinct route: integer Legendre recurrence and factorial functionals.
    polys=[[F(1)],[F(-2),F(4)]]
    for k in range(2,n+2):
        v=product(polys[-1],[-2*(2*k-1),4*(2*k-1)])
        for j,x in enumerate(polys[-2]):v[j]+=4*(k-1)*x
        polys.append([x/k for x in v])
    e=[F(1)]
    for d in range(1,2*n+2):e.append(e[-1]+F(1,factorial(d)))
    R=[]; T=[]
    for k in (n,n+1):
        R.append(sum((v/factorial(n+j) for j,v in enumerate(polys[k])),F(0)))
        T.append(sum((v*e[n+j] for j,v in enumerate(polys[k])),F(0)))
    f=F(factorial(n)**2,2**n)
    H,A=f*R[0],f*T[0]
    K,B=f*F(n+1,2)*R[1],f*F(n+1,2)*T[1]
    return H,K,A,B,K*A-H*B

def mod(x,p):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,p)%p

out=[]
for p in PRIMES:
    rows=[]
    for r in range(p):
        local=local_modular(r,p)
        independent=tuple(mod(x,p) for x in direct_rational(r))
        assert local==independent,(p,r,local,independent)
        rows.append(dict(r=r,H=local[0],K=local[1],A=local[2],B=local[3],C=local[4],
                         independent_factorial_functional_matches=True))
    zeros=[x['r'] for x in rows if x['C']==0]
    out.append(dict(p=p,zero_residues=zeros,only_forced_root=(zeros==[1]),rows=rows))
result=dict(scope="Closed predeclared prime list; complete scalar residues, no canonical HP solve.",
            all_checks_pass=True,primes=list(PRIMES),results=out,
            uniform_candidates=[x['p'] for x in out if x['only_forced_root']],
            warning="All-index claims on r=1 additionally require the independently proved root-disk lift.")
(HERE/'hp_b1_predeclared_prime_seed_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))
print([(x['p'],x['zero_residues']) for x in out])
