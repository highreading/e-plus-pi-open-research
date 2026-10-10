"""L16: verify the newly proved reverse-factorial identities at existing receipt primes."""
from pathlib import Path
from math import comb
import json

BASE=Path(__file__).resolve().parent


def jets(limit):
    a=[1];s=[1];d=[1];t=[0,1]
    for n in range(1,limit+1):
        a.append(n*a[-1]-(comb(n,2)*a[-2] if n>=2 else 0))
        s.append(n*s[-1]-(comb(n,2)*s[-2] if n>=2 else 0)+1)
        d.append(n*d[-1]+1)
        if n<limit:t.append((n+2)*t[-1]-n*t[-2]+s[n])
    assert len(a)==len(s)==len(d)==len(t)==limit+1
    return a,s,d,t


def run():
    receipt=json.loads((BASE/'BOUNDARY_MOMENT_QUOTIENT_RECEIPT.json').read_text())['rows']
    used=[r for r in receipt if r['h']==1]
    a,s,d,t=jets(max(r['p'] for r in used))
    # Literal Hurwitz product identity, at only the existing receipt indices.
    for r in used:
        n=r['p']-1
        direct=sum(comb(n,j)*a[j-1]*d[n-j] for j in range(1,n+1))
        assert direct==t[n]
    out=[]
    for r in used:
        p=r['p'];chi=r['chi'];C=d[p-1]%p
        U=s[p-1]%p
        W=(s[p-1]+s[p-2]*pow(2,-1,p))%p
        L=(-t[p-1]-chi*C)%p
        assert [U,W]==r['initial_mu'] and L==r['initial_lambda'][0] and C==r['C']
        assert a[p-1]%p==-chi%p and a[p]%p==0 and s[p]%p==1
        assert t[p]%p==-chi%p and (t[p-1]+t[p-2]+U+chi)%p==0
        if r['b']==4:
            nu=4*(-85*t[p-1]+(156-194*C)*s[p-1]+(163-97*C)*s[p-2]+(12-85*chi)*C-78)%p
        else:
            assert r['b']==5
            nu=384*(-93*t[p-1]+(24*C+90)*s[p-1]+(155-31*C)*s[p-2]-(148+93*chi)*C-28)%p
        assert nu==r['nu']
        out.append(dict(p=p,b=r['b'],chi=chi,C=C,S_last=s[p-1]%p,S_previous=s[p-2]%p,
                        T_last=t[p-1]%p,T_previous=t[p-2]%p,mu0=U,mu1=W,lambda0=L,nu=nu,
                        direct_convolution_exact=True))
    (BASE/'H1_LOGARITHMIC_JET_RELATION_RECEIPT.json').write_text(json.dumps(dict(
        status='AUTHOR existing-prime supporting receipt; no prime scan or residue-independence assertion',
        exact_integer_sequences='a=q0^-1 jets,S=e^z/q0 jets,D=e^z/(1-z) jets,T=e^z integral(q0^-1)/(1-z) jets',
        rows=out),indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':run()
