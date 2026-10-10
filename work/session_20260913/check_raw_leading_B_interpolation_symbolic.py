"""Symbolic audit of row ratios and moment blocks; no degree samples."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
n,k,d=s.symbols('n k d',integer=True,positive=True)
def m(d):
    return s.factorial(2*n+k)/s.factorial(2*n+1-d)*s.factorial(n+d-1)/(
        s.factorial(d-1)*(d+k-1)*s.factorial(k-1)*s.factorial(n-k))
assert s.combsimp(m(1)/(s.factorial(2*n+k)/s.factorial(2*n)*s.binomial(n,k)))==1
ratio2=s.combsimp(m(2)/m(1));ratio3=s.combsimp(m(3)/m(1))
assert s.cancel(ratio2-2*n*(n+1)*k/(k+1))==0
assert s.cancel(ratio3-2*n*(2*n-1)*(n+1)*(n+2)*k/(2*(k+2)))==0
h0,h1,h2,h3,q0,q1,q2,q3,u,v=s.symbols('h0 h1 h2 h3 q0 q1 q2 q3 u v',nonzero=True)
MA=s.Matrix([[0,h1,0],[-u*h0,0,h2],[q0,q1,q2]])
CA=s.factor(MA.det()/(h0*h1*q2))
assert s.cancel(CA-(u+h2/h0*q0/q2))==0
MB=s.Matrix([[0,h1,0,0],[-v*h0,0,h2,0],[0,-u*h1,0,h3],[q0,q1,q2,q3]])
CB=s.factor(MB.det()/(h0*h1*h2*q3))
assert s.cancel(CB-(-h3/h2)*(v*q2/q3+h2/h0*q0/q3))==0
assert s.expand((2*n-1)-n**3+(n-1)*(n*n+n-1))==0
out={'status':'passed','new_degree_samples':0,
     'row2_to_row1':str(ratio2),'row3_to_row1':str(ratio3),
     'three_by_three_C_ratio':str(CA),'four_by_four_C_ratio':str(CB),
     'paired_numerator_factorization':True}
(HERE/'raw_leading_B_interpolation_symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
