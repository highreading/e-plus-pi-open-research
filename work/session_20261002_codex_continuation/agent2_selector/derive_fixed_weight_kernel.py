import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
w,x=s.symbols('w x');N=int(sys.argv[1]);r=N//2;d=N+1
V=w*w-w+s.Rational(1,2);t=1-2*w*w
a=s.Poly((1+2*x+2*x*x)**N,x)
h=V**N/(4*w**(N+2));K=0
for ell in range(r+1):
    print('derivative',ell,flush=True)
    z=t**ell*h
    for k in range(ell): z=s.cancel(-s.diff(z,w)/(4*w))
    K+=2**ell*a.nth(N-2*ell)/s.factorial(ell)*z
P=s.cancel(-4*w*(1-t*t)**d*K)
num,den=P.as_numer_denom()
print('denominator',den,flush=True)
print('kernel',s.factor(P),flush=True)
Path(__file__).with_name(f'fixed_weight_kernel_n{N}.json').write_text(json.dumps({'n':N,'P':str(s.expand(P)),'factorization':str(s.factor(P))},indent=2))
print('saved',flush=True)
