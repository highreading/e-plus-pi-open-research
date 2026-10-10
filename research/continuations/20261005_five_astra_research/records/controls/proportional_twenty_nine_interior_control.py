"""Coordinator-authored exact audit of interior factorial carry at p=29.
Original polynomial coefficients; no external code, network, or key reads.
Finite auxiliary centers, not an assertion about powers-of-three indices.
"""
import math,json,time,resource,argparse
from pathlib import Path
from functools import lru_cache
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--depth',type=int,choices=(3,4),default=3)
depth=parser.parse_args().depth;p=29;mod=p**depth
def F(n):
    v=0
    while n:n//=p;v+=n
    return v
def mul(a,b,m):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%m
    return out
@lru_cache(None)
def small_power(e,m):
    out=[1]
    for _ in range(e):out=mul(out,[1,2,2],m)
    return tuple(out)
fullp=small_power(p,10**30)
# All coefficients of degree58 are less than10**30, checked with an
# independently exact multiplication before using any modular expansion.
exact=[1]
for _ in range(p):
    z=[0]*(len(exact)+2)
    for i,x in enumerate(exact):z[i]+=x;z[i+1]+=2*x;z[i+2]+=2*x
    exact=z
assert list(fullp)==exact
exact[0]-=1;exact[p]-=2;exact[2*p]-=2
assert all(x%p==0 for x in exact)
A=[x//p%mod for x in exact]
AP=[[1]]
for _ in range(1,depth):AP.append(mul(AP[-1],A,mod))
@lru_cache(None)
def kernel(d,loss,precision):
    m=p**precision
    return tuple(mul(small_power(d,m),AP[loss],m))
@lru_cache(None)
def base_coefficients(e):
    previous=0;current=1;out=[1]
    for k in range(2*e):
        numer=2*(e-k)*current+2*(2*e-k+1)*previous
        nxt,rem=divmod(numer,k+1);assert rem==0
        previous,current=current,nxt;out.append(current%mod)
    return tuple(out)
@lru_cache(None)
def coefficient(e,k,precision):
    if k<0 or k>2*e:return 0
    m=p**precision
    if e<10000:return base_coefficients(e)[k]%m
    E,d=divmod(e,p);value=0
    for loss in range(min(precision,E+1)):
        scalar=(p**loss)*math.comb(E,loss)
        subtotal=0
        for j,x in enumerate(kernel(d,loss,precision)):
            if x and (k-j)%p==0:
                subtotal+=x*coefficient(E-loss,(k-j)//p,precision-loss)
        value+=scalar*subtotal
    return value%m
def binseries(x,length):
    value=1;out=[1]
    for k in range(1,length):
        value=value*(x-k+1)//k;out.append(value%mod)
    return np.array(out,dtype=np.int64)
def general_binom(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)
records=[]
for b in (839,2521):
    start=time.monotonic();n=2001*b;N=n//p;B=b//p;cutoff=depth*p
    phi=[1]
    exponent=n;base=[1,-1,pow(2,-1,mod)]
    def truncmul(a,c):return mul(a,c,mod)[:cutoff]
    while exponent:
        if exponent&1:phi=truncmul(phi,base)
        base=truncmul(base,base);exponent//=2
    phi+=([0]*(cutoff-len(phi)))
    ds=[phi[s]*math.factorial(s)%mod for s in range(cutoff)]
    assert all(x%p==0 for x in ds[1:])
    tn=binseries(n,b+cutoff);tm=binseries(-n,b);tm2=binseries(-2*n,b)
    weights=binseries(n+2,b+1)
    def toeplitz(coeff,v,size=b):
        # Integer convolution is exact: at most2608 terms, each<mod^2.
        assert len(v)*mod*mod<2**63
        c=np.convolve(np.asarray(v,dtype=np.int64)[::-1],coeff)
        return (c[len(v)-size:len(v)][::-1]%mod).copy()
    def pascal_inverse(v):
        v=np.asarray(v,dtype=np.int64);row=np.array([1],dtype=np.int64)
        signs=np.where(np.arange(b)%2,-1,1).astype(np.int64)
        signed=v*signs;out=[]
        for i in range(b):
            out.append(int(row@signed[:i+1])*int(signs[i])%mod)
            row=np.r_[1,(row[:-1]+row[1:])%mod,1]
        return np.array(out,dtype=np.int64)
    shifts={s:np.array([math.comb(j+s,s)%(p**(depth-1)) for j in range(b)],dtype=np.int64)
            for s in range(1,cutoff) if ds[s]}
    def correction(v):
        y=toeplitz(tm,v);shifted=np.zeros(b+cutoff-1,dtype=np.int64)
        for s,choose in shifts.items():
            shifted[s:s+b]=(shifted[s:s+b]+(ds[s]//p)*choose*y)%mod
        return toeplitz(tn,shifted)
    def solution(v):
        g=pascal_inverse(v);out=g.copy();current=g
        for k in range(1,depth):
            current=correction(current);out=(out+((-p)**k)*current)%mod
        return toeplitz(tm2,out)
    def reconstruct(theta):
        z=np.zeros(b+1,dtype=np.int64);z[:b]-=theta
        z[1:]+=np.arange(1,b+1,dtype=np.int64)*theta
        return (z*weights)%mod
    central=[coefficient(n,n-l,depth) for l in range(cutoff)]
    force=[0]*b;rising=1
    for i in range(cutoff):
        if i:rising=rising*(n+i)%mod
        force[i]=rising*sum(math.comb(i,t)*central[t] for t in range(i+1))%mod
    Fb=F(b);tailend=next(t for t in range(b,b+4*p) if F(t)-Fb>=depth)
    length=b+cutoff-1;lower=2*n-cutoff+1;tail=[0]*length;ratio=1
    for t in range(b,tailend):
        if t>b:ratio=ratio*t%mod
        value=math.comb(lower,t)
        for j in range(length):
            tail[j]=(tail[j]+ratio*(value%mod))%mod
            upper=lower+j+1;value=value*upper//(upper-t)
    residual=[sum(ds[s]*math.comb(n+i,s)*tail[i-s+cutoff-1]
                  for s in range(cutoff) if ds[s])%mod for i in range(b)]
    Z=reconstruct(solution(force));Y=reconstruct(solution(residual))
    Y[b]=(Y[b]+weights[b])%mod
    assert np.all(Z%p==0) and np.all(Y%(p*p)==0)
    P1=(Z//p%p).tolist();Q2=(Y//(p*p)%p).tolist()
    T=[]
    for q in range(B+1):
        prod=math.comb(N,q)*math.comb(2*N+B-q,B-q)
        assert prod%p==0;T.append(((-1)**q)*(prod//p)%p)
    T.append(0);expectedP=[0]*(b+1);expectedQ=[0]*(b+1)
    J=central[0]%p;K=(B+1)//p;N1=(N-7)//p
    assert (B+1)%p==0 and N%p==7 and N1%p==24
    for q in range(B+1):
        for u,c in enumerate((-1,2,-1)):expectedP[p*q+u]=J*T[q]*c%p
        for u,c in enumerate((1,2,-2)):expectedQ[p*q+u]=6*T[q]*c%p
        correction_term=0
        if (q+1)%p==0:
            r=(q+1)//p
            correction_term=K*pow(12,-1,p)*general_binom(N1,r)*general_binom(-2*N1-1,K-r)
        expectedQ[p*q+27]=(-6*T[q+1]-correction_term)%p
    assert P1==expectedP and Q2==expectedQ
    if b==839:
        prior=json.loads((OUT/'proportional_twenty_nine_fourth_control.json').read_text())
        assert P1==prior['normalized_P1_mod29']
        assert Q2==prior['normalized_Q2_mod29']
        assert central[0]%(p*p)==prior['fourth_digit']['central_Cn_mod841']
        if depth==4:
            assert (Z//p%(p*p)).tolist()==prior['fourth_digit']['P1_mod841']
            assert (Y//(p*p)%(p*p)).tolist()==prior['fourth_digit']['Q2_mod841']
    logdepth=F(n)-F(b);upper=2*n+b-1;lg=0
    while upper>=p:upper//=p;lg+=1
    logdepth-=lg;assert logdepth>=depth
    record={'n':n,'b':b,'prime':p,'precision':depth,'auxiliary_index_only':True,
        'coefficient_method':'exact recursive original P^29=P(t^29)+29A; reduced precision in each carry',
        'independent_b839_baseline_verified':b==839,
        'P_formula_all_coordinates_pass':True,'Q_formula_all_coordinates_pass':True,
        'J_mod29':J,'Cn_mod841':central[0]%(p*p),
        'norm_mod29':sum(x*x for x in P1)%p,
        'mixed_mod29':sum(x*y for x,y in zip(P1,Q2))%p,
        'complete_hF_divided_bfactorial_depth_bound':logdepth,
        'cutoff':cutoff,'factorial_tail_end_exclusive':tailend,
        'interior_carry_values':{str(j):Q2[j] for j in (839,1680,2521) if j<=b},
        'interior_carry_predictions':{str(j):expectedQ[j] for j in (839,1680,2521) if j<=b},
        'T_signed_mod29':T,'normalized_P1_mod29':P1,'normalized_Q2_mod29':Q2,
        'finite_only':True,'seconds':round(time.monotonic()-start,3)}
    if b==2521:
        assert Q2[839]==(-6*T[29]+16)%p
        assert Q2[1680]==(-6*T[58]+17)%p
        assert Q2[2521]==16
    records.append(record)
    if depth==4:
        PP=(Z//p%(p*p)).tolist();QQ=(Y//(p*p)%(p*p)).tolist()
        DD=sum(x*x for x in PP)%(p*p);MM=sum(x*y for x,y in zip(PP,QQ))%(p*p)
        c=pow(6*(central[0]%(p*p)),-1,p*p);defect=(MM-c*DD)%(p*p)
        assert defect%p==0
        record['next_digit']={'P1_mod841':PP,'Q2_mod841':QQ,
            'norm_mod841':DD,'mixed_mod841':MM,
            'divided_alignment_defect_mod29':defect//p,
            'norm_divided29_mod29':DD//p if DD%p==0 else None,
            'mixed_divided29_mod29':MM//p if MM%p==0 else None}
    brief={k:v for k,v in record.items() if not isinstance(v,(list,dict))}
    brief['interior_carry_values']=record['interior_carry_values']
    if depth==4:brief['next_digit']={k:v for k,v in record['next_digit'].items() if not isinstance(v,list)}
    print(json.dumps(brief),flush=True)
filename='proportional_twenty_nine_interior_control.json' if depth==3 else 'proportional_twenty_nine_interior_fourth_control.json'
(OUT/filename).write_text(json.dumps({'records':records},indent=2)+'\n')
