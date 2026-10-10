import json
import sympy as sp
import mpmath as mp

# Finite reference identities supplement, but do not replace, the author proof.
mp.mp.dps = 70
x = sp.symbols('x')
legendre_checks = []
for i in range(9):
    n = 2*i
    p = sp.legendre(n, x)
    identity = sp.integrate(x*p*p, (x, 0, 1)) - p.subs(x, 0)**2/2
    assert sp.simplify(identity) == 0
    if n:
        lam = n*(n+1)
        energy = (1-x*x)**2*sp.diff(p,x)**2 + lam*(1-x*x)*p*p
        assert sp.expand(sp.diff(energy,x)+2*lam*x*p*p) == 0
    b = sp.Rational(1,2) + sp.Rational(1,2*(4*i-1)*(4*i+3))
    diag = (4*i+1)*sp.integrate(x*x*p*p, (x,0,1))
    assert sp.simplify(diag-b) == 0
    a = sp.Rational((2*i+1)*(2*i+2),4*i+3)/sp.sqrt((4*i+1)*(4*i+5))
    off = sp.sqrt((4*i+1)*(4*i+5))*sp.integrate(x*x*p*sp.legendre(n+2,x),(x,0,1))
    assert sp.simplify(off-a) == 0
    for j in range(i+1):
        coefficient = abs(sp.expand(p).coeff(x,2*j))
        bound = sp.Rational((4*(i+1))**(2*j),sp.factorial(2*j))
        assert coefficient <= bound
    legendre_checks.append({'i':i,'integral_identity':True,'jacobi_diagonal':True,'jacobi_off_diagonal':True,'coefficient_bound':True})

# The rational Legendre basis is diagonally similar to the orthonormal one.
# It permits exact finite checks of the compression boundary support.
def jacobi_rational(size):
    J = sp.zeros(size)
    for j in range(size):
        J[j,j] = sp.Rational(1,2)+sp.Rational(1,2*(4*j-1)*(4*j+3))
        if j+1 < size:
            J[j+1,j] = sp.Rational((2*j+1)*(2*j+2),(4*j+1)*(4*j+3))
        if j:
            J[j-1,j] = sp.Rational(2*j*(2*j-1),(4*j+1)*(4*j-1))
    return J

boundary_checks = []
for k,d in [(4,1),(5,2),(6,3),(8,4)]:
    J = jacobi_rational(k+d)
    Jk = J[:k,:k]
    for power in range(d+1):
        diff = (J**power)[:k,:k]-Jk**power
        for i in range(k):
            for j in range(k):
                if i < k-d or j < k-d:
                    assert diff[i,j] == 0
        assert diff.rank() <= d
    boundary_checks.append({'k':k,'d':d,'exact_boundary_support':True})

Z = 5*mp.pi*mp.exp(mp.mpf(5)/144)/432
zeta_checks = []
for k in [1,2,4,16,128,1024]:
    zeta = mp.fsum((mp.mpf(4*i+1)/2)*(mp.binomial(2*i,i)/mp.power(4,i))**2 for i in range(k))
    rem = zeta-2*k/mp.pi-mp.mpf('0.5')+2/mp.pi
    assert abs(rem) <= Z
    zeta_checks.append({'k':k,'zeta_remainder':str(rem),'absolute_bound':str(Z)})

parameter_checks = []
for k in [131072,262144,1048576,10**8]:
    h = mp.sqrt(8*mp.log(k)/k)
    u = 4*k*h
    r = int(mp.ceil(4*u))
    d = int(mp.ceil(mp.power(k,mp.mpf(4)/5)))
    assert h < mp.mpf('0.5')
    assert u >= mp.log(k)
    assert 1 <= d < k
    tail_log = u + 2*r*mp.log(mp.e*u/(2*r))
    assert tail_log <= -7*u
    assert 128*mp.power(k,-11) <= 1
    E = mp.sqrt(2)*mp.e*k/mp.power(d,mp.mpf(1)/4)+(mp.e-1)*d+mp.sqrt(mp.mpf(43)*k/72)+1
    bump = r*mp.log(32*k+2)+64*mp.power(k,-11)+8*mp.power(k,-2)
    parameter_checks.append({'k':k,'d':d,'r':r,'baseline_error_bound':str(E),'bump_logdet_bound':str(bump)})

receipt = {
    'status':'passed',
    'classification':'finite_reference_checks_not_all_degree_verification',
    'legendre_exact_checks':legendre_checks,
    'compression_exact_checks':boundary_checks,
    'zeta_high_precision_checks':zeta_checks,
    'large_parameter_high_precision_checks':parameter_checks,
    'note':'No actual primitive coefficient gcd or inherited nonvanishing assertion was numerically verified. The all-index argument is in COMPLETE_ERROR_CONTENT_THRESHOLD_STAGE1_V2.md.'
}
with open('COMPLETE_ERROR_CONTENT_THRESHOLD_REFINEMENT_RECEIPT.json','w') as f:
    json.dump(receipt,f,indent=2)
print(json.dumps({'status':'passed','legendre_sizes':len(legendre_checks),'boundary_cases':len(boundary_checks),'zeta_cases':len(zeta_checks),'parameter_cases':len(parameter_checks),'receipt':'COMPLETE_ERROR_CONTENT_THRESHOLD_REFINEMENT_RECEIPT.json'}))
