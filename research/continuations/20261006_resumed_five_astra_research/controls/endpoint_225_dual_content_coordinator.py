#!/usr/bin/env python3
"""Bounded post-processing of existing n225 data; no producer regenerated."""
from math import gcd
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(100000)

def primes(limit):
    result=[]
    for a in range(2,limit+1):
        if all(a%p for p in result if p*p<=a):
            result.append(a)
    return result

def main():
    source=ROOT/'complete_endpoint_225_certificate.json'
    data=json.loads(source.read_text())
    L,t0,t1,r0,r1,Omega=(int(data[k]) for k in ('L','t0','t1','r0','r1','Omega'))
    Gt=gcd(t0,t1)
    Ored=abs(Omega)//gcd(abs(Omega),Gt*Gt)
    rows=[]
    ps=primes(226)
    def large_part(x):
        x=abs(x)
        assert x
        for p in ps:
            while x%p==0:
                x//=p
        return x
    for j in ('0','3'):
        d=data['endpoints'][j]
        X,V,M,gam,E,aa,bb,gs,Rzero=(int(d[k]) for k in ('X','V','M','gamma','Ecoef','a_primitive','b_primitive','content','R_cancel'))
        Rone=t1*L*E-Omega*gam*aa
        Csharp=gcd(abs(X),abs(Rzero),abs(Rone))
        Ksharp=gam*abs(X)//Csharp
        assert t0*V-r0*M==Rzero and t1*V-r1*M==Rone
        assert Csharp==gcd(abs(X),abs(Gt*V))
        assert (L*Csharp)%gs==0 and (Gt*gs)%Csharp==0
        assert large_part(int(d['denominator']))==large_part(Ksharp)
        rows.append({'endpoint':j,'R1':str(Rone),'C_sharp':str(Csharp),'K_sharp':str(Ksharp),
                     'gamma_large':str(large_part(gam)), 'C_sharp_large':str(large_part(Csharp)),
                     'gamma_large_digits':len(str(large_part(gam))),
                     'C_sharp_large_digits':len(str(large_part(Csharp))),
                     'C_sharp_large_is_one':large_part(Csharp)==1,
                     'gamma_large_is_one':large_part(gam)==1})
    K0,K3=(int(r['K_sharp']) for r in rows)
    Zsharp=K0*K3//gcd(K0,K3)**2
    AB,ZX=int(data['AB']),int(data['Z_X'])
    qdelta=int(data['kappa_difference']['denominator'])
    assert (Ored*qdelta)%ZX==0
    assert (L*Gt*AB)%Zsharp==0 and (L*Gt*Zsharp)%AB==0
    ABlarge,Zlarge=large_part(AB),large_part(Zsharp)
    assert ABlarge==Zlarge
    from fractions import Fraction
    u=[Fraction(int(v['numerator']),int(v['denominator'])) for v in data['u']]
    v=[Fraction(int(z['numerator']),int(z['denominator'])) for z in data['v']]
    assert sum(u)==0 and sum(v)==1
    artifact={'n':225,'G_t':str(Gt),'Omega_reduced':str(Ored),'rows':rows,
              'Z_K_sharp':str(Zsharp),'AB_large_prime_part':str(ABlarge),
              'large_prime_cutoff':226,'AB_large_prime_part_digits':len(str(ABlarge))}
    target=ROOT/'endpoint_225_dual_content_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt={'status':'PASS','scope':'Existing original n225 data, dual-Wronskian content and exact prime part above226; no family theorem',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'producer_artifact_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'AB_large_prime_part_digits':len(str(ABlarge)),
             'endpoint_content_summary':[{k:z[k] for k in ('endpoint','gamma_large_digits','C_sharp_large_digits','gamma_large_is_one','C_sharp_large_is_one')} for z in rows],
             'prime_part_equality_above226':True,'sharper_difference_divisor_verified':True,
             'all_five_divisibilities_verified':True,'full_reconstruction_sums_verified':True}
    (ROOT/'endpoint_225_dual_content_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
