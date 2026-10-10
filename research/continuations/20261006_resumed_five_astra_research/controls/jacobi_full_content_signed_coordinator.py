#!/usr/bin/env python3
"""NEW independent full-coefficient audit of the 8/16-state modules."""
from pathlib import Path
from math import comb, factorial
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
C=Path(__file__).resolve().parent
start=time.monotonic()

def digits(x,L):
    out=[]
    for _ in range(L):
        out.append(x%3);x//=3
    assert x==0
    return out

def val3(x):
    assert x
    e=0
    while x%3==0:x//=3;e+=1
    return e

def module(s,n,signed):
    L=1
    while 3**L<=max(n,2*s):L+=1
    sd,nd=digits(s,L),digits(n,L)
    carry=0;ad=[]
    for z in sd:
        ad.append((z+1+carry)%3);carry=(z+1+carry)//3
    states={(0,0,0,0) if signed else (0,0,0):(0,1,0)}
    for i,(si,ni,ai) in enumerate(zip(sd,nd,ad)):
        new={}
        for state,(cost,weight,witness) in states.items():
            c,b,g=state[:3];doubling=state[3] if signed else 0
            for x in range(3):
                for y in range(3):
                    v=x+y+c-si
                    if v not in (0,3):continue
                    cp=v//3;bp=int(x+b>ni);gp=int(y+g>ai)
                    cp_cost=cost+bp+gp
                    if signed:
                        z=ni-x-b+3*bp
                        td=(2*x+doubling)%3;dp=(2*x+doubling)//3
                        sign=-1 if (bp+gp+x-int(z==2)-int(td==2)-int(y==2))%2 else 1
                        dst=(cp,bp,gp,dp)
                    else:
                        sign=1;dst=(cp,bp,gp)
                    contribution=(weight*sign)%3
                    candidate=witness+x*3**i
                    if dst not in new or cp_cost<new[dst][0]:
                        new[dst]=(cp_cost,contribution,candidate)
                    elif cp_cost==new[dst][0]:
                        old=new[dst];new[dst]=(old[0],(old[1]+contribution)%3,old[2])
        states=new
    terminal=(0,0,0,0) if signed else (0,0,0)
    assert terminal in states
    cost,total,witness=states[terminal]
    assert 0<=witness<=s
    if signed:
        def d2(x):return digits(x,L).count(2)
        if (d2(n)+d2(2*s)-d2(s))%2:total=-total%3
    return cost,total,witness,L

records=[]
for m in range(241,261):
    for s,n in ((m,3*m-1),(m-1,3*m-2)):
        # A single dyadic unit4^s clears every exact Bernstein coefficient.
        # Independent factorial arithmetic, followed by the full basis change.
        f=[factorial(z) for z in range(n+1)]
        scaled=[]
        for k in range(s+1):
            numerator=f[n]*f[2*s]*4**k
            denominator=f[n-k]*f[2*k]*f[s]*f[s-k]
            q,r=divmod(numerator,denominator);assert r==0
            scaled.append(q)
        rbern=min(map(val3,scaled))
        mono=[(-1)**(s-l)*sum(scaled[k]*comb(s-k,l-k) for k in range(l+1)) for l in range(s+1)]
        rmono=min(val3(x) for x in mono if x)
        endpoint=(-1)**s*sum(x*2**(s-k) for k,x in enumerate(scaled))
        assert endpoint==sum(x*(-1)**i for i,x in enumerate(mono))
        rmp,_,witness,L=module(s,n,False)
        rsigned,residue,_,_=module(s,n,True)
        exact_residue=(endpoint//3**rbern)%3
        assert rbern==rmono==rmp==rsigned
        assert residue==exact_residue
        assert val3(scaled[witness])==rbern
        pattern=''.join(map(str,reversed(digits(m,len(digits(m,L)))))).count('20')
        if m%3:assert rbern>=pattern
        records.append({'m':m,'s':s,'n':n,'full_Bernstein_content':rbern,
            'full_monomial_content':rmono,'min_plus_content':rmp,
            'minimizing_k':witness,'signed_residue':residue,
            'exact_endpoint_at_content_mod3':exact_residue,
            'endpoint_content':val3(endpoint),'pattern20_count':pattern,
            'input_digits':L,'terminal_carries':[0,0,0,0]})
artifact={'status':'PASS','scope':'40 NEW auxiliary full-polynomial-content and signed-minimum audits at m241..260; no original eligible power evaluated',
    'cases':records,'case_count':len(records),'old_mod81_comparisons_rerun':False,
    'original_window_index_evaluated':False,'irrationality_proved':False,
    'source_report_sha256':hashlib.sha256((C.parent/'responses/A1_turn18.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'jacobi_full_content_signed_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k!='cases'}
receipt['content_range']=[min(x['min_plus_content'] for x in records),max(x['min_plus_content'] for x in records)]
receipt['endpoint_extra_cancellation_cases']=sum(x['signed_residue']==0 for x in records)
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'jacobi_full_content_signed_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
