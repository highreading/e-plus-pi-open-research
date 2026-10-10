#!/usr/bin/env python3
"""New rigorous fixed-point enclosures of all five complete n3375 forms."""
from pathlib import Path
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(240,240))
sys.set_int_max_str_digits(500000)
ROOT=Path(__file__).resolve().parent

def constants(bits):
    S=1<<bits
    total=0;fac=1;k=0
    while True:
        total+=S//fac
        if fac>S:break
        k+=1;fac*=k
    # k+1 finite terms each lose <1 unit; the positive e-tail is <1.
    elo,ehi=total,total+k+2
    def atan(q):
        power=q;idx=0;base=0
        positive=negative=0
        while power<=S:
            term=S//((2*idx+1)*power)
            if idx%2:base-=term;negative+=1
            else:base+=term;positive+=1
            power*=q*q;idx+=1
        # The next alternating remainder is <1 unit, in either direction.
        return base-negative-1,base+positive+1,idx
    a,b,na=atan(5);c,d,nb=atan(239)
    slo,shi=elo+16*a-4*d,ehi+16*b-4*c
    assert slo<shi
    return S,slo,shi,{'e_terms':k+1,'atan5_terms':na,'atan239_terms':nb,'width_units':shi-slo}

def logfloor(a,S):
    assert a>0
    e=len(str(a))-len(str(S))
    if e>=0:
        if a<S*10**e:e-=1
    elif a*10**(-e)<S:e-=1
    return e

def main():
    started=time.monotonic()
    source=ROOT/'complete_endpoint_3375_certificate.json'
    data=json.loads(source.read_text())
    bits=120000
    S,slo,shi,budget=constants(bits)
    rows=[];full=[]
    for z in data['probes']:
        pp,qq=int(z['p']),int(z['q'])
        low,high=qq*slo-pp*S,qq*shi-pp*S
        assert low<high
        sign=1 if low>0 else -1 if high<0 else 0
        a=min(abs(low),abs(high)) if sign else 0
        b=max(abs(low),abs(high))
        rows.append({'label':z['label'],'sign_certified':sign,'interval_contains_zero':not sign,
                     'floor_log10_abs_lower':logfloor(a,S) if a else None,'floor_log10_abs_upper':logfloor(b,S),
                     'abs_form_above_one_certified':a>S,'abs_form_below_one_certified':b<S})
        full.append({'label':z['label'],'lower_numerator':str(low),'upper_numerator':str(high),'common_denominator':str(S)})
    artifact={'n':3375,'precision_bits':bits,'constant_lower_numerator':str(slo),'constant_upper_numerator':str(shi),
              'common_denominator':str(S),'series_budget':budget,'whole_form_intervals':full,'rows':rows}
    target=ROOT/'endpoint_3375_whole_forms_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt={'status':'PASS','scope':'New rigorous same-index complete forms at originaln3375 and five reduced weights; no infinite exclusion theorem',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'producer_artifact_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'enclosure_artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'precision_bits':bits,'series_budget':budget,'rows':rows,'elapsed_seconds':round(time.monotonic()-started,3),
             'irrationality_proved':False}
    (ROOT/'endpoint_3375_whole_forms_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()
