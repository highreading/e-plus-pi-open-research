"""Independent bounded exact reconstruction; finite evidence only."""
import json
import math
import resource
from pathlib import Path

import sympy as s

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
# Darwin does not permit lowering RLIMIT_AS/DATA in this runtime. The finite
# dimensions are fixed below and the hard CPU limit remains in force.
OUT = Path(__file__).resolve().parent
x = s.Symbol('x')


def v2(a):
    a = abs(int(a))
    if not a:
        return None
    return (a & -a).bit_length() - 1


def reconstruct(n):
    der = [1]
    for j in range(1, 4*n):
        der.append(j*der[-1] + (-1)**j)
    moments = [der[2*j] - (-1)**j for j in range(2*n)]
    mat = s.Matrix(n, n+1, lambda i, j: moments[i+j])
    kernel = mat.nullspace()
    assert len(kernel) == 1
    common = s.ilcm(*[a.q for a in kernel[0]])
    ints = [int(common*a) for a in kernel[0]]
    content = math.gcd(*ints)
    ints = [a//content for a in ints]
    if ints[-1] < 0:
        ints = [-a for a in ints]
    assert mat*s.Matrix(ints) == s.zeros(n, 1)
    poly = s.Poly(sum(a*x**j for j, a in enumerate(ints)), x)
    k = (n+1)//2
    w = int(poly.eval(-1))
    ls = [s.Rational(0)]
    for j in range(1, 2*n):
        ls.append(4*sum(s.Rational((-1)**h, 2*j-1-2*h) for h in range(j)))
    R = s.Matrix(k, k, lambda i, j: sum(ints[a]*(-math.factorial(2*(i+j+a))+ls[i+j+a]) for a in range(n+1)))
    v = s.Matrix([(-1)**j for j in range(k)])
    alpha = R.det(method='domain-ge')
    beta = w*(v.T*R.inv()*v)[0]*alpha
    center = s.cancel(-alpha/beta)
    basis = s.eye(k)
    for j in range(1, k):
        basis[0, j] = -(-1)**j
    assert basis.T*v == s.Matrix([1]+[0]*(k-1))
    Rt = basis.T*R*basis
    block = Rt[1:, 1:]
    assert beta == w*block.det(method='domain-ge')
    d = block.inv()*Rt[1:, :1]
    F = s.Poly(1-sum(d[j-1]*(x**j-(-1)**j) for j in range(1, k)), x)
    assert F.eval(-1) == 1
    roots = poly.intervals(eps=s.Rational(1, 10**8))
    return {
        'n': n, 'Q_coefficients': ints, 'Q_minus_one': w,
        'center_numerator': str(center.p), 'center_denominator': str(center.q),
        'v2_actual_q': v2(center.q), 'expected_v2': n+2,
        'log_actual_q': float(s.log(center.q).evalf(20)),
        'F_coefficients': [str(a) for a in reversed(F.all_coeffs())],
        'real_root_isolations': [[str(a), str(b), int(mult)] for ((a,b),mult) in roots],
        'root_count_in_0_1': sum(mult for ((a,b),mult) in roots if a>0 and b<1),
        'finite_only': True,
    }


records = []
for n in (5, 17):
    record = reconstruct(n)
    assert record['v2_actual_q'] == record['expected_v2']
    records.append(record)
    print(json.dumps({k: record[k] for k in ('n','v2_actual_q','log_actual_q','root_count_in_0_1','finite_only')}), flush=True)
    (OUT/'weighted_control.json').write_text(json.dumps(records, indent=2)+'\n')
