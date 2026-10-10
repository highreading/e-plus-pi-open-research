"""All-index algebra checked on existing exact controls only; no new solves."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z=s.symbols('z')
def v2(q):
    q=s.Rational(q)
    if q==0:return None
    a,b=abs(int(q.p)),int(q.q)
    return (a&-a).bit_length()-(b&-b).bit_length()
def polynomial(co):
    return sum(s.Rational(c)*z**(len(co)-1-i) for i,c in enumerate(co))
records=[]
for row in json.loads((HERE/'raw_accessory_scaling_probe.json').read_text())['cases']:
    n=row['n']; inp=row['exact_polynomial_input']
    A,B,C=(polynomial(inp[key]) for key in ('A','B','C'))
    P=s.Poly((1+z*z)*(s.diff(A,z)*C-A*s.diff(C,z))+C*C,z)
    pp=[P.nth(2*n-j) if 2*n-j>=0 else s.S.Zero for j in range(4)]
    K=[pp[0],pp[1],pp[2]-pp[0],pp[3]-pp[1]]
    bp=s.Poly(B,z);bb=[bp.nth(n-j) if n-j>=0 else s.S.Zero for j in range(4)]
    b0,b1,b2,b3=bb;k0,k1,k2,k3=K
    q=[b0*k0,
       b0*k1+(b1+2*b0)*k0,
       b0*k2+(b1+3*b0)*k1+(b2+2*b0)*k0,
       b0*k3+(b1+4*b0)*k2+(b2+b1+2*b0)*k1+(b3-2*b2+2*b1+4*b0)*k0]
    monic=list(map(s.Rational,row['monic_Q_exact']))
    assert all(s.cancel(qi/q[0]-mi)==0 for qi,mi in zip(q,monic))
    _,Bq,Cq,Dq=monic
    disc=s.discriminant(polynomial(monic),z)
    terms=[Bq**2*Cq**2,-4*Cq**3,-4*Bq**3*Dq,-27*Dq**2,18*Bq*Cq*Dq]
    records.append({'n':n,'coefficient_identity':'pass',
        'monic_valuations_ascending':[v2(v) for v in monic[::-1]],
        'discriminant_valuation':v2(disc),'discriminant_nonzero':disc!=0,
        'quadratic_cancellation_valuation':v2(Bq*Bq/4-Cq),
        'discriminant_combined_first_pair_valuation':v2(terms[0]+terms[1]),
        'last_three_term_valuations':[v2(v) for v in terms[2:]],
        'leading_gate_valuations':{'b1/b0':v2(b1/b0),'b2/b0':v2(b2/b0),
           'kappa1/kappa0':v2(k1/k0),'kappa2/kappa0':v2(k2/k0)}})

b0,b1,b2,k0,k1,k2=s.symbols('b0 b1 b2 k0 k1 k2')
q3=b0*k0;q2=b0*k1+(b1+2*b0)*k0
q1=b0*k2+(b1+3*b0)*k1+(b2+2*b0)*k0
rhs=b0*b0*(k1*k1-3*k0*k2)-b0*(b1+5*b0)*k0*k1+(b1*b1+4*b0*b1-2*b0*b0-3*b0*b2)*k0*k0
assert s.expand(q2*q2-3*q3*q1-rhs)==0
out={'scope':'Only the already saved n=2,4,8,16 exact triples; no new canonical degree or root computation.',
     'status':'pass','Hessian_symbolic_identity':'pass','cases':records}
(HERE/'raw_cubic_leading_coefficients_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
