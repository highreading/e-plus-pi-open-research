"""A new exact good-prime cancellation witness with a preserved disk of radius 2.
This computes fresh jets and endpoint integers; the earlier degree81 radius
certificate supplies only the certified baseline root-distance premise.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb, gcd, lcm
import json, hashlib

SESSION = Path('work/session_20261002_codex_continuation')
source = SESSION/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json'
raw = source.read_bytes()
base = json.loads(raw)
ks = base['endpoint_basis_integers']
assert len(ks) == 80 and base['all_gaps_strictly_positive']
assert base['strict_composition_radius_lower'] == {'numerator':401,'denominator':200}
p, r = 163, 159
P = [Q(0)]*(r+2)
P[1] = Q(1)
for k,v in enumerate(ks,1):
    P[k] += Q(v,factorial(k))
    P[k+1] -= Q(v,factorial(k))

def endpoint_arrays(poly,N):
    degree = len(poly)-1
    pj = [v*factorial(k) for k,v in enumerate(poly)]
    assert all(v.denominator == 1 for v in pj)
    pj = [int(v) for v in pj]
    qj = [2]+[sum(comb(j,k)*pj[k]*pj[j-k] for k in range(max(0,j-degree),min(degree,j)+1))
              -(2*pj[j] if j<=degree else 0) for j in range(1,N+1)]
    G,u,D,B = [0],[0],[1],[1]
    for n in range(1,N+1):
        num = (4*pj[n] if n<=degree else 0)-sum(comb(n-1,k)*qj[k]*G[n-k] for k in range(1,n))
        assert num%4 == 0
        G.append(num//2)
        u.append(sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1)))
        D.append(n*D[-1]+(-1)**n)
        B.append(n*B[-1]+u[-1])
    return pj,G,D,B

pj0,G0,D0,B0 = endpoint_arrays(P,r)
assert D0[r]%p == 0
residue = (B0[r]-factorial(r))%p
K = (-residue*pow(2,-1,p))%p
if K>p//2: K-=p
assert abs(K)<=81
P[r] += Q(K,factorial(r))
P[r+1] -= Q(K,factorial(r))
pj,G,D,B = endpoint_arrays(P,r)
assert sum(P) == 1 and P[0] == 0 and P[1] == 1
assert G[:r] == G0[:r] and G[r]-G0[r] == 2*K
assert B[r]-B0[r] == 2*K and D == D0
assert D[r]%p == (B[r]-factorial(r))%p == 0
# At N=r<p, the actual B includes r!, a unit.  Common-zero cells concern
# B-r!, and become actual common divisibility only after factorial vanishes.
assert B[r]%p == factorial(r)%p != 0
den = lcm(*(v.denominator for v in P))
assert den%p != 0
left = 81*3*2**r*401**81
right = factorial(r)
assert left < right
# Use a large N=r+p; Cartier carry gives common divisibility.  Compute it
# independently from the full original jet/convolution, rather than assuming it.
N = r+p
pj,G,D,B = endpoint_arrays(P,N)
assert N>=p and D[N]%p == B[N]%p == 0
h = gcd(D[N],B[N])
assert h%p == 0
out = {
 'status':'PASS_EXACT_NEW_RADIUS_PRESERVING_GOOD_PRIME_COMMON_CELL',
 'source_path':str(source),'source_sha256':hashlib.sha256(raw).hexdigest(),
 'baseline_degree':81,'baseline_certified_radius_lower':'401/200',
 'new_degree':max(k for k,v in enumerate(P) if v),'perturbation_index':r,
 'prime':p,'centered_integer_K':K,'baseline_B_minus_factorial_residue':residue,
 'polynomial':'P81(z)+K*z^159*(1-z)/159!',
 'all_polynomial_derivative_jets_integral':True,'all_G_derivative_jets_even':True,
 'endpoint_zero':0,'endpoint_one':1,'first_derivative':1,
 'good_prime_coefficient_denominator_coprime':True,
 'closed_disk_radius_2_factor_bound':'|P81(z)-(1+-i)| > 1/401^81',
 'uniform_perturbation_bound':'|K|*3*2^159/159! < 1/401^81',
 'integer_bound_left':str(left),'integer_bound_right':str(right),
 'bound_bit_gap':right.bit_length()-left.bit_length(),
 'strict_composition_radius_lower':2,
 'cell':{'r':r,'D_r_mod_p':D0[r]%p,'new_B_r_minus_factorial_mod_p':(B0[r]+2*K-factorial(r))%p,
         'new_B_r_mod_p':(B0[r]+2*K)%p,'factorial_r_mod_p':factorial(r)%p},
 'actual_endpoint':{'N':N,'D_N':str(D[N]),'B_N':str(B[N]),
                    'actual_gcd':str(h),'actual_q':str(D[N]//h)},
 'scope':'A common residue cell and one actual denominator cancellation are compatible with radius>2. No common p-adic zero, arbitrary-depth cancellation, global gcd growth, or irrationality proof is claimed.'
}
(SESSION/'main/RADIUS_PRESERVING_PRIME_CANCELLATION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'K',K,'N',N,'bound bit gap',out['bound_bit_gap'],'gcd divisible by',p)
