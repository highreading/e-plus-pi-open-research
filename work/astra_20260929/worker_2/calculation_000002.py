import sys
sys.path.insert(0, '[private local path removed]')
import sympy as S
n,h,u,v,z,t=S.symbols('n h u v z t')
def T(k):
    return S.Matrix([[-k,k,S.Rational(1,2)],[k+1,-k-1,(k+1)/2],[k*(k+1),k+1,-(k+1)*(k+2)/2]])
def jet_rows(k):
    return S.Matrix([[1,0,0],[k,1,0],[k*(k-1),2*k,1],[k*(k-1)*(k-2)+2*k,3*k*(k-1),2*k]])
state=S.Matrix([h,u,v])
rows=[jet_rows(n)[0:2,:],jet_rows(n+1)[1:3,:]*T(n),jet_rows(n+2)[2:4,:]*T(n+1)*T(n)]
M=S.Matrix([(r*state).T.tolist()[0] for r in rows])
D=2*(n+1)*h*h-2*h*u-(n-1)*u*u-u*v
E=-2*n*(n+2)*h*h+4*n*h*u+(n+2)*h*v+(n*n-2*n-1)*u*u+n*u*v
C=u**3+(n-2)*h*u*u+4*h*h*u-2*(n+2)*h**3
P=t**3-2*(n+1)*t*t+(n+2)**2*t-2*(n+1)*(n+2)
first=S.Matrix.vstack(*[r[0,:] for r in rows]); second=S.Matrix.vstack(*[r[1,:] for r in rows])
checks={}
def check(name,expr):
    residue=S.factor(expr)
    checks[name]=str(residue)
    assert residue==0,(name,residue)
check('transition determinant',T(n).det()-(n+1)**4/2)
check('minor 01',M.extract([0,1],[0,1]).det()-(n+1)*D)
check('minor 02',M.extract([0,2],[0,1]).det()-(n+2)*(2*n+3)*E)
check('boundary minor 12',M.extract([1,2],[0,1]).det().subs({h:0,u:0})-(n+1)*(n+2)**2*(2*n+3)*v*v)
check('homogeneous elimination',u*E+(n*u+(n+2)*h)*D+(n+1)*C)
check('first column determinant',first.det()+(n+1)**2*(n+2)*(2*n+3))
check('pencil determinant',(second-t*first).det()-(n+1)**2*(n+2)*(2*n+3)*P)
check('cubic shift',h**3*P.subs(t,n+u/h)-C)
check('discriminant',S.discriminant(P,t)-4*(n+2)*(2*n**3-12*n*n-35*n-22))
w=2*(n+1)/z-2-(n-1)*z
shift=T(n)*S.Matrix([1,z,w])
expected=S.Matrix([(n+1)*(z*z-2*z+2)/(2*z),-(n+1)**2*(z*z-2)/(2*z),(n+1)**2*(n*z*z-2*n+4*z-4)/(2*z)])
for i in range(3):check('transport '+str(i),shift[i]-expected[i])
f=z**3+(n-2)*z*z+4*z-2*(n+2)
g=(n*n+4*n+2)*z*z-(6*n+4)*z-2*n*n
check('next D',D.subs({n:n+1,h:shift[0],u:shift[1],v:shift[2]}, simultaneous=True)-(n+1)**2*(((2*n+3)*z-n-2)*f-g)/(2*z*z))
A=-(3*n**3+14*n*n+14*n+4)*z-4*n**3+8*n+4
B=(3*n+2)*z*z+(3*n*n-2)*z+4*n*n+12*n+8
check('integral Bezout',A*f+B*g+8*(n+1)**2*(n+2))
check('resultant',S.resultant(f,g,z)+32*(n+1)**4*(n+2)**2)
print(checks)
print('All expressions vanish identically; no files written. Polynomial identities do not certify the endpoint primitivity dependency.')