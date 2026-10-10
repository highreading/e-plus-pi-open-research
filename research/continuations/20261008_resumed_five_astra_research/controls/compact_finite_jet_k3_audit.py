"""Parent-authored bounded check of NEW A2turn3 jet/content identities."""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import comb, factorial, gcd, lcm
import hashlib
import json
import time
import sympy as sp

started = time.monotonic()
k = 3
prime = 149
last = 3*k-2
a = [1]
for degree in range(1, 2*last+3):
    a.append(1-degree*a[-1])
u = [a[2*n] for n in range(last+2)]
c = [u[n]-(-1)**n for n in range(last+1)]
f = [factorial(2*n) for n in range(last+2)]
tau = [Fraction(-f[n+1]-f[n])+Fraction(4, 2*n+1) for n in range(last)]
sigma = [u[n+1]+u[n] for n in range(last)]
lam = lcm(*range(1, 6*k-4, 2))

zraw = sp.Matrix([[*c[m:m+k], *tau[m:m+k-1]] for m in range(2*k)])
yraw = sp.Matrix([[*sigma[m:m+k], *tau[m:m+k]] for m in range(2*k-1)])
zpaid = zraw * sp.diag(*([1]*k+[lam]*(k-1)))
ypaid = yraw * sp.diag(*([1]*k+[lam]*k))

def transform(rows, h, exponent):
    diagonals = [factorial(2*m+h)//factorial(2*m) for m in range(rows)]
    s = sp.zeros(rows)
    for m in range(rows):
        for r in range(m+1):
            j = m-r
            if j <= exponent:
                s[m,r] = (-1)**j*comb(exponent,j)*factorial(2*m)//factorial(2*r)
    assert s.det() == 1
    return sp.diag(*diagonals), s, diagonals

dz, sz, az = transform(2*k, 2*k-3, 2*k-1)
dy, sy, ay = transform(2*k-1, 2*k-1, 2*k+1)
jz = dz*sz*zraw
jy = dy*sy*yraw
assert all(x.q == 1 for x in list(jz)+list(jy))

def signed_row_cofactors(mat):
    assert mat.rows == mat.cols+1
    return [int((-1)**r*mat.minor_submatrix(r,mat.cols).det())
            for r in []] if False else [int((-1)**r*mat.extract(
                [i for i in range(mat.rows) if i != r], range(mat.cols)).det())
                for r in range(mat.rows)]

def column_minors(mat):
    assert mat.cols == mat.rows+1
    return [int(mat.extract(range(mat.rows),
                [j for j in range(mat.cols) if j != omitted]).det())
                for omitted in range(mat.cols)]

gz = lambda values: reduce(gcd, (abs(int(v)) for v in values), 0)
r_content = gz(signed_row_cofactors(zpaid))
l_content = gz(column_minors(ypaid))
cz = gz(signed_row_cofactors(jz))
cy_minors = column_minors(jy)
cy = gz(cy_minors)
cof = signed_row_cofactors(sz*zpaid)
cof_content = gz(cof)
primitive = [v//cof_content for v in cof]
assert gz(primitive) == 1
zeta = lcm(*(aa//gcd(aa,abs(v)) for aa,v in zip(az,primitive)))
ay_content = gz(cy_minors[:k])
by_content = gz(cy_minors[k:])
chi = gcd(lam*ay_content,by_content)//cy
tz = reduce(lambda x,y:x*y,az,1)
ty = reduce(lambda x,y:x*y,ay,1)
assert lam % chi == 0
assert Fraction(lam**(k-1)*cz*zeta,tz) == r_content
assert Fraction(lam**(k-1)*cy*chi,ty) == l_content

interpolation = sp.Matrix([[factorial(2*m+2*j)//factorial(2*m)
                           for j in range(3)] for m in range(3)])
idet = int(interpolation.det())
assert idet == 7152 == 2**4*3*149
z_minor = int(zpaid[:5,:].det()) % prime
y_minor = int(ypaid[:,:5].det()) % prime
assert z_minor == 132 and y_minor == 95

receipt = {
    'all_checks_passed': True,
    'scope': 'NEW bounded k3,p149 mixed minors, finite jet integrality and exact all-prime cofactor/content-payment identities only; no uniform normality or irrationality theorem',
    'coordinator_authored': True,
    'external_code_executed': False,
    'network_or_keys_used': False,
    'k': k, 'prime': prime, 'Lambda': lam,
    'source_boundary': {'moment_max':last,'factorial_max':6*k-4,'last_odd':6*k-5},
    'interpolation_matrix': [list(map(int,interpolation.row(i))) for i in range(3)],
    'interpolation_determinant': idet,
    'actual_paid_Z_minor_mod149': z_minor,
    'actual_paid_Y_minor_mod149': y_minor,
    'Z_raw_mod149': [[int(sp.Mod(v,prime)) if v.q==1 else
                      int(v.p)*pow(int(v.q),-1,prime)%prime for v in zraw.row(i)]
                      for i in range(zraw.rows)],
    'Y_raw_mod149': [[int(sp.Mod(v,prime)) if v.q==1 else
                      int(v.p)*pow(int(v.q),-1,prime)%prime for v in yraw.row(i)]
                      for i in range(yraw.rows)],
    'triangular_Z_diagonal': az, 'triangular_Y_diagonal': ay,
    'triangular_Z_integer_unit_determinant': int(sz.det()),
    'triangular_Y_integer_unit_determinant': int(sy.det()),
    'J_Z_and_J_Y_integral': True,
    'actual_R': r_content, 'actual_L': l_content,
    'actual_C_Z':cz,'actual_C_Y':cy,'actual_zeta_Z':zeta,'actual_chi_Y':chi,
    't_Z':tz,'t_Y':ty,'primitive_transformed_Z_cofactor':primitive,
    'complete_content_identities_verified': True,
    'seconds':round(time.monotonic()-started,3),
    'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out = Path(__file__).with_name('compact_finite_jet_k3_certificate.json')
out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'k':k,'prime':prime,
                  'minor_mod149':[z_minor,y_minor], 'content_identities_verified':True,
                  'seconds':receipt['seconds']}))
