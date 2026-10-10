from fractions import Fraction as F
from math import factorial
import json

def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
def mul(a,b):
    return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,c):
    return (a[0]*c,a[1]*c)
def power(a,k):
    out=(F(1),F(0))
    for _ in range(k):
        out=mul(out,a)
    return out
def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j]+=u*v
    return out

z=(F(-3),F(2))
zero=(F(0),F(0))
rows=[]
for m in range(1,5):
    coeff=[1]
    for _ in range(m):
        coeff=poly_mul(coeff,[1,6,1])
    denom=8**m
    assert sum(coeff)==denom and coeff[0]==1
    weights=[F(c,denom) for c in coeff]
    zp=[power(z,j) for j in range(2*m+1)]
    moments=[]
    for k in range(m+1):
        val=zero
        for j,w in enumerate(weights):
            val=add(val,scale(zp[j],w*j**k))
        moments.append(val)
    assert all(val==zero for val in moments[:m])
    expected_moment=scale(power((F(2),F(-3,2)),m),factorial(m))
    assert moments[m]==expected_moment and moments[m]!=zero

    # Exact numerator over product_j(n+j), independently expanded.
    numerator=[zero for _ in range(2*m+1)]
    for j,w in enumerate(weights):
        term=[1]
        for k in range(2*m+1):
            if k!=j:
                term=poly_mul(term,[k,1])
        for degree,c in enumerate(term):
            numerator[degree]=add(numerator[degree],scale(zp[j],w*c))
    degree=max(i for i,c in enumerate(numerator) if c!=zero)
    expected_leading=scale(power((F(-2),F(3,2)),m),factorial(m))
    assert degree==m
    assert numerator[m]==expected_leading
    assert numerator[m]==scale(moments[m],(-1)**m)
    rows.append({'m':m,'filter_degree':2*m,'least_common_denominator':denom,'rational_function_numerator_degree':degree,'leading_coefficient_in_basis_1_sqrt2':[str(c) for c in numerator[m]]})
print(json.dumps({'exact_checks_passed':True,'cases':rows,'endpoint_reconstruction_executed':False},indent=2))