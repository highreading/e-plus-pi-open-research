"""Compare cached original data; no source solver or moment is rerun."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
R=HERE.parent
source=HERE/'original_source_j84645_top72_precision32.json'
report=R/'responses/A4_turn14.md'
destination=HERE/'cached_original_scalar_refinement_compatibility.json'
assert not destination.exists()
data=source.read_bytes()
saved=json.loads(data)
assert saved['status']=='PASS' and saved['actual_original_j']==84645
assert saved['M']==33 and saved['target_precision']==32
checks=[]
for field,exponent,expected in (
    ('Xi_mod_input',5,120),
    ('chi_mod_input',6,(-168)%(3**6)),
    ('xi_mod_target',4,31),
):
    value=saved[field]%(3**exponent)
    assert value==expected,(field,value,expected)
    checks.append({'field':field,'modulus_exponent':exponent,
                   'cached_residue':value,'report_residue':expected,'status':'PASS'})
assert saved['q_top'][:16]==[0]*16
assert saved['q_top'][16]==3**30
out={'status':'PASS','source_path':str(source),
     'source_sha256':hashlib.sha256(data).hexdigest(),
     'report_path':str(report),'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),
     'scope':'Compatibility of SAVED one original jet with new symbolic higher scalar claims; not a uniform proof audit.',
     'different_full_precision_block_audit_pending':True,'checks':checks,
     'first_retained_coefficient_q_N_minus_55':3**30,
     'short56_tail_width_is_sharp_for_saved_index_in_this_monomial_truncation':True,
     'new_original_matrix_solver_or_fixed_receipt_executed':False,
     'full_W_return_evaluated':False}
destination.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'scalar_compatibility_checks':len(checks),
                  'first_retained_tail_depth':30,'new_solver_executed':False}))
