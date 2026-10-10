"""Personally authored complete normalized finite binary contact audit.

Auxiliary b81,n4002b respects the continuation congruences but is not9^18+32u.
Symbol and force tails are omitted only with explicit valuation bounds. No keys.
"""
from pathlib import Path
from math import comb
from functools import lru_cache
import hashlib,json
from weighted_force_audit_coordinator import central,L

ROOT=Path(__file__).resolve().parent
P=13;Q=1<<P
prefix=[1]
for i in range(1,Q+1):prefix.append(prefix[-1]*(i if i%2 else 1)%Q)

@lru_cache(None)
def unitfac(n):
    out=1
    while n:
        out=out*pow(prefix[Q],n//Q,Q)*prefix[n%Q]%Q;n//=2
    return out

@lru_cache(None)
def binmod(n,k):
    if k<0 or k>n:return 0
    depth=L(n)-L(k)-L(n-k)
    if depth>=P:return 0
    return ((1<<depth)*unitfac(n)*pow(unitfac(k),-1,Q)*pow(unitfac(n-k),-1,Q))%Q

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col))%Q for col in zip(*b)] for row in a]

def solve(a,b):
    n=len(a);rr=[list(a[i])+list(b[i]) for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if rr[k][j]%2)
        rr[k],rr[j]=rr[j],rr[k];inv=pow(rr[j][j],-1,Q);rr[j]=[inv*x%Q for x in rr[j]]
        for i in range(n):
            if i==j:continue
            x=rr[i][j]
            if x:rr[i]=[(aa-x*bb)%Q for aa,bb in zip(rr[i],rr[j])]
    assert all(rr[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [r[n:] for r in rr]

def symbols(h):
    coeff=[0]*(4*(P-1)+1);dp=[1]
    for a in range(P):
        scalar=((1<<a)*binmod(h,a))%Q
        for s,x in enumerate(dp):coeff[s]=(coeff[s]+scalar*x)%Q
        nxt=[0]*(len(dp)+4)
        for s in range(len(nxt)):
            nxt[s]=sum(comb(s,j)*dp[s-j]*u for j,u in enumerate([0,-1,2,-3,3])
                       if j<=s and 0<=s-j<len(dp))%Q
        dp=nxt
    return coeff

def one(b):
    n=4002*b;h=n//2;k=(h-1)//32
    assert (h-1)%32==0 and k%2==1
    lam=symbols(h);support=[s for s,x in enumerate(lam) if x]
    Nt=[[sum(lam[s]*binmod(n+i,s)*binmod(n+i-s,j) for s in support)%Q
         for j in range(b)] for i in range(b)]
    upper=[[binmod(n,j-i) if j>=i else 0 for j in range(b)] for i in range(b)]
    A=mm(Nt,upper)
    ratio=1;tails=[]
    for t in range(2*P):
        if t:ratio=ratio*(b+t)%Q
        tails.append(ratio)
    assert L(2*P)>=P
    @lru_cache(None)
    def tail(m):return sum(ratio*binmod(m,b+t) for t,ratio in enumerate(tails) if ratio)%Q
    r=[sum(lam[s]*binmod(n+i,s)*tail(2*n+i-s) for s in support)%Q for i in range(b)]
    log_bound=1+L(h)-((2*n+b-1).bit_length()-1)-L(b)
    assert P<=log_bound
    B=[central(h,ell)%Q for ell in range(b)]
    ff=[]
    for i in range(b):
        z=0
        for ell in range(i+1):
            prod=1
            for t in range(ell+1,i+1):prod=prod*(n+t)%Q
            z+=binmod(i,ell)*prod*B[ell]
        ff.append(z%Q)
    sol=solve(A,[[ff[i],r[i]] for i in range(b)])
    assert all(sum(A[i][j]*sol[j][c] for j in range(b))%Q==([ff,r][c][i])
               for i in range(b) for c in range(2))
    W=[binmod(n+2,j) for j in range(b+1)];X2=[];Y4=[]
    for j in range(b+1):
        cur=[(j*(sol[j-1][c] if j else 0)-(sol[j][c] if j<b else 0))%Q for c in range(2)]
        X2.append(W[j]*cur[0]%Q);Y4.append(W[j]*(cur[1]+int(j==b))%Q)
    norm=sum(x*x for x in X2)%Q;mixed=sum(x*y for x,y in zip(X2,Y4))%Q
    assert norm%4==0 and mixed%8==0
    def depth(z):return P if not z else (z&-z).bit_length()-1
    first_witness=next((j for j,x in enumerate(Y4) if x),None)
    assert first_witness is not None
    print(json.dumps({'b':b,'n':n,'raw_precision':P,'normalized_second_nonzero_witness':first_witness,
                      'first_content_bounded':min(map(depth,X2)),
                      'second_content_bounded':min(map(depth,Y4)),
                      'N_mod2048':norm//4,'H_mod1024':mixed//8}),flush=True)
    return {'b':b,'n':n,'k':k,'precision':P,'modulus':Q,'symbol_last_degree':len(lam)-1,
            'logarithmic_normalized_depth_bound':log_bound,'factorial_content_depth':L(b),
            'normalized_first_force':ff,'normalized_second_force':r,'X2':X2,'Y4':Y4,
            'complete_contact_residuals_zero':True,'endpoint_Y4':Y4[-1],
            'actual_raw_Vw_zero_modulus':L(b)>=P,
            'normalized_second_nonzero_witness':first_witness,
            'N_mod2048':norm//4,'H_mod1024':mixed//8,
            'first_content_if_below_precision':min(map(depth,X2)),
            'second_content_if_below_precision':min(map(depth,Y4))}

def original_initial(u):
    b=9**(18+32*u);n=4002*b;h=n//2;k=(h-1)//32
    assert (h-1)%32==0 and k%2==1
    lam=symbols(h);support=[s for s,x in enumerate(lam) if x]
    ratios=[1]
    for t in range(1,2*P):ratios.append(ratios[-1]*(b+t)%Q)
    def tail(m):return sum(ratio*binmod(m,b+t) for t,ratio in enumerate(ratios) if ratio)%Q
    r=[sum(lam[s]*binmod(n+i,s)*tail(2*n+i-s) for s in support)%Q for i in (0,1)]
    log_bound=1+L(h)-((2*n+b-1).bit_length()-1)-L(b)
    assert P<=log_bound
    B0,B1=central(h,0)%Q,central(h,1)%Q
    f=[B0,((n+1)*B0+B1)%Q]
    print(json.dumps({'original_u':u,'normalized_first_initial':f,'complete_normalized_second_initial':r}),flush=True)
    return {'u':u,'b':str(b),'n':str(n),'k':str(k),'precision':P,
            'complete_normalized_second_initial':r,'normalized_first_initial':f,
            'logarithmic_normalized_depth_bound':str(log_bound),
            'force_tail_certificate':'t>=26 hasv2(t!)>=13; every complete-symbola>=13 hasdepth>=13; logarithmic normalizeddepth>=13'}

if __name__=='__main__':
    checks=0
    for n in list(range(64))+[257,8191,8192,8193,100003]:
        for k in range(min(n,100)+1):
            assert binmod(n,k)==comb(n,k)%Q;checks+=1
    out={'status':'PASS','scope':'One complete normalized auxiliary finite contact system; it is not an original exponential-family scalar theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'factorial_unit_binomial_checks':checks,'cases':[one(81),one(209)],
         'original_complete_force_initial_cases':[original_initial(u) for u in range(4)]}
    dest=ROOT/'normalized_binary_finite_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:out[k] for k in ['status','scope','source_sha256','factorial_unit_binomial_checks']}
    receipt['cases']=[{k:v for k,v in row.items() if k not in ['normalized_first_force','normalized_second_force','X2','Y4']} for row in out['cases']]
    receipt['original_complete_force_initial_cases']=out['original_complete_force_initial_cases']
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'normalized_binary_finite_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
