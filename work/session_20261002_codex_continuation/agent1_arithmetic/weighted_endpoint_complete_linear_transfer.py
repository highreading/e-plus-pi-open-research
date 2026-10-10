"""L24 complete primitive endpoint modulo8, fixed linear-transfer certificate.

No new complete determinant nodes. The fixed rational norm machine and all
linear endpoint corrections are combined at finite residue/state level.
"""
from pathlib import Path
from math import comb
import json
from weighted_endpoint_rational_norm_machine import pack,unpack,add,sub,scale,mul,power,sumring
from weighted_endpoint_first_transfer import step,index
from weighted_endpoint_binary_inverse import rho,inputs,matvec
from weighted_branch_mod8_lift import series
from weighted_regular_dyadic_subfamily import eo_residues

BASE=Path(__file__).resolve().parent
KAPPA=[1,5,7,3]


def setup():
    saved=json.loads((BASE/'WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json').read_text())
    O,E=[series(num,saved['common_denominator_D_power5'],963)
         for num in saved['numerators_O_E_mod8']]
    rr=[[rho(O if j%2 else E,d,j//2) for d in range(480)] for j in range(1,5)]
    assert all(rr[j-1][0]==rho(O if j%2 else E,480,j//2) for j in range(1,5))
    moments=json.loads((BASE/'WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json').read_text())
    zeta=pack(moments['zeta_coefficients']);eta=power(zeta,5)
    rising=[]
    for row in moments['positive_order_rho_polynomials_degree_at_most10']:
        modes=[]
        for mode in row['four_modes']:
            cc=[pack(a) for a in mode['integer_valued_Newton_coefficients'][:5]]
            qq=[sumring([scale(cc[t],(-1)**(t-s)*comb(t,s)) for t in range(s,5)]) for s in range(5)]
            assert all(all(x%4==0 for x in unpack(qq[s])) for s in (3,4))
            assert all(all(x%2==0 for x in unpack(qq[s])) for s in (1,2))
            modes.append(qq)
        rising.append(modes)
    e,o=eo_residues(15)
    return rr,rising,zeta,eta,e,o


def ell_periodic(p,e,o):
    # Fixed small coefficient extraction is justified by the F16 subset
    # formula; this is not a growing Gram or full endpoint calculation.
    m=32 if p==2 else 128
    out=[]
    for d in range(30):
        row=[]
        for s in range(2):
            z=(o if s==0 else e)[(m+d)%15]
            if d%2==0:
                for f in range(0,m,2):
                    if d&f:continue
                    x0=((1,1),(0,0),(1,0))[f%3]
                    z^=e[(d+f+1)%15]*x0[s^1]
            row.append(z)
        out.append(row)
    return out


def row_base(p,rr,rising,zeta,eta):
    mc=32 if p==2 else 8;qc=8 if p==2 else 32
    ah=[scale(sumring([scale(power(eta,(-a*d)%3),val) for d,val in enumerate((1,1,0))]),3)
        for a in range(3)]
    # Cache each finite K difference by phase,quarter,unit root and rmod60.
    K={}
    for q in range(4):
        for nu in (1,2,4,8):
            for a in range(3):
                z=power(zeta,(nu+5*a)%15)
                pair=[]
                for sign in (1,-1):
                    zz=scale(z,sign);u=sub(1,zz);inv=power(u,59)
                    assert mul(u,inv)==1
                    tail=1
                    for b,c in ((1,4),(2,2),(3,4)):
                        if q>=b:tail=add(tail,scale(power(u,qc*b),c))
                    numerator=sub(1,mul(power(zz,mc),tail))
                    pair.append([mul(power(inv,r+1),numerator) for r in range(60)])
                K[q,nu,a]=[sub(x,y) for x,y in zip(*pair)]
    table=[[[0]*480 for _ in range(2)] for _ in range(4)]
    for q in range(4):
        for f in range(480):
            for member in range(2):
                z=0;j=2+member # zero-based b3 or b4
                for i,nu in enumerate((1,2,4,8)):
                    for s in range(3):
                        c=scale(mul(rising[j][i][s],power(zeta,nu*f)),comb(f+s,s))
                        for a in range(3):
                            z=add(z,mul(mul(c,ah[a]),K[q,nu,a][(f+s)%60]))
                assert unpack(z)[1:]==(0,0,0)
                table[q][member][f]=unpack(z)[0]
    return table


def terminal(left,p,rr,e,o):
    mm=32 if p==2 else 128
    tables=[]
    for q in range(4):
        out=[]
        for a in range(15):
            for b in range(15):
                total=0
                for ell in range(32):
                    for u in range(32):
                        if ell|u !=31:continue
                        d=32*a+ell;f=32*b+u;cc=(2*(mm-1)-d-f)%15
                        for s in range(2):
                            for t in range(2):
                                total+=left[q][s][d%480]*(e if s==t else o)[cc]*rr[1+t][(mm+f)%480]
                out.append(total%8)
        tables.append(out)
    return tables


def response_at_points(p,rr,e,o):
    mm=32 if p==2 else 128
    hm=256 if p==2 else 64
    M=(p-1)%15;hh=(1 if p==2 else 4)-1
    wM=[3*rr[1+s][(2*mm-1)%480]%8 for s in range(2)]
    wH=[5*rr[1+s][(mm+hm-1)%480]%8 for s in range(2)]
    def c_apply(j,w):return [(e[j%15]*w[0]+o[j%15]*w[1])%8,
                             (o[j%15]*w[0]+e[j%15]*w[1])%8]
    x0=c_apply(M,wM)
    z=c_apply(M,wH);v=c_apply(hh,wM);xH=[(a+b)%8 for a,b in zip(z,v)]
    R0=[2*(rr[1+s][(mm-1)%480]+rr[2+s][(mm-1)%480])%8 for s in range(2)]
    RH=[4*(rr[1+s][(mm+hm-1)%480]+rr[2+s][(mm+hm-1)%480])%8 for s in range(2)]
    return {'x_index0':x0,'x_index_half':xH,'row_boundary_index0':R0,'row_boundary_index_half':RH,
            'row_boundary_contraction':sum(a*b for a,b in zip(R0,x0))+sum(a*b for a,b in zip(RH,xH))}


def w_omega(m,p,rr):
    mm=32 if p==2 else 128
    total=0
    for d in range(m):
        if d%6 in (1,3):total+=2*KAPPA[(4*d)//m]*rr[2][(mm+d)%480]
    total+=2*3*sum(rr[1+s][(2*mm-1)%480] for s in range(2))
    return total%8


def run():
    rr,rising,zeta,eta,e,o=setup();phase_data={}
    for p in (2,8):
        ep=ell_periodic(p,e,o);mm=32 if p==2 else 128
        L=[[[0]*480 for _ in range(2)] for _ in range(4)]
        for q in range(4):
            for d in range(480):
                for s in range(2):
                    k=(d+1)*(KAPPA[q]%4)*rr[0][(mm+d+1)%480] if s==0 else 0
                    L[q][s][d]=(ep[d%30][s]-k)%4
        R=row_base(p,rr,rising,zeta,eta)
        pt=response_at_points(p,rr,e,o)
        delta=[1-2*a for a in ep[0]]
        ellconst=sum(ep[d%30][s]*((1,1),(0,0),(1,0))[d%3][s]
                     for d in range(32 if p==2 else 8) for s in range(2))
        ellconst+=sum(delta)
        phase_data[p]={'ell_period30':ep,'L_terminal':terminal(L,p,rr,e,o),
            'R_terminal':terminal(R,p,rr,e,o),'ell_dot_x0_mod4':ellconst%4,
            'L_quarter_tables':L,'R_quarter_tables':R,
            'L_boundary_contraction':sum(a*b for a,b in zip(delta,pt['x_index0']))%4,
            'row_boundary_contraction':pt['row_boundary_contraction']%8,
            'twice_w_dot_omega_eventual':w_omega(8192 if p==2 else 2048,p,rr),
            'point_responses':pt}
    # One new REPRESENTATION check, not a full determinant/center node:
    # validate every closed row coefficient and every corrected start at
    # h7. The all-degree conclusion uses the identities and orbit closure.
    m=128;B,C,w,t,_=inputs(m);x=matvec(C,w)
    x0=[a for d in range(m) for a in ((1,1),(0,0),(1,0))[d%3]]
    H=[[((B[2*d+1][2*f+1]-B[2*d][2*f])%4)//2 for f in range(m)] for d in range(m)]
    ell=[(w[2*d+(s^1)]+sum(H[d][f]*x0[2*f+(s^1)] for f in range(m))+(d==0))%2
         for d in range(m) for s in range(2)]
    k=[((w[i^1]-t[i])%8)//2 for i in range(2*m)]
    actualL=[(a-b)%4 for a,b in zip(ell,k)]
    data=phase_data[8]
    reconstructedL=[data['L_quarter_tables'][(4*d)//m][s][d%480]
                    for d in range(m) for s in range(2)]
    for s in range(2):reconstructedL[s]=(reconstructedL[s]+1-2*data['ell_period30'][0][s])%4
    assert actualL==reconstructedL
    additive_w=[int(s==1 and d%6 in (1,3)) for d in range(m) for s in range(2)]
    additive_w[-2]+=1;additive_w[-1]+=1
    actualR=[sum(2*a*B[i][j] for i,a in enumerate(additive_w))%8 for j in range(2*m)]
    reconstructedR=[data['R_quarter_tables'][(4*d)//m][s][d%480]
                    for d in range(m) for s in range(2)]
    for s in range(2):
        reconstructedR[s]=(reconstructedR[s]+data['point_responses']['row_boundary_index0'][s])%8
        j=2*(m//2)+s
        reconstructedR[j]=(reconstructedR[j]+data['point_responses']['row_boundary_index_half'][s])%8
    assert actualR==reconstructedR
    assert x[:2]==data['point_responses']['x_index0']
    assert x[m:m+2]==data['point_responses']['x_index_half']
    states=[]
    for q in range(4):
        v=[0]*225
        for b in range(4):
            if q|b==3:v[index(q,b)]=KAPPA[b]
        states.append(v)
    terminal_dot=lambda tt:sum(sum(a*b for a,b in zip(v,tt[q])) for q,v in enumerate(states))%8
    L_from_transfer=(terminal_dot(data['L_terminal'])+data['L_boundary_contraction'])%4
    R_from_transfer=(terminal_dot(data['R_terminal'])+data['row_boundary_contraction'])%8
    assert L_from_transfer==sum(a*b for a,b in zip(actualL,x))%4
    assert R_from_transfer==sum(a*b for a,b in zip(actualR,x))%8
    seen={};orbit=[];outputs=[]
    for t in range(64):
        key=tuple(tuple(v) for v in states)
        if key in seen:
            pre=seen[key];period=t-pre;break
        seen[key]=t;orbit.append(states)
        h=t+7
        if h%2:
            p=2 if h%4==1 else 8;data=phase_data[p]
            dot=lambda tt:sum(sum(a*b for a,b in zip(v,tt[q])) for q,v in enumerate(states))%8
            LL=dot(data['L_terminal']);RR=dot(data['R_terminal'])
            ww=w_omega(2**h,p,rr) if h in (7,9) else data['twice_w_dot_omega_eventual']
            S1={1:2,3:0,5:2,7:4}[h%8];q0=6 if p==2 else 4
            U=(q0-2*S1-2*data['ell_dot_x0_mod4']
                +2*(LL+data['L_boundary_contraction'])
                -RR-data['row_boundary_contraction']+ww)%8
            outputs.append({'bulk_transfer_steps':t,'h':h,'S1':S1,'q0':q0,'L_base':LL,'R_base':RR,
                            'twice_w_dot_omega':ww,'complete_U_mod8':U})
        states=[step(v) for v in states]
    else:raise RuntimeError('No full state closure in bounded transfer certificate')
    # The two phase constants stabilize for odd h>=11. Certify every state
    # in one full period after that threshold, rather than scalar guessing.
    out={'status':'AUTHOR complete endpoint linear residue transfer',
         'full_vector_orbit_preperiod':pre,'full_vector_orbit_period':period,
         'full_vector_orbit':orbit,'phase_data':phase_data,'outputs':outputs,
         'all_checked_scalar_outputs_are4':all(row['complete_U_mod8']==4 for row in outputs),
         'finite_initial_h1_h3_h5_complete_sources':'WEIGHTED_ENDPOINT_BINARY_INVERSE_RECEIPT.json'}
    out['single_h7_full_row_normalization_check']={'L_coefficients_checked':256,'R_coefficients_checked':256,
                'point_responses_checked':2,'terminal_pairings_checked':2,
                'passed':True,'no_complete_new_center_determinant':True}
    (BASE/'WEIGHTED_ENDPOINT_COMPLETE_LINEAR_RECEIPT.json').write_text(json.dumps(out)+'\n')
    print(json.dumps({'preperiod':pre,'period':period,'outputs':outputs,'phase_constants':{
        p:{k:v for k,v in d.items() if k in ('ell_dot_x0_mod4','L_boundary_contraction',
              'row_boundary_contraction','twice_w_dot_omega_eventual')} for p,d in phase_data.items()}},indent=2))


if __name__=='__main__':run()
