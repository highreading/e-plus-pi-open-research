"""One pre-existing M24 pair, testing the new simultaneous monic basis."""
from math import factorial, gcd, lcm
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent
k=5
y=sp.symbols('y')
def v2(n):
    n=abs(int(n))
    if n==0:return 10**9
    return (n & -n).bit_length()-1
def m(j):return j//2
def b(j):return v2(factorial(m(j)))
def a(j):return m(j)+b(j)
def ss(n):return sum(a(j) for j in range(n))
def en(k):return 2*ss(k)-a(k-1)+ss(2*k-1)+k-1
def ew(k):return ss(k)+ss(k-1)+ss(2*k)-a(2*k-1)-b(k-1)-b(2*k-1)
def basis(n):
    return sp.Matrix(n,n,lambda i,j:sp.expand(y**(i%2)*(y*(y-1))**(i//2)).coeff(y,j))
def der(r):
    n=2*r
    return sum((-1)**j*factorial(n)//factorial(j) for j in range(n+1))
def gg(r):return der(r)+der(r+1)
def kk(r):return -factorial(2*r)-factorial(2*r+2)+sp.Rational(4,2*r+1)
L=lcm(*range(1,6*k-4,2))
N=sp.Matrix(k,2*k-1,lambda i,j:gg(i+j)).col_join(sp.Matrix(k,2*k-1,lambda i,j:L*kk(i+j)))
W=sp.Matrix(k,2*k,lambda i,j:der(i+j)-(-1)**(i+j)).col_join(sp.Matrix(k-1,2*k,lambda i,j:L*kk(i+j)))
Tk,Tkm,TcN,TcW=basis(k),basis(k-1),basis(2*k-1),basis(2*k)
assert all(T.det()==1 for T in [Tk,Tkm,TcN,TcW])
Nt=sp.diag(Tk,Tk)*N*TcN.T
Wt=sp.diag(Tk,Tkm)*W*TcW.T
checks=0
for i in range(2*k):
    for j in range(2*k-1):
        assert Nt[i,j].is_Integer
        assert v2(Nt[i,j])>=a(i%k)+a(j)+(1 if i<k else 0)
        checks+=1
D=sp.Matrix(k,2*k,lambda i,j:der(i+j))
Dt=Tk*D*TcW.T
top_eval=sp.Matrix([(-1)**(i%2)*2**m(i) for i in range(k)])
col_eval=sp.Matrix([(-1)**(j%2)*2**m(j) for j in range(2*k)])
assert Wt[:k,:]==Dt-top_eval*col_eval.T
for i in range(k):
    for j in range(2*k):
        assert v2(Dt[i,j])>=a(i)+a(j)
        checks+=1
for i in range(k-1):
    for j in range(2*k):
        assert v2(Wt[k+i,j])>=a(i)+a(j)
        checks+=1
hn=0
for omitted in range(2*k):
    d=int(Nt.extract([i for i in range(2*k) if i!=omitted],range(2*k-1)).det())
    assert v2(d)>=en(k)
    hn=gcd(hn,d)
hw=0
for omitted in range(2*k):
    d=int(Wt.extract(range(2*k-1),[j for j in range(2*k) if j!=omitted]).det())
    assert v2(d)>=ew(k)
    hw=gcd(hw,d)
old=json.loads((OUT/'SHORT_STACK_JOINT_CONTENT_RECEIPT.json').read_text())
assert abs(hn)==int(old['h_N']) and abs(hw)==int(old['h_W'])
ga=int(old['physical_pair_gcd'])
assert v2(ga)>=en(k)
# Exact polynomial identity behind the COMPLETE compact part, one mixed product.
i,j=4,7
mm=m(i)+m(j);u=mm+i%2+j%2
moment=sum((sp.Rational((-1)**(mm-s)*sp.binomial(mm,s),2*(u+s)+1) for s in range(mm+1)),sp.Integer(0))
beta=sp.Rational((-1)**mm*2**mm*factorial(mm),sp.prod(2*u+2*s+1 for s in range(mm+1)))
assert moment==beta
# Pricing the guaranteed exponent only; this is not a new complete-pair case.
K=64
olddepth=K*(K-1)+2*sum(v2(factorial(j)) for j in range(K-1))
out={
 'purpose':'new basis/entry/maximal-minor identity at one existing full pair; no degree or prime atlas',
 'k':k,'unimodular_basis_checks':4,'entry_checks':checks,
 'maximal_minor_checks':4*k,'E_N':en(k),'E_W':ew(k),
 'actual_v2_h_N':v2(hn),'actual_v2_h_W':v2(hw),'actual_v2_full_gcd':v2(ga),
 'saved_actual_q_bits':old['actual_q_bits'],
 'coefficient_formula_index_only':K,'new_guaranteed_depth':en(K),
 'old_guaranteed_depth':olddepth,'additional_guaranteed_depth':en(K)-olddepth,
 'complete_beta_identity_checked':True,'all_assertions_passed':True
}
(OUT/'SHORT_STACK_BOOLEAN_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
