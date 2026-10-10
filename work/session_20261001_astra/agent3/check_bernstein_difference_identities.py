"""Verify the new minor identities using only saved n=6,b=3 data.

No original control checker is imported or rerun. No polynomial family or
polynomial Wronskian is reconstructed. All writes stay in Agent 3's directory.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json

BASE = Path('work/session_20261001_astra/agent3')
INPUT_NAMES = ('bernstein_next_control_certificate.json',
               'bernstein_difference_saved_data_checks.json',
               'bernstein_difference_recurrence_checks.json')


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
            a[i][j] = 0
    return value


def main():
    raw = {name: (BASE/name).read_bytes() for name in INPUT_NAMES}
    hashes = {name: sha256(data).hexdigest() for name, data in raw.items()}
    cert, saved, recurrence = [json.loads(raw[name]) for name in INPUT_NAMES]
    assert (cert['n'], cert['b'], cert['proposed_sign']) == (6, 3, 1)
    assert hashes[INPUT_NAMES[0]] == '2d2597a0c40f5d681912f33cb934d34e324b70fbad7f82cfbdd0397e0c9ebf20'
    assert saved['source_sha256'] == hashes[INPUT_NAMES[0]]
    assert recurrence['source_sha256'] == hashes[INPUT_NAMES[0]]
    n, b, S = 6, 3, 3
    C = {int(k): [F(x) for x in row]
         for k, row in cert['r_coefficients_ascending'].items()}

    def at(row, m):
        return row[m] if 0 <= m < len(row) else F(0)

    high = [C[7], C[8]]
    high_minors = {I: determinant([[at(row, m) for m in I] for row in high])
                   for I in combinations(range(n+b+1), b-1)}
    monomial_sets = list(combinations(range(n+b+1), b))

    def low_contraction(M, low):
        return sum(((-1)**(b-1+a)*high_minors[M[:a]+M[a+1:]]*low(m)
                    for a, m in enumerate(M)), F(0))

    def vandermonde(M):
        value = 1
        for i in range(b):
            for j in range(i+1, b):
                value *= M[j]-M[i]
        return value

    def difference_sum(low, multiplier, degree, j):
        result = F(0)
        for M in monomial_sets:
            u = sum(M)-S
            if 1 <= u <= j+1:
                result += (multiplier*vandermonde(M)*low_contraction(M, low)
                           *F(comb(j, u-1), comb(degree, u)))
        return result

    def endpoint_sum(low, multiplier):
        return sum((multiplier*vandermonde(M)*low_contraction(M, low)
                    for M in monomial_sets), F(0))

    difference_count = 0
    for record, check in zip(cert['mixed_weighted_Wronskians'], saved['checks']):
        k, L = record['k'], record['degree']
        assert check['k'] == k and L == 15+k
        gamma = [F(x) for x in record['signed_Bernstein_coefficients']]
        differences = [gamma[j+1]-gamma[j] for j in range(L)]
        assert differences == [F(x) for x in check['successive_signed_differences']]
        assert all(x > 0 for x in gamma) and all(x < 0 for x in differences)
        weight = abs(F(record['kernel_weight']))
        eta = (-1)**(k+b-1)
        for j, expected in enumerate(differences):
            actual = difference_sum(lambda m: at(C[k], m), eta, L, j)
            assert weight*actual == expected, (k, j)
            difference_count += 1
    assert difference_count == 126
    assert saved['all_differences_nonpositive']
    assert saved['first_positive_difference_witness'] is None

    shift_count = 0
    for record in recurrence['recurrence_checks']:
        k = record['k']
        degree = record['target_degree']
        assert 1 <= k <= 5 and degree == 16+k
        eta = (-1)**(k+b-1)
        for j, expected in enumerate(record['shift_Bernstein_differences']):
            actual = difference_sum(lambda m: at(C[k], m-1)/F(n+m),
                                    -eta, degree, j)
            assert actual == F(expected), (k, j, actual, expected)
            assert actual > 0
            shift_count += 1
    assert shift_count == 95
    witness = recurrence['first_positive_shift_witness']
    assert (witness['k'], witness['j']) == (1, 0)
    assert F(witness['positive_shift_difference']) == F(12152941, 7064347530240)
    assert (F(witness['positive_shift_difference'])
            +F(witness['negative_inherited_difference'])
            ==F(witness['actual_total_difference']))

    endpoints = {}
    for record in recurrence['polynomial_endpoint_bridge']:
        k = record['polynomial_index']
        assert k in (6, 7)
        p = [F(x) for x in cert['monic_p_coefficients_ascending'][str(k)]]
        D = [F(factorial(n), factorial(n+m))*x for m, x in enumerate(p)]
        assert D == [F(x) for x in record['A_coefficients_ascending']]
        eta = (-1)**(k+b-1)
        E = endpoint_sum(lambda m: at(D, m), eta)
        assert E == F(record['signed_ordered_minor_sum_Ek']) > 0
        assert eta*E == F(record['Wr_r7_r8_Ak_at_one'])
        z = F((-1)**(b+1), factorial(n)**b)*eta*E
        assert z == F(record['endpoint_contraction_from_polynomial_bridge'])
        endpoints[k] = E

    pn = sum(map(F, cert['monic_p_coefficients_ascending']['6']), F(0))
    pn1 = sum(map(F, cert['monic_p_coefficients_ascending']['7']), F(0))
    h = F(2, (2*n+1)*comb(2*n, n)**2)
    dv = (pn1*endpoints[n]+pn*endpoints[n+1])/(h*factorial(n)**b)
    assert dv == F(cert['endpoint']['existing_D_V']) > 0
    assert -dv == F(cert['endpoint']['cofactor_Y'])
    assert all((BASE/name).read_bytes() == data for name, data in raw.items())

    result = {
        'status': 'PASS',
        'scope': 'Only saved n=6,b=3 data; no polynomial Wronskian reconstruction or new HP index.',
        'ordered_high_row_indices': [7, 8],
        'ordered_high_coefficient_minors_used': len(high_minors),
        'signed_difference_minor_identities_checked': difference_count,
        'shift_difference_minor_identities_checked': shift_count,
        'two_endpoint_minor_sums_checked': {str(k): str(v) for k, v in endpoints.items()},
        'endpoint_lemma_identity_D_V': str(dv),
        'source_hashes': hashes,
        'all_input_files_preserved': True,
        'checker_sha256': sha256((BASE/'check_bernstein_difference_identities.py').read_bytes()).hexdigest(),
        'unbounded_nonvanishing_claim': False,
        'quotient_audit_performed': False
    }
    text = json.dumps(result, indent=2)+'\n'
    target = BASE/'bernstein_difference_identity_verification.json'
    if target.exists():
        assert target.read_text() == text, 'Existing verification differs; inspect before replacing.'
    else:
        target.write_text(text)
    print(text)


if __name__ == '__main__':
    main()
