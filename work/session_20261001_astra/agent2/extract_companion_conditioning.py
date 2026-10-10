"""Extract exact conditioning from saved primitive minors only.
Run from the workspace root. No canonical systems or new indices are computed.
"""
import hashlib
import json
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

BASE = Path('work/session_20261001_astra/agent2')
SOURCE = BASE / 'two_scalar_quotient_evidence.json'
SCRIPT = BASE / 'extract_companion_conditioning.py'
OUTPUT = BASE / 'companion_conditioning_extraction.json'
WITNESS = BASE / 'conditioning_monotonicity_witness.json'
EXPECTED = [4, 6, 8, 10]


def exact(value):
    return str(Fraction(value))


def rational_or_none(numerator, denominator):
    return exact(Fraction(numerator, denominator)) if denominator else None


source_bytes = SOURCE.read_bytes()
source = json.loads(source_bytes)
assert [record['n'] for record in source['records']] == EXPECTED
records = []
first_monotonicity_failure = None

for old in source['records']:
    n, b = old['n'], old['b']
    assert b == n // 2
    size = b + 1
    N = [[0 for _ in range(size)] for _ in range(size)]
    expected_keys = {str(i) + ',' + str(j)
                     for i in range(size) for j in range(i + 1, size)}
    assert set(old['primitive_high_minors']) == expected_keys
    for key, value in old['primitive_high_minors'].items():
        i, j = map(int, key.split(','))
        entry = Fraction(value)
        assert entry.denominator == 1
        N[i][j] = entry.numerator
        N[j][i] = -entry.numerator
    assert reduce(gcd, (abs(N[i][j]) for i in range(size)
                        for j in range(i + 1, size)), 0) == 1

    kappas = [sum(N[i][j] for i in range(size)) for j in range(size)]
    rows = []
    eligible = []
    for j, row in enumerate(N):
        positive_mass = sum(max(value, 0) for value in row)
        negative_mass = sum(max(-value, 0) for value in row)
        signed_sum = sum(row)
        absolute_sum = positive_mass + negative_mass
        cancelled_mass = 2 * min(positive_mass, negative_mass)
        assert signed_sum == -kappas[j]
        assert absolute_sum - abs(signed_sum) == cancelled_mass
        is_eligible = kappas[j] != 0
        ratio = Fraction(absolute_sum, abs(kappas[j])) if is_eligible else None
        if is_eligible:
            eligible.append((ratio, j))
        rows.append({
            'j': j,
            'kappa_j': str(kappas[j]),
            'row_signed_sum': str(signed_sum),
            'row_absolute_sum': str(absolute_sum),
            'positive_mass': str(positive_mass),
            'negative_mass': str(negative_mass),
            'cancelled_mass': str(cancelled_mass),
            'eligible': is_eligible,
            'eligible_denominator_abs_kappa': str(abs(kappas[j])) if is_eligible else None,
            'eligible_ratio': str(ratio) if is_eligible else None,
            'surviving_fraction': rational_or_none(abs(signed_sum), absolute_sum),
            'cancelled_fraction': rational_or_none(cancelled_mass, absolute_sum),
            'cancelled_mass_over_net': rational_or_none(cancelled_mass, abs(signed_sum)),
            'minority_over_majority': rational_or_none(
                min(positive_mass, negative_mass), max(positive_mass, negative_mass))
        })
        # Stop this proposed monotonicity subroute at its first exact failure.
        if first_monotonicity_failure is None:
            columns = [k for k in range(size) if k != j]
            for left, right in zip(columns, columns[1:]):
                if abs(row[right]) > abs(row[left]):
                    first_monotonicity_failure = {
                        'status': 'REJECTED_AT_FIRST_RETAINED_WITNESS',
                        'candidate': 'Every row has nonincreasing absolute entries in increasing column order, omitting its diagonal.',
                        'n': n, 'b': b, 'row': j,
                        'left_column': left, 'right_column': right,
                        'left_entry': str(row[left]),
                        'right_entry': str(row[right]),
                        'absolute_increase': str(abs(row[right]) - abs(row[left])),
                        'consequence': 'This monotonicity shortcut is stopped. No further indices are searched.'
                    }
                    break

    assert eligible
    C = min(ratio for ratio, j in eligible)
    minimizing_rows = [j for ratio, j in eligible if ratio == C]

    # A concrete candidate inequality for the actual row with index one.
    pivot = abs(N[1][0])
    remaining_mass = sum(abs(N[1][k]) for k in range(2, size))
    margin = pivot - remaining_mass
    row_one_dominance = {
        'pivot_column': 0,
        'pivot_absolute_value': str(pivot),
        'remaining_absolute_mass': str(remaining_mass),
        'dominance_margin': str(margin),
        'strict_dominance': margin > 0,
        'remaining_over_pivot': rational_or_none(remaining_mass, pivot),
        'triangle_condition_bound': rational_or_none(pivot + remaining_mass, margin) if margin > 0 else None,
        'scope': 'Exact retained-data test only; no all-index domination claim.'
    }
    if margin > 0:
        assert kappas[1] != 0
        assert Fraction(rows[1]['eligible_ratio']) <= Fraction(pivot + remaining_mass, margin)

    A0, A1 = Fraction(old['A0']), Fraction(old['A1'])
    Z0 = Fraction(old['primitive_contractions']['Z0'])
    Z1 = Fraction(old['primitive_contractions']['Z1'])
    d = Fraction(old['primitive_contractions']['d'])
    assert d == A1 * Z1 - A0 * Z0 and d != 0
    Delta = abs(d) / (A0 * abs(Z0) + A1 * abs(Z1))
    assert Delta == Fraction(old['projective_pole_separation'])

    record = {
        'n': n, 'b': b,
        'primitive_antisymmetric_matrix': [[str(value) for value in row] for row in N],
        'rows': rows,
        'eligible_rows': [j for ratio, j in eligible],
        'C_min': str(C),
        'minimizing_rows': minimizing_rows,
        'row_one_first_entry_dominance': row_one_dominance,
        'actual_reduced_p': str(old['p']),
        'actual_reduced_q': str(old['q']),
        'projective_separation_Delta': str(Delta),
        'preserved_companion_data': {
            'Z0': str(Z0), 'Z1': str(Z1), 'd': str(d),
            'K_tail': old['primitive_contractions']['K'],
            'rational_e_companion': old['rational_e_companion']
        }
    }
    records.append(record)
    print(json.dumps({
        'n': n, 'C_min': str(C), 'minimizing_rows': minimizing_rows,
        'kappa': [str(value) for value in kappas],
        'row_absolute_sums': [row['row_absolute_sum'] for row in rows],
        'eligible_ratios': [row['eligible_ratio'] for row in rows],
        'row_one_strict_dominance': margin > 0
    }))

assert SOURCE.read_bytes() == source_bytes
assert first_monotonicity_failure is not None
result = {
    'scope': 'Exact extraction from the existing n=4,6,8,10 records only. No system solve, degree extension, numerical approximation, or prime scan.',
    'source_path': str(SOURCE),
    'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'source_unchanged_during_execution': True,
    'script_sha256': hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
    'conventions': {
        'matrix': 'N_ij is the saved primitive minor for i<j; N_ji=-N_ij.',
        'kappa': 'kappa_j=sum_i N_ij=-sum_k N_jk.',
        'C': 'Minimum of row_absolute_sum/abs(kappa_j) over nonzero kappa_j.',
        'cancelled_mass': 'S_j-abs(kappa_j)=2*min(positive_mass,negative_mass).',
        'null_ratios': 'A null ratio has zero denominator and is not an eligible condition ratio.'
    },
    'records': records,
    'first_rejected_monotonicity_witness': first_monotonicity_failure,
    'all_four_row_one_dominance_tests_pass': all(
        record['row_one_first_entry_dominance']['strict_dominance'] for record in records),
    'limitation': 'Finite exact values do not establish an exponential conditioning bound, a sign theorem, or full-remainder nonvanishing on an unbounded set.'
}
OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
WITNESS.write_text(json.dumps(first_monotonicity_failure, indent=2) + '\n')
print('Exact extraction and the first failed-property witness were saved. The source certificate is unchanged.')
