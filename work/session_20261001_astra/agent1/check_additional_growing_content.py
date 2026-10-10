"""Symbolic structural checks; no actual degree or prime scan."""
import json
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
x = s.symbols('x', positive=True)
k = s.symbols('k', integer=True, nonnegative=True)
r,n,m,l,L = s.symbols('r n m l L', integer=True)
F = s.Function('F')(x)
H = x**(-k)*F
checks = {}

# Translate the known H recurrence to F_k=x^k H_k.
next_F = x**(k+1)*(x*s.diff(H,x,2)/2+(k+1-x)*(s.diff(H,x)-H))
operator = (x*x*s.diff(F,x,2)+2*x*(1-x)*s.diff(F,x)+(2*x*x-2*x-k*(k+1))*F)/2
checks['F_operator_from_H_recurrence'] = s.simplify(s.expand(next_F-operator)) == 0

# Translate the third-order differential identity.
old_ode = x*s.diff(H,x,3)+(k+2-2*x)*s.diff(H,x,2)+2*(x-1)*s.diff(H,x)-2*k*H
new_ode = x*x*s.diff(F,x,3)+((2-2*k)*x-2*x*x)*s.diff(F,x,2)+(k*(k-1)+(4*k-2)*x+2*x*x)*s.diff(F,x)-(2*k*k+4*k*x)*F
checks['F_third_order_ODE'] = s.simplify(s.expand(x**(k+1)*old_ode-new_ode)) == 0

# Differentiate the ODE r times, using Leibniz with quadratic coefficients.
e = {j:s.symbols('E'+str(j)) for j in range(-2,4)}
expanded_ode = (e[3]+2*r*e[2]+r*(r-1)*e[1]
    -2*k*e[2]-2*r*(k+1)*e[1]-2*r*(r-1)*e[0]
    +k*(k+3)*e[1]+r*(4*k+2)*e[0]+2*r*(r-1)*e[-1]
    -2*k*(k+2)*e[0]-4*k*r*e[-1])
compact_ode = (e[3]-2*(k-r)*e[2]+(k-r)*(k-r+3)*e[1]
    -2*(k-r)*(k-r+2)*e[0]-2*r*(2*k-r+1)*e[-1])
checks['endpoint_derivative_recurrence'] = s.expand(expanded_ode-compact_ode) == 0
checks['spectral_row_factor'] = s.expand((l+m)*(2*n+l-m+1)-(l*(l+2*n+1)+m*(2*n+1-m))) == 0
checks['column_shift_k_minus_r'] = s.expand((n+l)-(l+m)-(n-m)) == 0

# Taylor coefficients a_(k,r)=E_(k,r)/r!: the k recurrence is integral.
a = {j:s.symbols('a'+str(j)) for j in range(-2,3)}
leibniz_divided = ((r+2)*(r+1)*a[2]+2*r*(r+1)*a[1]
    +(r*(r-3)-k*(k+1))*a[0]-2*(r-2)*a[-1]+2*a[-2])/2
integral_rec = ((r+2)*(r+1)*a[2]/2+r*(r+1)*a[1]
    +(r*(r-3)-k*(k+1))*a[0]/2-(r-2)*a[-1]+a[-2])
checks['factorial_normalized_integral_recurrence'] = s.expand(leibniz_divided-integral_rec) == 0

# An integral three-state transition generates the actual H states.
h,u,v = s.symbols('h u v')
hp = -k*h+k*(k*u)+k*(k-1)*v/2
up = (k+1)*(h-k*u+k*(k-1)*v/2)
vp = (k+1)*(k*h+k*u-(k+2)*k*(k-1)*v/2)
T = s.Matrix([[-k,k*k,k*(k-1)/2],[1,-k,k*(k-1)/2],[1,1,1-k*(k+1)/2]])
checks['integral_three_state_transition'] = all(s.simplify(value)==0 for value in s.Matrix([hp,up/(k+1),vp/(k*(k+1))])-T*s.Matrix([h,u,v]))
checks['three_state_determinant'] = s.factor(T.det()-k*(k-1)*(k+1)**2/2) == 0

# Formal column recurrence. L is an independent spectral indeterminate.
# Twelve abstract columns are checked; no HP degree is specialized.
initial = s.eye(4)
cols = [initial[:,j] for j in range(4)]
for j in range(8):
    nxt = (2*(n-j)*cols[j+3]-(n-j)*(n-j+3)*cols[j+2]
        +2*(n-j)*(n-j+2)*cols[j+1]
        +2*(L+j*(2*n+1-j))*cols[j])
    cols.append(nxt.applyfunc(s.expand))
# Coordinates in the ordered basis (2L)^q times starting vector s.
C = s.zeros(12)
for j,column in enumerate(cols):
    for seed in range(4):
        pol = s.Poly(column[seed],L)
        for (power,),coefficient in pol.terms():
            if coefficient == 0:
                continue
            index = 4*power+seed
            assert index <= j
            value = s.cancel(coefficient/2**power)
            assert s.Poly(value,n).domain == s.ZZ
            C[index,j] = value
checks['formal_columns_unitriangular_over_Z_n'] = all(C[i,i]==1 for i in range(12)) and all(C[i,j]==0 for i in range(12) for j in range(i))
checks['formal_column_change_determinant_one'] = C.det() == 1

# Exact scaling to the monic cleared endpoints.
rho,Gamma,d,f,Fclear,Ustar,Dstar,sign = s.symbols('rho Gamma d f Fclear Ustar Dstar sign', nonzero=True)
pow2 = s.symbols('pow2', nonzero=True)
M = pow2*Fclear**2*rho
X = Gamma*d*f*Ustar/(rho*sign*pow2)
Y = Gamma*d*f*Dstar/(rho*sign*pow2)
checks['monic_cleared_endpoint_X_scale'] = s.cancel(M*X-Gamma*d*Fclear**2*f*Ustar/sign)==0
checks['monic_cleared_endpoint_Y_scale'] = s.cancel(M*Y-Gamma*d*Fclear**2*f*Dstar/sign)==0

assert all(checks.values()),checks
result = {
    'status':'PASS_SYMBOLIC_STRUCTURAL_IDENTITIES',
    'checks':checks,
    'scope':'Symbolic recurrences, twelve abstract columns, and endpoint scale. No actual HP degree, prime list, or numerical content scan.',
    'column_recurrence':'R_(l,m+4)=2(n-m)R_(l,m+3)-(n-m)(n-m+3)R_(l,m+2)+2(n-m)(n-m+2)R_(l,m+1)+2[lambda_l+m(2n+1-m)]R_(l,m)',
    'lambda_l':'l(l+2n+1)',
    'transformed_column_j':'(2 diag(lambda_l))^floor(j/4) times original column (j mod 4)',
    'paper_proofs_required':['All-size unimodular transformation by induction','Four-group generalized Vandermonde minor expansion','No double counting of A_b^2 within Crows*mu','Integrality of the translated endpoint pair and exact gcd factorization'],
    'new_positive_quadratic_log_divisor_claimed':False,
    'independent_review':False
}
output = BASE/'additional_growing_content_certificate.json'
output.write_text(json.dumps(result,indent=2)+'\n')
assert json.loads(output.read_text()) == result
print(json.dumps(result,indent=2))
