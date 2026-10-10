"""Coordinator-authored bounded orientation and normalization certificate.

The auxiliary dimensions below are NOT an original ternary admissible index.
They test the general finite identity, not a growing 3-adic or global theorem.
"""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,hashlib

OUT=Path(__file__).resolve().parent
m,A,h,D,nu=6,11,8,2,2
d=D+nu;n=2*m+1;z=F(A+71,3);c=F(3**(h+1),2)
def binom(x,r):
    q=F(1)
    for j in range(r):q*=F(x-j,j+1)
    return q
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
    q=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):q[i+j]+=x*y
    return q
def scale(a,s):return [x*s for x in a]
def ev(a,x):return sum((v*x**i for i,v in enumerate(a)),F(0))
def rising(x,r):
    q=F(1)
    for j in range(r):q*=x+j
    return q
def I(s):
    den=1
    for j in range(A+1):den*=2*s+2*j+1
    return F(2**A*factorial(A),den)
def base(poly):return sum((2*I(i)*v for i,v in enumerate(poly)),F(0))
def pole(poly):return sum((3**h*(-1)**A*((-A-71)*I(i)+3*I(i+1))*v for i,v in enumerate(poly)),F(0))
def mm(a,b):return [[sum((x*y for x,y in zip(r,col)),F(0)) for col in zip(*b)] for r in a]
def tr(a):return [list(x) for x in zip(*a)]
def inverse(a):
    k=len(a);b=[list(a[i])+[F(int(i==j)) for j in range(k)] for i in range(k)]
    for j in range(k):
        p=next(i for i in range(j,k) if b[i][j]);b[j],b[p]=b[p],b[j]
        pivot=b[j][j];b[j]=[x/pivot for x in b[j]]
        for i in range(k):
            if i!=j:
                q=b[i][j];b[i]=[x-q*y for x,y in zip(b[i],b[j])]
    result=[r[k:] for r in b]
    assert mm(a,result)==[[F(int(i==j)) for j in range(k)] for i in range(k)]
    return result
def determinant(a):
    b=[list(r) for r in a];ans=F(1)
    for j in range(len(a)):
        p=next((i for i in range(j,len(a)) if b[i][j]),None)
        if p is None:return F(0)
        if p!=j:b[j],b[p]=b[p],b[j];ans=-ans
        pivot=b[j][j];ans*=pivot
        for i in range(j+1,len(a)):
            q=b[i][j]/pivot
            for s in range(j+1,len(a)):b[i][s]-=q*b[j][s]
    return ans
def pad(poly):return poly+[F(0)]*(m+1-len(poly))

p=[];hr=[]
for r in range(m+2):
    value=[F(0)]
    for j in range(r+1):
        term=[F((-1)**(r-j-v)*comb(r-j,v)) for v in range(r-j+1)]
        value=add(value,[F(0)]*j+scale(term,binom(F(r+A),j)*binom(F(r)-F(1,2),r-j)))
    ell=binom(F(2*r+A)-F(1,2),r);value=scale(value,1/ell)
    assert value[-1]==1
    norm=rising(F(r+1),A)/(rising(F(r)+F(1,2),A)*(2*r+A+F(1,2))*ell**2)
    if r<=m:assert base(mul(value,value))==norm
    assert all(base(mul(value,old))==0 for old in p)
    p.append(value);hr.append(norm)
q=[];Hr=[]
for r in range(m+1):
    a=ev(p[r+1],z)/ev(p[r],z)
    numerator=add(p[r+1],scale(p[r],-a));quot=[F(0)]*(r+1)
    remainder=list(numerator)
    for j in range(r+1,0,-1):quot[j-1]=remainder[j];remainder[j-1]+=z*remainder[j]
    assert remainder[0]==0 and quot[-1]==1
    norm=c*a*hr[r]
    assert pole(mul(quot,quot))==norm
    assert all(pole(mul(quot,old))==0 for old in q)
    q.append(quot);Hr.append(norm)
B=[[pole([F(0)]*(i+j)+[F(1)]) for j in range(m+1)] for i in range(m+1)]
Bi=inverse(B)
kernel=[[sum((pad(q[r])[i]*pad(q[r])[j]/Hr[r] for r in range(m+1)),F(0)) for j in range(m+1)] for i in range(m+1)]
assert Bi==kernel
I=list(range(D,d));J=list(range(D))+list(range(d,m+1))
M=[[Bi[i][j] for j in I] for i in I];Mi=inverse(M)
T=[[F((-1)**(i-r)*comb(D,i-r)) if r<=i else F(0) for i in range(nu)] for r in range(nu)]
assert determinant(T)==1
Z=tr([pad([F(0)]*i+[F((-1)**(D-v)*comb(D,v)) for v in range(D+1)]) for i in range(nu)])
assert [Z[i] for i in I]==T
E=[[B[i][j] for j in J] for i in J]
C=mm([[B[i][j] for j in range(m+1)] for i in J],Z)
correction=mm(inverse(E),C)
X=[list(r) for r in Z]
for r,j in enumerate(J):X[j]=[x-y for x,y in zip(X[j],correction[r])]
dual=mm(mm([[Bi[r][s] for s in I] for r in range(m+1)],Mi),T)
assert X==dual
S=mm(mm(tr(X),B),X);assert S==mm(mm(tr(T),Mi),T)
assert determinant(S)==1/determinant(M)==determinant(B)/determinant(E)
v=[[q[m][i] for i in I]]
terminal=scale(mm(mm(v,Mi),T)[0],1/Hr[m]);assert terminal==X[m]
Ml=[[sum((pad(q[r])[i]*pad(q[r])[j]/Hr[r] for r in range(m)),F(0)) for j in I] for i in I]
Mli=inverse(Ml);theta=mm(mm(v,Mli),tr(v))[0][0]
assert terminal==scale(mm(mm(v,Mli),T)[0],1/(Hr[m]+theta))
certificate={'scope':'AUXILIARY finite identity only; not an original ternary index',
 'parameters':{'m':m,'A':A,'h':h,'D':D,'nu':nu,'d':d,'n':n},
 'checks':{'base_monic_norm_orthogonality':True,'christoffel_norm_orthogonality':True,
 'full_kernel_inverse':True,'original_LOW_HIGH_projection':True,
 'upper_triangular_middle_coefficients':True,'corrected_pairing':True,
 'complementary_minor_ratio':True,'physical_terminal_row':True,
 'rank_one_complete_divisor':True},
 'matrix_M':M,'middle_T':T,'corrected_coefficients':X,'corrected_gram':S,
 'terminal_coefficients':terminal,'H_m':Hr[m],'theta':theta,
 'highest_pole_denominator':4*n-3,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'same_w_dual_interface_auxiliary_certificate.json').write_text(json.dumps(certificate,default=str,indent=2)+'\n')
print(json.dumps({'scope':certificate['scope'],'checks':certificate['checks'],'matrix_size':m+1,
 'terminal':list(map(str,terminal)),'saved':'same_w_dual_interface_auxiliary_certificate.json'}))
