#!/usr/bin/env python3
"""NEW target high-block valuation counter and exact bounded sum comparisons."""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
C=Path(__file__).resolve().parent
start=time.monotonic()
def v2(x):
    assert x
    return (abs(x)&-abs(x)).bit_length()-1
def count(m):
    A,S=4002*m,8005*m
    baseline=m.bit_count()+(8004*m).bit_count()-S.bit_count()
    # Each state retains its least REACHABLE exponent even if its count is0mod8.
    states={(0,0,0):(0,[1,0])}
    for i in range(S.bit_length()):
        bits=((A>>i)&1,(m>>i)&1,(S>>i)&1)
        candidates={}
        for state,(minimum,coeffs) in states.items():
            for digit in (0,1):
                new=tuple(int(digit+state[j]>bits[j]) for j in range(3))
                shift=new[0]+new[1]-new[2]
                for offset,coefficient in enumerate(coeffs):
                    degree=minimum+offset+shift
                    candidates.setdefault(new,[]).append((degree,coefficient))
        states={}
        for state,terms in candidates.items():
            minimum=min(degree for degree,coefficient in terms)
            coeffs=[sum(coefficient for degree,coefficient in terms if degree==minimum+j)%8 for j in range(2)]
            states[state]=(minimum,coeffs)
    minimum,coeffs=states[(0,0,0)]
    c=baseline+minimum
    return {'c':c,'N_c_mod8':coeffs[0],'N_c1_mod8':coeffs[1],
            'normalized_norm_mod8':(coeffs[0]+4*coeffs[1])%8}

comparisons=[]
for m in range(1,65):
    atoms=[comb(4002*m,k)*comb(8005*m-k,m-k) for k in range(m+1)]
    vals=[v2(x) for x in atoms]
    c=min(vals)
    exact={'c':c,'N_c_mod8':vals.count(c)%8,'N_c1_mod8':vals.count(c+1)%8,
           'normalized_norm_mod8':(sum(x*x for x in atoms)>>(2*c))%8}
    actual=count(m)
    assert actual==exact,(m,actual,exact)
    comparisons.append({'m':m,**actual})
assert comparisons[5]['c']==0 and comparisons[5]['N_c_mod8']==2 and comparisons[5]['N_c1_mod8']==1
assert comparisons[21]['c']==1 and comparisons[21]['N_c_mod8']==4 and comparisons[21]['N_c1_mod8']==4
large=[]
for g in (1,2,5,32):
    for h in (3,11):
        value=count((1<<g)*h)
        assert (value['c'],value['normalized_norm_mod8'])==((0,6) if h==3 else (1,4))
        large.append({'g':g,'h':h,**value})
depth_one_tests=0
for H in range(32):
    h=4*H+3
    # Determine rawSmod4 from exact content plus normalized3bits.
    value=count(2*h)
    raw_mod4=0 if value['c'] else value['normalized_norm_mod8']%4
    predicted=2*(comb(4003*H+3002,H)%2)
    assert raw_mod4==predicted
    assert (predicted==2)==(H&(4002*H+3002)==0)
    depth_one_tests+=1
artifact={'status':'PASS','scope':'NEW eight-state high-binomial valuation observable against64 complete exact bounded sums and separated high-block cases',
    'exact_auxiliary_m_range':[1,64],'complete_exact_sum_comparisons':64,
    'finite_sum_details':comparisons,'large_g_valuation_cases':large,
    'depth_one_full_word_tests':depth_one_tests,'all_terminal_zero_enforced':True,
    'unit_factorials_used_in_counter':False,'original_power_high_word_evaluated':False,
    'all_prime_final_pair_evaluated':False,'irrationality_proved':False,
    'report_sha256':hashlib.sha256((C.parent/'responses/A5_turn7.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'binary_high_norm_counter_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k!='finite_sum_details'}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'binary_high_norm_counter_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
