"""Parent-authored finite trial division; no new determinant or network."""
from pathlib import Path
from math import isqrt, gcd
import hashlib, json, sys

sys.set_int_max_str_digits(500000)
OUT = Path(__file__).resolve().parent
SOURCES = [
    OUT.parents[1]/'astra_pro5_resume_20261007'/'controls'/'compact_k32_content_envelope_certificate.json',
    OUT/'compact_k33_content_envelope_certificate.json',
]

def is_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def valuation(n,p):
    assert n>0 and is_prime(p)
    exponent=0
    while n%p==0:
        n//=p
        exponent+=1
    return exponent

rows=[]
for path in SOURCES:
    data=path.read_bytes()
    c=json.loads(data)
    k=c['k']
    p,q=int(c['primitive_p']),int(c['primitive_q'])
    G,H1=int(c['G']),int(c['H1'])
    assert gcd(abs(p),q)==1 and q==abs(H1)//G
    table=[{'prime':r,'q_valuation':valuation(q,r),
            'H1_valuation':valuation(abs(H1),r),'G_valuation':valuation(G,r)}
           for r in range(2*k+1,6*k-4) if is_prime(r)]
    assert all(t['q_valuation']==t['H1_valuation']-t['G_valuation'] for t in table)
    missing=[t['prime'] for t in table if t['q_valuation']==0]
    retained=1
    for t in table:retained*=t['prime']**t['q_valuation']
    assert q%retained==0
    rows.append({'k':k,'source':str(path),'source_sha256':hashlib.sha256(data).hexdigest(),
                 'q_decimal_digits':len(str(q)),'interval':'2k < p <= 6k-5',
                 'prime_valuations':table,'missing_primes':missing,
                 'every_interval_prime_retained_at_this_index':not missing,
                 'actual_retained_interval_factor':str(retained)})
result={'parent_authored':True,'all_checks_passed':True,
        'scope':'Only certified actual compact denominators at32 and33; no eventual conclusion.',
        'network_or_credentials_used':False,'indices':rows}
(OUT/'compact_prime_interval_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
