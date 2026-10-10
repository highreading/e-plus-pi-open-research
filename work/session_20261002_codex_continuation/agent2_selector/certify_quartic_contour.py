import sys, json
sys.path.insert(0, '[private local path removed]')
import sympy as s
from pathlib import Path

out=Path(__file__).resolve().parent
t=s.symbols('t')
A=(t*t+6*t+1)/4
B=(1-t)**2*(t*t+6*t+25)/16
p=s.Poly(s.Rational(5,8)-A*B,t)

def bernstein(a,b):
    v=s.symbols('v')
    q=s.Poly(p.as_expr().subs(t,a+(b-a)*v),v)
    d=p.degree()
    return [s.factor(sum(q.nth(j)*s.binomial(k,j)/s.binomial(d,j) for j in range(k+1))) for k in range(d+1)]

todo=[(s.Rational(0),s.Rational(1))]
parts=[]
while todo:
    a,b=todo.pop(0)
    coeff=bernstein(a,b)
    if min(coeff)>0:
        parts.append({'interval':[str(a),str(b)],'bernstein_coefficients':[str(x) for x in coeff]})
    else:
        assert b-a>s.Rational(1,2**12)
        c=(a+b)/2
        todo.extend([(a,c),(c,b)])

payload={'quantity':'5/8 - |z D|^2 on vertical contour with t=4 Im(w)^2',
 'polynomial':str(p.as_expr()),'parts':parts,
 'claim':'Every Bernstein coefficient is strictly positive; hence |z D|^2<5/8 on the whole contour.'}
(out/'quartic_contour_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
