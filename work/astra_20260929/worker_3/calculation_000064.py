from fractions import Fraction as Q
from math import comb
import sys
sys.path.insert(0, '[private local path removed]')
import mpmath as mp
mp.mp.dps = 240

# Reconstruct the original monic polynomials with exact rational arithmetic.
indices = [8, 16, 32, 64]
max_b = 3
max_degree = max(indices) + max_b - 1
polys = [[Q(1)], [Q(-1, 2), Q(1)]]
for m in range(1, max_degree):
    nxt = [Q(0)] * (m + 2)
    for r, coefficient in enumerate(polys[m]):
        nxt[r] -= coefficient / 2
        nxt[r + 1] += coefficient
    beta = Q(m*m, 4*(4*m*m-1))
    for r, coefficient in enumerate(polys[m-1]):
        nxt[r] += beta * coefficient
    polys.append(nxt)

# Exact moments mu_r = 4 Im(((1+i)/2)^(r+1))/(r+1).
z_real, z_imag = Q(1), Q(0)
moment_prefix = [Q(0)]
for r in range(max_degree + 1):
    z_real, z_imag = (z_real-z_imag)/2, (z_real+z_imag)/2
    moment_prefix.append(moment_prefix[-1] + 4*z_imag/(r+1))

def real(q):
    return mp.mpf(q.numerator) / q.denominator

endpoints = [sum(p, Q(0)) for p in polys]
norms = [Q(2*(-1)**k, (2*k+1)*comb(2*k,k)**2) for k in range(len(polys))]
# chi_k = pi*p_k(1) minus an exactly reconstructed rational number.
chi_rational = [-sum((p[r]*moment_prefix[r] for r in range(1,len(p))), Q(0)) for p in polys]
chi = [mp.pi*real(endpoints[k]) + real(chi_rational[k]) for k in range(len(polys))]
polys_mp = [[real(q) for q in p] for p in polys]

c = mp.sqrt(2)
rho = 1+c
s = rho**(-2)
A = 1-s
maximum_identity_error = mp.mpf(0)
results = []

for n in indices:
    V = [mp.mpf(0)]*(n+1)
    projection = [mp.mpf(0)]*(n+1)
    for k in range(n+1):
        v_multiplier = real(endpoints[k]/norms[k])
        w_multiplier = chi[k]/real(norms[k])
        for r, coefficient in enumerate(polys_mp[k]):
            V[r] += v_multiplier*coefficient
            projection[r] += w_multiplier*coefficient
    V0 = V[0]
    W0 = 1-projection[0]
    V0_identity = -2*real(endpoints[n])*polys_mp[n+1][0]/real(norms[n])
    W0_identity = (chi[n]*polys_mp[n+1][0]-chi[n+1]*polys_mp[n][0])/real(norms[n])
    for actual, expected in [(V0,V0_identity),(W0,W0_identity)]:
        error = abs(actual-expected)/max(mp.mpf(1),abs(expected))
        maximum_identity_error = max(maximum_identity_error,error)
        assert error < mp.mpf('1e-170')
    assert V0 != 0 and W0 != 0

    # Return n! times the factorial functional, avoiding tiny factorial scales.
    def polynomial_functional(coefficients,j):
        weight = mp.factorial(n)/mp.factorial(n+1-j)
        total = mp.mpf(0)
        for r, coefficient in enumerate(coefficients):
            total += coefficient*weight
            weight /= n+r+2-j
        return total

    def geometric_functional(j):
        term = mp.factorial(n)/mp.factorial(n+1-j)
        total = term
        r = 0
        while True:
            term /= n+r+2-j
            total += term
            r += 1
            if abs(term) < mp.eps*abs(total):
                return total
            assert r < 2000

    for b in range(1,max_b+1):
        high_rows = [[polynomial_functional(polys_mp[n+l],j)/polys_mp[n+l][0] for j in range(b+1)] for l in range(1,b)]
        v = [polynomial_functional(V,j)/V0 for j in range(b+1)]
        w = [(geometric_functional(j)-polynomial_functional(projection,j))/W0 for j in range(b+1)]
        denominator = mp.det(mp.matrix(high_rows+[[mp.mpf(1)]*(b+1),v]))
        numerator = mp.det(mp.matrix(high_rows+[v,w]))
        assert denominator != 0
        scaled_cofactor = n**(2*b+1)*numerator/denominator
        predicted = (-1)**b*mp.factorial(b)*mp.power(2,mp.mpf(1-b)/2)*mp.exp(-c)
        S = b*(b-1)//2
        EV = (-c)**S*(-1)**(b-1)/A**(b-1)
        EN = (-c)**(b*(b+1)//2)*(1+s)/(2**b*A**b)
        denominator_constant = (-1)**(b+1)*mp.exp(-c*b)*mp.fprod([mp.factorial(j) for j in range(b)])*EV
        numerator_constant = mp.exp(-c*(b+1))*mp.fprod([mp.factorial(j) for j in range(b+1)])*EN
        results.append({'n':n,'b':b,'scaled_cofactor':mp.nstr(scaled_cofactor,18),'predicted_limit':mp.nstr(predicted,18),'cofactor_ratio':mp.nstr(scaled_cofactor/predicted,14),'numerator_asymptotic_ratio':mp.nstr(numerator*n**((b+1)*(b+2)//2)/numerator_constant,14),'denominator_asymptotic_ratio':mp.nstr(denominator*n**S/denominator_constant,14)})

print({'precision_decimal_digits':mp.mp.dps,'maximum_endpoint_identity_relative_error':mp.nstr(maximum_identity_error,8),'results':results,'scope':'Bounded author numerical check; no independent approval or arithmetic denominator conclusion.'})