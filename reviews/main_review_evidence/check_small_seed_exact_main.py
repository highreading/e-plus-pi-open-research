"""Finite exact main checks of fixed seeds; stdlib only, no original execution."""
from pathlib import Path
from math import comb, factorial as fac, gcd
from functools import reduce
from itertools import permutations
import ast
import hashlib
import json

BASE = Path(__file__).resolve().parent
ROOT = Path('work/session_20260913')


def falling(n, h):
    out = 1
    for i in range(h):
        out *= n - i
    return out


def choose(n, h):
    return comb(n, h) if n >= 0 else (-1) ** h * comb(h - n - 1, h)


def bareiss(matrix):
    a = [list(r) for r in matrix]
    n = len(a)
    if not n:
        return 1
    sign, previous = 1, 1
    for k in range(n - 1):
        r = next((i for i in range(k, n) if a[i][k]), None)
        if r is None:
            return 0
        if r != k:
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                assert value % previous == 0
                a[i][j] = value // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def integer_augmented(degrees, b):
    a = [sum(choose(b, h) * falling(d, 2 * h) for h in range(d // 2 + 1)) for d in range(max(degrees) + 1)]
    m = [[falling(d, j) * a[d - j] if d >= j else 0 for j in range(len(degrees))] for d in degrees]
    vand = 1
    for i, x in enumerate(degrees):
        for y in degrees[i + 1:]:
            vand *= y - x
    det = bareiss(m)
    assert det % vand == 0
    return det // vand


def plus(a, b, sign=1):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += sign * v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def times(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return plus(out, [0])


def polynomial_augmented(degrees, b):
    matrix = []
    for d in degrees:
        row = []
        for j in range(len(degrees)):
            poly = [0] * (d + 1)
            for h in range(d // 2 + 1):
                if d - 2 * h >= j:
                    poly[d - 2 * h - j] += choose(b, h) * falling(d, 2 * h) * falling(d - 2 * h, j)
            row.append(plus(poly, [0]))
        matrix.append(row)
    out = [0]
    for perm in permutations(range(len(degrees))):
        term = [1]
        for i, j in enumerate(perm):
            term = times(term, matrix[i][j])
        inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
        out = plus(out, term, (-1) ** inversions)
    vand = 1
    for i, x in enumerate(degrees):
        for y in degrees[i + 1:]:
            vand *= y - x
    assert all(x % vand == 0 for x in out)
    return [x // vand for x in out]


def literal_polynomial(expression):
    # Parses a restricted data grammar; no eval/exec or calls/attributes.
    assert len(expression) < 1000
    def walk(node):
        if isinstance(node, ast.Name):
            assert node.id == 'x'
            return [0, 1]
        if isinstance(node, ast.Constant):
            assert type(node.value) is int
            return [node.value]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            sign = -1 if isinstance(node.op, ast.USub) else 1
            return [sign * x for x in walk(node.operand)]
        assert isinstance(node, ast.BinOp)
        if isinstance(node.op, ast.Pow):
            assert isinstance(node.right, ast.Constant) and type(node.right.value) is int and 0 <= node.right.value <= 20
            out, a = [1], walk(node.left)
            for _ in range(node.right.value):
                out = times(out, a)
            return out
        a, b = walk(node.left), walk(node.right)
        if isinstance(node.op, ast.Add):
            return plus(a, b)
        if isinstance(node.op, ast.Sub):
            return plus(a, b, -1)
        assert isinstance(node.op, ast.Mult)
        return times(a, b)
    return walk(ast.parse(expression, mode='eval').body)


small_name = 'small_residue_exact_seeds.json'
small_raw = (ROOT / small_name).read_bytes()
assert hashlib.sha256(small_raw).hexdigest() == 'a73ac4e2e7ccd53f906dfa24127bd843edc53f0f26b3431a2d66b36722db4d4d'
small = json.loads(small_raw)['seeds']
main = {r['n']: r for r in json.loads((BASE / 'RAW_PRIMITIVE_DUAL_NORMALIZATION_MAIN_CONTROL.json').read_text())['rows']}
positive_rows = []
for old in small:
    k = old['k']
    if k == 0:
        assert (old['MD'], old['M'], old['b'], old['V'], old['V1'], old['Pe1']) == (1, [1], [1], [1], 1, 1)
        positive_rows.append({'k': 0, 'all_exact_values_checked': True})
        continue
    degrees = list(range(k, 2 * k + 1))
    md = integer_augmented(degrees, k)
    ms = [integer_augmented([d for d in degrees if d != 2 * k - j], k) for j in range(k + 1)]
    assert (md, ms) == (old['MD'], old['M'])
    b = [(-1) ** (k - j) * comb(k, j) * ms[k - j] for j in range(k + 1)]
    content = reduce(gcd, b)
    b = [x // content for x in b]
    assert b == old['b']
    row = main[k]
    sign = 1 if sum(row['V']) * md > 0 else -1
    assert [sign * x for x in row['V']] == old['V']
    assert sum(old['V']) == old['V1'] == md // content
    assert [sign * row['U'][j] // fac(k + j) for j in range(k + 1)] == b
    border = [sum(comb(k + s, s) * falling(k + j, s) for s in range(k + j + 1)) for j in range(k + 1)]
    pe = sum(x * y for x, y in zip(old['V'], border))
    assert pe == old['Pe1']
    for name, number in [('MD_factors', md), ('Pe_factors', pe)]:
        product = 1
        for factor, power in old[name].items():
            product *= int(factor) ** power
        assert product == abs(number)
    positive_rows.append({'k': k, 'MD': md, 'M': ms, 'all_exact_values_checked': True})

negative_name = 'raw_negative_residue_fixed_seed_checks.json'
negative_raw = (ROOT / negative_name).read_bytes()
assert hashlib.sha256(negative_raw).hexdigest() == '4dba72a008c4b1b152b6c63d244cd4e4c5c9dd49e70efaf189e3079eafb5d023'
negative_rows = []
for old in json.loads(negative_raw)['results']:
    k, b = old['k'], old['background']
    assert k in (1, 2) and b == -k - 1
    degrees = list(range(k, 2 * k + 1))
    dpoly = polynomial_augmented(degrees, b)
    cpoly = [polynomial_augmented([d for d in degrees if d != k + i], b) for i in range(k + 1)]
    assert dpoly == literal_polynomial(old['D_polynomial'])
    assert cpoly == [literal_polynomial(s) for s in old['C_polynomials']]
    d, c = sum(dpoly), [sum(poly) for poly in cpoly]
    jets = [fac(h) * sum((-1) ** (k - i) * choose(b + i, i - h)
                        * sum(choose(b, u) * falling(b + i + 2 * u, 2 * u)
                              * choose(b, i + 2 * u) * c[i + 2 * u]
                              for u in range((k - i) // 2 + 1))
                        for i in range(h, k + 1)) for h in range(k + 1)]
    border = [sum((-1) ** s * comb(k, s) * comb(s, h) * falling(b, s - h) for s in range(h, k + 1)) for h in range(k + 1)]
    e = sum(x * y for x, y in zip(jets, border))
    assert (d, c, jets, border, e) == (old['D_at_one'], old['C_at_one'], old['J'], old['A'], old['E'])
    assert jets[0] == d and all(old['checks'].values())
    negative_rows.append({'k': k, 'D_polynomial_coefficients': dpoly, 'C_polynomial_coefficients': cpoly,
                          'D': d, 'C': c, 'J': jets, 'A': border, 'E': e, 'all_exact_values_checked': True})
out = {'reviewer': 'main Codex', 'finite_control_only': True, 'all_controls_passed': True,
       'original_code_executed': False, 'original_data_modified': False,
       'positive_fixed_degrees': [0, 6], 'negative_fixed_degrees': [1, 2],
       'factorization_products_checked': True, 'large_factor_primality_not_checked': True,
       'positive': positive_rows, 'negative': negative_rows}
(BASE / 'RAW_SMALL_EXACT_SEED_MAIN_CONTROL.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in ('positive', 'negative')}, ensure_ascii=False))
