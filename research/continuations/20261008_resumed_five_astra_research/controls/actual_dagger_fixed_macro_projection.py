"""NEW bounded exact macro projection, not an original-sized source solve.

Coordinator authored. Its universal applicability requires the source and
carry/unit arguments in the companion note; the receipt alone is not a proof.
No credentials, network, remote code, or original-sized arrays are used.
"""
from pathlib import Path
import datetime, hashlib, json, time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'ACTUAL_DAGGER_FIXED_MACRO_PROJECTION_RECEIPT.json'
assert not OUT.exists(), 'This new bounded receipt must not be rerun.'
started = time.monotonic()

def binomial_row_mod27(m):
    value = 1
    values = [1]
    for l in range(m):
        value, remainder = divmod(value * (m - l), l + 1)
        assert remainder == 0
        values.append(value % 27)
    return values

rows = {m: binomial_row_mod27(m) for m in (7245, 7299)}
coarse = [1]
value = 1
for n in range(3621):
    value, remainder = divmod(value * (7243 + n), n + 1)
    assert remainder == 0
    coarse.append(value % 27)
assert len(coarse) == 3622

sources = [(7299, 122, 1), (7299, 41, 3)]
sources += [(7245, b, 18) for b in (14, 15, 16, 41, 42, 43, 95, 96, 97)]
sources += [(7245, b, -9) for b in (131, 132, 133)]
assert len(sources) == 14

targets = {1: 0, 3: 1, 5: 0, 7: 0, 9: 2}
results = {}
term_count = 0
for v, target in targets.items():
    modulus = 3 ** (target + 1)
    divisor = 3 ** target
    source_rows = []
    total_scaled = 0
    checked_terms = 0
    for m, b, c in sources:
        r = (2187 * v - 1) // 2 - 27 * b
        subtotal = 0
        active = 0
        for n in range(3622):
            l = n + r - 3621
            if l < 0 or l > m:
                continue
            sign = -1 if l % 2 else 1
            term = (c * sign * rows[m][l] * coarse[n]) % modulus
            assert term % divisor == 0, (v, m, b, c, n, l, term, target)
            subtotal = (subtotal + term // divisor) % 3
            active += 1
        total_scaled = (total_scaled + subtotal) % 3
        checked_terms += active
        source_rows.append({'M': m, 'b': b, 'c': c, 'active_terms': active,
                            'scaled_coarse_source_sum_mod3': subtotal})
    # Actual binomial units have the universal extra factor 2 mod3;
    # literal C_d recurrence gives the minus sign.
    results[str(v)] = {'target_v3': target, 'termwise_target_verified': True,
                       'active_terms': checked_terms,
                       'scaled_coarse_total_mod3': total_scaled,
                       'actual_C_v_scaled_mod3': (-2 * total_scaled) % 3,
                       'sources': source_rows}
    term_count += checked_terms

cv = {v: results[str(v)]['actual_C_v_scaled_mod3'] for v in targets}
# The unit-source HIGH term has target_v3=2 from the v=9 check;
# every other source has a coefficient divisible by3. Thus zeta=0.
zeta = 0
a_eta = (zeta - cv[1] - 2 * cv[5] - cv[7] - 4 * cv[3] - 4 * cv[9]) % 3
obj = {'time': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),
       'scope': 'NEW fixed macro coefficients for original i_dagger=(g-1)/2-u+244; source/carry applicability proof is separate',
       'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'integer_binomial_rows': [7245, 7299], 'coarse_binomial': 'binom(7242+n,n)',
       'n_range': [0, 3621], 'all_fourteen_sources_retained': True,
       'active_term_checks': term_count, 'poles': results,
       'zeta_mod3_from_paid_source_depth': zeta,
       'a_eta_dagger_mod3': a_eta,
       'seconds': round(time.monotonic() - started, 6),
       'status': 'PASS exact fixed arithmetic; uniform source applicability and DIFFERENT audit pending',
       'e_plus_pi_decision': False}
OUT.write_text(json.dumps(obj, indent=2) + '\n')
print(json.dumps({'receipt': OUT.name, 'active_term_checks': term_count,
                  'scaled_actual_C_mod3': cv, 'zeta_mod3': zeta,
                  'a_eta_dagger_mod3': a_eta, 'seconds': obj['seconds']}))
