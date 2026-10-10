"""Exact symbolic fixed-d coefficient and rational interval checks on saved pairs."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import hashlib,json,sys
import sympy as sp

OUT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(20000)

def symbolic():
    d=sp.symbols('d',integer=True,positive=True);sig=sp.sqrt(2);alpha=2-sig
    a4=alpha/24-alpha**2/8
    def values(p,eps):
        c=sig+p;u=(sig-p+p*p)/2;v=(sig+p-3*p*p+2*p**3)/6
        m1=d/alpha*(sig+p-d/2)
        h1=d*(d-1)/alpha*(sig+p-(d-1)/2)
        m2=(-3*d*d*v+(2*d*c-d*d)*u+d*c*c/2-c*d*d/2+(4*d**3-d)/24)/alpha**2
        m2+=a4/alpha**3*(12*c*d*d-4*d**3-2*d)
        be=sig/(sig+eps)
        s2=d/(alpha*be)*((d-1)*p**3+eps*p*p/2)
        return m1,m2+s2,h1
    minus=values(sig/2,-1);plus=values((2-sig)/2,1)
    diff=[sp.simplify(a-b) for a,b in zip(minus,plus)]
    target=[d/sig,2*d+sig*d*(2-d)/2,d*(d-1)/sig]
    assert all(sp.simplify(a-b)==0 for a,b in zip(diff,target))
    cubic_difference=-sig*diff[1]+sig*(d-1)*diff[0]+2*diff[2]
    cubic_ratio=sp.simplify(cubic_difference-sig*d*d)
    assert sp.simplify(cubic_ratio-d*(2*d-3-3*sig))==0
    return {'differences_m1_m2joint_h1':list(map(str,diff)),
            'endpoint_ratio_cubic_coefficient':str(cubic_ratio),
            'd2_extrapolated_relative_coefficient':str(sp.simplify(cubic_ratio.subs(d,2)/2)),
            'status':'EXACT_Q_SQRT2_ALGEBRA_MATCHES_REPORT',
            'scope':'Finite symbolic algebra only; localization and remainder estimates require analytic review.'}

def arctan_bounds(base,terms):
    val=sum((F((-1)**k,(2*k+1)*base**(2*k+1)) for k in range(terms)),F(0))
    err=F(1,(2*terms+1)*base**(2*terms+1))
    return (val,val+err) if terms%2==0 else (val-err,val)

def e_pi_bounds(terms=256):
    ev=sum((F(1,factorial(k)) for k in range(terms+1)),F(0))
    eu=ev+F(terms+2,(terms+1)*factorial(terms+1))
    al,au=arctan_bounds(5,terms);bl,bu=arctan_bounds(239,terms)
    return ev+16*al-4*bu,eu+16*au-4*bl

def main():
    sy=symbolic();lo,hi=e_pi_bounds()
    pairs=json.loads((OUT/'endpoint_extrapolant_certificate.json').read_text())['cases']
    data=[]
    for item in pairs:
        p=int(item['p_hat']);q=int(item['q_hat']);assert q>0
        lower=q*lo-p;upper=q*hi-p
        assert lower>0 or upper<0,(item['n'],item['d'])
        absolute=lower if lower>0 else -upper
        exponent=absolute.numerator.bit_length()-absolute.denominator.bit_length()-1
        assert absolute>F(2**exponent) if exponent>=0 else absolute>F(1,2**(-exponent))
        assert exponent>0
        eb_num=int(item['actual_V'][-1])-int(item['actual_U'][-1])*lo
        eb_num2=int(item['actual_V'][-1])-int(item['actual_U'][-1])*hi
        assert eb_num*eb_num2>0
        data.append({'n':item['n'],'d':item['d'],'whole_qS_minus_p_sign':1 if lower>0 else -1,
                     'whole_absolute_form_strictly_greater_than_2_power':exponent,
                     'saved_pair_sha256':hashlib.sha256((str(p)+'/'+str(q)).encode()).hexdigest(),
                     'endpoint_b_error_nonzero_interval':True,
                     'scope':'Exact finite complete primitive pair; no asymptotic inference from this interval.'})
    cert={'status':'SYMBOLIC_DEFECT_AND16_RATIONAL_NONVANISHING_INTERVALS_PASS',
          'symbolic':sy,'e_factorial_terms':256,'Machin_terms_each_arctan':256,
          'S_interval_sha256':hashlib.sha256((str(lo)+'\n'+str(hi)).encode()).hexdigest(),
          'cases':data,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/'endpoint_defect_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps(cert))

if __name__=='__main__':main()
