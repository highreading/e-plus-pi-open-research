import json, math, time
from pathlib import Path
started = time.perf_counter()
base = Path('[private local path removed]')
certificate = json.loads((base / 'work/session_20260927/hp_b1_odd_dyadic_germs_checks.json').read_text())
assert (certificate['precision'], certificate['modulus'], certificate['outer_R_less_than'], certificate['inner_D_r_less_than']) == (10, 1024, 55, 20)
M = 1024
facts = [math.factorial(j) for j in range(55)]
powers8 = [8**j for j in range(110)]

def linear_product(factors):
    # Exact coefficients in T; independently build the complete kernel.
    result = [1]
    for constant, slope in factors:
        nxt = [0] * (len(result) + 1)
        for degree, coeff in enumerate(result):
            nxt[degree] += constant * coeff
            nxt[degree + 1] += slope * coeff
        result = nxt
    return result

def canonical(poly):
    result = [x % M for x in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def accumulate(target, poly):
    if len(target) < len(poly):
        target.extend([0] * (len(poly) - len(target)))
    for degree, coeff in enumerate(poly):
        target[degree] = (target[degree] + coeff) % M

def ring_product(left, right):
    # Sparse modular multiplication happens only after exact division.
    result = [0] * (len(left) + len(right) - 1)
    nz_left = [(i, v) for i, v in enumerate(left) if v]
    nz_right = [(i, v) for i, v in enumerate(right) if v]
    for i, u in nz_left:
        for j, v in nz_right:
            result[i + j] += u * v
    return canonical(result)

def contraction(argument):
    # Compute sum_{j=0}^{19}(argument+16Y)_j exactly before reduction.
    total = [0] * 20
    current = [1]
    for j in range(20):
        for degree, coeff in enumerate(current):
            total[degree] += coeff * 16**degree
        if j < 19:
            nxt = [0] * (len(current) + 1)
            for degree, coeff in enumerate(current):
                nxt[degree] += (argument - j) * coeff
                nxt[degree + 1] += coeff
            current = nxt
    return canonical(total)

rows = []
all_counts = []
for a in (1, 3, 5, 7):
    counts = {'residue_mod8': a, 'H_kernels': 0, 'K_nonconstant_kernels': 0, 'H_coefficients_checked': 0, 'K_coefficients_checked': 0}
    def normalized(factors, denominator, sign, family):
        numerator_in_T = linear_product(factors)
        two_part = denominator & -denominator
        numerator_in_Y = [coeff * powers8[j] for j, coeff in enumerate(numerator_in_T)]
        assert all(coeff % two_part == 0 for coeff in numerator_in_Y), (a, R, c, family)
        counts[family + '_coefficients_checked'] += len(numerator_in_Y)
        # Invert only after checking all complete integer coefficients.
        odd_part = denominator // two_part
        assert odd_part % 2 == 1
        inverse = pow(odd_part, -1, M)
        return canonical([sign * (coeff // two_part) * inverse for coeff in numerator_in_Y])
    sums = {name: [0] for name in ('H', 'K', 'A', 'B')}
    dcache = {argument: contraction(argument) for argument in range(2*a-54, 2*a+2)}
    # Enumerate by total R, independently of the source's b-first loops.
    for R in range(55):
        for c in range(R // 2 + 1):
            b = R - 2*c
            s = R - c
            denominator = (1 << c) * facts[b] * facts[c]
            sign = 1 if b % 2 == 0 else -1
            h_factors = [(a-j, 1) for j in range(R)] + [(a-j, 1) for j in range(s)]
            h = normalized(h_factors, denominator, sign, 'H')
            counts['H_kernels'] += 1
            if R == 0:
                assert b == c == s == 0 and denominator == 1
                k = [2]
            else:
                k_factors = [(a-j, 1) for j in range(R-1)] + [(a+1-j, 1) for j in range(s)] + [(2*a+2-R, 2)]
                k = normalized(k_factors, denominator, sign, 'K')
                counts['K_nonconstant_kernels'] += 1
            accumulate(sums['H'], h)
            accumulate(sums['K'], k)
            accumulate(sums['A'], ring_product(h, dcache[2*a-R]))
            accumulate(sums['B'], ring_product(k, dcache[2*a+1-R]))
    sums = {name: canonical(poly) for name, poly in sums.items()}
    result_c = ring_product(sums['K'], sums['A'])
    accumulate(result_c, [-v for v in ring_product(sums['H'], sums['B'])])
    sums['C'] = canonical(result_c)
    expected = next(row for row in certificate['rows'] if row['residue_mod8'] == a)
    for name, actual in sums.items():
        assert actual == expected[name], {'residue': a, 'name': name, 'actual': actual, 'expected': expected[name]}
    nonzero = [abs(v) for v in sums['C'] if v]
    gauss = min((v & -v).bit_length()-1 for v in nonzero)
    assert gauss == expected['v2_gauss_C']
    rows.append({'residue_mod8': a, **sums, 'v2_gauss_C': gauss})
    all_counts.append(counts)
print(json.dumps({'all_twenty_arrays_match': True, 'exact_divisibility_checks': all_counts, 'rows': rows, 'elapsed_seconds': time.perf_counter()-started, 'scope': 'Independent finite polynomial reconstruction only; source checker not executed; no files written; no analytic or denominator conclusion.'}, indent=2))