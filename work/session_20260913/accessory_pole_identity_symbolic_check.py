"""Exact universal checks; no scan of HP degrees or primes."""
from pathlib import Path
import json
import sympy as S

z,m,d,beta,gamma=S.symbols("z m d beta gamma")
a,a1,a2,b,b1,b2,c,c1,c2=S.symbols("a a1 a2 b b1 b2 c c1 c2")
D=1+z*z
s=3*d+2
J=c*(b+b1)-c1*b
matrix=S.Matrix([
    [a,b,c],
    [a1+c/D,b+b1,c1],
    [a2+2*c1/D-c*(2*z)/D**2,b+2*b1+b2,c2],
])
N=S.cancel(D**2*matrix.det())
pole_remainder=S.rem(S.Poly(S.expand(N-2*z*c*J),z),S.Poly(D,z)).as_expr()

# Four coefficients of L z^m, compared with the enveloping expression.
left=[
    -m*(m-1)+(2*d-2)*m-d*(d-1),
    m*(m-1)*(m-2)+(4-s)*m*(m-1)+beta*m+2*d*d*(d-1)-d*beta,
    -m*(m-1)+gamma*m,
    m*(m-1)*(m-2)-s*m*(m-1),
]
right=[
    -(m-d)*(m-d+1),
    (m-d)*(m*m-(2*d+1)*m-2*d*(d-1)+beta),
    m*(gamma+1-m),
    m*(m-1)*(m-3*d-4),
]
sl2_differences=[S.factor(l-r) for l,r in zip(left,right)]
assert pole_remainder==0
assert all(v==0 for v in sl2_differences)
out={
    "scope":"universal symbolic identities, not finite HP or prime samples",
    "cleared_Wronskian_pole_remainder":str(pole_remainder),
    "sl2_monomial_coefficient_differences":[str(v) for v in sl2_differences],
    "norm_convention":"Res(1+z^2,F)=det(multiplication by F in R[z]/(1+z^2))",
    "status":"pass",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
