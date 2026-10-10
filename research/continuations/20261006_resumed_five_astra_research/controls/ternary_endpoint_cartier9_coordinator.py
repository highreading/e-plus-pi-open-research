#!/usr/bin/env python3
"""NEW coordinator-owned paid modulo9 endpoint and suffix-carry arithmetic.
No original producer, force or old modulo3 sample is regenerated.
"""
from fractions import Fraction
from pathlib import Path
from math import comb
import hashlib
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
C = Path(__file__).resolve().parent
started = time.monotonic()
MOD = 9

def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % MOD
    return out

def power(a, exponent):
    out = [1]
    for _ in range(exponent):
        out = multiply(out, a)
    return out

def padded(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    assert len(a) <= 17
    return tuple(a + [0] * (17 - len(a)))

plus, minus = [1, 1], [1, -1]
denominator_restore = power([1, 0, -1], 3)
main_multipliers = [multiply(power(plus, 6-3*r), power(minus, 6+r)) for r in range(3)]
carry_multipliers = [multiply(power(plus, 6-3*r), power(minus, 4+r)) for r in range(3)]

def section_shift(poly, shift):
    out = []
    for i, value in enumerate(poly):
        exponent = i + shift
        if exponent % 3 == 0:
            assert exponent >= 0
            degree = exponent // 3
            while len(out) <= degree:
                out.append(0)
            out[degree] = value
    return out or [0]

def transition(state, digit, lookahead):
    first = section_shift(multiply(state, main_multipliers[digit]), -digit)
    second = section_shift(multiply(state, carry_multipliers[digit]), 1-digit)
    length = max(len(first), len(second))
    total = [(first[i] if i < len(first) else 0) - 3*lookahead*(second[i] if i < len(second) else 0)
             for i in range(length)]
    return padded(multiply(denominator_restore, total))

initial = [
    padded(multiply(power(minus, 7), power(plus, 8))),
    padded([0] + multiply(power(minus, 6), power(plus, 9))),
    padded(multiply(power(minus, 8), power(plus, 7))),
    padded(multiply(power(minus, 8), power(plus, 8))),
]

def run(state, digits, next_digit=0):
    for i, digit in enumerate(digits):
        q = digits[i+1] if i+1 < len(digits) else next_digit
        state = transition(state, digit, q)
    return state

def evaluate(state, n):
    while n:
        state = transition(state, n % 3, (n // 3) % 3)
        n //= 3
    return state[0]

def direct_endpoint(m, adjacent):
    limit = m-1 if adjacent else m
    top = 3*m-2 if adjacent else 3*m-1
    alpha = Fraction(2*m-3 if adjacent else 2*m-1, 2)
    coefficient, total = Fraction(1), Fraction(0)
    for k in range(limit+1):
        total += comb(top, limit-k) * coefficient * (1 << k)
        coefficient *= Fraction(alpha-k, k+1)
    total *= (-1) ** limit
    assert total.denominator % 3
    return total.numerator * pow(total.denominator, -1, MOD) % MOD

# New precision and new direct indices, independently using characteristic-zero
# generalized binomial coefficients rather than the transition recurrence.
direct_checks = 0
for m in range(141, 181):
    for adjacent in (False, True):
        assert evaluate(initial[int(adjacent)], m) == direct_endpoint(m, adjacent)
        direct_checks += 1

basis = [tuple(int(i == j) for i in range(17)) for j in range(17)]
degree_checks = 0
for state in basis:
    for r in range(3):
        for q in range(3):
            out = transition(state, r, q)
            assert out[16] == 0
            degree_checks += 1

embedding_factor = multiply(power(minus, 6), power(plus, 4))
def embed(h):
    return padded(multiply(embedding_factor, h))

R = [-1, 1, 0, -1, 1]
P = [1, 1, -1, -1]
injection_checks = 0
for q in range(3):
    for h, expected in ((R, power(minus, 2)),
                        (P, multiply(minus, [1+q, q]))):
        out = transition(embed(h), 2, q)
        assert all(value % 3 == 0 for value in out)
        assert tuple(value//3 % 3 for value in out) == tuple(value % 3 for value in embed(expected))
        injection_checks += 1

suffix = [2, 1, 1, 1, 1, 0, 1, 0]
states = [[run(h, suffix, next_digit) for next_digit in range(3)] for h in initial]
leading_functional = [run(h, [1]*25)[0] for h in basis]

# Record actual inherited carries, relative to the specified integral R lift.
inherited = []
for output, output_states in enumerate(states):
    sign = -1 if output == 0 else 1
    row = []
    base = embed(R)
    for state in output_states:
        remainder = [(state[i] - sign*base[i]) % MOD for i in range(17)]
        assert all(value % 3 == 0 for value in remainder)
        row.append([value//3 for value in remainder])
    inherited.append(row)

# NEW higher-layer endpoint classification on finite arbitrary-middle cylinders.
# This does not assert those words occur at original power-of-two indices.
counts = {}
witnesses = {}
middle_checks = 0
for length in range(6):
    for word in itertools.product(range(3), repeat=length):
        digits = suffix + list(reversed(word)) + [1]*25
        outputs = tuple(run(h, digits)[0] for h in initial)
        classification = ('endpoint_unit' if any(value % 3 for value in outputs[:2])
                          else 'endpoint_content_exactly1' if any(outputs[:2])
                          else 'endpoint_content_atleast2')
        counts[classification] = counts.get(classification, 0) + 1
        witnesses.setdefault(classification, {'middle_word_msf': list(word), 'outputs_mod9': outputs})
        middle_checks += 1

artifact = {
    'status': 'PASS',
    'scope': 'NEW seventeen-coordinate actual endpoint modulo9 realization, paid absorbing-digit injections, inherited suffix carries and finite middle-word higher-layer classification',
    'initial_numerators': initial,
    'degree_basis_checks': degree_checks,
    'direct_coefficient_indices': [141, 180],
    'direct_characteristic_zero_endpoint_checks': direct_checks,
    'paid_injection_checks': injection_checks,
    'suffix_next_digit_values': [0, 1, 2],
    'suffix_output_states_mod9': states,
    'actual_inherited_suffix_carries_mod3': inherited,
    'leading25ones_functional_mod9': leading_functional,
    'finite_middle_word_checks': middle_checks,
    'middle_lengths': [0, 5],
    'classification_counts': counts,
    'classification_witnesses': witnesses,
    'actual_original_power_middle_word_classified': False,
    'original_infinite_family_primitive_direction_proved': False,
    'all_prime_primitive_denominator_evaluated': False,
    'irrationality_proved': False,
    'report_sha256': hashlib.sha256((C.parent/'responses/A1_turn15.md').read_bytes()).hexdigest(),
    'elapsed_seconds': round(time.monotonic()-started, 3),
}
out = C/'ternary_endpoint_cartier9_certificate.json'
out.write_text(json.dumps(artifact, indent=2) + '\n')
receipt = {k: v for k, v in artifact.items() if k not in ('initial_numerators', 'suffix_output_states_mod9', 'actual_inherited_suffix_carries_mod3')}
receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256'] = hashlib.sha256(out.read_bytes()).hexdigest()
(C/'ternary_endpoint_cartier9_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
