import sys, json
sys.path.insert(0, '[private local path removed]')
import sympy as sp
X, Y, z, x = sp.symbols('X Y z x')
def falling(t, m):
    return sp.prod(t-j for j in range(m))
def truncated(r):
    terms = []
    for c in range(2):
        for b in range(3):
            if b + 2*c < 3:
                terms.append((-1)**b * falling(X,b+2*c+r) * falling(X,b+c) / (sp.Integer(2)**c * sp.factorial(b) * sp.factorial(c)))
    return sp.expand(sum(terms))
def mod3_poly(expr):
    poly = sp.Poly(sp.expand(expr), Y, domain=sp.QQ)
    ans = 0
    for (degree,), coeff in poly.terms():
        numerator, denominator = coeff.as_numer_denom()
        assert int(denominator) % 3 != 0
        residue = (int(numerator) * pow(int(denominator) % 3, -1, 3)) % 3
        ans += residue * Y**degree
    return sp.expand(ans)
T = [truncated(r) for r in range(4)]
for r in range(4):
    assert sp.expand(T[r] - (falling(X,r) - X*falling(X,r+1) + X**2*falling(X,r+2)/2)) == 0
residues = [[mod3_poly(T[r].subs(X,a+3*Y)) for r in range(4)] for a in range(3)]
assert residues == [[1,0,0,0],[0,1,0,0],[1,1,2,0]]
H, U, V, W = T
J = X*H + U
K = X*(X-1)*H + 2*X*U + V
M = X*(X-1)*(X-2)*H + 3*X*(X-1)*U + 3*X*V + W
rows = [(H,J),(J,K),(K,M)]
B = sp.Matrix([[mod3_poly(entry.subs(X,a+3*Y)) for entry in row] for a,row in enumerate(rows)])
assert B == sp.Matrix([[1,0],[1,2],[2,0]])
minors = [mod3_poly(B.extract([i,j],[0,1]).det()) for i,j in [(0,1),(0,2),(1,2)]]
assert minors == [2,0,2]
original_H = []
for n in range(3):
    exponential_truncation = sum(x**j*z**j/sp.factorial(j) for j in range(n+1))
    hn = sp.expand(sp.factorial(n)*sp.expand(exponential_truncation*(1-z+z**2/2)**n).coeff(z,n))
    original_H.append(hn)
    for r in range(4):
        assert sp.diff(hn,x,r).subs(x,1) == T[r].subs(X,n)
assert original_H == [1,x-1,x**2-4*x+4]
print(json.dumps({'retained_polynomial_identities': True, 'derivative_residues_by_disk': [[int(v) for v in row] for row in residues], 'coefficientwise_matrix_mod3': [[int(B[i,j]) for j in range(2)] for i in range(3)], 'ordered_minors_mod3': [int(v) for v in minors], 'original_H_0_through_2': [str(v) for v in original_H], 'scope': 'Exact finite polynomial checks; infinite-tail divisibility is proved separately in the accompanying note.'}, indent=2))