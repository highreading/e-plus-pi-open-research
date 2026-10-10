"""Exact limiting exterior-square observation check, not a density proof."""
import json,itertools
from pathlib import Path
import sympy as S
OUT=Path(__file__).resolve().parent
r,t=S.symbols('r t');d=json.loads((OUT/'witt_period_operator_symbolic.json').read_text());q=json.loads((OUT/'witt_period_contiguity_symbolic.json').read_text())
cc=[S.sympify(a) for a in d['0']['recurrence_coefficients']]
lead=[S.Poly(a,r).LC() for a in cc]
C=S.Matrix([[0,1,0],[0,0,1],[-lead[0]/lead[3],-lead[1]/lead[3],-lead[2]/lead[3]]])
pairs=list(itertools.combinations(range(3),2))
W=S.Matrix([[C.extract(i,j).det() for j in pairs] for i in pairs])
aa=[S.sympify(a) for a in q['period_coefficients']]
v=S.Matrix([[-S.limit(r*aa[1],r,S.oo),-S.limit(r*aa[2],r,S.oo),0]])
obs=S.Matrix.vstack(v,v*W,v*W**2)
assert obs.det()!=0
old=531441*t**3-301246857*t**2-266112*t-64
assert S.expand(64**3*old.subs(t,t/64)-(531441*t**3-19279798848*t**2-1089994752*t-16777216))==0
out={'C':str(C),'exterior_C':str(W),'scaled_observation':str(v),'observation_determinant':str(S.factor(obs.det())),'exterior_characteristic':str(S.factor(W.charpoly(t).as_expr())),'scaling_old_characteristic_exact':True,'interpretation':'Nonzero limiting observation proves symbolic nonidentity. Actual wedge-state nonvanishing and singularity control remain unproved.'}
(OUT/'witt_exterior_limit_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
