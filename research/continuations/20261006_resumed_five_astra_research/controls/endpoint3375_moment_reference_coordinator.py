#!/usr/bin/env python3
"""New terminal identity/gcd postprocessing of the retained original3375 producer.
No force, reference or whole-error producer is regenerated.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, gcd
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent
start=time.monotonic()
source=C/'complete_endpoint_3375_certificate.json'
data=json.loads(source.read_text())
n=int(data['n']);m=n+1;N=n+2;nf=factorial(n)
assert n==3375

def rational(x):
    return F(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else F(int(x))
def integer(x):
    q=rational(x) if isinstance(x,dict) else F(x)
    assert q.denominator==1
    return q.numerator
def det(a):
    return sum(a[0][k]*(a[1][(k+1)%3]*a[2][(k+2)%3]-a[1][(k+2)%3]*a[2][(k+1)%3]) for k in range(3))
def adj(a):
    return [[(-1)**(i+j)*det2([[a[r][c] for c in range(3) if c!=i] for r in range(3) if r!=j]) for j in range(3)] for i in range(3)]
def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

states=data['moment_states']
am={k:integer(factorial(k)*rational(states[str(k)]['moment'])) for k in range(n-2,n+3)}
um={k:integer(factorial(k)*rational(states[str(k)]['omega'])) for k in range(n,n+3)}
En=int(data['fixed_exponential_seed'])
tau,tau1,rho,rho1=[rational(data[key]) for key in ('tau_n','tau_n1','rho_n','rho_n1')]
A,B,D=am[n],am[n-1],am[n+1]
X,Y,Z=m*A,m*n*B,2*D-m*A
h=integer(nf*tau);ell=integer(nf*tau1)
h1=integer(F(m,2)*(h+ell))
b0=um[n]-En*h-A
b1=um[n+1]-En*h1-D
Kcal=h*b1-h1*b0-2*nf**3
assert Kcal<0 and nf**3<abs(Kcal)<3*nf**3
Jmat=[[m*N*A,n*m*N*B,n*(n-1)*m*N*am[n-2]],
      [N*D,m*N*A,n*m*N*B],
      [am[n+2],N*D,m*N*A]]
ad=adj(Jmat);detJ=det(Jmat)
assert detJ
for i in range(3):
    for j in range(3):
        assert sum(Jmat[i][k]*ad[k][j] for k in range(3))==(detJ if i==j else 0)
v=[2*N,N,m];w=[0,N,2*n+3]
H=[integer(F(m,2)*(h*v[k]+ell*w[k])) for k in range(3)]
U=[m*N*(um[n]-am[n]),N*(um[n+1]-am[n+1]),um[n+2]-am[n+2]]
Q=[integer(2*nf*factorial(m)*(rho*v[k]+rho1*w[k])) for k in range(3)]
Cv=[U[k]-En*H[k]+Q[k] for k in range(3)]
qboundary=[N,-2*(2*n+3),2*N]
assert dot(qboundary,H)==dot(qboundary,Q)==0
assert dot(qboundary,Cv)==2*m*N*Z

sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
for p in range(2,int(N**0.5)+1):
    if sieve[p]:
        for k in range(p*p,N+1,p):sieve[k]=0
primes=[p for p in range(2,N+1) if sieve[p]]
def largepart(x):
    x=abs(x);assert x
    for p in primes:
        while x%p==0:x//=p
    return x

endpoint_equations=projection_identities=0
results=[]
for endpoint,seed in [(0,[-1,n,-n*m]),(3,[0,0,1])]:
    raw=[sum(seed[k]*ad[k][i] for k in range(3)) for i in range(3)]
    content=gcd(*map(abs,raw));r=[q//content for q in raw]
    assert gcd(*map(abs,r))==1
    alpha,beta,z=dot(r,v),dot(r,w),r[2]
    G=gcd(abs(alpha),abs(beta));R=dot(r,H);Cr=dot(r,Cv)
    Rcal=h*alpha+ell*beta
    assert 2*R==m*Rcal
    I=beta*Kcal+m*h*Z*z
    JJ=-alpha*Kcal+m*ell*Z*z
    if endpoint==3:
        PQF=[(X,Z,Y-X-(2*n+1)*Z),(Y,2*X-Y,N*Y-(3*n+4)*X+N*Z)]
        Pi=n*n+4*n+1
        structural_bound=4*m*m*N*N
    else:
        PQF=[(n*X+Y,n*Z+2*X-Y,2*m*(Y-2*X-(n-1)*Z)),
             (m*Z-(n*n+1)*X-(n-1)*Y,m*Y-(n-1)*X-m*m*Z,2*m*(m*X-N*Y+(n*n+n+1)*Z))]
        Pi=n*n+6*n+4
        structural_bound=4*m*m*N*N*(n+3)
    residuals=[]
    for P0,Q0,F0 in PQF:
        assert P0*alpha+Q0*beta+F0*z==0
        endpoint_equations+=1
        Mr=Q0*h-P0*ell
        Dr=m*Z*Mr-F0*Kcal
        assert alpha*Dr-m*Z*Q0*Rcal-F0*JJ==0
        assert beta*Dr+m*Z*P0*Rcal+F0*I==0
        assert z*Dr-Q0*I+P0*JJ==0
        projection_identities+=3
        residuals.append(Dr)
    structural=gcd(G,abs(Cr))
    assert structural_bound%structural==0
    delta_large=largepart(gcd(abs(R),abs(Cr)))
    assert delta_large==1 and gcd(delta_large,G)==1
    projected=largepart(gcd(abs(R),abs(residuals[0]),abs(residuals[1])))
    # Remove all prime powers supported on G without factoring G.
    while True:
        common=gcd(projected,G)
        if common==1:break
        projected//=common
    assert projected%delta_large==0 and (Pi*delta_large)%projected==0
    Fl=largepart(gcd(abs(PQF[0][2]),abs(PQF[1][2])))
    while True:
        common=gcd(Fl,G)
        if common==1:break
        Fl//=common
    assert Pi%Fl==0
    results.append({'endpoint':endpoint,'primitive_contact_row_content_bits':content.bit_length(),
        'structural_gcd':str(structural),'structural_bound':str(structural_bound),
        'large_projected_actual_gcd':str(delta_large),'normal_coefficient_large_gcd_excluding_G':str(Fl),
        'new_mathfrakD':str(projected),'polynomial_projection_cost':Pi,
        'projected_divisor_check':True,'moment_reference_residual_bit_lengths':[x.bit_length() for x in residuals]})
artifact={'status':'PASS','scope':'NEW four terminal moment-reference identities, twelve integral projection identities and actual projected gcds from the retained complete original3375 artifact',
    'n':n,'source_force_regenerated':False,'complete_exterior_retained':True,'new_endpoint_equations':endpoint_equations,
    'new_integral_projection_identities':projection_identities,'complete_Wronskian_sign':-1,'complete_Wronskian_real_bounds_passed':True,
    'complete_terminal_normal_identity_passed':True,'results':results,'infinite_family_bound_proved':False,
    'irrationality_proved':False,'elapsed_seconds':round(time.monotonic()-start,3),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
out=C/'endpoint3375_moment_reference_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt=dict(artifact);receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint3375_moment_reference_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
