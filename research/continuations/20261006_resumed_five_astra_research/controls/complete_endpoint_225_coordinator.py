#!/usr/bin/env python3
"""Personally authored bounded n=225 complete-force/content corroboration.

Only exact rational/integer arithmetic. No network, credentials or remote code.
The finite result is not a family growth theorem or irrationality proof.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb, factorial, gcd, lcm
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.set_int_max_str_digits(100000)

def mulq(poly):
    out = [F(0)]*(len(poly)+2)
    for j, a in enumerate(poly):
        out[j] += a
        out[j+1] -= a
        out[j+2] += a/2
    return out

def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def mv(A, b):
    return [dot(row,b) for row in A]

def determinant(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def adjugate(A):
    out = [[F(0)]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != j]
            cols = [c for c in range(3) if c != i]
            out[i][j] = (-1)**(i+j)*(A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]])
    return out

def primitive_rationals(values):
    clear = lcm(*(x.denominator for x in values))
    ints = [int(clear*x) for x in values]
    content = gcd(*map(abs,ints))
    assert content
    return F(clear,content), [a//content for a in ints]

def valuation(n,p):
    assert n
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v

def serial(value):
    if isinstance(value,F):
        return {'numerator':str(value.numerator),'denominator':str(value.denominator)}
    if isinstance(value,int) and not isinstance(value,bool):
        return str(value)
    if isinstance(value,dict):
        return {k:serial(v) for k,v in value.items()}
    if isinstance(value,list):
        return [serial(v) for v in value]
    return value

def main():
    n=225
    fac=[factorial(i) for i in range(2*n+3)]
    qp=[F(1)]
    for _ in range(n):
        qp=mulq(qp)
    alog=[F(1),F(1)]
    for i in range(2,2*n+2):
        alog.append(alog[-1]-alog[-2]/2)
    exponential=[]
    complete=[]
    exacc=F(0)
    logacc=F(0)
    for N in range(2*n+3):
        exacc+=F(1,fac[N])
        if N:
            logacc+=2*alog[N-1]/N
        exponential.append(fac[N]*exacc)
        complete.append(fac[N]*(exacc+logacc))

    moments={N:sum((qp[j]/fac[N-j] for j in range(min(N,2*n)+1)),F(0)) for N in range(n-2,n+3)}
    T=[[moments[n+i-j] for j in range(3)] for i in range(3)]
    det=determinant(T)
    assert det
    adj=adjugate(T)
    for i in range(3):
        for j in range(3):
            assert sum(T[i][k]*adj[k][j] for k in range(3)) == (det if i==j else 0)

    tau=[F(1),F(1)]
    rho=[F(0),F(1)]
    for k in range(n+1):
        tau.append(((2*k+3)*tau[-1]+(k+1)*tau[-2])/(k+2))
        rho.append(((2*k+3)*rho[-1]+(k+1)*rho[-2])/(k+2))
    for N in (n,n+1,n+2):
        assert tau[N] == sum((F(comb(N,2*k)*comb(2*k,k),1<<k) for k in range(N//2+1)),F(0))
    assert tau[n]*rho[n+1]-tau[n+1]*rho[n] == F((-1)**n,n+1)
    t=[sum((qp[j]*comb(2*n+i-j,n) for j in range(n+i+1)),F(0)) for i in range(3)]
    assert t==[tau[n],(tau[n]+tau[n+1])/2,tau[n+2]/2]

    w=[]
    we=[]
    for i in range(3):
        terms=range(n+i+1)
        w.append(sum((qp[j]*F(fac[n+i],fac[n+i-j])*complete[2*n+i-j] for j in terms),F(0)))
        we.append(sum((qp[j]*F(fac[n+i],fac[n+i-j])*exponential[2*n+i-j] for j in terms),F(0)))
    zhat=[fac[n]*x for x in t]
    what=[w[i]/fac[n+i] for i in range(3)]
    wehat=[we[i]/fac[n+i] for i in range(3)]
    x=[a/det for a in mv(adj,zhat)]
    y=[a/det for a in mv(adj,what)]
    S=[[F(1),F(-n),F(n*(n+1))],[F(0),F(1),F(-2*n)],[F(0),F(0),F(1)]]
    sx,sy=mv(S,x),mv(S,y)
    u=[-sx[0],sx[0]-sx[1],sx[1]-sx[2],sx[2]]
    v=[1-sy[0],sy[0]-sy[1],sy[1]-sy[2],sy[2]]
    db=lcm(*(a.denominator for a in u+v))
    U,V=[int(db*a) for a in u],[int(db*a) for a in v]
    contents=[gcd(abs(a),abs(b)) for a,b in zip(U,V)]
    pu,pv=[a//g for a,g in zip(U,contents)],[a//g for a,g in zip(V,contents)]

    L=(1<<(n+1))*lcm(*range(1,n+2))
    t0,t1=int(L*tau[n]),int(L*tau[n+1])
    r0,r1=int(4*L*rho[n]),int(4*L*rho[n+1])
    assert all((L*a).denominator==1 for a in (tau[n],tau[n+1],4*rho[n],4*rho[n+1]))
    Omega=t0*r1-t1*r0
    assert Omega==4*(-1)**n*L*L//(n+1)
    vv=[F(1),F(1,2),F(n+1,2*(n+2))]
    ww=[F(0),F(1,2),F(2*n+3,2*(n+2))]
    rowdata={}
    for j,ell in ((0,[-1,n,-n*(n+1)]),(3,[0,0,1])):
        R=[sum((F(ell[k])*adj[k][i] for k in range(3)),F(0)) for i in range(3)]
        alpha,beta=dot(R,vv),dot(R,ww)
        xi=alpha*tau[n]+beta*tau[n+1]
        Nexp=(det if j==0 else F(0))+dot(R,wehat)
        Nwhole=(det if j==0 else F(0))+dot(R,what)
        assert Nwhole==Nexp+4*fac[n]*(alpha*rho[n]+beta*rho[n+1])
        assert u[j]==fac[n]*xi/det and v[j]==Nwhole/det
        sigma,(AA,BB,EE)=primitive_rationals([alpha,beta,Nexp/fac[n]])
        gamma=gcd(abs(AA),abs(BB))
        assert gamma and gcd(gamma,abs(EE))==1
        aa,bb=AA//gamma,BB//gamma
        X,Y=aa*t0+bb*t1,aa*r0+bb*r1
        M,VR=gamma*X,gamma*Y+L*EE
        gs=gcd(abs(M),abs(VR))
        kappa=F(Omega*bb,t0*X)
        assert kappa==4*(-1)**n*beta/((n+1)*tau[n]*xi)
        assert kappa==F(Y,X)-F(r0,t0)
        denom=kappa.denominator
        assert (abs(Omega)*t0*denom)%abs(X)==0
        assert (t0*abs(X))%denom==0
        cancellation=t0*L*EE+Omega*gamma*bb
        CC=gcd(abs(X),abs(cancellation))
        K=gamma*abs(X)//CC
        assert t0*VR==r0*M+cancellation
        assert (L*CC)%gs==0 and (t0*gs)%CC==0
        dj=abs(M)//gs
        assert dj==(v[j]/u[j]).denominator==abs(pu[j])
        rowdata[j]={'alpha':alpha,'beta':beta,'xi':xi,'Nexp':Nexp,'Nwhole':Nwhole,
                    'sigma':sigma,'Acoef':AA,'Bcoef':BB,'Ecoef':EE,'gamma':gamma,
                    'a_primitive':aa,'b_primitive':bb,'X':X,'Y':Y,'M':M,'V':VR,'content':gs,
                    'kappa':kappa,'kappa_height':max(abs(kappa.numerator),kappa.denominator),
                    'R_cancel':cancellation,'C_cancel':CC,'K':K,'denominator':dj}

    row0,row3=rowdata[0],rowdata[3]
    DD=row0['a_primitive']*row3['b_primitive']-row0['b_primitive']*row3['a_primitive']
    dk=row0['kappa']-row3['kappa']
    assert dk==-F(Omega*DD,row0['X']*row3['X'])
    ZX=abs(row0['X']*row3['X'])//gcd(abs(row0['X']),abs(row3['X']))**2
    ZK=row0['K']*row3['K']//gcd(row0['K'],row3['K'])**2
    h=gcd(abs(pu[0]),abs(pu[3]))
    A,B=pu[0]//h,pu[3]//h
    AB=abs(A*B)
    assert AB==row0['denominator']*row3['denominator']//h**2
    assert (abs(Omega)*dk.denominator)%ZX==0
    assert (L*t0*AB)%ZK==0 and (L*t0*ZK)%AB==0
    selected=1
    local=[]
    for p,pred0,pred3 in ((3,218,220),(5,107,110)):
        v0,v3,vab=valuation(row0['denominator'],p),valuation(row3['denominator'],p),valuation(AB,p)
        assert (v0,v3)==(pred0,pred3)
        selected*=p**vab
        local.append({'p':p,'v_d0':v0,'v_d3':v3,'v_AB':vab})
    assert selected==5*n
    J=B*pv[0]-A*pv[3]
    assert DD
    lambdaref=F(row3['b_primitive']*row0['X'],t0*DD)
    assert lambdaref*row0['kappa']+(1-lambdaref)*row3['kappa']==0
    probes=[]
    for label,lam in (('endpoint3',F(0)),('endpoint0',F(1)),('half',F(1,2)),('n_squared_half',F(n*n,2)),('reference_canceling',lambdaref)):
        aa,kk=lam.numerator,lam.denominator
        TT=aa*J+kk*A*pv[3]
        FF=gcd(abs(A),abs(aa))*gcd(abs(B),abs(aa-kk))
        GG=gcd(kk,abs(J))
        assert TT%(FF*GG)==0
        HH=gcd(h,abs(TT)//(FF*GG))
        q=kk*h*AB//(FF*GG*HH)
        pp=(1 if A*B>0 else -1)*TT//(FF*GG*HH)
        center=lam*v[0]/u[0]+(1-lam)*v[3]/u[3]
        assert center==F(pp,q) and gcd(abs(pp),q)==1
        probes.append({'label':label,'lambda':lam,'F_gcd':FF,'G_gcd':GG,'H_gcd':HH,'p':pp,'q':q,
                       'q_digits':len(str(q)),'whole_error_enclosure_computed':False})
    artifact={'n':n,'d':2,'force_last_index':2*n+2,'moment_indices':list(range(n-2,n+3)),
              'u':u,'v':v,'least_clearer':db,'U':U,'V':V,'all_row_contents':contents,
              'primitive_first':pu,'primitive_second':pv,'T':T,'detT':det,'L':L,'t0':t0,'t1':t1,
              'r0':r0,'r1':r1,'Omega':Omega,'endpoints':{str(j):data for j,data in rowdata.items()},
              'D_primitive':DD,'kappa_difference':dk,'Z_X':ZX,'Z_K':ZK,'h':h,'A':A,'B':B,'AB':AB,
              'selected_part':selected,'complementary_part':AB//selected,'local_valuations':local,'probes':probes}
    target=ROOT/'complete_endpoint_225_certificate.json'
    target.write_text(json.dumps(serial(artifact),indent=2)+'\n')
    receipt={'status':'PASS','scope':'One original n225 complete finite producer and new correction/content identities; no infinite height or growth bound',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'n':n,'all_eight_reconstructed_entries_retained':True,'complete_force_last_index':2*n+2,
             'exterior_plus_one_retained':True,'local_valuations':local,'selected_part':selected,
             'AB_digits':len(str(AB)),'complementary_part_digits':len(str(AB//selected)),
             'kappa_height_digits':{str(j):len(str(rowdata[j]['kappa_height'])) for j in (0,3)},
             'primitive_moment_pair_height_digits':{str(j):len(str(max(abs(rowdata[j]['a_primitive']),abs(rowdata[j]['b_primitive'])))) for j in (0,3)},
             'primitive_probes':[{'label':z['label'],'q_digits':z['q_digits']} for z in probes],
             'whole_error_enclosure_computed':False,'irrationality_proved':False}
    (ROOT/'complete_endpoint_225_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
