#!/usr/bin/env python3
"""New exact post-processing of the archived n225 force; no regeneration."""
from fractions import Fraction as F
from math import factorial, gcd
from pathlib import Path
import hashlib
import json
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
sys.set_int_max_str_digits(100000)
ROOT = Path(__file__).resolve().parent

def rational(x):
    return F(int(x['numerator']), int(x['denominator']))

def integer(x):
    x = F(x)
    assert x.denominator == 1
    return x.numerator

def egcd(a, b):
    a0, b0 = a, b
    x, y, xx, yy = 1, 0, 0, 1
    while b:
        q, rr = divmod(a, b)
        a, b = b, rr
        x, xx = xx, x-q*xx
        y, yy = yy, y-q*yy
    if a < 0:
        a, x, y = -a, -x, -y
    assert a0*x+b0*y == a
    return a, x, y

def primes(limit):
    ps = []
    for x in range(2, limit+1):
        if all(x%p for p in ps if p*p <= x):
            ps.append(x)
    return ps

def strip_small(x, limit=226):
    x = abs(x)
    assert x
    for p in primes(limit):
        while x%p == 0:
            x //= p
    return x

def supported_part(x, z):
    x, z = abs(x), abs(z)
    assert x and z
    out = 1
    while (g := gcd(x, z)) > 1:
        x //= g
        out *= g
    return out

def main():
    producer = ROOT/'complete_endpoint_225_certificate.json'
    d = json.loads(producer.read_text())
    dual = json.loads((ROOT/'endpoint_225_dual_content_certificate.json').read_text())
    n = int(d['n'])
    assert n == 225
    T = [[rational(z) for z in row] for row in d['T']]
    Delta = rational(d['detT'])
    b, c, dd = T[0][1], T[0][0], T[1][0]
    Z = b+(n-3)*c-2*(n-1)*dd
    row0, row3 = (d['endpoints'][j] for j in ('0','3'))
    a0, a3 = (rational(z['alpha']) for z in (row0,row3))
    b0, b3 = (rational(z['beta']) for z in (row0,row3))
    e0, e3 = (rational(z['Nexp']) for z in (row0,row3))
    determinant = a0*b3-b0*a3
    assert Z and determinant
    assert 2*(n+2)*determinant == (n+1)*Delta*Z
    # Recover the common force coordinates from ALREADY archived endpoints.
    P = Z*(e0*b3-e3*b0)/determinant
    Q = Z*(a0*e3-a3*e0)/determinant
    assert Z*e0 == a0*P+b0*Q and Z*e3 == a3*P+b3*Q
    D = (1<<n)*factorial(n+1)
    Z0, P0, Q0 = integer(D*Z), integer(D*D*P), integer(D*D*Q)
    B = factorial(n)*D*Z0
    L, t0, t1, r0, r1, Omega = (int(d[k]) for k in ('L','t0','t1','r0','r1','Omega'))
    U, W = B*r0+L*P0, B*r1+L*Q0
    resultant = t0*W-t1*U
    assert resultant == B*Omega+L*(t0*Q0-t1*P0) and resultant
    Gt, s, t = egcd(t0,t1)
    results = []
    for j, row, dualrow in zip(('0','3'),(row0,row3),dual['rows']):
        gam, aa, bb, E, X, V, R0 = (int(row[k]) for k in ('gamma','a_primitive','b_primitive','Ecoef','X','V','R_cancel'))
        R1 = t1*L*E-Omega*gam*aa
        Csharp = gcd(abs(X),abs(R0),abs(R1))
        assert Csharp == int(dualrow['C_sharp'])
        assert B*E == gam*(aa*P0+bb*Q0) and B%gam == 0
        flat = B//gam
        assert flat*V == aa*U+bb*W
        one, lam, mu = egcd(aa,bb)
        assert one == 1
        cj = mu*t0-lam*t1
        cx = Gt*(lam*W-mu*U)+cj*B*(s*r0+t*r1)
        cr0, cr1 = cj*flat*s, cj*flat*t
        assert cx*X+cr0*R0+cr1*R1 == Gt*resultant
        assert (Gt*resultant)%Csharp == 0
        Xlarge = strip_small(X)
        exceptional = supported_part(Xlarge, Z0)
        away = Xlarge//exceptional
        Cexceptional = supported_part(strip_small(Csharp), Z0)
        Caway = strip_small(Csharp)//Cexceptional
        # Exact common-resultant law for all primes away from B, collectively.
        assert Caway == gcd(away,strip_small(resultant))
        gamma_large = strip_small(gam)
        assert strip_small(Z0)%gamma_large == 0
        results.append({'endpoint':j,'C_sharp':str(Csharp),
                        'gamma_large':str(gamma_large),
                        'X_large_exceptional_support':str(exceptional),
                        'X_large_away_exceptional':str(away),
                        'C_sharp_large_exceptional_support':str(Cexceptional),
                        'C_sharp_large_away_exceptional':str(Caway),
                        'gcd_X_large_F_large':str(gcd(Xlarge,strip_small(resultant))),
                        'bezout_coefficients':[str(cx),str(cr0),str(cr1)],
                        'bezout_residual':'0'})
    # A3's specialized defect bounds, retaining its slightly larger cutoff.
    Bpartial0, Bpartial3 = 6*dd-(n+6)*c, 2*(n+2)*dd-(n+3)*c
    Pn = n*n+5*n+3
    assert (n+2)*Bpartial0-3*Bpartial3 == -Pn*c
    Dmom = (1<<n)*factorial(n+2)
    z_mom = integer(Dmom*Z)
    defects = [gcd(abs(z_mom),abs(integer(Dmom*x))) for x in (Bpartial0,Bpartial3)]
    U0, U3 = (strip_small(x,227) for x in defects)
    gamma0, gamma3 = (strip_small(int(z['gamma']),227) for z in (row0,row3))
    assert U0%gamma0 == 0 and U3%gamma3 == 0
    assert strip_small(Pn,227)%gcd(U0,U3) == 0
    assert strip_small(Pn*abs(Z.numerator),227)%(gamma0*gamma3) == 0
    artifact = {'n':n,'producer_artifact_sha256':hashlib.sha256(producer.read_bytes()).hexdigest(),
                'scope':'New specialized identities on archived original n225, not a family theorem',
                'Z':{'numerator':str(Z.numerator),'denominator':str(Z.denominator)},
                'D':str(D),'Z0':str(Z0),'P0':str(P0),'Q0':str(Q0),'B':str(B),
                'F_resultant':str(resultant),'Z0_large':str(strip_small(Z0)),
                'F_large':str(strip_small(resultant)),'rows':results,
                'A3_defect_gcds_large_cutoff227':[str(U0),str(U3)],
                'no_producer_or_force_regenerated':True}
    target = ROOT/'endpoint_225_specialized_resultant_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt = {'status':'PASS','n':n,'scope':artifact['scope'],
               'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'producer_artifact_sha256':artifact['producer_artifact_sha256'],
               'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
               'force_and_determinant_identities_zero_residual':True,
               'integer_bezout_identities_zero_residual':True,
               'large_prime_common_resultant_law_verified':True,
               'A3_specialized_defect_divisibilities_verified':True,
               'Z0_large_digits':len(str(strip_small(Z0))),
               'F_large_digits':len(str(strip_small(resultant))),
               'endpoint_gcd_X_large_F_large':[r['gcd_X_large_F_large'] for r in results],
               'X_exceptional_support_digits':[len(r['X_large_exceptional_support']) for r in results],
               'no_producer_or_force_regenerated':True,'irrationality_proved':False}
    (ROOT/'endpoint_225_specialized_resultant_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    main()
