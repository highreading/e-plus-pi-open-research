from pathlib import Path
from math import comb
import hashlib
import json
import datetime

HERE = Path(__file__).resolve().parent
R = HERE.parent
receipt_path = HERE / 'prefix_mod27_constants_certificate.json'
receipt = json.loads(receipt_path.read_text())
assert receipt['status'] == 'PASS' and len(receipt['rows']) == 122
report_path = R / 'responses/A1_turn9.md'
report_sha = hashlib.sha256(report_path.read_bytes()).hexdigest()
assert receipt['source_sha256'][str(report_path)] == report_sha
residues = {row['j']: row['D_j_mod27'] for row in receipt['rows']}
unit_indices = [j for j in residues if residues[j] % 3]
assert unit_indices == [27, 54, 108]
assert [residues[j] for j in unit_indices] == [5, 1, 23]


def direct_coefficient(n):
    return 0 if n < 0 else comb(24 + n, n) % 3


def frobenius_coefficient(n):
    return int(n >= 0 and n % 27 in (0, 1, 2))


checked_indices = set()
coefficients = []
for r in range(122):
    direct = 0
    frobenius = 0
    for j in range(1, 14):
        n = r + 9 * j - 122
        if n >= 0:
            checked_indices.add(n)
        direct += residues[9 * j] * direct_coefficient(n)
        frobenius += residues[9 * j] * frobenius_coefficient(n)
        assert direct_coefficient(n) == frobenius_coefficient(n)
    assert direct % 3 == frobenius % 3
    coefficients.append(direct % 3)
assert max(checked_indices) == 116
nonzero = {r: c for r, c in enumerate(coefficients) if c}
assert nonzero == {r: 2 for r in (14, 15, 16, 41, 42, 43, 95, 96, 97)}

# Independent multiplication of 2Y^14(1-Y)^2(1+Y^27+Y^81).
product_coefficients = [0] * 122
for offset in (0, 27, 81):
    for small, coefficient in enumerate((1, -2, 1)):
        product_coefficients[14 + offset + small] += 2 * coefficient
product_coefficients = [c % 3 for c in product_coefficients]
assert product_coefficients == coefficients
endpoint = sum(c * (-1) ** r for r, c in enumerate(coefficients)) % 3
assert endpoint == 1

gate_path = HERE / 'PREFIX_INVERSE_IMAGE_EVALUATION_GATE.md'
note_path = HERE / 'COORDINATOR_EVALUATED_PREFIX_INVERSE_IMAGES.md'
sources = {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
           for p in (report_path, receipt_path, gate_path, note_path)}
out = {
    'status': 'PASS',
    'time': datetime.datetime.now().astimezone().isoformat(),
    'scope': 'NEW finite coefficients GIVEN the source-specific A1turn9 formula; not a full prefix proof or physical7 computation.',
    'source_sha256': sources,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'reused_complete_prefix_constants': [
        {'j': row['j'], 'D_j_mod27': row['D_j_mod27'],
         'v3_combined_constant': row['v3_combined_constant']}
        for row in receipt['rows']],
    'source_formula_still_requires_independent_external_audit': True,
    'finite_range': [0, 121],
    'maximum_binomial_coefficient_index': max(checked_indices),
    'unit_constant_indices': unit_indices,
    'C_r_mod3': coefficients,
    'nonzero_coefficients': nonzero,
    'exact_polynomial_over_F3': '2Y^14(1-Y)^2(1+Y^27+Y^81)',
    'C_minus_one_mod3': endpoint,
    'nonexistent_blocks_excluded': [122, 123, 124],
    'actual_Delta_A_jet_evaluated': False,
    'global_proof': False,
}
(HERE / 'prefix_inverse_image_evaluation_certificate.json').write_text(
    json.dumps(out, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'finite_coefficients': len(coefficients),
                  'nonzero_blocks': len(nonzero),
                  'maximum_binomial_index': max(checked_indices),
                  'C_minus_one_mod3': endpoint, 'global_proof': False}))
