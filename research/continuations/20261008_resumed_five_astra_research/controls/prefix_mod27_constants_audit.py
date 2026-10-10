from pathlib import Path
from math import factorial,prod
from fractions import Fraction
from collections import Counter
import hashlib,json,datetime

HERE=Path(__file__).resolve().parent
R=HERE.parent
def valuation(n,p):
    assert n
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v

common=81*2**270*factorial(270)
rows=[]
failures=[]
profile=Counter()
for j in range(1,123):
    high=prod(243+2*j+2*a for a in range(271))
    low=prod(81+2*j+2*a for a in range(271))
    complete=Fraction(common,high)+Fraction(3*common,low)
    vn=valuation(complete.numerator,3)
    vd=valuation(complete.denominator,3)
    v=vn-vd
    residue=None
    if vd==0:
        residue=(complete.numerator%27)*pow(complete.denominator%27,-1,27)%27
    if v<0 or vd!=0:
        failures.append({'j':j,'issue':'combined constant not ternary integral','v3':v})
    if j%9 and v<1:
        failures.append({'j':j,'issue':'outside9-grid constant not divisible by3','v3':v})
    if j%3 and v<2:
        failures.append({'j':j,'issue':'outside3-grid constant not divisible by9','v3':v})
    vh=valuation(high,3)
    vl=valuation(low,3)
    if j in(121,122) and (vh,vl,residue)!=(135,135,0):
        failures.append({'j':j,'issue':'new edge product/residue mismatch',
                         'values':[vh,vl,residue]})
    rows.append({'j':j,'largest_high_factor':243+2*j+540,
                 'largest_low_factor':81+2*j+540,'v3_high_product':vh,
                 'v3_low_product':vl,'v3_combined_constant':v,'D_j_mod27':residue,
                 'high_summand_v3':138-vh,'low_summand_v3':139-vl,
                 'combined_reduced_denominator_3_unit':vd==0})
    profile[v]+=1
sources={}
for p in [R/'responses/A1_turn9.md',HERE/'PREFIX_MOD27_CONSTANTS_RECEIPT_GATE.md']:
    sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'status':'FAIL' if failures else 'PASS',
     'time':datetime.datetime.now().astimezone().isoformat(),
     'scope':'NEW universal122 prefix constants, not an original dense matrix or global proof.',
     'source_sha256':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'reused_v3_270_factorial':134,'rows':rows,'valuation_profile':dict(profile),
     'failures':failures,'full_prefix_proof_external_audit_still_required':True,
     'global_proof':False}
(HERE/'prefix_mod27_constants_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'new_constants':len(rows),
    'valuation_profile':dict(profile),'edges':rows[-2:],
    'failures':failures,'global_proof':False}))
if failures:
    raise SystemExit(1)
