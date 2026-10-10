#!/usr/bin/env python3
"""New original n=3375 producer via bounded integer coefficient recurrences.

Reuses personally authored rational linear-algebra helpers only. Does not run
the old225 producer. No network, credential access or unreviewed remote code.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
from pathlib import Path
import hashlib
import json
import resource
import sys
import time
from complete_endpoint_225_coordinator import dot,mv,determinant,adjugate,primitive_rationals,serial

resource.setrlimit(resource.RLIMIT_CPU,(600,600))
sys.set_int_max_str_digits(500000)
ROOT=Path(__file__).resolve().parent

def coefficient_states(n):
    E=1
    for r in range(1,n+1):
        E=r*E+1
    C,Cm,Cmm=1,0,0
    W,Wm,Wmm=E,0,0
    captured={}
    f=1
    for k in range(n+3):
        if k>=n-2:
            captured[k]={'C':C,'W':W,'moment':F(C,(1<<k)*f),'omega':F(W,(1<<k)*f)}
        Cnext=2*(k+1-n)*C+2*k*(2*n-k-1)*Cm+4*k*(k-1)*Cmm
        Wnext=(2*(2*k+1)*W+2*k*(2*n+1-3*k)*Wm+4*k*(k-1)*(k-n-1)*Wmm
               +2*C-4*k*Cm+4*k*(k-1)*Cmm)
        Cmm,Cm,C=Cm,C,Cnext
        Wmm,Wm,W=Wm,W,Wnext
        f*=k+1
    return E,captured

def references(n):
    tau=[F(1),F(1)]
    rho=[F(0),F(1)]
    for k in range(n+1):
        tau.append(((2*k+3)*tau[-1]+(k+1)*tau[-2])/(k+2))
        rho.append(((2*k+3)*rho[-1]+(k+1)*rho[-2])/(k+2))
    assert tau[n]*rho[n+1]-tau[n+1]*rho[n]==F((-1)**n,n+1)
    vv=[F(1),F(1,2),F(n+1,2*(n+2))]
    ww=[F(0),F(1,2),F(2*n+3,2*(n+2))]
    t=[tau[n]*a+tau[n+1]*b for a,b in zip(vv,ww)]
    logarithmic=[4*factorial(n)*(rho[n]*a+rho[n+1]*b) for a,b in zip(vv,ww)]
    return tau,rho,vv,ww,t,logarithmic

def independent_small_check():
    n=17
    E,st=coefficient_states(n)
    qp=[F(1)]
    for _ in range(n):
        out=[F(0)]*(len(qp)+2)
        for k,x in enumerate(qp):
            out[k]+=x;out[k+1]-=x;out[k+2]+=x/2
        qp=out
    fa=[factorial(k) for k in range(2*n+3)]
    exp=[];whole=[];x=F(0);l=F(0)
    alpha=[F(1),F(1)]
    for k in range(2,2*n+3):
        alpha.append(alpha[-1]-alpha[-2]/2)
    for k in range(2*n+3):
        x+=F(1,fa[k])
        if k:l+=2*alpha[k-1]/k
        exp.append(fa[k]*x);whole.append(fa[k]*(x+l))
    assert exp[n]==E
    for k in range(n-2,n+3):
        moment=sum((qp[r]/fa[k-r] for r in range(k+1)),F(0))
        omega=sum((qp[r]*exp[n+k-r]/fa[k-r] for r in range(k+1)),F(0))
        assert moment==st[k]['moment'] and omega==st[k]['omega']
    tau,rho,vv,ww,t,log=references(n)
    for i in range(3):
        complete=sum((qp[r]*whole[2*n+i-r]/fa[n+i-r] for r in range(n+i+1)),F(0))
        assert complete==st[n+i]['omega']+log[i]
        tref=sum((qp[r]*comb(2*n+i-r,n) for r in range(n+i+1)),F(0))
        assert tref==t[i]
    return {'n':17,'complete_force_last_index':36,'moment_checks':5,'exponential_force_checks':5,'full_log_force_checks':3,'reference_checks':3,'status':'PASS'}

def primes_to(N):
    keep=bytearray(b'\x01')*(N+1)
    keep[0:2]=b'\x00\x00'
    for p in range(2,int(N**.5)+1):
        if keep[p]:
            for k in range(p*p,N+1,p):keep[k]=0
    return [p for p in range(2,N+1) if keep[p]]

def strip(x,primes):
    x=abs(x)
    assert x
    valuations={}
    for p in primes:
        v=0
        while x%p==0:x//=p;v+=1
        if v:valuations[p]=v
    return x,valuations

def main():
    start=time.monotonic()
    small=independent_small_check()
    print(json.dumps({'stage':'new_small_exact_check','result':small}),flush=True)
    n=3375
    En,states=coefficient_states(n)
    tau,rho,vv,ww,t,log=references(n)
    moments={k:states[k]['moment'] for k in range(n-2,n+3)}
    wehat=[states[n+i]['omega'] for i in range(3)]
    what=[wehat[i]+log[i] for i in range(3)]
    T=[[moments[n+i-j] for j in range(3)] for i in range(3)]
    det=determinant(T);assert det
    adj=adjugate(T)
    for i in range(3):
        for j in range(3):assert sum(T[i][k]*adj[k][j] for k in range(3))==(det if i==j else 0)
    nf=factorial(n)
    x=[a/det for a in mv(adj,[nf*a for a in t])]
    y=[a/det for a in mv(adj,what)]
    S=[[F(1),F(-n),F(n*(n+1))],[F(0),F(1),F(-2*n)],[F(0),F(0),F(1)]]
    sx,sy=mv(S,x),mv(S,y)
    u=[-sx[0],sx[0]-sx[1],sx[1]-sx[2],sx[2]]
    v=[1-sy[0],sy[0]-sy[1],sy[1]-sy[2],sy[2]]
    db=lcm(*(a.denominator for a in u+v))
    U,V=[int(db*a) for a in u],[int(db*a) for a in v]
    contents=[gcd(abs(a),abs(b)) for a,b in zip(U,V)]
    pu,pv=[a//g for a,g in zip(U,contents)],[a//g for a,g in zip(V,contents)]
    assert all(gcd(abs(a),abs(b))==1 for a,b in zip(pu,pv))
    L=(1<<(n+1))*lcm(*range(1,n+2))
    t0,t1=int(L*tau[n]),int(L*tau[n+1])
    r0,r1=int(4*L*rho[n]),int(4*L*rho[n+1])
    assert all((L*a).denominator==1 for a in (tau[n],tau[n+1],4*rho[n],4*rho[n+1]))
    Omega=t0*r1-t1*r0
    assert Omega==4*(-1)**n*L*L//(n+1)
    primes=primes_to(n+2)
    endpoints={}
    for j,ell in ((0,[-1,n,-n*(n+1)]),(3,[0,0,1])):
        R=[sum((F(ell[k])*adj[k][i] for k in range(3)),F(0)) for i in range(3)]
        alpha,beta=dot(R,vv),dot(R,ww)
        xi=alpha*tau[n]+beta*tau[n+1]
        Nexp=(det if j==0 else F(0))+dot(R,wehat)
        Nwhole=(det if j==0 else F(0))+dot(R,what)
        assert Nwhole==Nexp+4*nf*(alpha*rho[n]+beta*rho[n+1])
        assert u[j]==nf*xi/det and v[j]==Nwhole/det
        sigma,(AA,BB,EE)=primitive_rationals([alpha,beta,Nexp/nf])
        gamma=gcd(abs(AA),abs(BB));assert gamma and gcd(gamma,abs(EE))==1
        aa,bb=AA//gamma,BB//gamma
        X,Y=aa*t0+bb*t1,aa*r0+bb*r1
        M,VR=gamma*X,gamma*Y+L*EE
        gs=gcd(abs(M),abs(VR));dj=abs(M)//gs
        assert dj==(v[j]/u[j]).denominator==abs(pu[j])
        R0=t0*L*EE+Omega*gamma*bb
        R1=t1*L*EE-Omega*gamma*aa
        Csharp=gcd(abs(X),abs(R0),abs(R1))
        assert R0==t0*VR-r0*M and R1==t1*VR-r1*M
        dlarge,dsmall=strip(dj,primes)
        glarge,gsmall=strip(gamma,primes)
        clarge,csmall=strip(Csharp,primes)
        xlarge,xsmall=strip(X,primes)
        assert dlarge==glarge*xlarge//clarge
        kappa=F(Omega*bb,t0*X)
        endpoints[j]={'alpha':alpha,'beta':beta,'Nexp':Nexp,'Nwhole':Nwhole,'sigma':sigma,
                      'Acoef':AA,'Bcoef':BB,'Ecoef':EE,'gamma':gamma,'a_primitive':aa,'b_primitive':bb,
                      'X':X,'Y':Y,'M':M,'V':VR,'content':gs,'denominator':dj,'kappa':kappa,
                      'R0':R0,'R1':R1,'Csharp':Csharp,'denominator_large':dlarge,'denominator_small_valuations':dsmall,
                      'gamma_large':glarge,'Csharp_large':clarge,'X_large':xlarge}
    e0,e3=endpoints[0],endpoints[3]
    h=gcd(abs(pu[0]),abs(pu[3]));A,B=pu[0]//h,pu[3]//h;AB=abs(A*B)
    assert AB==e0['denominator']*e3['denominator']//h**2
    ABl,ABs=strip(AB,primes)
    selected=1
    for p in (3,5):selected*=p**ABs.get(p,0)
    J=B*pv[0]-A*pv[3]
    DD=e0['a_primitive']*e3['b_primitive']-e0['b_primitive']*e3['a_primitive'];assert DD
    lamref=F(e3['b_primitive']*e0['X'],t0*DD)
    probes=[]
    for label,lam in [('endpoint3',F(0)),('endpoint0',F(1)),('half',F(1,2)),('n_squared_half',F(n*n,2)),('reference_canceling',lamref)]:
        aa,kk=lam.numerator,lam.denominator
        TT=aa*J+kk*A*pv[3]
        FF=gcd(abs(A),abs(aa))*gcd(abs(B),abs(aa-kk));GG=gcd(kk,abs(J))
        assert TT%(FF*GG)==0
        HH=gcd(h,abs(TT)//(FF*GG))
        q=kk*h*AB//(FF*GG*HH);pp=(1 if A*B>0 else -1)*TT//(FF*GG*HH)
        assert gcd(abs(pp),q)==1 and F(pp,q)==lam*v[0]/u[0]+(1-lam)*v[3]/u[3]
        probes.append({'label':label,'lambda':lam,'p':pp,'q':q,'q_digits':len(str(q))})
    bm,cm,dm=moments[n-1],moments[n],moments[n+1]
    Dmom=(1<<n)*factorial(n+2)
    momentints=[int(Dmom*a) for a in (bm,cm,dm)]
    assert all((Dmom*a).denominator==1 for a in (bm,cm,dm))
    momentcontent=gcd(*map(abs,momentints));epsilon=2 if n%4==1 else 1
    assert momentcontent==(1<<n)*(n+2)*epsilon
    H=bm+(n-3)*cm-2*(n-1)*dm
    B0=6*dm-(n+6)*cm;B3=2*(n+2)*dm-(n+3)*cm
    f1=factorial(n+1)
    hi,b0i,b3i=[int(f1*a) for a in (H,B0,B3)]
    assert all((f1*a).denominator==1 for a in (H,B0,B3))
    Pn=n*n+5*n+3
    Wdef=gcd(abs(hi),abs(b0i),Pn)
    assert gcd(abs(hi),abs(b0i),abs(b3i))==2*Wdef and Wdef%3
    Hlarge,_=strip(hi,primes)
    gamma_common=gcd(e0['gamma_large'],e3['gamma_large'])
    Wlarge,_=strip(Wdef,primes)
    assert gamma_common==Wlarge
    gamma_product=e0['gamma_large']*e3['gamma_large']
    assert (Hlarge*Wlarge)%gamma_product==0
    artifact={'status':'PASS','n':n,'d':2,'complete_force_last_index':2*n+2,'small_direct_check':small,
              'fixed_exponential_seed':En,'moment_states':states,'T':T,'detT':det,'tau_n':tau[n],'tau_n1':tau[n+1],
              'rho_n':rho[n],'rho_n1':rho[n+1],'wehat':wehat,'what':what,'u':u,'v':v,'least_clearer':db,
              'U':U,'V':V,'all_row_contents':contents,'primitive_first':pu,'primitive_second':pv,
              'L':L,'t0':t0,'t1':t1,'r0':r0,'r1':r1,'Omega':Omega,'endpoints':{str(j):z for j,z in endpoints.items()},
              'h':h,'A':A,'B':B,'AB':AB,'AB_large':ABl,'AB_small_valuations':ABs,'selected_part':selected,
              'probes':probes,'Dmom':Dmom,'moment_content':momentcontent,'H':H,'B0':B0,'B3':B3,
              'normalized_H':hi,'normalized_B0':b0i,'normalized_B3':b3i,'Pn':Pn,'common_defect_W':Wdef,
              'gamma_common_large':gamma_common,'whole_error_enclosure_computed':False,'irrationality_proved':False}
    target=ROOT/'complete_endpoint_3375_certificate.json'
    target.write_text(json.dumps(serial(artifact),indent=2)+'\n')
    receipt={'status':'PASS','scope':'ONE new original n3375 complete producer and all-prime primitive normalization; no infinite growth or whole-error theorem',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'helper_source_sha256':hashlib.sha256((ROOT/'complete_endpoint_225_coordinator.py').read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'n':n,'elapsed_seconds':round(time.monotonic()-start,3),
             'complete_force_last_index':2*n+2,'all_eight_reconstruction_entries_retained':True,'exterior_plus_one_retained':True,
             'small_direct_check':small,'all_row_content_digits':[len(str(a)) for a in contents],
             'AB_digits':len(str(AB)),'AB_large_above_n2_digits':len(str(ABl)),'selected_part':str(selected),
             'AB_small_valuations':ABs,'endpoint_denominator_small_valuations':{str(j):z['denominator_small_valuations'] for j,z in endpoints.items()},
             'endpoint_gamma_large_digits':{str(j):len(str(z['gamma_large'])) for j,z in endpoints.items()},
             'endpoint_Csharp_large_digits':{str(j):len(str(z['Csharp_large'])) for j,z in endpoints.items()},
             'moment_content_identity_pass':True,'common_defect_identity_pass':True,'common_defect_W':str(Wdef),
             'common_gamma_large':str(gamma_common),'probes':[{'label':z['label'],'q_digits':z['q_digits']} for z in probes],
             'whole_error_enclosure_computed':False,'irrationality_proved':False}
    (ROOT/'complete_endpoint_3375_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()
