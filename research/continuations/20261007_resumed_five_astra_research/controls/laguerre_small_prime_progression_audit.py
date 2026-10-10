"""Parent-authored bounded modular table, not an original huge matrix surrogate."""
from pathlib import Path
import json, math

OUT=Path(__file__).with_name('laguerre_small_prime_progression_certificate.json')
K0=249005515
K1=574312172
STEP=29**9
primes=[p for p in range(2,98) if all(p%q for q in range(2,math.isqrt(p)+1))]
rows=[]
tests=0
for p in primes:
    if p==3:
        rows.append({'prime':3,'period':1,'excluded_t_residues':[],
                     'reason':'h=2000*3^K+1 is identically 1 modulo3.'})
        continue
    order=next(j for j in range(1,p) if pow(3,j,p)==1)
    period=order//math.gcd(order,K1*STEP)
    base=(K0+2*K1)%order
    delta=(K1*STEP)%order
    residues=[]
    for t in range(period):
        tests+=1
        exponent=(base+delta*t)%order
        if (2000*pow(3,exponent,p)+1)%p==0:
            residues.append(t)
    assert period<=96
    rows.append({'prime':p,'order_of_3':order,'period':period,
                 'excluded_t_residues':residues})

assert tests<25*96
r19=next(row for row in rows if row['prime']==19)
assert r19['period']==9 and r19['excluded_t_residues']==[0]

nonempty=[r for r in rows if r['excluded_t_residues']]
combined_period=math.lcm(*(r['period'] for r in nonempty))
# A verified surviving congruence witnesses that these SMALL-prime exclusions
# do not cover the original t-domain. This bounded search does not claim an
# exhaustive enumeration of a potentially much larger combined period.
survivor=None
for t in range(10000):
    if all(t%r['period'] not in r['excluded_t_residues'] for r in nonempty):
        survivor=t
        break
assert survivor is not None, 'No survivor in bounded search; not a covering proof.'
assert all((2000*pow(3,(K0+2*K1+K1*STEP*survivor)%(p-1),p)+1)%p
           for p in primes if p!=3)

result={
 'status':'PASS',
 'scope':'Exact small-prime congruences of the ORIGINAL u=2+29^9*t progression, '
         'not an original huge Laguerre-matrix calculation or a global decay proof.',
 'primes':primes,'modular_tests':tests,'rows':rows,
 'combined_period_of_nonempty_exclusions':combined_period,
 'verified_surviving_t_residue':survivor,
 'surviving_t_progression_modulus':combined_period,
 'survivor_scope':'Every t congruent to this residue modulo the displayed modulus '
                  'avoids all prime divisors<=97 of h; no claim about larger primes '
                  'or unstated additional admissibility conditions.',
 'request_is_bounded':'At most25*96 modular evaluations plus10000*25 residue tests; '
                      'primes<=97, modular exponents<=95. No network/key reads.'
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','modular_tests',
 'combined_period_of_nonempty_exclusions','verified_surviving_t_residue')}))
print(json.dumps({'nonempty_exclusions':nonempty}))
