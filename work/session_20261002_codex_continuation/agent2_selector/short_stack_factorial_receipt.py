"""One complete-pair receipt for the authored all-k factorial identity.

This does not extend a degree/prime atlas. It tests the basis transformation,
all relevant Gamma minors at one dimension, and the final primitive gcd.
"""
from math import factorial, gcd, lcm, comb, prod
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
k = 5
def D(m):
    return sum((-1)**j * factorial(m)//factorial(j) for j in range(m+1))
def R(r):
    return -factorial(2*r) + sum((sp.Rational(4*(-1)**(r-a), 2*a-1) for a in range(1,r+1)), sp.Integer(0))
L = lcm(*range(1,6*k-4,2))
C = sp.Matrix(k,2*k,lambda i,j:D(2*(i+j))-(-1)**(i+j))
RR = sp.Matrix(k,2*k,lambda i,j:R(i+j))
V = sp.Matrix(k,2*k,lambda i,j:(-1)**(i+j))
Pr = sp.Matrix(k,k,lambda i,j:(comb(i,j)*(-1)**(i-j) if j<=i else 0))
Pc = sp.Matrix(2*k,2*k,lambda i,j:(comb(j,i)*(-1)**(j-i) if i<=j else 0))
def am(m):
    return sum(comb(m,s)*(-2)**(m-s)*factorial(m+s) for s in range(m+1))
A = sp.Matrix(k,2*k,lambda i,j:am(i+j))
av = sp.Matrix([(-2)**i for i in range(k)])
bv = sp.Matrix([[(-2)**j for j in range(2*k)]])
assert Pr.det()==Pc.det()==1
assert Pr*C*Pc == A-av*bv
assert V*Pc == sp.Matrix([(-1)**i for i in range(k)])*bv
assert all(A[i,j]%(factorial(i)*factorial(j))==0 for i in range(k) for j in range(2*k))
Fk = prod(factorial(r) for r in range(k))
Fm = prod(factorial(r) for r in range(k-1))
minor_count = 0
for rows in [tuple(range(k))] + list(combinations(range(k),k-1)):
    d = len(rows)
    for cols in combinations(range(2*k),d):
        det = int(A.extract(rows,cols).det())
        divisor=prod(factorial(i) for i in rows)*prod(factorial(j) for j in cols)
        assert det%divisor==0
        assert det%(Fk**2 if d==k else Fm**2)==0
        minor_count += 1
raw0 = int(C.col_join(L*RR).det())
raw_at1 = int(C.col_join(L*(RR+V)).det())
raw1 = raw_at1-raw0
assert int(C.col_join(L*(RR+2*V)).det())==raw0+2*raw1
assert raw0%Fm**2==0 and raw1%Fk**2==0
assert raw0%(2**(k*(k-1))*Fm**2)==0
assert raw1%(2**(k*(k-1))*Fk**2)==0
new0 = int((A-av*bv).col_join(L*RR*Pc).det())
new1 = int(A.col_join(L*(RR+V)*Pc).det()-A.col_join(L*RR*Pc).det())
assert new0==raw0 and new1==raw1
gg = gcd(raw0,raw1)
q = abs(raw1)//gg
n0 = raw0//Fm**2
n1 = raw1//Fm**2
assert q==abs(n1)//gcd(n0,n1)
result={
    "purpose":"single complete-pair normalization and minor-divisor receipt, not an atlas",
    "k":k,"L":str(L),"F_k":str(Fk),"F_k_minus_1":str(Fm),
    "Gamma_minor_checks":minor_count,
    "full_pair_gcd":str(gg),"actual_q":str(q),"actual_q_bits":q.bit_length(),
    "constant_divisible_F_k_minus_1_squared":True,
    "response_divisible_F_k_squared":True,
    "additional_simultaneous_2_power":k*(k-1),
    "unimodular_full_pair_identity":True,
    "primitive_pair_invariant_after_common_factor":True,
    "all_assertions_passed":True,
}
(OUT/"SHORT_STACK_FACTORIAL_RECEIPT.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({key:result[key] for key in ["k","Gamma_minor_checks","actual_q_bits","all_assertions_passed"]}))
