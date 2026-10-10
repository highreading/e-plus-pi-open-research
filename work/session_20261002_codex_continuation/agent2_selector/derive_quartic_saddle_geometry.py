import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
out=Path(__file__).resolve().parent
w=s.symbols('w'); v=s.symbols('v',real=True); x=s.symbols('x',real=True)
G=1-2*w*w+4*w**4-8*w**6
Y=s.symbols('Y',real=True)
abs2=s.expand(G.subs(w,x+s.I*Y)*G.subs(w,x-s.I*Y))
abs2=s.Poly(abs2,Y)
pv=sum(abs2.nth(2*j)*v**j for j in range(7))
x2=(s.sqrt(3)+1)/12
pv=s.expand(pv).subs(x**12,x2**6).subs(x**10,x2**5).subs(x**8,x2**4).subs(x**6,x2**3).subs(x**4,x2**2).subs(x**2,x2)
pv=s.expand(pv)
v0=(s.sqrt(3)-1)/12
der=s.factor(s.diff(pv,v),extension=s.sqrt(3))
quo=s.cancel(s.diff(pv,v)/(v-v0),extension=s.sqrt(3))
payload={'vertical_modulus_polynomial':str(pv),'derivative_factorization':str(der),'quotient':str(s.expand(quo)),
 'saddle_squared_real_part':str(x2),'saddle_squared_imaginary_part':str(v0),'saddle_modulus_squared':str(s.simplify(pv.subs(v,v0))),
 'quotient_roots_numerical_only': [str(q) for q in s.nroots(quo)]}
(out/'quartic_saddle_geometry.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
