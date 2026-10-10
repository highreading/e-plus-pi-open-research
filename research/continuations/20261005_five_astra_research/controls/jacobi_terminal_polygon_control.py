"""Coordinator-authored exact auxiliary terminal Jacobi coefficient control."""
import json
import resource
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent

def v3(n):
    if not n:return 999999
    n=abs(n)
    result=0
    while n%3==0:
        n//=3
        result+=1
    return result

rows=[]
for A in (243,729,1215):
    m=(A+1)//2
    for offset in (0,1,2):
        s=m+offset
        term=Fraction(1)
        total=term
        vals=[0]
        for u in range(1,s+1):
            term *= Fraction(-3*(s-u+1)*(2*s-2*u+1),
                             u*(2*A+4*s-2*u+1)*(A+71))
            total += term
            vals.append(v3(term.numerator)-v3(term.denominator))
        rel=v3(total.numerator)-v3(total.denominator)
        expected=-1 if offset==2 else 0
        assert rel==expected
        minimum=min(vals)
        indices=[i for i,v in enumerate(vals) if v==minimum]
        assert indices==([1] if offset==2 else [0])
        rows.append({'A':A,'s':s,'offset_from_m':offset,
                     'valuation_p_s_at_r':-s+rel,
                     'unique_dominant_drop':indices[0],
                     'minimum_relative_term_valuation':minimum})
report={'cases':rows,'all_nine_auxiliary_cases_pass':True,
        'exact_monic_Jacobi_coefficient_formula_used':True,
        'original_power4_domain_not_sampled':True,
        'no_uniform_dominance_or_actual_endpoint_claim':True}
(OUT/'jacobi_terminal_polygon_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
