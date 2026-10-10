"""Parent-authored bounded algebra for the newly received integral refinement.

Reuse the prior immutable A/B/Qloc*E arrays. Check only the new constant
forcing, denominator cancellation and formal return identities. No numerical
research index, prime-jet table, full normalization or final q is recomputed.
"""
from pathlib import Path
import hashlib
import json
import time
import sympy as s

OUT = Path(__file__).resolve().parent
started = time.monotonic()
prior = OUT/'signed_chebyshev_affine_midpoint_algebra_certificate.json'
data = json.loads(prior.read_text())
assert data['all_checks_passed']
n, j = s.symbols('n j')
alpha, beta, delta, X, Y = s.symbols('alpha beta delta X Y')

def from_low(values):
    return s.Poly(sum(s.Integer(v)*n**i for i, v in enumerate(values)), n, domain=s.ZZ)

A = from_low(data['A_coefficients_low_first']).as_expr()
B = from_low(data['B_coefficients_low_first']).as_expr()
QE = from_low(data['Q_local_E_coefficients_low_first'])
w = [1,8,58,168,399,-176,-916,-176,399,168,58,8,1]
assert sum(w) == 0
kappa = [s.Integer(0), s.Integer(0)]
for k in range(1,12):
    kappa.append(s.expand(kappa[k-1]+4*(n-k)*kappa[k]-2))
CU = s.Poly(679936-sum(w[k]*(n-k)*kappa[k] for k in range(13)), n, domain=s.ZZ)
assert CU.degree() == 11 and CU.LC() == 2**21
removed = s.Poly(s.prod(n-r for r in range(2,13)), n, domain=s.ZZ)
E_num, remainder = s.div(QE, removed)
assert remainder.is_zero and E_num.degree() == 11
constant_residual = s.expand(E_num.as_expr()-2*n*(n-1)*CU.as_expr()+(n-1)*A+n*B)
assert constant_residual == 0

E = E_num.as_expr()/(n*(n-1))
P = n*alpha**2+(n-2)*beta**2
Q = 4*(n-1)*(n-2)*beta**2-2*(n-1)*alpha*beta
CV = alpha**2+(2*n-3)*beta**2-delta**2
T_old = (alpha+beta)**2-2*delta**2+2*beta**2/n
T_residual = s.cancel(T_old-(2*CV-P/n-Q/(n-1)))
assert T_residual == 0
Delta = s.expand(A*Q-B*P)
rn = Q*CU.as_expr()-B*CV
rn1 = A*CV-P*CU.as_expr()
U_formal = (CU.as_expr()-A*X-B*Y)/4096
V_formal = CV-P*X-Q*Y
z_residual = s.expand(4096*Q*U_formal-B*V_formal+Delta*X-rn)
z1_residual = s.expand(A*V_formal-4096*P*U_formal+Delta*Y-rn1)
rho_residual = s.cancel(Q*E-B*T_old-2*rn+Delta/n)
rho1_residual = s.cancel(A*T_old-P*E-2*rn1+Delta/(n-1))
forcing_residual = s.cancel(1/(j+1)+2/(j*j-1)-1/(j-1))
assert all(v == 0 for v in [z_residual,z1_residual,rho_residual,rho1_residual,forcing_residual])

def low(poly):
    return [int(v) for v in reversed(poly.all_coeffs())]

receipt = {
    'all_checks_passed': True,
    'scope': 'New fixed12-step integral Theta constant and exact denominator cancellation; formal integer terminal and full forced-return identities only. Not a strict content-saving, final-q or irrationality theorem.',
    'network_or_credentials_used': False,
    'prior_certificate_sha256': hashlib.sha256(prior.read_bytes()).hexdigest(),
    'A3_turn6_sha256': hashlib.sha256((OUT.parent/'responses/A3_turn6.md').read_bytes()).hexdigest(),
    'source_coefficients_reused': ['A','B','Q_local_E'],
    'new_kappa_steps': 12,
    'sum_weights': 0,
    'CU_coefficients_low_first': low(CU),
    'n_times_nminus1_E_coefficients_low_first': low(E_num),
    'CU_degree': CU.degree(),
    'CU_leading_coefficient': int(CU.LC()),
    'n_times_nminus1_E_degree': E_num.degree(),
    'removed_denominator_factors': list(range(2,13)),
    'exact_zero_residuals': {name: str(value) for name,value in [
        ('CU_E',constant_residual), ('CV_T',T_residual),
        ('z_n',z_residual), ('z_nminus1',z1_residual),
        ('rho_n',rho_residual), ('rho_nminus1',rho1_residual),
        ('rational_forcing',forcing_residual)]},
    'numeric_h_lambda_G_q_recomputed': False,
    'seconds': round(time.monotonic()-started,3),
    'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(OUT/'signed_integral_theta_refinement_certificate.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'CU_degree':CU.degree(),
                  'CU_leading_coefficient':int(CU.LC()),'cancelled_factors':11,
                  'seconds':receipt['seconds']}),flush=True)
