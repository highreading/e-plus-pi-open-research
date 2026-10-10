"""Auxiliary positive equilibrium and formal forcing saddles; no center samples."""
import json
import mpmath as mp

mp.mp.dps = 45
sigma = mp.sqrt(2)
M = 1 + sigma

def geometry(c):
    A2 = M*M*c*(c+2)/(M*M+(c+1)**2)
    C = mp.sqrt((M*M+1)*(M*M+(c+1)**2))/c
    return mp.sqrt(A2), C

def gap(c):
    q = c+1
    Q = mp.sqrt(M*M+q*q)/mp.sqrt(M*M+1)
    return 2/c*(mp.atanh(1/Q)-q*mp.atanh(Q/q))

def bisect(fun, lo, hi, steps=90):
    fl = fun(lo)
    fh = fun(hi)
    if fl*fh >= 0:
        raise ValueError((lo,hi,fl,fh))
    for _ in range(steps):
        mid = (lo+hi)/2
        fm = fun(mid)
        if fl*fm <= 0:
            hi = mid
        else:
            lo, fl = mid, fm
    return (lo+hi)/2

def integrate(c, fn):
    A, C = geometry(c)
    def integrand(theta):
        x = A*mp.sin(theta)
        dens = C/mp.pi*A*A*mp.cos(theta)**2/((1+x*x)*(M*M-x*x))
        unitcos = (1-x*x)/(1+x*x)
        return dens*fn(unitcos)
    return mp.quad(integrand, [-mp.pi/2, 0, mp.pi/2])

def L(c,q):
    return integrate(c, lambda cost: mp.log(1+2*q*cost+q*q)/2)

def J(c,q):
    return integrate(c, lambda cost: (cost+q)/(1+2*q*cost+q*q))

def g(zeta):
    return 1+sigma/2*(zeta+1/zeta)

def h(zeta):
    return sigma/2*(zeta+1/zeta)-1

def force_saddles(c):
    def dp(zeta):
        return sigma/2*(1-1/zeta**2)/g(zeta)+c*J(c,sigma+zeta)
    def dm(zeta):
        return sigma/2*(1-1/zeta**2)/h(zeta)-c*J(c,sigma-zeta)
    zp = bisect(dp, mp.mpf('.05'), mp.mpf(1), 75)
    zm = bisect(dm, mp.mpf(1), sigma, 75)
    pp = mp.log(g(zp))+c*L(c,sigma+zp)
    pm = mp.log(h(zm))+c*L(c,sigma-zm)
    tau = pp-pm
    return {"zeta_plus":str(zp),"zeta_minus":str(zm),
            "formal_tau":str(tau),"stationary_one_tau":str((2+c)*mp.log(M)),
            "tau_difference":str(tau-(2+c)*mp.log(M)),
            "plus_derivative":str(dp(zp)),"minus_derivative":str(dm(zm))}

critical = bisect(gap, mp.mpf('.5'),mp.mpf(1))
rows=[]
for value in ['.01','.05','.1','.25','.5','.7']:
    c=mp.mpf(value)
    A,C=geometry(c)
    row={"c":value,"A":str(A),"mass":str(integrate(c,lambda _:mp.mpf(1))),
         "absolute_equilibrium_gap":str(gap(c)),
         "L_reciprocal_residual":str(L(c,M)-L(c,1/M)-mp.log(M))}
    row.update(force_saddles(c))
    rows.append(row)
result={"status":"formal saddle candidates only; no actual-center or denominator theorem",
        "absolute_equilibrium_critical_c":str(critical),"rows":rows}
print(json.dumps(result,indent=2))
