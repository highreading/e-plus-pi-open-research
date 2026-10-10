#!/usr/bin/env python3
"""NEW personally authored paid modulo81 endpoint corroboration.
No network, credentials, old producer, or old modulo27 rerun.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
C=Path(__file__).resolve().parent
started=time.monotonic()
MOD,SIZE=81,161
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if y:out[i+j]=(out[i+j]+x*y)%MOD
    return out
def power(a,n):
    out=[1]
    for _ in range(n):out=mul(out,a)
    return out
plus=[power([1,1],k) for k in range(85)]
minus=[power([1,-1],k) for k in range(85)]
restore=power([1,0,-1],39)
def negbin(q,j):
    return (-1)**j*comb(q+j-1,j) if q else int(j==0)
@lru_cache(None)
def kernel(r,q):
    out=[0]*85
    for i in range(4):
        for j in range(4-i):
            coefficient=(-3)**i*3**j*comb(3*q,i)*negbin(q,j)%MOD
            if not coefficient:continue
            poly=mul(plus[42-3*r-2*i],minus[42+r-2*j])
            for k,x in enumerate(poly):out[k+i+j]=(out[k+i+j]+coefficient*x)%MOD
    while out and not out[-1]:out.pop()
    return out or [0]
def step(N,r,q):
    poly=mul(N,kernel(r,q))
    section=[poly[k] for k in range(r,len(poly),3)]
    out=mul(restore,section or [0])
    while out and not out[-1]:out.pop()
    assert len(out)<=160
    return out or [0]
initial=[mul(minus[79],plus[80]),[0]+mul(minus[78],plus[81])]
def evaluate(digits):
    values=[]
    for initial_N in initial:
        N=initial_N
        for i,r in enumerate(digits):
            q=sum((digits[i+s] if i+s<len(digits) else 0)*3**(s-1) for s in range(1,4))
            N=step(N,r,q)
        values.append(N[0])
    return values
def digits(n):
    out=[]
    while n:out.append(n%3);n//=3
    return out
def direct(m,adjacent):
    count=m-1 if adjacent else m
    top=3*m-2 if adjacent else 3*m-1
    alpha=Fraction(2*m-3 if adjacent else 2*m-1,2)
    term,total=Fraction(1),Fraction(0)
    for k in range(count+1):
        total+=comb(top,count-k)*term*(1<<k)
        term*=Fraction(alpha-k,k+1)
    total*=(-1)**count
    assert total.denominator%3
    return total.numerator*pow(total.denominator,-1,MOD)%MOD

direct_rows=[]
for m in range(221,241):
    actual=evaluate(digits(m))
    expected=[direct(m,a) for a in (False,True)]
    assert actual==expected,(m,actual,expected)
    direct_rows.append({'m':m,'pair_mod81':actual})
transitions={
    'A':(('A',1),('C',-1),('Z',0)),
    'B':(('A',1),('C',1),('Z',0)),
    'C':(('A',1),('C',1),('Z',0)),
    'D':(('B',1),('D',-1),('E',-1)),
    'E':(('A',1),('D',1),('E',-1)),
    'Z':(('Z',0),('Z',0),('Z',0))}
terminal={'A':-1,'B':1,'C':1,'D':-1,'E':1,'Z':0}
def psi(word):
    state,amplitude='E',1
    for r in reversed(word):
        state,factor=transitions[state][r]
        amplitude=amplitude*factor%3
    return amplitude*terminal[state]%3
suffix=[2,1,1,1,1,0,1,0]+[2,0,2,0,2]
word_rows=[]
for length in range(5):
    for word in product(range(3),repeat=length):
        pair=evaluate(suffix+list(reversed(word))+[1]*25)
        z=psi(word)
        expected=[27*z%81,-27*z%81]
        assert pair==expected,(word,pair,expected)
        no_bad_order=not any(word[i]==2 and word[j]==0 for i in range(length) for j in range(i+1,length))
        assert bool(z)==no_bad_order
        word_rows.append({'high_word':list(word),'psi':z,'pair_mod81':pair})
artifact={'status':'PASS','scope':'NEW modulo81 module and divided endpoint image; finite cylinders, no original real-window power evaluated',
    'modulus':MOD,'coordinates':SIZE,'lookahead_modulus':27,
    'new_direct_characteristic_zero_checks':len(direct_rows)*2,
    'new_direct_index_range':[221,240],
    'finite_high_words_checked':len(word_rows),'maximum_high_word_length':4,
    'direct_rows':direct_rows,'word_rows':word_rows,
    'old_producer_or_mod27_computation_repeated':False,
    'infinite_original_nonzero_language_proved':False,'irrationality_proved':False,
    'elapsed_seconds':round(time.monotonic()-started,3)}
target=C/'ternary_endpoint_cartier81_certificate.json'
target.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k not in ('direct_rows','word_rows')}
receipt['three_named_witnesses']=[row for row in word_rows if row['high_word'] in ([],[0],[2,0])]
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
(C/'ternary_endpoint_cartier81_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
