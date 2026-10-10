#!/usr/bin/env python3
"""NEW canonical shared scalar and clipped product-certificate arithmetic.
Only new scalar fields are computed from the retained complete producer.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial,gcd
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent
start=time.monotonic()
source=C/'complete_endpoint_3375_certificate.json'
data=json.loads(source.read_text())
n=int(data['n']);assert n==3375
m,N=n+1,n+2
nf=factorial(n)
def rat(x):return Fraction(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else Fraction(int(x))
def integer(x):
    x=Fraction(x);assert x.denominator==1
    return x.numerator
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3)]
state=data['moment_states']
am={k:integer(factorial(k)*rat(state[str(k)]['moment'])) for k in range(n-2,n+3)}
um={k:integer(factorial(k)*rat(state[str(k)]['omega'])) for k in range(n,n+2)}
tau,tau1=rat(data['tau_n']),rat(data['tau_n1'])
h,ell=integer(nf*tau),integer(nf*tau1)
h1=integer(Fraction(m,2)*(h+ell))
En=int(data['fixed_exponential_seed'])
b0,b1=um[n]-En*h-am[n],um[n+1]-En*h1-am[n+1]
Kcal=h*b1-h1*b0-2*nf**3
X,Y,Z=m*am[n],m*n*am[n-1],2*am[n+1]-m*am[n]
P,Q,F=n*X+Y,n*Z+2*X-Y,2*m*(Y-2*X-(n-1)*Z)
DL=m*Z*(Q*h-P*ell)-F*Kcal
Lref=1<<(m//2)
Theta,remainder=divmod(Lref*DL,nf)
assert remainder==0 and Theta and nf*Theta==Lref*DL

J=[[m*N*am[n],n*m*N*am[n-1],n*(n-1)*m*N*am[n-2]],
   [N*am[n+1],m*N*am[n],n*m*N*am[n-1]],
   [am[n+2],N*am[n+1],m*N*am[n]]]
columns=[[J[i][j] for i in range(3)] for j in range(3)]
adj=[cross(columns[1],columns[2]),cross(columns[2],columns[0]),cross(columns[0],columns[1])]
raw=[[sum(seed[k]*adj[k][i] for k in range(3)) for i in range(3)]
     for seed in ([-1,n,-n*m],[0,0,1])]
rows=[[x//gcd(*map(abs,row)) for x in row] for row in raw]
sigma=gcd(*map(abs,cross(*rows)))

sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
for p in range(2,int(N**.5)+1):
    if sieve[p]:
        for j in range(p*p,N+1,p):sieve[j]=0
primes=[p for p in range(2,N+1) if sieve[p]]
def strip_small(x,record=False):
    x=abs(x);exponents=[]
    for p in primes:
        e=0
        while x%p==0:x//=p;e+=1
        if e and record:exponents.append([p,e])
    return x,exponents
Dlarge,factors=strip_small(Theta,True)
Sigma,_=strip_small(sigma)
U=abs(Theta)//Dlarge
assert U*Dlarge==abs(Theta)
joint=json.loads((C/'endpoint3375_joint_saturation_receipt.json').read_text())
assert joint['input_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
assert joint['actual_boundary_gcd_large']=='1'
assert Sigma.bit_length()==joint['large_contact_saturation_bits']
clipped=gcd(Sigma,Dlarge)
W=Dlarge*clipped
exclusive=Dlarge//clipped
artifact={'status':'PASS','scope':'NEW exact canonicalTheta, complete small-prime part and clipped product-certificate fields at original3375',
    'n':n,'producer_regenerated':False,'old_endpoint_gcd_regenerated':False,
    'old_denominator_or_whole_error_regenerated':False,
    'Theta':str(Theta),'shared_DL':str(DL),'D_large':str(Dlarge),'smooth_U':str(U),
    'Sigma_large':str(Sigma),'clipped_collision_gcd':str(clipped),
    'product_certificate_W':str(W),'exclusive_upper_divisor':str(exclusive),
    'Theta_integer_identity_passed':True,'Theta_sign':-1 if Theta<0 else 1,
    'canonical_small_prime_exponents':factors,
    'Theta_bits':abs(Theta).bit_length(),'D_large_bits':Dlarge.bit_length(),
    'smooth_U_bits':U.bit_length(),'Sigma_large_bits':Sigma.bit_length(),
    'clipped_collision_bits':clipped.bit_length(),'product_certificate_bits':W.bit_length(),
    'exclusive_upper_divisor_bits':exclusive.bit_length(),
    'n_factorial_bits':nf.bit_length(),'canonical_smooth_factor_is_multiple_of_factorial_cubed':U%(nf**3)==0,
    'actual_delta_large_values_reused':[1,1],
    'infinite_smoothness_bound_proved':False,'irrationality_proved':False,
    'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'report_sha256':hashlib.sha256((C.parent/'responses/A3_turn9.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'endpoint3375_product_scalar_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
large_fields=('Theta','shared_DL','D_large','smooth_U','Sigma_large','clipped_collision_gcd','product_certificate_W','exclusive_upper_divisor')
receipt={k:v for k,v in artifact.items() if k not in large_fields}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint3375_product_scalar_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
