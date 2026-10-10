"""Exact controls at the already studied degrees 1,2,3,4,5,8 only.

No degree range is scanned. The original appended-coordinate determinant
is compared with its two border parts and two distinguished Laplace terms.
"""
import sys,json,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s

DEGREES=(1,2,3,4,5,8)

def val(x):
    if x==0:return None
    a,b=map(int,s.fraction(s.cancel(x)))
    return ((abs(a)&-abs(a)).bit_length()-1)-((b&-b).bit_length()-1)

def phi(k):return k-k.bit_count()
def sf(n):return sum(phi(k) for k in range(n))
def f(k):return s.Rational(1,math.factorial(k)) if k>=0 else s.Integer(0)
def t(k):return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.Integer(0)

stored={r['n']:r for r in json.loads(Path(__file__).with_name('raw_accessory_scaling_probe.json').read_text())['cases']}
qvals=[s.Integer(1),s.Integer(1)]
for k in range(1,max(DEGREES)):
    qvals.append(s.cancel(qvals[-1]+s.Rational(k*k,4*k*k-1)*qvals[-2]))
result={'degrees':list(DEGREES),'normalization':'original integer high jets; Btop coordinate appended without factorial','cases':[]}

for n in DEGREES:
    high=list(range(n+1,3*n+1))
    rows=[[f(k-j) for j in range(n)]+[t(k-j) for j in range(n+1)] for k in high]
    dc=s.Matrix(rows+[[0]*n+[1]*(n+1)]).det()
    db=s.Matrix(rows+[[1]*n+[0]*(n+1)]).det()
    total=dc-4*db
    direct=s.Matrix(rows+[[-4]*n+[1]*(n+1)]).det()
    assert total==direct
    fullrows=[[f(k-j) for j in range(n+1)]+[t(k-j) for j in range(n+1)] for k in high]
    mend=s.Matrix(fullrows+[[-4]*(n+1)+[1]*(n+1),[1]*(n+1)+[0]*(n+1)]).det()
    btop=s.cancel((-1)**(n+1)*total/mend)
    factor=math.prod(math.factorial(k) for k in high)
    integer_top=s.cancel((-1)**(n+1)*factor*total)
    integer_endpoint=s.cancel(factor*mend)
    assert integer_top.q==integer_endpoint.q==1
    ell=2*sf(n)+2*((n+2)//4)
    baseline=sf(n)-sum(phi(k) for k in range(2*n+1,3*n+1))+ell
    expected_endpoint=sum(phi(k) for k in range(n+1,2*n+1))+sf(n)+ell
    assert val(integer_endpoint)==expected_endpoint
    distinguished=[]
    pair=[]
    for label,selected in [('S0',list(range(2*n+1,3*n+1))),('Sstar',[2*n]+list(range(2*n+2,3*n+1)))]:
        comp=[k for k in high if k not in selected]
        exp=s.Matrix([[f(k-j) for j in range(n)] for k in selected]).det()
        arc=s.Matrix([[t(k-j) for j in range(n+1)] for k in comp]+[[1]*(n+1)]).det()
        sign=(-1)**(sum(high.index(k) for k in selected)+n*(n-1)//2)
        term=sign*exp*arc
        pair.append(term)
        distinguished.append({'set':label,'exponential_valuation':val(exp),'arctangent_valuation':val(arc),'term_valuation':val(term)})
    pair_factor=s.cancel(((2*n-1)*qvals[n]-n**3*qvals[n-1])/((2*n-1)*qvals[n]))
    assert s.cancel(sum(pair)-pair[0]*pair_factor)==0
    if n%4!=1:
        assert val(total)==baseline and val(btop)==0
    else:
        assert total==0 or val(total)>=baseline+1
        assert pair[0]!=0 and pair[1]!=0 and val(pair[0])==val(pair[1])==baseline
        if n>=5:assert val(sum(pair))==baseline+val(s.Integer(n-1))
    row={'n':n,'baseline':baseline,'C_border_valuation':val(dc),'minus4_B_border_valuation':val(-4*db),'total_valuation':val(total),'integer_Btop_valuation':val(integer_top),'integer_endpoint_valuation':val(integer_endpoint),'normalized_btop':str(btop),'normalized_btop_valuation':val(btop),'distinguished_terms':distinguished,'pair_sum_valuation':val(sum(pair)),'C_border_zero':dc==0}
    if n in stored:
        bb=list(map(s.Rational,stored[n]['exact_polynomial_input']['B']))
        assert btop==bb[0]/sum(bb)
        row['stored_original_polynomial_match']=True
    if n==1:assert btop==8 and dc==0 and sum(pair)==0
    result['cases'].append(row)

Path(__file__).with_name('raw_leading_B_dyadic_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
