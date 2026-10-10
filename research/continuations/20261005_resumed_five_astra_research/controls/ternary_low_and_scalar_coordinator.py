"""Bounded personally authored modular checks; no original-family inference."""
from pathlib import Path
from math import comb,factorial
import hashlib,json
ROOT=Path(__file__).resolve().parent

def solve(A,B,mod):
    rows=len(A);cols=len(B[0]);aug=[list(A[i])+list(B[i]) for i in range(rows)]
    for k in range(rows):
        pivot=next(i for i in range(k,rows) if aug[i][k]%3)
        aug[k],aug[pivot]=aug[pivot],aug[k]
        inv=pow(aug[k][k],-1,mod);aug[k]=[(x*inv)%mod for x in aug[k]]
        for i in range(rows):
            if i==k:continue
            c=aug[i][k]
            if c:aug[i]=[(x-c*y)%mod for x,y in zip(aug[i],aug[k])]
    assert all(aug[i][j]==int(i==j) for i in range(rows) for j in range(rows))
    return [row[rows:] for row in aug]

def low27():
    H,D,h,kappa,nu=19683,18,10,9,8;A=H-D;n=A+2;beta=-71-A;mod=27
    cutoff=4*n-3;limit=H+2*D
    vf=[0]*(limit+1);uf=[1]*(limit+1)
    for i in range(1,limit+1):
        x=i;v=0
        while x%3==0:x//=3;v+=1
        vf[i]=vf[i-1]+v;uf[i]=uf[i-1]*x%mod
    def coeff(N,K):
        if K<0 or K>N:return 0
        v=vf[N]-vf[K]-vf[N-K]
        if v>=3:return 0
        b=pow(3,v)*uf[N]*pow(uf[K],-1,mod)*pow(uf[N-K],-1,mod)%mod
        return b if (N-K)%2==0 else -b%mod
    poles=[]
    for level in range(h):
        weight=3**(h-1-level)
        if weight%mod==0:continue
        for c in range(1,cutoff//(3**level)+1,2):
            if c%3==0:continue
            poles.append(((c*3**level-1)//2,weight*pow(c,-1,mod)%mod))
    L=[[sum(w*(beta*coeff(A+u+v,r)+3*coeff(A+u+v,r-1)) for r,w in poles)%mod
        for v in range(D)] for u in range(D)]
    inv=solve(L,[[int(i==j) for j in range(D)] for i in range(D)],mod)
    assert all(L[u][v]==0 for u in range(D) for v in range(D) if u+v>=D)
    assert all(inv[u][v]==0 for u in range(D) for v in range(D) if u+v<D-1)
    vectors=[]
    for b in range(kappa+1):
        for i in range(nu):
            v=[sum(w*coeff(H-kappa+b+u,r-i) for r,w in poles)%mod for u in range(D)]
            assert not any(v[kappa:]);vectors.append({'b':b,'i':i,'vector':v})
    assert all(sum(x['vector'][u]*inv[u][v]*y['vector'][v] for u in range(D) for v in range(D))%mod==0
               for x in vectors for y in vectors)
    out={'status':'PASS','scope':'Auxiliary finite core LOW and jet algebra, not original producer saturation or relative-pair proof',
         'H':H,'D':D,'h':h,'A':A,'cutoff':cutoff,'modulus':mod,'poles':poles,'L':L,'inverse':inv,
         'vectors':vectors,'zero_pairings':len(vectors)**2}
    out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'low27_isotropy_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('low27_isotropy_certificate.json PASS',len(vectors)**2,flush=True)

def scalar():
    mod=729;gam=[1,0]
    for r in range(1,248):gam.append(((4*r+2)*gam[-1]+4*gam[-2])%mod)
    cases=[]
    for n in list(range(2,84,3))+[92,110,122]:
        T=[[comb(i+j,i)*gam[i+j]%mod for j in range(n)] for i in range(n)]
        F=factorial(n-1);u=[F//factorial(i)*pow(-2,i,mod)%mod for i in range(n)]
        v=solve(T,[[x] for x in u],mod)
        eta=(F*F-sum(u[i]*v[i][0] for i in range(n)))%mod
        val=0;z=eta
        if eta:
            while z%3==0:z//=3;val+=1
        else:val=None
        assert all(sum(T[i][j]*v[j][0] for j in range(n))%mod==u[i] for i in range(n))
        cases.append({'n':n,'eta_mod729':eta,'v3_eta_if_below6':val,'eta_depth_at_least6':eta==0,
                      'terminal_response_mod3':v[-1][0]%3})
    out={'status':'PASS','scope':'Finite normalized signed-denominator probes only, not a growing original-index law',
         'modulus':mod,'cases':cases,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'signed_eta_mod729_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('signed_eta_mod729_certificate.json PASS',[(v['n'],v['v3_eta_if_below6']) for v in cases],flush=True)

if __name__=='__main__':low27();scalar()
