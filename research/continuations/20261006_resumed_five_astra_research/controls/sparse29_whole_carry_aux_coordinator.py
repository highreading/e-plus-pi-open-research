#!/usr/bin/env python3
"""NEW sparse whole p^-7 carry on three bounded compatible auxiliary phases.
These b are not original powers. No full physical producer is claimed.
Prime-power binomial units use the classical factorial-unit decomposition.
"""
from pathlib import Path
import hashlib
import itertools
import json
from math import comb
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
C = Path(__file__).resolve().parent
start = time.monotonic()
p, mod = 29, 841
P = p**6
beta = 555087455
# Exact beta from its authoritative six low digits.
beta = sum(d*p**i for i,d in enumerate([27,28,5,28,0,20]))
assert beta == 410910916
prefix = [1]*mod
for t in range(1,mod):
    prefix[t] = prefix[t-1]*(t if t%p else 1) % mod
assert prefix[-1] == mod-1

def fact_val(n):
    total = 0
    while n:
        n //= p
        total += n
    return total

def fact_unit(n):
    result = 1
    while n:
        if (n//mod)&1:
            result = -result
        result = result*prefix[n%mod] % mod
        n //= p
    return result

def choose_parts(top, lower, with_unit=True):
    if lower<0 or lower>top:
        return None
    v = fact_val(top)-fact_val(lower)-fact_val(top-lower)
    if not with_unit:
        return v
    unit = fact_unit(top)*pow(fact_unit(lower),-1,mod)*pow(fact_unit(top-lower),-1,mod) % mod
    return v,unit

small_checks = 0
for top in list(range(90)) + [841,842,1000,2000,29**3+33]:
    lower_values = range(top+1) if top<90 else range(30)
    for lower in lower_values:
        v,u = choose_parts(top,lower)
        exact = comb(top,lower)
        assert exact % (p**v) == 0 and (exact//p**v)%mod == u
        small_checks += 1

allowed = [range(3),list(range(8))+list(range(14,29)),range(6),list(range(8))+list(range(15,29)),[0],range(21)]
lows = [sum(d*p**i for i,d in enumerate(ds)) for ds in itertools.product(*allowed)]
assert len(lows) == 191268 and len(set(lows)) == len(lows)
assert all(0<=j<beta for j in lows)
rows=[]
for high in [0,1,2]:
    b = beta+P*high
    n = 2001*b
    N = n+2
    upper_sum=2*n+b-1
    assert N%P == 186913296
    counts={}
    total=0
    cases=0
    for q in range(high+1):
        for low in lows:
            j=low+P*q
            assert j<=b-1
            v1=choose_parts(N,j,False)
            top=upper_sum-j
            lower=b-1-j
            v2=choose_parts(top,lower,False)
            v=v1+v2
            assert v>=3
            counts[str(v)]=counts.get(str(v),0)+1
            cases += 1
            if v==3:
                _,u1=choose_parts(N,j)
                _,u2=choose_parts(top,lower)
                total=(total+(u1*u2)**2)%mod
    divisible = total%p == 0
    rows.append({'C_aux':high,'b_aux':str(b),'n_aux':str(n),'is_original_power':False,
        'sparse_complete_minimal_support_cases':cases,'atom_valuation_histogram':counts,
        'whole_atom_squared_norm_div29_6_mod29_2':total,'first_divided_carry_exists':divisible,
        'whole_kappa_div29_7_mod29':total//p if divisible else None})
# The support theorem excludes every other row from this squared carry:
# a combined valuation >=4 contributes >=p^8 and vanishes after p^6 mod p^2.
# That support theorem is not independently proved by this auxiliary evaluator.
artifact={'status':'PASS','scope':'NEW whole leading-atom p^-7 carry on three finite compatible auxiliary high continuations; not original powers, not complete columns',
    'beta':beta,'base_prefix':P,'modulus':mod,'low_support_rows':len(lows),
    'outside_support_exclusion_theorem_independently_proved_here':False,
    'unit_binomial_independent_small_checks':small_checks,'cases':rows,
    'complete_physical_eta_evaluated':False,'original_power_evaluated':False,'irrationality_proved':False,
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'sparse29_whole_carry_aux_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt=dict(artifact)
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'sparse29_whole_carry_aux_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
