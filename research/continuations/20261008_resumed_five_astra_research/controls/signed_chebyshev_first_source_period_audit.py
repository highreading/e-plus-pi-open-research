"""Parent-authored complete finite residue cycles for the signed K source.

This computes ONLY U mod p, p in 7,11,13. It does not compute c unless U
is a unit, and does not recompute h/lambda/G/q or any closed source jet.
The infinite progression reduction requires the proof in the companion note.
"""
from pathlib import Path
from math import factorial, comb
import hashlib, json

OUT = Path(__file__).resolve().parent

def jet(n, p):
    a = 1
    out = []
    for r in range(p):
        out.append(a % p)
        if r:
            # Independent binomial formula; division over the integers.
            direct, rem = divmod((-1)**r * n * 2**(2*r-1) * comb(n+r-1, 2*r-1), r)
            assert rem == 0 and direct == a
        if r+1 < p:
            a, rem = divmod(-2*(n*n-r*r)*a, (r+1)*(2*r+1))
            assert rem == 0
    return out

def mul(a, b, p):
    out = [0]*p
    for i, x in enumerate(a):
        for j, y in enumerate(b[:p-i]):
            out[i+j] = (out[i+j]+x*y) % p
    return out

def source_u(n, p):
    t = [1, -1]+[0]*(p-2)
    omt = [0, 1]+[0]*(p-2)
    one_t2 = mul(t, t, p)
    one_t2[0] += 1
    H = mul(mul(t, omt, p), mul(one_t2, one_t2, p), p)
    C = jet(n-3, p)
    K = mul(H, mul(C, C, p), p)
    return -sum(K[r]*(-1)**r*factorial(r) for r in range(p)) % p

records = []
for p in (7, 11, 13):
    modulus = p*p
    residue = pow(9, 18, modulus)
    start = residue
    step = pow(9, 32, modulus)
    cycle = []
    seen = set()
    while residue not in seen:
        assert len(cycle) < p*(p-1)
        seen.add(residue)
        n = residue+modulus
        # Check one shift using both fully paid integer coefficient formulas.
        assert jet(n-3,p) == jet(n-3+modulus,p)
        u = source_u(n,p)
        cycle.append({'u_residue_class':len(cycle),'N_mod_p_squared':residue,
                      'U_mod_p':u})
        residue = residue*step % modulus
    assert residue == start
    records.append({'p':p,'N_modulus':modulus,'start':start,'step':step,
                    'cycle_length':len(cycle),'complete_cycle':True,
                    'all_U_units':all(item['U_mod_p'] for item in cycle),
                    'U_zero_positions':[item['u_residue_class'] for item in cycle if not item['U_mod_p']],
                    'records':cycle})
    print(json.dumps({key:records[-1][key] for key in
          ('p','cycle_length','all_U_units','U_zero_positions')}),flush=True)

obj = {'checks_passed':True,'scope':'Complete N mod p^2 residue cycles for U mod p only. Infinite reduction has a separate elementary proof; no all-prime or primitive-q theorem.',
       'records':records,'network_or_keys_used':False,'h_lambda_G_q_computed':False,
       'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'signed_chebyshev_first_source_period_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
