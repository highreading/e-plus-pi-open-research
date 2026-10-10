"""Finite exact reference-jet checks; no full-stack or arithmetic audit."""
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
x=sp.Symbol('x')
weights=[]
slopes=[]
adjacent=[]
variance=[]
for j in range(31):
    p=sp.jacobi(j,sp.Rational(-1,2),0,x)
    val=p.subs(x,3)
    slope=-2*sp.diff(p,x).subs(x,3)/val
    weight=(2*j+sp.Rational(1,2))*val**2
    weights.append(weight)
    slopes.append(slope)
    if j:
        ratio=sp.cancel(weights[j-1]/weight)
        gap=sp.cancel(slopes[j-1]-slope)
        assert sp.Rational(1,245)<=ratio<=sp.Rational(4,9)
        assert sp.Rational(1,2)<=gap<=1
        adjacent.append({'degree':j,'weight_ratio':str(ratio),'slope_gap':str(gap)})
    if j>=1:
        k00=sum(weights)
        k01=sum(w*d for w,d in zip(weights,slopes))
        k11=sum(w*d*d for w,d in zip(weights,slopes))
        var=sp.cancel((k00*k11-k01*k01)/(k00*k00))
        assert sp.Rational(25,79380)<=var<=sp.Rational(468,125)
        variance.append({'k':j+1,'jet_variance_decimal':str(sp.N(var,18)),
                         'proved_lower_bound':str(sp.Rational(25,79380)),
                         'proved_upper_bound':str(sp.Rational(468,125))})

receipt={'scope':'Finite exact classical reference identities only. The all-k coercivity and complete determinant theorem are proved in prose. No Root full-stack receipt, actual primitive content, or small-k theorem is rechecked.',
         'status':'PASS','adjacent_checks':adjacent,'variance_checks':variance}
(HERE/'DOUBLE_POLE_REFERENCE_JET_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'PASS','adjacent_cases':len(adjacent),'variance_cases':len(variance)}))
