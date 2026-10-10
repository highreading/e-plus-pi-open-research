#!/usr/bin/env python3
"""New original complete 20-bit contractions by bounded odd-factorial transport.

Personally authored from inspected identities, not downloaded/external code.
Uses only retained physical short arrays; no endpoint operator regeneration.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
ROOT = Path(__file__).resolve().parent


def val2(x, cap):
    return cap if not x else (x & -x).bit_length() - 1


def differences(values, modulus):
    work = [x % modulus for x in values]
    out = []
    while work:
        out.append(work[0])
        work = [(work[i + 1] - work[i]) % modulus
                for i in range(len(work) - 1)]
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def consecutive_values(coefficients, count, modulus):
    work = coefficients[:]
    values = []
    for _ in range(count):
        values.append(work[0])
        for r in range(len(work) - 1):
            work[r] = (work[r] + work[r + 1]) % modulus
    return values


def newton_at(coefficients, x, modulus):
    choose, value = 1, 0
    for r, coefficient in enumerate(coefficients):
        if r:
            numerator = choose * (x - r + 1)
            assert numerator % r == 0
            choose = numerator // r
        value = (value + coefficient * choose) % modulus
    return value


class OddFactorial:
    def __init__(self, bits):
        self.bits, self.modulus = bits, 1 << bits
        g, values = 1, [1]
        for k in range(1, 2 * bits + 1):
            g = g * (2 * k - 1) % self.modulus
            values.append(g)
        self.coefficients = differences(values, self.modulus)
        assert len(self.coefficients) <= 2 * bits - 1
        for r, x in enumerate(self.coefficients[1:], 1):
            assert val2(x, bits) >= (r + 1) // 2
        self.cache = {}

    def at(self, h):
        if h not in self.cache:
            self.cache[h] = newton_at(self.coefficients, h, self.modulus)
        assert self.cache[h] & 1
        return self.cache[h]

    def sequence(self, h, step, count):
        result = []
        value = self.at(h)
        for i in range(count):
            result.append(value)
            current = h + step * i
            if step == 1:
                value = value * (2 * current + 1) % self.modulus
            else:
                assert step == -1
                value = value * pow((2 * current - 1) % self.modulus,
                                    -1, self.modulus) % self.modulus
        return result


def possible_flags(constants, t):
    mask = (1 << t) - 1
    thresholds = [x & mask for x in constants]
    prefixes = {0} | {x + 1 for x in thresholds if x + 1 <= mask}
    return {tuple(int(r > x) for x in thresholds) for r in prefixes}


def contraction(N, b, c, payloads, degrees, bits, log=False):
    assert 0 <= b <= N and c >= 0
    modulus = 1 << bits
    S = c + b
    length = max(N, b, c, S).bit_length()
    odd = OddFactorial(bits)
    states = {(0, 0, 0): [[x % modulus for x in p] for p in payloads]}
    trace, transitions, checked_coefficients = [], 0, 0
    for t in range(length):
        constants = [N >> t, b >> t, c >> t, S >> t]
        ncur, bcur, ccur, scur = constants
        half = [x >> 1 for x in constants]
        nh, bh, ch, sh = half
        nbit, bbit, cbit, sbit = [x & 1 for x in constants]
        kappa = sh - ch - bh
        assert kappa in (0, 1)
        reachable = possible_flags([N, b, S], t)
        assert set(states) <= reachable and len(reachable) <= 4
        next_states = {}
        for flags, arrays in states.items():
            ln, lb, ls = flags
            for epsilon in (0, 1):
                new = tuple(int(epsilon + borrow > bit)
                            for borrow, bit in zip(flags, (nbit, bbit, sbit)))
                lnn, lbn, lsn = new
                etan = nbit - ln - epsilon + 2 * lnn
                etab = bbit - lb - epsilon + 2 * lbn
                etas = sbit - ls - epsilon + 2 * lsn
                assert all(x in (0, 1) for x in (etan, etab, etas))
                power = kappa + lnn + lbn - lsn
                assert power in (0, 1, 2)
                upper_degree = max(len(p) - 1 for p in arrays) + 2 * bits - 2
                count = upper_degree + 1
                fixed = odd.at(nh + nbit) * pow(odd.at(ch + cbit), -1, modulus) % modulus
                gs = odd.sequence(sh - lsn + etas, -1, count)
                gn = odd.sequence(nh - lnn + etan, -1, count)
                gb = odd.sequence(bh - lbn + etab, -1, count)
                gj = odd.sequence(epsilon, 1, count)
                corrections = []
                for x, y, z, w in zip(gs, gn, gb, gj):
                    denominator = y * z * w % modulus
                    unit = fixed * x * pow(denominator, -1, modulus) % modulus
                    corrections.append(unit * unit % modulus)
                correction_coefficients = differences(corrections, modulus)
                assert len(correction_coefficients) <= 2 * bits - 1
                for r, x in enumerate(correction_coefficients[1:], 1):
                    assert val2(x, bits) >= (r + 1) // 2
                outputs = []
                for payload, initial_degree in zip(arrays, degrees):
                    vals = consecutive_values(payload, 2 * upper_degree + 2, modulus)
                    result = differences([
                        ((1 << (2 * power)) * correction * vals[2 * h + epsilon]) % modulus
                        for h, correction in enumerate(corrections)], modulus)
                    intercept = initial_degree >> (t + 1)
                    bound = intercept + 2 * (bits - 1)
                    assert len(result) <= bound + 1
                    for r, x in enumerate(result):
                        required = max(0, (r - intercept + 1) // 2)
                        assert val2(x, bits) >= required
                    checked_coefficients += len(result)
                    outputs.append(result)
                if new not in next_states:
                    next_states[new] = outputs
                else:
                    combined = next_states[new]
                    for z, p in zip(combined, outputs):
                        if len(z) < len(p):
                            z.extend([0] * (len(p) - len(z)))
                        for r, x in enumerate(p):
                            z[r] = (z[r] + x) % modulus
                        while len(z) > 1 and not z[-1]:
                            z.pop()
                transitions += 1
        states = {flag: arrays for flag, arrays in next_states.items()
                  if any(any(p) for p in arrays)}
        assert set(states) <= possible_flags([N, b, S], t + 1)
        if log:
            trace.append({'digit': t, 'bits_N_b_c_S': [nbit, bbit, cbit, sbit],
                          'masks': [list(x) for x in sorted(states)],
                          'degrees': [[len(p) - 1 for p in states[x]] for x in sorted(states)]})
    output = [p[0] for p in states.get((0, 0, 0), [[0] for _ in payloads])]
    return output, {'digits': length, 'transitions': transitions,
                    'valuation_degree_checks': checked_coefficients,
                    'terminal_state': [0, 0, 0], 'trace': trace}


def independent_small_checks():
    checks, nonzero = 0, 0
    for bits in (3, 7, 12):
        modulus = 1 << bits
        for b in range(17):
            n = 2 * b + 5 + b % 3
            N, c = n + 2, 2 * n - 1
            payloads = [[1], [3, 2, 5, 7, 11]]
            answers, _ = contraction(N, b, c, payloads, [0, 4], bits)
            expected = [sum(comb(N, j)**2 * comb(c + b - j, b - j)**2 *
                            sum(x * comb(j, r) for r, x in enumerate(p) if r <= j)
                            for j in range(b + 1)) % modulus for p in payloads]
            assert answers == expected
            checks += len(answers)
            nonzero += sum(x != 0 for x in answers)
    assert nonzero
    return {'exact_direct_contraction_checks': checks, 'nonzero_comparisons': nonzero}


def actual_payloads(data, bits):
    modulus = 1 << bits
    uf, ue = list(map(int, data['Uf_mod341'])), list(map(int, data['Ue_mod341']))
    newton = []
    for poly, exponent, degree in ((uf, 73, 81), (ue, 68, 77)):
        large_modulus = 1 << (bits + exponent)
        values = []
        for j in range(degree + 1):
            value = 0
            for coefficient in reversed(poly):
                value = (value * j + coefficient) % large_modulus
            assert value % (1 << exponent) == 0
            values.append(value >> exponent)
        newton.append(differences(values, modulus))
    f = consecutive_values(newton[0], 163, modulus)
    e = consecutive_values(newton[1], 163, modulus)
    ff = differences([x * x % modulus for x in f], modulus)
    fe = differences([x * y % modulus for x, y in zip(f, e)][:159], modulus)
    assert len(ff) <= 163 and len(fe) <= 159
    return [ff, fe]


def odd_product(start, length, bits):
    result, exponent = 1, 0
    modulus = 1 << bits
    for k in range(length):
        x = start + k
        e = val2(x, x.bit_length())
        exponent += e
        result = result * (x >> e) % modulus
    return result, exponent


def main():
    started = time.monotonic()
    checks = independent_small_checks()
    source = ROOT / 'binary_short_moment_certificate.json'
    data = json.loads(source.read_text())
    n, b = int(data['n']), int(data['b'])
    payloads = actual_payloads(data, 36)
    results, trace = contraction(n + 2, b, 2 * n - 1, payloads, [162, 158], 36, True)
    sf = results[0] % (1 << 34)
    sm = results[1]
    assert sf % (1 << 16) == 0 and sm % (1 << 18) == 0
    df, vf = odd_product(2 * n, 81, 20)
    de, ve = odd_product(2 * n, 77, 20)
    assert (vf, ve) == (80, 77)
    norm = (sf >> 14) * pow(df * df % (1 << 20), -1, 1 << 20) % (1 << 20)
    mixed = (sm >> 16) * pow(df * de % (1 << 20), -1, 1 << 20) % (1 << 20)
    assert norm % 4 == mixed % 4 == 0
    artifact = {'status': 'PASS', 'scope': 'NEW actual original u0 complete weighted norm/mixed contractions modulo2^20',
                'n': str(n), 'b': str(b), 'physical_bits': 20,
                'kernel_bits': [34, 36], 'shared_transport_bits': 36,
                'Sff_mod2_34': sf, 'Sfe_mod2_36': sm,
                'odd_normalizers_df_de_mod2_20': [df, de],
                'D_raw_mod2_20': norm, 'E_raw_mod2_20': mixed,
                'valuation_D_raw': {'value_or_lower_bound': val2(norm, 20), 'exact': bool(norm)},
                'valuation_E_raw': {'value_or_lower_bound': val2(mixed, 20), 'exact': bool(mixed)},
                'finite_range_inclusive': '0<=j<=b', 'complete_exterior_retained': True,
                'independent_small_checks': checks, 'transport': trace,
                'accepted_terminal_state_only': [0, 0, 0],
                'all_other_terminal_states_discarded': True,
                'all_prime_gcd_evaluated': False, 'irrationality_proved': False}
    target = ROOT / 'original_binary_gram_transport_certificate.json'
    target.write_text(json.dumps(artifact, indent=2) + '\n')
    receipt = {k: artifact[k] for k in (
        'status', 'scope', 'physical_bits', 'kernel_bits', 'D_raw_mod2_20', 'E_raw_mod2_20',
        'valuation_D_raw', 'valuation_E_raw', 'finite_range_inclusive',
        'complete_exterior_retained', 'independent_small_checks', 'all_prime_gcd_evaluated',
        'irrationality_proved')}
    receipt.update(digits=trace['digits'], transitions=trace['transitions'],
                   valuation_degree_checks=trace['valuation_degree_checks'],
                   maximum_live_states=max(len(x['masks']) for x in trace['trace']),
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                   artifact_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                   elapsed_seconds=time.monotonic() - started)
    (ROOT / 'original_binary_gram_transport_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)


if __name__ == '__main__':
    main()
