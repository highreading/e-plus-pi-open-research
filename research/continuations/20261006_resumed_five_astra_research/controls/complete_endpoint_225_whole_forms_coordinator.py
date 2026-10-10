#!/usr/bin/env python3
"""Personally authored rational enclosures for the complete n225 forms."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(100000)

def floor_log10_positive(x):
    assert x>0
    a,b=x.numerator,x.denominator
    e=len(str(a))-len(str(b))
    if e>=0:
        if a<b*10**e:
            e-=1
    elif a*10**(-e)<b:
        e-=1
    return e

def serial(x):
    if isinstance(x,F):
        return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
    if isinstance(x,dict):
        return {k:serial(v) for k,v in x.items()}
    if isinstance(x,list):
        return [serial(v) for v in x]
    return x

def main():
    source=ROOT/'complete_endpoint_225_certificate.json'
    data=json.loads(source.read_text())
    N=768
    elo=sum((F(1,factorial(k)) for k in range(N+1)),F(0))
    ehi=elo+F(N+2,(N+1)*factorial(N+1))
    def atan_bounds(c):
        lo=sum((F((-1)**k,(2*k+1)*c**(2*k+1)) for k in range(N)),F(0))
        return lo,lo+F(1,(2*N+1)*c**(2*N+1))
    alo,ahi=atan_bounds(5)
    blo,bhi=atan_bounds(239)
    slo,shi=elo+16*alo-4*bhi,ehi+16*ahi-4*blo
    assert slo<shi
    rows=[]
    full=[]
    for probe in data['probes']:
        p,q=int(probe['p']),int(probe['q'])
        lo,hi=q*slo-p,q*shi-p
        assert lo<hi
        sign=1 if lo>0 else -1 if hi<0 else 0
        if sign:
            minabs,maxabs=min(abs(lo),abs(hi)),max(abs(lo),abs(hi))
            e_low,e_high=floor_log10_positive(minabs),floor_log10_positive(maxabs)
            small=maxabs<1
            larger=minabs>1
        else:
            minabs,maxabs=F(0),max(abs(lo),abs(hi))
            e_low,e_high=None,floor_log10_positive(maxabs)
            small=maxabs<1
            larger=False
        rows.append({'label':probe['label'],'sign_certified':sign,
                     'floor_log10_abs_lower':e_low,'floor_log10_abs_upper':e_high,
                     'abs_form_below_one_certified':small,'abs_form_above_one_certified':larger,
                     'interval_contains_zero':sign==0})
        full.append({'label':probe['label'],'q_e_plus_pi_minus_p_lower':lo,'q_e_plus_pi_minus_p_upper':hi})
    artifact={'n':225,'S_lower':slo,'S_upper':shi,'series_degree':N,'whole_form_intervals':full}
    out=ROOT/'complete_endpoint_225_whole_forms_certificate.json'
    out.write_text(json.dumps(serial(artifact),indent=2)+'\n')
    receipt={'status':'PASS','scope':'Exact rational enclosures at one original n225 and five reduced weights; no infinite exclusion or irrationality proof',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'producer_artifact_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'enclosure_artifact_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
             'e_tail_bound':'(N+2)/((N+1)*(N+1)!)','pi_identity':'16*atan(1/5)-4*atan(1/239)',
             'atan_even_partial_sum_is_lower':True,'series_degree':N,'rows':rows,'irrationality_proved':False}
    (ROOT/'complete_endpoint_225_whole_forms_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
