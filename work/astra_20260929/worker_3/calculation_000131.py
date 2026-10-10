import sys
sys.path.insert(0, '[private local path removed]')
import sympy as sp
import json
u = sp.symbols('u')
m = 5*u
h = 1 + 5*u**2
j = 2 + 10*u + 10*u**2
k = -2 + 10*u - 10*u**2
hn = 20*u
Jn = -2 + 15*u**2
A = 18 + 10*u + 15*u**2
B = 5*(u+1)
T = m*j**2 - h*k
V = j*Jn - k*hn
C = (m*j-h)*Jn - m*(k-j)*hn
checks = {
    'T': (T, 2+10*u+20*u**2),
    'V': (V, -4+20*u+10*u**2),
    'C': (C, 2+5*u-5*u**2),
    '2AT': (2*A*T, 22+5*u**2),
    'BC': (B*C, 10+10*u),
    '2hV': (2*h*V, 17+15*u+5*u**2),
    'complete_F': (2*A*T-B*C-2*h*V, 20),
}
for name, (actual, expected) in checks.items():
    polynomial = sp.Poly(sp.expand(actual-expected), u)
    assert all(int(coefficient) % 25 == 0 for coefficient in polynomial.all_coeffs()), name
expressions = {'h':h, 'j':j, 'k':k, 'h_n':hn, 'J_n':Jn, 'A':A, 'B':B, 'T':T, 'V':V, 'C':C, '2AT':2*A*T, 'BC':B*C, '2hV':2*h*V, 'F':2*A*T-B*C-2*h*V}
rows = []
for n in (14,19,24,29,34):
    row = {'n':n, 'u':(n+1)//5}
    row.update({name:int(expression.subs(u,row['u'])) % 25 for name,expression in expressions.items()})
    rows.append(row)
print(json.dumps({'coefficientwise_congruences_passed':list(checks), 'modulus':25, 'table_from_proved_reductions':rows, 'scope':'Author substitution audit; original endpoint reconstructions not rerun; no independent approval.'}, indent=2))