#!/usr/bin/env python3
"""NEW exact finite-field Cartier realization and direct coefficient checks.
This is coordinator-authored arithmetic, not execution of remote report code.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
C=Path(__file__).resolve().parent
start=time.monotonic()
p=3

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c
def power(a,k):
    result=[1]
    for _ in range(k):result=mul(result,a)
    return result
def pad(a):
    assert len(a)<=7
    return tuple(a+[0]*(7-len(a)))
K=[mul([0]*(2-r)+[1],mul(power([1,-1],3+r),power([1,1],7-3*r))) for r in range(3)]
initial=[pad(mul([1,-1],power([1,1],4))),
         pad([0]+power([1,1],5)),
         pad(mul(power([1,-1],2),power([1,1],3))),
         pad(mul(power([1,-1],2),power([1,1],4)))]

def step(H,r):
    prod=mul(list(H),K[r])
    out=prod[2::3]
    while out and out[-1]==0:out.pop()
    return pad(out)
def explicit(H,r):
    h0,h1,h2,h3,h4,h5,h6=H
    if r==0:
        out=[h0,h3+h2+h0,h6+h5+h3+h2-h0,h6+h5-h3-h2-h0,-h6-h5-h3-h2,-h6-h5,0]
    elif r==1:
        out=[h1,h4-h2,-h5-h1,h2-h4,h5,0,0]
    else:
        out=[h2-h1-h0,h5-h4-h3+h1+h0,-h6+h4+h3-h2,h6-h5,0,0,0]
    return tuple(x%p for x in out)
def run(H,digits):
    for r in digits:H=step(H,r)
    return H
def coefficient(H,n):
    while n:
        H=step(H,n%3);n//=3
    return H[0]

basis=[tuple(int(i==j) for i in range(7)) for j in range(7)]
transition_checks=0
R=(2,1,0,2,1,0,0);P=(1,1,2,2,0,0,0)
suffix=[2,1,1,1,1,0,1,0]
shifted=[1,1,1,1,1,0,1,0]
for H in basis:
    for r in range(3):
        assert step(H,r)==explicit(H,r);transition_checks+=1
    scalar=(H[5]-H[4]-H[3]+H[1]+H[0])%3
    assert run(H,suffix)==tuple(scalar*x%3 for x in R)
    assert run(H,[1]*25)[0]==(H[1]-H[5])%3
    scalar2=(H[4]-H[2])%3
    assert run(H,shifted)==tuple(scalar2*x%3 for x in R)
assert [run(H,suffix) for H in initial]==[tuple(2*x%3 for x in R),R,R,R]
assert run(initial[2],shifted)==run(initial[3],shifted)==(0,)*7
reachable={R};frontier=[R]
while frontier:
    H=frontier.pop()
    for r in range(3):
        new=step(H,r)
        if new not in reachable:reachable.add(new);frontier.append(new)
assert reachable=={R,P,tuple(2*x%3 for x in R),tuple(2*x%3 for x in P),(0,)*7}

# Direct characteristic-zero coefficient definitions, new indices61..140.
def direct(m,adjacent):
    limit=m-1 if adjacent else m
    top=3*m-2 if adjacent else 3*m-1
    alpha=F(2*m-3 if adjacent else 2*m-1,2)
    gen=F(1);total=F(0)
    for k in range(limit+1):
        total+=comb(top,limit-k)*gen*(1<<k)
        gen*=F(alpha-k,k+1)
    total*=(-1)**limit
    assert total.denominator%3
    return total.numerator*pow(total.denominator,-1,3)%3
sample_checks=0
for m in range(61,141):
    assert coefficient(initial[0],m)==direct(m,False)
    assert coefficient(initial[1],m)==direct(m,True)
    sample_checks+=2
language_checks=0
for length in range(8):
    for word in itertools.product(range(3),repeat=length):
        state=run(R,list(reversed(word)))
        actual=(state[1]-state[5])%3
        expected=0 if 2 in word else (-1)**sum(word[i:i+2]==(0,1) for i in range(max(0,length-1)))%3
        assert actual==expected;language_checks+=1

artifact={'status':'PASS','scope':'NEW seven-dimensional actual endpoint Cartier realization modulo3, five-state suffix quotient, and160 direct same-index coefficient checks; cylinder language only',
    'multiplier_coefficients':K,'initial_numerators':initial,'basis_transition_checks':transition_checks,
    'suffix_basis_checks':7,'prefix_basis_checks':7,'shifted_suffix_basis_checks':7,
    'reachable_post_suffix_states':sorted(reachable),'direct_coefficient_indices':[61,140],'direct_coefficient_checks':sample_checks,
    'middle_word_checks':language_checks,'middle_word_lengths':[0,7],
    'original_power_middle_word_classified':False,'higher_primitive_layer_evaluated':False,
    'irrationality_proved':False,'report_sha256':hashlib.sha256((C.parent/'responses/A1_turn14.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'ternary_endpoint_cartier_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt=dict(artifact);receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'ternary_endpoint_cartier_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
