"""Exact bounded consistency checks for the ordinary j=1 Roth extension.

Does not replace Item243's full rational degree/Newton proof reconstruction.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from item237_j1_algebraic_residual_certificate import lagrange_coefficient

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads((ROOT / 'manifests/item243_order6_gauge_closure_manifest.json').read_text())
pins = {path: sha(ROOT / path) == info['sha256']
        for path, info in manifest['files'].items()}
pins.update({path: sha(ROOT / path) == digest
             for path, digest in manifest['dependencies'].items()})
assert all(pins.values())
canonical = ROOT / 'results/item243_order6_gauge_closure_certificate.json'
replay = OUT / 'item243_closure_current_replay.json'
assert json.loads(canonical.read_bytes()) == json.loads(replay.read_bytes())
assert canonical.read_bytes().replace(b'\r\n', b'\n') == replay.read_bytes()

def peval(coeffs, h):
    result = F(0)
    for value in reversed(coeffs):
        result = result * h + F(value)
    return result

desing = json.loads((OUT / 'fixed_prime_desingularization_check.json').read_text())
old = json.loads((ROOT / 'results/item237_j1_algebraic_residual_certificate.json').read_text())
old_factors = old['all_h_recurrence']['factored_coefficients']

def old_value(entry, h):
    value = F(entry['scalar']) * peval(entry['remaining_core_low_to_high'], h)
    for a, b in entry['linear_factor_roots_numerator_denominator']:
        value *= b * h - a
    return value

def new_value(entry, h):
    return peval(entry['numerator_low_to_high'], h) / peval(entry['denominator_low_to_high'], h)

rows = []
for e in [1, 2]:
    values = [lagrange_coefficient(2 * (e + 3 * n)) for n in range(5)]
    old_residue = sum(old_value(old_factors[j], e) * values[j] for j in range(4))
    new_residue = sum(new_value(desing['reverse_order4_coefficients'][j], e) * values[j]
                      for j in range(5))
    assert old_residue == new_residue == 0
    assert values[0] != 0
    rows.append({'e': e, 'initial_c': str(values[0]),
                 'old_recurrence_residue': str(old_residue),
                 'reverse_recurrence_residue': str(new_residue)})

# Verify the affine coefficient identities symbolically using linear triples
# (coefficient of p, coefficient of n, constant), separately for e=1,2.
affine = []
for e in [1, 2]:
    h = (F(0), F(3), F(e))
    s = (F(1, 6), F(-2), F(-4 * e - 3, 6))
    p_reconstructed = tuple(4 * h[i] + 6 * s[i] + (3 if i == 2 else 0)
                            for i in range(3))
    m_reconstructed = tuple(3 * h[i] + 4 * s[i] + (2 if i == 2 else 0)
                            for i in range(3))
    assert p_reconstructed == (1, 0, 0)
    assert m_reconstructed == (F(2, 3), 1, F(e, 3))
    affine.append({'e': e, 'p_coefficients': list(map(str, p_reconstructed)),
                   'M_coefficients': list(map(str, m_reconstructed))})

result = {'scope': 'bounded exact consistency checks; no prime scan',
          'item243_manifest_pins_checked': len(pins),
          'all_pins_match': all(pins.values()),
          'item243_assembler_replay_JSON_identical': True,
          'item243_assembler_replay_identical_after_CRLF_normalization': True,
          'item243_replay_sha256': sha(replay),
          'initial_checks': rows, 'affine_identities': affine}
(OUT / 'roth_j1_extension_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
