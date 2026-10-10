"""Reuse the saved original jet; no producer or fixed receipt is recomputed."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
source=HERE/'original_source_j84645_top72_precision32.json'
data=source.read_bytes(); original=json.loads(data)
assert original['status']=='PASS' and original['actual_original_j']==84645
assert original['target_precision']==32 and original['L']==72
Q=3**32
q=original['q_top'];v=original['V_coefficients']
assert len(q)==72 and len(v)==71
assert all(type(x) is int and 0<=x<Q for x in q+v)
reconstructed=[0]*72
for i,a in enumerate(v):
    reconstructed[i]=(reconstructed[i]+2*a)%Q
    reconstructed[i+1]=(reconstructed[i+1]+a)%Q
assert reconstructed==q
omitted=next(i for i,a in enumerate(q) if a)
assert omitted==16 and v[:omitted]==[0]*omitted
short_q=q[omitted:];short_v=v[omitted:]
assert len(short_q)==56 and len(short_v)==55
assert all(a%3**7==0 for a in short_q+short_v)
layers=[]
for precision in (8,9,10,11,12,13,14,18,22,26,30,32):
    modulus=3**precision
    nz=[i for i,a in enumerate(short_v) if a%modulus]
    layers.append({'coefficient_precision':precision,
                   'lowest_nonzero_degree_in_V54':min(nz) if nz else None,
                   'nonzero_coefficients':len(nz)})
out={'status':'PASS','scope':'Algebraic extraction from the saved ONE original candidate-derived coefficient receipt; no source contraction evaluated.',
     'source_path':str(source),'source_sha256':hashlib.sha256(data).hexdigest(),
     'original_j':84645,'frozen_infinite_branch':'j=84645+3^38*t, t>=0',
     'different_external_locality_proof_audit_pending':True,
     'coefficient_modulus_exponent':32,'omitted_leading_zero_coefficients':omitted,
     'short_q_length':len(short_q),'V54_degree_bound':54,
     'short_producer':'(y+1)*x^(A-54)*V54(x), x=y-1',
     'full_projection_reused_inverse_allowance':-1,
     'full_Schur_difference_lower_depth':30,
     'normalized_prefix_difference_lower_depth':4,
     'q_top56':short_q,'V54_coefficients':short_v,'saved_jet_layer_support':layers,
     'new_original_solver_executed':False,'complete_W_return_deleted':False}
destination=HERE/'frozen_original_short56_coefficient_certificate.json'
assert not destination.exists()
destination.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','omitted_leading_zero_coefficients','short_q_length','V54_degree_bound','new_original_solver_executed')}))
