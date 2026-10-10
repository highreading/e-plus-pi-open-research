from fractions import Fraction as F
from math import factorial
import json

# Exact dense polynomials in Y; only exactly zero trailing coefficients are removed.
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(p, q, sign=1):
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += sign * x
    return trim(r)

def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)

def scale(p, a):
    return trim([a*x for x in p])

fall_cache = {}
def fall(a, h, m):
    key = (a, h, m)
    if key not in fall_cache:
        p = [F(1)]
        for j in range(m):
            p = mul(p, [F(a-j), F(h)])
        fall_cache[key] = p
    return fall_cache[key]

D_cache = {}
def D9(a):
    if a not in D_cache:
        p = [F(0)]
        for j in range(9):
            p = add(p, fall(a, 6, j))
        D_cache[a] = p
    return D_cache[a]

def is_three_integral(p):
    return all(x.denominator % 3 != 0 for x in p)

def residue(p, modulus):
    r = []
    for i, x in enumerate(p):
        if x.denominator % 3 == 0:
            raise ArithmeticError('Non-3-integral coefficient at index ' + str(i))
        r.append((x.numerator * pow(x.denominator, -1, modulus)) % modulus)
    return trim(r)

names = ('H', 'K', 'A', 'B', 'KP', 'BP')
acc = {name: [F(0)] for name in names}
pairs = []
term_coefficient_count = 0
term_integrality_failures = []

# X=1+3Y. R=b+2c<12. K is constructed by its exact direct sum.
for c in range(6):
    for b in range(12-2*c):
        R = b+2*c
        s = b+c
        eps = F((-1)**b, (2**c)*factorial(b)*factorial(c))
        h = scale(mul(fall(1, 3, R), fall(1, 3, s)), eps)
        k = scale(mul(add(fall(2, 3, R), fall(1, 3, R)), fall(2, 3, s)), eps)
        a = mul(h, D9(2-R))
        bb = mul(k, D9(3-R))
        # Independently form the numerator used by the source's inverse representation.
        kp = scale(mul(mul(fall(2, 3, R), fall(2, 3, s)), [F(4-R), F(6)]), eps)
        bp = mul(kp, D9(3-R))
        terms = {'H': h, 'K': k, 'A': a, 'B': bb, 'KP': kp, 'BP': bp}
        for name, p in terms.items():
            term_coefficient_count += len(p)
            for i, x in enumerate(p):
                if x.denominator % 3 == 0:
                    term_integrality_failures.append([b, c, name, i, str(x)])
            acc[name] = add(acc[name], p)
        pairs.append((b, c))

H, K, A, B, KP, BP = (acc[name] for name in names)
C = add(mul(K, A), mul(H, B), -1)
inv = [F(1, 2), F(-3, 4), F(9, 8)]
K_source = mul(KP, inv)
B_source = mul(BP, inv)
C_source = add(mul(K_source, A), mul(H, B_source), -1)
source_factor = [F(1), F(0), F(0), F(27, 8)]
zero = [F(0)]

observed = {
    'H_mod9': residue(H, 9),
    'H_mod27': residue(H, 27),
    'K_mod9': residue(K, 9),
    'A_mod9': residue(A, 9),
    'A_mod3': residue(A, 3),
    'B_mod3': residue(B, 3),
    'C_mod27': residue(C, 27)
}
expected = {
    'H_mod9': [0],
    'H_mod27': [0, 9, 9],
    'K_mod9': [0, 3],
    'A_mod9': [3, 6],
    'A_mod3': [0],
    'B_mod3': [1],
    'C_mod27': [0, 0, 9]
}
all_polys = {
    'H': H, 'K': K, 'A': A, 'B': B, 'C': C,
    'KP': KP, 'BP': BP,
    'K_source': K_source, 'B_source': B_source, 'C_source': C_source
}
checks = {
    'outer_pairs_exactly_42': len(pairs) == 42 and len(set(pairs)) == 42,
    'all_term_coefficients_three_integral': not term_integrality_failures,
    'all_final_coefficients_three_integral': all(is_three_integral(p) for p in all_polys.values()),
    'exact_K_numerator_identity': add(mul([F(2), F(3)], K), KP, -1) == zero,
    'exact_B_numerator_identity': add(mul([F(2), F(3)], B), BP, -1) == zero,
    'exact_inverse_factor_identity': mul([F(2), F(3)], inv) == source_factor,
    'exact_source_K_factor': add(K_source, mul(K, source_factor), -1) == zero,
    'exact_source_B_factor': add(B_source, mul(B, source_factor), -1) == zero,
    'exact_source_C_factor': add(C_source, mul(C, source_factor), -1) == zero,
    'K_representations_agree_mod27': residue(add(K_source, K, -1), 27) == [0],
    'B_representations_agree_mod27': residue(add(B_source, B, -1), 27) == [0],
    'C_representations_agree_mod27': residue(add(C_source, C, -1), 27) == [0],
    'exact_H_at_X1': H[0] == 0,
    'exact_K_at_X1': K[0] == 0,
    'exact_A_at_X1': A[0] == 3,
    'exact_B_at_X1': B[0] == 10,
    'exact_C_at_X1': C[0] == 0,
    'exact_H_index_derivative_at_X1': H[1]/3 == F(-3, 2),
    'exact_K_index_derivative_at_X1': K[1]/3 == 4,
    'exact_C_index_derivative_at_X1': C[1]/3 == 27
}
for name in expected:
    checks[name + '_matches_certificate'] = observed[name] == expected[name]

report = {
    'scope': 'Exact coefficients of complete finite polynomials; infinite tails are justified by the separately proved Gauss bounds.',
    'method': 'Direct falling-factorial K sum, with an independent reconstruction of the source inverse representation.',
    'outer_cutoff': 'R=b+2c<12',
    'D_cutoff': 'j=0,...,8',
    'outer_pairs': len(pairs),
    'term_coefficients_checked_for_three_integrality': term_coefficient_count,
    'final_coefficients_checked_for_three_integrality': sum(len(p) for p in all_polys.values()),
    'term_integrality_failures': term_integrality_failures,
    'observed': observed,
    'exact_values_at_X1': {name: str(p[0]) for name, p in [('H', H), ('K', K), ('A', A), ('B', B), ('C', C)]},
    'exact_index_derivatives_at_X1': {'H': str(H[1]/3), 'K': str(K[1]/3), 'C': str(C[1]/3)},
    'degrees': {name: len(p)-1 for name, p in all_polys.items()},
    'max_polynomial_degree_checked': max(len(p)-1 for p in all_polys.values()),
    'checks': checks,
    'all_checks_pass': all(checks.values())
}
print(json.dumps(report, ensure_ascii=False, indent=2))
assert report['all_checks_pass'], 'One or more exact checks failed; inspect the printed report.'