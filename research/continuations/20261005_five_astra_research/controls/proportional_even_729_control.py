"""Original multinomial binary center audit, with exact structured inverse.
All formulas are coordinator-authored. No third-party code is executed.
"""
import math,json,time,resource
from functools import lru_cache
from pathlib import Path
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;depth=14;mod=2**depth;cutoff=64;forcecutoff=128
def F(k):
    v=0
    while k:k//=2;v+=k
    return v
def val(k):
    return (k&-k).bit_length()-1 if k else None
oddprefix=[1]*mod
for i in range(1,mod):oddprefix[i]=oddprefix[i-1]*(i if i%2 else 1)%mod
blockproduct=oddprefix[-1];assert blockproduct==1
@lru_cache(None)
def factorialunit(k):
    unit=1
    while k:
        unit=unit*pow(blockproduct,k//mod,mod)*oddprefix[k%mod]%mod;k//=2
    return unit
def binseries(x,length):
    value=1;out=[1]
    for k in range(1,length):
        value=value*(x-k+1)//k;out.append(value%mod)
    return np.array(out,dtype=np.int64)
records=[]
for b in (81,729):
    start=time.monotonic();n=4002*b;h=n//2
    ds=[]
    for s in range(cutoff):
        ds.append(sum(((-1)**s)*(math.factorial(s)//(2**j))
           *math.comb(n,s-j)*math.comb(s-j,j) for j in range(s//2+1))%mod)
    assert all(x%2==0 for x in ds[1:])
    tn=binseries(n,b+cutoff);tm=binseries(-n,b);tm2=binseries(-2*n,b)
    weights=binseries(n+2,b+1)
    def toeplitz(coeff,v,size=b):
        assert len(v)*mod*mod<2**63
        c=np.convolve(np.asarray(v,dtype=np.int64)[::-1],coeff)
        return (c[len(v)-size:len(v)][::-1]%mod).copy()
    def pascal_inverse(v):
        v=np.asarray(v,dtype=np.int64);row=np.array([1],dtype=np.int64)
        signs=np.where(np.arange(b)%2,-1,1).astype(np.int64);signed=v*signs;out=[]
        for i in range(b):
            out.append(int(row@signed[:i+1])*int(signs[i])%mod)
            row=np.r_[1,(row[:-1]+row[1:])%mod,1]
        return np.array(out,dtype=np.int64)
    shifts={s:np.array([math.comb(j+s,s)%(mod//2) for j in range(b)],dtype=np.int64)
             for s in range(1,cutoff) if ds[s]}
    def correction(v):
        y=toeplitz(tm,v);shifted=np.zeros(b+cutoff-1,dtype=np.int64)
        for s,choose in shifts.items():
            shifted[s:s+b]=(shifted[s:s+b]+(ds[s]//2)*choose*y)%mod
        return toeplitz(tn,shifted)
    def solution(v):
        g=pascal_inverse(v);total=g.copy();current=g
        for k in range(1,depth):
            current=correction(current);total=(total+((-2)**k)*current)%mod
        return toeplitz(tm2,total)
    def reconstruct(theta):
        z=np.zeros(b+1,dtype=np.int64);z[:b]-=theta
        z[1:]+=np.arange(1,b+1,dtype=np.int64)*theta
        return z*weights%mod
    Ddepth=[0]*forcecutoff;Dunit=[1]*forcecutoff
    for i in range(1,forcecutoff):
        v=val(n+i);Ddepth[i]=Ddepth[i-1]+v
        Dunit[i]=Dunit[i-1]*((n+i)//2**v)%mod
    normalized=[];uh=factorialunit(h)
    for l in range(cutoff):
        total=0;r0=(l+1)//2
        for r in range(r0,r0+64):
            indices=(2*r-l,h-r,h-r+l)
            vv=Ddepth[l]+r-l+2*F(h)-sum(F(z) for z in indices)
            assert vv>=0
            if vv>=depth:continue
            unit=Dunit[l]*uh*uh%mod
            for z in indices:unit=unit*pow(factorialunit(z),-1,mod)%mod
            total=(total+2**vv*unit)%mod
        normalized.append(total)
    force=[0]*b
    for i in range(min(b,forcecutoff)):
        for l in range(min(i+1,cutoff)):
            v=Ddepth[i]-Ddepth[l]
            if v<depth:
                rising=(2**v)*Dunit[i]*pow(Dunit[l],-1,mod)%mod
                force[i]=(force[i]+math.comb(i,l)*rising*normalized[l])%mod
    # B_l for l>=64 contains at least F(32!)=31 powers of2.
    # For i>=128 and l<64, the remaining rising factorial has depth>=F(65!).
    # Both omitted sets therefore vanish at depth14 uniformly.
    Fb=F(b);tailend=next(t for t in range(b,b+60) if F(t)-Fb>=depth)
    length=b+cutoff-1;lower=2*n-cutoff+1;tail=[0]*length;ratio=1
    for t in range(b,tailend):
        if t>b:ratio=ratio*t%mod
        value=math.comb(lower,t)
        for j in range(length):
            tail[j]=(tail[j]+ratio*(value%mod))%mod
            upper=lower+j+1;value=value*upper//(upper-t)
    residual=[sum(ds[s]*math.comb(n+i,s)*tail[i-s+cutoff-1]
               for s in range(cutoff) if ds[s])%mod for i in range(b)]
    ZR=reconstruct(solution(force));Vb=reconstruct(solution(residual))
    Vb[b]=(Vb[b]+weights[b])%mod
    assert np.all(ZR%2==0) and np.all(Vb%4==0)
    X=(ZR//2).tolist();Y=(Vb//4).tolist();commonmod=mod//4
    D=sum(x*x for x in X)%commonmod;C=sum(x*y for x,y in zip(X,Y))%commonmod
    alpha=val(D);gamma=val(C);assert alpha is not None and gamma is not None
    # Kummer/Legendre gives the central binomial valuation without
    # constructing its millions-of-bits integer value.
    vR=h+2*h.bit_count()-n.bit_count();vlam=2*F(n)-n
    vA=2*vlam+2*(vR+1)+alpha;vH=vlam+vR+1+Fb+2+gamma
    q=vA-min(vA,vH);hF=h+1-2*((2*n+b-1).bit_length()-1)-Fb
    assert hF>=depth
    baseline=False
    if b==81:
        old=json.loads((OUT/'proportional_even_four_control.json').read_text())['records'][0]
        assert [z%mod for z in old['weighted_P_divided_R_modulus']]==ZR.tolist()
        assert [z%mod for z in old['weighted_Q_divided_bfactorial_modulus']]==Vb.tolist()
        baseline=True
    if b==729:assert all(x%2==0 for x in X)
    record={'n':n,'b':b,'precision':depth,'common_contraction_precision':depth-2,
       'original_multinomial_sums':True,'structured_exact_inverse':True,
       'b81_independent_dense_baseline_pass':baseline,
       'contact_cutoff':cutoff,'force_cutoff':forcecutoff,'central_t_cutoff':64,
       'factorial_tail_end_exclusive':tailend,'complete_hF_divided_bfactorial_depth_bound':hF,
       'norm_residue':D,'mixed_residue':C,'norm_depth':alpha,'mixed_depth':gamma,
       'X_content_lower_bound':min(val(x) for x in X if x),
       'Y_content_lower_bound':min(val(y) for y in Y if y),
       'norm_leading_mod4':(D//2**alpha)%4,'mixed_leading_mod4':(C//2**gamma)%4,
       'actual_Gram_norm_depth':vA,'actual_Gram_mixed_depth':vH,
       'actual_final_gcd_depth':min(vA,vH),'actual_q_depth':q,
       'X_mod8192':X,'Y_mod4096':Y,'finite_only':True,'seconds':round(time.monotonic()-start,3)}
    records.append(record)
    print(json.dumps({k:v for k,v in record.items() if not isinstance(v,list)}),flush=True)
(OUT/'proportional_even_729_control.json').write_text(json.dumps({'records':records},indent=2)+'\n')
