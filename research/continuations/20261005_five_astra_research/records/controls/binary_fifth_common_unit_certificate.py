"""Coordinator independent finite certificate for A5 turn22's common-unit proof."""
import json
import math
import resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
P=(34,31,7,5,48,12,4,4,32,8,56,8)
DD=(112,102,10,124,16,24,56,0,96,16,80,96)
BE=(113,74,78,72,120,80,112)
def choose(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)
def base(s,x,coeff):
    return choose(s+3,3)*sum(coeff[r]*choose(x,r-s) for r in range(s,12)) if 0<=s<=11 else 0
def z(s,x):
    return BE[-s-1] if -7<=s<=-1 else base(s,x,DD)
def us(s,x):return base(s,x,P)+x*base(s,x-1,P)+x*base(s+1,x-1,P)
def vs(s,x):return z(s,x)+x*z(s,x-1)+x*z(s+1,x-1)
def val(a):
    return (abs(a)&-abs(a)).bit_length()-1 if a else 1000
rows=[];checks=[];fail=[]
rho_list=[r for r in range(69) if val(choose(68,r))<=3]
assert len(rho_list)==29
for rho in rho_list:
    a=84-rho
    bw=val(choose(68,rho))
    ff=sum(us(s,rho)*choose(a,s+4) for s in range(-1,12))
    gg=sum(vs(s,rho)*choose(a,s+4) for s in range(-4,12))
    product=2**(2*bw)*ff*gg%128
    expected=96 if rho in (0,1,64,65) else 0
    assert product==expected,(rho,product)
    for col,lo,target,fn in [('F',-1,5,us),('G',-3,6,vs)]:
        for s in range(lo,12):
            c=s+4
            q=7-(c.bit_length()-1)
            coefficient=fn(s,rho)
            depth=min(val(coefficient),6 if col=='F' else 7)+q
            checks.append([rho,col,s,depth,target])
            if depth<target:fail.append(checks[-1])
    for s in range(-8,-4):
        q=-(s+4)
        num=math.prod(128-i for i in range(q))
        den=math.prod(a+i for i in range(1,q+1))
        depth=min(val(vs(s,rho)),7)+val(num)-val(den)
        checks.append([rho,'Gnegative',s,depth,8])
        if depth<8:fail.append(checks[-1])
    rows.append({'rho':rho,'weight_depth':bw,'F_mod32':ff%32,'G_mod64':gg%64,
                 'weighted_product_mod128':product})
assert not fail,fail
assert sum(r['weighted_product_mod128'] for r in rows)%128==0
# Independent exact ratio and odd-unit checks at bounded auxiliary d,k.
from fractions import Fraction
ratio_cases=0
for a in [84-rho for rho in rho_list]:
    for d in (0,1,2,7):
        for k in (1,3,9):
            top=128*(d+k)+a
            anchor=choose(top,128*d+a)
            bd=choose(d+k,d)
            unit=Fraction(anchor,bd)
            assert val(unit.numerator)-val(unit.denominator)==0
            for c in range(-4,16):
                exact=Fraction(choose(top,128*d+a-c),anchor)
                if c>=0:
                    ratio=Fraction(choose(128*d+a,c),choose(128*k+c,c))
                else:
                    q=-c
                    ratio=Fraction(math.prod(128*k-i for i in range(q)),
                                   math.prod(128*d+a+i for i in range(1,q+1)))
                assert ratio==exact
                ratio_cases+=1
report={'status':'PASS','nonoverflow_rows':29,'nonzero_product_residues':[0,1,64,65],
        'fixed_weighted_product_sum_mod128':0,'coefficient_precision_checks':len(checks),
        'all_coefficient_precision_checks_pass':True,'bounded_exact_ratio_checks':ratio_cases,
        'rows':rows,'checks':checks,
        'scope':'Fixed coefficient, precision, and bounded auxiliary ratio certificate. Infinite conclusion additionally uses the algebraic common-unit representation, binomial translation, E_t evenness, full mixed support and endpoint proof; no all-depth valuation statement.'}
(OUT/'binary_fifth_common_unit_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('rows','checks')}))
