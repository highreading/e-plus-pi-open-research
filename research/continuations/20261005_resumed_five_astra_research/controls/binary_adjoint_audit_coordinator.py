"""Personally authored binary band/boundary and adjoint moment audit.

Uses two previously certified complete auxiliary systems, not original huge
indices. All finite boundaries and the exterior reconstructed endpoint survive.
"""
from pathlib import Path
from math import comb
import hashlib,json
from normalized_binary_finite_audit_coordinator import Q,P,binmod,symbols,mm,solve
from weighted_force_audit_coordinator import L

ROOT=Path(__file__).resolve().parent
def negbin(n,d):return (-1)**d*binmod(n+d-1,d)%Q if d>=0 else 0
def mv(a,v):return [sum(x*y for x,y in zip(row,v))%Q for row in a]
def tr(a):return list(map(list,zip(*a)))

def one(row):
    n,b=row['n'],row['b'];lam=symbols(n//2);m=len(lam)-1
    assert m==4*(P-1) and b>m
    supp=[s for s,x in enumerate(lam) if x]
    lower=[[comb(i,j)%Q if j<=i else 0 for j in range(b)] for i in range(b)]
    upper=[[binmod(n,j-i) if j>=i else 0 for j in range(b)] for i in range(b)]
    Nt=[[sum(lam[s]*binmod(n+i,s)*binmod(n+i-s,j) for s in supp)%Q
         for j in range(b)] for i in range(b)]
    A=mm(Nt,upper)
    H=[[lam[k-j]*comb(k,k-j)%Q if 0<=k-j<=m else 0 for j in range(b)] for k in range(b)]
    K=[[lam[b+r-j]*comb(b+r,b+r-j)%Q if 1<=b+r-j<=m else 0 for j in range(b)] for r in range(m)]
    Ftail=[[-sum(negbin(n,b+v-j)*binmod(n,r-v) for v in range(r+1))%Q for r in range(m)] for j in range(b)]
    Kbar=[row[b-m:] for row in K]
    Jend=mm(Ftail,Kbar)
    J=[row[:] for row in H]
    for i in range(b):
        for j in range(m):J[i][b-m+j]=(J[i][b-m+j]+Jend[i][j])%Q
    transfer=mm(mm(mm(lower,upper),J),upper)
    assert transfer==A
    assert all(H[i][j]%2==int(i==j) for i in range(b) for j in range(b))
    assert all(x%2==0 for row in Jend for x in row)
    aa=row['X2'];bb=row['Y4'];ff=row['normalized_first_force'];rr=row['normalized_second_force']
    W=[binmod(n+2,j) for j in range(b+1)]
    q=[(-W[j]*aa[j]+(j+1)*W[j+1]*aa[j+1])%Q for j in range(b)]
    def uinvT(v):return [sum(negbin(n,j-i)*v[i] for i in range(j+1))%Q for j in range(b)]
    def hinvT(v):
        z=[0]*b
        for j in range(b-1,-1,-1):
            z[j]=(v[j]-sum(lam[s]*comb(j+s,s)*z[j+s]
                           for s in range(1,min(m,b-1-j)+1)))%Q
        return z
    v=uinvT(q);z0=hinvT(v)
    Z=tr([hinvT([int(j==b-m+t) for j in range(b)]) for t in range(m)])
    S=mm(tr(Jend),Z)
    for i in range(m):S[i][i]=(S[i][i]+1)%Q
    assert all(S[i][j]%2==int(i==j) for i in range(m) for j in range(m))
    rhs=mv(tr(Jend),z0)
    beta=[x[0] for x in solve(S,[[x] for x in rhs])]
    correction=mv(Z,beta)
    z=[(x-y)%Q for x,y in zip(z0,correction)]
    assert mv(tr(J),z)==v
    tt=uinvT(z)
    ww=[sum((-1)**(j-i)*comb(j,i)*tt[j] for j in range(i,b))%Q for i in range(b)]
    assert mv(tr(A),ww)==q
    raw_norm=sum(x*x for x in aa)%Q;raw_mixed=sum(x*y for x,y in zip(aa,bb))%Q
    endpoint=W[b]*aa[b]%Q
    assert sum(x*y for x,y in zip(ww,ff))%Q==raw_norm
    assert (sum(x*y for x,y in zip(ww,rr))+endpoint)%Q==raw_mixed
    cutoff=next(i for i in range(1,b+1) if L(i//2)>=P)
    assert all(x==0 for x in ff[cutoff:])
    assert sum(ww[i]*ff[i] for i in range(cutoff))%Q==raw_norm
    ratios=[1]
    for t in range(1,2*P):ratios.append(ratios[-1]*(b+t)%Q)
    assert L(2*P)>=P and row['logarithmic_normalized_depth_bound']>=P
    high=0;checks=0
    for s in supp:
        # Independently form the coefficient vector of the adjoint polynomial
        # after substitution x=1+z and its coefficientwise binomial operator.
        prod=[ww[i]*binmod(n+i,s)%Q for i in range(b)]
        transformed=[sum(prod[i]*comb(i,j) for i in range(j,b))%Q for j in range(b)]
        for t,ratio in enumerate(ratios):
            if not ratio:continue
            coeff=sum(transformed[j]*binmod(2*n-s,b+t-j) for j in range(b))%Q
            direct=sum(prod[i]*binmod(2*n+i-s,b+t) for i in range(b))%Q
            assert coeff==direct;checks+=1
            high=(high+lam[s]*ratio*coeff)%Q
    assert (high+endpoint)%Q==raw_mixed
    out={'b':b,'n':n,'precision':P,'bandwidth':m,'endpoint_rank':m,
         'complete_contact_factorization_zero':True,'complete_adjoint_residual_zero':True,
         'adjoint_norm_and_mixed_match':True,'independent_high_moment_comparisons':checks,
         'first_force_cutoff':cutoff,'whole_raw_norm':raw_norm,'whole_raw_mixed':raw_mixed,
         'true_endpoint_contribution':endpoint,'interior_high_moment_sum':high,
         'scope':'Auxiliary complete finite system; no original-family contraction/invariant theorem'}
    print(json.dumps(out),flush=True)
    return out

if __name__=='__main__':
    src=ROOT/'normalized_binary_finite_audit_certificate.json'
    prior=json.loads(src.read_text())
    out={'status':'PASS','scope':'Two complete auxiliary normalized binary adjoint audits; no original exponential-index Gram law',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_certificate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
         'cases':[one(row) for row in prior['cases']]}
    dest=ROOT/'binary_adjoint_audit_receipt.json';dest.write_text(json.dumps(out,indent=2)+'\n')
