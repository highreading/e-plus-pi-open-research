"""Coordinator symbolic audit of differential row factor and actual norm."""
import json
import resource
from pathlib import Path
import sympy as s
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
x,k,sp,K,beta=s.symbols('x k s K beta')
f=s.Function('f')(x)
def B(a):return x*s.diff(a,x,2)+(1-k-2*x)*s.diff(a,x)+(k-1+2*x)*a
def T(a):return x*x*s.diff(a,x,2)/2+x*(1-x)*s.diff(a,x)+(x*x-x-k*(k+1)/2)*a
def C(a):return x*(x-k-1)*s.diff(a,x,2)+(k*k-1+2*(k+2)*x-2*x*x)*s.diff(a,x)-((k+1)*(2*k-1)+2*(k+2)*x-2*x*x)*a
f3=-(((2-2*k)*x-2*x*x)*s.diff(f,x,2)+(k*(k-1)+(4*k-2)*x+2*x*x)*s.diff(f,x)-(2*k*k+4*k*x)*f)/(x*x)
f4=s.diff(f3,x).subs(s.diff(f,x,3),f3)
expression=(k+1)*(B(B(f))-B(f))+2*T(f)-(k+1)**3*f-(2*k+3)*C(f)
reduced=s.factor(expression.subs(s.diff(f,x,4),f4).subs(s.diff(f,x,3),f3))
assert reduced==0
matching_row_identity=s.factor(C(f)-((x-1)*B(f)-x*s.diff(B(f),x)+(k+1)*x*f))
matching_reduced=s.factor(matching_row_identity.subs(s.diff(f,x,3),f3))
assert matching_reduced==0
v=s.Matrix([-(sp+1),sp,1]);w=s.Matrix([1-beta,beta,0])
scale=s.diag(1,-(sp-1),sp*(sp-1))
a=s.Matrix([sp-1,sp,sp+1]);b=s.Matrix([sp,sp+1,sp+2])
metric=s.eye(3)+4*a*a.T+4*b*b.T
norm=s.expand((scale*v).dot(metric*(scale*v)))
cross=s.expand((scale*v).dot(metric*(scale*w)))
expected=2*sp**4-4*sp**3+23*sp**2-6*sp+5
assert norm==expected
j=s.expand(K**4*norm.subs(sp,-2-1/K))
assert j==173*K**4+210*K**3+95*K**2+20*K+2
record={'b4_operator_remainder':str(reduced),'b4_equivalent_operator_remainder':str(matching_reduced),
        'matching_norm':str(norm),'matching_cross_term':str(cross),'progression_polynomial':str(j),
        'status':'exact formal symbolic identities; endpoint interpretation reviewed separately'}
(OUT/'contiguous_operator_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
