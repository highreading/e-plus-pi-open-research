"""Main integer interval checks of the two actual even saddle amplitudes.

Reuses exact saved witnesses and the already reconstructed full residuals.
Imports only the main-authored interval checker, never archived code/libraries.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import importlib.util
import json

BASE = Path(__file__).resolve().parent
proof_path = BASE / 'check_odd_fixed_operator_intervals_main.py'
spec = importlib.util.spec_from_file_location('main_fixed_operator', proof_path)
proof = importlib.util.module_from_spec(spec)
spec.loader.exec_module(proof)
I, C, SCALE = proof.I, proof.C, proof.SCALE
control_path = BASE / 'RAW_ODD_FIXED_OPERATOR_INTERVAL_MAIN_CONTROL.json'
control = json.loads(control_path.read_text())
assert control['all_controls_passed'] is True
assert control['own_verifier_SHA256'] == hashlib.sha256(proof_path.read_bytes()).hexdigest()
assert control['own_interval_module_SHA256'] == hashlib.sha256((BASE / 'fixed_interval_main.py').read_bytes()).hexdigest()
corner_path = BASE / 'RAW_EVEN_CORNER_FROM_WITNESSES_MAIN_CONTROL.json'
corner = json.loads(corner_path.read_text())
assert corner['all_controls_passed'] is True
assert corner['main_fixed_operator_control_SHA256'] == hashlib.sha256(control_path.read_bytes()).hexdigest()
assert corner['own_verifier_SHA256'] == hashlib.sha256((BASE / 'check_even_corner_from_witnesses_main.py').read_bytes()).hexdigest()
f = proof.load_all_dyadic_witnesses()


def interval_from_exact_json(row):
    lower, upper = Fraction(row['lower']), Fraction(row['upper'])
    assert (lower * SCALE).denominator == (upper * SCALE).denominator == 1
    return I(int(lower * SCALE), int(upper * SCALE))


def complex_from_exact_json(row):
    return C(interval_from_exact_json(row['real']), interval_from_exact_json(row['imag']))


def divide(a, b):
    norm = b.real * b.real + b.imag * b.imag
    assert norm.lo > 0
    return C((a.real * b.real + a.imag * b.imag) / norm,
             (a.imag * b.real - a.real * b.imag) / norm)


errors = []
for row in control['full_half_line_solution_error_bounds'][:2]:
    assert row['lower'] == row['upper']
    number = Fraction(row['upper'])
    errors.append(I.rational(number.numerator, number.denominator))
pv = [complex_from_exact_json(row) for row in corner['v_pairings']]
pw = [complex_from_exact_json(row) for row in corner['w_pairings']]
assert pw[0].real.lo > SCALE // 2
alpha = divide(pw[1], pw[0])
sqrt2, sqrt5 = I.integer(2).sqrt(), I.integer(5).sqrt()
phi, rho = (1 + sqrt5) / 2, (sqrt5 - 1) / 2
g = (pv[1] - divide(pv[0] * pw[1], pw[0])) * sqrt2
assert g.exact_json() == corner['g_even']
assert g.real.lo > 0
base_pair = 2 / (I.integer(15).sqrt() * (1 - 1 / sqrt5))
assert base_pair.lo > 0
phase = [C(1), C(0, 1), C(-1), C(0, -1)]
results = {}
for label, exterior in [('exterior', True), ('interior', False)]:
    # Both infinite test vectors have norm one; the two-channel test norm is <2.
    ell, magnitude = [], I.rational(2, 5).sqrt()
    ratio = I.rational(3, 5).sqrt()
    for r in range(proof.L):
        value = phase[r % 4] * magnitude
        ell.append(value.conjugate() if exterior else value)
        magnitude = magnitude * ratio
    component = -phi if exterior else rho
    assert 1 + Fraction(component.abs_upper().hi, SCALE) ** 2 < 4
    pairings = []
    for column in range(2):
        value = sum((ell[r].conjugate() * (f[column][2 * r] +
                    f[column][2 * r + 1] * component) for r in range(proof.L)), C())
        pairings.append(value.widen(2 * errors[column]))
    numerator = (pairings[1] - pairings[0] * alpha) * sqrt2
    # g is exactly real by the independently reviewed actual compression limit.
    amplitude = numerator / (g.real * base_pair)
    lower, upper = (Fraction(49, 1000), Fraction(50, 1000)) if exterior else (
        Fraction(604, 1000), Fraction(605, 1000))
    assert Fraction(amplitude.real.lo, SCALE) > lower
    assert Fraction(amplitude.real.hi, SCALE) < upper
    assert amplitude.imag.abs_upper().hi * 10 ** 8 < SCALE
    printed_lower, printed_upper = (
        Fraction('0.0493603201444840'), Fraction('0.0493603201863010')) if exterior else (
        Fraction('0.6040688968602422'), Fraction('0.6040688969081851'))
    assert Fraction(amplitude.real.lo, SCALE) > printed_lower
    assert Fraction(amplitude.real.hi, SCALE) < printed_upper
    results[label] = {'complete_solved_vector_error_bounds': [row.exact_json() for row in errors],
                     'full_test_norm_upper_bound': '2',
                     'saddle_test_pairings': [row.exact_json() for row in pairings],
                     'numerator': numerator.exact_json(), 'amplitude': amplitude.exact_json(),
                     'accepted_rational_bounds': [str(lower), str(upper)],
                     'original_printed_decimal_enclosures_reverified': [str(printed_lower), str(printed_upper)],
                     'phase': '(-1)^m Rtilde_2m(-1/phi)' if exterior else 'R_2m(rho)'}
result = {'reviewer': 'main Codex', 'all_controls_passed': True,
          'all_arithmetic_integer_outward_intervals': True,
          'original_program_or_library_executed': False, 'new_linear_solves': 0,
          'new_canonical_degrees': 0, 'witness_source_SHA256': proof.WITNESS_SHA,
          'main_fixed_operator_control_SHA256': hashlib.sha256(control_path.read_bytes()).hexdigest(),
          'main_even_corner_control_SHA256': hashlib.sha256(corner_path.read_bytes()).hexdigest(),
          'own_verifier_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'projection_coefficient': alpha.exact_json(), 'g_even': g.exact_json(),
          'base_pair': base_pair.exact_json(), 'amplitudes': results,
          'reality_requires_separately_reviewed_actual_polynomial_limit': True,
          'full_contour_error_or_gcd_estimate_proved_here': False,
          'whole_archive_audit_complete': False, 'e_plus_pi_proof': False}
target = BASE / 'RAW_EVEN_SADDLE_AMPLITUDES_MAIN_CONTROL.json'
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_controls_passed': True, 'exact_endpoints_saved': str(target)}))
