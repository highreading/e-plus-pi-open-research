"""Coordinator-authored exact algebra; analytic moment inputs are proposals."""
import sympy as s,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
out=Path(__file__).resolve().parent
sig=s.sqrt(2);M=1+sig;rho=1/M;ap=sig/M
def simp(v):return s.simplify(s.expand(v))
def terms(q,alpha,sign):
    A=1+q
    c2=(q-1)/(2*A**3)
    c4=(1-q)*(q*q-10*q+1)/(24*A**5)
    a1=sign/A;a2=sign*c2/ap
    a3=sign*(c2*(s.Rational(1,6)-ap)+2*c4)/ap**2
    b1=-1/A**2;b2=(2-q)/(ap*A**4);g1=sign*2/A**3
    f3=-3*alpha;f4=12*alpha-3*alpha**2
    x1=-a1/alpha
    x2=-(a2+b1*x1+f3*x1**2/2)/alpha
    pieces=[-alpha*x2**2/2,f4*x1**4/24,a3*x1,b2*x1**2/2,g1*x1**3/6]
    return {'x1':str(simp(x1)),'x2':str(simp(x2)),
        'pieces':list(map(lambda v:str(simp(v)),pieces)),
        'coefficient':str(simp(sum(pieces)))}
plus=terms(M,sig/M,1);minus=terms(rho,sig*M,-1)
difference=simp(s.sympify(minus['coefficient'])-s.sympify(plus['coefficient']))
report={'plus':plus,'minus':minus,'minus_minus_plus_quartic':str(difference),
    'exact_algebra_only':True,'moment_coefficients_require_independent_proof':True}
(out/'quartic_saddle_algebra_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
