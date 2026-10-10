"""Independent finite certificate: ONLY primes 71 and 83, every residue.

No source checker is imported. Every normalized cofactor is reconstructed
by its own Jacobi--Trudi determinant, using a generating-function recurrence.
Positive endpoints use Q times truncated exp, not the V endpoint border.
Negative endpoints use a polynomial/Stirling functional, not differences.
All arithmetic is exact in the specified prime fields.
"""
import hashlib
import json
from math import comb, factorial
from pathlib import Path

BASE = Path(__file__).resolve().parent
PRIMES = (71, 83)


def determinant(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    value = 1
    n = len(a)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            value = -value
        entry = a[j][j]
        value = value * entry % p
        inverse = pow(entry, -1, p)
        for i in range(j + 1, n):
            scale = a[i][j] * inverse % p
            a[i][j] = 0
            if scale:
                for h in range(j + 1, n):
                    a[i][h] = (a[i][h] - scale * a[j][h]) % p
    return value % p


def coefficients(background, degree, p):
    # (1+t^2) H'=(1+t^2+2 b t) H for H=e^t(1+t^2)^b.
    a = [1]
    for d in range(degree):
        numerator = a[d]
        if d >= 1:
            numerator += (2 * background - d + 1) * a[d - 1]
        if d >= 2:
            numerator += a[d - 2]
        a.append(numerator * pow(d + 1, -1, p) % p)
    return a


def augmented_schur(partition, a, p):
    length = len(partition)
    matrix = []
    for i in range(length):
        matrix.append([a[partition[i] - i + j]
                       if partition[i] - i + j >= 0 else 0
                       for j in range(length)])
    hooks = 1
    for i, width in enumerate(partition):
        for j in range(width):
            leg = sum(partition[h] > j for h in range(i + 1, length))
            hooks = hooks * (width - j + leg) % p
    assert hooks != 0
    det = determinant(matrix, p)
    return det * hooks % p, det, hooks


def seed_cofactors(k, background, p):
    assert 0 < 2 * k < p
    a = coefficients(background, 2 * k, p)
    full, det, hooks = augmented_schur([k] * (k + 1), a, p)
    cofactors, witnesses = [], []
    for i in range(k + 1):
        partition = [k + 1] * (k - i) + [k] * i
        value, minor, hook = augmented_schur(partition, a, p)
        cofactors.append(value)
        witnesses.append(dict(i=i, determinant=minor, hook_product=hook))
    return full, cofactors, dict(
        background=background, complete_coefficients=a,
        full_JT_determinant=det, full_hook_product=hooks,
        direct_cofactor_determinants=witnesses)


def multiply(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] = (c[i + j] + v * w) % p
    return c


def positive_endpoint(k, C, p):
    b = [(-1) ** (k - j) * comb(k, j) * C[j] % p
         for j in range(k + 1)]
    U = [factorial(k + j) * b[j] % p for j in range(k + 1)]
    even = [0] * (2 * k + 1)
    for j in range(k + 1):
        even[2 * j] = comb(k, j) % p
    S = multiply(U, even, p)
    Q = [comb(3 * k - j, k) * S[3 * k - j] % p
         for j in range(2 * k + 1)]
    inverse_factorials = [pow(factorial(j), -1, p)
                         for j in range(2 * k + 1)]
    Pe = [sum(Q[j] * inverse_factorials[h - j]
              for j in range(h + 1)) % p for h in range(2 * k + 1)]
    # Original high moment conditions are independent normalization checks.
    for h in range(2 * k + 1, 3 * k + 1):
        # Multiply by h! first; this remains integral even when h>=p.
        assert sum(Q[j] * falling(h, j) for j in range(2 * k + 1)) % p == 0
    return sum(Pe) % p, dict(b=b, U=U, S=S, Q=Q,
                             Pe_coefficients=Pe,
                             factorial_cleared_high_moments_zero=True)


def falling(n, j):
    v = 1
    for h in range(j):
        v *= n - h
    return v


def rising(n, j):
    v = 1
    for h in range(j):
        v *= n + h
    return v


def negative_endpoint(k, C, p):
    r = p - k - 1
    b = [(-1) ** (r - i) * comb(r, i) * C[i] % p
         for i in range(k + 1)]
    high = [sum(comb(r, u) * rising(r + i + 1, 2 * u) * b[i + 2 * u]
                for u in range((k - i) // 2 + 1)) % p
            for i in range(k + 1)]
    jets = [factorial(h) * sum(comb(r + i, r + h) * high[i]
                              for i in range(h, k + 1)) % p
            for h in range(k + 1)]
    # Build f(X)=sum_s binom(r+s,s)(r+X)_s as an ordinary polynomial.
    f = [0] * (k + 1)
    term = [1]
    for s in range(k + 1):
        weight = comb(r + s, s) % p
        for j, c in enumerate(term):
            f[j] = (f[j] + weight * c) % p
        term = multiply(term, [(r - s) % p, 1], p)
    # X^d=sum_h Stirling2(d,h) (X)_h converts Euler to ordinary jets.
    stirling = [[1]]
    for d in range(1, k + 1):
        prev = stirling[-1]
        row = [0] * (d + 1)
        for h in range(1, d + 1):
            row[h] = (prev[h - 1] + (h * prev[h] if h < d else 0)) % p
        stirling.append(row)
    functional = [sum(f[d] * stirling[d][h] for d in range(h, k + 1)) % p
                  for h in range(k + 1)]
    E = sum(x * y for x, y in zip(functional, jets)) % p
    return E, dict(selected_b=b, high_coefficients=high, jets=jets,
                   ordinary_endpoint_polynomial=f,
                   Stirling_jet_functional=functional)


def run():
    reference_path = BASE / 'raw_second_predeclared_uniform_seed_certificate.json'
    reference = json.loads(reference_path.read_text())
    references = {r['p']: r for r in reference['results'] if r['p'] in PRIMES}
    assert set(references) == set(PRIMES)
    results = []
    direct_determinants = 0
    for p in PRIMES:
        assert all(p % divisor for divisor in range(2, 10))
        ref = references[p]
        rows = ref['complete_classes']
        assert ref['all_residues_good'] and len(rows) == p
        assert [r['residue'] for r in rows] == list(range(p))
        calculated = []
        for residue in range(p):
            positive = residue <= (p - 1) // 2
            branch = 'positive' if positive else 'negative'
            k = residue if positive else p - 1 - residue
            old = rows[residue]
            assert (old['p'], old['branch'], old['k']) == (p, branch, k)
            assert 2 * k < p if positive else 2 * k + 1 < p
            if k == 0:
                D, E, C, proof, endpoint = 1, 1, [], {}, {}
            else:
                D, C, proof = seed_cofactors(k, k if positive else -k - 1, p)
                direct_determinants += k + 2
                E, endpoint = (positive_endpoint if positive else negative_endpoint)(k, C, p)
                assert C == old['matrix_certificate']['cofactor_values_gamma_i'], (p, residue, 'cofactors')
                assert proof['full_JT_determinant'] == old['matrix_certificate']['Jacobi_Trudi_determinant']
                if positive:
                    assert endpoint['b'] == old['scaled_B']
                else:
                    assert endpoint['jets'] == old['J']
                    assert endpoint['Stirling_jet_functional'] == old['A']
                    assert endpoint['jets'][0] == D
            assert D and E, (p, residue, 'not a unit', D, E)
            assert (D, E) == (old['D'], old['E']), (p, residue, 'endpoint')
            assert old['status'] == 'good'
            assert E * pow(D, -1, p) % p == old['endpoint_over_V1']
            calculated.append(dict(residue=residue, branch=branch, k=k,
                                   D=D, E=E, cofactors=C,
                                   determinant_witness=proof, endpoint_witness=endpoint,
                                   all_source_values_match=True, gate_is_unit=True))
        results.append(dict(p=p, every_residue_checked=True, all_residues_good=True,
                            positive_count=(p + 1) // 2, negative_count=(p - 1) // 2,
                            classes=calculated))
        print(f'PASS: p={p}, all {p} residue classes, independently normalized endpoints')
    payload = dict(status='PASS', scope='Only primes 71 and 83; all 154 residue classes.',
                   source_json_sha256=hashlib.sha256(reference_path.read_bytes()).hexdigest(),
                   source_checker_sha256=hashlib.sha256((BASE / 'check_second_predeclared_uniform_seed_list.py').read_bytes()).hexdigest(),
                   independent_direct_determinants=direct_determinants,
                   method='Generating-function coefficient recurrence; separate direct JT determinant for every full shape and cofactor; Q-exp positive endpoint; polynomial/Stirling negative endpoint.',
                   results=results)
    target = BASE / 'uniform_71_83_independent_certificate.json'
    target.write_text(json.dumps(payload, indent=2) + '\n')
    print(f'PASS: {direct_determinants} independent direct determinants; {target}')


if __name__ == '__main__':
    run()
