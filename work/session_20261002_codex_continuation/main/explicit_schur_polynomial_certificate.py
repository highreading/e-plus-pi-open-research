"""Exact certificate for the new degree61 endpoint-fixed Hurwitz polynomial.
Reuses only the archive's definition-level Gaussian Schur primitives."""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import importlib.util,json,hashlib,sys
sys.set_int_max_str_digits(0)
ROOT=Path('[private local path removed]')
SESSION=ROOT/'work/session_20261002_codex_continuation'
helper=ROOT/'scripts/nonpolynomial_integral_hurwitz_pullback_certificate.py'
spec=importlib.util.spec_from_file_location('exact_gaussian_schur_definitions',helper)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
candidates=json.loads((SESSION/'main/SCHUR_INTERPOLATED_POLYNOMIAL_CANDIDATES.json').read_text())
candidate=next(v for v in candidates['basis_candidates'] if v['last_basis_index']==60)
K=candidate['basis'];radius=Q(99,50)
real=[Q(0),Q(1)]+[Q(0)]*60;imag=[Q(0)]*len(real)
for k,v in enumerate(K,1):real[k]+=Q(v,factorial(k));real[k+1]-=Q(v,factorial(k))
assert sum(real)==1 and real[0]==0
jets=[int(v*factorial(k)) for k,v in enumerate(real)]
assert all(v*factorial(k)==jets[k] for k,v in enumerate(real))
real[0]-=1;imag[0]=-1
initial,den=base.initial_reversed_gaussian_integer_polynomial(real,imag,radius)
records,reflection,constant=base.fraction_free_schur_certificate(initial,128)
assert len(records)==61 and all(v['gap_positive'] for v in records)
record={'status':'PASS_EXACT_NEW_DEGREE61_INTEGRAL_HURWITZ_PULLBACK','strict_composition_radius_lower':{'numerator':radius.numerator,'denominator':radius.denominator},'polynomial':'z+sum_(k=1)^60 K_k z^k(1-z)/k!','endpoint_basis_integers':K,'polynomial_degree':61,'phi_zero':0,'phi_one':1,'all_polynomial_derivative_jets_integral':True,'derivative_jets_0_through_61':jets,'initial_reciprocal_state_sha256':base.gaussian_state_sha256(initial),'cleared_denominator':den,'schur_gap_count':61,'all_gaps_strictly_positive':True,'schur_records':records,'final_constant':list(constant),'dependency_path':str(helper),'dependency_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'scope':'Exact zero-free closed disk; all-order composition integrality follows from integer derivative recurrence and Bell polynomials. Numerical candidate generation is not part of this proof.'}
(SESSION/'main/EXPLICIT_DEGREE61_RADIUS198_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],'radius>99/50','gaps',len(records),'max norm bits',max(v['leading_norm_bit_length'] for v in records))
