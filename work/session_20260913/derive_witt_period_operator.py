"""Symbolic continuation of Item426, retaining the actual r -> r-6 step.

This produces identities over Q(r). No finite-field density is inferred.
"""
import json,time
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix

OUT=Path(__file__).resolve().parent
x,r,t=S.symbols('x r t')
u=x*(1-x); q=(1+x)*(1+x*x)
critical=S.expand(3*q*S.diff(u,x)-2*u*S.diff(q,x))
results={'critical_polynomial':str(critical),'inverse_critical_value_polynomial':str(S.factor(S.resultant(critical,t*u**6-q**4,x)))}
for nu in (0,1):
    started=time.time(); order=3; adeg=12*order-2+3*nu
    bracket=(-S.Rational(2,3)*r-nu)*u*S.diff(q,x)+(r-6*order+1)*q*S.diff(u,x)
    cols=[S.Poly(S.expand(u*q*S.diff(x**i,x)+bracket*x**i),x) for i in range(adeg+1)]
    cols += [S.Poly(-q**(4*k)*u**(6*(order-k)),x) for k in range(order+1)]
    mat=S.Matrix([[col.nth(i) for col in cols] for i in range(adeg+5)])
    dm=DomainMatrix.from_Matrix(mat).convert_to(S.QQ.frac_field(r))
    ns=dm.nullspace(divide_last=True).to_Matrix()
    print('nu',nu,'nullity',ns.rows,'seconds',time.time()-started,flush=True)
    if ns.rows==0:
        results[str(nu)]={'nullity':0}; continue
    vector=[S.cancel(v) for v in ns.row(0)]
    denom=S.lcm([S.denom(v) for v in vector])
    vector=[S.Poly(S.cancel(v*denom),r) for v in vector]
    common=S.gcd_list([v.as_expr() for v in vector])
    vector=[S.cancel(v.as_expr()/common) for v in vector]
    aa=sum(vector[i]*x**i for i in range(adeg+1)); cc=vector[adeg+1:]
    residual=S.Poly(S.expand(u*q*S.diff(aa,x)+bracket*aa-sum(cc[k]*q**(4*k)*u**(6*(order-k)) for k in range(order+1))),x,r)
    assert residual.is_zero
    top=max(S.degree(v,r) for v in cc)
    leading=[S.Poly(v,r).nth(top) for v in cc]
    result={'nullity':ns.rows,'A_coefficients':[str(v) for v in vector[:adeg+1]],'recurrence_coefficients':[str(S.factor(v)) for v in cc], 'identity_zero':True,'coefficient_degrees':[S.degree(v,r) for v in cc], 'leading_characteristic':str(S.factor(sum(leading[k]*t**k for k in range(order+1)))),'elapsed_seconds':time.time()-started}
    results[str(nu)]=result
    (OUT/'witt_period_operator_symbolic.json').write_text(json.dumps(results,indent=2,default=str)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='A_coefficients'},default=str),flush=True)
