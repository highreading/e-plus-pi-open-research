"""One multi-block structural receipt for the odd-saturation proof."""
from math import factorial, comb, prod
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent
def am(m):
    return sum(comb(m,s)*(-2)**(m-s)*factorial(m+s) for s in range(m+1))
def tm(m):
    assert am(m)%factorial(m)==0
    return am(m)//factorial(m)
def vp(x,p):
    if x==0:
        raise ValueError("valuation of zero was not requested")
    e=0
    while x%p==0:
        x//=p
        e+=1
    return e
# The complete inhomogeneous ODE, including its exceptional initial forcing.
z=sp.Symbol('z')
f=sum(am(m)*z**m for m in range(25))
res=sp.expand(4*z**3*(1+z)*sp.diff(f,z,2)+2*z**2*(5+8*z)*sp.diff(f,z)+(8*z**2+2*z-1)*f-(2*z-1))
assert all(res.coeff(z,m)==0 for m in range(25))
# One block with a genuinely non-leading optimal choice of low columns.
k,p=8,5
u,s=divmod(k,p)
base=sp.Matrix(p,p,lambda b,d:comb(b+d,b)*tm(b+d)%p)
assert int(base.det())%p==1
D=next(dd for dd in combinations(range(p),s) if int(base.extract(range(s),dd).det())%p)
J=list(range(u*p))+[u*p+d for d in D]
assert D!=(0,1,2) and max(J)<2*k
B=sp.Matrix(k,2*k,lambda i,j:comb(i+j,i)*tm(i+j))
assert int(B[:,J].det())%p
for i in range(k):
    for j in range(2*k):
        a,b=divmod(i,p)
        c,d=divmod(j,p)
        assert B[i,j]%p==pow(-2,a+c,p)*comb(a+c,a)*int(base[b,d])%p
A=sp.Matrix(k,2*k,lambda i,j:am(i+j))
full_minor=int(A[:,J].det())
Fk=prod(factorial(i) for i in range(k))
assert vp(full_minor,p)==2*vp(Fk,p)
assert sum(vp(factorial(j),p) for j in J)==vp(Fk,p)
result={
    "purpose":"one factorial-optimal multi-block minor and exact formal ODE, not a prime atlas",
    "k":k,"prime":p,"low_selected_columns":list(D),"actual_selected_columns":J,
    "normalized_minor_is_prime_unit":True,
    "Gamma_minor_prime_valuation":vp(full_minor,p),
    "twice_F_k_prime_valuation":2*vp(Fk,p),
    "formal_ODE_coefficient_checks":25,
    "block_tensor_checks":k*2*k,
    "all_assertions_passed":True,
}
(OUT/"EVEN_GAMMA_SATURATION_RECEIPT.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
