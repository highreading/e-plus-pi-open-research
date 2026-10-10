"""L22 bounded exact FORMAL-response denominator/content receipts.

All polynomial arithmetic uses Fraction; no numerical value of e or pi and no
assumption about algebraic independence is used. No prime scan is performed.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from math import factorial,gcd
import json

BASE=Path(__file__).resolve().parent


def lcm(a,b):return a*b//gcd(a,b)


def derangement(n):
    a,b=1,0
    if n==0:return a
    for k in range(2,n+1):a,b=b,(k-1)*(a+b)
    return b


def even_moment(k):
    # Moment index is 2k. Symbols X,Y represent the explicit e,pi responses.
    rat=-Fraction(factorial(2*k))
    rat+=4*sum((Fraction((-1)**j,2*k-1-2*j) for j in range(k)),Fraction(0))
    return {(0,0):rat,(1,0):Fraction(derangement(2*k)),(0,1):Fraction((-1)**k)}


def add(p,q):
    out=dict(p)
    for key,value in q.items():out[key]=out.get(key,Fraction(0))+value
    return {k:v for k,v in out.items() if v}


def mul(p,q):
    out={}
    for (a,b),x in p.items():
        for (c,d),y in q.items():
            key=(a+c,b+d);out[key]=out.get(key,Fraction(0))+x*y
    return {k:v for k,v in out.items() if v}


def scale(p,s):return {k:s*v for k,v in p.items() if s*v}


def det(matrix):
    n=len(matrix);out={}
    for order in permutations(range(n)):
        inv=sum(order[i]>order[j] for i in range(n) for j in range(i+1,n))
        term={(0,0):Fraction((-1)**inv)}
        for i,j in enumerate(order):term=mul(term,matrix[i][j])
        out=add(out,term)
    return out


def as_terms(p):
    return [dict(X_degree=a,Y_degree=b,coefficient=str(v))
            for (a,b),v in sorted(p.items())]


def substitute_target(p):
    # Exact Y=S-X substitution, result keyed by X and S exponents.
    out={}
    for (a,b),value in p.items():
        assert b<=1
        if b==0:out=add(out,{(a,0):value})
        else:out=add(out,{(a,1):value,(a+1,0):-value})
    return out


def receipt(m):
    H=[[even_moment(i+j) for j in range(m)] for i in range(m)]
    F=det(H)
    assert all(b<=1 for a,b in F)
    A=[[{(0,0):H[i][j][(1,0)]} for j in range(m)] for i in range(m)]
    gamma_det=det(A)[(0,0)]
    assert gamma_det>0 and gamma_det.denominator==1
    B=[[{(0,0):H[i][j][(1,0)]-H[i][j][(0,1)]}
         for j in range(m)] for i in range(m)]
    difference_det=det(B).get((0,0),Fraction(0))
    if m>=2:assert difference_det<0
    row_clears=[]
    for row in H:
        d=1
        for entry in row:
            for val in entry.values():d=lcm(d,val.denominator)
        row_clears.append(d)
    Drow=1
    for d in row_clears:Drow*=d
    content=0;Dcoeff=1
    for value in F.values():
        z=Drow*value;assert z.denominator==1
        content=gcd(content,abs(z.numerator))
        Dcoeff=lcm(Dcoeff,value.denominator)
    assert Dcoeff==Drow//gcd(Drow,content)
    target=substitute_target(F)
    if m>=2:
        assert target[(m,0)]==difference_det
        assert (m-1,1) in target and target[(m-1,1)]>0
    return dict(dimension=m,
                row_clears=row_clears,row_clear_product=Drow,
                row_cleared_full_coefficient_content=content,
                minimal_integer_formal_coefficient_denominator=Dcoeff,
                primitive_coefficient_multiplier=str(Fraction(Drow,content)),
                exact_Gram_exponential_det=int(gamma_det),
                exact_leading_coefficient_after_Y_S_minus_X=str(difference_det),
                determinant_terms=as_terms(F),target_substitution_terms=as_terms(target),
                actual_formal_denominator_identity_verified=True,
                numerical_period_denominator_not_inferred=True)


def run():
    rows=[receipt(m) for m in range(1,5)]
    assert rows[0]['determinant_terms']==[
        dict(X_degree=0,Y_degree=0,coefficient='-1'),
        dict(X_degree=0,Y_degree=1,coefficient='1'),
        dict(X_degree=1,Y_degree=0,coefficient='1')]
    out=dict(status='AUTHOR exact response-polynomial content evidence, dimensions1..4 only',
             polynomial_basis='1,x^2,...,x^(2m-2)',
             positive_weight='exp(x)+4/(1+x^2) on0..1',
             response_symbols='X=e,Y=pi formally; no algebraic independence assumed',
             rows=rows,no_prime_atlas_or_numerical_period_experiment=True)
    (BASE/'EXPONENTIAL_LOGARITHMIC_GRAM_TRANSPLANT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{key:r[key] for key in ('dimension','row_clear_product',
          'row_cleared_full_coefficient_content','minimal_integer_formal_coefficient_denominator',
          'primitive_coefficient_multiplier','exact_leading_coefficient_after_Y_S_minus_X')}
          for r in rows],indent=2))


if __name__=='__main__':run()
