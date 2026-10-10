"""Remove the apparent sextic of the new nu=0 period operator exactly."""
import json,time
from pathlib import Path
import sympy as S
OUT=Path(__file__).resolve().parent;r=S.symbols('r');started=time.time()
data=json.loads((OUT/'witt_period_operator_symbolic.json').read_text())
P=[S.sympify(v) for v in data['0']['recurrence_coefficients']]
shift=lambda a:S.expand(a.subs(r,r-6))
Q=next(a for a,e in S.factor_list(P[3],r)[1] if S.degree(a,r)==6)
Qp=shift(Q);Qpp=shift(Qp)
L0=S.cancel(P[0]/Qp);assert S.denom(L0)==1
assert S.gcd(Q,Qp)==1
B=S.rem(-P[1]*S.invert(L0*Qpp,Qp,r),Qp,r)
checks=[S.rem(P[k]*shift(L0)+B*shift(P[k-1])*L0,Qp,r)==0 for k in (2,3)]
out={'shift':-6,'Q':str(Q),'Q_shift_factor_exact':True,'removable_conditions':checks}
print('removability',checks,'seconds',time.time()-started,flush=True)
if all(checks):
    a=[S.cancel(v/P[0]) for v in P];bb=Qpp*B/Qp
    rr=[S.Integer(1)]+[S.cancel(a[j]+bb*a[j-1].subs(r,r-6)) for j in range(1,4)]+[S.cancel(bb*a[3].subs(r,r-6))]
    out['order4']=[str(S.factor(v)) for v in rr]
    out['denominator_factors']=[str(S.factor(S.denom(v))) for v in rr]
    out['variable_denominator_roots']=[[str(rt) for fac,power in S.factor_list(S.denom(v),r)[1] for rt in (S.solve(fac,r) if S.degree(fac,r)==1 else ['NONLINEAR:'+str(fac)])] for v in rr]
    # Check coefficient identity against the defining normalized recurrence.
    out['identity_checked']=all(S.cancel(rr[j]-(a[j] if j<4 else 0)-(bb*a[j-1].subs(r,r-6) if j>0 else 0))==0 for j in range(5))
out['elapsed_seconds']=time.time()-started
(OUT/'witt_period_desingularization.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='order4'},indent=2),flush=True)
