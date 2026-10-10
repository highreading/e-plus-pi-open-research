"""Independent fixed symbolic mod-eight calculation; no degree samples."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
n,u=s.symbols('n u')
uu,v,w,x=s.symbols('uu v w x')
beta=lambda k:k*k/(4*k*k-1)
sig=lambda k:k*(k-1)/(2*(2*k-1))
inv4=lambda k:k*(k-1)*(k-2)*(k-3)/(8*(2*k-5)*(2*k-3))
M1=[s.cancel((-1)**i*s.prod(2*n+j for j in range(i+1))
             *s.prod(n+1-j for j in range(i+1))/s.factorial(i+1)) for i in range(4)]
M2=[s.cancel(M1[i]*(2*n-1)*(n+2)*s.Rational(i+1,i+2)) for i in range(4)]
c,d=beta(n-2),beta(n)
mom=[c*v-sig(n-1)*x,-c*d*uu+sig(n)*c*w,
     -sig(n+1)*c*v+inv4(n+1)*x,
     sig(n+2)*c*d*uu-inv4(n+2)*c*w]
equations=[s.expand((c*w+sum(M1[i]*mom[i] for i in range(4)))/c),
           s.expand(x-sum(M2[i]*mom[i] for i in range(4)))]
Z=s.Matrix([[s.cancel(s.diff(eq,var)) for var in (w,x)] for eq in equations])
rhs=s.Matrix([-s.cancel(eq.subs({w:0,x:0,uu:1,v:-1})) for eq in equations])

def pmod(expr):
    p=s.Poly(s.expand(expr),u)
    return s.Poly.from_dict({mon:int(coef)%8 for mon,coef in p.terms()},u).as_expr()

def rational_mod8(expr):
    num,den=s.fraction(s.cancel(expr.subs(n,4*u+1)))
    num,den=pmod(num),pmod(den)
    const=int(den.subs(u,0))
    assert const%2
    tail=s.expand(den-const)
    assert all(int(v)%2==0 for v in s.Poly(tail,u).all_coeffs())
    inv=pow(const,-1,8)
    deninv=pmod(inv*(1-inv*tail+(inv*tail)**2))
    assert pmod(den*deninv)==1
    return pmod(num*deninv)

Z8=Z.applyfunc(rational_mod8)
R8=rhs.applyfunc(rational_mod8)
assert Z8==s.diag(1+4*u,1+4*u)
assert R8==s.Matrix([2+4*u,2+4*u])
solution=R8.applyfunc(lambda f:pmod((1+4*u)*f))
assert solution==s.Matrix([2+4*u,2+4*u])
residue=pmod(-solution[0]-5*solution[1])
assert residue==4
out={'status':'passed','scope':'one symbolic residue variable; no canonical degree samples',
     'matrix_mod8':[list(map(str,Z8.row(i))) for i in range(2)],
     'rhs_mod8':list(map(str,R8)),
     'w_x_mod8':list(map(str,solution)),
     'Xi_normalized_mod8':int(residue)}
(HERE/'Xi_remaining_class_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
