"""L23 new dyadic contractions of the parent-author supplied exact q/pairs.

This does not reconstruct or independently audit the parent's projection.
The all-degree conditional theorem is symbolic; finite evidence is labeled.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial,comb
import json
BASE=Path(__file__).resolve().parent
SOURCE=BASE.parent/'main'/'PAIRED_DERANGEMENT_LINEAR_S_CERTIFICATE.json'


def valuation(x):
    x=Fraction(x)
    if not x:return None
    a=abs(x.numerator);b=x.denominator;v=0
    while a%2==0:a//=2;v+=1
    while b%2==0:b//=2;v-=1
    return v


def arctan_rational(s):
    return 4*sum((Fraction((-1)**r,2*s-1-2*r) for r in range(s)),Fraction(0))


def normalized_orthogonal_state(mu,n):
    # New exact normal-basis state, not a rederivation of the parent projection.
    a=[[Fraction(mu[i+j]) for j in range(n)]+[Fraction(-mu[i+n])] for i in range(n)]
    determinant=Fraction(1)
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];determinant=-determinant
        val=a[j][j];determinant*=val;a[j]=[x/val for x in a[j]]
        for i in range(j+1,n):
            z=a[i][j]
            if z:a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    q=[Fraction(0)]*n
    for i in range(n-1,-1,-1):q[i]=a[i][-1]-sum(a[i][j]*q[j] for j in range(i+1,n))
    q.append(Fraction(1))
    vals=[valuation(x) for x in q]
    assert all(v is None or v>=0 for v in vals)
    return dict(n=n,normalized_moment_determinant_v2=valuation(determinant),
                monic_normalized_coefficients=list(map(str,q)),coefficient_v2=vals,
                all_coefficients_two_integral=True,
                max_minor_valuation_gate_verified_at_this_degree_only=True)


def run():
    b=[1,1]
    for r in range(1,40):
        b.append((r+1)*(2*r+1)*b[r]-r*(r+1)*b[r-1]-r)
    assert all(x%2 for x in b)
    rows=[]
    for source in json.loads(SOURCE.read_text())['rows']:
        q=list(map(int,source['primitive_integer_q_coefficients']));n=len(q)-1;k=source['k']
        t=[sum(q[i]*comb(i,j)*(-1)**(i-j) for i in range(j,n+1)) for j in range(n+1)]
        Pval=[valuation(t[j])+j-n if t[j] else None for j in range(n+1)]
        assert all(v is None or v>=0 for v in Pval) and q[0]%2
        V=[sum((q[j]*arctan_rational(s+j) for j in range(n+1)),Fraction(0))
           for s in range(2*k-1)]
        gaps=[valuation(V[i+j])-i-j-valuation(factorial(i))-valuation(factorial(j))
              for i in range(k) for j in range(k)]
        assert min(gaps)>=1
        gamma=k*(k-1)+2*sum(valuation(factorial(i)) for i in range(k))
        exact=[valuation(x) for x in source['rational_determinant_coefficients']]
        w=valuation(source['q_minus_one'])
        last=2*(k-1+valuation(factorial(k-1)))
        predicted=[gamma,gamma+w-last]
        assert predicted==exact
        actual=valuation(source['actual_center_denominator'])
        assert actual==max(0,w-last)
        rows.append(dict(k=k,n=n,normalized_polynomial_coefficient_v2=Pval,
                         q_zero_odd=True,q_minus_one_v2=w,
                         rational_arctan_contraction_v2=[valuation(x) for x in V],
                         minimum_same_basis_normalized_arctan_gap=min(gaps),
                         supplied_complete_pair_v2=exact,
                         conditional_formula_pair_v2=predicted,
                         supplied_actual_q_v2=actual,conditional_formula_actual_q_v2=max(0,w-last),
                         all_degree_premises_not_inferred=True))
    out=dict(status='AUTHOR new dyadic evidence using supplied q/pairs; no independent audit',
             source=str(SOURCE),shifted_moment_b_first_terms=list(map(str,b[:12])),
             shifted_moment_recurrence_terms=41,all_recurrence_terms_odd=True,
             supplied_node_dyadic_contractions=rows,
             new_normalized_orthogonal_states=[normalized_orthogonal_state([0]+b[1:],n)
                                              for n in range(2,13)],
             all_degree_open=['normalized-q cofactor inequalities','same-basis arctan divisibility'],
             no_finite_to_infinite_extrapolation=True)
    (BASE/'WEIGHTED_DETERMINANT_DYADIC_GATEWAY_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([dict(k=r['k'],same_basis_arctan_gap=r['minimum_same_basis_normalized_arctan_gap'],
          actual_q_v2=r['supplied_actual_q_v2']) for r in rows],indent=2))


if __name__=='__main__':run()
