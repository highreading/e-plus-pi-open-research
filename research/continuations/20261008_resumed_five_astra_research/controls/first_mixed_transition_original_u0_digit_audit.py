"""One NEW logarithmic digit audit at the first actual original index.

Only 58-bit arithmetic and factorial VALUATIONS are used, never huge
factorials, source arrays or matrices. Parent proof review is pending.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'FIRST_MIXED_TRANSITION_ORIGINAL_U0_DIGIT_RECEIPT.json'
assert not OUT.exists(), 'This one new receipt must not be repeated.'
k = 9**18
d = k-1
assert k.bit_length() <= 64
bits = d.bit_length()
alpha = 2*d-d.bit_count()
Ld = alpha-12
L = 1 << (k.bit_length()-2)
rho = d-2*L
assert d % 3 == 2 and (d & -d) == 16

def factorial_v2(n):
    assert n >= 0
    total = 0
    while n:
        n //= 2
        total += n
    return total

def D_legendre(p):
    lam = p-1+factorial_v2(p-1)
    e = factorial_v2(2*d-2)-factorial_v2(2*(d-p))
    rising = factorial_v2(d+p-2)-factorial_v2(d)
    return lam+2*e+(p-1)+rising

def D_digits(p):
    return (8*p-9+d.bit_count()-2*(d-1).bit_count()
            +2*(d-p).bit_count()-(p-1).bit_count()-(d+p-2).bit_count())

def prefix_popcount(n):
    total, bit = 0, 1
    while bit < n:
        cycle = 2*bit
        total += (n//cycle)*bit+max(0, n % cycle-bit)
        bit *= 2
    return total

def S(n):
    return n*(n-1)-prefix_popcount(n)

def E(p):
    return p*(p-1)+prefix_popcount(d)-prefix_popcount(d-p)-p*(d-1).bit_count()

def B(p):
    if p == 0:
        return 0
    return ((p-1)**2+(p-1)*d.bit_count()
            -(prefix_popcount(d+p-1)-prefix_popcount(d)))

def T(p):
    return S(p)+2*E(p)+B(p)

lo, hi, iterations = 2, d, 0
assert D_digits(lo) < Ld < D_digits(hi)
while lo < hi:
    p = (lo+hi)//2
    assert D_digits(p) == D_legendre(p)
    if D_digits(p) < Ld:
        lo = p+1
    else:
        hi = p
    iterations += 1
    assert iterations <= bits+1
s = lo
p = s-1
for j in (p-1, p, p+1, p+2):
    assert D_digits(j) == D_legendre(j) == T(j)-T(j-1)
assert D_digits(p) < Ld <= D_digits(p+1)
strict = Ld < D_digits(p+1)
q = p+1
conditions = {
    'strict_first_mixed_transition': strict,
    'p_is_odd': p % 2 == 1,
    'actual_return_width_2L_at_most_d': 2*L <= d,
    'rho_even_and_at_least2': rho >= 2 and rho % 2 == 0,
    'p_at_least_rho_plus1': p >= rho+1,
    'rho_plus_p_at_most_L': rho+p <= L,
    'alpha_minus2_gt_4q': alpha-2 > 4*q,
    'atom_correction_positive_gap': d-2*q+1-2*bits > 0,
}
receipt = {
    'status': 'PASS', 'scope': 'One actual ORIGINAL u0 digit-cost audit, not a source or cofactor computation.',
    'u': 0, 'k': k, 'd': d, 'maximum_integer_input_bit_length': (2*d+2).bit_length(),
    'binary_search_iterations': iterations,
    'L': L, 'rho': rho, 'L_d': Ld,
    'minimizing_product_count': p,
    'first_mixed_rank': q,
    'D_p': D_digits(p), 'D_next': D_digits(p+1),
    'equality_tie': not strict,
    'first_mixed_lower_payment': q*Ld+S(q)+T(p)-p*Ld,
    'conditional_parent_lemma_hypotheses': conditions,
    'all_hypotheses_hold': all(conditions.values()),
    'independent_paths': ['Binary popcount formula', 'Legendre valuations by repeated halving',
                          'Exact prefix-popcount T increment at the four neighboring counts'],
    'no_actual_factorials_matrices_sources_credentials_network_or_remote_code': True,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'parent_note_sha256': hashlib.sha256((HERE/'COORDINATOR_FIRST_MIXED_RETURN_NONMEMBERSHIP_AND_COST.md').read_bytes()).hexdigest(),
    'does_not_prove': ['Parent mixed theorem or actual cofactor valuation',
                       'Infinite original-index subfamily', 'Terminal pair upper',
                       'All-prime primitive-error result', 'Rationality of e+pi'],
}
OUT.write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({key: receipt[key] for key in ('status', 'k', 'd', 'minimizing_product_count',
                                               'first_mixed_rank', 'D_p', 'L_d', 'D_next',
                                               'equality_tie', 'conditional_parent_lemma_hypotheses')}))
