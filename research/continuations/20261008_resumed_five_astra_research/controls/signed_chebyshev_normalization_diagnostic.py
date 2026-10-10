"""Coordinator-authored bounded diagnostic for a distinct signed-source ansatz."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,gcd
import json,hashlib
OUT=Path(__file__).resolve().parent
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def scale(a,c):return [x*c for x in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def eval_i(a):return (sum(x*(-1)**(j//2) for j,x in enumerate(a) if j%2==0),sum(x*(-1)**(j//2) for j,x in enumerate(a) if j%2))
def egcd(a,b):
    g,r=abs(a),abs(b);x,xx=1,0;y,yy=0,1
    while r:
        d=g//r;g,r=r,g-d*r;x,xx=xx,x-d*xx;y,yy=yy,y-d*yy
    return g,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)
def content(a):
    g=0;w=[]
    for x in a:
        g,u,v=egcd(g,x);w=[u*z for z in w]+[v]
    assert sum(x*y for x,y in zip(a,w))==g
    return g,w
def val(a,p):
    if a==0:return None
    a=abs(a);v=0
    while a%p==0:a//=p;v+=1
    return v
def integral(a):return sum((Q(x,j+1) for j,x in enumerate(a)),Q(0))
cs=[[1],[-1,2]]
for n in range(1,12):cs.append(add(mul([-2,4],cs[-1]),scale(cs[-2],-1)))
records=[]
for N in range(3,13):
    moments=[1]
    for j in range(1,2*N+1):moments.append(1-j*moments[-1])
    def eta(a):return sum(x*moments[j] for j,x in enumerate(a))
    an,bn=eval_i(cs[N]);am,bm=eval_i(cs[N-1])
    d=an*bm-am*bn
    assert d!=0
    B=add(scale(cs[N],bm),scale(cs[N-1],-bn))
    assert eval_i(B)==(d,0)
    I=eta(mul(B,B));assert I>d*d
    K=mul(mul([0,1,-1],mul([1,0,1],[1,0,1])),mul(cs[N-3],cs[N-3]))
    assert len(K)==2*N+1 and eval_i(K)==(0,0)
    U=-eta(K);assert U>0
    raw=add(scale(mul(B,B),U),scale(K,I-d*d));Z=U*d*d
    assert eta(raw)==Z and eval_i(raw)==(Z,0)
    h,hbez=content(raw);assert h>0 and Z%h==0
    F=[x//h for x in raw];M=Z//h
    assert gcd(*F)==1 and eta(F)==M and eval_i(F)==(M,0)
    rem=F[:];rem[0]-=M;S=[0]*(len(F)-2)
    for j in range(len(rem)-1,1,-1):
        z=rem[j];S[j-2]=z;rem[j]-=z;rem[j-2]-=z
    assert all(x==0 for x in rem) and add([M],mul([1,0,1],S))==F
    end=sum(x*(-1)**j*factorial(j) for j,x in enumerate(F))
    arc=4*integral(S);lam=arc.denominator;A=lam*end-arc.numerator
    assert Q(A,lam)==end-arc and gcd(lam,A)==1
    G,gx,gy=egcd(lam*M,A)
    assert G==gcd(M,A) and gx*lam*M+gy*A==G
    p,q=A//G,lam*M//G;assert q>0 and gcd(abs(p),q)==1
    J=integral(F)/M;assert J>0
    records.append({'N':N,'C_N':cs[N],'C_Nminus1':cs[N-1],'d':d,'B':B,'I':I,
        'source_norm':str(Q(I,d*d)),'K':K,'U':U,'kappa':str(Q(I-d*d,Z)),
        'raw_W':raw,'raw_Z':Z,'h':h,'h_bezout':hbez,'primitive_W':F,'M':M,
        'S':S,'B_endpoint':end,'complete_arc':str(arc),'lambda':lam,'A':A,
        'final_G':G,'final_G_bezout':[gx,gy],'p':p,'q':q,'J':str(J),'qJ':str(q*J),
        'whole_error_interval':[str(3*q*J),str(7*q*J)],
        'valuations_2':{name:val(value,2) for name,value in [('d',d),('I',I),('U',U),('h',h),('M',M),('lambda',lam),('G',G),('q',q)]},
        'valuations_5':{name:val(value,5) for name,value in [('d',d),('I',I),('U',U),('h',h),('M',M),('lambda',lam),('G',G),('q',q)]}})
assert factorial(255)>6**511
out={'scope':'NEW signed-source Chebyshev ansatz N3..12 only; finite diagnostics do not certify an infinite primitive-error estimate.',
     'all_exact_checks_passed':True,'network_or_credentials_used':False,
     'producer_degree_max':24,'producer_factorial_max':24,'quotient_degree_max':22,
     'source_equality_and_actual_clearers_verified':True,'records':records,
     'separate_fixed_constant':{'inequality':'255! > 6^511','factorial_value':str(factorial(255)),'power_value':str(6**511)},
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'signed_chebyshev_normalization_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks_passed':True,'scope':out['scope'],'rows':[{'N':r['N'],'q_digits':len(str(r['q'])),'G_digits':len(str(r['final_G'])),'q_v2':r['valuations_2']['q'],'q_v5':r['valuations_5']['q'],'qJ':r['qJ']} for r in records]},indent=2))
