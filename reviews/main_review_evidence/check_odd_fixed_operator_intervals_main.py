"""Independent main reconstruction of one odd half-line interval certificate.

Consumes all saved dyadic coordinates as data, never imports archived code.
Uses only the main-authored binary integer interval module and stdlib.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import time

BASE = Path(__file__).resolve().parent
ROOT = Path('work/session_20260913')
module_path = BASE / 'fixed_interval_main.py'
spec = importlib.util.spec_from_file_location('main_fixed_interval', module_path)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
I, C, SCALE = iv.I, iv.C, iv.SCALE

WITNESS_SHA = '196c620cad7043be1932aaae4fc07f8192351053a2e0f9a1ce50d01e75ecc83f'
L, J, M, TERMS = 64, 128, 512, 24
zero, one, ii = C(), C(1), C(0, 1)
R = I.rational(4, 3)
sqrt3 = I.integer(3).sqrt()
a, gamma = sqrt3 / 2, sqrt3 / 4


def load_all_dyadic_witnesses():
    source = ROOT / 'raw_odd_limit_certificate_vectors.json'
    b = source.read_bytes()
    assert hashlib.sha256(b).hexdigest() == WITNESS_SHA
    raw = json.loads(b)
    assert set(raw) == {'L', 'description', 'solutions'} and raw['L'] == L
    assert len(raw['solutions']) == 3
    data, tokens, dyadic_scalars = [], 0, 0
    for column in raw['solutions']:
        assert len(column) == 2 * L
        converted = []
        for value in column:
            assert len(value) == 2 and all(len(pair) == 2 for pair in value)
            for pair in value:
                n, d = pair
                assert type(n) is int and type(d) is int and d > 0
                assert d & (d - 1) == 0
                tokens += 2
                dyadic_scalars += 1
            converted.append(C(I.rational(*value[0]), I.rational(*value[1])))
        data.append(converted)
    assert tokens == 1536 and dyadic_scalars == 768
    return data


def complete_fourier_enclosures():
    pi = iv.pi_interval()
    assert pi.lo > 3 * SCALE and pi.hi < 4 * SCALE
    cosines = [iv.cosine_small(2 * pi * j / M) for j in range(M // 2 + 1)]
    cosines[0], cosines[-1] = I.integer(1), I.integer(-1)
    coefficients = [[[C() for _ in range(2)] for _ in range(2)] for _ in range(J + 1)]
    series_error = I.rational(2, math.factorial(2 * TERMS))
    for node in range(M // 2 + 1):
        y = sqrt3 * cosines[node]
        # t=(1+iy)/(1-iy) in real coordinates; the denominator is positive.
        denominator = 1 + y * y
        t = C((1 - y * y) / denominator, 2 * y / denominator)
        power, c, s = C(1), C(), C()
        for j in range(TERMS):
            c = c + power / math.factorial(2 * j)
            s = s + power / math.factorial(2 * j + 1)
            power = power * t
        c, s = c.widen(series_error), s.widen(series_error)
        block = [[c, t * s], [s, c]]
        weight = 1 if node in (0, M // 2) else 2
        for k in range(J + 1):
            index = (k * node) % M
            cosine = cosines[min(index, M - index)]
            scalar = weight * cosine / M
            for u in range(2):
                for v in range(2):
                    coefficients[k][u][v] = coefficients[k][u][v] + block[u][v] * scalar
        if node % 64 == 0:
            print(json.dumps({'main_outward_quadrature_nodes': node, 'last_node': M // 2}), flush=True)
    alias = 32 * R ** (-(M - J)) / (1 - R ** (-M))
    for k in range(J + 1):
        for u in range(2):
            for v in range(2):
                coefficients[k][u][v] = coefficients[k][u][v].widen(alias)
    return coefficients, alias, pi


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(((-1) ** j * matrix[0][j] * determinant(
        [[matrix[r][k] for k in range(len(matrix)) if k != j]
         for r in range(1, len(matrix))]) for j in range(len(matrix))), C())


def main():
    started = time.monotonic()
    vectors = load_all_dyadic_witnesses()
    coefficients, alias, pi = complete_fourier_enclosures()
    geometric = []
    magnitude = I.rational(2, 3).sqrt()
    phase = [C(1), C(0, 1), C(-1), C(0, -1)]
    for r in range(J + 1):
        geometric.append(phase[r % 4] * magnitude)
        magnitude = magnitude / sqrt3

    errors, prefixes, tails, top, bottom = [], [], [], [], []
    weights = [R ** (s - L + 1) for s in range(L)]
    tail_factor = 16 * R ** (-(J - L)) / (1 - R ** (-2)).sqrt()
    rhs_tail = I.rational(1, 3 ** (J // 2))
    for column, f in enumerate(vectors):
        ef = [[C(), C()] for _ in range(J + 1)]
        for r in range(J + 1):
            for s in range(L):
                block = coefficients[abs(r - s)]
                for u in range(2):
                    ef[r][u] = ef[r][u] + block[u][0] * f[2 * s] + block[u][1] * f[2 * s + 1]
        residual_prefix = I.integer(0)
        for r in range(J):
            low = ef[r - 1] if r else [C(), C()]
            high = ef[r + 1]
            value = [(ef[r][1] + ii * a * (low[1] + high[1])) / 2,
                     (ef[r][0] - ii * a * (low[0] + high[0])) / 2]
            if column < 2:
                rhs = [C(gamma if r == 0 and channel == column else 0) for channel in range(2)]
            else:
                rhs = [geometric[r], C()]
            for u in range(2):
                residual_prefix = residual_prefix + (rhs[u] - value[u]).abs_upper()
        weighted_f = sum((weights[s] * (f[2 * s].abs_upper() + f[2 * s + 1].abs_upper())
                          for s in range(L)), I.integer(0))
        tail = weighted_f * tail_factor + (rhs_tail if column == 2 else 0)
        error = (12 * (residual_prefix + tail)).upper()
        reported_bound = [Fraction(3508, 10 ** 16), Fraction(2827, 10 ** 15), Fraction(1682, 10 ** 14)][column]
        assert Fraction(error.hi, SCALE) < reported_bound
        errors.append(error)
        prefixes.append(residual_prefix)
        tails.append(tail)

        wf = [C(), C()]
        for s in range(L):
            block = coefficients[s + 1]
            for u in range(2):
                wf[u] = wf[u] + block[u][0] * f[2 * s] + block[u][1] * f[2 * s + 1]
        top.append([(ii * wf[1]).widen(3 * error), (-ii * wf[0]).widen(3 * error)])
        pairing = sum((geometric[s].conjugate() * f[2 * s] for s in range(L)), C())
        bottom.append(pairing.widen(error))
        print(json.dumps({'column': column, 'solution_error_upper_descriptive': float(Fraction(error.hi, SCALE)),
                          'exact_reported_rational_bound_passed': True}), flush=True)

    d2 = [[top[j][i] + (1 if i == j else 0) for j in range(2)] for i in range(2)]
    d3 = [d2[0] + [top[2][0]], d2[1] + [top[2][1]], bottom]
    det2, det3 = determinant(d2), determinant(d3)
    assert Fraction(det2.real.lo, SCALE) > Fraction(62, 100)
    assert Fraction(det2.real.hi, SCALE) < Fraction(63, 100)
    assert Fraction(det3.real.lo, SCALE) > Fraction(-136, 100)
    assert Fraction(det3.real.hi, SCALE) < Fraction(-135, 100)
    assert det2.imag.abs_upper().hi * 10 ** 6 < SCALE
    assert det3.imag.abs_upper().hi * 10 ** 6 < SCALE
    # Reality follows analytically from the phase gauge, not small imaginary widths.
    ratio = det2.real / det3.real
    assert Fraction(ratio.lo, SCALE) > Fraction(-47, 100)
    assert Fraction(ratio.hi, SCALE) < Fraction(-45, 100)
    result = {
        'reviewer': 'main Codex', 'fixed_operator_control_only': True,
        'original_program_or_library_executed': False, 'original_data_modified': False,
        'integer_outward_arithmetic_only': True, 'binary_endpoint_bits': iv.BITS,
        'all_saved_dyadic_integer_tokens_checked': 1536, 'witness_source_SHA256': WITNESS_SHA,
        'own_interval_module_SHA256': hashlib.sha256(module_path.read_bytes()).hexdigest(),
        'own_verifier_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'fixed_parameters': {'L': L, 'output_cutoff': J, 'quadrature_nodes': M, 'Taylor_terms': TERMS},
        'pi_enclosure': pi.exact_json(), 'alias_bound': alias.exact_json(),
        'full_half_line_solution_error_bounds': [x.exact_json() for x in errors],
        'residual_prefix_bounds': [x.exact_json() for x in prefixes],
        'omitted_half_line_residual_tail_bounds': [x.exact_json() for x in tails],
        'D2': [[z.exact_json() for z in row] for row in d2],
        'D3': [[z.exact_json() for z in row] for row in d3],
        'det_D2': det2.exact_json(), 'det_D3': det3.exact_json(), 'real_ratio': ratio.exact_json(),
        'accepted_rational_bounds': {'det_D2': ['62/100', '63/100'],
                                     'det_D3': ['-136/100', '-135/100'], 'ratio': ['-47/100', '-45/100']},
        'reality_requires_separately_checked_analytic_phase_gauge': True,
        'new_canonical_degrees_solved': 0, 'all_controls_passed': True,
        'e_plus_pi_proof': False, 'elapsed_seconds': time.monotonic() - started,
    }
    target = BASE / 'RAW_ODD_FIXED_OPERATOR_INTERVAL_MAIN_CONTROL.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_passed': True, 'exact_endpoints_saved': str(target),
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
