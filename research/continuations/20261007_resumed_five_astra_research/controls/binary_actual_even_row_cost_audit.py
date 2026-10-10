"""Parent-authored finite whole-word cost calculation; no network or key access."""
from pathlib import Path
import hashlib, json, time

OUT = Path(__file__).resolve().parent

def minimum_even_row(d, g, h):
    assert 0 <= d <= g and h >= 0
    width = max(d.bit_length(), g.bit_length(), h.bit_length()) + 2
    assert width < 5000
    # An entry stores the cost and the already chosen bits of s,R,T.
    state = {(0, 0): (0, 0, 0, 0)}
    widths = []
    for bit in range(width):
        nxt = {}
        dk, gk, hk = (d >> bit)&1, (g >> bit)&1, (h >> bit)&1
        for (alpha, beta), (cost, sv, rv, tv) in state.items():
            for sigma in (0, 1):
                if bit == 0 and sigma:
                    continue
                for rho in (0, 1):
                    if rho and hk:
                        continue
                    ss = sigma+rho+alpha
                    if ss % 2 != dk:
                        continue
                    for tau in (0, 1):
                        tt = sigma+tau+beta
                        if tt % 2 != gk:
                            continue
                        key = (ss//2, tt//2)
                        candidate = (cost+key[1], sv|(sigma<<bit),
                                     rv|(rho<<bit), tv|(tau<<bit))
                        if key not in nxt or candidate < nxt[key]:
                            nxt[key] = candidate
        state = nxt
        widths.append(len(state))
    assert (0, 0) in state
    mu, s, remainder, other = state[(0,0)]
    independent = s.bit_count()+(g-s).bit_count()-g.bit_count()
    assert s+remainder == d and s+other == g
    assert s % 2 == 0 and remainder & h == 0
    assert mu == independent
    return {'cost':mu,'s':str(s),'remainder':str(remainder),'other':str(other),
            'j':str(4*s),'bits_processed':width,'max_states':max(widths),
            'digit_sum_check':independent}

def main():
    started=time.monotonic()
    auxiliary=[]
    for d in range(25):
        for h in (1,3,9,33,161,417):
            g=(h+1)//2
            if d>g:
                continue
            permissible=[s for s in range(0,d+1,2) if (d-s)&h==0]
            if not permissible:
                continue
            exact=min((s.bit_count()+(g-s).bit_count()-g.bit_count(),s)
                      for s in permissible)
            got=minimum_even_row(d,g,h)
            assert (got['cost'],int(got['s']))==exact
            auxiliary.append((d,h))
    records=[]
    for u in range(21):
        b=9**(18+32*u); h=2001*b; d=(b-1)//4; g=(h+1)//2
        assert b % 256==209 and h % 128==33 and g % 64==17 and d % 64==52
        rec={'u':u,'b':str(b),'d':str(d),'h':str(h),'g':str(g),
             'exact_arithmetic':minimum_even_row(d,g,h)}
        records.append(rec)
    assert records[0]['exact_arithmetic']['cost']<=21
    result={'authorship':'Coordinator; remote code not executed',
            'scope':'21 finite original full words; row valuations conditional on A5 turn5 theorem, not a sharp-content proof unless cost=1',
            'auxiliary_brute_force_cases':len(auxiliary),
            'original_cases':records,'seconds':round(time.monotonic()-started,4),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/'binary_actual_even_row_cost_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'auxiliary_checks':len(auxiliary),'original_minimum_costs':
                      [x['exact_arithmetic']['cost'] for x in records],
                      'seconds':result['seconds']}))

if __name__=='__main__':
    main()
