from pathlib import Path
from math import factorial, prod
import hashlib, json, datetime
import sympy as sp

HERE=Path(__file__).resolve().parent
R=HERE.parent
rows=[]
for k in range(1,11):
    D=sp.Matrix([[factorial(2*k+2*i+2*j) for j in range(k)] for i in range(k)])
    exact=int(D.det(method='bareiss'))
    bound=2**(k*(k-1))*prod(factorial(j)*factorial(3*k-1+j) for j in range(k))
    L=sp.Matrix([[factorial(3*k-1+i+j) for j in range(k)] for i in range(k)])
    laguerre_det=int(L.det(method='bareiss'))
    expected=prod(factorial(j)*factorial(3*k-1+j) for j in range(k))
    assert laguerre_det==expected
    assert exact>=bound>0
    ratio=sp.Rational(exact,bound)
    rows.append({'k':k,'maximum_reference_factorial':6*k-4,
                 'exact_reference_determinant':str(exact),
                 'amgm_size_lower_bound':str(bound),
                 'actual_to_lower_bound_numerator':str(ratio.p),
                 'actual_to_lower_bound_denominator':str(ratio.q),
                 'ordinary_laguerre_determinant_product_pass':True})

k0=512
assert sp.Rational(225,k0)<sp.Rational(1,2)
assert sp.Rational(450,k0*k0)<sp.Rational(1,2)
assert 8*k0<75*2**k0
assert 256*k0<75*2**k0
assert 2**32*4**12>11**12*3**9

t=sp.Symbol('t',positive=True)
F=t*t*sp.log(t)/2-sp.Rational(3,4)*t*t
reference_constant=sp.simplify(sp.log(2)-sp.Rational(3,4)+F.subs(t,4)-F.subs(t,3))
expected_constant=17*sp.log(2)-sp.Rational(9,2)*sp.log(3)-6
assert sp.simplify(reference_constant-expected_constant)==0
C_H=15*sp.log(2)-sp.Rational(9,2)*sp.log(3)
margin=16*sp.log(2)-sp.Rational(9,2)*sp.log(3)-6
Acrit=(19*sp.log(2)-sp.Rational(9,2)*sp.log(3)-6)/sp.log(2)

sources={}
for p in [HERE/'COORDINATOR_COMPACT_REFERENCE_GRAM_LOWER_BOUND_CANDIDATE.md',
          R/'gates/COMPACT_REFERENCE_GRAM_CONSTANT_GATE_20261009.md']:
    sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'time':datetime.datetime.now().astimezone().isoformat(),'status':'PASS',
     'scope':'NEW small reference-Gram checks, NOT original compact indices or a content estimate.',
     'source_sha256':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'reference_matrices':rows,'cutoff_512_exact_rational_checks_pass':True,
     'positive_margin_integer_certificate':{
         'left_2pow32_4pow12':str(2**32*4**12),
         'right_11pow12_3pow9':str(11**12*3**9),
         'uses_elementary_e_bound':'e<11/4 from the factorial series'},
     'symbolic_reference_constant':str(expected_constant),
     'candidate_C_H':str(C_H),'C_H_decimal_display_only':str(C_H.evalf(30)),
     'conditional_A3_retirement_margin':str(margin),
     'margin_decimal_display_only':str(margin.evalf(30)),
     'conditional_binary_upper_threshold':str(Acrit),
     'threshold_decimal_display_only':str(Acrit.evalf(30)),
     'independent_full_source_comparison_audit_still_required':True,
     'global_proof':False}
(HERE/'compact_reference_gram_constant_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','new_reference_matrices':len(rows),
       'candidate_C_H':str(C_H.evalf(18)),'conditional_A3_margin':str(margin.evalf(18)),
       'conditional_binary_upper_threshold':str(Acrit.evalf(18)),'global_proof':False}))
