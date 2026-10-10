import sys, json, time
sys.path.insert(0, '[private local path removed]')
import sympy as s
from pathlib import Path

base = Path(__file__).parent
n = int(sys.argv[1]); d = n+1
h, w = s.symbols('h w')
old = s.sympify(json.loads((base/f'fixed_weight_kernel_n{n}.json').read_text())['P'])
P = s.Poly(s.cancel(old/(2*(1-w*w))**d),w)
print('half kernel degree',P.degree(),flush=True)

# Rational state (D_h,A_h,B_h), with D_h=i integral z^h,
# A_h=(1-i)^h+(1+i)^h, B_h=i((1-i)^h-(1+i)^h).
# Forward state is M(h) times the current state.
def trans(t):
    return s.Matrix([[(2*t+2)/(2*t+3),0,1/(2*t+3)],
                     [0,1,-1],[0,1,1]])

def reduced(M):
    return M.applyfunc(s.cancel)

shifts = [s.eye(3)]
for j in range((P.degree()+1)//2+3):
    shifts.append(reduced(trans(h+j)*shifts[-1]))

# Output is i integral P(w) z(w)^h dw. The omitted actual W factor is 2^(n+1).
row = s.zeros(1,3)
for k in range(P.degree()+1):
    p = P.nth(k)
    if not p: continue
    ell = k//2
    for j in range(ell+1):
        b = p*s.binomial(ell,j)*(-1)**j
        if k%2==0:
            row += b*s.Rational(1,2**ell)*shifts[j][0,:]
        else:
            row -= b*s.Rational(1,2**(ell+2))*shifts[j+1][2,:]/(h+j+1)
row = reduced(row)
print('base output row reduced',flush=True)
rows = [row]
for j in (1,2):
    rows.append(reduced(row.subs(h,h+j)*shifts[j]))
O = s.Matrix.vstack(*rows)
print('three outputs assembled',flush=True)
det = s.cancel(O.det(method='domain-ge'))
print('determinant canceled',flush=True)
num,den = map(s.expand,det.as_numer_denom())
facnum,facden = s.factor(num),s.factor(den)
print('numerator factor',facnum,flush=True)
print('denominator factor',facden,flush=True)
poly = s.Poly(num,h)
roots = int(poly.count_roots(0,s.oo))
print('degree',poly.degree(),'nonnegative roots',roots,flush=True)
data={'n':n,'half_kernel':str(P.as_expr()),'row':[str(e) for e in row],
      'determinant':str(det),'numerator_factor':str(facnum),
      'denominator_factor':str(facden),'numerator_degree':poly.degree(),
      'nonnegative_roots':roots,'numerator_coefficients_positive':all(c>0 for c in poly.all_coeffs())}
(base/f'half_step_observability_n{n}.json').write_text(json.dumps(data,indent=2))
print('saved',flush=True)
