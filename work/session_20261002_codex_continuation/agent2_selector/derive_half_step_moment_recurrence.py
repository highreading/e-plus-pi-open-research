import sys, json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
w,n,h=s.symbols('w n h'); K=s.QQ.frac_field(n,h); z=1-2*w*w
def elt(x): return K.from_sympy(x)
def red(expr):
    p=s.Poly(s.expand(expr),w); a=[elt(p.nth(j)) for j in range(p.degree()+1)]
    for j in range(len(a)-1,3,-1):
        if not a[j]: continue
        k=j-4; c=a[j]/elt(2*k+4*h+2*n+8)
        for l,v in [(4,2*k+4*h+2*n+8),(3,-2*k-4*h-6),(2,2*h-2*n),(1,k+1),(0,(n-k)/2)]:
            a[k+l]-=c*elt(v)
    return (a+[K.zero]*4)[:4]
def det(a):
    a=[list(r) for r in a]; out=K.one
    for j in range(len(a)):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None: return K.zero
        if r!=j: a[r],a[j]=a[j],a[r]; out=-out
        pivot=a[j][j]; out*=pivot
        for r in range(j+1,len(a)):
            c=a[r][j]/pivot
            for l in range(j+1,len(a)): a[r][l]-=c*a[j][l]
    return out
cols=[red(z**j) for j in range(5)]
coeff=[]
for j in range(5):
    c=det([[cols[k][r] for k in range(5) if k!=j] for r in range(4)])*(-1)**j
    v=K.to_sympy(c); coeff.append(v)
    print('coefficient',j,s.factor(v),flush=True)
Path(__file__).with_name('half_step_moment_recurrence.json').write_text(json.dumps({'coefficients':[str(v) for v in coeff]},indent=2))
