"""Parent-authored finite audit of NEW Y/Z contents, with old Smith reuse."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,gcd,lcm,isqrt
import json,hashlib
OUT=Path(__file__).resolve().parent;K=5;M=3*K-2
checks=[]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def md(a,p):
    b=[[x%p for x in r] for r in a];s=1;v=1
    for j in range(len(a)):
        r=next((i for i in range(j,len(a)) if b[i][j]),None)
        if r is None:return 0
        if r!=j:b[r],b[j]=b[j],b[r];s=-s
        z=b[j][j];v=v*z%p;iv=pow(z,-1,p)
        for i in range(j+1,len(a)):
            z=b[i][j]*iv%p
            for t in range(j+1,len(a)):b[i][t]=(b[i][t]-z*b[j][t])%p
    return s*v%p
def det(a,label):
    b=[r[:] for r in a];s=1;old=1;divs=0
    for j in range(len(a)-1):
        r=next((i for i in range(j,len(a)) if b[i][j]),None)
        if r is None:v=0;break
        if r!=j:b[r],b[j]=b[j],b[r];s=-s
        pivot=b[j][j]
        for i in range(j+1,len(a)):
            x=b[i][j]
            for t in range(j+1,len(a)):
                value,rem=divmod(pivot*b[i][t]-x*b[j][t],old)
                assert rem==0;b[i][t]=value;divs+=1
            b[i][j]=0
        old=pivot
    else:v=s*b[-1][-1]
    mods=[]
    for p in (1000000007,1000000009,1000000033):
        assert prime(p);r=md(a,p);assert v%p==r;mods.append({'prime':p,'residue':r})
    checks.append({'label':label,'size':len(a),'det':str(v),'exact_divisions':divs,
      'matrix_sha256':hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest(),
      'modular':mods})
    return v
def eg(a,b):
    old,r=abs(a),abs(b);x,xx=1,0;y,yy=0,1
    while r:q=old//r;old,r=r,old-q*r;x,xx=xx,x-q*xx;y,yy=yy,y-q*yy
    return old,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)
def cg(a):
    g=0;w=[]
    for x in a:g,u,v=eg(g,x);w=[u*z for z in w]+[v]
    assert sum(x*y for x,y in zip(a,w))==g
    return g,w
def strip(x):
    x=abs(x);vals={}
    for p in range(2,6*K-3):
        if not prime(p):continue
        a=0
        while x and x%p==0:x//=p;a+=1
        if a:vals[str(p)]=a
    return {'small_prime_valuations':vals,'residual':str(x),'cutoff':6*K-4}

a=[1]
for j in range(1,2*M+1):a.append(1-j*a[-1])
c=[a[2*j]-(-1)**j for j in range(M+1)]
rho=[Q(0)]
for j in range(M):rho.append(Q(1,2*j+1)-rho[-1])
r=[-factorial(2*j)+4*rho[j] for j in range(M+1)]
sigma=[c[j+1]+c[j] for j in range(M)]
tau=[r[j+1]+r[j] for j in range(M)]
assert all(tau[j]==-factorial(2*j+2)-factorial(2*j)+Q(4,2*j+1) for j in range(M))
L=lcm(*range(1,6*K-4,2))
def integer(v):assert Q(v).denominator==1;return int(v)
Z=[[c[i+j] for j in range(K)]+[integer(L*tau[i+j]) for j in range(K-1)] for i in range(2*K)]
Y=[[sigma[i+j] for j in range(K)]+[integer(L*tau[i+j]) for j in range(K)] for i in range(2*K-1)]
zm=[(-1)**j*det(Z[:j]+Z[j+1:],f'Z_max_delete_row{j}') for j in range(2*K)]
ym=[(-1)**j*det([[x for t,x in enumerate(row) if t!=j] for row in Y],f'Y_max_delete_column{j}') for j in range(2*K)]
R,Rw=cg(zm);Lc,Lw=cg(ym)
assert all(sum(zm[i]*Z[i][j] for i in range(2*K))==0 for j in range(2*K-1))
assert all(sum(Y[i][j]*ym[j] for j in range(2*K))==0 for i in range(2*K-1))
B=[[sigma[i+j] for j in range(K)]+[integer(L*(tau[i+j]+tau[i+j-1])) for j in range(1,K)] for i in range(2*K-1)]
b=[c[j] for j in range(K)]+[integer(L*tau[j-1]) for j in range(1,K)]
d=[integer(L*tau[i]) for i in range(2*K-1)]
D=det(B,'actual_B');assert D!=0
minus_L=det([[0]+b]+[[d[i]]+B[i] for i in range(2*K-1)],'zero_corner_border_minus_L')
cross=-minus_L
F0=-L*D-cross;F1=L*D
H0=(-1)**K*F0;H1=(-1)**K*F1
def original(s):return [[c[i+j] for j in range(K)]+[integer(L*(r[i+j]+s*(-1)**(i+j))) for j in range(K)] for i in range(2*K)]
assert det(original(0),'H_at0_sign_comparison')==H0
assert det(original(1),'H_at1_sign_comparison')==H0+H1
G,Gw=cg([H0,H1]);assert G%lcm(R,Lc)==0 and (L*R*Lc)%G==0
old_path=OUT.parent.parent/'astra_pro5_resume_20261007/controls/compact_contact_saturation_certificate.json'
old=json.loads(old_path.read_text());old5=next(x for x in old['receipts'] if x['k']==5)
invs=old5['full_contact_invariants'];assert invs==[2,2,32,128,9216]
dk=1
for x in invs:dk*=x
assert dk==old5['gcd_maximal_minors']==150994944
assert R%dk==0 and Lc%(2*2*32*128)==0
product=2**(K*(K-1))
for j in range(K-1):product*=factorial(j)**2
Ej=1
for j in range(K):Ej*=L//lcm(*range(1,4*K+2*j-2,2))
assert G%(product*Ej)==0
cert={'scope':'NEW two-rectangle contents at auxiliary k5 only; no original-index or uniform support conclusion',
 'k':K,'moment_max':M,'factorial_max':2*M,'last_odd':6*K-5,'Lambda':L,
 'Z':Z,'Y':Y,'Z_signed_maximal_minors':list(map(str,zm)),
 'Y_signed_maximal_minors':list(map(str,ym)),'R':str(R),'R_bezout':list(map(str,Rw)),
 'L':str(Lc),'L_bezout':list(map(str,Lw)),'B':B,'b':b,'d':d,
 'D':str(D),'cross_L':str(cross),'H0':str(H0),'H1':str(H1),'G':str(G),
 'G_bezout':list(map(str,Gw)),'stripped_R':strip(R),'stripped_L':strip(Lc),
 'stripped_G':strip(G),'old_contact_Smith_reused':old5,
 'old_receipt_sha256':hashlib.sha256(old_path.read_bytes()).hexdigest(),
 'all_paid_divisibilities_checked':True,'new_determinant_checks':checks,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'compact_two_rectangle_k5_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({k:cert[k] for k in ('scope','R','L','G','stripped_R','stripped_L','stripped_G','all_paid_divisibilities_checked')}))
