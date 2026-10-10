from pathlib import Path
import hashlib
import json

project_root = Path('[private local path removed]')
specifications = [
    ('odd-prime-cutoff-sharpness-and-logarithmic-search-v1', 'cb90914afe3b69d4f1db4bbed7c007e1bb7eb0cb3ecf0abb6274cfe4971bbd93', 'f551c6049ebc68c0d462c7e6f06e21e8cedef5f12c992453bb0301975a5fb947'),
    ('odd-prime-interpolation-tail-cutoff-v1', '2757da21024783fba7cd9c881de89c14db59b114a26787209ef0e639b8130799', '80df0d51fcf8706c0114c3cb997fd74862abe93165f0e594decd5b7391cf71be')
]
hash_results = []
for claim_id, expected_payload, expected_file in specifications:
    candidate_path = project_root / 'work/astra_review_registry/candidates' / (claim_id + '.md')
    raw = candidate_path.read_bytes()
    marker = ('Content SHA256: ' + expected_payload + '\n\n').encode('utf-8')
    marker_position = raw.find(marker)
    record = {'claim_id': claim_id, 'file_bytes': len(raw), 'file_sha256': hashlib.sha256(raw).hexdigest()}
    record['ledger_hash_matches'] = record['file_sha256'] == expected_file
    if marker_position < 0:
        record['registry_hash_matches'] = False
        record['error'] = 'Expected payload header not found'
    else:
        start = marker_position + len(marker)
        payload = raw[start:]
        record.update({'payload_byte_offset': start, 'payload_bytes': len(payload), 'payload_sha256': hashlib.sha256(payload).hexdigest()})
        record['registry_hash_matches'] = record['payload_sha256'] == expected_payload
    hash_results.append(record)

def vp_integer(value, p):
    if value == 0:
        raise ValueError('Zero has infinite valuation')
    value = abs(value)
    result = 0
    while value % p == 0:
        value //= p
        result += 1
    return result

def vp_factorial(n, p):
    result = 0
    while n:
        n //= p
        result += n
    return result

def digit_sum(n, p):
    result = 0
    while n:
        n, digit = divmod(n, p)
        result += digit
    return result

def digit_count(n, p):
    result = 0
    while n:
        n //= p
        result += 1
    return result

def ceil_div(a, b):
    return -((-a) // b)

primes = [3, 5, 7, 11, 13, 17, 19, 31]
maximum_precision = 2000
arithmetic_results = []
reference_tables = {}
precision_cases = 0

# For every odd p, g(k) >= (k+1)/2 when k >= 1.
# Thus this independent reference scan includes every bad index
# for every tested precision, regardless of nonmonotonicity.
for p in primes:
    limit = 2 * maximum_precision
    g_values = [0]
    factorial_valuation = 0
    for k in range(1, limit + 1):
        factorial_valuation += vp_integer(k, p)
        g_values.append(k - factorial_valuation)
    for k, value in enumerate(g_values):
        assert (p - 1) * value == (p - 2) * k + digit_sum(k, p), (p, k)
        assert value >= 0

    last_at_value = [-1] * maximum_precision
    for k, value in enumerate(g_values):
        if value < maximum_precision:
            last_at_value[value] = k
    reference_J = [None] * (maximum_precision + 1)
    last_bad = -1
    for d in range(1, maximum_precision + 1):
        last_bad = max(last_bad, last_at_value[d - 1])
        reference_J[d] = last_bad + 1
    reference_tables[p] = reference_J

    largest_width = 0
    largest_gap = 0
    for d in range(1, maximum_precision + 1):
        A = p - 2
        B = (p - 1) * (d - 1)
        K = max(1, ceil_div(B, A))
        if d == 1:
            assert reference_J[d] == K == 1
        else:
            L = digit_count(K - 1, p)
            C = (p - 1) * L
            H = max(0, (B - C) // A)
            assert 0 <= H < K <= limit
            assert g_values[H] < d
            bad_in_interval = [k for k in range(H, K) if g_values[k] < d]
            scanned_J = bad_in_interval[-1] + 1
            assert scanned_J == reference_J[d], (p, d, H, K, scanned_J, reference_J[d])
            assert H + 1 <= scanned_J <= K
            assert K - H <= ceil_div(C, A) + 1
            assert 0 <= K - scanned_J <= ceil_div(C, A)
            largest_width = max(largest_width, K - H)
            largest_gap = max(largest_gap, K - scanned_J)
        precision_cases += 1
    arithmetic_results.append({'p': p, 'precisions_checked': maximum_precision, 'largest_search_width': largest_width, 'largest_K_minus_J': largest_gap})

power_cases = 0
power_cases_with_full_reference_scan = 0
for p in primes:
    for t in range(9):
        q = p ** t
        numerator = (p - 2) * q + 1
        assert numerator % (p - 1) == 0
        d = 1 + numerator // (p - 1)
        assert q - vp_factorial(q, p) == d - 1
        K = max(1, ceil_div((p - 1) * (d - 1), p - 2))
        assert K == q + 1
        if d <= maximum_precision:
            assert reference_tables[p][d] == q + 1
            power_cases_with_full_reference_scan += 1
        power_cases += 1

def falling_on_disk(a, p, length):
    coefficients = [1]
    for j in range(length):
        updated = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] += (a - j) * coefficient
            updated[degree + 1] += p * coefficient
        coefficients = updated
    return coefficients

def square_polynomial(coefficients):
    result = [0] * (2 * len(coefficients) - 1)
    for i, left in enumerate(coefficients):
        for j, right in enumerate(coefficients):
            result[i + j] += left * right
    return result

def gauss_valuation(coefficients, p):
    return min(vp_integer(coefficient, p) for coefficient in coefficients if coefficient)

witness_results = []
witness_count = 0
for p, q_values in [(3, [1, 3, 9]), (5, [1, 5]), (7, [1, 7]), (11, [1, 11])]:
    for q in q_values:
        length = p * q
        expected = q - vp_factorial(q, p)
        observed = []
        for a in range(p):
            falling = falling_on_disk(a, p, length)
            squared = square_polynomial(falling)
            assert gauss_valuation(falling, p) == q, (p, q, a, 'falling')
            numerator_valuation = gauss_valuation(squared, p)
            assert numerator_valuation == 2 * q, (p, q, a, 'square')
            summand_valuation = numerator_valuation - vp_factorial(length, p)
            assert summand_valuation == expected, (p, q, a, summand_valuation, expected)
            observed.append(summand_valuation)
            witness_count += 1
        witness_results.append({'p': p, 'q': q, 'disks_checked': p, 'minimum_summand_valuation': min(observed), 'maximum_summand_valuation': max(observed), 'expected_d_minus_one': expected})

assert gauss_valuation([1], 3) == 0
example = {'p': 3, 'd': 6, 'g8': 8 - vp_factorial(8, 3), 'g9': 9 - vp_factorial(9, 3), 'J': reference_tables[3][6]}
assert example == {'p': 3, 'd': 6, 'g8': 6, 'g9': 5, 'J': 10}
print(json.dumps({'hash_checks': hash_results, 'all_exact_payload_hashes_match': all(item['registry_hash_matches'] for item in hash_results), 'arithmetic_checks_passed': True, 'precision_cases': precision_cases, 'arithmetic_summary': arithmetic_results, 'power_identity_cases': power_cases, 'power_cases_with_full_reference_scan': power_cases_with_full_reference_scan, 'expanded_polynomial_witnesses': witness_count, 'witness_summary': witness_results, 'nonmonotonicity_example': example}, indent=2))