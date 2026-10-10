import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
m,n,x=s.symbols('m n x');K=s.QQ.frac_field(m)
data=json.loads(Path(__file__).with_name('moment_recurrence_coefficients.json').read_text())
ce=[s.sympify(z) for z in data['coefficients']]
def elt(x):return K.from_sympy(s.cancel(x))
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
N=int(sys.argv[1]);d=N+1;r=N//2
poly=s.Poly((1+2*x+2*x*x)**N,x)
U=s.expand(sum((-2)**j*s.prod(2*m-h for h in range(j))/s.factorial(j)*poly.nth(N-2*j) for j in range(r+1)))
print('U',U,flush=True)
rows=[[K.one if j==h else K.zero for h in range(4)] for j in range(4)]
cn=[s.cancel(z.subs(n,N)) for z in ce]
for j in range(4,d+3):
    print('state row',j,flush=True)
    ratio=[elt(-cn[l].subs(m,m+j-4)/cn[4].subs(m,m+j-4)) for l in range(4)]
    rows.append([sum((ratio[l]*rows[j-4+l][h] for l in range(4)),K.zero) for h in range(4)])
out=[]
for h in range(3):
    print('output row',h,flush=True)
    wt=[elt((-1)**(d-j)*s.binomial(d,j)*U.subs(m,m+h+j)) for j in range(d+1)]
    out.append([sum((wt[j]*rows[h+j][z] for j in range(d+1)),K.zero) for z in range(4)])
print('minor',flush=True)
q=det3([[out[h][z] for z in range(1,4)] for h in range(3)])/elt(U)
num,den=K.to_sympy(q).as_numer_denom()
print('tau numerator',s.factor(num),flush=True)
print('tau denominator',s.factor(den),flush=True)
Path(__file__).with_name('weighted_observability_n'+str(N)+'.json').write_text(json.dumps({'n':N,'U':str(U),'tau':str(K.to_sympy(q))},indent=2))
print('saved',flush=True)
