from fractions import Fraction as Q
from math import factorial, comb
import json

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def power(a,h):
    out=[1]
    for _ in range(h):
        out=mul(out,a)
    return out

def vp(x):
    x=Q(x)
    if not x:
        return None
    def val(a):
        a=abs(a)
        k=0
        while a%3==0:
            a//=3
            k+=1
        return k
    return val(x.numerator)-val(x.denominator)

def residue(x):
    x=Q(x)
    assert x.denominator%3
    return (x.numerator%3)*pow(x.denominator%3,-1,3)%3

def moment(j):
    real,imag=1,0
    for _ in range(j+1):
        real,imag=real-imag,real+imag
    return Q(2*imag,2**j*(j+1))

def legendre(h):
    u=power([1,-2,2],h)
    return [comb(h+d,h)*u[h+d] for d in range(h+1)],u

def auxiliary(h):
    c=power([2,-2,1],h)
    H=[Q(factorial(h)*c[h-d],factorial(d)*2**h) for d in range(h+1)]
    assert all(x.denominator==1 for x in H)
    h0=sum(H)
    h1=sum(d*x for d,x in enumerate(H))
    h2=sum(d*(d-1)*x for d,x in enumerate(H))
    return H,(h0,h*h0+h1,h*(h-1)*h0+2*h*h1+h2)

def solve(matrix,rhs):
    size=len(rhs)
    assert all(len(row)==size for row in matrix)
    a=[[Q(x) for x in row]+[Q(y)] for row,y in zip(matrix,rhs)]
    for j in range(size):
        pivot=next(i for i in range(j,size) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        c=a[j][j]
        a[j]=[x/c for x in a[j]]
        for i in range(size):
            if i!=j:
                c=a[i][j]
                a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    return [a[i][-1] for i in range(size)]

n=4
m=n+1
P,up=legendre(n)
U,uu=legendre(m)
Hn,(hn,Jn,Kn)=auxiliary(n)
Hm,(eta,Jm,Km)=auxiliary(m)
a,b=sum(P),sum(U)
S=Jm*Jm-eta*Km
C=(Jm-eta)*Jn-(Km-Jm)*hn
W=Jm*Jn-Km*hn
assert [residue(x) for x in (hn,Jn,eta,Jm,Km,S,C,W)]==[0,1,1,0,2,1,2,0]
assert a%3==b%3!=0

E=[]
e=[]
running=Q(0)
for j in range(2*n+2):
    running+=Q(1,factorial(j))
    E.append(running)
    ej=factorial(j)*running
    assert ej.denominator==1
    e.append(ej.numerator)

f=Q(2**n,factorial(n)**2)
TP=sum(Q(c)*E[n+d] for d,c in enumerate(P))
TU=sum(Q(c)*E[n+d] for d,c in enumerate(U))
def w(poly):
    return sum(Q(c)*sum((moment(j) for j in range(d)),Q(0)) for d,c in enumerate(poly))
wP,wU=w(P),w(U)
pterms=[Q(factorial(n)*up[n+d]*e[n+d],2**n*factorial(d)) for d in range(n+1)]
uterms=[Q(factorial(n)*(m+d)*uu[m+d]*e[n+d],2**n*m*factorial(d)) for d in range(m+1)]
assert sum(pterms)==TP/f
assert sum(uterms)==TU/f
assert all(x==0 or vp(x)>=1 for x in pterms[:n-1]+uterms[:n-1])
assert pterms[n]==e[2*n]
assert pterms[n-1]==-n*n*e[2*n-1]
assert uterms[m]==Q(4,m)*e[2*n+1]
assert uterms[m-1]==-2*(2*n+1)*e[2*n]
assert uterms[m-2]==2*n*n*m*e[2*n-1]
assert [residue(uterms[d]) for d in (m,m-1,m-2)]==[2,0,2]
assert residue(TP/f)==0 and residue(TU/f)==1
assert vp(wP/f) is None or vp(wP/f)>=1
assert vp(wU/f) is None or vp(wU/f)>=1

Pstar,Ustar=wP+TP,wU+TU
D=m*m*b*C-2*a*S
X=2*Pstar*S-m*m*Ustar*C-2*f*eta*W
assert D!=0 and X!=0
assert residue(X/f)==1 and int(D)%3==0
ratio=X/D
r=vp(factorial(n))
assert vp(X)==-2*r
assert vp(ratio.denominator)==2*r+vp(D)
gamma=Q((-1)**n,4*m**3*factorial(n)**4)
assert vp(gamma*X)==-6*r

# Solve the original order and endpoint-matching equations independently.
F=[Q(0)]+[moment(k-1) for k in range(1,2*n+3)]
matrix=[]
rhs=[]
for k in range(n+1,2*n+3):
    matrix.append([Q(1,factorial(k-j)) for j in range(3)]+[F[k-j] for j in range(n+1)])
    rhs.append(Q(0))
matrix.append([1]*3+[0]*(n+1)); rhs.append(Q(1))
matrix.append([0]*3+[1]*(n+1)); rhs.append(Q(1))
solution=solve(matrix,rhs)
Bpoly,Cpoly=solution[:3],solution[3:]
assert sum(Bpoly)==sum(Cpoly)==1
Apoly=[]
for k in range(n+1):
    val=sum((Bpoly[j]*Q(1,factorial(k-j)) for j in range(min(2,k)+1)),Q(0))
    val+=sum((Cpoly[j]*F[k-j] for j in range(k+1)),Q(0))
    Apoly.append(-val)
for k in range(2*n+3):
    val=Apoly[k] if k<=n else Q(0)
    val+=sum((Bpoly[j]*Q(1,factorial(k-j)) for j in range(min(2,k)+1)),Q(0))
    val+=sum((Cpoly[j]*F[k-j] for j in range(min(n,k)+1)),Q(0))
    assert val==0
assert sum(Apoly)==ratio

print(json.dumps({'n':n,'P':P,'U':U,'moment_values':[str(moment(j)) for j in range(n+1)],'wP':str(wP),'wU':str(wU),'moment_normalized_valuations':[vp(wP/f),vp(wU/f)],'TP_over_f':str(TP/f),'TU_over_f':str(TU/f),'U_surviving_terms_descending':[str(uterms[d]) for d in (m,m-1,m-2)],'U_surviving_residues_descending':[residue(uterms[d]) for d in (m,m-1,m-2)],'D':str(D),'X':str(X),'N':str(X/f),'endpoint_ratio':str(ratio),'valuations_D_X_q':[vp(D),vp(X),vp(ratio.denominator)],'direct_system_ratio':str(sum(Apoly)),'all_assertions_passed':True},indent=2))