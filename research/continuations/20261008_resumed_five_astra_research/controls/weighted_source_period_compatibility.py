"""Parent-authored exact weighted-period checks; no matrix solve/network."""
from pathlib import Path
import hashlib,json,math

HERE=Path(__file__).resolve().parent
p=HERE/'original_source_j84645_top72_precision32.json'
saved=json.loads(p.read_text())
M=33;Q=3**M
old=int(saved['n_residue'])
new=(pow(4,84645,Q)+1)%Q
assert old%Q==new and old%3==new%3==2
weight_old=weight_new=1
weighted=known=raw_force=unweighted_changed=0
for r in range(1,3*M+1):
    assert weight_old==weight_new
    # Full original factorial quotient, without assuming a stronger digit.
    v=0;z=weight_old
    if z==0:v=M
    else:
        while z%3==0:z//=3;v+=1
    assert v>=r//3 or v==M
    assert weight_old*pow(-2,old-r,Q)%Q==weight_new*pow(-2,new-r,Q)%Q
    raw_force+=1
    for s in range(r):
        a=math.comb(old-r+s,s)%Q
        b=math.comb(new-r+s,s)%Q
        if a!=b:unweighted_changed+=1
        assert (weight_old*a-weight_new*b)%Q==0
        weighted+=1
    assert (weight_old*math.comb(old,r)-weight_new*math.comb(new,r))%Q==0
    known+=1
    weight_old=weight_old*((old-r)%Q)%Q
    weight_new=weight_new*((new-r)%Q)%Q
assert unweighted_changed>0
out={'status':'PASS','scope':'Finite weighted input primitive corroboration; not a matrix solve or dependency proof',
     'M':M,'old_input_residue_mod3_39':str(old),'new_input_residue_mod3_33':str(new),
     'weighted_Pascal_congruences_checked':weighted,'weighted_known_h_congruences_checked':known,
     'complete_raw_force_congruences_checked':raw_force,
     'unweighted_Pascal_congruences_that_change':unweighted_changed,
     'original_jet_recomputed':False,'source_receipt_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'proof_dependencies':'Full precision-local producer theorem and A4turn14 full-precision finite block theorem; DIFFERENT audits pending',
     'new_weighted_period_corollary_different_audit':'pending'}
(HERE/'weighted_source_period_compatibility.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
