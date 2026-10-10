"""New selected scalar square division, reusing closed source receipts."""
from pathlib import Path
from math import gcd
import hashlib,json
P=Path(__file__).resolve().parent
src=P/'signed_chebyshev_source_gcd_extension_certificate.json'
old=json.loads(src.read_text())
cs=[(1,0),(-1,2)]
for j in range(1,80):
    a,b=cs[-1];pa,pb=cs[-2]
    cs.append((-2*a-4*b-pa,4*a-2*b-pb))
rows=[]
for r in old['rows']:
    n=r['N'];a,b=cs[n];pa,pb=cs[n-1]
    d=a*pb-pa*b;assert d==r['d']
    g=gcd(b,pb);assert g>0
    assert r['V']%(g*g)==0 and d%g==0
    v=r['V']//(g*g);c=gcd(r['U'],v)
    rows.append({'N':n,'b_N':b,'b_Nminus1':pb,'g_B':g,'delta':d//g,
                 'U':r['U'],'V_primitive_square':v,'actual_c':c,
                 'raw_gcd_U_V':r['gcd_U_V'],'predicted_actual_h':g*g*c})
out={'all_checks_passed':True,'network_or_keys_used':False,
     'source_receipt_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'scope':'N13..80 selected scalar square divisions only, reusing closed U/I/d values. No new complete normalization, no infinite inference.',
     'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'signed_chebyshev_primitive_source_content_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':True,'actual_c_not4':[{'N':r['N'],'g_B':r['g_B'],'actual_c':r['actual_c'],'raw_gcd_U_V':r['raw_gcd_U_V']} for r in rows if r['actual_c']!=4]}))
