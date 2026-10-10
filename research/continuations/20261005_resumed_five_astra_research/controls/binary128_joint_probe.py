"""Coordinator-authored low coefficient and complete bounded joint-sum probe.

All inversions are odd units. Actual coefficient arguments and all floor cases
are retained. This is finite reconnaissance, not a universal alignment theorem.
"""
from math import comb,factorial
from pathlib import Path
from functools import lru_cache
import json

OUT=Path(__file__).resolve().parent;MOD=1024
P=[34,31,71,69,48,12,4,4,96,72,120,72,0,64,64,64]
DELTA=[112,102,10,124,16,24,184,0,96,16,80,96,0,128,128,0]
BETA=[113,202,78,200,248,80,240,128,128]
EXTERIOR=[197,234,54,56,248,208,112,128,128]
ODD=[1]
for i in range(1,MOD):ODD.append(ODD[-1]*(i if i%2 else 1)%MOD)
assert ODD[-1]==1

def vf(n):return n-n.bit_count()

def l7(n):
    assert n>=0
    ans=1
    for i in range(7):ans=ans*ODD[(n>>i)%MOD]%MOD
    return ans

def uf(n):
    ans=1
    while n:ans=ans*ODD[n%MOD]%MOD;n//=2
    return ans

@lru_cache(maxsize=100000)
def binmod(n,r):
    if r<0 or r>n:return 0
    v=vf(n)-vf(r)-vf(n-r)
    if v>=10:return 0
    return (1<<v)*uf(n)*pow(uf(r)*uf(n-r)%MOD,-1,MOD)%MOD

@lru_cache(maxsize=100000)
def base(coeffkind,s,x):
    if not 0<=s<=15:return 0
    coeff=P if coeffkind==0 else DELTA
    return sum(coeff[r]*comb(x,r-s) for r in range(s,16) if 0<=r-s<=x)%MOD

def coefficient_data(A,x):
    aa=[comb(A+s-1,s)%MOD for s in range(16)]
    f=lambda s,z:aa[s]*base(0,s,z)%MOD if 0<=s<=15 else 0
    def z(s,xx):
        if -9<=s<=-1:return BETA[-s-1]
        if 0<=s<=15:return aa[s]*base(1,s,xx)%MOD
        return 0
    U={s:(f(s,x)+x*f(s,x-1)+x*f(s+1,x-1))%MOD for s in range(-1,16)}
    V={s:(z(s,x)+x*z(s,x-1)+x*z(s+1,x-1))%MOD for s in range(-10,16)}
    return U,V

SHAPES={}
for rho in range(128):
    for s in range(-10,16):
        a0=(84-rho)//128;ell0=(80-rho-s)//128;c0=(4+s)//128
        a=(84-rho)%128;ell=(80-rho-s)%128;c=(4+s)%128
        exponent=127*(a0-ell0-c0)+vf(a)-vf(ell)-vf(c)
        assert exponent>=0,(rho,s,exponent)
        SHAPES[rho,s]=(a0,ell0,c0,a,ell,c,exponent)

def moment_factor(C,D,t,rho,s):
    k=2*C+1;d=D-t;K=k+d
    a0,e0,c0,a,ell,c,exponent=SHAPES[rho,s]
    if d==0 and e0==-1:return 0
    if exponent>=10:return 0
    pattern=(a0,e0,c0)
    polynomial={(0,0,0):K,(0,-1,0):K*d,(0,0,-1):K*k,
                (-1,-1,0):d,(-1,0,-1):k,(-1,-1,-1):d*k}[pattern]
    assert K+a0>=0 and d+e0>=0 and k+c0>=0
    unit=l7(128*K+84-rho)*pow(l7(128*d+80-rho-s)*l7(128*k+4+s)%MOD,-1,MOD)%MOD
    return (1<<exponent)*unit*polynomial%MOD

def block(D,t,end=False,check=False):
    C=4002*D+2532;k=2*C+1;d=D-t;K=k+d;A=256*C+132
    invk=pow(k,-1,MOD);ansA=ansD=0
    highJ=binmod(K-1,d) if check else 0
    highW=binmod(C,t) if check else 0
    for rho in range(81 if end else 128):
        x=128*t+rho;U,V=coefficient_data(A,x)
        f=g=rawf=rawg=0
        for s in range(-10,16):
            mult=moment_factor(C,D,t,rho,s)
            f=(f+U.get(s,0)*mult)%MOD;g=(g+V[s]*mult)%MOD
            if check:
                mm=binmod(128*K+84-rho,128*d+80-rho-s)
                assert mm==highJ*invk*mult%MOD,(D,t,rho,s,'moment')
                rawf=(rawf+U.get(s,0)*mm)%MOD;rawg=(rawg+V[s]*mm)%MOD
        eps=int(rho>=69);z=68-rho+128*eps
        lowdepth=127*eps+vf(68)-vf(rho)-vf(z)
        assert lowdepth>=0
        wunit=l7(128*C+68)*pow(l7(128*t+rho)*l7(128*(C-t)+68-rho)%MOD,-1,MOD)%MOD
        weight=((1<<(2*lowdepth))*wunit*wunit*pow(C-t,2*eps,MOD)*invk*invk)%MOD
        acoef=weight*f*f%MOD;dcoef=weight*f*g%MOD
        ansA=(ansA+acoef)%MOD;ansD=(ansD+dcoef)%MOD
        if check:
            w=binmod(128*C+68,128*t+rho)
            assert w==((1<<lowdepth)*wunit*highW*pow(C-t,eps,MOD))%MOD
            high=highJ*highW%MOD
            assert w*w*rawf*rawf%MOD==high*high*acoef%MOD
            assert w*w*rawf*rawg%MOD==high*high*dcoef%MOD
    return ansA,ansD

def direct_whole(D):
    C=4002*D+2532;A=256*C+132;b=128*D+81;S=T=0
    for j in range(b):
        U,V=coefficient_data(A,j);rawf=rawg=0
        for s in range(-10,16):
            mm=binmod(A+b-1-j,b-1-j-s)
            rawf=(rawf+U.get(s,0)*mm)%MOD;rawg=(rawg+V[s]*mm)%MOD
        w=binmod(128*C+68,j)
        S=(S+w*w*rawf*rawf)%MOD;T=(T+w*w*rawf*rawg)%MOD
    # Retain the actual exterior endpoint, including +1.
    theta=sum(v*comb(b-1,r) for r,v in enumerate(P))%128
    qq=sum(v*comb(b-1,r) for r,v in enumerate([180,164,152,6,112,48,192,8,32,160,64,240,0,0,0,128]))%256
    eta=(qq-sum(ba*(-1)**(a+1)*binmod(A+a,a+1) for a,ba in enumerate(EXTERIOR)))%256
    wb=binmod(128*C+68,b)
    sb=wb*wb*b*b*theta*theta%MOD
    tb=wb*wb*b*theta*(1+b*eta-2*b*theta)%MOD
    assert sb==tb==0,(D,sb,tb)
    sumA=sumD=0
    for t in range(D+1):
        lowA,lowD=block(D,t,end=(t==D))
        high=binmod(C,t)*binmod(2*C+D-t,D-t)%MOD
        sumA=(sumA+high*high*lowA)%MOD;sumD=(sumD+high*high*lowD)%MOD
    assert (S,T)==(sumA,sumD),(D,S,T,sumA,sumD)
    assert S%4==0 and T%8==0
    return {'D_auxiliary':D,'b':b,'n':128*C+66,'N_mod256':S//4,'defect_H_minus_N_mod128':T//8,
            'H_mod128':(S//4+T//8)%128,'complete_high_reduction_match':True}

def main():
    states=[];period=[]
    for dp,tp in [(1,0),(1,1),(1,7),(3,0),(3,1),(3,2),(7,3),(15,7),(127,31),(255,127),(511,255),(513,511),(767,512),(1023,1023)]:
        D=dp+4096;t=tp+1024
        aa,dd=block(D,t,check=True)
        shiftedD=block(D+512,t);shiftedt=block(D,t+512)
        period.append({'D_mod1024':dp,'t_mod1024':tp,'D512_match':shiftedD==(aa,dd),'t512_match':shiftedt==(aa,dd)})
        states.append({'D_mod1024':dp,'t_mod1024':tp,'A_full_mod1024':aa,'D_full_mod1024':dd})
    terminal=[{'D_mod1024':d,'A_end_mod1024':block(d+4096,d+4096,True)[0],
               'D_end_mod1024':block(d+4096,d+4096,True)[1]} for d in (1,3,7,127,511,1023)]
    whole=[direct_whole(d) for d in (1,3,5,7)]
    report={'status':'FINITE_JOINT_REDUCTION_PROBE_PASS','low_states':states,'period512_finite_probes':period,
            'terminal_states':terminal,'complete_auxiliary_sums':whole,
            'scope':'Bounded arithmetic diagnostics on odd affine D, with full direct and stripped reconstruction. No universal coefficient identity, original exponent reachability, or actual infinite alignment is claimed.'}
    (OUT/'binary128_joint_probe_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__':main()
