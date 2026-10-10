#!/usr/bin/env python3
"""New precision dividend from certified depth-nine 20-bit physical columns.

Reuses the inspected finite transport implementation; does not regenerate
any operator, force, endpoint or old precision target.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import time

ROOT = Path(__file__).resolve().parent

def main():
    started = time.monotonic()
    producer = ROOT / 'original_binary_gram_transport_coordinator.py'
    spec = importlib.util.spec_from_file_location('accepted_transport', producer)
    tr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tr)
    source = ROOT / 'binary_short_moment_certificate.json'
    old = ROOT / 'binary_quadratic_precision37_certificate.json'
    data, previous = json.loads(source.read_text()), json.loads(old.read_text())
    content_path = ROOT / 'binary_kernel_content_certificate.json'
    content = json.loads(content_path.read_text())
    assert content['sharp_kernel_content'] == 8 and content['parity_lift_content_minima'] == [11, 10]
    n, b = int(data['n']), int(data['b'])
    assert previous['status'] == 'PASS' and previous['physical_column_bits'] == 20
    payloads = tr.actual_payloads(data, 45)
    values, trace = tr.contraction(n + 2, b, 2 * n - 1, payloads, [162, 158], 45, True)
    sf, sm = values[0] % (1 << 44), values[1]
    assert sf % (1 << 14) == 0 and sm % (1 << 16) == 0
    df, vf = tr.odd_product(2 * n, 81, 30)
    de, ve = tr.odd_product(2 * n, 77, 30)
    assert (vf, ve) == (80, 77)
    norm = (sf >> 14) * pow(df * df % (1 << 30), -1, 1 << 30) % (1 << 30)
    mixed = (sm >> 16) * pow(df * de % (1 << 29), -1, 1 << 29) % (1 << 29)
    assert norm % (1 << 22) == previous['D_raw_mod2_22']
    assert mixed % (1 << 21) == previous['E_raw_mod2_21']
    artifact = {
        'status': 'PASS', 'scope': 'NEW finite physical precision dividend justified by original-word depth-nine content; no higher physical producer',
        'n': str(n), 'b': str(b), 'physical_column_bits': 20,
        'certified_column_content_lower_bounds': [9, 9],
        'stability_norm_bits': min(20 + 9 + 1, 40),
        'stability_mixed_bits': min(20 + 9, 20 + 9, 40),
        'shared_transport_bits': 45, 'kernel_bits': [44, 45],
        'Sff_mod2_44': sf, 'Sfe_mod2_45': sm,
        'D_raw_mod2_30': norm, 'E_raw_mod2_29': mixed,
        'valuation_D_raw': {'value_or_lower_bound': tr.val2(norm, 30), 'exact': bool(norm)},
        'valuation_E_raw': {'value_or_lower_bound': tr.val2(mixed, 29), 'exact': bool(mixed)},
        'transport': trace, 'old_22_21_bit_reduction_passed': True,
        'complete_exterior_retained': True, 'finite_range_inclusive': '0<=j<=b',
        'all_prime_gcd_evaluated': False, 'irrationality_proved': False,
        'dependencies': [{'name': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (producer, source, old, content_path)]
    }
    target = ROOT / 'binary_quadratic_precision45_certificate.json'
    target.write_text(json.dumps(artifact, indent=2) + '\n')
    receipt = {k: v for k, v in artifact.items() if k != 'transport'}
    receipt['transport'] = {k: v for k, v in trace.items() if k != 'trace'}
    receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    receipt['elapsed_seconds'] = round(time.monotonic() - started, 3)
    (ROOT / 'binary_quadratic_precision45_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
