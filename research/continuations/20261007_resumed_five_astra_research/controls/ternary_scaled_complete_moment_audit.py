"""Parent-authored finite scaled analogues of the new complete moment lemma.

The original depth25 pole parameter is scaled to2..4 to permit direct checks of
EVERY retained denominator and monomial. No original-domain conclusion follows.
"""
from pathlib import Path
from math import comb
import hashlib,json,time

ROOT=Path(__file__).resolve().parent
start=time.monotonic()
cases=[]
for k,D in [(2,8),(3,10),(4,8),(3,6)]:
    H=3**(k+3);h=k+4;Omega=H//3**k;c=(Omega-1)//2
    n=H-D+1;cutoff=4*n-3;mod=3**(k+2)
    assert 2*D<Omega and h>=k+2 and H+2*D<(3*H-1)//2
    coeff=[((-1)**(H-j)*comb(H,j))%mod for j in range(H+1)]
    # The factorial piece is divisible by3^h and hence is zero at this modulus.
    weights={}
    for degree in range(H+2*D+1):
        den=2*degree+1
        if den>cutoff:continue
        unit=den;e=0
        while unit%3==0:unit//=3;e+=1
        assert e<=h
        weights[degree]=3**(h-e)*pow(unit,-1,mod)%mod
    evaluations=[];failures=[]
    for a in range(2*D+1):
        observed=sum(coeff[j]*weights.get(j+a,0) for j in range(H+1))%mod
        expected=3**(k+1) if a==c else 0
        evaluations.append({'monomial_degree':a,'observed':observed,'expected':expected})
        if observed!=expected:failures.append({'degree':a,'observed':observed,'expected':expected})
    cases.append({'scaled_pole_parameter':k,'D':D,'H':H,'h':h,
      'Omega':Omega,'c':c,'cutoff':cutoff,'modulus':mod,
      'all_retained_denominators_checked':True,'monomials':evaluations,
      'failures':failures})
out={'personally_authored':True,'network_and_credentials_denied':True,
 'scope':'Finite scaled analogues only, using all retained rational-functional poles and zero factorial term. No original depth26 theorem, support theorem, primitive cofactor or irrationality conclusion is inferred.',
 'cases':cases,'all_passed':all(not x['failures'] for x in cases),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':round(time.monotonic()-start,3)}
(ROOT/'ternary_scaled_complete_moment_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_passed':out['all_passed'],'cases':len(cases),
 'total_monomials':sum(len(x['monomials']) for x in cases),
 'failures':[x['failures'] for x in cases if x['failures']],
 'seconds':out['elapsed_seconds']}),flush=True)
