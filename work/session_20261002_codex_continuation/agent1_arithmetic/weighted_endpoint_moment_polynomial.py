"""L24 exact four-exponential integer-valued polynomial moment chart.

The finite rational partial-fraction calculation proves the representation;
bounded coefficient comparisons only check its normalization.
"""
from pathlib import Path
from math import comb
import json
from weighted_endpoint_spectral import ZERO,ONE,add,sub,scale,mul,power,inverse,root15
from weighted_branch_mod8_lift import series
from weighted_endpoint_binary_inverse import rho

BASE=Path(__file__).resolve().parent


def solve(a,rhs):
    n=len(a);width=len(rhs[0]);mat=[a[i][:]+rhs[i][:] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if any(x%2 for x in mat[i][j]))
        mat[j],mat[p]=mat[p],mat[j]
        iv=inverse(mat[j][j]);mat[j]=[mul(iv,x) for x in mat[j]]
        for i in range(n):
            if i==j:continue
            c=mat[i][j]
            if c!=ZERO:mat[i]=[sub(x,mul(c,y)) for x,y in zip(mat[i],mat[j])]
    return [row[n:] for row in mat]


def newton(values):
    out=[]
    while values:
        out.append(values[0])
        values=[sub(values[i+1],values[i]) for i in range(len(values)-1)]
    return out


def run():
    saved=json.loads((BASE/'WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json').read_text())
    zeta=root15();nus=(1,2,4,8);roots=[];units=[]
    def char(z):return sub(sub(add(add(power(z,4),power(z,3)),scale(power(z,2),2)),scale(z,4)),scale(ONE,3))
    def deriv(z):return sub(add(add(scale(power(z,3),4),scale(power(z,2),3)),scale(z,4)),scale(ONE,4))
    for nu in nus:
        teich=power(zeta,nu);z=teich
        for _ in range(2):z=sub(z,mul(char(z),inverse(deriv(z))))
        assert char(z)==ZERO
        principal=sub(mul(z,inverse(teich)),ONE)
        assert all(x%2==0 for x in principal)
        roots.append(z);units.append(tuple(x//2 for x in principal))
    A=[[scale(power(root,r),comb(r+s-1,s-1)) for root in roots for s in range(1,6)]
       for r in range(20)]
    proper=[series(num,saved['common_denominator_D_power5'],20)
            for num in saved['proper_numerators_O_E_mod8']]
    answers=solve(A,[[(proper[j][r],0,0,0) for j in range(2)] for r in range(20)])
    partial=[[[answers[5*i+s][j] for s in range(5)] for i in range(4)] for j in range(2)]
    def q(branch,i,r):
        z=ZERO
        for s,coef in enumerate(partial[branch][i]):z=add(z,scale(coef,comb(r+s,s)))
        unit=add(add(ONE,scale(units[i],2*r)),scale(mul(units[i],units[i]),4*comb(r,2)))
        return mul(z,unit)
    def p(start,i,r):
        branch=0 if start%2 else 1;c=start//2
        af=(r+1)*c+comb(r+1,2)
        bf=comb(r+2,2)*c*c+(r+2)*c*comb(r+1,2)+comb(r+2,3)+3*comb(r+2,4)
        teich=power(zeta,nus[i])
        return add(add(q(branch,i,r),scale(mul(teich,q(branch,i,r+1)),2*af)),
                   scale(mul(power(teich,2),q(branch,i,r+2)),4*bf))
    polys=[]
    for start in range(1,5):
        modes=[]
        for i,nu in enumerate(nus):
            coeff=newton([p(start,i,r) for r in range(11)])
            assert newton([p(start,i,r) for r in range(12)])[-1]==ZERO
            modes.append({'frequency':nu,'integer_valued_Newton_coefficients':coeff})
        polys.append({'starting_b_index':start,'four_modes':modes})
    original=[series(num,saved['common_denominator_D_power5'],164)
              for num in saved['numerators_O_E_mod8']]
    checks=0;origin_defects=[]
    for start in range(1,5):
        branch=0 if start%2 else 1;c=start//2
        for r in range(161):
            got=ZERO
            for i,nu in enumerate(nus):got=add(got,mul(power(zeta,nu*r),p(start,i,r)))
            expected=rho(original[branch],r,c)
            if r:
                assert got==(expected,0,0,0);checks+=1
            else:origin_defects.append({'starting_b_index':start,
                         'actual_minus_positive_order_chart':sub((expected,0,0,0),got)})
    out={'status':'AUTHOR exact finite rational moment-polynomial representation',
         'coefficient_ring':'(Z/8)[x]/(x^4+x+1)',
         'zeta_coefficients':zeta,'actual_recurrence_roots':roots,
         'principal_units_lambda_over_zeta_minus1_div2':units,
         'proper_branch_partial_fraction_coefficients_O_E':partial,
         'positive_order_rho_polynomials_degree_at_most10':polys,
         'order_zero_defects_retained':origin_defects,
         'coefficient_normalization_checks':checks,
         'internal_binomial_pairing_not_yet_evaluated':True}
    (BASE/'WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'degree_bound':10,'checks':checks,'origin_defects':origin_defects,
       'nonzero_polynomial_coefficient_orders':[[[r for r,a in enumerate(mode['integer_valued_Newton_coefficients']) if a!=ZERO]
                         for mode in group['four_modes']] for group in polys]},indent=2))


if __name__=='__main__':run()
