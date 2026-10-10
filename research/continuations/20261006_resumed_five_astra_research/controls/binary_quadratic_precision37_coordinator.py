#!/usr/bin/env python3
"""New precision dividend from certified even 20-bit physical columns.

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
    old = ROOT / 'original_binary_gram_transport_certificate.json'
    data, previous = json.loads(source.read_text()), json.loads(old.read_text())
    n, b = int(data['n']), int(data['b'])
    assert previous['status'] == 'PASS' and previous['physical_bits'] == 20
    payloads = tr.actual_payloads(data, 37)
    values, trace = tr.contraction(n + 2, b, 2 * n - 1, payloads, [162, 158], 37, True)
    sf, sm = values[0] % (1 << 36), values[1]
    assert sf % (1 << 14) == 0 and sm % (1 << 16) == 0
    df, vf = tr.odd_product(2 * n, 81, 22)
    de, ve = tr.odd_product(2 * n, 77, 22)
    assert (vf, ve) == (80, 77)
    norm = (sf >> 14) * pow(df * df % (1 << 22), -1, 1 << 22) % (1 << 22)
    mixed = (sm >> 16) * pow(df * de % (1 << 21), -1, 1 << 21) % (1 << 21)
    assert norm % (1 << 20) == previous['D_raw_mod2_20']
    assert mixed % (1 << 20) == previous['E_raw_mod2_20']
    artifact = {
        'status': 'PASS', 'scope': 'NEW finite physical precision dividend justified by evenness; no higher physical producer',
        'n': str(n), 'b': str(b), 'physical_column_bits': 20,
        'certified_column_content_lower_bounds': [1, 1],
        'stability_norm_bits': min(20 + 1 + 1, 40),
        'stability_mixed_bits': min(20 + 1, 20 + 1, 40),
        'shared_transport_bits': 37, 'kernel_bits': [36, 37],
        'Sff_mod2_36': sf, 'Sfe_mod2_37': sm,
        'D_raw_mod2_22': norm, 'E_raw_mod2_21': mixed,
        'valuation_D_raw': {'value_or_lower_bound': tr.val2(norm, 22), 'exact': bool(norm)},
        'valuation_E_raw': {'value_or_lower_bound': tr.val2(mixed, 21), 'exact': bool(mixed)},
        'transport': trace, 'old_20_bit_reduction_passed': True,
        'complete_exterior_retained': True, 'finite_range_inclusive': '0<=j<=b',
        'all_prime_gcd_evaluated': False, 'irrationality_proved': False,
        'dependencies': [{'name': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (producer, source, old)]
    }
    target = ROOT / 'binary_quadratic_precision37_certificate.json'
    target.write_text(json.dumps(artifact, indent=2) + '\n')
    receipt = {k: v for k, v in artifact.items() if k != 'transport'}
    receipt['transport'] = {k: v for k, v in trace.items() if k != 'trace'}
    receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    receipt['elapsed_seconds'] = round(time.monotonic() - started, 3)
    (ROOT / 'binary_quadratic_precision37_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
