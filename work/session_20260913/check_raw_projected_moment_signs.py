"""Closed exact test: n=4,5 projected Legendre moments, all maximal and 2x2 minors."""
import sys,json
from pathlib import Path
from math import factorial,comb
from itertools import combinations,product
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
x=s.symbols('x')
def moment(k,l):
    return s.Rational(factorial(k),factorial(2*k))*sum(
        s.Rational(comb(k,(k+d)//2)*factorial(k+d),factorial(d-l)*factorial(d+l+1))
        for d in range(l,k+1) if d%2==k%2)
def rawF(k):
    return s.Rational(factorial(k),factorial(2*k))*sum(
        s.Rational(comb(k,(k+d)//2)*factorial(k+d),factorial(d)**2)*x**d
        for d in range(k+1) if d%2==k%2)
out=[]
for n in (4,5):
    rows=list(range(n+1,2*n));cols=list(range(n+1))
    M=s.Matrix([[moment(k,l) for l in cols] for k in rows])
    assert all(v>0 for v in M)
    # Independent direct integration for every entry in this closed set.
    assert all(s.integrate(rawF(k)*s.legendre(l,2*x-1),(x,0,1))==M[i,l]
               for i,k in enumerate(rows) for l in cols)
    mm=[]
    for cc in combinations(cols,n-1):
        v=M[:,cc].det()
        mm.append({'columns':list(cc),'value':str(v),'sign':int(s.sign(v))})
    tw=[]
    for rr in combinations(range(n-1),2):
        for cc in combinations(cols,2):
            v=M.extract(rr,cc).det()
            tw.append({'rows':[rows[i] for i in rr],'columns':list(cc),'value':str(v),'sign':int(s.sign(v))})
    # Does any row/column sign reorientation make all natural-order
    # maximal minors have one sign? Full-row flips only change all signs.
    reorient=[]
    for sig in product((-1,1),repeat=n+1):
        adjusted=[d['sign']*s.prod(sig[j] for j in d['columns']) for d in mm]
        if len(set(adjusted))==1 and adjusted[0]!=0:
            reorient.append(list(sig))
    triangles=[]
    edge={tuple(j for j in cols if j not in d['columns']):d['sign'] for d in mm}
    for tri in combinations(cols,3):
        sign=s.prod(edge[tuple(sorted(e))] for e in combinations(tri,2))
        triangles.append({'omitted_column_triangle':list(tri),'sign_product':int(sign)})
    out.append({'n':n,'row_indices':rows,'column_indices':cols,'all_entries_strictly_positive':True,
                'matrix':[[str(v) for v in M.row(i)] for i in range(n-1)],
                'maximal_minors':mm,'maximal_sign_counts':{str(a):sum(d['sign']==a for d in mm) for a in (-1,0,1)},
                'two_by_two_minors':tw,'two_by_two_sign_counts':{str(a):sum(d['sign']==a for d in tw) for a in (-1,0,1)},
                'natural_order_maximal_reorientations':reorient,'complement_triangle_products':triangles})
result={'scope':'Only predeclared n4,n5 moment matrices; no canonical raw-degree construction and no extension of the index set.','status':'exact enumeration complete','rows':out}
(HERE/'raw_projected_moment_signs.json').write_text(json.dumps(result,indent=2)+'\n')
for r in out:
    print(json.dumps({k:r[k] for k in ('n','all_entries_strictly_positive','maximal_sign_counts','two_by_two_sign_counts','natural_order_maximal_reorientations')},indent=2))
    for sg in (-1,1):
        d=next((m for m in r['maximal_minors'] if m['sign']==sg),None)
        print('maximal witness',d)
