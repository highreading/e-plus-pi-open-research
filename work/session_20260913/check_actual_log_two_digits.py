"""Exact check of the actual residue pair and the two-digit Cartier lift.

No reconstructed endpoint program or old certificate is imported.
"""
from math import comb
import json
from pathlib import Path

def add(a,b,mod=None):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,0)+v
    return clean(out,mod)

def clean(a,mod=None):
    return {k:(v%mod if mod else v) for k,v in a.items() if (v%mod if mod else v)}

def mul(a,b,mod=None):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            key=(i+k,j+l); out[key]=out.get(key,0)+v*w
    return clean(out,mod)

def power(a,n,mod=None):
    out={(0,0):1}
    while n:
        if n&1: out=mul(out,a,mod)
        a=mul(a,a,mod); n//=2
    return out

def sec(a,p,r,s,mod=None):
    return clean({((i-r)//p,(j-s)//p):v for (i,j),v in a.items()
                  if i%p==r and j%p==s},mod)

def scale(a,k): return clean({ij:k*v for ij,v in a.items()})

D=add({(0,2*j):comb(4,j) for j in range(5)},
      {(1,j):-(-1)**j*comb(6,j) for j in range(7)})

def initial(nu,p):
    P=mul({(0,j):comb(1+3*nu,j) for j in range(2+3*nu)},
          {(0,2*j):comb(3-nu,j) for j in range(4-nu)})
    A=clean(P,p)
    carry={ij:(v-A.get(ij,0))//p for ij,v in P.items()}
    return A,mul(carry,D,p)

def setup(p):
    dp=power(D,p)
    frob={(p*i,p*j):v for (i,j),v in D.items()}
    dif=add(dp,scale(frob,-1))
    assert all(v%p==0 for v in dif.values())
    E=clean({ij:v//p for ij,v in dif.items()},p)
    q1=power(D,p-1,p*p)
    q2=power(D,2*p-2,p)
    return q1,q2,mul(q1,E,p)

def step(A,B,c,p,r,params):
    q1,q2,qE=params
    s=(4*r+c)%p; cp=(4*r+c)//p
    U=sec(mul(A,q1,p*p),p,r,s,p*p)
    Ap=clean(U,p)
    U1={ij:(v-Ap.get(ij,0))//p for ij,v in U.items()}
    Bp=add(mul(U1,D,p),sec(add(mul(B,q2,p),scale(mul(A,qE,p),-1)),p,r,s,p),p)
    assert all(i<=1 and j<=8 for i,j in Ap)
    assert all(i<=2 and j<=16 for i,j in Bp)
    assert 0<=cp<=3
    return Ap,Bp,cp

def output(A,B,c,p):
    def coeff(S,k):
        return sum(v*(-1)**((c-j)//2)*comb(k+(c-j)//2-1,(c-j)//2)
                   for (i,j),v in S.items() if i==0 and j<=c and (c-j)%2==0)
    return (coeff(A,4)+p*coeff(B,8))%(p*p)

def actual(m,nu):
    # Original coefficient formula, evaluated directly over the integers.
    N=4*m+nu; K=4*m+1+nu
    total=0
    for b in range(2+3*nu):
        for a in range(min(6*m,N-b)+1):
            rest=N-a-b
            if rest>=0 and rest%2==0:
                j=rest//2
                total+=(-1)**(a+j)*comb(6*m,a)*comb(1+3*nu,b)*comb(K+j-1,j)
    return total

rows=[]
for p in (5,7,11):
    params=setup(p)
    # Includes zero digits, multi-digit carries, and both sides of p^2.
    for m in (0,1,2,p-1,p,p+1,p*p-1,p*p,p*p+1):
        for nu in (0,1):
            A,B=initial(nu,p); c=nu; n=m; digits=[]
            while n:
                r=n%p; n//=p; digits.append(r)
                A,B,c=step(A,B,c,p,r,params)
            got=output(A,B,c,p); expected=actual(m,nu)%(p*p)
            assert got==expected,(p,m,nu,got,expected)
            # An added leading zero must preserve the output.
            Az,Bz,cz=step(A,B,c,p,0,params)
            assert output(Az,Bz,cz,p)==got
            rows.append(dict(p=p,m=m,nu=nu,digits=digits,output=got,pass_check=True))
out={'status':'passed','rows':rows,'count':len(rows),
     'scope':'finite normalization checks; no valuation-tail or density theorem'}
Path(__file__).with_name('actual_log_two_digit_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','count':len(rows)}))
