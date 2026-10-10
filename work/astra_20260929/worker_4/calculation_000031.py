import json

primes = [3, 5, 7, 11, 13]
max_d = 1000

def vp_factorial(n, p):
    value = 0
    while n:
        n //= p
        value += n
    return value

def digit_count(n, p):
    count = 0
    while n:
        count += 1
        n //= p
    return count

summaries = []
for p in primes:
    A = p - 2
    largest_K = ((p - 1) * (max_d - 1) + A - 1) // A
    # Full finite enumeration is independent of the proposed short interval.
    limit = largest_K + 2 * p
    g = [k - vp_factorial(k, p) for k in range(limit + 1)]
    largest_gap = 0
    largest_window = 0
    examples = []
    for d in range(1, max_d + 1):
        B = (p - 1) * (d - 1)
        K = max(1, (B + A - 1) // A)
        full_bad = [k for k in range(limit + 1) if g[k] < d]
        J_full = full_bad[-1] + 1
        assert J_full <= K
        if d == 1:
            assert J_full == K == 1
            continue
        L = digit_count(K - 1, p)
        C = (p - 1) * L
        H = max(0, (B - C) // A)
        assert 0 <= H < K
        assert g[H] < d
        J_short = 1 + max(k for k in range(H, K) if g[k] < d)
        assert J_short == J_full
        assert H + 1 <= J_full <= K
        assert K - H <= (C + A - 1) // A + 1
        assert K - J_full <= (C + A - 1) // A
        largest_gap = max(largest_gap, K - J_full)
        largest_window = max(largest_window, K - H)
        if d in [5, 10, 100, 1000]:
            examples.append({'d': d, 'H': H, 'J': J_full, 'K': K})
    summaries.append({'p': p, 'precisions_checked': max_d, 'largest_observed_gap': largest_gap, 'largest_search_window': largest_window, 'examples': examples})

print(json.dumps({'status': 'all finite checks passed', 'scope': 'Arithmetic validation of the unreviewed search-interval corollary; finite checks do not replace its proof.', 'results': summaries}, indent=2))