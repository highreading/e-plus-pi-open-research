import sys, json, time
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
w,n,m=s.symbols('w n m'); K=s.QQ.frac_field(n,m); V=w*w-w+s.Rational(1,2);A=(2*w*w-1)**2

def elt(x): return K.from_sympy(x)
def red(expr):
    p=s.Poly(s.expand(expr),w); a=[elt(p.nth(j)) for j in range(p.degree()+1)]
    for j in range(len(a)-1,3,-1):
        if not a[j]:continue
        k=j-4; c=a[j]/elt(2*k+8*m+2*n+8)
        for l,z in [(4,2*k+8*m+2*n+8),(3,-2*k-8*m-6),(2,4*m-2*n),(1,k+1),(0,(n-k)/2)]:a[k+l]-=c*elt(z)
    return (a+[K.zero]*4)[:4]
def det(a):
    # Bare field elimination.
    a=[list(r) for r in a]; out=K.one
    for j in range(len(a)):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None:return K.zero
        if r!=j:a[r],a[j]=a[j],a[r];out=-out
        pivot=a[j][j];out*=pivot
        for r in range(j+1,len(a)):
            c=a[r][j]/pivot
            for l in range(j+1,len(a)):a[r][l]-=c*a[j][l]
    return out
cols=[]
for j in range(5):
    print('reducing',j,flush=True);cols.append(red(A**j))
co=[]
for j in range(5):
    print('minor',j,flush=True)
    c=det([[cols[h][r] for h in range(5) if h!=j] for r in range(4)])*(-1)**j
    co.append(c)
    print('factor numerator',s.factor(K.to_sympy(c).as_numer_denom()[0]),flush=True)
    print('factor denominator',s.factor(K.to_sympy(c).as_numer_denom()[1]),flush=True)
Path(__file__).with_name('moment_recurrence_coefficients.json').write_text(json.dumps({'coefficients':[str(K.to_sympy(c)) for c in co]},indent=2))
print('saved',flush=True)
