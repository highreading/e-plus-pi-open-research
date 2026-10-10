from fractions import Fraction as F
from math import comb

def fall(a,t):
    x=1
    for i in range(t): x*=a-i
    return x

def coeff(a,T):
    c=[F(1)]+[F(0)]*T
    for _ in range(a):
        c=[c[t]-(c[t-1] if t else 0)+(c[t-2]/2 if t>=2 else 0) for t in range(T+1)]
    return c

def residue(x):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,25)%25

q25=coeff(25,10)
assert all(residue(q25[t])==0 for t in range(1,5))
assert all(residue(q25[t])%5==0 for t in range(1,11))
rows=[]
for n in (14,19,24,29,34):
    m=n+1
    cn=coeff(n,10); cm=coeff(m,10)
    e=[1]
    for a in range(1,2*m): e.append(a*e[-1]+1)
    hn=sum(fall(n,t)*cn[t] for t in range(10))
    Jn=n*hn+sum(fall(n,t+1)*cn[t] for t in range(9))
    h=sum(fall(m,t)*cm[t] for t in range(10))
    hp=sum(fall(m,t+1)*cm[t] for t in range(9))
    j=h+sum(fall(m-1,t)*cm[t] for t in range(10))
    k=(m-1)*h+2*hp+sum(fall(m-1,t+1)*cm[t] for t in range(9))
    A=sum(fall(n,t)*cn[t]*e[2*n-t] for t in range(10))
    boundary=4*e[2*m-1]
    B=boundary+2*sum(fall(m-1,t-1)*cm[t]*(2*m-t)*e[2*m-1-t] for t in range(1,11))
    C=(m*j-h)*Jn-m*(k-j)*hn
    Zexp=2*A*(m*j*j-h*k)-B*C-2*h*(j*Jn-k*hn)
    vals=[residue(x) for x in (h,j,k,hn,Jn,A,boundary,B,C,Zexp)]
    assert vals[-1]==20,(n,vals)
    rows.append({'n':n,'n_mod25':n%25,'values_mod25':vals})
print({'Q_power25_coefficients_mod25':[residue(x) for x in q25], 'columns':['h','j','k','h_n','J_n','A','boundary','B','C','F_n'], 'representatives':rows,'scope':'Exact representative evaluations. Universal reduction requires the separately supplied truncation, periodicity, and moment arguments; independent review remains outstanding.'})