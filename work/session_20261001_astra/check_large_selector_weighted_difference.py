from fractions import Fraction
from math import comb, lcm
from pathlib import Path
import json

ROOT = Path('work/session_20261001_astra')

def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def power(a, k):
    out = [1]
    for _ in range(k):
        out = mul(out, a)
    return out

def divide_monic(a, b):
    rem = a[:]
    out = [0] * (len(a)-len(b)+1)
    for j in range(len(out)-1, -1, -1):
        out[j] = rem[j+len(b)-1]
        for i, x in enumerate(b):
            rem[j+i] -= out[j]*x
    assert all(x == 0 for x in rem)
    return out

def compose(a, b):
    out = [0]
    for x in reversed(a):
        out = mul(out, b)
        out[0] += x
    return out

def forcing_and_moment(n, m):
    b = mul(power([1,-2,2], n), power([1,-4,2], 2*m))
    U, T, partial = 0, Fraction(0), Fraction(0)
    ga, gb = 1, 0
    for j, bj in enumerate(b):
        if j >= n:
            kj = comb(j,n)*bj
            U += kj
            T += kj*partial
        ga, gb = ga-gb, ga+gb
        partial += Fraction(2*gb, (2**j)*(j+1))
    return U, T

def imag_primitive_at_a(poly):
    ga, gb = 1, 0
    out = Fraction(0)
    for j, coeff in enumerate(poly):
        ga, gb = ga-gb, ga+gb
        out += coeff*Fraction(gb, (2**(j+1))*(j+1))
    return out

def v2_integer(a):
    a = abs(a)
    if a == 0:
        return None
    return (a & -a).bit_length()-1

rows = []
for n in (4,8,12):
    r, d = n//2, n+1
    cache = {m: forcing_and_moment(n,m) for m in range(d+5)}
    for m in range(5):
        weights = [(-1)**(d-j)*comb(d,j) for j in range(d+1)]
        values = [cache[m+j] for j in range(d+1)]
        W = sum((weights[j]*values[j][0]*values[j][1] for j in range(d+1)), Fraction(0))
        assert sum(weights[j]*values[j][0]**2 for j in range(d+1)) == 0
        pz = [weights[j]*values[j][0] for j in range(d+1)]
        divisor = [(-1)**(r+1-j)*comb(r+1,j) for j in range(r+2)]
        qz = divide_monic(pz, divisor)
        poly = mul([0,1], power([1,-2,2], n))
        poly = mul(poly, power([-1,0,1], r+1))
        poly = mul(poly, power([-1,0,2], 2*m))
        poly = mul(poly, compose(qz, [1,0,-4,0,4]))
        W_integral = -(2**(n+4))*imag_primitive_at_a(poly)
        assert W == W_integral, (n,m,W,W_integral)
        L = 5*n+4*m+4
        odd_lcm = 1
        for a in range(1,L+1,2):
            odd_lcm = lcm(odd_lcm,a)
        lattice = W*odd_lcm/(2**(r+1))
        assert lattice.denominator == 1, (n,m,lattice)
        rows.append({'n':n,'m':m,'W_numerator':str(W.numerator),
                     'W_denominator':str(W.denominator),'nonzero':W != 0,
                     'v2_W':None if W == 0 else v2_integer(W.numerator)-v2_integer(W.denominator),
                     'zero_forcing_nodes':[j for j,(U,T) in enumerate(values) if U == 0],
                     'polynomial_identity_pass':True,'lattice_identity_pass':True})
result = {'status':'Finite exact evidence only; no unbounded nonvanishing claim.',
          'cases':len(rows),'nonzero_cases':sum(row['nonzero'] for row in rows),
          'rows':rows}
path = ROOT/'large_selector_weighted_difference_checks.json'
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':result['cases'],'nonzero_cases':result['nonzero_cases'],
                  'identity_assertions':'passed','evidence_path':str(path)}))
