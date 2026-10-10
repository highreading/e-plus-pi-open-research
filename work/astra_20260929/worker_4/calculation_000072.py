from math import factorial
from fractions import Fraction
import json

MOD = 9

def falling(n, k):
    if k > n:
        return 0
    ans = 1
    for j in range(k):
        ans *= n-j
    return ans

def derivative(n, r, cutoff=None):
    total = Fraction(0)
    limit = n+1 if cutoff is None else min(n+1, cutoff)
    for c in range((limit-1)//2+1):
        for b in range(limit-2*c):
            total += Fraction((-1)**b * falling(n,b+2*c+r) * falling(n,b+c), 2**c * factorial(b) * factorial(c))
    assert total.denominator == 1
    return total.numerator

def auxiliary(n):
    h, hp = [derivative(n,r,6) % MOD for r in range(2)]
    eta, ep, epp = [derivative(n+1,r,6) % MOD for r in range(3)]
    m = n+1
    Jn = (n*h+hp) % MOD
    Jm = (m*eta+ep) % MOD
    Km = (m*(m-1)*eta+2*m*ep+epp) % MOD
    S = (Jm*Jm-eta*Km) % MOD
    C = ((Jm-eta)*Jn-(Km-Jm)*h) % MOD
    return (m*m % MOD,S,C)

# Independent finite checks of the truncation against the untruncated definition.
checked = 0
for n in range(41):
    for r in range(3):
        assert (derivative(n,r)-derivative(n,r,6)) % MOD == 0
        checked += 1

# Exact integer Legendre endpoint recurrence; division occurs before reduction.
maximum = 730
endpoints = [1,2]
for j in range(1,maximum+1):
    numerator = 2*(2*j+1)*endpoints[j]+4*j*endpoints[j-1]
    assert numerator % (j+1) == 0
    endpoints.append(numerator//(j+1))
assert all(a % 3 != 0 for a in endpoints)

aux_table = []
for residue in range(1,27,3):
    representative = residue+27
    triple = auxiliary(representative)
    for n in range(representative,maximum+1,27):
        assert auxiliary(n) == triple
    aux_table.append({'n_mod_27':residue,'k_S_C_mod_9':triple})

observations = {residue:set() for residue in range(1,27,3)}
for n in range(4,maximum+1,3):
    k,S,C = auxiliary(n)
    ratio = endpoints[n+1] * pow(endpoints[n] % MOD,-1,MOD) % MOD
    scaled_D = (k*ratio*C-2*S) % MOD
    observations[n % 27].add((ratio,scaled_D))
    assert scaled_D % 3 == 0
    if n % 9 == 1:
        assert ratio == 4

examples = []
for n in (4,7,10,28):
    k,S,C = auxiliary(n)
    examples.append({'n':n,'a_mod_9':endpoints[n]%MOD,'b_mod_9':endpoints[n+1]%MOD,'D_mod_9':(k*endpoints[n+1]*C-2*endpoints[n]*S)%MOD})

print(json.dumps({'untruncated_derivative_checks':checked,'auxiliary_table':aux_table,'observed_endpoint_ratio_and_D_over_a_mod_9':[{'n_mod_27':r,'pairs':sorted(observations[r])} for r in observations],'examples':examples,'scope':'Finite author computation. Periodicity and endpoint-ratio proofs are separate from these sampled observations.'},indent=2))