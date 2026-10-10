"""Exact normalization controls for existing n=4,5 seeds, not a degree scan."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
x,lam=s.symbols('x lam')
def g(k,par=None):
    sig=k%2 if par is None else par
    lv=s.Integer(k*(k+1)) if par is None else k
    coeff=s.Integer(1); ans=x**sig
    for j in range(1,5):
        d=sig+2*j-2
        coeff*= (lv-d*(d+1))/((d+1)**2*(d+2)**2)
        ans+=coeff*x**(sig+2*j)
    return s.expand(ans)
out=[]
for seeds in ((5,), (6,), (5,7), (6,8)):
    r=len(seeds);sig=seeds[0]%2;opp=1-sig
    fs=[g(k) for k in seeds]
    P=lambda z:s.prod(z-sig-2*j for j in range(r))
    S=sum(k*(k+1) for k in seeds)-sum((sig+2*j)*(sig+2*j+1) for j in range(r))
    b=-s.Rational(2*r*S,((sig+2*r)*(sig+2*r-1))**2)
    H=s.cancel(x**(r-opp)*s.wronskian(fs+[g(lam,opp)],x)/s.wronskian(fs,x)/P(opp))
    jet=s.series(H,x,0,5).removeO().expand()
    expected=((lam-2)/12+b)/(3-2*r) if sig==0 else (lam/4+b)/(1-2*r)
    assert s.simplify(jet.coeff(x,2)-expected)==0
    assert jet.coeff(x,0)==1
    for j in (1,2):
        leading=s.Poly(jet.coeff(x,2*j),lam).LC()
        assert leading==s.Rational(P(opp+2*j),P(opp))/s.factorial(opp+2*j)**2
    out.append({'seeds':seeds,'b_r':str(b),'normalized_x2_coefficient':str(s.factor(expected)),'all_claims_pass':True})
Path(__file__).with_name('raw_parity_elimination_jet_checks.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
