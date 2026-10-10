"""Parent new finite digit audit of A2 turn3's analytic branch inequalities.
This does not repeat the old full atom dictionary or scalar pairing computation.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parent;start=time.monotonic();p=29
def events(l0,l1,v,alpha):
    low=(5044+v)%(p*p);b0=low%p;b1=low//p
    a=(16384+alpha)%(p*p);a0=a%p;a1=a//p
    w0=int(l0>2);w1=int(l1+w0>7)
    borrow=int(l0>b0);k0=(b0-l0)%p;k1=(b1-l1-borrow)%p
    c0=int(a0+k0>=p);c1=int(a1+k1+c0>=p)
    return w0+w1+c0+c1
def lucas_zero(l0,l1,degree):
    return degree%p>l0 or degree//p>l1
results=[];count=0
for alpha in (0,29):
    for v in (0,1,2):
        minimum=10
        for l0 in range(p):
            for l1 in range(p):
                e=events(l0,l1,v,alpha)
                if v==2:e+=(0 if l0 else (1 if l1 else 2))
                minimum=min(minimum,e);count+=1
                assert e>=2,(alpha,v,l0,l1,e)
        results.append({'alpha':alpha,'lower_shift':v,'row_factor':'ell' if v==2 else '1',
                        'minimum_first_two_digit_paid_order':minimum})
positive=[]
for h in (0,1):
    for source_s in range(1,30):
        for derivative in (0,1):
            degree=source_s+derivative;v=h+degree;bad_free=[]
            for l0 in range(p):
                for l1 in range(p):
                    e=events(l0,l1,v,0);count+=1
                    if e==0:
                        # Reconstruction supplies (s+1) at derivative1.
                        row_zero=lucas_zero(l0,l1,degree) or (derivative==1 and (source_s+1)%p==0)
                        assert row_zero,(h,source_s,derivative,l0,l1)
                        bad_free.append([l0,l1])
            positive.append({'h':h,'source_s':source_s,'derivative':derivative,
                             'row_degree':degree,'lower_shift':v,'zero_event_patterns':bad_free,
                             'every_zero_event_pattern_has_paid_row_divisibility':True})
out={'scope':'Finite exhaustive first-two-digit verification of new analytic branch inequalities over all29^2 digit pairs. No full old dictionary assembly, upper-word evaluation, source omission theorem or primitive alignment is recomputed.',
     'p':p,'total_digit_patterns_checked':count,'unit_branch_minima':results,
     'positive_symbol_branches':positive,'all_passed':True,
     'elapsed_seconds':round(time.monotonic()-start,3),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'prime29_analytic_carry_lemma_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'patterns':count,'all_passed':True,'seconds':out['elapsed_seconds']}))
