import sys
sys.path.insert(0, '[private local path removed]')
import sympy as S
from fractions import Fraction
from math import factorial, gcd

T = S.Symbol('T')
def ff_poly(x, m):
    return S.prod(x-j for j in range(m))

def ff_int(n, m):
    return 0 if m > n else factorial(n)//factorial(n-m)

def exact_D(n, r):
    result = Fraction(0)
    for c in range(n//2+1):
        for b in range(n-2*c+1):
            result += Fraction((-1)**b * ff_int(n,b+2*c+r) * ff_int(n,b+c), 2**c * factorial(b) * factorial(c))
    return result

results = []
checks = 0
for a in range(3):
    X = a + 3*T
    for r in range(3):
        retained = S.Integer(0)
        for c in range(5):
            for b in range(9-2*c):
                retained += S.Rational((-1)**b, 2**c * factorial(b) * factorial(c)) * ff_poly(X,b+2*c+r) * ff_poly(X,b+c)
        poly = S.Poly(S.expand(retained), T, domain=S.QQ)
        residues = {}
        for (degree,), coefficient in poly.terms():
            numerator, denominator = map(int, coefficient.as_numer_denom())
            assert gcd(denominator,3) == 1, (a,r,degree,coefficient)
            residue = numerator * pow(denominator,-1,9) % 9
            if residue:
                residues[degree] = residue
        for t in range(9):
            n = a + 3*t
            value = exact_D(n,r)
            assert gcd(value.denominator,3) == 1
            exact_residue = value.numerator * pow(value.denominator,-1,9) % 9
            polynomial_residue = sum(v * pow(t,j,9) for j,v in residues.items()) % 9
            assert exact_residue == polynomial_residue, (a,r,t,exact_residue,polynomial_residue)
            checks += 1
        results.append({'a':a,'r':r,'coefficients_mod_9':residues})
print({'cutoff_b_plus_2c':9,'polynomials':results,'exact_integer_comparisons':checks,'status':'PASS'})