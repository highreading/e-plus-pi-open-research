"""Selected exact algebra checks for b=1 theorem; no rank/degree scan.

Represent linear expressions in pi by pairs of rational polynomials.
Verify CD rational remainder, endpoint reconstruction, and all high rows.
"""
from fractions import Fraction as Q
from pathlib import Path
from functools import reduce
import math,json

def add(a,b):
    c=[(a[j] if j<len(a) else Q(0))+(b[j] if j<len(b) else Q(0)) for j in range(max(len(a),len(b)))]
    while len(c)>1 and c[-1]==0:c.pop()
    return c
def scale(a,c):return [x*c for x in a]
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return add(c,[Q(0)])
def ps(n):
    p=[[Q(1)],[Q(-1,2),Q(1)]]
    for k in range(1,n):p.append(add(mul(p[-1],[Q(-1,2),Q(1)]),scale(p[-2],Q(k*k,4*(4*k*k-1)))))
    return p[:n+1]
def h(k):return Q(2*(-1)**k,(2*k+1)*math.comb(2*k,k)**2)
def moment(j):
    # Directly integrate ((1+iu)/2)^j over u=-1..1; no archived jet function.
    return sum((Q(2*math.comb(j,r)*(-1)**(r//2),(r+1)*2**j) for r in range(0,j+1,2)),Q(0))
def L(p):return sum((a*moment(j) for j,a in enumerate(p)),Q(0))
def v_pair(p):
    # (p(1)-p(t))/(1-t), by exact synthetic division.
    diff=scale(p,-1);diff[0]+=sum(p)
    qq=[];prev=Q(0)
    for a in diff[:-1]:prev+=a;qq.append(prev)
    assert add(mul(qq,[Q(1),Q(-1)]),scale(diff,-1))==[0]
    return -L(qq),sum(p)
def ell(p,n,j):return sum((a/Q(math.factorial(n+k+1-j)) for k,a in enumerate(p)),Q(0))
def trunc_prod(A,B,n):return mul(A,B)[:n+1]
rows=[]
for n in [1,2,8,16]:
    p=ps(n+1);vv=[v_pair(x) for x in p]
    H0=[Q(0)];H1=[Q(0)]
    for k in range(n+1):
        H0=add(H0,scale(p[k],vv[k][0]/h(k)))
        H1=add(H1,scale(p[k],vv[k][1]/h(k)))
    # h_n*((1-t)^(-1)-H) numerator equals v_n*p_(n+1)-v_(n+1)*p_n.
    lhs0=scale(add([Q(1)],scale(mul([Q(1),Q(-1)],H0),-1)),h(n))
    lhs1=scale(mul([Q(1),Q(-1)],H1),-h(n))
    rhs0=add(scale(p[n+1],vv[n][0]),scale(p[n],-vv[n+1][0]))
    rhs1=add(scale(p[n+1],vv[n][1]),scale(p[n],-vv[n+1][1]))
    assert add(lhs0,scale(rhs0,-1))==[0]
    assert add(lhs1,scale(rhs1,-1))==[0]
    t=[];Cj=[]
    for j in [0,1]:
        cs=[Q(0)]
        for k in range(n+1):cs=add(cs,scale(p[k],-ell(p[k],n,j)/h(k)))
        cs+= [Q(0)]*(n+1-len(cs))
        Cj.append(list(reversed(cs)));t.append(-sum(cs))
    B=[1+t[1],-1-t[0]]
    C=add(scale(Cj[0],B[0]),scale(Cj[1],B[1]));Y=sum(B)
    assert sum(C)==Y==t[1]-t[0]
    ff=[Q(0)]+[moment(k-1) for k in range(1,2*n+2)]
    ee=[Q(1,math.factorial(k)) for k in range(2*n+2)]
    combined=add(mul(B,ee),mul(C,ff))
    A=scale(combined[:n+1],-1)
    assert all((combined[k] if k<len(combined) else 0)==0 for k in range(n+1,2*n+2))
    X=sum(A)
    # ell_B(h-H)=Y*e + X + Y*pi, exactly in its three coefficients.
    epart=sum(B)
    pipart=-sum(B[j]*ell(H1,n,j) for j in [0,1])
    rational=-sum(B[j]*(sum(ee[:n+1-j])+ell(H0,n,j)) for j in [0,1])
    assert epart==Y and pipart==Y and rational==X
    T=2**(2*n+1)*math.factorial(2*n+1)
    dF=2**n*math.lcm(*range(1,n+1));D=T*T*dF
    assert (D*X).denominator==(D*Y).denominator==1
    rows.append({'n':n,'CD_rational_remainder_identity':True,'endpoint_and_high_rows':True,'remainder_e_and_pi_coefficients_equal_Y':True,'explicit_denominator_clears':True,'Y_zero':Y==0})
# Selected transform sign controls, no rank calculation.
for n,k in [(64,0),(64,1),(64,63),(64,64),(128,128)]:
    p=ps(k)[k]
    assert (-1)**k*(ell(p,n,1)-ell(p,n,0))>0
    assert (-1)**k*ell(p,n,1)>0
    rows.append({'N':n,'k':k,'selected_exact_factorial_transform_sign':True})
out={'status':'PASS; bounded algebra checks, not an asymptotic inference','rows':rows}
Path(__file__).with_name('hp_b1_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
