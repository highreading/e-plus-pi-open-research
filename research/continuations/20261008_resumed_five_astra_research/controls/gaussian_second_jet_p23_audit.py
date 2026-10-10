"""One coordinator-authored auxiliary audit of A5turn17's new second jet.

Fixed p23, a3, N35 is NOT an original research index. No credentials,
network, generic prime scan, original-sized source or remote code is used.
Independent paths: direct integer Chebyshev polynomials; full affine
states; the new second-jet formula with the small Hermite endpoints.
"""
from pathlib import Path
import hashlib
import json
from math import comb, factorial

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'GAUSSIAN_SECOND_JET_P23_AUDIT_RECEIPT.json'
assert not RECEIPT.exists(), 'This single new receipt must not be rerun.'
p, a, N = 23, 3, 35
mod = p * p
k = (p + 1) // 2
n = 2 * N
assert n == a * p + 1 and n == 70 and k == 12

def add(x, y, scale=1):
    z = x[:] + [0] * max(0, len(y) - len(x))
    for j, v in enumerate(y):
        z[j] += scale * v
    return z

def mul(x, y):
    z = [0] * (len(x) + len(y) - 1)
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            z[i + j] += u * v
    return z

def reflect(x):
    return [sum(x[j] * comb(j, r) * (-1)**r
                for j in range(r, len(x))) for r in range(len(x))]

def moment(x, sign=1):
    return sum(factorial(j) * sign**j * v for j, v in enumerate(x))

# C_j(t)=T_j(2t-1), built by its original integer recurrence.
C = [[1], [-1, 2]]
for j in range(1, N):
    C.append(add(mul([-2, 4], C[j]), C[j-1], -1))
square_N = mul(C[N], C[N])
square_prev = mul(C[N-1], C[N-1])
cross = [-2 * v for v in mul(C[N], C[N-1])]
assert max(map(len, (square_N, square_prev, cross))) - 1 == n
direct_source = [moment(reflect(x)) % mod
                 for x in (square_N, cross, square_prev)] + [mod-1]
direct_endpoint = [moment(x, -1) % mod
                   for x in (square_N, cross, square_prev)]

theta, phi = [0, 1], [0, 1]
for j in range(1, n):
    theta.append(2 - 4*j*theta[j] + theta[j-1])
    phi.append(2*(-1)**j - 4*j*phi[j] + phi[j-1])
Q, P = [1, 1], [1, 3]
for j in range(1, k):
    Q.append((4*j+2)*Q[j] + Q[j-1])
    P.append((4*j+2)*P[j] + P[j-1])

# Original complete quadratic columns, independently from the full states.
full_source = [(1 - n*theta[n]) % mod,
               (2*(n-1)*theta[n-1]) % mod,
               (2*n-3 - (n-2)*theta[n]
                - 4*(n-1)*(n-2)*theta[n-1]) % mod, mod-1]
full_endpoint = [(1 - n*phi[n]) % mod,
                 (4 + 2*(n-1)*phi[n-1]) % mod,
                 (5-2*n - (n-2)*phi[n]
                  - 4*(n-1)*(n-2)*phi[n-1]) % mod]

# Direct p-block polynomials and their exact factorial moments.
Rp = add(reflect(C[p]), [-1])
Sp_twice = add(reflect(C[p+1]), reflect(C[p-1]), -1)
assert all(v % 2 == 0 for v in Sp_twice)
Sp = [v // 2 for v in Sp_twice]
Bplus, Bminus = moment(Sp), moment(Sp, -1)
Bplus_states = -2*(p+1) + 4*p*(p+1)*theta[p] - 2*theta[p-1]
Bminus_states = 2*(p+1) + 4*p*(p+1)*phi[p] - 2*phi[p-1]
assert Bplus == Bplus_states and Bminus == Bminus_states
A_exact = [moment(Rp), moment(mul([1, -2], Rp)),
           moment(Rp, -1), moment(mul([1, -2], Rp), -1)]
assert all(v % p == 0 for v in A_exact)
A_direct = [v // p % p for v in A_exact]
A_hermite = [(-4*factorial(k)*Q[k-1]) % p,
             (4*factorial(k)*(Q[k]+2*Q[k-1])) % p,
             (4*factorial(k)*P[k-1]) % p,
             (4*factorial(k)*(P[k]+2*P[k-1])) % p]
assert (Bplus - 4*factorial(k)*Q[k]) % p == 0
assert (Bminus - 4*factorial(k)*P[k]) % p == 0
beta = [(Bplus - 4*factorial(k)*Q[k]) // p % p,
        (Bminus - 4*factorial(k)*P[k]) // p % p]
assert a*(a*a-1) % 3 == 0
aplus = a + 2*p*(a*(a*a-1)//3)
aminus = a - 2*p*(a*(a*a-1)//3)
half = pow(2, -1, mod)
A0p, A1p, A0m, A1m = A_hermite
jet_source = [((aplus*Bplus+p*a*a*A1p)*half) % mod,
              (-p*a*a*A0p) % mod,
              ((-aplus*Bplus+p*a*a*A1p)*half) % mod, mod-1]
jet_endpoint = [(2+(aminus*Bminus+p*a*a*A1m)*half) % mod,
                (4+p*a*a*A0m) % mod,
                (2+(-aminus*Bminus+p*a*a*A1m)*half) % mod]

assert [theta[j] % mod for j in (22, 23, 24)] == [329, 307, 124]
assert [phi[j] % mod for j in (22, 23, 24)] == [418, 204, 163]
assert [Q[11] % mod, Q[12] % mod, P[11] % mod, P[12] % mod] == [284, 291, 319, 135]
assert factorial(k) % mod == 35
assert [Bplus % mod, Bminus % mod] == [30, 523]
assert beta == [1, 6]
assert A_direct == A_hermite == [7, 16, 17, 5]
assert direct_source == full_source == jet_source == [344, 138, 323, 528]
assert direct_endpoint == full_endpoint == jet_endpoint == [292, 349, 218]

receipt = {
    'status': 'PASS', 'scope': 'One new auxiliary p23/a3 second-jet audit; N35 is not an original index.',
    'p': p, 'a': a, 'auxiliary_N': N, 'modulus': mod,
    'maximum_polynomial_degree': n, 'maximum_affine_index': n,
    'maximum_hermite_index': k,
    'paths': ['Direct exact integer Chebyshev squares and both factorial functionals',
              'Complete original affine columns through index70',
              'Second-jet formula from independent p-block and Hermite data'],
    'coefficient_order': ['alpha^2', 'alpha*beta', 'beta^2', 'delta^2 (source only)'],
    'source_vector': direct_source, 'endpoint_vector': direct_endpoint,
    'p_block_residues': [Bplus % mod, Bminus % mod],
    'beta_residues': beta, 'A_residues': A_direct,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'report_sha256': hashlib.sha256((HERE.parent/'responses/A5_turn17.md').read_bytes()).hexdigest(),
    'no_credentials_network_remote_code_or_original_sized_calculation': True,
    'does_not_prove': ['Second-collision nonvanishing', 'Original-family regular continuation',
                       'All-prime multiplier saving', 'Producer retirement', 'Rationality of e+pi']
}
RECEIPT.write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k: receipt[k] for k in ('status', 'p', 'a', 'modulus', 'source_vector', 'endpoint_vector')}))
