"""Independent fixed-list certificate audit; writes only in Agent 4 directory."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import hashlib

BASE=Path('work/session_20261001_astra')
OUT=BASE/'agent4'
SOURCE=BASE/'agent3/exact_certificate.json'
PRIMES=(41,43,59,67)

def decode(x):
    return F(int(x['numerator']),int(x['denominator']))

def logs(x,m=32):
    x=F(x)
    k=0
    while x>=2:
        x/=2
        k+=1
    def series(z):
        s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
        return s,s+2*z**(2*m+1)/((2*m+1)*(1-z*z))
    a,b=series(F(1,3))
    c,d=series((x-1)/(x+1))
    return k*a+c,k*b+d

def main():
    raw=SOURCE.read_bytes()
    cert=json.loads(raw)
    # (k+1)L_(k+1)=2(2k+1)(2t-1)L_k+4kL_(k-1).
    polys=[[1],[-2,4]]
    for k in range(1,67):
        v=[0]*(k+2)
        for j,c in enumerate(polys[k]):
            v[j]-=2*(2*k+1)*c
            v[j+1]+=4*(2*k+1)*c
        for j,c in enumerate(polys[k-1]):
            v[j]+=4*k*c
        assert all(c%(k+1)==0 for c in v)
        polys.append([c//(k+1) for c in v])
    fac=[factorial(j) for j in range(135)]
    partial=[sum((F(1,fac[h]) for h in range(j+1)),F(0)) for j in range(135)]
    seeds=[]
    for n in range(67):
        r=[sum((F(c,fac[n+j]) for j,c in enumerate(polys[k])),F(0)) for k in (n,n+1)]
        t=[sum((c*partial[n+j] for j,c in enumerate(polys[k])),F(0)) for k in (n,n+1)]
        scale=F(fac[n]**2,2**n)
        h,a=scale*r[0],scale*t[0]
        k,b=scale*F(n+1,2)*r[1],scale*F(n+1,2)*t[1]
        values=[h,k,a,b,k*a-h*b]
        assert h.denominator==k.denominator==1
        assert all(v.denominator&(v.denominator-1)==0 for v in values)
        seeds.append(values)
    saved=cert['exact_rational_scalar_seeds']
    assert [s['r'] for s in saved]==list(range(67))
    for n,s in enumerate(saved):
        assert seeds[n]==list(map(decode,s['values_in_coordinate_order'])),('rational seed',n)
    records={r['p']:r for r in cert['tested_prime_certificates']}
    rows_out={}
    count=0
    for p in PRIMES:
        rows=[]
        for n in range(p):
            row=[v.numerator*pow(v.denominator,-1,p)%p for v in seeds[n]]
            for j,value in enumerate(row):
                assert value==records[p]['modular_H_K_Acal_Bcal_Ccal'][n][j],('modular',p,n,j)
                assert value==records[p]['legendre_H_K_Acal_Bcal_Ccal'][n][j],('Legendre',p,n,j)
                count+=1
            rows.append(row)
        assert [n for n,row in enumerate(rows) if row[4]==0]==[1]
        assert records[p]['Ccal_zero_set']==[1]
        rows_out[str(p)]=rows
    assert count==1050
    rates=[]
    for rc in cert['rate_history']:
        bracket=rc['sqrt2_bracket']
        d=int(bracket['denominator']); a=int(bracket['lower_numerator'])
        assert int(bracket['upper_numerator'])==a+1
        assert 2*d*d-a*a==int(bracket['lower_square_gap'])>0
        assert (a+1)**2-2*d*d==int(bracket['upper_square_gap'])>0
        tl=2*logs(1+F(a,d))[0]
        tu=2*logs(1+F(a+1,d))[1]
        assert decode(rc['tau_lower'])<=tl<=tu<=decode(rc['tau_upper'])
        wl=wu=F(0)
        for p in rc['uniform_primes']:
            lower,upper=logs(p)
            saved_bounds=rc['log_p_bounds'][str(p)]
            lo,hi=decode(saved_bounds['lower']),decode(saved_bounds['upper'])
            assert lo<=lower<=upper<=hi,('log enclosure',p)
            wl+=F(2,p-1)*lo
            wu+=F(2,p-1)*hi
        assert wl==decode(rc['W_lower']) and wu==decode(rc['W_upper'])
        assert wl-decode(rc['tau_upper'])==decode(rc['strict_gap_lower'])
        assert decode(rc['coarse_W_lower'])<=wl
        assert decode(rc['coarse_tau_upper'])>=decode(rc['tau_upper'])
        assert decode(rc['coarse_gap_lower'])==decode(rc['coarse_W_lower'])-decode(rc['coarse_tau_upper'])
        verdict='above' if wl>decode(rc['tau_upper']) else 'below' if wu<decode(rc['tau_lower']) else 'unresolved'
        assert verdict==rc['verdict']
        rates.append(verdict)
    assert rates==['below']*4+['above']
    final=cert['final_rate_certificate']
    assert final==cert['rate_history'][-1]
    assert decode(final['coarse_gap_lower'])==F(20453,200000)>0
    assert decode(final['strict_gap_lower'])>F(20453,200000)
    result={'all_checks_pass':True,'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'method':'Independent integer Legendre recurrence, exact rational functionals, and 32-term rational logarithm enclosures.',
            'distinct_exact_seeds_checked':67,'selected_rows_checked':210,
            'coordinate_comparisons_against_each_saved_construction':count,
            'zero_sets':{str(p):[1] for p in PRIMES},'rate_history_verdicts':rates,
            'certified_margin':str(decode(final['coarse_gap_lower'])),
            'independent_selected_rows':rows_out,'new_primes_scanned':[]}
    (OUT/'whole_family_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='independent_selected_rows'},indent=2))

if __name__=='__main__':
    main()
