import sympy as s
# Universal scalar checks; no source scripts and no filesystem writes.
a,b,wp,wu,TP,TU,G=s.symbols('a b wp wu TP TU G')
a0,a1,a2,r1,r2=s.symbols('a0 a1 a2 r1 r2')
av=s.Matrix([[a0,a1,a2]])
e=s.Matrix([[1,1,1]])
tu=s.Matrix([[TU,TU-a1,TU-a1-a2]])
tp=s.Matrix([[TP,TP-r1,TP-r1-r2]])
t=(a*tu-b*tp)/G
x=(wp*tu-wu*tp)/G
S=a1*a1-a0*a2
C=(a1-a0)*r2-(a2-a1)*r1
W=a1*r2-a2*r1
def det3(u,v,w): return u.col_join(v).col_join(w).det()
def wronskian_zero(expr):
    num=s.together(expr).as_numer_denom()[0]
    return s.rem(s.Poly(s.expand(num),wu,wp,a,b,G,a0,a1,a2,r1,r2,TP,TU),s.Poly(a*wu-b*wp-G,wu,wp,a,b,G,a0,a1,a2,r1,r2,TP,TU)).as_expr()==0
checks={}
checks['Y_determinant']=s.factor(det3(av,e+t,e)-(b*C-a*S)/G)==0
checks['X_determinant']=wronskian_zero(det3(av,e+t,x)-((wp+TP)*S-(wu+TU)*C-a0*W)/G)
k,f,eta,SS,CC,WW,PS,US=s.symbols('k f eta SS CC WW PS US')
D=k*b*CC-2*a*SS
N=2*PS*SS-k*US*CC-2*f*eta*WW
V=b*PS-a*US
checks['b_chart']=s.expand(b*N+US*D-(2*V*SS-2*b*f*eta*WW))==0
checks['a_chart']=s.expand(a*N+PS*D-(k*V*CC-2*a*f*eta*WW))==0
g=2*f/k
checks['Y_scaling']=s.factor((b*g*f*CC-a*g*g*SS)/G-g*f*D/(G*k))==0
checks['X_scaling']=s.factor((PS*g*g*SS-US*g*f*CC-g*eta*g*f*WW)/G-g*f*N/(G*k))==0
print(checks)
assert all(checks.values())