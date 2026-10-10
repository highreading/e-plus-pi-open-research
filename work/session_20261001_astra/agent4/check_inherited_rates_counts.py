"""Independent exact rate/count audit; no HP degree or prime scan."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

OUT = Path('work/session_20261001_astra/agent4')
OLD = Path('work/session_20260927/hp_b1_closed_prime_rate_and_crt_certificate.json')


def multiply_pairs(x, y):
    a, b = x
    c, d = y
    return a*c + 2*b*d, a*d + b*c


def quadratic_power(k):
    """Return the integer pair for (1+sqrt(2))**k by binary powering."""
    result, base = (1, 0), (1, 1)
    while k:
        if k & 1:
            result = multiply_pairs(result, base)
        base = multiply_pairs(base, base)
        k //= 2
    return result


def compare(left, exponent):
    a, b = quadratic_power(exponent)
    assert b > 0
    d = left - a
    margin = d*d - 2*b*b
    sign = -1 if d <= 0 else (margin > 0) - (margin < 0)
    assert sign != 0
    return {
        'left_integer': left,
        'pell_exponent': exponent,
        'pell_a': a,
        'pell_b': b,
        'sign': sign,
        'squared_comparison_margin': margin,
        'decision_branch': 'left <= rational part' if d <= 0 else 'positive difference squared'
    }


def main():
    checks = {
        'all_even': compare(2**9 * 5**3 * 13, 12),
        'odd_7_good': compare(5**3 * 13 * 7**2, 12),
        'odd_smallest_two_good': compare(5**36 * 13**12 * 17**9 * 19**8, 144),
        'odd_largest_single_good_insufficient': compare(5**15 * 13**5 * 11**6, 60),
        'draft_B_low_c_exclusion': compare(2**6 * 5**3 * 13, 12)
    }
    expected = {
        'all_even': 1,
        'odd_7_good': 1,
        'odd_smallest_two_good': 1,
        'odd_largest_single_good_insufficient': -1,
        'draft_B_low_c_exclusion': 1
    }
    assert {key: value['sign'] for key, value in checks.items()} == expected

    prior = json.loads(OLD.read_text(encoding='utf-8'))
    compared_fields = ('left_integer', 'pell_exponent', 'pell_a', 'pell_b',
                       'sign', 'squared_comparison_margin')
    inherited_matches = {}
    for key in prior['rate_checks']:
        inherited_matches[key] = all(
            checks[key][field] == prior['rate_checks'][key][field]
            for field in compared_fields
        )
    assert all(inherited_matches.values())

    bad = {7: {2, 3}, 11: {2}, 17: {3, 11}, 19: {14}}
    labels = {
        (True, True, False): 'bad11_bad17_good19',
        (True, False, True): 'bad11_good17_bad19',
        (False, True, True): 'good11_bad17_bad19',
        (True, True, True): 'all_three_bad'
    }
    counts = {label: 0 for label in labels.values()}
    for a, b, c in product(range(11), range(17), range(19)):
        flags = (a in bad[11], b in bad[17], c in bad[19])
        if flags in labels:
            counts[labels[flags]] += 1
    assert counts == {
        'bad11_bad17_good19': 36,
        'bad11_good17_bad19': 15,
        'good11_bad17_bad19': 20,
        'all_three_bad': 2
    }
    assert counts == prior['crt_component_counts']
    assert sum(counts.values()) == 73

    modulus = 7*11*17*19
    assert modulus == 24871

    def retained(r):
        return (r % 7 in bad[7]
                and sum(r % p in bad[p] for p in (11, 17, 19)) >= 2)

    residues = [r for r in range(modulus) if retained(r)]
    assert len(residues) == 146 == prior['unexcluded_residue_count']
    assert modulus == prior['odd_modulus']
    odd_classes = {r if r % 2 else r + modulus for r in residues}
    assert len(odd_classes) == 146
    assert all(r % 2 == 1 and retained(r) for r in odd_classes)

    combined_modulus = 16*modulus
    inverse = pow(modulus, -1, 16)
    combined = sorted(r + modulus*((15-r)*inverse % 16) for r in residues)
    assert combined_modulus == 397936
    assert len(combined) == len(set(combined)) == 146
    assert all(0 <= r < combined_modulus and r % 16 == 15 and retained(r)
               for r in combined)
    direct_combined = [r for r in range(15, combined_modulus, 16) if retained(r)]
    assert combined == direct_combined
    density = Fraction(len(combined), combined_modulus)
    assert density == Fraction(73, 198968)

    certificate = {
        'scope': 'Exact rate comparisons and finite congruence counts only; arithmetic and analytic theorem inputs are audited separately.',
        'all_checks_pass': True,
        'method': 'Binary powering in Z[sqrt(2)], guarded integer comparisons, independent complete residue enumeration, and CRT lifting.',
        'rate_checks': checks,
        'inherited_rate_certificate_matches': inherited_matches,
        'crt_component_counts': counts,
        'closed_prime_modulus': modulus,
        'closed_prime_residue_count': len(residues),
        'closed_prime_residues': residues,
        'closed_prime_density_among_odd': str(Fraction(len(residues), modulus)),
        'closed_prime_with_odd_parity_density_among_all': str(Fraction(len(residues), 2*modulus)),
        'draft_A_modulus': combined_modulus,
        'draft_A_residue_count': len(combined),
        'draft_A_residues': combined,
        'draft_A_density_among_all': str(density),
        'new_HP_degrees_evaluated': 0,
        'new_primes_tested': [],
        'limitation': 'Retained residues are unexcluded indices, not certified successful approximants.'
    }
    OUT.mkdir(parents=True, exist_ok=True)
    destination = OUT / 'audit_rate_count_certificate.json'
    destination.write_text(json.dumps(certificate, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({
        'all_checks_pass': True,
        'rate_comparison_signs': expected,
        'inherited_certificate_matches': all(inherited_matches.values()),
        'component_counts': counts,
        'closed_prime_count_and_modulus': [len(residues), modulus],
        'draft_A_count_and_modulus': [len(combined), combined_modulus],
        'draft_A_density_among_all': str(density),
        'certificate': str(destination)
    }, indent=2))


if __name__ == '__main__':
    main()
