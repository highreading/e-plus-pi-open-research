"""Predeclared bounded scalar-prime extension; exact arithmetic only.

Run from the research workspace root. The default writes the certificate
and its summary exclusively in this agent's directory. --verify regenerates
both deterministically and compares them without writing. No old atlas is
executed, no canonical HP nullspace is constructed, and no network is used.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb, isqrt
from pathlib import Path
import json
import sys

OUT = Path('work/session_20261001_astra/agent3')
CANDIDATES = (23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
              79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
              137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
              191, 193, 197, 199)
BASE_PRIMES = (5, 13)
COORDINATES = ('H', 'K', 'Acal', 'Bcal', 'Ccal')
DEPENDENCIES = (
    'work/session_20260927/hp_b1_prime_seed_transfer_and_closed_atlas.md',
    'work/session_20260927/hp_b1_ternary_actual_denominator.md',
    'work/session_20260927/hp_b1_residue_one_actual_numerator.md',
    'work/session_20260927/hp_b1_uniform_5_13_independent_review.md',
    'work/session_20260927/hp_b1_uniform_five_thirteen_and_even_exclusion.md',
    'work/session_20260927/fixed_exponential_degree_error_theorem.md',
)


def fraction_record(x):
    x = F(x)
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def phi_step(coefficients, p):
    """Multiply by 1-x+x^2/2 in F_p[x]."""
    result = [0] * (len(coefficients) + 2)
    half = pow(2, -1, p)
    for j, value in enumerate(coefficients):
        result[j] = (result[j] + value) % p
        result[j + 1] = (result[j + 1] - value) % p
        result[j + 2] = (result[j + 2] + half * value) % p
    return result


def modular_scalar_rows(p):
    """Construction I: complete modular Rodrigues contractions."""
    d = [1]
    for j in range(1, 2 * p):
        d.append((j * d[-1] + 1) % p)
    coefficients = [1]
    rows = []
    for n in range(p):
        adjacent = phi_step(coefficients, p)
        h = a = 0
        falling = 1
        for s in range(n + 1):
            if s:
                falling = falling * (n - s + 1) % p
            term = falling * coefficients[s] % p
            h = (h + term) % p
            a = (a + term * d[2 * n - s]) % p
        k = 2 % p
        b = 2 * d[2 * n + 1] % p
        falling = 1
        for s in range(1, n + 2):
            if s > 1:
                falling = falling * (n - s + 2) % p
            term = falling * (2 * n + 2 - s) * adjacent[s] % p
            k = (k + term) % p
            b = (b + term * d[2 * n + 1 - s]) % p
        rows.append([h, k, a, b, (k * a - h * b) % p])
        coefficients = adjacent
    assert len(rows) == p
    assert rows[0] == [1, 1, 1, 3 % p, (-2) % p]
    assert rows[1] == [0, 0, 3 % p, 10 % p, 0]
    return rows


_FACTORIALS = [1]
_PARTIALS = [F(1)]


def factorial(n):
    while len(_FACTORIALS) <= n:
        j = len(_FACTORIALS)
        _FACTORIALS.append(j * _FACTORIALS[-1])
    return _FACTORIALS[n]


def exponential_partial(n):
    """Exact sum of reciprocal factorials; no modular D recurrence."""
    while len(_PARTIALS) <= n:
        j = len(_PARTIALS)
        _PARTIALS.append(_PARTIALS[-1] + F(1, factorial(j)))
    return _PARTIALS[n]


@lru_cache(maxsize=None)
def legendre_coefficients(k):
    """Ordinary Legendre binomial formula after the stated change of variable.

    L_k(t) = sum_j (2k-2j)!/[j!(k-j)!(k-2j)!] (2t-1)^(k-2j).
    This construction uses neither Rodrigues contractions nor their recurrence.
    """
    coefficients = [0] * (k + 1)
    for j in range(k // 2 + 1):
        degree = k - 2 * j
        denominator = factorial(j) * factorial(k - j) * factorial(degree)
        multiplier, remainder = divmod(factorial(2 * k - 2 * j), denominator)
        assert remainder == 0
        for r in range(degree + 1):
            coefficients[r] += (multiplier * comb(degree, r) * (2 ** r)
                                * (-1) ** (degree - r))
    return tuple(coefficients)


@lru_cache(maxsize=None)
def rational_scalar_seed(n):
    """Construction II: integer Legendre coefficients and rational functionals.

    Both polynomials use factorial index n+j, including the adjacent one.
    Normalization is performed over Q before reduction modulo any prime.
    """
    factorial_values = []
    exponential_values = []
    for k in (n, n + 1):
        coefficients = legendre_coefficients(k)
        factorial_values.append(sum(
            (F(c, factorial(n + j)) for j, c in enumerate(coefficients)), F(0)))
        exponential_values.append(sum(
            (c * exponential_partial(n + j)
             for j, c in enumerate(coefficients)), F(0)))
    scale = F(factorial(n) ** 2, 2 ** n)
    adjacent_scale = scale * F(n + 1, 2)
    h = scale * factorial_values[0]
    k = adjacent_scale * factorial_values[1]
    a = scale * exponential_values[0]
    b = adjacent_scale * exponential_values[1]
    result = (h, k, a, b, k * a - h * b)
    assert h.denominator == k.denominator == 1
    for value in result:
        denominator = value.denominator
        assert denominator > 0 and denominator & (denominator - 1) == 0
    if n == 0:
        assert result == (F(1), F(1), F(1), F(3), F(-2))
    if n == 1:
        assert result == (F(0), F(0), F(3), F(10), F(0))
    return result


def reduce_fraction(x, p):
    assert x.denominator % p != 0
    return x.numerator * pow(x.denominator, -1, p) % p


def atanh_log_interval(z, terms):
    """Bounds for log((1+z)/(1-z)), for 0 <= z < 1.

    The positive tail is at most
    2*z^(2m+1)/((2m+1)*(1-z^2)), with m=terms.
    """
    assert 0 <= z < 1 and terms >= 1
    total = F(0)
    power = z
    square = z * z
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= square
    error = 2 * power / ((2 * terms + 1) * (1 - square))
    return total, total + error


def log_interval(x, terms):
    """Exact rational bounds, reducing x by powers of 2 first."""
    x = F(x)
    assert x >= 1
    exponent = 0
    while x >= 2:
        x /= 2
        exponent += 1
    two_lo, two_hi = atanh_log_interval(F(1, 3), terms)
    lo, hi = atanh_log_interval((x - 1) / (x + 1), terms)
    return exponent * two_lo + lo, exponent * two_hi + hi


def floor_fraction(x):
    return x.numerator // x.denominator


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def outward_round(lo, hi, scale):
    return F(floor_fraction(lo * scale), scale), F(ceil_fraction(hi * scale), scale)


def rate_certificate(primes):
    """Compare W=sum 2 log(p)/(p-1) with tau=2 log(1+sqrt(2)).

    Arithmetic precision may increase; the prime bound never changes.
    """
    terms, sqrt_bits, decimal_digits = 16, 64, 12
    while True:
        scale = 10 ** decimal_digits
        denominator = 2 ** sqrt_bits
        root_floor = isqrt(2 * denominator * denominator)
        assert root_floor ** 2 < 2 * denominator ** 2 < (root_floor + 1) ** 2
        root_lo = F(root_floor, denominator)
        root_hi = F(root_floor + 1, denominator)
        lower_argument = 1 + root_lo
        upper_argument = 1 + root_hi
        tau_lo_raw = 2 * log_interval(lower_argument, terms)[0]
        tau_hi_raw = 2 * log_interval(upper_argument, terms)[1]
        tau_lo, tau_hi = outward_round(tau_lo_raw, tau_hi_raw, scale)
        w_lo = F(0)
        w_hi = F(0)
        prime_bounds = {}
        for p in primes:
            lo, hi = outward_round(*log_interval(F(p), terms), scale)
            prime_bounds[str(p)] = {'lower': fraction_record(lo),
                                    'upper': fraction_record(hi)}
            w_lo += F(2, p - 1) * lo
            w_hi += F(2, p - 1) * hi
        if w_lo > tau_hi:
            verdict = 'above'
        elif w_hi < tau_lo:
            verdict = 'below'
        else:
            terms *= 2
            sqrt_bits *= 2
            decimal_digits *= 2
            continue
        coarse_scale = 10 ** 6
        coarse_w = F(floor_fraction(w_lo * coarse_scale), coarse_scale)
        coarse_tau = F(ceil_fraction(tau_hi * coarse_scale), coarse_scale)
        return {
            'uniform_primes': list(primes),
            'verdict': verdict,
            'log_series_terms': terms,
            'rounding_scale': str(scale),
            'sqrt2_bracket': {
                'denominator': str(denominator),
                'lower_numerator': str(root_floor),
                'upper_numerator': str(root_floor + 1),
                'lower_square_gap': str(2 * denominator ** 2 - root_floor ** 2),
                'upper_square_gap': str((root_floor + 1) ** 2 - 2 * denominator ** 2),
            },
            'log_p_bounds': prime_bounds,
            'W_lower': fraction_record(w_lo),
            'W_upper': fraction_record(w_hi),
            'tau_lower': fraction_record(tau_lo),
            'tau_upper': fraction_record(tau_hi),
            'strict_gap_lower': fraction_record(w_lo - tau_hi),
            'coarse_W_lower': fraction_record(coarse_w),
            'coarse_tau_upper': fraction_record(coarse_tau),
            'coarse_gap_lower': fraction_record(coarse_w - coarse_tau),
        }


def build_certificate():
    assert CANDIDATES == tuple(p for p in range(23, 200) if is_prime(p))
    assert len(CANDIDATES) == 38
    records = []
    selected = []
    exact_seeds = {}
    history = [rate_certificate(BASE_PRIMES)]
    assert history[0]['verdict'] == 'below'
    for p in CANDIDATES:
        rows = modular_scalar_rows(p)
        zeros = [r for r, row in enumerate(rows) if row[4] == 0]
        assert 1 in zeros
        record = {
            'p': p,
            'Ccal_zero_set': zeros,
            'selected': zeros == [1],
            'modular_H_K_Acal_Bcal_Ccal': rows,
            'second_construction_checked': False,
        }
        if zeros == [1]:
            independent_rows = []
            for r in range(p):
                values = rational_scalar_seed(r)
                independent = [reduce_fraction(x, p) for x in values]
                assert independent == rows[r], (p, r, rows[r], independent)
                independent_rows.append(independent)
                if r not in exact_seeds:
                    exact_seeds[r] = [fraction_record(x) for x in values]
            record['legendre_H_K_Acal_Bcal_Ccal'] = independent_rows
            record['second_construction_checked'] = True
            record['all_five_coordinates_match_at_every_residue'] = True
            selected.append(p)
            history.append(rate_certificate(BASE_PRIMES + tuple(selected)))
        records.append(record)
        print(json.dumps({'p': p, 'Ccal_zero_set': zeros,
                          'selected_after_exact_comparison': record['selected']}), flush=True)
        if history[-1]['verdict'] == 'above':
            break
    tested = [record['p'] for record in records]
    assert tested == list(CANDIDATES[:len(tested)])
    success = history[-1]['verdict'] == 'above'
    if success:
        assert records[-1]['selected']
        assert all(item['verdict'] == 'below' for item in history[:-1])
    else:
        assert tested == list(CANDIDATES)
    return {
        'schema': 'astra-agent3-bounded-prime-extension-v1',
        'scope': 'Complete scalar seeds only; no canonical HP degree scan.',
        'status': ('SUCCESS_READY_FOR_INDEPENDENT_AUDIT' if success
                   else 'BOUNDED_LIST_EXHAUSTED_WITHOUT_RATE_CERTIFICATE'),
        'candidate_primes': list(CANDIDATES),
        'tested_primes': tested,
        'untested_primes': list(CANDIDATES[len(tested):]),
        'reviewed_existing_uniform_primes': list(BASE_PRIMES),
        'selected_new_uniform_primes': selected,
        'all_uniform_primes': list(BASE_PRIMES) + selected,
        'coordinate_order': list(COORDINATES),
        'row_order': 'Each row index is r, from 0 through p-1 inclusive.',
        'tested_prime_certificates': records,
        'exact_rational_scalar_seeds': [
            {'r': r, 'values_in_coordinate_order': exact_seeds[r]}
            for r in sorted(exact_seeds)],
        'rate_history': history,
        'final_rate_certificate': history[-1],
        'factorial_comparison_valid_for_n_at_least': max(BASE_PRIMES + tuple(selected)),
        'eventual_domain_condition': 'Delta_n != 0, supplied eventually by the reviewed analytic endpoint theorem.',
        'residue_one_dependency': 'All-depth lift for every p>=5; Sections 1-2 only.',
        'review_scope': 'Existing 5/13 seeds and general transfer/lift are cited, not rerun. New primes require independent audit.',
        'all_check_assertions_pass': True,
        'predeclaration_sha256': sha256((OUT / 'PREDECLARATION.md').read_bytes()).hexdigest(),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_sha256': {path: sha256(Path(path).read_bytes()).hexdigest()
                          for path in DEPENDENCIES},
    }


def encoded_json(value):
    return json.dumps(value, indent=2, ensure_ascii=True) + '\n'


def main():
    assert sys.argv[1:] in ([], ['--verify']), 'Use no arguments or --verify.'
    certificate = build_certificate()
    certificate_text = encoded_json(certificate)
    summary = {
        'status': certificate['status'],
        'candidate_count': len(CANDIDATES),
        'tested_primes': certificate['tested_primes'],
        'zero_sets': {str(item['p']): item['Ccal_zero_set']
                      for item in certificate['tested_prime_certificates']},
        'selected_new_uniform_primes': certificate['selected_new_uniform_primes'],
        'all_uniform_primes': certificate['all_uniform_primes'],
        'untested_primes': certificate['untested_primes'],
        'selected_dual_construction_rows': sum(
            item['p'] for item in certificate['tested_prime_certificates'] if item['selected']),
        'selected_dual_construction_coordinate_checks': 5 * sum(
            item['p'] for item in certificate['tested_prime_certificates'] if item['selected']),
        'distinct_exact_rational_seeds': len(certificate['exact_rational_scalar_seeds']),
        'final_rate_certificate': certificate['final_rate_certificate'],
        'all_check_assertions_pass': True,
        'exact_certificate_bytes': len(certificate_text.encode('utf-8')),
        'exact_certificate_sha256': sha256(certificate_text.encode('utf-8')).hexdigest(),
    }
    summary_text = encoded_json(summary)
    certificate_path = OUT / 'exact_certificate.json'
    summary_path = OUT / 'certificate_summary.json'
    if sys.argv[1:] == ['--verify']:
        assert certificate_path.read_text(encoding='utf-8') == certificate_text
        assert summary_path.read_text(encoding='utf-8') == summary_text
        print('Stored certificate and summary reproduce exactly.')
    else:
        certificate_path.write_text(certificate_text, encoding='utf-8')
        summary_path.write_text(summary_text, encoding='utf-8')
    print(summary_text)


if __name__ == '__main__':
    main()
