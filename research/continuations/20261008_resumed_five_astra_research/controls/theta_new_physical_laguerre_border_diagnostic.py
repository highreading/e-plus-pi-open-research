"""NEW physical-base Gram and complete reflected-border checks.

Reuse CLOSED r0..32 Laguerre coordinate rows; do not reconstruct them.
All checks are auxiliary, distinct from actual original-sized pivots.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, time

H = Path(__file__).resolve().parent
OUT = H / 'THETA_NEW_PHYSICAL_LAGUERRE_BORDER_RECEIPT.json'
assert not OUT.exists()
start = time.monotonic()
cache = H / 'THETA_DIVIDED_LAGUERRE_COORDINATE_RECEIPT.json'
old = json.loads(cache.read_text())
rows = [[Fraction(*c) for c in row] for row in old['coordinate_rows']]
assert old['all_checked_coordinates_integral']
assert all(c.denominator == 1 for row in rows for c in row)
rows = [[c.numerator for c in row] for row in rows]

def multiply_x(v):
    out = [0] * (len(v) + 1)
    for j, c in enumerate(v):
        out[j] -= 2*j*c
        out[j+1] += (j+1)*c
        if j:
            out[j-1] += j*c
    return out

der = [1, 0]
for j in range(2, 97):
    der.append((j-1)*(der[-1] + der[-2]))
physical = []
for s in range(9):
    v = rows[s]
    for m in range(1, 9):
        v = multiply_x(multiply_x(v))
        for r in range(9):
            got = sum(a*b for a,b in zip(v, rows[r]))
            k = r+s
            theta = Fraction(sum(math.comb(k,a)*(-1)**(k-a)*der[2*(m+a)]
                                 for a in range(k+1)), (1 << k)*math.factorial(k))
            expected = math.comb(k,r)*theta
            assert expected.denominator == 1 and got == expected
            physical.append([r,s,m,got])

reflection = []
for m in range(65):
    direct = sum((Fraction((-1)**(j+k)*math.comb(m,j)*math.comb(j,k)*math.factorial(k),
                           math.factorial(j))
                  for j in range(m+1) for k in range(j+1)), Fraction())
    beta = sum((Fraction(math.comb(m,j)*der[j],math.factorial(j))
                for j in range(m+1)), Fraction())
    assert direct == beta
    cleared = beta*math.factorial(m)
    assert cleared.denominator == 1 and cleared.numerator % 2 == 1
    reflection.append([m,beta.numerator,beta.denominator,cleared.numerator])

border = []
for r in range(33):
    F = sum(math.comb(r,j)*(-1)**(r-j)*math.factorial(2*j) for j in range(r+1))
    assert F % 2 == 1
    gamma = Fraction(F,(1 << r)*math.factorial(r))
    via_laguerre = sum((Fraction(c)*Fraction(reflection[m][1],reflection[m][2])
                        for m,c in enumerate(rows[r])), Fraction())
    assert gamma == via_laguerre
    # Exact integer division of [(z-1)^r-(-2)^r] by z+1.
    p = [math.comb(r,j)*(-1)**(r-j) for j in range(r+1)]
    p[0] -= (-2)**r
    quotient = [0] * r
    for j in range(r,0,-1):
        quotient[j-1] = p[j]
        p[j] = 0
        p[j-1] -= quotient[j-1]
    assert p == [0]*(r+1)
    reciprocal = sum((Fraction(c,2*j+1) for j,c in enumerate(quotient)), Fraction())
    clearer = math.lcm(*range(1,max(2*r,2),2))
    A = reciprocal*clearer
    assert A.denominator == 1
    kappa = -clearer*F + 4*A.numerator
    assert kappa % 2 == 1
    border.append([r,F,clearer,A.numerator,kappa,gamma.numerator,gamma.denominator])

receipt = {
 'time': time.strftime('%Y-%m-%d %H:%M:%S'),
 'scope': 'NEW auxiliary physical x^(2m) Gram and reflected COMPLETE border only; no original family pivot, pair upper or primitive-error claim',
 'coordinator_authored': True, 'network_and_credentials_denied_by_sandbox': True,
 'closed_coordinate_cache_reused_not_recomputed': True,
 'coordinate_cache_sha256': hashlib.sha256(cache.read_bytes()).hexdigest(),
 'new_physical_cases': len(physical), 'physical_m_range': [1,8],
 'contact_r_s_range': [0,8], 'all_new_physical_Gram_identities_pass': True,
 'reflection_Laguerre_m_range': [0,64], 'all_reflection_odd_numerator_identities_pass': True,
 'divided_y_complete_border_r_range': [0,32], 'all_gamma_reflection_and_complete_border_unit_checks_pass': True,
 'physical_cases': physical, 'reflection_cases': reflection, 'complete_border_cases': border,
 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'seconds': round(time.monotonic()-start,3)
}
OUT.write_text(json.dumps(receipt,indent=2) + '\n')
print(json.dumps({k:v for k,v in receipt.items() if not k.endswith('_cases')}))
