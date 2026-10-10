from fractions import Fraction as Q
from math import factorial, comb
from functools import lru_cache
from pathlib import Path
import hashlib
import json

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/worker2-fixed-b-projection-and-error-transfer-v2.md'
raw = path.read_bytes()
payload = raw.split(b'\n\n', 2)[2]
expected = 'b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245'
assert hashlib.sha256(payload).hexdigest() == expected
identity = {'file_bytes': len(raw), 'file_sha256': hashlib.sha256(raw).hexdigest(), 'payload_offset': len(raw)-len(payload), 'payload_bytes': len(payload), 'payload_sha256': expected}

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [Q(0)]

def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)

def scale(a, c):
    return trim([c*x for x in a])

def mul(a, b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)

@lru_cache(None)
def moment(m):
    return sum((Q(2*comb(m, 2*r)*(-1)**r, 2**m*(2*r+1)) for r in range(m//2+1)), Q(0))

def L(a):
    return sum((x*moment(i) for i, x in enumerate(a)), Q(0))

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))

def det(a):
    size = len(a)
    if size == 0: return Q(1)
    a = [list(row) for row in a]
    value = Q(1)
    for j in range(size):
        pivot = next((i for i in range(j, size) if a[i][j]), None)
        if pivot is None: return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        pivot_value = a[j][j]
        value *= pivot_value
        for i in range(j+1, size):
            ratio = a[i][j]/pivot_value
            for k in range(j+1, size): a[i][k] -= ratio*a[j][k]
            a[i][j] = Q(0)
    return value

def rank(a):
    a = [list(row) for row in a]
    row_count = len(a)
    col_count = len(a[0]) if a else 0
    r = 0
    for j in range(col_count):
        pivot = next((i for i in range(r, row_count) if a[i][j]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        for i in range(r+1, row_count):
            ratio = a[i][j]/v
            for k in range(j, col_count): a[i][k] -= ratio*a[r][k]
        r += 1
        if r == row_count: break
    return r

max_n = 7
max_b = 3
p = [[Q(1)], [Q(-1, 2), Q(1)]]
for k in range(1, max_n+max_b):
    beta = Q(k*k, 4*(4*k*k-1))
    p.append(add(mul(p[k], [Q(-1, 2), Q(1)]), scale(p[k-1], beta)))
h = [Q(2*(-1)**k, (2*k+1)*comb(2*k,k)**2) for k in range(len(p))]
norm_checks = 0
for i in range(len(p)):
    for j in range(len(p)):
        assert L(mul(p[i], p[j])) == (h[i] if i == j else 0)
        norm_checks += 1

# v_k is represented exactly as its rational and pi coefficients.
v = []
for pk in p:
    quotient = [sum(pk[j+1:], Q(0)) for j in range(len(pk)-1)]
    v.append((-L(quotient), sum(pk, Q(0))))

records = []
for n in range(1, max_n+1):
    for b in range(1, min(max_b, n)+1):
        def ell(poly, j):
            return sum((a/Q(factorial(n+k+1-j)) for k, a in enumerate(poly)), Q(0))
        def ellrow(poly):
            return [ell(poly, j) for j in range(b+1)]
        V = [Q(0)]
        Hr = [Q(0)]
        Hp = [Q(0)]
        for k in range(n+1):
            V = add(V, scale(p[k], sum(p[k], Q(0))/h[k]))
            Hr = add(Hr, scale(p[k], v[k][0]/h[k]))
            Hp = add(Hp, scale(p[k], v[k][1]/h[k]))
        bn = sum(p[n+1], Q(0))/sum(p[n], Q(0))
        assert mul(V, [Q(-1), Q(1)]) == scale(add(p[n+1], scale(p[n], -bn)), sum(p[n], Q(0))/h[n])
        for c, H in enumerate((Hr, Hp)):
            lhs = add([Q(1) if c == 0 else Q(0)], scale(mul(H, [Q(1), Q(-1)]), -1))
            rhs = scale(add(scale(p[n+1], v[n][c]), scale(p[n], -v[n+1][c])), 1/h[n])
            assert lhs == rhs
        W0 = (1-Hr[0], -Hp[0])
        for c in range(2):
            eps_n = (-1)**n*v[n][c]/sum(p[n], Q(0))
            eps_next = (-1)**(n+1)*v[n+1][c]/sum(p[n+1], Q(0))
            assert W0[c]/V[0] == Q((-1)**(n+1), 2)*(eps_n-eps_next)

        high = [ellrow(p[n+l]) for l in range(1, b)]
        e = [Q(1)]*(b+1)
        vr = ellrow(V)
        M = high + [[1+x for x in vr]]
        B = [(-1)**(b+j)*det([row[:j]+row[j+1:] for row in M]) for j in range(b+1)]
        assert all(dot(row, B) == 0 for row in M)
        reduced_rank = rank(M)
        assert reduced_rank == b, ('finite reduced rank exception', n, b)
        Cstar = [Q(0)]
        for k in range(n+1):
            Cstar = add(Cstar, scale(p[k], -dot(B, ellrow(p[k]))/h[k]))
        Cstar += [Q(0)]*(n+1-len(Cstar))
        C = Cstar[::-1]
        Y = sum(B, Q(0))
        assert sum(C, Q(0)) == Y

        # Check every original high Taylor coefficient directly from moments.
        direct = []
        for k in range(n+1, 2*n+b+1):
            row = [Q(1, factorial(k-j)) for j in range(b+1)]
            row += [moment(k-j-1) for j in range(n+1)]
            direct.append(row)
            assert dot(row, B+C) == 0
        direct.append([Q(1)]*(b+1)+[Q(-1)]*(n+1))
        assert dot(direct[-1], B+C) == 0
        full_rank = rank(direct)
        assert full_rank == n+1+reduced_rank
        Aminus = []
        for k in range(n+1):
            value = sum((B[j]/factorial(k-j) for j in range(min(b,k)+1)), Q(0))
            value += sum((C[j]*moment(k-j-1) for j in range(k)), Q(0))
            Aminus.append(value)
        A1 = sum(Aminus, Q(0))

        # Complete tails are affine forms in 1, e, pi, handled separately.
        w_parts = [[], [], []]
        for j in range(b+1):
            partial_exp = sum((Q(1, factorial(k)) for k in range(n-j+1)), Q(0))
            w_parts[0].append(-partial_exp-ell(Hr, j))
            w_parts[1].append(Q(1))
            w_parts[2].append(-ell(Hp, j))
        complete_remainder = [dot(B, row) for row in w_parts]
        assert complete_remainder == [-A1, Y, Y]
        D = det(high+[e, vr])
        assert Y == -D
        for c in range(3):
            E = det(high+[e, w_parts[c]])
            T = det(high+[vr, w_parts[c]])
            assert E+T == complete_remainder[c]
        if Y:
            approximant = A1/Y
            assert [x/Y for x in complete_remainder] == [-approximant, Q(1), Q(1)]
            Aplus1 = -A1
            assert -Aplus1/Y == approximant
        else:
            approximant = None
        if n == b == 1:
            assert [x/B[0] for x in B] == [Q(1), Q(-1)]
            assert [x/B[0] for x in C] == [Q(-1,2), Q(1,2)]
            assert [x/B[0] for x in Aminus] == [Q(1), Q(-1)]
            assert Y == A1 == 0
        records.append({'n': n, 'b': b, 'reduced_rank': reduced_rank, 'full_rank': full_rank, 'Y_nonzero': bool(Y), 'approximant_for_minus_A_convention': str(approximant) if approximant is not None else None})

print(json.dumps({'identity': identity, 'orthogonality_checks': norm_checks, 'parameter_pairs_checked': len(records), 'all_exact_checks_passed': True, 'records': records}, indent=2))