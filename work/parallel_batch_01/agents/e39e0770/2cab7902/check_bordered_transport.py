"""One adjacent-size check of new bordered determinant identities; no scan."""
import json
import math
from functools import reduce
from pathlib import Path
import sympy as sp

k = 3
n = 2*k
maxr = 3*k+1
L = sp.Integer(reduce(sp.ilcm, range(1,6*k-4,2), 1))
D = sp.Integer(reduce(sp.ilcm, range(1,6*(k+1)-4,2), 1))
rho = D/L
assert rho.q == 1
nums = [sp.Integer(1)]
for m in range(1,2*maxr+1):
    nums.append(m*nums[-1]+(-1)**m)
C = [nums[2*r]-(-1)**r for r in range(maxr+1)]
R = [-sp.factorial(2*r)+4*sum((sp.Rational((-1)**(r-a),2*a-1) for a in range(1,r+1)),sp.Integer(0)) for r in range(maxr+1)]
V = [sp.Integer((-1)**r) for r in range(maxr+1)]
rows = [('C',i) for i in range(k)]+[('R',i) for i in range(k)]

def matrix(rr, cc, t, clearer=D):
    return sp.Matrix([[C[i+j] if typ=='C' else clearer*(R[i+j]+t*V[i+j]) for j in cc] for typ,i in rr])

def affine(rr,cc,clearer=D):
    values=[matrix(rr,cc,t,clearer).det(method='domain-ge') for t in (0,1,2)]
    assert values[2]-2*values[1]+values[0] == 0
    assert all(x.q == 1 for x in values)
    return [values[0],values[1]-values[0]]

p=affine(rows,list(range(n)),L)
nextrows=[('C',i) for i in range(k+1)]+[('R',i) for i in range(k+1)]
pnext=affine(nextrows,list(range(n+2)))
B={}
for a in ('C','R'):
    for b in (0,1):
        B[a+str(b)]=affine(rows+[(a,k)],list(range(n))+[n+b])
x00,y00=B['C0']; x01,y01=B['C1']; x10,y10=B['R0']; x11,y11=B['R1']
N=[x00*x11-x01*x10,
   x00*y11+y00*x11-x01*y10-y01*x10,
   y00*y11-y01*y10]
expected=[(-1)**k*rho**k*p[0]*pnext[0],
          (-1)**k*rho**k*(p[0]*pnext[1]+p[1]*pnext[0]),
          (-1)**k*rho**k*p[1]*pnext[1]]
assert N == expected
G=sp.igcd(*p); Gnext=sp.igcd(*pnext)
Gamma=reduce(sp.igcd,N)
assert Gamma == rho**k*G*Gnext

# Read, but do not execute or recalculate, the previously saved recurrence.
old=Path('work/parallel_batch_01/agents/e39e0770/57bd747d/ACTUAL_RECURRENCE_RECEIPT.json')
s=sp.Symbol('s')
q=[sp.sympify(x,locals={'s':s}) for x in json.loads(old.read_text())['q_coefficients_in_s']]
def coeff(ell,r):
    return q[ell].subs(s,2*r+1)

j=3
levels=list(range(k+1))
sigma=sp.prod(coeff(4,j+i) for i in levels)
transport_checks=[]
for a in ('C','R'):
    rr=rows+[(a,k)]
    U=matrix(rr,list(range(n)),0)
    def col(t): return matrix(rr,[t],0)
    def projected(t,i):
        out=col(t)
        for z,(_,level) in enumerate(rr):
            if level!=i: out[z,0]=0
        return out
    lhs=sigma*U.row_join(col(j+4)).det(method='domain-ge')
    terms=[]
    for i in levels:
        for ell in range(4):
            minor=U.row_join(projected(j+ell,i)).det(method='domain-ge')
            factor=(sigma/coeff(4,j+i))*coeff(ell,j+i)
            assert factor.q==1
            terms.append(factor*minor)
    assert lhs == -sum(terms)
    # The actual column has nonzero support at each level. Its q4-orbit
    # therefore has the predicted k+1-dimensional linear weight boundary.
    J=sp.diag(*[i for _,i in rr])
    Q4=sp.diag(*[coeff(4,j+i) for _,i in rr])
    w=col(j)
    orbit=sp.Matrix.hstack(*[Q4**m*w for m in range(k+1)])
    assert orbit.rank()==k+1
    vand=sp.Matrix([[i**m for m in levels] for i in levels])
    assert vand.det()==sp.prod(sp.factorial(i) for i in levels)
    transport_checks.append({'row_type':a,'lhs':str(lhs),'terms':len(terms),'weight_orbit_rank':k+1})

receipt={'purpose':'Single k=3 to k=4 test of new fraction-free bordered condensation, actual gcd product, and projected-column recurrence; not an old audit or a scan.',
 'k':k,'L_k':str(L),'L_next':str(D),'rho':str(rho),
 'physical_pair_k':[str(x) for x in p], 'physical_pair_next':[str(x) for x in pnext],
 'border_pairs':{key:[str(x) for x in val] for key,val in B.items()},
 'quadratic_coefficients':[str(x) for x in N],
 'G_k':str(G),'G_next':str(Gnext),'Gamma':str(Gamma),
 'projection_start':j,'projection_sigma':str(sigma),'projection_checks':transport_checks,
 'checks':{'four_borders_affine':True,'three_coefficient_condensation_identities':True,'exact_gcd_product':True,'fraction_free_projector_transport':True,'actual_weight_boundary_rank':True},
 'limitations':'No uniform content bound; no exclusion of special nonlinear closure; no independent review.'}
Path('BORDERED_TRANSPORT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'all assertions passed','k':k,'borders':4,'projected_minor_terms_per_border':4*(k+1),'receipt':'BORDERED_TRANSPORT_RECEIPT.json'},indent=2))
