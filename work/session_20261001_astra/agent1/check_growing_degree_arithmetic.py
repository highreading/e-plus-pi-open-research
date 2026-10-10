"""Formal checks for growing-degree endpoint arithmetic.
No numerical degree evaluation, prime list, or seed recomputation.
Integrality and all-index functional identities require the written proof.
"""
import json
from hashlib import sha256
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
checks = {}

# Rodrigues coefficient normalization and the high-row derivative index.
k,m = s.symbols('k m', integer=True, nonnegative=True)
a = s.symbols('a')
left = 2**k*a*s.factorial(k+m)/(s.factorial(k)*s.factorial(m))/s.factorial(k+m)
right = 2**k/s.factorial(k)**2*s.factorial(k)*a/s.factorial(m)
checks['Rodrigues_coefficient_normalization'] = s.simplify(left-right)==0
n,l,j,z = s.symbols('n l j z', integer=True)
checks['high_row_factorial_index'] = s.expand((n+l)+z-(l+j-1)-(n+z+1-j))==0
monic_scalar = (2**k/s.factorial(k)**2)/(2**k*s.factorial(2*k)/s.factorial(k)**2)
checks['monic_high_row_scalar'] = s.simplify(monic_scalar-1/s.factorial(2*k))==0

# Universal alternating-form calculation in the span of e, uhat, p.
# B(e,uhat)=-sigma, B(e,p)=-c, B(uhat,p)=kappa.
t,f,G,A,B,wp,wu,TP0,TU0,Ac,Bc,sigma,c,kappa = s.symbols(
    't f G A B wp wu TP0 TU0 Ac Bc sigma c kappa')
Jmat = s.Matrix([[0,-sigma,-c],[sigma,0,kappa],[c,-kappa,0]])
def bracket(u,v):
    return (u.T*Jmat*v)[0]
e = s.Matrix([1,0,0])
uhat = s.Matrix([0,1,0])
p = s.Matrix([0,0,1])
TU = TU0*e-2*f*uhat/t
TP = TP0*e-f*p
endpoint_t = (A*TU-B*TP)/G
endpoint_x = (wp*TU-wu*TP)/G
Y = bracket(e+endpoint_t,e)
X = bracket(e+endpoint_t,endpoint_x)
D = t*B*c-2*A*sigma
Ufull = 2*(wp+TP0)*sigma-t*(wu+TU0)*c-2*f*kappa
checks['universal_endpoint_Y'] = s.cancel(Y-f*D/(t*G))==0
checks['universal_endpoint_X_with_Wronskian'] = s.cancel(
    (X-f*Ufull/(t*G)).subs(G,A*wu-B*wp))==0
Q = 2*wp*sigma-t*wu*c
V = sigma*Ac-c*Bc-kappa
checks['complete_partial_exponential_contraction'] = s.cancel(
    Ufull.subs({TP0:f*Ac,TU0:2*f*Bc/t})-(Q+2*f*V))==0
checks['second_kind_coefficient_determinant'] = s.cancel(
    ((A*(-wu)-(-B)*wp)/G**2+1/G).subs(G,A*wu-B*wp))==0

# Removing a proved common scalar from the three integer contractions.
d = s.symbols('d')
checks['scalar_content_denominator_factor'] = s.expand(
    D.subs({sigma:d*sigma,c:d*c,kappa:d*kappa}, simultaneous=True)-d*D)==0
checks['scalar_content_full_numerator_factor'] = s.expand(
    (Q+2*f*V).subs({sigma:d*sigma,c:d*c,kappa:d*kappa}, simultaneous=True)
    -d*(Q+2*f*V))==0

# General Laplace-sign convention, checked with a formal 2-by-4 block.
# Matrix size is a formal linear-algebra example, not an HP degree sample.
r0 = list(s.symbols('r00:04'))
r1 = list(s.symbols('r10:14'))
u = list(s.symbols('u0:4'))
v = list(s.symbols('v0:4'))
R = s.Matrix([r0,r1])
expanded = s.Integer(0)
for i in range(4):
    for jj in range(i+1,4):
        columns = [q for q in range(4) if q not in (i,jj)]
        minor = R.extract([0,1],columns).det()
        expanded += (-1)**(i+jj+1)*minor*(u[i]*v[jj]-u[jj]*v[i])
checks['signed_integer_minor_expansion'] = s.expand(
    s.Matrix([r0,r1,u,v]).det()-expanded)==0
c0,c1 = s.symbols('c0 c1')
checks['high_row_contents_factor_from_every_endpoint'] = s.expand(
    s.Matrix([[c0*q for q in r0],[c1*q for q in r1],u,v]).det()
    -c0*c1*s.Matrix([r0,r1,u,v]).det())==0

# b=2 specialization, using exactly the established normalized symbols.
a,h,J,kadj,ell = s.symbols('a h J kadj ell')
high = [a,t*kadj,t*ell]
e3 = [1,1,1]
u3 = [0,kadj,kadj+ell]
p3 = [0,h,h+J]
sigma2 = -s.Matrix([high,e3,u3]).det()
c2 = -s.Matrix([high,e3,p3]).det()
kappa2 = s.Matrix([high,u3,p3]).det()
expected_sigma = t*kadj**2-a*ell
expected_c = (t*kadj-a)*J-t*(ell-kadj)*h
omega = kadj*J-ell*h
checks['b2_sigma'] = s.expand(sigma2-expected_sigma)==0
checks['b2_C'] = s.expand(c2-expected_c)==0
checks['b2_kappa_retains_H_times_omega'] = s.expand(kappa2-a*omega)==0
Sold = (t*kadj)**2-a*t*ell
Wold = t*kadj*J-t*ell*h
Vold = Sold*Ac-t*expected_c*Bc-a*Wold
Vtilde2 = expected_sigma*Ac-expected_c*Bc-a*omega
Xold = 2*(wp+f*Ac)*Sold-t**2*(wu+2*f*Bc/t)*expected_c-2*f*a*Wold
Dold = t**2*B*expected_c-2*A*Sold
checks['b2_original_V_factor'] = s.expand(Vold-t*Vtilde2)==0
checks['b2_original_complete_X_factor'] = s.cancel(
    Xold-t*(2*wp*expected_sigma-t*wu*expected_c+2*f*Vtilde2))==0
checks['b2_original_D_factor'] = s.expand(
    Dold-t*(t*B*expected_c-2*A*expected_sigma))==0

# b=1: the high block is empty and its unique empty minor is one.
sigma1 = -s.Matrix([[1,1],[0,kadj]]).det()
c1value = -s.Matrix([[1,1],[0,h]]).det()
kappa1 = s.Matrix([[0,kadj],[0,h]]).det()
checks['b1_empty_block_orientation'] = (sigma1,c1value,kappa1)==(-kadj,-h,0)

assert all(checks.values()), {key:value for key,value in checks.items() if not value}
result = {
    'status':'PASS_FORMAL_IDENTITIES',
    'scope':'Symbolic coefficient, alternating-form, common-factor, and b=1/b=2 compatibility checks. No actual degree evaluation or prime computation.',
    'checks':checks,
    'normalized_quotient':{
        'D':'(n+1) P_(n+1) c - 2 P_n sigma',
        'Q':'2 w_P sigma - (n+1) w_U c',
        'V':'sigma Acal_n - c Bcal_n - kappa',
        'ratio':'(Q + 2^(n+1) V/(n!)^2)/D'
    },
    'paper_proofs_required':[
        'Extension of elementary endpoint formulas to all 0<=j<=b<=n.',
        'Integer derivative entries and divisibility E_(k,r) by k for r>=1.',
        'Cancellation of row contents, maximal-minor content, and scalar contraction content.',
        'Explicit rational clearer and exact final endpoint gcd.'
    ],
    'no_growing_degree_nonvanishing_claim':True,
    'independent_researcher_review':False,
    'checker_sha256':sha256((BASE/'check_growing_degree_arithmetic.py').read_bytes()).hexdigest()
}
output = BASE/'growing_degree_arithmetic_certificate.json'
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
assert json.loads(output.read_text(encoding='utf-8'))==result
print(json.dumps(result,indent=2))
