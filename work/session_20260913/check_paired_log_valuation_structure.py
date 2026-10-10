"""Root's independent exact coefficient audit for the valued pair theorem."""
import json
from math import comb
from pathlib import Path
import sympy as s

base=Path(__file__).parent
r=s.Symbol('r')
op=json.loads((base/'witt_period_operator_symbolic.json').read_text())['0']
co=json.loads((base/'witt_period_contiguity_symbolic.json').read_text())
c=[s.sympify(v,locals={'r':r}) for v in op['recurrence_coefficients']]
a=[s.sympify(v,locals={'r':r}) for v in co['period_coefficients']]
S=176275*r**6-6297825*r**5+89867547*r**4-649457253*r**3+2470644018*r**2-4573809342*r+3062922660
DH=40960*(r-3)*(2*r-21)*(2*r-15)*(2*r-9)*(2*r-3)*(2*r+3)*S
H=[s.Poly(s.cancel(DH*r*a[k]),r) for k in (1,2)]
assert all(v.degree()==12 and all(x.q==1 for x in v.all_coeffs()) for v in H)
T=s.Matrix([[0,1,0],[0,0,1],[-c[0]/c[3],-c[1]/c[3],-c[2]/c[3]]])
M=s.simplify(c[3]*T)
assert all(s.Poly(v,r).degree()<=17 for v in M)
C=T.applyfunc(lambda v:s.limit(v,r,s.oo))
assert C==s.Matrix([[0,1,0],[0,0,1],[s.Rational(16777216,531441),s.Rational(40370176,19683),s.Rational(26446912,729)]])
assert all(C[2,k]>0 for k in range(3))
A=[s.limit(r*a[k],r,s.oo) for k in (1,2)]
assert A[0]<0<A[1]
leading=[]
for d in (1,2,3,4):
    # Leading coefficient proof is exact for every d; these anchor its orientation.
    lead=s.Poly(c[3],r).LC()**d*(H[0].LC()*(C**d)[0,2]-H[1].LC()*(C**d)[0,1])
    assert lead!=0 and lead.q==1
    leading.append({'d':d,'degree':17*d+12,'leading_coefficient':str(lead)})

def Cnu(m,nu):
    N=4*m+nu; K=4*m+1+nu
    ans=0
    for b in range(2+3*nu):
        for aa in range(min(6*m,N-b)+1):
            rest=N-aa-b
            if rest>=0 and rest%2==0:
                j=rest//2
                ans+=(-1)**(aa+j)*comb(6*m,aa)*comb(1+3*nu,b)*comb(K+j-1,j)
    return ans

def L(m,nu): return s.Rational(Cnu(m,nu),2**(2*m+2*nu))
rows=[]
for m in (4,5,6,8):
    assert sum(c[k].subs(r,6*m)*L(m-k,0) for k in range(4))==0
    assert s.cancel(L(m,1)-sum(a[k].subs(r,6*m)*L(m-k,0) for k in range(3)))==0
    rows.append({'m':m,'recurrence_and_contiguity':True})
out={'status':'passed','H_degrees':[v.degree() for v in H],
     'leading_checks':leading,'original_log_checks':rows,
     'scope':'exact structural checks; the all-gap and moment estimates have separate written proofs'}
(base/'paired_log_valuation_structure_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','original_rows':len(rows),'leading_rows':len(leading)}))
