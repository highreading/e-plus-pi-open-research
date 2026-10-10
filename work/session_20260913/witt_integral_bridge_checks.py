"""Bounded exact normalization checks; the all-row bridge is proved in the review."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,math
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
spec=importlib.util.spec_from_file_location('witt_integral_helpers',ROOT/'scripts/item424_small_prime_witt_escape_certificate.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)


def coefficient(m,nu):
    at=4*m+nu;extra=1+3*nu;denpow=4*m+1+nu
    return sum((-1)**t*math.comb(denpow+t-1,t)*sum((-1)**(at-2*t-k)*math.comb(6*m,at-2*t-k)*math.comb(extra,k)
             for k in range(extra+1) if 0<=at-2*t-k<=6*m) for t in range(at//2+1))


def run():
    rows=[]
    for m,p,j,s in [(2,11,0,1),(3,17,0,2),(9,13,1,1),(13,11,2,1)]:
        r=(p-6*s-3)//2
        assert 4*m+1==(2*j+1)*p-2*s and 6*m==(3*j+1)*p+r
        assert 3*j+1<p and p*p>4*m+1
        chi=(-1)**((p-1)//2)
        omega=[];projected=[];W=[]
        for nu in (0,1):
            num=helper.poly_power(helper.U_POLY,6*m)
            original=helper.mixed_coordinates(num,4*m+1+nu)
            P=helper.poly_mul(helper.poly_power(helper.U_POLY,r),helper.poly_power(helper.Q,2*s-nu))
            T=helper.primitive_zero(P)
            D=list(map(F,[3*j+1,-5*j-2,-5*j-2,-5*j-2,1]))
            N=helper.poly_mul(T,D)
            H=[sum((N[p*n-4*z] for z in range(p) if 0<=p*n-4*z<len(N)),F(0)) for n in range(5)]
            mapped=helper.mixed_coordinates(helper.poly_mul(helper.poly_power(helper.U_POLY,3*j),H),2*j+2)
            w=[helper.mod_fraction(original[0],p),helper.mod_fraction(original[1]/p,p),helper.mod_fraction(original[2]/p,p)]
            e=[helper.mod_fraction(v,p) for v in mapped]
            assert w==[(-e[0])%p,(-e[1])%p,(-chi*e[2])%p]
            C=coefficient(m,nu)
            assert original[1]==F(C,2**(2*m+2*nu))
            omega.append(original);projected.append(e);W.append(w)
        minors=[(W[0][a]*W[1][b]-W[1][a]*W[0][b])%p for a,b in [(0,1),(0,2),(1,2)]]
        assert any(minors)
        rho0,l0,e0=omega[0][0],omega[0][1]/p,omega[0][2]/p
        rho1,l1,e1=omega[1][0],omega[1][1]/p,omega[1][2]/p
        K=l1*rho0-l0*rho1;X=l1*e0-l0*e1
        vp=lambda v:helper.valuation_fraction(v,p) if v else float('inf')
        t=min(vp(l0),vp(l1));d=min(vp(K),1+vp(X))
        assert min(vp(K),vp(X))==t and t<=d<=t+1
        rows.append(dict(m=m,p=p,j=j,s=s,r=r,chi=chi,projected_RLE=projected,integral_W_mod_p=W,
                         full_pair_minors=minors,min_log_valuation=t,postbaseline_depth=d))
    return dict(status='PASS',scope='Four exact normalization checks in both Frobenius classes; no all-row theorem inferred from samples.',
                helpers='Archived rational polynomial arithmetic and Hermite reduction only; no archived census replay.',rows=rows)


if __name__=='__main__':
    result=run();Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'rows':len(result['rows'])}))
