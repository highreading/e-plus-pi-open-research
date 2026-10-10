"""Exact rational contiguity identity, for the Item426 actual periods."""
import json,time
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
OUT=Path(__file__).resolve().parent
x,r=S.symbols('x r');u=x*(1-x);q=(1+x)*(1+x*x)
bracket=(r-11)*q*S.diff(u,x)+(-S.Rational(2,3)*r-1)*u*S.diff(q,x)
cols=[S.Poly(S.expand(u*q*S.diff(x**i,x)+bracket*x**i),x) for i in range(26)]
cols +=[S.Poly(u**(12-6*k)*q**(4*k+1),x) for k in range(3)]
target=S.Poly(u**12,x)
mat=S.Matrix([[c.nth(i) for c in cols]+[-target.nth(i)] for i in range(30)])
started=time.time()
ns=DomainMatrix.from_Matrix(mat).convert_to(S.QQ.frac_field(r)).nullspace(divide_last=True).to_Matrix()
assert ns.rows==1 and ns[0,-1]!=0
v=[S.cancel(a/ns[0,-1]) for a in ns.row(0)]
aa=sum(v[i]*x**i for i in range(26));cc=v[26:29]
den=S.lcm([S.denom(a) for a in v]);res=S.Poly(S.expand(S.cancel(den*(u*q*S.diff(aa,x)+bracket*aa+sum(cc[k]*u**(12-6*k)*q**(4*k+1) for k in range(3))-u**12))),x,r)
assert res.is_zero
out={'identity_zero':True,'orientation':'P_1(r) = sum a_k(r) P_0(r-6k) + derivative primitive','A_coefficients':[str(S.factor(a)) for a in v[:26]],'period_coefficients':[str(S.factor(a)) for a in cc],'limit_coefficients':[str(S.limit(a,r,S.oo)) for a in cc],'denominator_factors':str(S.factor(den)),'elapsed_seconds':time.time()-started}
(OUT/'witt_period_contiguity_symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:a for k,a in out.items() if k!='A_coefficients'},indent=2),flush=True)
