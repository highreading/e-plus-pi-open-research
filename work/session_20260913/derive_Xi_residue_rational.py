"""Symbolic fixed-size Xi residue calculation; no degree samples."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
n=s.symbols('n')
def beta(j):return j*j/(4*j*j-1)
def sig(j):return j*(j-1)/(2*(2*j-1))
def chi(j):return j*(j-1)*(j-2)*(j-3)/(8*(2*j-5)*(2*j-3))
def falling(z,k):return s.prod(z-j for j in range(k))
M1=[s.cancel((-1)**i*s.prod(2*n+j for j in range(i+1))*falling(n+1,i+1)/s.factorial(i+1)) for i in range(4)]
M2=[s.cancel(M1[i]*(2*n-1)*(n+2)*s.Rational(i+1,i+2)) for i in range(4)]
c,d=beta(n-2),beta(n)
sm,s0,sp,spp=map(sig,(n-1,n,n+1,n+2))
kp,kpp=chi(n+1),chi(n+2)
ww=s.cancel(1+M1[1]*s0-M1[3]*kpp)
wx=s.cancel((-M1[0]*sm+M1[2]*kp)/c)
xw=s.cancel(c*(-M2[1]*s0+M2[3]*kpp))
xx=s.cancel(1+M2[0]*sm-M2[2]*kp)
rw=s.cancel(M1[0]+M1[1]*d-M1[2]*sp-M1[3]*spp*d)
rx=s.cancel(c*(-M2[0]-M2[1]*d+M2[2]*sp+M2[3]*spp*d))
det=s.factor(ww*xx-wx*xw)
w=s.cancel((rw*xx-wx*rx)/det)
x=s.cancel((ww*rx-rw*xw)/det)
F=s.factor((2*n-1)-n*n/(2*n-1)-(2*n-5)*x-n*n/(2*n-1)*w)
out={'scope':'one symbolic rational variable; no degree sampling','M1':list(map(str,M1)),'M2':list(map(str,M2)),
     'matrix':list(map(str,(ww,wx,xw,xx))),'rhs':list(map(str,(rw,rx))),
     'determinant_factored':str(det),'w_factored':str(s.factor(w)),'x_factored':str(s.factor(x)),
     'F_factored':str(F)}
Path(__file__).with_name('Xi_residue_rational_symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
