"""Parent-authored exact N8 normalization of the new quadratic ansatz."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb, gcd, lcm
import json, hashlib

OUT=Path(__file__).resolve().parent
N=8

def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def scale(a,c):return [v*c for v in a]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def eval_i(poly):
    a=sum(v*((-1)**(j//2)) for j,v in enumerate(poly) if j%2==0)
    b=sum(v*((-1)**(j//2)) for j,v in enumerate(poly) if j%2)
    return a,b
def egcd(a,b):
    old,r=abs(a),abs(b);x,xx=1,0;y,yy=0,1
    while r:
        q=old//r;old,r=r,old-q*r;x,xx=xx,x-q*xx;y,yy=yy,y-q*yy
    return old,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)
def content_bezout(poly):
    g=0;w=[]
    for x in poly:
        g,u,v=egcd(g,x);w=[u*z for z in w]+[v]
    assert sum(w[i]*poly[i] for i in range(len(poly)))==g
    return g,w

a=[1]
for j in range(1,2*N+1):a.append(1-j*a[-1])
def eta(poly):return sum(x*a[j] for j,x in enumerate(poly))
def integral(poly):return sum((Q(x,j+1) for j,x in enumerate(poly)),Q(0))

basis=[]
fac=factorial(N)
for j in range(N+1):
    coeff=[]
    for d in range(j+1):
        value=sum((Q(fac*((-1)**(r+d))*comb(j,r)*comb(r,d),factorial(r)) for r in range(d,j+1)),Q(0))
        assert value.denominator==1;coeff.append(int(value))
    basis.append(coeff)
B=fac*fac
assert all(eta(mul(basis[j],basis[k]))==(B if j==k else 0) for j in range(N+1) for k in range(N+1))
values=[eval_i(p) for p in basis]
alpha=[v[0] for v in values];beta=[v[1] for v in values]
U=sum(v*v for v in alpha);V=sum(x*y for x,y in zip(alpha,beta));W=sum(v*v for v in beta)
Delta=U*W-V*V;D=Delta-B*W
assert Delta>0 and D>0 and Q(B*W,Delta)<=Q(2,3)
AA=[0];BB=[0]
for j in range(N+1):AA=add(AA,scale(basis[j],alpha[j]));BB=add(BB,scale(basis[j],beta[j]))
Phi=add(scale(AA,W),scale(BB,-V))
assert eval_i(Phi)==(Delta,0)
assert eta(mul(Phi,Phi))==B*W*Delta
g=mul([1,0,1],[((-1)**j)*comb(N-2,j) for j in range(N-1)])
assert eval_i(g)==(0,0)
T=factorial(2*N)-4*factorial(2*N-1)+8*factorial(2*N-2)-8*factorial(2*N-3)+4*factorial(2*N-4)
assert T>0 and eta(mul(g,g))==T
raw=add(scale(mul(Phi,Phi),T),scale(mul(g,g),D*Delta))
Z=T*Delta*Delta
assert eta(raw)==Z and eval_i(raw)==(Z,0)
h,h_witness=content_bezout(raw);assert h>0 and Z%h==0
poly=[x//h for x in raw];M=Z//h
assert gcd(*poly)==1 and eta(poly)==M and eval_i(poly)==(M,0)
assert all(h*poly[i]==raw[i] for i in range(len(poly)))

remainder=poly[:];remainder[0]-=M
S=[0]*(len(poly)-2)
for j in range(len(remainder)-1,1,-1):
    z=remainder[j];S[j-2]=z;remainder[j]-=z;remainder[j-2]-=z
assert all(x==0 for x in remainder)
assert add([M],mul([1,0,1],S))==poly
end=sum(x*((-1)**d)*factorial(d) for d,x in enumerate(poly))
Lentry=lcm(*( (j+1)//gcd(j+1,4*x) for j,x in enumerate(S)))
arc_integer=sum(4*x*(Lentry//(j+1)) if Lentry%(j+1)==0 else int(Q(4*x*Lentry,j+1)) for j,x in enumerate(S))
assert Q(arc_integer,Lentry)==4*integral(S)
darc=gcd(Lentry,arc_integer);lam=Lentry//darc
A=lam*end-arc_integer//darc
assert Q(A,lam)==end-4*integral(S) and gcd(lam,A)==1
G,x,y=egcd(lam*M,A)
assert x*lam*M+y*A==G and G==gcd(M,A) and gcd(G,lam)==1
p,q=A//G,lam*M//G
assert q>0 and gcd(abs(p),q)==1
J=integral(poly)/M
assert J>0
dphi=gcd(*Phi)
assert h%gcd(T*dphi*dphi,D*Delta)==0
assert T*gcd(Delta*Delta,sum(Phi)**2)%h==0
Bg=Q(1,2*N-3)+Q(4,(2*N-3)*(2*N-2)*(2*N-1))+Q(24,(2*N-3)*(2*N-2)*(2*N-1)*(2*N)*(2*N+1))
assert integral(mul(g,g))==Bg
assert J==integral(mul(Phi,Phi))/Delta**2+Q(D,Delta*T)*Bg
endpoint=[]
for prime in (11,13):
    residue=S[prime-1]%prime
    temp=lam;depth=0
    while temp%prime==0:temp//=prime;depth+=1
    assert depth==(1 if residue else 0)
    endpoint.append({'prime':prime,'post_content_s_pminus1_residue':residue,'lambda_valuation':depth})

out={'parent_authored':True,'all_checks_passed':True,'network_or_credentials_used':False,
     'scope':'Only full-degree two-square N8 auxiliary normalization; no uniform or original-index inference.',
     'N':N,'max_degree':2*N,'max_factorial':2*N,'quotient_degree':2*N-2,
     'basis_polynomials':basis,'gaussian_integer_evaluations':values,
     'U':U,'V':V,'W':W,'Delta':Delta,'D':D,'T':T,'Phi_coefficients':Phi,'g_coefficients':g,
     'raw_W_coefficients':raw,'raw_Z':Z,'actual_polynomial_content':h,
     'polynomial_content_bezout_witness':h_witness,'primitive_W_coefficients':poly,'M':M,
     'S_coefficients':S,'B_endpoint':end,'entry_clearer':Lentry,'arc_integer':arc_integer,
     'arc_cancellation':darc,'actual_lambda':lam,'A':A,'actual_final_gcd':G,
     'final_gcd_bezout_witness':[x,y],'primitive_p':p,'primitive_q':q,'qJ':str(q*J),
     'q_over_13T':str(Q(q,(2*N-3)*T)),'whole_error_interval_by_qJ':[str(3*q*J),str(7*q*J)],
     'source_eta_identity_verified':True,'source_i_identity_verified':True,
     'orthogonality_verified_for_all_81_pairs':True,'content_divisibilities_verified':True,
     'post_content_endpoint_residues':endpoint,
     'source_report_sha256':hashlib.sha256((OUT.parent/'responses/A3_turn0.md').read_bytes()).hexdigest()}
(OUT/'full_degree_two_square_n8_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['all_checks_passed','scope','actual_polynomial_content','M','actual_lambda','actual_final_gcd','primitive_q','qJ','q_over_13T','post_content_endpoint_residues']},indent=2))
