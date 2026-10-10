"""Exact Bernstein-sign test at the single frozen control n=6,b=3.

Run from the research workspace root. No other HP index is constructed.
The complete coefficient data for this one control are retained. A negative
signed coefficient closes the proposed uniform coefficient-sign branch.
Default: write the new certificate and summary only in Agent 3's directory.
--verify: regenerate and compare those files without writing.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import json
import sys

BASE = Path('work/session_20261001_astra/agent3')
SCRIPT = BASE / 'check_bernstein_next_control.py'
NOTE = BASE / 'GROWING_ENDPOINT_NONVANISHING.md'
SOURCE = Path('work/session_20261001_astra/agent2/growing_regime_certificates.json')
N, B = 6, 3
SIGMA = (-1)**(B-1)
assert (N, B, SIGMA) == (6, 3, 1)


def trim(values):
    values = list(map(F, values))
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [F(0)]


def add(a, b):
    values = [F(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        values[j] += x
    for j, x in enumerate(b):
        values[j] += x
    return trim(values)


def scale(a, c):
    return trim([c*x for x in a])


def multiply(a, b):
    values = [F(0)] * (len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            values[j+k] += x*y
    return trim(values)


def power(a, exponent):
    values = [F(1)]
    for _ in range(exponent):
        values = multiply(values, a)
    return values


def derivative(a, order=1):
    assert order >= 0
    return trim([a[m]*factorial(m)//factorial(m-order)
                 if a[m].denominator == 1 else
                 a[m]*F(factorial(m), factorial(m-order))
                 for m in range(order, len(a))])


def differentiate(a, order):
    # Explicit rational multiplication; no factorial at a negative argument.
    return trim([a[m]*F(factorial(m), factorial(m-order))
                 for m in range(order, len(a))])


def at_one(a):
    return sum(a, F(0))


def qdet(rows):
    size = len(rows)
    assert all(len(row) == size for row in rows)
    matrix = [list(map(F, row)) for row in rows]
    value = F(1)
    for col in range(size):
        pivot = next((i for i in range(col, size) if matrix[i][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            value = -value
        entry = matrix[col][col]
        value *= entry
        for i in range(col+1, size):
            ratio = matrix[i][col]/entry
            for j in range(col+1, size):
                matrix[i][j] -= ratio*matrix[col][j]
            matrix[i][col] = F(0)
    return value


def permutation_sign(indices):
    return (-1)**sum(indices[i] > indices[j]
                     for i in range(len(indices))
                     for j in range(i+1, len(indices)))


def polynomial_wronskian(rows):
    # Rows retain their given order; derivative columns increase from zero.
    size = len(rows)
    entries = [[differentiate(row, j) for j in range(size)] for row in rows]
    answer = [F(0)]
    for perm in permutations(range(size)):
        term = [F(permutation_sign(perm))]
        for i in range(size):
            term = multiply(term, entries[i][perm[i]])
        answer = add(answer, term)
    return trim(answer)


def explicit_legendre(k):
    # Ordinary Legendre binomial formula in monic normalization.
    coefficients = [0]*(k+1)
    for j in range(k//2+1):
        degree = k-2*j
        multiplier = comb(k, j)*comb(2*k-2*j, k)
        for m in range(degree+1):
            coefficients[m] += multiplier*comb(degree, m)*2**m*(-1)**(degree-m)
    denominator = 2**k*comb(2*k, k)
    answer = [F(value, denominator) for value in coefficients]
    assert answer[-1] == 1
    return answer


def transform(polynomial):
    return trim([F(factorial(N), factorial(N+m))*c
                 for m, c in enumerate(polynomial)])


def volterra(polynomial):
    return trim([F(0)]+[c/F(N+m+1) for m, c in enumerate(polynomial)])


def phi(polynomial):
    return trim([F(0)]*(N+1)+[c/F(factorial(N+m+1))
                              for m, c in enumerate(polynomial)])


def ell(polynomial, j):
    assert 0 <= j <= B <= N
    assert N+1-j >= 1
    return sum((c/F(factorial(N+m+1-j))
                for m, c in enumerate(polynomial)), F(0))


def cb_wronskian(rows):
    # Separate coefficient construction using increasing monomial indices.
    size = len(rows)
    cancellation_order = size*(size-1)//2
    degree = sum(len(row)-1 for row in rows)-cancellation_order
    result = [F(0)]*(degree+1)
    for indices in combinations(range(max(map(len, rows))), size):
        minor = qdet([[row[m] if m < len(row) else F(0)
                       for m in indices] for row in rows])
        if minor == 0:
            continue
        vandermonde = 1
        for i in range(size):
            for j in range(i+1, size):
                vandermonde *= indices[j]-indices[i]
        exponent = sum(indices)-cancellation_order
        assert 0 <= exponent <= degree
        result[exponent] += minor*vandermonde
    return trim(result)


def bernstein_coefficients(polynomial):
    degree = len(polynomial)-1
    return [sum((polynomial[m]*F(comb(j, m), comb(degree, m))
                 for m in range(j+1)), F(0)) for j in range(degree+1)]


def bernstein_to_monomial(coefficients):
    degree = len(coefficients)-1
    result = [F(0)]*(degree+1)
    for j, value in enumerate(coefficients):
        for m in range(j, degree+1):
            result[m] += value*comb(degree, j)*comb(degree-j, m-j)*(-1)**(m-j)
    return trim(result)


def sign(value):
    return int(value > 0)-int(value < 0)


def strings(values):
    return [str(value) for value in values]


def hashes():
    return {str(path): sha256(path.read_bytes()).hexdigest()
            for path in (NOTE, SOURCE)}


def build():
    before = hashes()
    source = json.loads(SOURCE.read_text(encoding='utf-8'))
    existing = [row for row in source['records'] if row['n'] == N]
    assert len(existing) == 1 and existing[0]['b'] == B
    existing = existing[0]

    # Polynomial indices 0,...,8 belong to this one n=6 control.
    ps = [explicit_legendre(k) for k in range(N+B)]
    for k in range(1, N+B-1):
        beta = F(k*k, 4*(4*k*k-1))
        recurrence = add(multiply([F(-1,2), F(1)], ps[k]),
                         scale(ps[k-1], beta))
        assert recurrence == ps[k+1]

    transformed = [transform(p) for p in ps]
    rs = [transform(multiply([F(1), F(-1)], p)) for p in ps]
    for a, r in zip(transformed, rs):
        assert r == add(a, scale(volterra(a), -1))
    for k in range(1, N+B-1):
        beta = F(k*k, 4*(4*k*k-1))
        assert rs[k+1] == add(add(volterra(rs[k]), scale(rs[k], F(-1,2))),
                             scale(rs[k-1], beta))

    high_identity_checks = []
    for ell_index in range(1, B):
        k = N+ell_index
        a = power([F(1), F(-1), F(1,2)], k)
        h = [F(factorial(k), factorial(m))*a[k-m] for m in range(k+1)]
        rhs = scale(differentiate([F(0)]*k+h, ell_index-1), F(1, factorial(2*k)))
        assert rhs == phi(ps[k])
        high_identity_checks.append({'l': ell_index, 'polynomial_index': k,
                                     'H_coefficients_ascending': strings(h),
                                     'identity_matches': True})

    norms = [F(2*(-1)**k, (2*k+1)*comb(2*k,k)**2) for k in range(N+1)]
    weights = [at_one(ps[k])/norms[k] for k in range(N+1)]
    vpoly = [F(0)]
    for k in range(N+1):
        vpoly = add(vpoly, scale(ps[k], weights[k]))
    rv = transform(multiply([F(1), F(-1)], vpoly))
    rv_from_kernel = [F(0)]
    for k in range(N+1):
        rv_from_kernel = add(rv_from_kernel, scale(rs[k], weights[k]))
    assert rv == rv_from_kernel
    rv_from_cd = scale(add(scale(transformed[N], at_one(ps[N+1])),
                           scale(transformed[N+1], -at_one(ps[N]))), 1/norms[N])
    assert rv == rv_from_cd

    high_indices = list(range(N+1, N+B))
    high_rows = [rs[k] for k in high_indices]
    zpoly = polynomial_wronskian(high_rows+[rv])
    assert len(zpoly)-1 == B*(N+1)

    high_functionals = [[ell(ps[k], j) for j in range(B+1)] for k in high_indices]
    vrow = [ell(vpoly, j) for j in range(B+1)]
    erow = [F(1)]*(B+1)
    dv = qdet(high_functionals+[erow, vrow])
    reduced = high_functionals+[[1+value for value in vrow]]
    cofactor = [(-1)**(B+j)*qdet([[row[k] for k in range(B+1) if k != j]
                                 for row in reduced]) for j in range(B+1)]
    y = sum(cofactor, F(0))
    assert all(sum((entry*value for entry, value in zip(row, cofactor)), F(0)) == 0
               for row in reduced)
    assert y == -dv
    dv_from_z = F((-1)**(B+1), factorial(N)**B)*at_one(zpoly)
    assert dv == dv_from_z == F(existing['D_V']) != 0
    assert y == F(existing['cofactor_Y'])
    for polynomial in [ps[k] for k in high_indices]+[vpoly]:
        for j in range(B+1):
            assert at_one(differentiate(phi(polynomial), j)) == ell(polynomial, j)

    mixed = []
    first_witness = None
    combined = [F(0)]
    for k in range(N+1):
        rows = high_rows+[rs[k]]
        polynomial = scale(polynomial_wronskian(rows), weights[k])
        independent = scale(cb_wronskian(rows), weights[k])
        assert polynomial == independent
        degree = (B-1)*N+B+k
        assert len(polynomial)-1 == degree
        assert sign(polynomial[-1]) == (-1)**(k+1)
        coefficients = bernstein_coefficients(polynomial)
        assert bernstein_to_monomial(coefficients) == polynomial
        assert coefficients[0] == polynomial[0]
        assert coefficients[-1] == at_one(polynomial)
        signed = [SIGMA*value for value in coefficients]
        if first_witness is None:
            for j, value in enumerate(signed):
                if value < 0:
                    terms = [SIGMA*polynomial[u]*F(comb(j,u), comb(degree,u))
                             for u in range(j+1)]
                    assert sum(terms, F(0)) == value
                    first_witness = {
                        'order': 'Increasing k, then increasing Bernstein index j.',
                        'n': N, 'b': B, 'k': k, 'j': j, 'degree': degree,
                        'row_polynomial_indices': high_indices+[k],
                        'kernel_weight': str(weights[k]), 'proposed_sign': SIGMA,
                        'Bernstein_coefficient': str(coefficients[j]),
                        'signed_Bernstein_coefficient': str(value),
                        'signed_numerator': str(value.numerator),
                        'positive_denominator': str(value.denominator),
                        'weighted_monomial_coefficients_used': strings(polynomial[:j+1]),
                        'signed_basis_conversion_terms': strings(terms),
                        'exact_sum_matches_witness': True,
                        'consequence': 'Refutes the specified sufficient coefficient conjecture; does not refute endpoint nonvanishing.'
                    }
                    break
        mixed.append({
            'k': k, 'row_polynomial_indices': high_indices+[k],
            'kernel_weight': str(weights[k]), 'degree': degree,
            'weighted_monomial_coefficients_ascending': strings(polynomial),
            'Bernstein_coefficients_on_0_1': strings(coefficients),
            'Bernstein_signs': [sign(value) for value in coefficients],
            'signed_Bernstein_coefficients': strings(signed),
            'signed_Bernstein_signs': [sign(value) for value in signed],
            'negative_signed_indices': [j for j,value in enumerate(signed) if value < 0],
            'zero_signed_indices': [j for j,value in enumerate(signed) if value == 0],
            'minimum_signed_coefficient': str(min(signed)),
            'minimum_attained_at': [j for j,value in enumerate(signed) if value == min(signed)],
            'weighted_value_at_zero': str(polynomial[0]),
            'weighted_value_at_one': str(at_one(polynomial)),
            'direct_Wronskian_equals_Cauchy_Binet': True,
            'Bernstein_reconstruction_exact': True
        })
        combined = add(combined, polynomial)
    assert combined == zpoly
    assert sum(F(row['weighted_value_at_one']) for row in mixed) == at_one(zpoly)
    coefficient_count = sum(len(row['Bernstein_coefficients_on_0_1']) for row in mixed)
    assert coefficient_count == 133
    minimum_sum = sum((F(row['minimum_signed_coefficient']) for row in mixed), F(0))
    if first_witness is not None:
        status = 'REFUTED_SPECIFIED_SUFFICIENT_COEFFICIENT_CONJECTURE'
    elif minimum_sum > 0:
        status = 'COMPLETE_FROZEN_CONTROL_PASS_FINITE_ONLY'
    else:
        status = 'NO_NEGATIVE_COEFFICIENT_BUT_REQUIRED_STRICT_MARGIN_NOT_ESTABLISHED'
    assert hashes() == before
    return {
        'schema': 'astra-agent3-bernstein-next-control-v1',
        'status': status,
        'scope': 'Exactly n=6,b=3. The complete requested single control is retained; no other HP index, prime, or uniform-proof computation is performed.',
        'n': N, 'b': B, 'proposed_sign': SIGMA,
        'basis': 'binom(L,j)*x^j*(1-x)^(L-j), using each polynomial actual degree L=15+k; no degree elevation.',
        'orientation': 'Wr(r_7,r_8,r_k) has rows in that order and derivative columns 0,1,2; w_k=p_k(1)/h_k.',
        'endpoint_orientation': 'D_V=Wr(Phi(p_7),Phi(p_8),exp(x-1),Phi(V))(1)=Z(1)/(6!)^3; Y=-D_V.',
        'factorial_domain': {
            'functional_indices': [0,1,2,3],
            'minimum_ell_factorial_argument': N+1-B,
            'transform_factorial_arguments_minimum': N,
            'transform_factorial_arguments_maximum': N+(N+B),
            'difference_dimension': B,
            'permitted_ordinary_dimension': B+1,
            'negative_factorial_extension_used': False
        },
        'input_construction': 'Explicit ordinary Legendre binomial coefficients, checked against the monic recurrence.',
        'mixed_constructions': ['Direct polynomial derivative determinant with permutation signs.',
                               'Rational coefficient minors times the increasing-index Vandermonde.'],
        'monic_p_coefficients_ascending': {str(k): strings(p) for k,p in enumerate(ps)},
        'r_coefficients_ascending': {str(k): strings(r) for k,r in enumerate(rs)},
        'kernel_weights': strings(weights),
        'high_function_identity_checks': high_identity_checks,
        'Volterra_recurrence_checked': True,
        'Christoffel_Darboux_transform_checked': True,
        'V_coefficients_ascending': strings(vpoly),
        'r_V_coefficients_ascending': strings(rv),
        'Z_coefficients_ascending': strings(zpoly),
        'mixed_weighted_Wronskians': mixed,
        'coefficient_count': coefficient_count,
        'sum_of_row_minimum_signed_coefficients': str(minimum_sum),
        'first_negative_signed_coefficient': first_witness,
        'endpoint': {
            'Z_at_one': str(at_one(zpoly)),
            'D_V_direct_functional_determinant': str(dv),
            'D_V_from_reduced_Wronskian': str(dv_from_z),
            'existing_D_V': existing['D_V'],
            'cofactor_B': strings(cofactor),
            'cofactor_Y': str(y),
            'existing_cofactor_Y': existing['cofactor_Y'],
            'matches_existing_certificate': True,
            'nonzero_at_this_frozen_control': True,
            'sum_of_mixed_polynomials_matches_Z': True
        },
        'source_sha256': before,
        'source_files_unchanged_during_run': True,
        'checker_sha256': sha256(SCRIPT.read_bytes()).hexdigest(),
        'all_exact_identity_checks_pass': True,
        'unbounded_nonvanishing_claim': False,
        'uniform_sign_proof_attempted_after_negative_witness': False
    }


def encode(value):
    return json.dumps(value, indent=2, ensure_ascii=True)+'\n'


def main():
    assert sys.argv[1:] in ([], ['--verify']), 'Use no arguments or --verify.'
    certificate = build()
    certificate_text = encode(certificate)
    summary = {
        'status': certificate['status'], 'n': N, 'b': B, 'proposed_sign': SIGMA,
        'coefficient_count': certificate['coefficient_count'],
        'per_k_sign_counts': [{
            'k': row['k'], 'degree': row['degree'],
            'negative': row['signed_Bernstein_signs'].count(-1),
            'zero': row['signed_Bernstein_signs'].count(0),
            'positive': row['signed_Bernstein_signs'].count(1),
            'minimum_signed_coefficient': row['minimum_signed_coefficient'],
            'weighted_value_at_one': row['weighted_value_at_one']
        } for row in certificate['mixed_weighted_Wronskians']],
        'first_negative_signed_coefficient': certificate['first_negative_signed_coefficient'],
        'endpoint': certificate['endpoint'],
        'sum_of_row_minimum_signed_coefficients': certificate['sum_of_row_minimum_signed_coefficients'],
        'all_exact_identity_checks_pass': True,
        'certificate_bytes': len(certificate_text.encode('utf-8')),
        'certificate_sha256': sha256(certificate_text.encode('utf-8')).hexdigest()
    }
    summary_text = encode(summary)
    outputs = [(BASE/'bernstein_next_control_certificate.json', certificate_text),
               (BASE/'bernstein_next_control_summary.json', summary_text)]
    if sys.argv[1:] == ['--verify']:
        for path, content in outputs:
            assert path.read_text(encoding='utf-8') == content
        print('Stored frozen-control certificate and summary reproduce exactly.')
    else:
        for path, content in outputs:
            path.write_text(content, encoding='utf-8')
    print(summary_text)


if __name__ == '__main__':
    main()
