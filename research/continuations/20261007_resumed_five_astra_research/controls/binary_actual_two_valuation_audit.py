"""Coordinator-authored bounded full-word optimization of both carry costs."""
from pathlib import Path
import hashlib, json, time

OUT = Path(__file__).resolve().parent

def cost_pair(d, g, h, retain_table=False):
    assert 0 <= d <= g and h >= 0
    width = max(d.bit_length(), g.bit_length(), h.bit_length()) + 2
    assert width < 5000
    state = {(0, 0, 0): (0, 0, 0, 0)}
    table = []
    for bit in range(width):
        dk, gk, hk = (d >> bit) & 1, (g >> bit) & 1, (h >> bit) & 1
        nxt = {}
        for (alpha, beta, gamma), (cost, s, r, t) in state.items():
            for sigma in (0, 1):
                if bit == 0 and sigma:
                    continue
                for rho in (0, 1):
                    ds = sigma + rho + alpha
                    if ds % 2 != dk:
                        continue
                    for tau in (0, 1):
                        gs = sigma + tau + beta
                        if gs % 2 != gk:
                            continue
                        hs = hk + rho + gamma
                        key = (ds // 2, gs // 2, hs // 2)
                        candidate = (cost + key[1] + key[2], s | (sigma << bit),
                                     r | (rho << bit), t | (tau << bit))
                        if key not in nxt or candidate < nxt[key]:
                            nxt[key] = candidate
        state = nxt
        if retain_table:
            table.append({'bit': bit, 'digits_d_g_h': [dk, gk, hk],
                          'costs': {''.join(map(str, k)): v[0]
                                    for k, v in sorted(state.items())}})
    assert (0, 0, 0) in state
    cost, s, r, t = state[(0, 0, 0)]
    c1 = s.bit_count() + t.bit_count() - g.bit_count()
    c2 = h.bit_count() + r.bit_count() - (h+r).bit_count()
    assert s+r == d and s+t == g and s % 2 == 0
    assert cost == c1+c2 and c1 >= 0 and c2 >= 0
    result = {'minimum': cost, 'first_valuation': c1, 'second_valuation': c2,
              's': str(s), 'R': str(r), 'T': str(t), 'physical_j': str(4*s),
              'bits_processed': width,
              'independent_digit_sum_check': c1+c2}
    if retain_table:
        result['complete_minimum_cost_table'] = table
    return result

def main():
    started = time.monotonic()
    checks = 0
    for d in range(21):
        for g in (d, d+1, 2*d+3, 3*d+7):
            for h in (0, 1, 3, 9, 33, 79):
                brute = min((s.bit_count() + (g-s).bit_count() - g.bit_count()
                             + h.bit_count() + (d-s).bit_count()
                             - (h+d-s).bit_count(), s)
                            for s in range(0, d+1, 2))
                got = cost_pair(d, g, h)
                assert (got['minimum'], int(got['s'])) == brute
                checks += 1
    cases = []
    for u in range(21):
        b = 9**(18+32*u)
        h, d = 2001*b, (b-1)//4
        g = (h+1)//2
        assert (b % 256, h % 128, g % 64, d % 64) == (209, 33, 17, 52)
        cases.append({'u': u, 'b_bits': b.bit_length(),
                      'exact_two_channel_result': cost_pair(d, g, h, u == 0)})
    result = {'authorship': 'Coordinator; third-party code was not executed',
              'scope': '21 finite original words only. Exact a=1 classification depends on A5 turn6 theorem; a larger minimum does not give its exact higher content.',
              'auxiliary_brute_force_comparisons': checks,
              'cases': cases, 'seconds': round(time.monotonic()-started, 5),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path = OUT/'binary_actual_two_valuation_certificate.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    compact = {'scope': result['scope'], 'auxiliary_comparisons': checks,
               'minima': [x['exact_two_channel_result']['minimum'] for x in cases],
               'u0_witness': {k: v for k, v in cases[0]['exact_two_channel_result'].items()
                              if k != 'complete_minimum_cost_table'},
               'full_certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
               'seconds': result['seconds']}
    (OUT/'binary_actual_two_valuation_receipt.json').write_text(json.dumps(compact, indent=2)+'\n')
    print(json.dumps(compact))

if __name__ == '__main__':
    main()
