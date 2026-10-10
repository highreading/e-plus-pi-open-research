"""Parent-authored bounded exact saturation audit for the specified even-contact family."""
from pathlib import Path
from math import gcd,lcm
from functools import reduce
import json
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

def bareiss(rows):
    a=[list(row) for row in rows];n=len(a);previous=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

a=[1]
for d in range(1,59):a.append(1-d*a[-1])
receipts=[]
for k in range(2,11):
    cs=[a[2*m]-(-1)**m for m in range(3*k-1)]
    raw=[[cs[i+j] for j in range(k)] for i in range(k)]
    full=[[cs[i+j] for j in range(2*k)] for i in range(k)]
    C=Matrix(raw);T=Matrix(full)
    det=bareiss(raw);assert det==int(C.det()) and det<0
    S=smith_normal_form(T,domain=ZZ)
    inv=[abs(int(S[i,i])) for i in range(k)]
    assert all(inv) and all(inv[i+1]%inv[i]==0 for i in range(k-1))
    delta=1
    for v in inv:delta*=v
    assert abs(det)%delta==0
    costs=[]
    for m in range(k,2*k):
        w=Matrix([cs[i+m] for i in range(k)])
        x=C.inv()*w
        assert C*x==w
        clearer=lcm(*(int(v.q) for v in x))
        coeff=[-int(v*clearer) for v in x]+[0]*(m-k)+[clearer]
        assert reduce(gcd,(abs(v) for v in coeff))==1
        assert all(sum(cs[i+j]*v for j,v in enumerate(coeff))==0 for i in range(k))
        costs.append(clearer)
        if k==2:
            assert coeff==({2:[-117,-4,1],3:[-6884,-133,0,1]}[m])
    receipts.append({'k':k,'determinant':det,'full_contact_invariants':inv,
                     'gcd_maximal_minors':delta,'high_coefficient_lattice_index':abs(det)//delta,
                     'actual_monic_row_clearers':costs,'all_contact_checks_passed':True})
out=Path(__file__).with_name('compact_contact_saturation_certificate.json')
out.write_text(json.dumps({'scope':'Finite sizes k2 through k10 only; no asymptotic saturation conclusion.',
                           'parent_authored':True,'receipts':receipts},indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'sizes':[x['k'] for x in receipts],
                  'index_bit_lengths':[x['high_coefficient_lattice_index'].bit_length() for x in receipts],
                  'determinant_bit_lengths':[abs(x['determinant']).bit_length() for x in receipts]}))
