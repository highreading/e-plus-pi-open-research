#!/usr/bin/env python3
"""Exact new eight-digit synchronization certificate and constructive paths."""
from itertools import product
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
ROOT = Path(__file__).resolve().parent
STATES = list(product(range(2), repeat=3))

def digits(x, length):
    return [(x // 3**i) % 3 for i in range(length)]

def prefix(m, adjacent, length):
    degree = m - int(adjacent)
    N = 3*m - 1 - int(adjacent)
    mod = 3**length
    alpha = ((2*m-1-2*int(adjacent))*pow(2, -1, mod)) % mod
    vec = {(0, 0, 0): 0}
    for mi, ni, ai in zip(digits(degree,length),digits(N,length),digits(alpha,length)):
        new = {}
        for (carry, nb, ab), cost in vec.items():
            for kd, rd in product(range(3),repeat=2):
                total = kd + rd + carry - mi
                if total not in (0, 3):
                    continue
                out = (total//3, int(ni-kd-nb<0), int(ai-rd-ab<0))
                candidate = cost + out[1] + out[2]
                new[out] = min(new.get(out, 10**9), candidate)
        vec = new
    return [vec.get(s) for s in STATES]

def content(m, adjacent=False):
    length = len(str(m))*3+6
    # An upper bound on ternary digits, followed by a common zero tail.
    return prefix(m,adjacent,length)[0]

def constructive_high_path(word):
    # The fixed low suffix ends with half-state q=0, evaluator state000.
    # Use 25 leading ones and a zero tail to discharge all finite borrows.
    high = list(word) + [1]*25 + [0]*4
    q = 0
    nb = ab = carry = cost = 0
    prev = 0
    events = []
    for i,d in enumerate(high):
        ai = ((1,2,0),(2,0,1))[q][d]
        qnew = ((0,0,1),(0,1,1))[q][d]
        kd = 0 if q==0 and d<2 else (2 if q==0 else int(d>0))
        rd = d-kd
        assert kd+rd+carry-d == 0
        nnew = int(prev-kd-nb<0)
        anew = int(ai-rd-ab<0)
        assert anew == 0
        if nnew:
            events.append(i)
            assert q==0 and d==2 and i<len(word)
        cost += nnew+anew
        prev, q, nb, ab = d,qnew,nnew,anew
    assert (carry,nb,ab)==(0,0,0)
    assert all(b-a>=2 for a,b in zip(events,events[1:]))
    assert cost <= (len(word)+1)//2
    return cost

def main():
    table = []
    for T in range(5,17):
        mod = 3**T
        m = 247*pow(8,-1,mod)%mod
        a,b = prefix(m,False,T),prefix(m,True,T)
        table.append({'T':T,'m_residue':m,'J':a,'adjacent':b,'equal':a==b})
        if T>=8:
            assert a==b and a[0]==0
            assert all(d in (0,1) for d in digits(m,T)[5:])
    assert table[3]['J']==[0,None,None,None,None,1,1,3]
    full = []
    for M in range(81):
        m = 851+6561*M
        r,u=content(m),content(m,True)
        assert r==u
        full.append({'M':M,'m':m,'r':r,'u':u})
    counts = []
    for length in range(8):
        costs = [constructive_high_path(w) for w in product(range(3),repeat=length)]
        counts.append({'middle_length':length,'words_checked':len(costs),'max_path_cost':max(costs),'bound':(length+1)//2})
    cert={'status':'PASS','scope':'finite exact synchronization vector, common-tail proof inputs, and constructive paths; no original Schur scalar evaluation',
          'state_order':STATES,'suffix_table':table,'complete_auxiliary_contents':full,'path_counts':counts,
          'common_high_degree':'M','common_high_N':'3*M','common_high_alpha':'M-1/2',
          'whole_inverse_norm_or_scalar_evaluated':False,'irrationality_proved':False}
    target=ROOT/'jacobi_suffix_identity_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'synchronized_suffix':[851,6561],'synchronized_vector':table[3]['J'],
             'complete_auxiliary_checks':len(full),'constructive_words_checked':sum(z['words_checked'] for z in counts),
             'max_middle_length':7,'original_scalar_evaluated':False}
    (ROOT/'jacobi_suffix_identity_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
