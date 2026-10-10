"""Personally authored exhaustive low-coefficient certificate, not a tail truncation.

Use the safe separate periods 1024, with all 512 odd D residues and 1024 t
residues. Reduce only after exact bounded binomial evaluation. Only odd units
are inverted. All actual floor patterns and terminal zeros are retained.
"""
from pathlib import Path
from math import comb
from collections import Counter
import hashlib,json,time
import numpy as np
import binary128_joint_probe as scalar

OUT=Path(__file__).resolve().parent
M=1024
P=np.array(scalar.P,dtype=np.int64)
Q=np.array(scalar.DELTA,dtype=np.int64)
BETA=scalar.BETA
SHAPES=scalar.SHAPES

def exact_coefficient_tables():
    # A D-shift by 16 has valuation 13; x-shift by 8192 has valuation 13.
    # All binomial lower indices <=15, so these preserve ten bits.
    choose=np.array([[comb(x,r) if r<=x else 0 for r in range(16)]
                     for x in range(8192)],dtype=object)
    choose=np.asarray(choose%M,dtype=np.int64)
    basep=np.zeros((8192,16),dtype=np.int64)
    baseq=np.zeros_like(basep)
    for s in range(16):
        basep[:,s]=(choose[:,:16-s]@P[s:])%M
        baseq[:,s]=(choose[:,:16-s]@Q[s:])%M
    x=np.arange(8192,dtype=np.int64)%M
    xm=(np.arange(8192)-1)%8192
    tables=[]
    for D in range(1,16,2):
        C=4002*D+2532;A=256*C+132
        aa=np.array([comb(A+s-1,s)%M for s in range(16)],dtype=np.int64)
        F=np.zeros((8192,27),dtype=np.int64)
        Z=np.zeros_like(F)
        F[:,10:26]=basep*aa%M;Z[:,10:26]=baseq*aa%M
        for s in range(-9,0):Z[:,s+10]=BETA[-s-1]
        U=(F[:,:26]+x[:,None]*F[xm,:26]+x[:,None]*F[xm,1:27])%M
        V=(Z[:,:26]+x[:,None]*Z[xm,:26]+x[:,None]*Z[xm,1:27])%M
        tables.append((U.reshape(64,128,26),V.reshape(64,128,26)))
    UT=np.stack([v[0] for v in tables]);VT=np.stack([v[1] for v in tables])
    # Independent direct exact evaluations of representative full columns.
    for D,t,rho in [(1,0,0),(3,63,127),(15,1,85),(1023,1023,68),(513,512,80)]:
        C=4002*(D+4096)+2532;A=256*C+132;x=128*(t+1024)+rho
        us,vs=scalar.coefficient_data(A,x)
        i=(D%16-1)//2
        assert all(int(UT[i,t%64,rho,s+10])==us.get(s,0) for s in range(-10,16))
        assert all(int(VT[i,t%64,rho,s+10])==vs[s] for s in range(-10,16))
    return UT,VT

def low_unit_tables():
    idx=np.arange(65536,dtype=np.int64)
    L=np.ones(65536,dtype=np.int64)
    O=np.array(scalar.ODD,dtype=np.int64)
    for i in range(7):L=L*O[(idx>>i)%M]%M
    inverses=np.zeros(M,dtype=np.int64)
    for i in range(1,M,2):inverses[i]=pow(i,-1,M)
    assert np.all(L%2==1)
    return L,inverses[L],inverses

def solve_batch(D,T,UT,VT,L,LI,OI,terminal=False):
    # D and T broadcast to the full finite rectangle (or terminal column).
    C=4002*D+2532;k=2*C+1;d=D-T;K=k+d
    shape=np.broadcast_shapes(D.shape,T.shape)
    asum=np.zeros(shape,dtype=np.int64);dsum=np.zeros_like(asum)
    di=(D%16-1)//2;ti=T%64
    for rho in range(81 if terminal else 128):
        eps=int(rho>=69);z=68-rho+128*eps
        dep=127*eps+scalar.vf(68)-scalar.vf(rho)-scalar.vf(z)
        assert dep>=0
        if dep>=5:continue   # exact raw factor 2^(2dep) is zero mod1024
        f=np.zeros(shape,dtype=np.int64);g=np.zeros_like(f)
        u=UT[di,ti,rho,:];v=VT[di,ti,rho,:]
        for s in range(-10,16):
            a0,e0,c0,a,ell,c,exponent=SHAPES[rho,s]
            if terminal and e0==-1:continue  # negative actual lower moment
            if exponent>=10:continue
            pattern=(a0,e0,c0)
            if pattern==(0,0,0):pol=K%M
            elif pattern==(0,-1,0):pol=(K%M)*(d%M)%M
            elif pattern==(0,0,-1):pol=(K%M)*(k%M)%M
            elif pattern==(-1,-1,0):pol=d%M
            elif pattern==(-1,0,-1):pol=k%M
            elif pattern==(-1,-1,-1):pol=(d%M)*(k%M)%M
            else:raise AssertionError(pattern)
            iu=((K+a0)%512)*128+a
            il=((d+e0)%512)*128+ell
            ic=((k+c0)%512)*128+c
            mult=L[iu]*LI[il]%M*LI[ic]%M
            mult=mult*pol%M*(1<<exponent)%M
            f=(f+u[...,s+10]*mult)%M;g=(g+v[...,s+10]*mult)%M
        iw=(C%512)*128+68
        it=(T%512)*128+rho
        ic=((C-T-eps)%512)*128+z
        w=L[iw]*LI[it]%M*LI[ic]%M
        scale=w*w%M*OI[k%M]%M*OI[k%M]%M*(1<<(2*dep))%M
        if eps:scale=scale*(C-T)%M*(C-T)%M
        asum=(asum+scale*f%M*f)%M
        dsum=(dsum+scale*f%M*g)%M
    return asum,dsum

def distributions(a):
    return {str(int(k)):int(v) for k,v in sorted(Counter(a.flatten()).items())}

def depths(a):
    return {str(k):sum(v for r,v in Counter(a.flatten()).items()
                        if (10 if r==0 else (int(r)&-int(r)).bit_length()-1)==k)
            for k in range(11)}

def main():
    started=time.monotonic();UT,VT=exact_coefficient_tables();L,LI,OI=low_unit_tables()
    fullA=np.zeros((512,1024),dtype=np.uint16);fullD=np.zeros_like(fullA)
    for begin in range(0,512,8):
        D=(np.arange(begin,begin+8)*2+1+4096)[:,None]
        T=(np.arange(1024)+1024)[None,:]
        a,d=solve_batch(D,T,UT,VT,L,LI,OI)
        fullA[begin:begin+8]=a;fullD[begin:begin+8]=d
        if begin%64==0:print(json.dumps({'completed_D_states':begin+8,'elapsed_seconds':round(time.monotonic()-started,2)}),flush=True)
    Dr=(np.arange(512)*2+1+4096)[:,None]
    ea,ed=solve_batch(Dr,Dr,UT,VT,L,LI,OI,True)
    endA=np.asarray(ea[:,0],dtype=np.uint16);endD=np.asarray(ed[:,0],dtype=np.uint16)
    probe=json.loads((OUT/'binary128_joint_probe_certificate.json').read_text())
    for s in probe['low_states']:
        i=(s['D_mod1024']-1)//2;t=s['t_mod1024']
        assert int(fullA[i,t])==s['A_full_mod1024']
        assert int(fullD[i,t])==s['D_full_mod1024']
    for s in probe['terminal_states']:
        i=(s['D_mod1024']-1)//2
        assert int(endA[i])==s['A_end_mod1024'] and int(endD[i])==s['D_end_mod1024']
    assert np.array_equal(fullA[:256],np.roll(fullA[256:],512,axis=1))
    assert np.array_equal(fullD[:256],np.roll(fullD[256:],512,axis=1))
    assert np.array_equal(endA[:256],endA[256:]) and np.array_equal(endD[:256],endD[256:])
    dest=OUT/'binary1024_full_low_tables.npz'
    np.savez_compressed(dest,full_A=fullA,full_D=fullD,end_A=endA,end_D=endD)
    nz=np.argwhere(fullD!=0);enz=np.argwhere(endD!=0).flatten()
    exceptional=[{'D_mod1024':int(2*i+1),'t_mod1024':int(t),'mixed':int(fullD[i,t])} for i,t in nz]
    (OUT/'binary1024_mixed_exceptions.json').write_text(json.dumps({'full':exceptional,'terminal':[{'D_mod1024':int(2*i+1),'mixed':int(endD[i])} for i in enz]},indent=2)+'\n')
    cert={'status':'EXHAUSTIVE_LOW_COEFFICIENT_TABLE_COMPLETE',
          'full_state_count':int(fullD.size),'terminal_state_count':int(endD.size),'modulus':M,
          'all_full_mixed_zero':not len(nz),'all_terminal_mixed_zero':not len(enz),
          'full_norm_distribution':distributions(fullA),'full_mixed_distribution':distributions(fullD),
          'terminal_norm_distribution':distributions(endA),'terminal_mixed_distribution':distributions(endD),
          'full_norm_depth_distribution':depths(fullA),'full_mixed_depth_distribution':depths(fullD),
          'separate_D512_period_verified':bool(np.array_equal(fullA[:256],fullA[256:]) and np.array_equal(fullD[:256],fullD[256:])),
          'separate_t512_period_verified':bool(np.array_equal(fullA[:,:512],fullA[:,512:]) and np.array_equal(fullD[:,:512],fullD[:,512:])),
          'proved_diagonal_period_consistency':True,'existing_scalar_probe_match':True,
          'table_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'elapsed_seconds':round(time.monotonic()-started,2),
          'scope':'Exhaustive auxiliary low coefficients only. Combine with proved safe periods, exact high reduction, force precision, and terminal endpoint bounds for original H-N congruence. Norm digits and full gcd remain open.'}
    (OUT/'binary1024_universal_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps(cert),flush=True)

if __name__=='__main__':main()
