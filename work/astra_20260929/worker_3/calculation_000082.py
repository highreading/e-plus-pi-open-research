from fractions import Fraction as F
from math import factorial as fac, comb
import json

# Author validation of the registered identification; not independent approval.
def legendre_L(m):
    out = [F(0) for _ in range(m + 1)]
    for j in range(m // 2 + 1):
        r = m - 2*j
        c = F(fac(2*m - 2*j), fac(j)*fac(m-j)*fac(r))
        for k in range(r + 1):
            out[k] += c*comb(r,k)*2**k*(-1)**(r-k)
    return out

def ell(poly, n, j):
    return sum((c/F(fac(n+r+1-j)) for r,c in enumerate(poly)), F(0))

def cross(x,y):
    return [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]

def h_jet(m):
    # Direct coefficient extraction from m![s^m] exp(xs)(1-s+s^2/2)^m.
    out = [F(0), F(0), F(0)]
    for c in range(m//2 + 1):
        for b in range(m-2*c + 1):
            r = m-b-2*c
            coeff = F(fac(m)**2*(-1)**b, fac(m-b-c)*fac(b)*fac(c)*2**c*fac(r))
            out[0] += coeff
            out[1] += r*coeff
            out[2] += r*(r-1)*coeff
    return out

indices = [2,3,4,5,6,7,8,9,12,16,20]
polys = [legendre_L(m) for m in range(max(indices)+2)]
checks = 0
rows = []
for n in indices:
    P,U = polys[n],polys[n+1]
    a,b = sum(P),sum(U)
    k = (n+1)**2
    G = F((-1)**n*2**(2*n+3), n+1)
    d = 2**(n+1)*comb(2*n+2,n+1)
    assert U[-1] == d
    checks += 1

    # Sum the kernel directly in the orthogonal basis, independently of CD.
    V = [F(0) for _ in range(n+1)]
    for m in range(n+1):
        norm = F((-1)**m*2**(2*m+1),2*m+1)
        endpoint = sum(polys[m])
        for r,c in enumerate(polys[m]):
            V[r] += c*endpoint/norm
    left = [F(0) for _ in range(n+2)]
    for r,c in enumerate(V):
        left[r] += G*c
        left[r+1] -= G*c
    right = [b*(P[r] if r<len(P) else 0)-a*U[r] for r in range(n+2)]
    assert left == right
    checks += 1

    E = [F(1)]
    for s in range(1,2*n+2):
        E.append(E[-1]+F(1,fac(s)))
    def T(poly,j):
        return sum((c*E[n+r-j] for r,c in enumerate(poly)),F(0))
    t = [(a*T(U,j)-b*T(P,j))/G for j in range(3)]
    v = [ell(V,n,j) for j in range(3)]
    assert t == v
    checks += 3

    raw_row = [ell(U,n,j) for j in range(3)]
    monic = [c/d for c in U]
    monic_row = [ell(monic,n,j) for j in range(3)]
    beta = cross(raw_row,[1+x for x in t])
    Bcof = cross(monic_row,[1+x for x in v])
    assert beta == [d*x for x in Bcof]
    checks += 3
    Yraw,Ycof = sum(beta),sum(Bcof)

    h,hp,hpp = h_jet(n)
    hn,hnp,hnpp = h_jet(n+1)
    J = n*h+hp
    Jn = (n+1)*hn+hnp
    Kn = (n+1)*n*hn+2*(n+1)*hnp+hnpp
    f = F(2**n,fac(n)**2)
    g = F(2**(n+1),fac(n+1)**2)
    assert [ell(P,n,1),ell(P,n,2)] == [f*h,f*J]
    assert raw_row == [g*hn,g*Jn,g*Kn]
    checks += 5

    S = Jn**2-hn*Kn
    C = (Jn-hn)*J-(Kn-Jn)*h
    D = k*b*C-2*a*S
    alpha = F((-1)**n,4*(n+1)**3*fac(n)**4)
    assert Yraw == alpha*D
    assert Ycof == alpha*D/d
    assert g*f/(G*k) == alpha
    checks += 3
    rows.append({'n':n,'D_zero':D==0,'D_sign':(D>0)-(D<0),'Y_cof_sign':(Ycof>0)-(Ycof<0),'scalar_identity':True,'cofactor_vector_identity':True})

print(json.dumps({'status':'passed','scope':'bounded exact author validation only','indices':indices,'scalar_and_component_checks':checks,'rows':rows,'limitations':'No asymptotic conclusion follows from these finite checks; independent review remains required.'},indent=2))