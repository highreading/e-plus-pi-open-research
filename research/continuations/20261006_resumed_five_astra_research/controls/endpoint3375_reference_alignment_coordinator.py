#!/usr/bin/env python3
"""NEW reference-alignment content; reuse completed reference gcd fields."""
from fractions import Fraction
from math import factorial, gcd
from pathlib import Path
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent;start=time.monotonic()
source=C/'complete_endpoint_3375_certificate.json'
data=json.loads(source.read_text());n=int(data['n']);assert n==3375
m,N=n+1,n+2
def rat(x):return Fraction(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else Fraction(int(x))
def integer(x):
    x=Fraction(x);assert x.denominator==1;return x.numerator
mom={k:integer(factorial(k)*rat(data['moment_states'][str(k)]['moment'])) for k in (n-1,n,n+1)}
X,Y,Z=m*mom[n],m*n*mom[n-1],2*mom[n+1]-m*mom[n]
P,Q,F=n*X+Y,n*Z+2*X-Y,2*m*(Y-2*X-(n-1)*Z)
L=1<<(m//2);hhat,ellhat=[integer(L*rat(data[key])) for key in ('tau_n','tau_n1')]
Mref=Q*hhat-P*ellhat
common=gcd(abs(F),abs(Mref));assert common
remaining=common;small=[]
def primes(bound):
    flags=bytearray(b'\x01')*(bound+1);flags[:2]=b'\x00\x00'
    for p in range(2,int(bound**.5)+1):
        if flags[p]:
            for j in range(p*p,bound+1,p):flags[j]=0
    return [i for i in range(2,bound+1) if flags[i]]
for p in primes(N):
    e=0
    while remaining%p==0:remaining//=p;e+=1
    if e:small.append([p,e])
reference_path=C/'endpoint3375_reference_filter_certificate.json'
ref=json.loads(reference_path.read_text())
prod_path=C/'endpoint3375_product_scalar_certificate.json'
prod=json.loads(prod_path.read_text())
assert ref['input_sha256']==prod['input_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
assert prod['clipped_collision_gcd']=='1'
assert ref['exclusive_divisor_before_filter']==ref['exclusive_divisor_after_defect_filter']==prod['D_large']
assert ref['V_endpoint_filters']==['1','1']
# Since gcd(D,Sigma)=1, gcd(D,Rj/gcd(Rj,Sigma))=gcd(D,Rj).
# Reuse the completed Vj=1 instead of recalculating those endpoint gcds.
Delta=[1,1];G=1
artifact={'status':'PASS','scope':'NEW I=Kref reference-alignment content at retained original3375; G and Delta values follow algebraically from completed filters',
    'n':n,'F':str(F),'M_ref':str(Mref),'alignment_gcd_all_primes':str(common),
    'alignment_small_prime_exponents':small,'I_ref_large':str(remaining),
    'I_ref_large_bits':remaining.bit_length(),'alignment_gcd_bits':common.bit_length(),
    'Delta_endpoint_large_reused':Delta,'G_intersection_large_derived':G,
    'I_ref_exactly_one':remaining==1,'G_divides_I_squared':remaining**2%G==0,
    'old_endpoint_gcds_recomputed':False,'producer_regenerated':False,
    'old_reference_filters_recomputed':False,'infinite_alignment_bound_proved':False,
    'irrationality_proved':False,'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'reference_input_sha256':hashlib.sha256(reference_path.read_bytes()).hexdigest(),
    'product_input_sha256':hashlib.sha256(prod_path.read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'endpoint3375_reference_alignment_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k not in ('F','M_ref','alignment_gcd_all_primes')}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint3375_reference_alignment_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
