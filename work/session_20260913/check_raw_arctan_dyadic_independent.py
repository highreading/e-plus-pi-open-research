"""Independent direct normalization checks, not a proof from finite data."""
from pathlib import Path
from math import factorial
from itertools import combinations
import sys,json
base=Path(__file__).parent
sys.path.insert(0,str(base/'math_packages'))
import sympy as S

def phi(k):
    return k-k.bit_count()
def sigma(k):
    return sum(phi(j) for j in range(k))
def nu(x):
    x=S.Rational(x)
    if x==0:return None
    a,b=abs(int(x.p)),int(x.q)
    return (a&-a).bit_length()-(b&-b).bit_length()
def f(k):return S.Rational(1,factorial(k)) if k>=0 else S.Rational(0)
def t(k):return S.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else S.Rational(0)
def matrix(n):
    rows=[[f(k-j) for j in range(n+1)]+[t(k-j) for j in range(n+1)] for k in range(n+1,3*n+1)]
    rows.append([-4]*(n+1)+[1]*(n+1))
    arow=[-sum(f(k) for k in range(n-j+1)) for j in range(n+1)]
    arow +=[-sum(t(k) for k in range(1,n-j+1)) for j in range(n+1)]
    return S.Matrix(rows),S.Matrix([arow])

out=[]
for n in [3,5,7]:
    J,arow=matrix(n)
    brow=S.Matrix([[1]*(n+1)+[0]*(n+1)])
    integral=J.copy()
    for row,k in enumerate(range(n+1,3*n+1)):
        for col in range(2*n+2):integral[row,col]*=factorial(k)
    DA=integral.col_join(factorial(n)*arow).det(method='domain-ge')
    DB=integral.col_join(brow).det(method='domain-ge')
    expected=phi(n)+sum(phi(k) for k in range(n+1,2*n+1))+3*sigma(n)-n
    assert nu(DA)==expected
    # Independently solve the actual high equations with B(1)=1,
    # then reconstruct A(1) from its low Taylor coefficients.
    rhs=S.zeros(2*n+2,1);rhs[-1]=1
    coeff=J.col_join(brow).inv()*rhs
    B=list(coeff[:n+1]);C=list(coeff[n+1:])
    Aval=-sum(sum(B[j]*f(k-j)+C[j]*t(k-j) for j in range(n+1)) for k in range(n+1))
    assert Aval==S.Rational(DA,factorial(n)*DB)
    q=int(S.denom(Aval))
    assert nu(q)==n+2*((n+2)//4)
    out.append({'n':n,'delta_A_valuation':nu(DA),'delta_B_valuation':nu(DB),'actual_reduced_endpoint_denominator_valuation':nu(q),'direct_low_endpoint_and_cofactor_agree':True})

# Independent small exhaustive control of the four combinatorial cases.
n=3;J,arow=matrix(n);M=J.col_join(arow);records=[]
for chosen in combinations(range(2*n+2),n+1):
    other=[k for k in range(2*n+2) if k not in chosen]
    term=M.extract(chosen,range(n+1)).det()*M.extract(other,range(n+1,2*n+2)).det()
    assignment=('border' if 2*n in chosen else '')+('A' if 2*n+1 in chosen else '')
    records.append((nu(term),tuple(chosen),assignment or 'neither'))
finite=[x for x in records if x[0] is not None]
minimum=min(v for v,_,_ in finite)
least=[x for x in finite if x[0]==minimum]
Vstar=3*sigma(n)-n-sum(phi(k) for k in range(2*n+1,3*n+1))
assert minimum==Vstar and len(least)==1
assert least[0][1]==tuple(range(n-1,2*n))
case_min={key:min(v for v,_,a in finite if a==key) for key in ['neither','A','border','borderA']}
assert case_min['A']>=Vstar+n
assert case_min['border']>=Vstar+n+2
assert case_min['borderA']>=Vstar+2+2*phi(2*n)
out.append({'n':n,'all_70_Laplace_assignments_checked':True,'least_term_valuation':Vstar,'unique_least_high_nodes':list(range(2*n,3*n+1)),'case_minima':case_min})
result={'status':'PASS; bounded exact controls only, semantic proof reviewed separately','rows':out}
(base/'raw_arctan_dyadic_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
