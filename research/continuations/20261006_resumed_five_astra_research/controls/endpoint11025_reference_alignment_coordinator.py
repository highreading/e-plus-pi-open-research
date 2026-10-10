#!/usr/bin/env python3
"""NEW original105^2 reference/moment alignment only, no force producer."""
from pathlib import Path
from math import gcd
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(60,60))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent;start=time.monotonic()
n=105**2;m=n+1;N=n+2
# q A'=(q+nq')A for A=e^z(1-z+z^2/2)^n; a_k=k![z^k]A.
states=[0,0,1];moment={}
for k in range(n+1):
    if k in (n-1,n):moment[k]=states[-1]
    a2,a1,a0=states
    c1=k*(2*n-k-1);c2=k*(k-1)
    assert c1%2==c2%2==0
    nxt=(k+1-n)*a0+(c1//2)*a1+(c2//2)*a2
    states=[a1,a0,nxt]
moment[n+1]=states[-1]
# T_k=2^floor(k/2)*tau_k integral by the explicit constant-term sum.
# (k+1)tau_(k+1)=(2k+1)tau_k+k tau_(k-1).
before,current=1,1
reference={0:1,1:1}
for k in range(1,n+1):
    numerator=(2 if k%2 else 1)*(2*k+1)*current+2*k*before
    nxt,remainder=divmod(numerator,k+1);assert remainder==0
    before,current=current,nxt
    if k+1 in (n,n+1):reference[k+1]=nxt
assert n%2==1
hhat,ellhat=2*reference[n],reference[n+1]
X,Y,Z=m*moment[n],m*n*moment[n-1],2*moment[n+1]-m*moment[n]
P,Q,F=n*X+Y,n*Z+2*X-Y,2*m*(Y-2*X-(n-1)*Z)
Mref=Q*hhat-P*ellhat
common=gcd(abs(F),abs(Mref));assert common
remaining=common;small=[]
sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
for p in range(2,int(N**.5)+1):
    if sieve[p]:
        for j in range(p*p,N+1,p):sieve[j]=0
for p in range(2,N+1):
    if not sieve[p]:continue
    e=0
    while remaining%p==0:remaining//=p;e+=1
    if e:small.append([p,e])
artifact={'status':'PASS','scope':'NEW original105^2=11025 reference-alignment content only; no force, contact, endpoint gcd, denominator or error calculated',
    'n':n,'n_family':'105^2','moments':{str(k):str(v) for k,v in moment.items()},
    'hhat':str(hhat),'ellhat':str(ellhat),'F':str(F),'M_ref':str(Mref),
    'alignment_gcd_all_primes':str(common),'alignment_small_prime_exponents':small,
    'I_ref_large':str(remaining),'I_ref_large_bits':remaining.bit_length(),
    'alignment_gcd_bits':common.bit_length(),'moment_bits':[abs(moment[k]).bit_length() for k in sorted(moment)],
    'reference_bits':[abs(hhat).bit_length(),abs(ellhat).bit_length()],
    'complete_force_calculated':False,'contact_rows_calculated':False,
    'old_producer_regenerated':False,'primitive_denominator_calculated':False,
    'whole_error_calculated':False,'infinite_alignment_bound_proved':False,
    'irrationality_proved':False,'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'endpoint11025_reference_alignment_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k not in ('moments','hhat','ellhat','F','M_ref','alignment_gcd_all_primes')}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint11025_reference_alignment_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
