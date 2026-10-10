from fractions import Fraction as F
from math import factorial, gcd, lcm
import json

n = 12

def vp(x, p=3):
    x = F(x)
    if not x:
        return None
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v

def content(poly):
    return min(vp(x) for x in poly if x)

def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def power(a, m):
    out = [F(1)]
    for _ in range(m):
        out = mul(out, a)
    return out

def legendre(m):
    u = power([F(1), F(-2), F(2)], m)
    return [u[m+d] * factorial(m+d) / (factorial(m)*factorial(d)) for d in range(m+1)]

P, U = legendre(n), legendre(n+1)
a, b = sum(P), sum(U)
G = F((-1)**n * 2**(2*n+3), n+1)
E = [F(1)]
for k in range(1, 2*n+3):
    E.append(E[-1] + F(1, factorial(k)))

def ell(poly, j):
    return sum((x / factorial(n+d+1-j) for d, x in enumerate(poly)), F(0))

def contraction(poly, j):
    return sum((x * E[n+d-j] for d, x in enumerate(poly)), F(0))

alpha = [ell(U,j) for j in range(3)]
second = [1 + (a*contraction(U,j)-b*contraction(P,j))/G for j in range(3)]
beta = [alpha[1]*second[2]-alpha[2]*second[1],
        alpha[2]*second[0]-alpha[0]*second[2],
        alpha[0]*second[1]-alpha[1]*second[0]]

# Exact moments from Gaussian integer powers of 1+i.
mu = []
re, im = 1, 0
for j in range(2*n+2):
    re, im = re-im, re+im
    mu.append(F(2*im, 2**j*(j+1)))

# Reconstruct Q directly from the moment equations.
aug = []
for k in range(n+1):
    rhs = -sum((beta[j]/factorial(n+k+1-j) for j in range(3)), F(0))
    aug.append([mu[k+d] for d in range(n+1)] + [rhs])
for col in range(n+1):
    pivot = next(row for row in range(col,n+1) if aug[row][col])
    aug[col], aug[pivot] = aug[pivot], aug[col]
    pivot_value = aug[col][col]
    aug[col] = [x/pivot_value for x in aug[col]]
    for row in range(n+1):
        if row != col and aug[row][col]:
            factor = aug[row][col]
            aug[row] = [x-factor*y for x,y in zip(aug[row],aug[col])]
Q = [aug[d][-1] for d in range(n+1)]
Craw = Q[::-1]

def remainder_coefficient(k):
    be = sum((beta[j]/factorial(k-j) for j in range(min(2,k)+1)), F(0))
    cf = sum((Craw[d]*mu[k-d-1] for d in range(min(n,k-1)+1)), F(0)) if k else F(0)
    return be+cf

Araw = [-remainder_coefficient(k) for k in range(n+1)]
assert all(remainder_coefficient(k) == 0 for k in range(n+1,2*n+3))
assert sum(beta) == sum(Craw)

# Original H-polynomials supply endpoint contractions and auxiliary minors.
def h_derivatives(m):
    u = power([F(1),F(-1),F(1,2)],m)
    h = [F(factorial(m),factorial(d))*u[m-d] for d in range(m+1)]
    return [sum((h[d]*factorial(d)//factorial(d-j) if h[d].denominator == 1 else h[d]*F(factorial(d),factorial(d-j)) for d in range(j,m+1)), F(0)) for j in range(4)]

def state(m):
    h, hp, hpp, hppp = h_derivatives(m)
    J = m*h+hp
    K = m*(m-1)*h+2*m*hp+hpp
    M = m*(m-1)*(m-2)*h+3*m*(m-1)*hp+3*m*hpp+hppp
    return h,J,K,M

hn,Jn,_,_ = state(n)
eta,Jnext,Knext,_ = state(n+1)
_,_,Klast,Mlast = state(n+2)
S = Jnext**2-eta*Knext
Cscalar = (Jnext-eta)*Jn-(Knext-Jnext)*hn
W = Jnext*Jn-Knext*hn
f = F(2**n,factorial(n)**2)
kappa = (n+1)**2

def endpoint_moment(poly):
    divided = [sum(poly[d+1:]) for d in range(len(poly)-1)]
    return sum((x*mu[d] for d,x in enumerate(divided)),F(0))

Pstar = endpoint_moment(P)+contraction(P,0)
Ustar = endpoint_moment(U)+contraction(U,0)
D = kappa*b*Cscalar-2*a*S
X = 2*Pstar*S-kappa*Ustar*Cscalar-2*f*eta*W
scale = F((-1)**n,4*(n+1)**3*factorial(n)**4)
assert sum(Araw) == scale*X
assert sum(beta) == scale*D
assert vp(D) == 0 and vp(X/f) == 0
assert ((X/f).numerator * pow((X/f).denominator,-1,3)) % 3 == 2

matrix = [(hn,Jn),(Jnext,Knext),(Klast,Mlast)]
minors = [matrix[i][0]*matrix[j][1]-matrix[i][1]*matrix[j][0] for i,j in [(0,1),(0,2),(1,2)]]
assert all(x.denominator == 1 for x in minors)
omega = 0
for x in minors:
    omega = gcd(omega,abs(x.numerator))

polys = {'A_raw':Araw,'B_raw':beta,'C_raw':Craw}
all_coefficients = Araw+beta+Craw
nu = min(content(poly) for poly in polys.values())
den = 1
for x in all_coefficients:
    den = lcm(den,x.denominator)
integer_content = 0
for x in all_coefficients:
    integer_content = gcd(integer_content,abs((x*den).numerator))
primitive_scale = F(den,integer_content)
Aend = primitive_scale*sum(Araw)
Bend = primitive_scale*sum(beta)
assert Aend.denominator == Bend.denominator == 1
endpoint_gcd = gcd(abs(Aend.numerator),abs(Bend.numerator))
ratio = sum(Araw)/sum(beta)
witnesses = [{'polynomial':name,'degree':d,'coefficient':str(x)} for name,poly in polys.items() for d,x in enumerate(poly) if x and vp(x)==nu]
assert nu == -31
assert vp(Aend) == 1 and vp(Bend) == 11
assert vp(endpoint_gcd) == 1 and vp(ratio.denominator) == 10
assert vp(omega) == 0

print(json.dumps({'status':'UNVERIFIED author exact computation',
 'n':n,'r':vp(factorial(n)),
 'coefficient_valuations':{name:[vp(x) for x in poly] for name,poly in polys.items()},
 'coefficient_contents':{name:content(poly) for name,poly in polys.items()},
 'nu':nu,'minimum_witnesses':witnesses,
 'raw_endpoint_valuations':{'A':vp(sum(Araw)),'B':vp(sum(beta))},
 'primitive_scale':str(primitive_scale),
 'primitive_A_endpoint':str(Aend),'primitive_B_endpoint':str(Bend),
 'primitive_endpoint_gcd':str(endpoint_gcd),'primitive_endpoint_gcd_v3':vp(endpoint_gcd),
 'reduced_denominator':str(ratio.denominator),'reduced_denominator_v3':vp(ratio.denominator),
 'auxiliary_omega':str(omega),'auxiliary_omega_v3':vp(omega),
 'order_conditions_checked_through':2*n+2,
 'endpoint_scaling_checks':True},indent=2))