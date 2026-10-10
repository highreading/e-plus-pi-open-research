"""Main integer interval postprocessing of the independently checked witnesses."""
from pathlib import Path
from fractions import Fraction
import hashlib
import importlib.util
import json
import math

BASE = Path(__file__).resolve().parent
proof_path = BASE / 'check_odd_fixed_operator_intervals_main.py'
spec = importlib.util.spec_from_file_location('main_odd_fixed_operator', proof_path)
proof = importlib.util.module_from_spec(spec)
spec.loader.exec_module(proof)
I, C, SCALE = proof.I, proof.C, proof.SCALE
control_path = BASE / 'RAW_ODD_FIXED_OPERATOR_INTERVAL_MAIN_CONTROL.json'
control = json.loads(control_path.read_text())
assert control['all_controls_passed'] is True
assert control['own_verifier_SHA256'] == hashlib.sha256(proof_path.read_bytes()).hexdigest()
assert control['own_interval_module_SHA256'] == hashlib.sha256((BASE / 'fixed_interval_main.py').read_bytes()).hexdigest()
f = proof.load_all_dyadic_witnesses()
errors = []
for row in control['full_half_line_solution_error_bounds'][:2]:
    assert row['lower'] == row['upper']
    number = Fraction(row['upper'])
    errors.append(I.rational(number.numerator, number.denominator))
assert Fraction(errors[0].hi, SCALE) < Fraction(4, 10 ** 13)
assert Fraction(errors[1].hi, SCALE) < Fraction(3, 10 ** 12)


def complex_divide(a, b):
    denominator = b.real * b.real + b.imag * b.imag
    assert denominator.lo > 0
    return C((a.real * b.real + a.imag * b.imag) / denominator,
             (a.imag * b.real - a.real * b.imag) / denominator)


def exp_one_interval(terms=80):
    lower = sum((Fraction(1, math.factorial(j)) for j in range(terms)), Fraction(0))
    # Starting at 1/terms!, each later ratio is at most 1/(terms+1).
    upper = lower + Fraction(terms + 1, terms * math.factorial(terms))
    return I(I.rational(lower.numerator, lower.denominator).lo,
             I.rational(upper.numerator, upper.denominator).hi)


vv, ww = [], []
phase = [C(1), C(0, 1), C(-1), C(0, -1)]
magnitude = I.rational(2, 3).sqrt()
sqrt3 = I.integer(3).sqrt()
for r in range(proof.L):
    value = phase[r % 4] * magnitude
    vv.append(value)
    ww.append(value.conjugate())
    magnitude = magnitude / sqrt3
pv, pw = [], []
for column in range(2):
    pv.append(sum((vv[r].conjugate() * f[column][2 * r] for r in range(proof.L)), C()).widen(errors[column]))
    pw.append(sum((ww[r].conjugate() * f[column][2 * r + 1] for r in range(proof.L)), C()).widen(errors[column]))
assert pw[0].real.lo > SCALE // 2
g = (pv[1] - complex_divide(pv[0] * pw[1], pw[0])) * I.integer(2).sqrt()
assert Fraction(g.real.lo, SCALE) > Fraction(91149, 10 ** 5)
assert Fraction(g.real.hi, SCALE) < Fraction(91150, 10 ** 5)
assert g.imag.abs_upper().hi * 10 ** 8 < SCALE
# Actual g is real by the proved compression limit; use that fact explicitly.
inverse_g = 1 / g.real
e = exp_one_interval()
constant = (3 * e).sqrt() / (4 * g.real)
assert Fraction(constant.lo, SCALE) > Fraction(783, 1000)
assert Fraction(constant.hi, SCALE) < Fraction(784, 1000)
result = {
    'reviewer': 'main Codex', 'all_controls_passed': True,
    'all_enclosures_use_integer_outward_arithmetic': True,
    'original_program_or_library_executed': False, 'original_data_modified': False,
    'new_linear_solves': 0, 'new_canonical_degrees': 0,
    'witness_source_SHA256': proof.WITNESS_SHA,
    'main_fixed_operator_control_SHA256': hashlib.sha256(control_path.read_bytes()).hexdigest(),
    'own_verifier_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'v_pairings': [value.exact_json() for value in pv],
    'w_pairings': [value.exact_json() for value in pw],
    'g_even': g.exact_json(), 'real_inverse_g_even': inverse_g.exact_json(),
    'e_interval': e.exact_json(), 'real_exponential_error_constant': constant.exact_json(),
    'accepted_rational_bounds': {'g_even': ['91149/100000', '91150/100000'],
                                 'exponential_error_constant': ['783/1000', '784/1000']},
    'reality_requires_separately_main_checked_compression_limit': True,
    'whole_archive_audit_complete': False, 'e_plus_pi_proof': False,
}
target = BASE / 'RAW_EVEN_CORNER_FROM_WITNESSES_MAIN_CONTROL.json'
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_controls_passed': True, 'exact_endpoints_saved': str(target)}))
