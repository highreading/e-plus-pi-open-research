"""Parent-authored54 NEW universal cancellation constants; not macro rerun."""
from pathlib import Path
from math import comb
import datetime
import hashlib
import json

HERE=Path(__file__).resolve().parent
R=HERE.parent


def v3(n):
    assert n
    depth=0
    while n%3==0:
        depth+=1;n//=3
    return depth


def factorial_v3(n):
    depth=0
    while n:
        n//=3;depth+=n
    return depth


def factorial_unit_mod3(n):
    value=1
    for a in range(1,n+1):
        while a%3==0:a//=3
        value=value*a%3
    return value


rows=[]
for u in range(27):
    for r in (1,2):
        v=3*u+r
        low,high=comb(810,v),comb(810,243+v)
        lv,hv=v3(low),v3(high)
        lfv=factorial_v3(810)-factorial_v3(v)-factorial_v3(810-v)
        hfv=factorial_v3(810)-factorial_v3(243+v)-factorial_v3(567-v)
        lu,hu=(low//81)%3,(high//243)%3
        ful=(factorial_unit_mod3(810)*pow(factorial_unit_mod3(v),-1,3)
             *pow(factorial_unit_mod3(810-v),-1,3))%3
        fuh=(factorial_unit_mod3(810)*pow(factorial_unit_mod3(243+v),-1,3)
             *pow(factorial_unit_mod3(567-v),-1,3))%3
        expected=pow(v,-1,3)*((-1)**(v-1))%3
        assert lv==lfv==4 and hv==hfv==5
        assert lu==hu==ful==fuh==expected
        assert (high-3*low)%729==0
        rows.append({'u':u,'r':r,'v':v,'low_v3':lv,'high_v3':hv,
                     'low_stripped_unit_mod3':lu,'high_stripped_unit_mod3':hu,
                     'independent_factorial_low_unit':ful,
                     'independent_factorial_high_unit':fuh,
                     'high_minus_3_low_mod729':(high-3*low)%729})
assert len(rows)==54
sources=[R/'responses/A4_turn13.md',R/'gates/NEW_FULL_K27_AND_NON_P_54_CHECK_GATE_20261009.md',
         HERE/'COORDINATOR_CLASSICAL_270P_SCALE_REUSE.md']
output={'status':'PASS','time':datetime.datetime.now().astimezone().isoformat(),
        'scope':'ONLY54 NEW binomial810 constants in the non-P cancellation. Complete source81 still needs full-proof different audit.',
        'case_count':54,'maximum_binomial_top':810,'modulus':729,'rows':rows,
        'independent_valuation_and_stripped_factorial_unit_checks':True,
        'old_122_macro_constants_recomputed':False,
        'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'actual_Delta_A_evaluated':False,'original_index_experiment':False,'global_proof':False}
(HERE/'prefix_non_p_54_binomial_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'PASS','case_count':54,'valuation_pair':[4,5],
                  'all_cancellations_zero_mod729':True,'global_proof':False}))
