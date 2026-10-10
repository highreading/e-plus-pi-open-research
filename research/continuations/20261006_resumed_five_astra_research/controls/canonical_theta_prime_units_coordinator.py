#!/usr/bin/env python3
"""NEW canonical shared-scalar congruence checks, no old producer rerun."""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent
started=time.monotonic()
def tau(n):
    return sum((Fraction(comb(n,2*k)*comb(2*k,k),1<<k) for k in range(n//2+1)),Fraction(0))
def integer(x):
    x=Fraction(x)
    assert x.denominator==1
    return x.numerator
def odd_prime_divisors(n):
    out=[]
    for p in range(3,n+1,2):
        if n%p==0 and all(p%j for j in range(2,int(p**.5)+1)):out.append(p)
    return out
def residue(x,p):
    x=Fraction(x)
    assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,p)%p
digit_tables={}
for p in (3,5,7):
    table=[residue(tau(i),p) for i in range(p)]
    assert all(table)
    digit_tables[str(p)]=table
lucas_checks=0
for p in (3,5,7):
    for n in range(241,321):
        k,value=n,1
        while k:value=value*digit_tables[str(p)][k%p]%p;k//=p
        assert residue(tau(n),p)==value
        lucas_checks+=1

auxiliary_rows=[]
for n in (15,21,33,35,45,63,75,105,147,175,195,221):
    m=n+1;nf=factorial(n)
    c=[1,-n]
    for j in range(1,2*n):
        pair=j*(2*n-j+1)
        assert pair%2==0
        c.append((j-n)*c[-1]+pair//2*c[-2])
    E=[1]
    for k in range(1,2*n+2):E.append(k*E[-1]+1)
    a={j:sum(comb(j,i)*c[i] for i in range(min(j,2*n)+1)) for j in (n-1,n,n+1)}
    u={j:sum(comb(j,i)*c[i]*E[n+j-i] for i in range(min(j,2*n)+1)) for j in (n,n+1)}
    tn,tn1=tau(n),tau(n+1)
    h,ell=integer(nf*tn),integer(nf*tn1)
    h1=integer(Fraction(m,2)*(h+ell))
    b0,b1=u[n]-E[n]*h-a[n],u[n+1]-E[n]*h1-a[n+1]
    K=h*b1-h1*b0-2*nf**3
    X,Y,Z=m*a[n],m*n*a[n-1],2*a[n+1]-m*a[n]
    P,Q,F=n*X+Y,n*Z+2*X-Y,2*m*(Y-2*X-(n-1)*Z)
    DL=m*Z*(Q*h-P*ell)-F*K
    L=1<<(m//2)
    Theta=integer(Fraction(L*DL,nf))
    congruences=[]
    for p in odd_prime_divisors(n):
        assert all(z%p==0 for z in c[1:])
        expected=4*pow(2,m//2,p)*residue(tn,p)%p
        assert Theta%p==expected
        congruences.append({'p':p,'Theta_mod_p':Theta%p,'expected_mod_p':expected})
    auxiliary_rows.append({'n':n,'original_family_member_claimed':False,'Theta_bits':abs(Theta).bit_length(),'congruences':congruences})

source=C/'endpoint3375_product_scalar_certificate.json'
data=json.loads(source.read_text())
assert data['n']==3375
Theta=int(data['Theta'])
# This is a NEW primewise observable of the retained scalar, not recomputation.
original_rows=[]
for p in (3,5):
    k,tmod=3375,1
    while k:tmod=tmod*digit_tables[str(p)][k%p]%p;k//=p
    expected=4*pow(2,1688,p)*tmod%p
    assert Theta%p==expected and expected
    original_rows.append({'p':p,'retained_Theta_mod_p':Theta%p,'expected_mod_p':expected})
artifact={'status':'PASS','scope':'NEW canonicalTheta congruences at12 auxiliary odd indices and retained original3375; no producer or denominator/gcd rerun',
    'selected_prime_digit_tables':digit_tables,
    'new_lucas_digit_product_checks':lucas_checks,'new_lucas_index_range':[241,320],
    'auxiliary_rows':auxiliary_rows,'original3375_rows':original_rows,
    'old_producer_or_denominator_repeated':False,
    'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'symbolic_all_family_congruence_independently_reviewed':False,
    'asymptotic_smoothness_disproved':False,'irrationality_proved':False,
    'elapsed_seconds':round(time.monotonic()-started,3)}
target=C/'canonical_theta_prime_units_certificate.json'
target.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k!='auxiliary_rows'}
receipt['new_auxiliary_index_count']=len(auxiliary_rows)
receipt['new_auxiliary_primewise_checks']=sum(len(r['congruences']) for r in auxiliary_rows)
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
(C/'canonical_theta_prime_units_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
