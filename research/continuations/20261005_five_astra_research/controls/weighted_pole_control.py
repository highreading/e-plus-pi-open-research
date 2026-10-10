"""Coordinator-authored exact audit of the new highest-pole cancellation."""
import json
import math
import resource
from pathlib import Path
import sympy as s

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
OUT = Path(__file__).resolve().parent
prior = json.loads((OUT/'weighted_control.json').read_text())
case = next(a for a in prior if a['n'] == 5)
n, prime = 5, 17
coeff = case['Q_coefficients']
k = (n+1)//2
der = [1]
for j in range(1, 4*n):
    der.append(j*der[-1]+(-1)**j)
orth = [sum(coeff[a]*(der[2*(i+a)]-(-1)**(i+a))
            for a in range(n+1)) for i in range(n)]
assert not any(orth)
Ls = [s.Integer(0)]
for j in range(1, 2*n):
    Ls.append(4*sum(s.Rational((-1)**h, 2*j-1-2*h) for h in range(j)))
R = s.Matrix(k,k,lambda i,j:sum(coeff[a]*(-math.factorial(2*(i+j+a))+Ls[i+j+a]) for a in range(n+1)))
basis = s.eye(k)
for j in range(1,k): basis[0,j] = -(-1)**j
Rend = basis.T*R*basis
ell = s.ilcm(*range(1,4*n-2,2))
w = sum(a*(-1)**j for j,a in enumerate(coeff))
Tmat = ell*Rend
assert all(a.q == 1 for a in Tmat)
Kmat = Tmat[1:,1:]
A = Tmat.det()
B = ell*w*Kmat.det()
g = math.gcd(int(A),int(B))
def vp(a):
    a=s.Rational(a)
    if a==0:return None
    num,den=abs(int(a.p)),int(a.q)
    out=0
    while num%prime==0:num//=prime;out+=1
    while den%prime==0:den//=prime;out-=1
    return out
def residue(a):
    a=s.Rational(a)
    assert a.q%prime
    return int(a.p)%prime*pow(int(a.q),-1,prime)%prime
pole=(prime*R).applyfunc(residue)
degree=max(j for j,a in enumerate(coeff) if a%prime)
h=max(0,n+degree-(prime+1)//2)
size=k-h
# Independent modular Gaussian elimination.
rows=[list(pole.row(i)) for i in range(k)]
rank=0
for col in range(k):
    piv=next((i for i in range(rank,k) if rows[i][col]%prime),None)
    if piv is None:continue
    rows[rank],rows[piv]=rows[piv],rows[rank]
    inv=pow(int(rows[rank][col]),-1,prime)
    for i in range(rank+1,k):
        f=rows[i][col]*inv%prime
        rows[i]=[(a-f*b)%prime for a,b in zip(rows[i],rows[rank])]
    rank+=1
assert rank==h
Dmat=Tmat[size:,size:]
E=(Tmat[:size,:size]-Tmat[:size,size:]*Dmat.inv()*Tmat[size:,:size])/prime
E0=E[1:,1:]
u=s.Rational(ell,prime)
identity_A=s.cancel(A-prime**size*Dmat.det()*E.det())
identity_B=s.cancel(B-prime**size*u*w*Dmat.det()*E0.det())
assert identity_A==identity_B==0
expected_g=size+min(vp(E.det()),vp(w)+vp(E0.det()))
expected_q=max(0,vp(w)+vp(E0.det())-vp(E.det()))
assert vp(g)==expected_g
assert vp(B/g)==expected_q
def matrix_record(mat):return [[str(a) for a in mat.row(i)] for i in range(mat.rows)]
record={'n':n,'prime':prime,'Q':coeff,'orthogonality_residuals':orth,
        'ell':str(ell),'degree_mod_prime':degree,'highest_pole':matrix_record(pole),
        'actual_rank':rank,'predicted_rank':h,'schur_dimension':size,
        'D':matrix_record(Dmat),'E':matrix_record(E),'E0':matrix_record(E0),
        'identity_A':str(identity_A),'identity_B':str(identity_B),
        'g_valuation':vp(g),'formula_g_valuation':expected_g,
        'actual_q_valuation':vp(B/g),'formula_q_valuation':expected_q,
        'status':'exact finite normalization audit; not an all-index proof'}
(OUT/'weighted_pole_control.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({a:record[a] for a in ('n','prime','degree_mod_prime','actual_rank','predicted_rank','schur_dimension','g_valuation','actual_q_valuation','identity_A','identity_B','status')},indent=2))
