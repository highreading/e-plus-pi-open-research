"""Independent main integer interval reuse for both actual odd amplitudes."""
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
f = proof.load_all_dyadic_witnesses()


def exact_interval(row):
    lower, upper = Fraction(row['lower']), Fraction(row['upper'])
    assert (lower * SCALE).denominator == (upper * SCALE).denominator == 1
    return I(int(lower * SCALE), int(upper * SCALE))


def exact_complex(row):
    return C(exact_interval(row['real']), exact_interval(row['imag']))


def divide(a, b):
    denominator = b.real * b.real + b.imag * b.imag
    assert denominator.lo > 0
    return C((a.real * b.real + a.imag * b.imag) / denominator,
             (a.imag * b.real - a.real * b.imag) / denominator)


d2 = [[exact_complex(row) for row in col] for col in control['D2']]
d3 = [[exact_complex(row) for row in col] for col in control['D3']]
assert [row[:2] for row in control['D3'][:2]] == control['D2']
c = [d3[0][2], d3[1][2]]
# Independently computed full boundary entries fit the original coarse boxes.
box_pairs = [(743784742762, 743784742765), (76149347069, 76149347087),
             (493103175444, 493103175447), (889138775516, 889138775534),
             (-512209298805, -512209298703), (1006345884897, 1006345884999)]
for value, (lower, upper) in zip([d2[0][0], d2[0][1], d2[1][0], d2[1][1], *c], box_pairs):
    assert Fraction(lower, 10 ** 12) < Fraction(value.real.lo, SCALE)
    assert Fraction(value.real.hi, SCALE) < Fraction(upper, 10 ** 12)
    assert value.imag.abs_upper().hi * 10 ** 10 < SCALE
det = d2[0][0] * d2[1][1] - d2[0][1] * d2[1][0]
assert Fraction(det.real.lo, SCALE) > Fraction(62, 100)
eta = [divide(d2[1][1] * c[0] - d2[0][1] * c[1], det),
       divide(-d2[1][0] * c[0] + d2[0][0] * c[1], det)]
g = d3[2][2] - d3[2][0] * eta[0] - d3[2][1] * eta[1]
assert Fraction(g.real.lo, SCALE) > Fraction('-2.170279018834')
assert Fraction(g.real.hi, SCALE) < Fraction('-2.170279018372')
assert g.real.hi < 0

errors = []
for row in control['full_half_line_solution_error_bounds']:
    assert row['lower'] == row['upper']
    value = Fraction(row['upper'])
    errors.append(I.rational(value.numerator, value.denominator))
assert all(Fraction(error.hi, SCALE) < bound for error, bound in zip(
    errors, [Fraction(4, 10 ** 13), Fraction(3, 10 ** 12), Fraction(2, 10 ** 11)]))
sqrt5 = I.integer(5).sqrt()
phi, rho = (1 + sqrt5) / 2, (sqrt5 - 1) / 2
base = 2 / (I.integer(15).sqrt() * (1 - 1 / sqrt5))
assert base.lo > 0
phase = [C(1), C(0, 1), C(-1), C(0, -1)]
results = {}
for label, exterior in [('interior', False), ('exterior', True)]:
    ell, magnitude = [], I.rational(2, 5).sqrt()
    ratio = I.rational(3, 5).sqrt()
    for r in range(proof.L):
        value = phase[r % 4] * magnitude
        ell.append(value.conjugate() if exterior else value)
        magnitude = magnitude * ratio
    component = -phi if exterior else rho
    assert 1 + Fraction(component.abs_upper().hi, SCALE) ** 2 < 4
    pairings = []
    for column in range(3):
        value = sum((ell[r].conjugate() * (f[column][2 * r] +
                    f[column][2 * r + 1] * component) for r in range(proof.L)), C())
        pairings.append(value.widen(2 * errors[column]))
    numerator = pairings[2] - pairings[0] * eta[0] - pairings[1] * eta[1]
    # Reality is a separately checked theorem of the actual finite ratios.
    # The exterior reference is in channel TWO and contributes z=-phi.
    denominator = g.real * base * (-phi if exterior else I.integer(1))
    assert denominator.lo > 0 if exterior else denominator.hi < 0
    amplitude = numerator / denominator
    lower, upper = (Fraction(-1193, 1000), Fraction(-1192, 1000)) if exterior else (
        Fraction(282, 1000), Fraction(283, 1000))
    assert Fraction(amplitude.real.lo, SCALE) > lower
    assert Fraction(amplitude.real.hi, SCALE) < upper
    assert amplitude.imag.abs_upper().hi * 10 ** 7 < SCALE
    printed_lower, printed_upper = (
        Fraction('-1.192623911385'), Fraction('-1.192623910411')) if exterior else (
        Fraction('0.282159231929'), Fraction('0.282159232248'))
    assert Fraction(amplitude.real.lo, SCALE) > printed_lower
    assert Fraction(amplitude.real.hi, SCALE) < printed_upper
    results[label] = {'full_test_norm_upper_bound': '2',
                     'saddle_test_pairings': [value.exact_json() for value in pairings],
                     'numerator': numerator.exact_json(), 'denominator': denominator.exact_json(),
                     'amplitude': amplitude.exact_json(),
                     'accepted_rational_bounds': [str(lower), str(upper)],
                     'original_printed_decimal_enclosures_reverified': [str(printed_lower), str(printed_upper)],
                     'phase': '(-1)^m Rtilde_(2m+1)(-rho)' if exterior else 'R_(2m+1)(rho)'}
result = {'reviewer': 'main Codex', 'all_controls_passed': True,
          'all_arithmetic_integer_outward_intervals': True,
          'original_program_or_library_executed': False, 'new_linear_solves': 0,
          'new_quadrature': 0, 'new_canonical_degrees': 0,
          'witness_source_SHA256': proof.WITNESS_SHA,
          'main_fixed_operator_control_SHA256': hashlib.sha256(control_path.read_bytes()).hexdigest(),
          'own_verifier_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'original_coarse_D2_and_c_boxes_contain_independent_main_enclosures': True,
          'full_solved_vector_error_bounds': [value.exact_json() for value in errors],
          'woodbury_coefficients': [value.exact_json() for value in eta],
          'g_odd': g.exact_json(), 'base_pair': base.exact_json(), 'amplitudes': results,
          'reality_requires_separately_reviewed_actual_polynomial_limit': True,
          'full_contour_error_or_gcd_estimate_proved_here': False,
          'whole_archive_audit_complete': False, 'e_plus_pi_proof': False}
target = BASE / 'RAW_ODD_SADDLE_AMPLITUDES_MAIN_CONTROL.json'
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_controls_passed': True, 'exact_endpoints_saved': str(target)}))
