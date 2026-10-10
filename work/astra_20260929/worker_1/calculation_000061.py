from fractions import Fraction as Q
from math import factorial, comb, gcd
import json

indices = (3, 6, 9, 12)
limit = max(indices) + 2

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

# Construct Legendre transforms from their three-term recurrence.
L = [[1], [-2, 4]]
for m in range(1, limit):
    top = [0] * (m+2)
    for j, c in enumerate(L[m]):
        top[j] -= 2*(2*m+1)*c
        top[j+1] += 4*(2*m+1)*c
    for j, c in enumerate(L[m-1]):
        top[j] += 4*m*c
    assert all(c % (m+1) == 0 for c in top)
    L.append([c // (m+1) for c in top])

def falling(m, r):
    return factorial(m) // factorial(m-r) if m >= r else 0

# Independently expand the defining generating polynomial for H_m.
H = []
transforms = []
for m in range(limit+1):
    power = [1]
    for _ in range(m):
        power = mul(power, [2, -2, 1])
    hp = [Q(factorial(m)*power[m-r], 2**m*factorial(r)) for r in range(m+1)]
    assert all(c.denominator == 1 for c in hp)
    hp = [int(c) for c in hp]
    H.append(hp)
    # Derivatives of x^m H_m(x) at x=1 give H,J,K,M.
    transforms.append(tuple(sum(c*falling(m+r, d) for r, c in enumerate(hp)) for d in range(4)))
    # Check Rodrigues' transform identity coefficient by coefficient.
    factor = Q(2**m, factorial(m)**2)
    for r in range(m+1):
        assert Q(L[m][r], factorial(m+r)) == factor*hp[r]

max_degree = 2*max(indices)+2
moments = [Q(2, 2**d)*sum((Q(comb(d,j)*(-1)**(j//2), j+1) for j in range(0,d+1,2)), Q(0)) for d in range(max_degree+1)]
E = []
s = Q(0)
for d in range(max_degree+1):
    s += Q(1, factorial(d))
    E.append(s)

def second_kind(poly):
    # (Q(t)-Q(1))/(t-1) has coefficient sum_{k>j} Q_k at t^j.
    quotient = [sum(poly[j+1:]) for j in range(len(poly)-1)]
    recovered = mul(quotient, [-1,1])
    target = list(poly)
    target[0] -= sum(poly)
    assert recovered == target
    return sum((c*moments[j] for j,c in enumerate(quotient)), Q(0))

def valuation(x, p=3):
    x = Q(x)
    if x == 0:
        return 'infinity'
    a, b = abs(x.numerator), x.denominator
    value = 0
    while a % p == 0:
        a //= p
        value += 1
    while b % p == 0:
        b //= p
        value -= 1
    return value

def solve_square(matrix, rhs):
    size = len(rhs)
    assert len(matrix) == size and all(len(row) == size for row in matrix)
    aug = [[Q(v) for v in row] + [Q(b)] for row,b in zip(matrix,rhs)]
    for col in range(size):
        pivot = next((r for r in range(col,size) if aug[r][col]), None)
        assert pivot is not None, 'Singular normalized defining system'
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v/scale for v in aug[col]]
        for r in range(size):
            if r != col and aug[r][col]:
                scale = aug[r][col]
                aug[r] = [u-scale*v for u,v in zip(aug[r],aug[col])]
    result = [aug[r][-1] for r in range(size)]
    assert all(sum((Q(a)*x for a,x in zip(row,result)),Q(0)) == Q(b) for row,b in zip(matrix,rhs))
    return result

records = []
for n in indices:
    P, U = L[n], L[n+1]
    a, b = sum(P), sum(U)
    wp, wu = second_kind(P), second_kind(U)
    G = Q((-1)**n * 2**(2*n+3), n+1)
    assert a*wu-b*wp == G
    def T(poly, j=0):
        return sum((Q(c)*E[n+d-j] for d,c in enumerate(poly)), Q(0))
    tp, tu = T(P), T(U)
    hn, jn, kn, mn = transforms[n]
    eta, j1, k1, m1 = transforms[n+1]
    h2, j2, k2, m2 = transforms[n+2]
    S = j1*j1-eta*k1
    C = (j1-eta)*jn-(k1-j1)*hn
    W = j1*jn-k1*hn
    k = (n+1)**2
    f = Q(2**n, factorial(n)**2)
    g = Q(2**(n+1), factorial(n+1)**2)
    assert g == 2*f/k
    D = k*b*C-2*a*S
    terms = (2*(wp+tp)*S, -k*(wu+tu)*C, -2*f*eta*W)
    X = sum(terms,Q(0))
    assert D != 0 and X != 0
    ratio = X/D
    q = ratio.denominator
    assert gcd(abs(ratio.numerator),q) == 1
    vx, vd, vq = valuation(X), valuation(D), valuation(q)
    assert vq == max(0,vd-vx)
    lam = 2**(n+1)*factorial(2*n+2)*factorial(n)**2
    N = lam*X
    assert N.denominator == 1
    assert abs(lam*D)//gcd(abs(lam*D),abs(N.numerator)) == q

    # Direct endpoint determinants, evaluated independently of S,C,W.
    av = [sum((Q(c,factorial(n+d+1-j)) for d,c in enumerate(U)),Q(0)) for j in range(3)]
    tv = [(a*T(U,j)-b*T(P,j))/G for j in range(3)]
    xv = [(wp*T(U,j)-wu*T(P,j))/G for j in range(3)]
    ev = [1+t for t in tv]
    beta = [av[1]*ev[2]-av[2]*ev[1], av[2]*ev[0]-av[0]*ev[2], av[0]*ev[1]-av[1]*ev[0]]
    yraw = sum(beta,Q(0))
    xraw = sum((bb*xx for bb,xx in zip(beta,xv)),Q(0))
    alpha = g*f/(G*k)
    assert yraw == alpha*D and xraw == alpha*X
    assert xraw/yraw == ratio

    # Independent rational solution of the defining approximation equations.
    def ef(degree):
        return Q(1,factorial(degree)) if degree >= 0 else Q(0)
    def ff(degree):
        return moments[degree-1] if degree >= 1 else Q(0)
    matrix, rhs = [], []
    for degree in range(n+1,2*n+3):
        matrix.append([ef(degree-j) for j in range(3)] + [ff(degree-j) for j in range(n+1)])
        rhs.append(0)
    matrix.append([-1]*3+[1]*(n+1))
    rhs.append(0)
    matrix.append([1]*3+[0]*(n+1))
    rhs.append(1)
    solution = solve_square(matrix,rhs)
    bp, cp = solution[:3], solution[3:]
    assert sum(bp) == sum(cp) == 1
    def other_coefficient(degree):
        return sum((bp[j]*ef(degree-j) for j in range(3)),Q(0)) + sum((cp[j]*ff(degree-j) for j in range(n+1)),Q(0))
    ap = [-other_coefficient(degree) for degree in range(n+1)]
    assert all((ap[degree] if degree <= n else Q(0))+other_coefficient(degree) == 0 for degree in range(2*n+3))
    assert sum(ap) == ratio

    matrix_aux = [(hn,jn),(j1,k1),(k2,m2)]
    minors = [matrix_aux[i][0]*matrix_aux[j][1]-matrix_aux[i][1]*matrix_aux[j][0] for i,j in ((0,1),(0,2),(1,2))]
    assert [[z%3 for z in row] for row in matrix_aux] == [[1,0],[1,2],[2,0]]
    assert [z%3 for z in minors] == [2,0,2]
    records.append({
        'n':n, 'L_endpoint_pair':[a,b], 'HJK_n':[hn,jn,kn], 'HJK_n_plus_1':[eta,j1,k1],
        'S':S, 'C':C, 'W':W, 'f':str(f),
        'w_P':str(wp), 'w_U':str(wu), 'T_P':str(tp), 'T_U':str(tu),
        'complete_X_terms':[str(z) for z in terms], 'term_v3':[valuation(z) for z in terms],
        'X':str(X), 'D':D, 'reduced_fraction':str(ratio),
        'reduced_numerator':ratio.numerator, 'q':q,
        'v3_X':vx, 'v3_D':vd, 'v3_q':vq, 'q_is_3adic_unit':vq==0,
        'auxiliary_matrix_mod3':[[z%3 for z in row] for row in matrix_aux],
        'auxiliary_minors':minors, 'auxiliary_minors_mod3':[z%3 for z in minors],
        'checks':{'wronskian':True,'rodrigues_transform':True,'complete_endpoint_determinants':True,'integral_gcd_reduction':True,'direct_defining_system_and_residual':True,'direct_reduced_denominator_valuation':True}
    })
print(json.dumps({'status':'all exact checks passed','definitions':'X and D are the scaled endpoint pair of original equations (9)-(10); q=den(X/D).','records':records,'scope':'Only n=3,6,9,12. No general denominator bound or irrationality conclusion.'},indent=2))