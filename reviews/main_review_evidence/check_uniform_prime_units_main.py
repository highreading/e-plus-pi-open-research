"""Finite independent main control of the exact ten-prime theorem inputs.

No archived Python is imported/executed. Only three locked JSON inputs
are read; the only output is inside this main work directory.
"""
from pathlib import Path
from math import comb, factorial as fac, isqrt
from functools import lru_cache
import hashlib
import json
import time

BASE = Path(__file__).resolve().parent
ROOT = Path('work/session_20260913')
PRIMES = (3, 7, 23, 43, 71, 83, 101, 109, 127, 151)
LOCKS = {
    'raw_predeclared_residue_seed_atlas.json': '48e6f9f9e07c72709e775601c6fd555dd6ba00221f1013f2161114e335695b16',
    'raw_second_predeclared_uniform_seed_certificate.json': '864873094eb83e9a2bc316ae301109119b4280109d5c6aff8830307dc6ea1bb6',
    'raw_third_predeclared_uniform_seed_certificate.json': '0c5b654d5bdff206eb6cc66c88ba5850b1beca7c4d258690935a9a055b22a033',
}


def choose(b, h):
    if h < 0:
        return 0
    if b >= 0:
        return comb(b, h) if h <= b else 0
    return (-1) ** h * comb(h - b - 1, h)


def falling(b, h):
    out = 1
    for j in range(h):
        out *= b - j
    return out


def rising(b, h):
    return falling(b + h - 1, h)


def multiply(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def eliminate(matrix, p, rhs=None):
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    b = list(rhs) if rhs is not None else None
    value, steps = 1, []
    for j in range(n):
        pivot_row = next((i for i in range(j, n) if a[i][j]), None)
        if pivot_row is None:
            return 0, None, steps
        if pivot_row != j:
            a[j], a[pivot_row] = a[pivot_row], a[j]
            if b is not None:
                b[j], b[pivot_row] = b[pivot_row], b[j]
            value = -value
        pivot = a[j][j]
        value = value * pivot % p
        steps.append([j, pivot_row, pivot])
        inverse = pow(pivot, -1, p)
        for i in range(j + 1, n):
            ratio = a[i][j] * inverse % p
            if ratio:
                a[i][j:] = [(x - ratio * y) % p for x, y in zip(a[i][j:], a[j][j:])]
                if b is not None:
                    b[i] = (b[i] - ratio * b[j]) % p
    if b is None:
        return value % p, None, steps
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = (b[i] - sum(a[i][j] * solution[j] for j in range(i + 1, n))) * pow(a[i][i], -1, p) % p
    assert all(sum(x * y for x, y in zip(row, solution)) % p == rhs[i] % p for i, row in enumerate(matrix))
    return value % p, solution, steps


@lru_cache(None)
def coefficients(background, degree, p):
    # Direct finite binomial expansion, independently of archived recurrences.
    assert degree < p
    return tuple(sum(choose(background, h) * pow(fac(d - 2 * h), -1, p)
                     for h in range(d // 2 + 1)) % p for d in range(degree + 1))


def hook(partition, p):
    out = 1
    for i, width in enumerate(partition):
        for j in range(width):
            out = out * (width - j + sum(r > j for r in partition[i + 1:])) % p
    assert out
    return out


def full_seed(k, background, p):
    h = coefficients(background, 2 * k, p)
    a = [[h[k + i - j] if k + i >= j else 0 for j in range(k + 1)] for i in range(k + 1)]
    determinant, column, _ = eliminate(a, p, [1] + [0] * k)
    full_hook = hook((k,) * (k + 1), p)
    d = full_hook * determinant % p
    assert d and column is not None
    c = []
    for i in range(k + 1):
        shape = (k + 1,) * (k - i) + (k,) * i
        c.append(hook(shape, p) * (-1) ** (k - i) * determinant * column[k - i] % p)
    return d, c, h, a


def original_border(n, j, p):
    return sum(comb(n + s, s) * falling(n + j, s) for s in range(n + j + 1)) % p


def positive(k, c, p):
    b = [(-1) ** (k - j) * comb(k, j) * c[j] % p for j in range(k + 1)]
    u = [fac(k + j) * b[j] % p for j in range(k + 1)]
    s = multiply(u, [comb(k, j // 2) if j % 2 == 0 else 0 for j in range(2 * k + 1)], p)
    q = [comb(3 * k - j, k) * s[3 * k - j] % p for j in range(2 * k + 1)]
    pe = [sum(q[j] * pow(fac(r - j), -1, p) for j in range(r + 1)) % p for r in range(2 * k + 1)]
    # Independent differential reconstruction and original V border.
    rhs = [0] * (2 * k + 1)
    for j, x in enumerate(b):
        for h in range((k + j) // 2 + 1):
            rhs[k + j - 2 * h] = (rhs[k + j - 2 * h] + comb(k, h) * falling(k + j, 2 * h) * x) % p
    divisor = [(-1) ** (k - j) * comb(k, j) for j in range(k + 1)]
    v = [0] * (k + 1)
    for j in range(k, -1, -1):
        v[j] = rhs[k + j]
        for h, x in enumerate(divisor):
            rhs[j + h] = (rhs[j + h] - v[j] * x) % p
    assert not any(rhs)
    high = multiply(v, divisor, p)[k:]
    border = [original_border(k, j, p) for j in range(k + 1)]
    e = sum(pe) % p
    assert e == sum(x * y for x, y in zip(v, border)) % p
    return e, {'scaled_B': b, 'scaled_high_W': high, 'scaled_V': v, 'border': border}


def negative(k, c, p):
    n = p - k - 1
    selected_b = [(-1) ** (n - j) * comb(n, j) * c[j] % p for j in range(k + 1)]
    high = [sum(comb(n, u) * rising(n + i + 1, 2 * u) * selected_b[i + 2 * u]
                for u in range((k - i) // 2 + 1)) % p for i in range(k + 1)]
    jets = [fac(h) * sum(comb(n + i, n + h) * high[i] for i in range(h, k + 1)) % p for h in range(k + 1)]
    toy = [sum(jets[h] * pow(fac(h), -1, p) * comb(h, j) * (-1) ** (h - j)
               for h in range(j, k + 1)) % p for j in range(k + 1)]
    e = sum(toy[j] * original_border(n, j, p) for j in range(k + 1)) % p
    b = -k - 1
    functional = [sum((-1) ** s * comb(k, s) * comb(s, h) * falling(b, s - h)
                      for s in range(h, k + 1)) % p for h in range(k + 1)]
    direct_jets = [fac(h) * sum((-1) ** (k - i) * choose(b + i, i - h)
                              * sum(choose(b, u) * rising(b + i + 1, 2 * u)
                                    * choose(b, i + 2 * u) * c[i + 2 * u]
                                    for u in range((k - i) // 2 + 1))
                              for i in range(h, k + 1)) % p for h in range(k + 1)]
    assert jets == direct_jets
    assert e == sum(x * y for x, y in zip(jets, functional)) % p
    return e, {'J': jets, 'A': functional}


def check_matrix_certificate(record, k, background, p, d, c, h, a):
    cert = record.get('matrix_certificate')
    if cert is None:
        return
    degrees = list(range(k, 2 * k + 1))
    assert cert['background'] == background and cert['k'] == k and cert['Appell_degrees'] == degrees
    w = [[falling(degree, j) * fac(degree - j) * h[degree - j] % p if degree >= j else 0
          for j in range(k + 1)] for degree in degrees]
    assert cert['Wronskian_matrix'] == w
    delta = 1
    for j in range(1, k + 1):
        delta = delta * fac(j) % p
    wt = [list(row) for row in zip(*w)]
    wd, inverse_last, pivots = eliminate(wt, p, [0] * k + [1])
    assert cert['Wronskian_determinant'] == wd and cert['Vandermonde'] == delta
    assert wd * pow(delta, -1, p) % p == d
    assert cert['transpose_elimination_pivots'] == pivots and cert['inverse_last_row'] == inverse_last
    assert cert['cofactor_values_gamma_i'] == c
    jt = [list(row) for row in zip(*a)]
    jd, _, jp = eliminate(jt, p)
    assert cert['Jacobi_Trudi_matrix'] == jt and cert['Jacobi_Trudi_determinant'] == jd
    assert cert['Jacobi_Trudi_pivots'] == jp and cert['hook_product'] == hook((k,) * (k + 1), p)
    assert cert['full_augmented_value'] == d and cert['determinant_formulas_agree'] is True
    assert cert['inverse_row_residual_checked'] is True


started = time.monotonic()
expected = {}
for name, digest in LOCKS.items():
    raw = (ROOT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest
    data = json.loads(raw)
    for prime in data.get('atlas', data.get('results', [])):
        if prime['p'] in PRIMES:
            assert prime['all_residues_good'] is True
            records = prime.get('classes', prime.get('complete_classes'))
            assert records is not None and len(records) == prime['p']
            assert [r['residue'] for r in records] == list(range(prime['p']))
            assert prime['p'] not in expected
            expected[prime['p']] = records
assert set(expected) == set(PRIMES) - {3, 7}
answers = []
for p in PRIMES:
    assert all(p % t for t in range(2, isqrt(p) + 1))
    rows = []
    for residue in range(p):
        positive_branch = residue <= (p - 1) // 2
        branch = 'positive' if positive_branch else 'negative'
        k = residue if positive_branch else p - 1 - residue
        assert 2 * k < p if positive_branch else 2 * k + 1 < p
        if k == 0:
            d, c, e, extra = 1, [1], 1, {}
        else:
            background = k if positive_branch else -k - 1
            d, c, h, a = full_seed(k, background, p)
            e, extra = (positive if positive_branch else negative)(k, c, p)
            assert (sum(extra['scaled_V']) if positive_branch else extra['J'][0]) % p == d
        assert d and e
        ratio = e * pow(d, -1, p) % p
        if p in expected:
            old = expected[p][residue]
            assert (old['branch'], old['k'], old['D'], old['E'], old['status']) == (branch, k, d, e, 'good')
            assert old['endpoint_over_V1'] == ratio
            if k:
                if 'C' in old:
                    # First atlas labels positive cofactors by inverse column j;
                    # later matrices and negative seeds label by omitted degree i.
                    assert old['C'] == (c[::-1] if positive_branch else c)
                else:
                    assert old['matrix_certificate']['cofactor_values_gamma_i'] == c
                for field, value in extra.items():
                    if field in old:
                        assert old[field] == value, (p, residue, field)
                check_matrix_certificate(old, k, background, p, d, c, h, a)
        rows.append({'residue': residue, 'branch': branch, 'k': k, 'D': d, 'E': e, 'C': c, 'ratio': ratio})
    answers.append({'p': p, 'all_residues_checked': True, 'residue_count': len(rows), 'rows': rows})
    print(json.dumps({'p': p, 'all_residues_checked': len(rows), 'all_seed_units': True}), flush=True)
out = {'reviewer': 'main Codex', 'finite_control_only': True,
       'scope': 'All718 small fixed residue seeds at the ten listed primes; all full matrices stored inside the selected class records, inverse residuals, hooks, pivot traces, cofactors and endpoints reconstructed. Separate atlas determinant registries, other prime rows and entire JSON containers are not approved.',
       'primes': list(PRIMES), 'selected_locked_inputs': LOCKS, 'original_code_executed': False,
       'original_data_modified': False, 'all_degree_theorems_proved_by_finite_testing': False,
       'empty_negative_seed_requires_separate_n_plus_1_theorem': True,
       'all_controls_passed': True, 'elapsed_seconds': time.monotonic() - started, 'results': answers}
(BASE / 'RAW_UNIFORM_PRIME_UNIT_MAIN_CONTROL.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'results'}, ensure_ascii=False))
