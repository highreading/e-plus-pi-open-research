"""Primary-agent algebra review of the last accepted report; no new research sampling.

Written independently from the retained transfer and definitions. The program
does not load API responses, external code, credentials, or network resources.
Only bounded rational-polynomial identities are checked.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

OUT = Path(__file__).resolve().parent
n = s.symbols('n', integer=True, positive=True)
P, Q, F, h, ell = s.symbols('P Q F h ell')
m, N, J, K = n+1, n+2, n+3, n+4
H, c = n*n+3*n+1, 2*n+3

def transfer(x):
    a, b, hh = x+1, x+2, x*x+3*x+1
    return s.Matrix([[0, a*b, b/s.Integer(2)],
        [b, -hh, -x*b/(2*a)],
        [-b*(2*x+3), b*hh, b*(x*x-2)/(2*a)]])

U = transfer(n)
inv = s.Matrix([[2*H, 3*m*N, m], [N*N, c*N, N],
    [-2*m*H, -2*m*c*N, -2*m*N]])/(m*N*J)
checks = {}

def check(name, expression):
    terms = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residuals = [s.cancel(x) for x in terms]
    checks[name] = all(x == 0 for x in residuals)
    if not checks[name]:
        raise AssertionError(name)

check('natural_transfer_determinant', U.det()-m*N*N*J/2)
check('paid_inverse_identity', inv*U-s.eye(3))
A = m*(2*n*n+9*n+8)
B = 3*n*n+7*n-2
AP = 5*n**3+28*n*n+43*n+18
BP = 8*n*n+25*n+11
target = s.Matrix([(AP*h+N*BP*ell)/(m*N*N*J*K),
    (c*J*h+m*(3*n+7)*ell)/(m*N*J*K),
    -2*(A*h+N*B*ell)/(N*N*J*K)])
check('actual_two_step_reference_all_three_coordinates',
    inv*inv.subs(n,n+1)*s.Matrix([h,ell,0])-target)
D, cp, E = 5*n*n+20*n+19, 2*n+5, 3*n+7
X, Y = s.symbols('X Y')
G = N*(D*X-c*J*Y)*(c*J*X+m*E*Y)-m*(J*Y-cp*X)*(AP*X+N*BP*Y)
K1 = 7*n**3+54*n*n+127*n+92
K2 = n**5+19*n**4+118*n**3+311*n*n+347*n+124
R = s.expand(N*(D*N*B+c*J*A)*K1+m*N*(J*A+cp*N*B)*K2)
check('first_resultant_simplification', m*E*A-c*J*N*B-K1)
check('second_resultant_simplification', BP*A-AP*B-K2)
check('homogeneous_resultant_identity', G.subs({X:-N*B,Y:A})+R)
check('two_step_second_observation',
    ((D*h-c*J*ell)/(m*N))*target[1]
    -((J*ell-cp*h)/N)*target[0]-G.subs({X:h,Y:ell})/(m*m*N**3*J*K))

z = s.Matrix([P,Q,F]); znext = U*z
red = U[:2,:2]-znext[:2,:]/znext[2]*U[2,:2]
check('actual_seed_reduction_determinant',red.det()-U.det()*F/znext[2])
check('scalar_off_diagonal_numerator',red[0,1]+m*N*N*(2*c*P+3*F)/(2*znext[2]))

# The affine identity is checked without assuming free rows satisfy a syzygy.
ah, bl, AC, BC, CC, kap, scale = s.symbols('ah bl AC BC CC kap scale')
vec_h=s.Matrix([ah,bl,0]); vec_a=s.Matrix([AC,BC,CC])
M=Q*ah-P*bl; transverse=ah*BC-bl*AC
theta=CC*M+F*(kap-transverse)
check('complete_cross_affine_sign',scale*z.dot(vec_h.cross(vec_a))-scale*(kap*F-theta))
Gni, Gnexti, fi = s.symbols('Gni Gnexti fi')
xf, yf, zf = s.symbols('xf yf zf')
coefficient=ah*(2*n+1)-m*(ah+bl)/2
check('final_source_coefficient',coefficient-((3*n+1)*ah-m*bl)/2)
check('two_final_source_substitutions',
    coefficient*(yf-xf+zf)/n+ah*(3*xf-yf-zf)/2
    -(((3*n+1)*ah-m*bl)/2*(yf-xf+zf)/n+ah/2*(3*xf-yf-zf)))

result={'scope':'Bounded independent primary-agent algebra review, not an infinite-family proof or an external audit.',
    'checks':checks,'all_zero':all(checks.values()),
    'resultant_degree':int(s.degree(R,n)),'resultant_leading_coefficient':int(s.LC(s.Poly(R,n))),
    'resultant_coefficients':[int(x) for x in s.Poly(R,n).all_coeffs()],
    'not_verified':['subfactorial multiplicative-block cofactor', 'subfactorial joint saturation gcd',
        'all-prime primitive denominator', 'infinite nonzero whole-error bound',
        'patched chart clearer optimality or subfactorial size'],
    'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target_file=OUT/'final_backward_defect_identity_certificate.json'
target_file.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_zero':result['all_zero'],'checks':len(checks),
    'resultant_degree':int(result['resultant_degree']),'resultant_leading_coefficient':8,
    'code_sha256':result['code_sha256'],
    'artifact_sha256':hashlib.sha256(target_file.read_bytes()).hexdigest()}))
