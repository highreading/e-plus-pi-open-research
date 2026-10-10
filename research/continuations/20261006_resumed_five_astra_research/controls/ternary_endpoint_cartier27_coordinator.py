#!/usr/bin/env python3
"""NEW coordinator-derived53-coordinate paid modulo27 endpoint experiment.
The symbolic congruence is independently derived; no remote code is executed.
"""
from fractions import Fraction
from pathlib import Path
from math import comb
import hashlib
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
C=Path(__file__).resolve().parent
started=time.monotonic()
MOD=27
SIZE=53

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%MOD
    return out
def power(a,e):
    out=[1]
    for _ in range(e):out=mul(out,a)
    return out
def padded(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    assert len(a)<=SIZE
    return tuple(a+[0]*(SIZE-len(a)))
plus,minus=[1,1],[1,-1]
restore=power([1,0,-1],12)
mults=[]
for r in range(3):
    mults.append([mul(power(plus,15-3*r),power(minus,15+r)),
                  mul(power(plus,15-3*r),power(minus,13+r)),
                  mul(power(plus,15-3*r),power(minus,11+r)),
                  mul(power(plus,13-3*r),power(minus,15+r))])
def section(poly,shift):
    out=[]
    for i,x in enumerate(poly):
        exponent=i+shift
        if exponent%3==0:
            assert exponent>=0
            k=exponent//3
            while len(out)<=k:out.append(0)
            out[k]=x
    return out or [0]
def step(N,r,q):
    sections=[section(mul(N,mults[r][i]),[-r,1-r,2-r,1-r][i]) for i in range(4)]
    weights=[1,-3*q,9*q*(q+1)//2,-9*q]
    total=[sum(weights[j]*(sections[j][i] if i<len(sections[j]) else 0) for j in range(4))
           for i in range(max(map(len,sections)))]
    return padded(mul(restore,total))
initial=[padded(mul(power(minus,25),power(plus,26))),
         padded([0]+mul(power(minus,24),power(plus,27))),
         padded(mul(power(minus,26),power(plus,25))),
         padded(mul(power(minus,26),power(plus,26)))]
def run(N,digits):
    for i,r in enumerate(digits):
        q=(digits[i+1] if i+1<len(digits) else 0)+3*(digits[i+2] if i+2<len(digits) else 0)
        N=step(N,r,q)
    return N
def value(N,n):
    while n:
        N=step(N,n%3,(n//3)%9)
        n//=3
    return N[0]
def direct(m,adjacent):
    count=m-1 if adjacent else m
    top=3*m-2 if adjacent else 3*m-1
    alpha=Fraction(2*m-3 if adjacent else 2*m-1,2)
    gen,total=Fraction(1),Fraction(0)
    for k in range(count+1):
        total+=comb(top,count-k)*gen*(1<<k)
        gen*=Fraction(alpha-k,k+1)
    total*=(-1)**count
    assert total.denominator%3
    return total.numerator*pow(total.denominator,-1,MOD)%MOD

direct_checks=0
for m in range(181,221):
    for adjacent in (False,True):
        assert value(initial[int(adjacent)],m)==direct(m,adjacent)
        direct_checks+=1
basis=[tuple(int(i==j) for i in range(SIZE)) for j in range(SIZE)]
degree_checks=0
for N in basis:
    for r in range(3):
        for q in range(9):
            assert step(N,r,q)[52]==0
            degree_checks+=1

suffix=[2,1,1,1,1,0,1,0]
middle=(2,0,2,0,2)
outputs={}
for length in range(4):
    for high_word in itertools.product(range(3),repeat=length):
        full_middle=high_word+middle
        digits=suffix+list(reversed(full_middle))+[1]*25
        pair=tuple(run(N,digits)[0] for N in initial[:2])
        assert all(x%9==0 for x in pair)
        outputs.setdefault(str(tuple(x//9 for x in pair)),[]).append(list(high_word))

# NEW numerical representative of the fixed-tail original exponent progression.
target=795583
jstar=0
for exponent in range(2,14):
    old_period=3**(exponent-2)
    candidates=[jstar+d*old_period for d in range(3)]
    matches=[j for j in candidates if pow(4,j,3**exponent)==target%(3**exponent)]
    assert len(matches)==1
    jstar=matches[0]
assert 0<=jstar<531441 and jstar%243==81
assert pow(4,jstar,1594323)==795583

artifact={'status':'PASS',
    'scope':'NEW coordinator-derived53-coordinate modulo27 endpoint realization, new characteristic-zero coefficients and finite killing-tail divided directions; not an original-window direction theorem',
    'dimension':SIZE,'denominator_Q_power':26,'restore_Q_power':12,
    'lookahead_modulus':9,'degree_basis_checks':degree_checks,
    'new_direct_coefficient_indices':[181,220],'direct_endpoint_checks':direct_checks,
    'killing_tail_msf':middle,'high_middle_lengths':[0,3],
    'finite_killing_tail_words':sum(map(len,outputs.values())),
    'divided_endpoint_direction_classes_mod3':{k:{'count':len(v),'first_high_word_msf':v[0]} for k,v in outputs.items()},
    'original_fixed_tail_j_residue':jstar,'original_fixed_tail_j_period':531441,
    'original_j81mod243_verified':True,'original_m_residue':1194953,'original_m_modulus':1594323,
    'eligible_original_power_middle_word_evaluated':False,
    'infinite_original_primitive_direction_proved':False,
    'all_prime_q_evaluated':False,'irrationality_proved':False,
    'initial_numerators':initial,
    'formula_explanation':'sigma(u)=sigma(u^3)Q(u^3)^4/Q(u)^13 mod27; x(u^3)/x(u)^3 raised toq equals1-3qu/b^2+9binom(q+1,2)u^2/b^4-9qu/a^2 mod27. Pad toQ^54, section, and restoreQ^26 withQ^12. All inversions have constant term1.',
    'elapsed_seconds':round(time.monotonic()-started,3)}
out=C/'ternary_endpoint_cartier27_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k!='initial_numerators'}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'ternary_endpoint_cartier27_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
