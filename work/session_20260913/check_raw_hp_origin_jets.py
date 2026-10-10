"""Exact origin recurrence controls against the original raw high-jet rows."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'math_packages'))
import sympy as s
from check_raw_hp_homogeneous_ode import raw_row, atan, z, D

def check(n):
    A, B, C = raw_row(n)
    fj = {j: s.diff(1 / D, z, j - 1) for j in range(1, 4)}
    mat = s.Matrix([
        [s.diff(A, z, r) + sum(s.binomial(r, j) * s.diff(C, z, r-j) * fj[j]
                              for j in range(1, r+1)),
         sum(s.binomial(r, j) * s.diff(B, z, j) for j in range(r+1)),
         s.diff(C, z, r)] for r in range(4)])
    wr = lambda rows: s.cancel(mat.extract(rows, [0,1,2]).det())
    w = wr([0,1,2])
    coeffs = [s.cancel(-z * wr([0,1,3]) / w),
              s.cancel(z**2 * wr([0,2,3]) / w),
              s.cancel(-z**3 * wr([1,2,3]) / w)]
    jets = [[s.expand(s.series(f, z, 0, 8).removeO()).coeff(z, j)
             for j in range(8)] for f in coeffs]
    t = s.symbols('t')
    I = s.expand(t*(t-1)*(t-2) + jets[0][0]*t*(t-1) + jets[1][0]*t + jets[2][0])
    high = [k for k in range(3*n+1, 3*n+5) if I.subs(t,k)==0]
    assert len(high)==1
    M = high[0]
    u = [s.S.One]
    for r in range(1,8):
        numerator = sum(((M+r-j)*(M+r-j-1)*jets[0][j]
                         +(M+r-j)*jets[1][j]+jets[2][j])*u[r-j]
                        for j in range(1,r+1))
        assert I.subs(t,M+r) != 0
        u.append(s.cancel(-numerator / I.subs(t,M+r)))
    def raw_coefficient(k):
        return A.coeff(z,k) + sum(B.coeff(z,j)/s.factorial(k-j) + C.coeff(z,j)*atan(k-j)
                                   for j in range(min(k,n)+1))
    assert all(raw_coefficient(k)==0 for k in range(M))
    leading = raw_coefficient(M)
    assert leading != 0
    assert all(u[r] == raw_coefficient(M+r)/leading for r in range(8))
    Q = s.cancel(D**2*w/z**(3*n-1))
    h = min(s.Poly(Q,z).monoms())[0]
    roots = sorted(int(k) for k in s.roots(I,t))
    assert len(roots)==3 and sum(roots)==3*n+2+h
    assert sum(roots[:2])<=4
    return {'n':n, 'indicial_roots':roots, 'origin_Q_order':h,
            'eight_relative_coefficients_match':True}

if __name__=='__main__':
    out = {'status':'PASS', 'checks':[check(n) for n in (1,3,5)],
           'scope':'Finite exact controls; exceptional-origin theorem proved separately.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))
