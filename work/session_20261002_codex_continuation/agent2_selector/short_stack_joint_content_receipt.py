"""One actual short-stack two-rectangle/full-gcd interface receipt."""
from math import factorial, gcd, lcm, prod
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent
k=5
def d(r):
    m=2*r
    return sum((-1)**j*factorial(m)//factorial(j) for j in range(m+1))
def rr(r):
    return -factorial(2*r)+sum((sp.Rational(4*(-1)**(r-a),2*a-1) for a in range(1,r+1)),sp.Integer(0))
def kk(r):
    return -factorial(2*r)-factorial(2*r+2)+sp.Rational(4,2*r+1)
def gg(r):
    return d(r)+d(r+1)
def content(X):
    S=smith_normal_form(X,domain=sp.ZZ)
    return abs(prod(int(S[i,i]) for i in range(min(X.shape))))
L=lcm(*range(1,6*k-4,2))
C=sp.Matrix(k,2*k,lambda i,j:d(i+j)-(-1)**(i+j))
R=sp.Matrix(k,2*k,lambda i,j:rr(i+j))
V=sp.Matrix(k,2*k,lambda i,j:(-1)**(i+j))
M=C.col_join(L*R)
I0=int(M.det())
I1=int(C.col_join(L*(R+V)).det())-I0
assert I1%L==0
J1=I1//L
N=sp.Matrix(k,2*k-1,lambda i,j:gg(i+j)).col_join(sp.Matrix(k,2*k-1,lambda i,j:L*kk(i+j)))
W=C.col_join(sp.Matrix(k-1,2*k,lambda i,j:L*kk(i+j)))
assert all(v.is_Integer for v in N) and all(v.is_Integer for v in W)
hN=content(N)
hW=content(W)
G0=gcd(I0,J1)
Ga=gcd(I0,I1)
assert I0%hN==J1%hN==I0%hW==J1%hW==0
assert G0%lcm(hN,hW)==0 and (hN*hW)%G0==0
assert Ga%lcm(hN,hW)==0 and (L*hN*hW)%Ga==0
q=abs(I1)//Ga
assert sp.Rational(abs(J1),hN*hW)<=q<=sp.Rational(L*abs(J1),lcm(hN,hW))
saved=json.loads((OUT/'SHORT_STACK_FACTORIAL_RECEIPT.json').read_text())
assert str(q)==saved['actual_q']
rem=Ga
small={}
for p in sp.primerange(2,6*k-4):
    e=0
    while rem%p==0:
        rem//=p;e+=1
    if e:small[str(p)]=e
result={
    'purpose':'one existing complete normalization and new rectangular contents, not an atlas',
    'k':k,'L':str(L),'h_N':str(hN),'h_W':str(hW),
    'base_pair_gcd':str(G0),'physical_pair_gcd':str(Ga),
    'actual_q':str(q),'actual_q_bits':q.bit_length(),
    'physical_gcd_factors_at_or_below_row_denominator_bound':small,
    'remaining_physical_gcd_cofactor':str(rem),
    'complete_gcd_sandwich_checked':True,'all_assertions_passed':True,
}
(OUT/'SHORT_STACK_JOINT_CONTENT_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:result[key] for key in ['k','h_N','h_W','actual_q_bits','remaining_physical_gcd_cofactor','all_assertions_passed']}))
