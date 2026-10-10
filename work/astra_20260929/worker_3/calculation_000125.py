from fractions import Fraction as F
from math import factorial

def fall(a,t):
    z=1
    for i in range(t): z*=a-i
    return z

def coeff(a,T):
    c=[F(1)]+[F(0)]*T
    for _ in range(a):
        c=[c[t]-(c[t-1] if t>=1 else 0)+(c[t-2]/2 if t>=2 else 0) for t in range(T+1)]
    return c

def mod(q,M=25):
    q=F(q)
    return q.numerator*pow(q.denominator,-1,M)%M

def calculate(n,cut):
    m=n+1
    cn=coeff(n, min(n,10) if cut else n)
    cm=coeff(m, min(m,10) if cut else m)
    e=[1]
    for a in range(1,2*m): e.append(a*e[-1]+1)
    def hd(a,c,d):
        return sum((fall(a,t+d)*c[t] for t in range(len(c)) if t+d<=a),F(0))
    hn=hd(n,cn,0); Jn=n*hn+hd(n,cn,1)
    h=hd(m,cm,0)
    hp=hd(m,cm,1)
    j=h+sum((fall(m-1,t)*cm[t] for t in range(min(m-1,len(cm)-1)+1)),F(0))
    k=(m-1)*h+2*hp+sum((fall(m-1,t+1)*cm[t] for t in range(min(m-2,len(cm)-1)+1)),F(0))
    A=sum((fall(n,t)*cn[t]*e[2*n-t] for t in range(len(cn))),F(0))
    B=4*e[2*m-1]+2*sum((fall(m-1,t-1)*cm[t]*(2*m-t)*e[2*m-1-t] for t in range(1,len(cm))),F(0))
    C=(m*j-h)*Jn-m*(k-j)*hn
    Z=2*A*(m*j*j-h*k)-B*C-2*h*(j*Jn-k*hn)
    return tuple(mod(x) for x in (h,j,k,hn,Jn,A,B,C,Z))

rows=[]
for n in range(14,150,5):
    r=calculate(n,True)
    if n<=39: assert r==calculate(n,False),(n,r,calculate(n,False))
    assert r[-1]%5==0
    rows.append([n,n%25,list(r),r[-1]//5])
print({'columns':['n','n_mod25','h_j_k_hn_Jn_A_B_C_Z_mod25','Z_over5_mod5'],'rows':rows,'scope':'Exponential part; moment omission justified only for the stated n>=14 progression. Finite residue agreement is not a proof of periodicity.'})