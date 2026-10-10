"""Parent-owned bounded corroboration, no original matrix solve or network."""
from pathlib import Path
import hashlib,json,math

HERE=Path(__file__).resolve().parent
source=HERE/'original_source_j84645_top72_precision32.json'
saved=json.loads(source.read_text())
M=33
H=6*M-1
Q=3**M
coarse=3**39
period=3**37
old=int(saved['n_residue'])
new=(pow(4,84645,period)+1)%period
assert old==(pow(4,84645,coarse)+1)%coarse
assert old%period==new and old%3==new%3==2
offsets=[0,-1,-2,-98,-197,-619]
count=0
for off in offsets:
    a=old+off
    b=new+off
    assert a>=H and b>=H
    for h in range(H+1):
        assert (math.comb(a,h)-math.comb(b,h))%Q==0
        count+=1
    assert pow(-2,a,Q)==pow(-2,b,Q)
left=right=1
for r in range(1,3*M+1):
    assert left==right
    left=left*((old-r)%Q)%Q
    right=right*((new-r)%Q)%Q
out={
 'status':'PASS','scope':'Finite input-primitive compatibility, NOT a new matrix solve or uniform-proof substitute',
 'M':M,'maximum_binomial_lower_index':H,'input_period_exponent':37,
 'original_j':84645,'old_input_residue_mod3_39':str(old),
 'reduced_input_residue_mod3_37':str(new),'row_offsets_tested':offsets,
 'exact_binomial_congruences_checked':count,'unit_power_congruences_checked':len(offsets),
 'finite_force_products_checked':3*M,'saved_source_receipt_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'complete_matrix_or_original_coefficients_recomputed':False,
 'uniform_period_proof_status':'Parent candidate; DIFFERENT audit pending; conditional on full local theorem'
}
(HERE/'degree_controlled_period_compatibility.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
