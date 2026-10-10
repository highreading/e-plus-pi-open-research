"""Coordinator-authored finite residue-cycle lower bound, free exit carries."""
from pathlib import Path
import hashlib, json, time

OUT = Path(__file__).resolve().parent

def prefix_cost(d, g, h, width):
    state = {(0, 0, 0): 0}
    for bit in range(width):
        nxt = {}
        dk, gk, hk = (d >> bit)&1, (g >> bit)&1, (h >> bit)&1
        for (alpha, beta, gamma), cost in state.items():
            for sigma in (0, 1):
                if bit == 0 and sigma:
                    continue
                for rho in (0, 1):
                    ds = sigma+rho+alpha
                    if ds % 2 != dk:
                        continue
                    for tau in (0, 1):
                        gs = sigma+tau+beta
                        if gs % 2 != gk:
                            continue
                        key = (ds//2, gs//2, (hk+rho+gamma)//2)
                        value = cost+key[1]+key[2]
                        nxt[key] = min(nxt.get(key, value), value)
        state = nxt
    assert state
    return min(state.values())

def main():
    started = time.monotonic()
    records = []
    # This bounds a prefix cost; no original huge integer is constructed.
    for width in (6, 7, 8, 10, 12, 14, 16, 18):
        modulus = 1 << (width+2)
        multiplier = pow(9, 32, modulus)
        residue = pow(9, 18, modulus)
        period = 1 << max(0, width-6)
        assert pow(multiplier, period, modulus) == 1
        if period > 1:
            assert pow(multiplier, period//2, modulus) != 1
        counts, low_examples = {}, []
        for u in range(period):
            d = (residue-1)//4
            h = 2001*residue
            g = (h+1)//2
            minimum = prefix_cost(d, g, h, width)
            counts[minimum] = counts.get(minimum, 0)+1
            if minimum < 2 and len(low_examples) < 8:
                low_examples.append({'u_residue': u, 'b_residue': residue,
                                     'prefix_lower_bound': minimum})
            residue = residue*multiplier % modulus
        assert residue == pow(9, 18, modulus)
        records.append({'processed_low_bits': width, 'b_modulus': modulus,
                        'u_period': period, 'minimum_cost_histogram': counts,
                        'free_exit_minimum': min(counts),
                        'low_cost_examples': low_examples})
    result = {'authorship': 'Coordinator',
              'scope': 'Complete finite residue cycles and unrestricted exit-carry prefix minima. A uniform original-family lower bound requires the mathematical period and Kummer transfer proved separately.',
              'records': records, 'seconds': round(time.monotonic()-started, 4),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/'binary_original_low_prefix_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'records': [{k: v for k, v in r.items() if k != 'low_cost_examples'}
                                for r in records], 'seconds': result['seconds']}))

if __name__ == '__main__':
    main()
