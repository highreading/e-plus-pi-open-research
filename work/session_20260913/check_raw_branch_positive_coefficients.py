"""Closed predeclared diagnostic: normalized spectral branches k<=12."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
xi=s.symbols('xi');last=12
records=[]
for sigma,seed in enumerate(((1,s.Rational(1,2)),(0,1))):
    r=[s.Rational(seed[0]),s.Rational(seed[1])]
    for k in range(last-1):
        up2=s.Rational((k+1)**2*(k+2)**2,(2*k+1)*(2*k+3))
        up1=s.Rational((k+1)**2,2*k+1)
        down1=s.Rational(k*k,2*k+1)
        down2=s.Rational(k*k*(k-1)**2,(2*k+1)*(2*k-1))
        diag=s.Rational((k+1)**4,(2*k+1)*(2*k+3))+s.Rational(k**4,(2*k+1)*(2*k-1))-k*(k+1)
        r.append(s.expand(((xi-diag)*r[k]+up1*r[k+1]+(down1*r[k-1] if k else 0)-(down2*r[k-2] if k>=2 else 0))/up2))
    for k,p in enumerate(r):
        co=s.Poly(p,xi).all_coeffs()
        rec={'sigma':sigma,'k':k,'coefficients_high_to_low':[str(q) for q in co],
             'zero':p==0,'all_coefficients_strictly_positive':all(q>0 for q in co),
             'negative_coefficients':[str(q) for q in co if q<0]}
        poly=s.Poly(p,xi)
        if poly.degree()>0:
            intervals=poly.intervals()
            negative=sum(m for (left,right),m in intervals if right<=0 and poly.eval(0)!=0)
            rec['negative_real_roots_with_multiplicity']=negative
            rec['real_roots_with_multiplicity']=sum(m for interval,m in intervals)
            rec['all_roots_real_negative']=negative==poly.degree()
            rec['isolating_intervals']=[[str(left),str(right),m] for (left,right),m in intervals]
        records.append(rec)
        if rec['negative_coefficients']:
            print('COUNTEREXAMPLE',json.dumps(rec))
out={'scope':'Only the predeclared k=0,...,12 in both normalized branches; no continuation beyond12.',
     'root_scope':'Exact rational real-root isolation on the same closed set; zero is excluded by the positive constant coefficient.',
     'rows':records,'negative_found':any(r['negative_coefficients'] for r in records)}
(HERE/'raw_branch_positive_coefficients_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'negative_found':out['negative_found'],'nonzero_rows_checked':sum(not r['zero'] for r in records),'all_nonzero_rows_strictly_positive':all(r['zero'] or r['all_coefficients_strictly_positive'] for r in records),'all_nonconstant_roots_real_negative':all(r.get('all_roots_real_negative',True) for r in records)}))
