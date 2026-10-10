"""Parent-authored bounded audit of NEW endpoint and complete-arc constants."""
from pathlib import Path
from math import comb, factorial
import hashlib, json, time
import sympy as sp

HERE=Path(__file__).resolve().parent
started=time.monotonic()
P=17
source_path=HERE/'signed_chebyshev_affine_midpoint_algebra_certificate.json'
theta_path=HERE/'signed_integral_theta_refinement_certificate.json'
source=json.loads(source_path.read_text())
theta=json.loads(theta_path.read_text())
assert source['all_checks_passed'] and theta['all_checks_passed']

def eval_low(arr,n,mod=None):
    value=sum(int(v)*n**j for j,v in enumerate(arr))
    return value if mod is None else value%mod

weights=[1,8,58,168,399,-176,-916,-176,399,168,58,8,1]
assert sum(weights)==sum((-1)**j*weights[j] for j in range(13))==0
A=eval_low(source['A_coefficients_low_first'],9,P)
B=eval_low(source['B_coefficients_low_first'],9,P)
CU=eval_low(theta['CU_coefficients_low_first'],9,P)
omega=[0,0]
for k in range(1,12):
    omega.append((omega[k-1]+4*(9-k)*omega[k]-2*(-1)**k)%P)
CE=(-1849344+sum(weights[k]*(9-k)*omega[k] for k in range(13)))%P
assert [A,B,CU,CE]==[7,1,11,0]
assert omega==[0,0,2,3,8,8,2,13,6,1,8,1,2]

def rec(sign,last):
    values=[0,1]
    for j in range(1,last):
        values.append((sign*4*j*values[j]+values[j-1]+2)%P)
    return values

Tminus=rec(-1,26)
Tplus=rec(1,26)
indices=[8,9,25,26]
assert [Tminus[j] for j in indices]==[2,11,15,7]
assert [Tplus[j] for j in indices]==[14,16,10,12]
for sign, values in [(-1,Tminus),(1,Tplus)]:
    for j in range(1,27):
        direct=sum((sign*4)**r*factorial(r)*comb(j+r,2*r+1)
                   for r in range(j))%P
        assert direct==values[j]
    assert (values[25]-values[8])%P==13
    assert (values[26]-values[9])%P==13

def gaussian_period(z):
    values=[1,z]
    for j in range(1,41):
        values.append((2*z*values[-1]-values[-2])%P)
        if (values[-2],values[-1])==(1,z):
            return j,values
    raise AssertionError('Period does not return within the bounded range')

plus_period,gaussian_plus=gaussian_period(7)
minus_period,gaussian_minus=gaussian_period(8)
assert [plus_period,minus_period]==[9,3]
inverse2=pow(2,-1,P)
inverse8=pow(8,-1,P)
aN=(gaussian_plus[0]+gaussian_minus[0])*inverse2%P
bN=(gaussian_plus[0]-gaussian_minus[0])*inverse8%P
aPrev=(gaussian_plus[8]+gaussian_minus[2])*inverse2%P
bPrev=(gaussian_plus[8]-gaussian_minus[2])*inverse8%P
assert [aN,bN,aPrev,bPrev]==[1,0,16,2]

ell,u,x,n=sp.symbols('ell u x n')
U=(CU-A*(11+13*ell)-B*(2+13*ell))*pow(4096,-1,P)
scaledV=-4*9*(11+13*ell)
EK=(A*(1-13*ell)+B*(14+13*ell)+CE)*pow(4096,-1,P)
def mod_poly(expr,var):
    return sp.Poly(sp.expand(expr),var,modulus=P)

assert mod_poly(U-2*ell,ell).is_zero
assert mod_poly(scaledV-12-8*ell,ell).is_zero
assert mod_poly(EK-13-10*ell,ell).is_zero
assert mod_poly(scaledV-4*U-12,ell).is_zero
assert mod_poly(EK-5*U-13,ell).is_zero
assert mod_poly(U.subs(ell,2+3*u)-4-6*u,u).is_zero
assert mod_poly(scaledV.subs(ell,2+3*u)-11-7*u,u).is_zero
assert mod_poly(EK.subs(ell,2+3*u)-16-13*u,u).is_zero
assert pow(9,18,289)==166 and pow(9,32,289)==103
assert (2*166-9-17*2)%289==0
assert (2*166*6*17-17*3)%289==0

L=(x-1)*(x-9)*(x-25)
AK=13*x**3-455*x**2+3502*x-5850
assert sp.expand(AK-13*L-45*(3*x-65))==0
assert sp.expand(27*L-(3*x-65)*(9*x**2-120*x-269)+23560)==0
assert sp.expand(L.subs(x,(n-6)**2)-
    (n-7)*(n-5)*(n-9)*(n-3)*(n-11)*(n-1))==0
assert int(AK.subs(x,9))==-1710 and int(AK.subs(x,9))%17!=0
arc_cap=1350*23560
assert arc_cap==31806000 and arc_cap%17!=0
cap_factors={int(p):int(e) for p,e in sp.factorint(arc_cap).items()}
assert cap_factors=={2:4,3:3,5:3,19:1,31:1}

# Check the NEW endpoint coordinate directly on small integral polynomials;
# no source moment, source content or rational normalization is recomputed.
t=sp.symbols('t')
def endpoint(poly):
    obj=sp.Poly(poly,t,domain=sp.ZZ)
    return sum(int(obj.nth(j))*(-1)**j*factorial(j)
               for j in range(obj.degree()+1))

phis=[0]+[endpoint(sp.chebyshevu(j-1,2*t-1)) for j in range(1,9)]
for j in range(1,9):
    assert endpoint(sp.chebyshevt(j,2*t-1))==(-1)**j-2*j*phis[j]
for j in range(1,8):
    assert phis[j+1]+4*j*phis[j]-phis[j-1]==2*(-1)**j

receipt={
    'all_checks_passed':True,'coordinator_authored':True,
    'external_code_executed':False,'network_or_credentials_used':False,
    'source_arrays_reused':['A','B','CU'],
    'source_receipt_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
    'theta_receipt_sha256':hashlib.sha256(theta_path.read_bytes()).hexdigest(),
    'report_sha256':hashlib.sha256((HERE.parent/'responses/A5_turn8.md').read_bytes()).hexdigest(),
    'boundary_indices':indices,'Tminus_values':[Tminus[j] for j in indices],
    'Tplus_values':[Tplus[j] for j in indices],
    'local_A_B_CU_CE':[A,B,CU,CE],'alternating_local_omega':omega,
    'Gaussian_periods':{'i4':plus_period,'i_minus4':minus_period},
    'original_Gaussian_boundary_residues':[aN,bN,aPrev,bPrev],
    'original_exponent_mod289':{'9pow18':166,'9pow32':103,
                               'symbolic_affine_residuals':[0,0]},
    'source_endpoint_mod17_symbolic_residuals':[0]*8,
    'arc_polynomial_residuals':[0,0,0],
    'arc_cancellation_cap':arc_cap,'arc_cap_factorization':cap_factors,
    'small_integral_Phi_values':phis,
    'numeric_h_lambda_G_q_recomputed':False,
    'scope':'NEW finite arithmetic for the original17 theorem and complete K arc; not a uniform all-prime mass theorem, producer retirement or e+pi decision.',
    'seconds':round(time.monotonic()-started,3),
    'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(HERE/'signed_endpoint17_arc_arithmetic_certificate.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'Gaussian_periods':[plus_period,minus_period],
                 'endpoint_source_residuals':8,'arc_residuals':3,
                 'arc_cap':arc_cap,'seconds':receipt['seconds']}),flush=True)
