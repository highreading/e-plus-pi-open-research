from pathlib import Path
from math import comb,factorial
import hashlib,json,time
OUT=Path(__file__).resolve().parent
started=time.monotonic()
sourcepath=OUT/'signed_chebyshev_affine_midpoint_algebra_certificate.json'
thetapath=OUT/'signed_integral_theta_refinement_certificate.json'
source=json.loads(sourcepath.read_text());theta=json.loads(thetapath.read_text())
assert source['all_checks_passed'] and theta['all_checks_passed']
def poly(arr,n,mod):return sum(int(v)*pow(n,j,mod) for j,v in enumerate(arr))%mod
def rec(c,last,mod):
    a=[0,1]
    for j in range(1,last):a.append((c*j*a[-1]+a[-2]+2)%mod)
    return a
minus=rec(-4,126,25);plus=rec(4,26,5)
assert minus[125:127]==[0,1] and plus[25:27]==[0,1]
assert [a%5 for a in minus[:7]]==[0,1,3,4,2,4,4]
assert plus[:7]==[0,1,1,1,0,3,2]
def gauss(z,cap):
    v=[1,z%5]
    for j in range(1,cap):v.append((2*z*v[-1]-v[-2])%5)
    return v
gplus=gauss(3,8);gminus=gauss(0,6)
assert gplus[6:8]==[1,3] and gminus[4:6]==[1,0]
def gaussian_at(j):
    pp=gplus[j%6];mm=gminus[j%4]
    return ((pp+mm)*3%5,(pp-mm)*4%5)
assert gaussian_at(9)+gaussian_at(8)==(2,1,4,4)
weights=[1,8,58,168,399,-176,-916,-176,399,168,58,8,1]
omega=[0,0]
for j in range(1,12):omega.append((omega[j-1]+4*(2-j)*omega[j]-2*(-1)**j)%5)
CE=(-1849344+sum(weights[j]*(2-j)*omega[j] for j in range(13)))%5
assert [poly(source['A_coefficients_low_first'],2,5),
        poly(source['B_coefficients_low_first'],2,5),
        poly(theta['CU_coefficients_low_first'],2,5),CE]==[4,0,2,3]
def vp5(x):
    assert x
    a=0
    while x%5==0:x//=5;a+=1
    return a
def convolve(a,b,size):
    return [sum(a[j]*b[r-j] for j in range(len(a)) if 0<=r-j<len(b))
            for r in range(size)]
H=[0,4,-12,16,-12,5,-1]
# Directly transform the ORIGINAL H(t)=t(1-t)(1+t^2)^2.
oneplus=[2,-2,1]
assert convolve([0,1,-1],convolve(oneplus,oneplus,5),7)==H
C2sq=[1,-16,80,-128,64]
base=convolve(H,C2sq,11)
assert base==[0,4,-76,528,-1740,3269,-3857,2976,-1488,448,-64]
assert sum(factorial(j)*v for j,v in enumerate(base))%25==20
rows=[]
for u in range(25):
    N=pow(9,18+32*u);n=2*N;m=N-3
    assert N%12==9 and N%25==(21+5*u)%25
    A=poly(source['A_coefficients_low_first'],n%25,25)
    B=poly(source['B_coefficients_low_first'],n%25,25)
    CU=poly(theta['CU_coefficients_low_first'],n%25,25)
    Uaff=(CU-A*minus[n%125]-B*minus[(n-1)%125])*pow(4096,-1,25)%25
    coeff=[1]+[((-4)**r*(comb(m+r,2*r)+comb(m+r-1,2*r))//2)%25
               for r in range(1,10)]
    K=convolve(H,convolve(coeff,coeff,10),10)
    Udirect=-sum(factorial(r)*K[r] for r in range(10))%25
    assert Uaff==Udirect and Udirect%5==(1-u)%5
    EK=(-A*plus[n%25]+B*plus[(n-1)%25]+CE)%5
    assert EK==4*u%5
    Vscaled=(1-2*(minus[n%125]%5)-2*(minus[(n-1)%125]%5))%5
    assert Vscaled==3
    x=(n-6)**2
    L=(x-1)*(x-9)*(x-25)
    AK=13*x**3-455*x**2+3502*x-5850
    Den=30*L
    vden=vp5(Den);vak=vp5(AK);paid=min(vden,vak)
    denlocal=Den//(5**paid);alocal=AK//(5**paid)
    ylocal=(denlocal*EK-alocal)%5
    expected_ddepth=0 if u%5==1 else vp5(n-7)
    assert vden-paid==expected_ddepth
    Jdepth=1 if Udirect%5==0 and ylocal==0 else 0
    if Jdepth:assert Udirect==10 and u==21
    assert Jdepth==(1 if u==21 else 0)
    if u%5==1:
        t=(u-1)//5
        assert N%125==(1+25*t)%125
        assert Udirect==5*(1-t)%25
        assert alocal*pow(denlocal,-1,5)%5==(3+4*t)%5
        assert ylocal==denlocal*(1+t)%5
    rows.append({'u':u,'N_mod125':N%125,'U_mod25':Udirect,'E_K_mod5':EK,
                 'gB2_V_mod5':Vscaled,'arc_den_v5':vden,'arc_AK_v5':vak,
                 'paid_arc_gcd_v5':paid,'reduced_dK_v5':vden-paid,
                 'local_primitive_yK_is_zero_mod5':ylocal==0,
                 'intrinsic_J0_v5':Jdepth})
obj={'all_checks_passed':True,'coordinator_authored':True,
     'external_code_executed':False,'network_or_credentials_used':False,
     'source_arrays_reused':['A','B','CU'],
     'source_sha256':hashlib.sha256(sourcepath.read_bytes()).hexdigest(),
     'theta_sha256':hashlib.sha256(thetapath.read_bytes()).hexdigest(),
     'report_sha256':hashlib.sha256((OUT.parent/'responses/A5_turn9.md').read_bytes()).hexdigest(),
     'boundary_periods':{'Theta_mod25':125,'Tplus_mod5':25},
     'Gaussian_periods_mod5':[6,4],'Gaussian_gB_is_unit_mod5':True,
     'literal_Chebyshev_coefficient_max':9,'binomial_order_max':18,
     'original_u_range':[0,24],'original_N_exponent_max':786,
     'U_affine_vs_literal_positive_factorial_residuals':[0]*25,
     'rows':rows,'seconds':round(time.monotonic()-started,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact finite original indices modulo5/25/125 with paid local arc reduction. No aggregate mass or actual global normalization.'}
(OUT/'signed_prime5_intrinsic_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'original_indices_checked':25,
                  'distinct_U_evaluations_agree':True,'exception_u':21,
                  'intrinsic_exception_depth':1,'seconds':obj['seconds']}))
