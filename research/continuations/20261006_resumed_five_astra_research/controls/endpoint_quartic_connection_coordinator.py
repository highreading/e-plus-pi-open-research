#!/usr/bin/env python3
"""New exact symbolic audit and seeded recurrence corroboration.

Personally authored from the inspected identities; external code is not run.
No original-power or real-window conclusion is inferred from finite indices.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib
import json
import resource
import sympy as sp
import time

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
ROOT = Path(__file__).resolve().parent

def v3(x):
    assert x
    numerator, denominator = x.numerator, x.denominator
    value = 0
    while numerator % 3 == 0:
        numerator //= 3; value += 1
    while denominator % 3 == 0:
        denominator //= 3; value -= 1
    return value

def half_binomial(alpha, k):
    result = F(1)
    for r in range(k):
        result *= F(alpha-r,k-r)
    return result

def actual_endpoints(m):
    first = (-1)**m * sum((F(comb(3*m-1,k))*half_binomial(F(2*m-1,2),m-k)*2**(m-k) for k in range(m+1)),F(0))
    second = (-1)**(m-1) * sum((F(comb(3*m-2,k))*half_binomial(F(2*m-3,2),m-1-k)*2**(m-1-k) for k in range(m)),F(0))
    return first,second

def main():
    started = time.monotonic()
    x,n = sp.symbols('x n')
    C = sp.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[2*x,-x,0,1]])
    L = sp.Matrix([[x,0,-3,4],[8*x,-3*x,0,1],[2*x,7*x,-3*x,1],[2*x,x,7*x,1-3*x]])
    K = sp.Matrix([[-3*x,0,-1,1],[-10*x,2*x,0,0],[-4*x,-4*x,0,0],[-4*x,-2*x,0,-2*x]])
    N = sp.Matrix([[-sp.Rational(1,2),0,-1/(2*x),1/(2*x)],[3,-2,0,0],[0,5,-3,0],[0,0,7,-4]])
    assert (4*C**3-3*C**2+x*sp.eye(4)-L).applyfunc(sp.simplify) == sp.zeros(4)
    assert (2*x*N-2*x*L.diff(x)-K).applyfunc(sp.simplify) == sp.zeros(4)
    determinant_L = sp.factor(L.det())
    assert sp.expand(determinant_L+x*x*(27*x*x+1264*x+108)) == 0
    D = (6*n+1)*(6*n+3)
    alpha = n*(82*n+27)/D
    beta = -(10*n+3)*(3*n-1)/D
    p = -7*n*(68*n*n+68*n+15)/((n+1)*D)
    q = (3*n-1)*(62*n*n+59*n+12)/((n+1)*D)
    T = sp.Matrix([[( (8*n+7)*p+(2*n+3)*alpha)/(6*n+5),((8*n+7)*q+(2*n+3)*beta)/(6*n+5)],[p,q]])
    expected_T = n*(3*n-1)*(3*n+1)*(2*n+3)/((n+1)*(6*n+1)*(2*n+1)*(6*n+5))
    assert sp.cancel(T.det()-expected_T) == 0
    O = sp.Matrix([[-n*(394*n*n+367*n+78)/((n+1)*D),(3*n-1)*(52*n*n+46*n+9)/((n+1)*D)],
                    [n*(22*n+7)/((2*n+1)*(6*n+1)),-(3*n-1)*(4*n+1)/((2*n+1)*(6*n+1))]])
    expected_O = n*(3*n-1)*(3*n+1)*(8*n+5)/((n+1)*(2*n+1)**2*(6*n+1))
    assert sp.cancel(O.det()-expected_O) == 0
    w,s = F(1),F(1)
    states, samples, checks = [], [], 0
    for k in range(851):
        d = (6*k+1)*(6*k+3)
        u = F(k*(82*k+27)*w-(10*k+3)*(3*k-1)*s,d)
        vn = F(10*k*w-(3*k-1)*s,6*k+1)
        sn = F(-7*k*(68*k*k+68*k+15)*w+(3*k-1)*(62*k*k+59*k+12)*s,(k+1)*d)
        wn = F((8*k+7)*sn+(2*k+3)*u,6*k+5)
        an = sn+u
        bn = F(k*(22*k+7)*w-(3*k-1)*(4*k+1)*s,(2*k+1)*(6*k+1))
        if k < 60:
            assert (an,bn) == actual_endpoints(k+1), (k+1,an,bn)
            checks += 2
        if k >= 1:
            content = min(v3(w),v3(s))
            bound = k-2+sum((lambda t: sum(t//3**r for r in range(1,t.bit_length()+1)))(2*k+1) for _ in [0])-v3(F(k))
            assert 0 <= content <= bound
            endpoint_content = min(v3(an),v3(bn))
            lower = content-1-v3(F(k+1))-v3(F(2*k+1))
            upper = content+1+v3(F(k))+v3(F(8*k+5))-v3(F(2*k+1))
            assert lower <= endpoint_content <= upper
            if k in (1,2,10,26,80,242,850):
                samples.append({'m':k+1,'state_content':content,'endpoint_content':endpoint_content,'observation_bounds':[lower,upper],'real_window_certified':False})
        states.append([str(w),str(s)])
        w,s = wn,sn
    numeric_O = O.subs(n,850)
    minimum = min(v3(F(int(z.p),int(z.q))) for z in numeric_O)
    determinant_valuation = v3(F(int(numeric_O.det().p),int(numeric_O.det().q)))
    assert (minimum,determinant_valuation-minimum) == (-6,-4)
    artifact = {
        'status':'PASS','scope':'NEW exact symbolic connection and finite actual adjacent endpoint recurrence checks; no original tuple evaluated',
        'polynomial_matrix_identity_checks':32, 'determinant_identity_checks':3,
        'det_L':str(determinant_L), 'det_T':str(sp.factor(expected_T)), 'det_O':str(sp.factor(expected_O)),
        'actual_endpoint_exact_checks':checks,'seeded_state_count':851,'samples':samples,
        'observation_smith_exponents_at_n850':[-6,-4],
        'actual_original_window_evaluated':False,'sublinear_content_theorem_proved':False,'irrationality_proved':False,
        'report_sha256':hashlib.sha256((ROOT.parent/'responses/A1_turn12.md').read_bytes()).hexdigest()
    }
    target = ROOT/'endpoint_quartic_connection_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt = dict(artifact)
    receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    receipt['elapsed_seconds'] = round(time.monotonic()-started,3)
    (ROOT/'endpoint_quartic_connection_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
