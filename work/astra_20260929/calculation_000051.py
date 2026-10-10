import json
from fractions import Fraction

path = 'work/session_20260927/hp_b1_closed_prime_rate_and_crt_certificate.json'
with open(path, 'r', encoding='utf-8') as f:
    certificate = json.load(f)

def pell_power(exponent):
    a, b = 1, 0
    for _ in range(exponent):
        a, b = a + 2*b, a + b
    assert a*a - 2*b*b == (-1)**exponent
    return a, b

def compare_exact(left, exponent):
    a, b = pell_power(exponent)
    assert b > 0
    d = left - a
    margin = d*d - 2*b*b
    sign = -1 if d < 0 else (margin > 0) - (margin < 0)
    return {'left_integer': left, 'pell_exponent': exponent,
            'pell_a': a, 'pell_b': b, 'sign': sign,
            'squared_comparison_margin': margin}

specifications = [
    ('all_even', 2**9 * 5**3 * 13, 12, 1),
    ('odd_7_good', 5**3 * 13 * 7**2, 12, 1),
    ('odd_smallest_two_good', 5**36 * 13**12 * 17**9 * 19**8, 144, 1),
    ('odd_largest_single_good_insufficient', 5**15 * 13**5 * 11**6, 60, -1)
]
rates = {name: compare_exact(left, exponent)
         for name, left, exponent, expected in specifications}
rate_signs_pass = all(rates[name]['sign'] == expected
                      for name, left, exponent, expected in specifications)

bad = {7: {2, 3}, 11: {2}, 17: {3, 11}, 19: {14}}
pattern_names = {
    (False, False, True): 'bad11_bad17_good19',
    (False, True, False): 'bad11_good17_bad19',
    (True, False, False): 'good11_bad17_bad19',
    (False, False, False): 'all_three_bad'
}
components = {name: 0 for name in pattern_names.values()}
small_modulus = 11*17*19
for r in range(small_modulus):
    pattern = tuple(r % p not in bad[p] for p in (11, 17, 19))
    if pattern in pattern_names:
        components[pattern_names[pattern]] += 1

modulus = 7*small_modulus

def survives_mandatory_rates(n):
    return (n % 7 in bad[7]
            and sum(n % p not in bad[p] for p in (11, 17, 19)) <= 1)

residues = [r for r in range(modulus) if survives_mandatory_rates(r)]
odd_residues = [r for r in range(2*modulus)
                if r % 2 == 1 and survives_mandatory_rates(r)]
crt_pass = (
    components == {'bad11_bad17_good19': 36,
                   'bad11_good17_bad19': 15,
                   'good11_bad17_bad19': 20,
                   'all_three_bad': 2}
    and len(residues) == 2*sum(components.values()) == 146
    and len(odd_residues) == len(residues)
    and {r % modulus for r in odd_residues} == set(residues)
    and modulus == 24871
)
computed = {
    'all_checks_pass': rate_signs_pass and crt_pass,
    'rate_checks': rates,
    'crt_component_counts': components,
    'unexcluded_residue_count': len(residues),
    'odd_modulus': modulus,
    'density_among_odd': str(Fraction(len(odd_residues), modulus)),
    'density_among_all': str(Fraction(len(odd_residues), 2*modulus))
}
differences = []
scalar_count = [0]

def compare_fields(actual, recorded, location):
    if isinstance(actual, dict):
        if not isinstance(recorded, dict):
            differences.append({'field': location, 'computed': actual, 'recorded': recorded})
            return
        if set(actual) != set(recorded):
            differences.append({'field': location + '.keys',
                                'computed': sorted(actual), 'recorded': sorted(recorded)})
        for key, value in actual.items():
            compare_fields(value, recorded.get(key), location + '.' + key)
    else:
        scalar_count[0] += 1
        if type(actual) is not type(recorded) or actual != recorded:
            differences.append({'field': location, 'computed': actual, 'recorded': recorded})

for key, value in computed.items():
    compare_fields(value, certificate.get(key), key)

print(json.dumps({
    'certificate_path': path,
    'computed': computed,
    'compared_scalar_fields': scalar_count[0],
    'differences': differences,
    'independent_finite_verification_pass': computed['all_checks_pass'] and not differences,
    'scope': 'Exact rate comparisons and exhaustive CRT enumeration only; actual denominator and error theorems remain separate dependencies.'
}, ensure_ascii=False, indent=2))