#!/usr/bin/env python3
"""New exhaustive finite check of the supplied repeated-block potential.

Does not evaluate an original norm, rerun a symbol audit, or infer an
infinite theorem from finite data. The potential proof is retained separately.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
triples = [(7,28,15),(3,0,6),(9,20,18)]
counts = []
for position,(W,B,A) in enumerate(triples):
    count = 0
    for w,k,c,x in product(range(2),range(2),range(2),range(29)):
        wp, kp = int(x+w > W), int(x+k > B)
        K = B-x-k+29*kp
        cp = int(A+K+c >= 29)
        cost = wp+cp
        if position == 0:
            assert cost >= 1
        elif position == 1:
            assert cost+1-kp >= 1
        else:
            assert cost-(1-k) >= 0
        count += 1
    counts.append(count)
beta, base = 410910916, 29**6
assert beta % (29**3) == 5044
assert 2001*beta == 1382*base+186913294
assert 4002*beta == 2764*base+373826588
for mu in range(-1,2002):
    assert 0 < 20387+mu < 29**3
for mu in range(-1,4003):
    assert 0 < 16385+mu < 29**3
for delta in (-1,0,1):
    assert 0 < beta+delta < base
    assert (beta+delta)//29**3 == beta//29**3
artifact = {'status':'PASS','scope':'NEW finite universal digit-potential and incoming offset audit only',
            'per_position_checks':counts,'total_potential_checks':sum(counts),
            'incoming_weight_offset_checks':2003,'incoming_upper_offset_checks':4004,
            'incoming_lower_offset_checks':3,'potential':'Phi(k)=1-k',
            'two_event_block_bound_checked':True,'full_endpoint_integrality_independently_reviewed':False,
            'original_norm_evaluated':False,'irrationality_proved':False,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target = ROOT/'repeated29_block_potential_certificate.json'
target.write_text(json.dumps(artifact,indent=2)+'\n')
receipt = dict(artifact)
receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
(ROOT/'repeated29_block_potential_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
