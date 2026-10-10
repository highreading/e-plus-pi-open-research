"""Exact normalization control using the already frozen degree-two data only."""
from pathlib import Path
import json
import sympy as s

z = s.symbols('z')
n = 2
D = 1 + z**2
v = (1176 - 972*z - 118*z**2)/s.Integer(1850)
C = z**2 + s.Rational(102,925)*z + s.Rational(588,925)
E = s.exp(z)*D**n
Kcal = s.expand(D*(C*s.diff(v,z)-s.diff(C,z)*v)+(D+2*n*z)*C*v)
K = s.cancel(Kcal/z**(2*n))
assert not s.denom(K).has(z)
assert s.Poly(K,z).degree() == 2
assert s.gcd(C,v) == 1
F = s.series(E*v-C,z,0,2*n+4).removeO()
assert all(s.expand(F).coeff(z,j) == 0 for j in range(2*n+1))
assert s.expand(F).coeff(z,2*n+1) != 0
h = 1+2*n*z/D
N = (s.diff(C,z)*s.diff(v,z,2)-s.diff(C,z,2)*s.diff(v,z)
     +2*h*s.diff(C,z)*s.diff(v,z)
     +(s.diff(h,z)+h*h)*s.diff(C,z)*v-h*s.diff(C,z,2)*v)
A2 = s.expand(z*D*K)
A1 = s.expand(-(((z+2*n)*D+(n-1)*z*s.diff(D,z))*K+z*D*s.diff(K,z)))
A0 = s.cancel(D**2*N/z**(2*n-1))
assert all(s.Poly(a,z).degree() == d for a,d in zip([A2,A1,A0],[5,5,4]))
assert s.cancel(A2*s.diff(C,z,2)+A1*s.diff(C,z)+A0*C) == 0
assert s.simplify((A2*s.diff(E*v,z,2)+A1*s.diff(E*v,z)+A0*E*v)/s.exp(z)) == 0
assert s.simplify((C*s.diff(E*v,z)-s.diff(C,z)*E*v)/s.exp(z)-D**(n-1)*z**(2*n)*K) == 0
assert s.Poly(K,z).LC() == s.Poly(v,z).LC()
out = dict(n=n,v=str(v),C=str(C),K=str(K),A2=str(A2),A1=str(A1),A0=str(A0),
           error_leading=str(s.expand(F).coeff(z,2*n+1)),
           checks='PASS; existing degree two only')
Path(__file__).with_name('raw_two_function_dual_existing_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
