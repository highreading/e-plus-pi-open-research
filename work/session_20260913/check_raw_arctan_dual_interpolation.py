"""Exact interpolation controls for three preselected degrees; no HP scan."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'math_packages'))
import sympy as s

x, lam = s.symbols('x lam')
Q = [s.Integer(1), x]
for k in range(1, 19):
    Q.append(s.expand(x*Q[-1]+s.Rational(k*k,4*k*k-1)*Q[-2]))
F = [sum(a*x**d/s.factorial(d) for (d,),a in s.Poly(q,x).terms())
     for q in Q]
out = {'scope': 'Exact spectral interpolation and low-coefficient controls only',
       'cases': []}
for n in (4,5,8):
    case = {'n':n,'parities':[]}
    T, S = s.Integer(0), s.Integer(0)
    for sigma in (0,1):
        high = [k for k in range(n+1,2*n) if k%2==sigma]
        nodes = [k*(k+1) for k in high]
        weights = [s.sympify(s.prod((lam-a)/(b-a) for a in nodes if a!=b)) for b in nodes]
        m = len(high)
        checked=[]
        for k in list(range(sigma,n+1,2))+[2*n+sigma,2*n+2+sigma]:
            q = Q[k].coeff(x,sigma)
            f = F[k]/q
            explicit = s.Integer(0)
            for r in range((k-sigma)//2+1):
                pr = s.prod(k*(k+1)-(2*a+sigma)*(2*a+sigma+1) for a in range(r))
                explicit += pr*x**(2*r+sigma)/s.factorial(2*r+sigma)**2
            assert s.expand(f-explicit)==0
            interp = sum(w.subs(lam,k*(k+1))*F[h]/Q[h].coeff(x,sigma)
                         for w,h in zip(weights,high))
            err = s.Poly(s.expand(f-interp),x)
            assert all(err.nth(d)==0 for d in range(2*m+sigma))
            checked.append(k)
            if k<=n:
                hk=(-1)**k*s.Rational(4**k,(2*k+1)*s.binomial(2*k,k)**2)
                ak=Q[k].subs(x,1)*q/hk
                T += ak*f
                S += ak*interp
        case['parities'].append({'sigma':sigma,'high_indices':high,
                                  'first_possible_degree':2*m+sigma,
                                  'checked_low_and_tail_indices':checked})
    E=s.Poly(s.expand(T-S),x)
    assert all(E.nth(d)==0 for d in range(n-2))
    case['normalizer_residual_coefficients']=list(map(str,reversed(E.all_coeffs())))
    out['cases'].append(case)
out['status']='passed'
(HERE/'raw_arctan_dual_interpolation_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact spectral interpolation, low/tail cancellation, and normalizer controls passed.')
