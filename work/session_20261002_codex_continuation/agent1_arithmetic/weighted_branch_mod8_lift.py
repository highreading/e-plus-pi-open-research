"""Author exact modulo8 branch-lift certificate for L24's next digit.

This computes formal Taylor series, not a new atlas of determinant nodes.
The complete coupled endpoint quotient remains a separate operation.
"""
from pathlib import Path
from math import factorial
import json
from weighted_regular_dyadic_subfamily import b_moments

BASE=Path(__file__).resolve().parent
MOD=8


def trim(a):
    a=[x%MOD for x in a]
    while len(a)>1 and not a[-1]:a.pop()
    return a


def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,x in enumerate(a):z[i]+=x
    for i,x in enumerate(b):z[i]+=x
    return trim(z)


def scale(a,c):return trim([c*x for x in a])
def sub(a,b):return add(a,scale(b,-1))


def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)


def power(a,n):
    z=[1]
    for _ in range(n):z=mul(z,a)
    return z


def deriv(a):return trim([i*a[i] for i in range(1,len(a))] or [0])


def matrix_vec(a,v):
    return [add(mul(a[i][0],v[0]),mul(a[i][1],v[1])) for i in range(2)]


def divmod_unit(a,b):
    r=trim(a)
    q=[0]*max(1,len(r)-len(b)+1)
    inv=pow(b[-1],-1,MOD)
    while len(r)>=len(b) and r != [0]:
        k=len(r)-len(b)
        c=r[-1]*inv%MOD
        q[k]=c
        r=sub(r,[0]*k+scale(b,c))
    return trim(q),r


def mulrem(a,b,modulus):return divmod_unit(mul(a,b),modulus)[1]


def powrem(a,n,modulus):
    z=[1]
    while n:
        if n%2:z=mulrem(z,a,modulus)
        a=mulrem(a,a,modulus);n//=2
    return z


def series(num,den,count):
    assert den[0]==1
    out=[]
    for i in range(count):
        x=num[i] if i<len(num) else 0
        x-=sum(den[j]*out[i-j] for j in range(1,min(i,len(den)-1)+1))
        out.append(x%MOD)
    return out


def normalized_differences(values):
    work=values[:]
    out=[]
    for d in range(len(values)):
        den=2**d*factorial(d)
        assert work[0]%den==0
        out.append(work[0]//den)
        work=[work[i+1]-work[i] for i in range(len(work)-1)]
    return out


def run():
    M=[[[0,-2,-2,4,4],[0,1,2,-1,-2]],
       [[0,-1,2],[0,1,-1]]]
    M=[[trim(x) for x in row] for row in M]
    c=[[1,1,-1,-2],[1,-1]]
    c=list(map(trim,c))
    A=[[sub([1],M[0][0]),scale(M[0][1],-1)],
       [scale(M[1][0],-1),sub([1],M[1][1])]]
    D=sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))
    assert D==trim([1,1,2,-4,-3])
    adj=[[A[1][1],scale(A[0][1],-1)],
         [scale(A[1][0],-1),A[0][0]]]
    Q=matrix_vec(adj,c)
    R=[[sub(adj[i][j],D if i==j else [0]) for j in range(2)]
       for i in range(2)]
    Dp=deriv(D)
    Qp=[sub(mul(deriv(q),D),mul(q,Dp)) for q in Q]
    Qpp=[sub(mul(deriv(q),D),scale(mul(q,Dp),2)) for q in Qp]
    T=matrix_vec(R,Qp)
    Tp=[sub(mul(deriv(t),D),scale(mul(t,Dp),3)) for t in T]
    RTp=matrix_vec(R,Tp)
    RQpp=matrix_vec(R,Qpp)
    numerator=[add(add(mul(Q[i],power(D,4)),scale(mul(T[i],power(D,2)),-2)),
                   add(scale(RTp[i],4),scale(mul(RQpp[i],D),2)))
               for i in range(2)]
    denominator=power(D,5)
    assert powrem([0,1],480,denominator)==[1]
    parts=[divmod_unit(x,denominator) for x in numerator]
    coeff=[series(x,denominator,1024) for x in numerator]
    max_poly_degree=max(len(q)-1 for q,r in parts)
    assert all(coeff[i][r]==coeff[i][r+480]
               for i in range(2) for r in range(max_poly_degree+1,544))
    b=b_moments(180)
    rho_even=normalized_differences(b[0:180:2])
    rho_odd=normalized_differences(b[1:180:2])
    conversion_checks=0
    for branch,rho in enumerate((rho_odd,rho_even)):
        for j in range(80):
            s1=(j+1)*(j+2)//2
            s2=(j+1)*(j+2)*(2*j+3)//6
            e2=(s1*s1-s2)//2
            got=(rho[j]-j*(j+1)*rho[j+1]+4*e2*rho[j+2])%MOD
            assert got==coeff[branch][j]
            conversion_checks+=1
    out={
        'status':'AUTHOR formal modulo8 moment-branch lift, no determinant atlas',
        'D_coefficients_mod8':D,
        'common_denominator_D_power5':denominator,
        'numerators_O_E_mod8':numerator,
        'polynomial_parts_O_E_mod8':[q for q,r in parts],
        'proper_numerators_O_E_mod8':[r for q,r in parts],
        'u_power480_mod_D5_mod8':[1],
        'eventual_Taylor_coefficient_period':480,
        'period_starts_after_degree':max_poly_degree,
        'exact_difference_to_Taylor_conversion_checks':conversion_checks,
        'first_32_O_coefficients_mod8':coeff[0][:32],
        'first_32_E_coefficients_mod8':coeff[1][:32],
        'exact_endpoint_digit_requires_coupled_Gram_transfer':True,
        'q2_equals_n_plus2_not_proved':True,
    }
    (BASE/'WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('eventual_Taylor_coefficient_period',
                    'period_starts_after_degree','exact_difference_to_Taylor_conversion_checks')},indent=2))


if __name__=='__main__':run()
