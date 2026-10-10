"""Bounded exact identity checks; these do not prove the all-index theorem."""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
y = sp.Symbol('y')
exact = []
for M in (1, 7, 100):
    a = sp.Rational(2*M-1, 2)
    def moment(poly):
        return sp.Add(*(coef/(a+degree[0]+1)
                        for degree, coef in sp.Poly(poly, y).terms()))
    for j in range(7):
        pj = sp.jacobi(j, a, 0, 3)
        lead = 2**j * sp.binomial(a+j, j)
        remainder = sum(sp.ff(j, ell)**2 /
                        (2**ell * sp.factorial(ell) * sp.rf(a+1, ell))
                        for ell in range(j+1))
        assert sp.simplify(pj-lead*remainder) == 0
        qj = sp.jacobi(j, 0, a, 2*y-1)
        norm = moment(qj**2)
        assert norm == 1/(2*j+a+1)
        diag = sp.Rational(1,2)*(1+a*a/((2*j+a)*(2*j+a+2)))
        assert sp.simplify(moment(y*qj**2)/norm-diag) == 0
        if j:
            qprev = sp.jacobi(j-1, 0, a, 2*y-1)
            normprev = moment(qprev**2)
            offsq = (j*(j+a))**2 / ((2*j+a)**2*((2*j+a)**2-1))
            assert sp.simplify(moment(y*qj*qprev)**2/(norm*normprev)-offsq) == 0
        exact.append({'M': M, 'j': j, 'finite_sum': True,
                      'norm': True, 'diagonal': True, 'offdiag_square': j > 0})

mp.mp.dps = 70
numerical = []
for k in (24, 50, 100, 200):
    j = k-1
    for M in (16*k, k*k, k**3, 2**k):
        zeta = mp.mpf(M)+mp.mpf('0.5')
        lam = mp.mpf(j*j)/(2*zeta)
        term = mp.mpf(1)
        remainder = term
        for ell in range(1,j+1):
            term *= mp.mpf((j-ell+1)**2)/(2*ell*(zeta+ell-1))
            remainder += term
        logr = mp.log(remainder)
        deficit = lam-logr
        upper = 2+mp.log(j+1)/2+mp.mpf(j)**3/(mp.mpf(M)**2)
        assert -mp.mpf('1e-60') <= deficit <= upper
        xi = (mp.mpf(1)/j+1/(2*zeta))*lam*lam
        if xi < 1:
            assert mp.exp(-lam)*remainder >= 1-xi-mp.mpf('1e-60')
        numerical.append({'k': k, 'M': str(M), 'log_R': mp.nstr(logr,25),
                          'lambda_minus_log_R': mp.nstr(deficit,25),
                          'explicit_bound': mp.nstr(upper,25),
                          'relative_Poisson_loss_bound': mp.nstr(xi,25)})

receipt = {'scope': 'Finite algebra/inequality diagnostics only; not all-degree proof, actual denominator arithmetic, or rationality proof.',
           'exact_checks': exact, 'remainder_checks': numerical,
           'status': 'PASS'}
(HERE/'SHIFTED_SHORT_UNBOUNDED_JACOBI_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'exact_identity_cases': len(exact),
                  'remainder_cases': len(numerical)}))
