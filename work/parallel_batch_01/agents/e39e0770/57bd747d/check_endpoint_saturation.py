import json
from functools import reduce
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

# One exact instance tests the new endpoint-saturation identities.
k = 4
n = 2*k
maxr = 3*k-2
D = [sp.Integer(1)]
for j in range(1, 2*maxr+1):
    D.append(j*D[-1]+(-1)**j)
C = [D[2*r]-(-1)**r for r in range(maxr+1)]
R = [-sp.factorial(2*r)+4*sum((sp.Rational((-1)**(r-a),2*a-1) for a in range(1,r+1)),sp.Integer(0)) for r in range(maxr+1)]
V = [sp.Integer((-1)**r) for r in range(maxr+1)]
L = sp.Integer(reduce(sp.ilcm, range(1,6*k-4,2),1))
H = sp.Integer(reduce(sp.ilcm, range(1,2*n-2,2),1))
base = sp.eye(n)
for r in range(2,n):
    assert C[r] % 2 == 0
    base[1,r] = -C[r]/2
    base[0,r] = -V[r]-C[r]/2
assert base.det() == 1
endC = sp.Matrix(1,n,C[:n])
endR = sp.Matrix(1,n,R[:n])
endV = sp.Matrix(1,n,V[:n])
a = H*(endR*base)[:,2:]
assert all(x.q == 1 for x in a)
assert reduce(sp.igcd,a) == 1
U = sp.eye(n-2)
for j in range(1,n-2):
    current = a*U
    x,y = current[0,0],current[0,j]
    s,t,g = sp.gcdex(x,y)
    assert s*x+t*y == g and g > 0
    step = sp.eye(n-2)
    step[0,0],step[j,0] = s,t
    step[0,j],step[j,j] = -y/g,x/g
    assert step.det() == 1
    U = U*step
assert a*U == sp.Matrix([[1]+[0]*(n-3)])
# Flip v and one kernel vector, preserving positive full orientation.
U[:,0] = -U[:,0]
U[:,1] = -U[:,1]
B = base*sp.diag(sp.eye(2),U)
assert B.det() == 1
assert all(x.q == 1 for x in B)
endpoint = endC.col_join(endV).col_join(L*endR)
expected = sp.zeros(3,n)
expected[0,1] = 2
expected[1,0],expected[1,1] = 1,-1
expected[2,0],expected[2,1],expected[2,2] = -L,2*L,-L/H
assert endpoint*B == expected
snf = smith_normal_form(endpoint,domain=sp.ZZ)
smith = [abs(snf[i,i]) for i in range(3)]
assert smith == [1,1,2*L/H]

def moment(mom, col, shift=0):
    return sum(B[r,col]*mom[r+shift] for r in range(n))

cols = [0]+list(range(2,n))
res = sp.Matrix([[moment(C,j,i) for j in cols] for i in range(1,k)] + [[L*(moment(R,j,i)-(-1)**i*moment(R,j)) for j in cols] for i in range(1,k)])
assert all(x.q == 1 for x in res)
b0 = res[:,1:].det(method='domain-ge')
b2 = -res[:,[0]+list(range(2,n-1))].det(method='domain-ge')
old = json.loads(Path('ACTUAL_RECURRENCE_RECEIPT.json').read_text())
I0,I1,G,Xi,Y,Dout = [sp.Integer(old[name]) for name in ['I0','I1','G','Xi','Y','D']]
assert I0 == (-1)**k*(2*L/H)*(-H*b0-b2)
assert I1 == (-1)**k*2*L*b0
Gb = sp.igcd(b2,H*b0)
assert G == (2*L/H)*Gb
assert abs(I1)/G == H*abs(b0)/Gb
assert Y == Xi*b0
assert Dout == (15*Xi/H)*b2
assert (15*Xi/H).q == 1
receipt = {
    'purpose':'Single-instance check of the new exact endpoint saturation, Smith invariants and full physical pair; no scan.',
    'k':k,'n':n,'L':str(L),'H_n':str(H),
    'endpoint_gcd':1,'basis_determinant':1,
    'endpoint_smith_invariants':[str(x) for x in smith],
    'basis_columns':[[str(B[i,j]) for i in range(n)] for j in range(n)],
    'b0':str(b0),'b2':str(b2),'gcd_b2_Hb0':str(Gb),
    'recurrence_kernel_index':str(15*Xi/H),
    'checks':{'endpoint_image':True,'unimodular_basis':True,'endpoint_smith':True,'both_physical_coefficients':True,'final_gcd':True,'primitive_denominator':True,'recurrence_index_reconciliation':True},
    'scope':'Bounded verification of the written identities; not a uniform content bound or independent review.'
}
Path('ENDPOINT_SATURATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'all assertions passed','k':k,'L':str(L),'H_n':str(H),'smith':[str(x) for x in smith],'receipt':'ENDPOINT_SATURATION_RECEIPT.json'},indent=2))
