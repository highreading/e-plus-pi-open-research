import json
import math
import sympy as sp
from functools import reduce
from pathlib import Path

s, y = sp.symbols('s y')
P = s**3 + 4*s**2 + 5*s + 1
J = s**4 + 8*s**3 + 23*s**2 + 30*s + 13
T = 2*s**6 + 32*s**5 + 215*s**4 + 768*s**3 + 1527*s**2 + 1588*s + 665
shift = lambda f, j: f.subs(s, s+2*j)
W = P*shift(J,1)/(s+4) - shift(P,1)*J/(s+2)
assert sp.cancel(W + 2*T/((s+2)*(s+4))) == 0
A = sp.expand(T*(s+6))
B = sp.expand((s+4)*(shift(P,2)*J*(s+6)-P*shift(J,2)*(s+2))/2)
Ccoef = sp.expand(shift(T,1)*(s+2))
assert all(c.q == 1 for c in sp.Poly(B,s).all_coeffs())
m = [Ccoef, -B, A]
for f in [P, J/(s+2)]:
    assert sp.cancel(sum(m[i]*shift(f,i) for i in range(3))) == 0

a = s*(s+1)
a1 = (s+2)*(s+3)
h = [-a*(a1+1), 1-a*a1, a+1]
d, f, ell, v = sp.symbols('d f ell v')
dseq = [d, a*d-s, a1*(a*d-s)-(s+2)]
fseq = [f, a*f, a1*a*f]
lseq = [ell, -ell+4/s, ell-4/s+4/(s+2)]
vseq = [v,-v,v]
assert sp.expand(sum(h[j]*(dseq[j]-vseq[j]) for j in range(3)) + 2*P) == 0
assert sp.cancel(sum(h[j]*(-fseq[j]+lseq[j]) for j in range(3)) + 4*J/(s+2)) == 0
assert sp.expand(sum(h[j]*vseq[j] for j in range(3))) == 0
qcoef = [sp.expand(sum(m[i]*shift(h[j-i],i) for i in range(3) if 0 <= j-i <= 2)) for j in range(5)]
assert sp.expand(qcoef[4] - T*(s+6)*((s+4)*(s+5)+1)) == 0
assert all(c.q == 1 for q in qcoef for c in sp.Poly(q,s).all_coeffs())

k = 4
n = 2*k
maxr = 3*k-2
Dnums = [sp.Integer(1)]
for j in range(1,2*maxr+1):
    Dnums.append(j*Dnums[-1]+(-1)**j)
Cmom = [Dnums[2*r]-(-1)**r for r in range(maxr+1)]
Rmom = [-sp.factorial(2*r)+4*sum((sp.Rational((-1)**(r-j),2*j-1) for j in range(1,r+1)),sp.Integer(0)) for r in range(maxr+1)]
Vmom = [sp.Integer((-1)**r) for r in range(maxr+1)]
recurrence_checks = 0
for moments in [Cmom,Rmom,Vmom]:
    for r in range(maxr-3):
        assert sum(qcoef[j].subs(s,2*r+1)*moments[r+j] for j in range(5)) == 0
        recurrence_checks += 1

def O(poly):
    out = sp.Integer(0)
    for (r,), coeff in sp.Poly(poly,y).terms():
        out += sum(coeff*qcoef[j].subs(s,2*r+1)*y**(r+j) for j in range(5))
    return sp.expand(out)

def evaluate(moments,poly):
    return sum(coeff*moments[r] for (r,), coeff in sp.Poly(poly,y).terms())

basis = [sp.Integer(1),y,y**2-4*y,y**3-133*y] + [O(y**r) for r in range(n-4)]
BT = sp.Matrix([[sp.expand(poly).coeff(y,r) for poly in basis] for r in range(n)])
Xi = sp.prod(qcoef[4].subs(s,2*r+1) for r in range(n-4))
assert BT.det() == Xi
for poly in basis[4:]:
    for moments in [Cmom,Rmom,Vmom]:
        assert evaluate(moments,poly) == 0
L = sp.Integer(reduce(sp.ilcm,range(1,6*k-4,2),1))
M0 = sp.Matrix([[Cmom[i+j] for j in range(n)] for i in range(k)] + [[L*Rmom[i+j] for j in range(n)] for i in range(k)])
MV = sp.Matrix([[0 for j in range(n)] for i in range(k)] + [[L*Vmom[i+j] for j in range(n)] for i in range(k)])
assert all(x.q == 1 for x in M0)
I0 = M0.det(method='domain-ge')
I1 = (M0+MV).det(method='domain-ge')-I0
head_values = [[evaluate(moments,poly) for poly in basis[:4]] for moments in [Cmom,Rmom,Vmom]]
assert head_values[0] == [0,2,0,0]
assert head_values[1] == [-1,2,-sp.Rational(104,3),-sp.Rational(14738,15)]
assert head_values[2] == [1,-1,5,132]
remaining = [basis[j] for j in [0,2,3]+list(range(4,n))]
residual = sp.Matrix([[evaluate(Cmom,y**i*poly) for poly in remaining] for i in range(1,k)] + [[L*(evaluate(Rmom,y**i*poly)-(-1)**i*evaluate(Rmom,poly)) for poly in remaining] for i in range(1,k)])
assert residual.shape == (2*k-2,2*k-1)
assert all(x.q == 1 for x in residual)
z = [(-1)**j*residual[:,[a for a in range(2*k-1) if a != j]].det(method='domain-ge') for j in range(2*k-1)]
z0,z2,z3 = z[:3]
Y = z0+5*z2+132*z3
Dout = 445*z2+12758*z3
Z = -112*z2-3211*z3
epsilon = (-1)**k
assert Xi*I0 == -epsilon*(2*L/15)*(15*Y+Dout)
assert Xi*I1 == epsilon*2*L*Y
G = sp.igcd(I0,I1)
gnew = sp.igcd(Dout,15*Y)
assert Xi*G == (2*L/15)*gnew
assert abs(I1)/G == 15*abs(Y)/gnew
U = sp.Matrix([[1,5,132],[0,445,12758],[0,-112,-3211]])
line = sp.Matrix([5050,-12758,445])
assert U.det() == 1
assert U*line == sp.Matrix([0,0,1])
assert U*sp.Matrix([z0,z2,z3]) == sp.Matrix([Y,Dout,Z])
receipt = {
 'purpose':'One exact test of the new common recurrence, nonunimodular basis, endpoint extraction and final gcd; no degree or prime atlas.',
 'symbolic_checks': {'casoratian':True,'M_annihilates_both_forcings':True,'H_complete_endpoint_identities':True,'integer_recurrence_coefficients':True,'leading_coefficient':True,'fixed_coordinate_map_unimodular':True},
 'q_coefficients_in_s':[str(q) for q in qcoef],
 'k':k,'recurrence_evaluations':recurrence_checks,'L':str(L),'Xi':str(Xi),
 'head_values':[[str(x) for x in row] for row in head_values],
 'I0':str(I0),'I1':str(I1),'G':str(G),'primitive_denominator':str(abs(I1)//G),
 'z0':str(z0),'z2':str(z2),'z3':str(z3),'Y':str(Y),'D':str(Dout),'Z':str(Z),'gcd_D_15Y':str(gnew),
 'checks':{'basis_index':True,'actual_pair_identity':True,'actual_gcd_identity':True,'actual_denominator_identity':True},
 'scope':'Exact symbolic and single-instance checks support the written algebra. They prove no uniform bound on the actual cofactor congruence depth.'
}
Path('ACTUAL_RECURRENCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'all assertions passed','k':k,'recurrence_evaluations':recurrence_checks,'receipt':'ACTUAL_RECURRENCE_RECEIPT.json','Xi_bits':int(Xi).bit_length(),'G_bits':int(G).bit_length()},indent=2))
