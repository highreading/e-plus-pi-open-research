from math import factorial, comb, gcd
from functools import reduce
from pathlib import Path
import json

def v(x,p):
    if x==0:return None
    k=0
    while x%p==0:x//=p;k+=1
    return k

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def transpose(A):return list(map(list,zip(*A)))
def mm(A,B):return [[dot(a,b) for b in transpose(B)] for a in A]
def mv(A,b):return [dot(a,b) for a in A]
def adj(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return [[e*i-f*h,c*h-b*i,b*f-c*e],[f*g-d*i,a*i-c*g,c*d-a*f],[d*h-e*g,b*g-a*h,a*e-b*d]]
def det(A):return dot(A[0],transpose(adj(A))[0])
def fall(a,k):return factorial(a)//factorial(a-k)
def center_data(n):
    b=[2**n]
    for s in range(n+2):
        num=2*(s-n)*b[s]+(2*n-s+1)*(b[s-1] if s else 0)
        assert num%(2*(s+1))==0
        b.append(num//(2*(s+1)))
    Dc=[1]
    for j in range(1,2*n+3):Dc.append(j*Dc[-1]+1)
    P=[1,2]
    for j in range(1,n+2):
        num=2*(2*j+1)*P[-1]+4*j*P[-2]
        assert num%(j+1)==0
        P.append(num//(j+1))
    J=[P[n],(2*P[n]+P[n+1])//4,P[n+2]//8]
    assert (2*P[n]+P[n+1])%4==0 and P[n+2]%8==0
    M=[[sum(b[s]*fall(n+i,j+s) for s in range(min(2*n,n+i-j)+1)) for j in range(3)] for i in range(3)]
    E=[sum(b[s]*fall(n+2,2-i+s)*Dc[2*n+i-s] for s in range(min(2*n,n+i)+1)) for i in range(3)]
    U=[[1,-n,n*(n+1)],[0,1,-2*n],[0,0,1]]
    Z=[[-1,0,0],[1,-1,0],[0,1,-1],[0,0,1]]
    K=mm(Z,U); D0=[[1,0,0],[0,n+1,0],[0,0,(n+1)*(n+2)]]
    C=mm(mm(K,adj(M)),D0)
    x=mv(C,J)
    om=[1,(n+2)**2,((n+2)*(n+1))**2,((n+2)*(n+1)*n)**2]
    Dg=sum(w*a*a for w,a in zip(om,x)); z=mv(transpose(C),[w*a for w,a in zip(om,x)])
    assert dot(z,J)==Dg
    g=reduce(gcd,z); A=dot(z,E); R=det(M)*x[0]; S=A+(n+1)*(n+2)*R
    h=(n+2)**4*(n+1)**2*(n*n*(((n+2)**2+1)*(n+1)**2+1)+1)
    assert h*S%g==0
    return dict(n=n,M=M,E=E,J=J,K=K,C=C,x=x,om=om,Dg=Dg,z=z,g=g,A=A,R=R,S=S,h=h,d=(n+1)*(n+2))

if __name__=='__main__':
    out=[]
    for n in range(3,91):
        d=center_data(n); row={'n':n,'pvals':{}}
        for p in [2,3,5,7,11,13,17,19]:
            row['pvals'][str(p)]={k:v(d[k],p) for k in ['Dg','g','S','h','d']}
            row['pvals'][str(p)]['ratio_depth']=v(d['Dg'],p)+v(d['d'],p)-v(d['S'],p)
            row['pvals'][str(p)]['primitive_S_depth']=v(d['h'],p)+v(d['S'],p)-v(d['g'],p)
        out.append(row)
    Path(__file__).with_name('exact_local_probe.json').write_text(json.dumps(out,indent=2))
    for p in [3,5,7,11,13]:
        print('p',p)
        for r in range(p):
            a=[(row['n'],row['pvals'][str(p)]['ratio_depth']) for row in out if row['n']%p==r]
            print(r,a)
