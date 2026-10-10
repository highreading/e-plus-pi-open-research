"""NEW fixed auxiliary check; raw integer differences, no network or keys.

This verifies only d=16,48,80. It is not an original-sized calculation,
a repeated closed receipt, or evidence of a global terminal upper.
"""
from pathlib import Path
import datetime, functools, hashlib, json, math, time

HERE = Path(__file__).resolve().parent
started = time.monotonic()
results = []

def differences(values, order):
    values = list(values)
    for _ in range(order):
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return values

def v2(value):
    assert value > 0
    return (value & -value).bit_length() - 1

for d in (16, 48, 80):
    assert v2(d) == 4
    limit = 3 * d + 1
    all_a = [1]
    for index in range(1, 2 * limit + 1):
        all_a.append(1 - index * all_a[-1])
    u = all_a[::2]
    assert len(u) == limit + 1
    theta = [1, 0]
    for index in range(1, limit):
        theta.append((2 * index + 1) * theta[-1] + theta[-2])
    assert len(theta) == limit + 1
    alpha = 2 * d - d.bit_count()
    od = math.factorial(d) >> (d - d.bit_count())
    inv_od4 = pow(od % 4, -1, 4)
    physical_top = [math.prod(2 * n + 2 * h + 1 for h in range(d))
                    for n in range(2 * d)]
    atom = differences([physical_top[n] * (-1) ** n for n in range(2 * d)], d)
    assert all(value % (1 << d) == 0 for value in atom)
    atom = [value // (1 << d) for value in atom]
    max_j = min(d // 3 + 1, 28)
    rising = [1]
    for j in range(1, max_j + 1):
        rising.append(rising[-1] * (d + j))
    atom_jets = {}
    for j in range(max_j + 1):
        raw = differences(atom, j)
        assert all(value % (1 << j) == 0 for value in raw)
        atom_jets[j] = [value // (1 << j) for value in raw]
    top = {}
    physical_theta = {}
    delta_u = list(u)
    for r in range(d + 1):
        dr = (1 << r) * math.factorial(r)
        assert delta_u[0] % dr == 0 and delta_u[0] // dr == theta[r]
        raw_theta = delta_u[d:2 * d + 2]
        assert len(raw_theta) == d + 2
        assert all(value % dr == 0 for value in raw_theta)
        physical_theta[r] = [value // dr for value in raw_theta]
        products = [physical_top[n] * delta_u[n] for n in range(2 * d)]
        raw = differences(products, d)
        divisor = (1 << alpha) * dr
        assert all(value % divisor == 0 for value in raw)
        source = [value // divisor for value in raw]
        for j in range(max_j + 1):
            source_j = differences(source, j)
            denominator = (1 << j) * rising[j]
            assert all(value % denominator == 0 for value in source_j)
            top[j, r] = [value // denominator for value in source_j]
        delta_u = differences(delta_u, 1)

    @functools.lru_cache(None)
    def kernel(b, z, r):
        assert b >= 0 and z >= 0 and r + z + b <= limit
        return sum(math.comb(b, t) * math.comb(r + z + t, r)
                   * (theta[r + z + t] % 4) for t in range(b + 1)) % 4

    counts = {'top_entries': 0, 'atom_entries': 0, 'bottom_entries': 0,
              'two_complete_second_even_rows': 0, 'configurations': 0}
    tested_p = sorted({5, 6, 7, 8, 10, d // 4, d // 3} & set(range(5, d // 3 + 1)))
    for p in tested_p:
        a = d - p
        gap = d - p
        for base in (0, a):
            for j in range(p + 1):
                if base + j > d - 1:
                    continue
                assert atom_jets[j][base] % 4 == (-1) ** (base + j) % 4
                counts['atom_entries'] += 1
                for r in range(d + 1):
                    prediction = od * (kernel(d, j, r)
                                       + 2 * base * (j + 1) * kernel(d, j + 1, r)) % 4
                    assert top[j, r][base] % 4 == prediction, (d, p, base, j, r, 'top')
                    counts['top_entries'] += 1
        for I in (tuple(range(a, d)), (a - 1,) + tuple(range(a + 1, d))):
            assert len(I) == p and min(I) >= 0
            pole_sum = sum(d + t for t in I) % 2
            beta = (pole_sum + p + math.comb(p, 2)) % 2
            qvalues = [math.prod(2 * (d + i + t) + 1 for t in I)
                       for i in range(d + 2)]
            bottom = [[0] * (d + 2) for _ in range(gap + 2)]
            for r in range(d + 1):
                qtheta = [qvalues[i] * physical_theta[r][i] for i in range(d + 2)]
                for j in range(p, d + 2):
                    value = differences(qtheta, j)[0]
                    den = (1 << j) * math.factorial(j)
                    assert value % den == 0
                    actual = value // den
                    z = j - p
                    prediction = (kernel(p, z, r)
                                  + 2 * (pole_sum + p * j) * kernel(p - 1, z + 1, r)
                                  + 2 * math.comb(p, 2) * kernel(p - 2, z + 1, r)) % 4
                    assert actual % 4 == prediction, (d, p, I, j, r, 'bottom')
                    bottom[z][r + 1] = actual % 4
                    counts['bottom_entries'] += 1
            for base in (0, a):
                for orders in (tuple(range(p)), tuple(range(p - 1)) + (p,)):
                    if base + max(orders) > d - 1:
                        continue
                    largest = max(orders)
                    assert v2(rising[largest]) >= 3
                    for j in (0, 1):
                        atom_entry = rising[largest] // rising[j] * atom_jets[j][base]
                        full_top = [(atom_entry * inv_od4) % 4]
                        full_top += [(top[j, r][base] * inv_od4) % 4 for r in range(d + 1)]
                        coefficients = [0] * (gap + 2)
                        terms = [(base * (j + 1), gap, j + 1),
                                 (-(p * j + beta), gap - 1, j + 1),
                                 (-(p * gap + math.comb(p, 2)), gap - 2, j + 2)]
                        for coefficient, exponent, shift in terms:
                            if coefficient % 2 == 0:
                                continue
                            assert shift + exponent <= gap + 1
                            for t in range(exponent + 1):
                                coefficients[shift + t] ^= math.comb(exponent, t) % 2
                        for column in range(d + 2):
                            first = full_top[column] - sum(math.comb(gap, t)
                                        * bottom[j + t][column] for t in range(gap + 1))
                            assert first % 2 == 0
                            second = first - 2 * sum(coefficients[z] * bottom[z][column]
                                                   for z in range(gap + 2))
                            assert second % 4 == 0, (d, p, base, j, column, 'second even')
                            counts['two_complete_second_even_rows'] += 1
                    counts['configurations'] += 1
    results.append({'auxiliary_d': d, 'tested_p': tested_p, 'counts': counts, 'status': 'PASS',
                    'scope': 'Raw complete finite source and mixed jets; auxiliary parameters only'})
    kernel.cache_clear()
    print(json.dumps(results[-1]), flush=True)

out = {'time': datetime.datetime.now().astimezone().isoformat(),
       'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'seconds': round(time.monotonic() - started, 3), 'results': results,
       'network_used': False, 'credential_read': False, 'original_sized_solve': False,
       'repeated_closed_calculation': False, 'global_proof_or_valuation_upper': False}
(HERE / 'THETA_FIRST_LIFT_RAW_AUXILIARY_RECEIPT.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'seconds': out['seconds'], 'receipt': 'THETA_FIRST_LIFT_RAW_AUXILIARY_RECEIPT.json'}))
