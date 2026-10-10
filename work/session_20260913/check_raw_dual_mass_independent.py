"""Independent exact controls for raw dual mass; no archived certificate replay."""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json

def add(a,b):
    return [(a[k] if k<len(a) else Q())+(b[k] if k<len(b) else Q()) for k in range(max(len(a),len(b)))]
def scale(a,c):return [x*c for x in a]
def qpolys(top):
    out=[[Q(1)],[Q(),Q(1)]]
    for k in range(1,top):out.append(add([Q()]+out[-1],scale(out[-2],Q(k*k,4*k*k-1))))
    return out
def borel(a):return [c/factorial(k) for k,c in enumerate(a)]
def integral_product(a,b):return sum((x*y/Q(j+k+1) for j,x in enumerate(a) for k,y in enumerate(b)),Q())
def solve(aa,bb):
    v=[list(row)+[rhs] for row,rhs in zip(aa,bb)];n=len(bb)
    for j in range(n):
        pivot=next(k for k in range(j,n) if v[k][j])
        v[j],v[pivot]=v[pivot],v[j]
        q=v[j][j];v[j]=[x/q for x in v[j]]
        for k in range(n):
            if k!=j:
                q=v[k][j];v[k]=[x-q*y for x,y in zip(v[k],v[j])]
    return [row[-1] for row in v]

rows=[]
for n in (4,5):
    qs=qpolys(2*n-1)
    # Derive all factorial high rows and kernel normalization from coefficients.
    def ellrow(q):return [sum((c/Q(factorial(n+d+1-j)) for d,c in enumerate(q)),Q()) for j in range(n+1)]
    kernel=[Q()]*(n+1)
    for k in range(n+1):
        hk=Q((-1)**k*4**k,(2*k+1)*comb(2*k,k)**2)
        kernel=add(kernel,scale(qs[k],sum(qs[k],Q())/hk))
    matrix=[ellrow(qs[k]) for k in range(n+1,2*n)]
    matrix += [ellrow(kernel),[Q(1)]*(n+1)]
    bb=solve(matrix,[Q()]*(n-1)+[Q(-4),Q(1)])
    pp=[Q()]*(n+1)
    for j,b in enumerate(bb):
        pp=add(pp,[b*Q((-1)**d*comb(n-j,d),factorial(n-j)) for d in range(n-j+1)])
    assert sum(bb)==1
    assert all(integral_product(pp,borel(qs[k]))==0 for k in range(n+1,2*n))
    assert integral_product(pp,borel(kernel))==-4
    degree_controls=[]
    for sigma in (0,1):
        hs=[k for k in range(n+1,2*n) if k%2==sigma];m=len(hs);start=2*m+sigma
        for k in range(sigma,n+1,2):
            lam=k*(k+1);weights=[]
            for j,h in enumerate(hs):
                w=Q(1)
                for a,hh in enumerate(hs):
                    if a!=j:w*=Q(lam-hh*(hh+1),h*(h+1)-hh*(hh+1))
                weights.append(w)
            interp=[Q()]
            for w,h in zip(weights,hs):interp=add(interp,scale(borel(qs[h]),w/qs[h][sigma]))
            error=add(scale(borel(qs[k]),1/qs[k][sigma]),scale(interp,-1))
            assert all(v==0 for v in error[:start])
        degree_controls.append({'sigma':sigma,'nodes':hs,'first_possible_error_degree':start})
    rows.append({'n':n,'B_endpoint':1,'kernel_integral':-4,'all_high_rows_vanish':True,'parity_interpolation':degree_controls,'B_coefficients':[str(x) for x in bb]})

out={'status':'PASS; independent fixed exact controls n4,n5','checks':rows}
Path(__file__).with_name('raw_dual_mass_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
