"""Two new scalar gcds from the CLOSED11-to12 determinant receipt, no determinants."""
from pathlib import Path
from math import gcd
import json,hashlib
P=Path(__file__).resolve().parent
source=P/'paid_schur_support_certificate.json'
d=json.loads(source.read_text())
def egcd(a,b):
    old,r=abs(a),abs(b);x,xx=1,0;y,yy=0,1
    while r:
        q=old//r;old,r=r,old-q*r;x,xx=xx,x-q*xx;y,yy=yy,y-q*yy
    return old,x*(1 if a>=0 else -1),y*(1 if b>=0 else -1)
alpha,beta,chi=(int(d[k]) for k in ['alpha','beta','chi'])
Ar=int(d['alpha_residual_after_all_primes_le67']);Cr=int(d['chi_residual_after_all_primes_le67'])
assert gcd(abs(alpha),chi)==1
rows=[]
for name,res,k in [('chi_residual',Cr,11),('alpha_residual',Ar,12)]:
    g,x,y=egcd(res,beta);assert x*res+y*beta==g
    content=int(d[f'original_content_{k}'])
    assert gcd(res,content)==g
    dets={x['label']:int(x['determinant']) for x in d['determinant_certificates']}
    H1=dets[f'original_{k}_s1']-dets[f'original_{k}_s0']
    assert abs(H1)%content==0
    q=abs(H1)//content
    assert q%(res//g)==0
    rows.append({'residual_name':name,'original_k':k,'residual':str(res),'beta':str(beta),
        'new_scalar_gcd':str(g),'bezout':[str(x),str(y)],
        'gcd_with_actual_closed_content':str(gcd(res,content)),
        'actual_q_surviving_divisor':str(res//g),'actual_q_from_closed_receipt':str(q),
        'surviving_divisor_digits':len(str(res//g))})
out={'all_checks_passed':True,'scope':'NEW two scalar gcds at AUXILIARY paid compact11-to12 only; no uniform or original-index support conclusion.',
     'closed_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'determinants_or_Smith_tables_recomputed':False,'network_or_credentials_used':False,
     'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'paid_schur_scalar_splitting_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks_passed':True,'rows':[{'k':r['original_k'],'gcd':r['new_scalar_gcd'],
        'surviving_divisor_digits':r['surviving_divisor_digits']} for r in rows]}))
