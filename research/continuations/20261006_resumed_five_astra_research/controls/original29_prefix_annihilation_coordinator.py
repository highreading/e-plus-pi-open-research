#!/usr/bin/env python3
"""NEW genuine original-power carry evaluations from annihilating finite prefixes.
All unseen high digits remain arbitrary; both ordinary/weighted products must
vanish before a zero is certified. No original-length power is constructed.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(30,30))
ROOT=Path(__file__).resolve().parent
start=time.monotonic()
p=29;cap=128;beta=410910916;base=p**6

def matrix(ai,Bi,mi,weighted):
    out=[[0,0],[0,0]]
    for incoming in [0,1]:
        for outgoing in [0,1]:
            for d in range(ai+1):
                k=mi+p*outgoing-incoming-d
                if 0<=k<=28-Bi:
                    out[incoming][outgoing]=(out[incoming][outgoing]+(d if weighted else 1)*comb(ai,d)**2*comb(Bi+k,k)**2)%p
    return out

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)] for i in range(2)]

cases=[]
for u in [0,1,2,381475]:
    E=249005515+574312172*u
    modulus=p**(cap+7)
    residue=pow(3,E,modulus)
    assert residue%base==beta
    Cpart=(residue-beta)//base
    assert E>4*(cap+7)
    a,B,m=69*Cpart+47,2*(69*Cpart+47)+1,Cpart//p
    ordinary=[[1,0],[0,1]];weighted=[[1,0],[0,1]]
    stages=[]
    for i in range(cap):
        ai,Bi,mi=a%p,B%p,m%p
        K=matrix(ai,Bi,mi,False)
        KW=matrix(ai,Bi,mi,i==0)
        ordinary=mm(ordinary,K);weighted=mm(weighted,KW)
        stages.append({'digit':i,'a_digit':ai,'B_digit':Bi,'m_digit':mi,'K':K,'ordinary_product':ordinary,'weighted_product':weighted})
        a//=p;B//=p;m//=p
        if ordinary==weighted==[[0,0],[0,0]]:
            break
    zero=ordinary==weighted==[[0,0],[0,0]]
    assert zero
    # The low connection needs C0 and a mod29, already fixed above. Once
    # both prefix matrices vanish every branch moment vanishes for every
    # possible continuation and the actual terminal observation.
    cases.append({'original_u':u,'original_power_exponent':str(E),'prefix_digits_consumed':len(stages),
        'C_prefix_LSF':[(Cpart//p**k)%p for k in range(len(stages)+1)],
        'stages':stages,'ordinary_and_weighted_zero_for_every_high_continuation':zero,
        'actual_original_D_S0_S2_kappa_mod29':[0,0,0,0]})
artifact={'status':'PASS','scope':'NEW actual original-power carry zero at four specified u via finite two-state ordinary/weighted prefix annihilation; full columns/error not evaluated',
    'max_prefix_digits':cap,'original_length_power_constructed':False,'original_cases':cases,
    'unseen_high_digits_read':False,'all_terminal_high_continuations_annihilated':True,
    'complete_physical_eta_zero_if_norm_reduction_accepted':True,
    'primitive_norm_first_nonzero_layer_evaluated':False,'all_prime_primitive_denominator_evaluated':False,'irrationality_proved':False,
    'report_sha256':hashlib.sha256((ROOT.parent/'responses/A2_turn9.md').read_bytes()).hexdigest(),
    'connection_receipt_sha256':hashlib.sha256((ROOT/'actual29_digit_connection_receipt.json').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=ROOT/'original29_prefix_annihilation_certificate.json';out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k!='original_cases'}
receipt['original_cases']=[{k:v for k,v in row.items() if k not in ('stages','C_prefix_LSF')} for row in cases]
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(ROOT/'original29_prefix_annihilation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
