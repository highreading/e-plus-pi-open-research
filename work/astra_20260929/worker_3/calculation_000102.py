from fractions import Fraction as F
from math import factorial
import json

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,m):
    q=[F(1)]
    for _ in range(m): q=mul(q,a)
    return q

def legendre(m):
    u=power([1,-2,2],m)
    return [u[m+d]*F(factorial(m+d),factorial(m)*factorial(d)) for d in range(m+1)]

def moment(j):
    x,y=1,0
    for _ in range(j+1): x,y=x-y,x+y
    return F(2*y,2**j*(j+1))

def derivative_data(m):
    c=power([1,-1,F(1,2)],m)
    return [sum((F(factorial(m),factorial(m-t-j))*c[t] for t in range(m-j+1)),F(0)) for j in range(3)]

def vp(z):
    z=F(z)
    if not z: return None
    def vi(a):
        a=abs(a); k=0
        while a%5==0: a//=5; k+=1
        return k
    return vi(z.numerator)-vi(z.denominator)

def residue(z,mod=5):
    z=F(z)
    return z.numerator*pow(z.denominator,-1,mod)%mod

def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]

rows=[]
for n in (8,23,28):
    polys=[legendre(m) for m in range(n+2)]
    P,U=polys[n:n+2]
    a,b=sum(P),sum(U)
    k=(n+1)**2
    f=F(2**n,factorial(n)**2)
    G=F((-1)**n*2**(2*n+3),n+1)
    E=[]; z=F(0)
    for j in range(2*n+4):
        z+=F(1,factorial(j)); E.append(z)
    def T(Q,j=0): return sum((c*E[n+d-j] for d,c in enumerate(Q)),F(0))
    def ell(Q,j): return sum((c/F(factorial(n+d+1-j)) for d,c in enumerate(Q)),F(0))
    def w(Q):
        q=[F(0)]*(len(Q)-1)
        q[-1]=Q[-1]
        for d in range(len(q)-1,0,-1): q[d-1]=Q[d]+q[d]
        assert -q[0]==Q[0]-sum(Q)
        return sum((c*moment(j) for j,c in enumerate(q)),F(0))
    wp,wu=w(P),w(U)
    assert a*wu-b*wp==G
    h,hp,hpp=derivative_data(n)
    eta,ep,epp=derivative_data(n+1)
    J=n*h+hp
    J1=(n+1)*eta+ep
    K1=n*(n+1)*eta+2*(n+1)*ep+epp
    S=J1**2-eta*K1
    C=(J1-eta)*J-(K1-J1)*h
    W=J1*J-K1*h
    D=k*b*C-2*a*S
    X=2*(wp+T(P))*S-k*(wu+T(U))*C-2*f*eta*W
    assert D.denominator==1 and D!=0
    alpha=[ell(U,j) for j in range(3)]
    tau=[(a*T(U,j)-b*T(P,j))/G for j in range(3)]
    beta=cross(alpha,[1+t for t in tau])
    Q=[F(0)]*(n+1)
    for i,Li in enumerate(polys[:n+1]):
        norm=F((-1)**i*2**(2*i+1),2*i+1)
        weight=-sum((beta[j]*ell(Li,j) for j in range(3)),F(0))/norm
        for d,c in enumerate(Li): Q[d]+=weight*c
    Cpoly=list(reversed(Q))
    def original_coefficient(m):
        exponential=sum((beta[j]/factorial(m-j) for j in range(min(2,m)+1)),F(0))
        moment_part=sum((Cpoly[j]*moment(m-j-1) for j in range(min(n,m-1)+1)),F(0)) if m else F(0)
        return exponential+moment_part
    Apoly=[-original_coefficient(m) for m in range(n+1)]
    assert all(original_coefficient(m)==0 for m in range(n+1,2*n+3))
    gamma=F((-1)**n,4*(n+1)**3*factorial(n)**4)
    assert sum(beta)==sum(Cpoly)==gamma*D
    assert sum(Apoly)==gamma*X
    ratio=X/D
    assert sum(Apoly)/sum(beta)==ratio
    r=vp(factorial(n))
    assert residue(T(P)/f)==4 and residue(T(U)/f)==1
    assert vp(wp/f)>=1 and vp(wu/f)>=1
    assert residue(X/f)==1 and vp(X)==-2*r
    assert vp(D)>=1 and vp(ratio.denominator)==2*r+vp(D)
    rows.append({'n':n,'r':r,'vD':vp(D),'vX':vp(X),'vq':vp(ratio.denominator),'loss5':max(0,2*r-vp(ratio.denominator)),'D_mod_125':residue(D,125),'X_over_f_mod_25':residue(X/f,25),'T_over_f_mod5':[residue(T(P)/f),residue(T(U)/f)],'normalized_moment_valuations':[vp(wp/f),vp(wu/f)],'aux_mod5':[residue(z) for z in (h,J,eta,J1,K1,S,C,W)],'raw_endpoint_valuations':[vp(sum(Apoly)),vp(sum(beta))],'ratio_numerator':str(ratio.numerator),'ratio_denominator':str(ratio.denominator),'order_conditions_checked':n+2})
print(json.dumps({'status':'all assertions passed','exact_reconstructions':rows},indent=2))