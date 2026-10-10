"""Coordinator-authored new forced recurrence; reuse preserved n225 producer."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb, gcd
from functools import reduce
import hashlib, json, time
from endpoint_actual_frame_content_audit import rational, integer, det, matvec, inverse_boundary, smallprimes

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parents[1]/'astra_pro5_resume_20261006/controls/complete_endpoint_225_certificate.json'

def vp(value, p):
    value = abs(integer(value))
    assert value != 0
    v = 0
    while value % p == 0:
        value //= p
        v += 1
    return v

def main():
    started = time.monotonic()
    saved = json.loads(SOURCE.read_text())
    n = int(saved['n'])
    assert n == 225
    N, m, K = n+2, n+1, 2*n+2
    T = [[rational(x) for x in row] for row in saved['T']]
    J = [[integer(factorial(N)*x) for x in row] for row in T]
    Delta = det(J)
    u, v = ([rational(x) for x in saved[name]] for name in ('u', 'v'))
    xx, yy = inverse_boundary(u, n), inverse_boundary(v, n)
    H = [integer(F(x, factorial(n))) for x in matvec(J, xx)]
    Bsrc = matvec(J, [yy[0]-1, yy[1], yy[2]])
    En = sum(factorial(n)//factorial(k) for k in range(n+1))
    C = [integer(x-En*y) for x, y in zip(Bsrc, H)]
    alpha = [F(1), F(1)]
    for k in range(2, n+1):
        alpha.append(alpha[-1]-alpha[-2]/2)
    epsilon = [F(1)]
    z = [F(0)]
    forcing = []
    for l in range(N):
        e1, e2 = (epsilon[l-1] if l >= 1 else F(0)), (epsilon[l-2] if l >= 2 else F(0))
        epsilon.append(((l-n)*epsilon[l]+F(2*n-l+1, 2)*e1+e2/2)/(l+1))
        rl = F(factorial(n)*((-1)**l)*comb(n+1, l), 2**l)*alpha[n-l] if l <= n else F(0)
        forcing.append(rl)
        z1, z2 = (z[l-1] if l >= 1 else F(0)), (z[l-2] if l >= 2 else F(0))
        z.append(((2*l+1)*z[l]+F(2*n+1-3*l, 2)*z1
                  +F(l-n-1, 2)*z2+epsilon[l]+2*rl)/(l+1))
    Z = [integer(factorial(N)*z[k]) for k in (n, n+1, n+2)]
    lam = 2*factorial(n)*sum((alpha[k-1]/k for k in range(1, n+1)), F(0))
    assert [lam*h+zz-J[i][0] for i, (h, zz) in enumerate(zip(H, Z))] == C
    an = factorial(n)*T[0][0]
    an1 = factorial(n-1)*T[0][1]
    anplus = factorial(n+1)*T[1][0]
    X, Y, ZZ = m*an, m*n*an1, 2*anplus-m*an
    P, Qv = n*X+Y, n*ZZ+2*X-Y
    Fpay = integer(2*m*(ZZ-Qv))
    a, b, c = J[0]
    dd, aa, bb = J[1]
    e, ddd, aaa = J[2]
    assert aa == aaa == a and bb == b and ddd == dd
    t3 = [dd*dd-a*e, b*e-a*dd, a*a-b*dd]
    t0 = [-(a*a-b*dd)+n*(b*e-a*dd)-n*m*t3[0],
          -(c*dd-a*b)+n*(a*a-c*e)-n*m*t3[1],
          -(b*b-a*c)+n*(c*dd-a*b)-n*m*t3[2]]
    rows = []
    for label, raw in ((0, t0), (3, t3)):
        content = reduce(gcd, (abs(x) for x in raw), 0)
        row = [x//content for x in raw]
        Rj = integer(sum(x*y for x, y in zip(row, H)))
        Cj = integer(sum(x*y for x, y in zip(row, C)))
        Xi = integer(sum(x*(zz-J[i][0]) for i, (x, zz) in enumerate(zip(row, Z))))
        assert Cj == lam*Rj+Xi
        if label == 0:
            assert Xi == integer(F(sum(x*y for x, y in zip(raw, Z))+Delta, content))
        else:
            assert Xi == integer(F(sum(x*y for x, y in zip(raw, Z)), content))
        rows.append({'endpoint': label, 'kernel_content': content, 'R': Rj, 'C': Cj, 'Xi': Xi})
    band = [p for p in smallprimes(K) if p > N]
    records, loss = [], 1
    for p in band:
        ps = []
        for row in rows:
            vv = {name: vp(row[name], p) for name in ('kernel_content', 'R', 'C', 'Xi')}
            f = vp(Fpay, p)
            depth = min(max(vv['R']-f, 0), vv['C'])
            predicted = min(max(vv['R']-f, 0), vv['Xi'])
            assert depth == predicted
            ps.append({'endpoint': row['endpoint'], 'v_p_F': f, **vv,
                       'paid_contact_depth': depth})
        loss *= p**max(v['paid_contact_depth'] for v in ps)
        records.append({'p': p, 'endpoints': ps})
    full = {'authorship': 'Coordinator; no remote code executed',
            'scope': 'One ORIGINAL n225 and the complete finite prime band227<p<=452 only. No infinite contact/acquisition/primitive-error theorem.',
            'input_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'n': n, 'forced_recurrence_positions': len(z),
            'complete_source_identity_residuals_zero': True,
            'both_saturated_endpoint_residuals_zero': True,
            'endpoint0_exterior_Delta_term_retained': True,
            'exact_valuations_by_prime': records, 'contact_loss_product': str(loss),
            'seconds': round(time.monotonic()-started, 4)}
    p = OUT/'endpoint_actual_forced_contact_certificate.json'
    p.write_text(json.dumps(full, indent=2)+'\n')
    receipt = {k: v for k, v in full.items() if k != 'exact_valuations_by_prime'}
    receipt.update({'band_prime_count': len(band), 'positive_contacts':
                    [{'p': a['p'], 'endpoint': e['endpoint'], 'depth': e['paid_contact_depth']}
                     for a in records for e in a['endpoints'] if e['paid_contact_depth']],
                    'full_certificate_sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    (OUT/'endpoint_actual_forced_contact_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
