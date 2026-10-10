import sys
sys.path.insert(0, '[private local path removed]')
import sympy as s
a,b,wp,wu,TP,TU,G=s.symbols('a b wp wu TP TU G')
a0,a1,a2,r1,r2=s.symbols('a0 a1 a2 r1 r2')
av=s.Matrix([[a0,a1,a2]])
e=s.Matrix([[1,1,1]])
tu=s.Matrix([[TU,TU-a1,TU-a1-a2]])
tp=s.Matrix([[TP,TP-r1,TP-r1-r2]])
t=(a*tu-b*tp)/G
x=(wp*tu-wu*tp)/G
S=a1**2-a0*a2
C=(a1-a0)*r2-(a2-a1)*r1
W=a1*r2-a2*r1
def det3(u,v,w):
    return u.col_join(v).col_join(w).det()
def zero(expr):
    return s.cancel(expr)==0
checks={}
checks['Y_reconstruction']=zero(det3(av,e+t,e)-(b*C-a*S)/G)
residual=det3(av,e+t,x)-((wp+TP)*S-(wu+TU)*C-a0*W)/G
checks['X_reconstruction_with_Wronskian']=zero(residual.subs(wu,(G+b*wp)/a))
k,f,eta,SS,CC,WW,PS,US=s.symbols('k f eta SS CC WW PS US')
D=k*b*CC-2*a*SS
N=2*PS*SS-k*US*CC-2*f*eta*WW
V=b*PS-a*US
checks['b_chart']=zero(b*N+US*D-(2*V*SS-2*b*f*eta*WW))
checks['a_chart']=zero(a*N+PS*D-(k*V*CC-2*a*f*eta*WW))
g=2*f/k
checks['Y_scaling']=zero((b*g*f*CC-a*g*g*SS)/G-g*f*D/(G*k))
checks['X_scaling']=zero((PS*g*g*SS-US*g*f*CC-g*eta*g*f*WW)/G-g*f*N/(G*k))
print(checks)
assert all(checks.values())