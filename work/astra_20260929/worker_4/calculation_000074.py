from fractions import Fraction as F
from math import factorial, inf
import json

indices=[6,11,16,21,26]
maxn=max(indices)
fac=[factorial(j) for j in range(2*maxn+5)]

def vp(x,p=5):
    x=F(x)
    if not x: return inf
    z=abs(x.numerator); w=x.denominator; v=0
    while z%p==0: z//=p; v+=1
    while w%p==0: w//=p; v-=1
    return v

def residue(x):
    x=F(x)
    assert x.denominator%5
    return (x.numerator*pow(x.denominator,-1,5))%5

def mulq(poly):
    out=[0]*(len(poly)+2)
    for j,c in enumerate(poly):
        out[j]+=c; out[j+1]-=2*c; out[j+2]+=2*c
    return out

powers=[[1]]
for m in range(1,maxn+2): powers.append(mulq(powers[-1]))
Ls=[]
for m in range(maxn+2):
    coeff=[]
    for d in range(m+1):
        z=F(fac[m+d]*powers[m][m+d],fac[m]*fac[d])
        assert z.denominator==1
        coeff.append(z.numerator)
    Ls.append(coeff)

mom=[]
re,im=1,0
for j in range(2*maxn+3):
    re,im=re-im,re+im
    mom.append(F(2*im,2**j*(j+1)))
E=[]; total=F(0)
for j in range(2*maxn+4):
    total+=F(1,fac[j]); E.append(total)
ees=[fac[j]*E[j] for j in range(len(E))]
assert all(x.denominator==1 for x in ees)

def Hder(m,j):
    z=F(0)
    for c in range((m-j)//2+1):
        for u in range(m-j-2*c+1):
            z+=F((-1)**u*fac[m]**2,fac[m-u-2*c-j]*fac[m-u-c]*2**c*fac[u]*fac[c])
    assert z.denominator==1
    return z.numerator

def wmoment(poly):
    # (poly(t)-poly(1))/(t-1) has coefficient sum_{d>j} poly[d].
    suffix=0; z=F(0)
    for j in range(len(poly)-2,-1,-1):
        suffix+=poly[j+1]
        z+=suffix*mom[j]
    return z

def printable(x):
    return 'inf' if x==inf else x

results=[]
for n in indices:
    P=Ls[n]; U=Ls[n+1]
    a=sum(P); b=sum(U); k=(n+1)**2
    f=F(2**n,fac[n]**2)
    G=F((-1)**n*2**(2*n+3),n+1)
    gamma=F((-1)**n,4*(n+1)**3*fac[n]**4)
    def ell(poly,j):
        return sum((F(c,fac[n+d+1-j]) for d,c in enumerate(poly)),F(0))
    def T(poly,j):
        return sum((c*E[n+d-j] for d,c in enumerate(poly)),F(0))
    wp=wmoment(P); wu=wmoment(U)
    assert a*wu-b*wp==G
    ps=wp+T(P,0); us=wu+T(U,0)
    h,h1,h2=[Hder(n,j) for j in range(3)]
    eta,u1,u2flat=[Hder(n+1,j) for j in range(3)]
    jn=n*h+h1
    ju=(n+1)*eta+u1
    ku=(n+1)*n*eta+2*(n+1)*u1+u2flat
    S=ju**2-eta*ku
    C=(ju-eta)*jn-(ku-ju)*h
    W=ju*jn-ku*h
    D=k*b*C-2*a*S
    X=2*ps*S-k*us*C-2*f*eta*W
    N=X/f
    assert [z%5 for z in (h,jn,eta,ju,ku)]==[0,1,1,0,1]
    assert [z%5 for z in (S,C,W,k)]==[4,4,0,4]
    assert a%5 and (b-4*sum(P))%5==0 and (D-a)%5==0
    pterms=[F(fac[n],fac[d])*powers[n][n+d]*ees[n+d]/2**n for d in range(n+1)]
    uterms=[F(fac[n],fac[d])*(n+1+d)*powers[n+1][n+1+d]*ees[n+d]/(2**n*(n+1)) for d in range(n+2)]
    assert sum(pterms)==T(P,0)/f
    assert sum(uterms)==T(U,0)/f
    assert all(vp(z)>=1 for z in pterms[:n-1]+uterms[:n-1])
    assert [residue(z) for z in pterms[-2:]]==[3,0]
    assert [residue(z) for z in uterms[-3:]]==[3,0,2]
    L=0; power=1
    while power*5<=n: power*=5; L+=1
    r=vp(fac[n])
    assert vp(wp/f)>=2*r-L>=1 and vp(wu/f)>=2*r-L
    assert [residue(z) for z in (ps/f,us/f,N)]==[3,0,4]

    # Reconstruct the full raw triple using the orthogonal expansion of the kernel.
    alpha=[ell(U,j) for j in range(3)]
    tau=[(a*T(U,j)-b*T(P,j))/G for j in range(3)]
    tt=[1+z for z in tau]
    beta=[alpha[1]*tt[2]-alpha[2]*tt[1],alpha[2]*tt[0]-alpha[0]*tt[2],alpha[0]*tt[1]-alpha[1]*tt[0]]
    Q=[F(0)]*(n+1)
    for m in range(n+1):
        norm=F((-1)**m*2**(2*m+1),2*m+1)
        rho=sum((beta[j]*ell(Ls[m],j) for j in range(3)),F(0))
        for d,c in enumerate(Ls[m]): Q[d]-=rho*c/norm
    Craw=Q[::-1]
    def tailcoef(deg):
        be=sum((beta[j]/fac[deg-j] for j in range(3) if j<=deg),F(0))
        cf=sum((Craw[d]*mom[deg-d-1] for d in range(n+1) if d<deg),F(0))
        return be+cf
    Araw=[-tailcoef(deg) for deg in range(n+1)]
    for deg in range(2*n+3):
        assert tailcoef(deg)+(Araw[deg] if deg<=n else 0)==0
    assert sum(beta)==sum(Craw)==gamma*D
    assert sum(Araw)==gamma*X
    ratio=X/D
    assert ratio==sum(Araw)/sum(beta)
    assert vp(D)==0 and vp(X)==-2*r and vp(ratio.denominator)==2*r
    assert vp(sum(Araw))==-6*r and vp(sum(beta))==-4*r
    if n==6:
        assert ratio.denominator==260737140696321600
    results.append({'n':n,'v5_n_minus_1':vp(n-1),'v5_n_factorial':r,'moment_loss_bound':L,'v5_D':vp(D),'v5_X':vp(X),'v5_q':vp(ratio.denominator),'normalized_P_U_N_mod5':[residue(ps/f),residue(us/f),residue(N)],'P_survivor_residues':[residue(z) for z in pterms[-2:]],'U_survivor_residues':[residue(z) for z in uterms[-3:]],'normalized_moment_valuations':[printable(vp(wp/f)),printable(vp(wu/f))],'raw_endpoint_valuations':[vp(sum(Araw)),vp(sum(beta))],'reduced_numerator':str(ratio.numerator),'reduced_denominator':str(ratio.denominator),'order_checked_through':2*n+2})
print(json.dumps({'status':'all exact assertions passed','results':results},indent=2))