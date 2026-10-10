import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
m,w,x=s.symbols('m w x'); K=s.QQ.frac_field(m)
def elt(z): return K.from_sympy(s.cancel(z))
def poch(a,h):
    return s.prod(a+j for j in range(h)) if h>=0 else 1/s.prod(a-j for j in range(1,-h+1))
N=int(sys.argv[1]);r=N//2;d=N+1
b=s.Poly((w*w-w+s.Rational(1,2))**N,w)
H=sum((elt(b.nth(2*k+1)*s.Integer(2)**(r-k)*poch(s.Rational(1,2),k-r)/poch(2*m+s.Rational(3,2),k-r)) for k in range(N)),K.zero)
print('H numerator',s.factor(K.to_sympy(H).as_numer_denom()[0]),flush=True)
print('H denominator',s.factor(K.to_sympy(H).as_numer_denom()[1]),flush=True)
a=s.Poly((1+2*x+2*x*x)**N,x)
U=s.expand(sum((-2)**j*s.prod(2*m-h for h in range(j))/s.factorial(j)*a.nth(N-2*j) for j in range(r+1)))
F=K.zero
for j in range(d+1):
    print('shift',j,flush=True)
    cj=elt(poch(2*m+1,2*j)/poch(2*m+s.Rational(3,2),2*j))
    F+=elt((-1)**(d-j)*s.binomial(d,j)*U.subs(m,m+j))*elt(K.to_sympy(H).subs(m,m+j))*cj
print('F numerator',s.factor(K.to_sympy(F).as_numer_denom()[0]),flush=True)
print('F denominator',s.factor(K.to_sympy(F).as_numer_denom()[1]),flush=True)
Path(__file__).with_name(f'beta_period_coordinate_n{N}.json').write_text(json.dumps({'n':N,'H':str(K.to_sympy(H)),'F':str(K.to_sympy(F))},indent=2))
print('saved',flush=True)
