"""Selected exact raw endpoint dyadic checks, independent of archive solver."""
from fractions import Fraction as F
from math import factorial, comb
from itertools import combinations
from pathlib import Path
import json


def phi(k):return k-k.bit_count()
def S(n):return sum(phi(k) for k in range(n))
def v2(x):
    x=F(x)
    if not x:return None
    a=abs(x.numerator);b=x.denominator
    return (a&-a).bit_length()-(b&-b).bit_length()


def determinant(matrix):
    a=[[F(x) for x in row] for row in matrix];n=len(a);ans=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:a[pivot],a[j]=a[j],a[pivot];ans=-ans
        value=a[j][j];ans*=value
        for k in range(j+1,n):
            ratio=a[k][j]/value
            if ratio:
                for ell in range(j+1,n):a[k][ell]-=ratio*a[j][ell]
            a[k][j]=F(0)
    return ans


def t(k):return F((-1)**((k-1)//2),k) if k>0 and k%2 else F(0)
def f(k):return F(1,factorial(k)) if k>=0 else F(0)


def coefficient_matrix(n):
    rows=[[f(k-j) for j in range(n+1)]+[t(k-j) for j in range(n+1)]
          for k in range(n+1,3*n+1)]
    rows.append([F(-4)]*(n+1)+[F(1)]*(n+1))
    rows.append([-sum((f(k) for k in range(n-j+1)),F(0)) for j in range(n+1)]+
                [-sum((t(k) for k in range(n-j+1)),F(0)) for j in range(n+1)])
    return rows


def exact_degree(n):
    mat=coefficient_matrix(n)
    integer=[]
    for k,row in enumerate(mat):
        scale=factorial(n+1+k) if k<2*n else factorial(n) if k==2*n+1 else 1
        rr=[v*scale for v in row]
        assert all(v.denominator==1 for v in rr)
        integer.append(rr)
    da=determinant(integer)
    db=determinant(integer[:-1]+[[F(1)]*(n+1)+[F(0)]*(n+1)])
    prediction=phi(n)+sum(phi(k) for k in range(n+1,2*n+1))+3*S(n)-n
    assert v2(da)==prediction
    ratio=da/(factorial(n)*db)
    qvaluation=v2(ratio.denominator)
    assert qvaluation==n+2*((n+2)//4)
    cminor=[[t(k-j) for j in range(n+1)] for k in range(n+1,2*n)]
    cminor.append([F(1)]*(n+1))
    cminor.append([-sum((t(k) for k in range(n-j+1)),F(0)) for j in range(n+1)])
    assert v2(determinant(cminor))==2*S(n)
    return dict(n=n,delta_A_v2=v2(da),delta_B_v2=v2(db),
                reduced_endpoint_q_v2=qvaluation,leading_C_minor_v2=2*S(n),
                all_claimed_formulas_verified=True)


def laplace_audit(n=4):
    mat=coefficient_matrix(n);size=2*n+2
    predicted=3*S(n)-n-sum(phi(k) for k in range(2*n+1,3*n+1))
    least=[];counts={};minimum_by_case={};nonzero=0
    for selected in combinations(range(size),n+1):
        selected=set(selected);other=[k for k in range(size) if k not in selected]
        pd=determinant([[mat[k][j] for j in range(n+1)] for k in sorted(selected)])
        cd=determinant([[mat[k][j] for j in range(n+1,size)] for k in other])
        vv=v2(pd*cd)
        case=(2*n in selected,2*n+1 in selected)
        key=f'border_to_B={case[0]},A_to_B={case[1]}'
        counts[key]=counts.get(key,0)+1
        if vv is None:continue
        nonzero+=1
        minimum_by_case[key]=min(minimum_by_case.get(key,vv),vv)
        gap={(False,False):0,(False,True):n,(True,False):n+2,
             (True,True):2+2*phi(2*n)}[case]
        assert vv>=predicted+gap
        if vv==predicted:least.append(sorted(selected))
    assert least==[list(range(n-1,2*n))]
    return dict(n=n,total_terms=sum(counts.values()),nonzero_terms=nonzero,
                unique_least_exponential_high_rows=list(range(2*n,3*n+1)),
                least_valuation=predicted,case_minima=minimum_by_case,
                all_four_case_bounds_verified=True)


if __name__=='__main__':
    result=dict(status='PASS',scope='Four selected exact degrees plus the entire n=4 Laplace expansion; no extrapolation.',
                degrees=[exact_degree(n) for n in (1,2,6,10)],laplace_audit=laplace_audit())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
