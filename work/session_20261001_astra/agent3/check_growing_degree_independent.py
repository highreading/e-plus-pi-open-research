"""Independent audit restricted to the existing n=4,6,8,10 certificates.

Uses explicit Legendre coefficients, direct monomial moments, and the
original Taylor matrix. Does not import or execute Agent 2's checker.
All outputs are confined to Agent 3's directory.
"""
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
from math import comb, factorial, gcd
from pathlib import Path
import json
import sympy as s

SOURCE = Path('work/session_20261001_astra/agent2')
OUT = Path('work/session_20261001_astra/agent3')
SOURCE_NAMES = ('PROOF_DRAFT.md', 'REPORT.md', 'check_growing_regime.py',
                'growing_regime_certificates.json')
FROZEN = (4, 6, 8, 10)


def source_hashes():
    return {name: sha256((SOURCE / name).read_bytes()).hexdigest()
            for name in SOURCE_NAMES}


def rational(x):
    return F(int(s.numer(x)), int(s.denom(x)))


def mat(rows):
    return s.Matrix([[s.Rational(x.numerator, x.denominator) for x in row]
                     for row in rows])


def det(rows):
    return rational(mat(rows).det())


def explicit_p(k):
    # Ordinary Legendre binomial formula, without the three-term recurrence.
    values = [0] * (k + 1)
    for j in range(k // 2 + 1):
        degree = k - 2 * j
        multiplier = comb(k, j) * comb(2 * k - 2 * j, k)
        for r in range(degree + 1):
            values[r] += multiplier * comb(degree, r) * 2**r * (-1)**(degree-r)
    scale = 2**k * comb(2*k, k)
    result = [F(value, scale) for value in values]
    assert result[-1] == 1
    return result


def monomial_moment(k):
    # Direct integral of ((1+i*u)/2)^k over -1 <= u <= 1.
    return sum((F(2 * comb(k, j) * (-1)**(j//2), 2**k * (j+1))
                for j in range(0, k+1, 2)), F(0))


def multiply(a, b):
    result = [F(0)] * (len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j+k] += x*y
    return result


def moment(a):
    return sum((value * monomial_moment(k) for k, value in enumerate(a)), F(0))


def linear_combination(polynomials, factors, size):
    result = [F(0)] * size
    for polynomial, factor in zip(polynomials, factors):
        for k, value in enumerate(polynomial):
            result[k] += factor * value
    return result


def ell(a, n, j):
    # No extension to negative factorial arguments is made in this checker.
    assert 0 <= j <= n
    return sum((value / factorial(n+k+1-j) for k, value in enumerate(a)), F(0))


def f_coefficients(maximum):
    # Obtain F from (z^2-2z+2) F'(z)=4, F(0)=0.
    derivative = [F(2)]
    if maximum > 1:
        derivative.append(F(2))
    while len(derivative) < maximum:
        derivative.append(derivative[-1] - derivative[-2]/2)
    return [F(0)] + [derivative[k-1]/k for k in range(1, maximum+1)]


def partial_e(k):
    return sum((F(1, factorial(j)) for j in range(k+1)), F(0))


def atan_interval(q, terms):
    lower_candidate = sum((F((-1)**j, (2*j+1)*q**(2*j+1))
                           for j in range(terms)), F(0))
    other = lower_candidate + F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(lower_candidate, other), max(lower_candidate, other)


def constant_intervals(atan_terms, e_last):
    a, b = atan_interval(5, atan_terms)
    c, d = atan_interval(239, atan_terms)
    pi_interval = (16*a-4*d, 16*b-4*c)
    e_lower = partial_e(e_last)
    e_interval = (e_lower, e_lower+F(1, e_last*factorial(e_last)))
    return e_interval, pi_interval


def floor_fraction(x):
    return x.numerator // x.denominator


def decade_of_positive(x):
    assert x > 0
    exponent = len(str(x.numerator))-len(str(x.denominator))
    while x < F(10)**exponent:
        exponent -= 1
    while x >= F(10)**(exponent+1):
        exponent += 1
    return exponent


def adjacent_differences(row):
    return [row[j+1]-row[j] for j in range(len(row)-1)]


def check_record(record, old_constants, fresh_constants):
    n = record['n']
    b = record['b']
    assert n in FROZEN and b == n//2
    order = 2*n+b+1
    assert record['order_required'] == order
    f = f_coefficients(max(order, 2*(n+b)))
    for k in range(len(f)-1):
        assert f[k+1] == monomial_moment(k)

    triple = record['primitive_full_triple']
    A, B, C = (list(map(F, triple[key])) for key in ('A', 'B', 'C'))
    assert [len(A), len(B), len(C)] == [n+1, b+1, n+1]
    integers = triple['A']+triple['B']+triple['C']
    assert all(isinstance(value, int) for value in integers)
    assert reduce(gcd, map(abs, integers)) == 1

    # Check every original Taylor coefficient, including the reconstructed A.
    for k in range(order):
        value = A[k] if k <= n else F(0)
        value += sum((B[j]/factorial(k-j) for j in range(min(k,b)+1)), F(0))
        value += sum((C[j]*f[k-j] for j in range(min(k,n)+1)), F(0))
        assert value == 0, (n, 'original Taylor coefficient', k)
    X, Y = sum(A), sum(B)
    assert Y == sum(C) and Y > 0
    assert X == record['primitive_endpoint_X']
    assert Y == record['primitive_endpoint_Y']
    endpoint_gcd = gcd(abs(int(X)), int(Y))
    assert endpoint_gcd == record['endpoint_gcd']
    p, q = int(X)//endpoint_gcd, int(Y)//endpoint_gcd
    assert (p, q) == (record['p'], record['q'])
    assert gcd(abs(p), q) == 1 and q > 0
    assert len(str(q)) == record['q_digits']

    # Independent original matrix, before the Legendre reduction.
    raw_rows = []
    for k in range(n+1, order):
        raw_rows.append([F(1, factorial(k-j)) for j in range(b+1)]
                        + [f[k-j] for j in range(n+1)])
    raw_rows.append([F(1)]*(b+1)+[F(-1)]*(n+1))
    raw = mat(raw_rows)
    assert raw*mat([[x] for x in B+C]) == s.zeros(n+b+1, 1)
    raw_rank = raw.rank()
    assert raw_rank == n+b+1

    ps = [explicit_p(k) for k in range(n+b)]
    norms = [F(2*(-1)**k, (2*k+1)*comb(2*k,k)**2) for k in range(n+b)]
    # Direct moments check the nondegenerate bilinear norms and all cross terms.
    for j in range(n+b):
        for k in range(j, n+b):
            assert moment(multiply(ps[j], ps[k])) == (norms[j] if j == k else 0)
    V = linear_combination(ps[:n+1],
                           [sum(ps[k])/norms[k] for k in range(n+1)], n+1)
    high = [[ell(ps[n+l], n, j) for j in range(b+1)] for l in range(1,b)]
    v = [ell(V, n, j) for j in range(b+1)]
    erow = [F(1)]*(b+1)
    reduced = mat(high+[[1+x for x in v]])
    assert reduced.rank() == b == record['rank']
    cofactor_B = [rational((-1)**(b+j)*reduced[:, [k for k in range(b+1) if k != j]].det())
                  for j in range(b+1)]
    cofactor_Y = sum(cofactor_B)
    dv = det(high+[erow, v])
    assert cofactor_Y == -dv != 0
    assert cofactor_Y == F(record['cofactor_Y']) and dv == F(record['D_V'])
    scaling = cofactor_Y/Y
    assert cofactor_B == [scaling*x for x in B]
    projection = linear_combination(ps[:n+1],
        [-sum((B[j]*ell(ps[k],n,j) for j in range(b+1)), F(0))/norms[k]
         for k in range(n+1)], n+1)
    assert projection == list(reversed(C))
    for row in high:
        assert sum((x*y for x,y in zip(row,B)), F(0)) == 0

    # Obtain Q from H=pi*V-Q using direct polynomial division and moments.
    quotients = []
    for polynomial in ps[:n+1]:
        quotient = [sum(polynomial[j+1:], F(0)) for j in range(len(polynomial)-1)]
        quotients.append(quotient or [F(0)])
    Q = linear_combination(ps[:n+1],
                           [moment(quotients[k])/norms[k] for k in range(n+1)], n+1)
    arow = [-partial_e(n-j)+ell(Q,n,j) for j in range(b+1)]
    # Thus w=e*erow-pi*v+arow, with the entire tails retained exactly.
    dw_rational = det(high+[erow,arow])
    t_rational = det(high+[v,arow])
    assert dw_rational+t_rational == scaling*X
    assert sum((cofactor_B[j]*arow[j] for j in range(b+1)), F(0)) == scaling*X
    assert -dw_rational/cofactor_Y == F(record['rational_pi_companion'])
    assert -t_rational/cofactor_Y == F(record['rational_e_companion'])
    assert F(record['rational_pi_companion'])+F(record['rational_e_companion']) == -F(p,q)
    # D_W=dw_rational+pi*Y and T=t_rational+e*Y, in cofactor normalization.
    assert det(high+[v,erow]) == cofactor_Y
    sign = (-1)**(b+1)
    assert dv == sign*det([adjacent_differences(row) for row in high+[v]])
    assert dw_rational == sign*det([adjacent_differences(row) for row in high+[arow]])

    # Independently regenerate saved rational intervals and refine them.
    old_e, old_pi = old_constants
    expected_interval = [F(p)+q*(old_e[k]+old_pi[k]) for k in (0,1)]
    stored_interval = [F(value) for value in record['integer_form_interval']]
    assert stored_interval == expected_interval
    new_e, new_pi = fresh_constants
    new_interval = [F(p)+q*(new_e[k]+new_pi[k]) for k in (0,1)]
    assert stored_interval[0] <= new_interval[0] < new_interval[1] <= stored_interval[1]
    assert new_interval[0] > 0
    magnitude_decade = decade_of_positive(new_interval[0])
    assert decade_of_positive(new_interval[1]) == magnitude_decade
    approximate_form = F(record['integer_form_decimal_finite_evidence'])
    approximate_relative = F(record['relative_error_decimal_finite_evidence'])
    for endpoint in new_interval:
        assert abs(endpoint-approximate_form) <= abs(approximate_form)/10**32
        assert abs(endpoint/q-approximate_relative) <= abs(approximate_relative)/10**32
    coarse_scaled = new_interval[0]/F(10)**magnitude_decade*10**8
    mantissa_lower = F(floor_fraction(coarse_scaled), 10**8)
    coarse_scaled_upper = new_interval[1]/F(10)**magnitude_decade*10**8
    mantissa_upper = F(-floor_fraction(-coarse_scaled_upper), 10**8)

    return {
        'n': n, 'b': b, 'original_matrix_rank': raw_rank,
        'reduced_matrix_rank': b, 'all_Taylor_coefficients_through': order-1,
        'direct_moment_orthogonality_pass': True,
        'full_projection_and_cofactor_scaling_pass': True,
        'complete_tail_rational_decomposition_pass': True,
        'column_difference_sign': sign,
        'full_polynomial_content': 1, 'endpoint_gcd': endpoint_gcd,
        'p': p, 'q': q, 'q_digits': len(str(q)),
        'D_V': str(dv), 'cofactor_Y': str(cofactor_Y),
        'stored_intervals_reproduced_exactly': True,
        'refined_intervals_inside_stored_intervals': True,
        'integer_form_sign': 'positive', 'integer_form_decade': magnitude_decade,
        'integer_form_outward_enclosure': {
            'lower_mantissa': str(mantissa_lower),
            'upper_mantissa': str(mantissa_upper), 'power_of_ten': magnitude_decade},
        'displayed_decimals_agree_to_relative_1e_minus_32': True,
        'status': 'PASS'
    }


def main():
    before = source_hashes()
    certificate = json.loads((SOURCE/'growing_regime_certificates.json').read_text())
    assert tuple(record['n'] for record in certificate['records']) == FROZEN
    old_constants = constant_intervals(220, 300)
    fresh_constants = constant_intervals(230, 320)
    records = []
    for record in certificate['records']:
        checked = check_record(record, old_constants, fresh_constants)
        records.append(checked)
        print(json.dumps({key: checked[key] for key in
            ('n','b','original_matrix_rank','reduced_matrix_rank','q_digits',
             'endpoint_gcd','integer_form_decade','status')}), flush=True)
    after = source_hashes()
    assert before == after, 'Agent 2 source files changed during the audit.'
    result = {
        'status': 'PASS',
        'scope': 'Independent exact verification of existing n=4,6,8,10 only; no asymptotic inference.',
        'construction': 'Explicit ordinary Legendre coefficients, direct moments, original Taylor matrix, exact rational intervals.',
        'author_checker_inspected_but_not_executed': True,
        'agent2_files_unchanged_during_run': True,
        'source_sha256': before,
        'independent_checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'refined_constant_intervals': {'Machin_terms_each':230, 'e_last_term':320},
        'records': records
    }
    target = OUT/'growing_degree_independent_certificate.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('Saved '+str(target), flush=True)


if __name__ == '__main__':
    main()
