#!/usr/bin/env python3
"""New p-square finite-prefix controls with exact integer corroboration."""
from math import comb
from pathlib import Path
import hashlib
import json
import random
import resource
from kernel29_digit_coordinator import tails

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
ROOT = Path(__file__).resolve().parent
p,Q = 29,841
H = [0]
for r in range(1,p):
    H.append((H[-1]+pow(r,-1,p))%p)
BIN = [[comb(n,k)%Q if k<=n else 0 for k in range(p)] for n in range(p)]

def digits(n):
    out = []
    while n:
        n,r = divmod(n,p)
        out.append(r)
    return out or [0]

def prefix(N,J):
    if J<0:
        return 0,0
    nd,jd = digits(N),digits(J)
    L = max(len(nd),len(jd))+1
    nd += [0]*(L-len(nd))
    jd += [0]*(L-len(jd))
    # Each pair is (ordinary digit product sum modp²,
    #                 weighted harmonic-correction sum modp).
    states = {(0,0):(1,0)}
    edges,max_states = 0,1
    for i in range(L):
        nxt = {}
        for (borrow,previous),(base,correction) in states.items():
            for d in range(nd[i]+1):
                outborrow = int(jd[i]-d-borrow<0)
                weight = BIN[nd[i]][d]**2%Q
                effect = 0 if i==0 else 2*(nd[i]*H[nd[i-1]]-d*H[previous]
                           -(nd[i]-d)*H[nd[i-1]-previous])%p
                target = (outborrow,d)
                old_base,old_correction = nxt.get(target,(0,0))
                nxt[target] = ((old_base+base*weight)%Q,
                              (old_correction+correction*weight+base*weight*effect)%p)
                edges += 1
        states = nxt
        max_states = max(max_states,len(states))
        assert len(states)<=58
    a,c = states.get((0,0),(0,0))
    return (a+p*c)%Q,edges

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%p

def main():
    assert pow(3,249005515,p**7)==5764320805
    assert pow(3,574312172,p**7)==(1+15*p**6)%(p**7)
    assert [((pow(3,249005515+574312172*u,p**7)//p**6)%p) for u in range(29)]==[(9-u)%p for u in range(29)]
    rng = random.Random(84120261006)
    exact = []
    for _ in range(64):
        N,J = rng.randrange(1,340),rng.randrange(0,100)
        actual = sum(comb(N,j)**2 for j in range(min(N,J)+1))%Q
        value,edges = prefix(N,J)
        assert value==actual
        exact.append({'N':N,'J':J,'value':value,'candidate_edges':edges})
    beta6 = 410910916
    controls = []
    expected = {0:667,1:87,2:203,8:812}
    rankrows = []
    for C in (0,1,2,3,4,5,8,9,28):
        b = beta6+p**6*C
        n = 2001*b
        value,edges = prefix(n+2,b-1)
        X = 2001*C+1382
        h = [sum(comb(X,q)**2*comb(X+C-q,C-q)**m for q in range(C+1))%p for m in (0,1,2)]
        Bstar,Nstar = (b-687936)//p**4,(n+2-191112)//p**4
        T1,T2 = tails(Bstar,Nstar)
        assert (T1,T2)==(20*h[1]%p,6*h[2]%p)
        assert value==667*h[0]%Q
        if C in expected:
            assert value==expected[C]
        if C<3:
            rankrows.append([h[0],T1,T2])
        controls.append({'C':C,'b':str(b),'n':str(n),'prefix_mod841':value,
                         'H_tails_mod29':h,'T_tails_mod29':[h[0],T1,T2],
                         'candidate_edges':edges,'original_power':False})
    assert det3(rankrows)==17
    cert = {'status':'PASS','scope':'Newmod841 finite phase-prefix/rank controls and64 exact bounded prefix checks; no original norm or tail evaluated',
            'phase_affine_digit_checked_for_all29_classes':True,'controls':controls,
            'exact_bounded_checks':exact,'rank_determinant_mod29':17,
            'original_Gram_pair_computed':False,'norm_relative_alignment_proved':False}
    target = ROOT/'kernel841_prefix_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {k:v for k,v in cert.items() if k not in ('controls','exact_bounded_checks')}
    receipt.update({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                    'phase_prefix_values':[[r['C'],r['prefix_mod841']] for r in controls],
                    'exact_bounded_count':len(exact),
                    'maximum_candidate_edges':max(r['candidate_edges'] for r in controls)})
    (ROOT/'kernel841_prefix_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
