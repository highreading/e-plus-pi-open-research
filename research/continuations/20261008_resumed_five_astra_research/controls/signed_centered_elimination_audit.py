from pathlib import Path
import json
import hashlib
import datetime
import sympy as sp

HERE = Path(__file__).resolve().parent
R = HERE.parent
source_path = HERE / 'signed_chebyshev_affine_midpoint_algebra_certificate.json'
theta_path = HERE / 'signed_integral_theta_refinement_certificate.json'
source = json.loads(source_path.read_text())
theta = json.loads(theta_path.read_text())
assert source['all_checks_passed'] and theta['all_checks_passed']
x, ell, m0, m1 = sp.symbols('x ell m0 m1')
P = -8*x**3 - 1116*x**2 - 8150*x + 151
Q = 76*x**2 + 2408*x + 5637
F = 4*x**2 + 492*x + 5463
G = 4*x**2 + 556*x - 3325
checks = []


def check(name, residual, variables):
    residual = sp.expand(residual)
    assert residual == 0, name
    checks.append({'identity': name, 'zero_coefficient_residual': True})


H_coefficients = [0, 1, -1, 2, -2, 1, -1]
for boundary in (0, 1):
    moments = [m0, m1]
    for k in range(5):
        forcing = sp.Rational(2*boundary-1, 2) * (boundary**k)
        previous = 0 if k == 0 else k*sp.Rational(2*k+1, 2)*moments[k-1]
        moments.append(sp.expand(-2*(k+1)*moments[k+1]
                       + (x + sp.Rational(1, 2)-k*k)*moments[k]
                       + previous + forcing))
    full_moment = sum(c*moment for c, moment in zip(H_coefficients, moments))
    if boundary == 1:
        check('complete source centered moment',
              2656-8*full_moment-(F-P*m0-2*Q*m1), (x, m0, m1))
    else:
        check('complete endpoint centered moment',
              -7224+8*full_moment-(G+P*m0+2*Q*m1), (x, m0, m1))

check('first elimination constant',
      (6593*x+115642)*F-(347*x+37773)*Q-418825845, (x,))
check('second elimination constant',
      1735*P+4753*Q+(3470*x-33052)*F+153508430, (x,))
assert 4548519*418825845-12409985*153508430 == 5
Z_F = 4548519*(6593*x+115642)+12409985*(3470*x-33052)
Z_Q = -4548519*(347*x+37773)+12409985*4753
Z_P = 12409985*1735
check('integer elimination to5', Z_F*F+Z_Q*Q+Z_P*P-5, (x,))
H = 32*x**4+1252*x**3+6496*x**2+9851*x+1036
check('paid polynomial division by5',
      (2*x*x+4*x+1)*Q-(x+3)*P-4-5*H, (x,))
BF = sp.expand((1+H)*Z_F)
BQ = sp.expand((1+H)*Z_Q-(2*x*x+4*x+1))
BP = sp.expand((1+H)*Z_P+(x+3))
check('integer unit Bezout certificate', BF*F+BQ*Q+BP*P-1, (x,))
assert max(sp.Poly(p, x).degree() for p in (BF, BQ, BP)) <= 5
assert max(abs(int(c)) for p in (BF, BQ, BP) for c in sp.Poly(p, x).all_coeffs()) < 10**17

subs = {x: ell**2}
Pt, Qt, Ft, Gt = [p.subs(subs) for p in (P, Q, F, G)]
At = sp.expand(2*ell*((2*ell+1)*Qt-Pt))
Bt = sp.expand(-2*ell*Qt)
CUt = sp.expand(Ft-Pt+2*ell*Qt)
CEt = sp.expand(Gt+Pt-2*(ell+1)*Qt)
check('centered coefficient elimination to2ell',
      2*ell*BF.subs(subs)*CUt-(BF+BP).subs(subs)*At
      -(BF+BQ+(2*ell+1)*BP).subs(subs)*Bt-2*ell, (ell,))


def cached_poly(coefficients):
    return sp.expand(sum(int(c)*(ell+6)**j for j, c in enumerate(coefficients)))


A = cached_poly(source['A_coefficients_low_first'])
B = cached_poly(source['B_coefficients_low_first'])
CU = cached_poly(theta['CU_coefficients_low_first'])
weights = [1, 8, 58, 168, 399, -176, -916, -176, 399, 168, 58, 8, 1]
omega = [sp.Integer(0), sp.Integer(0)]
for k in range(1, 12):
    omega.append(sp.expand(omega[k-1]+4*(ell+6-k)*omega[k]-2*(-1)**k))
CE = sp.expand(-1849344+sum(weights[k]*(ell+6-k)*omega[k] for k in range(13)))
transfer = sp.eye(2)
fminus = sp.zeros(2, 1)
fplus = sp.zeros(2, 1)
for r in range(6):
    Hr = sp.Matrix([[-4*(ell+r), 1], [1, 0]])
    transfer = (Hr*transfer).applyfunc(sp.expand)
    fminus = (Hr*fminus+sp.Matrix([2, 0])).applyfunc(sp.expand)
    fplus = (Hr*fplus+sp.Matrix([2*(-1)**r, 0])).applyfunc(sp.expand)
assert sp.expand(transfer.det()) == 1
original_row = sp.Matrix([[A, B]])
new_row = original_row*transfer
check('original homogeneous row first component', new_row[0]-256*At, (ell,))
check('original homogeneous row second component', new_row[1]-256*Bt, (ell,))
check('original complete source constant', CU-(original_row*fminus)[0]-256*CUt, (ell,))
check('original complete alternating endpoint constant', CE+(original_row*fplus)[0]-256*CEt, (ell,))
assert int(F.subs(x, 0)-P.subs(x, 0)) == 5312 == 64*83
assert int(CUt.subs(ell, 0)) == 5312
assert int(CEt.subs(ell, 0)) == -14448
assert int(Qt.subs(ell, 0)) == 5637
assert int(CUt.subs(ell, 12)) % 8 == 0
assert int(Bt.subs(ell, 12)) % 16 == 8
assert int(At.subs(ell, 12)) % 16 == 0

sources = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in
           (source_path, theta_path, R/'responses/A5_turn10.md',
            HERE/'SIGNED_CENTERED_ELIMINATION_RECEIPT_GATE.md')}
out = {
    'status': 'PASS', 'time': datetime.datetime.now().astimezone().isoformat(),
    'scope': 'NEW exact centered polynomial identities and original six-step comparison; NOT factorial excess or a global proof.',
    'source_sha256': sources,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'cached_source_arrays_reused': ['A', 'B', 'CU'],
    'checks': checks,
    'six_step_transfer_determinant': 1,
    'centered_P_coefficients_low_first': [151, -8150, -1116, -8],
    'centered_Q_coefficients_low_first': [5637, 2408, 76],
    'centered_F_coefficients_low_first': [5463, 492, 4],
    'centered_G_coefficients_low_first': [-3325, 556, 4],
    'centered_CU_at_ell0': 5312, 'centered_CE_at_ell0': -14448,
    'integer_unit_certificate_degree_max': 5,
    'original_domain_binary_payment_modulus': 16,
    'full_content_theorem_external_audit_still_required': True,
    'factorial_excess_bound_proved': False, 'global_proof': False,
}
(HERE/'signed_centered_elimination_certificate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'new_exact_polynomial_checks': len(checks),
                  'six_step_transfer_determinant': 1, 'source_arrays_reused': ['A', 'B', 'CU'],
                  'factorial_excess_bound_proved': False, 'global_proof': False}))
