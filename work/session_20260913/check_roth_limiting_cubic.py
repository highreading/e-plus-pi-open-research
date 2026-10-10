"""Exact finite arithmetic inputs to the all-spacing nondegeneracy proof."""
import json
from math import isqrt
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
entries=json.loads((ROOT/'results/item237_j1_algebraic_residual_certificate.json').read_text())['all_h_recurrence']['factored_coefficients']
leading=[]
for entry in entries:
    v=F(entry['scalar'])
    for _,b in entry['linear_factor_roots_numerator_denominator']:
        v*=b
    v*=entry['remaining_core_low_to_high'][-1]
    leading.append(v)
assert leading==[F(-64,531441),F(-9856,19683),F(-413233,729),F(1)]
a,b,c,d=531441,-301246857,-266112,-64
assert [F(d,a),F(c,a),F(b,a),F(1)]==leading
disc=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
assert disc==-572058527163885303300000000
mod7=[(a*x**3+b*x*x+c*x+d)%7 for x in range(7)]
assert a%7 and all(mod7)
squares={}
for k in [1,3]:
    value=F(-disc,k)
    n,q=value.numerator,value.denominator
    rn,rq=isqrt(n),isqrt(q)
    is_square=rn*rn==n and rq*rq==q
    assert not is_square
    squares[str(-k)]={
        'tested_rational':str(value),
        'numerator_floor_sqrt':str(rn),
        'denominator_floor_sqrt':str(rq),
        'is_square':is_square,
    }
result={'status':'exact_finite_inputs_pass',
        'scope':'not a numerical check of all spacings; all-d conclusion uses splitting-field proof',
        'leading_coefficients':[str(v) for v in leading],
        'primitive_cubic_high_to_low':[a,b,c,d],
        'discriminant':str(disc),'mod7_values':mod7,
        'quadratic_square_class_checks':squares}
(HERE/'roth_limiting_cubic_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
