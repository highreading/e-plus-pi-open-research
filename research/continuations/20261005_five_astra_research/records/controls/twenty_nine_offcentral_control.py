"""Independent finite arithmetic check of the off-central recurrence lemma."""
import json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
p=29; m=7; modulus=p*p; out=Path(__file__).resolve().parent
aa=[0]+[m*(8*pow(20,t,p)-20*pow(8,t,p))*pow(12*t,-1,p)%p for t in range(1,p)]
bb=[0]+[(m+1)*(pow(20,t,p)-pow(8,t,p))*pow(12*t,-1,p)%p for t in range(1,p)]
reports=[]
for n in (203,1044,1885):
    coef=[1];previous=0;current=1
    for r in range(n):
        numerator=2*(n-r)*current+2*(2*n-r+1)*previous
        nxt,remainder=divmod(numerator,r+1)
        assert remainder==0
        previous,current=current,nxt;coef.append(current%modulus)
    js=[coef[n-t] for t in range(p+1)]
    actual=[js[t]//p%p for t in range(1,p)]
    assert all(js[t]%p==0 for t in range(1,p))
    pred=[(aa[t]*js[0]+bb[t]*js[p])%p for t in range(1,p)]
    reports.append({'n':n,'m_mod29':n//p%p,'C_mod841':js[0],
        'J29_mod841':js[p],'actual_offcentral_div29_mod29':actual,
        'predicted':pred,'all_match':actual==pred})
receipt={'a_1_to28_mod29':aa[1:],'b_1_to28_mod29':bb[1:],
    'finite_examples':reports,'all_checks_pass':all(r['all_match'] for r in reports),
    'scope':'Fixed auxiliary arithmetic only; algebraic recurrence proof remains separate. '
        'No evaluation of Gamma0 or Gamma1, original-domain reachability or final denominator.'}
(out/'twenty_nine_offcentral_control.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'all_checks_pass':receipt['all_checks_pass'],
    'examples':[{'n':r['n'],'all_match':r['all_match']} for r in reports]}))
assert receipt['all_checks_pass']
