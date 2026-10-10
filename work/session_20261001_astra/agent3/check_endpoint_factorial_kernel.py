"""Check factorial-kernel identities using only the saved n=6 endpoint data.

No HP family or Bernstein control is rebuilt. The two endpoint contractions
are checked by kernel Cauchy-Binet and exact beta moments. Signed summands
are retained; no positivity of their coefficient transform is assumed.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json

BASE = Path('work/session_20261001_astra/agent3')
INPUTS = ('bernstein_next_control_certificate.json',
          'bernstein_difference_recurrence_checks.json',
          'bernstein_difference_identity_verification.json')


def determinant(rows):
    a = [list(map(F, row)) for row in rows]
    value = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        entry = a[j][j]
        value *= entry
        for i in range(j+1, len(a)):
            ratio = a[i][j]/entry
            for h in range(j+1, len(a)):
                a[i][h] -= ratio*a[j][h]
            a[i][j] = F(0)
    return value


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


def vandermonde(values):
    return product(values[j]-values[i]
                   for i in range(len(values)) for j in range(i+1, len(values)))


def coefficient(row, m):
    return row[m] if 0 <= m < len(row) else F(0)


def one_minus_t(row):
    return [coefficient(row, m)-coefficient(row, m-1) for m in range(len(row)+1)]


def borel_value(row, x):
    return sum((c*x**m/factorial(m) for m, c in enumerate(row)), F(0))


def main():
    raw = {name: (BASE/name).read_bytes() for name in INPUTS}
    cert, rec, verification = [json.loads(raw[name]) for name in INPUTS]
    assert (cert['n'], cert['b']) == (6, 3)
    assert verification['status'] == 'PASS'
    n, b = 6, 3
    p = {int(k): [F(v) for v in row]
         for k, row in cert['monic_p_coefficients_ascending'].items()}
    high = [one_minus_t(p[k]) for k in (7, 8)]
    expected = {row['polynomial_index']: F(row['signed_ordered_minor_sum_Ek'])
                for row in rec['polynomial_endpoint_bridge']}
    sets = list(combinations(range(n+b+1), b))
    offsets = list(range(n-b+1, n+1))
    kernel_checks = []
    kernels = {}
    for M in sets:
        # Increasing row and column offsets: sign (-1)^(b(b-1)/2).
        A = max(M)
        degrees = [A-m for m in reversed(M)]
        X = [A+c for c in offsets]
        count = determinant([[F(comb(x, e)) for x in X] for e in degrees])
        assert count.denominator == 1 and count > 0
        factorized = F((-1)**(b*(b-1)//2)*product(factorial(e) for e in degrees),
                       product(factorial(x) for x in X))*count
        increasing = determinant([[F(1, factorial(m+c)) for c in offsets] for m in M])
        assert increasing == factorized < 0
        reversed_columns = determinant([[F(1, factorial(n+m-j)) for j in range(b)] for m in M])
        explicit = F(vandermonde(M), product(factorial(n+m) for m in M))
        assert reversed_columns == -increasing == explicit > 0
        kernels[M] = explicit
        kernel_checks.append({'row_offsets': list(M), 'column_offsets': offsets,
                              'Pascal_path_count': int(count),
                              'signed_kernel_minor': str(increasing),
                              'reversed_consecutive_minor': str(explicit)})

    controls = []
    node_sets = [(F(1,8), F(1,4), F(3,8)),
                 (F(1,4), F(1,2), F(3,4)),
                 (F(5,8), F(3,4), F(7,8))]
    for k in (6, 7):
        eta = (-1)**(k+b-1)
        rows = high+[p[k]]
        terms = []
        total = F(0)
        positive = negative = F(0)
        for M in sets:
            coefficient_minor = determinant([[coefficient(row, m) for m in M] for row in rows])
            value = eta*factorial(n)**b*coefficient_minor*kernels[M]
            total += value
            if value > 0:
                positive += value
            elif value < 0:
                negative -= value
            terms.append({'monomial_indices': list(M),
                          'coefficient_minor': str(coefficient_minor),
                          'positive_kernel_minor': str(kernels[M]),
                          'signed_endpoint_contribution': str(value),
                          'sign': int(value > 0)-int(value < 0)})
        assert total == expected[k] > 0
        assert total == positive-negative
        # Direct shifted-factorial contraction (triangular jet change has determinant one).
        shifted = [[sum((c/F(factorial(n+m-j)) for m,c in enumerate(row)), F(0))
                    for j in range(b)] for row in rows]
        assert eta*factorial(n)**b*determinant(shifted) == total
        # Ordered-simplex integral from determinant integration, evaluated exactly
        # through beta moments. Borel(row)=sum c_m*t^m/m!.
        moments = [[sum((c*F(factorial(m+j)*factorial(n-b),
                             factorial(m)*factorial(m+j+n-b+1))
                         for m,c in enumerate(row)), F(0))
                    for j in range(b)] for row in rows]
        ordered_integral = determinant(moments)
        normalizer = F(factorial(n)**b,
                       product(factorial(n-j-1) for j in range(b)))
        assert eta*normalizer*ordered_integral == total
        point_checks = []
        for nodes in node_sets:
            signed_det = eta*determinant([[borel_value(row, x) for x in nodes] for row in rows])
            point_checks.append({'nodes': list(map(str,nodes)),
                                 'signed_Borel_evaluation_determinant': str(signed_det),
                                 'sign': int(signed_det > 0)-int(signed_det < 0)})
        controls.append({'k': k, 'eta': eta,
                         'actual_row_polynomials': ['(1-t)p_7', '(1-t)p_8', 'p_'+str(k)],
                         'actual_coefficients_ascending': [list(map(str,row)) for row in rows],
                         'Cauchy_Binet_terms': terms,
                         'positive_term_count': sum(t['sign'] == 1 for t in terms),
                         'negative_term_count': sum(t['sign'] == -1 for t in terms),
                         'zero_term_count': sum(t['sign'] == 0 for t in terms),
                         'first_positive_term': next((t for t in terms if t['sign'] == 1), None),
                         'first_negative_term': next((t for t in terms if t['sign'] == -1), None),
                         'positive_part': str(positive), 'negative_part_magnitude': str(negative),
                         'E_from_full_signed_sum': str(total), 'saved_E': str(expected[k]),
                         'beta_moment_matrix': [list(map(str,row)) for row in moments],
                         'ordered_simplex_integral': str(ordered_integral),
                         'positive_integral_normalizer': str(normalizer),
                         'integral_representation_matches': True,
                         'fixed_rational_node_checks': point_checks})
    assert all((BASE/name).read_bytes() == data for name,data in raw.items())
    result = {'status': 'PASS',
              'scope': 'Only the two actual endpoint contractions from saved n=6,b=3 data; no new HP indices or Bernstein coefficient scan.',
              'kernel_formula_scope_checked': 'The 120 three-row subsets and consecutive column offsets 4,5,6 used by these two contractions.',
              'bare_kernel_checks': kernel_checks,
              'endpoint_controls': controls,
              'source_hashes': {name: sha256(data).hexdigest() for name,data in raw.items()},
              'all_input_files_preserved': True,
              'checker_sha256': sha256((BASE/'check_endpoint_factorial_kernel.py').read_bytes()).hexdigest(),
              'uniform_endpoint_sign_proved': False}
    text = json.dumps(result, indent=2)+'\n'
    target = BASE/'endpoint_factorial_kernel_checks.json'
    if target.exists():
        assert target.read_text() == text, 'Existing output differs; inspect before changing it.'
    else:
        target.write_text(text)
    print(json.dumps({'status': 'PASS', 'bare_kernel_minors_checked': len(kernel_checks),
                      'endpoints': [{key: row[key] for key in
                          ('k','positive_term_count','negative_term_count','zero_term_count',
                           'first_positive_term','first_negative_term','positive_part',
                           'negative_part_magnitude','E_from_full_signed_sum',
                           'ordered_simplex_integral','positive_integral_normalizer',
                           'fixed_rational_node_checks')} for row in controls],
                      'all_input_files_preserved': True, 'saved': str(target)}, indent=2))


if __name__ == '__main__':
    main()
