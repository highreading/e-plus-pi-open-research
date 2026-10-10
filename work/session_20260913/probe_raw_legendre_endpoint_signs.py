"""Only reuse saved exact degrees 2,4,8,16 plus available 3,5; no solve or fit."""
import json
import sys
from decimal import Decimal,localcontext
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z=s.symbols('z')

rows={}
saved=json.loads((HERE/'raw_accessory_scaling_probe.json').read_text())
for case in saved['cases']:
    n=case['n'];assert n in (2,4,8,16)
    b=list(reversed([F(v) for v in case['exact_polynomial_input']['B']]))
    scale=sum(b);assert scale!=0
    rows[n]=([v/scale for v in b],'raw_accessory_scaling_probe.json')

frozen=json.loads((HERE/'raw_rational_transfer_checks.json').read_text())
case=next(t for t in frozen['steps'] if t['from_n']==2)
bp=s.Poly(s.sympify(case['next_triple'][1]),z)
rows[3]=([F(str(bp.nth(j))) for j in range(4)],'raw_rational_transfer_checks.json')
frozen=json.loads((HERE/'raw_dual_mass_independent_checks.json').read_text())
for case in frozen['checks']:
    n=case['n'];assert n in (4,5)
    b=[F(t) for t in case['B_coefficients']]
    if n==4:assert b==rows[4][0]
    else:rows[n]=(b,'raw_dual_mass_independent_checks.json')

def dec(v,digits=40):
    with localcontext() as ctx:
        ctx.prec=digits
        return str(Decimal(v.numerator)/Decimal(v.denominator))
def sg(v):return '+' if v>0 else '-' if v<0 else '0'
out={'status':'passed','scope':'Saved exact rows only; no new degree construction, no fit',
     'coefficient_convention':'P(t)=sum B_j t^(n-j)/(n-j)! = sum_l p_l P_l(2t-1)',
     'duplicate_n4_sources_agree':True,'cases':[]}
for n,(b,source) in sorted(rows.items()):
    assert sum(b)==1
    pp=[]
    for l in range(n+1):
        pp.append((2*l+1)*sum((b[j]*F(factorial(n-j),factorial(n-j-l)*factorial(n-j+l+1))
                  for j in range(n-l+1)),F(0)))
    for j in range(n+1):
        reconstruct=sum(pp[l]*(-1)**(l-j)*comb(l,j)*comb(l+j,j) for l in range(j,n+1))
        assert reconstruct==b[n-j]/factorial(j)
    weights=[(-1)**l*pp[l] for l in range(n+1)]
    centered=[sum((b[a]*F(1,2**(j-a)*factorial(j-a)) for a in range(j+1)),F(0))
              for j in range(n+1)]
    for l in range(n+1):
        pos_sum=F(0)
        poch=F(1)
        for r in range((n-l)//2+1):
            if r:poch*=F(2*l+3+2*(r-1),2)
            pos_sum+=centered[n-l-2*r]/(16**r*factorial(r)*poch)
        assert pp[l]==F(factorial(l),factorial(2*l))*pos_sum
    endpoint=sum(weights);assert endpoint==b[n]
    assert endpoint!=0
    mass=sum(map(abs,pp));kappa=abs(endpoint)/mass
    bad=[l for l,w in enumerate(weights) if w*endpoint<0]
    negative_relative_mass=sum(abs(weights[l]) for l in bad)/mass
    assert kappa==1-2*negative_relative_mass
    rec={'n':n,'source':source,'B_coefficients_ascending':list(map(str,b)),
       'p_coefficients_exact':list(map(str,pp)),
       'endpoint_weights_exact':list(map(str,weights)),
       'centered_exponential_coefficients_exact':list(map(str,centered)),
       'positive_parity_smoothing_identity':True,
       'modal_signs':''.join(map(sg,pp)),
       'endpoint_weight_signs':''.join(map(sg,weights)),
       'endpoint_sign':sg(endpoint),'endpoint_exact':str(endpoint),
       'opposite_endpoint_sign_indices':bad,
       'full_endpoint_sign_cone':not bad,
       'kappa_exact':str(kappa),'kappa_decimal':dec(kappa),
       'opposite_sign_absolute_mass_fraction':dec(negative_relative_mass),
       'normalized_endpoint_weights_decimal':[dec(w/endpoint,20) for w in weights],
       'exact_reconstruction':True}
    out['cases'].append(rec)
    print(json.dumps({k:rec[k] for k in ['n','modal_signs','endpoint_weight_signs','endpoint_sign',
        'opposite_endpoint_sign_indices','kappa_decimal','opposite_sign_absolute_mass_fraction']},indent=2))
(HERE/'raw_legendre_endpoint_sign_probe.json').write_text(json.dumps(out,indent=2)+'\n')
