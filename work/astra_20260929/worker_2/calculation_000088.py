from pathlib import Path
import hashlib, json, math, sys
sys.path.insert(0, '[private local path removed]')
import sympy as sp
import mpmath as mp

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/w3-cofactor-leading-v1.md'
data = path.read_bytes()
target = 'bd4dd231d066a28039e75fa399678b6eb7f2c6f1f431ca3771acddfe23f86c9b'
offsets = [0]
for line in data.splitlines(keepends=True):
    offsets.append(offsets[-1] + len(line))
matches = [i for i in offsets if hashlib.sha256(data[i:]).hexdigest() == target]
assert len(matches) == 1, matches
assert hashlib.sha256(data).hexdigest() == '0ac218f38ae392b1d390ad64b9019a8e640252e3028460095010ea6d11f5ba0a'
source_hashes = {
    'work/astra_20260929/worker_3/note_000064.md': '16a6c2a4ddceb23cfdb52a358a7c9d57c4482f7125550305cd0194c830d8feb',
    'work/astra_20260929/worker_3/note_000066.md': '48784ca3819cfa40e7304005a3fc8c77b5534890ae02a7683a014d33d7832101'
}
# Verify the exact ledger hash for note 64 (kept separately to avoid transcription ambiguity).
source_hashes['work/astra_20260929/worker_3/note_000064.md'] = '16a6c2a4ddceb23cfdb52a358a7e6a0f1e51029921ef4469817fe062b1' if False else '16a6c2a4ddceb23cfdb52a358a7c9d57c4482f7125550305cd0194ac830d8feb'
for rel, expected in source_hashes.items():
    actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
    assert actual == expected, (rel, actual, expected)

# Independently check the difference-kernel alternant's leading homogeneous part.
alternant_checks = []
for d in range(1, 5):
    ys = sp.symbols('y0:' + str(d))
    def falling(y, j):
        return sp.prod(y-h for h in range(j))
    mat = sp.Matrix([[falling(y, j+1)-falling(y, j) for j in range(d)] for y in ys])
    determinant = sp.expand(mat.det(method='domain-ge'))
    vand = sp.prod(ys[j]-ys[i] for i in range(d) for j in range(i+1,d))
    quotient, remainder = sp.div(determinant, sp.expand(vand), *ys)
    assert remainder == 0
    poly = sp.Poly(quotient, *ys)
    assert poly.total_degree() == d
    top = sum(coef*sp.prod(y**power for y,power in zip(ys,mon)) for mon,coef in poly.terms() if sum(mon) == d)
    assert sp.expand(top-sp.prod(ys)) == 0
    alternant_checks.append({'d':d, 'quotient_degree':poly.total_degree(), 'top_part_verified':True})

# Exact coefficient determinants, preserving the stated row order; b=1 has no polynomial rows.
A = sp.symbols('A', nonzero=True)
rt2 = sp.sqrt(2)
coefficient_checks = []
for b in range(1, 6):
    polynomial_rows = [[sp.binomial(i,r) for r in range(b+1)] for i in range(b-1)]
    vrow = [(-1/A)**r for r in range(b+1)]
    wrow = [(-sp.Rational(1,2))**r for r in range(b+1)]
    en_x = sp.factor(sp.Matrix(polynomial_rows+[vrow,wrow]).det(method='domain-ge'))
    ev_x = sp.factor(sp.Matrix([row[:b] for row in polynomial_rows+[vrow]]).det(method='domain-ge'))
    assert sp.cancel(en_x-(2-A)/(2**b*A**b)) == 0
    assert sp.cancel(ev_x-(-1)**(b-1)/A**(b-1)) == 0
    ratio = sp.simplify(((-rt2)**b*en_x/ev_x).subs(A,2*rt2-2))
    expected = -sp.Integer(2)**sp.Rational(1-b,2)
    assert sp.simplify(ratio-expected) == 0
    if b == 1:
        assert sp.simplify(((-rt2)*en_x).subs(A,2*rt2-2)+1) == 0
    coefficient_checks.append({'b':b,'E_N_over_E_V':str(ratio)})

# Supplementary numerical checks of the abstract theorem on an independently chosen polynomial family.
# This is NOT reconstruction of the project's endpoint polynomials and is NOT an asymptotic proof.
mp.mp.dps = 100
c = mp.sqrt(2)
a = 2*c-2

def multiply(left,right):
    out = [mp.mpf('0')]*(len(left)+len(right)-1)
    for i,u in enumerate(left):
        for j,v in enumerate(right):
            out[i+j] += u*v
    return out

def scaled_functionals(poly,n,columns):
    # Return n! T_j(poly), without forming huge factorials.
    weights = []
    w = mp.mpf(1)/(n+1)
    for m in range(len(poly)):
        weights.append(w)
        w /= n+m+2
    values = []
    for j in range(columns):
        total = mp.mpf('0')
        for m,coef in enumerate(poly):
            y = n+m+1
            falling_value = mp.mpf(1)
            for h in range(j):
                falling_value *= y-h
            total += coef*weights[m]*falling_value
        values.append(total)
    return values

numerics = []
for b in (1,2,3):
    for n in (40,80,160):
        F = [mp.mpf(1)]
        for k in range(n):
            F.append(F[-1]*(-c)*(n-k)/(k+1))
        L = b+4
        G = [[mp.mpf(math.comb(i,r))*(-c)**r for r in range(i+1)] for i in range(b-1)]
        G += [[(c/a)**r for r in range(L+1)], [(c/2)**r for r in range(L+1)]]
        rows = [scaled_functionals(multiply(F,g),n,b+1) for g in G]
        numerator = mp.det(mp.matrix(rows))
        difference_rows = [[row[j+1]-row[j] for j in range(b)] for row in rows[:-1]]
        denominator = (-1)**(b+1)*mp.det(mp.matrix(difference_rows))
        normalized = mp.mpf(n)**(2*b+1)*numerator/denominator
        predicted = (-1)**b*math.factorial(b)*mp.power(2,mp.mpf(1-b)/2)*mp.exp(-c)
        numerics.append({'b':b,'n':n,'normalized':mp.nstr(normalized,22),'predicted_limit':mp.nstr(predicted,22),'ratio_to_limit':mp.nstr(normalized/predicted,16)})

print(json.dumps({'integrity':{'payload_start':matches[0],'payload_end':len(data),'payload_sha256':target,'source_hashes_match':True},'difference_alternant_checks':alternant_checks,'exact_coefficient_determinants':coefficient_checks,'synthetic_polynomial_family_only':numerics},indent=2))