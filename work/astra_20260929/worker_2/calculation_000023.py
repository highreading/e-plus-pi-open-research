from fractions import Fraction as F
from math import gcd

cases = 0
positive_cases = 0
small_error_cases = 0
parameters = [(F(2), F(3,5)), (F(3,2), F(7,3)), (F(5,3), F(1,11))]
for v in range(1, 8):
    for u in range(-5, 6):
        if gcd(u, v) != 1:
            continue
        a = 0 if v == 1 else pow(u, -1, v)
        b = (u*a - 1)//v
        assert u*a-v*b == 1
        for beta, C in parameters:
            for n in range(1, 13):
                s = (-1)**n
                scale = beta**n
                bound = F(v*v)*C/(2*scale)
                for m in (1, 2, 3, 6, 11, 2**n+1):
                    Q = F(m)*scale/(v*C)
                    target = (Q-s*m*a)/v
                    rounding_argument = (target-1)/m + F(1,2)
                    j = rounding_argument.numerator//rounding_argument.denominator
                    t = 1+m*j
                    q = s*m*a+v*t
                    p = s*m*b+u*t
                    assert abs(q-Q) <= F(v*m,2)
                    assert u*q-v*p == s*m
                    assert -b*q+a*p == t
                    assert gcd(p,q) == 1
                    delta = (q-Q)/Q
                    assert abs(delta) <= bound
                    if q > 0:
                        positive_cases += 1
                        eta = F(s)*(F(u,v)-F(p,q))*scale/C-1
                        assert eta == -delta/(1+delta)
                    if bound <= F(1,2):
                        assert q > 0
                        assert abs(eta) <= 2*bound
                        small_error_cases += 1
                    cases += 1
print({'status':'PASS', 'exact_cases':cases, 'positive_denominator_cases':positive_cases, 'quantitative_error_bound_cases':small_error_cases, 'scope':'Finite exact checks of the author construction; no independent review or matched-family denominator estimate.'})