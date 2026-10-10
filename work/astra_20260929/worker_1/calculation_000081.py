from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb
import hashlib, json

root = Path('[private local path removed]')
candidate = root / 'work/astra_review_registry/candidates/b2-five-adic-endpoint-denominator-v1.md'
raw = candidate.read_bytes()
expected = '01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81'
whole = hashlib.sha256(raw).hexdigest()
assert whole == '254d314904b76ad73535da2636129b5ab6a9664d1c55ccbb4d754262995c15b9'
start = raw.index(b'UNVERIFIED CANDIDATE. Author: worker_4.')
tail = raw[start:]
variants = {tail, tail.rstrip(b'\n')}
matched = [body for body in variants if hashlib.sha256(body).hexdigest() == expected]
assert len(matched) == 1, 'Exact registered payload was not identified'
print(json.dumps({'provenance': {'whole_file_sha256': whole, 'payload_sha256': expected, 'payload_start': start, 'payload_bytes': len(matched[0])}}))

def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def power_poly(a, m):
    out = [1]
    for _ in range(m):
        out = convolution(out, a)
    return out

def legendre_rodrigues(m):
    coeff = power_poly([1, -2, 2], m)
    return [comb(m+d, m)*coeff[m+d] for d in range(m+1)]

def auxiliary(m):
    coeff = power_poly([2, -2, 1], m)
    deriv = []
    for j in range(3):
        value = F(factorial(m), 2**m) * sum((F(coeff[k], factorial(m-j-k)) for k in range(m-j+1)), F(0))
        assert value.denominator == 1
        deriv.append(value.numerator)
    h, hp, hpp = deriv
    return h, m*h+hp, m*(m-1)*h+2*m*hp+hpp, deriv

def valuation(x):
    x = F(x)
    if x == 0:
        return None
    def integer_v(a):
        a = abs(a)
        count = 0
        while a % 5 == 0:
            count += 1
            a //= 5
        return count
    return integer_v(x.numerator)-integer_v(x.denominator)

def residue(x):
    x = F(x)
    assert x.denominator % 5 != 0
    return (x.numerator % 5)*pow(x.denominator, -1, 5) % 5

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

certificates = []
for n in (5, 10, 15, 25):
    fac = [factorial(j) for j in range(2*n+5)]
    E = []
    running = F(0)
    for value in fac:
        running += F(1, value)
        E.append(running)
    e = [fac[j]*E[j] for j in range(len(E))]
    assert all(value.denominator == 1 for value in e)
    moments = []
    real, imag = 1, 0
    for j in range(2*n+2):
        real, imag = real-imag, real+imag
        moments.append(F(2*imag, 2**j*(j+1)))
    P, U = legendre_rodrigues(n), legendre_rodrigues(n+1)
    a, b = sum(P), sum(U)
    k = (n+1)**2
    f = F(2**n, fac[n]**2)
    g = F(2**(n+1), fac[n+1]**2)
    G = F((-1)**n*2**(2*n+3), n+1)
    gamma = g*f/(G*k)
    assert gamma == F((-1)**n, 4*(n+1)**3*fac[n]**4)

    def ell(poly, j):
        return sum((F(c, fac[n+d+1-j]) for d, c in enumerate(poly)), F(0))
    def T(poly, j=0):
        return sum((c*E[n+d-j] for d, c in enumerate(poly)), F(0))
    def endpoint_moment(poly):
        quotient = [0]*(len(poly)-1)
        running = 0
        for d in range(len(poly)-2, -1, -1):
            running += poly[d+1]
            quotient[d] = running
        product = convolution(quotient, [-1, 1])
        target = list(poly)
        target[0] -= sum(poly)
        assert product == target
        return sum((c*moments[d] for d, c in enumerate(quotient)), F(0))

    wp, wu = endpoint_moment(P), endpoint_moment(U)
    tp, tu = T(P), T(U)
    assert a*wu-b*wp == G
    h, J, K, deriv_n = auxiliary(n)
    eta, J1, K1, deriv_next = auxiliary(n+1)
    S = J1*J1-eta*K1
    C = (J1-eta)*J-(K1-J1)*h
    W = J1*J-K1*h
    D = k*b*C-2*a*S
    X = 2*(wp+tp)*S-k*(wu+tu)*C-2*f*eta*W
    alpha = [ell(U, j) for j in range(3)]
    assert alpha == [g*eta, g*J1, g*K1]
    assert [ell(P, 1), ell(P, 2)] == [f*h, f*J]
    tau = [(a*T(U, j)-b*T(P, j))/G for j in range(3)]
    beta = cross(alpha, [1+x for x in tau])

    # Polynomial long division of the original two-variable numerator.
    width = 2*n+3
    ppad = P+[0]
    numerator = [[U[i]*ppad[j]-ppad[i]*U[j] for j in range(n+2)] + [0]*(width-n-2) for i in range(n+2)]
    quotient_rows = [None]*(n+1)
    previous = [0]*width
    for d in range(n, -1, -1):
        shifted = [0]+previous[:-1]
        row = [numerator[d+1][j]+shifted[j] for j in range(width)]
        assert all(c == 0 for c in row[n+1:])
        quotient_rows[d] = row[:n+1]
        previous = row
    assert all(numerator[0][j]+([0]+previous[:-1])[j] == 0 for j in range(width))
    kernel = [[F(c)/G for c in row] for row in quotient_rows]
    assert all(kernel[i][j] == kernel[j][i] for i in range(n+1) for j in range(n+1))
    for degree in range(n+1):
        reproduced = [sum((kernel[i][j]*moments[j+degree] for j in range(n+1)), F(0)) for i in range(n+1)]
        assert reproduced == [F(int(i == degree)) for i in range(n+1)]

    # Reconstruct the raw triple directly from its defining functionals.
    weights = [sum((beta[j]/fac[n+s+1-j] for j in range(3)), F(0)) for s in range(n+1)]
    Qraw = [-sum((kernel[i][s]*weights[s] for s in range(n+1)), F(0)) for i in range(n+1)]
    Craw = list(reversed(Qraw))
    exp_part = [sum((beta[j]/fac[degree-j] for j in range(min(2, degree)+1)), F(0)) for degree in range(2*n+3)]
    F_part = [sum((Craw[j]*moments[degree-j-1] for j in range(min(n, degree-1)+1)), F(0)) if degree else F(0) for degree in range(2*n+3)]
    Araw = [-exp_part[degree]-F_part[degree] for degree in range(n+1)]
    assert all(exp_part[degree]+F_part[degree] == 0 for degree in range(n+1, 2*n+3))
    Aend, Bend, Cend = sum(Araw), sum(beta), sum(Craw)
    assert Bend == Cend == gamma*D
    assert Aend == gamma*X
    assert Bend != 0 and Aend != 0
    ratio = Aend/Bend
    assert ratio == X/D

    r = valuation(fac[n])
    L, power = 0, 1
    while power*5 <= n:
        L += 1
        power *= 5
    assert [residue(x) for x in deriv_n] == [1, 0, 0]
    assert [residue(x) for x in deriv_next] == [0, 1, 0]
    assert [residue(x) for x in (S, C, W, k)] == [1, 4, 3, 1]
    assert a % 5 != 0 and (b-2*a) % 5 == 0 and (D-a) % 5 == 0
    boundary_p = e[2*n]
    boundary_u = -2*(2*n+1)*e[2*n]+F(4, n+1)*e[2*n+1]
    assert residue(tp/f-boundary_p) == 0
    assert residue(tu/f-boundary_u) == 0
    assert residue(tp/f) == residue(tu/f) == 1
    assert all(value == 0 or valuation(value) >= 2*r-L for value in (wp/f, wu/f))
    numerator_terms = [2*(wp+tp)*S/f, -k*(wu+tu)*C/f, -2*eta*W]
    assert sum(numerator_terms) == X/f
    assert [residue(value) for value in numerator_terms] == [2, 1, 0]
    assert residue(X/f) == 3
    assert (valuation(D), valuation(X), valuation(ratio.denominator)) == (0, -2*r, 2*r)
    assert (valuation(Aend), valuation(Bend)) == (-6*r, -4*r)
    digit_sum, temp = 0, n
    while temp:
        digit_sum += temp % 5
        temp //= 5
    assert 2*r == (n-digit_sum)//2 and (n-digit_sum) % 2 == 0
    cert = {'n': n, 'r': r, 'moment_loss_bound_L': L, 'D_mod5': residue(D), 'X_over_f_mod5': residue(X/f), 'v5_D': valuation(D), 'v5_X': valuation(X), 'v5_q': valuation(ratio.denominator), 'v5_raw_A_endpoint': valuation(Aend), 'v5_raw_B_endpoint': valuation(Bend), 'v5_normalized_moments': [valuation(wp/f), valuation(wu/f)], 'complete_numerator_term_residues': [residue(value) for value in numerator_terms], 'reduced_numerator': str(ratio.numerator), 'reduced_denominator': str(ratio.denominator), 'kernel_reproduction_through_degree': n, 'remainder_coefficients_zero_through_degree': 2*n+2}
    certificates.append(cert)
    print(json.dumps(cert))
print(json.dumps({'status': 'all exact assertions passed', 'indices': [c['n'] for c in certificates], 'scope': 'Independent finite reconstruction and provenance; the all-index theorem requires the separate derivation audit.'}))