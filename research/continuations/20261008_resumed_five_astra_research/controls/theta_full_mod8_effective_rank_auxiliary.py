"""ONE new bounded complete-mod8 diagnostic, coordinator authored.

No network, keys, downloaded code, original-sized solve or old receipt rerun.
The complete normalized minimal theta aggregate is formed from DIFFERENT-
passed mod8 laws, with the actual atom ratios and all contact columns.
Binary precision is capped at3. This yields auxiliary module invariants,
not an original-index valuation upper or an e+pi proof.
"""
from pathlib import Path
import hashlib, json, math, time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'THETA_FULL_MOD8_EFFECTIVE_RANK_AUXILIARY_RECEIPT.json'
assert not OUT.exists(), 'A closed bounded diagnostic must not be rerun.'
CASES = ((144, 64, 16, 36), (272, 128, 16, 67), (272, 128, 16, 68))
start = time.monotonic()

def mul(a, b, modulus):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) % modulus
             for j in range(2)] for i in range(2)]

def transition(length, base, modulus):
    out = [[1, 0], [0, 1]]
    for n in range(base, base+length):
        out = mul([[2*n+1, 1], [1, 0]], out, modulus)
    return out

for n in range(4):
    diag = 3 if n % 2 == 0 else 7
    assert transition(6, n, 8) == [[diag, 4], [4, diag]]
    assert transition(12, n, 8) == [[1, 0], [0, 1]]
periods = []
for h in range(3, 11):
    modulus, period = 1 << h, 3*(1 << (h-1))
    theta = [1, 0]
    for n in range(1, 2*period+1):
        theta.append(((2*n+1)*theta[-1]+theta[-2]) % modulus)
    checks = period+2
    assert all(theta[n+period] == theta[n] for n in range(checks))
    periods.append({'precision': h, 'period': period, 'checks': checks})

def binary_rank(rows):
    pivots = {}
    for row in rows:
        bits = sum((x & 1) << i for i, x in enumerate(row))
        while bits:
            j = bits.bit_length()-1
            if j in pivots:
                bits ^= pivots[j]
            else:
                pivots[j] = bits
                break
    return len(pivots)

def capped_module_counts(rows):
    """Odd unit pivots, then whole even residual divided at each level.

    Every row elimination is unimodular modulo the current power of2.
    Clearing its pivot row by column operations does not change the trailing
    block because the pivot column has already been cleared below it.
    Division happens only after EVERY entry in the entire residual is even.
    """
    a = [r[:] for r in rows]
    counts = []
    for level in range(3):
        modulus = 1 << (3-level)
        size, pivot = len(a), 0
        while pivot < size:
            found = None
            for i in range(pivot, size):
                for j in range(pivot, size):
                    if a[i][j] & 1:
                        found = i, j
                        break
                if found is not None:
                    break
            if found is None:
                break
            i, j = found
            a[pivot], a[i] = a[i], a[pivot]
            if j != pivot:
                for row in a:
                    row[pivot], row[j] = row[j], row[pivot]
            inverse = pow(a[pivot][pivot], -1, modulus)
            prow = a[pivot]
            for i in range(pivot+1, size):
                factor = a[i][pivot]*inverse % modulus
                if factor:
                    for j in range(pivot+1, size):
                        a[i][j] = (a[i][j]-factor*prow[j]) % modulus
                    a[i][pivot] = 0
            pivot += 1
        counts.append(pivot)
        tail = [row[pivot:] for row in a[pivot:]]
        assert all(x % 2 == 0 for row in tail for x in row)
        a = [[x//2 for x in row] for row in tail]
    return counts + [len(a)]

results = []
for d, dyadic, rho, p in CASES:
    assert d == 2*dyadic+rho and dyadic & (dyadic-1) == 0
    assert rho >= 4 and rho % 2 == 0 and d % 16 == 0
    assert 5 <= p and p+rho <= dyadic-2 and d+2*p <= 4*dyadic
    n, depth = d+2, d-p
    highest = 2*d+p+2
    theta = [1, 0]
    for r in range(1, highest):
        theta.append(((2*r+1)*theta[-1]+theta[-2]) % 8)
    pascal = [[1]]
    for r in range(1, highest+1):
        prev = pascal[-1]
        pascal.append([1]+[(prev[j-1]+prev[j]) % 8 for j in range(1, r)]+[1])
    filters = {}
    def krow(b, z):
        key = b, z
        if key not in filters:
            terms = [(t, c) for t, c in enumerate(pascal[b]) if c]
            filters[key] = [sum(c*pascal[r+z+t][r]*theta[r+z+t]
                                for t, c in terms) % 8 for r in range(d+1)]
        return filters[key]
    # The passed normalized top contact row is T_j/o_d=K_d(j) modulo8
    # at base0. Multiply the ENTIRE atom column by odd o_d. This is a
    # unit column operation, leaving literal rising ratios and zero bottom
    # atom coordinates. No integer original content is divided by o_d.
    ratios = [0]*p
    ratios[p-1] = 1
    for j in range(p-2, -1, -1):
        ratios[j] = ratios[j+1]*(d+j+1) % 8
    rows = [[(ratios[j]*(-1)**j) % 8] + krow(d, j) for j in range(p)]
    c2, c3, c4 = (math.comb(p, j) for j in (2, 3, 4))
    x1 = 2*d*p-p*(p+1)//2
    x2 = math.comb((p+1)//2, 2) % 2
    for z in range(depth+2):
        j = p+z
        terms = [(1, p, z), (2*(x1+p*j), p-1, z+1),
                 (-2*c2, p-2, z+1),
                 (4*(x2+j*(x1*(p-1)+c2)), p-2, z+2),
                 (4*(x1*math.comb(p-1, 2)+c3+j*c2*(p-2)), p-3, z+2),
                 (4*c4, p-4, z+2)]
        contacts = [0]*(d+1)
        for coefficient, b, shift in terms:
            coefficient %= 8
            if coefficient:
                kr = krow(b, shift)
                contacts = [(x+coefficient*y) % 8 for x, y in zip(contacts, kr)]
        rows.append([0]+contacts)
    assert len(rows) == n and all(len(row) == n for row in rows)
    rank = binary_rank(rows)
    expected_chi = dyadic-p-rho+1 if dyadic % 3 == 1 else p+rho+1
    assert n-rank == expected_chi
    counts = capped_module_counts(rows)
    assert counts[0] == rank and sum(counts) == n
    results.append({'d': d, 'L': dyadic, 'rho': rho, 'p': p,
                    'complete_dimension': n, 'parity_rank': rank,
                    'corank': n-rank, 'expected_corank': expected_chi,
                    'capped_invariant_counts_v0_v1_v2_vge3': counts,
                    'complete_mod4_effective_rank': counts[1],
                    'complete_next_mod8_effective_rank': counts[2],
                    'determinant_valuation_lower_at_capped_precision': sum(i*x for i, x in enumerate(counts)),
                    'matrix_mod8_sha256': hashlib.sha256(json.dumps(rows).encode()).hexdigest()})
receipt = {'scope': 'New auxiliary complete normalized MINIMAL theta matrices modulo8 only; not original indices, all-pattern/tied/paired upper or e+pi proof.',
           'coordinator_authored': True, 'network_and_credentials_denied_by_sandbox': True,
           'period_checks': periods, 'six_step_phase_checks': 4,
           'results': results, 'seconds': round(time.monotonic()-start, 3),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt))
