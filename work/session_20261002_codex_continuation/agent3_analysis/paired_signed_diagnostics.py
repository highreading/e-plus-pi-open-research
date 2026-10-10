"""New M22 diagnostics only; exact scalar normalizations and Sturm root counts."""
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent
y=sp.Symbol('y')
D=[1]
for m in range(1,180):
    D.append(m*D[-1]+(-1)**m)
def rho(r):
    return sp.Integer(D[2*r]-(-1)**r)

rows=[]
for n in (3,5,7,9,15,23,31,39):
    mat=sp.Matrix(n,n,lambda i,j:rho(i+j))
    coeff=list(mat.inv().multiply(sp.Matrix([-rho(n+i) for i in range(n)])))+[sp.Integer(1)]
    pol=sp.Poly(sum(coeff[j]*y**j for j in range(n+1)),y)
    unit=pol.eval(-1)
    row={'n':n,'exact_positive_roots_in_zero_one':int(pol.count_roots(0,1)),
         'q_zero_over_q_minus_one':str(pol.eval(0)/unit),
         'q_one_over_q_minus_one':str(pol.eval(1)/unit),
         'scope':'Exact scalar root count, no determinant or asymptotic claim.'}
    rows.append(row)
    (OUT/'PAIRED_SIGNED_SCALAR_DIAGNOSTICS.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(n,row['exact_positive_roots_in_zero_one'],float(pol.eval(0)/unit),float(pol.eval(1)/unit),flush=True)
