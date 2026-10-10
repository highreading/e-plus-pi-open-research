#!/usr/bin/env python3
"""Exact local algebra supporting the all-gap paired-log separation proof."""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'math_packages'))
import sympy as s


def run():
    folder=Path(__file__).resolve().parent
    z=s.symbols('r')
    raw=json.loads((folder/'witt_period_operator_symbolic.json').read_text())['0']
    c=[s.Poly(s.sympify(v),z) for v in raw['recurrence_coefficients']]
    assert [v.degree() for v in c]==[17]*4
    a=[s.cancel(s.sympify(v)) for v in json.loads((folder/'witt_period_contiguity_symbolic.json').read_text())['period_coefficients']]
    h=[s.cancel(z*v) for v in a[1:]]
    dh=s.lcm([s.denom(v) for v in h])
    sextic=176275*z**6-6297825*z**5+89867547*z**4-649457253*z**3+2470644018*z**2-4573809342*z+3062922660
    expected=40960*(z-3)*(2*z-21)*(2*z-15)*(2*z-9)*(2*z-3)*(2*z+3)*sextic
    assert s.expand(dh-expected)==0
    hh=[s.Poly(s.cancel(v*dh),z) for v in h]
    assert all(v.degree()==12 and all(x.q==1 for x in v.all_coeffs()) for v in hh)
    limiting=s.Matrix([[0,1,0],[0,0,1],*[[ -c[k].LC()/c[3].LC() for k in range(3)]]])
    assert all(v>0 for v in limiting[2,:])
    ah=[s.limit(v,z,s.oo) for v in h]
    assert ah[0]==-s.Rational(165139233219,3610112000)
    assert ah[1]==s.Rational(291328083,231047168000)
    # The cleared polynomial matrix and its coefficient norm.
    m=s.Matrix([[0,c[3].as_expr(),0],[0,0,c[3].as_expr()],[-v.as_expr() for v in c[:3]]])
    norm=lambda v:sum(abs(t) for t in s.Poly(v,z).all_coeffs())
    bm=max(sum(norm(m[i,j]) for j in range(3)) for i in range(3))
    bh=max(1,*[norm(v.as_expr()) for v in hh])
    lead_m=m.applyfunc(lambda v:s.Poly(v,z).nth(17))
    lead_a=max(1,abs(hh[0].LC())+abs(hh[1].LC()))
    lead_b=max(2,*[sum(abs(lead_m[i,j]) for j in range(3)) for i in range(3)])
    witnesses=[]
    product=s.eye(3)
    for d in range(1,4):
        product=(m.subs(z,z-6*(d-1))*product).applyfunc(s.expand)
        jj=s.Poly(s.expand(hh[0].as_expr()*product[0,2]-hh[1].as_expr()*product[0,1]),z)
        assert jj.degree()==17*d+12
        detlimit=ah[0]*(limiting**d)[0,2]-ah[1]*(limiting**d)[0,1]
        assert detlimit<0
        # Leading coefficients obey the exact all-gap formula.
        assert jj.LC()==s.Poly(dh,z).LC()*c[3].LC()**d*detlimit
        witnesses.append(dict(gap=d,degree=jj.degree(),limiting_observation_determinant=str(detlimit),leading_coefficient=str(jj.LC())))
    return dict(status='EXACT_PAIRED_OBSERVATION_ALGEBRA_PASS',
                recurrence_degrees=[17]*4,observation_common_denominator=str(s.factor(dh)),
                observation_integer_numerator_degrees=[12,12],
                B_M=str(bm),B_H=str(bh),limiting_companion=[[str(v) for v in row] for row in limiting.tolist()],
                short_gap_leading_height_A=str(lead_a),short_gap_leading_height_B=str(lead_b),
                limiting_scaled_contiguity=[str(v) for v in ah],
                finite_symbolic_witnesses=witnesses,
                scope='The note proves every-gap nonvanishing from eventual positivity and gives the uniform norm/packing argument; these finite symbolic witnesses do not substitute for that proof.')


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_name('paired_log_separation_checks.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','recurrence_degrees','observation_integer_numerator_degrees']}))
