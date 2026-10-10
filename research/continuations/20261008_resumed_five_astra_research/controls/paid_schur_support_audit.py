"""Parent-authored bounded Schur arithmetic, network/key-denying sandbox."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, gcd, lcm, isqrt
import hashlib, json, sys, time

sys.set_int_max_str_digits(500000)
OUT=Path(__file__).resolve().parent
K=11
MAX=3*K+1
started=time.monotonic()
certs=[]

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def moddet(source,p):
    a=[[x%p for x in r] for r in source];sign=1;value=1
    for j in range(len(a)):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None:return 0
        if r!=j:a[j],a[r]=a[r],a[j];sign=-sign
        z=a[j][j];value=value*z%p;inv=pow(z,-1,p)
        for r in range(j+1,len(a)):
            ratio=a[r][j]*inv%p
            for c in range(j+1,len(a)):a[r][c]=(a[r][c]-ratio*a[j][c])%p
            a[r][j]=0
    return sign*value%p

def det(source,label):
    a=[r[:] for r in source];sign=1;old=1;divisions=0;swaps=[]
    for j in range(len(a)-1):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None:value=0;break
        if r!=j:a[j],a[r]=a[r],a[j];sign=-sign;swaps.append([j,r])
        pivot=a[j][j]
        for r in range(j+1,len(a)):
            left=a[r][j]
            for c in range(j+1,len(a)):
                z,remainder=divmod(pivot*a[r][c]-left*a[j][c],old)
                assert remainder==0
                a[r][c]=z;divisions+=1
            a[r][j]=0
        old=pivot
    else:value=sign*a[-1][-1]
    modular=[]
    for p in (1000000007,1000000009,1000000033):
        assert prime(p)
        residue=moddet(source,p);assert value%p==residue
        modular.append({'prime':p,'residue':residue})
    certs.append({'label':label,'size':len(a),'determinant':str(value),
                  'matrix_sha256':hashlib.sha256(json.dumps(source,separators=(',',':')).encode()).hexdigest(),
                  'exact_divisions':divisions,'row_swaps':swaps,'independent_modular_checks':modular})
    return value

def egcd(a,b):
    old,r=abs(a),abs(b);x,xx=1,0;y,yy=0,1
    while r:
        q=old//r;old,r=r,old-q*r;x,xx=xx,x-q*xx;y,yy=yy,y-q*yy
    return old,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)

a=[1]
for n in range(1,2*MAX+1):a.append(1-n*a[-1])
c=[a[2*n]-(-1)**n for n in range(MAX+1)]
rho=[Q(0)]
for n in range(MAX):rho.append(Q(1,2*n+1)-rho[-1])
r=[-factorial(2*n)+4*rho[n] for n in range(MAX+1)]
sigma=[c[n+1]+c[n] for n in range(MAX)]
tau=[r[n+1]+r[n] for n in range(MAX)]
assert all(tau[n]==-factorial(2*n+2)-factorial(2*n)+Q(4,2*n+1) for n in range(MAX))
lam=lcm(*range(1,6*(K+1)-4,2));lam0=lcm(*range(1,6*K-4,2));jump=lam//lam0
assert jump==67 and lam%lam0==0

def nested(size,s):
    result=[]
    for row in range(2*size):
        entries=[]
        for j in range(size):
            if j==0:right=s-1 if row==0 else tau[row-1]
            else:right=tau[j-1] if row==0 else tau[row+j-1]+tau[row+j-2]
            contact=c[j] if row==0 else sigma[row+j-1]
            right=lam*right;assert Q(right).denominator==1
            entries.extend([int(right),contact])
        result.append(entries)
    return result

def original(size,s):
    L=lam0 if size==K else lam
    result=[]
    for m in range(2*size):
        right=[L*(r[m+j]+s*(-1)**(m+j)) for j in range(size)]
        assert all(v.denominator==1 for v in right)
        result.append([c[m+j] for j in range(size)]+[int(v) for v in right])
    return result

full=nested(K+1,0);n=2*K
B=[row[1:n] for row in full[1:n]]
U=[row[n:n+2] for row in full[1:n]]
V=[row[1:n] for row in full[n:n+2]]
W=[row[n:n+2] for row in full[n:n+2]]
b=full[0][1:n];beta=full[0][n:n+2]
d=[row[0] for row in full[1:n]];delta=[row[0] for row in full[n:n+2]]
D=det(B,'D_actual_B0')

def border(col,row,corner,label):return det([B[i]+[col[i]] for i in range(n-1)]+[row+[corner]],label)

S=[[border([U[a][j] for a in range(n-1)],V[i],W[i][j],f'S_{i}_{j}') for j in range(2)] for i in range(2)]
t=[border([U[a][j] for a in range(n-1)],b,beta[j],f't_{j}') for j in range(2)]
z=[border(d,V[i],delta[i],f'z_{i}') for i in range(2)]
Kpaid=S[0][0]*S[1][1]-S[0][1]*S[1][0]
Tpaid=t[0]*(S[1][1]*z[0]-S[0][1]*z[1])+t[1]*(-S[1][0]*z[0]+S[0][0]*z[1])
assert D and Kpaid
pairs=[]
for size in (K,K+1):
    f=[det(nested(size,s),f'nested_{size}_s{s}') for s in (0,1,2)]
    h=[det(original(size,s),f'original_{size}_s{s}') for s in (0,1)]
    omega=(-1)**(size*(size+1)//2);scale=jump**K if size==K else 1
    assert f[2]==2*f[1]-f[0] and f[:2]==[omega*scale*v for v in h]
    pairs.append((f[0],f[1]-f[0],h[0],h[1]-h[0]))
F0,F1,H0,H1=pairs[0];Fp0,Fp1,Hp0,Hp1=pairs[1]
assert F1==lam*D
assert D*D*Fp0==Kpaid*F0-Tpaid and D*D*Fp1==Kpaid*F1
assert D*(F0*Fp1-Fp0*F1)==lam*Tpaid
G0,x0,y0=egcd(H0,H1);G1,x1,y1=egcd(Hp0,Hp1)
assert x0*H0+y0*H1==G0 and x1*Hp0+y1*Hp1==G1
gg,x,y=egcd(D*D,Kpaid);gtr,u,v=egcd(gg,Tpaid)
witness=[u*x,u*y,v]
assert witness[0]*D*D+witness[1]*Kpaid+witness[2]*Tpaid==gtr
alpha,beta,chi=Kpaid//gtr,-Tpaid//gtr,D*D//gtr
assert gcd(gcd(abs(alpha),abs(beta)),chi)==1
assert chi*Fp0==alpha*F0+beta and chi*Fp1==alpha*F1
assert gcd(chi*G1,abs(alpha)*jump**K*G0)==gcd(abs(alpha)*jump**K*G0,abs(beta))

def strip(x):
    residual=abs(x);table=[]
    for p in range(2,68):
        if not prime(p):continue
        depth=0
        while residual%p==0:residual//=p;depth+=1
        if depth:table.append({'prime':p,'valuation':depth})
    return str(residual),table

ar,at=strip(alpha);cr,ct=strip(chi)
out={'parent_authored':True,'all_checks_passed':True,'network_or_credentials_used':False,
     'scope':'Only actual paid Schur transfer at compact11-to12; no eventual or original-index implication.',
     'k':K,'max_moment':MAX,'max_factorial':2*MAX,'last_odd_denominator':67,
     'lambda':str(lam),'clearer_jump':jump,'D':str(D),'K_paid':str(Kpaid),'T_paid':str(Tpaid),
     'g_transfer':str(gtr),'transfer_bezout_witness':[str(v) for v in witness],
     'alpha':str(alpha),'beta':str(beta),'chi':str(chi),'primitive_transfer_gcd_one':True,
     'support_alpha_small_prime_valuations':at,'support_chi_small_prime_valuations':ct,
     'alpha_residual_after_all_primes_le67':ar,'chi_residual_after_all_primes_le67':cr,
     'unrestricted_S_unit_support_hypothesis_passes_this_index':ar=='1' and cr=='1',
     'original_content_11':str(G0),'original_content_12':str(G1),
     'original_content_bezout_11':[str(x0),str(y0)],'original_content_bezout_12':[str(x1),str(y1)],
     'determinant_certificates':certs,'seconds':round(time.monotonic()-started,3)}
(OUT/'paid_schur_support_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['all_checks_passed','scope','seconds','unrestricted_S_unit_support_hypothesis_passes_this_index','alpha_residual_after_all_primes_le67','chi_residual_after_all_primes_le67']},indent=2))
