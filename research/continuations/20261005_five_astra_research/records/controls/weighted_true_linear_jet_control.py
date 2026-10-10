"""Exact formal first derivatives from the complete moment series.
Coordinator-authored rational calculation, with an explicit infinite tail
bound; not inference of a Taylor coefficient from function values.
"""
import math,json,resource
from fractions import Fraction as Q
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;precision=6;mod=3**precision;cutoff=60
def val(n):
    if not n:return None
    v=0
    while n%3==0:n//=3;v+=1
    return v
def residue(x,m=mod):
    assert x.denominator%3!=0
    return x.numerator*pow(x.denominator,-1,m)%m
def pell_derivative(r,ell):
    if ell==0:return Q(0)
    if ell>r:
        return Q(((-1)**(r+1))*math.factorial(ell-r-1)*math.factorial(r+ell),
                 (2**ell)*math.factorial(ell))
    values=[r+a for a in range(-ell+1,ell+1)]
    total=sum(math.prod(values[:i]+values[i+1:]) for i in range(len(values)))
    return Q(((-1)**ell)*total,(2**ell)*math.factorial(ell))
def original_moment(r):
    return ((-2)**r)*sum(Q(((-1)**ell)*math.prod(r+a for a in range(-ell+1,ell+1)),
                           (2**ell)*math.factorial(ell)) for ell in range(r+1))
moments=[original_moment(r) for r in range(4)]
assert moments==[1,0,4,40]
logminus8=-sum(Q(9**k,k) for k in range(1,8))
# Terms beyond cutoff have Gauss valuation >=ell/6-1>=9, including
# the first derivative coefficient after substituting s=3T+r.
# The log tail k>=8 has valuation 2k-v3(k)>=15. Thus precision6 is safe,
# including the later single division by3.
derivatives=[logminus8*moments[r]+3*((-2)**r)*sum(pell_derivative(r,ell)
               for ell in range(cutoff)) for r in range(4)]
e0prime=4*derivatives[0]+4*derivatives[1]+36+2*derivatives[2]
e1prime=4*derivatives[1]+8*derivatives[2]+6*derivatives[3]+648
Hprime=2*e0prime/3;Gprime=3*272+2*e1prime
thetaprime=(4*Gprime-272*Hprime)/16
Nthetaprime=3*68+thetaprime
report={'method':'actual coefficient derivative of complete factorial moment expansion',
        'modulus':mod,'moment_cutoff_exclusive':cutoff,
        'infinite_omitted_derivative_tail_depth_lower_bound':9,
        'log_tail_depth_lower_bound':15,
        'moments_at0':[int(x) for x in moments],
        'B_derivatives_mod729':[residue(x) for x in derivatives],
        'e0prime_mod729':residue(e0prime),'e1prime_mod729':residue(e1prime),
        'Hprime_mod729':residue(Hprime),'Gprime_mod729':residue(Gprime),
        'Theta_raw_prime_mod729':residue(thetaprime),
        'NTheta_raw_prime_mod729':residue(Nthetaprime),
        'Hprime_mod9':residue(Hprime,9),'Gprime_mod9':residue(Gprime,9),
        'Theta_raw_prime_mod9':residue(thetaprime,9),
        'NTheta_raw_prime_mod9':residue(Nthetaprime,9),
        'projection_and_factorial_tail_transfer_not_proved_by_this_control':True}
assert report['Hprime_mod9']==report['Gprime_mod9']==3
assert report['Theta_raw_prime_mod9']==6
assert report['NTheta_raw_prime_mod9']==3
(OUT/'weighted_true_linear_jet_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
