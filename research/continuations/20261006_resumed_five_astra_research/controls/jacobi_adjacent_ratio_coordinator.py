#!/usr/bin/env python3
"""Independent new audit of the adjacent-polynomial normalization."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def general(alpha,k):
    out = F(1)
    for r in range(k):
        out = out*(alpha-r)/(r+1)
    return out

def polynomial(m,degree):
    out = [F(0)]*(degree+1)
    A = 2*m-1
    for k in range(degree+1):
        scalar = comb(degree+A,k)*general(F(2*degree-1,2),degree-k)
        for e in range(degree-k+1):
            out[k+e] += scalar*comb(degree-k,e)*(-1)**(degree-k-e)
    return out

def main():
    rows = []
    checks = 0
    for m in (1,2,3,4,5,8,11,16,23,32):
        c,d = polynomial(m,m),polynomial(m,m-1)+[F(0)]
        failures = 0
        for i in range(m+1):
            corrected = -F(6*(m-i),6*m+2*i-3)
            claimed = -F(3*(m-i),6*m+2*i-3)
            assert d[i] == corrected*c[i]
            failures += d[i] != claimed*c[i]
            if i:
                assert c[i]/c[i-1] == F((i-1-m)*(6*m+2*i-3),i*(2*i-1))
            checks += 1
        ratio = d[0]/c[0]
        rows.append({'m':m,'corrected_all_coefficients_verified':True,
                     'reported_ratio_fails_nonzero_coefficients':failures,
                     'constant_ratio':str(ratio),'corrected_constant_ratio':str(-F(2*m,2*m-1)),
                     'reported_constant_ratio':str(-F(m,2*m-1))})
    cert = {'status':'PASS_WITH_REPORT_CORRECTION',
            'scope':'Exact bounded normalization audit, no original-window inverse evaluation',
            'corrected_identity':'d_i/c_i=-6(m-i)/(6m+2i-3)',
            'reported_identity':'d_i/c_i=-3(m-i)/(6m+2i-3)',
            'impact':'Factor2 propagates to R_i and all evaluated collision minors; structural multiplication identity remains valid',
            'rows':rows,'coefficient_checks':checks}
    target = ROOT/'jacobi_adjacent_ratio_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {k:v for k,v in cert.items() if k!='rows'}
    receipt.update({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                    'm2_constant_actual':'-4/3','m2_constant_reported':'-2/3'})
    (ROOT/'jacobi_adjacent_ratio_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
