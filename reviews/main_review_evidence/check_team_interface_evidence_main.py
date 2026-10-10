"""Bounded main consistency checks of named assistants' finite evidence.

No assistant program or archived program is executed or imported. Infinite
manuscript claims are judged from the separately read mathematical reports.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, factorial
import datetime
import hashlib
import json

BASE = Path(__file__).resolve().parent
parts = [
    ('/root/proof_inventory', 'assistant1_inventory/math_spectral_gram_primitive_audit_20261004',
     'independent_exact_interface_examples.py'),
    ('/root/literature_map', 'assistant2_literature/arithmetic_mathematical_review_20261004',
     'independent_exact_control.py'),
    ('/root/organization_evidence', 'assistant3_organization/weighted_b1_b2_jet_interfaces_math_review_20261004',
     'check_interface_examples_owned.py'),
]
code_receipts = []
for author, relative, program in parts:
    p = BASE / relative / program
    raw = p.read_bytes()
    code_receipts.append({'author': author, 'path': relative + '/' + program,
                         'sha256': hashlib.sha256(raw).hexdigest(),
                         'main_read_in_full': True, 'executed_by_main': False,
                         'scope': 'Complete static reading of this assistant-owned standard-library program.'})

arith_path = BASE / parts[1][1] / 'INDEPENDENT_EXACT_CONTROLS.json'
arith = json.loads(arith_path.read_text())
assert arith['all_assertions_passed'] is True
assert arith['script_sha256'] == code_receipts[1]['sha256']
arith_controls = []
for r in arith['degrees']:
    Z, N, q, factor = map(int, (r['Z'], r['N'], r['q'], r['F']))
    assert sum(map(int, r['Qhat_coefficients_low_to_high'])) == Z
    assert sum(map(int, r['Pe_coefficients_low_to_high'])) + 4 * sum(map(int, r['Pa_coefficients_low_to_high'])) == N
    actual_gcd = gcd(abs(Z), abs(N))
    assert actual_gcd == int(r['endpoint_gcd']) and q == abs(Z) // actual_gcd
    n = r['n']
    assert int(r['E']) == (-1) ** n * factor * Z
    assert int(r['DeltaB']) == -int(r['E'])
    assert Fraction(int(r['DeltaA']), int(r['DeltaB'])) == -factorial(n) * Fraction(N, Z)
    arith_controls.append({'n': n, 'complete_selected_endpoint_arrays_and_gcd_consistent': True,
                           'local_scope': r['saturated_prime_control']})
assert [r['n'] for r in arith_controls] == [7, 25]

interface_path = BASE / parts[2][1] / 'OWN_EXACT_INTERFACE_EXAMPLES.json'
interface = json.loads(interface_path.read_text())
assert interface['owned_program_sha256'] == code_receipts[2]['sha256']
example = interface['n1_actual_HP_endpoint_counterexample']
kernel = list(map(Fraction, example['primitive_B'] + example['primitive_C']))
matrix = [[Fraction(x) for x in row] for row in example['high_matrix']]
assert all(sum(a * b for a, b in zip(row, kernel)) == 0 for row in matrix)
def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
assert determinant3([row[:3] for row in matrix]) != 0
assert example['endpoint_pair_A1_B1'] == [0, 0] and example['C1'] == 0
assert sum(example['primitive_A']) == sum(example['primitive_B']) == sum(example['primitive_C']) == 0
assert [Fraction(x) for x in example['ordinary_R_coefficients_0_through_4']] == [0, 0, 0, 0, Fraction(1, 12)]

spectral_path = BASE / parts[0][1] / 'independent_exact_raw_exclusion_rate_margin.json'
spectral = json.loads(spectral_path.read_text())
lower, upper = map(Fraction, spectral['L_minus_5_log_phi_interval'])
assert Fraction(3, 200) < lower < upper
assert spectral['actual_prime_transfers_or_saddle_inputs_recomputed'] is False

out = {'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'reviewer': 'main Codex', 'all_selected_consistency_controls_passed': True,
       'assistant_owned_code_reading_receipts': code_receipts,
       'arithmetic_selected_arrays': arith_controls,
       'actual_n1_rank3_zero_endpoint_example_consistent': True,
       'independent_spectral_rate_interval_exceeds_3_over_200': True,
       'source_JSON_SHA256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [arith_path, interface_path, spectral_path]},
       'every_generated_JSON_value_manually_read': False,
       'full_historical_archive_audited': False,
       'claims_not_made_by_manuscripts_are_not_labeled_errors': True,
       'scope': 'Main independently checked these finite endpoint/rank/margin interfaces. This does not reprove all assistant manuscript theorems or authenticate every determinant in their finite outputs.'}
(BASE / 'MAIN_TEAM_INTERFACE_EVIDENCE_CONSISTENCY.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'selected_endpoint_degrees': [r['n'] for r in arith_controls],
                  'actual_n1_rank_and_zero_endpoint': True, 'main_consistency_checks': 'passed'}))
