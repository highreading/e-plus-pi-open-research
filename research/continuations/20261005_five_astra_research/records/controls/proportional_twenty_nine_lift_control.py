"""Direct prescribed b839 audit via original coefficient and Newton identities.
No remote code is executed. Structured inverse replaces cubic dense inversion.
"""
import math,json,time,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
start=time.monotonic();p=29;depth=3;mod=p**3;b=839;n=2001*b;N=n//p;B=b//p;cutoff=3*p
def F(k):
    v=0
    while k:k//=p;v+=k
    return v
def poly_mul(a,b,limit,modulus):
    z=[0]*min(limit,len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:len(z)-i]):z[i+j]=(z[i+j]+x*y)%modulus
    return z
def poly_power(base,exponent,limit,modulus):
    out=[1]
    while exponent:
        if exponent&1:out=poly_mul(out,base,limit,modulus)
        base=poly_mul(base,base,limit,modulus);exponent//=2
    return out+[0]*(limit-len(out))
phi=poly_power([1,-1,pow(2,-1,mod)],n,cutoff,mod)
ds=[phi[s]*math.factorial(s)%mod for s in range(cutoff)]
assert all(v%p==0 for v in ds[1:])
def binomial_series(x,length):
    value=1;out=[1]
    for r in range(1,length):
        value=value*(x-r+1)//r;out.append(value%mod)
    return out
tn=binomial_series(n,b+cutoff);tm=binomial_series(-n,b);tm2=binomial_series(-2*n,b)
def toeplitz(coeff,v,size=b):
    return [sum(coeff[j-i]*v[j] for j in range(i,len(v)))%mod for i in range(size)]
def pascal_inverse(v):
    row=[1];out=[]
    for i in range(b):
        out.append(sum(((-1)**(i-j))*x*v[j] for j,x in enumerate(row))%mod)
        row=[1]+[(row[j-1]+row[j])%mod for j in range(1,len(row))]+[1]
    return out
choose_shift={s:[math.comb(j+s,s)%(p*p) for j in range(b)] for s in range(1,cutoff) if ds[s]}
def correction(v):
    y=toeplitz(tm,v)
    shifted=[0]*(b+cutoff-1)
    for s,choose in choose_shift.items():
        scalar=ds[s]//p
        for j,x in enumerate(y):shifted[j+s]=(shifted[j+s]+scalar*choose[j]*x)%mod
    return toeplitz(tn,shifted)
def divided_solution(v):
    g=pascal_inverse(v);e1=correction(g);e2=correction(e1)
    return toeplitz(tm2,[(g[i]-p*e1[i]+p*p*e2[i])%mod for i in range(b)])
weights=binomial_series(n+2,b+1)
def reconstruct(theta):
    return [weights[j]*((j*theta[j-1] if j else 0)-(theta[j] if j<b else 0))%mod for j in range(b+1)]
# Original central coefficient. P(t)^p=P(t^p)+p*A(t) exactly.
# Three binomial terms suffice modulo p^3; they reduce the large exponent
# from n to N,N-1,N-2, whose coefficients are computed as full integers.
small=[1]
for _ in range(p):
    z=[0]*(len(small)+2)
    for i,x in enumerate(small):z[i]+=x;z[i+1]+=2*x;z[i+2]+=2*x
    small=z
small[0]-=1;small[p]-=2;small[2*p]-=2
assert all(x%p==0 for x in small)
A=[(x//p)%mod for x in small];A2=poly_mul(A,A,len(A)*2-1,mod)
near=[]
for loss in range(3):
    exponent=N-loss;previous=0;current=1;data={}
    for r in range(N+2):
        numerator=2*(exponent-r)*current+2*(2*exponent-r+1)*previous
        nxt,remainder=divmod(numerator,r+1);assert remainder==0
        previous,current=current,nxt
        if r+1>=N-10:data[r+1]=current%mod
    near.append(data)
central=[]
for l in range(cutoff):
    value=near[0][N-l//p] if l%p==0 else 0
    for j,x in enumerate(A):
        if (l+j)%p==0:value+=p*N*x*near[1][N-(l+j)//p]
    for j,x in enumerate(A2):
        if (l+j)%p==0:value+=p*p*math.comb(N,2)*x*near[2][N-(l+j)//p]
    central.append(value%mod)
force=[0]*b;rising=1
for i in range(cutoff):
    if i:rising=rising*(n+i)%mod
    force[i]=rising*sum(math.comb(i,t)*central[t] for t in range(i+1))%mod
assert F(cutoff)==3 and central[0]%p==13
# Exact factorial-tail normalization. Precompute the consecutive-upper
# binomials as FULL integers before reducing; never divide nonunits mod p.
Fb=F(b);tailend=next(t for t in range(b,b+4*p) if F(t)-Fb>=depth)
lower=2*n-cutoff+1;length=b+cutoff-1;tail=[0]*length
ratio=1
for t in range(b,tailend):
    if t>b:ratio=ratio*t%mod
    value=math.comb(lower,t)
    for shift in range(length):
        tail[shift]=(tail[shift]+ratio*(value%mod))%mod
        upper=lower+shift+1;value=value*upper//(upper-t)
residual=[sum(ds[s]*math.comb(n+i,s)*tail[i-s+cutoff-1] for s in range(cutoff))%mod for i in range(b)]
thetaP=divided_solution(force);thetaQ=divided_solution(residual)
Z=reconstruct(thetaP);Y=reconstruct(thetaQ);Y[b]=(Y[b]+weights[b])%mod
assert all(x%p==0 for x in Z) and all(x%(p*p)==0 for x in Y)
P1=[x//p%p for x in Z];Q2=[x//(p*p) for x in Y]
expected=[0]*(b+1);T=[]
for q in range(B+1):
    product=math.comb(N,q)*math.comb(2*N+B-q,B-q)
    assert product%p==0
    tq=product//p%p;T.append(tq)
    for u,factor in enumerate((-1,2,-1)):expected[p*q+u]=13*((-1)**q)*tq*factor%p
assert P1==expected and T[0]==18 and P1[0]==27
norm=sum(x*x for x in P1)%p;mixed=sum(x*y for x,y in zip(P1,Q2))%p
assert norm==6*13*13*sum(x*x for x in T)%p
logdepth=F(n)-F(b);upper=2*n+b-1;lg=0
while upper>=p:upper//=p;lg+=1
logdepth-=lg;assert logdepth==59925
report={'n':n,'b':b,'prime':p,'precision':depth,'auxiliary_not_original_power3_index':True,
 'all_requested_P_column_predictions_pass':True,'J_mod29':central[0]%p,'T_mod29':T,
 'normalized_P1_mod29':P1,'normalized_Q2_mod29':Q2,
 'Q_divided_bfactorial_whole_column_zero_mod841':True,'normalized_norm_mod29':norm,
 'normalized_mixed_mod29':mixed,'full_log_forcing_divided_bfactorial_depth_lower_bound':logdepth,
 'divided_coefficient_cutoff':cutoff,'factorial_tail_end_exclusive':tailend,
 'finite_only':True,'seconds':round(time.monotonic()-start,3)}
(OUT/'proportional_twenty_nine_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if not isinstance(v,list)}))
