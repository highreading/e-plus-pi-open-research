"""New symbolic arithmetic only; no contact solves or old audit replay."""
import hashlib
import json
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra')
OUT = BASE / 'agent4'
source_names = [
    'agent3/CONTACT_NORMALITY_RESEARCH.md',
    'agent3/CONTACT_INVERSE_RESEARCH.md',
    'agent2/MULTIROW_REMAINDER_RESEARCH.md',
    'RATIONAL_CENTER_PAIR_CRITERION.md',
    'agent4/SLOW_GROWTH_NORMALITY_REVIEW.md',
    'agent4/ENDPOINT_LATTICE_RESEARCH.md',
]
protected = {}
for name in source_names:
    path = BASE / name
    if path.is_symlink():
        raise RuntimeError('Unexpected symbolic link')
    protected[name] = hashlib.sha256(path.read_bytes()).hexdigest()
checks = []

def equal(name, left, right):
    if s.simplify(left-right) != 0:
        raise AssertionError(name)
    checks.append(name)

g,k,c,t,d,tau,zeta,A,H,C,kap,dk,gamma,b = s.symbols(
    'g k c t d tau zeta A H C kap dk gamma b', nonzero=True)
D = A*C-H**2
c0 = g*k*c
Kgram = s.Matrix([[A,H],[H,C]])
R = s.Matrix([[g,k*t],[0,k*c]])
Sigma = tau**2/d**2 * R.T*Kgram*R
U, V, WW = Sigma[0,0], Sigma[0,1], Sigma[1,1]
Delta = s.factor(Sigma.det())
G = 2*(s.Matrix([[0,0],[0,1]])+zeta*Sigma)
q = g*A/kap
p = k*(t*A+c*H)/kap

equal('Sigma first entry', U, tau**2*g**2*A/d**2)
equal('Sigma mixed entry', V, tau**2*g*k*(t*A+c*H)/d**2)
equal('Sigma determinant', Delta, tau**4*c0**2*D/d**4)
equal('center preserved by complete pi term', G[0,1]/G[0,0], V/U)
equal('complete determinant', G.det(), 4*zeta*(U+zeta*Delta))
equal('complete directional defect', G.det()/G[0,0]**2,
      1/(zeta*U)+Delta/U**2)
equal('B directional defect', Delta/U**2, (k*c/g)**2*D/A**2)
equal('center fraction', p/q, V/U)
equal('center-vector first basis coordinate', -g*p+k*t*q, -c0*H/kap)
equal('center-vector second basis coordinate', k*c*q, c0*A/kap)
equal('center-vector squared B norm',
      (s.Matrix([[-p,q]])*Sigma*s.Matrix([-p,q]))[0],
      tau**2*c0**2*A*D/(d**2*kap**2))
equal('q squared times B directional defect', q**2*Delta/U**2,
      (k*c)**2*D/kap**2)

zeta_value = (b+1)*(gamma/dk)**2
H0 = 2*(b+1)*gamma**2*tau**2/d**2
E = (dk**2*G[0,0]/q**2).subs(zeta,zeta_value)
F = (dk**2*G.det()*q**2/G[0,0]).subs(zeta,zeta_value)
equal('exact E after gcd reduction', E, H0*kap**2/A)
equal('exact F retaining pi contribution', F,
      (2*dk**2*g**2*A**2+H0*c0**2*A*D)/kap**2)
equal('pair-product invariant', E*F,
      2*H0*dk**2*g**2*A+H0**2*c0**2*D)

ell = s.symbols('ell', integer=True)
shift = s.symbols('shift')
equal('transverse basis change preserves numerator',
      (t+c*shift)*A+c*(H-shift*A), t*A+c*H)
equal('transverse basis change preserves determinant',
      A*(C-2*shift*H+shift**2*A)-(H-shift*A)**2, D)

# One abstract symbolic weighted array checks polynomial bookkeeping only.
# It is not actual Hermite-Pade data and supplies no asymptotic evidence.
x = [s.Integer(1),s.Integer(-1),s.Integer(0)]
z = [s.Integer(0),s.Integer(1),s.Integer(1)]
weights = [s.Integer(1),ell,ell*(ell-1)]
a_poly = s.expand(sum(weights[j]**2*x[j]**2 for j in range(3)))
h_poly = s.expand(sum(weights[j]**2*x[j]*z[j] for j in range(3)))
c_poly = s.expand(sum(weights[j]**2*z[j]**2 for j in range(3)))
d_poly = s.expand(a_poly*c_poly-h_poly**2)
wedge_poly = sum(weights[i]**2*weights[j]**2*(x[i]*z[j]-x[j]*z[i])**2
                 for i in range(3) for j in range(i+1,3))
equal('weighted Cauchy-Binet polynomial', d_poly, wedge_poly)
for name, poly, order in [('A',a_poly,5),('H',h_poly,5),('D',d_poly,7)]:
    difference = s.expand(poly)
    for _ in range(order):
        difference = s.expand(difference.subs(ell,ell+1)-difference)
    equal('finite difference polynomial '+name, difference, 0)

for name, old in protected.items():
    if hashlib.sha256((BASE/name).read_bytes()).hexdigest() != old:
        raise AssertionError('Input changed: '+name)
result = {
    'status':'PASS_NEW_SYMBOLIC_IDENTITIES',
    'scope':'Formal Gram/gcd substitutions and one abstract weight-polynomial identity; no actual contact indices, no prime scan, no old checker.',
    'checks':checks,
    'check_count':len(checks),
    'all_inputs_unchanged':True,
    'source_sha256':protected,
    'limits':'Divisibility theorems are proved in the research note; symbolic identities do not prove their asymptotic hypotheses.'
}
(OUT/'rational_center_structure_checks.json').write_text(json.dumps(result,indent=2)+'\n')
summary = {key:result[key] for key in ['status','check_count','scope','all_inputs_unchanged']}
text = json.dumps(summary,indent=2)+'\n'
(OUT/'rational_center_structure_stdout.txt').write_text(text)
print(text,end='')
