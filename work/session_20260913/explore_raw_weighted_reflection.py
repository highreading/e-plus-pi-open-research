"""Closed n=8,16,32 exploratory row-matrix calculation; no HP solve."""
from pathlib import Path
import sys, json, time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import mpmath as mp
mp.mp.dps=120

def aa(k):
    return mp.mpf(0) if k==0 else k*k/mp.sqrt(4*k*k-1)

def tt(k):
    return mp.mpf(0) if k<0 else (k+1)/(2*mp.sqrt((2*k+1)*(2*k+3)))

def reflection(N):
    ec=mp.matrix(N,N)
    for k in range(N):
        for j in range(k%2,k+1,2):
            ec[j,k]=mp.sqrt(2*k+1)*mp.factorial(k+j)/(2**k*mp.factorial((k-j)//2)*mp.factorial((k+j)//2)*mp.factorial(j)**2)
    C=mp.matrix(N,N)
    for k in range(N):
        r=[(-1)**j*mp.fsum(ec[h,k]*mp.binomial(h,j) for h in range(j,k+1)) for j in range(k+1)]
        for j in range(k,-1,-1):
            C[j,k]=(r[j]-mp.fsum(ec[j,h]*C[h,k] for h in range(j+1,k+1)))/ec[j,j]
    return C

def nodes(n):
    out={}; residuals=[]
    cutoff=n+28
    for parity in (0,1):
        inds=list(range(parity,cutoff+1,2)); S=mp.matrix(len(inds))
        for j,l in enumerate(inds):
            S[j,j]=l*(l+1)+mp.mpf(3)/4+tt(l-1)**2+tt(l)**2
            if j+1<len(inds): S[j,j+1]=S[j+1,j]=tt(l)*tt(l+1)
        vals,vecs=mp.eigsy(S)
        for j,l in enumerate(inds):
            if l<=n:
                out[l]=vals[j]
                residuals.append(abs(tt(inds[-1])*tt(inds[-1]+1)*vecs[-1,j]))
    return out,max(residuals)

def onorm(A):
    return mp.svd(A,compute_uv=False)[0]

def channel_angle(A,B):
    qa,ra=mp.qr(A); qb,rb=mp.qr(B)
    qa=qa[:,:A.cols]; qb=qb[:,:B.cols]
    c=onorm(qa.T*qb)
    delta=mp.sqrt(1-c)
    err=max(onorm(qa.T*qa-mp.eye(A.cols)),onorm(qb.T*qb-mp.eye(B.cols)))
    return delta,err

ans=[]
for n in (8,16,32):
    start=time.time(); N=2*n
    K=mp.matrix(N)
    for k in range(N):
        K[k,k]=aa(k)**2+aa(k+1)**2-k*(k+1)
        if k+1<N: K[k,k+1]=K[k+1,k]=-aa(k+1)
        if k+2<N: K[k,k+2]=K[k+2,k]=aa(k+1)*aa(k+2)
    lam,V=mp.eigsy(K)
    C=reflection(N); cv=V.T*C*V
    xi,nres=nodes(n)
    b=min(n,int(mp.ceil(2*mp.sqrt(n))))
    high=[[l for l in range(b+1,n+1) if l%2==s] for s in (0,1)]
    if len(high[0])>len(high[1]): high[0].pop()
    if len(high[1])>len(high[0]): high[1].pop()
    sigma_b=1 if high[1] and high[1][0]>high[0][0] else 0
    betas=[xi[l] for l in high[sigma_b]]
    logf=[mp.fsum(mp.log(be-la) for be in betas) for la in lam]
    logf=[a-min(logf) for a in logf]
    sqrtf=[mp.exp(a/2) for a in logf]
    J=mp.matrix([[cv[i,j]*sqrtf[j]/sqrtf[i] for j in range(N)] for i in range(N)])
    full=onorm(J); cnorm=onorm(C)
    assert full >= 1-mp.mpf('1e-80')
    spaces=[]; spaces_un=[]
    for parity in (0,1):
        roots=[xi[l] for l in range(parity,n+1,2)]
        d=n-len(roots)
        seed=[V[0,i] if parity==0 else V[1,i]-mp.sqrt(3)/2*V[0,i] for i in range(N)]
        Z=mp.matrix(N,d)
        for i,la in enumerate(lam):
            fac=mp.fprod((la-rt)/(N*N) for rt in roots)*seed[i]
            z=2*(la-lam[0])/(lam[-1]-lam[0])-1
            old=mp.mpf(1); cur=z
            for j in range(d):
                val=old if j==0 else cur
                Z[i,j]=fac*val
                if j>=1: old,cur=cur,2*z*cur-old
        spaces_un.append(Z)
        spaces.append(mp.matrix([[Z[i,j]/sqrtf[i] for j in range(d)] for i in range(N)]))
    delta,orth=channel_angle(*spaces)
    du,orthu=channel_angle(*spaces_un)
    item={"n":n,"N":N,"cutoff":b,"high_factor_count":len(betas),
          "log_norm_C":str(mp.log(cnorm)),"log_norm_full_JF":str(mp.log(full)),
          "minus_log_delta_actual":str(-mp.log(delta)),
          "minus_log_delta_unweighted":str(-mp.log(du)),
          "log_cond_F":str(max(logf)),"node_residual_estimate":str(nres),
          "orthogonality_residual":str(max(orth,orthu)),
          "reflection_involution_residual":str(onorm(C*C-mp.eye(N))),
          "seconds":time.time()-start}
    ans.append(item)
    (HERE/'raw_weighted_reflection_exploration.json').write_text(json.dumps({
        'status':'Exploratory high precision; not interval-certified; no asymptotic inference',
        'predeclared_indices':[8,16,32],'decimal_precision':120,'data':ans},indent=2)+'\n')
    print(json.dumps(item),flush=True)
