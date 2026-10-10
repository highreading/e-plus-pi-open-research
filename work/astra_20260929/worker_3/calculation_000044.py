import json

def v2_nonzero(a):
    assert a != 0
    a = abs(a)
    return (a & -a).bit_length() - 1

def F(y):
    return 2*y*y + y - 3

pair_checks = 0
for x in range(-64, 65):
    for y in range(-64, 65):
        if x != y:
            assert v2_nonzero(F(x)-F(y)) == v2_nonzero(x-y)
            pair_checks += 1

K = 13
modulus = 1 << K
root_checks = []
roots = {}
assert [y for y in range(modulus) if F(y) % modulus == 0] == [1]
for M in range(1, 11):
    found = [y for y in range(modulus) if (F(y)+(1 << M)) % modulus == 0]
    assert len(found) == 1
    beta = found[0]
    assert v2_nonzero(beta-1) == M
    roots[M] = beta
    root_checks.append({'M': M, 'root_mod_8192': beta, 'difference_valuation': v2_nonzero(beta-1)})

disk_checks = []
N, h, r = 10, 3, 7
for s in (2, 3):
    M = N-s
    beta = roots[M]
    xi = r + (1 << h)
    xi_other = r + (1 << h)*beta
    assert v2_nonzero(xi_other-xi) == N-s+h
    assert (1 << s)*(1 << M) == (1 << N)
    disk_checks.append({'N': N, 's': s, 'h': h, 'exact_index_difference_valuation': v2_nonzero(xi_other-xi)})

factor_checks = 0
for m in range(-64, 65):
    if m not in (0, 1):
        for s in (2, 3):
            value = (1 << s)*m*F(m)
            assert v2_nonzero(value) == s+v2_nonzero(m)+v2_nonzero(m-1)
            factor_checks += 1

print(json.dumps({'status': 'finite author checks passed', 'valuation_pair_checks': pair_checks, 'root_checks': root_checks, 'disk_checks': disk_checks, 'extra_Y_factor_checks': factor_checks, 'scope': 'General polynomial examples only; not independent approval or project-germ verification.'}, indent=2))