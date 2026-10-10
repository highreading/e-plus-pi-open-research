#!/usr/bin/env python3
"""Personally authored digit/finite-prefix controls; no original-long scan."""
from math import comb
from pathlib import Path
import hashlib
import json
import random
import resource

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
ROOT = Path(__file__).resolve().parent
P = 29
DIGIT = [[comb(a,b)%P if b<=a else 0 for b in range(P)] for a in range(P)]

def digits(x):
    assert x >= 0
    out = []
    while x:
        x,r = divmod(x,P)
        out.append(r)
    return out or [0]

def lucas(n,k):
    if k<0 or n<k:
        return 0
    out = 1
    while n or k:
        n,a = divmod(n,P)
        k,b = divmod(k,P)
        if b>a:
            return 0
        out = out*DIGIT[a][b]%P
    return out

def general(n,k,exact=False):
    if k<0:
        return 0
    if n>=0:
        return ((comb(n,k)%P if k<=n else 0) if exact else lucas(n,k))
    return ((-1)**k*(comb(-n+k-1,k)%P if exact else lucas(-n+k-1,k)))%P

def direct(b,n,t,A,v,Ap,vp,exact=False):
    out = 0
    for j in range(b):
        w = general(n+2,j,exact)
        if w:
            out += w*w*general(j,t,exact)*general(A,b+v-j,exact)*general(Ap,b+vp-j,exact)
    return out%P

def kernel(b,n,t,A,v,Ap,vp):
    B,Bp = b+v,b+vp
    if A==0 or Ap==0:
        if Ap==0 and A!=0:
            return kernel(b,n,t,Ap,vp,A,v)
        if not (0<=B<b):
            return 0,1
        z = lucas(n+2,B)**2*lucas(B,t)*general(Ap,Bp-B)%P
        return z,1
    assert A<0 and Ap<0
    J = min(b-1,B,Bp)
    if J<0:
        return 0,1
    constants = [n+2,J,B,Bp,-A-1,-Ap-1,t]
    ds = [digits(x) for x in constants]
    L = max(map(len,ds))
    ds = [z+[0]*(L-len(z)) for z in ds]
    states = {(0,0,0):1}
    max_states = 1
    for i in range(L):
        N,JJ,BB,BBp,D,Dp,tt = (z[i] for z in ds)
        new = {}
        for (ej,eb,ebp), value in states.items():
            for j in range(tt,N+1):
                xj,xb,xbp = JJ-j-ej,BB-j-eb,BBp-j-ebp
                kj,kb,kbp = xj%P,xb%P,xbp%P
                if D+kb>=P or Dp+kbp>=P:
                    continue
                weight = DIGIT[N][j]**2*DIGIT[j][tt]*DIGIT[D+kb][D]*DIGIT[Dp+kbp][Dp]%P
                if not weight:
                    continue
                st = (int(xj<0),int(xb<0),int(xbp<0))
                new[st] = (new.get(st,0)+value*weight)%P
        states = new
        max_states = max(max_states,len(states))
        assert len(states)<=4
    return ((-1 if (v+vp)%2 else 1)*states.get((0,0,0),0))%P,max_states

def tails(B,N):
    ds = [digits(B),digits(N)]
    L = max(map(len,ds))
    ds = [z+[0]*(L-len(z)) for z in ds]
    state = {0:(1,1)}
    for i in range(L):
        bb,nn = ds[0][i],ds[1][i]
        new = {}
        for borrow,(v1,v2) in state.items():
            for q in range(nn+1):
                sub = bb-q-borrow
                k = sub%P
                if nn+k>=P:
                    continue
                w = DIGIT[nn][q]**2%P
                z = DIGIT[nn+k][k]
                out = int(sub<0)
                old1,old2 = new.get(out,(0,0))
                new[out] = ((old1+v1*w*z)%P,(old2+v2*w*z*z)%P)
        state = new
    return state.get(0,(0,0))

def main():
    beta = 687936
    assert pow(3,249005515,P**4)==beta
    assert pow(3,574312172,P**4)==1
    n = 2001*beta
    cases = [(0,-1,-1,-1,-1,0),(0,0,-1,-n,2,0),(0,-2*n,2,-n,2,0),
             (0,-n,2,-n,2,24),(0,-1,-1,-n,2,10)]
    phase = []
    for t,A,v,Ap,vp,expected in cases:
        computed, states = kernel(beta,n,t,A,v,Ap,vp)
        evaluated = direct(beta,n,t,A,v,Ap,vp)
        assert computed==evaluated==expected
        phase.append({'parameters':[t,A,v,Ap,vp],'digit_result':computed,
                      'direct_finite_prefix_result':evaluated,'max_reachable_states':states})
    tail_rows = []
    expected_rows = {0:(1,1),1:(13,25),28:(28,1),29:(4,7),30:(21,0)}
    for B in (0,1,2,3,5,11,28,29,30,31,55,80):
        N = 2001*B+1946
        pair = tuple(sum(comb(N,q)**2*comb(N+B-q,B-q)**m for q in range(B+1))%P for m in (1,2))
        computed = tails(B,N)
        assert computed==pair
        if B in expected_rows:
            assert pair==expected_rows[B]
        tail_rows.append({'B':B,'N':N,'values':list(computed),'exact_integer_sum_agrees':True})
    rng = random.Random(20261006)
    tests = []
    for _ in range(96):
        b,n = rng.randrange(2,64),rng.randrange(1,160)
        t = rng.randrange(0,9)
        A,Ap = -rng.randrange(0,90),-rng.randrange(0,90)
        v,vp = rng.randrange(-6,7),rng.randrange(-6,7)
        computed, states = kernel(b,n,t,A,v,Ap,vp)
        exact = direct(b,n,t,A,v,Ap,vp,True)
        assert computed==exact
        tests.append({'parameters':[b,n,t,A,v,Ap,vp],'value':computed,'max_states':states})
    cert = {'status':'PASS','scope':'Five new phase-compatible auxiliary kernels, twelve small tails and96 exact bounded kernels; no original tail or norm digit computed',
            'phase_kernel_checks':phase,'tail_checks':tail_rows,'exact_bounded_kernel_checks':tests,
            'no_original_long_array':True,'original_tail_evaluated':False,'irrationality_proved':False}
    target = ROOT/'kernel29_digit_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {k:v for k,v in cert.items() if k not in ('phase_kernel_checks','tail_checks','exact_bounded_kernel_checks')}
    receipt.update({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                    'phase_values':[z['digit_result'] for z in phase],
                    'exact_bounded_kernel_count':len(tests),'tail_count':len(tail_rows),
                    'max_observed_states':max(z['max_states'] for z in tests)})
    (ROOT/'kernel29_digit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
