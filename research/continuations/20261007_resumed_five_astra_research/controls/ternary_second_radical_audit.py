"""Coordinator-authored sparse next-layer audit; no original matrix built."""
from pathlib import Path
from math import comb
import hashlib, json, time

OUT = Path(__file__).resolve().parent
P, r = 2187, 227
P0, N0 = 243*P, 243*r
D, Q = P0+N0, P0//9
b = Q-N0
ell, E = 3*b//2+1, (Q-3)//2
nJ = (Q-4*b-5)//2

def lucas(n, k):
    if k < 0 or k > n:
        return 0
    answer = 1
    while n or k:
        a, c = n % 3, k % 3
        if c > a:
            return 0
        answer = answer*comb(a, c) % 3
        n //= 3
        k //= 3
    return answer

def xcoef(n, k):
    return ((-1 if (n-k) % 2 else 1)*lucas(n, k)) % 3

def main():
    started = time.monotonic()
    assert 10*r > P and 180*r < 19*P and r % 9 == 2
    assert b % 2 == 0 and b % 243 == 0 and 6*b < Q
    units = [1]*(D+1)
    vals = [0]*(D+1)
    for i in range(1, D+1):
        a, v = i, 0
        while a % 3 == 0:
            a //= 3
            v += 1
        units[i] = units[i-1]*a % 27
        vals[i] = vals[i-1]+v
    def bin27(n, k):
        if k < 0 or k > n:
            return 0
        v = vals[n]-vals[k]-vals[n-k]
        if v >= 3:
            return 0
        return (3**v*units[n]*pow(units[k]*units[n-k] % 27, -1, 27)) % 27
    comparisons = 2*(ell-1)+1
    for s in range(comparisons):
        k = (P0-3)//2-s
        value = ((-1 if (D-k)%2 else 1)*bin27(D, k)) % 27
        assert value % 9 == 0
        assert value//9 == xcoef(N0, E-s)
    sparse = [(k, xcoef(b, k)) for k in range(b+1) if xcoef(b, k)]
    series = [lucas(b+k-1, k) for k in range(E+1)]
    convolution_checks = 0
    for k in range(E+1):
        assert series[k] == (-xcoef(N0, k)) % 3
        value = sum(v*series[k-j] for j, v in sparse if j <= k) % 3
        assert value == int(k == 0)
        convolution_checks += 1
    scalar = sum(v*((-1 if (nJ-1-j)%2 else 1)*(nJ-j))
                 for j, v in sparse if j <= nJ-1) % 3
    assert scalar == ((-1 if (nJ-1)%2 else 1)*nJ) % 3 == 1
    assert pow(4, 27, 27) == 1 and comb(54, 27) % 27 == 20
    result = {'authorship': 'Coordinator; no remote code executed',
              'scope': 'One auxiliary P,r tuple only; does not establish actual producer jets, original index infinitude, or an irrationality theorem.',
              'parameters': {'P': P, 'r': r, 'P0': P0, 'N0': N0, 'D': D,
                             'Q': Q, 'b': b, 'ell': ell, 'E': E, 'nJ': nJ},
              'divided_binomial_comparisons': comparisons,
              'generating_function_and_recurrence_checks': convolution_checks,
              'sparse_denominator_terms': len(sparse),
              'intermediate_scalar_coefficient_mod3': scalar,
              'rank_certificate': {'minimal_rational_denominator_degree': b,
                                   'leading_and_constant_coefficients_units': True,
                                   'numerator_denominator_coprime': True,
                                   'full_radical_dimension': ell-b,
                                   'endpoint_annihilator_dimension': ell-b-1},
              'all_finite_checks_passed': True,
              'seconds': round(time.monotonic()-started, 4),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/'ternary_second_radical_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
